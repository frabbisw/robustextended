
# from matplotlib import docstring


def doc2comments_structural(code, entry_point, language="java"):
    # print(code)
    # import pdb; pdb.set_trace()
    """ change \"\"\" to # comments
    This function only fits for special style of MBXP or humaneval
    """
    # if "/*" not in code and "*/" not in code:
    #     print(f"got error for \n{code}")
    #     code = "/*\n" \
    #            "returns encoded string by shifting every character by 5 in the alphabet.\n" \
    #            "*/\n" + code
    #
    doc_start_sign = "/*"
    doc_end_sign = "*/"
    if language == "javascript":
        code = code.replace("*/", "*/\n")

    # print("doc_type not supported!")
    # exit()

    doc_start = code.find(doc_start_sign)
    assert doc_start != -1, "dataset not supported"
    # get all the indent before """
    doc_line_start = doc_start - 1
    indent = ""
    while True:
        ch = code[doc_line_start]
        if ch in [" ", "\t"]:
            doc_line_start -= 1
            indent = ch + indent
        else:
            break
    if code[doc_line_start] != "\n": import pdb; pdb.set_trace()
    assert code[doc_line_start] == "\n"
    doc_line_start += 1

    doc_end = code.find(doc_end_sign, doc_start + 2)
    # in case there are spaces after doc_end of """
    doc_line_end = doc_end + 2
    for ch in code[doc_line_end:]:
        if ch in [" ", "\t"]:
            doc_line_end += 1
        else:
            break
    if code[doc_line_end] != "\n": import pdb; pdb.set_trace()
    assert code[doc_line_end] == "\n"

    doc_lines = code[doc_line_start: doc_line_end + 1]

    lines = doc_lines.split("\n")

    new_lines = []
    for line in lines:
        new_line = str(line)
        if line.replace(" ", "").replace("\t", "").replace("\n", "") == doc_start_sign or line.replace(" ", "").replace("\t", "").replace("\n", "") == doc_end_sign:
            # remove these lines
            continue
        if doc_start_sign in line:
            new_line = new_line.replace(f"{doc_start_sign} ", "").replace(doc_start_sign, "")
        if doc_end_sign in line:
            new_line = new_line.replace(f"{doc_end_sign} ", "").replace(doc_end_sign, "")
        space_ahead = ""
        # import pdb; pdb.set_trace()
        for ch_idx, ch in enumerate(line):
            if ch in [" ", "\t"]:
                space_ahead += ch
            else:
                break

        # new_line = space_ahead.replace(indent, indent + "# ") + new_line[ch_idx:]
        if indent in space_ahead:
            new_line = space_ahead[: len(indent)] + "// " + space_ahead[len(indent):] + new_line[ch_idx:]
        new_lines.append(new_line)

    new_code = code[:doc_line_start] + "\n".join(new_lines) + code[doc_line_end + 1:]

    # print(new_code)
    # import pdb; pdb.set_trace()

    return new_code

def doc2comments(code, entry_point, language="python"):
    # print("@" * 50)
    # print(code)
    # print("+" * 50)
    # print(entry_point)
    # print("#"*50)
    if language in ["java", "cpp", "javascript", "go"]:
        return doc2comments_structural(code, entry_point, language)
    """ change \"\"\" to # comments
    This function only fits for special style of MBXP or humaneval
    """
    single_doc = code.find("\'\'\'")
    double_doc = code.find("\"\"\"")
    if single_doc == -1: doc_type = "\"\"\""
    elif double_doc == -1: doc_type = "\'\'\'"
    elif single_doc != -1 and double_doc != -1:
        doc_type = "\"\"\""
    else:
        print("doc_type not supported!")
        exit()
    
    doc_start = code.find(doc_type, code.find(entry_point))
    assert doc_start != -1, "only support mbxp and humaneval for this function"
    # get all the indent before """
    doc_line_start = doc_start - 1
    indent = ""
    while True:
        ch = code[doc_line_start]
        if ch in [" ", "\t"]:
            doc_line_start -= 1
            indent = ch + indent
        else:
            break
    # if code[doc_line_start] != "\n": import pdb; pdb.set_trace()
    assert code[doc_line_start] == "\n"
    doc_line_start += 1

    doc_end = code.find(doc_type, doc_start + 3)
    # in case there are spaces after doc_end of """
    doc_line_end = doc_end + 3
    for ch in code[doc_end:]:
        if ch in [" ", "\t"]:
            doc_line_end += 1
        else:
            break
    # if code[doc_line_end] != "\n": import pdb; pdb.set_trace()
    assert code[doc_line_end] == "\n"

    doc_lines = code[doc_line_start: doc_line_end + 1]

    lines = doc_lines.split("\n")

    new_lines = []
    for line in lines:
        new_line = str(line)
        if line.replace(" ", "").replace("\t", "").replace("\n", "") == doc_type:
            # remove these lines
            continue
        if doc_type in line:
            new_line = new_line.replace(f"{doc_type} ", "").replace(doc_type, "")
        space_ahead = ""
        # import pdb; pdb.set_trace()
        for ch_idx, ch in enumerate(line):
            if ch in [" ", "\t"]:
                space_ahead += ch
            else:
                break
        
        # new_line = space_ahead.replace(indent, indent + "# ") + new_line[ch_idx:]
        if indent in space_ahead:
            new_line = space_ahead[: len(indent)] + "# " + space_ahead[len(indent):]  + new_line[ch_idx:]
        new_lines.append(new_line)

    new_code = code[:doc_line_start] + "\n".join(new_lines) + code[doc_line_end + 1:]

    # import pdb; pdb.set_trace()
    return new_code

def doc2comments_general_structural(code, entry_point=None):
    """ change \"\"\" to # comments
    This function is general, perturbing all of \"\"\" to # comments
    """
    new_code = str(code)
    doc_start_sign = "/*"
    doc_end_sign = "*/"
    doc_start = new_code.find(doc_start_sign)
    while doc_start != -1:
        if doc_start > 0:
            # get all the indent before """
            doc_line_start = doc_start - 1
            indent = ""
            while doc_line_start >= 0:
                ch = new_code[doc_line_start]
                if ch in [" ", "\t"]:
                    doc_line_start -= 1
                    indent = ch + indent
                else:
                    break
            # if new_code[doc_line_start] != "\n": import pdb; pdb.set_trace()
            # assert new_code[doc_line_start] == "\n"
            doc_line_start += 1
        else:
            indent = ""
            doc_line_start = doc_start

        doc_end = new_code.find(doc_end_sign, doc_start + len(doc_end_sign))
        if doc_end == -1: break  # some times appear text/strings...
        # in case there are spaces after doc_end of """
        doc_line_end = doc_end + len(doc_end_sign)
        for ch in new_code[doc_end:]:
            if ch in [" ", "\t"]:
                doc_line_end += 1
            else:
                break
        # if new_code[doc_line_end] != "\n": import pdb; pdb.set_trace()
        # assert new_code[doc_line_end] == "\n"

        doc_lines = new_code[doc_line_start: doc_line_end]
        # print(doc_lines)
        # import pdb; pdb.set_trace()

        lines = doc_lines.split("\n")

        new_lines = []
        for line in lines:
            new_line = str(line)
            if line.replace(" ", "").replace("\t", "").replace("\n", "") == doc_start_sign or line.replace(" ", "").replace("\t", "").replace("\n", "") == doc_end_sign:
                # remove these lines
                new_lines.append(new_line.replace(f"{doc_start_sign} ", "").replace(doc_start_sign, ""))
                continue
            if doc_start_sign in line:
                new_line = new_line.replace(f"{doc_start_sign} ", "").replace(doc_start_sign, "")
            if doc_end_sign in line:
                new_line = new_line.replace(f"{doc_end_sign} ", "").replace(doc_end_sign, "")
            space_ahead = ""
            ch_idx = 0
            for ch_idx, ch in enumerate(line):
                if ch in [" ", "\t"]:
                    space_ahead += ch
                else:
                    break

            # new_line = space_ahead.replace(indent, indent + "# ") + new_line[ch_idx:]
            if indent in space_ahead:
                new_line = space_ahead[: len(indent)] + "// " + space_ahead[len(indent):] + new_line[ch_idx:]
            new_lines.append(new_line)

        new_code = new_code[:doc_line_start] + "\n".join(new_lines) + "\n" + new_code[doc_line_end + 1:]
        last_doc_start = doc_start
        doc_start = new_code.find(doc_start_sign)  # need to refind the doc end idx, previous ones already removed
        if last_doc_start == doc_start: print("Warning: doc start repeated!")

    return new_code

def doc2comments_general_python(code, entry_point=None):
    """ change \"\"\" to # comments
    This function is general, perturbing all of \"\"\" to # comments
    """
    new_code = str(code)
    doc_types = ["\"\"\"", "\'\'\'"]
    for doc_type in doc_types:
        doc_start = new_code.find(doc_type)
        while doc_start != -1:
            if doc_start > 0:
                # get all the indent before """
                doc_line_start = doc_start - 1
                indent = ""
                while doc_line_start >= 0:
                    ch = new_code[doc_line_start]
                    if ch in [" ", "\t"]:
                        doc_line_start -= 1
                        indent = ch + indent
                    else:
                        break
                # if new_code[doc_line_start] != "\n": import pdb; pdb.set_trace()
                # assert new_code[doc_line_start] == "\n"
                doc_line_start += 1
            else:
                indent = ""
                doc_line_start = doc_start

            doc_end = new_code.find(doc_type, doc_start + len(doc_type))
            if doc_end == -1: break # some times appear text/strings...
            # in case there are spaces after doc_end of """
            doc_line_end = doc_end + len(doc_type)
            for ch in new_code[doc_end:]:
                if ch in [" ", "\t"]:
                    doc_line_end += 1
                else:
                    break
            # if new_code[doc_line_end] != "\n": import pdb; pdb.set_trace()
            # assert new_code[doc_line_end] == "\n"

            doc_lines = new_code[doc_line_start: doc_line_end]
            # print(doc_lines)
            # import pdb; pdb.set_trace()

            lines = doc_lines.split("\n")

            new_lines = []
            for line in lines:
                new_line = str(line)
                if line.replace(" ", "").replace("\t", "").replace("\n", "") == doc_type:
                    # remove these lines
                    new_lines.append(new_line.replace(f"{doc_type} ", "").replace(doc_type, ""))
                    continue
                if doc_type in line:
                    new_line = new_line.replace(f"{doc_type} ", "").replace(doc_type, "")
                space_ahead = ""
                ch_idx = 0
                for ch_idx, ch in enumerate(line):
                    if ch in [" ", "\t"]:
                        space_ahead += ch
                    else:
                        break
                
                # new_line = space_ahead.replace(indent, indent + "# ") + new_line[ch_idx:]
                if indent in space_ahead:
                    new_line = space_ahead[: len(indent)] + "# " + space_ahead[len(indent):]  + new_line[ch_idx:]
                new_lines.append(new_line)

            new_code = new_code[:doc_line_start] + "\n".join(new_lines) + "\n" + new_code[doc_line_end + 1:]
            last_doc_start = doc_start
            doc_start = new_code.find(doc_type) # need to refind the doc end idx, previous ones already removed
            if last_doc_start == doc_start: print("Warning: doc start repeated!")

    return new_code


def doc2comments_general(code, entry_point=None, language="python"):
    if language == "python":
        return doc2comments_general_python(code, entry_point)
    elif language in ["java", "cpp", "javascript", "go"]:
        return doc2comments_general_structural(code, entry_point)
    else:
        print(f"language {language} not supported for doc2comments")
        exit()