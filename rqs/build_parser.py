import os
from tree_sitter import Language

# Force modern C++ standard for the compilation
os.environ["CFLAGS"] = "-std=c++17"

Language.build_library(
    # Output path
    "my-languages.so",
    # List of language grammars
    [
        "tree-sitter-cpp",
        "tree-sitter-java",
        "tree-sitter-javascript"
    ]
)

print("✅ Successfully rebuilt my-languages.so using C++17 standard.")
