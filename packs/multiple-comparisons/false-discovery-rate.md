---
title: "False discovery rate"
source: https://en.wikipedia.org/wiki/False_discovery_rate
domain: multiple-comparisons
license: CC-BY-SA-4.0
tags: multiple comparisons, family-wise error rate, false discovery rate, closed testing
fetched: 2026-07-02
---

# False discovery rate

In statistics, the **false discovery rate** (**FDR**) is a method of conceptualizing the rate of type I errors in null hypothesis testing when conducting multiple comparisons. FDR-controlling procedures are designed to control the FDR, which is the expected proportion of "discoveries" (rejected null hypotheses) that are false (incorrect rejections of the null). Equivalently, the FDR is the expected ratio of the number of false positive classifications (false discoveries) to the total number of positive classifications (rejections of the null). The total number of rejections of the null include both the number of false positives (FP) and true positives (TP). Simply put, FDR = FP / (FP + TP). FDR-controlling procedures provide less stringent control of Type I errors compared to family-wise error rate (FWER) controlling procedures (such as the Bonferroni correction), which control the probability of *at least one* Type I error. Thus, FDR-controlling procedures have greater power, at the cost of increased numbers of Type I errors.

## History

### Technological motivations

The modern widespread use of the FDR is believed to stem from, and be motivated by, the development in technologies that allowed the collection and analysis of a large number of distinct variables in several individuals (e.g., the expression level of each of 10,000 different genes in 100 different persons). By the late 1980s and 1990s, the development of "high-throughput" sciences, such as genomics, allowed for rapid data acquisition. This, coupled with the growth in computing power, made it possible to seamlessly perform a very high number of statistical tests on a given data set. The technology of microarrays was a prototypical example, as it enabled thousands of genes to be tested simultaneously for differential expression between two biological conditions.

As high-throughput technologies became common, technological and/or financial constraints led researchers to collect datasets with relatively small sample sizes (e.g. few individuals being tested) and large numbers of variables being measured per sample (e.g. thousands of gene expression levels). In these datasets, too few of the measured variables showed statistical significance after classic correction for multiple tests with standard multiple comparison procedures. This created a need within many scientific communities to abandon FWER and unadjusted multiple hypothesis testing for other ways to highlight and rank in publications those variables showing marked effects across individuals or treatments that would otherwise be dismissed as non-significant after standard correction for multiple tests. In response to this, a variety of error rates have been proposed—and become commonly used in publications—that are less conservative than FWER in flagging possibly noteworthy observations. The FDR is useful when researchers are looking for "discoveries" that will give them followup work (E.g.: detecting promising genes for followup studies), and are interested in controlling the proportion of "false leads" they are willing to accept.

### Literature

The FDR concept was formally described by Yoav Benjamini and Yosef Hochberg in 1995 (BH procedure) as a less conservative and arguably more appropriate approach for identifying the important few from the trivial many effects tested. The FDR has been particularly influential, as it was the first alternative to the FWER to gain broad acceptance in many scientific fields (especially in the life sciences, from genetics to biochemistry, oncology and plant sciences). In 2005, the Benjamini and Hochberg paper from 1995 was identified as one of the 25 most-cited statistical papers.

Prior to the 1995 introduction of the FDR concept, various precursor ideas had been considered in the statistics literature. In 1979, Holm proposed the Holm procedure, a stepwise algorithm for controlling the FWER that is at least as powerful as the well-known Bonferroni adjustment. This stepwise algorithm sorts the *p*-values and sequentially rejects the hypotheses starting from the smallest *p*-values.

Benjamini (2010) said that the false discovery rate, and the paper Benjamini and Hochberg (1995), had its origins in two papers concerned with multiple testing:

- The first paper is by Schweder and Spjotvoll (1982) who suggested plotting the ranked *p*-values and assessing the number of true null hypotheses ( $m_{0}$ ) via an eye-fitted line starting from the largest *p*-values. The *p*-values that deviate from this straight line then should correspond to the false null hypotheses. This idea was later developed into an algorithm and incorporated the estimation of $m_{0}$ into procedures such as Bonferroni, Holm or Hochberg. This idea is closely related to the graphical interpretation of the BH procedure.
- The second paper is by Branko Soric (1989) which introduced the terminology of "discovery" in the multiple hypothesis testing context. Soric used the expected number of false discoveries divided by the number of discoveries $\left(E[V]/R\right)$ as a warning that "a large part of statistical discoveries may be wrong". This led Benjamini and Hochberg to the idea that a similar error rate, rather than being merely a warning, can serve as a worthy goal to control.

The BH procedure was proven to control the FDR for independent tests in 1995 by Benjamini and Hochberg. In 1986, R. J. Simes offered the same procedure as the "Simes procedure", in order to control the FWER in the weak sense (under the intersection null hypothesis) when the statistics are independent.

## Definitions

Based on definitions below we can define Q as the proportion of false discoveries among the discoveries (rejections of the null hypothesis): $Q={\frac {V}{R}}={\frac {V}{V+S}}.$ where V is the number of false discoveries and S is the number of true discoveries.

The **false discovery rate** (**FDR**) is then simply the following: $\mathrm {FDR} =Q_{e}=\operatorname {E} [Q],$ where $\operatorname {E} [Q]$ is the expected value of Q . The goal is to keep FDR below a given threshold *q*. To avoid division by zero, Q is defined to be 0 when $R=0$ . Formally, $\mathrm {FDR} =\operatorname {E} [V/R\mid R>0]\cdot \operatorname {P} (R>0)$ .

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

## Controlling procedures

The settings for many procedures is such that we have $H_{1},\ldots ,H_{m}$ null hypotheses tested and $P_{1},\ldots ,P_{m}$ their corresponding *p*-values. We list these *p*-values in ascending order and denote them by $P_{(1)},\ldots ,P_{(m)}$ . A procedure that goes from a small test-statistic to a large one will be called a step-up procedure. In a similar way, in a "step-down" procedure we move from a large corresponding test statistic to a smaller one.

### Benjamini–Hochberg procedure

The *Benjamini–Hochberg procedure* (BH step-up procedure) controls the FDR at level $\alpha$ under certain conditions, such as independent test statistics. It works as follows:

1. For a given $\alpha$ , find the largest k for which $P_{(k)}\leq {\frac {k}{m}}\alpha$
2. Reject the null hypothesis (i.e., declare discoveries) for all $H_{(i)}$ for $i=1,\ldots ,k$

Geometrically, this corresponds to plotting $P_{(k)}$ vs. k (on the y and x axes respectively), drawing the line through the origin with slope ${\frac {\alpha }{m}}$ , and declaring discoveries for all points on the left, up to, and including the last point that is not above the line.

The BH procedure is valid when the m tests are independent, and also in various scenarios of dependence, but is not universally valid. It also satisfies the inequality: $E(Q)\leq {\frac {m_{0}}{m}}\alpha \leq \alpha$ If an estimator of $m_{0}$ is inserted into the BH procedure, it is no longer guaranteed to achieve FDR control at the desired level. Adjustments may be needed in the estimator and several modifications have been proposed.

Note that the mean $\alpha$ for these m tests is ${\frac {\alpha (m+1)}{2m}}$ , the Mean(FDR $\alpha$ ) or MFDR, $\alpha$ adjusted for m independent or positively correlated tests (see AFDR below). The MFDR expression here is for a single recomputed value of $\alpha$ and is not part of the Benjamini and Hochberg method.

### Benjamini–Yekutieli procedure

The *Benjamini–Yekutieli* procedure controls the false discovery rate under arbitrary dependence assumptions. This refinement modifies the threshold and finds the largest k for which $P_{(k)}\leq {\frac {k}{m\cdot c(m)}}\alpha .$

- If the tests are independent or positively correlated (as in Benjamini–Hochberg procedure): $c(m)=1$
- Under arbitrary dependence (including the case of negative correlation), c(m) is the harmonic number: $c(m)=\sum _{i=1}^{m}{\frac {1}{i}}$ . Note that $c(m)$ can be approximated by using the Taylor series expansion and the Euler–Mascheroni constant ( $\gamma =0.57721\ldots$ ): $\sum _{i=1}^{m}{\frac {1}{i}}\approx \ln(m)+\gamma +{\frac {1}{2m}}.$

Using MFDR and formulas above, an adjusted MFDR (or AFDR) is the minimum of the mean $\alpha$ for m dependent tests, i.e.,

${\frac {\mathrm {MFDR} }{c(m)}}={\frac {\alpha (m+1)}{2m[\ln(m)+\gamma ]+1}}.$

Another way to address dependence is by bootstrapping and rerandomization.

### Storey–Tibshirani procedure

In the Storey–Tibshirani procedure, q-values are used for controlling the FDR.

## Properties

### Adaptive and scalable

Using a multiplicity procedure that controls the FDR criterion is adaptive and scalable. Meaning that controlling the FDR can be very permissive (if the data justify it), or conservative (acting close to control of FWER for sparse problem) - all depending on the number of hypotheses tested and the level of significance.

The FDR criterion *adapts* so that the same number of false discoveries (V) will have different implications, depending on the total number of discoveries (R). This contrasts with the family-wise error rate criterion. For example, if inspecting 100 hypotheses (say, 100 genetic mutations or SNPs for association with some phenotype in some population):

- If we make 4 discoveries (R), having 2 of them be false discoveries (V) is often very costly. Whereas,
- If we make 50 discoveries (R), having 2 of them be false discoveries (V) is often not very costly.

The FDR criterion is *scalable* in that the same proportion of false discoveries out of the total number of discoveries (Q), remains sensible for different number of total discoveries (R). For example:

- If we make 100 discoveries (R), having 5 of them be false discoveries ( $q=5\%$ ) may not be very costly.
- Similarly, if we make 1000 discoveries (R), having 50 of them be false discoveries (as before, $q=5\%$ ) may still not be very costly.

### Dependency among the test statistics

Controlling the FDR using the linear step-up BH procedure, at level q, has several properties related to the dependency structure between the test statistics of the m null hypotheses that are being corrected for. If the test statistics are:

- Independent: $\mathrm {FDR} \leq {\frac {m_{0}}{m}}q$
- Independent and continuous: $\mathrm {FDR} ={\frac {m_{0}}{m}}q$
- Positive dependent: $\mathrm {FDR} \leq {\frac {m_{0}}{m}}q$
- In the general case: $\mathrm {FDR} \leq {\frac {m_{0}}{m}}{\frac {q}{1+{\frac {1}{2}}+{\frac {1}{3}}+\cdots +{\frac {1}{m}}}}\approx {\frac {m_{0}}{m}}{\frac {q}{\ln(m)+\gamma +{\frac {1}{2m}}}},$ where $\gamma$ is the Euler–Mascheroni constant.

### Proportion of true hypotheses

If all of the null hypotheses are true ( $m_{0}=m$ ), then controlling the FDR at level q guarantees control over the FWER (this is also called "weak control of the FWER"): $\mathrm {FWER} =P\left(V\geq 1\right)=E\left({\frac {V}{R}}\right)=\mathrm {FDR} \leq q$ , simply because the event of rejecting at least one true null hypothesis $\{V\geq 1\}$ is exactly the event $\{V/R=1\}$ , and the event $\{V=0\}$ is exactly the event $\{V/R=0\}$ (when $V=R=0$ , $V/R=0$ by definition). But if there are some true discoveries to be made ( $m_{0}<m$ ) then FWER ≥ FDR. In that case there will be room for improving detection power. It also means that any procedure that controls the FWER will also control the FDR.

### Average power

The average power of the Benjamini–Hochberg procedure can be computed analytically

The discovery of the FDR was preceded and followed by many other types of error rates. These include:

- PCER (per-comparison error rate) is defined as: $\mathrm {PCER} =E\left[{\frac {V}{m}}\right]$ . Testing individually each hypothesis at level α guarantees that $\mathrm {PCER} \leq \alpha$ (this is testing without any correction for multiplicity)
- FWER (the family-wise error rate) is defined as: $\mathrm {FWER} =P(V\geq 1)$ . There are numerous procedures that control the FWER.
- $k{\text{-FWER}}$ (The tail probability of the False Discovery Proportion), suggested by Lehmann and Romano, van der Laan at al, is defined as: $k{\text{-FWER}}=P(V\geq k)\leq q$ .
- $k{\text{-FDR}}$ (also called the *generalized FDR* by Sarkar in 2007) is defined as: $k{\text{-FDR}}=E\left({\frac {V}{R}}I_{(V>k)}\right)\leq q$ .
- $Q'$ is the proportion of false discoveries among the discoveries", suggested by Soric in 1989, and is defined as: $Q'={\frac {E[V]}{R}}$ . This is a mixture of expectations and realizations, and has the problem of control for $m_{0}=m$ .
- $\mathrm {FDR} _{-1}$ (or Fdr) was used by Benjamini and Hochberg, and later called "Fdr" by Efron (2008) and earlier. It is defined as: $\mathrm {FDR} _{-1}=Fdr={\frac {E[V]}{E[R]}}$ . This error rate cannot be strictly controlled because it is 1 when $m=m_{0}$ .
- $\mathrm {FDR} _{+1}$ was used by Benjamini and Hochberg, and later called "pFDR" by Storey (2002). It is defined as: $\mathrm {FDR} _{+1}=p\mathrm {FDR} =E\left[{\frac {V}{R}}\,{\Big \vert }\,R>0\right]$ . This error rate cannot be strictly controlled because it is 1 when $m=m_{0}$ . JD Storey promoted the use of the pFDR (a close relative of the FDR), and the q-value, which can be viewed as the proportion of false discoveries that we expect in an ordered table of results, up to the current line. Storey also promoted the idea (also mentioned by BH) that the actual number of null hypotheses, $m_{0}$ , can be estimated from the shape of the probability distribution curve. For example, in a set of data where all null hypotheses are true, 50% of results will yield probabilities between 0.5 and 1.0 (and the other 50% will yield probabilities between 0.0 and 0.5). We can therefore estimate $m_{0}$ by finding the number of results with $P>0.5$ and doubling it, and this permits refinement of our calculation of the pFDR at any particular cut-off in the data-set.
- False exceedance rate (the tail probability of FDP), defined as: $\mathrm {P} \left({\frac {V}{R}}>q\right)$
- $W{\text{-FDR}}$ (Weighted FDR). Associated with each hypothesis i is a weight $w_{i}\geq 0$ , the weights capture importance/price. The W-FDR is defined as: $W{\text{-FDR}}=E\left({\frac {\sum w_{i}V_{i}}{\sum w_{i}R_{i}}}\right)$ .
- FDCR (False Discovery Cost Rate). Stemming from statistical process control: associated with each hypothesis i is a cost $\mathrm {c} _{i}$ and with the intersection hypothesis $H_{00}$ a cost $c_{0}$ . The motivation is that stopping a production process may incur a fixed cost. It is defined as:

$\mathrm {FDCR} =E\left(c_{0}V_{0}+{\frac {\sum c_{i}V_{i}}{c_{0}R_{0}+\sum c_{i}R_{i}}}\right)$

- PFER (per-family error rate) is defined as: $\mathrm {PFER} =E(V)$ .
- FNR (False non-discovery rates) by Sarkar; Genovese and Wasserman is defined as

$\mathrm {FNR} =E\left({\frac {T}{m-R}}\right)=E\left({\frac {m-m_{0}-(R-V)}{m-R}}\right)$

- $\mathrm {FDR} (z)$ is defined as: $\mathrm {FDR} (z)={\frac {p_{0}F_{0}(z)}{F(z)}}$
- $\mathrm {fdr}$ , local-fdr is defined as: $\mathrm {fdr} ={\frac {p_{0}f_{0}(z)}{f(z)}}$ in a local interval of z .

### False coverage rate

The false coverage rate (FCR) is, in a sense, the FDR analog to the confidence interval. FCR indicates the average rate of false coverage, namely, not covering the true parameters, among the selected intervals. The FCR gives a simultaneous coverage at a $1-\alpha$ level for all of the parameters considered in the problem. Intervals with simultaneous coverage probability 1 − *q* can control the FCR to be bounded by *q*. There are many FCR procedures such as: Bonferroni-Selected–Bonferroni-Adjusted, Adjusted BH-Selected CIs (Benjamini and Yekutieli (2005)), Bayes FCR (Zhao and Hwang (2012)), and other Bayes methods.

### Bayesian approaches

Connections have been made between the FDR and Bayesian approaches (including empirical Bayes methods), thresholding wavelets coefficients and model selection, and generalizing the confidence interval into the false coverage statement rate (FCR).

### Structural false discovery rate (sFDR)

The **structural false discovery rate (sFDR)** is a generalization of the classical false discovery rate (FDR) introduced by D. Meskaldji and collaborators in 2018.

The sFDR extends the FDR by replacing the linear denominator R in the expected ratio E[*V*/*R*] with a non-decreasing concave function *s*(*R*), yielding the criterion E[*V*/*s*(*R*)]. This approach allows the control of false discoveries to adapt to the scale of testing, so that prudence increases faster than linearly as the number of rejections grows.

When *s*(*R*) = *R*, the classical FDR is recovered, while specific choices of s(R) can interpolate between FDR control and family-wise error control (*k*-FWER). The sFDR provides a structural connection between classical, local, and generalized false discovery concepts, and has been extended to online and adaptive settings.

### Empirical false discovery rate (eFDR)

Conventional *p*-value adjustment methods, like the Bonferroni and Benjamini-Hochberg, often overcorrect the *p*-values when the input datasets are not independent but interconnected, which is often the case in biological data, like functional enrichment analysis of differentially expressed genes. This overcorrection resulted in potentially missing biologically relevant terms with significant enrichment. Empirical false discovery rate address this problem with the so-called “plug-in” estimate of the false discovery rate (Algorithm 18.3 of Hastie et al. ), which is implemented within the *mulea* R package. This method is an *empirical*, resampling-based approach to calculating the false discovery rate (FDR), which we abbreviate as $eFDR$ .

#### The description of the eFDR algorithm applied for functional enrichment analysis

For each ontology entry ${\textstyle (j=1,2,\ldots ,J)}$ and the investigated target set (*e.g.*, significantly differentially expressed genes), *mulea* calculates a *p*-value ${\textstyle (p_{j})}$ based on the hypergeometric test. To assess the unbiased statistical significance of each ontology entry, we compute the empirical false discovery rate ${\textstyle (eFDR_{j})}$ using a resampling-based approach.

First, we determine the rank of each ontology entry's *p*-value relative to the *p*-values of all ontology entries. ${\textstyle R_{j}}$ refers to the rank of the *p*-value of the ${\textstyle j^{th}}$ ontology entry. Here, we do note the indicator function with Iverson brackets: ${\textstyle I()}$ :

$R_{j}=\sum _{i=1}^{J}I\!\left(p_{i}\leq p_{j}\right),\;j=1,\ldots ,J$

To calculate the expected rank ${\textstyle \left({\bar {R}}_{j}\right)}$ of the *p*-value of the ${\textstyle j^{th}}$ ontology entry, a resampling strategy is applied, where resampling steps are indexed with ${\textstyle (s=1,2,\ldots ,S)}$ . In each resampling step, a simulated target set with the same size as the original target set is generated, but with randomly selected elements from the background set. Then we recalculate the hypergeometric tests and the ranks of the *p*-values ${\textstyle \left(R_{j}^{s}\right)}$ for each resampling step. Let ${\textstyle {\bar {R}}_{j}}$ be the expectation of the ${\textstyle R_{j}^{s}}$ values over ${\textstyle s}$ :

${\bar {R}}_{j}={\frac {\displaystyle \sum _{s=1}^{S}R_{j}^{s}}{S}}$

The ${\textstyle eFDR}$ of the ${\textstyle j^{th}}$ ontology entry ${\textstyle (eFDR_{j})}$ is calculated as the ratio of the expected rank ${\textstyle \left({\bar {R}}_{j}\right)}$ to the actual rank ${\textstyle \left(R_{j}\right)}$ . If the calculated ${\textstyle eFDR_{j}}$ exceeds ${\textstyle 1}$ , it is truncated to ${\textstyle 1}$ .

$eFDR_{j}=\min \!\left({\frac {R_{j}}{{\bar {R}}_{j}}},\,1\right)$

## Software implementations

- False Discovery Rate Analysis in R – Lists links with popular R packages
- False Discovery Rate Analysis in Python – Python implementations of false discovery rate procedures
- Empirical False Discovery Rate Analysis in R using the *mulea* package.
