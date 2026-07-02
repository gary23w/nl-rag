---
title: "Doob's martingale inequality"
source: https://en.wikipedia.org/wiki/Doob's_martingale_inequality
domain: martingale-theory
license: CC-BY-SA-4.0
tags: martingale theory, stopping time, conditional expectation, optional stopping theorem
fetched: 2026-07-02
---

# Doob's martingale inequality

In mathematics, **Doob's martingale inequality**, also known as **Kolmogorov's submartingale inequality**, is a fundamental result in the study of stochastic processes.

Key aspects of the inequality include:

- It gives a bound on the probability that a submartingale exceeds any given value over a given interval of time.
- By bounding the running maximum of a stochastic process using only its terminal expectation, it provides a powerful tool for analyzing the extreme behaviors of sample paths.
- As the name suggests, the result is usually given in the case that the process is a martingale, but the core mathematics inherently apply to submartingales.
- The inequality is due to the American mathematician Joseph L. Doob.

## Statement of the inequality

The setting of Doob's inequality is a submartingale relative to a filtration of the underlying probability space.

- The probability measure on the sample space of the martingale will be denoted by P .
- The corresponding expected value of a random variable X , as defined by Lebesgue integration, will be denoted by $\operatorname {E} [X]$ .

Informally, Doob's inequality states that the expected value of the process at some final time controls the probability that a sample path will reach above any particular value beforehand. As the proof uses very direct reasoning, it does not require any restrictive assumptions on the underlying filtration or on the process itself, unlike for many other theorems about stochastic processes. In the continuous-time setting, right-continuity (or left-continuity) of the sample paths is required, but only for the sake of knowing that the supremal value of a sample path equals the supremum over an arbitrary countable dense subset of times.

### Discrete time

Let $X_{1},\dots ,X_{n}$ be a discrete-time submartingale relative to a filtration ${\mathcal {F}}_{1},\ldots ,{\mathcal {F}}_{n}$ of the underlying probability space, which is to say:

$X_{i}\leq \operatorname {E} [X_{i+1}\mid {\mathcal {F}}_{i}].$

The **submartingale inequality** (which constitutes the formal statement of Doob's martingale inequality) says that:

$P\left[\max _{1\leq i\leq n}X_{i}\geq C\right]\leq {\frac {\operatorname {E} [\max(X_{n},0)]}{C}}$

for any positive number C .

**Proof:**

- The proof relies on the set-theoretic fact that the event defined by $\max X_{i}>C$ may be decomposed as the disjoint union of the events $E_{i}$ defined by $X_{i}>C$ and $X_{j}\leq C$ for all $j<i$ .
- Then we can formulate the integral:

$CP(E_{i})=\int _{E_{i}}C\,dP\leq \int _{E_{i}}X_{i}\,dP\leq \int _{E_{i}}\operatorname {E} [X_{n}\mid {\mathcal {F}}_{i}]\,dP=\int _{E_{i}}X_{n}\,dP,$

- This makes use of the submartingale property for the last inequality and the fact that $E_{i}\in {\mathcal {F}}_{i}$ for the last equality.
- Summing this result as i ranges from 1 to n results in the conclusion:

$CP(E)\leq \int _{E}X_{n}\,dP,$

- This is sharper than the stated result. By using the elementary fact that $X_{n}\leq \max(X_{n},0)$ , the given submartingale inequality follows.

In this proof, the submartingale property is used once, together with the definition of conditional expectation. The proof can also be phrased in the language of stochastic processes so as to become a corollary of the powerful theorem that a stopped submartingale is itself a submartingale. In this setup, the minimal index i appearing in the above proof is interpreted as a stopping time.

### Continuous time

Now let $X_{t}$ be a submartingale indexed by an interval $[0,T]$ of real numbers, relative to a filtration ${\mathcal {F}}_{t}$ of the underlying probability space, which is to say:

$X_{s}\leq \operatorname {E} [X_{t}\mid {\mathcal {F}}_{s}].$

for all $s<t$ .

The continuous-time formulation of Doob's inequality states that if the sample paths of the martingale are almost-surely right-continuous, then:

$P\left[\sup _{0\leq t\leq T}X_{t}\geq C\right]\leq {\frac {\operatorname {E} [\max(X_{T},0)]}{C}}$

for any positive number C .

**Proof Derivation:**

- This is a corollary of the above discrete-time result, obtained by writing:

$\sup _{0\leq t\leq T}X_{t}=\sup\{X_{t}:t\in [0,T]\cap \mathbb {Q} \}=\lim _{i\to \infty }\sup\{X_{t}:t\in [0,T]\cap Q_{i}\}$

- In this expression, $Q_{1}\subset Q_{2}\subset \dots$ is any sequence of finite sets whose union is the set of all rational numbers.
- The first equality is a consequence of the right-continuity assumption, while the second equality is purely set-theoretic.
- The discrete-time inequality applies to say that:

$P\left[\sup _{t\in [0,T]\cap Q_{i}}X_{t}\geq C\right]\leq {\frac {\operatorname {E} [\max(X_{T},0)]}{C}}$

- This relation holds for each i , and this passes to the limit to yield the submartingale inequality.

This passage from discrete time to continuous time is very flexible, as it only requires having a countable dense subset of $[0,T]$ , which can then automatically be built out of an increasing sequence of finite sets. As such, the submartingale inequality holds even for more general index sets, which are not required to be intervals or natural numbers.

## Further inequalities

There are further submartingale inequalities also due to Doob. Now let $X_{t}$ be a martingale or a positive submartingale; if the index set is uncountable, then (as above) assume that the sample paths are right-continuous.

Under these conditions:

- Jensen's inequality implies that $|X_{t}|^{p}$ is a submartingale for any number $p\geq 1$ , provided that these new random variables all have finite integral.
- The submartingale inequality is then applicable to say that:

$P\left[\sup _{0\leq t\leq T}|X_{t}|\geq C\right]\leq {\frac {\operatorname {E} [|X_{T}|^{p}]}{C^{p}}}$

for any positive number C . Here T is the *final time*, i.e. the largest value of the index set.

- Furthermore, one has:

$\operatorname {E} [|X_{T}|^{p}]\leq \operatorname {E} \left[\sup _{0\leq s\leq T}|X_{s}|^{p}\right]\leq \left({\frac {p}{p-1}}\right)^{p}\operatorname {E} [|X_{T}|^{p}]$

if p is larger than one.

- This secondary result is known as **Doob's maximal inequality**. It is a direct result of combining the layer cake representation with the submartingale inequality and the Hölder inequality.

In addition to the above inequality, the following relationship also holds:

$\operatorname {E} \left[\sup _{0\leq s\leq T}X_{s}\right]\leq {\frac {e}{e-1}}\left(1+\operatorname {E} [\max\{|X_{T}|\log |X_{T}|,0\}]\right)$

- **Kolmogorov's Inequality:** Doob's inequality for discrete-time martingales directly implies Kolmogorov's inequality. If $X_{1},X_{2},\dots$ is a sequence of real-valued independent random variables, each with mean zero, it is clear that:

${\begin{aligned}\operatorname {E} \left[X_{1}+\cdots +X_{n}+X_{n+1}\mid X_{1},\ldots ,X_{n}\right]&=X_{1}+\cdots +X_{n}+\operatorname {E} \left[X_{n+1}\mid X_{1},\ldots ,X_{n}\right]\\&=X_{1}+\cdots +X_{n},\end{aligned}}$

- Consequently, the partial sums $S_{n}=X_{1}+\dots +X_{n}$ form a martingale.
- Note that Jensen's inequality implies that $|S_{n}|$ is a nonnegative submartingale if $S_{n}$ is a martingale.
- Hence, taking $p=2$ in Doob's martingale inequality gives:

$P\left[\max _{1\leq i\leq n}\left|S_{i}\right|\geq \lambda \right]\leq {\frac {\operatorname {E} \left[S_{n}^{2}\right]}{\lambda ^{2}}},$

which is precisely the statement of Kolmogorov's inequality.

- **Burkholder–Davis–Gundy inequalities:** Doob's maximal inequality acts as a precursor to the more general Burkholder–Davis–Gundy inequalities, which provide two-sided bounds relating the maximum of a martingale to its quadratic variation.
- The last one of Doob's martingale inequalities can be improved to the following inequalities that holds for non-negative martingales

${\begin{aligned}\gamma (\max _{1\leq i\leq n}X_{i})&\leq E(X_{n}\ln(X_{n}))\\\gamma (\min _{1\leq i\leq n}X_{i})&\leq E(X_{n}\ln(X_{n}))\end{aligned}}$

where $\gamma (x)=x-1-\ln(x).$

## Significance and applications

### Stochastic calculus

Doob's maximal inequality, particularly in the $p=2$ case, is foundational to the rigorous construction of the Itô integral. It guarantees that the sequence of integrals of simple predictable processes converges uniformly in the space of square-integrable martingales. This boundedness is what allows the integral definition to be safely extended to a much broader class of predictable processes via the Itô isometry.

### Martingale convergence

The submartingale inequality serves as a fundamental stepping stone in the proofs of Doob's martingale convergence theorems. By bounding the probability of extreme excursions of the sample paths, it ensures that martingales with bounded expectations do not oscillate infinitely. This mathematically enforces the condition required for the sequence to converge almost surely to a well-defined limit.

### Bounding Brownian motion

Doob's inequality provides a direct way to bound the maximum of canonical one-dimensional Brownian motion, denoted here as B . Because the exponential function is monotonically increasing, for any non-negative $\lambda$ :

$\left\{\sup _{0\leq t\leq T}B_{t}\geq C\right\}=\left\{\sup _{0\leq t\leq T}\exp(\lambda B_{t})\geq \exp(\lambda C)\right\}.$

By applying Doob's inequality, and noting that the exponential of Brownian motion is a positive submartingale, we obtain:

${\begin{aligned}P\left[\sup _{0\leq t\leq T}B_{t}\geq C\right]&=P\left[\sup _{0\leq t\leq T}\exp(\lambda B_{t})\geq \exp(\lambda C)\right]\\[8pt]&\leq {\frac {\operatorname {E} [\exp(\lambda B_{T})]}{\exp(\lambda C)}}\\[8pt]&=\exp \left({\tfrac {1}{2}}\lambda ^{2}T-\lambda C\right)&&\left({\text{since }}\operatorname {E} \left[\exp(\lambda B_{t})\right]=\exp \left({\tfrac {1}{2}}\lambda ^{2}t\right)\right)\end{aligned}}$

Since the left-hand side does not depend on $\lambda$ , we can minimize the right-hand side by choosing $\lambda =C/T$ . This provides the final bound:

$P\left[\sup _{0\leq t\leq T}B_{t}\geq C\right]\leq \exp \left(-{\frac {C^{2}}{2T}}\right).$
