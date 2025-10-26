import os
import re
import nltk
import Levenshtein
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from tree_sitter import Language, Parser

# ---------------- SETUP ---------------- #
import tree_sitter_cpp as tscpp
import tree_sitter_java as tsjava
import tree_sitter_javascript as tsjs

from radon.complexity import cc_visit
from radon.visitors import ComplexityVisitor

# Ensure required data
nltk.download("punkt", quiet=True)

# Load embedding model for semantic similarity
model_emb = SentenceTransformer("all-MiniLM-L6-v2")

# Tree-sitter setup
LANG_CPP = Language(tscpp.language())
LANG_JAVA = Language(tsjava.language())
LANG_JS = Language(tsjs.language())

PARSERS = {
    "cpp": LANG_CPP,
    "java": LANG_JAVA,
    "js": LANG_JS,
}

# ---------------- UTILITIES ---------------- #

def tokenize_code(code: str):
    """Basic code tokenizer."""
    code = re.sub(r"([^\w])", r" \1 ", code)
    return nltk.word_tokenize(code)

def jaccard_tokens(a, b):
    sa, sb = set(a), set(b)
    return len(sa & sb) / max(len(sa | sb), 1)

def levenshtein_norm(a, b):
    if not a and not b:
        return 0
    return Levenshtein.distance(a, b) / max(len(a), len(b), 1)

def identifier_extraction(code: str):
    """Extract variable/function identifiers."""
    return re.findall(r"\b[_a-zA-Z]\w*\b", code)

def identifier_rename_fraction(ids_nom, ids_pert):
    """Fraction of identifiers changed."""
    if not ids_nom:
        return 0
    changed = sum(1 for i in ids_nom if i not in ids_pert)
    return changed / len(ids_nom)

def token_length_change(code_nom, code_pert):
    """Relative token length change."""
    return (len(tokenize_code(code_pert)) - len(tokenize_code(code_nom))) / max(len(tokenize_code(code_nom)), 1)

def semantic_similarity(text1, text2):
    """Cosine similarity between embeddings."""
    emb1, emb2 = model_emb.encode([text1, text2], convert_to_tensor=True)
    
    # Move tensors to the CPU before using with NumPy
    emb1_cpu = emb1.cpu()
    emb2_cpu = emb2.cpu()

    sim = float(np.dot(emb1_cpu, emb2_cpu) / (np.linalg.norm(emb1_cpu) * np.linalg.norm(emb2_cpu)))
    return sim

def parse_with_treesitter(code: str, lang_key: str):
    """Count AST nodes using Tree-Sitter."""
    try:
        parser = Parser()
        parser.set_language(PARSERS[lang_key])
        tree = parser.parse(bytes(code, "utf8"))
        stack = [tree.root_node]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            stack.extend(node.children)
        return count
    except Exception:
        return np.nan

def ast_node_delta(code_nom, code_pert, lang_key: str):
    """Relative AST node count difference."""
    n_nom = parse_with_treesitter(code_nom, lang_key)
    n_pert = parse_with_treesitter(code_pert, lang_key)
    if np.isnan(n_nom) or np.isnan(n_pert):
        return np.nan
    return (n_pert - n_nom) / max(n_nom, 1)

def generation_similarity(gen_nom, gen_pert):
    tok_nom, tok_pert = tokenize_code(gen_nom), tokenize_code(gen_pert)
    return jaccard_tokens(tok_nom, tok_pert)

def identifier_preservation(ref, gen):
    """How many identifiers preserved from reference in generated code."""
    ids_ref, ids_gen = set(identifier_extraction(ref)), set(identifier_extraction(gen))
    if not ids_ref:
        return 0
    return len(ids_ref & ids_gen) / len(ids_ref)


def cyclomatic_complexity(code: str):
    """Compute average cyclomatic complexity of functions in code."""
    try:
        blocks = cc_visit(code)
        if not blocks:
            return 0
        return np.mean([b.complexity for b in blocks])
    except Exception:
        return np.nan



# ---------------- METRIC COMPUTATION ---------------- #

def compute_prompt_metrics(prompt_nom, prompt_pert):
    """
    Prompt-level metrics (safe for incomplete code)
    """
    tok_nom, tok_pert = tokenize_code(prompt_nom), tokenize_code(prompt_pert)
    token_change = 1 - jaccard_tokens(tok_nom, tok_pert)

    ids_nom, ids_pert = identifier_extraction(prompt_nom), identifier_extraction(prompt_pert)
    rename_frac = identifier_rename_fraction(ids_nom, ids_pert)

    len_change = token_length_change(prompt_nom, prompt_pert)
    sem_sim = semantic_similarity(prompt_nom, prompt_pert)
    sem_change = 1 - sem_sim

    # Skip AST or CC since prompts are incomplete
    return {
        "token_change": token_change,
        "rename_frac": rename_frac,
        "len_change_prompt": len_change,
        "sem_change": sem_change,
    }


def compute_generation_metrics(gen_nom, gen_pert, reference, lang_key):
    """
    Generation-level metrics (safe for full model outputs)
    """
    gen_sim = generation_similarity(gen_nom, gen_pert)
    gen_change = 1 - gen_sim

    id_preserve = identifier_preservation(reference, gen_pert) if reference else np.nan
    ast_delta_val = ast_node_delta(gen_nom, gen_pert, lang_key)

    # Complexity and length
    cc_nom, cc_pert = cyclomatic_complexity(gen_nom), cyclomatic_complexity(gen_pert)
    cc_delta = np.nan if np.isnan(cc_nom) or np.isnan(cc_pert) else (cc_pert - cc_nom) / max(cc_nom, 1)

    len_change_out = token_length_change(gen_nom, gen_pert)

    return {
        "gen_change": gen_change,
        "id_preserve": id_preserve,
        "ast_delta": ast_delta_val,
        "cc_delta_gen": cc_delta,
        "len_change_gen": len_change_out,
    }


def compute_metrics(sample):
    lang_key = sample["language"].lower()
    prompt_metrics = compute_prompt_metrics(sample["prompt_nom"], sample["prompt_pert"])
    gen_metrics = compute_generation_metrics(sample["gen_nom"], sample["gen_pert"], sample.get("reference", ""), lang_key)

    return {
        "language": sample["language"],
        "perturbation": sample["perturbation"],
        **prompt_metrics,
        **gen_metrics,
    }

# ---------------- EXAMPLE ---------------- #

if __name__ == "__main__":
    samples = [
        {
            "language": "java",
            "perturbation": "func_name",
            "prompt_nom": "int add(int a, int b",  # incomplete prompt
            "prompt_pert": "int sumValues(int a, int b",  # incomplete
            "gen_nom": "int add(int a, int b) { return a + b; }",
            "gen_pert": "int sumValues(int a, int b) { return a + b; }",
            "reference": "int add(int a, int b) { return a + b; }",
        },
        {
            "language": "cpp",
            "perturbation": "syntax",
            "prompt_nom": "int add(int a, int b",  # incomplete
            "prompt_pert": "int add(int a, int b) return a + b",
            "gen_nom": "int add(int a, int b) { return a + b; }",
            "gen_pert": "int add(int a, int b) { return a + b; }",
        },
    ]

    df = pd.DataFrame([compute_metrics(s) for s in samples])
    print(df.round(3))
