from tree_sitter import Language, Parser

Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    './tree-sitter-python', './tree-sitter-cpp', './tree-sitter-go', './tree-sitter-javascript', './tree-sitter-java'
  ]
)

PY_LANGUAGE = Language('build/my-languages.so', 'python')
JAVA_LANGUAGE = Language('build/my-languages.so', 'java')
CPP_LANGUAGE = Language('build/my-languages.so', 'javascript')
GO_LANGUAGE = Language('build/my-languages.so', 'go')
JS_LANGUAGE = Language('build/my-languages.so', 'cpp')
