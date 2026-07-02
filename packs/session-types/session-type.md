---
title: "Session type"
source: https://en.wikipedia.org/wiki/Session_type
domain: session-types
license: CC-BY-SA-4.0
tags: session type, multiparty session types, typed channel, protocol conformance
fetched: 2026-07-02
---

# Session type

In type theory, **session types** are used to ensure correctness in concurrent programs. They guarantee that messages sent and received between concurrent programs are in the expected order and of the expected type. Session type systems have been adapted for both channel and actor systems.

Session types are used to ensure desirable properties in concurrent and distributed systems, i.e. absence of communication errors or deadlocks, and protocol conformance.

## Binary versus multiparty session types

Interaction between two processes can be checked using *binary* session types, while interactions between more than two processes can be checked using *multiparty* session types. In multiparty session types interactions between all participants are described using a *global type*, which is then projected into *local types* that describe communication from the local view of each participant. Importantly, the global type encodes the sequencing information of the communication, which would be lost if we were to use binary session types to encode the same communication.

## Formal definition of binary session types

Binary session types can be described using send operations ( ${\displaystyle$ ), receive operations ( ${\displaystyle$ ), branches ( $\&$ ), selections ( $\oplus$ ), recursion ( $rec$ ) and termination ( $end$ ).

For example, $S=\;!bool.?int.end$ represents a session type S which first sends a boolean ( $!bool$ ), then receives an integer ( $?int$ ) before finally terminating ( $end$ ).

## Implementations

Session types have been adapted for several existing programming languages, including:

- lchannels (Scala)
- Effpi (Scala)
- STMonitor (Scala)
- EnsembleS
- Session-types (Rust)
- sesh (Rust)
- Session Actors (Python)
- Monitored Session Erlang (Erlang)
- FuSe (OCaml)
- session-ocaml (OCaml)
- Priority Sesh (Haskell)
- Java Typestate Checker (Java)
- Swift Sessions (Swift)
