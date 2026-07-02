---
title: "Tensor rank decomposition"
source: https://en.wikipedia.org/wiki/Canonical_polyadic_decomposition
domain: tensor-decomposition
license: CC-BY-SA-4.0
tags: tensor decomposition, tucker decomposition, canonical polyadic decomposition, tensor rank
fetched: 2026-07-02
---

# Tensor rank decomposition

(Redirected from

Canonical polyadic decomposition

)

In multilinear algebra, the **tensor rank decomposition** or **rank-*R* decomposition** is the decomposition of a tensor as a sum of *R* rank-1 tensors, where *R* is minimal. Computing this decomposition is an open problem.

**Canonical polyadic decomposition (CPD)** is a variant of the tensor rank decomposition, in which the tensor is approximated as a sum of *K* rank-1 tensors for a user-specified *K*. The CP decomposition has found some applications in linguistics and chemometrics. It was introduced by Frank Lauren Hitchcock in 1927 and later rediscovered several times, notably in psychometrics. The CP decomposition is referred to as CANDECOMP, PARAFAC, or CANDECOMP/PARAFAC (CP). Note that the PARAFAC2 rank decomposition is a variation of the CP decomposition.

Another popular generalization of the matrix SVD known as the higher-order singular value decomposition computes orthonormal mode matrices and has found applications in econometrics, signal processing, computer vision, computer graphics, and psychometrics.

## Notation

A scalar variable is denoted by lower case italic letters, a and an upper bound scalar is denoted by an upper case italic letter, A .

Indices are denoted by a combination of lowercase and upper case italic letters, $1\leq i\leq I$ . Multiple indices that one might encounter when referring to the multiple modes of a tensor are conveniently denoted by $1\leq i_{m}\leq I_{m}$ where $1\leq m\leq M$ .

A vector is denoted by a lower case bold roman, $\mathbf {a}$ and a matrix is denoted by bold upper case letters $\mathbf {A}$ .

A higher order tensor is denoted by calligraphic letters, ${\mathcal {A}}$ . An element of an M -order tensor ${\mathcal {A}}\in \mathbb {C} ^{I_{1}\times I_{2}\times \dots I_{m}\times \dots I_{M}}$ is denoted by $a_{i_{1},i_{2},\dots ,i_{m},\dots i_{M}}$ or ${\mathcal {A}}_{i_{1},i_{2},\dots ,i_{m},\dots i_{M}}$ .

## Definition

A data tensor ${\mathcal {A}}\in {\mathbb {F} }^{I_{0}\times I_{1}\times \ldots \times I_{C}}$ is a collection of multivariate observations organized into a M-way array where M=C+1. Every tensor may be represented with a suitably large R as a linear combination of R rank-1 tensors:

${\mathcal {A}}=\sum _{r=1}^{R}\lambda _{r}\mathbf {a} _{0,r}\otimes \mathbf {a} _{1,r}\otimes \mathbf {a} _{2,r}\dots \otimes \mathbf {a} _{c,r}\otimes \cdots \otimes \mathbf {a} _{C,r},$

where $\lambda _{r}\in {\mathbb {F} }$ and $\mathbf {a} _{m,r}\in {\mathbb {F} }^{I_{m}}$ where $1\leq m\leq M$ . When the number of terms R is minimal in the above expression, then R is called the **rank** of the tensor, and the decomposition is often referred to as a *(tensor) rank decomposition*, *minimal CP decomposition*, or *Canonical Polyadic Decomposition (CPD)*. If the number of terms is not minimal, then the above decomposition is often referred to as *CANDECOMP/PARAFAC*, *Polyadic decomposition*.

## Tensor rank

Contrary to the case of matrices, computing the rank of a tensor is NP-hard. The only notable well-understood case consists of tensors in $F^{I_{m}}\otimes F^{I_{n}}\otimes F^{2}$ , whose rank can be obtained from the Kronecker–Weierstrass normal form of the linear matrix pencil that the tensor represents. A simple polynomial-time algorithm exists for certifying that a tensor is of rank 1, namely the higher-order singular value decomposition.

The rank of the tensor of zeros is zero by convention. The rank of a tensor $\mathbf {a} _{1}\otimes \cdots \otimes \mathbf {a} _{M}$ is one, provided that $\mathbf {a} _{m}\in F^{I_{m}}\setminus \{0\}$ .

### Field dependence

The rank of a tensor depends on the field over which the tensor is decomposed. It is known that some real tensors may admit a complex decomposition whose rank is strictly less than the rank of a real decomposition of the same tensor. As an example, consider the following real tensor

${\mathcal {A}}=\mathbf {x} _{1}\otimes \mathbf {x} _{2}\otimes \mathbf {x} _{3}+\mathbf {x} _{1}\otimes \mathbf {y} _{2}\otimes \mathbf {y} _{3}-\mathbf {y} _{1}\otimes \mathbf {x} _{2}\otimes \mathbf {y} _{3}+\mathbf {y} _{1}\otimes \mathbf {y} _{2}\otimes \mathbf {x} _{3},$

where $\mathbf {x} _{i},\mathbf {y} _{j}\in \mathbb {R} ^{2}$ . The rank of this tensor over the reals is known to be 3, while its complex rank is only 2 because it is the sum of a complex rank-1 tensor with its complex conjugate, namely

${\mathcal {A}}={\frac {1}{2}}({\bar {\mathbf {z} }}_{1}\otimes \mathbf {z} _{2}\otimes {\bar {\mathbf {z} }}_{3}+\mathbf {z} _{1}\otimes {\bar {\mathbf {z} }}_{2}\otimes \mathbf {z} _{3}),$

where $\mathbf {z} _{k}=\mathbf {x} _{k}+i\mathbf {y} _{k}$ .

In contrast, the rank of real matrices will never decrease under a field extension to $\mathbb {C}$ : real matrix rank and complex matrix rank coincide for real matrices.

### Generic rank

The **generic rank** $r(I_{1},\ldots ,I_{M})$ is defined as the least rank r such that the closure in the Zariski topology of the set of tensors of rank at most r is the entire space $F^{I_{1}}\otimes \cdots \otimes F^{I_{M}}$ . In the case of complex tensors, tensors of rank at most $r(I_{1},\ldots ,I_{M})$ form a dense set S : every tensor in the aforementioned space is either of rank less than the generic rank, or it is the limit in the Euclidean topology of a sequence of tensors from S . In the case of real tensors, the set of tensors of rank at most $r(I_{1},\ldots ,I_{M})$ only forms an open set of positive measure in the Euclidean topology. There may exist Euclidean-open sets of tensors of rank strictly higher than the generic rank. All ranks appearing on open sets in the Euclidean topology are called **typical ranks**. The smallest typical rank is called the generic rank; this definition applies to both complex and real tensors. The generic rank of tensor spaces was initially studied in 1983 by Volker Strassen.

As an illustration of the above concepts, it is known that both 2 and 3 are typical ranks of $\mathbb {R} ^{2}\otimes \mathbb {R} ^{2}\otimes \mathbb {R} ^{2}$ while the generic rank of $\mathbb {C} ^{2}\otimes \mathbb {C} ^{2}\otimes \mathbb {C} ^{2}$ is 2. Practically, this means that a randomly sampled real tensor (from a continuous probability measure on the space of tensors) of size $2\times 2\times 2$ will be a rank-1 tensor with probability zero, a rank-2 tensor with positive probability, and rank-3 with positive probability. On the other hand, a randomly sampled complex tensor of the same size will be a rank-1 tensor with probability zero, a rank-2 tensor with probability one, and a rank-3 tensor with probability zero. It is even known that the generic rank-3 real tensor in $\mathbb {R} ^{2}\otimes \mathbb {R} ^{2}\otimes \mathbb {R} ^{2}$ will be of complex rank equal to 2.

The generic rank of tensor spaces depends on the distinction between balanced and unbalanced tensor spaces. A tensor space $F^{I_{1}}\otimes \cdots \otimes F^{I_{M}}$ , where $I_{1}\geq I_{2}\geq \cdots \geq I_{M}$ , is called **unbalanced** whenever

$I_{1}>1+\prod _{m=2}^{M}I_{m}-\sum _{m=2}^{M}(I_{m}-1),$

and it is called **balanced** otherwise.

#### Unbalanced tensor spaces

When the first factor is very large with respect to the other factors in the tensor product, then the tensor space essentially behaves as a matrix space. The generic rank of tensors living in an unbalanced tensor spaces is known to equal

$r(I_{1},\ldots ,I_{M})=\min \left\{I_{1},\prod _{m=2}^{M}I_{m}\right\}$

almost everywhere. More precisely, the rank of every tensor in an unbalanced tensor space $F^{I_{1}\times \cdots \times I_{M}}\setminus Z$ , where Z is some indeterminate closed set in the Zariski topology, equals the above value.

#### Balanced tensor spaces

The **expected** generic rank of tensors living in a balanced tensor space is equal to

$r_{E}(I_{1},\ldots ,I_{M})=\left\lceil {\frac {\Pi }{\Sigma +1}}\right\rceil$

almost everywhere for complex tensors and on a Euclidean-open set for real tensors, where

$\Pi =\prod _{m=1}^{M}I_{m}\quad {\text{and}}\quad \Sigma =\sum _{m=1}^{M}(I_{m}-1).$

More precisely, the rank of every tensor in $\mathbb {C} ^{I_{1}\times \cdots \times I_{M}}\setminus Z$ , where Z is some indeterminate closed set in the Zariski topology, is expected to equal the above value. For real tensors, $r_{E}(I_{1},\ldots ,I_{M})$ is the least rank that is expected to occur on a set of positive Euclidean measure. The value $r_{E}(I_{1},\ldots ,I_{M})$ is often referred to as the **expected generic rank** of the tensor space $F^{I_{1}\times \cdots \times I_{M}}$ because it is only conjecturally correct. It is known that the true generic rank always satisfies

$r(I_{1},\ldots ,I_{M})\geq r_{E}(I_{1},\ldots ,I_{M}).$

The **Abo–Ottaviani–Peterson conjecture** states that equality is expected, i.e., $r(I_{1},\ldots ,I_{M})=r_{E}(I_{1},\ldots ,I_{M})$ , with the following exceptional cases:

- $F^{(2m+1)\times (2m+1)\times 3}{\text{ with }}m=1,2,\ldots$
- $F^{(m+1)\times (m+1)\times 2\times 2}{\text{ with }}m=2,3,\ldots$

In each of these exceptional cases, the generic rank is known to be $r(I_{1},\ldots ,I_{m},\ldots ,I_{M})=r_{E}(I_{1},\ldots ,I_{M})+1$ . Note that while the set of tensors of rank 3 in $F^{2\times 2\times 2\times 2}$ is defective (13 and not the expected 14), the generic rank in that space is still the expected one, 4. Similarly, the set of tensors of rank 5 in $F^{4\times 4\times 3}$ is defective (44 and not the expected 45), but the generic rank in that space is still the expected 6.

The AOP conjecture has been proved completely in a number of special cases. Lickteig showed already in 1985 that $r(n,n,n)=r_{E}(n,n,n)$ , provided that $n\neq 3$ . In 2011, a major breakthrough was established by Catalisano, Geramita, and Gimigliano who proved that the expected dimension of the set of rank s tensors of format $2\times 2\times \cdots \times 2$ is the expected one except for rank 3 tensors in the 4 factor case, yet the expected rank in that case is still 4. As a consequence, $r(2,2,\ldots ,2)=r_{E}(2,2,\ldots ,2)$ for all binary tensors.

### Maximum rank

The **maximum rank** that can be admitted by any of the tensors in a tensor space is unknown in general; even a conjecture about this maximum rank is missing. Presently, the best general upper bound states that the maximum rank $r_{\mbox{max}}(I_{1},\ldots ,I_{M})$ of $F^{I_{1}}\otimes \cdots \otimes F^{I_{M}}$ , where $I_{1}\geq I_{2}\geq \cdots \geq I_{M}$ , satisfies

$r_{\mbox{max}}(I_{1},\ldots ,I_{M})\leq \min \left\{\prod _{m=2}^{M}I_{m},2\cdot r(I_{1},\ldots ,I_{M})\right\},$

where $r(I_{1},\ldots ,I_{M})$ is the (least) *generic rank* of $F^{I_{1}}\otimes \cdots \otimes F^{I_{M}}$ . It is well known that the foregoing inequality may be strict. For instance, the generic rank of tensors in $\mathbb {R} ^{2\times 2\times 2}$ is two, so that the above bound yields $r_{\mbox{max}}(2,2,2)\leq 4$ , while it is known that the maximum rank equals 3.

### Border rank

A rank- s tensor ${\mathcal {A}}$ is called a **border tensor** if there exists a sequence of tensors of rank at most $r<s$ whose limit is ${\mathcal {A}}$ . If r is the least value for which such a convergent sequence exists, then it is called the **border rank** of ${\mathcal {A}}$ . For order-2 tensors, i.e., matrices, rank and border rank *always* coincide, however, for tensors of order $\geq 3$ they may differ. Border tensors were first studied in the context of fast *approximate* matrix multiplication algorithms by Bini, Lotti, and Romani in 1980.

A classic example of a border tensor is the rank-3 tensor

${\mathcal {A}}=\mathbf {u} \otimes \mathbf {u} \otimes \mathbf {v} +\mathbf {u} \otimes \mathbf {v} \otimes \mathbf {u} +\mathbf {v} \otimes \mathbf {u} \otimes \mathbf {u} ,\quad {\text{with }}\|\mathbf {u} \|=\|\mathbf {v} \|=1{\text{ and }}\langle \mathbf {u} ,\mathbf {v} \rangle \neq 1.$

It can be approximated arbitrarily well by the following sequence of rank-2 tensors

${\begin{aligned}{\mathcal {A}}_{m}&=m\left(\mathbf {u} +{\frac {1}{m}}\mathbf {v} \right)\otimes \left(\mathbf {u} +{\frac {1}{m}}\mathbf {v} \right)\otimes \left(\mathbf {u} +{\frac {1}{m}}\mathbf {v} \right)-m\mathbf {u} \otimes \mathbf {u} \otimes \mathbf {u} \\&=\mathbf {u} \otimes \mathbf {u} \otimes \mathbf {v} +\mathbf {u} \otimes \mathbf {v} \otimes \mathbf {u} +\mathbf {v} \otimes \mathbf {u} \otimes \mathbf {u} +{\frac {1}{m}}(\mathbf {u} \otimes \mathbf {v} \otimes \mathbf {v} +\mathbf {v} \otimes \mathbf {u} \otimes \mathbf {v} +\mathbf {v} \otimes \mathbf {v} \otimes \mathbf {u} )+{\frac {1}{m^{2}}}\mathbf {v} \otimes \mathbf {v} \otimes \mathbf {v} \end{aligned}}$

as $m\to \infty$ . Therefore, its border rank is 2, which is strictly less than its rank. When the two vectors are orthogonal, this example is also known as a W state.

## Properties

### Identifiability

It follows from the definition of a pure tensor that ${\mathcal {A}}=\mathbf {a} _{1}\otimes \mathbf {a} _{2}\otimes \cdots \otimes \mathbf {a} _{M}=\mathbf {b} _{1}\otimes \mathbf {b} _{2}\otimes \cdots \otimes \mathbf {b} _{M}$ if and only if there exist $\lambda _{k}$ such that $\lambda _{1}\lambda _{2}\cdots \lambda _{M}=1$ and $\mathbf {a} _{m}=\lambda _{m}\mathbf {b} _{m}$ for all *m*. For this reason, the parameters $\{\mathbf {a} _{m}\}_{m=1}^{M}$ of a rank-1 tensor ${\mathcal {A}}$ are called identifiable or essentially unique. A rank- r tensor ${\mathcal {A}}\in F^{I_{1}}\otimes F^{I_{2}}\otimes \cdots \otimes F^{I_{M}}$ is called **identifiable** if every of its tensor rank decompositions is the sum of the same set of r distinct tensors $\{{\mathcal {A}}_{1},{\mathcal {A}}_{2},\ldots ,{\mathcal {A}}_{r}\}$ where the ${\mathcal {A}}_{i}$ 's are of rank 1. An identifiable rank- r thus has only one essentially unique decomposition ${\mathcal {A}}=\sum _{i=1}^{r}{\mathcal {A}}_{i},$ and all $r!$ tensor rank decompositions of ${\mathcal {A}}$ can be obtained by permuting the order of the summands. Observe that in a tensor rank decomposition all the ${\mathcal {A}}_{i}$ 's are distinct, for otherwise the rank of ${\mathcal {A}}$ would be at most $r-1$ .

#### Generic identifiability

Order-2 tensors in $F^{I_{1}}\otimes F^{I_{2}}\simeq F^{I_{1}\times I_{2}}$ , i.e., matrices, are not identifiable for $r>1$ . This follows essentially from the observation ${\mathcal {A}}=\sum _{i=1}^{r}\mathbf {a} _{i}\otimes \mathbf {b} _{i}=\sum _{i=1}^{r}\mathbf {a} _{i}\mathbf {b} _{i}^{T}=AB^{T}=(AX^{-1})(BX^{T})^{T}=\sum _{i=1}^{r}\mathbf {c} _{i}\mathbf {d} _{i}^{T}=\sum _{i=1}^{r}\mathbf {c} _{i}\otimes \mathbf {d} _{i},$ where $X\in \mathrm {GL} _{r}(F)$ is an invertible $r\times r$ matrix, $A=[\mathbf {a} _{i}]_{i=1}^{r}$ , $B=[\mathbf {b} _{i}]_{i=1}^{r}$ , $AX^{-1}=[\mathbf {c} _{i}]_{i=1}^{r}$ and $BX^{T}=[\mathbf {d} _{i}]_{i=1}^{r}$ . It can be shown that for every $X\in \mathrm {GL} _{n}(F)\setminus Z$ , where Z is a closed set in the Zariski topology, the decomposition on the right-hand side is a sum of a different set of rank-1 tensors than the decomposition on the left-hand side, entailing that order-2 tensors of rank $r>1$ are generically not identifiable.

The situation changes completely for higher-order tensors in $F^{I_{1}}\otimes F^{I_{2}}\otimes \cdots \otimes F^{I_{M}}$ with $M>2$ and all $I_{m}\geq 2$ . For simplicity in notation, assume without loss of generality that the factors are ordered such that $I_{1}\geq I_{2}\geq \cdots \geq I_{M}\geq 2$ . Let $S_{r}\subset F^{I_{1}}\otimes \cdots F^{I_{m}}\otimes \cdots \otimes F^{I_{M}}$ denote the set of tensors of rank bounded by r . Then, the following statement was proved to be correct using a computer-assisted proof for all spaces of dimension $\Pi <15000$ , and it is conjectured to be valid in general:

There exists a closed set $Z_{r}$ in the Zariski topology such that *every tensor* ${\mathcal {A}}\in S_{r}\setminus Z_{r}$ *is identifiable* ( $S_{r}$ is called **generically identifiable** in this case), unless either one of the following exceptional cases holds:

1. The rank is too large: $r>r_{E}(I_{1},I_{2},\ldots ,I_{M})$ ;
2. The space is identifiability-unbalanced, i.e., ${\textstyle I_{1}>\prod _{m=2}^{M}i_{m}-\sum _{m=2}^{M}(I_{m}-1)}$ , and the rank is too large: ${\textstyle r\geq \prod _{m=2}^{M}I_{m}-\sum _{m=2}^{M}(I_{m}-1)}$ ;
3. The space is the defective case $F^{4}\otimes F^{4}\otimes F^{3}$ and the rank is $r=5$ ;
4. The space is the defective case $F^{n}\otimes F^{n}\otimes F^{2}\otimes F^{2}$ , where $n\geq 2$ , and the rank is $r=2n-1$ ;
5. The space is $F^{4}\otimes F^{4}\otimes F^{4}$ and the rank is $r=6$ ;
6. The space is $F^{6}\otimes F^{6}\otimes F^{3}$ and the rank is $r=8$ ; or
7. The space is $F^{2}\otimes F^{2}\otimes F^{2}\otimes F^{2}\otimes F^{2}$ and the rank is $r=5$ .
8. The space is perfect, i.e., ${\textstyle r_{E}(I_{1},I_{2},\ldots ,I_{M})={\frac {\Pi }{\Sigma +1}}}$ is an integer, and the rank is ${\textstyle r=r_{E}(I_{1},I_{2},\ldots ,I_{M})}$ .

In these exceptional cases, the generic (and also minimum) number of *complex* decompositions is

- proved to be $\infty$ in the first 4 cases;
- proved to be two in case 5;
- expected to be six in case 6;
- proved to be two in case 7; and
- expected to be at least two in case 8 with exception of the two identifiable cases $F^{5}\otimes F^{4}\otimes F^{3}$ and $F^{3}\otimes F^{2}\otimes F^{2}\otimes F^{2}$ .

In summary, the generic tensor of order $M>2$ and rank ${\textstyle r<{\frac {\Pi }{\Sigma +1}}}$ that is not identifiability-unbalanced is expected to be identifiable (modulo the exceptional cases in small spaces).

### Ill-posedness of the standard approximation problem

The rank approximation problem asks for the rank- r decomposition closest (in the usual Euclidean topology) to some rank- s tensor ${\mathcal {A}}$ , where $r<s$ . That is, one seeks to solve

$\min _{\mathbf {a} _{i}^{m}\in F^{I_{m}}}\left\|{\mathcal {A}}-\sum _{i=1}^{r}\mathbf {a} _{i}^{1}\otimes \mathbf {a} _{i}^{2}\otimes \cdots \otimes \mathbf {a} _{i}^{M}\right\|_{F},$

where $\|\cdot \|_{F}$ is the Frobenius norm.

It was shown in a 2008 paper by de Silva and Lim that the above standard approximation problem may be *ill-posed*. A solution to aforementioned problem may sometimes not exist because the set over which one optimizes is not closed. As such, a minimizer may not exist, even though an infimum would exist. In particular, it is known that certain so-called *border tensors* may be approximated arbitrarily well by a sequence of tensor of rank at most r , even though the limit of the sequence converges to a tensor of rank strictly higher than r . The rank-3 tensor

${\mathcal {A}}=\mathbf {u} \otimes \mathbf {u} \otimes \mathbf {v} +\mathbf {u} \otimes \mathbf {v} \otimes \mathbf {u} +\mathbf {v} \otimes \mathbf {u} \otimes \mathbf {u} ,\quad {\text{with }}\|\mathbf {u} \|=\|\mathbf {v} \|=1{\text{ and }}\langle \mathbf {u} ,\mathbf {v} \rangle \neq 1$

can be approximated arbitrarily well by the following sequence of rank-2 tensors

${\mathcal {A}}_{n}=n\left(\mathbf {u} +{\frac {1}{n}}\mathbf {v} \right)\otimes \left(\mathbf {u} +{\frac {1}{n}}\mathbf {v} \right)\otimes \left(\mathbf {u} +{\frac {1}{n}}\mathbf {v} \right)-n\mathbf {u} \otimes \mathbf {u} \otimes \mathbf {u}$

as $n\to \infty$ . This example neatly illustrates the general principle that a sequence of rank- r tensors that converges to a tensor of strictly higher rank needs to admit at least two individual rank-1 terms whose norms become unbounded. Stated formally, whenever a sequence

${\mathcal {A}}_{n}=\sum _{i=1}^{r}\mathbf {a} _{i,n}^{1}\otimes \mathbf {a} _{i,n}^{2}\otimes \cdots \otimes \mathbf {a} _{i,n}^{M}$

has the property that ${\mathcal {A}}_{n}\to {\mathcal {A}}$ (in the Euclidean topology) as $n\to \infty$ , then there should exist at least $1\leq i\neq j\leq r$ such that

$\|\mathbf {a} _{i,n}^{1}\otimes \mathbf {a} _{i,n}^{2}\otimes \cdots \otimes \mathbf {a} _{i,n}^{M}\|_{F}\to \infty {\text{ and }}\|\mathbf {a} _{j,n}^{1}\otimes \mathbf {a} _{j,n}^{2}\otimes \cdots \otimes \mathbf {a} _{j,n}^{M}\|_{F}\to \infty$

as $n\to \infty$ . This phenomenon is often encountered when attempting to approximate a tensor using numerical optimization algorithms. It is sometimes called the problem of *diverging components*. It was, in addition, shown that a random low-rank tensor over the reals may not admit a rank-2 approximation with positive probability, leading to the understanding that the ill-posedness problem is an important consideration when employing the tensor rank decomposition.

A common partial solution to the ill-posedness problem consists of imposing an additional inequality constraint that bounds the norm of the individual rank-1 terms by some constant. Other constraints that result in a closed set, and, thus, well-posed optimization problem, include imposing positivity or a bounded inner product strictly less than unity between the rank-1 terms appearing in the sought decomposition.

## Calculating the CPD

Alternating algorithms:

- alternating least squares (ALS)
- alternating slice-wise diagonalisation (ASD)

Direct algorithms:

- pencil-based algorithms
- moment-based algorithms

General optimization algorithms:

- simultaneous diagonalization (SD)
- simultaneous generalized Schur decomposition (SGSD)
- Levenberg–Marquardt (LM)
- nonlinear conjugate gradient (NCG)
- limited memory BFGS (L-BFGS)

Eigenvalue algorithms:

- Power iteration

Factorization Machines:

- Support Vector Machines (SVMs) and factorization

Bayesian factorizations/Sampling/Markov Chain Monte Carlo (MCMC):

- Bayesian Probabilistic Tensor Factorization (Gibbs sampling)

Deep learning/Neural Networks (Gradient-based learning):

- LFM
- Semantic Matching Energy Network (SME)
- Neural Tensor Networks
- Recurrent Graph Tensor Networks

General polynomial system solving algorithms:

- homotopy continuation

However, P Wiriyathammabhum and B Kijsirikul found that there are no optimal solving algorithms (all existing optimization methods cannot provide provably optimal solutions.) as they had created a score tensor and reranked the solutions using just a greedy stepwise selection which can give significantly better solutions, at least on nd-PCA, nd-FLD/LDA, and so on (CPD and Tucker variants). The hypothesis is fixing all the other n-1th parameters while optimizing the nth parameter is always (provably) suboptimal. MS Mahanta and KN Plataniotis proposed another spectral clustering solution which further provides better solutions.

## Applications

In machine learning, the CP-decomposition is the central ingredient in learning probabilistic latent variables models via the technique of moment-matching. For example, consider the multi-view model which is a probabilistic latent variable model. In this model, the generation of samples are posited as follows: there exists a hidden random variable that is not observed directly, given which, there are several conditionally independent random variables known as the different "views" of the hidden variable. For example, assume there are three views $x_{1},x_{2},x_{3}$ of a k -state categorical hidden variable h . Then the empirical third moment of this latent variable model $E[x_{1}\otimes x_{2}\otimes x_{3}]$ is a rank 3 tensor and can be decomposed as: $E[x_{1}\otimes x_{2}\otimes x_{3}]=\sum _{i=1}^{k}Pr(h=i)E[x_{1}|h=i]\otimes E[x_{2}|h=i]\otimes E[x_{3}|h=i]$ .

In applications such as topic modeling, this can be interpreted as the co-occurrence of words in a document. Then the coefficients in the decomposition of this empirical moment tensor can be interpreted as the probability of choosing a specific topic and each column of the factor matrix $E[x|h=i]$ corresponds to probabilities of words in the vocabulary in the corresponding topic.
