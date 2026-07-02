---
title: "GNU make (part 17/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 17/17
---

## Index of Concepts

| Jump to: | **!**   **#**   **$**   **%**   *****   **+**   **,**   **-**   **.**   **:**   **=**   **?**   **@**   **[**   **\**   **_**   **~**   **A**   **B**   **C**   **D**   **E**   **F**   **G**   **H**   **I**   **J**   **K**   **L**   **M**   **N**   **O**   **P**   **Q**   **R**   **S**   **T**   **U**   **V**   **W**   **Y** |
|---|---|

Index Entry

Section

!

!=

:

Setting

!=, expansion

:

Reading Makefiles

#

#

(comments), in makefile

:

Makefile Contents

#

(comments), in recipes

:

Recipe Syntax

#include

:

Automatic Prerequisites

$

$

, in function call

:

Syntax of Functions

$

, in rules

:

Rule Syntax

$

, in variable name

:

Computed Names

$

, in variable reference

:

Reference

%

%

, in pattern rules

:

Pattern Intro

%

, quoting in

patsubst

:

Text Functions

%

, quoting in static pattern

:

Static Usage

%

, quoting in

vpath

:

Selective Search

%

, quoting with

\

(backslash)

:

Selective Search

%

, quoting with

\

(backslash)

:

Static Usage

%

, quoting with

\

(backslash)

:

Text Functions

*

*

(wildcard character)

:

Wildcards

+

+, and

define

:

Canned Recipes

+, and recipe execution

:

Instead of Execution

+, and recipes

:

MAKE Variable

+=

:

Appending

+=, expansion

:

Reading Makefiles

+=, expansion

:

Reading Makefiles

,

,v

(RCS file extension)

:

Catalogue of Rules

-

-

(in recipes)

:

Errors

-, and

define

:

Canned Recipes

--always-make

:

Options Summary

--assume-new

:

Instead of Execution

--assume-new

:

Options Summary

--assume-new

, and recursion

:

Options/Recursion

--assume-old

:

Avoiding Compilation

--assume-old

:

Options Summary

--assume-old

, and recursion

:

Options/Recursion

--check-symlink-times

:

Options Summary

--debug

:

Options Summary

--directory

:

Recursion

--directory

:

Options Summary

--directory

, and

--print-directory

:

-w Option

--directory

, and recursion

:

Options/Recursion

--dry-run

:

Echoing

--dry-run

:

Instead of Execution

--dry-run

:

Options Summary

--environment-overrides

:

Options Summary

--eval

:

Options Summary

--file

:

Makefile Names

--file

:

Makefile Arguments

--file

:

Options Summary

--file

, and recursion

:

Options/Recursion

--help

:

Options Summary

--ignore-errors

:

Errors

--ignore-errors

:

Options Summary

--include-dir

:

Include

--include-dir

:

Options Summary

--jobs

:

Parallel

--jobs

:

Options Summary

--jobs

, and recursion

:

Options/Recursion

--jobserver-auth

:

Job Slots

--jobserver-style

:

Options Summary

--jobserver-style

:

POSIX Jobserver

--jobserver-style

for Windows

:

Windows Jobserver

--just-print

:

Echoing

--just-print

:

Instead of Execution

--just-print

:

Options Summary

--keep-going

:

Errors

--keep-going

:

Testing

--keep-going

:

Options Summary

--load-average

:

Parallel

--load-average

:

Options Summary

--makefile

:

Makefile Names

--makefile

:

Makefile Arguments

--makefile

:

Options Summary

--max-load

:

Parallel

--max-load

:

Options Summary

--new-file

:

Instead of Execution

--new-file

:

Options Summary

--new-file

, and recursion

:

Options/Recursion

--no-builtin-rules

:

Options Summary

--no-builtin-variables

:

Options Summary

--no-keep-going

:

Options Summary

--no-print-directory

:

-w Option

--no-print-directory

:

Options Summary

--old-file

:

Avoiding Compilation

--old-file

:

Options Summary

--old-file

, and recursion

:

Options/Recursion

--output-sync

:

Parallel Output

--output-sync

:

Options Summary

--print-data-base

:

Options Summary

--print-directory

:

Options Summary

--print-directory

, and

--directory

:

-w Option

--print-directory

, and recursion

:

-w Option

--print-directory

, disabling

:

-w Option

--question

:

Instead of Execution

--question

:

Options Summary

--quiet

:

Echoing

--quiet

:

Options Summary

--recon

:

Echoing

--recon

:

Instead of Execution

--recon

:

Options Summary

--shuffle

:

Options Summary

--silent

:

Echoing

--silent

:

Options Summary

--stop

:

Options Summary

--touch

:

Instead of Execution

--touch

:

Options Summary

--touch

, and recursion

:

MAKE Variable

--trace

:

Options Summary

--version

:

Options Summary

--warn-undefined-variables

:

Options Summary

--what-if

:

Instead of Execution

--what-if

:

Options Summary

-b

:

Options Summary

-B

:

Options Summary

-C

:

Recursion

-C

:

Options Summary

-C

, and

-w

:

-w Option

-C

, and recursion

:

Options/Recursion

-d

:

Options Summary

-e

:

Options Summary

-E

:

Options Summary

-e

(shell flag)

:

Automatic Prerequisites

-f

:

Makefile Names

-f

:

Makefile Arguments

-f

:

Options Summary

-f

, and recursion

:

Options/Recursion

-h

:

Options Summary

-I

:

Include

-i

:

Errors

-i

:

Options Summary

-I

:

Options Summary

-j

:

Parallel

-j

:

Options Summary

-j

, and archive update

:

Archive Pitfalls

-j

, and recursion

:

Options/Recursion

-k

:

Errors

-k

:

Testing

-k

:

Options Summary

-l

:

Options Summary

-L

:

Options Summary

-l

(library search)

:

Libraries/Search

-l

(load average)

:

Parallel

-m

:

Options Summary

-M

(to compiler)

:

Automatic Prerequisites

-MM

(to GNU compiler)

:

Automatic Prerequisites

-n

:

Echoing

-n

:

Instead of Execution

-n

:

Options Summary

-O

:

Parallel Output

-o

:

Avoiding Compilation

-o

:

Options Summary

-O

:

Options Summary

-o

, and recursion

:

Options/Recursion

-p

:

Options Summary

-q

:

Instead of Execution

-q

:

Options Summary

-r

:

Options Summary

-R

:

Options Summary

-s

:

Echoing

-s

:

Options Summary

-S

:

Options Summary

-t

:

Instead of Execution

-t

:

Options Summary

-t

, and recursion

:

MAKE Variable

-v

:

Options Summary

-W

:

Instead of Execution

-w

:

Options Summary

-W

:

Options Summary

-w

, and

-C

:

-w Option

-W

, and recursion

:

Options/Recursion

-w

, and recursion

:

-w Option

-w

, disabling

:

-w Option

.

.a

(archives)

:

Archive Suffix Rules

.c

:

Catalogue of Rules

.C

:

Catalogue of Rules

.cc

:

Catalogue of Rules

.ch

:

Catalogue of Rules

.cpp

:

Catalogue of Rules

.d

:

Automatic Prerequisites

.def

:

Catalogue of Rules

.dvi

:

Catalogue of Rules

.f

:

Catalogue of Rules

.F

:

Catalogue of Rules

.info

:

Catalogue of Rules

.l

:

Catalogue of Rules

.LIBPATTERNS

, and link libraries

:

Libraries/Search

.ln

:

Catalogue of Rules

.mod

:

Catalogue of Rules

.NOTPARALLEL special target

:

Parallel Disable

.o

:

Catalogue of Rules

.o

:

Catalogue of Rules

.ONESHELL

, use of

:

One Shell

.p

:

Catalogue of Rules

.r

:

Catalogue of Rules

.s

:

Catalogue of Rules

.S

:

Catalogue of Rules

.sh

:

Catalogue of Rules

.SHELLFLAGS

, value of

:

Choosing the Shell

.sym

:

Catalogue of Rules

.tex

:

Catalogue of Rules

.texi

:

Catalogue of Rules

.texinfo

:

Catalogue of Rules

.txinfo

:

Catalogue of Rules

.w

:

Catalogue of Rules

.WAIT special target

:

Parallel Disable

.web

:

Catalogue of Rules

.y

:

Catalogue of Rules

:

::

rules (double-colon)

:

Double-Colon

:::=

:

Immediate Assignment

:::=

:

Setting

::=

:

Simple Assignment

::=

:

Setting

:=

:

Simple Assignment

:=

:

Setting

=

=

:

Recursive Assignment

=

:

Setting

=, expansion

:

Reading Makefiles

?

?

(wildcard character)

:

Wildcards

?=

:

Conditional Assignment

?=

:

Setting

?=, expansion

:

Reading Makefiles

@

@

(in recipes)

:

Echoing

@, and

define

:

Canned Recipes

[

[…]

(wildcard characters)

:

Wildcards

\

\

(backslash), for continuation lines

:

Simple Makefile

\

(backslash), in recipes

:

Splitting Recipe Lines

\

(backslash), to quote

%

:

Selective Search

\

(backslash), to quote

%

:

Static Usage

\

(backslash), to quote

%

:

Text Functions

_

__.SYMDEF

:

Archive Symbols

~

~

(tilde)

:

Wildcards

A

abspath

:

File Name Functions

algorithm for directory search

:

Search Algorithm

all

(standard target)

:

Goals

appending to variables

:

Appending

ar

:

Implicit Variables

archive

:

Archives

archive member targets

:

Archive Members

archive symbol directory updating

:

Archive Symbols

archive, and

-j

:

Archive Pitfalls

archive, and parallel execution

:

Archive Pitfalls

archive, suffix rule for

:

Archive Suffix Rules

Arg list too long

:

Options/Recursion

arguments of functions

:

Syntax of Functions

as

:

Catalogue of Rules

as

:

Implicit Variables

assembly, rule to compile

:

Catalogue of Rules

automatic generation of prerequisites

:

Include

automatic generation of prerequisites

:

Automatic Prerequisites

automatic variables

:

Automatic Variables

automatic variables in prerequisites

:

Automatic Variables

B

backquotes

:

Shell Function

backslash (

\

), for continuation lines

:

Simple Makefile

backslash (

\

), in recipes

:

Splitting Recipe Lines

backslash (

\

), to quote

%

:

Selective Search

backslash (

\

), to quote

%

:

Static Usage

backslash (

\

), to quote

%

:

Text Functions

backslash (

\

), to quote newlines

:

Splitting Lines

backslashes in pathnames and wildcard expansion

:

Wildcard Pitfall

basename

:

File Name Functions

binary packages

:

Install Command Categories

broken pipe

:

Parallel Input

bugs, reporting

:

Bugs

built-in special targets

:

Special Targets

C

C++, rule to compile

:

Catalogue of Rules

C, rule to compile

:

Catalogue of Rules

canned recipes

:

Canned Recipes

cc

:

Catalogue of Rules

cc

:

Implicit Variables

cd

(shell command)

:

Execution

cd

(shell command)

:

MAKE Variable

chains of rules

:

Chained Rules

check

(standard target)

:

Goals

clean

(standard target)

:

Goals

clean

target

:

Simple Makefile

clean

target

:

Cleanup

cleaning up

:

Cleanup

clobber

(standard target)

:

Goals

co

:

Catalogue of Rules

co

:

Implicit Variables

combining rules by prerequisite

:

Combine By Prerequisite

command expansion

:

Shell Function

command line variable definitions, and recursion

:

Options/Recursion

command line variables

:

Overriding

commands, sequences of

:

Canned Recipes

comments, in makefile

:

Makefile Contents

comments, in recipes

:

Recipe Syntax

compatibility

:

Features

compatibility in exporting

:

Variables/Recursion

compilation, testing

:

Testing

computed variable name

:

Computed Names

conditional expansion

:

Conditional Functions

conditional variable assignment

:

Conditional Assignment

conditionals

:

Conditionals

continuation lines

:

Simple Makefile

controlling make

:

Make Control Functions

conventions for makefiles

:

Makefile Conventions

convert guile types

:

Guile Types

ctangle

:

Catalogue of Rules

ctangle

:

Implicit Variables

cweave

:

Catalogue of Rules

cweave

:

Implicit Variables

D

data base of

make

rules

:

Options Summary

deducing recipes (implicit rules)

:

make Deduces

default directories for included makefiles

:

Include

default goal

:

How Make Works

default goal

:

Rules

default makefile name

:

Makefile Names

default rules, last-resort

:

Last Resort

define, expansion

:

Reading Makefiles

defining variables verbatim

:

Multi-Line

deletion of target files

:

Errors

deletion of target files

:

Interrupts

directive

:

Makefile Contents

directories, creating installation

:

Directory Variables

directories, printing them

:

-w Option

directories, updating archive symbol

:

Archive Symbols

directory part

:

File Name Functions

directory search (

VPATH

)

:

Directory Search

directory search (

VPATH

), and implicit rules

:

Implicit/Search

directory search (

VPATH

), and link libraries

:

Libraries/Search

directory search (

VPATH

), and recipes

:

Recipes/Search

directory search algorithm

:

Search Algorithm

directory search, traditional (GPATH)

:

Search Algorithm

disabling parallel execution

:

Parallel Disable

dist

(standard target)

:

Goals

distclean

(standard target)

:

Goals

dollar sign (

$

), in function call

:

Syntax of Functions

dollar sign (

$

), in rules

:

Rule Syntax

dollar sign (

$

), in variable name

:

Computed Names

dollar sign (

$

), in variable reference

:

Reference

DOS, choosing a shell in

:

Choosing the Shell

double-colon rules

:

Double-Colon

duplicate words, removing

:

Text Functions

E

E2BIG

:

Options/Recursion

echoing of recipes

:

Echoing

editor

:

Introduction

Emacs (

M-x compile

)

:

Errors

empty recipes

:

Empty Recipes

empty targets

:

Empty Targets

environment

:

Environment

environment, and recursion

:

Variables/Recursion

environment,

SHELL

in

:

Choosing the Shell

error, stopping on

:

Make Control Functions

errors (in recipes)

:

Errors

errors with wildcards

:

Wildcard Pitfall

evaluating makefile syntax

:

Eval Function

example of loaded objects

:

Loaded Object Example

example using Guile

:

Guile Example

execution, in parallel

:

Parallel

execution, instead of

:

Instead of Execution

execution, of recipes

:

Execution

exit status (errors)

:

Errors

exit status of make

:

Running

expansion, secondary

:

Secondary Expansion

explicit rule, definition of

:

Makefile Contents

explicit rule, expansion

:

Reading Makefiles

explicit rules, secondary expansion of

:

Secondary Expansion

exporting variables

:

Variables/Recursion

extensions, Guile

:

Guile Integration

extensions, load directive

:

load Directive

extensions, loading

:

Loading Objects

F

f77

:

Catalogue of Rules

f77

:

Implicit Variables

FDL, GNU Free Documentation License

:

GNU Free Documentation License

features of GNU

make

:

Features

features, missing

:

Missing

file name functions

:

File Name Functions

file name of makefile

:

Makefile Names

file name of makefile, how to specify

:

Makefile Names

file name prefix, adding

:

File Name Functions

file name suffix

:

File Name Functions

file name suffix, adding

:

File Name Functions

file name with wildcards

:

Wildcards

file name, abspath of

:

File Name Functions

file name, basename of

:

File Name Functions

file name, directory part

:

File Name Functions

file name, nondirectory part

:

File Name Functions

file name, realpath of

:

File Name Functions

file, reading from

:

File Function

file, writing to

:

File Function

files, assuming new

:

Instead of Execution

files, assuming old

:

Avoiding Compilation

files, avoiding recompilation of

:

Avoiding Compilation

files, intermediate

:

Chained Rules

filtering out words

:

Text Functions

filtering words

:

Text Functions

finding strings

:

Text Functions

flags

:

Options Summary

flags for compilers

:

Implicit Variables

flavor of variable

:

Flavor Function

flavors of variables

:

Flavors

FORCE

:

Force Targets

force targets

:

Force Targets

Fortran, rule to compile

:

Catalogue of Rules

function arguments, special characters in

:

Syntax of Functions

functions

:

Functions

functions, for controlling make

:

Make Control Functions

functions, for file names

:

File Name Functions

functions, for text

:

Text Functions

functions, syntax of

:

Syntax of Functions

functions, user defined

:

Call Function

G

g++

:

Catalogue of Rules

g++

:

Implicit Variables

gcc

:

Catalogue of Rules

generating prerequisites automatically

:

Include

generating prerequisites automatically

:

Automatic Prerequisites

get

:

Catalogue of Rules

get

:

Implicit Variables

globbing (wildcards)

:

Wildcards

goal

:

How Make Works

goal, default

:

How Make Works

goal, default

:

Rules

goal, how to specify

:

Goals

grouped targets

:

Multiple Targets

Guile

:

Guile Function

Guile

:

Guile Integration

Guile example

:

Guile Example

guile, conversion of types

:

Guile Types

H

home directory

:

Wildcards

I

IEEE Standard 1003.2

:

Overview

ifdef, expansion

:

Reading Makefiles

ifeq, expansion

:

Reading Makefiles

ifndef, expansion

:

Reading Makefiles

ifneq, expansion

:

Reading Makefiles

immediate variable assignment

:

Immediate Assignment

implicit rule

:

Implicit Rules

implicit rule, and directory search

:

Implicit/Search

implicit rule, and

VPATH

:

Implicit/Search

implicit rule, definition of

:

Makefile Contents

implicit rule, expansion

:

Reading Makefiles

implicit rule, how to use

:

Using Implicit

implicit rule, introduction to

:

make Deduces

implicit rule, predefined

:

Catalogue of Rules

implicit rule, search algorithm

:

Implicit Rule Search

implicit rules, secondary expansion of

:

Secondary Expansion

included makefiles, default directories

:

Include

including (

MAKEFILES

variable)

:

MAKEFILES Variable

including (

MAKEFILE_LIST

variable)

:

Special Variables

including other makefiles

:

Include

incompatibilities

:

Missing

independent targets

:

Multiple Targets

Info, rule to format

:

Catalogue of Rules

inheritance, suppressing

:

Suppressing Inheritance

input during parallel execution

:

Parallel Input

install

(standard target)

:

Goals

installation directories, creating

:

Directory Variables

installations, staged

:

DESTDIR

interface for loaded objects

:

Loaded Object API

intermediate files

:

Chained Rules

intermediate files, preserving

:

Chained Rules

intermediate targets, explicit

:

Special Targets

interrupt

:

Interrupts

J

job slots

:

Parallel

job slots, and recursion

:

Options/Recursion

job slots, sharing

:

Job Slots

jobs, limiting based on load

:

Parallel

jobserver

:

Job Slots

jobserver on POSIX

:

POSIX Jobserver

jobserver on Windows

:

Windows Jobserver

joining lists of words

:

File Name Functions

K

killing (interruption)

:

Interrupts

L

last-resort default rules

:

Last Resort

ld

:

Catalogue of Rules

lex

:

Catalogue of Rules

lex

:

Implicit Variables

Lex, rule to run

:

Catalogue of Rules

libraries for linking, directory search

:

Libraries/Search

library archive, suffix rule for

:

Archive Suffix Rules

limiting jobs based on load

:

Parallel

link libraries, and directory search

:

Libraries/Search

link libraries, patterns matching

:

Libraries/Search

linking, predefined rule for

:

Catalogue of Rules

lint

:

Catalogue of Rules

lint

:

Implicit Variables

lint

, rule to run

:

Catalogue of Rules

list of all prerequisites

:

Automatic Variables

list of changed prerequisites

:

Automatic Variables

load average

:

Parallel

load directive

:

load Directive

loaded object API

:

Loaded Object API

loaded object example

:

Loaded Object Example

loaded object licensing

:

Loaded Object API

loaded objects

:

Loading Objects

loaded objects, remaking of

:

Remaking Loaded Objects

long lines, splitting

:

Splitting Lines

loops in variable expansion

:

Recursive Assignment

lpr

(shell command)

:

Wildcard Examples

lpr

(shell command)

:

Empty Targets

M

m2c

:

Catalogue of Rules

m2c

:

Implicit Variables

macro

:

Using Variables

make depend

:

Automatic Prerequisites

make extensions

:

Extending make

make integration

:

Integrating make

make interface to guile

:

Guile Interface

make procedures in guile

:

Guile Interface

makefile

:

Introduction

makefile name

:

Makefile Names

makefile name, how to specify

:

Makefile Names

makefile rule parts

:

Rule Introduction

makefile syntax, evaluating

:

Eval Function

makefile, and

MAKEFILES

variable

:

MAKEFILES Variable

makefile, conventions for

:

Makefile Conventions

makefile, how

make

processes

:

How Make Works

makefile, how to write

:

Makefiles

makefile, including

:

Include

makefile, overriding

:

Overriding Makefiles

makefile, reading

:

Reading Makefiles

makefile, remaking of

:

Remaking Makefiles

makefile, simple

:

Simple Makefile

makefiles, and

MAKEFILE_LIST

variable

:

Special Variables

makefiles, and special variables

:

Special Variables

makefiles, parsing

:

Parsing Makefiles

makeinfo

:

Catalogue of Rules

makeinfo

:

Implicit Variables

MAKE_TMPDIR

:

Temporary Files

match-anything rule

:

Match-Anything Rules

match-anything rule, used to override

:

Overriding Makefiles

missing features

:

Missing

mistakes with wildcards

:

Wildcard Pitfall

modified variable reference

:

Substitution Refs

Modula-2, rule to compile

:

Catalogue of Rules

mostlyclean

(standard target)

:

Goals

multi-line variable definition

:

Multi-Line

multiple rules for one target

:

Multiple Rules

multiple rules for one target (

::

)

:

Double-Colon

multiple targets

:

Multiple Targets

multiple targets, in pattern rule

:

Pattern Intro

N

name of makefile

:

Makefile Names

name of makefile, how to specify

:

Makefile Names

nested variable reference

:

Computed Names

newline, quoting, in makefile

:

Simple Makefile

newline, quoting, in recipes

:

Splitting Recipe Lines

nondirectory part

:

File Name Functions

normal prerequisites

:

Prerequisite Types

not intermediate targets, explicit

:

Special Targets

O

obj

:

Variables Simplify

OBJ

:

Variables Simplify

objects

:

Variables Simplify

OBJECTS

:

Variables Simplify

objects, loaded

:

Loading Objects

objs

:

Variables Simplify

OBJS

:

Variables Simplify

old-fashioned suffix rules

:

Suffix Rules

options

:

Options Summary

options, and recursion

:

Options/Recursion

options, setting from environment

:

Options/Recursion

options, setting in makefiles

:

Options/Recursion

order of pattern rules

:

Pattern Match

order-only prerequisites

:

Prerequisite Types

origin of variable

:

Origin Function

output during parallel execution

:

Parallel Output

output during parallel execution

:

Options Summary

overriding makefiles

:

Overriding Makefiles

overriding variables with arguments

:

Overriding

overriding with

override

:

Override Directive

P

parallel execution

:

Parallel

parallel execution, and archive update

:

Archive Pitfalls

parallel execution, disabling

:

Parallel Disable

parallel execution, input during

:

Parallel Input

parallel execution, output during

:

Parallel Output

parallel execution, output during

:

Options Summary

parallel execution, overriding

:

Special Targets

parallel output to terminal

:

Terminal Output

parsing makefiles

:

Parsing Makefiles

parts of makefile rule

:

Rule Introduction

Pascal, rule to compile

:

Catalogue of Rules

pattern rule

:

Pattern Intro

pattern rule, expansion

:

Reading Makefiles

pattern rules, order of

:

Pattern Match

pattern rules, static (not implicit)

:

Static Pattern

pattern rules, static, syntax of

:

Static Usage

pattern-specific variables

:

Pattern-specific

pc

:

Catalogue of Rules

pc

:

Implicit Variables

phony targets

:

Phony Targets

phony targets and recipe execution

:

Instead of Execution

pitfalls of wildcards

:

Wildcard Pitfall

plugin_is_GPL_compatible

:

Loaded Object API

portability

:

Features

POSIX

:

Overview

POSIX

:

Options/Recursion

POSIX-conforming mode, setting

:

Special Targets

post-installation commands

:

Install Command Categories

pre-installation commands

:

Install Command Categories

precious targets

:

Special Targets

predefined rules and variables, printing

:

Options Summary

prefix, adding

:

File Name Functions

prerequisite

:

Rules

prerequisite pattern, implicit

:

Pattern Intro

prerequisite pattern, static (not implicit)

:

Static Usage

prerequisite types

:

Prerequisite Types

prerequisite, expansion

:

Reading Makefiles

prerequisites

:

Rule Syntax

prerequisites, and automatic variables

:

Automatic Variables

prerequisites, automatic generation

:

Include

prerequisites, automatic generation

:

Automatic Prerequisites

prerequisites, introduction to

:

Rule Introduction

prerequisites, list of all

:

Automatic Variables

prerequisites, list of changed

:

Automatic Variables

prerequisites, normal

:

Prerequisite Types

prerequisites, order-only

:

Prerequisite Types

prerequisites, varying (static pattern)

:

Static Pattern

preserving intermediate files

:

Chained Rules

preserving with

.PRECIOUS

:

Special Targets

preserving with

.SECONDARY

:

Special Targets

print

(standard target)

:

Goals

print

target

:

Wildcard Examples

print

target

:

Empty Targets

printing directories

:

-w Option

printing messages

:

Make Control Functions

printing of recipes

:

Echoing

printing user warnings

:

Make Control Functions

problems and bugs, reporting

:

Bugs

problems with wildcards

:

Wildcard Pitfall

processing a makefile

:

How Make Works

Q

question mode

:

Instead of Execution

quoting

%

, in

patsubst

:

Text Functions

quoting

%

, in static pattern

:

Static Usage

quoting

%

, in

vpath

:

Selective Search

quoting newline, in makefile

:

Simple Makefile

quoting newline, in recipes

:

Splitting Recipe Lines

R

Ratfor, rule to compile

:

Catalogue of Rules

RCS, rule to extract from

:

Catalogue of Rules

reading from a file

:

File Function

reading makefiles

:

Reading Makefiles

README

:

Makefile Names

realclean

(standard target)

:

Goals

realpath

:

File Name Functions

recipe

:

Simple Makefile

recipe execution, single invocation

:

Special Targets

recipe lines, single shell

:

One Shell

recipe syntax

:

Recipe Syntax

recipe, execution

:

Execution

recipes

:

Rule Syntax

recipes

:

Recipes

recipes setting shell variables

:

Execution

recipes, and directory search

:

Recipes/Search

recipes, backslash (

\

) in

:

Splitting Recipe Lines

recipes, canned

:

Canned Recipes

recipes, comments in

:

Recipe Syntax

recipes, echoing

:

Echoing

recipes, empty

:

Empty Recipes

recipes, errors in

:

Errors

recipes, execution in parallel

:

Parallel

recipes, how to write

:

Recipes

recipes, instead of executing

:

Instead of Execution

recipes, introduction to

:

Rule Introduction

recipes, quoting newlines in

:

Splitting Recipe Lines

recipes, splitting

:

Splitting Recipe Lines

recipes, using variables in

:

Variables in Recipes

recompilation

:

Introduction

recompilation, avoiding

:

Avoiding Compilation

recording events with empty targets

:

Empty Targets

recursion

:

Recursion

recursion, and

-C

:

Options/Recursion

recursion, and

-f

:

Options/Recursion

recursion, and

-j

:

Options/Recursion

recursion, and

-o

:

Options/Recursion

recursion, and

-t

:

MAKE Variable

recursion, and

-W

:

Options/Recursion

recursion, and

-w

:

-w Option

recursion, and command line variable definitions

:

Options/Recursion

recursion, and environment

:

Variables/Recursion

recursion, and

MAKE

variable

:

MAKE Variable

recursion, and

MAKEFILES

variable

:

MAKEFILES Variable

recursion, and options

:

Options/Recursion

recursion, and printing directories

:

-w Option

recursion, and variables

:

Variables/Recursion

recursion, level of

:

Variables/Recursion

recursive variable expansion

:

Using Variables

recursive variable expansion

:

Flavors

recursively expanded variables

:

Flavors

reference to variables

:

Reference

reference to variables

:

Advanced

relinking

:

How Make Works

remaking loaded objects

:

Remaking Loaded Objects

remaking makefiles

:

Remaking Makefiles

removal of target files

:

Errors

removal of target files

:

Interrupts

removing duplicate words

:

Text Functions

removing targets on failure

:

Special Targets

removing whitespace from split lines

:

Splitting Lines

removing, to clean up

:

Cleanup

reporting bugs

:

Bugs

rm

:

Implicit Variables

rm

(shell command)

:

Simple Makefile

rm

(shell command)

:

Wildcard Examples

rm

(shell command)

:

Phony Targets

rm

(shell command)

:

Errors

rule prerequisites

:

Rule Syntax

rule syntax

:

Rule Syntax

rule targets

:

Rule Syntax

rule, double-colon (

::

)

:

Double-Colon

rule, explicit, definition of

:

Makefile Contents

rule, how to write

:

Rules

rule, implicit

:

Implicit Rules

rule, implicit, and directory search

:

Implicit/Search

rule, implicit, and

VPATH

:

Implicit/Search

rule, implicit, chains of

:

Chained Rules

rule, implicit, definition of

:

Makefile Contents

rule, implicit, how to use

:

Using Implicit

rule, implicit, introduction to

:

make Deduces

rule, implicit, predefined

:

Catalogue of Rules

rule, introduction to

:

Rule Introduction

rule, multiple for one target

:

Multiple Rules

rule, no recipe or prerequisites

:

Force Targets

rule, pattern

:

Pattern Intro

rule, static pattern

:

Static Pattern

rule, static pattern versus implicit

:

Static versus Implicit

rule, with multiple targets

:

Multiple Targets

rules, and

$

:

Rule Syntax

S

s.

(SCCS file prefix)

:

Catalogue of Rules

SCCS, rule to extract from

:

Catalogue of Rules

search algorithm, implicit rule

:

Implicit Rule Search

search path for prerequisites (

VPATH

)

:

Directory Search

search path for prerequisites (

VPATH

), and implicit rules

:

Implicit/Search

search path for prerequisites (

VPATH

), and link libraries

:

Libraries/Search

searching for strings

:

Text Functions

secondary expansion

:

Secondary Expansion

secondary expansion and explicit rules

:

Secondary Expansion

secondary expansion and implicit rules

:

Secondary Expansion

secondary expansion and static pattern rules

:

Secondary Expansion

secondary files

:

Chained Rules

secondary targets

:

Special Targets

sed

(shell command)

:

Automatic Prerequisites

selecting a word

:

Text Functions

selecting word lists

:

Text Functions

sequences of commands

:

Canned Recipes

setting options from environment

:

Options/Recursion

setting options in makefiles

:

Options/Recursion

setting variables

:

Setting

several rules for one target

:

Multiple Rules

several targets in a rule

:

Multiple Targets

shar

(standard target)

:

Goals

shell command, function for

:

Shell Function

shell file name pattern (in

include

)

:

Include

shell variables, setting in recipes

:

Execution

shell wildcards (in

include

)

:

Include

shell, choosing the

:

Choosing the Shell

SHELL, exported value

:

Variables/Recursion

SHELL, import from environment

:

Environment

shell, in DOS and Windows

:

Choosing the Shell

SHELL

, MS-DOS specifics

:

Choosing the Shell

SHELL

, value of

:

Choosing the Shell

signal

:

Interrupts

silent operation

:

Echoing

simple makefile

:

Simple Makefile

simple variable expansion

:

Using Variables

simplifying with variables

:

Variables Simplify

simply expanded variables

:

Simple Assignment

sorting words

:

Text Functions

spaces, in variable values

:

Simple Assignment

spaces, stripping

:

Text Functions

special characters in function arguments

:

Syntax of Functions

special targets

:

Special Targets

special variables

:

Special Variables

specifying makefile name

:

Makefile Names

splitting long lines

:

Splitting Lines

splitting recipes

:

Splitting Recipe Lines

staged installs

:

DESTDIR

standard input

:

Parallel Input

standards conformance

:

Overview

standards for makefiles

:

Makefile Conventions

static pattern rule

:

Static Pattern

static pattern rule, syntax of

:

Static Usage

static pattern rule, versus implicit

:

Static versus Implicit

static pattern rules, secondary expansion of

:

Secondary Expansion

stem

:

Static Usage

stem

:

Pattern Match

stem, shortest

:

Pattern Match

stem, variable for

:

Automatic Variables

stopping make

:

Make Control Functions

strings, searching for

:

Text Functions

stripping whitespace

:

Text Functions

sub-

make

:

Variables/Recursion

subdirectories, recursion for

:

Recursion

substitution variable reference

:

Substitution Refs

suffix rule

:

Suffix Rules

suffix rule, for archive

:

Archive Suffix Rules

suffix, adding

:

File Name Functions

suffix, function to find

:

File Name Functions

suffix, substituting in variables

:

Substitution Refs

suppressing inheritance

:

Suppressing Inheritance

switches

:

Options Summary

symbol directories, updating archive

:

Archive Symbols

syntax of recipe

:

Recipe Syntax

syntax of rules

:

Rule Syntax

T

tab character (in commands)

:

Rule Syntax

tabs in rules

:

Rule Introduction

TAGS

(standard target)

:

Goals

tangle

:

Catalogue of Rules

tangle

:

Implicit Variables

tar

(standard target)

:

Goals

target

:

Rules

target pattern, implicit

:

Pattern Intro

target pattern, static (not implicit)

:

Static Usage

target, deleting on error

:

Errors

target, deleting on interrupt

:

Interrupts

target, expansion

:

Reading Makefiles

target, multiple in pattern rule

:

Pattern Intro

target, multiple rules for one

:

Multiple Rules

target, touching

:

Instead of Execution

target-specific variables

:

Target-specific

targets

:

Rule Syntax

targets without a file

:

Phony Targets

targets, built-in special

:

Special Targets

targets, empty

:

Empty Targets

targets, force

:

Force Targets

targets, grouped

:

Multiple Targets

targets, independent

:

Multiple Targets

targets, introduction to

:

Rule Introduction

targets, multiple

:

Multiple Targets

targets, phony

:

Phony Targets

TEMP

:

Temporary Files

temporary files

:

Temporary Files

terminal rule

:

Match-Anything Rules

terminal, output to

:

Terminal Output

test

(standard target)

:

Goals

testing compilation

:

Testing

tex

:

Catalogue of Rules

tex

:

Implicit Variables

TeX, rule to run

:

Catalogue of Rules

texi2dvi

:

Catalogue of Rules

texi2dvi

:

Implicit Variables

Texinfo, rule to format

:

Catalogue of Rules

tilde (

~

)

:

Wildcards

TMP

:

Temporary Files

TMPDIR

:

Temporary Files

tools, sharing job slots

:

Job Slots

touch

(shell command)

:

Wildcard Examples

touch

(shell command)

:

Empty Targets

touching files

:

Instead of Execution

traditional directory search (GPATH)

:

Search Algorithm

types of prerequisites

:

Prerequisite Types

types, conversion of

:

Guile Types

U

undefined variables, warning message

:

Options Summary

undefining variable

:

Undefine Directive

updating archive symbol directories

:

Archive Symbols

updating loaded objects

:

Remaking Loaded Objects

updating makefiles

:

Remaking Makefiles

user defined functions

:

Call Function

V

value

:

Using Variables

value, how a variable gets it

:

Values

variable

:

Using Variables

variable definition

:

Makefile Contents

variable references in recipes

:

Variables in Recipes

variables

:

Variables Simplify

variables, ‘

$

’ in name

:

Computed Names

variables, and implicit rule

:

Automatic Variables

variables, appending to

:

Appending

variables, automatic

:

Automatic Variables

variables, command line

:

Overriding

variables, command line, and recursion

:

Options/Recursion

variables, computed names

:

Computed Names

variables, conditional assignment

:

Conditional Assignment

variables, defining verbatim

:

Multi-Line

variables, environment

:

Variables/Recursion

variables, environment

:

Environment

variables, exporting

:

Variables/Recursion

variables, flavor of

:

Flavor Function

variables, flavors

:

Flavors

variables, how they get their values

:

Values

variables, how to reference

:

Reference

variables, immediate assignment

:

Immediate Assignment

variables, local

:

Let Function

variables, loops in expansion

:

Recursive Assignment

variables, modified reference

:

Substitution Refs

variables, multi-line

:

Multi-Line

variables, nested references

:

Computed Names

variables, origin of

:

Origin Function

variables, overriding

:

Override Directive

variables, overriding with arguments

:

Overriding

variables, pattern-specific

:

Pattern-specific

variables, recursively expanded

:

Flavors

variables, setting

:

Setting

variables, simply expanded

:

Simple Assignment

variables, spaces in values

:

Simple Assignment

variables, substituting suffix in

:

Substitution Refs

variables, substitution reference

:

Substitution Refs

variables, target-specific

:

Target-specific

variables, unexpanded value

:

Value Function

variables, warning for undefined

:

Options Summary

varying prerequisites

:

Static Pattern

verbatim variable definition

:

Multi-Line

vpath

:

Directory Search

VPATH

, and implicit rules

:

Implicit/Search

VPATH

, and link libraries

:

Libraries/Search

W

warnings, printing

:

Make Control Functions

weave

:

Catalogue of Rules

weave

:

Implicit Variables

Web, rule to run

:

Catalogue of Rules

what if

:

Instead of Execution

whitespace, avoiding on line split

:

Splitting Lines

whitespace, in variable values

:

Simple Assignment

whitespace, stripping

:

Text Functions

wildcard

:

Wildcards

wildcard pitfalls

:

Wildcard Pitfall

wildcard, function

:

File Name Functions

wildcard, in archive member

:

Archive Members

wildcard, in

include

:

Include

wildcards and MS-DOS/MS-Windows backslashes

:

Wildcard Pitfall

Windows, choosing a shell in

:

Choosing the Shell

word, selecting a

:

Text Functions

words, extracting first

:

Text Functions

words, extracting last

:

Text Functions

words, filtering

:

Text Functions

words, filtering out

:

Text Functions

words, finding number

:

Text Functions

words, iterating over

:

Foreach Function

words, joining lists

:

File Name Functions

words, removing duplicates

:

Text Functions

words, selecting lists of

:

Text Functions

writing recipes

:

Recipes

writing rules

:

Rules

writing to a file

:

File Function

Y

yacc

:

Catalogue of Rules

yacc

:

Implicit Variables

yacc

:

Canned Recipes

Yacc, rule to run

:

Catalogue of Rules

| Jump to: | **!**   **#**   **$**   **%**   *****   **+**   **,**   **-**   **.**   **:**   **=**   **?**   **@**   **[**   **\**   **_**   **~**   **A**   **B**   **C**   **D**   **E**   **F**   **G**   **H**   **I**   **J**   **K**   **L**   **M**   **N**   **O**   **P**   **Q**   **R**   **S**   **T**   **U**   **V**   **W**   **Y** |
|---|---|

Previous: Index of Concepts, Up: GNU `make`   [Contents][Index]


## Index of Functions, Variables, & Directives

| Jump to: | **$**   **%**   *****   **+**   **-**   **.**   **/**   **<**   **?**   **@**   **^**   **\|**   **A**   **B**   **C**   **D**   **E**   **F**   **G**   **I**   **J**   **L**   **M**   **N**   **O**   **P**   **R**   **S**   **T**   **U**   **V**   **W**   **Y** |
|---|---|

Index Entry

Section

$

$%

:

Automatic Variables

$(%D)

:

Automatic Variables

$(%F)

:

Automatic Variables

$(*D)

:

Automatic Variables

$(*F)

:

Automatic Variables

$(+D)

:

Automatic Variables

$(+F)

:

Automatic Variables

$(<D)

:

Automatic Variables

$(<F)

:

Automatic Variables

$(?D)

:

Automatic Variables

$(?F)

:

Automatic Variables

$(@D)

:

Automatic Variables

$(@F)

:

Automatic Variables

$(^D)

:

Automatic Variables

$(^F)

:

Automatic Variables

$*

:

Automatic Variables

$*

, and static pattern

:

Static Usage

$+

:

Automatic Variables

$<

:

Automatic Variables

$?

:

Automatic Variables

$@

:

Automatic Variables

$^

:

Automatic Variables

$|

:

Automatic Variables

%

%

(automatic variable)

:

Automatic Variables

%D

(automatic variable)

:

Automatic Variables

%F

(automatic variable)

:

Automatic Variables

*

*

(automatic variable)

:

Automatic Variables

*

(automatic variable), unsupported bizarre usage

:

Missing

*D

(automatic variable)

:

Automatic Variables

*F

(automatic variable)

:

Automatic Variables

+

+

(automatic variable)

:

Automatic Variables

+D

(automatic variable)

:

Automatic Variables

+F

(automatic variable)

:

Automatic Variables

-

-load

:

load Directive

.

.DEFAULT

:

Special Targets

.DEFAULT

:

Last Resort

.DEFAULT

, and empty recipes

:

Empty Recipes

.DEFAULT_GOAL

(define default goal)

:

Special Variables

.DELETE_ON_ERROR

:

Special Targets

.DELETE_ON_ERROR

:

Errors

.EXPORT_ALL_VARIABLES

:

Special Targets

.EXPORT_ALL_VARIABLES

:

Variables/Recursion

.EXTRA_PREREQS

(prerequisites not added to automatic variables)

:

Special Variables

.FEATURES

(list of supported features)

:

Special Variables

.IGNORE

:

Special Targets

.IGNORE

:

Errors

.INCLUDE_DIRS

(list of include directories)

:

Special Variables

.INTERMEDIATE

:

Special Targets

.LIBPATTERNS

:

Libraries/Search

.LOADED

:

load Directive

.LOW_RESOLUTION_TIME

:

Special Targets

.NOTINTERMEDIATE

:

Special Targets

.NOTPARALLEL

:

Special Targets

.NOTPARALLEL

:

Parallel Disable

.ONESHELL

:

Special Targets

.ONESHELL

:

One Shell

.PHONY

:

Phony Targets

.PHONY

:

Special Targets

.POSIX

:

Special Targets

.POSIX

:

Options/Recursion

.PRECIOUS

:

Special Targets

.PRECIOUS

:

Interrupts

.RECIPEPREFIX

(change the recipe prefix character)

:

Special Variables

.SECONDARY

:

Special Targets

.SECONDEXPANSION

:

Secondary Expansion

.SECONDEXPANSION

:

Special Targets

.SHELLFLAGS

:

Choosing the Shell

.SHELLFLAGS

:

Choosing the Shell

.SHELLSTATUS

:

Shell Function

.SILENT

:

Special Targets

.SILENT

:

Echoing

.SUFFIXES

:

Special Targets

.SUFFIXES

:

Suffix Rules

.VARIABLES

(list of variables)

:

Special Variables

.WAIT

:

Parallel Disable

/

/usr/gnu/include

:

Include

/usr/include

:

Include

/usr/local/include

:

Include

<

<

(automatic variable)

:

Automatic Variables

<D

(automatic variable)

:

Automatic Variables

<F

(automatic variable)

:

Automatic Variables

?

?

(automatic variable)

:

Automatic Variables

?D

(automatic variable)

:

Automatic Variables

?F

(automatic variable)

:

Automatic Variables

@

@

(automatic variable)

:

Automatic Variables

@D

(automatic variable)

:

Automatic Variables

@F

(automatic variable)

:

Automatic Variables

^

^

(automatic variable)

:

Automatic Variables

^D

(automatic variable)

:

Automatic Variables

^F

(automatic variable)

:

Automatic Variables

|

|

(automatic variable)

:

Automatic Variables

A

abspath

:

File Name Functions

addprefix

:

File Name Functions

addsuffix

:

File Name Functions

and

:

Conditional Functions

AR

:

Implicit Variables

ARFLAGS

:

Implicit Variables

AS

:

Implicit Variables

ASFLAGS

:

Implicit Variables

B

basename

:

File Name Functions

bindir

:

Directory Variables

C

call

:

Call Function

CC

:

Implicit Variables

CFLAGS

:

Implicit Variables

CO

:

Implicit Variables

COFLAGS

:

Implicit Variables

COMSPEC

:

Choosing the Shell

CPP

:

Implicit Variables

CPPFLAGS

:

Implicit Variables

CTANGLE

:

Implicit Variables

CURDIR

:

Recursion

CWEAVE

:

Implicit Variables

CXX

:

Implicit Variables

CXXFLAGS

:

Implicit Variables

D

define

:

Multi-Line

DESTDIR

:

DESTDIR

dir

:

File Name Functions

E

else

:

Conditional Syntax

endef

:

Multi-Line

endif

:

Conditional Syntax

error

:

Make Control Functions

eval

:

Eval Function

exec_prefix

:

Directory Variables

export

:

Variables/Recursion

F

FC

:

Implicit Variables

FFLAGS

:

Implicit Variables

file

:

File Function

filter

:

Text Functions

filter-out

:

Text Functions

findstring

:

Text Functions

firstword

:

Text Functions

flavor

:

Flavor Function

foreach

:

Foreach Function

G

GET

:

Implicit Variables

GFLAGS

:

Implicit Variables

gmk-eval

:

Guile Interface

gmk-expand

:

Guile Interface

gmk_add_function

:

Loaded Object API

gmk_alloc

:

Loaded Object API

gmk_eval

:

Loaded Object API

gmk_expand

:

Loaded Object API

gmk_free

:

Loaded Object API

gmk_func_ptr

:

Loaded Object API

GNUmakefile

:

Makefile Names

GPATH

:

Search Algorithm

guile

:

Guile Function

I

if

:

Conditional Functions

if

:

Conditional Functions

ifdef

:

Conditional Syntax

ifeq

:

Conditional Syntax

ifndef

:

Conditional Syntax

ifneq

:

Conditional Syntax

include

:

Include

info

:

Make Control Functions

intcmp

:

Conditional Functions

J

join

:

File Name Functions

L

lastword

:

Text Functions

LDFLAGS

:

Implicit Variables

LDLIBS

:

Implicit Variables

let

:

Let Function

LEX

:

Implicit Variables

LFLAGS

:

Implicit Variables

libexecdir

:

Directory Variables

LINT

:

Implicit Variables

LINTFLAGS

:

Implicit Variables

load

:

load Directive

LOADLIBES

:

Implicit Variables

M

M2C

:

Implicit Variables

MAKE

:

MAKE Variable

MAKE

:

Simple Assignment

MAKECMDGOALS

:

Goals

Makefile

:

Makefile Names

makefile

:

Makefile Names

MAKEFILES

:

MAKEFILES Variable

MAKEFILES

:

Variables/Recursion

MAKEFILE_LIST

(list of parsed makefiles)

:

Special Variables

MAKEFLAGS

:

Options/Recursion

MAKEINFO

:

Implicit Variables

MAKELEVEL

:

Variables/Recursion

MAKELEVEL

:

Simple Assignment

MAKEOVERRIDES

:

Options/Recursion

MAKESHELL

(MS-DOS alternative to

SHELL

)

:

Choosing the Shell

MAKE_HOST

:

Quick Reference

MAKE_RESTARTS

(number of times

make

has restarted)

:

Special Variables

MAKE_TERMERR

(whether stderr is a terminal)

:

Special Variables

MAKE_TERMOUT

(whether stdout is a terminal)

:

Special Variables

MAKE_VERSION

:

Quick Reference

MFLAGS

:

Options/Recursion

N

notdir

:

File Name Functions

O

or

:

Conditional Functions

origin

:

Origin Function

OUTPUT_OPTION

:

Catalogue of Rules

override

:

Override Directive

P

patsubst

:

Substitution Refs

patsubst

:

Text Functions

PC

:

Implicit Variables

PFLAGS

:

Implicit Variables

prefix

:

Directory Variables

private

:

Suppressing Inheritance

R

realpath

:

File Name Functions

RFLAGS

:

Implicit Variables

RM

:

Implicit Variables

S

sbindir

:

Directory Variables

SHELL

:

Choosing the Shell

SHELL

:

Choosing the Shell

shell

:

Shell Function

SHELL

(recipe execution)

:

Execution

sort

:

Text Functions

strip

:

Text Functions

subst

:

Multiple Targets

subst

:

Text Functions

suffix

:

File Name Functions

SUFFIXES

:

Suffix Rules

T

TANGLE

:

Implicit Variables

TEX

:

Implicit Variables

TEXI2DVI

:

Implicit Variables

U

undefine

:

Undefine Directive

unexport

:

Variables/Recursion

V

value

:

Value Function

VPATH

:

Directory Search

VPATH

:

General Search

vpath

:

Directory Search

vpath

:

Selective Search

W

warning

:

Make Control Functions

WEAVE

:

Implicit Variables

wildcard

:

Wildcard Function

wildcard

:

File Name Functions

word

:

Text Functions

wordlist

:

Text Functions

words

:

Text Functions

Y

YACC

:

Implicit Variables

YFLAGS

:

Implicit Variables

| Jump to: | **$**   **%**   *****   **+**   **-**   **.**   **/**   **<**   **?**   **@**   **^**   **\|**   **A**   **B**   **C**   **D**   **E**   **F**   **G**   **I**   **J**   **L**   **M**   **N**   **O**   **P**   **R**   **S**   **T**   **U**   **V**   **W**   **Y** |
|---|---|
