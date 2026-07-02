---
title: "GitHub"
source: https://github.com/bazelbuild/starlark
domain: starlark
license: Apache-2.0
tags: starlark language, bazel build language, python-like config dialect, starlark scripting
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

bazelbuild

/

starlark

Public

- Notifications You must be signed in to change notification settings
- Fork 176
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History136 Commits136 Commits |   |   |   |
| .bazelci | .bazelci |   |   |
| proposals | proposals |   |   |
| test_suite | test_suite |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitignore | .gitignore |   |   |
| BUILD | BUILD |   |   |
| CODEOWNERS | CODEOWNERS |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE | LICENSE |   |   |
| MODULE.bazel | MODULE.bazel |   |   |
| README.md | README.md |   |   |
| design.md | design.md |   |   |
| process.md | process.md |   |   |
| setup_workspace.sh | setup_workspace.sh |   |   |
| spec.md | spec.md |   |   |
| spec_md_gen.py | spec_md_gen.py |   |   |
| spec_md_gen_lib.py | spec_md_gen_lib.py |   |   |
| spec_md_gen_test.py | spec_md_gen_test.py |   |   |
| users.md | users.md |   |   |
|   |   |   |   |

## Repository files navigation

# Starlark

(Build status)

## Overview

Starlark (formerly known as Skylark) is a language intended for use as a configuration language. It was designed for the Bazel build system, but may be useful for other projects as well. This repository is where Starlark features are proposed, discussed, and specified. It contains information about the language, including the specification. There are multiple implementations of Starlark.

Starlark is a dialect of Python. Like Python, it is a dynamically typed language with high-level data types, first-class functions with lexical scope, and garbage collection. Independent Starlark threads execute in parallel, so Starlark workloads scale well on parallel machines. Starlark is a small and simple language with a familiar and highly readable syntax. You can use it as an expressive notation for structured data, defining functions to eliminate repetition, or you can use it to add scripting capabilities to an existing application.

A Starlark interpreter is typically embedded within a larger application, and the application may define additional domain-specific functions and data types beyond those provided by the core language. For example, Starlark was originally developed for the Bazel build tool. Bazel uses Starlark as the notation both for its BUILD files (like Makefiles, these declare the executables, libraries, and tests in a directory) and for its macro language, through which Bazel is extended with custom logic to support new languages and compilers.

## Design Principles

- **Deterministic evaluation**. Executing the same code twice will give the same results.
- **Hermetic execution**. Execution cannot access the file system, network, system clock. It is safe to execute untrusted code.
- **Parallel evaluation**. Modules can be loaded in parallel. To guarantee a thread-safe execution, shared data becomes immutable.
- **Simplicity**. We try to limit the number of concepts needed to understand the code. Users should be able to quickly read and write code, even if they are not experts. The language should avoid pitfalls as much as possible.
- **Focus on tooling**. We recognize that the source code will be read, analyzed, modified, by both humans and tools.
- **Python-like**. Python is a widely used language. Keeping the language similar to Python can reduce the learning curve and make the semantics more obvious to users.

## Tour

The code provides an example of the syntax of Starlark:

```highlight
# Define a number
number = 18

# Define a dictionary
people = {
    "Alice": 22,
    "Bob": 40,
    "Charlie": 55,
    "Dave": 14,
}

names = ", ".join(people.keys())  # Alice, Bob, Charlie, Dave

# Define a function
def greet(name):
    """Return a greeting."""
    return "Hello {}!".format(name)

greeting = greet(names)

above30 = [name for name, age in people.items() if age >= 30]

print("{} people are above 30.".format(len(above30)))

def fizz_buzz(n):
    """Print Fizz Buzz numbers from 1 to n."""
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        print(s if s else i)

fizz_buzz(20)
```

If you've ever used Python, this should look very familiar. In fact, the code above is also a valid Python code. Still, this short example shows most of the language. Starlark is indeed a very small language.

For more information, see:

- Discussions for some design choices
- Why Starlark was created (previously named Skylark)
- The specification
- The mailing-list: starlark@googlegroups.com

## Build API

The first use-case of the Starlark language is to describe builds: how to compile a C++ or a Scala library, how to build a project and its dependencies, how to run tests. Describing a build can be surprisingly complex, especially as a codebase mixes multiple languages and targets multiple platforms.

In the future, this repository will contain a complete description of the build API used in Bazel. The goal is to have a clear specification and precise semantics, in order to interoperate with other systems. Ideally, other tools will be able to understand the build API and take advantage of it.

## Evolution

Read about the design process if you want to suggest improvements to the specification. Follow the mailing-list to discuss the evolution of Starlark.

## Implementations, tools, and users

See Awesome Starlark.
