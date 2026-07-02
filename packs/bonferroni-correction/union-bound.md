---
title: "Boole's inequality"
source: https://en.wikipedia.org/wiki/Union_bound
domain: bonferroni-correction
license: CC-BY-SA-4.0
tags: Bonferroni correction, Holm Bonferroni, Sidak correction, union bound
fetched: 2026-07-02
---

# Boole's inequality

(Redirected from

Union bound

)

In probability theory, **Boole's inequality**, also known as the **union bound**, says that for any finite or countable set of events, the probability that at least one of the events happens is no greater than the sum of the probabilities of the individual events. This inequality provides an upper bound on the probability of occurrence of at least one of a countable number of events in terms of the individual probabilities of the events. Boole's inequality is named for its discoverer, George Boole.

Formally, for a countable set of events *A*1, *A*2, *A*3, ..., we have

${\mathbb {P} }\left(\bigcup _{i=1}^{\infty }A_{i}\right)\leq \sum _{i=1}^{\infty }{\mathbb {P} }(A_{i}).$

In measure-theoretic terms, Boole's inequality follows from the fact that a measure (and certainly any probability measure) is *σ*-sub-additive. Thus Boole's inequality holds not only for probability measures ${\mathbb {P} }$ , but more generally when ${\mathbb {P} }$ is replaced by any measure.

## Proof

### Proof using induction

Boole's inequality may be proved for finite collections of n events using the method of induction.

For the $n=1$ case, it follows that

$\mathbb {P} (A_{1})\leq \mathbb {P} (A_{1}).$

For the case n , we have

${\mathbb {P} }\left(\bigcup _{i=1}^{n}A_{i}\right)\leq \sum _{i=1}^{n}{\mathbb {P} }(A_{i}).$

Since $\mathbb {P} (A\cup B)=\mathbb {P} (A)+\mathbb {P} (B)-\mathbb {P} (A\cap B),$ and because the union operation is associative, we have

$\mathbb {P} \left(\bigcup _{i=1}^{n+1}A_{i}\right)=\mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)+\mathbb {P} (A_{n+1})-\mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\cap A_{n+1}\right).$

Since

${\mathbb {P} }\left(\bigcup _{i=1}^{n}A_{i}\cap A_{n+1}\right)\geq 0,$

by the first axiom of probability, we have

$\mathbb {P} \left(\bigcup _{i=1}^{n+1}A_{i}\right)\leq \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)+\mathbb {P} (A_{n+1}),$

and therefore

$\mathbb {P} \left(\bigcup _{i=1}^{n+1}A_{i}\right)\leq \sum _{i=1}^{n}\mathbb {P} (A_{i})+\mathbb {P} (A_{n+1})=\sum _{i=1}^{n+1}\mathbb {P} (A_{i}).$

### Proof without using induction

Let events $A_{1},A_{2},A_{3},\dots$ in our probability space be given. The countable additivity of the measure $\mathbb {P}$ states that if $B_{1},B_{2},B_{3},\dots$ are pairwise disjoint events, then

$\mathbb {P} \left(\bigcup _{i}B_{i}\right)=\sum _{i}\mathbb {P} (B_{i}).$

Set

$B_{i}:=A_{i}-\bigcup _{j=1}^{i-1}A_{j}.$

Then $B_{1},B_{2},B_{3},\dots$ are pairwise disjoint. We claim that:

$\bigcup _{i=1}^{\infty }A_{i}=\bigcup _{i=1}^{\infty }B_{i}.$

One inclusion is clear. Indeed, since $B_{i}\subset A_{i}$ for all i, thus $\bigcup _{i=1}^{\infty }B_{i}\subset \bigcup _{i=1}^{\infty }A_{i}$ .

For the other inclusion, let $x\in \bigcup _{i=1}^{\infty }A_{i}$ be given. Write k for the minimum positive integer such that $x\in A_{k}$ . Then $x\in A_{k}-\bigcup _{j=1}^{k-1}A_{j}=B_{k}$ . Thus $x\in \bigcup _{i=1}^{\infty }B_{i}$ . Therefore $\bigcup _{i=1}^{\infty }A_{i}\subset \bigcup _{i=1}^{\infty }B_{i}$ .

Therefore

$\mathbb {P} \left(\bigcup _{i}A_{i}\right)=\mathbb {P} \left(\bigcup _{i}B_{i}\right)=\sum _{i}\mathbb {P} (B_{i})\leq \sum _{i}\mathbb {P} (A_{i}),$

where the last inequality holds because $B_{i}\subset A_{i}$ implies that $\mathbb {P} (B_{i})\leq \mathbb {P} (A_{i}),$ for all i.

## Bonferroni inequalities

Boole's inequality for a finite number of events may be generalized to certain upper and lower bounds on the probability of finite unions of events. These bounds are known as **Bonferroni inequalities**, after Carlo Emilio Bonferroni; see Bonferroni (1936).

Let

$S_{1}:=\sum _{i=1}^{n}{\mathbb {P} }(A_{i}),\quad S_{2}:=\sum _{1\leq i_{1}<i_{2}\leq n}{\mathbb {P} }(A_{i_{1}}\cap A_{i_{2}}),\quad \ldots ,\quad S_{k}:=\sum _{1\leq i_{1}<\cdots <i_{k}\leq n}{\mathbb {P} }(A_{i_{1}}\cap \cdots \cap A_{i_{k}})$

for all integers *k* in {1, ..., *n*}.

Then, when $K\leq n$ is odd:

$\sum _{j=1}^{K}(-1)^{j-1}S_{j}\geq \mathbb {P} {\Big (}\bigcup _{i=1}^{n}A_{i}{\Big )}=\sum _{j=1}^{n}(-1)^{j-1}S_{j}$

holds, and when $K\leq n$ is even:

$\sum _{j=1}^{K}(-1)^{j-1}S_{j}\leq \mathbb {P} {\Big (}\bigcup _{i=1}^{n}A_{i}{\Big )}=\sum _{j=1}^{n}(-1)^{j-1}S_{j}$

holds.

The inequalities follow from the inclusion–exclusion principle, and Boole's inequality is the special case of $K=1$ . Since the proof of the inclusion-exclusion principle requires only the finite additivity (and nonnegativity) of $\mathbb {P}$ , the Bonferroni inequalities holds more generally when $\mathbb {P}$ is replaced by any finite content, in the sense of measure theory.

### Proof for odd K

Let $E=\bigcap _{i=1}^{n}B_{i}$ , where $B_{i}\in \{A_{i},A_{i}^{c}\}$ for each $i=1,\dots ,n$ . These such E partition the sample space, and for each E and every i , E is either contained in $A_{i}$ or disjoint from it.

If $E=\bigcap _{i=1}^{n}A_{i}^{c}$ , then E contributes 0 to both sides of the inequality.

Otherwise, assume E is contained in exactly L of the $A_{i}$ . Then E contributes exactly $\mathbb {P} (E)$ to the right side of the inequality, while it contributes

$\sum _{j=1}^{K}(-1)^{j-1}{L \choose j}\mathbb {P} (E)$

to the left side of the inequality. However, by Pascal's rule, this is equal to

$\sum _{j=1}^{K}(-1)^{j-1}{\Big (}{L-1 \choose j-1}+{L-1 \choose j}{\Big )}\mathbb {P} (E)$

which telescopes to

${\Big (}1+{L-1 \choose K}{\Big )}\mathbb {P} (E)\geq \mathbb {P} (E)$

Thus, the inequality holds for all events E , and so by summing over E , we obtain the desired inequality:

$\sum _{j=1}^{K}(-1)^{j-1}S_{j}\geq \mathbb {P} {\Big (}\bigcup _{i=1}^{n}A_{i}{\Big )}$

The proof for even K is nearly identical.

### Example

Suppose that you are estimating five parameters based on a random sample, and you can control each parameter separately. If you want your estimations of all five parameters to be good with a chance 95%, what should you do to each parameter?

Tuning each parameter's chance to be good to within 95% is not enough because "all are good" is a subset of each event "Estimate *i* is good". We can use Boole's Inequality to solve this problem. By finding the complement of event "all five are good", we can change this question into another condition:

P

(at least one estimation is bad) = 0.05 ≤

P

(

A

1

is bad) +

P

(

A

2

is bad) +

P

(

A

3

is bad) +

P

(

A

4

is bad) +

P

(

A

5

is bad)

One way is to make each of them equal to 0.05/5 = 0.01, that is 1%. In other words, you have to guarantee each estimate good to 99%( for example, by constructing a 99% confidence interval) to make sure the total estimation to be good with a chance 95%. This is called the Bonferroni Method of simultaneous inference.
