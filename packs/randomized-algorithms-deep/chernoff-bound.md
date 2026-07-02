---
title: "Chernoff bound"
source: https://en.wikipedia.org/wiki/Chernoff_bound
domain: randomized-algorithms-deep
license: CC-BY-SA-4.0
tags: randomized algorithm, monte carlo algorithm, probabilistic method, chernoff bound
fetched: 2026-07-02
---

# Chernoff bound

In probability theory, a **Chernoff bound** is an exponentially decreasing upper bound on the tail of a random variable based on its moment generating function. The minimum of all such exponential bounds forms *the* Chernoff or **Chernoff-Cramér bound**, which may decay faster than exponential (e.g. sub-Gaussian). It is especially useful for sums of independent random variables, such as sums of Bernoulli random variables.

The bound is commonly named after Herman Chernoff who described the method in a 1952 paper, though Chernoff himself attributed it to Herman Rubin. In 1938 Harald Cramér had published an almost identical concept now known as Cramér's theorem.

It is a sharper bound than the first- or second-moment-based tail bounds such as Markov's inequality or Chebyshev's inequality, which only yield power-law bounds on tail decay. However, when applied to sums the Chernoff bound requires the random variables to be independent, a condition that is not required by either Markov's inequality or Chebyshev's inequality.

The Chernoff bound is related to the Bernstein inequalities. It is also used to prove Hoeffding's inequality, Bennett's inequality, and McDiarmid's inequality.

## Generic Chernoff bounds

The generic Chernoff bound for a random variable X is attained by applying Markov's inequality to $e^{tX}$ (which is why it is sometimes called the *exponential Markov* or *exponential moments* bound). For positive t this gives a bound on the right tail of X in terms of its moment-generating function $M(t)=\operatorname {E} (e^{tX})$ :

$\operatorname {P} \left(X\geq a\right)=\operatorname {P} \left(e^{tX}\geq e^{ta}\right)\leq M(t)e^{-ta}\qquad (t>0)$

Since this bound holds for every positive t , we may take the infimum:

$\operatorname {P} \left(X\geq a\right)\leq \inf _{t>0}M(t)e^{-ta}$

Performing the same analysis with negative t we get a similar bound on the left tail:

$\operatorname {P} \left(X\leq a\right)=\operatorname {P} \left(e^{tX}\geq e^{ta}\right)\leq M(t)e^{-ta}\qquad (t<0)$

and

$\operatorname {P} \left(X\leq a\right)\leq \inf _{t<0}M(t)e^{-ta}$

The quantity $M(t)e^{-ta}$ can be expressed as the expected value $\operatorname {E} (e^{tX})e^{-ta}$ , or equivalently $\operatorname {E} (e^{t(X-a)})$ .

### Properties

The exponential function is convex, so by Jensen's inequality $\operatorname {E} (e^{tX})\geq e^{t\operatorname {E} (X)}$ . It follows that the bound on the right tail is greater or equal to one when $a\leq \operatorname {E} (X)$ , and therefore trivial; similarly, the left bound is trivial for $a\geq \operatorname {E} (X)$ . We may therefore combine the two infima and define the two-sided Chernoff bound: $C(a)=\inf _{t}M(t)e^{-ta}$ which provides an upper bound on the folded cumulative distribution function of X (folded at the mean, not the median).

The logarithm of the two-sided Chernoff bound is known as the rate function (or *Cramér transform*) $I=-\log C$ . It is equivalent to the Legendre–Fenchel transform or convex conjugate of the cumulant generating function $K=\log M$ , defined as: $I(a)=\sup _{t}at-K(t)$ The moment generating function is log-convex, so by a property of the convex conjugate, the Chernoff bound must be log-concave. The Chernoff bound attains its maximum at the mean, $C(\operatorname {E} (X))=1$ , and is invariant under translation: ${\textstyle C_{X+k}(a)=C_{X}(a-k)}$ .

The Chernoff bound is exact if and only if X is a single concentrated mass (degenerate distribution). The bound is tight only at or beyond the extremes of a bounded random variable, where the infima are attained for infinite t . For unbounded random variables the bound is nowhere tight, though it is asymptotically tight up to sub-exponential factors ("exponentially tight"). Individual moments can provide tighter bounds, at the cost of greater analytical complexity.

In practice, the exact Chernoff bound may be unwieldy or difficult to evaluate analytically, in which case a suitable upper bound on the moment (or cumulant) generating function may be used instead (e.g. a sub-parabolic CGF giving a sub-Gaussian Chernoff bound).

| Distribution | $\operatorname {E} (X)$ | $K(t)$ | $I(a)$ | $C(a)$ |
|---|---|---|---|---|
| Normal distribution | 0 | ${\frac {1}{2}}\sigma ^{2}t^{2}$ | ${\frac {1}{2}}\left({\frac {a}{\sigma }}\right)^{2}$ | $\exp \left({-{\frac {a^{2}}{2\sigma ^{2}}}}\right)$ |
| Bernoulli distribution (detailed below) | p | $\ln \left(1-p+pe^{t}\right)$ | $D_{KL}(a\parallel p)$ | $\left({\frac {p}{a}}\right)^{a}{\left({\frac {1-p}{1-a}}\right)}^{1-a}$ |
| Standard Bernoulli (*H* is the binary entropy function) | ${\frac {1}{2}}$ | $\ln \left(1+e^{t}\right)-\ln(2)$ | $\ln(2)-H(a)$ | ${\frac {1}{2}}a^{-a}(1-a)^{-(1-a)}$ |
| Rademacher distribution | 0 | $\ln \cosh(t)$ | $\ln(2)-H\left({\frac {1+a}{2}}\right)$ | ${\sqrt {(1+a)^{-1-a}(1-a)^{-1+a}}}$ |
| Gamma distribution | $\theta k$ | $-k\ln(1-\theta t)$ | $-k\ln {\frac {a}{\theta k}}-k+{\frac {a}{\theta }}$ | $\left({\frac {a}{\theta k}}\right)^{k}e^{k-a/\theta }$ |
| Chi-squared distribution | k | $-{\frac {k}{2}}\ln(1-2t)$ | ${\frac {k}{2}}\left({\frac {a}{k}}-1-\ln {\frac {a}{k}}\right)$ | $\left({\frac {a}{k}}\right)^{k/2}e^{k/2-a/2}$ |
| Poisson distribution | $\lambda$ | $\lambda (e^{t}-1)$ | $a\ln(a/\lambda )-a+\lambda$ | $(a/\lambda )^{-a}e^{a-\lambda }$ |

### Bounds from below from the MGF

Using only the moment generating function, a bound from below on the tail probabilities can be obtained by applying the Paley-Zygmund inequality to $e^{tX}$ , yielding: $\operatorname {P} \left(X>a\right)\geq \sup _{t>0\land M(t)\geq e^{ta}}\left(1-{\frac {e^{ta}}{M(t)}}\right)^{2}{\frac {M(t)^{2}}{M(2t)}}$ (a bound on the left tail is obtained for negative t ). Unlike the Chernoff bound however, this result is not exponentially tight.

Theodosopoulos constructed a tight(er) MGF-based bound from below using an exponential tilting procedure.

For particular distributions (such as the binomial) bounds from below of the same exponential order as the Chernoff bound are often available.

## Sums of independent random variables

When X is the sum of n independent random variables *X*1, ..., *Xn*, the moment generating function of X is the product of the individual moment generating functions, giving that:

| $\Pr(X\geq a)\leq \inf _{t>0}{\frac {\operatorname {E} \left[\prod _{i}e^{t\cdot X_{i}}\right]}{e^{t\cdot a}}}=\inf _{t>0}e^{-t\cdot a}\prod _{i}\operatorname {E} \left[e^{t\cdot X_{i}}\right].$ |   | 1 |
|---|---|---|

and:

$\Pr(X\leq a)\leq \inf _{t<0}e^{-ta}\prod _{i}\operatorname {E} \left[e^{tX_{i}}\right]$

Specific Chernoff bounds are attained by calculating the moment-generating function $\operatorname {E} \left[e^{-t\cdot X_{i}}\right]$ for specific instances of the random variables $X_{i}$ .

When the random variables are also *identically distributed* (iid), the Chernoff bound for the sum reduces to a simple rescaling of the single-variable Chernoff bound. That is, the Chernoff bound for the *average* of *n* iid variables is equivalent to the *n*th power of the Chernoff bound on a single variable (see Cramér's theorem).

## Sums of independent bounded random variables

Chernoff bounds may also be applied to general sums of independent, bounded random variables, regardless of their distribution; this is known as Hoeffding's inequality. The proof follows a similar approach to the other Chernoff bounds, but applying Hoeffding's lemma to bound the moment generating functions (see Hoeffding's inequality).

Hoeffding's inequality

.

Suppose

X

1

, ...,

X

n

are

independent

random variables taking values in

[a,b].

Let

X

denote their sum and let

μ

= E[

X

]

denote the sum's expected value. Then for any

$t>0$

,

$\Pr(X\leq \mu -t)<e^{-2t^{2}/(n(b-a)^{2})},$

$\Pr(X\geq \mu +t)<e^{-2t^{2}/(n(b-a)^{2})}.$

## Sums of independent Bernoulli random variables

The bounds in the following sections for Bernoulli random variables are derived by using that, for a Bernoulli random variable $X_{i}$ with probability *p* of being equal to 1,

$\operatorname {E} \left[e^{t\cdot X_{i}}\right]=(1-p)e^{0}+pe^{t}=1+p(e^{t}-1)\leq e^{p(e^{t}-1)}.$

One can encounter many flavors of Chernoff bounds: the original *additive form* (which gives a bound on the absolute error) or the more practical *multiplicative form* (which bounds the error relative to the mean).

### Multiplicative form (relative error)

**Multiplicative Chernoff bound.** Suppose *X*1, ..., *Xn* are independent random variables taking values in {0, 1}. Let X denote their sum and let *μ* = E[*X*] denote the sum's expected value. Then for any *δ* > 0,

$\Pr(X\geq (1+\delta )\mu )\leq \left({\frac {e^{\delta }}{(1+\delta )^{1+\delta }}}\right)^{\mu }.$

A similar proof strategy can be used to show that for 0 < *δ* < 1

$\Pr(X\leq (1-\delta )\mu )\leq \left({\frac {e^{-\delta }}{(1-\delta )^{1-\delta }}}\right)^{\mu }.$

The above formula is often unwieldy in practice, so the following looser but more convenient bounds are often used, which follow from the inequality $\textstyle {\frac {2\delta }{2+\delta }}\leq \log(1+\delta )$ from the list of logarithmic inequalities:

$\Pr(X\geq (1+\delta )\mu )\leq e^{-\delta ^{2}\mu /(2+\delta )},\qquad 0\leq \delta ,$

$\Pr(X\leq (1-\delta )\mu )\leq e^{-\delta ^{2}\mu /2},\qquad 0\leq \delta \leq 1,$

$\Pr(|X-\mu |\geq \delta \mu )\leq 2e^{-\delta ^{2}\mu /3},\qquad 0\leq \delta \leq 1.$

Notice that the bounds are trivial for $\delta =0$ .

In addition, based on the Taylor expansion for the Lambert W function,

$\Pr(X\geq R)\leq 2^{-xR},\qquad x>0,\ \mu >0,\ R\geq (2^{x}e-1)\mu .$

### Additive form (absolute error)

The following theorem is due to Wassily Hoeffding and hence is called the Chernoff–Hoeffding theorem.

Chernoff–Hoeffding theorem.

Suppose

X

1

, ...,

X

n

are

i.i.d.

random variables, taking values in

{0, 1}.

Let

p

= E[

X

1

]

and

ε

> 0

.

${\begin{aligned}\Pr \left({\frac {1}{n}}\sum X_{i}\geq p+\varepsilon \right)\leq \left(\left({\frac {p}{p+\varepsilon }}\right)^{p+\varepsilon }{\left({\frac {1-p}{1-p-\varepsilon }}\right)}^{1-p-\varepsilon }\right)^{n}&=e^{-D(p+\varepsilon \parallel p)n}\\\Pr \left({\frac {1}{n}}\sum X_{i}\leq p-\varepsilon \right)\leq \left(\left({\frac {p}{p-\varepsilon }}\right)^{p-\varepsilon }{\left({\frac {1-p}{1-p+\varepsilon }}\right)}^{1-p+\varepsilon }\right)^{n}&=e^{-D(p-\varepsilon \parallel p)n}\end{aligned}}$

where

$D(x\parallel y)=x\ln {\frac {x}{y}}+(1-x)\ln \left({\frac {1-x}{1-y}}\right)$

is the

Kullback–Leibler divergence

between

Bernoulli distributed

random variables with parameters

x

and

y

respectively. If

p

≥

⁠

1

/

2

⁠

,

then

$D(p+\varepsilon \parallel p)\geq {\tfrac {\varepsilon ^{2}}{2p(1-p)}}$

which means

$\Pr \left({\frac {1}{n}}\sum X_{i}>p+x\right)\leq \exp \left(-{\frac {x^{2}n}{2p(1-p)}}\right).$

A simpler bound follows by relaxing the theorem using *D*(*p* + *ε* || *p*) ≥ 2*ε*2, which follows from the convexity of *D*(*p* + *ε* || *p*) and the fact that

${\frac {d^{2}}{d\varepsilon ^{2}}}D(p+\varepsilon \parallel p)={\frac {1}{(p+\varepsilon )(1-p-\varepsilon )}}\geq 4={\frac {d^{2}}{d\varepsilon ^{2}}}(2\varepsilon ^{2}).$

This result is a special case of Hoeffding's inequality. Sometimes, the bounds

${\begin{aligned}D((1+x)p\parallel p)\geq {\frac {1}{4}}x^{2}p,&&&{-{\tfrac {1}{2}}}\leq x\leq {\tfrac {1}{2}},\\[6pt]D(x\parallel y)\geq {\frac {3(x-y)^{2}}{2(2y+x)}},\\[6pt]D(x\parallel y)\geq {\frac {(x-y)^{2}}{2y}},&&&x\leq y,\\[6pt]D(x\parallel y)\geq {\frac {(x-y)^{2}}{2x}},&&&x\geq y\end{aligned}}$

which are stronger for *p* < ⁠1/8⁠, are also used.

## Applications

Chernoff bounds have very useful applications in set balancing and packet routing in sparse networks.

The set balancing problem arises while designing statistical experiments. Typically while designing a statistical experiment, given the features of each participant in the experiment, we need to know how to divide the participants into 2 disjoint groups such that each feature is roughly as balanced as possible between the two groups.

Chernoff bounds are also used to obtain tight bounds for permutation routing problems which reduce network congestion while routing packets in sparse networks.

Chernoff bounds are used in computational learning theory to prove that a learning algorithm is probably approximately correct, i.e. with high probability the algorithm has small error on a sufficiently large training data set.

Chernoff bounds can be effectively used to evaluate the "robustness level" of an application/algorithm by exploring its perturbation space with randomization. The use of the Chernoff bound permits one to abandon the strong—and mostly unrealistic—small perturbation hypothesis (the perturbation magnitude is small). The robustness level can be, in turn, used either to validate or reject a specific algorithmic choice, a hardware implementation or the appropriateness of a solution whose structural parameters are affected by uncertainties.

A simple and common use of Chernoff bounds is for "boosting" of randomized algorithms. If one has an algorithm that outputs a guess that is the desired answer with probability *p* > 1/2, then one can get a higher success rate by running the algorithm $n=\log(1/\delta )2p/(p-1/2)^{2}$ times and outputting a guess that is output by more than *n*/2 runs of the algorithm. (There cannot be more than one such guess.) Assuming that these algorithm runs are independent, the probability that more than *n*/2 of the guesses is correct is equal to the probability that the sum of independent Bernoulli random variables *Xk* that are 1 with probability *p* is more than *n*/2. This can be shown to be at least $1-\delta$ via the multiplicative Chernoff bound (Corollary 13.3 in Sinclair's class notes, *μ* = *np*).:

$\Pr \left[X>{n \over 2}\right]\geq 1-e^{-n\left(p-1/2\right)^{2}/(2p)}\geq 1-\delta$

## Matrix Chernoff bound

Rudolf Ahlswede and Andreas Winter introduced a Chernoff bound for matrix-valued random variables. The following version of the inequality can be found in the work of Tropp.

Let *M*1, ..., *Mt* be independent matrix valued random variables such that $M_{i}\in \mathbb {C} ^{d_{1}\times d_{2}}$ and $\mathbb {E} [M_{i}]=0$ . Let us denote by $\lVert M\rVert$ the operator norm of the matrix M . If $\lVert M_{i}\rVert \leq \gamma$ holds almost surely for all $i\in \{1,\ldots ,t\}$ , then for every *ε* > 0

$\Pr \left(\left\|{\frac {1}{t}}\sum _{i=1}^{t}M_{i}\right\|>\varepsilon \right)\leq (d_{1}+d_{2})\exp \left(-{\frac {3\varepsilon ^{2}t}{8\gamma ^{2}}}\right).$

Notice that in order to conclude that the deviation from 0 is bounded by *ε* with high probability, we need to choose a number of samples t proportional to the logarithm of $d_{1}+d_{2}$ . In general, unfortunately, a dependence on $\log(\min(d_{1},d_{2}))$ is inevitable: take for example a diagonal random sign matrix of dimension $d\times d$ . The operator norm of the sum of *t* independent samples is precisely the maximum deviation among *d* independent random walks of length *t*. In order to achieve a fixed bound on the maximum deviation with constant probability, it is easy to see that *t* should grow logarithmically with *d* in this scenario.

The following theorem can be obtained by assuming *M* has low rank, in order to avoid the dependency on the dimensions.

### Theorem without the dependency on the dimensions

Let 0 < *ε* < 1 and *M* be a random symmetric real matrix with $\|\operatorname {E} [M]\|\leq 1$ and $\|M\|\leq \gamma$ almost surely. Assume that each element on the support of *M* has at most rank *r*. Set

$t=\Omega \left({\frac {\gamma \log(\gamma /\varepsilon ^{2})}{\varepsilon ^{2}}}\right).$

If $r\leq t$ holds almost surely, then

$\Pr \left(\left\|{\frac {1}{t}}\sum _{i=1}^{t}M_{i}-\operatorname {E} [M]\right\|>\varepsilon \right)\leq {\frac {1}{\mathbf {poly} (t)}}$

where *M*1, ..., *Mt* are i.i.d. copies of *M*.

## Sampling variant

The following variant of Chernoff's bound can be used to bound the probability that a majority in a population will become a minority in a sample, or vice versa.

Suppose there is a general population *A* and a sub-population *B* ⊆ *A*. Mark the relative size of the sub-population (|*B*|/|*A*|) by *r*.

Suppose we pick an integer *k* and a random sample *S* ⊂ *A* of size *k*. Mark the relative size of the sub-population in the sample (|*B*∩*S*|/|*S*|) by *rS*.

Then, for every fraction *d* ∈ [0,1]:

$\Pr \left(r_{S}<(1-d)\cdot r\right)<\exp \left(-r\cdot d^{2}\cdot {\frac {k}{2}}\right)$

In particular, if *B* is a majority in *A* (i.e. *r* > 0.5) we can bound the probability that *B* will remain majority in *S*(*rS* > 0.5) by taking: *d* = 1 − 1/(2*r*):

$\Pr \left(r_{S}>0.5\right)>1-\exp \left(-r\cdot \left(1-{\frac {1}{2r}}\right)^{2}\cdot {\frac {k}{2}}\right)$

This bound is of course not tight at all. For example, when *r* = 0.5 we get a trivial bound Prob > 0.

## Proofs

### Multiplicative form

Following the conditions of the multiplicative Chernoff bound, let *X*1, ..., *Xn* be independent Bernoulli random variables, whose sum is *X*, each having probability *pi* of being equal to 1. For a Bernoulli variable:

$\operatorname {E} \left[e^{t\cdot X_{i}}\right]=(1-p_{i})e^{0}+p_{i}e^{t}=1+p_{i}(e^{t}-1)\leq e^{p_{i}(e^{t}-1)}$

So, using (**1**) with $a=(1+\delta )\mu$ for any $\delta >0$ and where $\mu =\operatorname {E} [X]=\textstyle \sum _{i=1}^{n}p_{i}$ ,

${\begin{aligned}\Pr(X>(1+\delta )\mu )&\leq \inf _{t\geq 0}\exp(-t(1+\delta )\mu )\prod _{i=1}^{n}\operatorname {E} [\exp(tX_{i})]\\[4pt]&\leq \inf _{t\geq 0}\exp {\Big (}-t(1+\delta )\mu +\sum _{i=1}^{n}p_{i}(e^{t}-1){\Big )}\\[4pt]&=\inf _{t\geq 0}\exp {\Big (}-t(1+\delta )\mu +(e^{t}-1)\mu {\Big )}.\end{aligned}}$

If we simply set *t* = log(1 + *δ*) so that *t* > 0 for *δ* > 0, we can substitute and find

$\exp {\Big (}-t(1+\delta )\mu +(e^{t}-1)\mu {\Big )}={\frac {\exp((1+\delta -1)\mu )}{(1+\delta )^{(1+\delta )\mu }}}=\left[{\frac {e^{\delta }}{(1+\delta )^{(1+\delta )}}}\right]^{\mu }.$

This proves the result desired.

### Chernoff–Hoeffding theorem (additive form)

Let *q* = *p* + *ε*. Taking *a* = *nq* in (**1**), we obtain:

$\Pr \left({\frac {1}{n}}\sum X_{i}\geq q\right)\leq \inf _{t>0}{\frac {E\left[\prod e^{tX_{i}}\right]}{e^{tnq}}}=\inf _{t>0}\left({\frac {E\left[e^{tX_{i}}\right]}{e^{tq}}}\right)^{n}.$

Now, knowing that Pr(*Xi* = 1) = *p*, Pr(*Xi* = 0) = 1 − *p*, we have

$\left({\frac {\operatorname {E} \left[e^{tX_{i}}\right]}{e^{tq}}}\right)^{n}=\left({\frac {pe^{t}+(1-p)}{e^{tq}}}\right)^{n}=\left(pe^{(1-q)t}+(1-p)e^{-qt}\right)^{n}.$

Therefore, we can easily compute the infimum, using calculus:

${\frac {d}{dt}}\left(pe^{(1-q)t}+(1-p)e^{-qt}\right)=(1-q)pe^{(1-q)t}-q(1-p)e^{-qt}$

Setting the equation to zero and solving, we have

${\begin{aligned}(1-q)pe^{(1-q)t}&=q(1-p)e^{-qt}\\(1-q)pe^{t}&=q(1-p)\end{aligned}}$

so that

$e^{t}={\frac {(1-p)q}{(1-q)p}}.$

Thus,

$t=\log \left({\frac {(1-p)q}{(1-q)p}}\right).$

As *q* = *p* + *ε* > *p*, we see that *t* > 0, so our bound is satisfied on t. Having solved for t, we can plug back into the equations above to find that

${\begin{aligned}\log \left(pe^{(1-q)t}+(1-p)e^{-qt}\right)&=\log \left(e^{-qt}(1-p+pe^{t})\right)\\&=\log \left(e^{-q\log \left({\frac {(1-p)q}{(1-q)p}}\right)}\right)+\log \left(1-p+pe^{\log \left({\frac {1-p}{1-q}}\right)}e^{\log {\frac {q}{p}}}\right)\\&=-q\log {\frac {1-p}{1-q}}-q\log {\frac {q}{p}}+\log \left(1-p+p\left({\frac {1-p}{1-q}}\right){\frac {q}{p}}\right)\\&=-q\log {\frac {1-p}{1-q}}-q\log {\frac {q}{p}}+\log \left({\frac {(1-p)(1-q)}{1-q}}+{\frac {(1-p)q}{1-q}}\right)\\&=-q\log {\frac {q}{p}}+\left(-q\log {\frac {1-p}{1-q}}+\log {\frac {1-p}{1-q}}\right)\\&=-q\log {\frac {q}{p}}+(1-q)\log {\frac {1-p}{1-q}}\\&=-D(q\parallel p).\end{aligned}}$

We now have our desired result, that

$\Pr \left({\tfrac {1}{n}}\sum X_{i}\geq p+\varepsilon \right)\leq e^{-D(p+\varepsilon \parallel p)n}.$

To complete the proof for the symmetric case, we simply define the random variable *Yi* = 1 − *Xi*, apply the same proof, and plug it into our bound.

### An elementary proof of the Chernoff–Hoeffding theorem (additive form)

The following proof is from an article by Wolfgang Mulzer. Let $q\geq p$ . The proof analyzes two distributions $D_{p}$ and $D_{q}$ , both over n -tuples of bits $X=(X_{1},\dots ,X_{n})$ . In the distribution $D_{p}$ each $X_{i}$ is an independent Bernoulli random variable with expectation p , and $D_{q}$ is defined analogously. When $\sum X_{i}=k$ , the ratio $D_{q}(X)/D_{p}(X)$ is

$\left({\frac {q}{p}}\right)^{k}\left({\frac {1-q}{1-p}}\right)^{n-k}.$

Note that this is monotone in *k*, and so whenever $\sum X_{i}\geq qn$ , the ratio $D_{q}(X)/D_{p}(X)$ is at least

$\left({\frac {q}{p}}\right)^{qn}\left({\frac {1-q}{1-p}}\right)^{n-qn}=e^{D(q\parallel p)n}.$

This shows us that $\sum X_{i}\geq qn$ is unlikely in $D_{p}$ since

$\Pr _{X\sim D_{p}}\left(\sum X_{i}\geq qn\right)\leq e^{-D(q\parallel p)n}\Pr _{X\sim D_{q}}\left(\sum X_{i}\geq qn\right)\leq e^{-D(q\parallel p)n}.$

As in the previous proof, for the symmetric case we simply define the random variable *Yi* = 1 − *Xi*, apply the same proof, and plug it into our bound.
