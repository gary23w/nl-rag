---
title: "Divergence (computer science)"
source: https://en.wikipedia.org/wiki/Divergence_(computer_science)
domain: strictness-analysis
license: CC-BY-SA-4.0
tags: strictness analysis, demand analysis, backwards analysis, call-by-value transformation
fetched: 2026-07-02
---

# Divergence (computer science)

In computer science, a computation is said to **diverge** if it does not terminate or terminates in an exceptional state. Otherwise it is said to **converge**. In domains where computations are expected to be infinite, such as process calculi, a computation is said to diverge if it fails to be productive (i.e. to continue producing an action within a finite amount of time).

## Definitions

Various subfields of computer science use varying, but mathematically precise, definitions of what it means for a computation to converge or diverge.

### Rewriting

In abstract rewriting, an abstract rewriting system is called convergent if it is both confluent and terminating.

The notation *t* ↓ *n* means that *t* reduces to normal form *n* in zero or more reductions, *t*↓ means *t* reduces to some normal form in zero or more reductions, and *t*↑ means *t* does not reduce to a normal form; the latter is impossible in a terminating rewriting system.

In the lambda calculus an expression is divergent if it has no normal form.

### Denotational semantics

In denotational semantics an object function *f* : *A* → *B* can be modelled as a mathematical function $f:A\cup \{\perp \}\rightarrow B\cup \{\perp \}$ where ⊥ (bottom) indicates that the object function or its argument diverges.

### Concurrency theory

In the calculus of communicating sequential processes (CSP), divergence occurs when a process performs an endless series of hidden actions. For example, consider the following process, defined by CSP notation: $Clock=tick\rightarrow Clock$ The traces of this process are defined as: $\operatorname {traces} (Clock)=\{\langle \rangle ,\langle tick\rangle ,\langle tick,tick\rangle ,\ldots \}=\{tick\}^{*}$ Now, consider the following process, which hides the *tick* event of the *Clock* process: $P=Clock\setminus tick$ As P cannot do anything other than perform hidden actions forever, it is equivalent to the process that does nothing but diverge, denoted $\mathbf {div}$ . One semantic model of CSP is the failures-divergences model, which refines the stable failures model by distinguishing processes based on the sets of traces after which they can diverge.
