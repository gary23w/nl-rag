---
title: "Initial value theorem"
source: https://en.wikipedia.org/wiki/Initial_value_theorem
domain: laplace-transform
license: CC-BY-SA-4.0
tags: laplace transform, inverse laplace transform, transfer function, final value theorem
fetched: 2026-07-02
---

# Initial value theorem

In mathematical analysis, the **initial value theorem** is a theorem used to relate frequency domain expressions to the time domain behavior as time approaches zero.

Let

$F(s)=\int _{0}^{\infty }f(t)e^{-st}\,dt$

be the (one-sided) Laplace transform of *ƒ*(*t*). If f is bounded on $(0,\infty )$ (or if just $f(t)=O(e^{ct})$ ) and $\lim _{t\to 0^{+}}f(t)$ exists then the initial value theorem says

$\lim _{t\,\to \,0}f(t)=\lim _{s\to \infty }{sF(s)}.$

## Proofs

### Proof using dominated convergence theorem and assuming that function is bounded

Suppose first that f is bounded, i.e. $\lim _{t\to 0^{+}}f(t)=\alpha$ . A change of variable in the integral $\int _{0}^{\infty }f(t)e^{-st}\,dt$ shows that

$sF(s)=\int _{0}^{\infty }f\left({\frac {t}{s}}\right)e^{-t}\,dt$

.

Since f is bounded, the Dominated Convergence Theorem implies that

$\lim _{s\to \infty }sF(s)=\int _{0}^{\infty }\alpha e^{-t}\,dt=\alpha .$

### Proof using elementary calculus and assuming that function is bounded

Of course we don't really need DCT here, one can give a very simple proof using only elementary calculus:

Start by choosing A so that $\int _{A}^{\infty }e^{-t}\,dt<\epsilon$ , and then note that $\lim _{s\to \infty }f\left({\frac {t}{s}}\right)=\alpha$ *uniformly* for $t\in (0,A]$ .

### Generalizing to non-bounded functions that have exponential order

The theorem assuming just that $f(t)=O(e^{ct})$ follows from the theorem for bounded f :

Define $g(t)=e^{-ct}f(t)$ . Then g is bounded, so we've shown that $g(0^{+})=\lim _{s\to \infty }sG(s)$ . But $f(0^{+})=g(0^{+})$ and $G(s)=F(s+c)$ , so

$\lim _{s\to \infty }sF(s)=\lim _{s\to \infty }(s-c)F(s)=\lim _{s\to \infty }sF(s+c)=\lim _{s\to \infty }sG(s),$

since $\lim _{s\to \infty }F(s)=0$ .
