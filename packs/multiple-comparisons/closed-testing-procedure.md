---
title: "Closed testing procedure"
source: https://en.wikipedia.org/wiki/Closed_testing_procedure
domain: multiple-comparisons
license: CC-BY-SA-4.0
tags: multiple comparisons, family-wise error rate, false discovery rate, closed testing
fetched: 2026-07-02
---

# Closed testing procedure

In statistics, the **closed testing procedure** is a general method for performing more than one hypothesis test simultaneously.

## The closed testing principle

Suppose there are *k* hypotheses *H*1,..., *H**k* to be tested and the overall type I error rate is α. The closed testing principle allows the rejection of any one of these elementary hypotheses, say *H**i*, if all possible intersection hypotheses involving *H**i* can be rejected by using valid local level α tests; the adjusted p-value is the largest among those hypotheses. It controls the family-wise error rate for all the *k* hypotheses at level α in the strong sense.

## Example

Suppose there are three hypotheses *H*1,*H*2, and *H*3 to be tested and the overall type I error rate is 0.05. Then *H*1 can be rejected at level α if *H*1 ∩ *H*2 ∩ *H*3, *H*1 ∩ *H*2, *H*1 ∩ *H*3 and *H*1 can all be rejected using valid tests with α = 0.05.

## Special cases

The Holm–Bonferroni method is a special case of a closed test procedure for which each intersection null hypothesis is tested using the simple Bonferroni test. As such, it controls the family-wise error rate for all the *k* hypotheses at level α in the strong sense.

Multiple test procedures developed using the graphical approach for constructing and illustrating multiple test procedures are a subclass of closed testing procedures.
