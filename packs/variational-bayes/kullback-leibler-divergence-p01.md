---
title: "Kullback–Leibler divergence (part 1/2)"
source: https://en.wikipedia.org/wiki/Kullback–Leibler_divergence
domain: variational-bayes
license: CC-BY-SA-4.0
tags: variational Bayesian methods, evidence lower bound, Kullback Leibler divergence, mean field
fetched: 2026-07-02
part: 1/2
---

# Kullback–Leibler divergence

In mathematical statistics, the **Kullback–Leibler** (**KL**) **divergence** (also called **relative entropy** and **I-divergence**), denoted $D_{\text{KL}}(P\parallel Q)$ , is a type of statistical distance: a measure of how much an approximating probability distribution Q is different from a true probability distribution P. Mathematically, it is defined as

$D_{\text{KL}}(P\parallel Q)=\sum _{x\in {\mathcal {X}}}P(x)\,\log {\frac {P(x)}{Q(x)}}{\text{.}}$

A simple interpretation of the KL divergence of P from Q is the expected excess surprisal from using the approximation Q instead of P when the actual is P. While it is a measure of how different two distributions are and is thus a distance in some sense, it is not actually a metric, which is the most familiar and formal type of distance. In particular, it is not symmetric in the two distributions (in contrast to variation of information), and does not satisfy the triangle inequality. Instead, in terms of information geometry, it is a type of divergence, a generalization of squared distance, and for certain classes of distributions (notably an exponential family), it satisfies a generalized Pythagorean theorem (which applies to squared distances).

KL divergence is always a non-negative real number, with value 0 if and only if the two distributions in question are identical. It has diverse applications, both theoretical, such as characterizing the relative (Shannon) entropy in information systems, randomness in continuous time-series, and information gain when comparing statistical models of inference; and practical, such as applied statistics, fluid mechanics, neuroscience, bioinformatics, and machine learning.


## Introduction and context

Consider two probability distributions, a true P and an approximating Q. Often, P represents the data, the observations, or a measured probability distribution and distribution Q represents instead a theory, a model, a description, or another approximation of P. However, sometimes the true distribution P represents a model and the approximating distribution Q represents (simulated) data that are intended to match the true distribution. The Kullback–Leibler divergence $D_{\text{KL}}(P\parallel Q)$ is then interpreted as the average difference of the number of bits required for encoding samples of P using a code optimized for Q rather than one optimized for P.

Note that the roles of P and Q can be reversed in some situations where that is easier to compute and the goal is to minimize $D_{\text{KL}}(P\parallel Q)$ , such as with the expectation–maximization algorithm (EM) and evidence lower bound (ELBO) computations. This role-reversal approach exploits that $D_{\text{KL}}(P\parallel Q)=0$ if and only if $D_{\text{KL}}(Q\parallel P)=0$ and that, in many cases, reducing one has the effect of reducing the other.


## Etymology

The relative entropy was introduced by Solomon Kullback and Richard Leibler in Kullback & Leibler (1951) as "the mean information for discrimination between $H_{1}$ and $H_{2}$ per observation from $\mu _{1}$ ", where one is comparing two probability measures $\mu _{1},\mu _{2}$ , and $H_{1},H_{2}$ are the hypotheses that one is selecting from measure $\mu _{1},\mu _{2}$ (respectively). They denoted this by $I(1:2)$ , and defined the "'divergence' between $\mu _{1}$ and $\mu _{2}$ " as the symmetrized quantity $J(1,2)=I(1:2)+I(2:1)$ , which had already been defined and used by Harold Jeffreys in 1948. In Kullback (1959), the symmetrized form is again referred to as the "divergence", and the relative entropies in each direction are referred to as a "directed divergences" between two distributions; Kullback preferred the term **discrimination information**. The term "divergence" is in contrast to a distance (metric), since the symmetrized divergence does not satisfy the triangle inequality. Numerous references to earlier uses of the symmetrized divergence and to other statistical distances are given in Kullback (1959). The asymmetric "directed divergence" has come to be known as the Kullback–Leibler divergence, while the symmetrized "divergence" is now referred to as the **Jeffreys divergence**.


## Definition

For discrete probability distributions P and Q defined on the same sample space, ${\mathcal {X}}$ , the relative entropy from Q to P is defined to be

$D_{\text{KL}}(P\parallel Q)=\sum _{x\in {\mathcal {X}}}P(x)\,\log {\frac {P(x)}{Q(x)}}{\text{,}}$

which is equivalent to

$D_{\text{KL}}(P\parallel Q)=\left(-\sum _{x\in {\mathcal {X}}}P(x)\,\log Q(x)\right)-\left(-\sum _{x\in {\mathcal {X}}}P(x)\,\log P(x)\right){\text{.}}$

In other words, it is the expectation of the logarithmic difference between the probabilities P and Q, where the expectation is taken using the probabilities P.

Relative entropy is only defined in this way if, for all x, $Q(x)=0$ implies $P(x)=0$ (absolute continuity). Otherwise, it is often defined as $+\infty$ , but the value $\ +\infty \$ is possible even if $Q(x)\neq 0$ everywhere, provided that ${\mathcal {X}}$ is infinite in extent. Analogous comments apply to the continuous and general measure cases defined below.

Whenever $P(x)$ is zero the contribution of the corresponding term is interpreted as zero because

$\lim _{x\to 0^{+}}x\,\log(x)=0{\text{.}}$

For distributions P and Q of a continuous random variable, relative entropy is defined to be the integral

$D_{\text{KL}}(P\parallel Q)=\int _{-\infty }^{\infty }p(x)\,\log {\frac {p(x)}{q(x)}}\,dx{\text{.}}$

where p and q denote the probability density functions of P and Q.

More generally, if P and Q are probability measures on a measurable space ${\mathcal {X}}\,,$ and P is absolutely continuous with respect to Q, then the relative entropy from Q to P is defined as

$D_{\text{KL}}(P\parallel Q)=\int _{x\in {\mathcal {X}}}\log {\frac {dP(x)}{dQ(x)}}\,dP(x){\text{,}}$

where ${\frac {dP(x)}{dQ(x)}}$ is the Radon–Nikodym derivative of P with respect to Q, i.e. the unique Q almost everywhere defined function r on ${\mathcal {X}}$ such that $dP(x)=r(x)dQ(x)$ which exists because P is absolutely continuous with respect to Q. Also we assume the expression on the right-hand side exists. Equivalently (by the chain rule), this can be written as

$D_{\text{KL}}(P\parallel Q)=\int _{x\in {\mathcal {X}}}{\frac {dP(x)}{dQ(x)}}\ \log {\frac {dP(x)}{dQ(x)}}\ dQ(x){\text{,}}$

which is the entropy of P relative to Q. Continuing in this case, if $\mu$ is any measure on ${\mathcal {X}}$ for which densities p and q with $dP(x)=p(x)\,d\mu (x)$ and $dQ(x)=q(x)\,d\mu (x)$ exist (meaning that P and Q are both absolutely continuous with respect to $\mu$ ), then the relative entropy from Q to P is given as

$D_{\text{KL}}(P\parallel Q)=\int _{x\in {\mathcal {X}}}p(x)\,\log {\frac {p(x)}{q(x)}}\ d\mu (x){\text{.}}$

Note that such a measure $\mu$ for which densities can be defined always exists, since one can take ${\textstyle \mu ={\frac {1}{2}}\left(P+Q\right)}$ although in practice it will usually be one that applies in the context such as counting measure for discrete distributions, or Lebesgue measure or a convenient variant thereof such as Gaussian measure or the uniform measure on the sphere, Haar measure on a Lie group etc. for continuous distributions. The logarithms in these formulae are usually taken to base 2 if information is measured in units of bits, or to base e if information is measured in nats. Most formulas involving relative entropy hold regardless of the base of the logarithm.

Various conventions exist for referring to $D_{\text{KL}}(P\parallel Q)$ in words. Often it is referred to as the divergence *between* P and Q, but this fails to convey the fundamental asymmetry in the relation. Sometimes, as in this article, it may be described as the divergence of P *from* Q or as the divergence *from* Q *to* P. This reflects the asymmetry in Bayesian inference, which starts *from* a prior distribution Q and updates *to* the posterior P. Another common way to refer to $D_{\text{KL}}(P\parallel Q)$ is as the relative entropy of P *with respect to* Q or the information gain from P over Q.


## Basic example

Kullback gives the following example (Table 2.1, Example 2.1). Let P and Q be the distributions shown in the table and figure. P is the distribution on the left side of the figure, a binomial distribution with $N=2$ and $p=0.4$ . Q is the distribution on the right side of the figure, a discrete uniform distribution with the three possible outcomes *x* = 0, 1, 2 (i.e. ${\mathcal {X}}=\{0,1,2\}$ ), each with probability $p=1/3$ .

| xDistribution | 0 | 1 | 2 |
|---|---|---|---|
| $P(x)$ | ⁠9/25⁠ | ⁠12/25⁠ | ⁠4/25⁠ |
| $Q(x)$ | ⁠1/3⁠ | ⁠1/3⁠ | ⁠1/3⁠ |

Relative entropies $D_{\text{KL}}(P\parallel Q)$ and $D_{\text{KL}}(Q\parallel P)$ are calculated as follows. This example uses the natural log with base e, designated ln to get results in nats (see units of information):

${\begin{aligned}D_{\text{KL}}(P\parallel Q)&=\sum _{x\in {\mathcal {X}}}P(x)\,\ln {\frac {P(x)}{Q(x)}}\\&={\frac {9}{25}}\ln {\frac {9/25}{1/3}}+{\frac {12}{25}}\ln {\frac {12/25}{1/3}}+{\frac {4}{25}}\ln {\frac {4/25}{1/3}}\\&={\frac {1}{25}}\left(32\ln 2+55\ln 3-50\ln 5\right)\\&\approx 0.0852996{\text{,}}\end{aligned}}$

${\begin{aligned}D_{\text{KL}}(Q\parallel P)&=\sum _{x\in {\mathcal {X}}}Q(x)\,\ln {\frac {Q(x)}{P(x)}}\\&={\frac {1}{3}}\,\ln {\frac {1/3}{9/25}}+{\frac {1}{3}}\,\ln {\frac {1/3}{12/25}}+{\frac {1}{3}}\,\ln {\frac {1/3}{4/25}}\\&={\frac {1}{3}}\left(-4\ln 2-6\ln 3+6\ln 5\right)\\&\approx 0.097455{\text{.}}\end{aligned}}$


## Interpretations

### Statistics

In the field of statistics, the Neyman–Pearson lemma states that the most powerful way to distinguish between the two distributions P and Q based on an observation Y (drawn from one of them) is through the log of the ratio of their likelihoods: $\log P(Y)-\log Q(Y)$ . The KL divergence is the expected value of this statistic if Y is actually drawn from P. Kullback motivated the statistic as an expected log likelihood ratio.

### Coding

In the context of coding theory, $D_{\text{KL}}(P\parallel Q)$ can be constructed by measuring the expected number of extra bits required to code samples from P using a code optimized for Q rather than the code optimized for P.

### Inference

In the context of machine learning, $D_{\text{KL}}(P\parallel Q)$ is often called the information gain achieved if P would be used instead of Q which is currently used. By analogy with information theory, it is called the *relative entropy* of P with respect to Q.

Expressed in the language of Bayesian inference, $D_{\text{KL}}(P\parallel Q)$ is a measure of the information gained by revising one's beliefs from the prior probability distribution Q to the posterior probability distribution P. In other words, it is the amount of information lost when Q is used to approximate P.

### Information geometry

In applications, P typically represents the "true" distribution of data, observations, or a precisely calculated theoretical distribution, while Q typically represents a theory, model, description, or approximation of P. In order to find a distribution Q that is closest to P, we can minimize the KL divergence and compute an information projection.

While it is a statistical distance, it is not a metric, the most familiar type of distance, but instead it is a divergence. While metrics are symmetric and generalize *linear* distance, satisfying the triangle inequality, divergences are asymmetric and generalize *squared* distance, in some cases satisfying a generalized Pythagorean theorem. In general $D_{\text{KL}}(P\parallel Q)$ does not equal $D_{\text{KL}}(Q\parallel P)$ , and the asymmetry is an important part of the geometry. The infinitesimal form of relative entropy, specifically its Hessian, gives a metric tensor that equals the Fisher information metric; see § Fisher information metric. Fisher information metric on the certain probability distribution let determine the natural gradient for information-geometric optimization algorithms. Its quantum version is Fubini-study metric. Relative entropy satisfies a generalized Pythagorean theorem for exponential families (geometrically interpreted as dually flat manifolds), and this allows one to minimize relative entropy by geometric means, for example by information projection and in maximum likelihood estimation.

The relative entropy is the Bregman divergence generated by the negative entropy, but it is also of the form of an f-divergence. For probabilities over a finite alphabet, it is unique in being a member of both of these classes of statistical divergences. The application of Bregman divergence can be found in mirror descent.

### Finance (game theory)

Consider a growth-optimizing investor in a fair game with mutually exclusive outcomes (e.g. a "horse race" in which the official odds add up to one). The rate of return expected by such an investor is equal to the relative entropy between the investor's believed probabilities and the official odds. This is a special case of a much more general connection between financial returns and divergence measures.

Financial risks are connected to $D_{\text{KL}}$ via information geometry. Investors' views, the prevailing market view, and risky scenarios form triangles on the relevant manifold of probability distributions. The shape of the triangles determines key financial risks (both qualitatively and quantitatively). For instance, obtuse triangles in which investors' views and risk scenarios appear on "opposite sides" relative to the market describe negative risks, acute triangles describe positive exposure, and the right-angled situation in the middle corresponds to zero risk. Extending this concept, relative entropy can be hypothetically utilised to identify the behaviour of informed investors, if one takes this to be represented by the magnitude and deviations away from the prior expectations of fund flows, for example.


## Motivation

In information theory, the Kraft–McMillan theorem establishes that any directly decodable coding scheme for coding a message to identify one value $x_{i}$ out of a set of possibilities X can be seen as representing an implicit probability distribution $q(x_{i})=2^{-\ell _{i}}$ over X, where $\ell _{i}$ is the length of the code for $x_{i}$ in bits. Therefore, relative entropy can be interpreted as the expected extra message-length per datum that must be communicated if a code that is optimal for a given (wrong) distribution Q is used, compared to using a code based on the true distribution P: it is the *excess* entropy.

${\begin{aligned}D_{\text{KL}}(P\parallel Q)&=\sum _{x\in {\mathcal {X}}}p(x)\log {\frac {1}{q(x)}}-\sum _{x\in {\mathcal {X}}}p(x)\log {\frac {1}{p(x)}}\\[5pt]&=\mathrm {H} (P,Q)-\mathrm {H} (P)\end{aligned}}$

where $\mathrm {H} (P,Q)$ is the cross entropy of Q relative to P and $\mathrm {H} (P)$ is the entropy of P (which is the same as the cross-entropy of P with itself).

The relative entropy $D_{\text{KL}}(P\parallel Q)$ can be thought of geometrically as a statistical distance, a measure of how far the distribution Q is from the distribution P. Geometrically it is a divergence: an asymmetric, generalized form of squared distance. The cross-entropy $H(P,Q)$ is itself such a measurement (formally a loss function), but it cannot be thought of as a distance, since $H(P,P)=:H(P)$ is not zero. This can be fixed by subtracting $H(P)$ to make $D_{\text{KL}}(P\parallel Q)$ agree more closely with our notion of distance, as the *excess* loss. The resulting function is asymmetric, and while this can be symmetrized (see § Symmetrised divergence), the asymmetric form is more useful. See § Interpretations for more on the geometric interpretation.

Relative entropy relates to "rate function" in the theory of large deviations.

Arthur Hobson proved that relative entropy is the only measure of difference between probability distributions that satisfies some desired properties, which are the canonical extension to those appearing in a commonly used characterization of entropy. Consequently, mutual information is the only measure of mutual dependence that obeys certain related conditions, since it can be defined in terms of Kullback–Leibler divergence.


## Properties

- Relative entropy is always non-negative, $D_{\text{KL}}(P\parallel Q)\geq 0,$ a result known as Gibbs' inequality, with $D_{\text{KL}}(P\parallel Q)$ equals zero if and only if $P=Q$ as measures.

In particular, if $P(dx)=p(x)\mu (dx)$ and $Q(dx)=q(x)\mu (dx)$ , then $p(x)=q(x)$ $\mu$ -almost everywhere. The entropy $\mathrm {H} (P)$ thus sets a minimum value for the cross-entropy $\mathrm {H} (P,Q)$ , the expected number of bits required when using a code based on Q rather than P; and the Kullback–Leibler divergence therefore represents the expected number of extra bits that must be transmitted to identify a value x drawn from X, if a code is used corresponding to the probability distribution Q, rather than the "true" distribution P.

- No upper-bound exists for the general case. However, it is shown that if P and Q are two discrete probability distributions built by distributing the same discrete quantity, then the maximum value of $D_{\text{KL}}(P\parallel Q)$ can be calculated.
- Relative entropy remains well-defined for continuous distributions, and furthermore is invariant under parameter transformations. For example, if a transformation is made from variable x to variable $y(x)$ , then, since $P(dx)=p(x)\,dx={\tilde {p}}(y)\,dy={\tilde {p}}(y(x))\left|{\tfrac {dy}{dx}}(x)\right|\,dx$ and $Q(dx)=q(x)\,dx={\tilde {q}}(y)\,dy={\tilde {q}}(y)\left|{\tfrac {dy}{dx}}(x)\right|dx$ where $\left|{\tfrac {dy}{dx}}(x)\right|$ is the absolute value of the derivative or more generally of the Jacobian, the relative entropy may be rewritten: ${\begin{aligned}D_{\text{KL}}(P\parallel Q)&=\int _{x_{a}}^{x_{b}}p(x)\,\log {\frac {p(x)}{q(x)}}\,dx\\[6pt]&=\int _{x_{a}}^{x_{b}}{\tilde {p}}(y(x))\left|{\frac {dy}{dx}}\right|\log {\frac {{\tilde {p}}(y(x))\,\left|{\frac {dy}{dx}}\right|}{{\tilde {q}}(y(x))\,\left|{\frac {dy}{dx}}\right|}}\,dx\\&=\int _{y_{a}}^{y_{b}}{\tilde {p}}(y)\,\log {\frac {{\tilde {p}}(y)}{{\tilde {q}}(y)}}\,dy\end{aligned}}$ where $y_{a}=y(x_{a})$ and $y_{b}=y(x_{b})$ . Although it was assumed that the transformation was continuous, this need not be the case. This also shows that the relative entropy produces a dimensionally consistent quantity, since if x is a dimensioned variable, $p(x)$ and $q(x)$ are also dimensioned, since e.g. $P(dx)=p(x)\,dx$ is dimensionless. The argument of the logarithmic term is and remains dimensionless, as it must. It can therefore be seen as in some ways a more fundamental quantity than some other properties in information theory (such as self-information or Shannon entropy), which can become undefined or negative for non-discrete probabilities.
- Relative entropy is additive for independent distributions in much the same way as Shannon entropy. If $P_{1},P_{2}$ are independent distributions, and $P(dx,dy)=P_{1}(dx)P_{2}(dy)$ , and likewise $Q(dx,dy)=Q_{1}(dx)Q_{2}(dy)$ for independent distributions $Q_{1},Q_{2}$ then $D_{\text{KL}}(P\parallel Q)=D_{\text{KL}}(P_{1}\parallel Q_{1})+D_{\text{KL}}(P_{2}\parallel Q_{2}).$
- Relative entropy $D_{\text{KL}}(P\parallel Q)$ is convex in the pair of probability measures $(P,Q)$ , i.e. if $(P_{1},Q_{1})$ and $(P_{2},Q_{2})$ are two pairs of probability measures then $D_{\text{KL}}(\lambda P_{1}+(1-\lambda )P_{2}\parallel \lambda Q_{1}+(1-\lambda )Q_{2})\leq \lambda D_{\text{KL}}(P_{1}\parallel Q_{1})+(1-\lambda )D_{\text{KL}}(P_{2}\parallel Q_{2}){\text{ for }}0\leq \lambda \leq 1.$
- $D_{\text{KL}}(P\parallel Q)$ may be Taylor expanded about its minimum (i.e. $P=Q$ ) as $D_{\text{KL}}(P\parallel Q)=\sum _{n=2}^{\infty }{\frac {1}{n(n-1)}}\sum _{x\in {\mathcal {X}}}{\frac {(Q(x)-P(x))^{n}}{Q(x)^{n-1}}}$ which converges if and only if $P\leq 2Q$ almost surely w.r.t Q .

[Proof]

Denote $f(\alpha ):=D_{\text{KL}}((1-\alpha )Q+\alpha P\parallel Q)$ and note that $D_{\text{KL}}(P\parallel Q)=f(1)$ . The first derivative of f may be derived and evaluated as follows ${\begin{aligned}f'(\alpha )&=\sum _{x\in {\mathcal {X}}}(P(x)-Q(x))\left(\log \left({\frac {(1-\alpha )Q(x)+\alpha P(x)}{Q(x)}}\right)+1\right)\\&=\sum _{x\in {\mathcal {X}}}(P(x)-Q(x))\log \left({\frac {(1-\alpha )Q(x)+\alpha P(x)}{Q(x)}}\right)\\f'(0)&=0\end{aligned}}$ Further derivatives may be derived and evaluated as follows ${\begin{aligned}f''(\alpha )&=\sum _{x\in {\mathcal {X}}}{\frac {(P(x)-Q(x))^{2}}{(1-\alpha )Q(x)+\alpha P(x)}}\\f''(0)&=\sum _{x\in {\mathcal {X}}}{\frac {(P(x)-Q(x))^{2}}{Q(x)}}\\f^{(n)}(\alpha )&=(-1)^{n}(n-2)!\sum _{x\in {\mathcal {X}}}{\frac {(P(x)-Q(x))^{n}}{\left((1-\alpha )Q(x)+\alpha P(x)\right)^{n-1}}}\\f^{(n)}(0)&=(-1)^{n}(n-2)!\sum _{x\in {\mathcal {X}}}{\frac {(P(x)-Q(x))^{n}}{Q(x)^{n-1}}}\end{aligned}}$ Hence solving for $D_{\text{KL}}(P\parallel Q)$ via the Taylor expansion of f about 0 evaluated at $\alpha =1$ yields ${\begin{aligned}D_{\text{KL}}(P\parallel Q)&=\sum _{n=0}^{\infty }{\frac {f^{(n)}(0)}{n!}}\\&=\sum _{n=2}^{\infty }{\frac {1}{n(n-1)}}\sum _{x\in {\mathcal {X}}}{\frac {(Q(x)-P(x))^{n}}{Q(x)^{n-1}}}\end{aligned}}$ $P\leq 2Q$ a.s. is a sufficient condition for convergence of the series by the following absolute convergence argument ${\begin{aligned}\sum _{n=2}^{\infty }\left\vert {\frac {1}{n(n-1)}}\sum _{x\in {\mathcal {X}}}{\frac {(Q(x)-P(x))^{n}}{Q(x)^{n-1}}}\right\vert &=\sum _{n=2}^{\infty }{\frac {1}{n(n-1)}}\sum _{x\in {\mathcal {X}}}\left\vert Q(x)-P(x)\right\vert \left\vert 1-{\frac {P(x)}{Q(x)}}\right\vert ^{n-1}\\&\leq \sum _{n=2}^{\infty }{\frac {1}{n(n-1)}}\sum _{x\in {\mathcal {X}}}\left\vert Q(x)-P(x)\right\vert \\&\leq \sum _{n=2}^{\infty }{\frac {1}{n(n-1)}}\\&=1\end{aligned}}$ $P\leq 2Q$ a.s. is also a necessary condition for convergence of the series by the following proof by contradiction. Assume that $P>2Q$ with measure strictly greater than 0 . It then follows that there must exist some values $\varepsilon >0$ , $\rho >0$ , and $U<\infty$ such that $P\geq 2Q+\varepsilon$ and $Q\leq U$ with measure $\rho$ . The previous proof of sufficiency demonstrated that the measure $1-\rho$ component of the series where $P\leq 2Q$ is bounded, so we need only concern ourselves with the behavior of the measure $\rho$ component of the series where $P\geq 2Q+\varepsilon$ . The absolute value of the n th term of this component of the series is then lower bounded by ${\frac {1}{n(n-1)}}\rho \left(1+{\frac {\varepsilon }{U}}\right)^{n}$ , which is unbounded as $n\to \infty$ , so the series diverges.


## Duality formula for variational inference

The following result, due to Donsker and Varadhan, is known as **Donsker and Varadhan's variational formula**.

**Theorem [Duality Formula for Variational Inference]**—Let $\Theta$ be a set endowed with an appropriate $\sigma$ -field ${\mathcal {F}}$ , and two probability measures P and Q, which formulate two probability spaces $(\Theta ,{\mathcal {F}},P)$ and $(\Theta ,{\mathcal {F}},Q)$ , with $Q\ll P$ . ( $Q\ll P$ indicates that Q is absolutely continuous with respect to P.) Let h be a real-valued integrable random variable on $(\Theta ,{\mathcal {F}},P)$ . Then the following equality holds

$\log E_{P}[\exp h]=\operatorname {sup} _{Q\ll P}\{E_{Q}[h]-D_{\text{KL}}(Q\parallel P)\}{\text{.}}$

Further, the supremum on the right-hand side is attained if and only if it holds

${\frac {Q(d\theta )}{P(d\theta )}}={\frac {\exp h(\theta )}{E_{P}[\exp h]}}{\text{,}}$

almost surely with respect to probability measure P, where ${\frac {Q(d\theta )}{P(d\theta )}}$ denotes the Radon-Nikodym derivative of Q with respect to P.

Proof

For a short proof assuming integrability of $\exp(h)$ with respect to P, let $Q^{*}$ have P-density ${\frac {\exp h(\theta )}{E_{P}[\exp h]}}$ , i.e. $Q^{*}(d\theta )={\frac {\exp h(\theta )}{E_{P}[\exp h]}}P(d\theta )$ Then

$D_{\text{KL}}(Q\parallel Q^{*})-D_{\text{KL}}(Q\parallel P)=-E_{Q}[h]+\log E_{P}[\exp h]{\text{.}}$

Therefore,

$E_{Q}[h]-D_{\text{KL}}(Q\parallel P)=\log E_{P}[\exp h]-D_{\text{KL}}(Q\parallel Q^{*})\leq \log E_{P}[\exp h]{\text{,}}$

where the last inequality follows from $D_{\text{KL}}(Q\parallel Q^{*})\geq 0$ , for which equality occurs if and only if $Q=Q^{*}$ . The conclusion follows.


## Examples

### Multivariate normal distributions

Suppose that we have two multivariate normal distributions, with means $\mu _{0},\mu _{1}$ and with (non-singular) covariance matrices $\Sigma _{0},\Sigma _{1}.$ If the two distributions have the same dimension, k, then the relative entropy between the distributions is as follows:

$D_{\text{KL}}\left({\mathcal {N}}_{0}\parallel {\mathcal {N}}_{1}\right)={\frac {1}{2}}\left[\operatorname {tr} \left(\Sigma _{1}^{-1}\Sigma _{0}\right)-k+\left(\mu _{1}-\mu _{0}\right)^{\mathsf {T}}\Sigma _{1}^{-1}\left(\mu _{1}-\mu _{0}\right)+\ln {\frac {\det \Sigma _{1}}{\det \Sigma _{0}}}\right]{\text{.}}$

The logarithm in the last term must be taken to base e since all terms apart from the last are base-e logarithms of expressions that are either factors of the density function or otherwise arise naturally. The equation therefore gives a result measured in nats. Dividing the entire expression above by $\ln(2)$ yields the divergence in bits.

In a numerical implementation, it is helpful to express the result in terms of the Cholesky decompositions $L_{0},L_{1}$ such that $\Sigma _{0}=L_{0}L_{0}^{T}$ and $\Sigma _{1}=L_{1}L_{1}^{T}$ . Then with M and y solutions to the triangular linear systems $L_{1}M=L_{0}$ , and $L_{1}y=\mu _{1}-\mu _{0}$ ,

$D_{\text{KL}}\left({\mathcal {N}}_{0}\parallel {\mathcal {N}}_{1}\right)={\frac {1}{2}}\left(\sum _{i,j=1}^{k}{\left(M_{ij}\right)}^{2}-k+|y|^{2}+2\sum _{i=1}^{k}\ln {\frac {(L_{1})_{ii}}{(L_{0})_{ii}}}\right){\text{.}}$

A special case, and a common quantity in variational inference, is the relative entropy between a diagonal multivariate normal, and a standard normal distribution (with zero mean and unit variance):

$D_{\text{KL}}\left({\mathcal {N}}\left(\left(\mu _{1},\ldots ,\mu _{k}\right)^{\mathsf {T}},\operatorname {diag} \left(\sigma _{1}^{2},\ldots ,\sigma _{k}^{2}\right)\right)\parallel {\mathcal {N}}\left(\mathbf {0} ,\mathbf {I} \right)\right)={\frac {1}{2}}\sum _{i=1}^{k}\left[\sigma _{i}^{2}+\mu _{i}^{2}-1-\ln \left(\sigma _{i}^{2}\right)\right]{\text{.}}$

For two univariate normal distributions **p** and **q** the above simplifies to $D_{\text{KL}}\left({\mathcal {p}}\parallel {\mathcal {q}}\right)=\log {\frac {\sigma _{1}}{\sigma _{0}}}+{\frac {\sigma _{0}^{2}+{\left(\mu _{0}-\mu _{1}\right)}^{2}}{2\sigma _{1}^{2}}}-{\frac {1}{2}}$

In the case of co-centered normal distributions with $k=\sigma _{1}/\sigma _{0}$ , this simplifies to:

$D_{\text{KL}}\left({\mathcal {p}}\parallel {\mathcal {q}}\right)=\log _{2}k+(k^{-2}-1)/2/\ln(2)\mathrm {bits}$

### Uniform distributions

Consider two uniform distributions, with the support of $p=[A,B]$ enclosed within $q=[C,D]$ ( $C\leq A<B\leq D$ ). Then the information gain is:

$D_{\text{KL}}\left({\mathcal {p}}\parallel {\mathcal {q}}\right)=\log {\frac {D-C}{B-A}}$

Intuitively, the information gain to a k times narrower uniform distribution contains $\log _{2}k$ bits. This connects with the use of bits in computing, where $\log _{2}k$ bits would be needed to identify one element of a k long stream.

### Exponential family

The exponential family of distribution is given by

$p_{X}(x|\theta )=h(x)\exp \left(\theta ^{\mathsf {T}}T(x)-A(\theta )\right)$

where $h(x)$ is reference measure, $T(x)$ is sufficient statistics, $\theta$ is canonical natural parameters, and $A(\theta )$ is the log-partition function.

The KL divergence between two distributions $p(x|\theta _{1})$ and $p(x|\theta _{2})$ is given by

$D_{\text{KL}}(\theta _{1}\parallel \theta _{2})={\left(\theta _{1}-\theta _{2}\right)}^{\mathsf {T}}\mu _{1}-A(\theta _{1})+A(\theta _{2})$

where $\mu _{1}=E_{\theta _{1}}[T(X)]=\nabla A(\theta _{1})$ is the mean parameter of $p(x|\theta _{1})$ .

For example, for the Poisson distribution with mean $\lambda$ , the sufficient statistics $T(x)=x$ , the natural parameter $\theta =\log \lambda$ , and log partition function $A(\theta )=e^{\theta }$ . As such, the divergence between two Poisson distributions with means $\lambda _{1}$ and $\lambda _{2}$ is

$D_{\text{KL}}(\lambda _{1}\parallel \lambda _{2})=\lambda _{1}\log {\frac {\lambda _{1}}{\lambda _{2}}}-\lambda _{1}+\lambda _{2}{\text{.}}$

As another example, for a normal distribution with unit variance $N(\mu ,1)$ , the sufficient statistics $T(x)=x$ , the natural parameter $\theta =\mu$ , and log partition function $A(\theta )=\mu ^{2}/2$ . Thus, the divergence between two normal distributions $N(\mu _{1},1)$ and $N(\mu _{2},1)$ is

$D_{\text{KL}}(\mu _{1}\parallel \mu _{2})=\left(\mu _{1}-\mu _{2}\right)\mu _{1}-{\frac {\mu _{1}^{2}}{2}}+{\frac {\mu _{2}^{2}}{2}}={\frac {{\left(\mu _{2}-\mu _{1}\right)}^{2}}{2}}{\text{.}}$

As final example, the divergence between a normal distribution with unit variance $N(\mu ,1)$ and a Poisson distribution with mean $\lambda$ is

$D_{\text{KL}}(\mu \parallel \lambda )=(\mu -\log \lambda )\mu -{\frac {\mu ^{2}}{2}}+\lambda {\text{.}}$


## Relation to metrics

While relative entropy is a statistical distance, it is not a metric on the space of probability distributions, but instead it is a divergence. While metrics are symmetric and generalize *linear* distance, satisfying the triangle inequality, divergences are asymmetric in general and generalize *squared* distance, in some cases satisfying a generalized Pythagorean theorem. In general $D_{\text{KL}}(P\parallel Q)$ does not equal $D_{\text{KL}}(Q\parallel P)$ , and while this can be symmetrized (see § Symmetrised divergence), the asymmetry is an important part of the geometry.

It generates a topology on the space of probability distributions. More concretely, if $\{P_{1},P_{2},\ldots \}$ is a sequence of distributions such that

$\lim _{n\to \infty }D_{\text{KL}}(P_{n}\parallel Q)=0{\text{,}}$

then it is said that

$P_{n}\xrightarrow {D} \,Q{\text{.}}$

Pinsker's inequality entails that

$P_{n}\xrightarrow {D} P\Rightarrow P_{n}\xrightarrow {TV} P{\text{,}}$

where the latter stands for the usual convergence in total variation.

### Fisher information metric

Relative entropy is directly related to the Fisher information metric. This can be made explicit as follows. Assume that the probability distributions P and Q are both parameterized by some (possibly multi-dimensional) parameter $\theta$ . Consider then two close by values of $P=P(\theta )$ and $Q=P(\theta _{0})$ so that the parameter $\theta$ differs by only a small amount from the parameter value $\theta _{0}$ . Specifically, up to first order one has (using the Einstein summation convention) $P(\theta )=P(\theta _{0})+\Delta \theta _{j}\,P_{j}(\theta _{0})+\cdots$

with $\Delta \theta _{j}=(\theta -\theta _{0})_{j}$ a small change of $\theta$ in the j direction, and $P_{j}\left(\theta _{0}\right)={\frac {\partial P}{\partial \theta _{j}}}(\theta _{0})$ the corresponding rate of change in the probability distribution. Since relative entropy has an absolute minimum 0 for $P=Q$ , i.e. $\theta =\theta _{0}$ , it changes only to *second* order in the small parameters $\Delta \theta _{j}$ . More formally, as for any minimum, the first derivatives of the divergence vanish

$\left.{\frac {\partial }{\partial \theta _{j}}}\right|_{\theta =\theta _{0}}D_{\text{KL}}(P(\theta )\parallel P(\theta _{0}))=0,$

and by the Taylor expansion one has up to second order

$D_{\text{KL}}(P(\theta )\parallel P(\theta _{0}))={\frac {1}{2}}\,\Delta \theta _{j}\,\Delta \theta _{k}\,g_{jk}(\theta _{0})+\cdots$

where the Hessian matrix of the divergence

$g_{jk}(\theta _{0})=\left.{\frac {\partial ^{2}}{\partial \theta _{j}\,\partial \theta _{k}}}\right|_{\theta =\theta _{0}}D_{\text{KL}}(P(\theta )\parallel P(\theta _{0}))$

must be positive semi-definite. Letting $\theta _{0}$ vary (and dropping the subindex 0) the Hessian $g_{jk}(\theta )$ defines a (possibly degenerate) Riemannian metric on the θ parameter space, called the Fisher information metric.

#### Fisher information metric theorem

There is an associated theorem. When $p_{(x,\rho )}$ satisfies the following regularity conditions:

${\frac {\partial \log(p)}{\partial \rho }},{\frac {\partial ^{2}\log(p)}{\partial \rho ^{2}}},{\frac {\partial ^{3}\log(p)}{\partial \rho ^{3}}}$ exist, ${\begin{aligned}\left|{\frac {\partial p}{\partial \rho }}\right|&<F(x):\int _{x=0}^{\infty }F(x)\,dx<\infty ,\\\left|{\frac {\partial ^{2}p}{\partial \rho ^{2}}}\right|&<G(x):\int _{x=0}^{\infty }G(x)\,dx<\infty \\\left|{\frac {\partial ^{3}\log(p)}{\partial \rho ^{3}}}\right|&<H(x):\int _{x=0}^{\infty }p(x,0)H(x)\,dx<\xi <\infty \end{aligned}}$

where ξ is independent of ρ $\left.\int _{x=0}^{\infty }{\frac {\partial p(x,\rho )}{\partial \rho }}\right|_{\rho =0}\,dx=\left.\int _{x=0}^{\infty }{\frac {\partial ^{2}p(x,\rho )}{\partial \rho ^{2}}}\right|_{\rho =0}\,dx=0$

then: ${\mathcal {D}}(p(x,0)\parallel p(x,\rho ))={\frac {c\rho ^{2}}{2}}+{\mathcal {O}}\left(\rho ^{3}\right){\text{ as }}\rho \to 0{\text{.}}$

### Variation of information

Another information-theoretic metric is variation of information, which is roughly a symmetrization of conditional entropy. It is a metric on the set of partitions of a discrete probability space.

### MAUVE Metric

MAUVE is a measure of the statistical gap between two text distributions, such as the difference between text generated by a model and human-written text. This measure is computed using Kullback–Leibler divergences between the two distributions in a quantized embedding space of a foundation model.


## Relation to other quantities of information theory

Many of the other quantities of information theory can be interpreted as applications of relative entropy to specific cases.

### Self-information

The self-information, also known as the information content of a signal, random variable, or event is defined as the negative logarithm of the probability of the given outcome occurring.

When applied to a discrete random variable, the self-information can be represented as

$\operatorname {\operatorname {I} } (m)=D_{\text{KL}}\left(\delta _{\text{im}}\parallel \{p_{i}\}\right),$

is the relative entropy of the probability distribution $P(i)$ from a Kronecker delta representing certainty that $i=m$ — i.e. the number of extra bits that must be transmitted to identify i if only the probability distribution $P(i)$ is available to the receiver, not the fact that $i=m$ .

### Mutual information

The mutual information,

${\begin{aligned}\operatorname {I} (X;Y)&=D_{\text{KL}}(P_{X,Y}\parallel P_{X}\cdot P_{Y})\\&=\operatorname {E} _{X}[D_{\text{KL}}^{Y}(P_{Y\mid X}\parallel P_{Y})]\\&=\operatorname {E} _{Y}[D_{\text{KL}}^{X}(P_{X\mid Y}\parallel P_{X})]\end{aligned}}$

is the relative entropy of the joint probability distribution $P_{X,Y}(x,y)$ from the product $(P_{X}\cdot P_{Y})(x,y)=P_{X}(x)P_{Y}(y)$ of the two marginal probability distributions — i.e. the expected number of extra bits that must be transmitted to identify X and Y if they are coded using only their marginal distributions instead of the joint distribution.

### Shannon entropy

The Shannon entropy,

${\begin{aligned}\mathrm {H} (X)&=\operatorname {E} \left[\operatorname {I} _{X}(x)\right]\\&=\log N-D_{\text{KL}}{\left(p_{X}(x)\parallel P_{U}(X)\right)}\end{aligned}}$

is the number of bits which would have to be transmitted to identify X from N equally likely possibilities, *less* the relative entropy of the uniform distribution on the random variates of X, $P_{U}(X)$ , from the true distribution $P(X)$ — i.e. *less* the expected number of bits saved, which would have had to be sent if the value of X were coded according to the uniform distribution $P_{U}(X)$ rather than the true distribution $P(X)$ . This definition of Shannon entropy forms the basis of E.T. Jaynes's alternative generalization to continuous distributions, the limiting density of discrete points (as opposed to the usual differential entropy), which defines the continuous entropy as $\lim _{N\to \infty }H_{N}(X)=\log N-\int p(x)\log {\frac {p(x)}{m(x)}}\,dx{\text{,}}$ which is equivalent to: $\log(N)-D_{\text{KL}}(p(x)||m(x))$

### Conditional entropy

The conditional entropy,

${\begin{aligned}\mathrm {H} (X\mid Y)&=\log N-D_{\text{KL}}(P(X,Y)\parallel P_{U}(X)P(Y))\\[5pt]&=\log N-D_{\text{KL}}(P(X,Y)\parallel P(X)P(Y))-D_{\text{KL}}(P(X)\parallel P_{U}(X))\\[5pt]&=\mathrm {H} (X)-\operatorname {I} (X;Y)\\[5pt]&=\log N-\operatorname {E} _{Y}\left[D_{\text{KL}}\left(P\left(X\mid Y\right)\parallel P_{U}(X)\right)\right]\end{aligned}}$

is the number of bits which would have to be transmitted to identify X from N equally likely possibilities, *less* the relative entropy of the true joint distribution $P(X,Y)$ from the product distribution $P_{U}(X)P(Y)$ from — i.e. *less* the expected number of bits saved which would have had to be sent if the value of X were coded according to the uniform distribution $P_{U}(X)$ rather than the conditional distribution $P(X|Y)$ of X given Y.

### Cross entropy

When we have a set of possible events, coming from the distribution p, we can encode them (with a lossless data compression) using entropy encoding. This compresses the data by replacing each fixed-length input symbol with a corresponding unique, variable-length, prefix-free code (e.g.: the events (A, B, C) with probabilities p = (1/2, 1/4, 1/4) can be encoded as the bits (0, 10, 11)). If we know the distribution p in advance, we can devise an encoding that would be optimal (e.g.: using Huffman coding). Meaning the messages we encode will have the shortest length on average (assuming the encoded events are sampled from p), which will be equal to Shannon's Entropy of p (denoted as $\mathrm {H} (p)$ ). However, if we use a different probability distribution (q) when creating the entropy encoding scheme, then a larger number of bits will be used (on average) to identify an event from a set of possibilities. This new (larger) number is measured by the cross entropy between p and q.

The cross entropy between two probability distributions (p and q) measures the average number of bits needed to identify an event from a set of possibilities, if a coding scheme is used based on a given probability distribution q, rather than the "true" distribution p. The cross entropy for two distributions p and q over the same probability space is thus defined as follows.

$\mathrm {H} (p,q)=\operatorname {E} _{p}[-\log q]=\mathrm {H} (p)+D_{\text{KL}}(p\parallel q)$

For explicit derivation of this, see the Motivation section above.

Under this scenario, relative entropies (kl-divergence) can be interpreted as the extra number of bits, on average, that are needed (beyond $\mathrm {H} (p)$ ) for encoding the events because of using q for constructing the encoding scheme instead of p.


## Bayesian updating

In Bayesian statistics, relative entropy can be used as a measure of the information gain in moving from a prior distribution to a posterior distribution: $p(x)\to p(x\mid I)$ . If some new fact $Y=y$ is discovered, it can be used to update the posterior distribution for X from $p(x\mid I)$ to a new posterior distribution $p(x\mid y,I)$ using Bayes' theorem:

$p(x\mid y,I)={\frac {p(y\mid x,I)p(x\mid I)}{p(y\mid I)}}$

This distribution has a new entropy:

$\mathrm {H} {\big (}p(x\mid y,I){\big )}=-\sum _{x}p(x\mid y,I)\log p(x\mid y,I){\text{,}}$

which may be less than or greater than the original entropy $\mathrm {H} (p(x\mid I))$ . However, from the standpoint of the new probability distribution one can estimate that to have used the original code based on $p(x\mid I)$ instead of a new code based on $p(x\mid y,I)$ would have added an expected number of bits:

$D_{\text{KL}}{\big (}p(x\mid y,I)\parallel p(x\mid I){\big )}=\sum _{x}p(x\mid y,I)\log {\frac {p(x\mid y,I)}{p(x\mid I)}}$

to the message length. This therefore represents the amount of useful information, or information gain, about X, that has been learned by discovering $Y=y$ .

If a further piece of data, $Y_{2}=y_{2}$ , subsequently comes in, the probability distribution for x can be updated further, to give a new best guess $p(x\mid y_{1},y_{2},I)$ . If one reinvestigates the information gain for using $p(x\mid y_{1},I)$ rather than $p(x\mid I)$ , it turns out that it may be either greater or less than previously estimated:

$\sum _{x}p(x\mid y_{1},y_{2},I)\log {\frac {p(x\mid y_{1},y_{2},I)}{p(x\mid I)}}$ may be ≤ or > than ${\textstyle \sum _{x}p(x\mid y_{1},I)\log {\frac {p(x\mid y_{1},I)}{p(x\mid I)}}}$

and so the combined information gain does *not* obey the triangle inequality:

$D_{\text{KL}}{\big (}p(x\mid y_{1},y_{2},I)\parallel p(x\mid I){\big )}$ may be <, = or > than $D_{\text{KL}}{\big (}p(x\mid y_{1},y_{2},I)\parallel p(x\mid y_{1},I){\big )}+D_{\text{KL}}{\big (}p(x\mid y_{1},I)\parallel p(x\mid I){\big )}$

All one can say is that on *average*, averaging using $p(y_{2}\mid y_{1},x,I)$ , the two sides will average out.

### Bayesian experimental design

A common goal in Bayesian experimental design is to maximise the expected relative entropy between the prior and the posterior. When posteriors are approximated to be Gaussian distributions, a design maximising the expected relative entropy is called Bayes d-optimal.


## Discrimination information

Relative entropy ${\textstyle D_{\text{KL}}{\bigl (}p(x\mid H_{1})\parallel p(x\mid H_{0}){\bigr )}}$ can also be interpreted as the expected **discrimination information** for $H_{1}$ over $H_{0}$ : the mean information per sample for discriminating in favor of a hypothesis $H_{1}$ against a hypothesis $H_{0}$ , when hypothesis $H_{1}$ is true. Another name for this quantity, given to it by I. J. Good, is the expected weight of evidence for $H_{1}$ over $H_{0}$ to be expected from each sample.

The expected weight of evidence for $H_{1}$ over $H_{0}$ is **not** the same as the information gain expected per sample about the probability distribution $p(H)$ of the hypotheses,

$D_{\text{KL}}(p(x\mid H_{1})\parallel p(x\mid H_{0}))\neq IG=D_{\text{KL}}(p(H\mid x)\parallel p(H\mid I)){\text{.}}$

Either of the two quantities can be used as a utility function in Bayesian experimental design, to choose an optimal next question to investigate: but they will in general lead to rather different experimental strategies.

On the entropy scale of *information gain* there is very little difference between near certainty and absolute certainty—coding according to a near certainty requires hardly any more bits than coding according to an absolute certainty. On the other hand, on the logit scale implied by weight of evidence, the difference between the two is enormous – infinite perhaps; this might reflect the difference between being almost sure (on a probabilistic level) that, say, the Riemann hypothesis is correct, compared to being certain that it is correct because one has a mathematical proof. These two different scales of loss function for uncertainty are *both* useful, according to how well each reflects the particular circumstances of the problem in question.

### Principle of minimum discrimination information

The idea of relative entropy as discrimination information led Kullback to propose the Principle of **Minimum Discrimination Information** (**MDI**): given new facts, a new distribution f should be chosen which is as hard to discriminate from the original distribution $f_{0}$ as possible; so that the new data produces as small an information gain $D_{\text{KL}}(f\parallel f_{0})$ as possible.

For example, if one had a prior distribution $p(x,a)$ over x and a, and subsequently learnt the true distribution of a was $u(a)$ , then the relative entropy between the new joint distribution for x and a, $q(x\mid a)u(a)$ , and the earlier prior distribution would be:

$D_{\text{KL}}(q(x\mid a)u(a)\parallel p(x,a))=\operatorname {E} _{u(a)}\left\{D_{\text{KL}}(q(x\mid a)\parallel p(x\mid a))\right\}+D_{\text{KL}}(u(a)\parallel p(a)),$

i.e. the sum of the relative entropy of $p(a)$ the prior distribution for a from the updated distribution $u(a)$ , plus the expected value (using the probability distribution $u(a)$ ) of the relative entropy of the prior conditional distribution $p(x\mid a)$ from the new conditional distribution $q(x\mid a)$ . (Note that often the later expected value is called the *conditional relative entropy* (or *conditional Kullback–Leibler divergence*) and denoted by $D_{\text{KL}}(q(x\mid a)\parallel p(x\mid a))$ ) This is minimized if $q(x\mid a)=p(x\mid a)$ over the whole support of $u(a)$ ; and we note that this result incorporates Bayes' theorem, if the new distribution $u(a)$ is in fact a δ function representing certainty that a has one particular value.

MDI can be seen as an extension of Laplace's Principle of Insufficient Reason, and the Principle of Maximum Entropy of E.T. Jaynes. In particular, it is the natural extension of the principle of maximum entropy from discrete to continuous distributions, for which Shannon entropy ceases to be so useful (see *differential entropy*), but the relative entropy continues to be just as relevant.

In the engineering literature, MDI is sometimes called the **Principle of Minimum Cross-Entropy** (MCE) or **Minxent** for short. Minimising relative entropy from m to p with respect to m is equivalent to minimizing the cross-entropy of p and m, since

$\mathrm {H} (p,m)=\mathrm {H} (p)+D_{\text{KL}}(p\parallel m),$

which is appropriate if one is trying to choose an adequate approximation to p. However, this is just as often *not* the task one is trying to achieve. Instead, just as often it is m that is some fixed prior reference measure, and p that one is attempting to optimise by minimising $D_{\text{KL}}(p\parallel m)$ subject to some constraint. This has led to some ambiguity in the literature, with some authors attempting to resolve the inconsistency by redefining cross-entropy to be $D_{\text{KL}}(p\parallel m)$ , rather than $\mathrm {H} (p,m)$ .
