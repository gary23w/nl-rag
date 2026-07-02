---
title: "Usage message"
source: https://en.wikipedia.org/wiki/Usage_message
domain: clap-cli-rust
license: CC-BY-SA-4.0
tags: clap cli, rust argument parser, command line parsing rust, clap derive api
fetched: 2026-07-02
---

# Usage message

In computer programming, a **usage message** or **help message** is a brief message displayed by a program that utilizes a command-line interface for execution. This message usually consists of the correct command line usage for the program and includes a list of the correct command-line arguments or options acceptable to said program.

Usage messages are utilized as a quick way for a program to inform the user of proper command syntax, and should not be substituted for proper error messages or for detailed documentation such as a man page.

## Pattern

On Unix-like platforms, usage messages usually follow the same common pattern:

- They often begin with "Usage:", the command, followed by a list of arguments.
- To indicate optional arguments, square brackets are commonly used, and can also be used to group parameters that must be specified together.
- To indicate required arguments, angled brackets are commonly used, following the same grouping conventions as square brackets.
- Exclusive parameters can be indicated by separating them with vertical bars within groups.

## Examples

Here is an example based on the NetBSD source code style guide:

```mw
Usage: program [-aDde] [-f | -g] [-n number] [-b b_arg | -c c_arg] req1 req2 [opt1 [opt2]]
```

This would indicate that "program" should be called with:

- options without operands: a, D, d, e (any of which may be omitted). Note that in this case some parameters are case-sensitive
- exclusive options: f, g (denoted by the vertical bar)
- options with operands: n
- exclusive options with operands: b, c
- required arguments: req1, req2
- optional argument opt1, which may be used with or without opt2 (marked optional within the group by using another set of square brackets)
- optional argument opt2, which requires opt1

## Implementation

To print a usage statement in a shell script, one might write:

```mw
case "$arg" in
...
h) printf 'Usage: %s parameter1 parameter2 ...\n' "$(basename "$0")"
   exit 0
   ;;
...
esac
```

## Anti-patterns

A usage statement is not an error message, and thus it should generally only be printed when specifically requested by the user (via `--help`, or `-h`, or `-?`, or some similar flag or argument). It should be written to the standard error; if the user has entered an incorrect command, the program should ideally respond with a succinct error message that describes the exact error made by the user rather than printing the usage statement and requiring the user to figure out what the mistake was. If the user fails to pass the correct number of arguments, for example, a single line stating that an argument is missing is far more useful than several pages of output providing a general usage.
