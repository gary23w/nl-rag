---
title: "V (programming language)"
source: https://en.wikipedia.org/wiki/V_(programming_language)
domain: vlang
license: CC-BY-SA-4.0
tags: vlang, v lang, v language
fetched: 2026-07-02
---

# V (programming language)

**V**, also known as **vlang**, is an in-development statically typed, compiled programming language created by Alexander Medvednikov in early 2019. It was inspired by Go, and other programming languages including Oberon, Swift, and Rust. It is free and open-source software released under the MIT License, and currently in beta.

The goals of V include ease of use, readability, and maintainability.

## History

The new language was created as a result of frustration with existing languages being used for personal projects. It was originally intended for personal use, but after being mentioned publicly and increasing interest, it was decided to make it public. V was initially created to develop a desktop messaging client named Volt. On public release, the compiler was written in V, and could compile itself. Key design goals in creating V were being easy to learn and use, higher readability, fast compiling, increased safety, efficient development, cross-platform usability, improved C interoperability, better error handling, modern features, and more maintainable software.

V is developed, maintained, and released through GitHub by developers and contributors internationally. In 2025, V started being ranked on the TIOBE index.

## Features

### Safety

V has policies to facilitate memory-safety, speed, and secure code, including various default features for greater program safety. It employs bounds checking, to guard against out of bounds use of variables. Option/result types are used, where the option data type (`?`) can be represented by `none` (among possible choices) and the result type (`!`) can handle any returned errors. To ensure greater safety, error checking is mandatory. By default, the following are immutable: variables, structs, and function arguments. This includes string values are immutable, so elements cannot be mutated. Other protections, which are the default for the language, are: no use of undefined values, variable shadowing, null pointers (unless marked as unsafe), or global variables (unless enabled via flag).

### Performance

V uses value types and string buffers to reduce memory allocations. The language can be compiled to human-readable C, and in executing and compiling, is considered as fast.

### Memory management

V supports four memory management options:

1. A garbage collector. This is the default.
2. Manual memory management via disabling the garbage collector.
3. Autofree, which is experimental, for invoking the necessary calls to automatically release objects while compiling.
4. Arena allocation.

### Source code translators

V supports a source-to-source compiler (transpiler) and can translate C code into V.

Working translators are also being developed for Go, JavaScript, and WebAssembly.

## Syntax

Representative examples of V syntax include:

### Hello world

The "Hello, World!" program in V:

```mw
fn main() {
	println("Hello, World!")
}
```

### Variables

Variables are immutable by default and are defined using `:=` and a value. Use the `mut` reserved word (keyword) to make them mutable. Mutable variables can be assigned to using `=`:

```mw
x := 1
mut y := 2
y = 3
```

Redeclaring a variable, whether in an inner scope or in the same scope, is not allowed:

```mw
x := 1
{
    x := 3 // error: redefinition of x
}
x := 2 // error: redefinition of x
```

### Structs

Struct example:

```mw
struct Foo {
    number int
	name string
    score f32
}

// Struct fields can be initialized by name
var1 := Foo {
    number: 21
    name: "baz"
    score: 2.5
}

// or by position
var2 := Foo{50, "taz", 3.14}
```

### Heap structs

By default, structs are allocated via stack-based memory allocation (on the stack). When structs are referenced by using the prefix `&` or have the `[heap]` attribute, they are allocated via heap-based memory allocation (on the heap) instead:

```mw
struct Foo {
    number int
}

@[heap]
struct Baz {
    number f32
}

// Structs that are referenced are heap allocated
var1 := &Foo{2}

// Baz is always heap allocated because of its [heap] attribute
var2 := Baz{4.5}
```

### Methods

Methods in V are functions defined with a receiver argument. The receiver appears in its own argument list between the `fn` keyword and the method name. Methods must be in the same module as the receiver type.

The enrolled_status method (below) has a receiver of type `Client` named `x`. The convention is not to use receiver names like self or this, but preferably a short name. For example:

```mw
struct Client {
    enrolled bool
}

fn (x Client) enrolled_status() bool {
    return x.enrolled
}

client_1 := Client{true}
client_2 := Client{false}

println(client_1.enrolled_status()) // "true"
println(client_2.enrolled_status()) // "false"
```

### Error handling

Result types may represent an error returned from a function. Result types are declared by prepending `!`: `!Type`

Optional types may represent `none`. Option types prepend `?` to the type name: `?Type`.

```mw
fn something(t string) !string {
	if t == "foo" { return "foo" }
	return error("invalid")
}

x := something("foo") or { "default" } // x will be "foo"
y := something("baz") or { "default" } // y will be "default"
z := something("baz") or { panic("{err}") } // z will exit with an error

println(x)
println(y)
```
