---
title: "BEAM (Erlang virtual machine)"
source: https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)
domain: gleam-lang
license: CC-BY-SA-4.0
tags: gleam language, gleam lang, gleam beam
fetched: 2026-07-02
---

# BEAM (Erlang virtual machine)

**BEAM** is the virtual machine at the core of the Erlang Open Telecom Platform (OTP). BEAM is part of the Erlang Run-Time System (ERTS), which compiles Erlang source code into bytecode, which is then executed on the BEAM. BEAM bytecode files have the `.beam` file extension. BEAM was written in the C language.

Originally BEAM was short for *Bogdan's Erlang Abstract Machine*, named after Bogumil "Bogdan" Hausman, who wrote the original version, but the name may also be referred to as *Björn's Erlang Abstract Machine*, after Björn Gustavsson, who wrote and maintains the current version. Both developers worked on the system while at Ericsson.

The predecessor of the BEAM was JAM (Joe's Abstract Machine), which was the first virtual machine for the Erlang language and was written by Joe Armstrong and Mike Williams in the C language as well.

## BEAM languages

Although BEAM was created for Erlang, several other languages have been either created for it or ported to run on it. The most popular of these is Elixir, which had more responses than Erlang itself in a 2023 Stack Overflow developer survey. Other notable examples include:

- Clojerl, a port of Clojure to BEAM
- Cuneiform, a language for large-scale scientific data analysis
- Gleam, a statically typed functional language for BEAM
- LFE, Lisp Flavored Erlang, a lisp frontend for the Erlang compiler
- Luerl, Lua on the BEAM, designed and implemented by one of the creators of Erlang
