import re
import difflib
from typing import List, Dict, Union

# NOTE ON EXTERNAL DEPENDENCIES:
# This script relies on the 'radon' library for Cyclomatic Complexity, which you will
# need to install if you plan to use this metric on your generated code.
# Installation: pip install radon

try:
    from radon.complexity import cc_visit, cc_rank
    RADON_AVAILABLE = True
except ImportError:
    # If radon is not available, Cyclomatic Complexity calculation will be skipped.
    RADON_AVAILABLE = False
    print("Warning: 'radon' library not found. Cyclomatic Complexity will be skipped.")


# ----------------------------------------------------------------------
# Helper Function for Tokenization (Simplified Model Tokenizer Proxy)
# ----------------------------------------------------------------------
def simple_tokenize(code_or_prompt: str) -> List[str]:
    """
    Splits the string into tokens using whitespace and common symbols as delimiters.
    This serves as a proxy for the LLM's full tokenization process.
    """
    # Replace common structural symbols with spaces for token separation, then split by whitespace
    # This ensures symbols like '{', '(', ';', are treated as individual tokens.
    text = re.sub(r'([{}()\[\].,;:\'\"=\+\-\*/&|!<>])', r' \1 ', code_or_prompt)
    tokens = text.split()
    return tokens


# ----------------------------------------------------------------------
# BEFORE GENERATION METRICS (Type 1: Input Shock)
# ----------------------------------------------------------------------

def calculate_token_level_change(nominal_prompt: str, perturbed_prompt: str) -> float:
    """
    Metric 1: Token-level Change Ratio (1.0 = identical, 0.0 = completely different)
    Measures the similarity between the nominal and perturbed prompts using
    the Ratcliff-Obershelp similarity algorithm (via difflib).
    """
    nominal_tokens = simple_tokenize(nominal_prompt)
    perturbed_tokens = simple_tokenize(perturbed_prompt)

    # SequenceMatcher is ideal for calculating similarity ratios between sequences
    matcher = difflib.SequenceMatcher(None, nominal_tokens, perturbed_tokens)
    return matcher.ratio()

def calculate_prompt_length_ratio(nominal_prompt: str, perturbed_prompt: str) -> float:
    """
    Metric (Suggested Complement): Tokenization Efficiency Ratio (TER)
    Measures the ratio of token lengths. TER close to 1.0 indicates stable tokenization.
    A high TER (e.g., 1.5) might indicate 'token explosion' due to the perturbation.
    """
    nominal_tokens = simple_tokenize(nominal_prompt)
    perturbed_tokens = simple_tokenize(perturbed_prompt)

    if len(nominal_tokens) == 0:
        return 0.0
    return len(perturbed_tokens) / len(nominal_tokens)


# ----------------------------------------------------------------------
# AFTER GENERATION METRICS (Type 2: Output Complexity and Structure)
# ----------------------------------------------------------------------

def calculate_keyword_complexity(code: str) -> int:
    """
    Proxy Metric for Cyclomatic Complexity: Counts decision-making keywords.
    This method is highly robust and works on non-compilable code.
    
    Decision points include: if, for, while, else if, elif, switch, case, 
    && (AND), || (OR), try, catch, finally, return (if not the last statement).
    
    For simplicity, we count common branching/looping structures and boolean operators.
    """
    # List of keywords that increase CC (preceded and followed by word boundaries \b)
    keywords = [
        r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\belse\b', r'\belif\b', 
        r'\bcase\b', r'\bswitch\b', r'\btry\b', r'\bcatch\b', r'\bfinally\b'
    ]
    # Boolean operators (often used for short-circuiting logic in if/while)
    operators = [r'&&', r'\|\|']

    total_decision_points = 0
    
    # 1. Count keywords
    for keyword in keywords:
        # re.IGNORECASE makes this work across Python, Java, JS, etc.
        total_decision_points += len(re.findall(keyword, code, re.IGNORECASE))

    # 2. Count operators
    for op in operators:
        total_decision_points += len(re.findall(op, code))
        
    # CC is typically defined as 1 + total decision points.
    return 1 + total_decision_points


def calculate_cyclomatic_complexity(code: str, language: str = 'python') -> Union[int, None]:
    """
    Metric 2: Cyclomatic Complexity (CC)
    Measures the complexity of the control flow graph.
    - Uses 'radon' for Python if possible (more accurate).
    - Uses keyword counting for other languages or non-parseable Python code (more robust).
    """
    
    if language.lower() == 'python' and RADON_AVAILABLE:
        try:
            # Try to use radon for accurate CC, which requires successful AST parsing.
            results = cc_visit(code)
            total_cc = sum(r.complexity for r in results)
            return total_cc
            
        except Exception as e:
            # If Python code is non-compilable (SyntaxError), fall back to keyword counting.
            print(f"  CC Error: Python code unparseable by radon ({e.__class__.__name__}). Falling back to keyword counting.")
            return calculate_keyword_complexity(code)
    
    elif language.lower() in ['java', 'c++', 'javascript', 'js', 'cpp']:
        # Use the highly robust keyword counting proxy for non-Python languages.
        return calculate_keyword_complexity(code)

    return None # Return None if radon is not installed and language is not supported for proxy CC.

def calculate_structural_similarity(nominal_code: str, perturbed_code: str) -> float:
    """
    Metric 3: Code-to-Code Structural Similarity (AST-Based Proxy)
    Measures the similarity of the generated code structures by tokenizing the code
    and calculating the similarity ratio of the token sequences.
    (This serves as a proxy for true AST Delta without needing tree-sitter).
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
    nominal_code: str,
    perturbed_code: str,
    language: str = 'python'
) -> Dict[str, Union[float, int, None]]:
    """
    Calculates and returns a dictionary of all robustness metrics.
    """
    print(f"--- Analyzing Robustness for Language: {language.upper()} ---")

    # BEFORE GENERATION METRICS
    token_change = calculate_token_level_change(nominal_prompt, perturbed_prompt)
    length_ratio = calculate_prompt_length_ratio(nominal_prompt, perturbed_prompt)

    # AFTER GENERATION METRICS
    cc_nominal = calculate_cyclomatic_complexity(nominal_code, language)
    cc_perturbed = calculate_cyclomatic_complexity(perturbed_code, language)
    
    structural_similarity = calculate_structural_similarity(nominal_code, perturbed_code)

    # Summary of results
    metrics = {
        # Input Shock Metrics
        "Prompt_Token_Similarity_Ratio": round(token_change, 4),
        "Prompt_Length_Ratio (TER)": round(length_ratio, 4),

        # Output Structure Metrics
        "Nominal_Code_CC": cc_nominal,
        "Perturbed_Code_CC": cc_perturbed,
        "Code_Structural_Similarity_Ratio": round(structural_similarity, 4),
        "CC_Difference": cc_nominal - cc_perturbed if (cc_nominal is not None and cc_perturbed is not None) else None
    }
    
    # Print analysis and findings
    print("\n[Type 1: BEFORE GENERATION (Input Shock)]")
    print(f"  Prompt Token Similarity Ratio (1.0 is identical): {metrics['Prompt_Token_Similarity_Ratio']}")
    print(f"  Prompt Length Ratio (TER) (1.0 is stable): {metrics['Prompt_Length_Ratio (TER)']}")
    
    print("\n[Type 2: AFTER GENERATION (Output Structure)]")
    print(f"  Nominal Code Cyclomatic Complexity (CC): {metrics['Nominal_Code_CC']} (Proxy/Radon)")
    print(f"  Perturbed Code Cyclomatic Complexity (CC): {metrics['Perturbed_Code_CC']} (Proxy/Radon)")
    print(f"  CC Difference (Nominal - Perturbed): {metrics['CC_Difference']}")
    print(f"  Code Structural Similarity Ratio (1.0 is identical): {metrics['Code_Structural_Similarity_Ratio']}")
    
    if language.lower() in ['java', 'c++', 'javascript', 'js', 'cpp']:
         print(f"\n*CC Note: Cyclomatic Complexity for {language.upper()} is calculated using the robust keyword counting proxy (1 + decision points).*")
    elif language.lower() == 'python':
        print(f"\n*CC Note: Python CC uses radon (or keyword proxy on failure).*")
    
    return metrics


# ----------------------------------------------------------------------
# EXAMPLE USAGE
# ----------------------------------------------------------------------

if __name__ == '__main__':
    # --- EXAMPLE 1: Python - Brittle Failure (High Change, High CC Drop) ---
    print("=====================================================================")
    print("EXAMPLE 1: PYTHON - Total Failure (Non-compilable code falls back to proxy)")
    print("=====================================================================")
    
    python_nominal_prompt = "def find_max_element(input_list): Given a list of integers, find and return the maximum value in the list. Use a loop."
    python_perturbed_prompt = "def FIND_MAX_ELEMENT(input_LIST): Given a list of integers, find and rettrn the maximum value in the list. Use a loop"

    python_nominal_code = """
def find_max_element(input_list): # CC should be 3 (1 + 1 for for + 1 for if)
    max_val = input_list[0]
    for x in input_list:
        if x > max_val:
            max_val = x
    return max_val
    """
    # Perturbed Code with SYNTAX ERROR (Missing colon in 'if')
    python_perturbed_code = """
def FIND_MAX_ELEMENT(input_LIST):
    max_val = input_LIST[0]
    for x in input_LIST:
        if x > max_val # <--- SYNTAX ERROR HERE
            max_val = x
    return max_val
    """
    
    # Note: If radon is installed, nominal CC is accurate (3). Perturbed CC falls back to proxy (3) or fails entirely.
    analyze_robustness(
        python_nominal_prompt,
        python_perturbed_prompt,
        python_nominal_code,
        python_perturbed_code,
        language='python'
    )
    
    print("\n" + "="*70 + "\n")

    # --- EXAMPLE 2: JAVASCRIPT - Using Keyword Counting Proxy ---
    print("=====================================================================")
    print("EXAMPLE 2: JAVASCRIPT - Robust Success (Using Keyword Proxy)")
    print("=====================================================================")

    js_nominal_prompt = "// function calculateSum(arr): returns the sum of all elements in the array. Use reduce."
    js_perturbed_prompt = "// func CalculateSum(arr): returns the sum of all elements in the array. Use reduce."

    js_nominal_code = """
// CC should be 1 (no if/for/while)
function calculateSum(arr) {
  // Check for null or empty array (if is 1 decision point)
  if (!arr || arr.length === 0) { 
    return 0; 
  }
  return arr.reduce((acc, current) => acc + current, 0);
}
    """
    # Perturbed Code: Still structurally similar, maintains logic
    js_perturbed_code = """
function CalculateSum(arr) {
  // Check for null or empty array (if is 1 decision point)
  if (!arr || arr.length === 0) { // || is an additional decision point
    return 0; 
  }
  return arr.reduce((acc, current) => {
    return acc + current;
  }, 0);
}
    """
    
    # Nominal Proxy CC: 1 (base) + 1 (if) + 1 (||) = 3
    # Perturbed Proxy CC: 1 (base) + 1 (if) + 1 (||) = 3
    analyze_robustness(
        js_nominal_prompt,
        js_perturbed_prompt,
        js_nominal_code,
        js_perturbed_code,
        language='javascript'
    )
    
    print("\n" + "="*70 + "\n")
    
    # --- EXAMPLE 3: C++ - Using Keyword Counting Proxy with Fail ---
    print("=====================================================================")
    print("EXAMPLE 3: C++ - Structural Failure (Using Keyword Proxy)")
    print("=====================================================================")
    
    cpp_nominal_prompt = "// function factorial(n): calculate the factorial of an integer n using recursion."
    cpp_perturbed_prompt = "// FUNCTION factorial(n): calculate the FACTORIAL of an integer n using recursion."

    cpp_nominal_code = """
// CC should be 2 (1 + 1 for if)
int factorial(int n) {
    if (n <= 1) { // 1 decision point
        return 1;
    }
    return n * factorial(n - 1);
}
    """
    # Perturbed Code: Iterative solution (Structural Change)
    cpp_perturbed_code = """
// CC should be 2 (1 + 1 for for)
int factorial(int n) {
    int res = 1;
    for (int i = 2; i <= n; i++) { // 1 decision point
        res = res * i;
    }
    return res;
}
    """
    
    # Nominal Proxy CC: 1 (base) + 1 (if) = 2
    # Perturbed Proxy CC: 1 (base) + 1 (for) = 2
    analyze_robustness(
        cpp_nominal_prompt,
        cpp_perturbed_prompt,
        cpp_nominal_code,
        cpp_perturbed_code,
        language='c++'
    )
