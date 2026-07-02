---
title: "Plancherel theorem"
source: https://en.wikipedia.org/wiki/Plancherel_theorem
domain: harmonic-analysis
license: CC-BY-SA-4.0
tags: harmonic analysis, fourier transform, fourier series, pontryagin duality
fetched: 2026-07-02
---

# Plancherel theorem

In mathematics, the **Plancherel theorem** (sometimes called the **Parseval–Plancherel identity**) is a result in harmonic analysis, proven by Michel Plancherel in 1910. It is a generalization of Parseval's theorem; often used in the fields of science and engineering, proving the unitarity of the Fourier transform.

The theorem states that the integral of a function's squared modulus is equal to the integral of the squared modulus of its frequency spectrum. That is, if $f(x)$ is a function on the real line, and ${\widehat {f}}(\xi )$ is its frequency spectrum, then

$\int _{-\infty }^{\infty }|f(x)|^{2}\,dx=\int _{-\infty }^{\infty }|{\widehat {f}}(\xi )|^{2}\,d\xi$

## Formal definition

The Fourier transform of an *L**1* function f on the real line $\mathbb {R}$ is defined as the Lebesgue integral ${\hat {f}}(\xi )=\int _{\mathbb {R} }f(x)e^{-2\pi ix\xi }dx.$ If f belongs to both $L^{1}$ and $L^{2}$ , then the Plancherel theorem states that ${\hat {f}}$ also belongs to $L^{2}$ , and the Fourier transform is an isometry with respect to the *L*2 norm, which is to say that $\int _{-\infty }^{\infty }|f(x)|^{2}\,dx=\int _{-\infty }^{\infty }|{\widehat {f}}(\xi )|^{2}\,d\xi$

This implies that the Fourier transform restricted to $L^{1}(\mathbb {R} )\cap L^{2}(\mathbb {R} )$ has a unique extension to a linear isometric map $L^{2}(\mathbb {R} )\mapsto L^{2}(\mathbb {R} )$ , sometimes called the Plancherel transform. This isometry is actually a unitary map. In effect, this makes it possible to speak of Fourier transforms of *L**2* functions.

A proof of the theorem is available from *Rudin (1987, Chapter 9)*. The basic idea is to prove it for Gaussian distributions, and then use density. But a standard Gaussian is transformed to itself under the Fourier transformation, and the theorem is trivial in that case. Finally, the standard transformation properties of the Fourier transform then imply Plancherel for all Gaussians.

Plancherel's theorem remains valid as stated on *n*-dimensional Euclidean space $\mathbb {R} ^{n}$ . The theorem also holds more generally in locally compact abelian groups. There is also a version of the Plancherel theorem which makes sense for non-commutative locally compact groups satisfying certain technical assumptions. This is the subject of non-commutative harmonic analysis.

Due to the polarization identity, one can also apply Plancherel's theorem to the $L^{2}(\mathbb {R} )$ inner product of two functions. That is, if $f(x)$ and $g(x)$ are two $L^{2}(\mathbb {R} )$ functions, and ${\mathcal {P}}$ denotes the Plancherel transform, then $\int _{-\infty }^{\infty }f(x){\overline {g(x)}}\,dx=\int _{-\infty }^{\infty }({\mathcal {P}}f)(\xi ){\overline {({\mathcal {P}}g)(\xi )}}\,d\xi ,$ and if $f(x)$ and $g(x)$ are furthermore $L^{1}(\mathbb {R} )$ functions, then $({\mathcal {P}}f)(\xi )={\widehat {f}}(\xi )=\int _{-\infty }^{\infty }f(x)e^{-2\pi i\xi x}\,dx,$ and $({\mathcal {P}}g)(\xi )={\widehat {g}}(\xi )=\int _{-\infty }^{\infty }g(x)e^{-2\pi i\xi x}\,dx,$ so

$\int _{-\infty }^{\infty }f(x){\overline {g(x)}}\,dx=\int _{-\infty }^{\infty }{\widehat {f}}(\xi ){\overline {{\widehat {g}}(\xi )}}\,d\xi .$

## Locally compact groups

There is also a Plancherel theorem for the Fourier transform in locally compact groups. In the case of an abelian group G , there is a Pontryagin dual group ${\widehat {G}}$ of characters on G . Given a Haar measure on G , the Fourier transform of a function in $L^{1}(G)$ is ${\hat {f}}(\chi )=\int _{G}{\overline {\chi (g)}}f(g)\,dg$ for $\chi$ a character on G .

The Plancherel theorem states that there is a Haar measure on ${\widehat {G}}$ , the *dual measure* such that $\|f\|_{G}^{2}=\|{\hat {f}}\|_{\widehat {G}}^{2}$ for all $f\in L^{1}\cap L^{2}$ (and the Fourier transform is also in $L^{2}$ ).

The theorem also holds in many non-abelian locally compact groups, except that the set of irreducible unitary representations ${\widehat {G}}$ may not be a group. For example, when G is a finite group, ${\widehat {G}}$ is the set of irreducible characters. From basic character theory, if f is a class function, we have the Parseval formula $\|f\|_{G}^{2}=\|{\hat {f}}\|_{\widehat {G}}^{2}$ $\|f\|_{G}^{2}={\frac {1}{|G|}}\sum _{g\in G}|f(g)|^{2},\quad \|{\hat {f}}\|_{\widehat {G}}^{2}=\sum _{\rho \in {\widehat {G}}}(\dim \rho )^{2}|{\hat {f}}(\rho )|^{2}.$ More generally, when f is not a class function, the norm is $\|{\hat {f}}\|_{\widehat {G}}^{2}=\sum _{\rho \in {\widehat {G}}}\dim \rho \,\operatorname {tr} ({\hat {f}}(\rho )^{*}{\hat {f}}(\rho ))$ so the Plancherel measure weights each representation by its dimension.

In full generality, a Plancherel theorem is $\|f\|_{G}^{2}=\int _{\hat {G}}\|{\hat {f}}(\rho )\|_{HS}^{2}d\mu (\rho )$ where the norm is the Hilbert-Schmidt norm of the operator ${\hat {f}}(\rho )=\int _{G}f(g)\rho (g)^{*}\,dg$ and the measure $\mu$ , if one exists, is called the Plancherel measure.
