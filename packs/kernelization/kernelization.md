---
title: "Kernelization"
source: https://en.wikipedia.org/wiki/Kernelization
domain: kernelization
license: CC-BY-SA-4.0
tags: kernelization technique, problem kernel, data reduction rule, vertex cover kernel
fetched: 2026-07-02
---

# Kernelization

In computer science, a **kernelization** is a technique for designing efficient algorithms that achieve their efficiency by a preprocessing stage in which inputs to the algorithm are replaced by a smaller input, called a "kernel". The result of solving the problem on the kernel should either be the same as on the original input, or it should be easy to transform the output on the kernel to the desired output for the original problem.

Kernelization is often achieved by applying a set of reduction rules that cut away parts of the instance that are easy to handle. In parameterized complexity theory, it is often possible to prove that a kernel with guaranteed bounds on the size of a kernel (as a function of some parameter associated to the problem) can be found in polynomial time. When this is possible, it results in a fixed-parameter tractable algorithm whose running time is the sum of the (polynomial time) kernelization step and the (non-polynomial but bounded by the parameter) time to solve the kernel. Indeed, every problem that can be solved by a fixed-parameter tractable algorithm can be solved by a kernelization algorithm of this type. This is also true for approximate kernelization.

## Example: vertex cover

A standard example for a kernelization algorithm is the kernelization of the vertex cover problem by S. Buss. In this problem, the input is an undirected graph G together with a number k . The output is a set of at most k vertices that includes an endpoint of every edge in the graph, if such a set exists, or a failure exception if no such set exists. This problem is NP-hard. However, the following reduction rules may be used to kernelize it:

1. If $k>0$ and v is a vertex of degree greater than k , remove v from the graph and decrease k by one. Every vertex cover of size k must contain v since otherwise too many of its neighbors would have to be picked to cover the incident edges. Thus, an optimal vertex cover for the original graph may be formed from a cover of the reduced problem by adding v back to the cover.
2. If v is an isolated vertex, remove it. An isolated vertex cannot cover any edges, so in this case v cannot be part of any minimal cover.
3. If more than $k^{2}$ edges remain in the graph, and neither of the previous two rules can be applied, then the graph cannot contain a vertex cover of size k . For, after eliminating all vertices of degree greater than k , each remaining vertex can only cover at most k edges and a set of k vertices could only cover at most $k^{2}$ edges. In this case, the instance may be replaced by an instance with two vertices, one edge, and $k=0$ , which also has no solution.

An algorithm that applies these rules repeatedly until no more reductions can be made necessarily terminates with a kernel that has at most $k^{2}$ edges and (because each edge has at most two endpoints and there are no isolated vertices) at most $2k^{2}$ vertices. This kernelization may be implemented in linear time. Once the kernel has been constructed, the vertex cover problem may be solved by a brute force search algorithm that tests whether each subset of the kernel is a cover of the kernel. Thus, the vertex cover problem can be solved in time $O(2^{2k^{2}}+n+m)$ for a graph with n vertices and m edges, allowing it to be solved efficiently when k is small even if n and m are both large.

Although this bound is fixed-parameter tractable, its dependence on the parameter is higher than might be desired. More complex kernelization procedures can improve this bound, by finding smaller kernels, at the expense of greater running time in the kernelization step. In the vertex cover example, kernelization algorithms are known that produce kernels with at most $2k$ vertices. One algorithm that achieves this improved bound exploits the half-integrality of the linear program relaxation of vertex cover due to Nemhauser and Trotter. Another kernelization algorithm achieving that bound is based on what is known as the crown reduction rule and uses alternating path arguments. The currently best known kernelization algorithm in terms of the number of vertices is due to Lampis (2011) and achieves $2k-c\log k$ vertices for any fixed constant c .

It is not possible, in this problem, to find a kernel of size $O(\log k)$ , unless P = NP, for such a kernel would lead to a polynomial-time algorithm for the NP-hard vertex cover problem. However, much stronger bounds on the kernel size can be proven in this case: unless coNP $\subseteq$ NP/poly (believed unlikely by complexity theorists), for every $\epsilon >0$ it is impossible in polynomial time to find kernels with $O(k^{2-\epsilon })$ edges. It is unknown for vertex cover whether kernels with $(2-\epsilon )k$ vertices for some $\epsilon >0$ would have any unlikely complexity-theoretic consequences.

## Definition

In the literature, there is no clear consensus on how kernelization should be formally defined and there are subtle differences in the uses of that expression.

### Downey–Fellows notation

In the notation of Downey & Fellows (1999), a *parameterized problem* is a subset $L\subseteq \Sigma ^{*}\times \mathbb {N}$ describing a decision problem.

A **kernelization** for a parameterized problem L is an algorithm that takes an instance $(x,k)$ and maps it in time polynomial in $|x|$ and k to an instance $(x',k')$ such that

- $(x,k)$ is in L if and only if $(x',k')$ is in L ,
- the size of $x'$ is bounded by a computable function f in k , and
- $k'$ is bounded by a function in k .

The output $(x',k')$ of kernelization is called a kernel. In this general context, the *size* of the string $x'$ just refers to its length. Some authors prefer to use the number of vertices or the number of edges as the size measure in the context of graph problems.

### Flum–Grohe notation

In the notation of Flum & Grohe (2006, p. 4), a *parameterized problem* consists of a decision problem $L\subseteq \Sigma ^{*}$ and a function $\kappa :\Sigma ^{*}\to \mathbb {N}$ , the parameterization. The *parameter* of an instance x is the number $\kappa (x)$ .

A **kernelization** for a parameterized problem L is an algorithm that takes an instance x with parameter k and maps it in polynomial time to an instance y such that

- x is in L if and only if y is in L and
- the size of y is bounded by a computable function f in k .

Note that in this notation, the bound on the size of y implies that the parameter of y is also bounded by a function in k .

The function f is often referred to as the size of the kernel. If $f=k^{O(1)}$ , it is said that L admits a polynomial kernel. Similarly, for $f={O(k)}$ , the problem admits linear kernel.

## Kernelizability and fixed-parameter tractability are equivalent

A problem is fixed-parameter tractable if and only if it is kernelizable and decidable.

That a kernelizable and decidable problem is fixed-parameter tractable can be seen from the definition above: First the kernelization algorithm, which runs in time $O(|x|^{c})$ for some c, is invoked to generate a kernel of size $f(k)$ . The kernel is then solved by the algorithm that proves that the problem is decidable. The total running time of this procedure is $g(f(k))+O(|x|^{c})$ , where $g(n)$ is the running time for the algorithm used to solve the kernels. Since $g(f(k))$ is computable, e.g. by using the assumption that $f(k)$ is computable and testing all possible inputs of length $f(k)$ , this implies that the problem is fixed-parameter tractable.

The other direction, that a fixed-parameter tractable problem is kernelizable and decidable is a bit more involved. Assume that the question is non-trivial, meaning that there is at least one instance that is in the language, called $I_{yes}$ , and at least one instance that is not in the language, called $I_{no}$ ; otherwise, replacing any instance by the empty string is a valid kernelization. Assume also that the problem is fixed-parameter tractable, i.e., it has an algorithm that runs in at most $f(k)\cdot |x|^{c}$ steps on instances $(x,k)$ , for some constant c and some function $f(k)$ . To kernelize an input, run this algorithm on the given input for at most $|x|^{c+1}$ steps. If it terminates with an answer, use that answer to select either $I_{yes}$ or $I_{no}$ as the kernel. If, instead, it exceeds the $|x|^{c+1}$ bound on the number of steps without terminating, then return $(x,k)$ itself as the kernel. Because $(x,k)$ is only returned as a kernel for inputs with $f(k)\cdot |x|^{c}>|x|^{c+1}$ , it follows that the size of the kernel produced in this way is at most $\max\{|I_{yes}|,|I_{no}|,f(k)\}$ . This size bound is computable, by the assumption from fixed-parameter tractability that $f(k)$ is computable.

## More examples

- **Vertex cover** parametrized by the size of the vertex cover: The vertex cover problem has kernels with at most $2k$ vertices and $O(k^{2})$ edges. Furthermore, for any $\varepsilon >0$ , vertex cover does not have kernels with $O(k^{2-\varepsilon })$ edges unless ${\text{coNP}}\subseteq {\text{NP/poly}}$ . The vertex cover problems in d -uniform hypergraphs has kernels with $O(k^{d})$ edges using the sunflower lemma, and it does not have kernels of size $O(k^{d-\varepsilon })$ unless ${\text{coNP}}\subseteq {\text{NP/poly}}$ .
- **Feedback vertex set** parametrized by the size of the feedback vertex set: The feedback vertex set problem has kernels with $4k^{2}$ vertices and $O(k^{2})$ edges. Furthermore, it does not have kernels with $O(k^{2-\varepsilon })$ edges unless ${\text{coNP}}\subseteq {\text{NP/poly}}$ .
- **k -path:** The k -path problem is to decide whether a given graph has a path of length at least k . This problem has kernels of size exponential in k , and it does not have kernels of size polynomial in k unless ${\text{coNP}}\subseteq {\text{NP/poly}}$ .
- **Bidimensional problems:** Many parameterized versions of bidimensional problems have linear kernels on planar graphs, and more generally, on graphs excluding some fixed graph as a minor.

## Kernelization for structural parameterizations

While the parameter k in the examples above is chosen as the size of the desired solution, this is not necessary. It is also possible to choose a structural complexity measure of the input as the parameter value, leading to so-called structural parameterizations. This approach is fruitful for instances whose solution size is large, but for which some other complexity measure is bounded. For example, the *feedback vertex number* of an undirected graph G is defined as the minimum cardinality of a set of vertices whose removal makes G acyclic. The vertex cover problem parameterized by the feedback vertex number of the input graph has a polynomial kernelization: There is a polynomial-time algorithm that, given a graph G whose feedback vertex number is k , outputs a graph $G'$ on $O(k^{3})$ vertices such that a minimum vertex cover in $G'$ can be transformed into a minimum vertex cover for G in polynomial time. The kernelization algorithm therefore guarantees that instances with a small feedback vertex number k are reduced to small instances.
