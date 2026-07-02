---
title: "ANTLR"
source: https://www.antlr.org/
domain: antlr-parser
license: CC-BY-SA-4.0
tags: antlr parser generator, ll star parsing, grammar parser generator, recursive descent parsing
fetched: 2026-07-02
---

## What is ANTLR?

**ANTLR** (ANother Tool for Language Recognition) is a powerful parser generator for reading, processing, executing, or translating structured text or binary files. It's widely used to build languages, tools, and frameworks. From a grammar, ANTLR generates a parser that can build and walk parse trees.

Terence Parr

is a tech lead at Google and until 2022 was a professor of data science / computer science at Univ. of San Francisco. He is the maniac behind ANTLR and has been working on language tools since 1989.

Check out Terence impersonating a machine learning droid:

explained.ai

Quick Start

To try ANTLR immediately, jump to the

new

ANTLR Lab

!

To install locally, use

antlr4-tools

, which installs Java and ANTLR if needed and creates

antlr4

and

antlr4-parse

executables:

```
$ pip install antlr4-tools
```

(Windows must add

..\LocalCache\local-packages\Python310\Scripts

to the

PATH

). See the

Getting Started

doc. Paste the following grammar into file

Expr.g4

and, from that directory, run the

antlr4-parse

command. Hit control-D on Unix (or control-Z on Windows) to indicate end-of-input. A window showing the parse tree will appear.

| grammar Expr; prog: (expr NEWLINE)* ; expr: expr ('*'\|'/') expr \| expr ('+'\|'-') expr \| INT \| '(' expr ')' ; NEWLINE : [\r\n]+ ; INT : [0-9]+ ; | $ antlr4-parse Expr.g4 prog -gui 10+20*30 *^D* $ antlr4 Expr.g4 # gen code $ ls ExprParser.java ExprParser.java | (sample3) |
|---|---|---|
