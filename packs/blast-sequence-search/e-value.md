---
title: "E-values"
source: https://en.wikipedia.org/wiki/E-value
domain: blast-sequence-search
license: CC-BY-SA-4.0
tags: blast sequence search, substitution matrix, sequence database, expectation value blast
fetched: 2026-07-02
---

# E-values

(Redirected from

E-value

)

In statistical hypothesis testing, **e-values** quantify the evidence in the data against a null hypothesis (e.g., "the coin is fair", or, in a medical context, "this new treatment has no effect"). They serve as a more robust alternative to p-values, addressing some shortcomings of the latter.

In contrast to p-values, e-values can deal with optional continuation: e-values of subsequent experiments (e.g. clinical trials concerning the same treatment) may simply be multiplied to provide a new, "product" e-value that represents the evidence in the joint experiment. This works even if, as often happens in practice, the decision to perform later experiments may depend in vague, unknown ways on the data observed in earlier experiments, and it is not known beforehand how many trials will be conducted: the product e-value remains a meaningful quantity, leading to tests with Type-I error control. For this reason, e-values and their sequential extension, the *e-process*, are the fundamental building blocks for anytime-valid statistical methods (e.g. confidence sequences). Another advantage over p-values is that any weighted average of e-values remains an e-value, even if the individual e-values are arbitrarily dependent. This is one of the reasons why e-values have also turned out to be useful tools in multiple testing.

E-values can be interpreted in a number of different ways: first, an e-value can be interpreted as rescaling of a test that is presented on a more appropriate scale that facilitates merging them. Second, the reciprocal of an e-value is a p-value, but not just any p-value: a special p-value for which a rejection `at level p' retains a generalized Type-I error guarantee. Third, they are broad generalizations of likelihood ratios and are also related to, yet distinct from, Bayes factors. Fourth, they have an interpretation as bets. Fifth, in a sequential context, they can also be interpreted as increments of nonnegative supermartingales. Interest in e-values has exploded since 2019, when the term 'e-value' was coined and a number of breakthrough results were achieved by several research groups. The first overview article appeared in 2023.

## Definition and mathematical background

Let the null hypothesis $H_{0}$ be given as a set of distributions for data Y . Usually $Y=(X_{1},\ldots ,X_{\tau })$ with each $X_{i}$ a single outcome and $\tau$ a fixed sample size or some stopping time. We shall refer to such Y , which represent the full sequence of outcomes of a statistical experiment, as a *sample* or *batch of outcomes.* But in some cases Y may also be an unordered bag of outcomes or a single outcome.

An **e-variable** or **e-statistic** is a *nonnegative* random variable $E=E(Y)$ such that under all $P\in H_{0}$ , its expected value is bounded by 1:

${\mathbb {E} }_{P}[E]\leq 1$ .

The value taken by e-variable E is called the **e-value***.* In practice, the term *e-value* (a number) is often used when one is really referring to the underlying e-variable (a random variable, that is, a measurable function of the data).

## Interpretations

### As the continuous interpretation of a test

A test for a null hypothesis $H_{0}$ is traditionally modeled as a function $\phi$ from the data to $\{{\text{not reject }}H_{0},{\text{ reject }}H_{0}\}$ . A test $\phi _{\alpha }$ is said to be valid for level $\alpha$ if

$P(\phi _{\alpha }={\text{reject }}H_{0})\leq \alpha ,{\text{ for every }}P\in H_{0}.$

This is classically conveniently summarized as a function $\phi _{\alpha }$ from the data to $\{0,1\}$ that satisfies

$\mathbb {E} ^{P}[\phi _{\alpha }]\leq \alpha ,{\text{ for every }}P\in H_{0}$ .

Moreover, this is sometimes generalized to permit external randomization by letting the test $\phi _{\alpha }$ take value in $[0,1]$ . Here, its value is interpreted as a probability with which one should subsequently reject the hypothesis.

An issue with modelling a test in this manner, is that the traditional decision space $\{{\text{not reject }}H_{0},{\text{ reject }}H_{0}\}$ or $\{0,1\}$ does not encode the level $\alpha$ at which the test $\phi _{\alpha }$ rejects. This is odd at best, because a rejection at level 1% is a much stronger claim than a rejection at level 10%. A more suitable decision space seems to be $\{{\text{not reject }}H_{0},{\text{ reject }}H_{0}{\text{ at level }}\alpha \}$ .

The e-value can be interpreted as resolving this problem. Indeed, we can rescale from $\{0,1\}$ to $\{0,1/\alpha \}$ and $[0,1]$ to $[0,1/\alpha ]$ by rescaling the test by its level:

$\varepsilon _{\alpha }=\phi _{\alpha }/\alpha$ ,

where we denote a test on this **evidence** scale by $\varepsilon _{\alpha }$ to avoid confusion. Such a test is then valid if

$\mathbb {E} ^{P}[\varepsilon _{\alpha }]\leq 1,{\text{ for every }}P\in H_{0}$ .

That is: it is valid if it is an e-value.

In fact, this reveals that e-values bounded to $[0,1/\alpha ]$ **are** rescaled randomized tests, that are continuously interpreted as evidence against the hypothesis. The standard e-value that takes value in $[0,\infty ]$ appears as a generalization of a level 0 test.

This interpretation shows that e-values are indeed fundamental to testing: they are equivalent to tests, thinly veiled by a rescaling. From this perspective, it may be surprising that typical e-values look very different from traditional tests: maximizing the objective

$\mathbb {E} ^{Q}[\varepsilon _{\alpha }]$

for an alternative hypothesis $H_{1}=\{Q\}$ would yield traditional Neyman-Pearson style tests. Indeed, this maximizes the probability under Q that $\varepsilon _{\alpha }=1/\alpha$ .

But if we continuously interpret the value of the test $\varepsilon _{\alpha }$ as evidence against the hypothesis, then we may also be interested in maximizing different targets such as

$\mathbb {E} ^{Q}[\log \varepsilon _{\alpha }]$ .

This yields tests that are remarkably different from traditional Neyman-Pearson tests, and more suitable when merged through multiplication as they are positive with probability 1 under Q . From this angle, the main innovation of the e-value compared to traditional testing is to maximize a different power target.

### As p-values with a stronger data-dependent-level Type-I error guarantee

For any e-variable E and any $0<\alpha \leq 1$ and all $P\in H_{0}$ , it holds that

$P\left(E\geq {\frac {1}{\alpha }}\right)=P(1/E\leq \alpha )\ {\overset {(*)}{\leq }}\ \alpha$ .

This means $p^{\prime }=1/E$ is a valid p-value. Moreover, the *e-value based test with significance level $\alpha$ ,* which rejects $P_{0}$ if $p^{\prime }\leq \alpha$ , has a Type-I error bounded by $\alpha$ . But, whereas with standard p-values the inequality (*) above is usually an equality (with continuous-valued data) or near-equality (with discrete data), this is not the case with e-variables. This makes e-value-based tests more conservative (less power) than those based on standard p-values.

In exchange for this conservativeness, the p-value $p^{\prime }=1/E$ comes with a stronger guarantee. In particular, for every possibly data-dependent significance level ${\widetilde {\alpha }}>0$ , we have

$\mathbb {E} \left[{\frac {P(p^{\prime }\leq {\widetilde {\alpha }}\mid {\widetilde {\alpha }})}{\widetilde {\alpha }}}\right]\leq 1,$

if and only if $\mathbb {E} [1/p^{\prime }]\leq 1$ . This means that a p-value satisfies this guarantee if and only if it is the reciprocal $1/E$ of an e-variable E .

The interpretation of this guarantee is that, on average, the relative Type-I error distortion $P(p^{\prime }\leq {\widetilde {\alpha }}\mid {\widetilde {\alpha }})/{\widetilde {\alpha }}$ caused by using a data-dependent level ${\widetilde {\alpha }}$ is controlled for every choice of the data-dependent significance level. Traditional p-values only satisfy this guarantee for data-independent or pre-specified levels.

This stronger guarantee is also called the **post-hoc $\alpha$ Type-I error**, as it allows one to choose the significance level after observing the data: post-hoc. A p-value that satisfies this guarantee is also called a **post-hoc p-value**. As $p^{\prime }$ is a post-hoc p-value if and only if $p^{\prime }=1/E$ for some e-value E , it is possible to view this as an alternative definition of an e-value.

Under this post-hoc Type-I error, the problem of choosing the significance level $\alpha$ vanishes: we can simply choose the smallest data-dependent level at which we reject the hypothesis by setting it equal to the post-hoc p-value: ${\widetilde {\alpha }}=p^{\prime }$ . Indeed, at this data-dependent level we have

$\mathbb {E} \left[{\frac {P(p^{\prime }\leq p^{\prime }\mid p^{\prime })}{p^{\prime }}}\right]=\mathbb {E} \left[{\frac {1}{p^{\prime }}}\right]\leq 1,$

since $1/p^{\prime }$ is an e-variable. As a consequence, we can truly reject at level $p^{\prime }$ and still retain the post-hoc Type-I error guarantee. For a traditional p-value p , rejecting at level p comes with no such guarantee.

Moreover, a post-hoc p-value inherits optional continuation and merging properties of e-values. But instead of an arithmetic weighted average, a weighted harmonic average of post-hoc p-values is still a post-hoc p-value.

### As generalizations of likelihood ratios

Let $H_{0}=\{P_{0}\}$ be a simple null hypothesis. Let Q be any other distribution on Y , and let

$E:={\frac {q(Y)}{p_{0}(Y)}}$

be their likelihood ratio. Then E is an e-variable. Conversely, any e-variable relative to a simple null $H_{0}=\{P_{0}\}$ can be written as a likelihood ratio with respect to *some* distribution Q . Thus, when the null is simple, e-variables coincide with likelihood ratios. E-variables exist for general composite nulls as well though, and they may then be thought of as generalizations of likelihood ratios. The two main ways of constructing e-variables, UI and RIPr (see below) both lead to expressions that are variations of likelihood ratios as well.

Two other standard generalizations of the likelihood ratio are (a) the generalized likelihood ratio as used in the standard, classical likelihood ratio test and (b) the Bayes factor. Importantly, neither (a) nor (b) are e-variables in general: generalized likelihood ratios in sense (a) are not e-variables unless the alternative is simple (see below under "universal inference"). Bayes factors *are* e-variables if the null is simple. To see this, note that, if ${\mathcal {Q}}=\{Q_{\theta }:\theta \in \Theta \}$ represents a statistical model, and w a prior density on $\Theta$ , then we can set Q as above to be the Bayes marginal distribution with density

$q(Y)=\int q_{\theta }(Y)w(\theta )d\theta$

and then $E=q(Y)/p_{0}(Y)$ is also a Bayes factor of $H_{0}$ vs. $H_{1}:={\mathcal {Q}}$ . If the null is composite, then some special e-variables can be written as Bayes factors with some very special priors, but most Bayes factors one encounters in practice are not e-variables and many e-variables one encounters in practice are not Bayes factors.

### As bets

Suppose you can buy a ticket for 1 monetary unit, with nonnegative pay-off $E=E(Y)$ . The statements " E is an e-variable" and "if the null hypothesis is true, you do not expect to gain any money if you engage in this bet" are logically equivalent. This is because E being an e-variable means that the expected gain of buying the ticket is the pay-off minus the cost, i.e. $E-1$ , which has expectation $\leq 0$ . Based on this interpretation, the product e-value for a sequence of tests can be interpreted as the amount of money you have gained by sequentially betting with pay-offs given by the individual e-variables and always re-investing all your gains.

The betting interpretation becomes particularly visible if we rewrite an e-variable as $E:=1+\lambda U$ where U has expectation $\leq 0$ under all $P\in H_{0}$ and $\lambda \in {\mathbb {R} }$ is chosen so that $E\geq 0$ a.s. Any e-variable can be written in the $1+\lambda U$ form although with parametric nulls, writing it as a likelihood ratio is usually mathematically more convenient. The $1+\lambda U$ form on the other hand is often more convenient in nonparametric settings. As a prototypical example, consider the case that $Y=(X_{1},\ldots ,X_{n})$ with the $X_{i}$ taking values in the bounded interval $[0,1]$ . According to $H_{0}$ , the $X_{i}$ are i.i.d. according to a distribution P with mean $\mu$ ; no other assumptions about P are made. Then we may first construct a family of e-variables for single outcomes, $E_{i,\lambda }:=1+\lambda (X_{i}-\mu )$ , for any $\lambda \in [-1/(1-\mu ),1/\mu ]$ (these are the $\lambda$ for which $E_{i,\lambda }$ is guaranteed to be nonnegative). We may then define a new e-variable for the complete data vector Y by taking the product

$E:=\prod _{i=1}^{n}E_{i,{\breve {\lambda }}|X^{i-1}}$ ,

where ${\breve {\lambda }}|X^{i-1}$ is an estimate for ${\lambda }$ , based only on past data $X^{i-1}=(X_{1},\ldots ,X_{i-1})$ , and designed to make $E_{i,\lambda }$ as large as possible in the "e-power" or "GRO" sense (see below). Waudby-Smith and Ramdas use this approach to construct "nonparametric" confidence intervals for the mean that tend to be significantly narrower than those based on more classical methods such as Chernoff, Hoeffding and Bernstein bounds.

## A fundamental property: optional continuation

E-values are more suitable than p-value when one expects follow-up tests involving the same null hypothesis with different data or experimental set-ups. This includes, for example, combining individual results in a meta-analysis. The advantage of e-values in this setting is that they allow for *optional continuation.* Indeed, they have been employed in what may be the world's first fully 'online' meta-analysis with explicit Type-I error control.

Informally, optional continuation implies that the product of any number of e-values, $E_{(1)},E_{(2)},\ldots$ , defined on independent samples $Y_{(1)},Y_{(2)},\ldots$ , is itself an e-value, even if the *definition* of each e-value is allowed to depend on all previous outcomes, and no matter what rule is used to decide when to stop gathering new samples (e.g. to perform new trials). It follows that, for any significance level $0<\alpha <1$ , if the null is true, then the probability that a product of e-values will *ever* become larger than $1/\alpha$ is bounded by $\alpha$ . Thus if we decide to combine the samples observed so far and reject the null if the product e-value is larger than $1/\alpha$ , then our Type-I error probability remains bounded by $\alpha$ . We say that testing based on e-values *remains safe (Type-I valid) under optional continuation*.

Mathematically, this is shown by first showing that the product e-variables form a nonnegative discrete-time martingale in the filtration generated by $Y_{(1)},Y_{(2)},\ldots$ (the individual e-variables are then increments of this martingale). The results then follow as a consequence of Doob's optional stopping theorem and Ville's inequality.

We already implicitly used product e-variables in the example above, where we defined e-variables on individual outcomes $X_{i}$ and designed a new e-value by taking products. Thus, in the example, the individual outcomes $X_{i}$ play the role of 'batches' (full samples) $Y_{(j)}$ above, and we can therefore even engage in *optional stopping* "within" the original batch Y : we may stop the data analysis at any individual *outcome* (not just "batch of outcomes") we like, for whatever reason, and reject if the product so far exceeds $1/\alpha$ . Not all e-variables defined for batches of outcomes Y can be decomposed as a product of per-outcome e-values in this way though. If this is not possible, we cannot use them for optional stopping (within a sample Y ) but only for optional continuation (from one sample $Y_{(j)}$ to the next $Y_{(j+1)}$ and so on).

## Construction and optimality

If we set $E:=1$ independently of the data we get a *trivial* e-value: it is an e-variable by definition, but it will never allow us to reject the null hypothesis. This example shows that some e-variables may be better than others, in a sense to be defined below. Intuitively, a good e-variable is one that tends to be large (much larger than 1) if the alternative is true. This is analogous to the situation with p-values: both e-values and p-values can be defined without referring to an alternative, but *if* an alternative is available, we would like them to be small (p-values) or large (e-values) with high probability. In standard hypothesis tests, the quality of a valid test is formalized by the notion of *statistical power* but this notion has to be suitably modified in the context of e-values.

The standard notion of quality of an e-variable relative to a given alternative $H_{1}$ , used by most authors in the field, is a generalization of the Kelly criterion in economics and (since it does exhibit close relations to classical power) is sometimes called *e-power*; the optimal e-variable in this sense is known as *log-optimal* or *growth-rate optimal* (often abbreviated to GRO). In the case of a simple alternative $H_{1}=\{Q\}$ , the e-power of a given e-variable S is simply defined as the expectation ${\mathbb {E} }_{Q}[\log E]$ ; in case of composite alternatives, there are various versions (e.g. worst-case absolute, worst-case relative) of e-power and GRO.

### Simple alternative, simple null: likelihood ratio

Let $H_{0}=\{P_{0}\}$ and $H_{1}=\{Q\}$ both be simple. Then the likelihood ratio e-variable $E=q(Y)/p_{0}(Y)$ has maximal e-power in the sense above, i.e. it is GRO.

### Simple alternative, composite null: reverse information projection (RIPr)

Let $H_{1}=\{Q\}$ be simple and $H_{0}=\{P_{\theta }:\theta \in \Theta _{0}\}$ be composite, such that all elements of $H_{0}\cup H_{1}$ have densities (denoted by lower-case letters) relative to the same underlying measure. Grünwald et al. show that under weak regularity conditions, the GRO e-variable exists, is essentially unique, and is given by

$E:={\frac {q(Y)}{p_{\curvearrowleft Q}(Y)}}$

where $p_{\curvearrowleft Q}$ is the **Reverse Information Projection (RIPr)** of Q unto the convex hull of $H_{0}$ . Under further regularity conditions (and in all practically relevant cases encountered so far), $p_{\curvearrowleft Q}$ is given by a Bayes marginal density: there exists a specific, unique distribution W on $\Theta _{0}$ such that $p_{\curvearrowleft Q}(Y)=\int _{\Theta _{0}}p_{\theta }(Y)dW(\theta )$ .

### Simple alternative, composite null: universal inference (UI)

In the same setting as above, show that, under no regularity conditions at all,

$E={\frac {q(Y)}{\sup _{P\in H_{0}}p(Y)}}\left(={\frac {q(Y)}{{p}_{{\hat {\theta }}\mid Y}(Y)}}\right)$

is an e-variable (with the second equality holding if the MLE (maximum likelihood estimator) ${\hat {\theta }}\mid Y$ based on data Y is always well-defined). This way of constructing e-variables has been called the **universal inference (UI)** method, "universal" referring to the fact that no regularity conditions are required.

### Composite alternative, simple null

Now let $H_{0}=\{P\}$ be simple and $H_{1}=\{Q_{\theta }:\theta \in \Theta _{1}\}$ be composite, such that all elements of $H_{0}\cup H_{1}$ have densities relative to the same underlying measure. There are now two generic, closely related ways of obtaining e-variables that are close to growth-optimal (appropriately redefined for composite $H_{1}$ ): Robbins' **method of mixtures** and the **plug-in method**, originally due to Wald but, in essence, re-discovered by Philip Dawid as "prequential plug-in" and Jorma Rissanen as "predictive MDL". The method of mixtures essentially amounts to "being Bayesian about the numerator" (the reason it is not called "Bayesian method" is that, when both null and alternative are composite, the numerator may often not be a Bayes marginal): we posit any prior distribution W on $\Theta _{1}$ and set

${\bar {q}}_{W}(Y):=\int _{\Theta _{1}}q_{\theta }(Y)dW(\theta )$

and use the e-variable ${\bar {q}}_{W}(Y)/p(Y)$ .

To explicate the plug-in method, suppose that $Y=(X_{1},\ldots ,X_{n})$ where $X_{1},X_{2},\ldots$ constitute a stochastic process and let ${\breve {\theta }}\mid X^{i}$ be an estimator of $\theta \in \Theta _{1}$ based on data $X^{i}=(X_{1},\ldots ,X_{i})$ for $i\geq 0$ . In practice one usually takes a "smoothed" maximum likelihood estimator (such as, for example, the regression coefficients in ridge regression), initially set to some "default value" ${\breve {\theta }}\mid X^{0}:=\theta _{0}$ . One now recursively constructs a density ${\bar {q}}_{\breve {\theta }}$ for $X^{n}$ by setting ${\bar {q}}_{\breve {\theta }}(X^{n})=\prod _{i=1}^{n}q_{{\breve {\theta }}\mid X^{i-1}}(X_{i}\mid X^{i-1})$ .

Effectively, both the method of mixtures and the plug-in method can be thought of *learning* a specific instantiation of the alternative that explains the data well.

### Composite null and alternative

In **parametric** settings, we can simply combine the main methods for the composite alternative (obtaining ${\bar {q}}_{\breve {\theta }}$ or ${\bar {q}}_{W}$ ) with the main methods for the composite null (UI or RIPr, using the single distribution ${\bar {q}}_{\breve {\theta }}$ or ${\bar {q}}_{W}$ as an alternative). Note in particular that when using the plug-in method together with the UI method, the resulting e-variable will look like

${\frac {\prod _{i=1}^{n}q_{{\breve {\theta }}\mid X^{i-1}}(X_{i})}{q_{{\hat {\theta }}\mid X^{n}}(X^{n})}}$

which resembles, but is still fundamentally different from, the generalized likelihood ratio as used in the classical likelihood ratio test.

The advantage of the UI method compared to RIPr is that (a) it can be applied whenever the MLE can be efficiently computed - in many such cases, it is not known whether/how the reverse information projection can be calculated; and (b) that it 'automatically' gives not just an e-variable but a full e-process (see below): if we replace n in the formula above by a general stopping time $\tau$ , the resulting ratio is still an e-variable; for the reverse information projection this automatic e-process generation only holds in special cases.

Its main disadvantage compared to RIPr is that it can be substantially sub-optimal in terms of the e-power/GRO criterion, which means that it leads to tests which also have less classical statistical power than RIPr-based methods. Thus, for settings in which the RIPr-method is computationally feasible and leads to e-processes, it is to be preferred. These include the z-test, t-test and corresponding linear regressions, k-sample tests with Bernoulli, Gaussian and Poisson distributions and the logrank test (an R package is available for a subset of these), as well as conditional independence testing under a *model-X assumption*. However, in many other statistical testing problems, it is currently (2023) unknown whether fast implementations of the reverse information projection exist, and they may very well not exist (e.g. generalized linear models without the model-X assumption).

In **nonparametric** settings (such as testing a mean as in the example above, or nonparametric 2-sample testing), it is often more natural to consider e-variables of the $1+\lambda U$ type. However, while these superficially look very different from likelihood ratios, they can often still be interpreted as such and sometimes can even be re-interpreted as implementing a version of the RIPr-construction.

Finally, in practice, one sometimes resorts to mathematically or computationally convenient combinations of RIPr, UI and other methods. For example, RIPr is applied to get optimal e-variables for small blocks of outcomes and these are then multiplied to obtain e-variables for larger samples - these e-variables work well in practice but cannot be considered optimal anymore.

### A third construction method: p-to-e (and e-to-p) calibration

There exist functions that convert p-values into e-values. Such functions are called *p-to-e calibrators*. Formally, a calibrator is a nonnegative decreasing function $f:[0,1]\rightarrow [0,\infty ]$ which, when applied to a p-variable (a random variable whose value is a p-value), yields an e-variable. A calibrator f is said to dominate another calibrator g if $f\geq g$ , and this domination is strict if the inequality is strict. An admissible calibrator is one that is not strictly dominated by any other calibrator. One can show that for a function to be a calibrator, it must have an integral of at most 1 over the uniform probability measure.

One family of admissible calibrators is given by the set of functions $\{f_{\kappa }:0<\kappa <1\}$ with $f_{\kappa }(p):=\kappa p^{\kappa -1}$ . Another calibrator is given by integrating out $\kappa$ :

$\int _{0}^{1}\kappa p^{\kappa -1}d\kappa ={\frac {1-p+p\log p}{p(-\log p)^{2}}}$

Conversely, an e-to-p calibrator transforms e-values back into p-variables. Interestingly, the following calibrator dominates all other e-to-p calibrators:

$f(t):=\min(1,1/t)$

.

While of theoretical importance, calibration is not much used in the practical design of e-variables since the resulting e-variables are often far from growth-optimal for any given $H_{1}$ .

## E-processes

### Definition

Now consider data $X_{1},X_{2},\ldots$ arriving sequentially, constituting a discrete-time stochastic process. Let $E_{1},E_{2},\ldots$ be another discrete-time process where for each $n,E_{n}$ can be written as a (measurable) function of the first $(X_{1},\ldots ,X_{n})$ outcomes. We call $E_{1},E_{2},\ldots$ an **e-process** if for any stopping time $\tau ,E_{\tau }$ is an e-variable, i.e. for all $P\in H_{0}:{\mathbb {E} }_{P}[E_{\tau }]\leq 1$ .

In basic cases, the stopping time can be defined by any rule that determines, at each sample size n , based only on the data observed so far, whether to stop collecting data or not. For example, this could be "stop when you have seen four consecutive outcomes larger than 1", "stop at $n=100$ ", or the **level- $\alpha$ -aggressive rule**, "stop as soon as you can reject at level $\alpha$ -level, i.e. at the smallest n such that $E_{n}\geq 1/\alpha$ ", and so on. With e-processes, we obtain an e-variable with any such rule. Crucially, the data analyst may not know the rule used for stopping. For example, her boss may tell her to stop data collecting and she may not know exactly why - nevertheless, she gets a valid e-variable and Type-I error control. This is in sharp contrast to data analysis based on p-values (which becomes invalid if stopping rules are not determined in advance) or in classical Wald-style sequential analysis (which works with data of varying length but again, with stopping times that need to be determined in advance). In more complex cases, the stopping time has to be defined relative to some slightly reduced filtration, but this is not a big restriction in practice. In particular, the level- $\alpha$ -aggressive rule is always allowed. Because of this validity under optional stopping, e-processes are the fundamental building block of confidence sequences, also known as anytime-valid confidence intervals.

Technically, e-processes are generalizations of test supermartingales, which are nonnegative supermartingales with starting value 1: any test supermartingale constitutes an e-process but not vice versa.

### Construction

E-processes can be constructed in a number of ways. Often, one starts with an e-value $E_{i}$ for $X_{i}$ whose definition is allowed to depend on previous data, i.e.,

for all $P\in H_{0}:{\mathbb {E} }_{P}[E_{i}|X_{1},\ldots ,X_{i-1}]\leq 1$

(again, in complex testing problems this definition needs to be modified a bit using reduced filtrations). Then the product process $M_{1},M_{2},\ldots$ with $M_{n}=E_{1}\times E_{2}\cdots \times E_{n}$ is a test supermartingale, and hence also an e-process (note that we already used this construction in the example described under "e-values as bets" above: for fixed $\lambda$ , the e-values $E_{i,\lambda }$ were not dependent on past-data, but by using $\lambda ={\breve {\lambda }}|X^{i-1}$ depending on the past, they became dependent on past data).

Another way to construct an e-process is to use the universal inference construction described above for sample sizes $1,2,\ldots$ The resulting sequence of e-values $E_{1},E_{2},\ldots$ will then always be an e-process.

## History

Historically, e-values implicitly appear as building blocks of nonnegative supermartingales in the pioneering work on anytime-valid confidence methods by well-known mathematician Herbert Robbins and some of his students. The first time e-values (or something very much like them) are treated as a quantity of independent interest is by another well-known mathematician, Leonid Levin, in 1976, within the theory of algorithmic randomness. With the exception of contributions by pioneer V. Vovk in various papers with various collaborators (e.g.), and an independent re-invention of the concept in an entirely different field, the concept did not catch on at all until 2019, when, within just a few months, several pioneering papers by several research groups appeared on arXiv (the corresponding journal publications referenced below sometimes coming years later). In these, the concept was finally given a proper name ("S-Value" and "E-Value"; in later versions of their paper, also adapted "E-Value"); describing their general properties, two generic ways to construct them, and their intimate relation to betting). Since then, interest by researchers around the world has been surging. In 2023 the first overview paper on "safe, anytime-valid methods", in which e-values play a central role, appeared.
