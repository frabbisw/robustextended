from tree_sitter import Language

# Build the shared library with three grammars
Language.build_library(
    'my-languages.so',
    [
        'tree-sitter-cpp',
        'tree-sitter-java',
        'tree-sitter-javascript'
    ]
)

print("✅ Successfully built my-languages.so with C++, Java, and JavaScript parsers.")
