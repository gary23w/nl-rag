---
title: "Gamma matrices (part 2/2)"
source: https://en.wikipedia.org/wiki/Gamma_matrices
domain: clifford-algebra
license: CC-BY-SA-4.0
tags: clifford algebra, geometric algebra, spinor field, gamma matrices
fetched: 2026-07-02
part: 2/2
---

## Other representation-free properties

The gamma matrices are diagonalizable with eigenvalues $\pm 1$ for $\gamma ^{0}$ , and eigenvalues $\pm i$ for $\gamma ^{k}$ .

| Proof |
|---|
| This can be demonstrated for $\gamma ^{0}$ and follows similarly for $\gamma ^{i}$ . We can rewrite $(\gamma ^{0})^{2}=+1$ as $(\gamma ^{0}+1)(\gamma ^{0}-1)=0.$ By a well-known result in linear algebra, this means there is a basis in which $\gamma ^{0}$ is diagonal with eigenvalues $\{\pm 1\}$ . |

In particular, this implies that $\gamma ^{0}$ is simultaneously Hermitian and unitary, while the $\gamma ^{i}$ are simultaneously anti–Hermitian and unitary.

Further, the multiplicity of each eigenvalue is two.

| Proof |
|---|
| If v is an eigenvector of $\ \gamma ^{0}\ ,$ then $\ \gamma ^{1}v\$ is an eigenvector with the opposite eigenvalue. Then eigenvectors can be paired off if they are related by multiplication by $\ \gamma ^{1}~.$ Result follows similarly for $\ \gamma ^{i}~.$ |

More generally, if $\ \gamma ^{\mu }X_{\mu }\$ is not null, a similar result holds. For concreteness, we restrict to the positive norm case $\ \gamma ^{\mu }p_{\mu }=p\!\!\!/\$ with $\ p\cdot p=m^{2}>0~.$ The negative case follows similarly.

| Proof |
|---|
| It can be shown $p\!\!\!/^{2}=m^{2}\ ,$ so by the same argument as the first result, $\ p\!\!\!/\$ is diagonalizable with eigenvalues $\ \pm m~.$ We can adapt the argument for the second result slightly. We pick a non-null vector $\ q_{\mu }\$ which is orthogonal to $p_{\mu }~.$ Then eigenvectors can be paired off similarly if they are related by multiplication by $\ q\!\!\!/~.$ |

It follows that the solution space to $\ p\!\!\!/-m=0\$ (that is, the kernel of the left-hand side) has dimension 2. This means the solution space for plane wave solutions to Dirac's equation has dimension 2.

This result still holds for the massless Dirac equation. In other words, if $p_{\mu }$ null, then $p\!\!\!/$ has nullity 2.

| Proof |
|---|
| If $p_{\mu }$ null, then $p\!\!\!/p\!\!\!/=0.$ By generalized eigenvalue decomposition, this can be written in some basis as diagonal in $2\times 2$ Jordan blocks with eigenvalue 0, with either 0, 1, or 2 blocks, and other diagonal entries zero. It turns out to be the 2 block case. The zero case is not possible as if $\ \gamma ^{\mu }p_{\mu }=0\ ,$ by linear independence of the $\ \gamma ^{\mu }\$ we must have $\ p_{\mu }=0~.$ But null vectors are by definition non-zero. Consider $(q_{\mu })=(\|\mathbf {p} \|,-\mathbf {p} )$ and a zero-eigenvector v of $p\!\!\!/$ . Note $q_{\mu }$ is also null and satisfies $p\!\!\!/q\!\!\!/+q\!\!\!/p\!\!\!/=4\|\mathbf {p} \|.-(*)$ If $p\!\!\!/v=0$ , then it cannot simultaneously be a zero eigenvector of $q\!\!\!/$ by (*). Considering $q\!\!\!/v$ , if we apply $p\!\!\!/$ then we get $p\!\!\!/q\!\!\!/v=4\|\mathbf {p} \|v$ . Therefore, after a rescaling, v and $q\!\!\!/v$ give a $2\times 2$ Jordan block. This gives a pairing. There must be another zero eigenvector of $p\!\!\!/$ , which can be used to make the second Jordan block. There is also a pleasant structure to these pairs. If left arrows correspond to application of $p\!\!\!/$ , and right arrows to application of $q\!\!\!/$ , and v is a zero eigenvector of $p\!\!\!/$ , up to scalar factors we have $0\leftarrow v\leftrightarrow q\!\!\!/v\rightarrow 0$ . |


## Euclidean Dirac matrices

In quantum field theory one can Wick rotate the time axis to transit from Minkowski space to Euclidean space. This is particularly useful in some renormalization procedures as well as lattice gauge theory. In Euclidean space, there are two commonly used representations of Dirac matrices:

### Chiral representation

$\gamma ^{1,2,3}={\begin{pmatrix}0&i\sigma ^{1,2,3}\\-i\sigma ^{1,2,3}&0\end{pmatrix}},\quad \gamma ^{4}={\begin{pmatrix}0&I_{2}\\I_{2}&0\end{pmatrix}}$

Notice that the factors of i have been inserted in the spatial gamma matrices so that the Euclidean Clifford algebra

$\left\{\gamma ^{\mu },\gamma ^{\nu }\right\}=2\delta ^{\mu \nu }I_{4}$

will emerge. It is also worth noting that there are variants of this which insert instead $-i$ on one of the matrices, such as in lattice QCD codes which use the chiral basis.

In Euclidean space,

$\gamma _{\mathrm {M} }^{5}=i\left(\gamma ^{0}\gamma ^{1}\gamma ^{2}\gamma ^{3}\right)_{\mathrm {M} }={\tfrac {1}{i^{2}}}\left(\gamma ^{4}\gamma ^{1}\gamma ^{2}\gamma ^{3}\right)_{\mathrm {E} }=\left(\gamma ^{1}\gamma ^{2}\gamma ^{3}\gamma ^{4}\right)_{\mathrm {E} }=\gamma _{\mathrm {E} }^{5}~.$

Using the anti-commutator and noting that in Euclidean space $\left(\gamma ^{\mu }\right)^{\dagger }=\gamma ^{\mu }$ , one shows that

$\left(\gamma ^{5}\right)^{\dagger }=\gamma ^{5}$

In chiral basis in Euclidean space,

$\gamma ^{5}={\begin{pmatrix}-I_{2}&0\\0&I_{2}\end{pmatrix}}$

which is unchanged from its Minkowski version.

### Non-relativistic representation

$\gamma ^{1,2,3}={\begin{pmatrix}0&-i\sigma ^{1,2,3}\\i\sigma ^{1,2,3}&0\end{pmatrix}}\ ,\quad \gamma ^{4}={\begin{pmatrix}I_{2}&0\\0&-I_{2}\end{pmatrix}},\quad \gamma ^{5}={\begin{pmatrix}0&-I_{2}\\-I_{2}&0\end{pmatrix}}$
