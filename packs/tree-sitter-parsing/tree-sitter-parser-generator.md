---
title: "Tree-sitter (parser generator)"
source: https://en.wikipedia.org/wiki/Tree-sitter_(parser_generator)
domain: tree-sitter-parsing
license: CC-BY-SA-4.0
tags: tree-sitter parser, incremental parsing, concrete syntax tree, editor syntax parsing
fetched: 2026-07-02
---

# Tree-sitter (parser generator)

**Tree-sitter** is a free and open-source parser generator and incremental parsing library. It is used to parse source code into concrete syntax trees usable in compilers, interpreters, text editors, and static analyzers. It is specialized for use in text editors, as it supports incremental parsing for updating parse trees while code is edited in real time, and provides a built-in S-expression query system for analyzing code.

Text editors which have official integrations with Tree-sitter include GNU Emacs, Neovim, Lapce, Zed, Helix, and Atom. Language bindings allow it to be used from programming languages including Go, Haskell, Java, JavaScript (with Node.js and WASM), Kotlin, Lua, OCaml, Perl, Python, Ruby, Rust, Swift, and Zig. Tree-sitter parsers have been written for these languages and many others. GitHub uses Tree-sitter to support in-browser symbolic code navigation in Git repositories.

Tree-sitter uses a GLR parser, a type of LR parser.

Tree-sitter was originally developed by GitHub for use in the Atom text editor, where it was first released in 2018.
