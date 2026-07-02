---
title: "Minkowski's theorem"
source: https://en.wikipedia.org/wiki/Minkowski's_theorem
domain: algebraic-number-theory
license: CC-BY-SA-4.0
tags: algebraic number theory, ring of integers, ideal class group, dedekind domain
fetched: 2026-07-02
---

# Minkowski's theorem

In mathematics, **Minkowski's theorem** is the statement that every convex set in $\mathbb {R} ^{n}$ which is symmetric with respect to the origin and which has volume greater than $2^{n}$ contains a non-zero integer point (meaning a point in $\mathbb {Z} ^{n}$ that is not the origin). The theorem was proved by Hermann Minkowski in 1889 and became the foundation of the branch of number theory called the geometry of numbers. It can be extended from the integers to any lattice L and to any symmetric convex set with volume greater than $2^{n}d(L)$ , where $d(L)$ denotes the covolume of the lattice (the absolute value of the determinant of any of its bases).

## Formulation

Suppose that *L* is a lattice of determinant d(*L*) in the *n*-dimensional real vector space $\mathbb {R} ^{n}$ and *S* is a convex subset of $\mathbb {R} ^{n}$ that is symmetric with respect to the origin, meaning that if *x* is in *S* then −*x* is also in *S*. Minkowski's theorem states that if the volume of *S* is strictly greater than 2*n* d(*L*), then *S* must contain at least one lattice point other than the origin. (Since the set *S* is symmetric, it would then contain at least three lattice points: the origin 0 and a pair of points ± *x*, where *x* ∈ *L* \ 0.)

## Example

The simplest example of a lattice is the integer lattice $\mathbb {Z} ^{n}$ of all points with integer coefficients; its determinant is 1. For *n* = 2, the theorem claims that a convex figure in the Euclidean plane symmetric about the origin and with area greater than 4 encloses at least one lattice point in addition to the origin. The area bound is sharp: if *S* is the interior of the square with vertices (±1, ±1) then *S* is symmetric and convex, and has area 4, but the only lattice point it contains is the origin. This example, showing that the bound of the theorem is sharp, generalizes to hypercubes in every dimension *n*.

## Proof

The following argument proves Minkowski's theorem for the specific case of $L=\mathbb {Z} ^{2}.$

**Proof of the ${\textstyle \mathbb {Z} ^{2}}$ case:** Consider the map

$f:S\to \mathbb {R} ^{2}/2L,\qquad (x,y)\mapsto (x{\bmod {2}},y{\bmod {2}})$

Intuitively, this map cuts the plane into 2 by 2 squares, then stacks the squares on top of each other. Clearly *f* (*S*) has area less than or equal to 4, because this set lies within a 2 by 2 square. Assume for a contradiction that *f* could be injective, which means the pieces of *S* cut out by the squares stack up in a non-overlapping way. Because *f* is locally area-preserving, this non-overlapping property would make it area-preserving for all of *S*, so the area of *f* (*S*) would be the same as that of *S*, which is greater than 4. That is not the case, so the assumption must be false: *f* is not injective, meaning that there exist at least two distinct points *p*1, *p*2 in *S* that are mapped by *f* to the same point: *f* (*p*1) = *f* (*p*2).

Because of the way *f* was defined, the only way that *f* (*p*1) can equal *f* (*p*2) is for *p*2 to equal *p*1 + (2*i*, 2*j*) for some integers *i* and *j*, not both zero. That is, the coordinates of the two points differ by two even integers. Since *S* is symmetric about the origin, −*p*1 is also a point in *S*. Since *S* is convex, the line segment between −*p*1 and *p*2 lies entirely in *S*, and in particular the midpoint of that segment lies in *S*. In other words,

${\tfrac {1}{2}}\left(-p_{1}+p_{2}\right)={\tfrac {1}{2}}\left(-p_{1}+p_{1}+(2i,2j)\right)=(i,j)$

is a point in *S*. This point (*i*, *j*) is an integer point, and is not the origin since *i* and *j* are not both zero. Therefore, *S* contains a nonzero integer point.

**Remarks:**

- The argument above proves the theorem that any set of volume ${\textstyle >\!\det(L)}$ contains two distinct points that differ by a lattice vector. This is a special case of Blichfeldt's theorem.
- The argument above highlights that the term ${\textstyle 2^{n}\det(L)}$ is the covolume of the lattice ${\textstyle 2L}$ .
- To obtain a proof for general lattices, it suffices to prove Minkowski's theorem only for ${\textstyle \mathbb {Z} ^{n}}$ ; this is because every full-rank lattice can be written as ${\textstyle B\mathbb {Z} ^{n}}$ for some linear transformation ${\textstyle B}$ , and the properties of being convex and symmetric about the origin are preserved by linear transformations, while the covolume of ${\textstyle B\mathbb {Z} ^{n}}$ is ${\textstyle |\!\det(B)|}$ and volume of a body scales by exactly ${\textstyle {\frac {1}{\det(B)}}}$ under an application of ${\textstyle B^{-1}}$ .

## Applications

### Bounding the shortest vector

Minkowski's theorem gives an upper bound for the length of the shortest nonzero vector. This result has applications in lattice cryptography and number theory.

**Theorem (Minkowski's bound on the shortest vector):** Let ${\textstyle L}$ be a lattice. Then there is a ${\textstyle x\in L\setminus \{0\}}$ with ${\textstyle \|x\|_{\infty }\leq \left|\det(L)\right|^{1/n}}$ . In particular, by the standard comparison between ${\textstyle l_{2}}$ and ${\textstyle l_{\infty }}$ norms, ${\textstyle \|x\|_{2}\leq {\sqrt {n}}\,\left|\det(L)\right|^{1/n}}$ .

Proof

Let ${\textstyle l=\min\{\|x\|_{\infty }:x\in L\setminus \{0\}\}}$ , and set ${\textstyle C=\{y:\|y\|_{\infty }<l\}}$ . Then ${\textstyle {\text{vol}}(C)=(2l)^{n}}$ . If ${\textstyle (2l)^{n}>2^{n}|d(L)|}$ , then ${\textstyle C}$ contains a non-zero lattice point, which is a contradiction. Thus ${\textstyle l\leq |d(L)|^{1/n}}$ . Q.E.D.

**Remarks:**

- The constant in the ${\textstyle L^{2}}$ bound can be improved, for instance by taking the open ball of radius ${\textstyle <l}$ as ${\textstyle C}$ in the above argument. The optimal constant is known as the Hermite constant.
- The bound given by the theorem can be very loose, as can be seen by considering the lattice generated by ${\textstyle (1,0),(0,n)}$ . But it cannot be further improved in the sense that there exists a global constant c such that there exists an n -dimensional lattice L satisfying $\|x\|_{2}\geq c{\sqrt {n}}\cdot \left|\det(L)\right|^{1/n}$ for all $x\in L\setminus \{0\}$ . Furthermore, such lattice can be self-dual.
- Even though Minkowski's theorem guarantees a short lattice vector within a certain magnitude bound, finding this vector is in general a hard computational problem. Finding the vector within a factor guaranteed by Minkowski's bound is referred to as Minkowski's Vector Problem (MVP), and it is known that approximation SVP reduces to it using transference properties of the dual lattice. The computational problem is also sometimes referred to as HermiteSVP.
- The LLL-basis reduction algorithm can be seen as a weak but efficiently algorithmic version of Minkowski's bound on the shortest vector. This is because a ${\textstyle \delta }$ -LLL reduced basis ${\textstyle b_{1},\ldots ,b_{n}}$ for ${\textstyle L}$ has the property that ${\textstyle \|b_{1}\|\leq \left({\frac {1}{\delta -.25}}\right)^{\frac {n-1}{4}}\det(L)^{1/n}}$ ; see these lecture notes of Micciancio for more on this. As explained in, proofs of bounds on the Hermite constant contain some of the key ideas in the LLL-reduction algorithm.

### Applications to number theory

#### Primes that are sums of two squares

The difficult implication in Fermat's theorem on sums of two squares can be proven using Minkowski's bound on the shortest vector.

**Theorem:** Every prime with ${\textstyle p\equiv 1\mod 4}$ can be written as a sum of two squares.

Proof

Since ${\textstyle 4\,|\,p-1}$ and a is a quadratic residue modulo a prime ${\textstyle p}$ if and only if $a^{\frac {p-1}{2}}=1~({\text{mod}}~p)$ (Euler's Criterion) there is a square root of ${\textstyle -1}$ in ${\textstyle \mathbb {Z} /p\mathbb {Z} }$ ; choose one and call one representative in ${\textstyle \mathbb {Z} }$ for it ${\textstyle j}$ . Consider the lattice ${\textstyle L}$ defined by the vectors ${\textstyle (1,j),(0,p)}$ , and let ${\textstyle B}$ denote the associated matrix. The determinant of this lattice is ${\textstyle p}$ , whence Minkowski's bound tells us that there is a nonzero ${\textstyle x=(x_{1},x_{2})\in \mathbb {Z} ^{2}}$ with ${\textstyle 0<\|Bx\|_{2}^{2}<2p}$ . We have ${\textstyle \|Bx\|^{2}=\|(x_{1},jx_{1}+px_{2})\|^{2}=x_{1}^{2}+(jx_{1}+px_{2})^{2}}$ and we define the integers ${\textstyle a=x_{1},b=(jx_{1}+px_{2})}$ . Minkowski's bound tells us that ${\textstyle 0<a^{2}+b^{2}<2p}$ , and simple modular arithmetic shows that ${\textstyle a^{2}+b^{2}=x_{1}^{2}+(jx_{1}+px_{2})^{2}=0\mod p}$ , and thus we conclude that ${\textstyle a^{2}+b^{2}=p}$ . Q.E.D.

Additionally, the lattice perspective gives a computationally efficient approach to Fermat's theorem on sums of squares:

| Algorithm |
|---|
| First, recall that finding any nonzero vector with norm less than ${\textstyle 2p}$ in ${\textstyle L}$ , the lattice of the proof, gives a decomposition of ${\textstyle p}$ as a sum of two squares. Such vectors can be found efficiently, for instance using LLL-algorithm. In particular, if ${\textstyle b_{1},b_{2}}$ is a ${\textstyle 3/4}$ -LLL reduced basis, then, by the property that ${\textstyle \\|b_{1}\\|\leq ({\frac {1}{\delta -.25}})^{\frac {n-1}{4}}{\text{det}}(B)^{1/n}}$ , ${\textstyle \\|b_{1}\\|^{2}\leq {\sqrt {2}}p<2p}$ . Thus, by running the LLL-lattice basis reduction algorithm with ${\textstyle \delta =3/4}$ , we obtain a decomposition of ${\textstyle p}$ as a sum of squares. Note that because every vector in ${\textstyle L}$ has norm squared a multiple of ${\textstyle p}$ , the vector returned by the LLL-algorithm in this case is in fact a shortest vector. |

#### Lagrange's four-square theorem

Minkowski's theorem is also useful to prove Lagrange's four-square theorem, which states that every natural number can be written as the sum of the squares of four natural numbers.

#### Dirichlet's theorem on simultaneous rational approximation

Minkowski's theorem can be used to prove Dirichlet's theorem on simultaneous rational approximation.

#### Algebraic number theory

Another application of Minkowski's theorem is the result that every class in the ideal class group of a number field *K* contains an integral ideal of norm not exceeding a certain bound, depending on *K*, called Minkowski's bound: the finiteness of the class number of an algebraic number field follows immediately.

## Complexity theory

The complexity of finding the point guaranteed by Minkowski's theorem, or the closely related Blichfeldt's theorem, have been studied from the perspective of TFNP search problems. In particular, it is known that a computational analogue of Blichfeldt's theorem, a corollary of the proof of Minkowski's theorem, is PPP-complete. It is also known that the computational analogue of Minkowski's theorem is in the class PPP, and it was conjectured to be PPP-complete.
