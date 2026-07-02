---
title: "Common Lisp (part 2/2)"
source: https://en.wikipedia.org/wiki/Common_Lisp
domain: common-lisp
license: CC-BY-SA-4.0
tags: common lisp, hyperspec, clos, sbcl
fetched: 2026-07-02
part: 2/2
---

## Code examples

### Birthday paradox

The following program calculates the smallest number of people in a room for whom the probability of unique birthdays is less than 50% (the birthday paradox, where for 1 person the probability is obviously 100%, for 2 it is 364/365, etc.). The answer is 23.

In Common Lisp, by convention, constants are enclosed with + characters.

```mw
(defconstant +year-size+ 365)

(defun birthday-paradox (probability number-of-people)
  (let ((new-probability (* (/ (- +year-size+ number-of-people)
                               +year-size+)
                            probability)))
    (if (< new-probability 0.5)
        (1+ number-of-people)
        (birthday-paradox new-probability (1+ number-of-people)))))
```

Calling the example function using the REPL (Read Eval Print Loop):

```mw
CL-USER > (birthday-paradox 1.0 1)
23
```

### Sorting a list of person objects

We define a class `person` and a method for displaying the name and age of a person. Next we define a group of persons as a list of `person` objects. Then we iterate over the sorted list.

```mw
(defclass person ()
  ((name :initarg :name :accessor person-name)
   (age  :initarg :age  :accessor person-age))
  (:documentation "The class PERSON with slots NAME and AGE."))

(defmethod display ((object person) stream)
  "Displaying a PERSON object to an output stream."
  (with-slots (name age) object
    (format stream "~a (~a)" name age)))

(defparameter *group*
  (list (make-instance 'person :name "Bob"   :age 33)
        (make-instance 'person :name "Chris" :age 16)
        (make-instance 'person :name "Ash"   :age 23))
  "A list of PERSON objects.")

(dolist (person (sort (copy-list *group*)
                      #'>
                      :key #'person-age))
  (display person *standard-output*)
  (terpri))
```

It prints the three names with descending age.

```mw
Bob (33)
Ash (23)
Chris (16)
```

### Exponentiating by squaring

Use of the LOOP macro is demonstrated:

```mw
(defun power (x n)
  (loop with result = 1
        while (plusp n)
        when (oddp n) do (setf result (* result x))
        do (setf x (* x x)
                 n (truncate n 2))
        finally (return result)))
```

Example use:

```mw
CL-USER > (power 2 200)
1606938044258990275541962092341162602522202993782792835301376
```

Compare with the built in exponentiation:

```mw
CL-USER > (= (expt 2 200) (power 2 200))
T
```

### Find the list of available shells

WITH-OPEN-FILE is a macro that opens a file and provides a stream. When the form is returning, the file is automatically closed. FUNCALL calls a function object. The LOOP collects all lines that match the predicate.

```mw
(defun list-matching-lines (file predicate)
  "Returns a list of lines in file, for which the predicate applied to
 the line returns T."
  (with-open-file (stream file)
    (loop for line = (read-line stream nil nil)
          while line
          when (funcall predicate line)
          collect it)))
```

The function AVAILABLE-SHELLS calls the above function LIST-MATCHING-LINES with a pathname and an anonymous function as the predicate. The predicate returns the pathname of a shell or NIL (if the string is not the filename of a shell).

```mw
(defun available-shells (&optional (file #p"/etc/shells"))
  (list-matching-lines
   file
   (lambda (line)
     (and (plusp (length line))
          (char= (char line 0) #\/)
          (pathname
           (string-right-trim '(#\space #\tab) line))))))
```

Example results (on Mac OS X 10.6):

```mw
CL-USER > (available-shells)
(#P"/bin/bash" #P"/bin/csh" #P"/bin/ksh" #P"/bin/sh" #P"/bin/tcsh" #P"/bin/zsh")
```


## Comparison with other Lisps

Common Lisp is most frequently compared with, and contrasted to, Scheme—if only because they are the two most popular Lisp dialects. Scheme predates CL, and comes not only from the same Lisp tradition but from some of the same engineers—Guy Steele, with whom Gerald Jay Sussman designed Scheme, chaired the standards committee for Common Lisp.

Common Lisp is a general-purpose programming language, in contrast to Lisp variants such as Emacs Lisp and AutoLISP which are extension languages embedded in particular products (GNU Emacs and AutoCAD, respectively). Unlike many earlier Lisps, Common Lisp (like Scheme) uses lexical variable scope by default for both interpreted and compiled code.

Most of the Lisp systems whose designs contributed to Common Lisp—such as ZetaLisp and Franz Lisp—used dynamically scoped variables in their interpreters and lexically scoped variables in their compilers. Scheme introduced the sole use of lexically scoped variables to Lisp; an inspiration from ALGOL 68. CL supports dynamically scoped variables as well, but they must be explicitly declared as "special". There are no differences in scoping between ANSI CL interpreters and compilers.

Common Lisp is sometimes termed a *Lisp-2* and Scheme a *Lisp-1*, referring to CL's use of separate namespaces for functions and variables. (In fact, CL has *many* namespaces, such as those for go tags, block names, and `loop` keywords). There is a long-standing controversy between CL and Scheme advocates over the tradeoffs involved in multiple namespaces. In Scheme, it is (broadly) necessary to avoid giving variables names that clash with functions; Scheme functions frequently have arguments named `lis`, `lst`, or `lyst` so as not to conflict with the system function `list`. However, in CL it is necessary to explicitly refer to the function namespace when passing a function as an argument—which is also a common occurrence, as in the `sort` example above.

CL also differs from Scheme in its handling of Boolean values. Scheme uses the special values #t and #f to represent truth and falsity. CL follows the older Lisp convention of using the symbols T and NIL, with NIL standing also for the empty list. In CL, *any* non-NIL value is treated as true by conditionals, such as `if`, whereas in Scheme all non-#f values are treated as true. These conventions allow some operators in both languages to serve both as predicates (answering a Boolean-valued question) and as returning a useful value for further computation, but in Scheme the value '() which is equivalent to NIL in Common Lisp evaluates to true in a Boolean expression.

Lastly, the Scheme standards documents require tail-call optimization, which the CL standard does not. Most CL implementations do offer tail-call optimization, although often only when the programmer uses an optimization directive. Nonetheless, common CL coding style does not favor the ubiquitous use of recursion that Scheme style prefers—what a Scheme programmer would express with tail recursion, a CL user would usually express with an iterative expression in `do`, `dolist`, `loop`, or (more recently) with the `iterate` package.


## Implementations

See the Category Common Lisp implementations.

Common Lisp is defined by a specification (like Ada and C) rather than by one implementation (like Perl). There are many implementations, and the standard details areas in which they may validly differ.

In addition, implementations tend to come with extensions, which provide functionality not covered in the standard:

- Interactive Top-Level (REPL)
- Garbage Collection
- Debugger, Stepper and Inspector
- Weak data structures (hash tables)
- Extensible sequences
- Extensible LOOP
- Environment access
- CLOS Meta-object Protocol
- CLOS based extensible streams
- CLOS based Condition System
- Network streams
- Persistent CLOS
- Unicode support
- Foreign-Language Interface (often to C)
- Operating System interface
- Java Interface
- Threads and Multiprocessing
- Application delivery (applications, dynamic libraries)
- Saving of images

Free and open-source software libraries have been created to support extensions to Common Lisp in a portable way, and are most notably found in the repositories of the Common-Lisp.net and CLOCC (Common Lisp Open Code Collection) projects.

Common Lisp implementations may use any mix of native code compilation, byte code compilation or interpretation. Common Lisp has been designed to support incremental compilers, file compilers and block compilers. Standard declarations to optimize compilation (such as function inlining or type specialization) are proposed in the language specification. Most Common Lisp implementations compile source code to native machine code. Some implementations can create (optimized) stand-alone applications. Others compile to interpreted bytecode, which is less efficient than native code, but eases binary-code portability. Some compilers compile Common Lisp code to C code. The misconception that Lisp is a purely interpreted language is most likely because Lisp environments provide an interactive prompt and that code is compiled one-by-one, in an incremental way. With Common Lisp incremental compilation is widely used.

Some Unix-based implementations (CLISP, SBCL) can be used as a scripting language; that is, invoked by the system transparently in the way that a Perl or Unix shell interpreter is.

### List of implementations

#### Commercial implementations

**Allegro Common Lisp**

For Microsoft Windows, FreeBSD, Linux, Apple macOS and various UNIX variants. Allegro CL provides an

Integrated Development Environment (IDE)

(for Windows and Linux) and extensive capabilities for application delivery.

**Liquid Common Lisp**

Formerly called Lucid Common Lisp. Only maintenance, no new releases.

**LispWorks**

for Microsoft Windows, FreeBSD, Linux, Apple macOS, iOS, Android and various UNIX variants. LispWorks provides an

Integrated Development Environment (IDE)

(available for most platforms, but not for iOS and Android) and extensive capabilities for application delivery.

**mocl**

For iOS, Android, and macOS.

**Open Genera**

For DEC Alpha.

**Scieneer Common Lisp**

Designed for high-performance scientific computing.

#### Freely redistributable implementations

**Armed Bear Common Lisp (ABCL)**

A CL implementation that runs on the

Java Virtual Machine

.

It includes a compiler to

Java byte code

, and allows access to Java libraries from CL. It was formerly just a component of the

Armed Bear J Editor

.

**Clasp**

An LLVM-based implementation that seamlessly interoperates with C++ libraries. Runs on several Unix and Unix-like systems (including

macOS

).

**CLISP**

A bytecode-compiling implementation, portable and runs on several Unix and Unix-like systems (including

macOS

), as well as Microsoft Windows and several other systems.

**Clozure CL (CCL)**

Originally a

free and open-source

fork of Macintosh Common Lisp. As that history implies, CCL was written for the Macintosh, but Clozure CL now runs on

macOS

,

FreeBSD

,

Linux

,

Solaris

, and

Windows

. 32 and 64-bit

x86

ports are supported on each platform. Additionally, there are Power PC ports for macOS and Linux. CCL was previously known as OpenMCL, but that name is no longer used to avoid confusion with the open source version of Macintosh Common Lisp.

**CMUCL**

Originally from

Carnegie Mellon University

, now maintained as

free and open-source software

by a group of volunteers. CMUCL uses a fast native-code compiler. It is available on

Linux

and

BSD

for Intel x86;

Linux

for Alpha;

macOS

for Intel x86 and PowerPC; and Solaris, IRIX, and HP-UX on their native platforms.

**Corman Common Lisp**

For Microsoft Windows. In January 2015, Corman Lisp was published under the MIT license.

**Embeddable Common Lisp (ECL)**

ECL includes a bytecode interpreter and compiler. It can also compile Lisp code to machine code via a C compiler. ECL then compiles Lisp code to C, compiles the C code with a C compiler, and can then load the resulting machine code. It is also possible to embed ECL in

C

programs, and C code into Common Lisp programs.

**GNU Common Lisp (GCL)**

The

GNU

Project's Lisp compiler. Not yet fully ANSI-compliant, GCL is, however, the implementation of choice for several large projects, including the mathematical tools

Maxima

,

AXIOM

, and (historically)

ACL2

. GCL runs on

Linux

under eleven different architectures, and also under Windows, macOS, Solaris, and

FreeBSD

.

**Macintosh Common Lisp (MCL)**

Version 5.2 for Apple Macintosh computers with a PowerPC processor running macOS X is open source. RMCL (based on MCL 5.2) runs on Intel-based Apple Macintosh computers using the Rosetta binary translator from Apple.

**ManKai Common Lisp (MKCL)**

A branch of

ECL

. MKCL emphasises reliability, stability, and overall code quality through a heavily reworked, natively multi-threaded runtime system. On Linux, MKCL features a fully POSIX-compliant runtime system.

**Movitz**

Implements a Lisp environment for

x86

computers without relying on any underlying OS.

**Poplog**

Poplog implements a version of CL, with

POP-11

, and optionally

Prolog

, and

Standard ML

(SML), allowing mixed language programming. For all, the implementation language is POP-11, which is compiled incrementally. It also has an integrated

Emacs

-like editor that communicates with the compiler.

**Steel Bank Common Lisp (SBCL)**

A branch from

CMUCL

. "Broadly speaking, SBCL is distinguished from CMU CL by a greater emphasis on maintainability."

SBCL runs on the platforms CMUCL does, except HP/UX; in addition, it runs on Linux for AMD64, PowerPC, SPARC, MIPS, Windows x86, and AMD64.

SBCL does not use an interpreter by default; all expressions are compiled to native code unless the user switches the interpreter on. The SBCL compiler generates fast native code according to a previous version of

The Computer Language Benchmarks Game

.

**Ufasoft Common Lisp**

Port of CLISP for Windows with core written in C++.

#### Other implementations

**Austin Kyoto Common Lisp**

An evolution of

Kyoto Common Lisp

by

Bill Schelter

.

**Butterfly Common Lisp**

An implementation written in Scheme for the

BBN Butterfly

multi-processor computer.

**CLICC**

A Common Lisp to C compiler.

**CLOE**

Common Lisp for PCs by

Symbolics

.

**Codemist Common Lisp**

Used for the commercial version of the computer algebra system Axiom.

**ExperCommon Lisp**

An early implementation for the Apple Macintosh by ExperTelligence.

**Golden Common Lisp**

An implementation for the PC by GoldHill Inc.

**Ibuki Common Lisp**

A commercialized version of Kyoto Common Lisp.

**Kyoto Common Lisp**

The first Common Lisp compiler that used C as a target language. GCL, ECL and MKCL originate from this Common Lisp implementation.

**L**

A small version of Common Lisp for embedded systems developed by IS Robotics, now iRobot

**Lisp Machines (from Symbolics, TI and Xerox)**

provided implementations of Common Lisp in addition to their native Lisp dialect (Lisp Machine Lisp or Interlisp). CLOS was also available. Symbolics provides an enhanced version Common Lisp.

**Procyon Common Lisp**

An implementation for Windows and macOS, used by Franz for their Windows port of Allegro CL.

**Star Sapphire Common LISP**

An implementation for the PC.

**SubL**

A variant of Common Lisp used for the implementation of the

Cyc

knowledge-based system.

**Top Level Common Lisp**

An early implementation for concurrent execution.

**WCL**

A shared library implementation.

**VAX Common Lisp**

Digital Equipment Corporation

's implementation that ran on

VAX

systems running

VMS

or

ULTRIX

.

**XLISP**

An implementation written by David Betz.


## Applications

Common Lisp is used to develop research applications (often in Artificial Intelligence), for rapid development of prototypes or for deployed applications.

Common Lisp is used in many commercial applications, including the Yahoo! Store web-commerce site, which originally involved Paul Graham and was later rewritten in C++ and Perl. Other notable examples include:

- ACT-R, a cognitive architecture used in a large number of research projects.
- Authorizer's Assistant, a large rule-based system used by American Express, analyzing credit requests.
- Cyc, a long running project to create a knowledge-based system that provides a huge amount of common sense knowledge.
- Gensym G2, a real-time expert system and business rules engine
- Genworks GDL, based on the open-source Gendl kernel.
- The development environment for the *Jak and Daxter* video game series, developed by Naughty Dog.
- ITA Software's low fare search engine, used by travel websites such as Orbitz and Kayak.com and airlines such as American Airlines, Continental Airlines and US Airways.
- Mirai, a 3D graphics suite, known for having been used to design the character of Gollum in The Lords of the Rings movies.
- Opusmodus is a music composition system based on Common Lisp, used in Computer assisted composition.
- Prototype Verification System (PVS), a mechanized environment for formal specification and verification.
- PWGL is a sophisticated visual programming environment based on Common Lisp, used in Computer assisted composition and sound synthesis.
- Piano, a complete aircraft analysis suite, written in Common Lisp, used by companies like Boeing, Airbus, and Northrop Grumman.
- Grammarly, an English-language writing-enhancement platform, has its core grammar engine written in Common Lisp.
- The Dynamic Analysis and Replanning Tool (DART), which is said to alone have paid back during the years from 1991 to 1995 for all thirty years of DARPA investments in AI research.
- NASA's Jet Propulsion Lab's "Deep Space 1", an award-winning Common Lisp program for autopiloting the Deep Space One spaceship.
- SigLab, a Common Lisp platform for signal processing used in missile defense, built by Raytheon.
- NASA's Mars Pathfinder Mission Planning System.
- SPIKE, a scheduling system for Earth or space based observatories and satellites, notably the Hubble Space Telescope, written in Common Lisp.
- Common Lisp has been used for prototyping the garbage collector of Microsoft's .NET Common Language Runtime.
- The original version of Reddit, though the developers later switched to Python due to the lack of libraries for Common Lisp, according to an official blog post by Reddit co-founder Steve Huffman. The reddit v1 source code has been open-sourced and modernized.
- the Hacker News platform, which switched to Common Lisp (with the SBCL implementation) in 2024.

There also exist open-source applications written in Common Lisp, such as:

- ACL2, a full-featured automated theorem prover for an applicative variant of Common Lisp.
- Axiom, a sophisticated computer algebra system.
- the Lem editor, a general-purpose Emacs-like editor written and extensible in Common Lisp.
- Maxima, a sophisticated computer algebra system, based on Macsyma.
- OpenMusic, an object-oriented visual programming environment based on Common Lisp, used in computer assisted composition.
- Pgloader, a data loader for PostgreSQL, which was re-written from Python to Common Lisp.
- Stumpwm, a tiling, keyboard driven X11 Window Manager written entirely in Common Lisp.
- Kandria, an open-source game published on the Steam platform in 2023.
