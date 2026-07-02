---
title: "Kantorovich theorem"
source: https://en.wikipedia.org/wiki/Kantorovich_theorem
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Kantorovich theorem

The **Kantorovich theorem**, or Newton–Kantorovich theorem, is a mathematical statement on the semi-local convergence of Newton's method. It was first stated by Leonid Kantorovich in 1948. It is similar to the form of the Banach fixed-point theorem, although it states existence and uniqueness of a zero rather than a fixed point.

Newton's method constructs a sequence of points that under certain conditions will converge to a solution x of an equation $f(x)=0$ or a vector solution of a system of equation $F(x)=0$ . The Kantorovich theorem gives conditions on the initial point of this sequence. If those conditions are satisfied then a solution exists close to the initial point and the sequence converges to that point.

## Assumptions

Let $X\subset \mathbb {R} ^{n}$ be an open subset and $F:X\subset \mathbb {R} ^{n}\to \mathbb {R} ^{n}$ a differentiable function with a Jacobian $F^{\prime }(\mathbf {x} )$ that is locally Lipschitz continuous (for instance if F is twice differentiable). That is, it is assumed that for any $x\in X$ there is an open subset $U\subset X$ such that $x\in U$ and there exists a constant $L>0$ such that for any $\mathbf {x} ,\mathbf {y} \in U$

$\|F'(\mathbf {x} )-F'(\mathbf {y} )\|\leq L\;\|\mathbf {x} -\mathbf {y} \|$

holds. The norm on the left is the operator norm. In other words, for any vector $\mathbf {v} \in \mathbb {R} ^{n}$ the inequality

$\|F'(\mathbf {x} )(\mathbf {v} )-F'(\mathbf {y} )(\mathbf {v} )\|\leq L\;\|\mathbf {x} -\mathbf {y} \|\,\|\mathbf {v} \|$

must hold.

Now choose any initial point $\mathbf {x} _{0}\in X$ . Assume that $F'(\mathbf {x} _{0})$ is invertible and construct the Newton step $\mathbf {h} _{0}=-F'(\mathbf {x} _{0})^{-1}F(\mathbf {x} _{0}).$

The next assumption is that not only the next point $\mathbf {x} _{1}=\mathbf {x} _{0}+\mathbf {h} _{0}$ but the entire ball $B(\mathbf {x} _{1},\|\mathbf {h} _{0}\|)$ is contained inside the set X . Let M be the Lipschitz constant for the Jacobian over this ball (assuming it exists).

As a last preparation, construct recursively, as long as it is possible, the sequences $(\mathbf {x} _{k})_{k}$ , $(\mathbf {h} _{k})_{k}$ , $(\alpha _{k})_{k}$ according to

${\begin{alignedat}{2}\mathbf {h} _{k}&=-F'(\mathbf {x} _{k})^{-1}F(\mathbf {x} _{k})\\[0.4em]\alpha _{k}&=M\,\|F'(\mathbf {x} _{k})^{-1}\|\,\|\mathbf {h} _{k}\|\\[0.4em]\mathbf {x} _{k+1}&=\mathbf {x} _{k}+\mathbf {h} _{k}.\end{alignedat}}$

## Statement

Now if $\alpha _{0}\leq {\tfrac {1}{2}}$ then

1. a solution $\mathbf {x} ^{*}$ of $F(\mathbf {x} ^{*})=0$ exists inside the closed ball ${\bar {B}}(\mathbf {x} _{1},\|\mathbf {h} _{0}\|)$ and
2. the Newton iteration starting in $\mathbf {x} _{0}$ converges to $\mathbf {x} ^{*}$ with at least linear order of convergence.

A statement that is more precise but slightly more difficult to prove uses the roots $t^{\ast }\leq t^{**}$ of the quadratic polynomial

$p(t)=\left({\tfrac {1}{2}}L\|F'(\mathbf {x} _{0})^{-1}\|^{-1}\right)t^{2}-t+\|\mathbf {h} _{0}\|$

,

$t^{\ast /**}={\frac {2\|\mathbf {h} _{0}\|}{1\pm {\sqrt {1-2\alpha _{0}}}}}$

and their ratio

$\theta ={\frac {t^{*}}{t^{**}}}={\frac {1-{\sqrt {1-2\alpha _{0}}}}{1+{\sqrt {1-2\alpha _{0}}}}}.$

Then

1. a solution $\mathbf {x} ^{*}$ exists inside the closed ball ${\bar {B}}(\mathbf {x} _{1},\theta \|\mathbf {h} _{0}\|)\subset {\bar {B}}(\mathbf {x} _{0},t^{*})$
2. it is unique inside the bigger ball $B(\mathbf {x} _{0},t^{*\ast })$
3. and the convergence to the solution of F is dominated by the convergence of the Newton iteration of the quadratic polynomial $p(t)$ towards its smallest root $t^{\ast }$ , if $t_{0}=0,\,t_{k+1}=t_{k}-{\tfrac {p(t_{k})}{p'(t_{k})}}$ , then $\|\mathbf {x} _{k+p}-\mathbf {x} _{k}\|\leq t_{k+p}-t_{k}.$
4. The quadratic convergence is obtained from the error estimate $\|\mathbf {x} _{n+1}-\mathbf {x} ^{*}\|\leq \theta ^{2^{n}}\|\mathbf {x} _{n+1}-\mathbf {x} _{n}\|\leq {\frac {\theta ^{2^{n}}}{2^{n}}}\|\mathbf {h} _{0}\|.$

## Corollary

In 1986, Yamamoto proved that the error evaluations of the Newton method such as Doring (1969), Ostrowski (1971, 1973), Gragg-Tapia (1974), Potra-Ptak (1980), Miel (1981), Potra (1984), can be derived from the Kantorovich theorem.

## Generalizations

There is a *q*-analog for the Kantorovich theorem. For other generalizations/variations, see Ortega & Rheinboldt (1970).

## Applications

Oishi and Tanabe claimed that the Kantorovich theorem can be applied to obtain reliable solutions of linear programming.
