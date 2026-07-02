---
title: "Quantum complexity theory"
source: https://en.wikipedia.org/wiki/Quantum_complexity_theory
domain: quantum-complexity-theory
license: CC-BY-SA-4.0
tags: quantum complexity theory, quantum query complexity, quantum supremacy, qma class
fetched: 2026-07-02
---

# Quantum complexity theory

**Quantum complexity theory** is the subfield of computational complexity theory that deals with complexity classes defined using quantum computers, a computational model based on quantum mechanics. It studies the hardness of computational problems in relation to these complexity classes, as well as the relationship between quantum complexity classes and classical (i.e., non-quantum) complexity classes.

Two important quantum complexity classes are BQP and QMA.

## Background

A complexity class is a collection of computational problems that can be solved by a computational model under certain resource constraints. For instance, the complexity class P is defined as the set of problems solvable by a (deterministic) Turing machine in polynomial time. Similarly, quantum complexity classes may be defined using quantum models of computation, such as the quantum circuit model or the equivalent quantum Turing machine. One of the main aims of quantum complexity theory is to find out how these classes relate to classical complexity classes such as P, NP, BPP, and PSPACE.

One of the reasons quantum complexity theory is studied are the implications of quantum computing for the modern Church–Turing thesis. In short the modern Church–Turing thesis states that any computational model can be simulated in polynomial time with a probabilistic Turing machine. However, questions around the Church–Turing thesis arise in the context of quantum computing. It is unclear whether the Church–Turing thesis holds for the quantum computation model. There is much evidence that the thesis does not hold. It may not be possible for a probabilistic Turing machine to simulate quantum computation models in polynomial time.

Asymptotic computational complexities of both quantum algorithms and classical algorithms are often expressed with asymptotic notation. Some common forms of asymptotic notation of functions are $O(T(n))$ , $\Omega (T(n))$ , and $\Theta (T(n))$ . $O(T(n))$ expresses that something is bounded above by $cT(n)$ where c is a constant such that $c>0$ and $T(n)$ is a function of n , $\Omega (T(n))$ expresses that something is bounded below by $cT(n)$ where c is a constant such that $c>0$ and $T(n)$ is a function of n , and $\Theta (T(n))$ expresses both $O(T(n))$ and $\Omega (T(n))$ . These notations also have their own names. $O(T(n))$ is called big O notation, $\Omega (T(n))$ is called big Omega notation, and $\Theta (T(n))$ is called big Theta notation.

## Overview of complexity classes

The important complexity classes P, BPP, BQP, PP, and PSPACE can be compared based on promise problems. A promise problem is a decision problem that has an input assumed to be selected from the set of all possible input strings. A promise problem is a pair $A=(A_{\text{yes}},A_{\text{no}})$ , where $A_{\text{yes}}$ is the set of yes instances and $A_{\text{no}}$ is the set of no instances, and the intersection of these sets is empty: $A_{\text{yes}}\cap A_{\text{no}}=\varnothing$ . All of the previous complexity classes contain promise problems.

| Complexity Class | Criteria |
|---|---|
| P | Promise problems for which a polynomial-time deterministic Turing machine accepts all strings in $A_{\text{yes}}$ and rejects all strings in $A_{\text{no}}$ |
| BPP | Promise problems for which a polynomial-time probabilistic Turing machine accepts every string in $A_{\text{yes}}$ with a probability of at least ${\frac {2}{3}}$ , and accepts every string in $A_{\text{no}}$ with a probability of at most ${\frac {1}{3}}$ |
| BQP | Promise problems such that for functions $a,b:\mathbb {N} \to [0,1]$ , there exists a polynomial-time generated family of quantum circuits $Q={\{Q_{n}:n\in \mathbb {N} \}}$ , where $Q_{n}$ is a circuit that accepts n qubits and gives an output of one qubit. An element x of $A_{\text{yes}}$ is accepted by Q with a probability greater than or equal to $a(\left\vert x\right\vert )$ . An element x of $A_{\text{no}}$ is accepted by Q with a probability less than or equal to $b(\left\vert x\right\vert )$ . |
| PP | Promise problems for which a polynomial-time probabilistic Turing machine accepts every string in $A_{\text{yes}}$ with a probability greater than ${\frac {1}{2}}$ , and accepts every string in $A_{\text{no}}$ with a probability of at most ${\frac {1}{2}}$ |
| PSPACE | Promise problems for which a deterministic Turing machine that runs in polynomial space, accepts every string in $A_{\text{yes}}$ and rejects all strings in $A_{\text{no}}$ |

## BQP

| AnswerproducedCorrect answer | Yes | No |
|---|---|---|
| Yes | ≥ 2/3 | ≤ 1/3 |
| No | ≤ 1/3 | ≥ 2/3 |

The class of problems that can be efficiently solved by a quantum computer with bounded error is called BQP ("bounded error, quantum, polynomial time"). More formally, BQP is the class of problems that can be solved by a polynomial-time quantum Turing machine with error probability of at most 1/3.

As a class of probabilistic problems, BQP is the quantum counterpart to BPP ("bounded error, probabilistic, polynomial time"), the class of problems that can be efficiently solved by probabilistic Turing machines with bounded error. It is known that ${\mathsf {BPP\subseteq BQP}}$ and widely suspected, but not proven, that ${\mathsf {BQP\nsubseteq BPP}}$ , which intuitively would mean that quantum computers are more powerful than classical computers in terms of time complexity. BQP is a subset of PP.

The exact relationship of BQP to P, NP, and PSPACE is not known. However, it is known that ${\mathsf {P\subseteq BQP\subseteq PSPACE}}$ ; that is, the class of problems that can be efficiently solved by quantum computers includes all problems that can be efficiently solved by deterministic classical computers but does not include any problems that cannot be solved by classical computers with polynomial space resources. It is further suspected that BQP is a strict superset of P, meaning there are problems that are efficiently solvable by quantum computers that are not efficiently solvable by deterministic classical computers. For instance, integer factorization and the discrete logarithm problem are known to be in BQP and are suspected to be outside of P. On the relationship of BQP to NP, little is known beyond the fact that some NP problems are in BQP (integer factorization and the discrete logarithm problem are both in NP, for example). It is suspected that ${\mathsf {NP\nsubseteq BQP}}$ ; that is, it is believed that there are efficiently checkable problems that are not efficiently solvable by a quantum computer. As a direct consequence of this belief, it is also suspected that BQP is disjoint from the class of NP-complete problems (if any NP-complete problem were in BQP, then it follows from NP-hardness that all problems in NP are in BQP).

The relationship of BQP to the essential classical complexity classes can be summarized as:

${\mathsf {P\subseteq BPP\subseteq BQP\subseteq PP\subseteq PSPACE}}$

It is also known that BQP is contained in the complexity class ⁠ $\color {Blue}{\mathsf {\#P}}$ ⁠ (or more precisely in the associated class of decision problems ⁠ ${\mathsf {P^{\#P}}}$ ⁠), which is a subset of PSPACE.

## Simulation of quantum circuits

There is no known way to efficiently simulate a quantum computational model with a classical computer. This means that a classical computer cannot simulate a quantum computational model in polynomial time. However, a quantum circuit of $S(n)$ qubits with $T(n)$ quantum gates can be simulated by a classical circuit with $O(2^{S(n)}T(n)^{3})$ classical gates. This number of classical gates is obtained by determining how many bit operations are necessary to simulate the quantum circuit. In order to do this, first the amplitudes associated with the $S(n)$ qubits must be accounted for. Each of the states of the $S(n)$ qubits can be described by a two-dimensional complex vector, or a state vector. These state vectors can also be described a linear combination of its component vectors with coefficients called amplitudes. These amplitudes are complex numbers that are normalized to one, meaning the sum of the squares of the absolute values of the amplitudes must be one. The entries of the state vector are these amplitudes. The amplitudes, acting as coefficients in the linear combination description, each correspond to a non-zero component of the state vector. As an equation this is described as $\alpha {\begin{bmatrix}1\\0\end{bmatrix}}+\beta {\begin{bmatrix}0\\1\end{bmatrix}}={\begin{bmatrix}\alpha \\\beta \end{bmatrix}}$ or $\alpha \left\vert 1\right\rangle +\beta \left\vert 0\right\rangle ={\begin{bmatrix}\alpha \\\beta \end{bmatrix}}$ using Dirac notation. The state of the entire $S(n)$ qubit system can be described by a single state vector. This state vector describing the entire system is the tensor product of the state vectors describing the individual qubits in the system. The result of the tensor products of the $S(n)$ qubits is a single state vector that has $2^{S(n)}$ dimensions and entries that are the amplitudes associated with each basis state or component vector. Therefore, $2^{S(n)}$ amplitudes must be accounted for with a $2^{S(n)}$ dimensional complex vector, which is the state vector for the $S(n)$ qubit system. In order to obtain an upper bound for the number of gates required to simulate a quantum circuit we need a sufficient upper bound for the amount data used to specify the information about each of the $2^{S(n)}$ amplitudes. To do this $O(T(n))$ bits of precision are sufficient for encoding each amplitude. So it takes $O(2^{S(n)}T(n))$ classical bits to account for the state vector of the $S(n)$ qubit system. Next the application of the $T(n)$ quantum gates on $2^{S(n)}$ amplitudes must be accounted for. The quantum gates can be represented as $2^{S(n)}\times 2^{S(n)}$ sparse matrices. So to account for the application of each of the $T(n)$ quantum gates, the state vector must be multiplied by a $2^{S(n)}\times 2^{S(n)}$ sparse matrix for each of the $T(n)$ quantum gates. Every time the state vector is multiplied by a $2^{S(n)}\times 2^{S(n)}$ sparse matrix, $O(2^{S(n)})$ arithmetic operations must be performed. Therefore, there are $O(2^{S(n)}T(n)^{2})$ bit operations for every quantum gate applied to the state vector. So $O(2^{S(n)}T(n)^{2})$ classical gate are needed to simulate $S(n)$ qubit circuit with just one quantum gate. Therefore, $O(2^{S(n)}T(n)^{3})$ classical gates are needed to simulate a quantum circuit of $S(n)$ qubits with $T(n)$ quantum gates. While there is no known way to efficiently simulate a quantum computer with a classical computer, it is possible to efficiently simulate a classical computer with a quantum computer. This is evident from the fact that ${\mathsf {BPP\subseteq BQP}}$ .

## Quantum query complexity

One major advantage of using a quantum computational system instead of a classical one, is that a quantum computer may be able to give a polynomial-time algorithm for some problem for which no classical polynomial-time algorithm exists, but more importantly, a quantum computer may significantly decrease the calculation time for a problem that a classical computer can already solve efficiently. Essentially, a quantum computer may be able to both determine how long it will take to solve a problem, while a classical computer may be unable to do so, and can also greatly improve the computational efficiency associated with the solution to a particular problem. Quantum query complexity refers to how complex, or how many queries to the graph associated with the solution of a particular problem, are required to solve the problem. Before we delve further into query complexity, let us consider some background regarding graphing solutions to particular problems, and the queries associated with these solutions.

### Query models of directed graphs

One type of problem that quantum computing can make easier to solve are graph problems. If we are to consider the amount of queries to a graph that are required to solve a given problem, let us first consider the most common types of graphs, called directed graphs, that are associated with this type of computational modelling. In brief, directed graphs are graphs where all edges between vertices are unidirectional. Directed graphs are formally defined as the graph $G=(N,E)$ , where N is the set of vertices, or nodes, and E is the set of edges.

#### Adjacency matrix model

When considering quantum computation of the solution to directed graph problems, there are two important query models to understand. First, there is the adjacency matrix model, where the graph of the solution is given by the adjacency matrix: $M\in {\{0,1\}}^{n\times n}$ , with $M_{ij}=1$ , if and only if $(v_{i},v_{j})\in E$ .

#### Adjacency array model

Next, there is the slightly more complicated adjacency array model built on the idea of adjacency lists, where every vertex, u *,* is associated with an array of neighboring vertices such that $f_{i}:[d_{i}^{+}]\rightarrow [n]$ , for the out-degrees of vertices $d_{i}^{+},...,d_{n}^{+}$ , where n is the minimum value of the upper bound of this model, and $f_{i}(j)$ returns the " $j^{th}$ " vertex adjacent to i . Additionally, the adjacency array model satisfies the simple graph condition, $\forall i\in [n],j,j'\in [k],j\neq j':f_{i}(j)\neq f_{i}(j')$ , meaning that there is only one edge between any pair of vertices, and the number of edges is minimized throughout the entire model (see Spanning tree model for more background).

### Quantum query complexity of certain types of graph problems

Both of the above models can be used to determine the query complexity of particular types of graphing problems, including the connectivity, strong connectivity (a directed graph version of the connectivity model), minimum spanning tree, and single source shortest path models of graphs. An important caveat to consider is that the quantum complexity of a particular type of graphing problem can change based on the query model (namely either matrix or array) used to determine the solution. The following table showing the quantum query complexities of these types of graphing problems illustrates this point well.

| Problem | Matrix model | Array model |
|---|---|---|
| Minimum spanning tree | $\Theta (n^{3/2})$ | $\Theta ({\sqrt {nm}})$ |
| Connectivity | $\Theta (n^{3/2})$ | $\Theta (n)$ |
| Strong connectivity | $\Theta (n^{3/2})$ | $\Omega ({\sqrt {nm}})$ , $O({\sqrt {nm\log(n)}})$ |
| Single source shortest path | $\Omega (n^{3/2})$ , $O(n^{3/2}\log ^{2}n)$ | $\Omega ({\sqrt {nm}})$ , $O({\sqrt {nm}}\log ^{2}(n))$ |

Notice the discrepancy between the quantum query complexities associated with a particular type of problem, depending on which query model was used to determine the complexity. For example, when the matrix model is used, the quantum complexity of the connectivity model in big O notation is $\Theta (n^{3/2})$ , but when the array model is used, the complexity is $\Theta (n)$ . Additionally, for brevity, we use the shorthand m in certain cases, where $m=\Theta (n^{2})$ . The important implication here is that the efficiency of the algorithm used to solve a graphing problem is dependent on the type of query model used to model the graph.

### Other types of quantum computational queries

In the query complexity model, the input can also be given as an oracle (black box). The algorithm gets information about the input only by querying the oracle. The algorithm starts in some fixed quantum state and the state evolves as it queries the oracle.

Similar to the case of graphing problems, the quantum query complexity of a black-box problem is the smallest number of queries to the oracle that are required in order to calculate the function. This makes the quantum query complexity a lower bound on the overall time complexity of a function.

#### Grover's algorithm

An example depicting the power of quantum computing is Grover's algorithm for searching unstructured databases. The algorithm's quantum query complexity is ${\textstyle O{\left({\sqrt {N}}\right)}}$ , a quadratic improvement over the best possible classical query complexity $O(N)$ , which is a linear search. Grover's algorithm is asymptotically optimal; in fact, it uses at most a $1+o(1)$ fraction more queries than the best possible algorithm.

#### Deutsch–Jozsa algorithm

The Deutsch–Jozsa algorithm is a quantum algorithm designed to solve a toy problem with a smaller query complexity than is possible with a classical algorithm. The toy problem asks whether a function $f:\{0,1\}^{n}\rightarrow \{0,1\}$ is constant or balanced, those being the only two possibilities. The only way to evaluate the function f is to consult a black box or oracle. A classical deterministic algorithm will have to check more than half of the possible inputs to be sure of whether or not the function is constant or balanced. With $2^{n}$ possible inputs, the query complexity of the most efficient classical deterministic algorithm is $2^{n-1}+1$ . The Deutsch–Jozsa algorithm takes advantage of quantum parallelism to check all of the elements of the domain at once and only needs to query the oracle once, making its query complexity 1 .

## Other theories of quantum physics

It has been speculated that further advances in physics could lead to even faster computers. For instance, it has been shown that a non-local, but non-signaling hidden variable quantum computer could implement a search of an N-item database in at most $O({\sqrt[{3}]{N}})$ steps, a slight speedup over Grover's algorithm, which runs in $O({\sqrt {N}})$ steps. Note, however, that neither search method would allow quantum computers to solve NP-complete problems in polynomial time. Theories of quantum gravity, such as M-theory and loop quantum gravity, may allow even faster computers to be built. However, defining computation in these theories is an open problem due to the problem of time; that is, within these physical theories there is currently no obvious way to describe what it means for an observer to submit input to a computer at one point in time and then receive output at a later point in time.
