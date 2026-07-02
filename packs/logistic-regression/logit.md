---
title: "Logit"
source: https://en.wikipedia.org/wiki/Logit
domain: logistic-regression
license: CC-BY-SA-4.0
tags: logistic regression, logit, odds ratio, probit model
fetched: 2026-07-02
---

# Logit

In statistics, the **logit** (/ˈloʊdʒɪt/ *LOH-jit*) function is the quantile function associated with the standard logistic distribution. It has many uses in data analysis and machine learning, especially in data transformations.

Mathematically, the logit is the inverse of the standard logistic function ⁠ $\textstyle \sigma (x)=1/(1+e^{-x})$ ⁠, so the logit is defined as $\operatorname {logit} p=\sigma ^{-1}(p)=\ln {\frac {p}{1-p}}\quad {\text{for}}\quad p\in (0,1).$

Because of this, the logit is also called the **log-odds** since it is equal to the logarithm of the odds ${\textstyle {\frac {p}{1-p}}}$ where p is a probability. Thus, the logit is a type of function that maps probability values from $(0,1)$ to real numbers in ⁠ $(-\infty ,+\infty )$ ⁠, akin to the probit function.

## Definition

If p is a probability, then ${\textstyle {\tfrac {p}{1-p}}}$ is the corresponding odds; the logit of the probability is the logarithm of the odds, i.e.: ${\begin{aligned}\operatorname {logit} (p)&={\hphantom {-}}\ln \left({\frac {p}{1-p}}\right)=\ln(p)-\ln(1-p)\\&=-\ln \left({\frac {1}{p}}-1\right)=2\operatorname {atanh} (2p-1).\end{aligned}}$

The base of the logarithm function used is of little importance in the present article, as long as it is greater than 1, but the natural logarithm with base e is the one most often used. The choice of base corresponds to the choice of logarithmic unit for the value: base 2 corresponds to a shannon, base e to a nat, and base 10 to a hartley; these units are particularly used in information-theoretic interpretations. For each choice of base, the logit function takes values between negative and positive infinity.

The logistic function of any number $\alpha$ is given by the inverse-logit: $\operatorname {logit} ^{-1}(\alpha )=\operatorname {logistic} (\alpha )={\frac {1}{1+e^{-\alpha }}}={\frac {e^{\alpha }}{e^{\alpha }+1}}={\frac {\tanh({\frac {\alpha }{2}})+1}{2}}$

The difference between the logits of two probabilities is the logarithm of the odds ratio (R), thus providing a shorthand for writing the correct combination of odds ratios only by adding and subtracting: ${\begin{aligned}\ln(R)&=\ln \left({\frac {\tfrac {p_{1}}{1-p_{1}}}{\tfrac {p_{2}}{1-p_{2}}}}\right)\\&=\ln \left({\frac {p_{1}}{1-p_{1}}}\right)-\ln \left({\frac {p_{2}}{1-p_{2}}}\right)\\&=\operatorname {logit} (p_{1})-\operatorname {logit} (p_{2})\,.\end{aligned}}$

The Taylor series for the logit function is given by: $\operatorname {logit} (x)=2\sum _{n=0}^{\infty }{\frac {(2x-1)^{2n+1}}{2n+1}}.$

## History

Several approaches have been explored to adapt linear regression methods to a domain where the output is a probability value ⁠ $(0,1)$ ⁠, instead of any real number ⁠ $(-\infty ,+\infty )$ ⁠. In many cases, such efforts have focused on modeling this problem by mapping the range ⁠ $(0,1)$ ⁠ to ⁠ $(-\infty ,+\infty )$ ⁠ and then running the linear regression on these transformed values.

In 1934, Chester Ittner Bliss used the cumulative normal distribution function to perform this mapping and called his model *probit*, an abbreviation of "probability unit". This is, however, computationally more expensive. In 1944, Joseph Berkson used log of odds and called this function *logit*, an abbreviation of "logistic unit", following the analogy for probit.

Log odds was used extensively by Charles Sanders Peirce in the late 19th century. G. A. Barnard in 1949 coined the commonly used term **log-odds**; the log-odds of an event is the logit of the probability of the event. Barnard also coined the term *lods* as an abstract form of "log-odds", but suggested that "in practice the term 'odds' should normally be used, since this is more familiar in everyday life".

## Uses and properties

- The logit in logistic regression is a special case of a link function in a generalized linear model: it is the canonical link function for the Bernoulli distribution.
- More abstractly, the logit is the natural parameter for the binomial distribution .
- The logit function is the negative of the derivative of the binary entropy function.
- The logit is also central to the probabilistic Rasch model for measurement, which has applications in psychological and educational assessment, among other areas.
- The inverse-logit function (i.e., the logistic function) is also sometimes referred to as the *expit* function.
- In plant disease epidemiology, the logistic, Gompertz, and monomolecular models are collectively known as the Richards family models.
- The log-odds function of probabilities is often used in state estimation algorithms because of its numerical advantages in the case of small probabilities. Instead of multiplying very small floating point numbers, log-odds probabilities can just be summed up to calculate the (log-odds) joint probability.

## Comparison with probit

Closely related to the logit function (and logit model) are the probit function and probit model. The logit and probit are both sigmoid functions with a domain between 0 and 1, which makes them both quantile functions – i.e., inverses of the cumulative distribution function (CDF) of a probability distribution. In fact, the logit is the quantile function of the logistic distribution, while the probit is the quantile function of the normal distribution. The probit function is denoted ⁠ $\operatorname {\Phi } ^{-1}(x)$ ⁠, where ⁠ $\operatorname {\Phi } (x)$ ⁠ is the CDF of the standard normal distribution, as just mentioned: $\operatorname {\Phi } (x)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x}e^{-y^{2}/2}dy.$

As shown in the graph on the right, the logit and probit functions are extremely similar when the probit function is scaled, so that its slope at *y* = 0 matches the slope of the logit. As a result, probit models are sometimes used in place of logit models because for certain applications (e.g., in item response theory) the implementation is easier.
