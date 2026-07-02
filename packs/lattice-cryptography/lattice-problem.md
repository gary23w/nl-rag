---
title: "Lattice problem"
source: https://en.wikipedia.org/wiki/Lattice_problem
domain: lattice-cryptography
license: CC-BY-SA-4.0
tags: lattice based cryptography, learning with errors problem, shortest vector problem, quantum resistant key exchange, ntru lattice scheme
fetched: 2026-07-02
---

# Lattice problem

In computer science, **lattice problems** are a class of optimization problems related to mathematical objects called *lattices*. The conjectured intractability of such problems is central to the construction of secure lattice-based cryptosystems: lattice problems are an example of NP-hard problems which have been shown to be average-case hard, providing a test case for the security of cryptographic algorithms. In addition, some lattice problems which are worst-case hard can be used as a basis for extremely secure cryptographic schemes. The use of worst-case hardness in such schemes makes them among the very few schemes that are very likely secure even against quantum computers. For applications in such cryptosystems, lattices over vector spaces (often $\mathbb {Q} ^{n}$ ) or free modules (often $\mathbb {Z} ^{n}$ ) are generally considered.

For all the problems below, assume that we are given (in addition to other more specific inputs) a basis for the vector space *V* and a norm *N*. The norm usually considered is the Euclidean norm *L*2. However, other norms (such as *L**p*) are also considered and show up in a variety of results.

Throughout this article, let $\lambda (L)$ denote the length of the shortest non-zero vector in the lattice *L*: that is,

$\lambda (L)=\min _{v\in L\smallsetminus \{\mathbf {0} \}}\|v\|_{N}.$

## Shortest vector problem (SVP)

In the SVP, a basis of a vector space *V* and a norm *N* (often *L*2) are given for a lattice *L* and one must find the shortest non-zero vector in *V*, as measured by *N*, in *L*. In other words, the algorithm should output a non-zero vector *v* such that ⁠ $\|v\|_{N}=\lambda (L)$ ⁠. In the following, the size of the problem is specified by *n*, the dimension of the vector space *V*.

In the γ-approximation version SVPγ, one must find a non-zero lattice vector of length at most $\gamma \cdot \lambda (L)$ for given ⁠ $\gamma \geq 1$ ⁠.

### Hardness results

The exact version of the problem is only known to be NP-hard for randomized reductions. By contrast, the corresponding problem with respect to the uniform norm is known to be NP-hard.

### Algorithms for the Euclidean norm

To solve the exact version of the SVP under the Euclidean norm, several different approaches are known, which can be split into two classes: algorithms requiring superexponential time ( $2^{\omega (n)}$ ) and $\operatorname {poly} (n)$ memory, and algorithms requiring both exponential time and space ( $2^{\Theta (n)}$ ) in the lattice dimension. The former class of algorithms most notably includes lattice enumeration and random sampling reduction, while the latter includes lattice sieving, computing the Voronoi cell of the lattice, and discrete Gaussian sampling. An open problem is whether algorithms for solving exact SVP exist running in single exponential time ( $2^{O(n)}$ ) and requiring memory scaling polynomially in the lattice dimension.

To solve the γ-approximation version SVPγ for $\gamma >1$ for the Euclidean norm, the best known approaches are based on using lattice basis reduction. For large ⁠ $\gamma =2^{\Omega (n)}$ ⁠, the Lenstra–Lenstra–Lovász (LLL) algorithm can find a solution in time polynomial in the lattice dimension. For smaller values $\gamma$ , the Block Korkine-Zolotarev algorithm (BKZ) is commonly used, where the input to the algorithm (the blocksize $\beta$ ) determines the time complexity and output quality: for large approximation factors $\gamma$ , a small block size $\beta$ suffices, and the algorithm terminates quickly. For small $\gamma$ , larger $\beta$ are needed to find sufficiently short lattice vectors, and the algorithm takes longer to find a solution. The BKZ algorithm internally uses an exact SVP algorithm as a subroutine (running in lattices of dimension at most $\beta$ ), and its overall complexity is closely related to the costs of these SVP calls in dimension ⁠ $\beta$ ⁠.

## GapSVP

The problem GapSVPβ consists of distinguishing between the instances of SVP in which the length of the shortest vector is at most 1 or larger than ⁠ $\beta$ ⁠, where $\beta$ can be a fixed function of the dimension of the lattice ⁠ n ⁠. Given a basis for the lattice, the algorithm must decide whether $\lambda (L)\leq 1$ or ⁠ $\lambda (L)>\beta$ ⁠. Like other promise problems, the algorithm is allowed to err on all other cases.

Yet another version of the problem is GapSVPζ,γ for some functions ζ and γ. The input to the algorithm is a basis B and a number d . It is assured that all the vectors in the Gram–Schmidt orthogonalization are of length at least 1, and that $\lambda (L(B))\leq \zeta (n)$ and that ⁠ $1\leq d\leq \zeta (n)/\gamma (n)$ ⁠, where n is the dimension. The algorithm must accept if ⁠ $\lambda (L(B))\leq d$ ⁠, and reject if ⁠ $\lambda (L(B))\geq \gamma (n)\cdot d$ ⁠. For large $\zeta$ (i.e. ⁠ $\zeta (n)>2^{n/2}$ ⁠), the problem is equivalent to GapSVPγ because a preprocessing done using the LLL algorithm makes the second condition (and hence, ⁠ $\zeta$ ⁠) redundant.

## Closest vector problem (CVP)

In CVP, a basis of a vector space *V* and a metric *M* (often *L*2) are given for a lattice *L*, as well as a vector *v* in *V* but not necessarily in *L*. It is desired to find the vector in *L* closest to *v* (as measured by *M*). In the $\gamma$ -approximation version CVPγ, one must find a lattice vector at distance at most $\gamma$ .

### Relationship with SVP

The closest vector problem is a generalization of the shortest vector problem. It is easy to show that given an oracle for CVPγ (defined below), one can solve SVPγ by making some queries to the oracle. The naive method to find the shortest vector by calling the CVPγ oracle to find the closest vector to 0 does not work because 0 is itself a lattice vector and the algorithm could potentially output 0.

The reduction from SVPγ to CVPγ is as follows: Suppose that the input to the SVPγ is the basis for lattice $B=[b_{1},b_{2},\ldots ,b_{n}]$ . Consider the basis $B^{i}=[b_{1},\ldots ,2b_{i},\ldots ,b_{n}]$ and let $x_{i}$ be the vector returned by CVPγ(*B**i*, *b**i*). The claim is that the shortest vector in the set $\{x_{i}-b_{i}\}$ is the shortest vector in the given lattice.

### Hardness results

Goldreich et al. showed that any hardness of SVP implies the same hardness for CVP. Using PCP tools, Arora et al. showed that CVP is hard to approximate within factor $2^{\log ^{1-\epsilon }(n)}$ unless $\operatorname {NP} \subseteq \operatorname {DTIME} (2^{\operatorname {poly} (\log n)})$ . Dinur et al. strengthened this by giving a NP-hardness result with $\epsilon =(\log \log n)^{c}$ for $c<1/2$ .

### Sphere decoding

Algorithms for CVP, especially the Fincke and Pohst variant, have been used for data detection in multiple-input multiple-output (MIMO) wireless communication systems (for coded and uncoded signals). In this context it is called *sphere decoding* due to the radius used internal to many CVP solutions.

It has been applied in the field of the integer ambiguity resolution of carrier-phase GNSS (GPS). It is called the *LAMBDA method* in that field. In the same field, the general CVP problem is referred to as *Integer Least Squares*.

## GapCVP

This problem is similar to the GapSVP problem. For GapSVPβ, the input consists of a lattice basis and a vector v , and the algorithm must answer whether one of the following holds:

- there is a lattice vector such that the distance between it and v is at most 1, and
- every lattice vector is at a distance greater than $\beta$ away from v .

The opposite condition is that the closest lattice vector is at a distance $1<\lambda (L)\leq \beta$ , hence the name *Gap*CVP.

### Known results

The problem is trivially contained in NP for any approximation factor.

Schnorr, in 1987, showed that deterministic polynomial time algorithms can solve the problem for $\beta =2^{O(n(\log \log n)^{2}/\log n)}$ . Ajtai et al. showed that probabilistic algorithms can achieve a slightly better approximation factor of $\beta =2^{O(n\log \log n/\log n)}$ .

In 1993, Banaszczyk showed that GapCVPn is in ${\mathsf {NP\cap coNP}}$ . In 2000, Goldreich and Goldwasser showed that $\beta ={\sqrt {n/\log n}}$ puts the problem in both NP and coAM. In 2005, Aharonov and Regev showed that for some constant c , the problem with $\beta =c{\sqrt {n}}$ is in ${\mathsf {NP\cap coNP}}$ .

For lower bounds, Dinur et al. showed in 1998 that the problem is NP-hard for $\beta =n^{o(1/\log {\log {n}})}$ .

## Shortest independent vectors problem (SIVP)

Given a lattice L of dimension *n*, the algorithm must output *n* linearly independent $v_{1},v_{2},\ldots ,v_{n}$ so that $\max \|v_{i}\|\leq \max _{B}\|b_{i}\|$ , where the right-hand side considers all bases $B=\{b_{1},\ldots ,b_{n}\}$ of the lattice.

In the $\gamma$ -approximate version, given a lattice L with dimension *n*, one must find *n* linearly independent vectors $v_{1},v_{2},\ldots ,v_{n}$ of length ⁠ $\max \|v_{i}\|\leq \gamma \lambda _{n}(L)$ ⁠, where $\lambda _{n}(L)$ is the ⁠ n ⁠th successive minimum of ⁠ L ⁠.

## Bounded distance decoding

This problem is similar to CVP. Given a vector such that its distance from the lattice is at most $\lambda (L)/2$ , the algorithm must output the closest lattice vector to it.

## Covering radius problem

Given a basis for the lattice, the algorithm must find the largest distance (or in some versions, its approximation) from any vector to the lattice.

## Shortest basis problem

Many problems become easier if the input basis consists of short vectors. An algorithm that solves the Shortest Basis Problem (SBP) must, given a lattice basis ⁠ B ⁠, output an equivalent basis $B'$ such that the length of the longest vector in $B'$ is as short as possible.

The approximation version SBPγ problem consist of finding a basis whose longest vector is at most $\gamma$ times longer than the longest vector in the shortest basis.

## Use in cryptography

Average-case hardness of problems forms a basis for proofs-of-security for most cryptographic schemes. However, experimental evidence suggests that most NP-hard problems lack this property: they are probably only worst case hard. Many lattice problems have been conjectured or proven to be average-case hard, making them an attractive class of problems to base cryptographic schemes on. Moreover, worst-case hardness of some lattice problems have been used to create secure cryptographic schemes. The use of worst-case hardness in such schemes makes them among the very few schemes that are very likely secure even against quantum computers.

The above lattice problems are easy to solve if the algorithm is provided with a "good" basis. Lattice reduction algorithms aim, given a basis for a lattice, to output a new basis consisting of relatively short, nearly orthogonal vectors. The Lenstra–Lenstra–Lovász lattice basis reduction algorithm (LLL) was an early efficient algorithm for this problem which could output an almost reduced lattice basis in polynomial time. This algorithm and its further refinements were used to break several cryptographic schemes, establishing its status as a very important tool in cryptanalysis. The success of LLL on experimental data led to a belief that lattice reduction might be an easy problem in practice; however, this belief was challenged in the late 1990s, when several new results on the hardness of lattice problems were obtained, starting with the result of Ajtai.

In his seminal papers, Ajtai showed that the SVP problem was NP-hard and discovered some connections between the worst-case complexity and average-case complexity of some lattice problems. Building on these results, Ajtai and Dwork created a public-key cryptosystem whose security could be proven using only the worst case hardness of a certain version of SVP, thus making it the first result to have used worst-case hardness to create secure systems.
