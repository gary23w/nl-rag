---
title: "Idris: A Language for Type-Driven Development"
source: https://www.idris-lang.org/
domain: idris-lang
license: CC-BY-SA-4.0
tags: idris language, idris lang, idris dependent types
fetched: 2026-07-02
---

# Idris: A Language for Type-Driven Development

Idris is a programming language designed to encourage *Type-Driven Development*.

In type-driven development, types are tools for constructing programs. We treat the type as the *plan* for a program, and use the compiler and type checker as our assistant, guiding us to a complete program that satisfies the type. The more expressive the type is that we give up front, the more confidence we can have that the resulting program will be correct.

In Idris, types are first-class constructs in the language. This means types can be passed as arguments to functions, and returned from functions just like any other value, such as numbers, strings, or lists. This is a small but powerful idea, enabling:

- relationships to be expressed between values; for example, that two lists have the same length.
- assumptions to be made explicit and checked by the compiler. For example, if you assume that a list is non-empty, Idris can ensure this assumption always holds before the program is run.
- if desired, properties of program behaviour to be formally stated and proven.

## Getting Started

You can see some small examples, then take a look at the documentation.

## Community

****Mailing list****

Long-form discussion happens on the

mailing list

.

****GitHub****

The Idris source is available from the Idris repository.

LSP, tools, and code by the wider Idris community can generally be found at:

- The idris-community organisation, and
- the pack package collection.

There are some legacy tools and code available in the idris-hackers organisation.

****Zulip****

There is an Idris community on

Zulip

, with several channels for learning, help, and different aspects of development. This is probably the most active place for interactive discussion of Idris and projects using it.

****IRC****

There is also an irc channel

#idris

on

libera

. Point your irc client to

irc.libera.chat

then

/join #idris

. For a web interface, you can try

IRCCloud

.

****Discord (DEPRECATED)****

*NOTE: The Discord will be read-only by 2026-05-25 UTC+1,* it is being deprecated in favour of Zulip.

There is an Idris community on Discord with several channels for learning, help and different aspects of development. You can get an invitation to join here This is currently probably the most active place for interactive discussion of Idris.

****Slack (DEPRECATED)****

There is an

#idris

channel on the

Functional Programming

Slack. However, at the time of writing (2026-05-18), it is very rarely used.

All participants in these forums are requested to abide by the community standards.

Idris development is led by Edwin Brady at the School of Computer Science, University of St Andrews.

Many thanks to Heath Johns for designing the logo.

## Support

Idris has been generously supported by the following EPSRC grants:

- Type-driven Verification of Communicating Systems
- Programming as Conversation: Type-Driven Development in Action

We are also grateful for the continuing support of SICSA, the Scottish Informatics and Computer Science Alliance.

Finally, we are grateful to Zulip (an organized team chat app designed for efficient communication) for providing us with a sponsored Zulip Cloud Standard plan.
