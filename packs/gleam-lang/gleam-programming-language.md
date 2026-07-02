---
title: "Gleam (programming language)"
source: https://en.wikipedia.org/wiki/Gleam_(programming_language)
domain: gleam-lang
license: CC-BY-SA-4.0
tags: gleam language, gleam lang, gleam beam
fetched: 2026-07-02
---

# Gleam (programming language)

**Gleam** is a general-purpose, concurrent, functional, high-level programming language that compiles to Erlang or JavaScript source code.

Gleam is a statically-typed language, which is different from the most popular languages that run on Erlang’s virtual machine BEAM, Erlang and Elixir. Gleam has its own type-safe implementation of OTP, Erlang's actor framework. Packages are provided using the Hex package manager, and an index for finding packages written for Gleam is available.

## History

Gleam was originally created in 2016 by Louis Pilfold for a conference talk. It was later redesigned and adapted into what it is today.

The first numbered version of Gleam was released on April 15, 2019. Compiling to JavaScript was introduced with version v0.16.

In 2023 the Erlang Ecosystem Foundation funded the creation of a course for learning Gleam on the learning platform Exercism.

Version v1.0.0 was released on March 4, 2024.

In April 2025, Thoughtworks added Gleam to its Technology Radar in the Assess ring (languages & frameworks worth exploring).

## Adoption

Gleam has seen some adoption in recent years. According to a blog post, the language creators have placed strong emphasis on developer experience (DX), which has contributed to its appeal.

Although it compiles to run on the BEAM virtual machine, most new Gleam users do not have a background in Erlang nor Elixir, two older BEAM languages. In 2025, Louis Pilfold reported on results from the 2024 developer survey, which received 841 responses. Pilfold concluded that Gleam developers "overwhelmingly come from other ecosystems other than Erlang and Elixir". The core team also reported on Gleam's efforts to expand the BEAM ecosystem in a keynote talk at Code BEAM Europe 2024.

Developers have cited Gleam’s simplicity, static typing, and user-friendly tooling as reasons for adoption. The developer behind Nestful described their motivations for rewriting the project in Gleam as driven by its clarity and ease of use. There is a community-maintained list of companies using Gleam in production.

In 2025, Gleam appeared for the first time in the Stack Overflow Developer Survey, where it was the 2nd "most admired" language, with 70% of users currently using the language wanting to continue working with it. 1.1% of developer respondents reported doing "extensive development work" in the language over the past year.

## Features

Gleam includes the following features.

- Result type for error handling
- Immutable objects
- Algebraic data types
- Pattern matching
- No null pointers
- No implicit type conversions

## Example

A "Hello, World!" example:

```mw
import gleam/io

pub fn main() {
  io.println("hello, world!")
}
```

Gleam supports tail call optimization:

```mw
pub fn factorial(x: Int) -> Int {
  // The public function calls the private tail recursive function
  factorial_loop(x, 1)
}

fn factorial_loop(x: Int, accumulator: Int) -> Int {
  case x {
    1 -> accumulator

    // The last thing this function does is call itself
    _ -> factorial_loop(x - 1, accumulator * x)
  }
}
```

## Implementation

Gleam's toolchain is implemented in the Rust programming language. The toolchain is a single native binary executable which contains the compiler, build tool, package manager, source code formatter, and language server. A WebAssembly binary containing the Gleam compiler is also available, enabling Gleam code to be compiled within a web browser. This is used in Gleam's interactive language tour and online playground.
