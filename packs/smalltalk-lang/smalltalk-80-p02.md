---
title: "Smalltalk (part 2/2)"
source: https://en.wikipedia.org/wiki/Smalltalk-80
domain: smalltalk-lang
license: CC-BY-SA-4.0
tags: smalltalk language, smalltalk lang, pharo smalltalk, squeak smalltalk
fetched: 2026-07-02
part: 2/2
---

## Integrated Development Environment

Smalltalk is one of the first systems to be based around an Integrated Development Environment. There are a rich variety of tools to support code development, and other activities, such as graphics, and music. Smalltalk was the first system in which the modern desktop paradigm of Windows, Icons, Menus, and Pointers (WIMP) was created. Although pointers had already been invented, Smalltalk was the first system to implement overlapping windows and pop-up menus. While there are several programming tools we shall describe the following five major tools. The images of the tools are from a 2024 Squeak system

- browser, the main code viewing and writing tool
- workspace, a text editor in which expressions can be evaluate
- transcript, an output window for text, which in many dialects is also a workspace
- inspector
- notifier/debugger, a window opened in response to an unhandled exception, and can morph into a full debugger

### Browser

Smalltalk-80 derived systems organize classes within "system categories", such as `Kernel-Numbers`, `Kernel-Objects`, `Collections-Abstract`, `Collections-Sequenceable`, etc, and within classes methods are organized in named categories such as `accessing`, `arithmetic`, `instance creation`, etc. From this follows the classic five paned browser, with four panes in the upper half of the window containing from high to left the list of system categories, that when one is selected displays in the second window the list of classes in that category, that when one is selected displays the list of message categories in the selected class, that when one is selected displays in the last pane the selectors of the methods in the selected category in the selected class. When one of the selectors in the fourth pane is selected the source for that method is displayed in the fifth pane. If only a category is selected and not a method, the fifth pane shows a template for defining a new method. If a system category is selected but no class, a template for creating a class in the category is displayed. Various pop-up menus allow one to query the tool such as searching for a class by name, finding all senders of a selected message, or all implementors of the message, and so on. In this way the browser is both a code reading and system exploration tool and a code authoring tool.

### Workspace

A Workspace is a simple text editor editing a single string. One can type arbitrary text in the workspace, including Smalltalk expressions. On the pop-up menu "do it" (evaluate the selected expression), "print it" (evaluate the selected expression and insert the print string of the result immediately after the selection), and "inspect it" (open an inspector on the result of the evaluation of the selected expression, see "Inspector" below) are three oft used actions. Note that the fifth pane in the Browser is also a workspace, so that one can evaluate expressions and insert their results while editing method definitions, and a common thing is to include evalteable expressions, typically examples, in comments in a method, because almost everywhere the text of a method is shown (for example in the debugger) code is executable as in a workspace. Both workspaces and the browser's text panes are typically syntax highlighted. By using blocks to separate different expressions one can have several syntax highlighted expressions, each with their own temporaries in a single workspace.

### Transcript

The Transcript is a special workspace associated with the global Transcript. So evaluating `Transcript print: 52 factorial; cr; flush` causes 80658175170943878571660636856403766975289505440883277824000000000000 followed by a newline to appear on the Transcript window. The Transcript therefore serves as a place to emit logging messages, although it can also function as a Workspace

### Inspector

There are various inspectors, some tailored to displaying different kinds of object. The most basic inspector has two panes. To the left is a list of the object itself (with the label "self"), followed by the instance variables in the object, which will include numbered instance variables in sequences such as strings and arrays. To the right is a workspace pane. Selecting a name in the list replaces the workspace's contents with a print string of the selected variable. Editing and "accepting" the text in the workspace pane when an instance variable is selected will assign the result of the evaluation to the selected variable. One can "drill down" by using the "inspect" command on the list menu which will apply to the selected instance variable. More sophisticated inspectors (e.g. explorers) support finder-like tree access so that object structure can be traversed without opening additional windows.

### Notifier/Debugger

The default response to an unhandled exception is to open a Notifier, which is a window containing a stack backtrace of the first few activations, and buttons such as "Debug", "Proceed", "Close", etc. If the programmer chooses "Debug" then the full debugger opens. This has six panes. At the top is the stack window, containing a list of the contexts in the stack. Selecting a context causes the middle pane to display the text of the context's method, and to highlight the current expression within the method. Selecting the top context will display the method raising the exception and the message raising the exception will be highlighted. Selecting a context causes the bottom four panes to be updated. The bottom left two panes are the receiver inspector, that inspect the receiver of the selected message. The bottom right two panes are the context inspector that show the argument and temporary variable names in the selected context and allow display and modification of these variables.

Sending the message `self halt` causes an exception which opens a notifier, providing a simple breakpoint facility (typically breakpoint facilities provide more than just the simple halt, but it was the first such facility). Workspaces also provide a "debug it" evaluator which opens a debugger on the selected expression positioned at the first message send within the expression. So selecting `52 factorial` and choosing "debug it" from the pop-up menu opens a debugger with the "doit context" selected and the `factorial` selector highlighted. The debugger provides buttons to do "step into", "step over", etc. Hence by choosing "step into" one can explore the evaluation of `52 factorial`. In this way the debugger provides an inspector of a process, allowing one to explore a halted computation.

If an exception results from a doesNotUnderstand:, or subclassResponsibility send, then the notifier will include a "Create" button, allowing the programmer to choose where in the receiver's hierarchy to define an "initial draft" of the method to be implemented. Redefining a method in the debugger causes the selected context to reset back to the first statement (arguments are not modifiable in Smalltalk so this gets the execution state back to the start of a method). In this way the debugger supports live programming, defining methods as the computation proceeds. This is an extremely productive and enjoyable way to program. Everything in the system is at your finger tips. One has the full power of workspaces to evaluate subexpressions, and the browser to search for supporting code as one programs.

Clicking on the Debug button opens the Notifier into a Debugger allowing inspecting the call stack and editing and continuing from any method activation. In this case the Notifier has created a template of the missing method that the programmer can edit, compile, and then continue the computation.


## Hello World example

The Hello world program is used by virtually all texts to new programming languages as the first program learned to show the most basic syntax and environment of the language. For Smalltalk, the program is extremely simple to write. The following code, the message "show:" is sent to the object "Transcript" with the String literal 'Hello, world!' as its argument. Invocation of the "show:" method causes the characters of its argument (the String literal 'Hello, world!') to be displayed in the transcript ("terminal") window.

```mw
Transcript show: 'Hello, world!'.
```

To see the results of this example, a Transcript window must be open.


## Image-based persistence

Most popular programming systems separate static program code (in the form of class definitions, functions or procedures) from dynamic, or run time, program state (such as objects or other forms of program data). They load program code when a program starts, and any prior program state must be recreated explicitly from configuration files or other data sources. Any settings the program (and programmer) does not explicitly save must be set up again for each restart. A traditional program also loses much useful document information each time a program saves a file, quits, and reloads. This loses details such as undo history or cursor position. Image based systems don't force losing all that just because a computer is turned off, or an OS updates.

Many Smalltalk systems, however, do not differentiate between program data (objects) and code (classes). In fact, classes are objects. Thus, most Smalltalk systems store the entire program state (including both Class and non-Class objects) in an image file. The image can then be loaded by the Smalltalk virtual machine to restore a Smalltalk-like system to a prior state. This was inspired by FLEX, a language created by Alan Kay and described in his M.Sc. thesis.

Smalltalk images are similar to (restartable) core dumps and can provide the same functionality as core dumps, such as delayed or remote debugging with full access to the program state at the time of error.

Other languages that model application code as a form of data, such as Lisp, often use image-based persistence as well (see EMACS, for example). This method of persistence is powerful for rapid development because all the development information (e.g. parse trees of the program) is saved which facilitates debugging.

However, it also has serious drawbacks as a true persistence mechanism. For one thing, developers may often want to hide implementation details and not make them available in a run time environment. For reasons of legality and maintenance, allowing anyone to modify a program at run time inevitably introduces complexity and potential errors that would not be possible with a compiled system that exposes no source code in the run time environment. Also, while the persistence mechanism is easy to use, it lacks the true persistence abilities needed for most multi-user systems. The most obvious is the ability to do transactions with multiple users accessing the same database in parallel.


## Level of access

Everything in Smalltalk-80, unless customised to avoid the possibility, is available for modification from within a running program. This means that, for example, the IDE can be changed in a running system without restarting it. In some implementations, the syntax of the language or the garbage collection implementation can also be changed on the fly. Even the statement `true become: false` is valid in Smalltalk, although executing it is not recommended except for demonstration purposes (see virtual machine, image-based persistence, and backups).


## Just-in-time compilation

Smalltalk programs are usually compiled to bytecode, which is then interpreted by a virtual machine or dynamically translated into native machine-code. The results of previous message lookups are cached in self-modifying machine-code resulting in very high-performance sends that can out-perform the indirect function calls in C++ virtual method calls.


## List of implementations

### OpenSmalltalk

OpenSmalltalk VM (**OS VM**) is a relatively high-performance implementation of the Smalltalk virtual machine on which several modern open-source Smalltalk dialects are based. The OS VM derives from the original Back-to-the-Future (BTTF) Squeak interpreter implemented by Dan Ingalls, Ted Khaeler, John Maloney and many other contributors. As with the BTTF VM, OS VM is transpiled from the Smalltalk system in which it is developed (using a subset of Smalltalk named Slang) to native C language source code, which is in turn compiled against specific platform and architecture of the hardware practically enabling cross-platform execution of the Smalltalk images. The OS VM differs from the BTTF VM in

- introducing a JIT compiler to native machine code, including sophisticated machine-code method cacheing techniques
- using "context-to-stack-mapping" to vastly reduce the overheads of context objects
- supporting both the original BTTF object representation, and Spur, a much more efficient and native 32-bit and 64-bit scheme with a much improved garbage collector, object pinning, and lazy become

The notable Smalltalk dialects based on the OS VM are:

- Squeak, the original open source Smalltalk that the OpenSmalltalk VM was built for, that derives from Xerox PARC's Smalltalk-80 v1
- Pharo Smalltalk, an open-source cross-platform language, that derives from Squeak
- Croquet, a replicating distributed Smalltalk for the Croquet Project
- Cuis Smalltalk that derives from Squeak

### Others

- Amber Smalltalk, runs on JavaScript via transpiling
- Dolphin Smalltalk from Object Arts
- Etoys, a visual programming system for learning built in Squeak
- GemStone/S from GemTalk Systems
- GNU Smalltalk, headless (lacks GUI) implementation of Smalltalk
- Smalltalk MT Smalltalk for Windows from Object Connect
- ObjectStudio from Cincom
- Scratch a visual programming system (only versions before 2.0 are Smalltalk-based)
- Smalltalk/X from exept.de
- StepTalk, GNUstep scripting framework uses Smalltalk language on an Objective-C runtime
- Strongtalk, an open-source (since 2006) Windows-only version, offers optional strong typing; initially created at Sun Microsystem Labs.
- VisualAge Smalltalk from IBM
- Visual Smalltalk Enterprise, and family, including Smalltalk/V
- VisualWorks from Cincom, a descendant of the original Xerox PARC Smalltalk-80 v2
