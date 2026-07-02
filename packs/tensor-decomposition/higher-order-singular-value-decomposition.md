---
title: "Higher-order singular value decomposition"
source: https://en.wikipedia.org/wiki/Higher-order_singular_value_decomposition
domain: tensor-decomposition
license: CC-BY-SA-4.0
tags: tensor decomposition, tucker decomposition, canonical polyadic decomposition, tensor rank
fetched: 2026-07-02
---

# Higher-order singular value decomposition

In multilinear algebra, the **higher-order singular value decomposition** (**HOSVD**) is a misnomer. There does not exist a single tensor decomposition that retains all the defining properties of the matrix SVD. The matrix SVD simultaneously yields a

- *rank-𝑅* decomposition and
- orthonormal subspaces for the row and column spaces.

These properties are not realized within a single algorithm for higher-order tensors, but are instead realized by two distinct algorithmic developments and represent two distinct research directions. Harshman, as well as, the team of Carol and Chang proposed Canonical polyadic decomposition (CPD), which is a variant of the tensor rank decomposition, in which a tensor is approximated as a sum of *K rank-1* tensors for a user-specified *K*. L. R. Tucker proposed a strategy for computing orthonormal subspaces for third order tensors. Aspects of these algorithms can be traced as far back as F. L. Hitchcock in 1928.

De Lathauwer *et al.* introduced clarity to the Tucker concepts, while Vasilescu and Terzopoulos introduced algorithmic clarity. Vasilescu and Terzopoulos introduced the **M-mode SVD**, which is the classic algorithm that is currently referred in the literature as the **Tucker** or the **HOSVD**. The Tucker approach and De Lathauwer's implementation are both sequential and rely on iterative procedures such as gradient descent or the power method. By contrast, the M-mode SVD provides a closed-form solution that can be executed sequentially and is well-suited for parallel computation.

This misattribution has had lasting impact on the scholarly record, obscuring the original source of a widely adopted algorithm, and complicating efforts to trace its development, reproduce results, and recognizing the respective contributions of different research efforts.

The term **M-mode SVD** accurately reflects the algorithm employed. It captures the actual computation, a set of SVDs on mode-flattenings without making assumptions about the structure of the core tensor or implying a rank decomposition.

Robust and L1-norm-based variants of this decomposition framework have since been proposed.

## Definition

For the purpose of this article, the abstract tensor ${\mathcal {A}}$ is assumed to be given in coordinates with respect to some basis as a M-way array, also denoted by ${\mathcal {A}}\in \mathbb {C} ^{I_{1}\times I_{2}\cdots \times \cdots I_{m}\cdots \times I_{M}}$ , where *M* is the number of modes and the order of the tensor. $\mathbb {C}$ is the complex numbers and it includes both the real numbers $\mathbb {R}$ and the pure imaginary numbers.

Let ${\mathcal {A}}_{[m]}\in \mathbb {C} ^{I_{m}\times (I_{1}I_{2}\cdots I_{m-1}I_{m+1}\cdots I_{M})}$ denote the mode-*m* flattening of ${\mathcal {A}}$ , so that the left index of ${\mathcal {A}}_{[m]}$ corresponds to the m 'th index ${\mathcal {A}}$ and the right index of ${\mathcal {A}}_{[m]}$ corresponds to all other indices of ${\mathcal {A}}$ combined. Let ${\bf {U}}_{m}\in \mathbb {C} ^{I_{m}\times I_{m}}$ be a unitary matrix containing a basis of the left singular vectors of the ${\mathcal {A}}_{[m]}$ such that the *j*th column $\mathbf {u} _{j}$ of ${\bf {U}}_{m}$ corresponds to the *j*th largest singular value of ${\mathcal {A}}_{[m]}$ . Observe that the **mode/factor matrix** ${\bf {U}}_{m}$ does not depend on the particular on the specific definition of the mode *m* flattening. By the properties of the multilinear multiplication, we have ${\begin{array}{rcl}{\mathcal {A}}&=&{\mathcal {A}}\times ({\bf {I}},{\bf {I}},\ldots ,{\bf {I}})\\&=&{\mathcal {A}}\times ({\bf {U}}_{1}{\bf {U}}_{1}^{H},{\bf {U}}_{2}{\bf {U}}_{2}^{H},\ldots ,{\bf {U}}_{M}{\bf {U}}_{M}^{H})\\&=&\left({\mathcal {A}}\times ({\bf {U}}_{1}^{H},{\bf {U}}_{2}^{H},\ldots ,{\bf {U}}_{M}^{H})\right)\times ({\bf {U}}_{1},{\bf {U}}_{2},\ldots ,{\bf {U}}_{M}),\end{array}}$ where $\cdot ^{H}$ denotes the conjugate transpose. The second equality is because the ${\bf {U}}_{m}$ 's are unitary matrices. Define now the **core tensor** ${\mathcal {S}}:={\mathcal {A}}\times ({\bf {U}}_{1}^{H},{\bf {U}}_{2}^{H},\ldots ,{\bf {U}}_{M}^{H}).$ Then, the M-mode SVD(HOSVD) of ${\mathcal {A}}$ is the decomposition ${\mathcal {A}}={\mathcal {S}}\times ({\bf {U}}_{1},{\bf {U}}_{2},\ldots ,{\bf {U}}_{M}).$ The above construction shows that every tensor has a M-mode SVD(HOSVD).

## Compact M-mode SVD (mis-identified as Tucker or HOSVD)

As in the case of the compact singular value decomposition of a matrix, where the rows and columns corresponding to vanishing singular values are dropped, it is also possible to consider a **compact M-mode SVD**(HOSVD), which is very useful in applications.

Assume that ${\bf {U}}_{m}\in \mathbb {C} ^{I_{m}\times R_{m}}$ is a matrix with unitary columns containing a basis of the left singular vectors corresponding to the nonzero singular values of the standard factor-*m* flattening ${\mathcal {A}}_{[m]}$ of ${\mathcal {A}}$ . Let the columns of ${\bf {U}}_{m}$ be sorted such that the $r_{m}$ th column ${\bf {u}}_{r_{m}}$ of ${\bf {U}}_{m}$ corresponds to the *$r_{m}$*th largest nonzero singular value of ${\mathcal {A}}_{[m]}$ . Since the columns of ${\bf {U}}_{m}$ form a basis for the image of ${\mathcal {A}}_{[m]}$ , we have ${\mathcal {A}}_{[m]}={\bf {U}}_{m}{\bf {U}}_{m}^{H}{\mathcal {A}}_{[m]}={\bigl (}{\mathcal {A}}\times _{m}({\bf {U}}_{m}{\bf {U}}_{m}^{H}){\bigr )}_{[m]},$ where the first equality is due to the properties of orthogonal projections (in the Hermitian inner product) and the last equality is due to the properties of multilinear multiplication. As flattenings are bijective maps and the above formula is valid for all $m=1,2,\ldots ,m,\ldots ,M$ , we find as before that ${\begin{array}{rcl}{\mathcal {A}}&=&{\mathcal {A}}\times ({\bf {U}}_{1}{\bf {U}}_{1}^{H},{\bf {U}}_{2}{\bf {U}}_{2}^{H},\ldots ,{\bf {U}}_{M}{\bf {U}}_{M}^{H})\\&=&\left({\mathcal {A}}\times ({\bf {U}}_{1}^{H},{\bf {U}}_{2}^{H},\ldots ,{\bf {U}}_{M}^{H})\right)\times ({\bf {U}}_{1},{\bf {U}}_{2},\ldots ,{\bf {U}}_{M})\\&=&{\mathcal {S}}\times ({\bf {U}}_{1},{\bf {U}}_{2},\ldots ,{\bf {U}}_{M}),\end{array}}$ where the core tensor ${\mathcal {S}}$ is now of size $R_{1}\times R_{2}\times \cdots \times R_{M}$ .

## Multilinear rank

The **multilinear rank** of ${\mathcal {A}}$ is denoted with rank- $(R_{1},R_{2},\ldots ,R_{M})$ . The multilinear rank is a tuple in $\mathbb {N} ^{M}$ where $R_{m}:=\mathrm {rank} ({\mathcal {A}}_{[m]})$ . Not all tuples in $\mathbb {N} ^{M}$ are multilinear ranks. The multilinear ranks are bounded by $1\leq R_{m}\leq I_{m}$ and it satisfy the constraint ${\textstyle R_{m}\leq \prod _{i\neq m}R_{i}}$ must hold.

The compact M-mode SVD(HOSVD) is a rank-revealing decomposition in the sense that the dimensions of its core tensor correspond with the components of the multilinear rank of the tensor.

## Interpretation

The following geometric interpretation is valid for both the full and compact M-mode SVD(HOSVD). Let $(R_{1},R_{2},\ldots ,R_{M})$ be the multilinear rank of the tensor ${\mathcal {A}}$ . Since ${\mathcal {S}}\in {\mathbb {C} }^{R_{1}\times R_{2}\times \cdots \times R_{M}}$ is a multidimensional array, we can expand it as follows ${\mathcal {S}}=\sum _{r_{1}=1}^{R_{1}}\sum _{r_{2}=1}^{R_{2}}\cdots \sum _{r_{M}=1}^{R_{M}}s_{r_{1},r_{2},\ldots ,r_{M}}\mathbf {e} _{r_{1}}\otimes \mathbf {e} _{r_{2}}\otimes \cdots \otimes \mathbf {e} _{r_{M}},$ where $\mathbf {e} _{r_{m}}$ is the $r_{m}$ th standard basis vector of ${\mathbb {C} }^{I_{m}}$ . By definition of the multilinear multiplication, it holds that ${\mathcal {A}}=\sum _{r_{1}=1}^{R_{1}}\sum _{r_{2}=1}^{R_{2}}\cdots \sum _{r_{M}=1}^{R_{M}}s_{r_{1},r_{2},\ldots ,r_{M}}\mathbf {u} _{r_{1}}\otimes \mathbf {u} _{r_{2}}\otimes \cdots \otimes \mathbf {u} _{r_{M}},$ where the $\mathbf {u} _{r_{m}}$ are the columns of ${\bf {U}}_{m}\in {\mathbb {C} }^{I_{m}\times R_{m}}$ . It is easy to verify that $B=\{\mathbf {u} _{r_{1}}\otimes \mathbf {u} _{r_{2}}\otimes \cdots \otimes \mathbf {u} _{r_{M}}\}_{r_{1},r_{2},\ldots ,r_{M}}$ is an orthonormal set of tensors. This means that the M-mode SVD(HOSVD) can be interpreted as a way to express the tensor ${\mathcal {A}}$ with respect to a specifically chosen orthonormal basis B with the coefficients given as the multidimensional array ${\mathcal {S}}$ .

## Computation

Let ${\mathcal {A}}\in {\mathbb {C} }^{I_{1}\times I_{2}\times \cdots \times I_{M}}$ be a tensor with a rank- $(R_{1},R_{2},\ldots ,R_{M})$ , where $\mathbb {C}$ contains the reals $\mathbb {R}$ as a subset.

### Classic computation

While De Lathauwer et al. clarified Tucker's concepts through two influential papers, Vasilescu and Terzopoulos provided algorithmic clarity. The Tucker algorithm and De Lathauwer *et al.* companion algorithm are sequential, relying on iterative methods such as gradient descent or the power method. In contrast, the **M-mode SVD** is computes the othonormal subspaces in closed-form that can be executed sequentially, but it is also well-suited for parallel computation.

### M-mode SVD (also referred to as HOSVD or Tucker)

What is commonly referred to as the HOSVD or Tucker was developed by Vasilescu and Terzopoulos under the name M-mode SVD.

- For $m=1,\ldots ,M$ , do the following:

1. Construct the mode-*m* flattening ${\mathcal {A}}_{[m]}$ ;
2. Compute the (compact) singular value decomposition ${\mathcal {A}}_{[m]}={\bf {U}}_{m}{\bf {\Sigma }}_{m}{\bf {V}}_{m}^{T}$ , and store the left singular vectors ${\bf {U}}\in \mathbb {C} ^{I_{m}\times R_{m}}$ ;

- Compute the core tensor ${\mathcal {S}}$ via the mode-m product ${\mathcal {S}}={\mathcal {A}}\times _{1}{\bf {U}}_{1}^{H}\times _{2}{\bf {U}}_{2}^{H}\ldots \times _{m}{\bf {U}}_{m}^{H}\ldots \times _{M}{\bf {U}}_{M}^{H}$

### Interlacing computation

A strategy that is significantly faster when some or all $R_{m}\ll I_{m}$ consists of interlacing the computation of the core tensor and the factor matrices, as follows:

- Set ${\mathcal {A}}^{0}={\mathcal {A}}$ ;
- For $m=1,2\ldots ,M$ perform the following:
  1. Construct the standard mode-*m* flattening ${\mathcal {A}}_{[m]}^{m-1}$ ;
  2. Compute the (compact) singular value decomposition ${\mathcal {A}}_{[m]}^{m-1}=U_{m}\Sigma _{m}V_{m}^{T}$ , and store the left singular vectors $U_{m}\in F^{I_{m}\times R_{m}}$ ;
  3. Set ${\mathcal {A}}^{m}=U_{m}^{H}\times _{m}{\mathcal {A}}^{m-1}$ , or, equivalently, ${\mathcal {A}}_{[m]}^{m}=\Sigma _{m}V_{m}^{T}$ .

### In-place computation

The M-mode SVD (HOSVD) can be computed *in-place* via the Fused In-place Sequentially Truncated Higher Order Singular Value Decomposition (FIST-HOSVD) algorithm by overwriting the original tensor by the M-mode SVD (HOSVD) core tensor, significantly reducing the memory consumption of computing HOSVD.

## Approximation

In applications, such as those mentioned below, a common problem consists of approximating a given tensor ${\mathcal {A}}\in \mathbb {C} ^{I_{1}\times I_{2}\times \cdots \times I_{m}\cdots \times I_{M}}$ by one with a reduced multilinear rank. Formally, if the multilinear rank of ${\mathcal {A}}$ is denoted by $\mathrm {rank-} (R_{1},R_{2},\ldots ,R_{m},\ldots ,R_{M})$ , then computing the optimal ${\mathcal {\bar {A}}}$ that approximates ${\mathcal {A}}$ for a given reduced $\mathrm {rank-} ({\bar {R}}_{1},{\bar {R}}_{2},\ldots ,{\bar {R}}_{m},\ldots ,{\bar {R}}_{M})$ is a nonlinear non-convex $\ell _{2}$ -optimization problem $\min _{{\mathcal {\bar {A}}}\in \mathbb {C} ^{I_{1}\times I_{2}\times \cdots \times I_{M}}}{\frac {1}{2}}\|{\mathcal {A}}-{\mathcal {\bar {A}}}\|_{F}^{2}\quad {\text{s.t.}}\quad \mathrm {rank-} ({\bar {R}}_{1},{\bar {R}}_{2},\ldots ,{\bar {R}}_{M}),$ where $({\bar {R}}_{1},{\bar {R}}_{2},\ldots ,{\bar {R}}_{M})\in \mathbb {N} ^{M}$ is the reduced multilinear rank with $1\leq {\bar {R}}_{m}<R_{m}\leq I_{m}$ , and the norm $\|.\|_{F}$ is the Frobenius norm.

A simple idea for trying to solve this optimization problem is to truncate the (compact) SVD in step 2 of either the classic or the interlaced computation. A **classically** **truncated M-mode SVD/HOSVD** is obtained by replacing step 2 in the classic computation by

- Compute a rank- ${\bar {R}}_{m}$ truncated SVD ${\mathcal {A}}_{[m]}\approx U_{m}\Sigma _{m}V_{m}^{T}$ , and store the top ${\bar {R}}_{m}$ left singular vectors $U_{m}\in F^{I_{m}\times {\bar {R}}_{m}}$ ;

while a **sequentially truncated M-mode SVD (HOSVD)** (or **successively truncated M-mode SVD(HOSVD)**) is obtained by replacing step 2 in the interlaced computation by

- Compute a rank- ${\bar {R}}_{m}$ truncated SVD ${\mathcal {A}}_{[m]}^{m-1}\approx U_{m}\Sigma _{m}V_{m}^{T}$ , and store the top ${\bar {R}}_{m}$ left singular vectors $U_{m}\in F^{I_{m}\times {\bar {R}}_{m}}$ . Unfortunately, truncation does not result in an optimal solution for the best low multilinear rank optimization problem,. However, both the classically and interleaved truncated M-mode SVD/HOSVD result in a **quasi-optimal** solution: if ${\mathcal {\bar {A}}}_{t}$ denotes the classically or sequentially truncated M-mode SVD(HOSVD) and ${\mathcal {\bar {A}}}^{*}$ denotes the optimal solution to the best low multilinear rank approximation problem, then $\|{\mathcal {A}}-{\mathcal {\bar {A}}}_{t}\|_{F}\leq {\sqrt {M}}\|{\mathcal {A}}-{\mathcal {\bar {A}}}^{*}\|_{F};$ in practice this means that if there exists an optimal solution with a small error, then a truncated M-mode SVD/HOSVD will for many intended purposes also yield a sufficiently good solution.

## Applications

The M-mode SVD (HOSVD/Tucker) is most commonly applied to the extraction of relevant information from multi-way arrays.

Starting in the early 2000s, Vasilescu addressed causal questions by reframing the data analysis, recognition and synthesis problems as multilinear tensor problems. The power of the tensor framework was showcased by decomposing and representing an image in terms of its causal factors of data formation, in the context of Human Motion Signatures for gait recognition, face recognition—TensorFaces and computer graphics—TensorTextures.

The M-mode SVD (HOSVD) has been successfully applied to signal processing and big data, e.g., in genomic signal processing. These applications also inspired a higher-order GSVD (HO GSVD) and a tensor GSVD.

A combination of M-mode SVD (HOSVD) and SVD also has been applied for real-time event detection from complex data streams (multivariate data with space and time dimensions) in disease surveillance.

It is also used in tensor product model transformation-based controller design.

The concept of M-mode SVD (HOSVD) was carried over to functions by Baranyi and Yam via the TP model transformation. This extension led to the definition of the M-mode SVD/HOSVD canonical form of tensor product functions and Linear Parameter Varying system models and to convex hull manipulation based control optimization theory, see TP model transformation in control theories.

M-mode SVD (HOSVD) was proposed to be applied to multi-way data analysis in an unsupervised manner and was successfully applied to in silico drug discovery from gene expression.

## Robust L1-norm variant

L1-Tucker is the L1-norm-based, robust variant of Tucker decomposition. L1-HOSVD is the analogous of M-mode SVD(HOSVD) for the solution to L1-Tucker.
