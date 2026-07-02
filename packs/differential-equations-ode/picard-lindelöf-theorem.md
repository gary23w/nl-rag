---
title: "Picard–Lindelöf theorem"
source: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
domain: differential-equations-ode
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, laplace transform, linear differential equation
fetched: 2026-07-02
---

# Picard–Lindelöf theorem

In mathematics, specifically the study of differential equations, the **Picard–Lindelöf theorem** gives a set of sufficient (but not necessary) conditions under which an initial value problem has a unique solution. It is also known as **Picard's existence theorem**, the **Cauchy–Lipschitz theorem**, or the **existence and uniqueness theorem**.

The theorem is named after Émile Picard, Ernst Lindelöf, Rudolf Lipschitz and Augustin-Louis Cauchy.

## Theorem

Let $D\subseteq \mathbb {R} \times \mathbb {R} ^{n}$ be a closed rectangle with $(t_{0},y_{0})$ a point in the interior of $D.$ Let $f:D\to \mathbb {R} ^{n}$ be a function that is continuous in t and Lipschitz continuous in y (with Lipschitz constant independent from $t).$ Then there exists some $\varepsilon >0$ such that the initial value problem $y'(t)=f(t,y(t)),\qquad y(t_{0})=y_{0}$ has a unique solution $y(t)$ on the interval $[t_{0}-\varepsilon ,t_{0}+\varepsilon ].$

## Proof sketch

A standard proof relies on transforming the differential equation into an integral equation, then applying the Banach fixed-point theorem to prove the existence and uniqueness of solutions.

Integrating both sides of the differential equation ${\textstyle y'(t)=f(t,y(t))}$ shows that any solution to the differential equation must also satisfy the integral equation

$y(t)-y(t_{0})=\int _{t_{0}}^{t}f(s,y(s))\,ds.$

Given the hypotheses that f is continuous in t and Lipschitz continuous in y , this integral operator is a contraction (See detailed proof below) and so the Banach fixed-point theorem proves that a solution can be obtained by fixed-point iteration of successive approximations. In this context, this fixed-point iteration method is known as Picard iteration.

Set

$\varphi _{0}(t)=y_{0}$

and

$\varphi _{k+1}(t)=y_{0}+\int _{t_{0}}^{t}f(s,\varphi _{k}(s))\,ds.$

It follows from the Banach fixed-point theorem that the sequence of "Picard iterates" ${\textstyle \varphi _{k}}$ is convergent and that its limit is a solution to the original initial value problem:

$\lim _{k\to \infty }\varphi _{k}(t)=y(t)$

.

Since the Banach fixed-point theorem states that the fixed-point is unique, the solution found through this iteration is the unique solution to the differential equation given an initial value.

## Example of Picard iteration

Let $y(t)=\tan(t),$ the solution to the equation $y'(t)=1+y(t)^{2}$ with initial condition $y(t_{0})=y_{0}=0,t_{0}=0.$ Starting with $\varphi _{0}(t)=0,$ we iterate

$\varphi _{k+1}(t)=\int _{0}^{t}(1+(\varphi _{k}(s))^{2})\,ds$

so that $\varphi _{n}(t)\to y(t)$ :

$\varphi _{1}(t)=\int _{0}^{t}(1+0^{2})\,ds=t$

$\varphi _{2}(t)=\int _{0}^{t}(1+s^{2})\,ds=t+{\frac {t^{3}}{3}}$

$\varphi _{3}(t)=\int _{0}^{t}\left(1+\left(s+{\frac {s^{3}}{3}}\right)^{2}\right)\,ds=t+{\frac {t^{3}}{3}}+{\frac {2t^{5}}{15}}+{\frac {t^{7}}{63}}$

and so on. Evidently, the functions are computing the Taylor series expansion of our known solution $y=\tan(t).$ Since $\tan$ has poles at $\pm {\tfrac {\pi }{2}},$ it is not Lipschitz-continuous in the neighborhood of those points, and the iteration converges toward a local solution for $|t|<{\tfrac {\pi }{2}}$ only that is not valid over all of $\mathbb {R}$ .

## Example of non-uniqueness

To understand uniqueness of solutions, contrast the following two examples of first order ordinary differential equations for *y*(*t*). Both differential equations will possess a single stationary point *y* = 0.

First, the homogeneous linear equation ⁠*dy*/*dt*⁠ = *ay* ( $a<0$ ), a stationary solution is *y*(*t*) = 0, which is obtained for the initial condition *y*(0) = 0. Beginning with any other initial condition *y*(0) = *y*0 ≠ 0, the solution $y(t)=y_{0}e^{at}$ tends toward the stationary point *y* = 0, but it only approaches it in the limit of infinite time, so the uniqueness of solutions over all finite times is guaranteed.

By contrast for an equation in which the stationary point can be reached after a *finite* time, uniqueness of solutions does not hold. Consider the homogeneous nonlinear equation ⁠*dy*/*dt*⁠ = *ay* ⁠2/3⁠, which has at least these two solutions corresponding to the initial condition *y*(0) = 0: *y*(*t*) = 0 and

$y(t)={\begin{cases}\left({\tfrac {at}{3}}\right)^{3}&t<0\\\ \ \ \ 0&t\geq 0,\end{cases}}$

so the previous state of the system is not uniquely determined by its state at or after *t* = 0. The uniqueness theorem does not apply because the derivative of the function  *f* (*y*) = *y* ⁠2/3⁠ is not bounded in the neighborhood of *y* = 0 and therefore it is not Lipschitz continuous, violating the hypothesis of the theorem.

## Detailed proof

Let L be the Lipschitz constant of $(t,y)\mapsto f(t,y)$ with respect to $y.$ The function f is continuous as a function of $(t,y)$ . In particular, since $t\mapsto f(t,y)$ is a continuous function of t , we have that for any point $(t_{0},y_{0})$ and $\epsilon >0$ there exist $\delta >0$ such that $|f(t,y_{0})-f(t_{0},y_{0})|<\epsilon /2$ when $|t-t_{0}|<\delta$ . We have $|f(t,y)-f(t_{0},y_{0})|\leq |f(t,y)-f(t,y_{0})|+|f(t,y_{0})-f(t_{0},y_{0})|<\epsilon ,$ provided $|t-t_{0}|<\delta$ and $|y-y_{0}|<\epsilon /2L$ , which shows that f is continuous at $(t_{0},y_{0})$ .

Let $a:=1/2L$ and take any $b>0$ such that $C_{a,b}=I_{a}(t_{0})\times B_{b}(y_{0})$ is a subset of $D,$ where ${\begin{aligned}I_{a}(t_{0})&=[t_{0}-a,t_{0}+a]\\B_{b}(y_{0})&=[y_{0}-b,y_{0}+b].\end{aligned}}$ Such a set exists because $(t_{0},y_{0})$ is in the interior of $D,$ by assumption.

Let

$M=\sup _{(t,y)\in C_{a,b}}\|f(t,y)\|,$

which is the supremum of (the absolute values of) the slopes of the function. The function f attains a maximum on $C_{a,b}$ because f is continuous and $C_{a,b}$ is compact. For a later step in the proof, we need that $a<b/M,$ so if $a\geq b/M,$ then change a to $a:={\tfrac {1}{2}}\min\{1/L,\ b/M\},$ and update $I_{a}(t_{0}),$ $B_{b}(y_{0}),$ $C_{a,b},$ and M accordingly (this update will be needed at most once since M cannot increase as a result of restricting $C_{a,b}$ ).

Consider ${\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0}))$ , the function space of continuous functions $I_{a}(t_{0})\to B_{b}(y_{0}).$ We will proceed by applying the Banach fixed-point theorem using the metric on ${\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0}))$ induced by the uniform norm. Namely, for each continuous function $\varphi :I_{a}(t_{0})\to B_{b}(y_{0}),$ the norm of $\varphi$ is $\|\varphi \|_{\infty }=\sup _{t\in I_{a}}\|\varphi (t)\|.$ The *Picard operator* $\Gamma :{\mathcal {C}}{\big (}I_{a}(t_{0}),B_{b}(y_{0}){\big )}\to {\mathcal {C}}{\big (}I_{a}(t_{0}),B_{b}(y_{0}){\big )}$ is defined for each $\varphi \in {\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0}))$ by $\Gamma \varphi \in {\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0}))$ given by $\Gamma \varphi (t)=y_{0}+\int _{t_{0}}^{t}f(s,\varphi (s))\,ds\quad \forall t\in I_{a}(t_{0}).$

To apply the Banach fixed-point theorem, we must show that $\Gamma$ maps a complete non-empty metric space *X* into itself and also is a contraction mapping.

We first show that $\Gamma$ takes $B_{b}(y_{0})$ into itself in the space of continuous functions with the uniform norm. Here, $B_{b}(y_{0})$ is a closed ball in the space of continuous (and bounded) functions "centered" at the constant function $y_{0}$ . Hence we need to show that $\|\varphi -y_{0}\|_{\infty }\leq b$ implies $\left\|\Gamma \varphi (t)-y_{0}\right\|=\left\|\int _{t_{0}}^{t}f(s,\varphi (s))\,ds\right\|\leq \int _{t_{0}}^{t'}\left\|f(s,\varphi (s))\right\|ds\leq \int _{t_{0}}^{t'}M\,ds=M\left|t'-t_{0}\right|\leq Ma\leq b$

where $t'$ is some number in $[t_{0}-a,t_{0}+a]$ where the maximum is achieved. The last inequality in the chain is true since $a<b/M.$

Now let us prove that $\Gamma$ is a contraction mapping as required to apply the Banach fixed-point theorem. In particular, we want to show that there exists $0\leq q<1,$ such that $\left\|\Gamma \varphi _{1}-\Gamma \varphi _{2}\right\|_{\infty }\leq q\left\|\varphi _{1}-\varphi _{2}\right\|_{\infty }$ for all $\varphi _{1},\varphi _{2}\in {\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0})).$

Let $q=aL$ and take any $\varphi _{1},\varphi _{2}\in {\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0})).$ Take t such that

$\|\Gamma \varphi _{1}-\Gamma \varphi _{2}\|_{\infty }=\left\|\left(\Gamma \varphi _{1}-\Gamma \varphi _{2}\right)(t)\right\|.$

Then, using the definition of $\Gamma$ ,

${\begin{aligned}\left\|\left(\Gamma \varphi _{1}-\Gamma \varphi _{2}\right)(t)\right\|&=\left\|\int _{t_{0}}^{t}\left(f(s,\varphi _{1}(s))-f(s,\varphi _{2}(s))\right)ds\right\|\\&\leq \int _{t_{0}}^{t}\left\|f\left(s,\varphi _{1}(s)\right)-f\left(s,\varphi _{2}(s)\right)\right\|ds\\&\leq L\int _{t_{0}}^{t}\left\|\varphi _{1}(s)-\varphi _{2}(s)\right\|ds&&{\text{since }}f{\text{ is Lipschitz-continuous}}\\&\leq L\int _{t_{0}}^{t}\left\|\varphi _{1}-\varphi _{2}\right\|_{\infty }\,ds\\&\leq La\left\|\varphi _{1}-\varphi _{2}\right\|_{\infty },\end{aligned}}$

where $t-t_{0}\leq a,$ because the domains of $\phi _{1},\phi _{2}$ are both $I_{a}(t_{0})\times B_{b}(y_{0}).$ By definition, $q=aL,$ and $a<1/L,$ so $q<1.$ Therefore, $\Gamma$ is a contraction.

We have established that the Picard's operator is a contraction on the Banach spaces with the metric induced by the uniform norm. This allows us to apply the Banach fixed-point theorem to conclude that the operator has a unique fixed point. In particular, there is a unique function $\varphi \in {\mathcal {C}}(I_{a}(t_{0}),B_{b}(y_{0}))$ such that $\Gamma \varphi =\varphi .$ Thus, $\varphi$ is the unique solution of the initial value problem, valid on the interval $I_{a}.$

## Optimization of the solution's interval

We wish to remove the dependence of the interval *Ia* on *L*. To this end, there is a corollary of the Banach fixed-point theorem: if an operator *T**n* is a contraction for some *n* in **N**, then *T* has a unique fixed point. Before applying this theorem to the Picard operator, recall the following:

**Lemma**— $\left\|\Gamma ^{m}\varphi _{1}(t)-\Gamma ^{m}\varphi _{2}(t)\right\|\leq {\frac {L^{m}|t-t_{0}|^{m}}{m!}}\left\|\varphi _{1}-\varphi _{2}\right\|$ for all $t\in [t_{0}-\alpha ,t_{0}+\alpha ]$

*Proof.* Induction on *m*. For the base of the induction (*m* = 1) we have already seen this, so suppose the inequality holds for *m* − 1, then we have: ${\begin{aligned}\left\|\Gamma ^{m}\varphi _{1}(t)-\Gamma ^{m}\varphi _{2}(t)\right\|&=\left\|\Gamma \Gamma ^{m-1}\varphi _{1}(t)-\Gamma \Gamma ^{m-1}\varphi _{2}(t)\right\|\\&\leq \left|\int _{t_{0}}^{t}\left\|f\left(s,\Gamma ^{m-1}\varphi _{1}(s)\right)-f\left(s,\Gamma ^{m-1}\varphi _{2}(s)\right)\right\|ds\right|\\&\leq L\left|\int _{t_{0}}^{t}\left\|\Gamma ^{m-1}\varphi _{1}(s)-\Gamma ^{m-1}\varphi _{2}(s)\right\|ds\right|\\&\leq L\left|\int _{t_{0}}^{t}{\frac {L^{m-1}|s-t_{0}|^{m-1}}{(m-1)!}}\left\|\varphi _{1}-\varphi _{2}\right\|ds\right|\\&\leq {\frac {L^{m}|t-t_{0}|^{m}}{m!}}\left\|\varphi _{1}-\varphi _{2}\right\|.\end{aligned}}$

By taking a supremum over $t\in [t_{0}-\alpha ,t_{0}+\alpha ]$ we see that $\left\|\Gamma ^{m}\varphi _{1}-\Gamma ^{m}\varphi _{2}\right\|\leq {\frac {L^{m}\alpha ^{m}}{m!}}\left\|\varphi _{1}-\varphi _{2}\right\|$ .

This inequality assures that for some large *m*, ${\frac {L^{m}\alpha ^{m}}{m!}}<1,$ and hence Γ*m* will be a contraction. So by the previous corollary Γ will have a unique fixed point. Finally, we have been able to optimize the interval of the solution by taking *α* = min{*a*, ⁠*b*/*M*⁠}.

In the end, this result shows the interval of definition of the solution does not depend on the Lipschitz constant of the field, but only on the interval of definition of the field and its maximum absolute value.

## Other existence theorems

The Picard–Lindelöf theorem shows that the solution exists and that it is unique. The Peano existence theorem shows only existence, not uniqueness, but it assumes only that  *f*  is continuous in y, instead of Lipschitz continuous. For example, the right-hand side of the equation ⁠*dy*/*dt*⁠ = *y* ⁠1/3⁠ with initial condition *y*(0) = 0 is continuous but not Lipschitz continuous. Indeed, rather than being unique, this equation has at least three solutions:

$y(t)=0,\qquad y(t)=\pm \left({\tfrac {2}{3}}t\right)^{\frac {3}{2}}$

.

Even more general is Carathéodory's existence theorem, which proves existence (in a more general sense) under weaker conditions on  *f* . Although these conditions are only sufficient, there also exist necessary and sufficient conditions for the solution of an initial value problem to be unique, such as Okamura's theorem.

## Global existence of solution

The Picard–Lindelöf theorem ensures that solutions to initial value problems exist uniquely within a local interval $[t_{0}-\varepsilon ,t_{0}+\varepsilon ]$ , possibly dependent on each solution. The behavior of solutions beyond this local interval can vary depending on the properties of  *f*  and the domain over which  *f*  is defined. For instance, if  *f*  is globally Lipschitz, then the local interval of existence of each solution can be extended to the entire real line and all the solutions are defined over the entire **R**.

If  *f*  is only locally Lipschitz, some solutions may not be defined for certain values of *t*, even if  *f*  is smooth. For instance, the differential equation ⁠*dy*/*dt*⁠ = *y* 2 with initial condition *y*(0) = 1 has the solution *y*(*t*) = 1/(1-*t*), which is not defined at *t* = 1. Nevertheless, if  *f*  is a differentiable function defined on a compact submanifold of **R**n such that the prescribed derivative is tangent to the given submanifold, then the initial value problem has a unique solution for all time. More generally, in differential geometry: if  *f*  is a differentiable vector field defined over a domain which is a compact smooth manifold, then all its trajectories (integral curves) exist for all time.
