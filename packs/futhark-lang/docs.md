---
title: "Docs"
source: https://futhark-lang.org/docs.html
domain: futhark-lang
license: CC-BY-SA-4.0
tags: futhark language, futhark lang, futhark gpu
fetched: 2026-07-02
---

# Docs

The Futhark documentation is divided into several parts. The in-progress book Parallel Programming in Futhark can be read freely online, and is the starting point for learning Futhark. The Futhark User's Guide contains detailed instructions on how to use the compilers, as well as the language reference and instructions on how to install the Futhark compiler.

There is also automatically generated documentation for the Futhark prelude. The prelude library is very small, so in most cases you will want to use external packages.

If there is something you believe should be documented, but is not, you are very welcome to report the omission as a bug on our bug tracker. See the page Get Involved for more information.

## Bridges

The Futhark compiler can generate C or Python code. A bridge allows programs written in other languages to conveniently call this code.

- **Haskell**: Futhask
- **J**: Futhark-J Bridge
- **Python**: futhark-pycffi (or the compiler's builtin Python backend, which is slower but more convenient)
- **Rust**: genfut, futhark-bindgen, cargo-futhark
- **Standard ML**: futhark-server-sml, smlfut
- **OCaml**: futhark-bindgen

## Tools

- Futhark support for Sublime Text 3
- futhark-mode for Emacs
- Syntax highlighting for Vim
- Language Extension for VS Code
- Futhark language definition for Gedit (place the linked file in `~/.local/share/gtksourceview-3.0/language-specs/`)
- Property-based testing for Futhark

## Syntax highlighters that support Futhark

- Linguist (through language-etc).
- Pygments
- Kate Highlighting XML, compatible with Skylighting which is used by Pandoc.
- LaTeX `listings`
