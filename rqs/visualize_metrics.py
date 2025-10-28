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

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

def visualize_metrics(data_points, column_names, filename, title="Metrics Relationship"):
    """
    Visualize relationships between two metrics, colored by pass status and shaped by language.
    Adds big average dots for PASSED and FAILED cases per language.

    Parameters:
        data_points: list of [metric1, metric2, pass_status, language]
        column_names: ["Metric 1 Name", "Metric 2 Name", "Pass Status Label", "Language Label"]
        filename: output image name (without extension)
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

    # Plot individual points
    for x, y, status, lang in zip(x_vals, y_vals, statuses, langs):
        color = color_map.get(status, "gray")
        marker = marker_map.get(lang, "x")
        plt.scatter(x, y, c=color, marker=marker, s=80, alpha=0.8)

    # --- Compute and plot averages per language for PASSED and FAILED --- #
    languages = sorted(set(langs))
    for lang in languages:
        lang_indices = [i for i, l in enumerate(langs) if l == lang]
        if not lang_indices:
            continue

        # Separate PASSED and FAILED
        pass_indices = [i for i in lang_indices if statuses[i] == "PASSED"]
        fail_indices = [i for i in lang_indices if statuses[i] != "PASSED"]

        # Compute averages if present
        if pass_indices:
            avg_pass_x = np.mean([x_vals[i] for i in pass_indices])
            avg_pass_y = np.mean([y_vals[i] for i in pass_indices])
            plt.scatter(
                avg_pass_x, avg_pass_y,
                s=400, c="limegreen", edgecolor="black", alpha=0.9,
                marker="o", label=f"{lang.upper()} PASSED avg"
            )
            plt.text(avg_pass_x, avg_pass_y, f"{lang.upper()}✓",
                     fontsize=9, ha="center", va="center", color="black", fontweight="bold")

        if fail_indices:
            avg_fail_x = np.mean([x_vals[i] for i in fail_indices])
            avg_fail_y = np.mean([y_vals[i] for i in fail_indices])
            plt.scatter(
                avg_fail_x, avg_fail_y,
                s=400, c="tomato", edgecolor="black", alpha=0.9,
                marker="X", label=f"{lang.upper()} FAIL avg"
            )
            plt.text(avg_fail_x, avg_fail_y, f"{lang.upper()}×",
                     fontsize=9, ha="center", va="center", color="black", fontweight="bold")

    # --- Labels and title --- #
    plt.xlabel(metric1_name, fontsize=12)
    plt.ylabel(metric2_name, fontsize=12)
    plt.title(title, fontsize=14, fontweight="bold")

    # --- Legends --- #
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

    # --- Save figure --- #
    os.makedirs(os.path.dirname(f"figures/{filename}.png"), exist_ok=True)
    plt.savefig(f"figures/{filename}.png", dpi=300, bbox_inches="tight")
    print(f"✅ Figure saved at: figures/{filename}.png")



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


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from typing import List, Any, Tuple

# Headers for the input data structure
FULL_HEADERS = [
    "func_name_change", "docstring_change", "code_change", "prompt_change", 
    "generated_code_change", "nominal_LOC", "perturbed_LOC", "nominal_tokens", 
    "perturbed_tokens", "nominal_complexity", "perturbed_complexity", 
    "run_status", "language"
]

def load_and_preprocess_data(raw_data: List[List[Any]]) -> pd.DataFrame:
    """Loads raw data into a DataFrame and performs essential preprocessing."""
    
    df = pd.DataFrame(raw_data, columns=FULL_HEADERS)
    
    # Ensure all change/metric columns are truly numeric
    # This prevents errors where pandas might infer a float column as 'object' due to mixed types
    numeric_cols_to_convert = FULL_HEADERS[:11] # first 11 columns are metrics
    for col in numeric_cols_to_convert:
        # Coerce non-numeric values to NaN
        df[col] = pd.to_numeric(df[col], errors='coerce') 

    # 1. Feature Engineering: Calculate differences and ratios
    df['cc_diff'] = df['nominal_complexity'] - df['perturbed_complexity']
    df['token_diff'] = df['nominal_tokens'] - df['perturbed_tokens']
    df['loc_diff'] = df['nominal_LOC'] - df['perturbed_LOC']
    
    # 2. Convert categorical status to a usable binary outcome (Pass/Fail)
    # 1 (Failure/Error) vs 0 (Pass)
    # This is necessary for standard correlation and Logistic Regression
    df['is_failure'] = np.where(df['run_status'].str.lower() == 'pass', 0, 1)

    # 3. Handle potential NaN/Infinity values (which can arise from divisions/preprocessing)
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['is_failure'])

    # Select only the numerical features we want to correlate/predict with
    CORRELATION_FEATURES = [
        'is_failure', 'cc_diff', 'token_diff', 'loc_diff', 
        'func_name_change', 'docstring_change', 'code_change', 'prompt_change', 
        'generated_code_change', 'nominal_LOC', 'nominal_complexity'
    ]
    
    return df[df.columns.intersection(CORRELATION_FEATURES + ['language', 'run_status'])].copy()

# ---
## 1. Correlation Heatmap Function
# ---

def calculate_correlation_heatmap(df: pd.DataFrame, title_suffix: str = "Overall", save_filename: str = None) -> None:
    """
    Generates a correlation heatmap to visualize the linear relationship 
    between all numerical metrics and the 'is_failure' outcome.
    
    If save_filename is provided, the figure is saved instead of displayed.
    """
    print(f"\n--- Correlation Analysis: {title_suffix} ---")
    
    # Exclude non-numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    
    # CRITICAL FIX FOR NAN CORRELATION: Remove columns with zero variance (constant columns)
    # Correlation is undefined when a variable is constant.
    non_constant_cols = numeric_df.columns[numeric_df.nunique() > 1]
    filtered_df = numeric_df[non_constant_cols]
    
    # Check if 'is_failure' still exists and is non-constant
    if 'is_failure' not in filtered_df.columns:
        print("Warning: 'is_failure' column is constant or missing. Cannot calculate correlation.")
        return
    
    if filtered_df.shape[1] < 2:
        print("Warning: After removing constants, only one or zero columns remain. Cannot calculate correlation.")
        return

    # Calculate the correlation matrix
    correlation_matrix = filtered_df.corr()
    
    # Extract the correlation values of metrics with 'is_failure'
    failure_correlation = correlation_matrix['is_failure'].sort_values(ascending=False)
    
    print("\nCorrelation with 'is_failure' (Higher value = Stronger link to Failure):")
    # Drop 'is_failure' from the output list itself for cleaner display
    print(failure_correlation.drop('is_failure', errors='ignore'))

    # Plotting the full correlation heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap='coolwarm', 
        fmt=".2f",
        linewidths=.5,
        cbar_kws={'label': 'Pearson Correlation Coefficient'},
        ax=ax,
        robust=True # Added robust=True to potentially help with the Numpy/Seaborn version issue
    )
    plt.title(f"Correlation Heatmap ({title_suffix})", fontsize=14)
    
    # Logic to save or show the figure
    plt.tight_layout() 
    if save_filename:
        # Save figure at 300 dpi for high-quality publication/report use
        plt.savefig(save_filename, dpi=300)
        plt.close(fig) # Close the figure to free up memory
        print(f"Correlation Heatmap saved to: {save_filename}")
    else:
        plt.show()

# ---
## 2. Logistic Regression Function (The answer to RQ2)
# ---

def run_logistic_regression_analysis(df: pd.DataFrame, language: str) -> None:
    """
    Runs a Logistic Regression model to find which features statistically predict 
    the probability of failure (is_failure=1) for a specific language.
    """
    print(f"\n--- Logistic Regression Analysis for {language.upper()} ---")
    
    # Filter data for the specific language
    subset_df = df[df['language'].str.lower() == language.lower()]
    
    # Define the dependent variable (Y) and independent variables (X)
    Y = subset_df['is_failure']
    
    # Drop columns that are constants, the outcome itself, or not predictors
    X_cols = subset_df.select_dtypes(include=[np.number]).columns.tolist()
    
    predictors = [col for col in X_cols if col not in ['is_failure']]
    
    # CRITICAL FIX FOR LOGISTIC REGRESSION: Remove constant predictors in the subset
    subset_X = subset_df[predictors]
    non_constant_predictors = subset_X.columns[subset_X.nunique() > 1]
    
    X = subset_X[non_constant_predictors]
    
    # Add a constant term for the intercept
    X = sm.add_constant(X, prepend=False)
    
    if len(Y) < 10:
        print(f"Skipping {language.upper()}: Not enough data points (<10).")
        return

    if X.isnull().any().any():
        # Drop rows with NaN values if they exist, to ensure sm.Logit runs
        combined_data = pd.concat([Y, X], axis=1).dropna()
        Y = combined_data['is_failure']
        X = combined_data.drop('is_failure', axis=1)
        
        if len(Y) < 10:
            print(f"Skipping {language.upper()}: Not enough non-NaN data points.")
            return

        
    try:
        # Run the logistic model
        model = sm.Logit(Y, X).fit(disp=False)
        
        # Display the results summary
        print(model.summary())
        
        print(f"\nInterpretation for {language.upper()}:")
        
        # We need to iterate over the predictors actually used in the model
        final_predictors = [col for col in X.columns if col != 'const']
        
        for predictor in final_predictors:
            p_value = model.pvalues[predictor]
            odds_ratio = np.exp(model.params[predictor])
            
            if p_value < 0.05:
                print(f"-> {predictor}: Statistically Significant (p={p_value:.3f}). Odds Ratio = {odds_ratio:.2f}")
                print(f"   A one-unit increase in {predictor} is associated with a {odds_ratio:.2f}x increase in the odds of failure.")
            elif p_value < 0.10:
                 print(f"-> {predictor}: Marginally Significant (p={p_value:.3f}). Odds Ratio = {odds_ratio:.2f}")

    except Exception as e:
        print(f"An error occurred during Logistic Regression for {language.upper()}: {e}")
        print("Check if the dependent variable 'is_failure' is constant (e.g., all 0s or all 1s) in this subset.")


# ---
## MAIN ANALYSIS FUNCTION
# ---

def analyze_robustness_statistics(raw_data: List[List[Any]], heatmap_filename: str = None) -> None:
    """
    Main function to run the full statistical analysis for RQ2.
    
    Args:
        raw_data: The list of lists containing all metric values.
        heatmap_filename: If provided, the correlation heatmap will be saved 
                          to this path (e.g., 'heatmap.png') instead of shown.
    """
    if not raw_data:
        print("Error: Input raw_data list is empty.")
        return
        
    df = load_and_preprocess_data(raw_data)
    
    if df.empty:
        print("Error: Preprocessed DataFrame is empty after cleaning.")
        return

    # 1. Correlation Analysis (Overall View) - Now accepts save_filename
    calculate_correlation_heatmap(df, title_suffix="All Languages Combined", save_filename=heatmap_filename)
    
    # 2. Language-Specific Logistic Regression (Direct Answer to RQ2)
    print("\n" + "="*80)
    print("LOGISTIC REGRESSION: PREDICTING FAILURE PROBABILITY BY LANGUAGE")
    print("="*80)
    
    for lang in df['language'].str.lower().unique():
        run_logistic_regression_analysis(df, lang)


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

    # key_metrics = ["nominal_complexity", "perturbed_complexity"]
    key_metrics = ["func_name_change", "docstring_change", "code_change", "prompt_change", "generated_code_change", "nominal_LOC", "perturbed_LOC", "nominal_tokens", "perturbed_tokens", "nominal_complexity", "perturbed_complexity"]
    key_columns = ["run_status", "lang"]
    column_names = key_metrics + key_columns 
    small_list = get_a_short_list(stat_list, key_metrics, key_columns)
    print(len(small_list))
    print(len(small_list[0]))


    # print(analyze_language_and_status(small_list))
    analyze_robustness_statistics(
        small_list,
        heatmap_filename="figures/language_correlation_heatmap.png" 
    )
    
    # visualize_metrics(small_list, column_names, f"{model_name}_{pert_type}")
    




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
