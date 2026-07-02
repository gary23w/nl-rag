---
title: "TC0 - Wikipedia"
source: https://en.wikipedia.org/wiki/TC0
domain: circuit-complexity
license: CC-BY-SA-4.0
tags: circuit complexity, circuit lower bound, ac0 class, natural proofs barrier
fetched: 2026-07-02
---

# TC0

In theoretical computer science, and specifically computational complexity theory and circuit complexity, **TC0** (Threshold Circuit) is the first class in the hierarchy of TC classes. TC0 contains all languages which are decided by Boolean circuits with constant depth and polynomial size, containing only unbounded fan-in AND gates, OR gates, NOT gates, and MAJ gates, or equivalently, threshold gates.

TC0 contains several important problems, such as sorting *n* *n*-bit numbers, multiplying two *n*-bit numbers, integer division or recognizing the Dyck language with multiple types of parentheses. It is commonly used to model the computational complexity of bounded-depth neural networks, and indeed, it was originally proposed for this purpose.

## Definitions

A **Boolean circuit family** is a sequence of Boolean circuits $C_{1},C_{2},C_{3},\dots$ consisting of a feedforward network of Boolean functions. A binary language $L\in 2^{*}$ is in the TC0 class if there exists a Boolean circuit family $C_{1},C_{2},C_{3},\dots$ , such that

- There exists a polynomial function p , and a constant d .
- Each $C_{n}$ is composed of up to $p(n)$ unbounded fan-in AND, OR, NOT, and MAJ gates in up to d layers.
- For each $x\in 2^{n}$ , we have $x\in L$ iff $C_{n}(x)=1$ .

Equivalently, instead of majority gates, we can use threshold gates with integer weights and thresholds, bounded by a polynomial. A threshold gate with k inputs is defined by a list of weights $w_{1},\dots ,w_{k}$ and a single threshold $\theta$ . Upon binary inputs $x_{1},\dots ,x_{k}$ , it outputs $+1$ if $\sum _{i}w_{i}x_{k}>\theta$ , else it outputs $-1$ . A threshold gate is also called an artificial neuron.

Given a Boolean circuit with AND, OR, NOT, and threshold gates whose weights and thresholds are bounded within $[-M,+M]$ , If we also provide the network with negations of binary inputs: $\neg x_{1},\dots ,\neg x_{k}$ , then we can convert the network to one that computes the same input-output function using only AND, OR, and threshold gates, with the same depth, at most double the number of gates in each layer, weights bounded within $[0,+M]$ , and thresholds bounded within $[-M,+M]$ . Therefore, TC0 can be defined equivalently as the languages decidable by some Boolean circuit family $C_{1},C_{2},C_{3},\dots$ such that

- There exists a polynomial function p , and a constant d .
- Each $C_{n}$ is composed of up to $p(n)$ threshold gates in up to d layers, whose weights are non-negative integers, thresholds are integers, and both weights and thresholds are bounded within $\pm p(n)$ .
- For each $x\in 2^{n}$ , we have $x\in L$ iff $C_{n}(x)=1$ .

In this article, we by default consider Boolean circuits with a polynomial number of AND, OR, NOT, and threshold gates, with polynomial bound on integer weights and thresholds. The polynomial bound on weights and thresholds can be relaxed without changing the class ${\mathsf {TC}}^{0}$ .

In arithmetic circuit complexity theory, ${\mathsf {TC}}^{0}$ can be equivalently characterized as the class of languages defined as the images of $\mathrm {sign} \circ f_{n}$ , where each $f_{n}:\{0,1\}^{n}\to \mathbb {Z}$ is computed by a polynomial-size constant-depth unbounded-fan-in arithmetic circuits with + and × gates, and constants from $\{-1,0,+1\}$ .

## Complexity class relations

Unsolved problem in computer science

${\mathsf {TC}}^{0}{\overset {?}{=}}{\mathsf {NC}}^{1}$

More unsolved problems in computer science

We can relate TC0 to other circuit classes, including AC0 and NC1 as follows:

> ${\mathsf {AC}}^{0}\subsetneq {\mathsf {AC}}^{0}[p]\subsetneq {\mathsf {TC}}^{0}\subseteq {\mathsf {NC}}^{1}.$

Whether ${\mathsf {TC}}^{0}\subseteq {\mathsf {NC}}^{1}$ is a strict inclusion is "one of the main open problems in circuit complexity". In fact, it is even open whether ${\mathsf {TC}}^{0}\subseteq {\mathsf {P/poly}}$ is a strict inclusion! This is in some sense unsurprising, since there is no natural proof for ${\mathsf {TC}}^{0}\subsetneq {\mathsf {P/poly}}$ , assuming that there is a cryptographically secure pseudorandom number generator in ${\mathsf {TC}}^{0}$ , which have been explicitly constructed under the assumption that factoring Blum integers is hard (i.e. requires circuits of size $2^{{\mathsf {poly}}(n)}$ ), which is widely suspected to be true. More generally, randomness and hardness for have been shown to be closely related. It is also an open question whether ${\mathsf {NEXP}}\subseteq {\mathsf {TC}}^{0}$ . Indeed, ${\mathsf {NEXP}}\not \subseteq {\mathsf {ACC}}^{0}$ was only proven in 2011.

Note that because non-uniform ${\mathsf {TC}}^{0}$ and ${\mathsf {ACC}}^{0}$ can compute functions that are not Turing-computable, it is certainly the case that ${\mathsf {TC}}^{0}\not \subseteq {\mathsf {NEXP}}$ and ${\mathsf {ACC}}^{0}\not \subseteq {\mathsf {NEXP}}$ . The 2011 result simply shows that ${\mathsf {ACC}}^{0}$ and ${\mathsf {NEXP}}$ are incomparable classes. The open question is whether ${\mathsf {TC}}^{0}$ and ${\mathsf {NEXP}}$ are incomparable as well.

Note that, while the nondeterministic time hierarchy theorem proves that ${\mathsf {NP}}\subsetneq {\mathsf {NEXP}}$ , both complexity classes are *uniform*, meaning that a single Turing machine is responsible for solving the problem at any input length. In contrast, a ${\mathsf {TC}}^{0}$ circuit family may be non-uniform, meaning that there may be no good algorithm for finding the correct circuit, other than exhaustive search over all $2^{{\mathsf {poly}}(n)}$ possible Boolean circuits of bounded depth and ${\mathsf {poly}}(n)$ size, then checking all $2^{n}$ possible inputs to verify that the circuit is correct.

It has been proven that if ${\mathsf {TC}}^{0}={\mathsf {NC}}^{1}$ , then any $\epsilon >0$ , there exists a ${\mathsf {TC}}^{0}$ circuit family of gate number $O(n^{1+\epsilon })$ that solves the Boolean Formula Evaluation problem. Thus, any superlinear bound suffices to prove ${\mathsf {TC}}^{0}\neq {\mathsf {NC}}^{1}$ .

## Uniform TC0

DLOGTIME-uniform ${\mathsf {TC}}^{0}$ is also known as ${\mathsf {FOM}}$ , because it is equivalent to first-order logic with Majority quantifiers. Specifically, given a logic formula that takes $x_{1},x_{2},\dots ,x_{n}$ Boolean variables, a Majority quantifier M is used as follows: given a formula with exactly one free variable $\phi (x)$ , the quantified $Mx\phi (x)$ is true iff $\phi (x_{i})$ is true for over half of $i\in 1:n$ , Integer division (given $x,y$ n -bit integers, find $\lfloor x/y\rfloor$ ), powering (given x an n -bit integer, and k a $O(\ln(n))$ -bit integer, find $x^{k}$ ), and iterated multiplication (multiplying n of n -bit integers) are all in DLOGTIME-uniform ${\mathsf {TC}}^{0}$ . It is usually considered the appropriate level of uniformity for ${\mathsf {TC}}^{0}$ , neither too strong nor too weak. Specifically, because P is usually suspected to be stronger than ${\mathsf {TC}}^{0}$ , while DLOGTIME is suspected to be equivalent in strength in some sense, DLOGTIME-uniformity is usually assumed, when uniformity is considered for ${\mathsf {TC}}^{0}$ .

The permanent of a 0-1 matrix is not in uniform ${\mathsf {TC}}^{0}$ .

Uniform ${\mathsf {TC}}^{0}\subsetneq {\mathsf {PP}}$ .

The functional version of the uniform TC0 coincides with the closure with respect to composition of the projections and one of the following function sets $\{n+m,n\,{\stackrel {.}{-}}\,m,n\wedge m,\lfloor n/m\rfloor ,2^{\lfloor \log _{2}n\rfloor ^{2}}\}$ , $\{n+m,n\,{\stackrel {.}{-}}\,m,n\wedge m,\lfloor n/m\rfloor ,n^{\lfloor \log _{2}m\rfloor }\}$ . Here $n\,{\stackrel {.}{-}}\,m=\max(0,n-m)$ , $n\wedge m$ is a bitwise AND of n and m . By functional version one means the set of all functions $f(x_{1},\ldots ,x_{n})$ over non-negative integers that are bounded by functions of FP and $(y{\text{-th bit of }}f(x_{1},\ldots ,x_{n}))$ is in the uniform TC0.

## Fine structure

TC0 can be divided further, into a hierarchy of languages requiring up to 1 layer, 2 layers, etc. Let ${\mathsf {TC}}_{d}^{0}$ be the class of languages decidable by a threshold circuit family of up to depth d : ${\mathsf {TC}}_{1}^{0}\subset {\mathsf {TC}}_{2}^{0}\subset \cdots \subset {\mathsf {TC}}^{0}=\bigcup _{d=1}^{\infty }{\mathsf {TC}}_{d}^{0}$ The hierarchy can be even more finely divided.

### MAJ vs threshold

The MAJ gate is sometimes called an **unweighted** threshold gate. They are equivalent up to a uniform polynomial overhead. In detail:

- A MAJ gate is a threshold gate where all the weights are 1, and threshold is $1/2$ the fan-in.
- A polynomial-size circuit containing threshold gates with polynomial integer weights and threshold can be converted to a polynomial-size circuit with the same depth. Specifically, the weights can be simulated by replicating the input circuits, and the threshold can be simulated by replicating constant True/False inputs.

Furthermore, there is an explicit algorithm, by which, given a single n -input threshold gate with arbitrary (unbounded) integer weights and thresholds, it constructs a depth-2 circuit using ${\mathsf {poly}}(n)$ -many AND, OR, NOT, and MAJ gates. Thus, any polynomial-size, depth- d threshold circuit can be simulated uniformly by a polynomial-size majority circuit of depth $d+1$ .

As a separation theorem, it is known that the n -input Boolean inner product function (IP), defined below, is computable by a majority circuit with 3 layers and $O(n)$ gates, but is not computable by a threshold circuit with 2 layers and ${\mathsf {poly}}(n)$ gates.

### Arbitrary threshold gate

For any fixed n , because there are only finitely many Boolean functions that can be computed by a threshold logic unit, it is possible to set all $w_{1},\dots ,w_{n},\theta$ to be integers. Let $W(n)$ be the smallest number W such that every possible real threshold function of n variables can be realized using integer weights of absolute value $\leq W$ . It is known that ${\frac {1}{2}}n\log n-2n+o(n)\leq \log _{2}W(n)\leq {\frac {1}{2}}n\log n-n+o(n)$ See for a literature review.

Sometimes the class of polynomial-bounded weights and thresholds with depth d is denoted as ${\widehat {\mathsf {LT}}}_{d}:={\mathsf {TC}}_{d}^{0}$ , and ${\mathsf {LT}}_{d}$ denotes the class where the weight and thresholds are unbounded ("large weight threshold circuit"). This formalizes neural networks with real-valued activation functions.

As previously stated, any polynomial-size, depth- d threshold circuit can be simulated uniformly by a polynomial-size majority circuit of depth $d+1$ . Therefore, ${\mathsf {TC}}_{d}^{0}\subset {\mathsf {LT}}_{d}\subset {\mathsf {TC}}_{d+1}^{0}$ . It has been proven that ${\mathsf {TC}}_{2}^{0}\subsetneq {\mathsf {LT}}_{2}$ .

Allowing the sigmoid activation function $\sigma$ does not increase the power, that is, ${\mathsf {TC}}_{d}^{0}={\mathsf {TC}}_{d}^{0}(\sigma )$ for all $d\geq 1$ , assuming the weights are polynomially bounded.

### Probabilistic version

Like how the P class has a probabilistic version BPP, the ${\mathsf {TC}}^{0}$ has a probabilistic version ${\mathsf {RTC}}^{0}$ . It is defined as the class of languages that can be polynomial-probabilistically decided.

Let $C_{1},C_{2},C_{3},\dots$ be a Boolean circuit family that takes two kinds of inputs. A given circuit $C_{n}$ takes the deterministic inputs $x_{1},\dots ,x_{n}$ , and the random inputs $y_{1},\dots ,y_{m}$ , where $m={\mathsf {poly}}(n)$ . The random inputs are sampled uniformly over all $2^{m}$ possibilities.

A language $L\subset 2^{*}$ is decided polynomial-probabilistically by the family if for each $x\in 2^{n}$ , if $x\in L$ , then the probability that $C_{n}(x,y)=+1$ is at least ${\frac {1}{2}}+{\frac {1}{{\mathsf {poly}}(n)}}$ , and if $x\not \in L$ , then the probability that $C_{n}(x,y)=+1$ is at most ${\frac {1}{2}}-{\frac {1}{{\mathsf {poly}}(n)}}$ .

Similarly, (feedforward) Boltzmann machines have been modelled as ${\mathsf {RTC}}^{0}$ circuits with boundedly-unreliable threshold units. That is, each threshold unit may, independently at random, with a bounded probability $\epsilon <1/2$ , make the wrong output.

Sometimes, this class is also called ${\mathsf {BPTC}}^{0}$ , in a closer analogy with BPP. In this definition, the probability that $C_{n}(x,y)=+1$ is at least ${\frac {2}{3}}$ , and if $x\not \in L$ , then the probability that $C_{n}(x,y)=+1$ is at most ${\frac {1}{3}}$ . By the standard trick of sampling many times then taking the majority opinion, any d -layer ${\mathsf {RTC}}^{0}$ circuit can be converted to a $(d+1)$ -layer ${\mathsf {BPTC}}^{0}$ circuit.

### Hierarchy

Analogous to how ${\textstyle {\mathsf {TC}}_{1}^{0}\subset {\mathsf {TC}}_{2}^{0}\subset \cdots \subset {\mathsf {TC}}^{0}=\bigcup _{d=1}^{\infty }{\mathsf {TC}}_{d}^{0}}$ , ${\mathsf {RTC}}^{0}$ can also be divided into ${\mathsf {RTC}}_{1}^{0}\subset {\mathsf {RTC}}_{2}^{0}\subset \cdots \subset {\mathsf {RTC}}^{0}=\bigcup _{d=1}^{\infty }{\mathsf {RTC}}_{d}^{0}$ By definition, ${\mathsf {TC}}_{d}^{0}\subset {\mathsf {RTC}}_{d}^{0}$ . Furthermore, since ${\mathsf {RTC}}_{d}^{0}\subset {\mathsf {TC}}_{d+1}^{0}$ , there is a full hierarchy: ${\mathsf {TC}}_{1}^{0}\subset {\mathsf {RTC}}_{1}^{0}\subset {\mathsf {TC}}_{2}^{0}\subset {\mathsf {RC}}_{2}^{0}\subset \cdots \subset {\mathsf {TC}}^{0}={\mathsf {RTC}}^{0}$ Similarly, allowing boundedly-unreliable threshold units, a ${\mathsf {RTC}}_{d}^{0}$ circuit can be converted to a ${\mathsf {TC}}_{d+1}^{0}$ circuit by running several copies of the original circuit in parallel, each with a fixed choice for the random inputs (a hardcoded advice), and then taking a Majority over their outputs. That at least one advice exists is proven by Hoeffding's inequality, with essentially the same argument as the median trick. This argument is merely an existence proof, and thus not uniform in a way that matters for ${\mathsf {TC}}^{0}$ , since it gives no algorithm for discovering the advice other than brute-force enumeration.

Similarly, ${\mathsf {RTC}}^{0}/{\mathsf {poly}}={\mathsf {TC}}^{0}/{\mathsf {poly}}$ .

Let $\oplus$ be defined as the parity function, or the XOR function. Then the following two separations are theorems:

- ${\mathsf {RTC}}_{1}^{0}\subsetneq {\mathsf {TC}}_{2}^{0}$ : The PARITY function $\oplus$ is in ${\mathsf {TC}}_{2}^{0}$ , but not in ${\mathsf {RTC}}_{1}^{0}$ .
- ${\mathsf {TC}}_{2}^{0}\subsetneq {\mathsf {RTC}}_{2}^{0}$ : The Boolean inner product function (IP) is in ${\mathsf {RTC}}_{2}^{0}$ but not in ${\mathsf {TC}}_{2}^{0}$ , where $\mathrm {IP} _{n}\left(x_{1},\ldots ,x_{n},x_{1}^{\prime },\ldots ,x_{n}^{\prime }\right)=\bigoplus _{i=1}^{n}\mathrm {AND} \left(x_{i},x_{i}^{\prime }\right)$

The inner product function falls outside ${\mathsf {TC}}_{2}^{0}$ in a precise sense:

- If the weights of the bottom gates of a threshold circuit of depth 2 computing $\mathrm {IP} _{n}$ are polynomial, then for any $\epsilon >0$ , for all large enough n , $\mathrm {IP} _{n}$ requires $\geq 2^{(1/2-\epsilon )n}$ gates.
- If the weights of the top gate in a threshold circuit of depth 2 computing $\mathrm {IP} _{n}$ are at most $2^{o\left(n^{1/3}\right)}$ , then the top gate must have fanin at least $2^{\Omega \left(n^{1/3}\right)}$ .
- If the weights of the bottom gates of a threshold circuit of depth 2 computing $\mathrm {IP} _{n}$ do not exceed $2^{n/3}$ , then the top gate must have fanin at least $2^{\Omega (n)}$ .

It is an open question how many levels the hierarchy has. It is also an open question whether the hierarchy collapses, that is, ${\mathsf {TC}}^{0}={\mathsf {TC}}_{3}^{0}$ . In fact, there is still no exponential lower bound for ${\mathsf {LT}}_{2}^{0}$ . Therefore, *a fortiori*, there is still no exponential lower bound for depth-3 polynomial-size majority circuits. There are exponential lower bounds if further restrictions are imposed on layer 1, such as requiring it to only contain AND gates, or only bounded fan-in gates.

The hierarchy for *monotone* ${\mathsf {TC}}^{0}$ (that is, ${\mathsf {TC}}^{0}$ without Boolean negations) is strongly separated. Specifically, for each d , there has been constructed a language that is decidable by a depth d circuit family using only $O(n)$ AND and OR gates, but requires exponential size to compute by a monotone ${\mathsf {TC}}_{d-1}^{0}$ .

If the polynomial bound on the number of gates is relaxed, then ${\mathsf {TC}}_{3}^{0}$ is quite powerful. Specifically, any language in ${\mathsf {ACC}}^{0}$ can be decided by a circuit family in ${\mathsf {TC}}_{3}^{0}$ (using Majority gates), except that it uses a quasi-polynomial number of gates (instead of polynomial). This result is optimal, in that there exists a function that is computable with 3 layers of ${\mathsf {AC}}^{0}$ , but requires at least an exponential number of gates for ${\mathsf {TC}}_{2}^{0}$ (using Majority gates).
