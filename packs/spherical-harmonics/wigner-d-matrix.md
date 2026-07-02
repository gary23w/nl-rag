---
title: "Wigner D-matrix"
source: https://en.wikipedia.org/wiki/Wigner_D-matrix
domain: spherical-harmonics
license: CC-BY-SA-4.0
tags: spherical harmonics, associated legendre polynomials, multipole expansion, wigner d-matrix
fetched: 2026-07-02
---

# Wigner D-matrix

The **Wigner D-matrix** is a unitary matrix in an irreducible representation of the groups SU(2) and SO(3). It was introduced in 1927 by Eugene Wigner, and plays a fundamental role in the quantum mechanical theory of angular momentum. The complex conjugate of the D-matrix is an eigenfunction of the Hamiltonian of spherical and symmetric rigid rotors. The letter D stands for *Darstellung*, which means "representation" in German.

## Definition of the Wigner D-matrix

Let *Jx*, *Jy*, *Jz* be generators of the Lie algebra of SU(2) and SO(3). In quantum mechanics, these three operators are the components of a vector operator known as *angular momentum*. Examples are the angular momentum of an electron in an atom, electronic spin, and the angular momentum of a rigid rotor.

In all cases, the three operators satisfy the following commutation relations,

$[J_{x},J_{y}]=iJ_{z},\quad [J_{z},J_{x}]=iJ_{y},\quad [J_{y},J_{z}]=iJ_{x},$

where *i* is the purely imaginary number and the Planck constant ħ has been set equal to one. The Casimir operator

$J^{2}=J_{x}^{2}+J_{y}^{2}+J_{z}^{2}$

commutes with all generators of the Lie algebra. Hence, it may be diagonalized together with Jz.

This defines the spherical basis used here. That is, there is a *complete set* of kets (i.e. orthonormal basis of joint eigenvectors labelled by quantum numbers that define the eigenvalues) with

$J^{2}|jm\rangle =j(j+1)|jm\rangle ,\quad J_{z}|jm\rangle =m|jm\rangle ,$

where *j* = 0, 1/2, 1, 3/2, 2, ... for SU(2), and *j* = 0, 1, 2, ... for SO(3). In both cases, *m* = −*j*, −*j* + 1, ..., *j*.

A 3-dimensional rotation operator can be written as

${\mathcal {R}}(\alpha ,\beta ,\gamma )=e^{-i\alpha J_{z}}e^{-i\beta J_{y}}e^{-i\gamma J_{z}},$

where *α*, *β*, *γ* are Euler angles (characterized by the keywords: z-y-z convention, right-handed frame, right-hand screw rule, active interpretation).

The **Wigner D-matrix** is a unitary square matrix of dimension 2*j* + 1 in this spherical basis with elements

$D_{m'm}^{j}(\alpha ,\beta ,\gamma )\equiv \langle jm'|{\mathcal {R}}(\alpha ,\beta ,\gamma )|jm\rangle =e^{-im'\alpha }d_{m'm}^{j}(\beta )e^{-im\gamma },$

where

$d_{m'm}^{j}(\beta )=\langle jm'|e^{-i\beta J_{y}}|jm\rangle =D_{m'm}^{j}(0,\beta ,0)$

is an element of the orthogonal **Wigner's (small) d-matrix** (sometimes referred to as the reduced Wigner D-matrix).

That is, in this basis,

$D_{m'm}^{j}(\alpha ,0,0)=e^{-im'\alpha }\delta _{m'm}$

is diagonal, like the *γ* matrix factor, but unlike the above *β* factor.

## Wigner (small) d-matrix

Wigner gave the following expression:

$d_{m'm}^{j}(\beta )=[(j+m')!(j-m')!(j+m)!(j-m)!]^{\frac {1}{2}}\sum _{s=s_{\mathrm {min} }}^{s_{\mathrm {max} }}\left[{\frac {(-1)^{m'-m+s}\left(\cos {\frac {\beta }{2}}\right)^{2j+m-m'-2s}\left(\sin {\frac {\beta }{2}}\right)^{m'-m+2s}}{(j+m-s)!s!(m'-m+s)!(j-m'-s)!}}\right].$

The sum over *s* is over such values that the factorials are nonnegative, i.e. $s_{\mathrm {min} }=\mathrm {max} (0,m-m')$ , $s_{\mathrm {max} }=\mathrm {min} (j+m,j-m')$ .

*Note:* The d-matrix elements defined here are real. In the often-used z-x-z convention of Euler angles, the factor $(-1)^{m'-m+s}$ in this formula is replaced by $(-1)^{s}i^{m-m'},$ causing half of the functions to be purely imaginary. The realness of the d-matrix elements is one of the reasons that the z-y-z convention, used in this article, is usually preferred in quantum mechanical applications.

The d-matrix elements are related to Jacobi polynomials $P_{k}^{(a,b)}(\cos \beta )$ with nonnegative a and $b.$ Let

$k=\min(j+m,j-m,j+m',j-m').$

If

$k={\begin{cases}j+m:&a=m'-m;\quad \lambda =m'-m\\j-m:&a=m-m';\quad \lambda =0\\j+m':&a=m-m';\quad \lambda =0\\j-m':&a=m'-m;\quad \lambda =m'-m\\\end{cases}}$

Then, with $b=2j-2k-a,$ the relation is

$d_{m'm}^{j}(\beta )=(-1)^{\lambda }{\binom {2j-k}{k+a}}^{\frac {1}{2}}{\binom {k+b}{b}}^{-{\frac {1}{2}}}\left(\sin {\frac {\beta }{2}}\right)^{a}\left(\cos {\frac {\beta }{2}}\right)^{b}P_{k}^{(a,b)}(\cos \beta ),$

where $a,b\geq 0.$

It is also useful to consider the relations $a=|m'-m|,b=|m'+m|,\lambda ={\frac {m-m'-|m-m'|}{2}},k=j-M$ , where $M=\max(|m|,|m'|)$ and $N=\min(|m|,|m'|)$ , which lead to:

$d_{m'm}^{j}(\beta )=(-1)^{\frac {m-m'-|m-m'|}{2}}\left[{\frac {(j+M)!(j-M)!}{(j+N)!(j-N)!}}\right]^{\frac {1}{2}}\left(\sin {\frac {\beta }{2}}\right)^{|m-m'|}\left(\cos {\frac {\beta }{2}}\right)^{|m+m'|}P_{j-M}^{(|m-m'|,|m+m'|)}(\cos \beta ).$

## Properties of the Wigner D-matrix

The complex conjugate of the D-matrix satisfies a number of differential properties that can be formulated concisely by introducing the following operators with $(x,y,z)=(1,2,3),$

${\begin{aligned}{\hat {\mathcal {J}}}_{1}&=i\left(\cos \alpha \cot \beta {\frac {\partial }{\partial \alpha }}+\sin \alpha {\partial \over \partial \beta }-{\cos \alpha \over \sin \beta }{\partial \over \partial \gamma }\right)\\{\hat {\mathcal {J}}}_{2}&=i\left(\sin \alpha \cot \beta {\partial \over \partial \alpha }-\cos \alpha {\partial \over \partial \beta }-{\sin \alpha \over \sin \beta }{\partial \over \partial \gamma }\right)\\{\hat {\mathcal {J}}}_{3}&=-i{\partial \over \partial \alpha }\end{aligned}}$

which have quantum mechanical meaning: they are space-fixed rigid rotor angular momentum operators.

Further,

${\begin{aligned}{\hat {\mathcal {P}}}_{1}&=i\left({\cos \gamma \over \sin \beta }{\partial \over \partial \alpha }-\sin \gamma {\partial \over \partial \beta }-\cot \beta \cos \gamma {\partial \over \partial \gamma }\right)\\{\hat {\mathcal {P}}}_{2}&=i\left(-{\sin \gamma \over \sin \beta }{\partial \over \partial \alpha }-\cos \gamma {\partial \over \partial \beta }+\cot \beta \sin \gamma {\partial \over \partial \gamma }\right)\\{\hat {\mathcal {P}}}_{3}&=-i{\partial \over \partial \gamma },\\\end{aligned}}$

which have quantum mechanical meaning: they are body-fixed rigid rotor angular momentum operators.

The operators satisfy the commutation relations

$\left[{\mathcal {J}}_{1},{\mathcal {J}}_{2}\right]=i{\mathcal {J}}_{3},\qquad {\hbox{and}}\qquad \left[{\mathcal {P}}_{1},{\mathcal {P}}_{2}\right]=-i{\mathcal {P}}_{3},$

and the corresponding relations with the indices permuted cyclically. The ${\mathcal {P}}_{i}$ satisfy *anomalous commutation relations* (have a minus sign on the right hand side).

The two sets mutually commute,

$\left[{\mathcal {P}}_{i},{\mathcal {J}}_{j}\right]=0,\quad i,j=1,2,3,$

and the total operators squared are equal,

${\mathcal {J}}^{2}\equiv {\mathcal {J}}_{1}^{2}+{\mathcal {J}}_{2}^{2}+{\mathcal {J}}_{3}^{2}={\mathcal {P}}^{2}\equiv {\mathcal {P}}_{1}^{2}+{\mathcal {P}}_{2}^{2}+{\mathcal {P}}_{3}^{2}.$

Their explicit form is,

${\mathcal {J}}^{2}={\mathcal {P}}^{2}=-{\frac {1}{\sin ^{2}\beta }}\left({\frac {\partial ^{2}}{\partial \alpha ^{2}}}+{\frac {\partial ^{2}}{\partial \gamma ^{2}}}-2\cos \beta {\frac {\partial ^{2}}{\partial \alpha \partial \gamma }}\right)-{\frac {\partial ^{2}}{\partial \beta ^{2}}}-\cot \beta {\frac {\partial }{\partial \beta }}.$

The operators ${\mathcal {J}}_{i}$ act on the first (row) index of the D-matrix,

${\begin{aligned}{\mathcal {J}}_{3}D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}&=m'D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}\\({\mathcal {J}}_{1}\pm i{\mathcal {J}}_{2})D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}&={\sqrt {j(j+1)-m'(m'\pm 1)}}D_{m'\pm 1,m}^{j}(\alpha ,\beta ,\gamma )^{*}\end{aligned}}$

The operators ${\mathcal {P}}_{i}$ act on the second (column) index of the D-matrix,

${\mathcal {P}}_{3}D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}=mD_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*},$

and, because of the anomalous commutation relation the raising/lowering operators are defined with reversed signs,

$({\mathcal {P}}_{1}\mp i{\mathcal {P}}_{2})D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}={\sqrt {j(j+1)-m(m\pm 1)}}D_{m',m\pm 1}^{j}(\alpha ,\beta ,\gamma )^{*}.$

Finally,

${\mathcal {J}}^{2}D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}={\mathcal {P}}^{2}D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}=j(j+1)D_{m'm}^{j}(\alpha ,\beta ,\gamma )^{*}.$

In other words, the rows and columns of the (complex conjugate) Wigner D-matrix span irreducible representations of the isomorphic Lie algebras generated by $\{{\mathcal {J}}_{i}\}$ and $\{-{\mathcal {P}}_{i}\}$ .

An important property of the Wigner D-matrix follows from the commutation of ${\mathcal {R}}(\alpha ,\beta ,\gamma )$ with the time reversal operator T,

$\langle jm'|{\mathcal {R}}(\alpha ,\beta ,\gamma )|jm\rangle =\langle jm'|T^{\dagger }{\mathcal {R}}(\alpha ,\beta ,\gamma )T|jm\rangle =(-1)^{m'-m}\langle j,-m'|{\mathcal {R}}(\alpha ,\beta ,\gamma )|j,-m\rangle ^{*},$

or

$D_{m'm}^{j}(\alpha ,\beta ,\gamma )=(-1)^{m'-m}D_{-m',-m}^{j}(\alpha ,\beta ,\gamma )^{*}.$

Here, we used that T is anti-unitary (hence the complex conjugation after moving $T^{\dagger }$ from ket to bra), $T|jm\rangle =(-1)^{j-m}|j,-m\rangle$ and $(-1)^{2j-m'-m}=(-1)^{m'-m}$ .

A further symmetry implies

$(-1)^{m'-m}D_{mm'}^{j}(\alpha ,\beta ,\gamma )=D_{m'm}^{j}(\gamma ,\beta ,\alpha )~.$

## Orthogonality relations

The Wigner D-matrix elements $D_{mk}^{j}(\alpha ,\beta ,\gamma )$ form a set of orthogonal functions of the Euler angles $\alpha ,\beta ,$ and $\gamma$ :

$\int _{0}^{2\pi }d\alpha \int _{0}^{\pi }d\beta \sin \beta \int _{0}^{2\pi }d\gamma \,\,D_{m'k'}^{j'}(\alpha ,\beta ,\gamma )^{\ast }D_{mk}^{j}(\alpha ,\beta ,\gamma )={\frac {8\pi ^{2}}{2j+1}}\delta _{m'm}\delta _{k'k}\delta _{j'j}.$

This is a special case of the Schur orthogonality relations.

Crucially, by the Peter–Weyl theorem, they further form a *complete* set.

The fact that $D_{mk}^{j}(\alpha ,\beta ,\gamma )$ are matrix elements of a unitary transformation from one spherical basis $|lm\rangle$ to another ${\mathcal {R}}(\alpha ,\beta ,\gamma )|lm\rangle$ is represented by the relations:

$\sum _{k}D_{m'k}^{j}(\alpha ,\beta ,\gamma )^{*}D_{mk}^{j}(\alpha ,\beta ,\gamma )=\delta _{m,m'},$

$\sum _{k}D_{km'}^{j}(\alpha ,\beta ,\gamma )^{*}D_{km}^{j}(\alpha ,\beta ,\gamma )=\delta _{m,m'}.$

The group characters for SU(2) only depend on the rotation angle *β*, being class functions, so, then, independent of the axes of rotation,

$\chi ^{j}(\beta )\equiv \sum _{m}D_{mm}^{j}(\beta )=\sum _{m}d_{mm}^{j}(\beta )={\frac {\sin \left({\frac {(2j+1)\beta }{2}}\right)}{\sin \left({\frac {\beta }{2}}\right)}},$

and consequently satisfy simpler orthogonality relations, through the Haar measure of the group,

${\frac {1}{\pi }}\int _{0}^{2\pi }d\beta \sin ^{2}\left({\frac {\beta }{2}}\right)\chi ^{j}(\beta )\chi ^{j'}(\beta )=\delta _{j'j}.$

The completeness relation is (cf. Eq. (3.95) in ref., or Eq. (4.10.7) in ref.)

$\sum _{j}\chi ^{j}(\beta )\chi ^{j}(\beta ')=\delta (\beta -\beta '),$

whence, for $\beta '=0,$

$\sum _{j}\chi ^{j}(\beta )(2j+1)=\delta (\beta ).$

## Kronecker product of Wigner D-matrices, Clebsch–Gordan series

The set of Kronecker product matrices

$\mathbf {D} ^{j}(\alpha ,\beta ,\gamma )\otimes \mathbf {D} ^{j'}(\alpha ,\beta ,\gamma )$

forms a reducible matrix representation of the groups SO(3) and SU(2). Reduction into irreducible components is by the following equation:

$D_{mk}^{j}(\alpha ,\beta ,\gamma )D_{m'k'}^{j'}(\alpha ,\beta ,\gamma )=\sum _{J=|j-j'|}^{j+j'}\langle jmj'm'|J\left(m+m'\right)\rangle \langle jkj'k'|J\left(k+k'\right)\rangle D_{\left(m+m'\right)\left(k+k'\right)}^{J}(\alpha ,\beta ,\gamma )$

The symbol $\langle j_{1}m_{1}j_{2}m_{2}|j_{3}m_{3}\rangle$ is a Clebsch–Gordan coefficient.

## Relation to spherical harmonics and Legendre polynomials

For integer values of l , the D-matrix elements with second index equal to zero are proportional to spherical harmonics and associated Legendre polynomials, normalized to unity and with Condon and Shortley phase convention:

$D_{m0}^{\ell }(\alpha ,\beta ,\gamma )={\sqrt {\frac {4\pi }{2\ell +1}}}Y_{\ell }^{m*}(\beta ,\alpha )={\sqrt {\frac {(\ell -m)!}{(\ell +m)!}}}\,P_{\ell }^{m}(\cos {\beta })\,e^{-im\alpha }.$

This implies the following relationship for the d-matrix:

$d_{m0}^{\ell }(\beta )={\sqrt {\frac {(\ell -m)!}{(\ell +m)!}}}\,P_{\ell }^{m}(\cos {\beta }).$

A rotation of spherical harmonics $\langle \theta ,\phi |\ell m'\rangle$ then is effectively a composition of two rotations,

$\sum _{m'=-\ell }^{\ell }Y_{\ell }^{m'}(\theta ,\phi )~D_{m'~m}^{\ell }(\alpha ,\beta ,\gamma ).$

When both indices are set to zero, the Wigner D-matrix elements are given by ordinary Legendre polynomials:

$D_{0,0}^{\ell }(\alpha ,\beta ,\gamma )=d_{0,0}^{\ell }(\beta )=P_{\ell }(\cos \beta ).$

In the present convention of Euler angles, $\alpha$ is a longitudinal angle and $\beta$ is a colatitudinal angle (spherical polar angles in the physical definition of such angles). This is one of the reasons that the *z*-*y*-*z* convention is used frequently in molecular physics. From the time-reversal property of the Wigner D-matrix follows immediately

$\left(Y_{\ell }^{m}\right)^{*}=(-1)^{m}Y_{\ell }^{-m}.$

There exists a more general relationship to the spin-weighted spherical harmonics:

$D_{ms}^{\ell }(\alpha ,\beta ,-\gamma )=(-1)^{s}{\sqrt {\frac {4\pi }{2{\ell }+1}}}{}_{s}Y_{\ell }^{m}(\beta ,\alpha )e^{is\gamma }.$

## Connection with transition probability under rotations

The absolute square of an element of the D-matrix,

$F_{mm'}(\beta )=|D_{mm'}^{j}(\alpha ,\beta ,\gamma )|^{2},$

gives the probability that a system with spin j prepared in a state with spin projection m along some direction will be measured to have a spin projection $m'$ along a second direction at an angle $\beta$ to the first direction. The set of quantities $F_{mm'}$ itself forms a real symmetric matrix, that depends only on the Euler angle $\beta$ , as indicated.

Remarkably, the eigenvalue problem for the F matrix can be solved completely:

$\sum _{m'=-j}^{j}F_{mm'}(\beta )f_{\ell }^{j}(m')=P_{\ell }(\cos \beta )f_{\ell }^{j}(m)\qquad (\ell =0,1,\ldots ,2j).$

Here, the eigenvector, $f_{\ell }^{j}(m)$ , is a scaled and shifted discrete Chebyshev polynomial, and the corresponding eigenvalue, $P_{\ell }(\cos \beta )$ , is the Legendre polynomial.

## Relation to Bessel functions

In the limit when $\ell \gg m,m^{\prime }$ , one obtains

$D_{mm'}^{\ell }(\alpha ,\beta ,\gamma )\approx e^{-im\alpha -im'\gamma }J_{m-m'}(\ell \beta )$

where $J_{m-m'}(\ell \beta )$ is the Bessel function and $\ell \beta$ is finite.

## List of d-matrix elements

Using sign convention of Wigner, et al. the d-matrix elements $d_{m'm}^{j}(\theta )$ for *j* = 1/2, 1, 3/2, and 2 are given below.

For *j* = 1/2

${\begin{aligned}d_{{\frac {1}{2}},{\frac {1}{2}}}^{\frac {1}{2}}&=\cos {\frac {\theta }{2}}\\[6pt]d_{{\frac {1}{2}},-{\frac {1}{2}}}^{\frac {1}{2}}&=-\sin {\frac {\theta }{2}}\end{aligned}}$

For *j* = 1

${\begin{aligned}d_{1,1}^{1}&={\frac {1}{2}}(1+\cos \theta )\\[6pt]d_{1,0}^{1}&=-{\frac {1}{\sqrt {2}}}\sin \theta \\[6pt]d_{1,-1}^{1}&={\frac {1}{2}}(1-\cos \theta )\\[6pt]d_{0,0}^{1}&=\cos \theta \end{aligned}}$

For *j* = 3/2

${\begin{aligned}d_{{\frac {3}{2}},{\frac {3}{2}}}^{\frac {3}{2}}&={\frac {1}{2}}(1+\cos \theta )\cos {\frac {\theta }{2}}\\[6pt]d_{{\frac {3}{2}},{\frac {1}{2}}}^{\frac {3}{2}}&=-{\frac {\sqrt {3}}{2}}(1+\cos \theta )\sin {\frac {\theta }{2}}\\[6pt]d_{{\frac {3}{2}},-{\frac {1}{2}}}^{\frac {3}{2}}&={\frac {\sqrt {3}}{2}}(1-\cos \theta )\cos {\frac {\theta }{2}}\\[6pt]d_{{\frac {3}{2}},-{\frac {3}{2}}}^{\frac {3}{2}}&=-{\frac {1}{2}}(1-\cos \theta )\sin {\frac {\theta }{2}}\\[6pt]d_{{\frac {1}{2}},{\frac {1}{2}}}^{\frac {3}{2}}&={\frac {1}{2}}(3\cos \theta -1)\cos {\frac {\theta }{2}}\\[6pt]d_{{\frac {1}{2}},-{\frac {1}{2}}}^{\frac {3}{2}}&=-{\frac {1}{2}}(3\cos \theta +1)\sin {\frac {\theta }{2}}\end{aligned}}$

For *j* = 2

${\begin{aligned}d_{2,2}^{2}&={\frac {1}{4}}\left(1+\cos \theta \right)^{2}\\[6pt]d_{2,1}^{2}&=-{\frac {1}{2}}\sin \theta \left(1+\cos \theta \right)\\[6pt]d_{2,0}^{2}&={\sqrt {\frac {3}{8}}}\sin ^{2}\theta \\[6pt]d_{2,-1}^{2}&=-{\frac {1}{2}}\sin \theta \left(1-\cos \theta \right)\\[6pt]d_{2,-2}^{2}&={\frac {1}{4}}\left(1-\cos \theta \right)^{2}\\[6pt]d_{1,1}^{2}&={\frac {1}{2}}\left(2\cos ^{2}\theta +\cos \theta -1\right)\\[6pt]d_{1,0}^{2}&=-{\sqrt {\frac {3}{8}}}\sin 2\theta \\[6pt]d_{1,-1}^{2}&={\frac {1}{2}}\left(-2\cos ^{2}\theta +\cos \theta +1\right)\\[6pt]d_{0,0}^{2}&={\frac {1}{2}}\left(3\cos ^{2}\theta -1\right)\end{aligned}}$

Wigner d-matrix elements with swapped lower indices are found with the relation:

$d_{m',m}^{j}=(-1)^{m-m'}d_{m,m'}^{j}=d_{-m,-m'}^{j}.$

## Symmetries and special cases

${\begin{aligned}d_{m',m}^{j}(\pi )&=(-1)^{j-m}\delta _{m',-m}\\[6pt]d_{m',m}^{j}(\pi -\beta )&=(-1)^{j+m'}d_{m',-m}^{j}(\beta )\\[6pt]d_{m',m}^{j}(\pi +\beta )&=(-1)^{j-m}d_{m',-m}^{j}(\beta )\\[6pt]d_{m',m}^{j}(2\pi +\beta )&=(-1)^{2j}d_{m',m}^{j}(\beta )\\[6pt]d_{m',m}^{j}(-\beta )&=d_{m,m'}^{j}(\beta )=(-1)^{m'-m}d_{m',m}^{j}(\beta )\end{aligned}}$
