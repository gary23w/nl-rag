---
title: "Mutation testing"
source: https://en.wikipedia.org/wiki/Mutation_testing
domain: mutation-testing
license: CC-BY-SA-4.0
tags: mutation testing, test effectiveness, fault injection, code coverage
fetched: 2026-07-02
---

# Mutation testing

**Mutation testing** (or *mutation analysis* or *program mutation*) is used to design new software tests and evaluate the quality of existing software tests. Mutation testing involves making small changes to the program being tested. Each changed version is called a *mutant*. A test detects, and therefore rejects, a mutant upon test failure –– failure indicating that the test successfully discerned that the behaviour of the mutant differs from the behaviour of the original code. Rejection is called *killing* the mutant. The value of a test suite is measured by the percentage of mutants that it kills. The test suite can then be improved by adding new tests designed to kill additional mutants.

Mutant creation is done using well-defined *mutation operators* that either mimic typical programming errors (such as using the wrong operator or variable name) or force the creation of valuable tests (such as dividing each expression by zero).

Mutation testing is a form of white-box testing. Its purpose is to help the tester develop effective regression tests by locating weaknesses in the test data used to test the program and discovering sections of the tested program's code that are seldom or never accessed during execution.

## Introduction

Most of this article is about "program mutation", in which the program is modified. A more general definition of *mutation analysis* is using well-defined rules defined on syntactic structures to make systematic changes to software artifacts. Mutation analysis has been applied to other problems, but is usually applied to testing. So *mutation testing* is defined as using mutation analysis to design new software tests or to evaluate existing software tests. Thus, mutation analysis and testing can be applied to design models, specifications, databases, tests, XML, and other types of software artifacts, although program mutation is the most common.

## Overview

Tests can be created to verify the correctness of the implementation of a given software system, but the creation of tests still poses the question of whether the tests are correct and sufficiently cover the requirements associated with the implementation. (This technological problem is itself an instance of a deeper philosophical problem named "Quis custodiet ipsos custodes?" ["Who will guard the guards?"].)

The idea behind mutation testing is that the program being tested works as intended, so if a mutant is introduced and functionality changes this means a bug is introduced, which the tests should then find. In this way, the tests are tested. If a mutant is not detected by the test suite, this typically indicates that the test suite is unable to locate the faults represented by the mutant, but it can also indicate that the mutation introduces no faults. That is, the mutation is a valid change, one that either produces a desired result or one that does not affect functionality. One (common) way a mutant can be valid is that the code that has been changed is "dead code" that is never executed.

For mutation testing to function at scale, a large number of mutants are usually introduced, leading to the compilation and execution of an extremely large number of copies of the program. This problem of the expense of mutation testing had reduced its practical use as a method of software testing. However, the increased use of object-oriented programming languages and unit testing frameworks has led to the creation of mutation testing tools that test individual portions of an application.

## Goals

The goals of mutation testing are multiple:

- identify weakly tested pieces of code (those for which mutants are not killed)
- identify weak tests (those that never kill mutants)
- compute the mutation score, the mutation score is the number of mutants killed / total number of mutants.
- learn about error propagation and state infection in the program

## History

Mutation testing was originally proposed by Richard Lipton as a student in 1971, and first developed and published by DeMillo, Lipton and Sayward. The first implementation of a mutation testing tool was by Timothy Budd as part of his PhD work (titled *Mutation Analysis*) in 1980 from Yale University.

Recently, with the availability of massive computing power, there has been a resurgence of mutation analysis within the computer science community, and work has been done to define methods of applying mutation testing to object oriented programming languages and non-procedural languages such as XML, SMV, and finite-state machines.

In 2004, a company called Certess Inc. (now part of Synopsys) extended many of the principles into the hardware verification domain. Whereas mutation analysis only expects to detect a difference in the output produced, Certess extends this by verifying that a checker in the testbench will actually detect the difference. This extension means that all three stages of verification, namely: activation, propagation, and detection are evaluated. They called this functional qualification.

Fuzzing can be considered to be a special case of mutation testing. In fuzzing, the messages or data exchanged inside communication interfaces (both inside and between software instances) are mutated to catch failures or differences in processing the data. Codenomicon (2001) and Mu Dynamics (2005) evolved fuzzing concepts to a fully stateful mutation testing platform, complete with monitors for thoroughly exercising protocol implementations.

## Mutation testing overview

Mutation testing is based on two hypotheses. The first is the *competent programmer* hypothesis. This hypothesis states that competent programmers write programs that are close to being correct. "Close" is intended to be based on behavior, not syntax. The second hypothesis is called the *coupling effect*. The coupling effect asserts that simple faults can cascade or *couple* to form other emergent faults.

Subtle and important faults are also revealed by higher-order mutants, which further support the coupling effect. Higher-order mutants are enabled by creating mutants with more than one mutation.

Mutation testing is done by selecting a set of mutation operators and then applying them to the source program one at a time for each applicable piece of the source code. The result of applying one mutation operator to the program is called a *mutant*. If the test suite is able to detect the change (i.e., one of the tests fails), then the mutant is said to be *killed*.

For example, consider the following C++ code fragment:

```mw
if (a && b) {
    c = 1;
} else {
    c = 0;
}
```

The condition mutation operator would replace `&&` with `||` and produce the following mutant:

```mw
if (a || b) {
    c = 1;
} else {
    c = 0;
}
```

Now, for the test to kill this mutant, the following three conditions should be met:

1. A test must *reach* the mutated statement.
2. Test input data should *infect* the program state by causing different program states for the mutant and the original program. For example, a test with `a = 1` and `b = 0` would do this.
3. The incorrect program state (the value of 'c') must *propagate* to the program's output and be checked by the test.

These conditions are collectively called the *RIP model*.

*Weak mutation testing* (or *weak mutation coverage*) requires that only the first and second conditions are satisfied. *Strong mutation testing* requires that all three conditions are satisfied. Strong mutation is more powerful, since it ensures that the test suite can really catch the problems. Weak mutation is closely related to code coverage methods. It requires much less computing power to ensure that the test suite satisfies weak mutation testing than strong mutation testing.

However, there are cases where it is not possible to find a test case that could kill this mutant. The resulting program is behaviorally equivalent to the original one. Such mutants are called *equivalent mutants*.

Equivalent mutants detection is one of the biggest obstacles to practical usage of mutation testing. The effort needed to check if mutants are equivalent or not can be very high, even for small programs. A 2014 systematic literature review of a wide range of approaches to overcome the Equivalent Mutant Problem identified 17 relevant techniques (in 22 articles) and three categories of techniques: detecting (DEM); suggesting (SEM); and avoiding equivalent mutant generation (AEMG). The experiment indicated that Higher Order Mutation in general and JudyDiffOp strategy in particular provide a promising approach to the Equivalent Mutant Problem.

In addition to equivalent mutants, there are *subsumed mutants* which are mutants that exist in the same source code location as another mutant, and are said to be "subsumed" by the other mutant. Subsumed mutants are not visible to a mutation testing tool, and do not contribute to coverage metrics. For example, let's say you have two mutants, A and B, that both change a line of code in the same way. Mutant A is tested first, and the result is that the code is not working correctly. Mutant B is then tested, and the result is the same as with mutant A. In this case, Mutant B is considered to be subsumed by Mutant A, since the result of testing Mutant B is the same as the result of testing Mutant A. Therefore, Mutant B does not need to be tested, as the result will be the same as Mutant A.

## Mutation operators

To make syntactic changes to a program, a mutation operator serves as a guideline that substitutes portions of the source code. Given that mutations depend on these operators, scholars have created a collection of mutation operators to accommodate different programming languages, like Java. The effectiveness of these mutation operators plays a pivotal role in mutation testing.

Many mutation operators have been explored by researchers. Here are some examples of mutation operators for imperative languages:

- Statement deletion
- Statement duplication or insertion, e.g. `goto fail;`
- Replacement of Boolean subexpressions with *true* and *false*
- Replacement of some arithmetic operations with others, e.g. `+` with `*`, `-` with `/`
- Replacement of some Boolean relations with others, e.g. `>` with `>=`, `==` and `<=`
- Replacement of variables with others from the same scope (variable types must be compatible)
- Remove method body.

These mutation operators are also called traditional mutation operators. There are also mutation operators for object-oriented languages, for concurrent constructions, complex objects like containers, etc.

### Types of mutation operators

Operators for containers are called *class-level* mutation operators. Operators at the class level alter the program's structure by adding, removing, or changing the expressions being examined. Specific operators have been established for each category of changes. For example, the muJava tool offers various class-level mutation operators such as Access Modifier Change, Type Cast Operator Insertion, and Type Cast Operator Deletion. Mutation operators have also been developed to perform security vulnerability testing of programs.

Apart from the *class-level* operators, MuJava also includes *method-level* mutation operators, referred to as traditional operators. These traditional operators are designed based on features commonly found in procedural languages. They carry out changes to statements by adding, substituting, or removing primitive operators. These operators fall into six categories: *Arithmetic operators*, *Relational operator*s, *Conditional operators*, *Shift operators*, *Logical operators* and *Assignment operators*.

## Types of mutation testing

There are three types of mutation testing;

### Statement mutation

Statement mutation is a process where a block of code is intentionally modified by either deleting or copying certain statements. Moreover, it allows for the reordering of statements within the code block to generate various sequences. This technique is crucial in software testing as it helps identify potential weaknesses or errors in the code. By deliberately making changes to the code and observing how it behaves, developers can uncover hidden bugs or flaws that might go unnoticed during regular testing. Statement mutation is like a diagnostic tool that provides insights into the code's robustness and resilience, helping programmers improve the overall quality and reliability of their software.

For example, in the code snippet below, entire 'else' section is removed:

```mw
function checkCredentials(username, password) {
  if (username === "admin" && password === "password") {
    return true;
  } 
}
```

### Value mutation

Value mutation occurs when modifications are made to parameter or constant values within the code. This typically involves adjusting the values by adding or subtracting 1, but it can also involve making more substantial changes to the values. The specific alterations made during value mutation include two main scenarios:

Firstly, there's the transformation from a small value to a higher value. This entails replacing a small value in the code with a larger one. The purpose of this change is to assess how the code responds when it encounters larger inputs. It helps ensure that the code can accurately and efficiently process these larger values without encountering errors or unexpected issues.

Conversely, the second scenario involves changing a higher value to a smaller one. In this case, we replace a higher value within the code with a smaller value. This test aims to evaluate how the code handles smaller inputs. Ensuring that the code performs correctly with smaller values is essential to prevent unforeseen problems or errors when dealing with such input data.

For example:

```mw
// Original code
function multiplyByTwo(value) {
  return value * 2;
}

// Value mutation: Small value to higher value
function multiplyByTwoMutation1(value) {
  return value * 10;
}

// Value mutation: Higher value to small value
function multiplyByTwoMutation2(value) {
  return value / 10;
}
```

### Decision mutation

Decision mutation testing centers on the identification of design errors within the code, with a particular emphasis on detecting flaws or weaknesses in the program's decision-making logic. This method involves deliberately altering arithmetic and logical operators to expose potential issues. By manipulating these operators, developers can systematically evaluate how the code responds to different decision scenarios. This process helps ensure that the program's decision-making pathways are robust and accurate, preventing costly errors that could arise from faulty logic. Decision mutation testing serves as a valuable tool in software development, enabling developers to enhance the reliability and effectiveness of their decision-making code segments.

For example:

```mw
// Original code
function isPositive(number) {
  return number > 0;
}

// Decision mutation: Changing the comparison operator
function isPositiveMutation1(number) {
  return number >= 0;
}

// Decision mutation: Negating the result
function isPositiveMutation2(number) {
  return !(number > 0);
}
```
