from tree_sitter import Language

Language.build_library(
  'my-languages.so',  # Output file
  [
    'tree-sitter-cpp',
    'tree-sitter-java',
    'tree-sitter-javascript'
  ]
)
