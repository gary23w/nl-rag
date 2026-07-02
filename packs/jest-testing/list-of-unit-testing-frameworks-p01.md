---
title: "List of unit testing frameworks (part 1/4)"
source: https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks
domain: jest-testing
license: CC-BY-SA-4.0
tags: jest testing, javascript testing, test runner, mock functions
fetched: 2026-07-02
part: 1/4
---

# List of unit testing frameworks

This is a list of notable test automation frameworks commonly used for unit testing. Such frameworks are not limited to unit-level testing; they can be used for integration and system level testing.

Frameworks are grouped below. For unit testing, a framework must be the same language as the source code under test, and therefore, grouping frameworks by language is valuable. But some groupings transcend language. For example, .NET groups frameworks that work for any language supported for .NET, and HTTP groups frameworks that test an HTTP server regardless of the implementation language on the server.


## Columns

The columns in the tables below are described here.

- **Name**: Name of the framework
- **xUnit**: Whether classified as xUnit
- **TAP**: Whether can emit Test Anything Protocol (TAP) output
- **Generators**: Whether supports data generators – generating test input data and running a test with the generated data
- **Fixtures**: Whether supports test local fixtures – associating a test environment with a single test
- **Group fixtures**: Whether supports group fixtures – associating a test environment with a group of tests

Some columns do not apply to some groupings and are therefore omitted from that groupings table.

## Groups

### ABAP

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| ABAP Unit | Yes |   | since SAP NetWeaver 2004 |
| TEST.easy |   |   | since SAP NetWeaver 7.02 SP13 |

### Active Server Pages (ASP)

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| ASPUnit |   |   |   |

### Ada

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| AUnit | Yes |   |   |
| AdaTEST 95 | No |   |   |
| Ahven |   |   |   |
| TBrun |   |   |   |
| VectorCAST/Ada | No |   |   |
| RTRT |   |   |   |

### Ant

For Apache Ant tasks.

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| AntUnit |   |   |   |

### AppleScript

For AppleScript.

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| ASUnit | Yes |   | influenced by SUnit, ASTest and Python unittest |
| ASTest | Yes |   |   |

### ASCET

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| TPT | Yes |   | Model based physical stimulation and implemented stimulation |

### Bash

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| shUnit2 | Yes |   | an xUnit unit test framework for Bourne-based shell scripts |
| bats-core |   |   | Bats-Core: Bash Automated Testing System |
| ShellSpec |   |   | BDD style unit testing framework. Supports all POSIX compliant shells including Bash, Dash, Ksh and Zsh. Nestable blocks that realize local scope and easy mocking. Parallel execution. RSpec-like/TAP/JUnit XML Reporter. Code coverage integration. MIT license. |
| bash_unit |   |   | bash unit testing enterprise edition framework. GPL-3.0 License. |
| bach |   |   | Bach is a testing framework for Bash that provides the possibility to write unit tests for your Bash scripts. |

### BASIC

#### Visual Basic (VB6.0)

For unit testing frameworks for VB.NET, see .NET languages.

| Name | xUnit | License | Source | Remarks |
|---|---|---|---|---|
| vbUnit |   | Commercial |   | Visual Basic and COM objects |
| vbUnitFree |   | LGPL |   | Visual Basic and COM objects |
| VbaUnit |   | BSD |   | Visual Basic for Applications |
| ExcelVbaUnit |   | LGPL |   | Similar to VbaUnit, but specifically for testing Excel VBA (written as an Excel add-in) |
| TinyUnit |   |   |   | Visual Basic 6, VB .NET, and PHP5 |
| SimplyVBUnit | Yes | MIT |   | VB6 Unit Testing Framework modeled after the popular NUnit for .NET |
| VBLiteUnit |   | BSD |   | Visual Basic and COM objects |

#### Xojo (REALbasic)

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| RBUnit | No |   |   |
| XojoUnit | Yes |   | Unit testing framework for Xojo that works with Desktop, Web and iOS project types. |

### Business Process Execution Language (BPEL)

| Name | xUnit | Source | Remarks |
|---|---|---|---|
| BPELUnit |   |   |   |

### C

Name

xUnit

TAP

Fixtures

Group fixtures

Generators

Year

Source

License

Remarks

AceUnit

Yes

Yes

2007

BSD license

Is JUnit 4.x style, easy, modular and flexible. It can be used in resource constrained environments, e.g., embedded software development, and PCs, workstations, servers (Windows and Unix).

AcuTest

Yes

Yes

MIT

Simple, straightforward, fast. Single .h file. Used in the Apache Portable Runtime Library. Renamed from CUTest.

API Sanity Checker

Yes

Yes (spectypes)

Yes (spectypes)

Yes

2009

LGPL

Unit test generator for C/C++ libraries. Can automatically generate reasonable input data for every API function.

Automated Testing Framework

2007

BSD

Originally developed for the NetBSD operating system but works well in most Unix-like platforms. Ability to install tests as part of a release.

BDD-for-C

Yes

MIT

BDD test framework with TAP output in a single header file.

Cantata++

No

Yes

Yes

Yes

Proprietary

Automated unit and integration testing tool for C. Certified testing for host or embedded systems. Code coverage and unique call interface control to simulate and intercept calls.

Catsrunner

GPL

Unit testing framework for cross-platform embedded development.

CBDD

Yes

Yes

Apache License

libcbdd is a block-based

Behavior-driven development

library which allows for very readable tests. Tests are written inside main functions. Works only with clang and the libblocksruntime extension.

cfix

Yes

LGPL

Specialized for Windows development—both Win32 and NT kernel mode. Compatible to WinUnit.

Cgreen

Yes

ISC

Unit test framework including strict and loose

mocks

, auto-discovering of tests, suites, BDD-ish style notation, test protected against exceptions, "natural language" output, extensible reporter, learning mocks to discover actual values sent to a mock.

CHEAT

Yes

2012

BSD

Header-only unit testing framework. Multi-platform. Supports running each test in a separate process. Works without needing to "register" test cases.

Check

Yes

Yes

Yes

Yes

2001

LGPL

Check features a simple interface for defining unit tests, putting little in the way of the developer. Tests are run in a separate process, so Check can catch both assertion failures and code errors that cause segmentation faults or other signals. The output from unit tests can be used within source code editors and IDEs. Can output to multiple formats, like the TAP format, JUnit XML or SubUnit. Supports Linux, macOS, FreeBSD, Windows.

Cmocka

Yes

Yes

Yes

Yes

2012

Apache License 2.0

CMocka is a test framework for C with support for mock objects. It's easy to use and setup. CMocka is forked from and a successor to cmockery, which was developed by Google but has been unmaintained for some time. Can output to multiple formats, like the TAP format, JUnit XML, or SubUnit.

Cmockery

Yes

2008

Apache License 2.0

Google

sponsored project.

CppUTest

Yes

Yes

No

Yes

3-clause BSD

Limited C++ set by design to keep usage easy and allow it to work on embedded platforms. C++ is buried in macros so the learning curve for C programmers is minimal. Ported to Symbian. Has a mocking support library CppUMock

Criterion

Yes

Yes

Yes

Yes

Yes

MIT

Unit testing framework with automatic test registration. Supports theories and parameterized tests. Each test is run in its own process, so signals and crashes can be reported. Can output to multiple formats, like the

TAP

format or JUnit XML. Supports Linux, macOS, FreeBSD, Windows.

CU

3-clause BSD

CU is a simple unit testing framework for handling automated tests in C.

CTest

Yes

Yes

Yes

Apache License 2.0

Ctest is a framework with some special features: formatted output for easy parsing, easy to use.

CUnit

Yes

2001

LGPL

OS independent (Windows, Linux, macOS, Solaris, HP-UX, AIX and probably others)

CUnit (CUnity Fork)

Yes

2018

LGPL

Forked from CUnit in 2018 to provide ongoing development and support. OS independent (Windows, Linux, macOS, Solaris, HP-UX, AIX and probably others). Also supports output compatible with JUnit and in most cases can be a drop in replacement for CUnit.

CUnitWin32

Yes

LGPL

For Win32. Minimalistic framework. Executes each test as a separate process.

CUT

No

BSD

Cutter

Yes

LGPL

A Unit Testing Framework for C.

EmbeddedUnit

Yes

Yes

2003

MIT

Embedded C

Embunit

No

Proprietary

Create unit tests for C/C++ and Embedded C++

FCTX

Yes

BSD

Fast and complete unit testing framework all in one header. Declare and write your functions in one step. No dependencies. Cross-platform.

GLib Testing

Yes

Yes

Part of

GLib

GUnit

for

GNOME

Hammocking

Yes

Yes

MIT

Creates gmocks for C code . Also creates custom code. Usecase: Testing of legacy code

lcut

Yes

Yes

Yes

Apache License 2.0

a Lightweight C Unit Testing framework, including mock support

libcester

Yes

Yes

Yes

No

Yes

MIT

A robust header only unit testing framework, for C and C++. Supports function mocking, memory leak detection, crash report. Works on various platforms including embedded systems and compatible with various compilers. Outputs to multiple format like TAP, JunitXML, TAPV13 or plain text.

LibU

Yes

No

BSD

multiplatform (Unix, Windows); explicit test case/suite dependencies; parallel and sandboxed execution; xml, txt and customizable report formatting.

Mimicc

Proprietary

Fully automated mock generation for C and C++. Based on clang, provides the ability to compile header files straight into linkable mock object files and control them with an accompanying API.

MinUnit

MIT

extreme minimalist unit testing using 2 C macros

Mut

No

No

No

No

MIT

Another minimalistic framework for C and Unix. Single header file.

Nala

MIT

Powerful mocking. Clean API.

NovaProva

Yes

Yes

Yes

Yes

Apache License 2.0

Unit testing framework with automatic test registration. Supports mocking and stubbing. Each test is run in parallel with valgrind in its own process, so memory errors and signals can be caught. Supports Linux.

Opmock

Yes

Yes

Yes

Yes

GPLv3

Stubbing and mocking framework for C and C++ based on code generation from headers. Can check call parameters, call sequence, handle multiple implementations of a mock, and more. Includes as well a small unit testing framework, with JUnit compatible XML output, but works also with any unit testing framework.

Parasoft C/C++test

Yes

Yes

Yes

Yes

Proprietary

Automated unit/component test generation and execution on host or embedded systems with code coverage and runtime error detection. Also provides static analysis and peer code review.

PicoTest

Yes

Yes

Yes

3-clause BSD

PicoTest is a single-file unit testing framework for C programs that follows the

xUnit

principles. It provides a

CMake

module definition for easier integration with other CMake projects.

RCUNIT

Yes

Yes

Yes

MIT

RCUNIT is a small framework for testing C programs. It uses non-local jumps to emulate exceptions and handles program terminating signals (e.g. SIGILL) during test runs. RCUNIT allows creation of test fixtures, either per test or per test group.

Rexo

Yes

No

Yes

Yes

No

Public domain

Framework for C89/C++ featuring automatic registration of tests and a polished API.

RK Test

Yes

Public domain

A single-header unit testing library closely mimicking Google Test, featuring self registering tests.

RTRT

Proprietary

SeaTest

Yes

Yes

MIT

Simple, pure C, unit testing framework

Smarttester

Proprietary

Automated unit and integration testing, and

code coverage

Sput

2-clause BSD

Simple, portable C unit testing framework, single header file

STRIDE

Yes

Yes

Yes

No

Proprietary

Embedded software quality solution that includes techniques for unit, API, Behavior & Integration testing as well as interactive reporting portal

TBrun

Yes

Proprietary

Automated unit and integration testing, and

code coverage

Generators available across another component named TBExtreme

Tau

Yes

Yes

Yes

Yes

Yes

MIT

A Micro Unit testing framework for C/C++. At ~1k lines of code, it is simpler, lighter and much faster than heavier frameworks like Googletest and Catch2. Includes a rich set of assertion macros, supports automatic test registration and can output to multiple formats, like the

TAP

format or JUnit XML. Supports Linux, macoOS, FreeBSD, Windows.

TESSY

Proprietary

Automated unit and integration testing, and code coverage focused on embedded systems

TestApe

Test and mocking framework. Automatic default mocks for unresolved externals

Test Dept.

Yes

GPL

Can modify calls from software under test; e.g. test error conditions by stubbing malloc and letting it return null. Well documented

TF unit test

Yes

Yes

2012

GNU Lesser GPL

Pure C, supports test isolation in separate processes

Theft

Yes

2014

ISC

C library for property-based testing.

tinytest

Yes

Apache

Standalone, no dependencies, header-only.

TPT

Yes

Yes

Yes

Yes

Proprietary

Time Partition Testing

: Automated model based unit and integration testing for embedded systems. For C code under test, TPT supports automatic test frame generation including automatic interface analysis as well as automatic test execution, evaluation and logging.

Unity

Yes

Yes

MIT

Lightweight and includes features for embedded development. Can work with Mocks and Exceptions via CMock and CException. Also integrated with test build environment Ceedling.

usfstl

Yes

Yes

BSD

User Space Firmware Simulation Testing Library. built on top of C Unit Testing framework, which allows mocking of any symbol in runtime to multiple implementations.

VectorCAST/C

No

Yes

Yes

Yes

Proprietary

Automated unit and integration testing, and

code coverage

Visual Assert

Yes

Unit-Testing Add-In for Visual Studio. Based on the cfix testing framework.

qc

Yes

FreeBSD

qc is a C port of the QuickCheck unit test framework

xTests

BSD

Depends on STLSoft C & C++ Libraries

### C

See .NET languages below.

### C++

Name

License

xUnit

Fixtures

Group fixtures

Generators

Mocks

Exceptions

Macros

Templates

Grouping

Source

Remarks

Aeryn

No

Yes

Yes

No

No

Yes

Yes

Yes

Yes

API Sanity Checker

GNU LGPL

Yes

Yes (spectypes)

Yes (spectypes)

Yes

Unit test generator for C/C++ libraries. Can automatically generate reasonable input data for every API function. LGPL.

ATF

BSD

Yes

Yes

Yes

Yes

Originally developed for the NetBSD operating system but works well in most Unix-like platforms. Ability to install tests as part of a release.

Bandit

MIT

No (describe/it)

Yes (describe)

Yes (Nested describe)

No

No

Yes

Yes

No

Yes (Nested describe)

Header only. Automatic test registration. Specifically developed for C++11

Boost Test Library

Boost

Yes

Yes

Yes

Yes

With additional library "Turtle"

Yes

User decision

Yes

Suites and labels

Part of

Boost

. Powerful dataset concept for generating test cases. Different levels of fixtures (global, once per test suite, once per each test case in a suite). Powerful floating point comparison.

BugEye

Boost

No

No

No

No

No

Yes

No

No

Yes

Header-only.

TAP

output.

QA Systems Cantata

Proprietary

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Commercial. Automated unit and integration testing tool for C++. Certified testing for host or embedded systems. Code coverage and unique call interface control to simulate and intercept calls.

Casmine

GPL 2.0

No

Yes

Yes

No

No

Yes

Yes

Yes

Yes

C++17, modeled after the Jasmine testing framework, type-safe tests, auto-registration, BDD features, focused/disabled/pending tests, flexible configuration (JSON), colored console reporter, extendable, Windows/Linux/macOS

Catch or Catch2

Boost

No

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Header only, no external dependencies, auto-registration, tdd and bdd features

CATCH-VC6

No

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

VC6 port of CATCH

cfix

Yes

Yes

No

No

No

Yes

Yes

No

Specialized for Windows development—both Win32 and NT kernel mode. Compatible to WinUnit.

Cput

Yes

Yes

Yes

Yes

Yes

Yes

No

Suites

Library and MS Visual Studio add-in to create and run unit tests. Open Source.

CPPOCL/test

Apache 2

No

Yes

No

Yes

Yes

Released Under Apache 2.0, compliant with C++ 98 and C++ 11. Works for Linux, Windows 32/64 bit using gcc, Cygwin, VS2005, VS2015. Header file only library. Provides ability to write performance tests in a similar way to unit tests. Has some support for reporting memory leaks.

CppTest

GNU LGPL

Yes

Yes

Suites

Released under

LGPL

cpptest-lite

MIT

Yes

Yes

Yes

Suites

Released under

MIT

. Developed for C++11.

CppUnit

GNU LGPL

Yes

Yes

Yes

No

No

Yes

Yes

No

Suites

Released under

LGPL

Name

License

xUnit

Fixtures

Group fixtures

Generators

Mocks

Exceptions

Macros

Templates

Grouping

Source

Remarks

CppUTest

Yes

Yes

Yes

No

Yes

No

Yes

No

Suites

Limited C++ set by design to keep usage easy and allow it to work on embedded platforms. C++ is buried in macros so the learning curve for C programmers is minimal. Ported to Symbian. Has a mocking support library CppUMock

CppUnitLite

Yes

No

No

No

Yes

No

Suites

CPUnit

Yes

Yes

Yes

No

No

Yes

Yes

Yes

Yes

Released under BSD.

Criterion

MIT

Yes

Yes

Yes

Yes

No

Yes

Yes

Yes

Suites

Unit testing framework with automatic test registration. Needs C++11 compiler support for the C++ API. Supports theories and parameterized tests. Each test is run in its own process, so signals and crashes can be reported. Can output to multiple formats, like the

TAP

format or JUnit XML. Supports Linux, macOS, FreeBSD, Windows.

libcester

MIT

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

File

A robust header only unit testing framework for C and C++ programming language. Support function mocking, memory leak detection, crash report. Works on various platforms including embedded systems and compatible with various compilers. Outputs to multiple format like TAP, JunitXML, TAPV13 or plain text.

crpcut

No

Yes

No

No

Yes

Yes

Suites within Suites

BSD 2 clause. Runs each test in its own process, guaranteeing that the test suite continues even in the event of an unexpected crash or infinite loop.

CUTE

Yes

Yes

No

No

Yes

Yes

Suites

CUTE (C++ Unit Testing Easier) with Eclipse CDT integration. Single line include, without inheritance. Mock support is provided by Mockator.

cutee

No

No

No

No

CuteX

No

No

No

No

No

Yes

No

Yes

Yes (by wildcard)

Native C++ unit test framework using template recursive, no "weird" fixture. Assertion template only, zero learning time. Header only, no external library.

CxxTest

Yes

Yes

Yes

No

Yes*

Optional

Yes

No

Suites

Uses a C++ parser and code generator (requiring

Python

) for test registration. * Has framework to generate mocks of global functions, but not of objects.

doctest

MIT

No

Yes

Yes

No

No

Yes

Yes

Yes

Yes

Light, feature rich C++ single header testing framework

Embunit

No

No

Yes

Commercial. Create unit tests for C/C++ and Embedded C++

Exercisix

BSD

No

No

No

No

No

Yes

Yes

Yes

Executables

Goal: make adding tests as fast and easy as possible.

FakeIt

MIT

Yes

Use the latest C++11 features to create an expressive, yet very simple, API.

FCTX

Yes

Yes

Yes

No

No

No

Yes

No

Yes

Fast and complete unit testing framework all in one header. Declare and write your functions in one step. No dependencies. Cross platform.

Fructose

No

Yes

No

Yes

No

Yes

Yes
