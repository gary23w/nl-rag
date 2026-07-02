---
title: "Jensen's inequality"
source: https://en.wikipedia.org/wiki/Jensen's_inequality
domain: expectation-maximization
license: CC-BY-SA-4.0
tags: expectation maximization algorithm, gaussian mixture model, maximum likelihood estimation, latent variable
fetched: 2026-07-02
---

# Jensen's inequality

In mathematics, **Jensen's inequality**, named after the Danish mathematician Johan Jensen, relates the value of a convex function of an integral to the integral of the convex function. It was proved by Jensen in 1906, building on an earlier proof of the same inequality for doubly-differentiable functions by Otto Hölder in 1889. Given its generality, the inequality appears in many forms depending on the context, some of which are presented below. In its simplest form the inequality states that the convex transformation of a mean is less than or equal to the mean applied after convex transformation (or equivalently, the opposite inequality for concave transformations).

Jensen's inequality generalizes the statement that the secant line of a convex function lies *above* the graph of the function, which is Jensen's inequality for two points: the secant line consists of weighted means of the convex function (for *t* ∈ [0,1]),

$tf(x_{1})+(1-t)f(x_{2}),$

while the graph of the function is the convex function of the weighted means,

$f(tx_{1}+(1-t)x_{2}).$

Thus, Jensen's inequality in this case is

$f(tx_{1}+(1-t)x_{2})\leq tf(x_{1})+(1-t)f(x_{2}).$

In the context of probability theory, it is generally stated in the following form: if *X* is a random variable and φ is a convex function, then

$\varphi (\operatorname {E} [X])\leq \operatorname {E} \left[\varphi (X)\right].$

The difference between the two sides of the inequality, $\operatorname {E} \left[\varphi (X)\right]-\varphi \left(\operatorname {E} [X]\right)$ , is called the Jensen gap.

## Statements

The classical form of Jensen's inequality involves several numbers and weights. The inequality can be stated quite generally using either the language of measure theory or (equivalently) probability. In the probabilistic setting, the inequality can be further generalized to its *full strength*.

### Finite form

For a real convex function $\varphi$ , numbers $x_{1},x_{2},\ldots ,x_{n}$ in its domain, and positive weights $a_{i}$ , Jensen's inequality can be stated as:

| $\varphi \left({\frac {\sum a_{i}x_{i}}{\sum a_{i}}}\right)\leq {\frac {\sum a_{i}\varphi (x_{i})}{\sum a_{i}}}$ |   | 1 |
|---|---|---|

and the inequality is reversed if $\varphi$ is concave, which is

| $\varphi \left({\frac {\sum a_{i}x_{i}}{\sum a_{i}}}\right)\geq {\frac {\sum a_{i}\varphi (x_{i})}{\sum a_{i}}}.$ |   | 2 |
|---|---|---|

Equality holds if and only if $x_{1}=x_{2}=\cdots =x_{n}$ or $\varphi$ is linear on a domain containing $x_{1},x_{2},\cdots ,x_{n}$ .

As a particular case, if the weights $a_{i}$ are all equal, then (**1**) and (**2**) become

| $\varphi \left({\frac {\sum x_{i}}{n}}\right)\leq {\frac {\sum \varphi (x_{i})}{n}}$ |   | 3 |
|---|---|---|

| $\varphi \left({\frac {\sum x_{i}}{n}}\right)\geq {\frac {\sum \varphi (x_{i})}{n}}$ |   | 4 |
|---|---|---|

For instance, the function log(*x*) is *concave*, so substituting $\varphi (x)=\log(x)$ in the previous formula (**4**) establishes the (logarithm of the) familiar arithmetic-mean/geometric-mean inequality:

$\log \!\left({\frac {\sum _{i=1}^{n}x_{i}}{n}}\right)\geq {\frac {\sum _{i=1}^{n}\log \!\left(x_{i}\right)}{n}}$ $\exp \!\left(\log \!\left({\frac {\sum _{i=1}^{n}x_{i}}{n}}\right)\right)\geq \exp \!\left({\frac {\sum _{i=1}^{n}\log \!\left(x_{i}\right)}{n}}\right)$ ${\frac {x_{1}+x_{2}+\cdots +x_{n}}{n}}\geq {\sqrt[{n}]{x_{1}\cdot x_{2}\cdots x_{n}}}$

A common application has x as a function of another variable (or set of variables) t, that is, $x_{i}=g(t_{i})$ . All of this carries directly over to the general continuous case: the weights *ai* are replaced by a non-negative integrable function  *f* (*x*), such as a probability distribution, and the summations are replaced by integrals.

### Measure-theoretic form

Let $(\Omega ,A,\mu )$ be a probability space. Let $f:\Omega \to \mathbb {R}$ be a $\mu$ -integrable function and $\varphi :\mathbb {R} \to \mathbb {R}$ be convex. Then: $\varphi \left(\int _{\Omega }f\,\mathrm {d} \mu \right)\leq \int _{\Omega }\varphi \circ f\,\mathrm {d} \mu$

In real analysis, we may require an estimate on

$\varphi \left(\int _{a}^{b}f(x)\,dx\right)$

where $a,b\in \mathbb {R}$ , and $f\colon [a,b]\to \mathbb {R}$ is a non-negative Lebesgue-integrable function. In this case, the Lebesgue measure of $[a,b]$ need not be 1. However, by integration by substitution, the interval can be rescaled so that it has measure 1. Then Jensen's inequality can be applied to get

$\varphi \left({\frac {1}{b-a}}\int _{a}^{b}f(x)\,dx\right)\leq {\frac {1}{b-a}}\int _{a}^{b}\varphi (f(x))\,dx.$

### Probabilistic form

The same result can be equivalently stated in a probability theory setting, by a simple change of notation. Let $(\Omega ,{\mathfrak {F}},\operatorname {P} )$ be a probability space, *X* an integrable real-valued random variable and $\varphi$ a convex function. Then $\varphi {\big (}\operatorname {E} [X]{\big )}\leq \operatorname {E} [\varphi (X)].$

In this probability setting, the measure μ is intended as a probability $\operatorname {P}$ , the integral with respect to μ as an expected value $\operatorname {E}$ , and the function f as a random variable *X*.

Note that the equality holds if and only if $\varphi$ is a linear function on some convex set A such that $P(X\in A)=1$ (which follows by inspecting the measure-theoretical proof below).

### General inequality in a probabilistic setting

More generally, let *T* be a real topological vector space, and *X* a *T*-valued integrable random variable. In this general setting, *integrable* means that there exists an element $\operatorname {E} [X]$ in *T*, such that for any element *z* in the dual space of *T*: $\operatorname {E} |\langle z,X\rangle |<\infty$ , and $\langle z,\operatorname {E} [X]\rangle =\operatorname {E} [\langle z,X\rangle ]$ . Then, for any measurable convex function φ and any sub-σ-algebra ${\mathfrak {G}}$ of ${\mathfrak {F}}$ :

$\varphi \left(\operatorname {E} \left[X\mid {\mathfrak {G}}\right]\right)\leq \operatorname {E} \left[\varphi (X)\mid {\mathfrak {G}}\right].$

Here $\operatorname {E} [\cdot \mid {\mathfrak {G}}]$ stands for the expectation conditioned to the σ-algebra ${\mathfrak {G}}$ . This general statement reduces to the previous ones when the topological vector space T is the real axis, and ${\mathfrak {G}}$ is the trivial σ-algebra {∅, Ω} (where ∅ is the empty set, and Ω is the sample space).

### A sharpened and generalized form

Let *X* be a one-dimensional random variable with mean $\mu$ and variance $\sigma ^{2}\geq 0$ . Let $\varphi (x)$ be a twice differentiable function, and define the function

$h(x)\triangleq {\frac {\varphi \left(x\right)-\varphi \left(\mu \right)}{\left(x-\mu \right)^{2}}}-{\frac {\varphi '\left(\mu \right)}{x-\mu }}.$

Then

$\sigma ^{2}\inf {\frac {\varphi ''(x)}{2}}\leq \sigma ^{2}\inf h(x)\leq E\left[\varphi \left(X\right)\right]-\varphi \left(E[X]\right)\leq \sigma ^{2}\sup h(x)\leq \sigma ^{2}\sup {\frac {\varphi ''(x)}{2}}.$

In particular, when $\varphi (x)$ is convex, then $\varphi ''(x)\geq 0$ , and the standard form of Jensen's inequality immediately follows for the case where $\varphi (x)$ is additionally assumed to be twice differentiable.

## Proofs

### Intuitive graphical proof

Jensen's inequality can be proved in several ways, and three different proofs corresponding to the different statements above will be offered. Before embarking on these mathematical derivations, however, it is worth analyzing an intuitive graphical argument based on the probabilistic case where X is a real number (see figure). Assuming a hypothetical distribution of X values, one can immediately identify the position of $\operatorname {E} [X]$ and its image $\varphi (\operatorname {E} [X])$ in the graph. Noticing that for convex mappings *Y* = *φ*(*x*) of some x values the corresponding distribution of Y values is increasingly "stretched up" for increasing values of X, it is easy to see that the distribution of Y is broader in the interval corresponding to *X* > *X*0 and narrower in *X* < *X*0 for any *X*0; in particular, this is also true for $X_{0}=\operatorname {E} [X]$ . Consequently, in this picture the expectation of Y will always shift upwards with respect to the position of $\varphi (\operatorname {E} [X])$ . A similar reasoning holds if the distribution of X covers a decreasing portion of the convex function, or both a decreasing and an increasing portion of it. This "proves" the inequality, i.e.

$\varphi (\operatorname {E} [X])\leq \operatorname {E} [\varphi (X)]=\operatorname {E} [Y],$

with equality when *φ*(*X*) is not strictly convex, e.g. when it is a straight line, or when X follows a degenerate distribution (i.e. is a constant).

The proofs below formalize this intuitive notion.

### Proof 1 (finite form)

If *λ*1 and *λ*2 are two arbitrary nonnegative real numbers such that *λ*1 + *λ*2 = 1 then convexity of φ implies

$\forall x_{1},x_{2}:\qquad \varphi \left(\lambda _{1}x_{1}+\lambda _{2}x_{2}\right)\leq \lambda _{1}\,\varphi (x_{1})+\lambda _{2}\,\varphi (x_{2}).$

This can be generalized: if *λ*1, ..., *λn* are nonnegative real numbers such that *λ*1 + ... + *λn* = 1, then

$\varphi (\lambda _{1}x_{1}+\lambda _{2}x_{2}+\cdots +\lambda _{n}x_{n})\leq \lambda _{1}\,\varphi (x_{1})+\lambda _{2}\,\varphi (x_{2})+\cdots +\lambda _{n}\,\varphi (x_{n}),$

for any *x*1, ..., *xn*.

The *finite form* of the Jensen's inequality can be proved by induction: by convexity hypotheses, the statement is true for *n* = 2. Suppose the statement is true for some *n*, so

$\varphi \left(\sum _{i=1}^{n}\lambda _{i}x_{i}\right)\leq \sum _{i=1}^{n}\lambda _{i}\varphi \left(x_{i}\right)$

for any *λ*1, ..., *λn* such that *λ*1 + ... + *λn* = 1.

One needs to prove it for *n* + 1. At least one of the *λi* is strictly smaller than 1 , say *λ**n*+1; therefore by convexity inequality:

${\begin{aligned}\varphi \left(\sum _{i=1}^{n+1}\lambda _{i}x_{i}\right)&=\varphi \left((1-\lambda _{n+1})\sum _{i=1}^{n}{\frac {\lambda _{i}}{1-\lambda _{n+1}}}x_{i}+\lambda _{n+1}x_{n+1}\right)\\&\leq (1-\lambda _{n+1})\varphi \left(\sum _{i=1}^{n}{\frac {\lambda _{i}}{1-\lambda _{n+1}}}x_{i}\right)+\lambda _{n+1}\,\varphi (x_{n+1}).\end{aligned}}$

Since *λ*1 + ... +*λ**n* + *λ**n*+1 = 1,

$\sum _{i=1}^{n}{\frac {\lambda _{i}}{1-\lambda _{n+1}}}=1$

,

applying the inductive hypothesis gives

$\varphi \left(\sum _{i=1}^{n}{\frac {\lambda _{i}}{1-\lambda _{n+1}}}x_{i}\right)\leq \sum _{i=1}^{n}{\frac {\lambda _{i}}{1-\lambda _{n+1}}}\varphi (x_{i})$

therefore

${\begin{aligned}\varphi \left(\sum _{i=1}^{n+1}\lambda _{i}x_{i}\right)&\leq (1-\lambda _{n+1})\sum _{i=1}^{n}{\frac {\lambda _{i}}{1-\lambda _{n+1}}}\varphi (x_{i})+\lambda _{n+1}\,\varphi (x_{n+1})=\sum _{i=1}^{n+1}\lambda _{i}\varphi (x_{i})\end{aligned}}$

We deduce the inequality is true for *n* + 1, by induction it follows that the result is also true for all integer *n* greater than 2.

In order to obtain the general inequality from this finite form, one needs to use a density argument. The finite form can be rewritten as:

$\varphi \left(\int x\,d\mu _{n}(x)\right)\leq \int \varphi (x)\,d\mu _{n}(x),$

where *μ**n* is a measure given by an arbitrary convex combination of Dirac deltas:

$\mu _{n}=\sum _{i=1}^{n}\lambda _{i}\delta _{x_{i}}.$

Since convex functions are continuous, and since convex combinations of Dirac deltas are weakly dense in the set of probability measures (as could be easily verified), the general statement is obtained simply by a limiting procedure.

### Proof 2 (measure-theoretic form)

Let g be a real-valued $\mu$ -integrable function on a probability space $\Omega$ , and let $\varphi$ be a convex function on the real numbers. Since $\varphi$ is convex, at each real number x we have a nonempty set of subderivatives, which may be thought of as lines touching the graph of $\varphi$ at x , but which are below the graph of $\varphi$ at all points (support lines of the graph).

Now, if we define

$x_{0}:=\int _{\Omega }g\,d\mu ,$

because of the existence of subderivatives for convex functions, we may choose a and b such that

$ax+b\leq \varphi (x),$

for all real x and

$ax_{0}+b=\varphi (x_{0}).$

But then we have that

$\varphi \circ g(\omega )\geq ag(\omega )+b$

for almost all $\omega \in \Omega$ . Since we have a probability measure, the integral is monotone with $\mu (\Omega )=1$ so that

$\int _{\Omega }\varphi \circ g\,d\mu \geq \int _{\Omega }(ag+b)\,d\mu =a\int _{\Omega }g\,d\mu +b\int _{\Omega }d\mu =ax_{0}+b=\varphi (x_{0})=\varphi \left(\int _{\Omega }g\,d\mu \right),$

as desired.

### Proof 3 (general inequality in a probabilistic setting)

Let *X* be an integrable random variable that takes values in a real topological vector space *T*. Since $\varphi :T\to \mathbb {R}$ is convex, for any $x,y\in T$ , the quantity

${\frac {\varphi (x+\theta \,y)-\varphi (x)}{\theta }},$

is decreasing as θ approaches 0+. In particular, the *subdifferential* of $\varphi$ evaluated at x in the direction y is well-defined by

$(D\varphi )(x)\cdot y:=\lim _{\theta \downarrow 0}{\frac {\varphi (x+\theta \,y)-\varphi (x)}{\theta }}=\inf _{\theta \neq 0}{\frac {\varphi (x+\theta \,y)-\varphi (x)}{\theta }}.$

It is easily seen that the subdifferential is linear in y (that is false and the assertion requires Hahn-Banach theorem to be proved) and, since the infimum taken in the right-hand side of the previous formula is smaller than the value of the same term for *θ* = 1, one gets

$\varphi (x)\leq \varphi (x+y)-(D\varphi )(x)\cdot y.$

In particular, for an arbitrary sub-σ-algebra ${\mathfrak {G}}$ we can evaluate the last inequality when $x=\operatorname {E} [X\mid {\mathfrak {G}}],\,y=X-\operatorname {E} [X\mid {\mathfrak {G}}]$ to obtain

$\varphi (\operatorname {E} [X\mid {\mathfrak {G}}])\leq \varphi (X)-(D\varphi )(\operatorname {E} [X\mid {\mathfrak {G}}])\cdot (X-\operatorname {E} [X\mid {\mathfrak {G}}]).$

Now, if we take the expectation conditioned to ${\mathfrak {G}}$ on both sides of the previous expression, we get the result since:

$\operatorname {E} \left[\left[(D\varphi )(\operatorname {E} [X\mid {\mathfrak {G}}])\cdot (X-\operatorname {E} [X\mid {\mathfrak {G}}])\right]\mid {\mathfrak {G}}\right]=(D\varphi )(\operatorname {E} [X\mid {\mathfrak {G}}])\cdot \operatorname {E} [\left(X-\operatorname {E} [X\mid {\mathfrak {G}}]\right)\mid {\mathfrak {G}}]=0,$

by the linearity of the subdifferential in the *y* variable, and the following well-known property of the conditional expectation:

$\operatorname {E} \left[\left(\operatorname {E} [X\mid {\mathfrak {G}}]\right)\mid {\mathfrak {G}}\right]=\operatorname {E} [X\mid {\mathfrak {G}}].$

## Applications and special cases

### Form involving a probability density function

Suppose Ω is a measurable subset of the real line and *f*(*x*) is a non-negative function such that

$\int _{-\infty }^{\infty }f(x)\,dx=1.$

In probabilistic language, *f* is a probability density function.

Then Jensen's inequality becomes the following statement about convex integrals:

If *g* is any real-valued measurable function and ${\textstyle \varphi }$ is convex over the range of *g*, then

$\varphi \left(\int _{-\infty }^{\infty }g(x)f(x)\,dx\right)\leq \int _{-\infty }^{\infty }\varphi (g(x))f(x)\,dx.$

If *g*(*x*) = *x*, then this form of the inequality reduces to a commonly used special case:

$\varphi \left(\int _{-\infty }^{\infty }x\,f(x)\,dx\right)\leq \int _{-\infty }^{\infty }\varphi (x)\,f(x)\,dx.$

This is applied in Variational Bayesian methods.

### Example: even moments of a random variable

If *g*(*x*) = *x2n*, and *X* is a random variable, then *g* is convex as

${\frac {d^{2}g}{dx^{2}}}(x)=2n(2n-1)x^{2n-2}\geq 0\quad \forall \ x\in \mathbb {R}$

and so

$g(\operatorname {E} [X])=(\operatorname {E} [X])^{2n}\leq \operatorname {E} [X^{2n}].$

In particular, if some even moment *2n* of *X* is finite, *X* has a finite mean. An extension of this argument shows *X* has finite moments of every order $l\in \mathbb {N}$ dividing *n*.

### Alternative finite form

Let Ω = {*x*1, ... *xn*}, and take μ to be the counting measure on Ω, then the general form reduces to a statement about sums:

$\varphi \left(\sum _{i=1}^{n}g(x_{i})\lambda _{i}\right)\leq \sum _{i=1}^{n}\varphi (g(x_{i}))\lambda _{i},$

provided that *λi* ≥ 0 and

$\lambda _{1}+\cdots +\lambda _{n}=1.$

There is also an infinite discrete form.

### Statistical physics

Jensen's inequality is of particular importance in statistical physics when the convex function is an exponential, giving:

$e^{\operatorname {E} [X]}\leq \operatorname {E} \left[e^{X}\right],$

where the expected values are with respect to some probability distribution in the random variable X.

### Information theory

If *p*(*x*) is the true probability density for X, and *q*(*x*) is another density, then applying Jensen's inequality for the random variable *Y*(*X*) = *q*(*X*)/*p*(*X*) and the convex function *φ*(*y*) = −log(*y*) gives

$\operatorname {E} [\varphi (Y)]\geq \varphi (\operatorname {E} [Y])$

Therefore:

$-D(p(x)\|q(x))=\int p(x)\log \left({\frac {q(x)}{p(x)}}\right)\,dx\leq \log \left(\int p(x){\frac {q(x)}{p(x)}}\,dx\right)=\log \left(\int q(x)\,dx\right)=0$

a result called Gibbs' inequality.

It shows that the average message length is minimised when codes are assigned on the basis of the true probabilities *p* rather than any other distribution *q*. The quantity that is non-negative is called the Kullback–Leibler divergence of *q* from *p*, where $D(p(x)\|q(x))=\int p(x)\log \left({\frac {p(x)}{q(x)}}\right)dx$ .

Since −log(*x*) is a strictly convex function for *x* > 0, it follows that equality holds when *p*(*x*) equals *q*(*x*) almost everywhere.

### Rao–Blackwell theorem

If *L* is a convex function and ${\mathfrak {G}}$ a sub-sigma-algebra, then, from the conditional version of Jensen's inequality, we get

$L(\operatorname {E} [\delta (X)\mid {\mathfrak {G}}])\leq \operatorname {E} [L(\delta (X))\mid {\mathfrak {G}}]\quad \Longrightarrow \quad \operatorname {E} [L(\operatorname {E} [\delta (X)\mid {\mathfrak {G}}])]\leq \operatorname {E} [L(\delta (X))].$

So if δ(*X*) is some estimator of an unobserved parameter θ given a vector of observables *X*; and if *T*(*X*) is a sufficient statistic for θ; then an improved estimator, in the sense of having a smaller expected loss *L*, can be obtained by calculating

$\delta _{1}(X)=\operatorname {E} _{\theta }[\delta (X')\mid T(X')=T(X)],$

the expected value of δ with respect to θ, taken over all possible vectors of observations *X* compatible with the same value of *T*(*X*) as that observed. Further, because T is a sufficient statistic, $\delta _{1}(X)$ does not depend on θ, hence, becomes a statistic.

This result is known as the Rao–Blackwell theorem.

### Risk aversion

The relation between risk aversion and declining marginal utility for scalar outcomes can be stated formally with Jensen's inequality: risk aversion can be stated as preferring a certain outcome $u(E[x])$ to a fair gamble with potentially larger but uncertain outcome of $u(x)$ :

$u(E[x])>E[u(x)]$ .

But this is simply Jensen's inequality for a *concave* $u(x)$ : a utility function that exhibits declining marginal utility.

## Generalizations

Beyond its classical formulation for real numbers and convex functions, Jensen's inequality has been extended to the realm of operator theory. In this non‐commutative setting the inequality is expressed in terms of operator convex functions—that is, functions defined on an interval I that satisfy

$f{\bigl (}\lambda x+(1-\lambda )y{\bigr )}\leq \lambda f(x)+(1-\lambda )f(y)$

for every pair of self‐adjoint operators x and y (with spectra in I) and every scalar $\lambda \in [0,1]$ . Hansen and Pedersen established a definitive version of this inequality by considering genuine non‐commutative convex combinations. In particular, if one has an n‑tuple of bounded self‐adjoint operators $x_{1},\dots ,x_{n}$ with spectra in I and an n‑tuple of operators $a_{1},\dots ,a_{n}$ satisfying

$\sum _{i=1}^{n}a_{i}^{*}a_{i}=I,$

then the following operator Jensen inequality holds:

$f{\Bigl (}\sum _{i=1}^{n}a_{i}^{*}x_{i}a_{i}{\Bigr )}\leq \sum _{i=1}^{n}a_{i}^{*}f(x_{i})a_{i}.$

This result shows that the convex transformation “respects” non-commutative convex combinations, thereby extending the classical inequality to operators without the need for additional restrictions on the interval of definition. A closely related extension is given by the Jensen trace inequality. For a continuous convex function f defined on I, if one considers self‐adjoint matrices $x_{1},\dots ,x_{n}$ (with spectra in I) and matrices $a_{1},\dots ,a_{n}$ satisfying $\sum _{i=1}^{n}a_{i}^{*}a_{i}=I$ , then one has

$\operatorname {Tr} {\Bigl (}f{\Bigl (}\sum _{i=1}^{n}a_{i}^{*}x_{i}a_{i}{\Bigr )}{\Bigr )}\leq \operatorname {Tr} {\Bigl (}\sum _{i=1}^{n}a_{i}^{*}f(x_{i})a_{i}{\Bigr )}.$

This inequality naturally extends to C*-algebras equipped with a finite trace and is particularly useful in applications ranging from quantum statistical mechanics to information theory. Furthermore, contractive versions of these operator inequalities are available when one only assumes $\sum _{i=1}^{n}a_{i}^{t}a_{i}\leq I$ , provided that additional conditions such as $f(0)\leq 0$ (when 0 ∈ I) are imposed. Extensions to continuous fields of operators and to settings involving conditional expectations on C-algebras further illustrate the broad applicability of these generalizations.
