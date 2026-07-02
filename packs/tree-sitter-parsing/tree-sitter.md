---
title: "Introduction"
source: https://tree-sitter.github.io/tree-sitter/
domain: tree-sitter-parsing
license: CC-BY-SA-4.0
tags: tree-sitter parser, incremental parsing, concrete syntax tree, editor syntax parsing
fetched: 2026-07-02
---

# Introduction

Tree-sitter is a parser generator tool and an incremental parsing library. It can build a concrete syntax tree for a source file and efficiently update the syntax tree as the source file is edited. Tree-sitter aims to be:

- **General** enough to parse any programming language
- **Fast** enough to parse on every keystroke in a text editor
- **Robust** enough to provide useful results even in the presence of syntax errors
- **Dependency-free** so that the runtime library (which is written in pure C11) can be embedded in any application

## Language Bindings

There are bindings that allow Tree-sitter to be used from the following languages:

### Official

- C#
- Go
- Haskell
- Java (JDK 22+)
- JavaScript (Node.js)
- JavaScript (Wasm)
- Kotlin
- Python
- Rust
- Swift
- Zig

### Third-party

- C# (.NET)
- C++
- Crystal
- D
- Delphi
- ELisp
- Go
- Guile
- Janet
- Java (JDK 8+)
- Java (JDK 11+)
- Julia
- Lua
- Lua
- OCaml
- Odin
- Perl
- Pharo
- PHP
- R
- Ruby

*Keep in mind that some of the bindings may be incomplete or out of date.*

## Parsers

The following parsers can be found in the upstream organization:

- Agda
- Bash
- C
- C++
- C#
- CSS
- ERB / EJS
- Go
- Haskell
- HTML
- Java
- JavaScript
- JSDoc
- JSON
- Julia
- OCaml
- PHP
- Python
- Regex
- Ruby
- Rust
- Scala
- TypeScript
- Verilog

A list of known parsers can be found in the wiki.

## Talks on Tree-sitter

- Strange Loop 2018
- FOSDEM 2018
- GitHub Universe 2017

## Underlying Research

The design of Tree-sitter was greatly influenced by the following research papers:

- Practical Algorithms for Incremental Software Development Environments
- Context Aware Scanning for Parsing Extensible Languages
- Efficient and Flexible Incremental Parsing
- Incremental Analysis of Real Programming Languages
- Error Detection and Recovery in LR Parsers
- Error Recovery for LR Parsers
