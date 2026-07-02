---
title: "Rademacher complexity"
source: https://en.wikipedia.org/wiki/Rademacher_complexity
domain: vc-dimension
license: CC-BY-SA-4.0
tags: vapnik chervonenkis dimension, shattering set, growth function, sauer shelah lemma
fetched: 2026-07-02
---

# Rademacher complexity

In computational learning theory (machine learning and theory of computation), **Rademacher complexity**, named after Hans Rademacher, measures richness of a class of sets with respect to a probability distribution. The concept can also be extended to real valued functions.

## Definitions

### Rademacher complexity of a set

Given a set $A\subseteq \mathbb {R} ^{m}$ , the **Rademacher complexity of** *A* is defined as follows:

$\operatorname {Rad} (A):={\frac {1}{m}}\mathbb {E} _{\sigma }\left[\sup _{a\in A}\sum _{i=1}^{m}\sigma _{i}a_{i}\right]$

where $\sigma _{1},\sigma _{2},\dots ,\sigma _{m}$ are independent random variables drawn from the Rademacher distribution i.e. $\Pr(\sigma _{i}=+1)=\Pr(\sigma _{i}=-1)=1/2$ for $i\in \{1,2,\dots ,m\}$ , and $a=(a_{1},\ldots ,a_{m})\in A$ . Some authors take the absolute value of the sum before taking the supremum, but if A is symmetric this makes no difference.

### Rademacher complexity of a function class

Let $S=\{z_{1},z_{2},\dots ,z_{m}\}\subseteq Z$ be a sample of points and consider a function class ${\mathcal {F}}$ of real-valued functions over Z . Then, the **empirical Rademacher complexity** of ${\mathcal {F}}$ given S is defined as:

$\operatorname {Rad} _{S}({\mathcal {F}})={\frac {1}{m}}\mathbb {E} _{\sigma }\left[\sup _{f\in {\mathcal {F}}}\left|\sum _{i=1}^{m}\sigma _{i}f(z_{i})\right|\right]$

This can also be written using the previous definition:

$\operatorname {Rad} _{S}({\mathcal {F}})=\operatorname {Rad} ({\mathcal {F}}\circ S)$

where ${\mathcal {F}}\circ S$ denotes function composition, i.e.:

${\mathcal {F}}\circ S:=\{(f(z_{1}),\ldots ,f(z_{m}))\mid f\in {\mathcal {F}}\}$

The **worst case empirical Rademacher complexity** is ${\overline {\operatorname {Rad} }}_{m}({\mathcal {F}})=\sup _{S=\{z_{1},\dots ,z_{m}\}}\operatorname {Rad} _{S}({\mathcal {F}})$ Let P be a probability distribution over Z . The **Rademacher complexity** of the function class ${\mathcal {F}}$ with respect to P for sample size m is:

$\operatorname {Rad} _{P,m}({\mathcal {F}}):=\mathbb {E} _{S\sim P^{m}}\left[\operatorname {Rad} _{S}({\mathcal {F}})\right]$

where the above expectation is taken over an identically independently distributed (i.i.d.) sample $S=(z_{1},z_{2},\dots ,z_{m})$ generated according to P .

## Intuition

The Rademacher complexity is typically applied on a function class of models that are used for classification, with the goal of measuring their ability to classify points drawn from a probability space under arbitrary labellings. When the function class is rich enough, it contains functions that can appropriately adapt for each arrangement of labels, simulated by the random draw of $\sigma _{i}$ under the expectation, so that this quantity in the sum is maximized.

The Rademacher complexity of a set A can be rewritten as $\operatorname {Rad} (A):={\frac {1}{m}}\mathbb {E} _{\sigma }\left[\sup _{a\in A}\sum _{i=1}^{m}\sigma _{i}a_{i}\right]={\frac {1}{{\sqrt {m}}2^{m}}}\sum _{\sigma \in \{-1/{\sqrt {m}},+1/{\sqrt {m}}\}^{m}}\left[\sup _{a\in A}\langle \sigma ,a\rangle \right].$ Each term in the summation is the farthest distance of the set A from the origin, along a unit-length direction $\sigma$ . The directions are along the vertices of a hypercube. Thus, we can also write it as $\operatorname {Rad} (A)={\frac {1}{2{\sqrt {m}}}}{\frac {1}{2^{m-1}}}\sum _{\sigma \in \{-1/{\sqrt {m}},+1/{\sqrt {m}}\}^{m}/\{-1,+1\}}\left[\sup _{a\in A}\langle \sigma ,a\rangle -\inf _{a\in A}\langle \sigma ,a\rangle \right]$ Here, the set $\{-1/{\sqrt {m}},+1/{\sqrt {m}}\}^{m}/\{-1,+1\}$ denotes half of the vertices of a hypercube, selected so that each diagonal has exactly one vertex selected.

In words, this states that $2{\sqrt {m}}\operatorname {Rad} (A)$ is precisely the average width of the set A along all diagonal directions of a hypercube.

## Examples

A singleton set has 0 width in any direction, so it has Rademacher complexity 0.

The set $A=\{(1,1),(1,2)\}\subseteq \mathbb {R} ^{2}$ has average width $1/{\sqrt {2}}$ along the two diagonal directions of the square, so it has Rademacher complexity $1/4$ .

The unit cube $[0,1]^{m}$ has constant width ${\sqrt {m}}$ along the diagonal directions, so it has Rademacher complexity $1/2$ . Similarly, the unit cross-polytope $\{x\in \mathbb {R} ^{m}:\|x\|_{1}\leq 1\}$ has constant width $2/{\sqrt {m}}$ along the diagonal directions, so it has Rademacher complexity $1/m$ .

## Using the Rademacher complexity

The Rademacher complexity can be used to derive data-dependent upper-bounds on the learnability of function classes. Intuitively, a function-class with smaller Rademacher complexity is easier to learn.

### Bounding the representativeness

In machine learning, it is desired to have a training set that represents the true distribution of some sample data S . This can be quantified using the notion of **representativeness**. Denote by P the probability distribution from which the samples are drawn. Denote by H the set of hypotheses (potential classifiers) and denote by ${\mathcal {F}}$ the corresponding set of error functions, i.e., for every hypothesis $h\in H$ , there is a function $f_{h}\in F$ , that maps each training sample (features,label) to the error of the classifier h (note in this case hypothesis and classifier are used interchangeably). For example, in the case that h represents a binary classifier, the error function is a 0–1 loss function, i.e. the error function $f_{h}$ returns 0 if h correctly classifies a sample and 1 else. We omit the index and write f instead of $f_{h}$ when the underlying hypothesis is irrelevant. Define:

$L_{P}(f):=\mathbb {E} _{z\sim P}[f(z)]$

– the expected error of some error function

$f\in {\mathcal {F}}$

on the real distribution

P

;

$L_{S}(f):={1 \over m}\sum _{i=1}^{m}f(z_{i})$

– the estimated error of some error function

$f\in {\mathcal {F}}$

on the sample

S

.

The representativeness of the sample S , with respect to P and ${\mathcal {F}}$ , is defined as:

$\operatorname {Rep} _{P}({\mathcal {F}},S):=\sup _{f\in F}(L_{P}(f)-L_{S}(f))$

Smaller representativeness is better, since it provides a way to avoid overfitting: it means that the true error of a classifier is not much higher than its estimated error, and so selecting a classifier that has low estimated error will ensure that the true error is also low. Note however that the concept of representativeness is relative and hence can not be compared across distinct samples.

The expected representativeness of a sample can be bounded above by the Rademacher complexity of the function class: If ${\mathcal {F}}$ is a set of functions with range within $[0,1]$ , then

$\operatorname {Rad} _{P,m}({\mathcal {F}})-{\sqrt {\frac {\ln 2}{2m}}}\leq \mathbb {E} _{S\sim P^{m}}[\operatorname {Rep} _{P}({\mathcal {F}},S)]\leq 2\operatorname {Rad} _{P,m}({\mathcal {F}})$

Furthermore, the representativeness is concentrated around its expectation: For any $\epsilon$ , with probability $\geq 1-2e^{-2\epsilon ^{2}m}$ , $\operatorname {Rep} _{P}({\mathcal {F}},S)\in \mathbb {E} _{S\sim P^{m}}[\operatorname {Rep} _{P}({\mathcal {F}},S)]\pm \epsilon$

### Bounding the generalization error

The Rademacher complexity is a theoretical justification for empirical risk minimization.

When the error function is binary (0-1 loss), for every $\delta >0$ ,

$\sup _{f\in {\mathcal {F}}}(L_{P}(f)-L_{S}(f))\leq 2\operatorname {Rad} _{S}({\mathcal {F}})+4{\sqrt {2\ln(4/\delta ) \over m}}$

with probability at least $1-\delta$ .

There exists a constant $c>0$ , such that when the error function is squared $\ell ({\hat {y}},y):=({\hat {y}}-y)^{2}$ , and the function class ${\mathcal {F}}$ consists of functions with range within $[-1,+1]$ , then for any $\delta >0$ $L_{P}(f)-L_{S}(f)\leq c\left[L_{S}(f)+(\ln m)^{4}{\overline {\operatorname {Rad} }}_{m}({\mathcal {F}})^{2}+{\frac {\ln(1/\delta )}{m}}\right],\quad \forall f\in {\mathcal {F}}$ with probability at least $1-\delta$ .

### Oracle inequalities

Let the Bayes risk $L^{*}=\inf _{f}L_{P}(f)$ , where f can be *any* measurable function.

Let the function class ${\mathcal {F}}$ be split into "complexity classes" ${\mathcal {F}}_{r}$ , where $r\in \mathbb {R}$ are levels of complexity. Let $p_{r}$ be real numbers. Let the complexity measure function p be defined such that $p(f):=\min\{p_{r}:f\in {\mathcal {F}}_{r}\}$ .

For any dataset S , let ${\hat {f}}$ be a minimizer of $L_{S}(f)+p(f)$ . If $\sup _{f\in {\mathcal {F}}_{r}}|L_{P}(f)-L_{S}(f)|\leq p_{r},\quad \forall r$ then we have the oracle inequality $L({\hat {f}})-L^{*}\leq \inf _{r}\left(\inf _{f\in {\mathcal {F}}_{r}}L(f)-L^{*}+2p_{r}\right)$ Define $f_{r}^{*}\in \arg \min _{f\in {\mathcal {F}}_{r}}L(f)$ . If we further assume $r\leq s{\text{ implies }}{\mathcal {F}}_{r}\subseteq {\mathcal {F}}_{s}{\text{ and }}p_{r}\leq p_{s}$ and ${\begin{aligned}\forall r,\sup _{f\in {\mathcal {F}}_{r}}\left(L_{P}(f)-L_{P}\left(f_{r}^{*}\right)-2\left(L_{S}(f)-L_{S}\left(f_{r}^{*}\right)\right)\right)&\leq 2p_{r}/7\\\sup _{f\in {\mathcal {F}}_{r}}\left(L_{S}(f)-L_{S}\left(f_{r}^{*}\right)-2\left(L_{P}(f)-L_{P}\left(f_{r}^{*}\right)\right)\right)&\leq 2p_{r}/7\end{aligned}}$ then we have the oracle inequality $L_{P}({\widehat {f}})-L^{*}\leq \inf _{r}\left(\inf _{f\in {\mathcal {F}}_{r}}L_{P}(f)-L^{*}+3p_{r}\right)$

## Bounding the Rademacher complexity

Since smaller Rademacher complexity is better, it is useful to have upper bounds on the Rademacher complexity of various function sets. The following rules can be used to upper-bound the Rademacher complexity of a set $A\subset \mathbb {R} ^{m}$ .

- If all vectors in A are translated by a constant vector $a_{0}\in \mathbb {R} ^{m}$ , then Rad(*A*) does not change.
- If all vectors in A are multiplied by a scalar $c\in \mathbb {R}$ , then Rad(*A*) is multiplied by $|c|$ .
- $\operatorname {Rad} (A+B)=\operatorname {Rad} (A)+\operatorname {Rad} (B)$ .
- (Kakade & Tewari Lemma) If all vectors in A are operated by a Lipschitz function, then Rad(*A*) is (at most) multiplied by the Lipschitz constant of the function. In particular, if all vectors in A are operated by a contraction mapping, then Rad(*A*) strictly decreases.
- The Rademacher complexity of the convex hull of A equals Rad(*A*).
- (Massart Lemma) The Rademacher complexity of a finite set grows logarithmically with the set size. Formally, let A be a set of N vectors in $\mathbb {R} ^{m}$ , and let ${\bar {a}}$ be the mean of the vectors in A . Then:

$\operatorname {Rad} (A)\leq \max _{a\in A}\|a-{\bar {a}}\|\cdot {{\sqrt {2\log N}} \over m}$

In particular, if A is a set of binary vectors, the norm is at most ${\sqrt {m}}$ , so:

$\operatorname {Rad} (A)\leq {\sqrt {2\log N \over m}}$

Let H be a set family whose VC dimension is d . It is known that the growth function of H is bounded as:

for all

$m>d+1$

:

$\operatorname {Growth} (H,m)\leq (em/d)^{d}$

This means that, for every set h with at most m elements, $|H\cap h|\leq (em/d)^{d}$ . The set-family $H\cap h$ can be considered as a set of binary vectors over $\mathbb {R} ^{m}$ . Substituting this in Massart's lemma gives:

$\operatorname {Rad} (H\cap h)\leq {\sqrt {2d\log(em/d) \over m}}$

With more advanced techniques (Dudley's entropy bound and Haussler's upper bound) one can show, for example, that there exists a constant C , such that any class of $\{0,1\}$ -indicator functions with Vapnik–Chervonenkis dimension d has Rademacher complexity upper-bounded by $C{\sqrt {\frac {d}{m}}}$ .

The following bounds are related to linear operations on S – a constant set of m vectors in $\mathbb {R} ^{n}$ .

- Define $A_{2}=\{(w\cdot x_{1},\ldots ,w\cdot x_{m})\mid \|w\|_{2}\leq 1\}=$ the set of dot-products of the vectors in S with vectors in the unit ball. Then:

$\operatorname {Rad} (A_{2})\leq {\max _{i}\|x_{i}\|_{2} \over {\sqrt {m}}}$

- Define $A_{1}=\{(w\cdot x_{1},\ldots ,w\cdot x_{m})\mid \|w\|_{1}\leq 1\}=$ the set of dot-products of the vectors in S with vectors in the unit ball of the 1-norm. Then:

$\operatorname {Rad} (A_{1})\leq \max _{i}\|x_{i}\|_{\infty }\cdot {\sqrt {2\log(2n) \over m}}$

The following bound relates the Rademacher complexity of a set A to its external covering number – the number of balls of a given radius r whose union contains A . The bound is attributed to Dudley.

Suppose $A\subset \mathbb {R} ^{m}$ is a set of vectors whose length (norm) is at most c . Then, for every integer $M>0$ :

$\operatorname {Rad} (A)\leq {c\cdot 2^{-M} \over {\sqrt {m}}}+{6c \over m}\cdot \sum _{i=1}^{M}2^{-i}{\sqrt {\log \left(N_{c\cdot 2^{-i}}^{\text{ext}}(A)\right)}}$

In particular, if A lies in a *d*-dimensional subspace of $\mathbb {R} ^{m}$ , then:

$\forall r>0:N_{r}^{\text{ext}}(A)\leq (2c{\sqrt {d}}/r)^{d}$

Substituting this in the previous bound gives the following bound on the Rademacher complexity:

$\operatorname {Rad} (A)\leq {6c \over m}\cdot {\bigg (}{\sqrt {d\log(2{\sqrt {d}})}}+2{\sqrt {d}}{\bigg )}=O{\bigg (}{c{\sqrt {d\log(d)}} \over m}{\bigg )}$

## Gaussian complexity

**Gaussian complexity** is a similar complexity with similar physical meanings, and can be obtained from the Rademacher complexity using the random variables $g_{i}$ instead of $\sigma _{i}$ , where $g_{i}$ are Gaussian i.i.d. random variables with zero-mean and variance 1, i.e. $g_{i}\sim {\mathcal {N}}(0,1)$ . Gaussian and Rademacher complexities are known to be equivalent up to logarithmic factors.

### Equivalence of Rademacher and Gaussian complexity

Given a set $A\subseteq \mathbb {R} ^{n}$ then it holds that: ${\frac {G(A)}{2{\sqrt {\log {n}}}}}\leq {\text{Rad}}(A)\leq {\sqrt {\frac {\pi }{2}}}G(A)$ Where $G(A)$ is the Gaussian Complexity of A. As an example, consider the rademacher and gaussian complexities of the L1 ball. The Rademacher complexity is given by exactly 1, whereas the Gaussian complexity is on the order of ${\sqrt {\log d}}$ (which can be shown by applying known properties of suprema of a set of subgaussian random variables).
