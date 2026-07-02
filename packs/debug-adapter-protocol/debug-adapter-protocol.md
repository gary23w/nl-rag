---
title: "Official page for Debug Adapter Protocol"
source: https://microsoft.github.io/debug-adapter-protocol/
domain: debug-adapter-protocol
license: CC-BY-SA-4.0
tags: debug adapter protocol, dap debugging, editor debugger integration, breakpoint protocol
fetched: 2026-07-02
---

# Debug Adapter Protocol

The Debug Adapter Protocol (DAP) defines the abstract protocol used between a development tool (e.g. IDE or editor) and a debugger.

Star

## What is the Debug Adapter Protocol?

Adding a debugger for a new language to an IDE or editor is not only a significant effort, but it is also frustrating that this effort can not be easily amortized over multiple development tools, as each tool uses different APIs for implementing the same feature.

The idea behind the *Debug Adapter Protocol* (DAP) is to abstract the way how the debugging support of development tools communicates with debuggers or runtimes into a protocol. Since it is unrealistic to assume that existing debuggers or runtimes adopt this protocol any time soon, we rather assume that an intermediary component - a so called *Debug Adapter* - adapts an existing debugger or runtime to the Debug Adapter Protocol.

The Debug Adapter Protocol makes it possible to implement a generic debugger for a development tool that can communicate with different debuggers via Debug Adapters. And Debug Adapters can be re-used across multiple development tools which significantly reduces the effort to support a new debugger in different tools.

The *Debug Adapter Protocol* is a win for both debugger providers and tooling vendors!

*VS Code showing inline values powered by the Python Debug Adapter*

*VS Code's multi-thread debugging powered by the Java Debug Adapter*

*REPL console in VS Code powered by the Node.js Debug Adapter*

### Overview

The protocol defines the format of the messages sent using JSON between the development tool and the debug adapter.

### Specification

The latest version of the protocol specification is version 1.71.0.

Change History

### Implementations

The DAP has been implemented for many debuggers or runtimes and some development tools are hosting these debug adapters.
