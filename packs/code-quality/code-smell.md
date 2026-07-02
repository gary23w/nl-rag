---
title: "Code smell"
source: https://en.wikipedia.org/wiki/Code_smell
domain: code-quality
license: CC-BY-SA-4.0
tags: refactoring, code smell, technical debt, cyclomatic complexity, coupling, clean code
fetched: 2026-07-02
---

# Code smell

In computer programming, a **code smell** is any characteristic of source code that hints at a deeper problem. Determining what a code smell is and is not is subjective, and varies by language, developer, and development methodology.

The term was popularized by Kent Beck on WardsWiki in the late 1990s. Usage of the term increased after it was featured in the 1999 book *Refactoring: Improving the Design of Existing Code* by Martin Fowler. It is also a term used by agile programmers.

## Definition

One way to look at smells is with respect to principles and quality: "Smells are certain structures in the code that indicate violation of fundamental design principles and negatively impact design quality". Code smells are usually not bugs; they are not technically incorrect and do not prevent the program from functioning. Instead, they indicate weaknesses in design that may slow down development or increase the risk of bugs or failures in the future. Bad code smells can be an indicator of factors that contribute to technical debt. Robert C. Martin calls a list of code smells a "value system" for software craftsmanship.

Contrary to these severe interpretations, Cunningham's original definition was that a smell is a suggestion that something may be wrong, not evidence that there is already a problem.

Often the deeper problem hinted at by a code smell can be uncovered when the code is subjected to a short feedback cycle, where it is refactored in small, controlled steps, and the resulting design is examined to see if there are any further code smells that in turn indicate the need for more refactoring. From the point of view of a programmer charged with performing refactoring, code smells are heuristics to indicate when to refactor, and what specific refactoring techniques to use. Thus, a code smell is a driver for refactoring.

Factors such as the understandability of code, how easy it is to be modified, the ease in which it can be enhanced to support functional changes, the code's ability to be reused in different settings, how testable the code is, and code reliability are factors that can be used to identify code smells.

A 2015 study utilizing automated analysis for half a million source code commits and the manual examination of 9,164 commits determined to exhibit "code smells" found that:

- There exists empirical evidence for the consequences of "technical debt", but there exists only anecdotal evidence as to *how*, *when*, or *why* this occurs.
- Common wisdom suggests that urgent maintenance activities and pressure to deliver features while prioritizing time-to-market over code quality are often the causes of such smells.

Tools such as Checkstyle, PMD, FindBugs, and SonarQube can automatically identify code smells.

## Examples

### Application-level smells

**Duplicated code**

identical or very similar code that exists in more than one location.

**Shotgun surgery**

a single change that needs to be applied to multiple classes at the same time.

### Class-level smells

**Large class, a.k.a. god object**

a

class

that contains too many types or contains many unrelated methods.

**Refused bequest**

a class that

overrides

a method of a base class in such a way that the

contract

of the

base class

is not honored by the

derived class

, violating the

Liskov substitution principle

.

**Excessive use of literals or magic numbers**

these should be coded as named constants, to improve readability and to avoid programming errors. Additionally,

literals

can and should be externalized into resource files/scripts, or other data stores such as databases where possible, to facilitate localization of software if it is intended to be deployed in different regions.

**Downcasting**

a type cast which breaks the abstraction model; the abstraction may have to be refactored or eliminated.

**Data clump**

Occurs when a group of variables are passed around together in various parts of the program. In general, this suggests that it would be more appropriate to formally group the different variables together into a single object, and pass around only the new object instead.

### Method-level smells

**Too many parameters**

a long list of parameters is hard to read, and makes calling and testing the function complicated. It may indicate that the purpose of the function is ill-conceived and that the code should be refactored so responsibility is assigned in a more clean-cut way.
