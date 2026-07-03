---
title: "Hello, world"
source: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
domain: cobol
license: CC-BY-SA-4.0
tags: cobol
fetched: 2026-07-03
---

# Hello, world

(Redirected from

"Hello, World!" program

)

A "**Hello, world**" program is usually a simple computer program that displays on the screen (often the console) a message similar to "Hello, world". A small piece of code in most general-purpose programming languages, this program is used to illustrate a language's basic syntax. Such a program is often the first written by a student of a new programming language, but it can also be used as a sanity check to ensure that the computer software intended to compile or run source code is correctly installed, and that its operator understands how to use it.

## History

While several small test programs have existed since the development of programmable computers, the tradition of using the phrase "Hello, world" as a test message was influenced by an example program in the 1978 book *The C Programming Language*, with likely earlier use in BCPL. The example program from the book prints "hello, world", and was inherited from a 1974 Bell Laboratories internal memorandum by Brian Kernighan, *Programming in C: A Tutorial*:

```mw
main( ) {
        printf("hello, world");
}
```

In the above example, the main( ) function defines where the program should start executing. The function body consists of a single statement, a call to the printf() function, which stands for "*print f*ormatted"; it outputs to the console whatever is passed to it as the parameter, in this case the string "hello, world".

The C-language version was preceded by Kernighan's own 1972 *A Tutorial Introduction to the Language B*, where the first known version of the program is found in an example used to illustrate external variables:

```mw
main( ) {
    extrn a, b, c;
    putchar(a); putchar(b); putchar(c); putchar('!*n');
}
 
a 'hell';
b 'o, w';
c 'orld';
```

The program above prints *hello, world!* on the terminal, including a newline character. The phrase is divided into multiple variables because in B, a character constant is limited to four ASCII characters. The previous example in the tutorial printed *hi!* on the terminal, and the phrase *hello, world!* was introduced as a slightly longer greeting that required several character constants for its expression.

The Jargon File reports that "hello, world!" instead originated in 1967 with the language BCPL. Outside computing, use of the exact phrase began over a decade prior; it was the catchphrase of New York radio disc jockey William B. Williams beginning in the 1950s.

## Variations

"Hello, world" programs vary in complexity between different languages. In some languages, particularly scripting languages, the "Hello, world" program can be written as one statement, while in others (more so many low-level languages) many more statements can be required. For example, in Python, to print the string *Hello, world* followed by a newline, one only needs to write `print("Hello, world")`. In contrast, the equivalent code in C++ requires the import of the C++ standard library, the declaration of an entry point (main function), and a call to print a line of text to the standard output stream.

The phrase "Hello, world" has seen various deviations in casing and punctuation, such as the presence or absence of the comma or exclamation mark. Some devices limit the format to specific variations, such as all-capitalized versions on systems that support only capital letters, while some esoteric programming languages may have to print a slightly modified string. Other human languages have been used as the output; for example, a tutorial for the Go language emitted both English and Chinese or Japanese characters, demonstrating the language's built-in Unicode support. Another notable example is the Rust language, whose management system automatically inserts a "Hello, World" program when creating new projects.

Some languages change the function of the "Hello, world" program while maintaining the spirit of demonstrating a simple example. Functional programming languages, such as Lisp, ML, and Haskell, tend to substitute a factorial program for "Hello, world", as functional programming emphasizes recursive techniques, whereas the original examples emphasize I/O, which violates the spirit of pure functional programming by producing side effects. Languages otherwise able to print "Hello, world" (assembly language, C, VHDL) may also be used in embedded systems, where text output is either difficult (requiring added components or communication with another computer) or nonexistent. For devices such as microcontrollers, field-programmable gate arrays, and complex programmable logic devices (CPLDs), "Hello, world" may thus be substituted with a blinking light-emitting diode (LED), which demonstrates timing and interaction between components.

The Debian and Ubuntu Linux distributions provide the "Hello, world" program through their software package manager systems, which can be invoked with the command *hello*. It serves as a sanity check and a simple example of installing a software package. For developers, it provides an example of creating a .deb package, either traditionally or using *debhelper*, and the version of hello used, GNU Hello, serves as an example of writing a GNU program.

Variations of the "Hello, world" program that produce a graphical output (as opposed to text output) have also been shown. Sun demonstrated a "Hello, world" program in Java based on scalable vector graphics, and the XL programming language features a spinning Earth "Hello, world" using 3D computer graphics. Mark Guzdial and Elliot Soloway have suggested that the "hello, world" test message may be outdated now that graphics and sound can be manipulated as easily as text.

In computer graphics, rendering a triangle—the "Hello Triangle"—is sometimes used as an introductory example for graphics libraries.

## Time to Hello World

"Time to hello world" (TTHW) is the time it takes to author a "Hello, world" program in a given programming language. This is one measure of a programming language's ease of use. Since the program is meant as an introduction for people unfamiliar with the language, a more complex "Hello, world" program may indicate that the programming language is less approachable. For instance, the first publicly known "Hello, world" program in Malbolge (which actually output "HEllO WORld") took two years to be announced, and it was produced not by a human but by a code generator written in Common Lisp .

The concept has been extended beyond programming languages to APIs, as a measure of how simple it is for a new developer to get a basic example working; a shorter time indicates an easier API for developers to adopt.

## Wikipedia articles containing "Hello, world" programs

- ABAP
- Ada
- Aldor
- ALGOL
- ALGOL 60
- AmbientTalk
- Amiga E
- Apache Click
- Apache Jelly
- Apache Wicket
- AppJar
- AppleScript
- Applesoft BASIC
- Arc
- Atari Assembler Editor
- AutoLISP
- AviSynth
- AWK
- BASIC
- Basic Assembly Language
- Ballerina
- BCPL
- Beatnik
- Befunge
- BETA
- Blitz BASIC
- Brainfuck
- C
- Caché ObjectScript
- Cairo
- C/AL
- Casio BASIC
- Charm
- CherryPy
- Clean
- Clipper
- C++
- C#
- COBOL
- Cobra
- Common Intermediate Language
- Cython
- Dart
- Darwin
- Data General Nova
- DOORS Extension Language
- Easy Programming Language
- Эль-76
- Elixir
- Enyo
- எழில்
- F#
- FastAPI
- Fjölnir
- Flask
- Flix
- Forth
- FORTRAN
- Fortress
- FreeBASIC
- Go
- Godot
- Google Gadgets
- GNU Smalltalk
- Hack
- Harbour
- Haskell
- Hollywood
- HTML
- HTML Application
- IBM Open Class
- Idris
- INTERCAL
- Internet Foundation Classes
- Io
- IRAF
- J
- JADE
- Java
- JavaFX Script
- JFace
- K
- KERNAL
- Kivy
- Kotlin
- K-Meleon
- LibreLogo
- Lisp
- LiveScript
- LOLCODE
- Lua
- MAC/65
- MACRO-10
- MACRO-11
- MAD
- Magik
- Malbolge
- MATLAB
- Mercury
- MicroPython
- Microsoft Small Basic
- mIRC scripting language
- MMIX
- Mockito
- Modula-3
- Monad
- MUMPS
- Nemerle
- Newspeak
- Nim
- OmniMark
- OpenEdge Advanced Business Language
- Open Programming Language
- Oriel
- ParaSail
- Parrot assembly language
- Parrot intermediate representation
- Pascal
- PCASTL
- PDP-8
- Perl
- Perl module
- PHP
- Plack
- Plua
- Plus
- PostScript
- PowerBASIC
- Prolog
- PureBasic
- Pure Data
- PureScript
- PyGTK
- Python
- Q
- QB64
- QuickBASIC
- R
- Rack
- Racket
- Raku
- React Native
- Rebol
- Refal
- RGtk2
- Robot Framework
- Ruby
- Rust
- SAKO
- SARL
- Scala
- Scilab
- Scratch
- Self
- Shakespeare
- Simula
- SmallBASIC
- Smalltalk
- Standard ML
- Standard Widget Toolkit
- Swift
- TeX
- TI-990
- TI‑BASIC
- Tornado
- Turing
- UCBLogo
- Umple
- Unlambda
- V
- Vala
- Visual Basic
- Visual IRC
- web2py
- Web Server Gateway Interface
- Whitespace
- Wt
- XBLite
- Xojo
- Zig
