---
title: "Circuit complexity"
source: https://en.wikipedia.org/wiki/Monotone_circuit
domain: boolean-circuit
license: CC-BY-SA-4.0
tags: boolean circuit, logic gate network, circuit satisfiability, monotone circuit
fetched: 2026-07-02
---

# Circuit complexity

(Redirected from

Monotone circuit

)

In theoretical computer science, **circuit complexity** is a branch of computational complexity theory in which Boolean functions are classified according to the size or depth of the Boolean circuits that compute them. A related notion is the circuit complexity of a recursive language that is decided by a **uniform** family of circuits $C_{1},C_{2},\ldots$ (see below).

Proving lower bounds on size of Boolean circuits computing explicit Boolean functions is a popular approach to separating complexity classes. For example, a prominent circuit class P/poly consists of Boolean functions computable by circuits of polynomial size. Proving that ${\mathsf {NP}}\not \subseteq {\mathsf {P/poly}}$ would separate P and NP (see below).

Complexity classes defined in terms of Boolean circuits include AC0, AC, TC0, NC1, NC, and P/poly.

## Size and depth

A Boolean circuit with n input bits is a directed acyclic graph in which every node (usually called *gates* in this context) is either an input node of in-degree 0 labelled by one of the n input bits, an AND gate, an OR gate, or a NOT gate. One of these gates is designated as the output gate. Such a circuit naturally computes a function of its n inputs. The **size** of a circuit is the number of gates it contains and its **depth** is the maximal length of a path from an input gate to the output gate.

There are two major notions of circuit complexity. The **circuit-size complexity** of a Boolean function f is the minimal size of any circuit computing f . The **circuit-depth complexity** of a Boolean function f is the minimal depth of any circuit computing f .

These notions generalize when one considers the circuit complexity of any formal language that contains strings with different bit lengths, especially infinite languages. Boolean circuits, however, only allow a fixed number of input bits. Thus, no single Boolean circuit is capable of deciding such a language. To account for this possibility, one considers families of circuits $C_{1},C_{2},\ldots$ where each $C_{n}$ accepts inputs of size n . Each circuit family will naturally generate the language by circuit $C_{n}$ outputting 1 when a length n string is a member of the family, and 0 otherwise. We say that a family of circuits is **size minimal** if there is no other family that decides on inputs of any size, n , with a circuit of smaller size than $C_{n}$ (respectively for **depth minimal** families). Thus, circuit complexity is meaningful even for non-recursive languages. The notion of a **uniform family** enables variants of circuit complexity to be related to algorithm-based complexity measures of recursive languages. However, the non-uniform variant is helpful to find lower bounds on how complex any circuit family must be in order to decide given languages.

Hence, the **circuit-size complexity** of a formal language A is defined as the function $t:\mathbb {N} \to \mathbb {N}$ , that relates a bit length of an input, n , to the circuit-size complexity of a minimal circuit $C_{n}$ that decides whether inputs of that length are in A . The **circuit-depth complexity** is defined similarly.

## Uniformity

Boolean circuits are one of the prime examples of so-called non-uniform models of computation in the sense that inputs of different lengths are processed by different circuits, in contrast with uniform models such as Turing machines where the same computational device is used for all possible input lengths. An individual computational problem is thus associated with a particular *family* of Boolean circuits $C_{1},C_{2},\dots$ where each $C_{n}$ is the circuit handling inputs of *n* bits. A *uniformity* condition is often imposed on these families, requiring the existence of some possibly resource-bounded Turing machine that, on input *n*, produces a description of the individual circuit $C_{n}$ . When this Turing machine has a running time polynomial in *n*, the circuit family is said to be P-uniform. The stricter requirement of DLOGTIME-uniformity is of particular interest in the study of shallow-depth circuit-classes such as AC0 or TC0. When no resource bounds are specified, a language is recursive (i.e., decidable by a Turing machine) if and only if the language is decided by a uniform family of Boolean circuits.

### Polynomial-time uniform

A family of Boolean circuits $\{C_{n}:n\in \mathbb {N} \}$ is *polynomial-time uniform* if there exists a deterministic Turing machine *M*, such that

- *M* runs in polynomial time
- For all $n\in \mathbb {N}$ , *M* outputs a description of $C_{n}$ on input $1^{n}$

### Logspace uniform

A family of Boolean circuits $\{C_{n}:n\in \mathbb {N} \}$ is *logspace uniform* if there exists a deterministic Turing machine *M*, such that

- *M* runs in logarithmic work space (i.e. *M* is a log-space transducer)
- For all $n\in \mathbb {N}$ , *M* outputs a description of $C_{n}$ on input $1^{n}$

## History

Circuit complexity goes back to Shannon in 1949, who proved that almost all Boolean functions on *n* variables require circuits of size Θ(2*n*/*n*). Despite this fact, complexity theorists have so far been unable to prove a superlinear lower bound for any explicit function.

Superpolynomial lower bounds have been proved under certain restrictions on the family of circuits used. The first function for which superpolynomial circuit lower bounds were shown was the parity function, which computes the sum of its input bits modulo 2. The fact that parity is not contained in AC0 was first established independently by Ajtai in 1983 and by Furst, Saxe and Sipser in 1984. Later improvements by Håstad in 1987 established that any family of constant-depth circuits computing the parity function requires exponential size. Extending a result of Razborov, Smolensky in 1987 proved that this is true even if the circuit is augmented with gates computing the sum of its input bits modulo some odd prime *p*.

The *k*-clique problem is to decide whether a given graph on *n* vertices has a clique of size *k*. For any particular choice of the constants *n* and *k*, the graph can be encoded in binary using ${n \choose 2}$ bits, which indicate for each possible edge whether it is present. Then the *k*-clique problem is formalized as a function $f_{k}:\{0,1\}^{n \choose 2}\to \{0,1\}$ such that $f_{k}$ outputs 1 if and only if the graph encoded by the string contains a clique of size *k*. This family of functions is monotone and can be computed by a family of circuits, but it has been shown that it cannot be computed by a polynomial-size family of monotone circuits (that is, circuits with AND and OR gates but without negation). The original result of Razborov in 1985 was later improved to an exponential-size lower bound by Alon and Boppana in 1987. In 2008, Rossman showed that constant-depth circuits with AND, OR, and NOT gates require size $\Omega (n^{k/4})$ to solve the *k*-clique problem even in the average case. Moreover, there is a circuit of size $n^{k/4+O(1)}$ that computes $f_{k}$ .

In 1999, Raz and McKenzie later showed that the monotone NC hierarchy is infinite.

The integer division problem lies in uniform TC0.

## Circuit lower bounds

Circuit lower bounds are generally difficult. Known results include

- Parity is not in nonuniform AC0, proved by Ajtai in 1983 as well as by Furst, Saxe and Sipser in 1984.
- Uniform TC0 is strictly contained in PP, proved by Allender.
- The classes OP 2, PP and MA/1 (MA with one bit of advice) are not in **SIZE**(*nk*) for any constant k.
- While it is suspected that the nonuniform class ACC0 does not contain the majority function, it was only in 2010 that Williams proved that ${\mathsf {NEXP}}\not \subseteq {\mathsf {ACC}}^{0}$ .

It is open whether NEXPTIME has nonuniform TC0 circuits.

Proofs of circuit lower bounds are strongly connected to derandomization. A proof that ${\mathsf {P}}={\mathsf {BPP}}$ would imply that either ${\mathsf {NEXP}}\not \subseteq {\mathsf {P/poly}}$ or that the permanent of a matrix cannot be computed by nonuniform arithmetic circuits (polynomials) of polynomial size and polynomial degree.

In 1997, Razborov and Rudich showed that many known circuit lower bounds for explicit Boolean functions imply the existence of so called natural properties useful against the respective circuit class. On the other hand, natural properties useful against P/poly would break strong pseudorandom generators. This is often interpreted as a "natural proofs" barrier for proving strong circuit lower bounds. In 2016, Carmosino, Impagliazzo, Kabanets and Kolokolova proved that natural properties can be also used to construct efficient learning algorithms.

## Complexity classes

Many circuit complexity classes are defined in terms of class hierarchies. For each non-negative integer *i*, there is a class NCi, consisting of polynomial-size circuits of depth $O(\log ^{i}(n))$ , using bounded fan-in AND, OR, and NOT gates. The union NC of all of these classes is a subject of study. By considering unbounded fan-in gates, the classes ACi and AC (which is equal to NC) can be constructed. Many other circuit complexity classes with the same size and depth restrictions can be constructed by allowing different sets of gates.

## Relation to time complexity

If a certain language, A , belongs to the time-complexity class ${\text{TIME}}(t(n))$ for some function $t:\mathbb {N} \to \mathbb {N}$ , then A has circuit complexity ${\mathcal {O}}(t(n)\log t(n))$ . If the Turing Machine that accepts the language is oblivious (meaning that it reads and writes the same memory cells regardless of input), then A has circuit complexity ${\mathcal {O}}(t(n))$ .

## Monotone circuits

A monotone Boolean circuit is one that has only AND and OR gates, but no NOT gates. A monotone circuit can only compute a monotone Boolean function, which is a function $f:\{0,1\}^{n}\to \{0,1\}$ where for every $x,y\in \{0,1\}^{n}$ , $x\leq y\implies f(x)\leq f(y)$ , where $x\leq y$ means that $x_{i}\leq y_{i}$ for all $i\in \{1,\ldots ,n\}$ .
