---
title: "Odds ratio"
source: https://en.wikipedia.org/wiki/Odds_ratio
domain: logistic-regression
license: CC-BY-SA-4.0
tags: logistic regression, logit, odds ratio, probit model
fetched: 2026-07-02
---

# Odds ratio

An **odds ratio** (**OR**) is a statistic that quantifies the strength of the association between two events, A and B. The odds ratio is defined as the ratio of the odds of event A taking place in the presence of B, and the odds of A in the absence of B. Due to symmetry, odds ratio reciprocally calculates the ratio of the odds of B occurring in the presence of A, and the odds of B in the absence of A. Two events are independent if and only if the OR equals 1, i.e., the odds of one event are the same in either the presence or absence of the other event. If the OR is greater than 1, then A and B are associated (correlated) in the sense that, compared to the absence of B, the presence of B raises the odds of A, and symmetrically the presence of A raises the odds of B. Conversely, if the OR is less than 1, then A and B are negatively correlated, and the presence of one event reduces the odds of the other event occurring.

Note that the odds ratio is symmetric in the two events, and no causal direction is implied (correlation does not imply causation): an OR greater than 1 does not establish that B causes A, or that A causes B.

Two similar statistics that are often used to quantify associations are the relative risk (RR) and the absolute risk reduction (ARR). Often, the parameter of greatest interest is actually the RR, which is the ratio of the probabilities analogous to the odds used in the OR. However, available data frequently do not allow for the computation of the RR or the ARR, but do allow for the computation of the OR, as in case-control studies, as explained below. On the other hand, if one of the properties (A or B) is sufficiently rare (in epidemiology this is called the rare disease assumption), then the OR is approximately equal to the corresponding RR.

The OR plays an important role in the logistic model.

## Definition and basic properties

### Intuition from an example for laypeople

If we flip an unbiased coin, the probability of getting heads and the probability of getting tails are equal — both are 50%. Imagine we get a biased coin such that, if one flips it, one is twice as likely to get heads than tails (i.e., the *odds* double: from 1:1 to 2:1). The new probabilities would be 66.666...% for heads and 33.333...% for tails.

### A motivating example, in the context of the rare disease assumption

Suppose a radiation leak in a village of 1,000 people increased the incidence of a rare disease. The total number of people exposed to the radiation was $V_{E}=400,$ out of which $D_{E}=20$ developed the disease and $H_{E}=380$ stayed healthy. The total number of people not exposed was $V_{N}=600,$ out of which $D_{N}=6$ developed the disease and $H_{N}=594$ stayed healthy. We can organize this in a contingency table:

${\begin{array}{|r|cc|}\hline &{\text{ Diseased }}&{\text{ Healthy }}\\\hline {\text{ Exposed }}&20&380\\{\text{ Not exposed }}&6&594\\\hline \end{array}}$

The *risk* of developing the disease given exposure is $D_{E}/V_{E}=20/400=.05$ and of developing the disease given non-exposure is $D_{N}/V_{N}=6/600=.01$ . One obvious way to compare the risks is to use the ratio of the two, the *relative risk*.

${\text{Relative risk}}={\frac {D_{E}/(D_{E}+H_{E})}{D_{N}/(D_{N}+H_{N})}}={\frac {D_{E}/V_{E}}{D_{N}/V_{N}}}={\frac {20/400}{6/600}}={\frac {.05}{.01}}=5\,.$

The odds ratio is different. The *odds* of getting the disease if exposed is $D_{E}/H_{E}=20/380\approx .0526,$ and the odds if *not* exposed is $D_{N}/H_{N}=6/594\approx .0101\,.$ The *odds ratio* is the ratio of the two,

${\text{Odds ratio}}={\frac {D_{E}/H_{E}}{D_{N}/H_{N}}}={\frac {20/380}{6/594}}\approx {\frac {.0526}{.0101}}=5.2\,.$

As illustrated by this example, in a rare-disease case like this, the relative risk and the odds ratio are almost the same. By definition, rare disease implies that $V_{E}\approx H_{E}$ and $V_{N}\approx H_{N}$ . Thus, the denominators in the relative risk and odds ratio are almost the same ( $400\approx 380$ and $600\approx 594)$ .

Relative risk is easier to understand than the odds ratio, but one reason to use odds ratio is that usually, data on the entire population is not available and random sampling must be used. In the example above, if it were very costly to interview villagers and find out if they were exposed to the radiation, then the prevalence of radiation exposure would not be known, and neither would the values of $V_{E}$ or $V_{N}$ . One could take a random sample of fifty villagers, but quite possibly such a random sample would not include anybody with the disease, since only 2.6% of the population are diseased. Instead, one might use a case-control study in which all 26 diseased villagers are interviewed as well as a random sample of 26 who do not have the disease. The results might turn out as follows ("might", because this is a random sample):

${\begin{array}{|r|cc|}\hline &{\text{ Diseased }}&{\text{ Healthy }}\\\hline {\text{ Exposed }}&20&10\\{\text{ Not exposed }}&6&16\\\hline \end{array}}$

The odds in this sample of getting the disease given that someone is exposed is 20/10 and the odds given that someone is not exposed is 6/16. The odds ratio is thus ${\frac {20/10}{6/16}}\approx 5.3$ , quite close to the odds ratio calculated for the entire village. The relative risk, however, cannot be calculated, because it is the ratio of the risks of getting the disease and we would need $V_{E}$ and $V_{N}$ to figure those out. Because the study selected for people with the disease, half the people in the sample have the disease and it is known that that is more than the population-wide prevalence. Therefore, the numbers of diseased and healthy within exposed, and diseased and healthy within non-exposed, are not addable.

It is standard in the medical literature to calculate the odds ratio and then use the rare-disease assumption (which is usually reasonable) to claim that the relative risk is approximately equal to it. This not only allows for the use of case-control studies, but makes controlling for confounding variables such as weight or age using regression analysis easier and has the desirable properties discussed in other sections of this article of invariance and insensitivity to the type of sampling.

### Definition in terms of group-wise odds

The odds ratio is the ratio of the odds of an event occurring in one group to the odds of it occurring in another group. The term is also used to refer to sample-based estimates of this ratio. These groups might be men and women, an experimental group and a control group, or any other dichotomous classification. If the probabilities of the event in each of the groups are *p*1 (first group) and *p*2 (second group), then the odds ratio is:

$OR={\frac {p_{1}/(1-p_{1})}{p_{2}/(1-p_{2})}}={\frac {p_{1}/q_{1}}{p_{2}/q_{2}}}={\frac {\;p_{1}q_{2}\;}{\;p_{2}q_{1}\;}},$

where *q*x = 1 − *p**x*. An odds ratio of 1 indicates that the condition or event under study is equally likely to occur in both groups. An odds ratio greater than 1 indicates that the condition or event is more likely to occur in the first group. And an odds ratio less than 1 indicates that the condition or event is less likely to occur in the first group. The odds ratio must be nonnegative if it is defined. It is undefined if *p*2*q*1 equals zero, i.e., if *p*2 equals zero or *q*1 equals zero.

### Definition in terms of joint and conditional probabilities

The odds ratio can also be defined in terms of the joint probability distribution of two binary random variables. The joint distribution of binary random variables X and Y can be written

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&p_{11}&p_{10}\\X=0&p_{01}&p_{00}\end{array}}$

where p11, p10, p01 and p00 are non-negative "cell probabilities" that sum to one. The odds for Y within the two subpopulations defined by X = 1 and X = 0 are defined in terms of the conditional probabilities given X, *i.e.*, *P*(*Y* |*X*):

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&{\frac {p_{11}}{p_{11}+p_{10}}}&{\frac {p_{10}}{p_{11}+p_{10}}}\\X=0&{\frac {p_{01}}{p_{01}+p_{00}}}&{\frac {p_{00}}{p_{01}+p_{00}}}\end{array}}$

Thus, the odds ratio is:

$OR={\dfrac {p_{11}/(p_{11}+p_{10})}{p_{10}/(p_{11}+p_{10})}}{\bigg /}{\dfrac {p_{01}/(p_{01}+p_{00})}{p_{00}/(p_{01}+p_{00})}}={\frac {p_{11}p_{00}}{p_{10}p_{01}}}$

Note that the odds ratio is also the product of the probabilities of the "concordant cells" (X = Y) divided by the product of the probabilities of the "discordant cells" (X ≠ Y). However, in some applications the labelling of categories as zero and one is arbitrary, so there is nothing special about concordant versus discordant values in these applications.

### Symmetry

If we had calculated the odds ratio based on the conditional probabilities given *Y*,

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&{\frac {p_{11}}{p_{11}+p_{01}}}&{\frac {p_{10}}{p_{10}+p_{00}}}\\X=0&{\frac {p_{01}}{p_{11}+p_{01}}}&{\frac {p_{00}}{p_{10}+p_{00}}}\end{array}}$

we would have obtained the same result

${\dfrac {p_{11}/(p_{11}+p_{01})}{p_{01}/(p_{11}+p_{01})}}{\bigg /}{\dfrac {p_{10}/(p_{10}+p_{00})}{p_{00}/(p_{10}+p_{00})}}={\dfrac {p_{11}p_{00}}{p_{10}p_{01}}}.$

Other measures of effect size for binary data such as the relative risk do not have this symmetry property.

### Relation to statistical independence

If *X* and *Y* are independent, their joint probabilities can be expressed in terms of their marginal probabilities *p**x* =  *P*(*X* = 1) and *p**y* =  *P*(*Y* = 1), as follows

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&p_{x}p_{y}&p_{x}(1-p_{y})\\X=0&(1-p_{x})p_{y}&(1-p_{x})(1-p_{y})\end{array}}$

In this case, the odds ratio equals one, and conversely the odds ratio can only equal one if the joint probabilities can be factored in this way. Thus the odds ratio equals one if and only if *X* and *Y* are independent.

### Recovering the cell probabilities from the odds ratio and marginal probabilities

The odds ratio is a function of the cell probabilities, and conversely, the cell probabilities can be recovered given knowledge of the odds ratio and the marginal probabilities *P*(*X* = 1) = *p*11 + *p*10 and *P*(*Y* = 1) = *p*11 + *p*01. If the odds ratio *R* differs from 1, then

$p_{11}={\frac {1+(p_{1\cdot }+p_{\cdot 1})(R-1)-S}{2(R-1)}}$

where *p*1• = *p*11 + *p*10,  *p*•1 = *p*11 + *p*01, and

$S={\sqrt {(1+(p_{1\cdot }+p_{\cdot 1})(R-1))^{2}+4R(1-R)p_{1\cdot }p_{\cdot 1}}}.$

In the case where *R* = 1, we have independence, so *p*11 = *p*1•*p*•1.

Once we have *p*11, the other three cell probabilities can easily be recovered from the marginal probabilities.

## Example

Suppose that in a sample of 100 men, 90 drank wine in the previous week (so 10 did not), while in a sample of 80 women only 20 drank wine in the same period (so 60 did not). This forms the contingency table:

${\begin{array}{c|cc}&M=1&M=0\\\hline D=1&90&20\\D=0&10&60\end{array}}$

The odds ratio (OR) can be directly calculated from this table as:

${OR}={\frac {\;90\times 60\;}{\;10\times 20\;}}=27$

Alternatively, the odds of a man drinking wine are 90 to 10, or 9:1, while the odds of a woman drinking wine are only 20 to 60, or 1:3 = 0.33. The odds ratio is thus 9/0.33, or 27, showing that men are much more likely to drink wine than women. The detailed calculation is:

${0.9/0.1 \over 0.2/0.6}={\frac {\;0.9\times 0.6\;}{\;0.1\times 0.2\;}}={0.54 \over 0.02}=27$

This example also shows how odds ratios are sometimes sensitive in stating relative positions: in this sample men are (90/100)/(20/80) = 3.6 times as likely to have drunk wine than women, but have 27 times the odds. The logarithm of the odds ratio, the difference of the logits of the probabilities, tempers this effect, and also makes the measure symmetric with respect to the ordering of groups. For example, using natural logarithms, an odds ratio of 27/1 maps to 3.296, and an odds ratio of 1/27 maps to −3.296.

## Statistical inference

Several approaches to statistical inference for odds ratios have been developed.

One approach to inference uses large sample approximations to the sampling distribution of the log odds ratio (the natural logarithm of the odds ratio). If we use the joint probability notation defined above, the population log odds ratio is

${\log \left({\frac {p_{11}p_{00}}{p_{01}p_{10}}}\right)=\log(p_{11})+\log(p_{00}{\big )}-\log(p_{10})-\log(p_{01})}.\,$

If we observe data in the form of a contingency table

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&n_{11}&n_{10}\\X=0&n_{01}&n_{00}\end{array}}$

then the probabilities in the joint distribution can be estimated as

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&{\hat {p}}_{11}&{\hat {p}}_{10}\\X=0&{\hat {p}}_{01}&{\hat {p}}_{00}\end{array}}$

where ︿*p**ij* = *n**ij* / *n*, with *n* = *n*11 + *n*10 + *n*01 + *n*00 being the sum of all four cell counts. The sample log odds ratio is

${L=\log \left({\dfrac {{\hat {p}}_{11}{\hat {p}}_{00}}{{\hat {p}}_{10}{\hat {p}}_{01}}}\right)=\log \left({\dfrac {n_{11}n_{00}}{n_{10}n_{01}}}\right)}$

.

The distribution of the log odds ratio is approximately normal with:

$L\ \sim \ {\mathcal {N}}(\log(OR),\,\sigma ^{2}).\,$

The standard error for the log odds ratio is approximately

${{\rm {SE}}={\sqrt {{\dfrac {1}{n_{11}}}+{\dfrac {1}{n_{10}}}+{\dfrac {1}{n_{01}}}+{\dfrac {1}{n_{00}}}}}}$

.

This is an asymptotic approximation, and will not give a meaningful result if any of the cell counts are very small. If *L* is the sample log odds ratio, an approximate 95% confidence interval for the population log odds ratio is *L* ± 1.96SE. This can be mapped to exp(*L* − 1.96SE), exp(*L* + 1.96SE) to obtain a 95% confidence interval for the odds ratio. If we wish to test the hypothesis that the population odds ratio equals one, the two-sided p-value is 2*P*(*Z* < −|*L*|/SE), where *P* denotes a probability, and *Z* denotes a standard normal random variable.

An alternative approach to inference for odds ratios looks at the distribution of the data conditionally on the marginal frequencies of *X* and *Y*. An advantage of this approach is that the sampling distribution of the odds ratio can be expressed exactly.

## Role in logistic regression

Logistic regression is one way to generalize the odds ratio beyond two binary variables. Suppose we have a binary response variable *Y* and a binary predictor variable *X*, and in addition we have other predictor variables *Z*1, ..., *Zp* that may or may not be binary. If we use multiple logistic regression to regress *Y* on *X*, *Z1*, ..., *Zp*, then the estimated coefficient ${\hat {\beta }}_{x}$ for *X* is related to a conditional odds ratio. Specifically, at the population level

$e^{\beta _{x}}=\exp(\beta _{x})={\frac {P(Y=1\mid X=1,Z_{1},\ldots ,Z_{p})/P(Y=0\mid X=1,Z_{1},\ldots ,Z_{p})}{P(Y=1\mid X=0,Z_{1},\ldots ,Z_{p})/P(Y=0\mid X=0,Z_{1},\ldots ,Z_{p})}},$

so $\exp({\hat {\beta }}_{x})$ is an estimate of this conditional odds ratio. The interpretation of $\exp({\hat {\beta }}_{x})$ is as an estimate of the odds ratio between *Y* and *X* when the values of *Z*1, ..., *Zp* are held fixed.

## Insensitivity to the type of sampling

If the data form a "population sample", then the cell probabilities ${\widehat {p\,}}_{ij}$ are interpreted as the frequencies of each of the four groups in the population as defined by their *X* and *Y* values. In many settings it is impractical to obtain a population sample, so a selected sample is used. For example, we may choose to sample units with *X* = 1 with a given probability *f*, regardless of their frequency in the population (which would necessitate sampling units with *X* = 0 with probability 1 − *f*). In this situation, our data would follow the following joint probabilities:

${\begin{array}{c|cc}&Y=1&Y=0\\\hline X=1&{\frac {fp_{11}}{p_{11}+p_{10}}}&{\frac {fp_{10}}{p_{11}+p_{10}}}\\X=0&{\frac {(1-f)p_{01}}{p_{01}+p_{00}}}&{\frac {(1-f)p_{00}}{p_{01}+p_{00}}}\end{array}}$

The *odds ratio* *p*11*p*00 / *p*01*p*10 for this distribution does not depend on the value of *f*. This shows that the odds ratio (and consequently the log odds ratio) is invariant to non-random sampling based on one of the variables being studied. Note however that the standard error of the log odds ratio does depend on the value of *f*.

This fact is exploited in two important situations:

- Suppose it is inconvenient or impractical to obtain a population sample, but it is practical to obtain a convenience sample of units with different *X* values, such that within the *X* = 0 and *X* = 1 subsamples the *Y* values are representative of the population (i.e. they follow the correct conditional probabilities).
- Suppose the marginal distribution of one variable, say *X*, is very skewed. For example, if we are studying the relationship between high alcohol consumption and pancreatic cancer in the general population, the incidence of pancreatic cancer would be very low, so it would require a very large population sample to get a modest number of pancreatic cancer cases. However we could use data from hospitals to contact most or all of their pancreatic cancer patients, and then randomly sample an equal number of subjects without pancreatic cancer (this is called a "case-control study").

In both these settings, the odds ratio can be calculated from the selected sample, without biasing the results relative to what would have been obtained for a population sample.

## Use in quantitative research

Due to the widespread use of logistic regression, the odds ratio is widely used in many fields of medical and social science research. The odds ratio is commonly used in survey research, in epidemiology, and to express the results of some clinical trials, such as in case-control studies. It is often abbreviated "OR" in reports. When data from multiple surveys is combined, it will often be expressed as "pooled OR".

## Relation to relative risk

As explained in the "Motivating Example" section, the relative risk is usually better than the odds ratio for understanding the relation between risk and some variable such as radiation or a new drug. That section also explains that if the rare disease assumption holds, the odds ratio is a good approximation to relative risk and that it has some advantages over relative risk. When the rare disease assumption does not hold, the unadjusted odds ratio will be greater than the relative risk, but novel methods can easily use the same data to estimate the relative risk, risk differences, base probabilities, or other quantities.

If the absolute risk in the unexposed group is available, conversion between the two is calculated by:

${\text{Relative risk}}\approx {\frac {\text{Odds ratio}}{1-R_{C}+(R_{C}\times {\text{Odds ratio}})}}$

where *R**C* is the absolute risk of the unexposed group.

If the rare disease assumption does not apply, the odds ratio may be very different from the relative risk and should not be interpreted as a relative risk.

Consider the death rate of men and women passengers when a ship sank. Of 462 women, 154 died and 308 survived. Of 851 men, 709 died and 142 survived. Clearly a man on the ship was more likely to die than a woman, but how much more likely? Since over half the passengers died, the rare disease assumption is strongly violated.

To compute the odds ratio, note that for women the odds of dying were 1 to 2 (154/308). For men, the odds were 5 to 1 (709/142). The odds ratio is 9.99 (4.99/.5). Men had ten times the odds of dying as women.

For women, the probability of death was 33% (154/462). For men the probability was 83% (709/851). The relative risk of death is 2.5 (.83/.33). A man had 2.5 times a woman's probability of dying.

### Confusion and exaggeration

Odds ratios have often been confused with relative risk in medical literature. For non-statisticians, the odds ratio is a difficult concept to comprehend, and it gives a more impressive figure for the effect. However, most authors consider that the relative risk is readily understood. In one study, members of a national disease foundation were actually 3.5 times more likely than nonmembers to have heard of a common treatment for that disease – but the odds ratio was 24 and the paper stated that members were ‘more than 20-fold more likely to have heard of’ the treatment. A study of papers published in two journals reported that 26% of the articles that used an odds ratio interpreted it as a risk ratio.

This may reflect the simple process of uncomprehending authors choosing the most impressive-looking and publishable figure. But its use may in some cases be deliberately deceptive. It has been suggested that the odds ratio should only be presented as a measure of effect size when the risk ratio cannot be estimated directly, but with newly available methods it is always possible to estimate the risk ratio, which should generally be used instead.

While relative risks are potentially easier to interpret for a general audience, there are mathematical and conceptual advantages when using an odds-ratio instead of a relative risk, particularly in regression models. For that reason, there is not a consensus within the fields of epidemiology or biostatistics that relative risks or odds-ratios should be preferred when both can be validly used, such as in clinical trials and cohort studies.

## Invertibility and invariance

The odds ratio has another unique property of being directly mathematically invertible whether analyzing the OR as either disease survival or disease onset incidence – where the OR for survival is direct reciprocal of 1/OR for risk. This is known as the 'invariance of the odds ratio'. In contrast, the relative risk does not possess this mathematical invertible property when studying disease survival vs. onset incidence. This phenomenon of OR invertibility vs. RR non-invertibility is best illustrated with an example:

Suppose in a clinical trial, one has an adverse event risk of 4/100 in drug group, and 2/100 in placebo... yielding a RR=2 and OR=2.04166 for drug-vs-placebo adverse risk. However, if analysis was inverted and adverse events were instead analyzed as event-free survival, then the drug group would have a rate of 96/100, and placebo group would have a rate of 98/100—yielding a drug-vs-placebo a RR=0.9796 for survival, but an OR=0.48979. As one can see, a RR of 0.9796 is clearly not the reciprocal of a RR of 2. In contrast, an OR of 0.48979 is indeed the direct reciprocal of an OR of 2.04166.

This is again what is called the 'invariance of the odds ratio', and why a RR for survival is not the same as a RR for risk, while the OR has this symmetrical property when analyzing either survival or adverse risk. The danger to clinical interpretation for the OR comes when the adverse event rate is not rare, thereby exaggerating differences when the OR rare-disease assumption is not met. On the other hand, when the disease is rare, using a RR for survival (e.g. the RR=0.9796 from above example) can clinically hide and conceal an important doubling of adverse risk associated with a drug or exposure.

## Estimators of the odds ratio

### Sample odds ratio

The **sample odds ratio** *n*11*n*00 / *n*10*n*01 is easy to calculate, and for moderate and large samples performs well as an estimator of the population odds ratio. When one or more of the cells in the contingency table can have a small value, the sample odds ratio can be biased and exhibit high variance.

### Alternative estimators

A number of alternative estimators of the odds ratio have been proposed to address limitations of the sample odds ratio. One alternative estimator is the conditional maximum likelihood estimator, which conditions on the row and column margins when forming the likelihood to maximize (as in Fisher's exact test). Another alternative estimator is the Mantel–Haenszel estimator.

## Numerical examples

The following four contingency tables contain observed cell counts, along with the corresponding sample odds ratio (*OR*) and sample log odds ratio (*LOR*):

OR

= 1,

LOR

= 0

OR

= 1,

LOR

= 0

OR

= 4,

LOR

= 1.39

OR

= 0.25,

LOR

= −1.39

Y

= 1

Y

= 0

Y

= 1

Y

= 0

Y

= 1

Y

= 0

Y

= 1

Y

= 0

X

= 1

10

10

100

100

20

10

10

20

X

= 0

5

5

50

50

10

20

20

10

The following joint probability distributions contain the population cell probabilities, along with the corresponding population odds ratio (*OR*) and population log odds ratio (*LOR*):

OR

= 1,

LOR

= 0

OR

= 1,

LOR

= 0

OR

= 16,

LOR

= 2.77

OR

= 0.67,

LOR

= −0.41

Y

= 1

Y

= 0

Y

= 1

Y

= 0

Y

= 1

Y

= 0

Y

= 1

Y

= 0

X

= 1

0.2

0.2

0.4

0.4

0.4

0.1

0.1

0.3

X

= 0

0.3

0.3

0.1

0.1

0.1

0.4

0.2

0.4

## Numerical example

| Quantity | Experimental group (E) | Control group (C) | Total |
|---|---|---|---|
| Events (E) | *EE* = 15 | *CE* = 100 | 115 |
| Non-events (N) | *EN* = 135 | *CN* = 150 | 285 |
| Total subjects (S) | *ES* = *EE* + *EN* = 150 | *CS* = *CE* + *CN* = 250 | 400 |
| Event rate (ER) | *EER* = *EE* / *ES* = 0.1, or 10% | *CER* = *CE* / *CS* = 0.4, or 40% | — |

| Variable | Abbr. | Formula | Value |
|---|---|---|---|
| Absolute risk reduction | ARR | *CER* − *EER* | 0.3, or 30% |
| Number needed to treat | NNT | 1 / (*CER* − *EER*) | 3.33 |
| Relative risk (risk ratio) | RR | *EER* / *CER* | 0.25 |
| Relative risk reduction | RRR | (*CER* − *EER*) / *CER*, or 1 − *RR* | 0.75, or 75% |
| Preventable fraction among the unexposed | PFu | (*CER* − *EER*) / *CER* | 0.75 |
| Odds ratio | OR | (*EE* / *EN*) / (*CE* / *CN*) | 0.167 |

There are various other summary statistics for contingency tables that measure association between two events, such as Yule's *Y*, Yule's *Q*; these two are normalized so they are 0 for independent events, 1 for perfectly correlated, −1 for perfectly negatively correlated. A. W. F. Edwards studied these and argued that these measures of association must be functions of the odds ratio, which he referred to as the cross-ratio.

## Odds Ratio for a Matched Case-Control Study

A case-control study involves selecting representative samples of cases and controls who do, and do not, have some disease, respectively. These samples are usually independent of each other. The prior prevalence of exposure to some risk factor is observed in subjects from both samples. This permits the estimation of the odds ratio for disease in exposed vs. unexposed people as noted above. Sometimes, however, it makes sense to match cases to controls on one or more confounding variables. In this case, the prior exposure of interest is determined for each case and her/his matched control. The data can be summarized in the following table.

### Matched 2 × 2 Table

| Case-control pairs | Control exposed | Control unexposed |
|---|---|---|
| Case exposed | $n_{11}$ | $n_{10}$ |
| Case unexposed | $n_{01}$ | $n_{00}$ |

This table gives the exposure status of the matched pairs of subjects. There are $n_{11}$ pairs where both the case and her/his matched control were exposed, $n_{10}$ pairs where the case patient was exposed but the control subject was not, $n_{01}$ pairs where the control subject was exposed but the case patient was not, and $n_{00}$ pairs were neither subject was exposed. The exposure of matched case and control pairs is correlated due to the similar values of their shared confounding variables.

The following derivation is due to Breslow & Day. We consider each pair as belonging to a stratum with identical values of the confounding variables. Conditioned on belonging to the same stratum, the exposure status of cases and controls are independent of each other. For any case-control pair within the same stratum let

$p_{1}$

be the probability that a case patient is exposed,

$p_{0}$

be the probability that a control patient is exposed,

$q_{1}=1-p_{1}$

be the probability that a case patient is not exposed, and

$q_{0}=1-p_{0}$

be the probability that a control patient is not exposed.

Then the probability that a case is exposed and a control is not is $p_{1}q_{0}$ , and the probability that a control is exposed and a case in not is $p_{0}q_{1}$ . The within-stratum odds ratio for exposure in cases relative to controls is

$\psi =(p_{1}/q_{1})/(p_{0}/q_{0})=p_{1}q_{0}/(q_{1}p_{0})$

We assume that ψ is constant across strata.

Now concordant pairs in which either both the case and the control are exposed, or neither are exposed tell us nothing about the odds of exposure in cases relative to the odds of exposure among controls. The probability that the case is exposed and the control is not given that the pair is discordant is

$\pi =(p_{1}q_{0})/(p_{1}q_{0}+q_{1}p_{0})=\psi /(\psi +1)$

The distribution of $n_{10}$ given the number of discordant pairs is binomial  ~  B $(n_{10}+n_{01},\pi )$ and the maximum likelihood estimate of π is

${\hat {\pi }}=n_{10}/(n_{10}+n_{01})={\hat {\psi }}/({\hat {\psi }}+1)$

Multiplying both sides of this equation by $(n_{10}+n_{01})({\hat {\psi }}+1)$ and subtracting $n_{10}{\hat {\psi }}$ gives

$n_{10}={\hat {\psi }}(n_{10}+n_{01}-n_{10})$

and hence

${\hat {\psi }}=n_{10}/n_{01}$

.

Now ${\hat {\pi }}$ is the maximum likelihood estimate of π, and ψ is a monotonic function of ${\hat {\pi }}$ . It follows that ${\hat {\psi }}$ is the conditional maximum likelihood estimate of ${\hat {\psi }}$ given the number of discordant pairs. Rothman et al. give an alternate derivation of ${\hat {\psi }}$ by showing that it is a special case of the Mantel-Haenszel estimate of the intra-strata odds ratio for stratified 2x2 tables. They also reference Breslow & Day as providing the derivation given here.

Under the null hypothesis that $\psi =1,\pi =1/(1+1)=0.5$ .

Hence, we can test the null hypothesis that $\psi =1$ by testing the null hypothesis that $\pi =0.5$ . This is done using McNemar's test.

There are a number of ways to calculate a confidence interval for π. Let ${\hat {\pi }}_{LB}$ and ${\hat {\pi }}_{UB}$ denote the lower and upper bound of a confidence interval for π, respectively. Since $\psi =\pi /(1-\pi )$ , the corresponding confidence interval for ψ is

$({\frac {{\hat {\pi }}_{LB}}{1-{\hat {\pi }}_{LB}}},{\frac {{\hat {\pi }}_{UB}}{1-{\hat {\pi }}_{UB}}})$

.

Matched 2x2 tables may also be analyzed using conditional logistic regression. This technique has the advantage of allowing users to regress case-control status against multiple risk factors from matched case-control data.

### Example

McEvoy et al. studied the use of cell phones by drivers as a risk factor for automobile crashes in a case-crossover study. All study subjects were involved in an automobile crash requiring hospital attendance. Each driver's cell phone use at the time of her/his crash was compared to her/his cell phone use in a control interval at the same time of day one week earlier. We would expect that a person's cell phone use at the time of the crash would be correlated with his/her use one week earlier. Comparing usage during the crash and control intervals adjusts for driver's characteristics and the time of day and day of the week. The data can be summarized in the following table.

| Case-control pairs | Phone used in control interval | Phone not used in control interval |
|---|---|---|
| Phone used in crash interval | 5 | 27 |
| Phone not used in crash interval | 6 | 288 |

There were 5 drivers who used their phones in both intervals, 27 who used them in the crash but not the control interval, 6 who used them in the control but not the crash interval, and 288 who did not use them in either interval. The odds ratio for crashing while using their phone relative to driving when not using their phone was

${\hat {\psi }}=27/6=4.5$

.

Testing the null hypothesis that ${\hat {\psi }}=1$ is the same as testing the null hypothesis that ${\hat {\pi }}=0.5$ given 27 out of 33 discordant pairs in which the driver was using her/his phone at the time of his crash. McNemar's $\chi ^{2}=13.36$ . This statistic has one degree of freedom and yields a *P* value of 0.0003. This allows us to reject the hypothesis that cell phone use has no effect on the risk of automobile crashes ( $\psi =1$ ) with a high level of statistical significance.

Using Wilson's method, a 95% confidence interval for π is (0.6561, 0.9139). Hence, a 95% confidence interval for ψ is

$\left({\frac {0.6561}{1-0.6561}},{\frac {0.9139}{1-0.9139}}\right)=(1.9,10.6)$

(McEvoy et al. analyzed their data using conditional logistic regression and obtained almost identical results to those given here. See the last row of Table 3 in their paper.)
