import re
import difflib
import nltk
from nltk import word_tokenize
import json
import jsonlines

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Ensure tokenizers are available
nltk.download("punkt", quiet=True)

CODE_RUN_STATUS = {"PASSED":0, "ASSERTION":1, "COMPILATION":2, "TIMEOUT": 3, "RUNTIME": 4}
RUN_STATUS_MAP = {v: k for k, v in CODE_RUN_STATUS.items()}

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

# Visualize
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

def visualize_metrics(data_points, column_names, filename, title="Metrics Relationship"):
    """
    Visualize relationships between two metrics, colored by pass status and shaped by language.
    Adds big average dots for each language.

    Parameters:
        data_points: list of [metric1, metric2, pass_status, language]
        column_names: ["Metric 1 Name", "Metric 2 Name", "Pass Status Label", "Language Label"]
        filename: name for saving the figure
        title: optional plot title
    """

    # Extract columns
    metric1_name, metric2_name, _, _ = column_names
    x_vals = [d[0] for d in data_points]
    y_vals = [d[1] for d in data_points]
    statuses = [d[2].upper() for d in data_points]
    langs = [d[3].lower() for d in data_points]

    # Define colors for pass status
    color_map = {
        "PASSED": "green",
        "COMPILATION": "red",
        "ASSERTION": "violet",
        "TIMEOUT": "blue",
        "RUNTIME": "black"
    }

    # Define markers for language
    marker_map = {
        "java": "|",
        "cpp": "_",
        "js": "x"
    }

    plt.figure(figsize=(8, 6))

    # Plot each individual point
    for x, y, status, lang in zip(x_vals, y_vals, statuses, langs):
        color = color_map.get(status, "gray")
        marker = marker_map.get(lang, "x")
        plt.scatter(x, y, c=color, marker=marker, s=80, alpha=0.8)

    # ---- Plot average points per language ----
    for lang in sorted(set(langs)):
        indices = [i for i, l in enumerate(langs) if l == lang]
        if not indices:
            continue
        avg_x = np.mean([x_vals[i] for i in indices])
        avg_y = np.mean([y_vals[i] for i in indices])

        plt.scatter(
            avg_x, avg_y,
            s=400,                # Large size for average dot
            c="gold",             # Gold to make it pop
            edgecolor="black",
            alpha=0.9,
            label=f"{lang.upper()} avg"
        )
        plt.text(
            avg_x, avg_y,
            lang.upper(),
            fontsize=9,
            ha="center",
            va="center",
            color="black",
            fontweight="bold"
        )

    # ---- Labels and title ----
    plt.xlabel(metric1_name, fontsize=12)
    plt.ylabel(metric2_name, fontsize=12)
    plt.title(title, fontsize=14, fontweight="bold")

    # ---- Legends ----
    color_patches = [mpatches.Patch(color=v, label=k.capitalize()) for k, v in color_map.items()]
    marker_patches = [
        plt.Line2D([0], [0], marker=v, color="w", label=k.capitalize(),
                   markerfacecolor="gray", markersize=10, markeredgecolor="black")
        for k, v in marker_map.items()
    ]

    legend1 = plt.legend(handles=color_patches, title="Pass Status", loc="upper right")
    plt.gca().add_artist(legend1)
    plt.legend(handles=marker_patches, title="Language", loc="lower right")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    # ---- Save figure ----
    os.makedirs(os.path.dirname(f"figures/{filename}.png"), exist_ok=True)
    plt.savefig(f"figures/{filename}.png", dpi=300, bbox_inches="tight")
    print(f"✅ Figure saved at: figures/{filename}.png")

# Example
# data = [
#     [5.3, 0.12, "pass", "java"],
#     [4.1, 0.32, "compilation", "cpp"],
#     [6.8, 0.15, "assertion", "python"],
#     [5.5, 0.08, "pass", "cpp"],
# ]

# cols = ["Cyclomatic Complexity", "Change %", "Pass Status", "Language"]

# visualize_metrics(data, cols, title="Cyclomatic Complexity vs Change%", save_path="figures/complexity_vs_change.png")


# ---------- TOKENIZATION & BASIC UTILITIES ----------

def tokenize_code(code: str):
    """Tokenize code using NLTK; language-agnostic but good for Java/C++/JS."""
    code = re.sub(r"([^\w])", r" \1 ", code)
    return word_tokenize(code)

def calc_change_percent(text1: str, text2: str) -> float:
    """Compute change % between two code snippets using token-based comparison."""
    tokens1 = tokenize_code(text1)
    tokens2 = tokenize_code(text2)
    seq = difflib.SequenceMatcher(None, tokens1, tokens2)
    similarity = seq.ratio()
    change_percent = (1 - similarity) * 100
    return round(change_percent, 3)

def count_loc(code: str) -> int:
    """Count non-empty lines of code."""
    return sum(1 for line in code.splitlines() if line.strip())

def token_length(code: str) -> int:
    """Count total number of tokens in the code."""
    return len(tokenize_code(code))

# ---------- CYCLOMATIC COMPLEXITY (language-generic) ----------

def cyclomatic_complexity(code: str) -> int:
    """
    Approximate cyclomatic complexity for C++/Java/JS by counting decision points.
    Counts keywords like if, for, while, case, catch, etc.
    Works even for non-compilable code.
    """
    # Lowercase for uniformity
    code = code.lower()
    
    # Common control flow keywords across C++, Java, JS
    patterns = [
        r"\bif\b",
        r"\bfor\b",
        r"\bwhile\b",
        r"\bcase\b",
        r"\bcatch\b",
        r"\belse\s+if\b",
        r"\?\s*[^:]+:",      # ternary operator
        r"\b&&\b",
        r"\b\|\|\b"
    ]

    count = 1  # base complexity
    for p in patterns:
        count += len(re.findall(p, code))
    return count

# ---------- CODE PART SEPARATION ----------

def extract_function_parts(code: str, func_name: str):
    """
    Roughly separate docstring/comments, function signature, and body for the target function.
    Works across Java/C++/JS.
    """
    lines = code.splitlines()
    docstring_lines, signature_lines, body_lines = [], [], []
    in_docstring = False
    in_function = False

    for line in lines:
        stripped = line.strip()

        # Detect docstring (/* ... */, //, or /** ... */)
        if stripped.startswith("/*") or stripped.startswith("/**"):
            in_docstring = True
        if in_docstring:
            docstring_lines.append(line)
            if stripped.endswith("*/"):
                in_docstring = False
            continue
        elif stripped.startswith("//"):
            docstring_lines.append(line)
            continue

        # Detect function signature
        if re.search(rf"\b{func_name}\s*\(", stripped):
            in_function = True
            signature_lines.append(line)
            continue

        # Function body (until closing brace)
        if in_function:
            body_lines.append(line)

    docstring = "\n".join(docstring_lines)
    signature = "\n".join(signature_lines)
    body = "\n".join(body_lines)
    return docstring, signature, body

# ---------- METRICS WRAPPERS ----------

def compute_pre_generation_metrics(nominal_prompt: str, perturbed_prompt: str, nominal_func_name: str, perturbed_func_name: str):
    """Metrics comparing nominal vs perturbed prompts before generation."""
    n_doc, n_sig, n_body = extract_function_parts(nominal_prompt, nominal_func_name)
    p_doc, p_sig, p_body = extract_function_parts(perturbed_prompt, perturbed_func_name)

    return {
        "func_name_change": calc_change_percent(n_sig, p_sig),
        "docstring_change": calc_change_percent(n_doc, p_doc),
        "code_change": calc_change_percent(n_body, p_body),
        "prompt_change": calc_change_percent(nominal_prompt, perturbed_prompt),
    }

def compute_post_generation_metrics(nominal_code: str, perturbed_code: str):
    """Metrics comparing generated codes and their complexity."""
    return {
        "generated_code_change": calc_change_percent(nominal_code, perturbed_code),
        "nominal_LOC": count_loc(nominal_code),
        "perturbed_LOC": count_loc(perturbed_code),
        "nominal_tokens": token_length(nominal_code),
        "perturbed_tokens": token_length(perturbed_code),
        "nominal_complexity": cyclomatic_complexity(nominal_code),
        "perturbed_complexity": cyclomatic_complexity(perturbed_code),
    }

def eliminate_second_Sollution(sample_java_solution):
    ##eliminate 2nd solution class
    first_class_pointer = sample_java_solution.find("class Solution")
    if first_class_pointer < 0:
        return sample_java_solution
    second_class_pointer = sample_java_solution.find("class Solution", first_class_pointer + 5)
    if second_class_pointer < 0:
        second_class_pointer = sample_java_solution.find("public class", first_class_pointer + 5)
    if second_class_pointer < 0:
        return sample_java_solution
    sample_java_solution = sample_java_solution[:second_class_pointer]
    return sample_java_solution[:sample_java_solution.rfind("}")+1]

def filter_gc(gc, lang):
    stop_tokens = [["<｜begin▁of▁sentence｜>", "<｜end▁of▁sentence｜>"], ["<|endoftext|>", "<|endoftext|>"], ["<code>", "</code>"], ["<|im_start|>", "<|im_end|>"]]
    for st, et in stop_tokens:
        if st in gc:
            gc = gc[gc.find(st)+len(st):]
        if et in gc:
            gc = gc[:gc.find(et)]
    gc = gc.strip()
    if lang == "java":
        gc = eliminate_second_Sollution(gc)
    return gc

def get_a_list(dataset_path, model_name, lang, pert_type, aug_type):
    print("preparing files ...")
    pert_folder=f"{dataset_path}/{model_name}/generated_pass5_1/{lang}/{pert_type}/{aug_type}"
    if pert_type in ["natgen", "format"]:
        nominal_path=f"{dataset_path}/{model_name}/generated_pass5_1/{lang}/partial/f_s0.jsonl"
    else:
        nominal_path=f"{dataset_path}/{model_name}/generated_pass5_1/{lang}/nominal/f_s0.jsonl"

    ret_list = []
    nominal_prompts = load_prompts(nominal_path)
    nominal_dict = {p["task_id"]: p for p in nominal_prompts}

    print("preparing metrics from perturbed files ...")
    for i in range(5):
        pert_path = f"{pert_folder}/f_s{i}.jsonl"
        pert_prompts = load_prompts(pert_path)
        for p in pert_prompts:
            # print(f"{p['task_id']}")
            if nominal_dict[p["task_id"]]["passed_evalplus"] == 0:
                continue
            # change = compute_pre_generation_metrics(nominal_dict[p["task_id"]]["prompt"], p["prompt"], nominal_dict[p["task_id"]]["entry_point"], p["entry_point"])
            # ret_list.append([change["func_name_change"], change["prompt_change"], RUN_STATUS_MAP[p["run_status_evalplus"]], lang])
            change_pre = compute_pre_generation_metrics(nominal_dict[p["task_id"]]["prompt"], p["prompt"], nominal_dict[p["task_id"]]["entry_point"], p["entry_point"])
            change_post = compute_post_generation_metrics(filter_gc(nominal_dict[p["task_id"]]["gc"], lang), filter_gc(p["gc"], lang))
            change = change_pre | change_post            
            ret_list.append(change | {"run_status": RUN_STATUS_MAP[p["run_status_evalplus"]], "lang": lang})
            # ret_list.append([change[keys[0]], change[keys[1]], RUN_STATUS_MAP[p["run_status_evalplus"]], lang])
            
    return ret_list

def get_a_short_list(stat_list, key_metrics, key_columns):
    ret_list = []
    for s in stat_list:
        row = []
        for m in key_metrics:
            row.append(s[m])
        for c in key_columns:
            row.append(s[c])
        ret_list.append(row)
    return ret_list        
            
# ---------- EXAMPLE USAGE ----------
if __name__ == "__main__":
    dataset_path = "/home/f_rabbi/recode/extended_all_results/datasets-backup"
    model_name = sys.argv[1]
    pert_type = sys.argv[2]
    langs = ["cpp", "java", "js"]
    
    stat_list = []
    for lang in langs:
        for aug_type in os.listdir(f"{dataset_path}/{model_name}/generated_pass5_1/{lang}/{pert_type}"):        
            local_list = get_a_list(dataset_path, model_name, lang, pert_type, aug_type)
            print(len(local_list))
            stat_list += local_list

    key_metrics = ["nominal_complexity", "perturbed_complexity"]
    key_columns = ["run_status", "lang"]
    column_names = key_metrics + key_columns 
    small_list = get_a_short_list(stat_list, ["nominal_complexity", "perturbed_complexity"], ["run_status", "lang"])
    print(len(small_list))
    print(len(small_list[0]))
    
    # visualize_metrics(small_list, column_names, "func_name")
    # print(len(res))
    # print(res[0])
  

  
    # nominal_prompt = """
    # /** Add two numbers */
    # int add(int a, int b) {
    #     return a + b;
    # }
    # """

    # perturbed_prompt = """
    # // Function to sum two integers
    # int addNumbers(int x, int y) {
    #     return x + y;
    # }
    # """

    # nominal_code = """
    # int result = add(3, 4);
    # if (result > 0) {
    #     printf("Positive");
    # }
    # """

    # perturbed_code = """
    # int result = addNumbers(3, 4);
    # if (result > 0) {
    #     printf("Positive");
    # } else {
    #     printf("Zero or Negative");
    # }
    # """

    # print("Pre-generation metrics:")
    # print(compute_pre_generation_metrics(nominal_prompt, perturbed_prompt, func_name="add"))

    # print("\nPost-generation metrics:")
    # print(compute_post_generation_metrics(nominal_code, perturbed_code))
