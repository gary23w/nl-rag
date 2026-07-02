---
title: "Space hierarchy theorem"
source: https://en.wikipedia.org/wiki/Space_hierarchy_theorem
domain: space-complexity-classes
license: CC-BY-SA-4.0
tags: space complexity, savitch theorem, space hierarchy theorem, reachability problem
fetched: 2026-07-02
---

# Space hierarchy theorem

In computational complexity theory, the **space hierarchy theorems** are separation results that show that both deterministic and nondeterministic machines can solve more problems in (asymptotically) more space, subject to certain conditions. For example, a deterministic Turing machine can solve more decision problems in space *n* log *n* than in space *n*. The somewhat weaker analogous theorems for time are the time hierarchy theorems.

The foundation for the hierarchy theorems lies in the intuition that with either more time or more space comes the ability to compute more functions (or decide more languages). The hierarchy theorems are used to demonstrate that the time and space complexity classes form a hierarchy where classes with tighter bounds contain fewer languages than those with more relaxed bounds. Here we define and prove the space hierarchy theorem.

The space hierarchy theorems rely on the concept of space-constructible functions. The deterministic and nondeterministic space hierarchy theorems state that for all space-constructible functions $f(n)$ and all $g(n)\in o(f(n))$ ,

${\mathsf {SPACE}}(g(n))\subsetneq {\mathsf {SPACE}}(f(n))$

,

where SPACE stands for either DSPACE or NSPACE, and o refers to the little o notation.

## Statement

Formally, a function $f:\mathbb {N} \longrightarrow \mathbb {N}$ is space-constructible if $f(n)\geq \log ~n$ and there exists a Turing machine which computes the function $f(n)$ in space $O(f(n))$ when starting with an input $1^{n}$ , where $1^{n}$ represents a string of *n* consecutive 1s. Most of the common functions that we work with are space-constructible, including polynomials, exponents, and logarithms.

For every space-constructible function $f:\mathbb {N} \longrightarrow \mathbb {N}$ , there exists a language L that is decidable in space $O(f(n))$ but not in space $o(f(n))$ .

## Proof

The goal is to define a language that can be decided in space $O(f(n))$ but not space $o(f(n))$ . The language is defined as L:

> $L=\{~(\langle M\rangle ,10^{k}):M{\mbox{ uses space }}\leq f(|\langle M\rangle ,10^{k}|){\mbox{ and time }}\leq 2^{f(|\langle M\rangle ,10^{k}|)}{\mbox{ and }}M{\mbox{ does not accept }}(\langle M\rangle ,10^{k})~\}$

For any machine M that decides a language in space $o(f(n))$ , L will differ in at least one spot from the language of M. Namely, for some large enough k, M will use space $\leq f(|\langle M\rangle ,10^{k}|)$ on $(\langle M\rangle ,10^{k})$ and will therefore differ at its value.

On the other hand, L is in ${\mathsf {SPACE}}(f(n))$ . The algorithm for deciding the language L is as follows:

1. On an input x, compute $f(|x|)$ using space-constructibility, and mark off $f(|x|)$ cells of tape. Whenever an attempt is made to use more than $f(|x|)$ cells, *reject*.
2. If x is not of the form $\langle M\rangle ,10^{k}$ for some TM M, *reject*.
3. Simulate M on input x for at most $2^{f(|x|)}$ steps (using $f(|x|)$ space). If the simulation tries to use more than $f(|x|)$ space or more than $2^{f(|x|)}$ operations, then *reject*.
4. If M accepted x during this simulation, then *reject*; otherwise, *accept*.

Note on step 3: Execution is limited to $2^{f(|x|)}$ steps in order to avoid the case where M does not halt on the input x. That is, the case where M consumes space of only $O(f(x))$ as required, but runs for infinite time.

The above proof holds for the case of PSPACE, but some changes need to be made for the case of NPSPACE. The crucial point is that while on a deterministic TM, acceptance and rejection can be inverted (crucial for step 4), this is not possible on a non-deterministic machine.

For the case of NPSPACE, L needs to be redefined first:

> $L=\{~(\langle M\rangle ,10^{k}):M{\mbox{ uses space }}\leq f(|\langle M\rangle ,10^{k}|){\mbox{ and }}M{\mbox{ accepts }}(\langle M\rangle ,10^{k})~\}$

Now, the algorithm needs to be changed to accept L by modifying step 4 to:

- If M accepted x during this simulation, then *accept*; otherwise, *reject*.

L can not be decided by a TM using $o(f(n))$ cells. Assuming L can be decided by some TM M using $o(f(n))$ cells, and following from the Immerman–Szelepcsényi theorem, ${\overline {L}}$ can also be determined by a TM (called ${\overline {M}}$ ) using $o(f(n))$ cells. Here lies the contradiction, therefore the assumption must be false:

1. If $w=(\langle {\overline {M}}\rangle ,10^{k})$ (for some large enough k) is not in ${\overline {L}}$ then M will accept it, therefore ${\overline {M}}$ rejects w, therefore w is in ${\overline {L}}$ (contradiction).
2. If $w=(\langle {\overline {M}}\rangle ,10^{k})$ (for some large enough k) is in ${\overline {L}}$ then M will reject it, therefore ${\overline {M}}$ accepts w, therefore w is not in ${\overline {L}}$ (contradiction).

## Comparison and improvements

The space hierarchy theorem is stronger than the analogous time hierarchy theorems in several ways:

- It only requires s(n) to be at least log *n* instead of at least *n*.
- It can separate classes with any asymptotic difference, whereas the time hierarchy theorem requires them to be separated by a logarithmic factor.
- It only requires the function to be space-constructible, not time-constructible.
- It only requires $f(n)$ to be space-constructible, with no constraint on the constructability of $g(n)$ .
- However, it is known from results in axiomatic complexity theory that the theorem is false if $f(n)$ is not required to be space-constructible.

It seems to be easier to separate classes in space than in time. Indeed, whereas the time hierarchy theorem has seen little remarkable improvement since its inception, the nondeterministic space hierarchy theorem has seen at least one important improvement by Viliam Geffert in his 2003 paper "Space hierarchy theorem revised". This paper made several generalizations of the theorem:

- It relaxes the space-constructibility requirement. Let s be a nondeterministically fully space-constructible function. Let ⁠ $f(n)$ ⁠ be an arbitrary ⁠ $\Omega (s(n))$ ⁠ function, and $g(n)$ be a computable ⁠ $o(s(n))$ ⁠ function. These functions need not be space-constructible or even monotone increasing. Then ⁠ ${\mathsf {DSPACE}}(f(n))\subsetneq {\mathsf {DSPACE}}(g(n))$ ⁠ and ⁠ ${\mathsf {NSPACE}}(f(n))\subsetneq {\mathsf {NSPACE}}(g(n))$ ⁠.
- It identifies a unary language, or tally language, which is in one class but not the other. In the original theorem, the separating language was arbitrary.
- It does not require ⁠ $s(n)$ ⁠ to be at least log *n*; it can be any nondeterministically fully space-constructible function.

## Refinement of space hierarchy

If space is measured as the number of cells used regardless of alphabet size, then ⁠ ${\mathsf {SPACE}}(f(n))={\mathsf {SPACE}}(O(f(n)))$ ⁠ because one can achieve any linear compression by switching to a larger alphabet. However, by measuring space in bits, a much sharper separation is achievable for deterministic space. Instead of being defined up to a multiplicative constant, space is now defined up to an additive constant. However, because any constant amount of external space can be saved by storing the contents into the internal state, we still have ⁠ ${\mathsf {SPACE}}(f(n))={\mathsf {SPACE}}(f(n)+O(1))$ ⁠.

Assume that f is space-constructible. SPACE is deterministic.

- For a wide variety of sequential computational models, including for Turing machines, SPACE(*f*(*n*)-ω(log(*f*(*n*)+*n*))) ⊊ SPACE(*f*(*n*)). This holds even if SPACE(*f*(*n*)-*ω*(log(*f*(*n*)+*n*))) is defined using a different computational model than ⁠ ${\mathsf {SPACE}}(f(n))$ ⁠ because the different models can simulate each other with ⁠ $O(\log(f(n)+n))$ ⁠ space overhead.
- For certain computational models, we even have SPACE(*f*(*n*)-*ω*(1)) ⊊ SPACE(*f*(*n*)). In particular, this holds for Turing machines if we fix the alphabet, the number of heads on the input tape, the number of heads on the worktape (using a single worktape), and add delimiters for the visited portion of the worktape (that can be checked without increasing space usage). SPACE(*f*(*n*)) does not depend on whether the worktape is infinite or semi-infinite. We can also have a fixed number of worktapes if *f*(*n*) is either a SPACE constructible tuple giving the per-tape space usage, or a SPACE(*f*(*n*)-*ω*(log(*f*(*n*)))-constructible number giving the total space usage (not counting the overhead for storing the length of each tape).

The proof is similar to the proof of the space hierarchy theorem, but with two complications: The universal Turing machine has to be space-efficient, and the reversal has to be space-efficient. One can generally construct universal Turing machines with ⁠ $O(\log(space))$ ⁠ space overhead, and under appropriate assumptions, just ⁠ $O(1)$ ⁠ space overhead (which may depend on the machine being simulated). For the reversal, the key issue is how to detect if the simulated machine rejects by entering an infinite (space-constrained) loop. Simply counting the number of steps taken would increase space consumption by about ⁠ $f(n)$ ⁠. At the cost of a potentially exponential time increase, loops can be detected space-efficiently as follows:

Modify the machine to erase everything and go to a specific configuration A on success. Use depth-first search to determine whether A is reachable in the space bound from the starting configuration. The search starts at A and goes over configurations that lead to A. Because of determinism, this can be done in place and without going into a loop.

It can also be determined whether the machine exceeds a space bound (as opposed to looping within the space bound) by iterating over all configurations about to exceed the space bound and checking (again using depth-first search) whether the initial configuration leads to any of them.

## Corollaries

### Corollary 1

*For any two functions $f_{1}$ , $f_{2}:\mathbb {N} \longrightarrow \mathbb {N}$ , where $f_{1}(n)$ is $o(f_{2}(n))$ and $f_{2}$ is space-constructible, ${\mathsf {SPACE}}(f_{1}(n))\subsetneq {\mathsf {SPACE}}(f_{2}(n))$ .*

This corollary lets us separate various space complexity classes. For any natural number k, the function $n^{k}$ is space-constructible. Therefore for any two natural numbers $k_{1}<k_{2}$ we can prove ${\mathsf {SPACE}}(n^{k_{1}})\subsetneq {\mathsf {SPACE}}(n^{k_{2}})$ .

### Corollary 2

NL

⊊

PSPACE

.

#### Proof

Savitch's theorem shows that ${\mathsf {NL}}\subseteq {\mathsf {SPACE}}(\log ^{2}n)$ , while the space hierarchy theorem shows that ${\mathsf {SPACE}}(\log ^{2}n)\subsetneq {\mathsf {SPACE}}(n)$ . The result is this corollary along with the fact that TQBF ∉ NL since TQBF is PSPACE-complete.

This could also be proven using the non-deterministic space hierarchy theorem to show that NL ⊊ NPSPACE, and using Savitch's theorem to show that PSPACE = NPSPACE.

### Corollary 3

PSPACE

⊊

EXPSPACE

.

This last corollary shows the existence of decidable problems that are intractable. In other words, their decision procedures must use more than polynomial space.

### Corollary 4

There are problems in PSPACE requiring an arbitrarily large exponent to solve; therefore PSPACE does not collapse to DSPACE(*n**k*) for some constant *k*.

### Corollary 5

SPACE(

n

) ≠

PTIME

.

To see it, assume the contrary, thus any problem decided in space $O(n)$ is decided in time $O(n^{c})$ , and any problem L decided in space $O(n^{b})$ is decided in time $O((n^{b})^{c})=O(n^{bc})$ . Now ${\mathsf {P}}:=\bigcup _{k\in \mathbb {N} }{\mathsf {DTIME}}(n^{k})$ , thus P is closed under such a change of bound, that is $\bigcup _{k\in \mathbb {N} }{\mathsf {DTIME}}(n^{bk})\subseteq {\mathsf {P}}$ , so $L\in {\mathsf {P}}$ . This implies that for all $b,{\mathsf {SPACE}}(n^{b})\subseteq {\mathsf {P}}\subseteq {\mathsf {SPACE}}(n)$ , but the space hierarchy theorem implies that ${\mathsf {SPACE}}(n^{2})\not \subseteq {\mathsf {SPACE}}(n)$ , and Corollary 6 follows. Note that this argument neither proves that ${\mathsf {P}}\not \subseteq {\mathsf {SPACE}}(n)$ nor that ${\mathsf {SPACE}}(n)\not \subseteq {\mathsf {P}}$ , as to reach a contradiction we used the negation of both sentences, that is we used both inclusions, and can only deduce that at least one fails. It is currently unknown which fail(s) but conjectured that both do, that is that ${\mathsf {SPACE}}(n)$ and ${\mathsf {P}}$ are incomparable -at least for deterministic space. This question is related to that of the time complexity of (nondeterministic) linear bounded automata which accept the complexity class ${\mathsf {NSPACE}}(n)$ (a.k.a. as context-sensitive languages, CSL); so by the above CSL is not known to be decidable in polynomial time -see also Kuroda's two problems on LBA.
