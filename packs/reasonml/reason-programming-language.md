---
title: "Reason (programming language)"
source: https://en.wikipedia.org/wiki/Reason_(programming_language)
domain: reasonml
license: CC-BY-SA-4.0
tags: reasonml language, reason language, ocaml language, javascript language, source to source compiler
fetched: 2026-07-02
---

# Reason (programming language)

**Reason**, also known as **ReasonML**, is a programming language and toolchain that is part of the OCaml programming language ecosystem. Reason uses many syntax elements from JavaScript, compiles to native code using OCaml's compiler toolchain, and can compile to JavaScript using the **Melange** compiler.

## Language characteristics

Since Reason is an alternate syntax to OCaml, they share the same characteristics. Both languages are general-purpose, functional and object-oriented.

While Reason compiles down to native code via OCaml's toolchain, it specifically differs in its syntax, error messaging, and editor tooling. This allows Reason to provide an experience more similar to JavaScript or TypeScript for developers.

Reason’s syntax is more similar to JavaScript and other C-style languages than to OCaml. For example, Reason tends to use curly braces to delimit blocks and semicolons for separating statements, while OCaml primarily uses parentheses or `begin`/`end` keywords to delimit blocks, with nothing separating declarations. Reason also defines functions via an arrow-like syntax (rather than OCaml's `fun` keyword), and calling a function requires parentheses around its arguments. Other notable differences include naming the pattern matching keyword `switch` (instead of `match`), and reformatting error messages to be more familiar to JavaScript programmers.

The Reason community officially provides ReasonReact as a solution for web applications based on the React framework.

## Example

```mw
type schoolPerson = Teacher | Director | Student(string);

let greeting = person =>
  switch (person) {
  | Teacher => "Hey Professor!"
  | Director => "Hello Director."
  | Student("Richard") => "Still here Ricky?"
  | Student(anyOtherName) => "Hey, " ++ anyOtherName ++ "."
  };
```

## History

Jordan Walke, creator of the React web framework, first released Reason in 2016 while employed at Facebook.

In the same year, Bloomberg L.P. introduced BuckleScript, a compiler which compiled OCaml to JavaScript. As both projects were influenced by JavaScript, Reason and BuckleScript soon became an integrated toolchain, allowing Reason to target JavaScript.

However, the Reason team and the BuckleScript team had different priorities. The Reason team wanted to maintain compatibility with the OCaml ecosystem, while the BuckleScript team wanted to be able to change the syntax to give the best developer experience to JavaScript programmers.

In 2020, BuckleScript introduced a new syntax that started to diverge from Reason. A month later, the BuckleScript team rebranded its toolchain to ReScript, to focus solely on the JavaScript ecosystem and essentially becoming its own language, distinct from Reason.

To maintain the ability for Reason to target JavaScript, António Monteiro forked a version of BuckleScript before it was rebranded as ReScript, and changed it to bring it closer to the OCaml ecosystem. The fork, named Melange, released its first stable version in 2023.
