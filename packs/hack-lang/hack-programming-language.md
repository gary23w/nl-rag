---
title: "Hack (programming language)"
source: https://en.wikipedia.org/wiki/Hack_(programming_language)
domain: hack-lang
license: CC-BY-SA-4.0
tags: hack language, hacklang, hhvm hack, facebook hack
fetched: 2026-07-02
---

# Hack (programming language)

**Hack** is a programming language for the HipHop Virtual Machine (HHVM), created by Meta (formerly Facebook) as a dialect of PHP. The language implementation is free and open-source software, licensed under an MIT License.

Hack allows use of both dynamic typing and static typing. This kind of a type system is called gradual typing, which is also implemented in other programming languages such as ActionScript. Hack's type system allows types to be specified for function arguments, function return values, and class properties; however, types of local variables are always inferred and cannot be specified.

## History

Hack was introduced on March 20, 2014. Before the announcement of the new language, Facebook had already implemented the code and tested it on a large part of its web site.

## Features

Hack is designed to interoperate seamlessly with PHP, which is a widely used open-source scripting language that has a focus on web development and can be embedded into HTML. A majority of valid PHP scripts are also valid in Hack; however, many less-often used PHP features and language constructs are unsupported in Hack.

Hack extends the type hinting available in PHP 5 through the introduction of static typing, by adding new type hints (for example, for scalar types such as integer or string), as well as by extending the use of type hints (for example, for class properties or function return values). However, types of local variables cannot be specified. Since Hack uses a gradual typing system, in the default mode, type annotations are not mandatory even in places they cannot be inferred; the type system will assume the author is correct and admit the code. However, a "strict" mode is available which requires such annotations, and thus enforces fully sound code.

## Syntax and semantics

The basic file structure of a Hack script is similar to a PHP script with a few changes. A Hack file does not include the `<?php` opening markup tag and forbids using top-level declarations. Code must be placed in an entrypoint function. These are automatically executed if they are in the top-level file, but not if the file is included via `include`, `require`, or the autoloader. Like other functions in Hack, the function names must be unique within a project – i.e., projects with multiple entrypoints can not both be called `main`:

```mw
<<__EntryPoint>>
function main(): void {
  echo 'Hello, World!';
}
```

The above script, similar to PHP, will be executed and the following output is sent to the browser:

```mw
Hello, World!
```

Unlike PHP, Hack and HTML code do not mix; either XHP or another template engine needs to be used.

### Functions

Like PHP 7, Hack allows types to be specified for function arguments and function return values. Functions in Hack are thus annotated with types like the following:

```mw
// Hack functions are annotated with types.
function negate(bool $x): bool {
    return !$x;
}
```
