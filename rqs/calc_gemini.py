import re
import difflib
from typing import List, Dict, Union, Tuple

# NOTE ON EXTERNAL DEPENDENCIES:
# All external dependencies (like 'radon') have been explicitly removed.
# Cyclomatic Complexity is now calculated exclusively using keyword counting.


# ----------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------

def simple_tokenize(code_or_prompt: str) -> List[str]:
    """
    Splits the string into tokens using whitespace and common symbols as delimiters.
    This serves as a robust, language-agnostic proxy for LLM tokenization.
    """
    # Replace common structural symbols with spaces for token separation, then split by whitespace
    text = re.sub(r'([{}()\[\].,;:\'\"=\+\-\*/&|!<>])', r' \1 ', code_or_prompt)
    tokens = text.split()
    return tokens

def calculate_total_token_length(code_or_prompt: str) -> int:
    """Calculates the total number of tokens in a string."""
    return len(simple_tokenize(code_or_prompt))

def calculate_percentage_change(nominal_value: int, perturbed_value: int) -> float:
    """Calculates the percentage change from nominal to perturbed value."""
    if nominal_value == 0:
        # If nominal is zero, treat change as infinite unless perturbed is also zero
        return 0.0 if perturbed_value == 0 else float('inf')
    return (perturbed_value - nominal_value) / nominal_value * 100.0


# ----------------------------------------------------------------------
# BEFORE GENERATION METRICS (Input Shock)
# ----------------------------------------------------------------------

def calculate_token_level_change(nominal_prompt: str, perturbed_prompt: str) -> float:
    """
    Metric 1.1: Token-level Change Ratio (1.0 = identical, 0.0 = completely different)
    Measures the similarity between the nominal and perturbed prompts.
    """
    nominal_tokens = simple_tokenize(nominal_prompt)
    perturbed_tokens = simple_tokenize(perturbed_prompt)

    matcher = difflib.SequenceMatcher(None, nominal_tokens, perturbed_tokens)
    return matcher.ratio()

def separate_prompt_sections(prompt: str) -> Dict[str, str]:
    """
    Separates a typical code generation prompt into structured components:
    (Docstring/Comment, Function Name, Code Part)

    The 'func_name' extraction targets the primary function defined in the prompt,
    which is the focus of the LLM completion task.
    
    NOTE: In the analyze_robustness function, the token length for 'func_name'
    is now overridden by the explicitly passed nominal_func_name and 
    perturbed_func_name strings. This function is still used to isolate 
    the 'comment' and 'code_part' for token counting.
    """
    sections = {
        'func_name': '',
        'docstring_comment': '',
        'code_part': '',
    }
    
    # 1. Isolate Comments/Docstrings
    comment_pattern = re.compile(
        r'(\/\*[\s\S]*?\*\/|\/\/.*|#.*|\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\")', 
        re.MULTILINE
    )
    comments = comment_pattern.findall(prompt)
    sections['docstring_comment'] = " ".join(comments).strip()
    
    # 2. Isolate Code Part (Everything that is NOT a comment)
    code_part = comment_pattern.sub('', prompt).strip()
    sections['code_part'] = code_part

    # 3. Isolate Function Name (for completeness, though overridden later)
    signature_match = re.search(
        r'(?:class\s+\w+\s*|public\s+|private\s+|static\s+|def\s*|function\s*)\s*(\w+)\s*\(.*?\)', 
        code_part, 
        re.IGNORECASE | re.DOTALL
    )

    if signature_match:
        sections['func_name'] = signature_match.group(1)
    
    return sections

def calculate_prompt_section_metrics(nominal_prompt: str, perturbed_prompt: str) -> Dict[str, Union[float, int]]:
    """
    Calculates initial metrics for comment, code_part, and total prompt length.
    Note: Function name tokens are handled directly in analyze_robustness using
    the provided nominal_func_name and perturbed_func_name arguments.
    """
    
    nominal_sections = separate_prompt_sections(nominal_prompt)
    perturbed_sections = separate_prompt_sections(perturbed_prompt)
    
    # Calculate token lengths for Nominal and Perturbed Prompts
    token_lengths_nominal = {
        'total': calculate_total_token_length(nominal_prompt),
        'comment': calculate_total_token_length(nominal_sections['docstring_comment']),
        'code_part': calculate_total_token_length(nominal_sections['code_part'])
    }
    
    token_lengths_perturbed = {
        'total': calculate_total_token_length(perturbed_prompt),
        'comment': calculate_total_token_length(perturbed_sections['docstring_comment']),
        'code_part': calculate_total_token_length(perturbed_sections['code_part'])
    }
    
    metrics = {}
    
    # Calculate Percentage Change for the 3 key sections (excluding func_name for now)
    for key in ['total', 'comment', 'code_part']:
        change = calculate_percentage_change(
            token_lengths_nominal[key],
            token_lengths_perturbed[key]
        )
        metrics[f"Prompt_Tokens_Nominal_{key}"] = token_lengths_nominal[key]
        metrics[f"Prompt_Tokens_Perturbed_{key}"] = token_lengths_perturbed[key]
        metrics[f"Prompt_Tokens_Pct_Change_{key}"] = round(change, 4)
        
    # Calculate core similarity metrics
    metrics["Prompt_Token_Similarity_Ratio"] = round(
        calculate_token_level_change(nominal_prompt, perturbed_prompt), 4
    )
    
    # TER (Tokenization Efficiency Ratio) - ratio of total lengths
    if token_lengths_nominal['total'] == 0:
        ter = 0.0 if token_lengths_perturbed['total'] == 0 else float('inf')
    else:
        ter = token_lengths_perturbed['total'] / token_lengths_nominal['total']
        
    metrics["Prompt_Length_Ratio (TER)"] = round(ter, 4)

    return metrics

# ----------------------------------------------------------------------
# AFTER GENERATION METRICS (Output Complexity and Structure)
# ----------------------------------------------------------------------

def calculate_cyclomatic_complexity(code: str, language: str = 'python') -> int:
    """
    Metric 2.1: Cyclomatic Complexity (CC) calculated ONLY by keyword counting.
    This provides a robust, language-agnostic metric across C++, Java, and JavaScript.
    CC is calculated as 1 + total decision points.
    
    Decision Points: if, for, while, else, elif, case, switch, try, catch, finally, &&, ||.
    """
    # Keywords that increase CC (preceded and followed by word boundaries \b)
    keywords = [
        r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\belse\b', r'\belif\b', 
        r'\bcase\b', r'\bswitch\b', r'\btry\b', r'\bcatch\b', r'\bfinally\b'
    ]
    # Boolean operators
    operators = [r'&&', r'\|\|']

    total_decision_points = 0
    
    # 1. Count keywords
    for keyword in keywords:
        total_decision_points += len(re.findall(keyword, code, re.IGNORECASE))

    # 2. Count operators
    for op in operators:
        total_decision_points += len(re.findall(op, code))
        
    return 1 + total_decision_points


def calculate_structural_similarity(nominal_code: str, perturbed_code: str) -> float:
    """
    Metric 2.3: Code-to-Code Structural Similarity (AST-Based Proxy)
    Measures the similarity of the generated code structures based on token sequences.
    """
    nominal_tokens = simple_tokenize(nominal_code)
    perturbed_tokens = simple_tokenize(perturbed_code)

    matcher = difflib.SequenceMatcher(None, nominal_tokens, perturbed_tokens)
    return matcher.ratio()


# ----------------------------------------------------------------------
# Main Analysis Function
# ----------------------------------------------------------------------

def analyze_robustness(
    nominal_prompt: str,
    perturbed_prompt: str,
    nominal_func_name: str,       # ADDED: Explicit nominal function name
    nominal_code: str,
    perturbed_code: str,
    perturbed_func_name: str,     # ADDED: Explicit perturbed function name
    language: str = 'python',
) -> Dict[str, Union[float, int, None]]:
    """
    Calculates and returns a dictionary of all robustness metrics, separating
    Input Shock and Output Structure metrics.
    """
    print(f"--- Analyzing Robustness for Language: {language.upper()} ---")

    # BEFORE GENERATION METRICS (Metric 1)
    # Calculate base metrics for total, comment, and code_part
    input_metrics = calculate_prompt_section_metrics(nominal_prompt, perturbed_prompt)
    
    # Override/Calculate function name token metrics using the provided names
    token_lengths_nominal_func_name = calculate_total_token_length(nominal_func_name)
    token_lengths_perturbed_func_name = calculate_total_token_length(perturbed_func_name)
    
    change_func_name = calculate_percentage_change(
        token_lengths_nominal_func_name,
        token_lengths_perturbed_func_name
    )

    input_metrics["Prompt_Tokens_Nominal_func_name"] = token_lengths_nominal_func_name
    input_metrics["Prompt_Tokens_Perturbed_func_name"] = token_lengths_perturbed_func_name
    input_metrics["Prompt_Tokens_Pct_Change_func_name"] = round(change_func_name, 4)

    # AFTER GENERATION METRICS (Metric 2 + Others)
    cc_nominal = calculate_cyclomatic_complexity(nominal_code, language)
    cc_perturbed = calculate_cyclomatic_complexity(perturbed_code, language)
    
    structural_similarity = calculate_structural_similarity(nominal_code, perturbed_code)
    
    code_tokens_nominal = calculate_total_token_length(nominal_code)
    code_tokens_perturbed = calculate_total_token_length(perturbed_code)

    # Summary of results
    output_metrics = {
        # Output Structure Metrics
        "Nominal_Code_CC": cc_nominal,
        "Perturbed_Code_CC": cc_perturbed,
        "CC_Difference": cc_nominal - cc_perturbed,
        
        "Nominal_Code_Total_Tokens": code_tokens_nominal,
        "Perturbed_Code_Total_Tokens": code_tokens_perturbed,
        "Code_Token_Length_Difference": code_tokens_perturbed - code_tokens_nominal,
        
        "Code_Structural_Similarity_Ratio": round(structural_similarity, 4),
    }
    
    # Combine all metrics
    metrics = {**input_metrics, **output_metrics}

    
    # Print analysis and findings
    print("\n[Type 1: BEFORE GENERATION (Input Analysis)]")
    print(f"  Similarity Ratio (1.0 is identical): {metrics['Prompt_Token_Similarity_Ratio']}")
    print(f"  Length Ratio (TER) (1.0 is stable): {metrics['Prompt_Length_Ratio (TER)']}")
    print("\n  --- Token Length Percentage Change (Perturbed vs. Nominal) ---")
    print(f"  Total Prompt Tokens Change: {metrics['Prompt_Tokens_Pct_Change_total']}%")
    # Display func_name metric using the explicitly passed names
    print(f"  Func Name Tokens Change:    {metrics['Prompt_Tokens_Pct_Change_func_name']}%")
    print(f"  Comment Tokens Change:      {metrics['Prompt_Tokens_Pct_Change_comment']}%")
    print(f"  Code Part Tokens Change:    {metrics['Prompt_Tokens_Pct_Change_code_part']}%")
    
    print("\n[Type 2: AFTER GENERATION (Output Structure)]")
    print(f"  Nominal Code CC: {metrics['Nominal_Code_CC']}")
    print(f"  Perturbed Code CC: {metrics['Perturbed_Code_CC']}")
    print(f"  CC Difference (Nominal - Perturbed): {metrics['CC_Difference']}")
    print("-" * 40)
    print(f"  Nominal Code Total Tokens: {metrics['Nominal_Code_Total_Tokens']}")
    print(f"  Perturbed Code Total Tokens: {metrics['Perturbed_Code_Total_Tokens']}")
    print(f"  Code Token Length Difference: {metrics['Code_Token_Length_Difference']}")
    print("-" * 40)
    print(f"  Code Structural Similarity Ratio (1.0 is identical): {metrics['Code_Structural_Similarity_Ratio']}")
    
    print(f"\n*CC Note: Cyclomatic Complexity is calculated using the Keyword Counting Proxy: 1 + (if + for + while + else + elif + case + switch + try + catch + finally + && + ||).*")
    
    return metrics


# ----------------------------------------------------------------------
# EXAMPLE USAGE
# ----------------------------------------------------------------------

if __name__ == '__main__':
    # --- EXAMPLE 1: C++ - High DocString Perturbation, Minimal Code Change ---
    print("="*70)
    print("EXAMPLE 1: C++ - Keyword CC Calculation")
    print("=====================================================================")
    
    cpp_nominal_prompt = """
/*
 * Calculate the factorial of a positive integer 'n'.
 */
int calculateFactorial(int n) { // Code Part starts here
    // Please implement the solution
"""
    # Perturbation: ONLY changes the docstring (comment part)
    cpp_perturbed_prompt = """
// Function that computes THE factorial of a GIVEN positive integer.
int calculateFactorial(int n) {
    // Please implement the solution
"""
    # Explicit function names (provided by user/experiment setup)
    cpp_nominal_func_name = "calculateFactorial"
    cpp_perturbed_func_name = "calculateFactorial" # Same in this example


    # Nominal Code: Recursive solution, CC=2 (1 base + 1 if)
    cpp_nominal_code = """
int calculateFactorial(int n) {
    if (n <= 1) { 
        return 1;
    }
    return n * calculateFactorial(n - 1);
}
    """
    # Perturbed Code: Model is robust and keeps the same logic, CC=3 (1 base + 2 if)
    cpp_perturbed_code = """
int calculateFactorial(int n) {
    if (n == 0) return 1;
    if (n < 0) return -1; 
    return n * calculateFactorial(n - 1);
}
    """
    
    analyze_robustness(
        cpp_nominal_prompt,
        cpp_perturbed_prompt,
        cpp_nominal_func_name,
        cpp_nominal_code,
        cpp_perturbed_code,
        cpp_perturbed_func_name,
        language='c++',
    )
    
    print("\n" + "="*70 + "\n")

    # --- EXAMPLE 2: JavaScript - Function Name Perturbation, Code Structural Failure ---
    print("="*70)
    print("EXAMPLE 2: JAVASCRIPT - Keyword CC Calculation")
    print("=====================================================================")
    
    js_nominal_prompt = "function mergeTwoSortedArrays(arr1, arr2) { // Returns a new merged sorted array."
    # Perturbation: Minor change to function name case
    js_perturbed_prompt = "function MergeTwoSortedArrays(arr1, arr2) { // Returns a new merged sorted array."
    
    # Explicit function names (provided by user/experiment setup)
    js_nominal_func_name = "mergeTwoSortedArrays"
    js_perturbed_func_name = "MergeTwoSortedArrays"

    # Nominal Code: Full merge logic, CC=5 (1 base + 2 while + 1 && + 1 if)
    js_nominal_code = """
function mergeTwoSortedArrays(arr1, arr2) {
    let merged = [];
    let i = 0, j = 0;
    while (i < arr1.length && j < arr2.length) { 
        if (arr1[i] < arr2[j]) { 
            merged.push(arr1[i++]);
        } else {
            merged.push(arr2[j++]);
        }
    }
    while (i < arr1.length) { 
        merged.push(arr1[i++]);
    }
    while (j < arr2.length) { 
        merged.push(arr2[j++]);
    }
    return merged;
}
    """
    # Perturbed Code: Model fails the merge logic, CC=1 (1 base)
    js_perturbed_code = """
function MergeTwoSortedArrays(arr1, arr2) {
    // Fails the logic due to perturbation, returns simple concatenation
    return arr1.concat(arr2).sort((a, b) => a - b);
}
    """
    
    analyze_robustness(
        js_nominal_prompt,
        js_perturbed_prompt,
        js_nominal_func_name,
        js_nominal_code,
        js_perturbed_code,
        js_perturbed_func_name,
        language='javascript'
    )
