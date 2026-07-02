---
title: "Family-wise error rate"
source: https://en.wikipedia.org/wiki/Family-wise_error_rate
domain: bonferroni-correction
license: CC-BY-SA-4.0
tags: Bonferroni correction, Holm Bonferroni, Sidak correction, union bound
fetched: 2026-07-02
---

# Family-wise error rate

**Family-wise error rate** (**FWER**) is a term from statistics for the probability of making one or more false discoveries, or type I errors when performing multiple hypotheses tests. FWER is a metric that quantifies the risk caused by multiple testing. It's the probability of making one or more Type I errors across all tests in a family of comparisons. Controlling the FWER (for example, with Bonferroni or Holm corrections) is a way to address the problem created with multiple testing.

## Familywise and experimentwise error rates

John Tukey developed in 1953 the concept of a familywise error rate as the probability of making a Type I error among a specified group, or "family," of tests. Ryan (1959) proposed the related concept of an *experimentwise error rate*, which is the probability of making a Type I error in a given experiment. Hence, an experimentwise error rate is a familywise error rate where the family includes all the tests that are conducted within an experiment.

As Ryan (1959, Footnote 3) explained, an experiment may contain two or more families of multiple comparisons, each of which relates to a particular statistical inference and each of which has its own separate familywise error rate. Hence, familywise error rates are usually based on theoretically informative collections of multiple comparisons. In contrast, an experimentwise error rate may be based on a collection of simultaneous comparisons that refer to a diverse range of separate inferences. Some have argued that it may not be useful to control the experimentwise error rate in such cases. Indeed, Tukey suggested that familywise control was preferable in such cases (Tukey, 1956, personal communication, in Ryan, 1962, p. 302).

## Background

Within the statistical framework, there are several definitions for the term "family":

- Hochberg & Tamhane (1987) defined "family" as "any collection of inferences for which it is meaningful to take into account some combined measure of error".
- According to Cox (1982), a set of inferences should be regarded a family:

1. To take into account the selection effect due to data dredging
2. To ensure simultaneous correctness of a set of inferences as to guarantee a correct overall decision

To summarize, a family could best be defined by the potential selective inference that is being faced: A family is the smallest set of items of inference in an analysis, interchangeable about their meaning for the goal of research, from which selection of results for action, presentation or highlighting could be made (Yoav Benjamini).

### Classification of multiple hypothesis tests

The following table defines the possible outcomes when testing multiple null hypotheses. Suppose we have a number *m* of null hypotheses, denoted by: *H*1, *H*2, ..., *H**m*. Using a statistical test, we reject the null hypothesis if the test is declared significant. We do not reject the null hypothesis if the test is non-significant. Summing each type of outcome over all *Hi*  yields the following random variables:

|   | Null hypothesis is true (H0) | Alternative hypothesis is true (HA) | Total |
|---|---|---|---|
| Test is declared significant | V | S | R |
| Test is declared non-significant | U | T | $m-R$ |
| Total | $m_{0}$ | $m-m_{0}$ | m |

- m is the total number hypotheses tested
- $m_{0}$ is the number of true null hypotheses, an unknown parameter
- $m-m_{0}$ is the number of true alternative hypotheses
- V is the number of false positives (Type I error) (also called "false discoveries")
- S is the number of true positives (also called "true discoveries")
- T is the number of false negatives (Type II error)
- U is the number of true negatives
- $R=V+S$ is the number of rejected null hypotheses (also called "discoveries", either true or false)

In m hypothesis tests of which $m_{0}$ are true null hypotheses, R is an observable random variable, and S, T, U, and V are unobservable random variables.

## Definition

The FWER is the probability of making at least one type I error in the family,

$\mathrm {FWER} =\Pr(V\geq 1),\,$

or equivalently,

$\mathrm {FWER} =1-\Pr(V=0).$

Thus, by assuring $\mathrm {FWER} \leq \alpha \,\!\,$ , the probability of making one or more type I errors in the family is controlled at level $\alpha \,\!$ .

A procedure controls the FWER *in the weak sense* if the FWER control at level $\alpha \,\!$ is guaranteed *only* when all null hypotheses are true (i.e. when $m_{0}=m$ , meaning the "global null hypothesis" is true).

A procedure controls the FWER *in the strong sense* if the FWER control at level $\alpha \,\!$ is guaranteed for *any* configuration of true and non-true null hypotheses (whether the global null hypothesis is true or not).

## Controlling procedures

Some classical solutions that ensure strong level $\alpha$ FWER control, and some newer solutions exist.

### The Bonferroni procedure

- Denote by $p_{i}$ the *p*-value for testing $H_{i}$
- reject $H_{i}$ if $p_{i}\leq {\frac {\alpha }{m}}$

### The Šidák procedure

- Testing each hypothesis at level $\alpha _{SID}=1-(1-\alpha )^{\frac {1}{m}}$ is Sidak's multiple testing procedure.
- This procedure is more powerful than Bonferroni but the gain is small.
- This procedure can fail to control the FWER when the tests are negatively dependent.

### Tukey's procedure

- Tukey's procedure is only applicable for pairwise comparisons.
- It assumes independence of the observations being tested, as well as equal variation across observations (homoscedasticity).
- The procedure calculates for each pair the studentized range statistic: ${\frac {Y_{A}-Y_{B}}{SE}}$ where $Y_{A}$ is the larger of the two means being compared, $Y_{B}$ is the smaller, and $SE$ is the standard error of the data in question.
- Tukey's test is essentially a Student's t-test, except that it corrects for **family-wise error-rate**.

### Holm's step-down procedure (1979)

- Start by ordering the *p*-values (from lowest to highest) $P_{(1)}\ldots P_{(m)}$ and let the associated hypotheses be $H_{(1)}\ldots H_{(m)}$
- Let k be the minimal index such that $P_{(k)}>{\frac {\alpha }{m+1-k}}$
- Reject the null hypotheses $H_{(1)}\ldots H_{(k-1)}$ . If $k=1$ then none of the hypotheses are rejected.

This procedure is uniformly more powerful than the Bonferroni procedure. The reason why this procedure controls the family-wise error rate for all the m hypotheses at level α in the strong sense is, because it is a closed testing procedure. As such, each intersection is tested using the simple Bonferroni test.

### Hochberg's step-up procedure

Yosef Hochberg's step-up procedure (1988) is performed using the following steps:

- Start by ordering the *p*-values (from lowest to highest) $P_{(1)}\ldots P_{(m)}$ and let the associated hypotheses be $H_{(1)}\ldots H_{(m)}$
- For a given $\alpha$ , let R be the largest k such that $P_{(k)}\leq {\frac {\alpha }{m+1-k}}$
- Reject the null hypotheses $H_{(1)}\ldots H_{(R)}$

Hochberg's procedure is more powerful than Holm's. Nevertheless, while Holm’s is a closed testing procedure (and thus, like Bonferroni, has no restriction on the joint distribution of the test statistics), Hochberg’s is based on the Simes test, so it holds only under non-negative dependence. The Simes test is derived under assumption of independent tests; it is conservative for tests that are positively dependent in a certain sense and is anti-conservative for certain cases of negative dependence. However, it has been suggested that a modified version of the Hochberg procedure remains valid under general negative dependence.

### Dunnett's correction

Charles Dunnett (1955, 1966) described an alternative alpha error adjustment when *k* groups are compared to the same control group. Now known as Dunnett's test, this method is less conservative than the Bonferroni adjustment.

### Scheffé's method

### Resampling procedures

The procedures of Bonferroni and Holm control the FWER under any dependence structure of the *p*-values (or equivalently the individual test statistics). Essentially, this is achieved by accommodating a `worst-case' dependence structure (which is close to independence for most practical purposes). But such an approach is conservative if dependence is actually positive. To give an extreme example, under perfect positive dependence, there is effectively only one test and thus, the FWER is uninflated.

Accounting for the dependence structure of the *p*-values (or of the individual test statistics) produces more powerful procedures. This can be achieved by applying resampling methods, such as bootstrapping and permutations methods. The procedure of Westfall and Young (1993) requires a certain condition that does not always hold in practice (namely, subset pivotality). The procedures of Romano and Wolf (2005a,b) dispense with this condition and are thus more generally valid.

### Harmonic mean *p*-value procedure

The harmonic mean *p*-value (HMP) procedure provides a multilevel test that improves on the power of Bonferroni correction by assessing the significance of *groups* of hypotheses while controlling the strong-sense family-wise error rate. The significance of any subset ${\textstyle {\mathcal {R}}}$ of the ${\textstyle m}$ tests is assessed by calculating the HMP for the subset, ${\overset {\circ }{p}}_{\mathcal {R}}={\frac {\sum _{i\in {\mathcal {R}}}w_{i}}{\sum _{i\in {\mathcal {R}}}w_{i}/p_{i}}},$ where ${\textstyle w_{1},\dots ,w_{m}}$ are weights that sum to one (i.e. ${\textstyle \sum _{i=1}^{m}w_{i}=1}$ ). An approximate procedure that controls the strong-sense family-wise error rate at level approximately ${\textstyle \alpha }$ rejects the null hypothesis that none of the *p*-values in subset ${\textstyle {\mathcal {R}}}$ are significant when ${\textstyle {\overset {\circ }{p}}_{\mathcal {R}}\leq \alpha \,w_{\mathcal {R}}}$ (where ${\textstyle w_{\mathcal {R}}=\sum _{i\in {\mathcal {R}}}w_{i}}$ ). This approximation is reasonable for small ${\textstyle \alpha }$ (e.g. ${\textstyle \alpha <0.05}$ ) and becomes arbitrarily good as ${\textstyle \alpha }$ approaches zero. An asymptotically exact test is also available (see main article).

## Alternative approaches

FWER control exerts a more stringent control over false discovery compared to false discovery rate (FDR) procedures. FWER control limits the probability of *at least one* false discovery, whereas FDR control limits (in a loose sense) the expected proportion of false discoveries. Thus, FDR procedures have greater power at the cost of increased rates of type I errors, i.e., rejecting null hypotheses that are actually true.

On the other hand, FWER control is less stringent than per-family error rate control, which limits the expected number of errors per family. Because FWER control is concerned with *at least one* false discovery, unlike per-family error rate control it does not treat multiple simultaneous false discoveries as any worse than one false discovery. The Bonferroni correction is often considered as merely controlling the FWER, but in fact also controls the per-family error rate.
