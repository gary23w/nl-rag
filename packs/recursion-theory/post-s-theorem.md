---
title: "Post's theorem"
source: https://en.wikipedia.org/wiki/Post's_theorem
domain: recursion-theory
license: CC-BY-SA-4.0
tags: computability theory, turing degree, halting problem, arithmetical hierarchy
fetched: 2026-07-02
---

# Post's theorem

In computability theory, **Post's theorem**, named after Emil Post, describes the connection between the arithmetical hierarchy and the Turing degrees.

## Background

The statement of Post's theorem uses several concepts relating to definability and computability theory. This section gives a brief overview of these concepts, which are covered in depth in their respective articles.

The arithmetical hierarchy classifies certain sets of natural numbers that are definable in the language of first-order Peano arithmetic. A formula is said to be $\Sigma _{m}^{0}$ if it is an existential statement in prenex normal form (all quantifiers at the front) with m alternations between existential and universal quantifiers applied to a formula with bounded quantifiers only. Formally a formula $\phi (s)$ in the language of Peano arithmetic is a $\Sigma _{m}^{0}$ formula if it is of the form

$\left(\exists n_{1}^{1}\exists n_{2}^{1}\cdots \exists n_{j_{1}}^{1}\right)\left(\forall n_{1}^{2}\cdots \forall n_{j_{2}}^{2}\right)\left(\exists n_{1}^{3}\cdots \right)\cdots \left(Qn_{1}^{m}\cdots \right)\rho (n_{1}^{1},\ldots n_{j_{m}}^{m},x_{1},\ldots ,x_{k})$

where $\rho$ contains only bounded quantifiers and *Q* is $\forall$ if *m* is even and $\exists$ if *m* is odd.

A set of natural numbers A is said to be $\Sigma _{m}^{0}$ if it is definable by a $\Sigma _{m}^{0}$ formula, that is, if there is a $\Sigma _{m}^{0}$ formula $\phi (s)$ such that each number n is in A if and only if $\phi (n)$ holds. It is known that if a set is $\Sigma _{m}^{0}$ then it is $\Sigma _{n}^{0}$ for any $n>m$ , but for each *m* there is a $\Sigma _{m+1}^{0}$ set that is not $\Sigma _{m}^{0}$ . Thus the number of quantifier alternations required to define a set gives a measure of the complexity of the set.

Post's theorem uses the relativized arithmetical hierarchy as well as the unrelativized hierarchy just defined. A set A of natural numbers is said to be $\Sigma _{m}^{0}$ relative to a set B , written $\Sigma _{m}^{0,B}$ , if A is definable by a $\Sigma _{m}^{0}$ formula in an extended language that includes a predicate for membership in B .

While the arithmetical hierarchy measures definability of sets of natural numbers, Turing degrees measure the level of uncomputability of sets of natural numbers. A set A is said to be Turing reducible to a set B , written $A\leq _{T}B$ , if there is an oracle Turing machine that, given an oracle for B , computes the characteristic function of A . The Turing jump of a set A is a form of the halting problem relative to A . Given a set A , the Turing jump $A'$ is the set of indices of oracle Turing machines that halt on input 0 when run with oracle A . It is known that every set A is Turing reducible to its Turing jump, but the Turing jump of a set is never Turing reducible to the original set.

Post's theorem uses finitely iterated Turing jumps. For any set A of natural numbers, the notation $A^{(n)}$ indicates the n -fold iterated Turing jump of A . Thus $A^{(0)}$ is just A , and $A^{(n+1)}$ is the Turing jump of $A^{(n)}$ .

## Post's theorem and corollaries

Post's theorem establishes a close connection between the arithmetical hierarchy and the Turing degrees of the form $\emptyset ^{(n)}$ , that is, finitely iterated Turing jumps of the empty set. (The empty set could be replaced with any other computable set without changing the truth of the theorem.)

Post's theorem states:

1. A set B is $\Sigma _{n+1}^{0}$ if and only if B is computably enumerable by an oracle Turing machine with an oracle for $\emptyset ^{(n)}$ , that is, if and only if B is $\Sigma _{1}^{0,\emptyset ^{(n)}}$ .
2. The set $\emptyset ^{(n)}$ is $\Sigma _{n}^{0}$ -complete for every $n>0$ . This means that every $\Sigma _{n}^{0}$ set is many-one reducible to $\emptyset ^{(n)}$ .

Post's theorem has many corollaries that expose additional relationships between the arithmetical hierarchy and the Turing degrees. These include:

1. Fix a set C . A set B is $\Sigma _{n+1}^{0,C}$ if and only if B is $\Sigma _{1}^{0,C^{(n)}}$ . This is the relativization of the first part of Post's theorem to the oracle C .
2. A set B is $\Delta _{n+1}^{0}$ if and only if $B\leq _{T}\emptyset ^{(n)}$ . More generally, B is $\Delta _{n+1}^{0,C}$ if and only if $B\leq _{T}C^{(n)}$ .
3. A set is defined to be arithmetical if it is $\Sigma _{n}^{0}$ for some n . Post's theorem shows that, equivalently, a set is arithmetical if and only if it is Turing reducible to $\emptyset ^{(m)}$ for some *m*.

## Proof of Post's theorem

### Formalization of Turing machines in first-order arithmetic

The operation of a Turing machine T on input n can be formalized logically in first-order arithmetic. For example, we may use symbols $A_{k}$ , $B_{k}$ , and $C_{k}$ for the tape configuration, machine state and location along the tape after k steps, respectively. T 's transition system determines the relation between $(A_{k},B_{k},C_{k})$ and $(A_{k+1},B_{k+1},C_{k+1})$ ; their initial values (for $k=0$ ) are the input, the initial state and zero, respectively. The machine halts if and only if there is a number k such that $B_{k}$ is the halting state.

The exact relation depends on the specific implementation of the notion of Turing machine (e.g. their alphabet, allowed mode of motion along the tape, etc.)

In case T halts at time $n_{1}$ , the relation between $(A_{k},B_{k},C_{k})$ and $(A_{k+1},B_{k+1},C_{k+1})$ must be satisfied only for *k* bounded from above by $n_{1}$ .

Thus there is a formula $\varphi (n,n_{1})$ in first-order arithmetic with no unbounded quantifiers, such that T halts on input n at time at most $n_{1}$ if and only if $\varphi (n,n_{1})$ is satisfied.

### Implementation example

For example, for a prefix-free Turing machine with binary alphabet and no blank symbol, we may use the following notations:

- $A_{k}$ is the 1-ary symbol for the configuration of the whole tape after k steps (which we may write as a number with LSB first, the value of the *m*th location on the tape being its *m*th least significant bit). In particular $A_{0}$ is the initial configuration of the tape, which corresponds the input to the machine.
- $B_{k}$ is the 1-ary symbol for the Turing machine state after k steps. In particular, $B_{0}=q_{I}$ , the initial state of the Turing machine.
- $C_{k}$ is the 1-ary symbol for the Turing machine location on the tape after k steps. In particular $C_{0}=0$ .
- $M(q,b)$ is the transition function of the Turing machine, written as a function from a pair (machine state, bit read by the machine) to a triple (new machine state, bit written by the machine, +1 or -1 machine movement along the tape).
- $bit(j,m)$ is the *j*th bit of a number m . This can be written as a first-order arithmetic formula with no unbounded quantifiers.

For a prefix-free Turing machine we may use, for input *n*, the initial tape configuration $t(n)=cat(2^{ceil(log_{2}n)}-1,0,n)$ where cat stands for concatenation; thus $t(n)$ is a $\log(n)$ -length string of $1-s$ followed by 0 and then by n .

The operation of the Turing machine at the first $n_{1}$ steps can thus be written as the conjunction of the initial conditions and the following formulas, quantified over k for all $k<n_{1}$ :

- $(B_{k+1},bit(C_{k},A_{k+1}),D)=M(B_{k},bit(C_{k},A_{k}))$ . Since *M* has a finite domain, this can be replaced by a first-order quantifier-free arithmetic formula. The exact formula obviously depends on M.
- $C_{k+1}=C_{k}+D$
- $\forall j:j\neq C_{k}\rightarrow bit(j,A_{k+1})=bit(j,A_{k})$ . Note that at the first $n_{1}$ steps, T never arrives at a location along the tape greater than $n_{1}$ . Thus the universal quantifier over *j* can be bounded by $n_{1}$ +1, as bits beyond this location have no relevance for the machine's operation.

*T* halts on input n at time at most $n_{1}$ if and only if $\varphi (n,n_{1})$ is satisfied, where:

${\begin{aligned}\varphi (n,n_{1})=&(A_{0}=t(n))\land (B_{0}=q_{I})\land (C_{0}=0)\land (B_{n_{1}}=q_{H})\\&\land \forall k<n_{1}:((B_{k+1},bit(C_{k},A_{k+1}),1)=M(B_{k},bit(C_{k},A_{k}))\land C_{k+1}=C_{k}+1)&\\&\lor ((B_{k+1},bit(C_{k},A_{k+1}),-1)=M(B_{k},bit(C_{k},A_{k}))\land C_{k+1}=C_{k}-1))&\\&\land \forall j<n_{1}+1:j\neq C_{k}\rightarrow (bit(j,A_{k+1})=bit(j,A_{k}))&\end{aligned}}$

This is a first-order arithmetic formula with no unbounded quantifiers, i.e. it is in $\Sigma _{0}^{0}$ .

### Computably enumerable sets

Let S be a set that can be computably enumerated by a Turing machine. Then there is a Turing machine T such that for every n , T halts when given n as an input if and only if n is in S .

This can be formalized by the first-order arithmetical formula presented above. The members of S are the numbers n satisfying the following formula:

$\exists n_{1}:\varphi (n,n_{1})$

This formula is in $\Sigma _{1}^{0}$ . Therefore, S is in $\Sigma _{1}^{0}$ . Thus every computably enumerable set is in $\Sigma _{1}^{0}$ .

The converse is true as well: for every formula $\varphi (n)$ in $\Sigma _{1}^{0}$ with *k* existential quantifiers, we may enumerate the k -tuples of natural numbers and run a Turing machine that goes through all of them until it finds the formula is satisfied. This Turing machine halts on precisely the set of natural numbers satisfying $\varphi (n)$ , and thus enumerates its corresponding set.

### Oracle machines

Similarly, the operation of an oracle machine T with an oracle *O* that halts after at most $n_{1}$ steps on input n can be described by a first-order formula $\varphi _{O}(n,n_{1})$ , except that the formula $\varphi _{1}(n,n_{1})$ now includes:

- A new predicate, $O_{m}$ , giving the oracle answer. This predicate must satisfy some formula to be discussed below.
- An additional tape - the oracle tape - on which T has to write the number *m* for every call *O*(*m*) to the oracle; writing on this tape can be logically formalized in a similar manner to writing on the machine's tape. Note that an oracle machine that halts after at most $n_{1}$ steps has time to write at most $n_{1}$ digits on the oracle tape. So the oracle can only be called with numbers *m* satisfying $m<2^{n_{1}}$ .

If the oracle is for a decision problem, $O_{m}$ is always "Yes" or "No", which we may formalize as 0 or 1. Suppose the decision problem itself can be formalized by a first-order arithmetic formula $\psi ^{O}(m)$ . Then T halts on n after at most $n_{1}$ steps if and only if the following formula is satisfied: $\varphi _{O}(n,n_{1})=\forall m<2^{n_{1}}:((\psi ^{O}(m)\rightarrow (O_{m}=1))\land (\lnot \psi ^{O}(m)\rightarrow (O_{m}=0)))\land {\varphi _{O}}_{1}(n,n_{1})$

where ${\varphi _{O}}_{1}(n,n_{1})$ is a first-order formula with no unbounded quantifiers.

### Turing jump

If *O* is an oracle to the halting problem of a machine $T'$ , then $\psi ^{O}(m)$ is the same as "there exists $m_{1}$ such that $T'$ starting with input *m* is at the halting state after $m_{1}$ steps". Thus: $\psi ^{O}(m)=\exists m_{1}:\psi _{H}(m,m_{1})$ where $\psi _{H}(m,m_{1})$ is a first-order formula that formalizes $T'$ . If $T'$ is a Turing machine (with no oracle), $\psi _{H}(m,m_{1})$ is in $\Sigma _{0}^{0}=\Pi _{0}^{0}$ (i.e. it has no unbounded quantifiers).

Since there is a finite number of numbers *m* satisfying $m<2^{n_{1}}$ , we may choose the same number of steps for all of them: there is a number $m_{1}$ , such that $T'$ halts after $m_{1}$ steps precisely on those inputs $m<2^{n_{1}}$ for which it halts at all.

Moving to prenex normal form, we get that the oracle machine halts on input n if and only if the following formula is satisfied: $\varphi (n)=\exists n_{1}\exists m_{1}\forall m_{2}:(\psi _{H}(m,m_{2})\rightarrow (O_{m}=1))\land (\lnot \psi _{H}(m,m_{1})\rightarrow (O_{m}=0)))\land {\varphi _{O}}_{1}(n,n_{1})$

(informally, there is a "maximal number of steps" $m_{1}$ such every oracle that does not halt within the first $m_{1}$ steps does not stop at all; however, for every $m_{2}$ , each oracle that halts after $m_{2}$ steps does halt).

Note that we may replace both $n_{1}$ and $m_{1}$ by a single number - their maximum - without changing the truth value of $\varphi (n)$ . Thus we may write: $\varphi (n)=\exists n_{1}\forall m_{2}:(\psi _{H}(m,m_{2})\rightarrow (O_{m}=1))\land (\lnot \psi _{H}(m,n_{1})\rightarrow (O_{m}=0)))\land {\varphi _{O}}_{1}(n,n_{1})$

For the oracle to the halting problem over Turing machines, $\psi _{H}(m,m_{1})$ is in $\Pi _{0}^{0}$ and $\varphi (n)$ is in $\Sigma _{2}^{0}$ . Thus every set that is computably enumerable by an oracle machine with an oracle for $\emptyset ^{(1)}$ , is in $\Sigma _{2}^{0}$ .

The converse is true as well: Suppose $\varphi (n)$ is a formula in $\Sigma _{2}^{0}$ with $k_{1}$ existential quantifiers followed by $k_{2}$ universal quantifiers. Equivalently, $\varphi (n)$ has $k_{1}$ > existential quantifiers followed by a negation of a formula in $\Sigma _{1}^{0}$ ; the latter formula can be enumerated by a Turing machine and can thus be checked immediately by an oracle for $\emptyset ^{(1)}$ .

We may thus enumerate the $k_{1}$ -tuples of natural numbers and run an oracle machine with an oracle for $\emptyset ^{(1)}$ that goes through all of them until it finds a satisfaction for the formula. This oracle machine halts on precisely the set of natural numbers satisfying $\varphi (n)$ , and thus enumerates its corresponding set.

### Higher Turing jumps

More generally, suppose every set that is computably enumerable by an oracle machine with an oracle for $\emptyset ^{(p)}$ is in $\Sigma _{p+1}^{0}$ . Then for an oracle machine with an oracle for $\emptyset ^{(p+1)}$ , $\psi ^{O}(m)=\exists m_{1}:\psi _{H}(m,m_{1})$ is in $\Sigma _{p+1}^{0}$ .

Since $\psi ^{O}(m)$ is the same as $\varphi (n)$ for the previous Turing jump, it can be constructed (as we have just done with $\varphi (n)$ above) so that $\psi _{H}(m,m_{1})$ in $\Pi _{p}^{0}$ . After moving to prenex formal form the new $\varphi (n)$ is in $\Sigma _{p+2}^{0}$ .

By induction, every set that is computably enumerable by an oracle machine with an oracle for $\emptyset ^{(p)}$ , is in $\Sigma _{p+1}^{0}$ .

**The other direction** can be proven by induction as well: Suppose every formula in $\Sigma _{p+1}^{0}$ can be enumerated by an oracle machine with an oracle for $\emptyset ^{(p)}$ .

Now Suppose $\varphi (n)$ is a formula in $\Sigma _{p+2}^{0}$ with $k_{1}$ existential quantifiers followed by $k_{2}$ universal quantifiers etc. Equivalently, $\varphi (n)$ has $k_{1}$ > existential quantifiers followed by a negation of a formula in $\Sigma _{p+1}^{0}$ ; the latter formula can be enumerated by an oracle machine with an oracle for $\emptyset ^{(p)}$ and can thus be checked immediately by an oracle for $\emptyset ^{(p+1)}$ .

We may thus enumerate the $k_{1}$ -tuples of natural numbers and run an oracle machine with an oracle for $\emptyset ^{(p+1)}$ that goes through all of them until it finds a satisfaction for the formula. This oracle machine halts on precisely the set of natural numbers satisfying $\varphi (n)$ , and thus enumerates its corresponding set.
