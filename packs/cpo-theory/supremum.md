---
title: "Infimum and supremum"
source: https://en.wikipedia.org/wiki/Supremum
domain: cpo-theory
license: CC-BY-SA-4.0
tags: complete partial order, directed-complete partial order, chain-complete poset, least upper bound
fetched: 2026-07-02
---

# Infimum and supremum

(Redirected from

Supremum

)

In mathematics, the **infimum** (abbreviated **inf**; pl.: **infima**) of a subset S of a partially ordered set P is the greatest element in P that is less than or equal to each element of $S,$ if such an element exists. If the infimum of S exists, it is unique, and if *b* is a lower bound of S , then *b* is less than or equal to the infimum of S . Consequently, the term *greatest lower bound* (abbreviated as *GLB*) is also commonly used. The **supremum** (abbreviated **sup**; pl.: **suprema**) of a subset S of a partially ordered set P is the least element in P that is greater than or equal to each element of $S,$ if such an element exists. If the supremum of S exists, it is unique, and if *b* is an upper bound of S , then the supremum of S is less than or equal to *b*. Consequently, the supremum is also referred to as the *least upper bound* (or *LUB*).

The infimum is, in a precise sense, dual to the concept of a supremum. Infima and suprema of real numbers are common special cases that are important in analysis, and especially in Lebesgue integration. However, the general definitions remain valid in the more abstract setting of order theory where arbitrary partially ordered sets are considered.

The concepts of infimum and supremum are close to minimum and maximum, but are more useful in analysis because they better characterize special sets which may have *no minimum or maximum*. For instance, the set of positive real numbers $\mathbb {R} ^{+}$ (not including 0 ) does not have a minimum, because any given element of $\mathbb {R} ^{+}$ could simply be divided in half resulting in a smaller number that is still in $\mathbb {R} ^{+}.$ There is, however, exactly one infimum of the positive real numbers relative to the real numbers: $0,$ which is smaller than all the positive real numbers and greater than any other real number which could be used as a lower bound. An infimum of a set is always and only defined relative to a superset of the set in question. For example, there is no infimum of the positive real numbers inside the positive real numbers (as their own superset), nor any infimum of the positive real numbers inside the complex numbers with positive real part.

## Formal definition

A *lower bound* of a subset S of a partially ordered set $(P,\leq )$ is an element y of P such that

- $y\leq x$ for all $x\in S.$

A lower bound a of S is called an *infimum* (or *greatest lower bound*, or *meet*) of S if

- for all lower bounds y of S in $P,$ $y\leq a$ ( a is larger than any other lower bound).

Similarly, an *upper bound* of a subset S of a partially ordered set $(P,\leq )$ is an element z of P such that

- $z\geq x$ for all $x\in S.$

An upper bound b of S is called a *supremum* (or *least upper bound*, or *join*) of S if

- for all upper bounds z of S in $P,$ $z\geq b$ ( b is less than any other upper bound).

We can also define suprema and infima without restricting to sets. For example, there is no set containing all cardinal numbers (and there is no greatest cardinal number), but the axiom of choice implies that every set of cardinal numbers has a least upper bound among cardinal numbers. The axiom of choice is equivalent to the statement that every nonempty set of cardinal numbers has a minimum element (which is also the infimum of the set). The empty set of cardinal numbers has many lower bounds but no greatest lower bound among cardinal numbers.

## Existence and uniqueness

Infima and suprema do not necessarily exist. Existence of an infimum of a subset S of P can fail if S has no lower bound at all, or if the set of lower bounds does not contain a greatest element. (An example of this is the subset $\{x\in \mathbb {Q} :x^{2}<2\}$ of $\mathbb {Q}$ . It has upper bounds, such as 1.5, but no supremum in $\mathbb {Q}$ .)

Consequently, partially ordered sets for which certain infima are known to exist become especially interesting. For instance, a lattice is a partially ordered set in which all *nonempty finite* subsets have both a supremum and an infimum, and a complete lattice is a partially ordered set in which *all* subsets have both a supremum and an infimum. More information on the various classes of partially ordered sets that arise from such considerations are found in the article on completeness properties.

If the supremum of a subset S exists, it is unique. If S contains a greatest element, then that element is the supremum; otherwise, the supremum does not belong to S (or does not exist). Likewise, if the infimum exists, it is unique. If S contains a least element, then that element is the infimum; otherwise, the infimum does not belong to S (or does not exist).

## Relation to maximum and minimum elements

The infimum of a subset S of a partially ordered set $P,$ assuming it exists, does not necessarily belong to $S.$ If it does, it is a minimum or least element of $S.$ Similarly, if the supremum of S belongs to $S,$ it is a maximum or greatest element of $S.$

For example, consider the set of negative real numbers (excluding zero). This set has no greatest element, since for every element of the set, there is another, larger, element. For instance, for any negative real number $x,$ there is another negative real number ${\tfrac {x}{2}},$ which is greater. On the other hand, every real number greater than or equal to zero is certainly an upper bound on this set. Hence, 0 is the least upper bound of the negative reals, so the supremum is 0. This set has a supremum but no greatest element.

However, the definition of maximal and minimal elements is more general. In particular, a set can have many maximal and minimal elements, whereas infima and suprema are unique.

Whereas maxima and minima must be members of the subset that is under consideration, the infimum and supremum of a subset need not be members of that subset themselves.

### Minimal upper bounds

Finally, a partially ordered set may have many minimal upper bounds without having a least upper bound. Minimal upper bounds are those upper bounds for which there is no strictly smaller element that also is an upper bound. This does not say that each minimal upper bound is smaller than all other upper bounds, it merely is not greater. The distinction between "minimal" and "least" is only possible when the given order is not a total one. In a totally ordered set, like the real numbers, the concepts are the same.

As an example, let S be the set of all finite subsets of natural numbers and consider the partially ordered set obtained by taking all sets from S together with the set of integers $\mathbb {Z}$ and the set of positive real numbers $\mathbb {R} ^{+},$ ordered by subset inclusion as above. Then clearly both $\mathbb {Z}$ and $\mathbb {R} ^{+}$ are greater than all finite sets of natural numbers. Yet, neither is $\mathbb {R} ^{+}$ smaller than $\mathbb {Z}$ nor is the converse true: both sets are minimal upper bounds but none is a supremum.

### Least-upper-bound property

The *least-upper-bound property* is an example of the aforementioned completeness properties which is typical for the set of real numbers. This property is sometimes called *Dedekind completeness*.

If an ordered set S has the property that every nonempty subset of S having an upper bound also has a least upper bound, then S is said to have the least-upper-bound property. As noted above, the set $\mathbb {R}$ of all real numbers has the least-upper-bound property. Similarly, the set $\mathbb {Z}$ of integers has the least-upper-bound property; if S is a nonempty subset of $\mathbb {Z}$ and there is some number n such that every element s of S is less than or equal to $n,$ then there is a least upper bound u for $S,$ an integer that is an upper bound for S and is less than or equal to every other upper bound for $S.$ A well-ordered set also has the least-upper-bound property, and the empty subset has also a least upper bound: the minimum of the whole set.

An example of a set that *lacks* the least-upper-bound property is $\mathbb {Q} ,$ the set of rational numbers. Let S be the set of all rational numbers q such that $q^{2}<2.$ Then S has an upper bound ( $1000,$ for example, or 6 ) but no least upper bound in $\mathbb {Q}$ : If we suppose $p\in \mathbb {Q}$ is the least upper bound, a contradiction is immediately deduced because between any two reals x and y (including ${\sqrt {2}}$ and p ) there exists some rational $r,$ which itself would have to be the least upper bound (if $p>{\sqrt {2}}$ ) or a member of S greater than p (if $p<{\sqrt {2}}$ ). Another example is the hyperreals; there is no least upper bound of the set of positive infinitesimals.

There is a corresponding *greatest-lower-bound property*; an ordered set possesses the greatest-lower-bound property if and only if it also possesses the least-upper-bound property; the least-upper-bound of the set of lower bounds of a set is the greatest-lower-bound, and the greatest-lower-bound of the set of upper bounds of a set is the least-upper-bound of the set.

If in a partially ordered set P every bounded subset has a supremum, this applies also, for any set $X,$ in the function space containing all functions from X to $P,$ where $f\leq g$ if and only if $f(x)\leq g(x)$ for all $x\in X.$ For example, it applies for real functions, and, since these can be considered special cases of functions, for real n -tuples and sequences of real numbers.

The least-upper-bound property is an indicator of the suprema.

## Infima and suprema of real numbers

In analysis, infima and suprema of subsets S of the real numbers are particularly important. For instance, the negative real numbers do not have a greatest element, and their supremum is 0 (which is not a negative real number). The completeness of the real numbers implies (and is equivalent to) that any bounded nonempty subset S of the real numbers has an infimum and a supremum. If S is not bounded below, one often formally writes $\inf _{}S=-\infty .$ If S is empty, one writes $\inf _{}S=+\infty .$

### Properties

If A is any set of real numbers then $A\neq \varnothing$ if and only if $\sup A\geq \inf A,$ and otherwise $-\infty =\sup \varnothing <\inf \varnothing =\infty .$

**Set inclusion**

If $A\subseteq B$ are sets of real numbers then $\inf A\geq \inf B$ (if $A=\varnothing$ this reads as $\inf B\leq \infty$ ) and $\sup A\leq \sup B.$

**Image under functions** If $f\colon \mathbb {R} \to \mathbb {R}$ is a nondecreasing function and S is a nonempty bounded subset of $\mathbb {R}$ , then $f(\inf(S))\leq \inf(f[S])$ and $f(\sup(S))\geq \sup(f[S])$ , where the image is defined as $f[S]\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\{f(s):s\in S\}.$

**Identifying infima and suprema**

If the infimum of A exists (that is, $\inf A$ is a real number) and if p is any real number then $p=\inf A$ if and only if p is a lower bound and for every $\epsilon >0$ there is an $a_{\epsilon }\in A$ with $a_{\epsilon }<p+\epsilon .$ Similarly, if $\sup A$ is a real number and if p is any real number then $p=\sup A$ if and only if p is an upper bound and if for every $\epsilon >0$ there is an $a_{\epsilon }\in A$ with $a_{\epsilon }>p-\epsilon .$

**Relation to limits of sequences**

If $S\neq \varnothing$ is any non-empty set of real numbers then there always exists a non-decreasing sequence $s_{1}\leq s_{2}\leq \cdots$ in S such that $\lim _{n\to \infty }s_{n}=\sup S.$ Similarly, there will exist a (possibly different) non-increasing sequence $s_{1}\geq s_{2}\geq \cdots$ in S such that $\lim _{n\to \infty }s_{n}=\inf S.$ In particular, the infimum and supremum of a set belong to its closure if $\inf S\in \mathbb {R}$ then $\inf S\in {\bar {S}}$ and if $\sup S\in \mathbb {R}$ then $\sup S\in {\bar {S}}$

Expressing the infimum and supremum as a limit of a such a sequence allows theorems from various branches of mathematics to be applied. Consider for example the well-known fact from topology that if f is a continuous function and $s_{1},s_{2},\ldots$ is a sequence of points in its domain that converges to a point $p,$ then $f\left(s_{1}\right),f\left(s_{2}\right),\ldots$ necessarily converges to $f(p).$ It implies that if $\lim _{n\to \infty }s_{n}=\sup S$ is a real number (where all $s_{1},s_{2},\ldots$ are in S ) and if f is a continuous function whose domain contains S and $\sup S,$ then $f(\sup S)=f\left(\lim _{n\to \infty }s_{n}\right)=\lim _{n\to \infty }f\left(s_{n}\right),$ which (for instance) guarantees that $f(\sup S)$ is an adherent point of the set $f(S)\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\{f(s):s\in S\}.$ If in addition to what has been assumed, the continuous function f is also an increasing or non-decreasing function, then it is even possible to conclude that $\sup f(S)=f(\sup S).$ This may be applied, for instance, to conclude that whenever g is a real (or complex) valued function with domain $\Omega \neq \varnothing$ whose sup norm $\|g\|_{\infty }\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\sup _{x\in \Omega }|g(x)|$ is finite, then for every non-negative real number $q,$ $\|g\|_{\infty }^{q}~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\left(\sup _{x\in \Omega }|g(x)|\right)^{q}=\sup _{x\in \Omega }\left(|g(x)|^{q}\right)$ since the map $f:[0,\infty )\to \mathbb {R}$ defined by $f(x)=x^{q}$ is a continuous non-decreasing function whose domain $[0,\infty )$ always contains $S:=\{|g(x)|:x\in \Omega \}$ and $\sup S\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\|g\|_{\infty }.$

Although this discussion focused on $\sup ,$ similar conclusions can be reached for $\inf$ with appropriate changes (such as requiring that f be non-increasing rather than non-decreasing). Other norms defined in terms of $\sup$ or $\inf$ include the weak $L^{p,w}$ space norms (for $1\leq p<\infty$ ), the norm on Lebesgue space $L^{\infty }(\Omega ,\mu ),$ and operator norms. Monotone sequences in S that converge to $\sup S$ (or to $\inf S$ ) can also be used to help prove many of the formula given below, since addition and multiplication of real numbers are continuous operations.

### Arithmetic operations on sets

The following formulas depend on a notation that conveniently generalizes arithmetic operations on sets. Throughout, $A,B\subseteq \mathbb {R}$ are sets of real numbers.

**Sum of sets**

The Minkowski sum of two sets A and B of real numbers is the set $A+B~:=~\{a+b:a\in A,b\in B\}$ consisting of all possible arithmetic sums of pairs of numbers, one from each set. The infimum and supremum of the Minkowski sum satisfy, if $A\neq \varnothing \neq B$ $\inf(A+B)=(\inf A)+(\inf B)$ and $\sup(A+B)=(\sup A)+(\sup B).$

**Product of sets**

The multiplication of two sets A and B of real numbers is defined similarly to their Minkowski sum: $A\cdot B~:=~\{a\cdot b:a\in A,b\in B\}.$

If A and B are nonempty sets of positive real numbers then $\inf(A\cdot B)=(\inf A)\cdot (\inf B)$ and similarly for suprema $\sup(A\cdot B)=(\sup A)\cdot (\sup B).$

**Scalar product of a set**

The product of a real number r and a set B of real numbers is the set $rB~:=~\{r\cdot b:b\in B\}.$

If $r>0$ then $\inf(r\cdot A)=r(\inf A)\quad {\text{ and }}\quad \sup(r\cdot A)=r(\sup A),$ while if $r<0$ then $\inf(r\cdot A)=r(\sup A)\quad {\text{ and }}\quad \sup(r\cdot A)=r(\inf A).$ In the case $r=0$ , one has, if $A\neq \varnothing$ $\inf(0\cdot A)=0\quad {\text{ and }}\quad \sup(0\cdot A)=0$ Using $r=-1$ and the notation ${\textstyle -A:=(-1)A=\{-a:a\in A\},}$ it follows that, $\inf(-A)=-\sup A\quad {\text{ and }}\quad \sup(-A)=-\inf A.$

**Multiplicative inverse of a set**

For any set S that does not contain $0,$ let ${\frac {1}{S}}~:=\;\left\{{\tfrac {1}{s}}:s\in S\right\}.$

If $S\subseteq (0,\infty )$ is non-empty then ${\frac {1}{\sup _{}S}}~=~\inf _{}{\frac {1}{S}}$ where this equation also holds when $\sup _{}S=\infty$ if the definition ${\frac {1}{\infty }}:=0$ is used. This equality may alternatively be written as ${\frac {1}{\displaystyle \sup _{s\in S}s}}=\inf _{s\in S}{\tfrac {1}{s}}.$ Moreover, $\inf _{}S=0$ if and only if $\sup _{}{\tfrac {1}{S}}=\infty ,$ where if $\inf _{}S>0,$ then ${\tfrac {1}{\inf _{}S}}=\sup _{}{\tfrac {1}{S}}.$

## Duality

If one denotes by $P^{\operatorname {op} }$ the partially-ordered set P with the opposite order relation; that is, for all $x{\text{ and }}y,$ declare: $x\leq y{\text{ in }}P^{\operatorname {op} }\quad {\text{ if and only if }}\quad x\geq y{\text{ in }}P,$ then infimum of a subset S in P equals the supremum of S in $P^{\operatorname {op} }$ and vice versa.

For subsets of the real numbers, another kind of duality holds: $\inf S=-\sup(-S),$ where $-S:=\{-s~:~s\in S\}.$

## Examples

### Infima

- The infimum of the set of numbers $\{2,3,4\}$ is $2.$ The number 1 is a lower bound, but not the greatest lower bound, and hence not the infimum.
- More generally, if a set has a smallest element, then the smallest element is the infimum for the set. In this case, it is also called the minimum of the set.
- $\inf\{1,2,3,\ldots \}=1.$
- $\inf\{x\in \mathbb {R} :0<x<1\}=0.$
- $\inf \left\{x\in \mathbb {Q} :x^{3}>2\right\}={\sqrt[{3}]{2}}.$
- $\inf \left\{(-1)^{n}+{\tfrac {1}{n}}:n=1,2,3,\ldots \right\}=-1.$
- If $\left(x_{n}\right)_{n=1}^{\infty }$ is a decreasing sequence with limit $x,$ then $\inf x_{n}=x.$

### Suprema

- The supremum of the set of numbers $\{1,2,3\}$ is $3.$ The number 4 is an upper bound, but it is not the least upper bound, and hence is not the supremum.
- $\sup\{x\in \mathbb {R} :0<x<1\}=\sup\{x\in \mathbb {R} :0\leq x\leq 1\}=1.$
- $\sup \left\{(-1)^{n}-{\tfrac {1}{n}}:n=1,2,3,\ldots \right\}=1.$
- $\sup\{a+b:a\in A,b\in B\}=\sup A+\sup B.$
- $\sup \left\{x\in \mathbb {Q} :x^{2}<2\right\}={\sqrt {2}}.$

In the last example, the supremum of a set of rationals is irrational, which means that the rationals are incomplete.

One basic property of the supremum is $\sup\{f(t)+g(t):t\in A\}~\leq ~\sup\{f(t):t\in A\}+\sup\{g(t):t\in A\}$ for any functionals f and $g.$

The supremum of a subset S of $(\mathbb {N} ,\mid \,)$ where $\,\mid \,$ denotes "divides", is the lowest common multiple of the elements of $S.$

The supremum of a set S containing subsets of some set X is the union of the subsets when considering the partially ordered set $(P(X),\subseteq )$ , where P is the power set of X and $\,\subseteq \,$ is subset.
