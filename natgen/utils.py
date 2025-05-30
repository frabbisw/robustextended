'''
This file includes helper function for transformations on code structure. Many of the functions are built based on 
NatGEN (https://github.com/saikat107/NatGen).
Original Copyright 2021 Saikat Chakraborty. Licensed under the MIT License.
Modifications Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''

from tree_sitter import Node
import os
import re
import time
# import jsbeautifier

def get_tokens(code_str, root, include_comments=False):
    """ Get all the tokens
    """
    if isinstance(code_str, str):
        code_str = code_str.encode()
    assert isinstance(root, Node)
    tokens = []
    if root.type == "comment":
        if include_comments: tokens.append(code_str[root.start_byte:root.end_byte].decode()) # append comments with #
        return tokens
    if "string" in str(root.type):
        # return [code_str[root.start_byte:root.end_byte].decode()]
        parent = root.parent
        if len(parent.children) == 1:
            if include_comments: tokens.append(code_str[root.start_byte:root.end_byte].decode()) # append comments with """
            return tokens
        else:
            return [code_str[root.start_byte:root.end_byte].decode()]
    children = root.children
    if len(children) == 0:
        tokens.append(code_str[root.start_byte:root.end_byte].decode().strip())
    for child in children:
        tokens += get_tokens(code_str, child)
    return tokens


def get_tokens_insert_before(code_str, root, insertion_code, insert_before_node, include_comments=False):
    """ Get all the tokens ahead
    """
    if isinstance(code_str, str):
        code_str = code_str.encode()
    assert isinstance(root, Node)
    tokens = []
    if root.type == "comment":
        if include_comments: tokens.append(code_str[root.start_byte:root.end_byte].decode()) # append comments with #
        return tokens
    if "string" in str(root.type):
        # return [code_str[root.start_byte:root.end_byte].decode()]
        parent = root.parent
        if len(parent.children) == 1:
            if include_comments: tokens.append(code_str[root.start_byte:root.end_byte].decode()) # append comments with """
            return tokens
        else:
            return [code_str[root.start_byte:root.end_byte].decode()]
    if root == insert_before_node:
        tokens += insertion_code.split()
    children = root.children
    if len(children) == 0:
        tokens.append(code_str[root.start_byte:root.end_byte].decode())
    for child in children:
        tokens += get_tokens_insert_before(code_str, child, insertion_code, insert_before_node)
    return tokens


def dfs_print(root, level=0):
    """ A help function to print in a dfs manner
    """
    for _ in range(level):
        print("\t", end="")
    print(root)
    for child in root.children:
        dfs_print(child, level + 1)


def count_nodes(root):
    """ Count nodes in parsed code
    """
    num_nodes = 1
    for child in root.children:
        if child is not None:
            num_nodes += count_nodes(child)
    return num_nodes


def extract_statement_within_size(root, max_node=10, endswith=None, code_string=None, tokenizer=None):
    """ Extract needed statements
    """
    if endswith is None:
        endswith = ["statement"]
    statements = []
    queue = [root]
    while len(queue) > 0:
        current_node = queue[0]
        queue = queue[1:]
        node_count = count_nodes(current_node)
        if code_string is not None and tokenizer is not None:
            tokens = tokenizer(code_string, current_node)
            current_code = " ".join(tokens).strip()
        else:
            current_code = "please provide code string and tokenizer to analyze code length"
        if any(str(current_node.type).endswith(e) for e in endswith) and\
                1 < node_count < max_node and len(current_code) > 0:
                statements.append(current_node)
        for child in current_node.children:
            queue.append(child)
    return statements


''' Start of Amazon Addition '''

def beautify_code(tokens, language="python"):
    if language in ["humaneval", "mbpp"]:
        language = "python"
    if language == "python":
        return beautify_python_code(tokens)
    else:
        print(f"language {language} not supported for beatify_code!")
        exit()

#         cond_signs = ["if", "else", "switch", "for", "foreach", "while", "do"]
#         operators = ["+", "-", "/", "*", "&", "&&", "<", ">", "%"]
#         incrementers = ["++", "+=", "--", "-=", "**", "/="]

def beautify_cpp_java_js_code(tokens, indent="    "):
    tmp = []
    for i in range(len(tokens)):
        tok = tokens[i]
        if "NEWLINE" in tok:
            rr = tok.split("NEWLINE")
            tmp.append(rr[0])
            for r in rr[1:]:
                tmp.append("NEWLINE")
                tmp.append(r)
        elif tok in ["{","}"]:
            try:
                if tokens[i+1] != "NEWLINE":
                    tmp.append(tok)
                    tmp.append("NEWLINE")
                else:
                    tmp.append(tok)
            except:
                tmp.append(tok)
        else:
            tmp.append(tok)
    tokens=tmp
    if "" in tokens:
        tmp = []
        for t in tokens:
            if t == "" or t is None:
                continue
            else:
                tmp.append(t)
        tokens=tmp

    total_indent = 0
    trailing_space = True;
    new_tokens = tokens[:1]

    # indent = "\t"
    # quote_start = False
    # trailing_space * " " +
    for i in range(1, len(tokens)):
        tok = tokens[i]
        if tok in ["#include","#define","using", "package", "import"] and tokens[i-1] != "NEWLINE":
            new_tokens.append("\n")
            new_tokens.append(tok)
            trailing_space = True
        elif tok == "{":
            new_tokens.append(" {")
            total_indent += 1
            trailing_space = False
        elif tok == "}":
            new_tokens.append("}")
            total_indent -= 1
            trailing_space = True
        elif tok == "(":
            # new_tokens.append(trailing_space * " " +"(")
            if tokens[i-1] in ["if", "for", "foreach", "while", "do"]:
                new_tokens.append(" " + "(")
            else:
                new_tokens.append("(")
            trailing_space = False
        elif tok == ")":
            new_tokens.append(")")
            trailing_space = True
        elif tok == ",":
            new_tokens.append(tok)
            trailing_space = True
        elif tok in ["if", "for", "foreach", "while", "do"]:
            if tokens[i-1] == "NEWLINE":
                new_tokens.append(tok)
            else:
                new_tokens.append("\n")
                new_tokens.append(tok)
                # new_tokens.append(trailing_space * " " + tok)
            trailing_space = True
        elif tok == ".":
            trailing_space = False
            new_tokens.append(tok)
        elif tok == "*":
            if tokens[i-1] == ".":
                new_tokens.append(tok)
                trailing_space = False
            else:
                new_tokens.append(" " + tok)
                trailing_space = True
        elif tok in ["+", "-", "/", "*", "&", "&&", "<", ">", "%"]:
            trailing_space = True
            new_tokens.append(trailing_space * " " + tok)
        elif tok == "!":
            new_tokens.append(" " + tok)
            trailing_space = False
        elif tok == ";":
            new_tokens.append(tok)
            trailing_space = True
        elif tok in ["++", "+=", "--", "-=", "**", "/=", ":="]:
            new_tokens.append(tok)
            trailing_space = False
        elif tok == "NEWLINE":
            trailing_space = False
            new_tokens.append("\n" + total_indent * indent)
        elif tok == "namespace":
            if trailing_space == False:
                new_tokens.append(" "+tok)
            trailing_space = True
        else:
            new_tokens.append(trailing_space * " " + tok)
            trailing_space = True
    if new_tokens[0] == "\n":
        new_tokens[1:]
    return "".join(new_tokens)
def beautify_python_code(tokens):
    """ A customized beautify function for python.
    NatGEN transformation will return a list of perturbed tokens, 
    we need to concatenate them together into a complete code.
    This is done before black normalization.
    """
    indent_count = 0
    code = ""
    i = 0
    new_tokens = []
    cat = False # if the next token should be concatenated to the previous one
    for ti, token in enumerate(tokens):
        if cat:
            cat = False
            if token not in ["NEWLINE", "INDENT", "DEDENT", "=", "+", "-", "*", "/"]:
                new_tokens[-1] = new_tokens[-1] + token
                cat = False
                continue
        if token in [".", "(", ")", "[", "]"]:
            if ti > 0 and new_tokens[-1] not in ["NEWLINE", "INDENT", "DEDENT", "=", "+", "-", "*", "/"]:
                # cat to the previous token
                new_tokens[-1] = new_tokens[-1] + token
                cat = True
            else:
                new_tokens.append(token)
                cat = True
            continue
        if token == ",":
            new_tokens[-1] = new_tokens[-1] + token
            continue
        new_tokens.append(token)
    tokens = new_tokens
    # import pdb; pdb.set_trace()

    while i < len(tokens):
        token = tokens[i]
        if token == "NEWLINE":
            code += "\n"
            for _ in range(indent_count):
                code += "\t"
        elif token == "INDENT":
            indent_count += 1
            code += "\t"
        elif token == "DEDENT":
            indent_count -= 1
            if code[-1] == "\t":
                code = code[:-1]
        else:
            code += token + " "
        i += 1
    lines = code.split("\n")
    taken_lines = []
    for line in lines:
        if len(line.strip()) > 0:
            taken_lines.append(line.rstrip())
    code = "\n".join(taken_lines)
    # code = code.replace(" . ", ".").replace(" .", ".").replace(". ", ".")
    # code = code.replace(" ,", ",")
    code = code.replace("NEWLINE", "\n")
    return code


def black_tablize_doc(doc, indent_type):
    """ we manually change doc indent to \t to align black normalization
    """
    new_doc = str(doc)
    if indent_type != "\t":
        new_lines = []
        lines = doc.split("\n")
        for line in lines:
            new_line = str(line)
            space_ahead = ""
            for ch_idx, ch in enumerate(line):
                if ch in [" ", "\t"]:
                    space_ahead += ch
                else:
                    break
            
            # new_line = space_ahead.replace(indent, indent + "# ") + new_line[ch_idx:]
            if indent_type in space_ahead:
                new_line = space_ahead.replace(indent_type, "\t") + new_line[ch_idx:]
            new_lines.append(new_line)
        new_doc = "\n".join(new_lines)
    return new_doc


def count_lines(s):
    """ count total line numbers of code
    """
    # import pdb; pdb.set_trace()
    try:
        if s[-1] != "\n": s += "\n"
    except:
        return 1
        # import pdb;
        # pdb.set_trace()
    tmp = cnt = 0
    while tmp != -1:
        start = tmp + 1
        tmp = s.find('\n', start)
        if tmp == -1: break
        cnt += 1
    return cnt


# def sep(code, entry_point):
#     """ core function to seperate function signature (header) ||| docstring ||| code
#     here entry point is the main function we need to complete
#     """
#     single_doc = code.find("\'\'\'")
#     double_doc = code.find("\"\"\"")
#     if single_doc == -1: doc_type = "\"\"\""
#     elif double_doc == -1: doc_type = "\'\'\'"
#     elif single_doc != -1 and double_doc != -1:
#         doc_type = "\"\"\""
#     else:
#         print("doc_type not supported!")
#         exit()
#     header_end = code.find('\n', code.find(entry_point))
#     header = code[:header_end + 1]
#     doc_begin = code.find(doc_type, header_end)
#     doc_end = code.find(f"{doc_type}\n", doc_begin + 3)
#     # doc_begin != -1 and doc_end != -1, means no docstring in the code, just return "" for docstring
#     doc = code[header_end+1 : doc_end+4] if doc_begin != -1 and doc_end != -1 else ""
#     code = code[doc_end+4:] if doc_begin != -1 and doc_end != -1 else code[header_end+1:]
#     # import pdb; pdb.set_trace()
#     return header, doc, code

def sep(code, entry_point, data):
    # import pdb; pdb.set_trace()
    if data in ["humanevalpy", "humaneval", "mbpp"]:
        # if code is None:
        #     import pdb; pdb.set_trace()
        single_doc = code.find("\'\'\'")
        double_doc = code.find("\"\"\"")
        if single_doc == -1:
            doc_type = "\"\"\""
        elif double_doc == -1:
            doc_type = "\'\'\'"
        elif single_doc != -1 and double_doc != -1:
            doc_type = "\"\"\""
        else:
            print("doc_type not supported!")
            exit()
        header_end = code.find('\n', code.find(entry_point))
        header = code[:header_end + 1]
        doc_begin = code.find(doc_type, header_end)
        doc_end = code.find(f"{doc_type}\n", doc_begin + 3)
        # doc_begin != -1 and doc_end != -1, means no docstring in the code, just return "" for docstring
        doc = code[header_end + 1: doc_end + 4] if doc_begin != -1 and doc_end != -1 else ""
        code = code[doc_end + 4:] if doc_begin != -1 and doc_end != -1 else code[header_end + 1:]
        # import pdb; pdb.set_trace()
        return header, doc, code
    elif data in ["humanevaljava"]:
        lines = code.split("\n")
        first_index = 0
        last_index = 0
        for i in range(len(lines)):
            if "Solution" in lines[i]:
                first_index=i
            elif entry_point in lines[i]:
                last_index=i
                # break
        # if "accepts a list of strings as a parameter" in code:
        #     import pdb; pdb.set_trace()
        return "\n".join(lines[:first_index+1])+"\n", "\n".join(lines[first_index+1:last_index])+"\n", "\n".join(lines[last_index:])
    elif data in ["humanevalcpp"]:
        if "*/" not in code:
            return "","",code
        else:
            lines = code.split("\n")
            first_index = 0
            last_index = 0
            for i in range(len(lines)):
                if "/*" in lines[i]:
                    first_index = i
                elif "*/" in lines[i]:
                    last_index = i
        return "","\n".join(lines[:last_index + 1])+"\n", "\n".join(lines[last_index + 1:])
    elif data in ["humanevaljs"]:
        if "*/" not in code:
            return "", "", code
        else:
            lines = code.split("\n")
            first_index = 0
            last_index = 0
            for i in range(len(lines)):
                if "/*" in lines[i]:
                    first_index = i
                elif "*/" in lines[i]:
                    last_index = i
        return "", "\n".join(lines[:last_index + 1]) + "\n", "\n".join(lines[last_index + 1:])
    elif data in ["humanevalgo", "mbppgo"]:
        if "//" not in code:
            entry_line = -1
            lines = code.split("\n")
            for i in range(len(lines)):
                if entry_point in lines[i]:
                    entry_line = i
                    break
            return "\n".join(lines[0:entry_line])+"\n", "", "\n".join(lines[entry_line:])
        else:
            start_point = -1
            end_point = -1
            lines = code.split("\n")
            for i in range(len(lines)):
                if "//" in lines[i]:
                    if start_point < 0:
                        start_point = i
                if entry_point in lines[i]:
                    if "func" in lines[i]:
                        end_point = i
                        break
                    else:
                        continue
            head = "\n".join(lines[0:start_point])+"\n"
            doc = "\n".join(lines[start_point:end_point])+"\n"
            test = "\n".join(lines[end_point:])
            return head, doc, test
    else:
        print(f"dataset {data} not supported")
        exit()

def black_reformat(code, orig_code=None, order=0, debug=False):
    """ Calling black function to normalize python code
    """
    tmp_name = f"tmp{order}_{time.time()}.py"
    with open(tmp_name, 'w') as file:
        file.write(code)
    resp = os.system(f"black {tmp_name} -q")
    if resp != 0:
        if debug: print("black failed to parse for code:\n")
        if debug: print(code)
        if orig_code is not None and "partial" in orig_code:
            print(f"\n === black fail to parse on [{orig_code['task_id']}] ===\n")
            if debug: print(orig_code["partial"])
        if debug: import pdb; pdb.set_trace()
    with open(tmp_name, 'r') as file:
        res = file.read()
    # if resp: os.system(f"rm {tmp_name}")
    os.system(f"rm {tmp_name}")
    return res, resp == 0


def move_partial_code(entry, tsf, black = False, ptb = False):
    """ A back up function to perturb with natgen
    """
    res = {}
    for k, v in entry.items():
        res[k] = v
    
    whole = res['prompt'] + res['canonical_solution']
    header, doc, body = sep(whole)
    before = header+body
    if ptb:
        new_code, meta = tsf.transform_code(code = before)
        after = beautify_python_code(new_code.split()).replace("\\", "")
    else:
        after = before
    if black:
        after = black_reformat(after)
    new_header,_, new_body = sep(after)
    
    num_lines = count_lines(new_body)
    if num_lines == 1:
        idx = new_body.find('return')
        res['prompt'] = header + doc + new_body[:idx + 6] + "   \\\n"
        res['canonical_solution'] = "   " + new_body[idx + 6:]
    else:
        half = num_lines // 2
        tmp = 0
        while half > 0:
            idx = new_body.find('\n', tmp)
            tmp = idx + 1
            half -= 1
        res['prompt'] = header + doc + new_body[:idx + 1]
        res['canonical_solution'] = new_body[idx + 1:]
    return res #, flag
''' End of Amazon Addition '''
