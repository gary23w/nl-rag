---
title: "Fold change"
source: https://en.wikipedia.org/wiki/Fold_change
domain: gene-expression-analysis
license: CC-BY-SA-4.0
tags: gene expression profiling, dna microarray, differential gene expression, rna sequencing
fetched: 2026-07-02
---

# Fold change

**Fold change** is a measure describing how much a quantity changes between an original and a subsequent measurement. In bioinformatics that utilize case-control studies, the convention is to compare a given metric of the case relative to the control, e.g., divide the signal of a particular metabolite (or gene or protein) in the "case" by the signal of the same parameter in the "control". In pharmacological studies, the "response" of the experimental group would be divided by the "response" in the contol group. Fold change is defined as the ratio between two quantities; for quantities *A* and *B* the fold change of *B* with respect to *A* is *B*/*A*. In other words, a change from 30 to 60 is defined as a fold-change of 2. This is also referred to as a "one fold increase". Similarly, a change from 30 to 15 is referred to as a "0.5-fold decrease". Fold change is often used when analysing multiple measurements of a biological system taken at different times as the change described by the ratio between the time points is easier to interpret than the difference.

Fold change is so called because it is common to describe an increase of multiple *X* as an "*X*-fold increase". As such, several dictionaries, including the Oxford English Dictionary and Merriam-Webster Dictionary, as well as Collins's Dictionary of Mathematics, define "-fold" to mean "times", as in "2-fold" = "2 times" = "double". Likely because of this definition, many scientists use not only "fold", but also "fold change" to be synonymous with "times", as in "3-fold larger" = "3 times larger".

Fold change is often used in analysis of gene expression data from microarray and RNA-Seq experiments for measuring change in the expression level of a gene. A disadvantage of using fold change occurs when the denominator is close to zero. In this case, the ratio may be difficult to interpret because the fold change value can be disproportionately affected by measurement noise.

## Fold changes in genomics and bioinformatics

In the field of genomics (and more generally in bioinformatics), the modern usage is to define fold change in terms of ratios, and not by the alternative definition.

However, log-ratios are often used for analysis and visualization of fold changes. The logarithm to base 2 is most commonly used, as it is easy to interpret, e.g. a doubling in the original scaling is equal to a log2 fold change of 1, a quadrupling is equal to a log2 fold change of 2 and so on. Conversely, the measure is symmetric when the change decreases by an equivalent amount e.g. a halving is equal to a log2 fold change of −1, a quartering is equal to a log2 fold change of −2 and so on. This leads to more aesthetically pleasing plots, as exponential changes are displayed as linear and so the dynamic range is increased. For example, on a plot axis showing log2 fold changes, an 8-fold increase will be displayed at an axis value of 3 (since 23 = 8). However, there is no mathematical reason to only use logarithm to base 2, and due to many discrepancies in describing the log2 fold changes in gene/protein expression, a new term "loget" has been proposed.
