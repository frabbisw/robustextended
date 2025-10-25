import os
import re
import ast
import nltk
import Levenshtein
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from tree_sitter import Language, Parser
from tiktoken import get_encoding

# ---------------- SETUP ---------------- #
# Ensure NLTK data
nltk.download("punkt", quiet=True)

# Sentence-BERT model for semantic similarity
model_emb = SentenceTransformer("all-MiniLM-L6-v2")

# ---- Build or load Tree-Sitter multi-language library ---- #
# Create once: my-languages.so with Java, C++, JS grammars
if not os.path.exists("my-languages.so"):
    Language.build_library(
        "my-languages.so",
        [
            "tree-sitter-cpp",
            "tree-sitter-java",
            "tree-sitter-javascript",
        ],
    )

LIB_PATH = os.path.join(os.path.dirname(__file__), "my-languages.so")

LANG_CPP = Language(LIB_PATH, "cpp")
LANG_JAVA = Language(LIB_PATH, "java")
LANG_JS = Language(LIB_PATH, "javascript")

PARSERS = {"cpp": LANG_CPP, "java": LANG_JAVA, "js": LANG_JS}

# ---------------- UTILITIES ---------------- #

def tokenize_code(code: str):
    """Simple tokenizer for code."""
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
    return re.findall(r"\b[_a-zA-Z]\w*\b", code)

def identifier_rename_fraction(ids_nom, ids_pert):
    if not ids_nom:
        return 0
    changed = sum(1 for i in ids_nom if i not in ids_pert)
    return changed / len(ids_nom)

def token_length_change(code_nom, code_pert):
    return (len(tokenize_code(code_pert)) - len(tokenize_code(code_nom))) / max(len(tokenize_code(code_nom)), 1)

def semantic_similarity(text1, text2):
    emb1, emb2 = model_emb.encode([text1, text2], convert_to_tensor=True)
    sim = float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))
    return sim

def parse_with_treesitter(code: str, lang_key: str):
    """Count AST nodes using Tree-Sitter."""
    try:
        parser = Parser()
        parser.set_language(PARSERS[lang_key])
        tree = parser.parse(bytes(code, "utf8"))
        # Count all nodes recursively
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
    n_nom = parse_with_treesitter(code_nom, lang_key)
    n_pert = parse_with_treesitter(code_pert, lang_key)
    if np.isnan(n_nom) or np.isnan(n_pert):
        return np.nan
    return (n_pert - n_nom) / max(n_nom, 1)

def generation_similarity(gen_nom, gen_pert):
    tok_nom, tok_pert = tokenize_code(gen_nom), tokenize_code(gen_pert)
    return jaccard_tokens(tok_nom, tok_pert)

def identifier_preservation(ref, gen):
    ids_ref, ids_gen = set(identifier_extraction(ref)), set(identifier_extraction(gen))
    if not ids_ref:
        return 0
    return len(ids_ref & ids_gen) / len(ids_ref)

# ---------------- MAIN METRIC FUNCTION ---------------- #

def compute_metrics(sample):
    """
    sample = {
        "language": "java" | "cpp" | "js",
        "perturbation": "func_name",
        "prompt_nom": "...",
        "prompt_pert": "...",
        "gen_nom": "...",
        "gen_pert": "...",
        "reference": "..."  # optional
    }
    """
    lang_key = sample["language"].lower()
    prompt_nom, prompt_pert = sample["prompt_nom"], sample["prompt_pert"]
    gen_nom, gen_pert = sample["gen_nom"], sample["gen_pert"]
    reference = sample.get("reference", "")

    # Token + identifier metrics
    tok_nom, tok_pert = tokenize_code(prompt_nom), tokenize_code(prompt_pert)
    token_change = 1 - jaccard_tokens(tok_nom, tok_pert)
    ids_nom, ids_pert = identifier_extraction(prompt_nom), identifier_extraction(prompt_pert)
    rename_frac = identifier_rename_fraction(ids_nom, ids_pert)
    len_change = token_length_change(prompt_nom, prompt_pert)
    sem_sim = semantic_similarity(prompt_nom, prompt_pert)
    sem_change = 1 - sem_sim

    # Generated code metrics
    gen_sim = generation_similarity(gen_nom, gen_pert)
    gen_change = 1 - gen_sim
    id_preserve = identifier_preservation(reference, gen_pert) if reference else np.nan
    ast_delta_val = ast_node_delta(gen_nom, gen_pert, lang_key)

    return {
        "language": sample["language"],
        "perturbation": sample["perturbation"],
        "token_change": token_change,
        "rename_frac": rename_frac,
        "len_change": len_change,
        "sem_change": sem_change,
        "gen_change": gen_change,
        "id_preserve": id_preserve,
        "ast_delta": ast_delta_val,
    }

# ---------------- EXAMPLE ---------------- #

if __name__ == "__main__":
    samples = [
        {
            "language": "java",
            "perturbation": "func_name",
            "prompt_nom": "int add(int a, int b) { return a + b; }",
            "prompt_pert": "int sumValues(int a, int b) { return a + b; }",
            "gen_nom": "int add(int a, int b) { return a + b; }",
            "gen_pert": "int sumValues(int a, int b) { return a + b; }",
            "reference": "int add(int a, int b) { return a + b; }",
        },
        {
            "language": "cpp",
            "perturbation": "syntax",
            "prompt_nom": "int add(int a, int b) { return a + b; }",
            "prompt_pert": "int add(int a, int b) return a + b;",
            "gen_nom": "int add(int a, int b) { return a + b; }",
            "gen_pert": "int add(int a, int b) { return a + b; }",
        },
    ]

    df = pd.DataFrame([compute_metrics(s) for s in samples])
    print(df.round(3))
    # df.to_csv("robustness_error_metrics_treesitter.csv", index=False)
    # print("Saved → robustness_error_metrics_treesitter.csv")
