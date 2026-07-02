---
title: "Hy (programming language)"
source: https://en.wikipedia.org/wiki/Hy_(programming_language)
domain: hy-lisp
license: CC-BY-SA-4.0
tags: hy language, lisp language, python language, abstract syntax tree, macro computer science
fetched: 2026-07-02
---

# Hy (programming language)

**Hy** is a dialect of the Lisp programming language designed to interact with Python by translating s-expressions into Python's abstract syntax tree (AST). Hy was introduced at Python Conference (PyCon) 2013 by Paul Tagliamonte. Lisp allows operating on code as data (metaprogramming), thus Hy can be used to write domain-specific languages.

Similar to Kawa's and Clojure's mappings onto the Java virtual machine (JVM), Hy is meant to operate as a transparent Lisp front-end for Python. It allows Python libraries, including the standard library, to be imported and accessed alongside Hy code with a compiling step where both languages are converted into Python's AST.

## Example code

From the language documentation:

```mw
=> (print "Hy!")
Hy!
=> (defn salutationsnm [name] (print (+ "Hy " name "!")))
=> (salutationsnm "YourName")
Hy YourName!
```
