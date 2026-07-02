---
title: "Givens rotation"
source: https://en.wikipedia.org/wiki/Givens_rotation
domain: qr-algorithm
license: CC-BY-SA-4.0
tags: qr algorithm, qr decomposition, hessenberg matrix, givens rotation
fetched: 2026-07-02
---

# Givens rotation

In numerical linear algebra, a **Givens rotation** is a rotation in the plane spanned by two coordinates axes. Givens rotations are named after Wallace Givens, who introduced them to numerical analysts in the 1950s while he was working at Argonne National Laboratory.

## As action on matrices

A Givens rotation acting on a matrix from the left is a row operation, moving data between rows but always within the same column. Unlike the elementary operation of row-addition, a Givens rotation changes both of the rows addressed by it. To understand how it is a rotation, one may denote the elements of one target row by $x_{1}$ through $x_{n}$ and the elements of the other target row by $y_{1}$ through $y_{n}$ : ${\begin{bmatrix}\vdots &\vdots &\ddots &\vdots \\x_{1}&x_{2}&\dots &x_{n}\\\vdots &\vdots &\ddots &\vdots \\y_{1}&y_{2}&\dots &y_{n}\\\vdots &\vdots &\ddots &\vdots \end{bmatrix}}$ Then the effect of a Givens rotation is to rotate each subvector $(x_{k},y_{k})$ by the same angle. As with row-addition, algorithms often choose this angle so that one specific element becomes zero, and whatever happens in remaining columns is considered acceptable side-effects.

A Givens rotation acting on a matrix from the right is instead a column operation, moving data between two columns but always within the same row. As with action from the left, it rotates each subvector $(x_{k},y_{k})$ by the same angle, but here these named elements occur in the matrix as ${\begin{bmatrix}\dots &x_{1}&\dots &y_{1}&\dots \\\dots &x_{2}&\dots &y_{2}&\dots \\\ddots &\vdots &\ddots &\vdots &\ddots \\\dots &x_{n}&\dots &y_{n}&\dots \end{bmatrix}}$ Some algorithms, especially those concerned with preserving matrix similarity, apply Givens rotations as a conjugate action: both rotating by one angle between two rows, and rotating by the same angle between the corresponding columns. In this case the effect on the four elements affected by both rotations is more complicated; a Jacobi rotation is such a conjugate action to the end of zeroing the two off-diagonal elements among these four.

The main use of Givens rotations in numerical linear algebra is to transform vectors or matrices into a special form with zeros in certain coefficients. This effect can, for example, be employed for computing the QR decomposition of a matrix. One advantage over Householder transformations is that they can easily be parallelised, and another is that often for very sparse matrices they have a lower operation count.

## Matrix representation

A Givens rotation is represented by a matrix of the form

$G(i,j,\theta )={\begin{bmatrix}1&\cdots &0&\cdots &0&\cdots &0\\\vdots &\ddots &\vdots &&\vdots &&\vdots \\0&\cdots &c&\cdots &-s&\cdots &0\\\vdots &&\vdots &\ddots &\vdots &&\vdots \\0&\cdots &s&\cdots &c&\cdots &0\\\vdots &&\vdots &&\vdots &\ddots &\vdots \\0&\cdots &0&\cdots &0&\cdots &1\end{bmatrix}},$

where *c* = cos *θ* and *s* = sin *θ* appear at the intersections ith and jth rows and columns. That is, for fixed i > j, the non-zero elements of Givens matrix are given by:

${\begin{aligned}g_{kk}&{}=1\qquad {\text{for}}\ k\neq i,\,j\\g_{kk}&{}=c\qquad {\text{for}}\ k=i,\,j\\g_{ji}&{}=-g_{ij}=-s\\\end{aligned}}$

The product *G*(*i*, *j*, *θ*)**x** represents a counterclockwise rotation of the vector **x** in the (*i*, *j*) plane of θ radians, hence the name Givens rotation.

## Stable calculation

When a Givens rotation matrix, *G*(*i*, *j*, *θ*), multiplies another matrix, A, from the left, *G A*, only rows i and j of A are affected. Thus we restrict attention to the following counterclockwise problem. Given a and b, find *c* = cos *θ* and *s* = sin *θ* such that

${\begin{bmatrix}c&-s\\s&c\end{bmatrix}}{\begin{bmatrix}a\\b\end{bmatrix}}={\begin{bmatrix}r\\0\end{bmatrix}},$

where $r={\sqrt {a^{2}+b^{2}}}$ is the length of the vector $(a,b)$ . Explicit calculation of θ is rarely necessary or desirable. Instead we directly seek c and s. An obvious solution would be

${\begin{aligned}c&{}\leftarrow a/r\\s&{}\leftarrow -b/r.\end{aligned}}$

However, the computation for r may overflow or underflow. An alternative formulation avoiding this problem (Golub & Van Loan 1996, §5.1.8) is implemented as the hypot function in many programming languages.

The following Fortran code is a minimalistic implementation of Givens rotation for real numbers. If the input values 'a' or 'b' are frequently zero, the code may be optimized to handle these cases as presented here.

```mw
subroutine givens_rotation(a, b, c, s, r)

real a, b, c, s, r
real h, d

if (b .ne. 0.0) then
    h = hypot(a, b)
    d = 1.0 / h
    c = abs(a) * d
    s = sign(d, a) * b
    r = sign(1.0, a) * h
else
    c = 1.0
    s = 0.0
    r = a
end if

return
end
```

Furthermore, as Edward Anderson discovered in improving LAPACK, a previously overlooked numerical consideration is continuity. To achieve this, we require r to be positive. The following MATLAB/GNU Octave code illustrates the algorithm.

```mw
function [c, s, r] = givens_rotation(a, b)
    if b == 0;
        c = sign(a);
        if (c == 0);
            c = 1.0; % Unlike other languages, MatLab's sign function returns 0 on input 0.
        end;
        s = 0;
        r = abs(a);
    elseif a == 0;
        c = 0;
        s = -sign(b);
        r = abs(b);
    elseif abs(a) > abs(b);
        t = b / a;
        u = sign(a) * sqrt(1 + t * t);
        c = 1 / u;
        s = -c * t;
        r = a * u;
    else
        t = a / b;
        u = sign(b) * sqrt(1 + t * t);
        s = -1 / u;
        c = t / u;
        r = b * u;
    end
end
```

The IEEE 754 `copysign(x,y)` function, provides a safe and cheap way to copy the sign of `y` to `x`. If that is not available, |*x*|⋅sgn(*y*), using the abs and sgn functions, is an alternative as done above.

## Triangularization

Given the following 3×3 Matrix:

$A_{1}={\begin{bmatrix}6&5&0\\5&1&4\\0&4&3\\\end{bmatrix}},$

two iterations of the Givens rotation (note that the Givens rotation algorithm used here differs slightly from above) yield an upper triangular matrix in order to compute the QR decomposition.

In order to form the desired matrix, zeroing elements (2,1) and (3,2) is required; element (2,1) is zeroed first, using a rotation matrix of:

$G_{1}={\begin{bmatrix}c&-s&0\\s&c&0\\0&0&1\\\end{bmatrix}}.$

The following matrix multiplication results:

${\begin{aligned}G_{1}A_{1}&{}=A_{2}\\&{}={\begin{bmatrix}c&-s&0\\s&c&0\\0&0&1\\\end{bmatrix}}{\begin{bmatrix}6&5&0\\5&1&4\\0&4&3\\\end{bmatrix}},\end{aligned}}$

where

${\begin{aligned}r&{}={\sqrt {6^{2}+5^{2}}}\approx 7.8102\\c&{}=6/r\approx 0.7682\\s&{}=-5/r\approx -0.6402.\end{aligned}}$

Using these values for c and s and performing the matrix multiplication above yields A2:

$A_{2}\approx {\begin{bmatrix}7.8102&4.4813&2.5607\\0&-2.4327&3.0729\\0&4&3\\\end{bmatrix}}$

Zeroing element (3,2) finishes off the process. Using the same idea as before, the rotation matrix is:

$G_{2}={\begin{bmatrix}1&0&0\\0&c&-s\\0&s&c\\\end{bmatrix}}$

Afterwards, the following matrix multiplication is:

${\begin{aligned}G_{2}A_{2}&{}=A_{3}\\&{}\approx {\begin{bmatrix}1&0&0\\0&c&-s\\0&s&c\\\end{bmatrix}}{\begin{bmatrix}7.8102&4.4813&2.5607\\0&-2.4327&3.0729\\0&4&3\\\end{bmatrix}},\end{aligned}}$

where

${\begin{aligned}r&{}\approx {\sqrt {(-2.4327)^{2}+4^{2}}}\approx 4.6817\\c&{}\approx -2.4327/r\approx -0.5196\\s&{}\approx -4/r\approx -0.8544.\end{aligned}}$

Using these values for c and s and performing the multiplications results in A3:

$A_{3}\approx {\begin{bmatrix}7.8102&4.4813&2.5607\\0&4.6817&0.9665\\0&0&-4.1843\\\end{bmatrix}}.$

This new matrix A3 is the upper triangular matrix needed to perform an iteration of the QR decomposition. Q is now formed using the transpose of the rotation matrices in the following manner:

$Q=G_{1}^{T}\,G_{2}^{T}.$

Performing this matrix multiplication yields:

$Q\approx {\begin{bmatrix}0.7682&0.3327&0.5470\\0.6402&-0.3992&-0.6564\\0&0.8544&-0.5196\\\end{bmatrix}}.$

This completes two iterations of the Givens Rotation and calculating the QR decomposition can now be done.

### QR iteration variant

If performing the above calculations as a step in the QR algorithm for finding the eigenvalues of a matrix, then one next wants to compute the matrix $RQ$ , but one should not do so by first multiplying $G_{1}^{T}$ and $G_{2}^{T}$ to form Q , instead rather by multiplying each $G_{k}^{T}$ by $RG_{1}^{T}\dots G_{k-1}^{T}$ (on the right). The reason for this is that each multiplication by a Givens matrix on the right changes only two columns of R , thus requiring a mere $O(n)$ arithmetic operations, which for $n-1$ Givens rotations sums up to $O(n^{2})$ arithmetic operations; multiplying by the general $n\times n$ matrix Q would require $O(n^{3})$ arithmetic operations. Likewise, storing the full Q matrix amounts to $n^{2}$ elements, but each Givens matrix is fully specified the pairs $(c,s)$ and $(i,j),$ and $n-1$ of them can thus be stored in $4n-4$ elements.

In the example, ${\begin{aligned}RQ=A_{3}(G_{1}^{T}G_{2}^{T})={}&(A_{3}G_{1}^{T})G_{2}^{T}\\\approx {}&{\begin{bmatrix}8.8687&-1.5575&2.5607\\2.9972&3.5965&0.9665\\0&0&-4.1843\end{bmatrix}}G_{2}^{T}\approx {\begin{bmatrix}8.8687&2.9972&0.0\\2.9972&-1.0430&-3.5750\\0&-3.5750&2.1742\end{bmatrix}}\end{aligned}}$

## Complex matrices

A Givens rotation in the complex case would have to be a unitary matrix which maps a nonzero vector ${\begin{pmatrix}w\\z\end{pmatrix}}\in \mathbb {C} ^{2}$ to some ${\begin{pmatrix}r\\0\end{pmatrix}}$ . A straightforward solution for this is ${\frac {1}{\sqrt {|w|^{2}+|z|^{2}}}}{\begin{pmatrix}{\overline {w}}&{\overline {z}}\\-z&w\end{pmatrix}}$ which is even in SU(2) and makes r real $={\sqrt {|w|^{2}+|z|^{2}}}$ .

(Golub & Van Loan 2013, §5.1.13) suggest the specialised form ${\begin{pmatrix}\cos(\theta )&-\sin(\theta )e^{i\phi }\\\sin(\theta )e^{-i\phi }&\cos(\theta )\end{pmatrix}}$ (coinciding with the above when w is real) for a Givens rotation. Their idea is to choose $\theta$ and $\phi$ so that $e^{i\phi }={\frac {\overline {z}}{|z|}}{\bigg /}{\frac {\overline {w}}{|w|}}$ $|w|\sin(\theta )+|z|\cos(\theta )=0$ and they explain how to obtain $\cos(\theta ),\sin(\theta ),\cos(\phi ),\sin(\phi )$ from three calls to a function for computing *real* Givens rotations. This more complicated initialisation can be justified by the observation that since half the matrix elements are real, fewer arithmetic operations are needed when applying this rotation. Note however that having only two real degrees of freedom means the r component of the result cannot in general be made real.

A more elementary approach to the same end is to first multiply both rows being targeted by unit magnitude complex numbers of appropriate phase, so that both elements in the column considered become real – then a real Givens rotation suffices for zeroing out one of those entires. In the same notation as above, this amounts to $\underbrace {{\frac {1}{\sqrt {|w|^{2}+|z|^{2}}}}{\begin{pmatrix}|w|&|z|\\-|z|&|w|\end{pmatrix}}} _{G}\underbrace {\begin{pmatrix}{\overline {w}}/|w|&0\\0&{\overline {z}}/|z|\end{pmatrix}} _{D}{\begin{pmatrix}w\\z\end{pmatrix}}={\begin{pmatrix}{\sqrt {|w|^{2}+|z|^{2}}}\\0\end{pmatrix}}$ where D is unitary (but in general not special unitary) because it is a diagonal matrix whose diagonal elements have unit magnitudes, and the product $GD$ is unitary because a product of unitary matrices is unitary. Here we save some arithmetic operations because multiplication by D acts on each row separately, and multiplication by G has real coefficients throughout.

A potential concern with the latter two methods is however that the choice of rotation is discontinuous along the $w=0$ line, and for the last method also along the $z=0$ line; even though the result of applying the rotation to ${\begin{pmatrix}w\\z\end{pmatrix}}$ varies continuously, the result of applying that same rotation to other columns of a matrix does not. For example,

the Golub–Van Loan method picks

${\begin{pmatrix}{\frac {\varepsilon }{\sqrt {1+\varepsilon ^{2}}}}&e^{i\alpha }{\frac {1}{\sqrt {1+\varepsilon ^{2}}}}\\-e^{-i\alpha }{\frac {1}{\sqrt {1+\varepsilon ^{2}}}}&{\frac {\varepsilon }{\sqrt {1+\varepsilon ^{2}}}}\end{pmatrix}}$

to rotate

${\begin{pmatrix}\varepsilon e^{i\alpha }&10\\1&0\end{pmatrix}}$

, producing

${\begin{pmatrix}e^{i\alpha }{\sqrt {1+\varepsilon ^{2}}}&{\frac {10\varepsilon }{\sqrt {1+\varepsilon ^{2}}}}\\0&-10e^{-i\alpha }{\frac {1}{\sqrt {1+\varepsilon ^{2}}}}\end{pmatrix}}$

.

## In Clifford algebras

In Clifford algebras and its child structures such as geometric algebras, rotations are represented by bivectors. Givens rotations are represented by the exterior product of the basis vectors. Given any pair of basis vectors $\mathbf {e} _{i},\mathbf {e} _{j}$ Givens rotations bivectors are:

$B_{ij}=\mathbf {e} _{i}\wedge \mathbf {e} _{j}.$

Their action on any vector is written:

$v=e^{-(\theta /2)(\mathbf {e} _{i}\wedge \mathbf {e} _{j})}ue^{(\theta /2)(\mathbf {e} _{i}\wedge \mathbf {e} _{j})},$

where

$e^{(\theta /2)(\mathbf {e} _{i}\wedge \mathbf {e} _{j})}=\cos(\theta /2)+\sin(\theta /2)\mathbf {e} _{i}\wedge \mathbf {e} _{j}.$

## Dimension 3

There are three Givens rotations in dimension 3:

$R_{X}(\theta )={\begin{bmatrix}1&0&0\\0&\cos \theta &-\sin \theta \\0&\sin \theta &\cos \theta \end{bmatrix}}.$

${\begin{aligned}\\R_{Y}(\theta )={\begin{bmatrix}\cos \theta &0&-\sin \theta \\0&1&0\\\sin \theta &0&\cos \theta \end{bmatrix}}\end{aligned}}$

${\begin{aligned}\\R_{Z}(\theta )={\begin{bmatrix}\cos \theta &-\sin \theta &0\\\sin \theta &\cos \theta &0\\0&0&1\end{bmatrix}}\end{aligned}}$

Given that they are endomorphisms they can be composed with each other as many times as desired, keeping in mind that *g* ∘ *f* ≠ *f* ∘ *g*.

These three Givens rotations composed can generate any rotation matrix according to Davenport's chained rotation theorem. This means that they can transform the standard basis of the space to any other frame in the space.

When rotations are performed in the right order, the values of the rotation angles of the final frame will be equal to the Euler angles of the final frame in the corresponding convention. For example, an operator $R=R_{Y}(\theta _{3})\cdot R_{X}(\theta _{2})\cdot R_{Z}(\theta _{1})$ transforms the basis of the space into a frame with angles roll, pitch and yaw $YPR=(\theta _{3},\theta _{2},\theta _{1})$ in the Tait–Bryan convention *z*-*x*-*y* (convention in which the line of nodes is perpendicular to *z* and *Y* axes, also named *Y*-*X′*-*Z″*).

For the same reason, any rotation matrix in 3D can be decomposed in a product of three of these rotation operators.

The meaning of the composition of two Givens rotations *g* ∘ *f* is an operator that transforms vectors first by f and then by g, being f and g rotations about one axis of basis of the space. This is similar to the extrinsic rotation equivalence for Euler angles.

### Table of composed rotations

The following table shows the three Givens rotations equivalent to the different Euler angles conventions using extrinsic composition (composition of rotations about the basis axes) of active rotations and the right-handed rule for the positive sign of the angles.

The notation has been simplified in such a way that *c*1 means cos *θ*1 and *s*2 means sin *θ*2). The subindexes of the angles are the order in which they are applied using *extrinsic* composition (1 for intrinsic rotation, 2 for nutation, 3 for precession)

As rotations are applied just in the opposite order of the Euler angles table of rotations, this table is the same but swapping indexes 1 and 3 in the angles associated with the corresponding entry. An entry like *zxy* means to apply first the *y* rotation, then *x*, and finally *z*, in the basis axes.

All the compositions assume the right hand convention for the matrices that are multiplied, yielding the following results.

| *xzx* | ${\begin{bmatrix}c_{2}&-c_{1}s_{2}&s_{1}s_{2}\\c_{3}s_{2}&c_{3}c_{2}c_{1}-s_{3}s_{1}&-c_{2}c_{3}s_{1}-c_{1}s_{3}\\s_{2}s_{3}&c_{3}s_{1}+c_{1}c_{2}s_{3}&c_{3}c_{1}-c_{2}s_{3}s_{1}\end{bmatrix}}$ | *xzy* | ${\begin{bmatrix}c_{2}c_{3}&-c_{3}s_{2}c_{1}+s_{3}s_{1}&c_{3}s_{2}s_{1}+s_{3}c_{1}\\s_{2}&c_{1}c_{2}&-c_{2}s_{1}\\-s_{3}c_{2}&s_{3}s_{2}c_{1}+c_{3}s_{1}&-s_{3}s_{2}s_{1}+c_{3}c_{1}\end{bmatrix}}$ |
|---|---|---|---|
| *xyx* | ${\begin{bmatrix}c_{2}&s_{1}s_{2}&c_{1}s_{2}\\s_{2}s_{3}&c_{3}c_{1}-c_{2}s_{3}s_{1}&-c_{3}s_{1}-c_{1}c_{2}s_{3}\\-c_{3}s_{2}&c_{3}c_{2}s_{1}+c_{1}s_{3}&c_{3}c_{2}c_{1}-s_{3}s_{1}\end{bmatrix}}$ | *xyz* | ${\begin{bmatrix}c_{3}c_{2}&-s_{3}c_{1}+c_{3}s_{2}s_{1}&s_{3}s_{1}+c_{3}s_{2}c_{1}\\s_{3}c_{2}&c_{3}c_{1}+s_{3}s_{2}s_{1}&-c_{3}s_{1}+s_{3}s_{2}c_{1}\\-s_{2}&c_{2}s_{1}&c_{2}c_{1}\end{bmatrix}}$ |
| *yxy* | ${\begin{bmatrix}c_{3}c_{1}-c_{2}s_{3}s_{1}&s_{2}s_{3}&c_{3}s_{1}+s_{3}c_{2}c_{1}\\s_{1}s_{2}&c_{2}&-c_{1}s_{2}\\-c_{2}c_{3}s_{1}-c_{1}s_{3}&c_{3}s_{2}&c_{3}c_{2}c_{1}-s_{3}s_{1}\end{bmatrix}}$ | *yxz* | ${\begin{bmatrix}c_{3}c_{1}-s_{3}s_{2}s_{1}&-s_{3}c_{2}&c_{3}s_{1}+s_{3}s_{2}c_{1}\\s_{3}c_{1}+c_{3}s_{2}s_{1}&c_{3}c_{2}&s_{3}s_{1}-c_{3}s_{2}c_{1}\\-c_{2}s_{1}&s_{2}&c_{2}c_{1}\end{bmatrix}}$ |
| *yzy* | ${\begin{bmatrix}c_{3}c_{2}c_{1}-s_{3}s_{1}&-c_{3}s_{2}&c_{2}c_{3}s_{1}+c_{1}s_{3}\\c_{1}s_{2}&c_{2}&s_{1}s_{2}\\-c_{3}s_{1}-c_{1}c_{2}s_{3}&s_{2}s_{3}&c_{3}c_{1}-c_{2}s_{3}s_{1}\end{bmatrix}}$ | *yzx* | ${\begin{bmatrix}c_{2}c_{1}&-s_{2}&c_{2}s_{1}\\c_{3}s_{2}c_{1}+s_{3}s_{1}&c_{3}c_{2}&c_{3}s_{2}s_{1}-s_{3}c_{1}\\s_{3}s_{2}c_{1}-c_{3}s_{1}&s_{3}c_{2}&s_{3}s_{2}s_{1}+c_{3}c_{1}\end{bmatrix}}$ |
| *zyz* | ${\begin{bmatrix}c_{3}c_{2}c_{1}-s_{3}s_{1}&-c_{2}s_{1}c_{3}-c_{1}s_{3}&c_{3}s_{2}\\c_{3}s_{1}+c_{1}c_{2}s_{3}&c_{3}c_{1}-c_{2}s_{3}s_{1}&s_{2}s_{3}\\-c_{1}s_{2}&s_{1}s_{2}&c_{2}\end{bmatrix}}$ | *zyx* | ${\begin{bmatrix}c_{2}c_{1}&-c_{2}s_{1}&s_{2}\\s_{3}s_{2}c_{1}+c_{3}s_{1}&-s_{3}s_{2}s_{1}+c_{3}c_{1}&-s_{3}c_{2}\\-c_{3}s_{2}c_{1}+s_{3}s_{1}&c_{3}s_{2}s_{1}+s_{3}c_{1}&c_{3}c_{2}\end{bmatrix}}$ |
| *zxz* | ${\begin{bmatrix}c_{3}c_{1}-c_{2}s_{1}s_{3}&-c_{3}s_{1}-c_{1}c_{2}s_{3}&s_{2}s_{3}\\c_{2}c_{3}s_{1}+c_{1}s_{3}&c_{3}c_{2}c_{1}-s_{3}s_{1}&-c_{3}s_{2}\\s_{1}s_{2}&c_{1}s_{2}&c_{2}\end{bmatrix}}$ | *zxy* | ${\begin{bmatrix}c_{3}c_{1}+s_{3}s_{2}s_{1}&-c_{3}s_{1}+s_{3}s_{2}c_{1}&s_{3}c_{2}\\c_{2}s_{1}&c_{2}c_{1}&-s_{2}\\-s_{3}c_{1}+c_{3}s_{2}s_{1}&s_{3}s_{1}+c_{3}s_{2}c_{1}&c_{3}c_{2}\end{bmatrix}}$ |
