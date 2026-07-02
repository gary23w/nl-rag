---
title: "Harmonic analysis"
source: https://en.wikipedia.org/wiki/Harmonic_analysis
domain: harmonic-analysis
license: CC-BY-SA-4.0
tags: harmonic analysis, fourier transform, fourier series, pontryagin duality
fetched: 2026-07-02
---

# Harmonic analysis

**Harmonic analysis** is an area of mathematical analysis that emerged from the study of harmonic functions, and especially their boundary behavior. The methods of harmonic analysis decompose functions and related objects, such as measures, into components based on symmetries, scales, spectra, or oscillation. It is also concerned with the analytic estimates for operators arising from such decompositions. Basic examples include Fourier series and the Fourier transform, while modern harmonic analysis also studies maximal functions, singular integrals, oscillatory integrals, Fourier multipliers, Littlewood–Paley theory, and spectral decompositions.

A related tradition is **abstract harmonic analysis** where the emphasis is on functions and representations on topological groups, including Pontryagin duality, the Peter–Weyl theorem, and Plancherel-type theorems. Harmonic analysis overlaps substantially with Fourier analysis, real analysis, functional analysis, partial differential equations, potential theory, ergodic theory, representation theory, and number theory.

## Overview

Harmonic analysis shares many methods with Fourier analysis, which is also concerned with the decomposition of functions into frequencies or harmonics. It differs from Fourier analysis chiefly in the kinds of functions considered and the types of questions addressed. Fourier analysis has a basic form in Hilbert space, where orthogonality and Plancherel's theorem are central, and studies objects close to the orthogonal frequency decomposition, such as multipliers and convolutions and linear constant-coefficient partial differential equations. In contrast, harmonic analysis often studies Fourier-like decompositions in situations where orthogonality alone is not enough. As a result, it often must look for finer kinds of decompositions and properties of functions than those of Fourier theory.

One source of harmonic analysis, and especially of its real-variable tradition, is the study of harmonic functions and classical potential theory. In particular, the Poisson integral formula represents a harmonic function in a disk or half-space in terms of boundary data. But the boundary behavior of harmonic functions, and of the Poisson kernel, is often more delicate than Fourier methods alone can resolve. Thus questions about the convergence of Poisson integrals, the existence of boundary values, and the behavior of conjugate harmonic functions lead to maximal estimates and singular integral operators.

Modern harmonic analysis is usually concerned with real variable methods first encountered the study of harmonic functions. The Poisson integral sits between real and complex methods: complex analysis gives powerful tools for holomorphic and harmonic functions, while boundary convergence and estimates in *L**p*, weak *L*1, and related spaces often require real-variable methods. The real variable theory is also apparent in the related Hilbert transform, which arises in the theory of conjugate harmonic functions and boundary values of holomorphic functions. These transforms became a prototype for more general singular integral operators, which the real variable methods of harmonic analysis are more suited for. In higher dimensions, analogous operators include the Riesz transforms, which are connected with the derivatives of harmonic and Newtonian potentials.

One ingredient is Hardy–Littlewood maximal function. Maximal functions are used to control pointwise convergence, differentiation of integrals, and boundary limits of harmonic or subharmonic functions. They also provide a model for many later estimates in real-variable analysis, including weak-type inequalities, interpolation arguments, and weighted norm inequalities.

The theory of Calderón–Zygmund operators is one of the main developments in the analytic treatment of singular integral operators. This theory gives conditions under which singular integral operators are bounded on spaces such as *L**p* and related function spaces. It handles the Hilbert transform, Riesz transforms, many convolution operators, and singular integral operators arising in elliptic and parabolic partial differential equations.

Littlewood–Paley theory is another component of harmonic analysis. It seeks to decompose functions by scale or frequency and estimating square functions built from the resulting pieces. This technique is used together with Fourier theory, but replaces the orthogonality arguments of Fourier theory with almost-orthogonality methods that are suited to situations where orthogonality is no longer available, such as $L^{p}$ where $p\neq 2$ . The kind of decompositions involved are often finer than the Hilbert-space methods that suffice for many basic questions in Fourier analysis.

The Fourier transform remains a fundamental tool in harmonic analysis. But much of modern real-variable harmonic analysis is concerned less with explicit Fourier inversion than with estimates for operators. This distinguishes it from classical Fourier analysis and also from abstract harmonic analysis, where the emphasis is on symmetry, locally compact groups, and representation theory.

## Examples

### Decomposition and singular integrals

A real-variable method in harmonic analysis is to decompose a function into a controlled part and a collection of localized exceptional parts. One example is the Calderón–Zygmund decomposition. Given an integrable function f and a threshold $\lambda >0$ , one selects intervals or cubes on which the average size of f is larger than $\lambda$ . The function is then written schematically as

$f=g+\sum _{j}b_{j}.$

Here g is the "good" part: it agrees with f away from the selected cubes and is bounded in size by a constant multiple of $\lambda$ . Each $b_{j}$ is a "bad" part supported on one of the selected cubes, but it has cancellation:

$\int b_{j}=0.$

The cubes occupy a set whose total measure is controlled by $\|f\|_{1}/\lambda$ . Thus the places where f is too large are localized, while the remaining part is bounded and easier to estimate.

To estimate an operator such as a singular integral, one treats g using Hilbert-space or $L^{2}$ estimates, where orthogonality and boundedness are available. The localized terms $b_{j}$ are handled separately: near their supporting cubes, the total measure is small, while far from those cubes their mean-zero cancellation reduces the size of the operator. In this way a function is split locally according to size, before it is decomposed globally into frequencies. This local-global decomposition is characteristic of many arguments in harmonic analysis.

For example, the Hilbert transform is not bounded in $L^{1}$ , but it does map into weak-type $L^{1,\infty }$ . A proof takes a function $f\in L^{1}\cap L^{2}$ and decomposes it into a $\lambda$ -bounded part plus a $2\lambda$ mean-bounded part over a collection of subintervals, $f=g+b$ . One then has $\|g\|_{2}^{2}\leq C\|g\|_{\infty }\|g\|_{1}\leq C\lambda \|f\|_{1}$ which bounds the $L^{2}$ norm of g in terms of the $L^{1}$ norm of f . The Hilbert transform is bounded on $L^{2}$ , so the good part g inherits the same bound. Because the bad set has measure controlled by $\lambda$ , for the weak-type bound it is sufficient to estimate the Hilbert transform of b *away* from the bad set, and here cancellation produces an estimate like $\int _{\mathbb {R} \setminus E_{*}}|Hg|\leq C\|f\|_{1}$ where $E_{*}$ is a slight enlargement of the bad set (say doubling the size of every interval about the center).

### Fourier restriction problems

Fourier restriction problems illustrate another way in which harmonic analysis extends classical Fourier analysis. In elementary Fourier analysis, the Fourier transform is first studied as a transform on functions on a whole space, such as $\mathbb {R} ^{n}$ , with basic results concerning inversion, convolution, Plancherel's theorem, and the decomposition of functions into frequencies. A restriction problem asks the question of whether the Fourier transform of a function can be meaningfully restricted to a lower-dimensional set in frequency space, such as a sphere, cone, or paraboloid.

If $f\in L^{1}(\mathbb {R} ^{n})$ , then ${\widehat {f}}$ is continuous, so its restriction to a smooth surface S is well defined. The problem becomes nontrivial for functions in $L^{p}(\mathbb {R} ^{n})$ , where the Fourier transform need not be given by an ordinary pointwise-defined function. One asks whether an estimate of the form

$\|{\widehat {f}}|_{S}\|_{L^{q}(S,d\sigma )}\leq C\|f\|_{L^{p}(\mathbb {R} ^{n})}$

can hold, where $d\sigma$ is surface measure on S . Equivalently, by duality, one studies the extension operator

$Eg(x)=\int _{S}g(\xi )e^{2\pi ix\cdot \xi }\,d\sigma (\xi )$

and asks for estimates such as

$\|Eg\|_{L^{r}(\mathbb {R} ^{n})}\leq C\|g\|_{L^{q}(S)}.$

In this formulation, $Eg$ is a superposition of plane waves whose frequencies lie on the surface S .

The Fourier-analytic aspect of the problem is the oscillatory representation itself. A function is described by waves with prescribed frequencies, and different choices of S correspond to different geometric or physical situations. For example, the paraboloid is connected with the free Schrödinger equation, while the cone is connected with the wave equation. The harmonic-analytic aspect is the estimate theory, determining which exponents are possible and how the answer depends on curvature, cancellation, scaling, and the way wave packets overlap in physical space.

Frequencies concentrated on a flat hyperplane do not disperse like frequencies on a curved hypersurface. For curved surfaces, oscillation can force cancellation and spreading, allowing estimates that would fail for flat sets. A basic result of this type is the Stein–Tomas theorem, which gives an $L^{2}$ restriction theorem for the sphere. More advanced restriction problems involve bilinear and multilinear estimates, wave-packet decompositions, induction on scales, and connections with Kakeya-type geometry.

Thus in Fourier restriction problems, Fourier analysis supplies the transform and the frequency-space formulation, while harmonic analysis studies the resulting inequalities and the fine behavior of the associated operators.

## Connections to other areas

### Real analysis

Harmonic analysis supplies analytic tools for results relating to the Lebesgue measure. One is the Lebesgue differentiation theorem, which states that a locally integrable function is almost everywhere equal to the limit of its average over balls. The proof uses weak-type estimates and maximal functions to control the almost everywhere convergence.

### Ergodic theory

Harmonic analysis is used in classical results of ergodic theory. The maximal ergodic theorem is analogous to the Hardy–Littlewood maximal theorem: it bounds the measure of the set on which a supremum of ergodic averages is large. Such maximal estimates are used in proofs of the Birkhoff ergodic theorem, where they help pass from convergence on a dense class of functions to almost-everywhere convergence.

Calderón showed that harmonic analytic estimates for translation-invariant operators can be transferred to ergodic averages associated with measure-preserving transformations. This allows harmonic-analytic estimates for maximal functions and singular integrals to be used in ergodic settings.

Later work on ergodic averages has focused on studying the oscillation and deviations around those averages. This involves estimating short variations in $L^{p}$ norms, using techniques of harmonic analysis.

### Sobolev spaces and partial differential equations

Harmonic analysis is closely connected with Sobolev spaces and the regularity theory of partial differential equations. Riesz potentials and fractional integral operators are used to prove Sobolev-type inequalities, including embeddings between *L**p* spaces and spaces of weakly differentiable functions.

Singular integral estimates also give information about weak derivatives. For example, Calderón–Zygmund operators are used to obtain *L**p* estimates for derivatives of solutions to elliptic equations from estimates on the equation itself. In this way, harmonic-analytic bounds for singular integrals become regularity estimates for solutions of differential equations.

Littlewood–Paley theory gives another description of Sobolev and related function spaces by decomposing functions into pieces at different scales or frequencies. This point of view is especially useful for fractional Sobolev spaces, Besov spaces, Triebel–Lizorkin spaces, and nonlinear problems where estimates must be made scale by scale.

## Abstract harmonic analysis

Harmonic analysis is used in a different, but related, sense in mathematics, to describe how real or complex functions (often on very general domains) can be studied using symmetries such as translations or rotations. An example is the decomposition of a function on Euclidean space into spherical harmonics, which are eigenfunctions of the Laplace operator.

Abstract harmonic analysis extends the classical spherical harmonic decompositions to functions on spaces associated to other groups. In this way, the theory is close to representation theory and functional analysis.

One of the most modern branches of harmonic analysis, having its roots in the mid-20th century, is analysis on topological groups. The core motivating ideas are the various Fourier transforms, which can be generalized to a transform of functions defined on Hausdorff locally compact topological groups.

One of the major results in the theory of functions on abelian locally compact groups is called Pontryagin duality. Harmonic analysis studies the properties of that duality. Different generalization of Fourier transforms attempts to extend those features to different settings, for instance, first to the case of general abelian topological groups and second to the case of non-abelian Lie groups.

Harmonic analysis is closely related to the theory of unitary group representations for general non-abelian locally compact groups. For compact groups, the Peter–Weyl theorem explains how one may get harmonics by choosing one irreducible representation out of each equivalence class of representations. This choice of harmonics enjoys some of the valuable properties of the classical Fourier transform in terms of carrying convolutions to pointwise products or otherwise showing a certain understanding of the underlying group structure. See also: Non-commutative harmonic analysis.

If the group is neither abelian nor compact, no general satisfactory theory is currently known ("satisfactory" means at least as strong as the Plancherel theorem). However, many specific cases have been analyzed, for example, SL*n*. In this case, representations in infinite dimensions play a crucial role.

Abstract harmonic analysis also has applications in number theory. In Tate's thesis, questions about L-functions are formulated using harmonic analysis on the adele ring and idele group.

Harmonic analysis, in this latter sense, is closely connected with spectral theory, especially through the study of the Laplacian and other differential operators. On Euclidean spaces, manifolds, symmetric spaces, and graphs, questions about eigenfunctions, eigenvalues, heat kernels, and wave propagation are often treated using harmonic-analytic methods. This point of view includes problems such as hearing the shape of a drum and the analysis of spherical functions on symmetric spaces.

On Euclidean space, harmonic analysis also studies phenomena special to the Fourier transform on **R***n*, such as rotation invariance, restriction estimates, radial Fourier transforms, Bessel functions, and spherical harmonics. These topics connect the real-variable theory with classical special functions and with partial differential equations.

Several more specialized areas use harmonic-analytic methods. Harmonic analysis on symmetric spaces and locally compact groups is related to representation theory. Harmonic analysis on tube domains is connected with Hardy spaces and several complex variables. Automorphic forms may also be viewed as harmonic-analytic objects associated with arithmetic symmetry groups, although they are usually treated as a separate subject closely connected with number theory and the Langlands program.
