---
title: "Reliability block diagram"
source: https://en.wikipedia.org/wiki/Reliability_block_diagram
domain: fault-tree-analysis
license: CC-BY-SA-4.0
tags: fault tree analysis, top event logic, event tree analysis, reliability block diagram
fetched: 2026-07-02
---

# Reliability block diagram

A **reliability block diagram (RBD)** is a diagrammatic method for showing how component reliability contributes to the success or failure of a redundant system. RBD is also known as a dependence diagram (DD).

An RBD is drawn as a series of blocks connected in parallel or series configuration. Parallel blocks indicate redundant subsystems or components that contribute to a lower failure rate. Each block represents a component of the system with a failure rate. RBDs will indicate the type of redundancy in the parallel path. For example, a group of parallel blocks could require two out of three components to succeed for the system to succeed. By contrast, any failure along a series path causes the entire series path to fail.

An RBD may be drawn using switches in place of blocks, where a closed switch represents a working component and an open switch represents a failed component. If a path may be found through the network of switches from beginning to end, the system still works.

An RBD may be converted to a success tree or a fault tree depending on how the RBD is defined. A success tree may then be converted to a fault tree or vice versa by applying de Morgan's theorem.

To evaluate an RBD, closed form solutions are available when blocks or components have *statistical independence*.

When statistical independence is not satisfied, specific formalisms and solution tools such as dynamic RBD have to be considered.

## Calculating an RBD

The first thing one must determine when calculating an RBD is whether to use probability or rate. Failure rates are often used in RBDs to determine system failure rates. Use probabilities or rates in an RBD but not both.

Series probabilities are calculated by multiplying the reliability (a probability) of the series components:

$R_{\text{SYS}}=R_{1}(t)\times R_{2}(t)\times \cdots \times R_{n}(t)$

Parallel probabilities are calculated by multiplying the unreliability (*Q*) of the series components where *Q* = 1 – *R* if only one unit needs to function for system success:

$Q_{\text{SYS}}=Q_{1}(t)\times Q_{2}(t)\times \cdots \times Q_{n}(t)$

For constant failure rates, series rates are calculated by superimposing the Poisson point processes of the series components:

$\lambda _{\text{SYS}}=\lambda _{1}+\lambda _{2}+\cdots +\lambda _{n}$

Parallel rates can be evaluated using a number of formulas including this formula for all units active with equal component failure rates. *n* − *q* out of *n* redundant units are required for success. *μ* >> *λ*

$\lambda _{\text{SYS}}={\frac {n!\lambda ^{q+1}}{(n-q-1)!\mu ^{q}}}$

If the components in a parallel system have *n* different failure rates a more general formula can be used as follows. For the repairable model *Q* = *λ*/*μ* as long as ${\textstyle \mu \gg \lambda }$ .

$\lambda _{\text{SYS}}=\sum _{i=1}^{n}\left(\lambda _{i}\prod _{j=1;j\neq i}^{n}Q_{j}\right)$
