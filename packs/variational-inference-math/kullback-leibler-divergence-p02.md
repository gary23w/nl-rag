---
title: "Kullback–Leibler divergence (part 2/2)"
source: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
domain: variational-inference-math
license: CC-BY-SA-4.0
tags: variational bayesian methods, evidence lower bound, mean field theory, kullback-leibler divergence
fetched: 2026-07-02
part: 2/2
---

## Relationship to available work

Surprisals add where probabilities multiply. The surprisal for an event of probability p is defined as $s=-k\ln p$ . If k is $\left\{1,1/\ln 2,1.38\times 10^{-23}\right\}$ then surprisal is in $\{$ nats, bits, or $J/K\}$ so that, for instance, there are N bits of surprisal for landing all "heads" on a toss of N coins.

Best-guess states (e.g. for atoms in a gas) are inferred by maximizing the *average surprisal* S (entropy) for a given set of control parameters (like pressure P or volume V). This constrained entropy maximization, both classically and quantum mechanically, minimizes Gibbs availability in entropy units $A\equiv -k\ln Z$ where Z is a constrained multiplicity or partition function.

When temperature T is fixed, free energy ( $T\times A$ ) is also minimized. Thus if $T,V$ and number of molecules N are constant, the Helmholtz free energy $F\equiv U-TS$ (where U is energy and S is entropy) is minimized as a system "equilibrates." If T and P are held constant (say during processes in your body), the Gibbs free energy $G=U+PV-TS$ is minimized instead. The change in free energy under these conditions is a measure of available work that might be done in the process. Thus available work for an ideal gas at constant temperature $T_{o}$ and pressure $P_{o}$ is $W=\Delta G=NkT_{o}\Theta (V/V_{o})$ where $V_{o}=NkT_{o}/P_{o}$ and $\Theta (x)=x-1-\ln x\geq 0$ (see also Gibbs inequality).

More generally the work available relative to some ambient is obtained by multiplying ambient temperature $T_{o}$ by relative entropy or *net surprisal* $\Delta I\geq 0,$ defined as the average value of $k\ln(p/p_{o})$ where $p_{o}$ is the probability of a given state under ambient conditions. For instance, the work available in equilibrating a monatomic ideal gas to ambient values of $V_{o}$ and $T_{o}$ is thus $W=T_{o}\Delta I$ , where relative entropy

$\Delta I=Nk\left[\Theta {\left({\frac {V}{V_{o}}}\right)}+{\frac {3}{2}}\Theta {\left({\frac {T}{T_{o}}}\right)}\right].$

The resulting contours of constant relative entropy, shown at right for a mole of Argon at standard temperature and pressure, for example put limits on the conversion of hot to cold as in flame-powered air-conditioning or in the unpowered device to convert boiling-water to ice-water discussed here. Thus relative entropy measures thermodynamic availability in bits.


## Quantum information theory

For density matrices P and Q on a Hilbert space, the quantum relative entropy from Q to P is defined to be

$D_{\text{KL}}(P\parallel Q)=\operatorname {Tr} (P(\log P-\log Q)).$

In quantum information science the minimum of $D_{\text{KL}}(P\parallel Q)$ over all separable states Q can also be used as a measure of entanglement in the state P.


## Relationship between models and reality

Just as relative entropy of "actual from ambient" measures thermodynamic availability, relative entropy of "reality from a model" is also useful even if the only clues we have about reality are some experimental measurements. In the former case relative entropy describes *distance to equilibrium* or (when multiplied by ambient temperature) the amount of *available work*, while in the latter case it tells you about surprises that reality has up its sleeve or, in other words, *how much the model has yet to learn*.

Although this tool for evaluating models against systems that are accessible experimentally may be applied in any field, its application to selecting a statistical model via Akaike information criterion are particularly well described in papers and a book by Burnham and Anderson. In a nutshell the relative entropy of reality from a model may be estimated, to within a constant additive term, by a function of the deviations observed between data and the model's predictions (like the mean squared deviation) . Estimates of such divergence for models that share the same additive term can in turn be used to select among models.

When trying to fit parametrized models to data there are various estimators which attempt to minimize relative entropy, such as maximum likelihood and maximum spacing estimators.


## Symmetrised divergence

Kullback & Leibler (1951) also considered the symmetrized function:

$D_{\text{KL}}(P\parallel Q)+D_{\text{KL}}(Q\parallel P)$

which they referred to as the "divergence", though today the "KL divergence" refers to the asymmetric function (see § Etymology for the evolution of the term). This function is symmetric and nonnegative, and had already been defined and used by Harold Jeffreys in 1948; it is accordingly called the **Jeffreys divergence**.

This quantity has sometimes been used for feature selection in classification problems, where P and Q are the conditional Probability density functions of a feature under two different classes. In the Banking and Finance industries, this quantity is referred to as **Population Stability Index** (**PSI**), and is used to assess distributional shifts in model features through time.

An alternative is given via the $\lambda$ -divergence,

$D_{\lambda }(P\parallel Q)=\lambda D_{\text{KL}}(P\parallel \lambda P+(1-\lambda )Q)+(1-\lambda )D_{\text{KL}}(Q\parallel \lambda P+(1-\lambda )Q){\text{,}}$

which can be interpreted as the expected information gain about X from discovering which probability distribution X is drawn from, P or Q, if they currently have probabilities $\lambda$ and $1-\lambda$ respectively.

The value $\lambda =0.5$ gives the Jensen–Shannon divergence, defined by

$D_{\text{JS}}={\tfrac {1}{2}}D_{\text{KL}}(P\parallel M)+{\tfrac {1}{2}}D_{\text{KL}}(Q\parallel M)$

where M is the average of the two distributions,

$M={\tfrac {1}{2}}\left(P+Q\right){\text{.}}$

We can also interpret $D_{\text{JS}}$ as the capacity of a noisy information channel with two inputs giving the output distributions P and Q. The Jensen–Shannon divergence, like all f-divergences, is *locally* proportional to the Fisher information metric. It is similar to the Hellinger metric (in the sense that it induces the same affine connection on a statistical manifold).

Furthermore, the Jensen–Shannon divergence can be generalized using abstract statistical M-mixtures relying on an abstract mean M.


## Relationship to other probability-distance measures

There are many other important measures of probability distance. Some of these are particularly connected with relative entropy. For example:

- The total-variation distance, $\delta (p,q)$ . This is connected to the divergence through Pinsker's inequality: $\delta (P,Q)\leq {\sqrt {{\tfrac {1}{2}}D_{\text{KL}}(P\parallel Q)}}.$ Pinsker's inequality is vacuous for any distributions where $D_{\mathrm {KL} }(P\parallel Q)>2$ , since the total variation distance is at most 1. For such distributions, an alternative bound can be used, due to Bretagnolle and Huber (see, also, Tsybakov): $\delta (P,Q)\leq {\sqrt {1-e^{-D_{\mathrm {KL} }(P\parallel Q)}}}.$
- The family of Rényi divergences generalize relative entropy. Depending on the value of a certain parameter, $\alpha$ , various inequalities may be deduced.

Other notable measures of distance include the Hellinger distance, *histogram intersection*, *Chi-squared statistic*, *quadratic form distance*, *match distance*, *Kolmogorov–Smirnov distance*, and *earth mover's distance*.


## Data differencing

Just as *absolute* entropy serves as theoretical background for data *compression*, *relative* entropy serves as theoretical background for data *differencing* – the absolute entropy of a set of data in this sense being the data required to reconstruct it (minimum compressed size), while the relative entropy of a target set of data, given a source set of data, is the data required to reconstruct the target *given* the source (minimum size of a patch).
