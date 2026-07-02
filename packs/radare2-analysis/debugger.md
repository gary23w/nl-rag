---
title: "Debugger"
source: https://en.wikipedia.org/wiki/Debugger
domain: radare2-analysis
license: CC-BY-SA-4.0
tags: radare2 analysis framework, command line reverse engineering, binary debugger toolkit, hex editor inspection, disassembly workflow
fetched: 2026-07-02
---

# Debugger

A **debugger** is software for executing a computer program in an environment that allows for programming-level inspection and control. A debugger is often used to debug, but can be used for other goals including testing. Common features of a debugger include stepping through code line-by-line, breaking into the program's flow of control, managing breakpoints, and reporting and modifying memory.

A **source-level debugger** (a.k.a. **symbolic debugger**) provides a user experience that integrates the program's source code. Typically, such a debugger can indicate which line of source code corresponds to the execution point of the program and allows for reading and writing memory via the symbols of the source code. In contrast, a **low-level debugger** (a.k.a. **machine-language debugger**) shows the execution point as machine code or its associated assembly language and allows memory access by address only.

The code to be examined might alternatively be running on an *instruction set simulator* (ISS), a technique that allows great power in its ability to halt when specific conditions are encountered, but which will typically be somewhat slower than executing the code directly on the appropriate (or the same) processor. Some debuggers offer two modes of operation, full or partial simulation, to limit this impact.

## Features

Typically, debuggers offer a query processor, a symbol resolver, an expression interpreter, and a debug support interface at its top level. Debuggers also offer more sophisticated functions such as running a program step by step (**single-stepping** or program animation), stopping (**breaking**) (pausing the program to examine the current state) at some event or specified instruction by means of a breakpoint, and tracking the values of variables.Some debuggers have the ability to modify the program state while it is running. It may also be possible to continue execution at a different location in the program to bypass a crash or logical error.

The same functionality which makes a debugger useful for correcting bugs allows it to be used as a software cracking tool to evade copy protection, digital rights management, and other software protection features. It often also makes it useful as a general verification tool, fault coverage, and performance analyser, especially if instruction path lengths are shown.

Most mainstream debugging engines, such as gdb and dbx, provide console-based command line interfaces. Debugger front-ends are popular extensions to debugger engines that provide IDE integration, program animation, and visualization features.

### Handling program errors

If a program is running with a debugger, and an exception occurs because of a programming bug or invalid data, the debugger is notified of the exception. When the program "traps" or reaches a preset condition, the debugger typically shows the location in the original code if it is a source-level debugger or symbolic debugger. If it is a low-level debugger or a machine-language debugger it shows the line in the disassembly (unless it also has online access to the original source code and can display the appropriate section of code from the assembly or compilation).

### Record and replay debugging

Record and replay debugging, also known as "software flight recording" or "program execution recording", captures application state changes and stores them to disk as each instruction in a program executes. The recording can then be replayed and interactively debugged to diagnose and resolve defects. Record and replay debugging is useful for remote debugging and for resolving intermittent, non-deterministic, and other hard-to-reproduce defects.

### Reverse debugging

Some debuggers include a feature called "**reverse debugging**", also known as "historical debugging" or "backwards debugging". These debuggers make it possible to step a program's execution backwards in time. Various debuggers include this feature. Microsoft Visual Studio (2010 Ultimate edition, 2012 Ultimate, 2013 Ultimate, and 2015 Enterprise edition) offers IntelliTrace reverse debugging for C#, Visual Basic .NET, and some other languages, but not C++. Reverse debuggers also exist for C, C++, Java, Python, Perl, and other languages. Some are open source; some are proprietary commercial software. Some reverse debuggers slow down the target by orders of magnitude, but the best reverse debuggers cause a slowdown of 2× or less. Reverse debugging is very useful for certain types of problems, but is not commonly used.

### Time travel debugging

In addition to the features of reverse debuggers, time travel debugging also allow users to interact with the program, changing the history if desired, and watch how the program responds.

## Language dependency

Some debuggers operate on a single specific language while others can handle multiple languages transparently. For example, if the main target program is written in COBOL but calls assembly language subroutines and PL/1 subroutines, the debugger may have to dynamically switch modes to accommodate the changes in language as they occur.

## Memory protection

Some debuggers also incorporate memory protection to avoid storage violations such as buffer overflow. This may be extremely important in transaction processing environments where memory is dynamically allocated from memory 'pools' on a task by task basis.

## Hardware support for debugging

Some processors have hardware support for single-stepping a program, such as the trap flag.

Most modern microprocessors have at least one of these features in their CPU design to make debugging easier:

- Hardware support for code and data breakpoints, such as address comparators and data value comparators or, with considerably more work involved, page fault hardware.
- In-system programming allows an external hardware debugger to reprogram a system under test (for example, adding or removing instruction breakpoints). Many systems with such ISP support also have other hardware debug support.
- JTAG access to hardware debug interfaces such as those on ARM architecture processors or using the Nexus command set. Processors used in embedded systems typically have extensive JTAG debug support.
- Micro controllers with as few as six pins need to use low pin-count substitutes for JTAG, such as BDM, Spy-Bi-Wire, or debugWIRE on the Atmel AVR. DebugWIRE, for example, uses bidirectional signaling on the RESET pin.

## Debugger front-ends

Some of the most capable and popular debuggers implement only a simple command line interface (CLI)—often to maximize portability and minimize resource consumption. Developers typically consider debugging via a graphical user interface (GUI) easier and more productive. This is the reason for visual front-ends, that allow users to monitor and control subservient CLI-only debuggers via graphical user interface. Some GUI debugger front-ends are designed to be compatible with a variety of CLI-only debuggers, while others are targeted at one specific debugger.

## Ethical or legal debugging

Debugging is often used to illegally crack or pirate software, which is usually illegal even when done non-maliciously. Crackme's are programs specifically designed to be cracked or debugged. These programs allow those with debuggers to practice their debugging ability without getting into legal trouble.
