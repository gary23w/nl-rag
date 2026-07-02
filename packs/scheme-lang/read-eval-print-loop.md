---
title: "Read–eval–print loop"
source: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
domain: scheme-lang
license: CC-BY-SA-4.0
tags: scheme language, scheme lang, r7rs scheme, scheme lisp
fetched: 2026-07-02
---

# Read–eval–print loop

A **read–eval–print loop** (**REPL**), also termed an **interactive toplevel** or **language shell**, is a simple interactive computer programming environment that takes single user inputs, executes them, and returns the result to the user; a program written in a REPL environment is executed piecewise. The term usually refers to programming interfaces similar to the classic Lisp machine interactive environment or to Common Lisp with the SLIME development environment. Common examples include command-line shells and similar environments for programming languages, and the technique is very characteristic of scripting languages, even though their characteristics can vary greatly.

## History

The expression *READ-EVAL-PRINT cycle* is used by L. Peter Deutsch and Edmund Berkeley for a 1964 implementation of Lisp on the PDP-1. Just one month later, Project Mac published a report by Joseph Weizenbaum (the creator of ELIZA, the world's first chatbot) describing a REPL-based language, called OPL-1, implemented in his Fortran-SLIP language on the Compatible Time Sharing System (CTSS).

The 1974 Maclisp reference manual by David A. Moon attests "Read-eval-print loop" on page 89, but does not use the acronym REPL.

Since at least the 1980s, the abbreviations *REP Loop* and *REPL* are attested in the context of Scheme.

## Overview

In a REPL, the user enters one or more expressions (rather than an entire compilation unit) and the REPL evaluates them and displays the results. The name *read–eval–print loop* comes from the names of the Lisp primitive functions which implement this functionality:

- The *read* function accepts an expression from the user, and parses it into a data structure in memory. For instance, the user may enter the s-expression `(+ 1 2 3)`, which is parsed into a linked list containing four data elements.
- The *eval* function takes this internal data structure and evaluates it. In Lisp, evaluating an s-expression beginning with the name of a function means calling that function on the arguments that make up the rest of the expression. So the function `+` is called on the arguments `1 2 3`, yielding the result `6`.
- The *print* function takes the result yielded by *eval*, and prints it out to the user. If it is a complex expression, it may be pretty-printed to make it easier to understand.

The development environment then returns to the read state, creating a loop, which terminates when the program is closed.

REPLs facilitate exploratory programming and debugging because the programmer can inspect the printed result before deciding what expression to provide for the next read. The read–eval–print loop involves the programmer more frequently than the classic edit–compile–run–debug cycle.

Because the *print* function outputs in the same textual format that the *read* function uses for input, most results are printed in a form that could be copied and pasted back into the REPL. However, it is sometimes necessary to print representations of elements that cannot sensibly be read back in, such as a socket handle or a complex class instance. In these cases, there must exist a syntax for unreadable objects. In Python, it is the `<__module__.class instance>` notation, and in Common Lisp, the `#<whatever>` form. The REPL of CLIM, SLIME, and the Symbolics Lisp Machine can also read back unreadable objects. They record for each output which object was printed. Later when the code is read back, the object will be retrieved from the printed output.

REPLs can be created to support any text-based language. REPL support for compiled languages is usually achieved by implementing an interpreter on top of a virtual machine which provides an interface to the compiler. For example, starting with JDK 9, Java included JShell as a command-line interface to the language. Various other languages have third-party tools available for download that provide similar shell interaction with the language, although the features can vary greatly.

## Uses

As a shell, a REPL environment allows users to access relevant features of an operating system in addition to providing access to programming capabilities. The most common use for REPLs outside of operating system shells is for interactive prototyping. Other uses include mathematical calculation, creating documents that integrate scientific analysis (e.g. IPython), interactive software maintenance, benchmarking, and algorithm exploration.

## Lisp specifics

### Implementation

A minimal definition in Common Lisp is:

```mw
(loop (print (eval (read))))
```

where `read` waits for user input and `eval` evaluates it. `print` prints the result, and `loop` loops indefinitely. You can enter `(+ 1 1)` and stop the loop with `C-c`.

### Functionality

Typical functionality provided by a Common Lisp REPL includes:

- History of inputs and outputs.
- Variables are set for the input expressions and results. These variables are also available in the REPL. For example in Common Lisp `*` refers to the last result, `**` and `***` to the results before that.
- Levels of REPLs. In many Lisp systems if an error occurs during the reading, evaluation or printing of an expression, the system is not thrown back to the top level with an error message. Instead a new REPL, one level deeper, is started in the error context. The user can then inspect the problem, fix it and continue – if possible. If an error occurs in such a debug REPL, another REPL, again a level deeper, is started. Often the REPL offers special debug commands.
- Error handling. In Common Lisp, the REPL opens an interactive debugger when a certain error occurs. The debugger allows to inspect the call stack, it allows to jump to the buggy function, fix it, re-compile it, and resume execution, without restarting the whole program from scratch. The debugger also provides restarts. These restarts can be used to go back to a certain REPL level or to provide a different input value.
- Mouse sensitive input and output of data objects.
- Input editing and context specific completion over symbols, pathnames, class names and other objects.
- Help and documentation for commands.
- Variables to control the reader. For example, the variable *read-base* controls in which base numbers are read by default.
- Variables to control the printer. Example: maximum length or maximum depth of expressions to print.
- Additional command syntax. Some REPLs have commands that follow not the s-expression syntax, but often work with Lisp data as arguments.
- Graphical REPLs. Some Lisp REPLs (the CLIM Listener is an example and, to a lower extent, SLIME) accept also graphical input and output.
- Connecting to a remote running program. It is possible to connect to a Common Lisp program running on another machine and to interact with it. This allows to: explore its internal state, change parameters, or even compile new code and update the system.

### Combining source files and REPL development

Developers of Lisp applications typically do *not* write or copy-paste code to a REPL. They use the REPL for quick tests, for debugging and to explore a running system. They write their application in a source file under version control, they use commands or keyboard shortcuts to compile their code interactively. The Lisp process is running and connected to their editor, and it compiles new code "on the fly", without restarting.

In Common Lisp, developers typically compile the current function they are working on. They can also compile a whole file, or compile a whole project. When a function is compiled, they may get type warnings (specially with the SBCL implementation), and they can invoke the newly created function from the REPL. If an error occurs, they are given an interactive debugger.

This process of compiling one single function and testing it on the REPL is very fast in comparison to other processes. The cycle of writing a new function, compiling it and testing is very short, and interactive, making it suitable for development. It also means that the application state is not lost during development.

It is only when they choose to do so that they run or compile all the application from scratch.
