---
title: "ReScript"
source: https://en.wikipedia.org/wiki/ReScript
domain: rescript-lang
license: CC-BY-SA-4.0
tags: rescript language, ocaml language, javascript language, type inference, source to source compiler
fetched: 2026-07-02
---

# ReScript

**ReScript** is a high-level programming language that transpiles to JavaScript. Its syntax is descended from the Reason programming language, which is an alternate syntax for OCaml.

## Language characteristics

ReScript shares characteristics with its ancestors Reason and OCaml. It is a statically typed language with a sound type system, and it emphasizes functional programming.

However, ReScript’s syntax has started to evolve away from OCaml and closer to JavaScript. For example, it uses the same arithmetic operators for integers and floating point numbers (like JavaScript), while OCaml and Reason use separate operators.

Since ReScript transpiles to JavaScript, it can access the entire JavaScript ecosystem. It can both call JavaScript functions and have its functions called from JavaScript. It has direct language support for the React front-end web library, including JSX.

## History

ReScript traces its roots back to **BuckleScript**, a compiler that compiled OCaml to JavaScript, which was first released in 2016 by Bloomberg L.P. In the same year, the Reason programming language was released, which was an alternate syntax for OCaml that was more similar to JavaScript. As both projects were influenced by JavaScript, Reason and BuckleScript soon became an integrated toolchain.

However, the BuckleScript team and the Reason team had different priorities. The Reason team wanted to maintain compatibility with the OCaml ecosystem, while the BuckleScript team wanted to be able to change the syntax to give the best developer experience to JavaScript programmers.

In 2020, BuckleScript introduced a new syntax that started to diverge from Reason. A month later, the BuckleScript team rebranded its toolchain to ReScript, to focus solely on the JavaScript ecosystem and essentially becoming its own language, distinct from Reason. ReScript’s support for compiling OCaml ended with version 12, released in 2025.
