---
title: "Cucumber (software)"
source: https://en.wikipedia.org/wiki/Cucumber_(software)
domain: gherkin
license: CC-BY-SA-4.0
tags: gherkin syntax, given when then, behavior-driven development, specification language
fetched: 2026-07-02
---

# Cucumber (software)

**Cucumber** is a software tool that supports behavior-driven development (BDD). Central to the Cucumber BDD approach is its ordinary language parser called Gherkin. It allows expected software behaviors to be specified in a logical language that customers can understand. As such, Cucumber allows the execution of feature documentation written in business-facing text. It is often used for testing other software. It runs automated acceptance tests written in a behavior-driven development (BDD) style.

Cucumber was originally written in the Ruby programming language and was originally used exclusively for Ruby testing as a complement to the RSpec BDD framework. Cucumber now supports a variety of different programming languages through various implementations, including Java and JavaScript. There is a port of Cucumber to .NET called SpecFlow, now superseded by Reqnroll.

## Gherkin language

Gherkin is the language that Cucumber uses to define test cases. It is designed to be non-technical and human readable, and collectively describes use cases relating to a software system. The purpose behind Gherkin's syntax is to promote behavior-driven development practices across an entire development team, including business analysts and managers. It seeks to enforce firm, unambiguous requirements starting in the initial phases of requirements definition by business management and in other stages of the development lifecycle.

In addition to providing a script for automated testing, Gherkin's natural language syntax is designed to provide simple documentation of the code under test. Gherkin currently supports keywords in dozens of languages.

### Syntax

Syntax is centered around a line-oriented design, similar to that of Python. The structure of a file is defined using whitespace and other control characters. Lines starting with `#` are considered comments, and can be placed anywhere in a file. Instructions are any non-empty and non-comment line. They consist of a recognized Gherkin keyword followed by a string.

All Gherkin files have the `.feature` file extension. They contain a single Feature definition for the system under test and are an executable test script.

Here is an example of the syntax:

```mw
Feature: Guess the word

  # The first example has two steps
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  # The second example has three steps
  Scenario: Breaker joins a game
    Given the Maker has started a game with the word "silky"
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```

## Command line

Cucumber comes with a built-in command line interface that covers a comprehensive list of instructions. Like most command line tools, cucumber provides the `--help` option that provides a summary of arguments the command accepts.

```mw
$ cucumber --help
        -r, --require LIBRARY|DIR        Require files before executing the features.
        --i18n LANG                      List keywords for in a particular language.
                                         Run with "--i18n help" to see all languages.
        -f, --format FORMAT              How to format features (Default: pretty).
        -o, --out [FILE|DIR]             Write output to a file/directory instead of
        ...
```

Cucumber command line can be used to quickly run defined tests. It also supports running a subset of scenarios by filtering tags.

```mw
$ cucumber --tags @tag-name
```

The above command helps in executing only those scenarios that have the specified `@tag-name`. Arguments can be provided as a logical `OR` or `AND` operation of tags. Apart from tags, scenarios can be filtered on scenario names.

```mw
$ cucumber --name logout
```

The above command will run only those scenarios that contain the word 'logout'.

It is also useful to be able to know what went wrong when a test fails. Cucumber makes it easy to catch bugs in the code with the `--backtrace` option.
