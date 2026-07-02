---
title: "Epigraph (mathematics)"
source: https://en.wikipedia.org/wiki/Epigraph_(mathematics)
domain: convex-analysis
license: CC-BY-SA-4.0
tags: convex analysis, convex conjugate, proximal operator, fenchel duality
fetched: 2026-07-02
---

# Epigraph (mathematics)

In mathematics, the **epigraph** or **supergraph** of a function $f:X\to [-\infty ,\infty ]$ valued in the extended real numbers $[-\infty ,\infty ]=\mathbb {R} \cup \{\pm \infty \}$ is the set $\operatorname {epi} f=\{(x,r)\in X\times \mathbb {R} ~:~r\geq f(x)\}$ consisting of all points in the Cartesian product $X\times \mathbb {R}$ lying on or above the function's graph. Similarly, the **strict epigraph** $\operatorname {epi} _{S}f$ is the set of points in $X\times \mathbb {R}$ lying strictly above its graph.

Importantly, unlike the graph of $f,$ the epigraph *always* consists *entirely* of points in $X\times \mathbb {R}$ (this is true of the graph only when f is real-valued). If the function takes $\pm \infty$ as a value then $\operatorname {graph} f$ will *not* be a subset of its epigraph $\operatorname {epi} f.$ For example, if $f\left(x_{0}\right)=\infty$ then the point $\left(x_{0},f\left(x_{0}\right)\right)=\left(x_{0},\infty \right)$ will belong to $\operatorname {graph} f$ but not to $\operatorname {epi} f.$ These two sets are nevertheless closely related because the graph can always be reconstructed from the epigraph, and vice versa.

The study of continuous real-valued functions in real analysis has traditionally been closely associated with the study of their graphs, which are sets that provide geometric information (and intuition) about these functions. Epigraphs serve this same purpose in the fields of convex analysis and variational analysis, in which the primary focus is on convex functions valued in $[-\infty ,\infty ]$ instead of continuous functions valued in a vector space (such as $\mathbb {R}$ or $\mathbb {R} ^{2}$ ). This is because in general, for such functions, geometric intuition is more readily obtained from a function's epigraph than from its graph. Similarly to how graphs are used in real analysis, the epigraph can often be used to give geometrical interpretations of a convex function's properties, to help formulate or prove hypotheses, or to aid in constructing counterexamples.

## Definition

The definition of the epigraph was inspired by that of the graph of a function, where the ***graph*** of $f:X\to Y$ is defined to be the set $\operatorname {graph} f:=\{(x,y)\in X\times Y~:~y=f(x)\}.$

The ***epigraph*** or ***supergraph*** of a function $f:X\to [-\infty ,\infty ]$ valued in the extended real numbers $[-\infty ,\infty ]=\mathbb {R} \cup \{\pm \infty \}$ is the set ${\begin{alignedat}{4}\operatorname {epi} f&=\{(x,r)\in X\times \mathbb {R} ~:~r\geq f(x)\}\\&=\left[f^{-1}(-\infty )\times \mathbb {R} \right]\cup \bigcup _{x\in f^{-1}(\mathbb {R} )}(\{x\}\times [f(x),\infty ))\end{alignedat}}$ where all sets being unioned in the last line are pairwise disjoint.

In the union over $x\in f^{-1}(\mathbb {R} )$ that appears above on the right hand side of the last line, the set $\{x\}\times [f(x),\infty )$ may be interpreted as being a "vertical ray" consisting of $(x,f(x))$ and all points in $X\times \mathbb {R}$ "directly above" it. Similarly, the set of points on or below the graph of a function is its hypograph.

The ***strict epigraph*** is the epigraph with the graph removed: ${\begin{alignedat}{4}\operatorname {epi} _{S}f&=\{(x,r)\in X\times \mathbb {R} ~:~r>f(x)\}\\&=\operatorname {epi} f\setminus \operatorname {graph} f\\&=\bigcup _{x\in X}\left(\{x\}\times (f(x),\infty )\right)\end{alignedat}}$ where all sets being unioned in the last line are pairwise disjoint, and some may be empty.

## Relationships with other sets

Despite the fact that f might take one (or both) of $\pm \infty$ as a value (in which case its graph would *not* be a subset of $X\times \mathbb {R}$ ), the epigraph of f is nevertheless defined to be a subset of $X\times \mathbb {R}$ rather than of $X\times [-\infty ,\infty ].$ This is intentional because when X is a vector space then so is $X\times \mathbb {R}$ but $X\times [-\infty ,\infty ]$ is *never* a vector space (since the extended real number line $[-\infty ,\infty ]$ is not a vector space). This deficiency in $X\times [-\infty ,\infty ]$ remains even if instead of being a vector space, X is merely a non-empty subset of some vector space. The epigraph being a subset of a vector space allows for tools related to real analysis and functional analysis (and other fields) to be more readily applied.

The domain (rather than the codomain) of the function is not particularly important for this definition; it can be any linear space or even an arbitrary set instead of $\mathbb {R} ^{n}$ .

The strict epigraph $\operatorname {epi} _{S}f$ and the graph $\operatorname {graph} f$ are always disjoint.

The epigraph of a function $f:X\to [-\infty ,\infty ]$ is related to its graph and strict epigraph by $\,\operatorname {epi} f\,\subseteq \,\operatorname {epi} _{S}f\,\cup \,\operatorname {graph} f$ where set equality holds if and only if f is real-valued. However, $\operatorname {epi} f=\left[\operatorname {epi} _{S}f\,\cup \,\operatorname {graph} f\right]\,\cap \,[X\times \mathbb {R} ]$ always holds.

## Reconstructing functions from epigraphs

The epigraph is empty if and only if the function is identically equal to infinity.

Just as any function can be reconstructed from its graph, so too can any extended real-valued function f on X be reconstructed from its epigraph $E:=\operatorname {epi} f$ (even when f takes on $\pm \infty$ as a value). Given $x\in X,$ the value $f(x)$ can be reconstructed from the intersection $E\cap (\{x\}\times \mathbb {R} )$ of E with the "vertical line" $\{x\}\times \mathbb {R}$ passing through x as follows:

- case 1: $E\cap (\{x\}\times \mathbb {R} )=\varnothing$ if and only if $f(x)=\infty ,$
- case 2: $E\cap (\{x\}\times \mathbb {R} )=\{x\}\times \mathbb {R}$ if and only if $f(x)=-\infty ,$
- case 3: otherwise, $E\cap (\{x\}\times \mathbb {R} )$ is necessarily of the form $\{x\}\times [f(x),\infty ),$ from which the value of $f(x)$ can be obtained by taking the infimum of the interval.

The above observations can be combined to give a single formula for $f(x)$ in terms of $E:=\operatorname {epi} f.$ Specifically, for any $x\in X,$ $f(x)=\inf _{}\{r\in \mathbb {R} ~:~(x,r)\in E\}$ where by definition, $\inf _{}\varnothing :=\infty .$ This same formula can also be used to reconstruct f from its strict epigraph $E:=\operatorname {epi} _{S}f.$

## Relationships between properties of functions and their epigraphs

A function is convex if and only if its epigraph is a convex set. The epigraph of a real affine function $g:\mathbb {R} ^{n}\to \mathbb {R}$ is a halfspace in $\mathbb {R} ^{n+1}.$

A function is lower semicontinuous if and only if its epigraph is closed.
