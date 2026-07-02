---
title: "Stieltjes transformation"
source: https://en.wikipedia.org/wiki/Stieltjes_transformation
domain: integral-transforms
license: CC-BY-SA-4.0
tags: integral transform, hilbert transform, hartley transform, convolution theorem
fetched: 2026-07-02
---

# Stieltjes transformation

In mathematics, the **Stieltjes transformation** *S**ρ*(*z*) of a measure of density *ρ* on a real interval I is the function of the complex variable z defined outside I by the formula

$S_{\rho }(z)=\int _{I}{\frac {\rho (t)\,dt}{t-z}},\qquad z\in \mathbb {C} \setminus I.$

## Inverse formula

Under certain conditions we can reconstitute the density function *ρ* starting from its Stieltjes transformation thanks to the inverse formula of Stieltjes–Perron. For example, if the density *ρ* is continuous throughout I, one will have inside this interval $\rho (x)=\lim _{\varepsilon \to 0^{+}}{\frac {S_{\rho }(x+i\varepsilon )-S_{\rho }(x-i\varepsilon )}{2i\pi }}.$

### Derivation of formula

Recall from basic calculus that $\int _{-\infty }^{\infty }{\frac {1}{x^{2}+1}}dx=\lim _{x\to \infty }\arctan x-\lim _{x\to -\infty }\arctan x={\tfrac {\pi }{2}}-(-{\tfrac {\pi }{2}})=\pi {\text{.}}$ Hence $f(x)={\tfrac {1}{\pi }}(x^{2}+1)^{-1}$ is the probability density function of a distribution—a Cauchy distribution. Via the change of variables $x=(t-t_{0})/\varepsilon$ we get the full family of Cauchy distributions: $1=\int _{-\infty }^{\infty }{\frac {1/\pi }{x^{2}+1}}dx=\int _{-\infty }^{\infty }{\frac {1/\pi }{({\frac {t-t_{0}}{\varepsilon }})^{2}+1}}{\frac {dx}{dt}}dt=\int _{-\infty }^{\infty }{\frac {\varepsilon /\pi }{(t-t_{0})^{2}+\varepsilon ^{2}}}dt$ As $\varepsilon \to 0^{+}$ , these tend to a Dirac distribution with the mass at $t_{0}$ . Integrating any function $\rho (t)$ against *that* would pick out the value $\rho (t_{0})$ . Rather integrating $\int _{-\infty }^{\infty }{\frac {\varepsilon /\pi }{(t-t_{0})^{2}+\varepsilon ^{2}}}\rho (t)\,dt$ for some $\varepsilon >0$ instead produces the value at $t_{0}$ for some smoothed variant of $\rho$ —the smaller the value of $\varepsilon$ , the less smoothing is applied. Used in this way, the factor ${\frac {\varepsilon /\pi }{(t-t_{0})^{2}+\varepsilon ^{2}}}$ is also known as the Poisson kernel (for the half-plane).

The denominator $(t-t_{0})^{2}+\varepsilon ^{2}$ has no real zeroes, but it has two complex zeroes $t=t_{0}\pm i\varepsilon$ , and thus there is a partial fraction decomposition ${\frac {\varepsilon /\pi }{(t-t_{0})^{2}+\varepsilon ^{2}}}={\frac {1/2\pi i}{t-(t_{0}+i\varepsilon )}}-{\frac {1/2\pi i}{t-(t_{0}-i\varepsilon )}}$ Hence for any measure $\mu$ , $\int _{\mathbb {R} }{\frac {\varepsilon /\pi }{(t-x)^{2}+\varepsilon ^{2}}}d\mu (t)={\frac {1}{2\pi i}}\int _{\mathbb {R} }\left({\frac {1}{t-(x+i\varepsilon )}}-{\frac {1}{t-(x-i\varepsilon )}}\right)d\mu (t)={\frac {S_{\mu }(x+i\varepsilon )-S_{\mu }(x-i\varepsilon )}{2\pi i}}$ If the measure $\mu$ is absolutely continuous (with respect to the Lebesgue measure) at x then as $\varepsilon \to 0^{+}$ that integral tends to the density at x . If instead the measure has a point mass at x , then the limit as $\varepsilon \to 0^{+}$ of the integral diverges, and the Stieltjes transform $S_{\mu }$ has a pole at x .

## Connections with moments of measures

If the measure of density *ρ* has moments of any order defined for each integer by the equality $m_{n}=\int _{I}t^{n}\,\rho (t)\,dt,$

then the Stieltjes transformation of *ρ* admits for each integer n the asymptotic expansion in the neighbourhood of infinity given by $S_{\rho }(z)=\sum _{k=0}^{n}{\frac {m_{k}}{z^{k+1}}}+o\left({\frac {1}{z^{n+1}}}\right).$

Under certain conditions the complete expansion as a Laurent series can be obtained: $S_{\rho }(z)=\sum _{n=0}^{\infty }{\frac {m_{n}}{z^{n+1}}}.$

## Relationships to orthogonal polynomials

The correspondence ${\textstyle (f,g)\mapsto \int _{I}f(t)g(t)\rho (t)\,dt}$ defines an inner product on the space of continuous functions on the interval I.

If {*Pn*} is a sequence of orthogonal polynomials for this product, we can create the sequence of associated secondary polynomials by the formula $Q_{n}(x)=\int _{I}{\frac {P_{n}(t)-P_{n}(x)}{t-x}}\rho (t)\,dt.$

It appears that ${\textstyle F_{n}(z)={\frac {Q_{n}(z)}{P_{n}(z)}}}$ is a Padé approximation of *S**ρ*(*z*) in a neighbourhood of infinity, in the sense that $S_{\rho }(z)-{\frac {Q_{n}(z)}{P_{n}(z)}}=O\left({\frac {1}{z^{2n+1}}}\right).$

Since these two sequences of polynomials satisfy the same recurrence relation in three terms, we can develop a continued fraction for the Stieltjes transformation whose successive convergents are the fractions *Fn*(*z*).

The Stieltjes transformation can also be used to construct from the density *ρ* an effective measure for transforming the secondary polynomials into an orthogonal system. (For more details see the article secondary measure.)
