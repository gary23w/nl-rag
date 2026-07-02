---
title: "Software verification"
source: https://en.wikipedia.org/wiki/Software_verification
domain: do-178c
license: CC-BY-SA-4.0
tags: do-178c, airborne software, dal assurance level, avionics certification
fetched: 2026-07-02
---

# Software verification

**Software verification** is a discipline of software engineering, programming languages, and theory of computation whose goal is to assure that software satisfies the expected requirements.

## Broad scope and classification

A broad definition of verification makes it related to software testing. In that case, there are two fundamental approaches to verification:

- *Dynamic verification*, also known as experimentation, dynamic testing or, simply testing. - This is good for finding faults (software bugs).
- *Static verification*, also known as analysis or, static testing - This is useful for proving the correctness of a program. Although it may result in false positives when there are one or more conflicts between the process a software really does and what the static verification assumes it does.

Under the ACM Computing Classification System, software verification topics appear under "Software and its engineering", within "Software creation", whereas Program verification also appears under Theory of computation under Semantics and reasoning, Program reasoning.

## Dynamic verification (Test, experimentation)

Dynamic verification is performed during the execution of software, and dynamically checks its behavior; it is commonly known as the Test phase. Verification is a Review Process. Depending on the scope of tests, we can categorize them in three families:

- *Test in the small*: a test that checks a single function or class (Unit test)
- *Test in the large*: a test that checks a group of classes, such as
  - Module test (a single module)
  - Integration test (more than one module)
  - System test (the entire system)
- *Acceptance test*: a formal test defined to check acceptance criteria for a software
  - Functional test
  - Non functional test (performance, stress test)

The aim of software dynamic verification is to find the errors introduced by an activity (for example, having a medical software to analyze bio-chemical data); or by the repetitive performance of one or more activities (such as a stress test for a web server, i.e. check if the current product of the activity is as correct as it was at the beginning of the activity).

## Static verification (Analysis)

Static verification is the process of checking that software meets requirements by inspecting the code before it runs. For example:

- *Code conventions verification*
- *Bad practices (anti-pattern) detection*
- Software metrics calculation
- Formal verification

Verification by Analysis - The analysis verification method applies to verification by investigation, mathematical calculations, logical evaluation, and calculations using classical textbook methods or accepted general use computer methods. Analysis includes sampling and correlating measured data and observed test results with calculated expected values to establish conformance with requirements.

## Narrow scope

When it is defined more strictly, verification is equivalent only to static testing and it is intended to be applied to artifacts. And, validation (of the whole software product) would be equivalent to dynamic testing and intended to be applied to the running software product (not its artifacts, except requirements). Notice that requirements validation can be performed statically and dynamically (See artifact validation).

## Comparison with validation

Software verification is often confused with software validation. The difference between *verification* and *validation*:

- Software *verification* asks the question, "Are we building the product right?"; that is, does the software conform to its specifications? (As a house conforms to its blueprints.)
- Software *validation* asks the question, "Are we building the right product?"; that is, does the software do what the user really requires? (As a house conforms to what the owner needs and wants.)
