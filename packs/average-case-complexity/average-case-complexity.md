---
title: "Average-case complexity"
source: https://en.wikipedia.org/wiki/Average-case_complexity
domain: average-case-complexity
license: CC-BY-SA-4.0
tags: average case complexity, distributional problem, planted clique problem, smoothed analysis
fetched: 2026-07-02
---

# Average-case complexity

In computational complexity theory, the **average-case complexity** of an algorithm is the amount of some computational resource (typically time) used by the algorithm, averaged over all possible inputs. It is frequently contrasted with worst-case complexity which considers the maximal complexity of the algorithm over all possible inputs.

There are three primary motivations for studying average-case complexity. First, although some problems may be intractable in the worst-case, the inputs which elicit this behavior may rarely occur in practice, so the average-case complexity may be a more accurate measure of an algorithm's performance. Second, average-case complexity analysis provides tools and techniques to generate hard instances of problems which can be utilized in areas such as cryptography and derandomization. Third, average-case complexity allows discriminating the most efficient algorithm in practice among algorithms of equivalent best case complexity (for instance Quicksort).

Average-case analysis requires a notion of an "average" input to an algorithm, which leads to the problem of devising a probability distribution over inputs. Alternatively, a randomized algorithm can be used. The analysis of such algorithms leads to the related notion of an **expected complexity**.

## History and background

The average-case performance of algorithms has been studied since modern notions of computational efficiency were developed in the 1950s. Much of this initial work focused on problems for which worst-case polynomial time algorithms were already known. In 1973, Donald Knuth published Volume 3 of the Art of Computer Programming which extensively surveys average-case performance of algorithms for problems solvable in worst-case polynomial time, such as sorting and median-finding.

An efficient algorithm for **NP**-complete problems is generally characterized as one which runs in polynomial time for all inputs; this is equivalent to requiring efficient worst-case complexity. However, an algorithm which is inefficient on a "small" number of inputs may still be efficient for "most" inputs that occur in practice. Thus, it is desirable to study the properties of these algorithms where the average-case complexity may differ from the worst-case complexity and find methods to relate the two.

The fundamental notions of average-case complexity were developed by Leonid Levin in 1986 when he published a one-page paper defining average-case complexity and completeness while giving an example of a complete problem for **distNP**, the average-case analogue of **NP**.

## Definitions

### Efficient average-case complexity

The first task is to precisely define what is meant by an algorithm which is efficient "on average". An initial attempt might define an efficient average-case algorithm as one which runs in expected polynomial time over all possible inputs. Such a definition has various shortcomings; in particular, it is not robust to changes in the computational model. For example, suppose algorithm A runs in time *t**A*(*x*) on input x and algorithm B runs in time *t**A*(*x*)2 on input x; that is, B is quadratically slower than A. Intuitively, any definition of average-case efficiency should capture the idea that A is efficient-on-average if and only if B is efficient on-average. Suppose, however, that the inputs are drawn randomly from the uniform distribution of strings with length n, and that A runs in time *n*2 on all inputs except the string 1*n* for which A takes time 2*n*. Then it can be easily checked that the expected running time of A is polynomial but the expected running time of B is exponential.

To create a more robust definition of average-case efficiency, it makes sense to allow an algorithm A to run longer than polynomial time on some inputs but the fraction of inputs on which A requires larger and larger running time becomes smaller and smaller. This intuition is captured in the following formula for average polynomial running time, which balances the polynomial trade-off between running time and fraction of inputs:

$\Pr _{x\in _{R}D_{n}}\left[t_{A}(x)\geq t\right]\leq {\frac {p(n)}{t^{\epsilon }}}$

for every *n*, *t* > 0 and polynomial p, where *t**A*(*x*) denotes the running time of algorithm A on input x, and ε is a positive constant value. Alternatively, this can be written as

$E_{x\in _{R}D_{n}}\left[{\frac {t_{A}(x)^{\epsilon }}{n}}\right]\leq C$

for some constants C and ε, where *n* = |*x*|. In other words, an algorithm A has good average-case complexity if, after running for *t**A*(*n*) steps, A can solve all but a ⁠*n**c*/(*t**A*(*n*))*ε*⁠ fraction of inputs of length n, for some *ε*, *c* > 0.

### Distributional problem

The next step is to define the "average" input to a particular problem. This is achieved by associating the inputs of each problem with a particular probability distribution. That is, an "average-case" problem consists of a language L and an associated probability distribution D which forms the pair (*L*, *D*). The two most common classes of distributions which are allowed are:

1. Polynomial-time computable distributions (**P**-computable): these are distributions for which it is possible to compute the cumulative density of any given input x. More formally, given a probability distribution μ and a string *x* ∈ {0, 1}*n* it is possible to compute the value $\mu (x)=\sum \limits _{y\in \{0,1\}^{n}:y\leq x}\Pr[y]$ in polynomial time. This implies that Pr[*x*] is also computable in polynomial time.
2. Polynomial-time samplable distributions (**P**-samplable): these are distributions from which it is possible to draw random samples in polynomial time.

These two formulations, while similar, are not equivalent. If a distribution is **P**-computable it is also **P**-samplable, but the converse is not true if **P** ≠ **P****#P**.

### AvgP and distNP

A distributional problem (*L*, *D*) is in the complexity class **AvgP** if there is an efficient average-case algorithm for L, as defined above. The class **AvgP** is occasionally called **distP** in the literature.

A distributional problem (*L*, *D*) is in the complexity class **distNP** if L is in **NP** and D is **P**-computable. When L is in **NP** and D is **P**-samplable, (*L*, *D*) belongs to **sampNP**.

Together, **AvgP** and **distNP** define the average-case analogues of **P** and **NP**, respectively.

## Reductions between distributional problems

Let (*L*,*D*) and (*L′*, *D′*) be two distributional problems. (*L*, *D*) average-case reduces to (*L′*, *D′*) (written (*L*, *D*) ≤**AvgP** (*L′*, *D′*)) if there is a function f that for every n, on input x can be computed in time polynomial in n and

1. (Correctness) *x* ∈ *L* if and only if *f*(*x*) ∈ *L′*
2. (Domination) There are polynomials p and m such that, for every n and y, $\sum \limits _{x:f(x)=y}D_{n}(x)\leq p(n)D'_{m(n)}(y)$

The domination condition enforces the notion that if problem (*L*, *D*) is hard on average, then (*L′*, *D′*) is also hard on average. Intuitively, a reduction should provide a way to solve an instance x of problem L by computing *f*(*x*) and feeding the output to the algorithm which solves L'. Without the domination condition, this may not be possible since the algorithm which solves L in polynomial time on average may take super-polynomial time on a small number of inputs but f may map these inputs into a much larger set of D' so that algorithm A' no longer runs in polynomial time on average. The domination condition only allows such strings to occur polynomially as often in D'.

### DistNP-complete problems

The average-case analogue to **NP**-completeness is **distNP**-completeness. A distributional problem (*L′*, *D′*) is **distNP**-complete if (*L′*, *D′*) is in **distNP** and for every (*L*, *D*) in **distNP**, (*L*, *D*) is average-case reducible to (*L′*, *D′*).

An example of a **distNP**-complete problem is the Bounded Halting Problem, (BH,*D*) (for any **P**-computable *D*) defined as follows:

$BH=\{(M,x,1^{t}):M{\text{ is a non-deterministic Turing machine that accepts }}x{\text{ in}}\leq t{\text{ steps}}\}$

In his original paper, Levin showed an example of a distributional tiling problem that is average-case **NP**-complete. A survey of known **distNP**-complete problems is available online.

One area of active research involves finding new **distNP**-complete problems. However, finding such problems can be complicated due to a result of Gurevich which shows that any distributional problem with a flat distribution cannot be **distNP**-complete unless **EXP** = **NEXP**. (A flat distribution μ is one for which there exists an *ε* > 0 such that for any x, *μ*(*x*) ≤ 2−|*x*|*ε*.) A result by Livne shows that all natural **NP**-complete problems have **DistNP**-complete versions. However, the goal of finding a natural distributional problem that is **DistNP**-complete has not yet been achieved.

## Applications

### Sorting algorithms

As mentioned above, much early work relating to average-case complexity focused on problems for which polynomial-time algorithms already existed, such as sorting. For example, many sorting algorithms which utilize randomness, such as Quicksort, have a worst-case running time of O(*n*2), but an average-case running time of O(*n* log(*n*)), where n is the length of the input to be sorted.

### Cryptography

For most problems, average-case complexity analysis is undertaken to find efficient algorithms for a problem that is considered difficult in the worst-case. In cryptographic applications, however, the opposite is true: the worst-case complexity is irrelevant; we instead want a guarantee that the average-case complexity of every algorithm which "breaks" the cryptographic scheme is inefficient.

Thus, all secure cryptographic schemes rely on the existence of one-way functions. Although the existence of one-way functions is still an open problem, many candidate one-way functions are based on hard problems such as integer factorization or computing the discrete log. Note that it is not desirable for the candidate function to be **NP**-complete since this would only guarantee that there is likely no efficient algorithm for solving the problem in the worst case; what we actually want is a guarantee that no efficient algorithm can solve the problem over random inputs (i.e. the average case). In fact, both the integer factorization and discrete log problems are in **NP** ∩ **coNP**, and are therefore not believed to be **NP**-complete. The fact that all of cryptography is predicated on the existence of average-case intractable problems in **NP** is one of the primary motivations for studying average-case complexity.

## Other results

Yao's principle, from a 1978 paper by Andrew Yao, shows that for broad classes of computational problems, average-case complexity for a hard input distribution and a deterministic algorithm adapted to that distribution is the same thing as expected complexity for a fast randomized algorithm and its worst-case input.

In 1990, Impagliazzo and Levin showed that if there is an efficient average-case algorithm for a **distNP**-complete problem under the uniform distribution, then there is an average-case algorithm for every problem in **NP** under any polynomial-time samplable distribution. Applying this theory to natural distributional problems remains an outstanding open question.

In 1992, Ben-David et al. showed that if all languages in **distNP** have good-on-average decision algorithms, they also have good-on-average search algorithms. Further, they show that this conclusion holds under a weaker assumption: if every language in **NP** is easy on average for decision algorithms with respect to the uniform distribution, then it is also easy on average for search algorithms with respect to the uniform distribution. Thus, cryptographic one-way functions can exist only if there are **distNP** problems over the uniform distribution that are hard on average for decision algorithms.

In 1993, Feigenbaum and Fortnow showed that it is not possible to prove, under non-adaptive random reductions, that the existence of a good-on-average algorithm for a **distNP**-complete problem under the uniform distribution implies the existence of worst-case efficient algorithms for all problems in **NP**. In 2003, Bogdanov and Trevisan generalized this result to arbitrary non-adaptive reductions. These results show that it is unlikely that any association can be made between average-case complexity and worst-case complexity via reductions.
