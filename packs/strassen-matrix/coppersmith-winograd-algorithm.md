---
title: "Matrix multiplication algorithm"
source: https://en.wikipedia.org/wiki/Coppersmith–Winograd_algorithm
domain: strassen-matrix
license: CC-BY-SA-4.0
tags: strassen algorithm, matrix multiplication, divide and conquer, coppersmith winograd
fetched: 2026-07-02
---

# Matrix multiplication algorithm

(Redirected from

Coppersmith–Winograd algorithm

)

Because matrix multiplication is such a central operation in many numerical algorithms, much work has been invested in making **matrix multiplication algorithms** efficient. Applications of matrix multiplication in computational problems are found in many fields including scientific computing and pattern recognition and in seemingly unrelated problems such as counting the paths through a graph. Many different algorithms have been designed for multiplying matrices on different types of hardware, including parallel and distributed systems, where the computational work is spread over multiple processors (perhaps over a network).

Directly applying the mathematical definition of matrix multiplication gives an algorithm that takes time on the order of *n*3 field operations to multiply two *n* × *n* matrices over that field (Θ(*n*3) in big O notation). Better asymptotic bounds on the time required to multiply matrices have been known since the Strassen's algorithm in the 1960s, but the optimal time (that is, the computational complexity of matrix multiplication) remains unknown. As of September 2025, the best bound on the asymptotic complexity of a matrix multiplication algorithm is O(*n*2.371339) time, given by Alman, Duan, Williams, Xu, Xu, and Zhou. However, this algorithm is a galactic algorithm because of the large constants and cannot be realized practically.

## Iterative algorithm

The definition of matrix multiplication is that if *C* = *AB* for an *n* × *m* matrix A and an *m* × *p* matrix B, then C is an *n* × *p* matrix with entries

$c_{ij}=\sum _{k=1}^{m}a_{ik}b_{kj}.$

From this, a simple algorithm can be constructed which loops over the indices i from 1 through n and j from 1 through p, computing the above using a nested loop:

- Input: matrices A and B
- Let C be a new matrix of the appropriate size
- For i from 1 to n:
  - For j from 1 to p:
    - Let sum = 0
    - For k from 1 to m:
      - Set sum ← sum + *Aik* × *Bkj*
    - Set *Cij* ← sum
- Return C

This algorithm takes time Θ(*nmp*) (in asymptotic notation). A common simplification for the purpose of algorithm analysis is to assume that the inputs are all square matrices of size *n* × *n*, in which case the running time is Θ(*n*3), i.e., cubic in the size of the dimension.

### Cache behavior

The three loops in iterative matrix multiplication can be arbitrarily swapped with each other without an effect on correctness or asymptotic running time. However, the order can have a considerable impact on practical performance due to the memory access patterns and cache use of the algorithm; which order is best also depends on whether the matrices are stored in row-major order, column-major order, or a mix of both.

In particular, in the idealized case of a fully associative cache consisting of M bytes and b bytes per cache line (i.e. ⁠*M*/*b*⁠ cache lines), the above algorithm is sub-optimal for A and B stored in row-major order. When *n* > ⁠*M*/*b*⁠, every iteration of the inner loop (a simultaneous sweep through a row of A and a column of B) incurs a cache miss when accessing an element of B. This means that the algorithm incurs Θ(*n*3) cache misses in the worst case. As of 2010, the speed of memories compared to that of processors is such that the cache misses, rather than the actual calculations, dominate the running time for sizable matrices.

The optimal variant of the iterative algorithm for A and B in row-major layout is a *tiled* version, where the matrix is implicitly divided into square tiles of size √*M* by √*M*:

- Input: matrices A and B
- Let C be a new matrix of the appropriate size
- Pick a tile size *T* = Θ(√*M*)
- For I from 1 to n in steps of T:
  - For J from 1 to p in steps of T:
    - For K from 1 to m in steps of T:
      - Multiply *A**I*:*I*+*T*, *K*:*K*+*T* and *B**K*:*K*+*T*, *J*:*J*+*T* into *C**I*:*I*+*T*, *J*:*J*+*T*, that is:
      - For i from I to min(*I* + *T*, *n*):
        - For j from J to min(*J* + *T*, *p*):
          - Let sum = 0
          - For k from K to min(*K* + *T*, *m*):
            - Set sum ← sum + *Aik* × *Bkj*
          - Set *Cij* ← *Cij* + sum
- Return C

In the idealized cache model, this algorithm incurs only Θ(⁠*n*3/*b* √*M*⁠) cache misses; the divisor *b* √*M* amounts to several orders of magnitude on modern machines, so that the actual calculations dominate the running time, rather than the cache misses.

## Divide-and-conquer algorithm

An alternative to the iterative algorithm is the divide-and-conquer algorithm for matrix multiplication. This relies on the block partitioning

$C={\begin{pmatrix}C_{11}&C_{12}\\C_{21}&C_{22}\\\end{pmatrix}},\,A={\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\\\end{pmatrix}},\,B={\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\\\end{pmatrix}},$

which works for all square matrices whose dimensions are powers of two, i.e., the shapes are 2*n* × 2*n* for some n. The matrix product is now

${\begin{pmatrix}C_{11}&C_{12}\\C_{21}&C_{22}\\\end{pmatrix}}={\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\\\end{pmatrix}}{\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\\\end{pmatrix}}={\begin{pmatrix}A_{11}B_{11}+A_{12}B_{21}&A_{11}B_{12}+A_{12}B_{22}\\A_{21}B_{11}+A_{22}B_{21}&A_{21}B_{12}+A_{22}B_{22}\\\end{pmatrix}}$

which consists of eight multiplications of pairs of submatrices, followed by an addition step. The divide-and-conquer algorithm computes the smaller multiplications recursively, using the scalar multiplication *c*11 = *a*11*b*11 as its base case.

The complexity of this algorithm as a function of n is given by the recurrence

$T(1)=\Theta (1);$

$T(n)=8T(n/2)+\Theta (n^{2}),$

accounting for the eight recursive calls on matrices of size *n*/2 and Θ(*n*2) to sum the four pairs of resulting matrices element-wise. Application of the master theorem for divide-and-conquer recurrences shows this recursion to have the solution Θ(*n*3), the same as the iterative algorithm.

### Non-square matrices

A variant of this algorithm that works for matrices of arbitrary shapes and is faster in practice splits matrices in two instead of four submatrices, as follows. Splitting a matrix now means dividing it into two parts of equal size, or as close to equal sizes as possible in the case of odd dimensions.

- Inputs: matrices A of size *n* × *m*, B of size *m* × *p*.
- Base case: if max(*n*, *m*, *p*) is below some threshold, use an unrolled version of the iterative algorithm.
- Recursive cases:

- If max(*n*, *m*, *p*) = *n*, split A horizontally:

$C={\begin{pmatrix}A_{1}\\A_{2}\end{pmatrix}}{B}={\begin{pmatrix}A_{1}B\\A_{2}B\end{pmatrix}}$

- Else, if max(*n*, *m*, *p*) = *p*, split B vertically:

$C=A{\begin{pmatrix}B_{1}&B_{2}\end{pmatrix}}={\begin{pmatrix}AB_{1}&AB_{2}\end{pmatrix}}$

- Otherwise, max(*n*, *m*, *p*) = *m*. Split A vertically and B horizontally:

$C={\begin{pmatrix}A_{1}&A_{2}\end{pmatrix}}{\begin{pmatrix}B_{1}\\B_{2}\end{pmatrix}}=A_{1}B_{1}+A_{2}B_{2}$

### Cache behavior

The cache miss rate of recursive matrix multiplication is the same as that of a tiled iterative version, but unlike that algorithm, the recursive algorithm is cache-oblivious: there is no tuning parameter required to get optimal cache performance, and it behaves well in a multiprogramming environment where cache sizes are effectively dynamic due to other processes taking up cache space. (The simple iterative algorithm is cache-oblivious as well, but much slower in practice if the matrix layout is not adapted to the algorithm.)

The number of cache misses incurred by this algorithm, on a machine with M lines of ideal cache, each of size b bytes, is bounded by

$\Theta \left(m+n+p+{\frac {mn+np+mp}{b}}+{\frac {mnp}{b{\sqrt {M}}}}\right)$

## Sub-cubic algorithms

Algorithms exist that provide better running times than the straightforward ones. The first to be discovered was Strassen's algorithm, devised by Volker Strassen in 1969 and often referred to as "fast matrix multiplication". It is based on a way of multiplying two 2×2 matrices which requires only 7 multiplications (instead of the usual 8), at the expense of several additional addition and subtraction operations. Applying this recursively gives an algorithm with a multiplicative cost of $O(n^{\log _{2}7})\approx O(n^{2.807})$ . Strassen's algorithm is more complex, and the numerical stability is reduced compared to the naïve algorithm, but it is faster in cases where *n* > 100 or so and appears in several libraries, such as BLAS. It is very useful for large matrices over exact domains such as finite fields, where numerical stability is not an issue.

Since Strassen's algorithm is actually used in practical numerical software and computer algebra systems, improving on the constants hidden in the big-O notation has its merits. A table that compares key aspects of the improved version based on recursive multiplication of 2×2-block matrices via 7 block matrix multiplications follows. As usual, n gives the dimensions of the matrix and M designates the memory size.

| Year | Reference | #matrix multiplications per step | #matrix additions per step | total arithmetic operations | total I/O-complexity |
|---|---|---|---|---|---|
| 1969 | Strassen | 7 | 18 | $7n^{\log _{2}7}-6n^{2}$ | $6\left({\frac {{\sqrt {3}}n}{\sqrt {M}}}\right)^{\log _{2}7}\cdot M-18n^{2}+3M$ |
| 1971 | Winograd | 7 | 15 | $6n^{\log _{2}7}-5n^{2}$ | $5\left({\frac {{\sqrt {3}}n}{\sqrt {M}}}\right)^{\log _{2}7}\cdot M-15n^{2}+3M$ |
| 2017 | Karstadt, Schwartz | 7 | 12 | $5n^{\log _{2}7}-4n^{2}+3n^{2}\log _{2}n$ | $4\left({\frac {{\sqrt {3}}n}{\sqrt {M}}}\right)^{\log _{2}7}\cdot M-12n^{2}+3n^{2}\cdot \log _{2}\left({\frac {{\sqrt {2}}n}{\sqrt {M}}}\right)+5M$ |
| 2023 | Schwartz, Vaknin | 7 | 12 | $5n^{\log _{2}7}-4n^{2}+1.5n^{2}\log _{2}n$ | $4\left({\frac {{\sqrt {3}}n}{\sqrt {M}}}\right)^{\log _{2}7}\cdot M-12n^{2}+1.5n^{2}\cdot \log _{2}\left({\frac {{\sqrt {2}}n}{\sqrt {M}}}\right)+5M$ |

It is known that a Strassen-like algorithm with a 2×2-block matrix step requires at least 7 block matrix multiplications. In 1976 Probert showed that such an algorithm requires at least 15 additions (including subtractions); however, a hidden assumption was that the blocks and the 2×2-block matrix are represented in the same basis. Karstadt and Schwartz computed in different bases and traded 3 additions for less expensive basis transformations. They also proved that one cannot go below 12 additions per step using different bases. In subsequent work Beniamini et el. applied this base-change trick to more general decompositions than 2×2-block matrices and improved the leading constant for their run times.

It is an open question in theoretical computer science how well Strassen's algorithm can be improved in terms of asymptotic complexity. The *matrix multiplication exponent*, usually denoted $\omega$ , is the smallest real number for which any $n\times n$ matrix over a field can be multiplied together using $n^{\omega +o(1)}$ field operations. The current best bound on $\omega$ is $\omega <2.371339$ , by Alman, Duan, Williams, Xu, Xu, and Zhou. This algorithm, like all other recent algorithms in this line of research, is a generalization of the Coppersmith–Winograd algorithm, which was given by Don Coppersmith and Shmuel Winograd in 1990. The conceptual idea of these algorithms is similar to Strassen's algorithm: a way is devised for multiplying two *k* × *k*-matrices with fewer than *k*3 multiplications, and this technique is applied recursively. However, the constant coefficient hidden by the big-O notation is so large that these algorithms are only worthwhile for matrices that are too large to handle on present-day computers. Victor Pan proposed so-called feasible sub-cubic matrix multiplication algorithms with an exponent slightly above 2.77, but in return with a much smaller hidden constant coefficient.

Freivalds' algorithm is a simple Monte Carlo algorithm that, given matrices A, B and C, verifies in Θ(*n*2) time if *AB* = *C*.

### AlphaTensor

In 2022, DeepMind introduced AlphaTensor, a neural network that used a single-player game analogy to invent thousands of matrix multiplication algorithms, including some previously discovered by humans and some that were not. Operations were restricted to the non-commutative ground field (normal arithmetic) and finite field $\mathbb {Z} /2\mathbb {Z}$ (mod 2 arithmetic). The best "practical" (explicit low-rank decomposition of a matrix multiplication tensor) algorithm found ran in O(n2.778). Finding low-rank decompositions of such tensors (and beyond) is NP-hard; optimal multiplication even for 3×3 matrices remains unknown, even in commutative field. On 4×4 matrices, AlphaTensor unexpectedly discovered a solution with 47 multiplication steps, an improvement over the 49 required with Strassen’s algorithm of 1969, albeit restricted to mod 2 arithmetic. Similarly, AlphaTensor solved 5×5 matrices with 96 rather than Strassen's 98 steps. Based on the surprising discovery that such improvements exist, other researchers were quickly able to find a similar independent 4×4 algorithm, and separately tweaked Deepmind's 96-step 5×5 algorithm down to 95 steps in mod 2 arithmetic and to 97 in normal arithmetic. Some algorithms were completely new: for example, (4, 5, 5) was improved to 76 steps from a baseline of 80 in both normal and mod 2 arithmetic.

## Parallel and distributed algorithms

### Shared-memory parallelism

The divide-and-conquer algorithm sketched earlier can be parallelized in two ways for shared-memory multiprocessors. These are based on the fact that the eight recursive matrix multiplications in

${\begin{pmatrix}A_{11}B_{11}+A_{12}B_{21}&A_{11}B_{12}+A_{12}B_{22}\\A_{21}B_{11}+A_{22}B_{21}&A_{21}B_{12}+A_{22}B_{22}\\\end{pmatrix}}$

can be performed independently of each other, as can the four summations (although the algorithm needs to "join" the multiplications before doing the summations). Exploiting the full parallelism of the problem, one obtains an algorithm that can be expressed in fork–join style pseudocode:

**Procedure** multiply(*C*, *A*, *B*):

- Base case: if *n* = 1, set *c*11 ← *a*11 × *b*11 (or multiply a small block matrix).
- Otherwise, allocate space for a new matrix T of shape *n* × *n*, then:
  - Partition A into *A*11, *A*12, *A*21, *A*22.
  - Partition B into *B*11, *B*12, *B*21, *B*22.
  - Partition C into *C*11, *C*12, *C*21, *C*22.
  - Partition T into *T*11, *T*12, *T*21, *T*22.
  - Parallel execution:
    - *Fork* multiply(*C*11, *A*11, *B*11).
    - *Fork* multiply(*C*12, *A*11, *B*12).
    - *Fork* multiply(*C*21, *A*21, *B*11).
    - *Fork* multiply(*C*22, *A*21, *B*12).
    - *Fork* multiply(*T*11, *A*12, *B*21).
    - *Fork* multiply(*T*12, *A*12, *B*22).
    - *Fork* multiply(*T*21, *A*22, *B*21).
    - *Fork* multiply(*T*22, *A*22, *B*22).
  - *Join* (wait for parallel forks to complete).
  - add(*C*, *T*).
  - Deallocate T.

**Procedure** add(*C*, *T*) adds T into C, element-wise:

- Base case: if *n* = 1, set *c*11 ← *c*11 + *t*11 (or do a short loop, perhaps unrolled).
- Otherwise:
  - Partition C into *C*11, *C*12, *C*21, *C*22.
  - Partition T into *T*11, *T*12, *T*21, *T*22.
  - In parallel:
    - *Fork* add(*C*11, *T*11).
    - *Fork* add(*C*12, *T*12).
    - *Fork* add(*C*21, *T*21).
    - *Fork* add(*C*22, *T*22).
  - *Join*.

Here, *fork* is a keyword that signal a computation may be run in parallel with the rest of the function call, while *join* waits for all previously "forked" computations to complete. partition achieves its goal by pointer manipulation only.

This algorithm has a critical path length of Θ(log2 *n*) steps, meaning it takes that much time on an ideal machine with an infinite number of processors; therefore, it has a maximum possible speedup of Θ(*n*3/log2 *n*) on any real computer. The algorithm isn't practical due to the communication cost inherent in moving data to and from the temporary matrix T, but a more practical variant achieves Θ(*n*2) speedup, without using a temporary matrix.

### Communication-avoiding and distributed algorithms

On modern architectures with hierarchical memory, the cost of loading and storing input matrix elements tends to dominate the cost of arithmetic. On a single machine this is the amount of data transferred between RAM and cache, while on a distributed memory multi-node machine it is the amount transferred between nodes; in either case it is called the *communication bandwidth*. The naïve algorithm using three nested loops uses Ω(*n*3) communication bandwidth.

Cannon's algorithm, also known as the *2D algorithm*, is a communication-avoiding algorithm that partitions each input matrix into a block matrix whose elements are submatrices of size √*M*/3 by √*M*/3, where *M* is the size of fast memory. The naïve algorithm is then used over the block matrices, computing products of submatrices entirely in fast memory. This reduces communication bandwidth to *O*(*n*3/√*M*), which is asymptotically optimal (for algorithms performing Ω(*n*3) computation).

In a distributed setting with p processors arranged in a √*p* by √*p* 2D mesh, one submatrix of the result can be assigned to each processor, and the product can be computed with each processor transmitting *O*(*n*2/√*p*) words, which is asymptotically optimal assuming that each node stores the minimum *O*(*n*2/*p*) elements. This can be improved by the *3D algorithm,* which arranges the processors in a 3D cube mesh, assigning every product of two input submatrices to a single processor. The result submatrices are then generated by performing a reduction over each row. This algorithm transmits *O*(*n*2/*p*2/3) words per processor, which is asymptotically optimal. However, this requires replicating each input matrix element *p*1/3 times, and so requires a factor of *p*1/3 more memory than is needed to store the inputs. This algorithm can be combined with Strassen to further reduce runtime. "2.5D" algorithms provide a continuous tradeoff between memory usage and communication bandwidth. On modern distributed computing environments such as MapReduce, specialized multiplication algorithms have been developed.

### Algorithms for meshes

There are a variety of algorithms for multiplication on meshes. For multiplication of two *n*×*n* on a standard two-dimensional mesh using the 2D Cannon's algorithm, one can complete the multiplication in 3*n*-2 steps although this is reduced to half this number for repeated computations. The standard array is inefficient because the data from the two matrices does not arrive simultaneously and it must be padded with zeroes.

The result is even faster on a two-layered cross-wired mesh, where only 2*n*-1 steps are needed. The performance improves further for repeated computations leading to 100% efficiency. The cross-wired mesh array may be seen as a special case of a non-planar (i.e. multilayered) processing structure.

In a 3D mesh with *n*3 processing elements, two matrices can be multiplied in ${\mathcal {O}}(\log n)$ using the DNS algorithm.
