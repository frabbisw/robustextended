'''
This file includes code to apply transformations on code generation tasks.
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''

# from natgen.transformations import VarRenamerBase
from natgen import VarRenamerBase


def sep_doc(data, prompt, entry_point):
    """ A help function to seperate docstring, a specific function for MBXP and humaneval
    Note that there is another sep function in natgen which is used to seperate 
    the whole documents in prompt including docstring & examples.
    """
    # sep into header, docstring only (without any special charaters like """), examples
    if data in ["humaneval", "mbpp", "humanevalpy", "humanevaljava", "humanevalcpp", "humanevaljs", "humanevalgo", "mbgo"]:
        if data in ["humanevalgo", "mbgo"]:
            start_point = -1
            end_point = -1
            lines = prompt.split("\n")
            for i in range(len(lines)):
                if "//" in lines[i]:
                    if start_point < 0:
                        start_point = i
                if entry_point in lines[i]:
                    end_point = i
                    break
            head = "\n".join(lines[0:start_point])+"\n"
            doc = "\n".join(lines[start_point:end_point])
            doc = doc.replace("// ", "")
            doc = doc.replace("//", "")
            test = "\n"+"\n".join(lines[end_point:])
            return head, doc, test

        elif data in ["humanevalpy", "humaneval", "mbpp"]:
            doc_start_sign = '"""'
            doc_start_sign_alt = '\'\'\''
            start_limit = prompt.find(entry_point)
        elif data in ["humanevaljava", "humanevalcpp", "humanevaljs", "mbjp", "mbjsp", "mbcp"]:
            doc_start_sign = '/*'
            doc_start_sign_alt = '//'
            start_limit = 0
        start = prompt.find(doc_start_sign, start_limit)
        if start == -1: # some humaneval will use "'''" for docstrings
            start = prompt.find(doc_start_sign_alt, start_limit)

        # import pdb;
        # pdb.set_trace()

        assert start != -1
        start = start + 2
        # some transformation might remove \n, so we need to keep \n \t in head part
        special = start + 1
        while prompt[special] in [" ", "\n", "\t", "*"]:
            special += 1
        start = special
        end = prompt.find(">>>", start_limit)
        if end == -1: #some docstring has no >>> string. instead they have for example, example strings
            end = prompt.lower().find("for example", start_limit)
        if end == -1:
            end = prompt.lower().find("example", start_limit)

        # some transformation might remove \n, so we need to keep \n \t in cases part
        special = end - 1
        while prompt[special] in [" ", "\n", "\t"]:
            special -= 1
        end = special + 1

        # import pdb;
        # pdb.set_trace()

        return prompt[:start], prompt[start:end], prompt[end:]

    # elif data in ["humanevalcpp"]:
    #     import pdb;
    #     pdb.set_trace()
    #     return "dummy"

    elif data in ["mbjp", "mbjsp", "mbjp", "mbjsp", "mbcp"]:
        # start = prompt.find('/**', prompt.find(entry_point))
        start = prompt.find('/**')
        assert start != -1
        start = start + 3
        special = start + 1
        while prompt[special] in [" ", "\n", "\t", "*"]:
            special += 1
        start = special
        end = prompt.find("* >")
        special = end - 1
        while prompt[special] in [" ", "\n", "\t"]:
            special -= 1
        end = special + 1
        return prompt[:start], prompt[start:end], prompt[end:]
    elif data in ["mbphp", "mbkp", "mbrbp"]:
        if data == "mbphp":
            start_flag = "You are an expert PHP programmer, and here is your task.\n *"
            end_flag = "* php >"
        elif data == "mbkp":
            start_flag = "You are an expert Kotlin programmer, and here is your task.\n *"
            end_flag = "* >>>"
        elif data == "mbrbp":
            start_flag = "You are an expert Ruby programmer, and here is your task.\n#"
            end_flag = "# irb>"
        start = prompt.find(start_flag) + len(start_flag)
        special = start + 1
        while prompt[special] in [" ", "\n", "\t", "*"]:
            special += 1
        start = special
        end = prompt.find(end_flag)
        special = end - 1
        while prompt[special] in [" ", "\n", "\t"]:
            special -= 1
        end = special + 1
        return prompt[:start], prompt[start:end], prompt[end:]
    else:
        print(f"Dataset {data} not supported for transformation!")
        exit()

def word_blacklist(code_string, language="python"):
    """ A help function to get a blacklist of words in the docstring that cannot be perturbed by nlaugmenter
    """
    # tsf = VarRenamerBase("natgen/languages.so", language)
    if language in ["humaneval", "humanevalpy", "mbpp"]: language = "python"
    elif language in ["humanevaljava", "mbjp"]: language = "java"
    elif language in ["humanevalcpp", "mbcp"]: language = "cpp"
    elif language in ["humanevaljs", "mbjsp"]: language = "javascript"
    elif language in ["humanevalgo", "mbgop"]: language = "go"
    else: print(f"data {language} not supported for docstring perturbation")

    tsf = VarRenamerBase("natgen/treesitter/build/my-languages.so", language)
    
    root = tsf.parse_code(code_string)
    var_names = tsf.extract_var_names(root, code_string)
    var_names = set(var_names)
    # for variables in type variables, add
    var_names.update(tsf.TYPE_VARS)
    # for variable name appears in function/class name, add
    not_var_ptype_var_names = tsf.get_not_var_ptype_var_names(root, code_string)
    var_names.update(not_var_ptype_var_names)
    return var_names


def clean_word(word):
    """ A help function to clean up words
    """
    # if word is "\ncost[]"", => "cost"
    new_word = ""
    start = False
    end = False
    for ch in word:
        if ch.isalnum():
            if not start: start = True
            new_word += ch
        else:
            if start: break
    return new_word


def preprocess_docstring(black_list, docstring, tsf):
    """ Preprocess docstring to replace variables in the blacklist to <|||> such that we will not perturb them
    """
    if hasattr(tsf, "perturb_level") and tsf.perturb_level in ["word-level", "char-level"]:
        docstring_words = docstring.split(" ")
        new_words = []
        replaces = []
        for word in docstring_words:
            if clean_word(word) in black_list:
                new_words.append("<|||>")
                replaces.append(word)
            else:
                new_words.append(word)
        new_doc = ' '.join(new_words)
        # import pdb; pdb.set_trace()
        return new_doc, replaces
    else:
        return docstring, []


def postprocess_docstring(docstring, replaces):
    """ Postprocess docstring to replace <|||> to original words
    """
    docstring = docstring.replace("< ||| >", "<|||>") # sometimes will be separated due to tokenization
    for replace in replaces:
        docstring = docstring.replace("<|||>", replace, 1)
    return docstring
