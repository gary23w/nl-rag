---
title: "G-test"
source: https://en.wikipedia.org/wiki/G-test
domain: chi-squared-tests
license: CC-BY-SA-4.0
tags: chi-squared test, contingency table, goodness of fit, G-test
fetched: 2026-07-02
---

# *G*-test

In statistics, ***G*-tests** are likelihood-ratio or maximum likelihood statistical significance tests that are increasingly being used in situations where chi-squared tests were previously recommended.

## Formulation

The general formula for test statistics of the *G*-test is

$G=2\sum _{i}{O_{i}\cdot \ln \left({\frac {O_{i}}{E_{i}}}\right)},$

where $O_{i}\geq 0$ is the observed count in a cell, $E_{i}>0$ is the expected count under the null hypothesis, $\ln$ denotes the natural logarithm, and the sum is taken over all non-empty cells. The resulting G is asymptotically chi-squared distributed as the total number of observations tends to infinity (convergence in distribution).

Furthermore, the total observed count must be equal to the total expected count:

$\sum _{i}O_{i}=\sum _{i}E_{i}=N,$

where N is the total number of observations.

Both, the *G*-test statistics G and the chi-square test statistics $\chi ^{2}$ are special cases of a general family of power divergence statistics by Cressie and Read. For $\lambda \notin \{0,-1\}$ set

$\operatorname {CR} _{\lambda }={\frac {2}{\lambda (\lambda +1)}}\sum _{i}O_{i}\left(\left({\frac {O_{i}}{E_{i}}}\right)^{\lambda }-1\right).$

Then,

$G=\lim _{\lambda \to 0}\operatorname {CR} _{\lambda },\qquad \chi ^{2}=\operatorname {CR} _{1}.$

### Derivation

We can derive the value of the *G*-test from the log-likelihood ratio test where the underlying model is a multinomial model.

Suppose we had a sample $O=(O_{1},\ldots ,O_{m})$ where each $O_{i}$ is the number of times that an object of type i was observed. Furthermore, let $N=\sum _{i=1}^{m}O_{i}$ be the total number of observations. If we assume that the underlying model is multinomial, then the test statistic is defined by

$\ln \left({\frac {L({\tilde {p}}|O)}{L({\hat {p}}|O)}}\right)=\ln \left({\frac {\prod _{i=1}^{m}{\tilde {p}}_{i}^{O_{i}}}{\prod _{i=1}^{m}{\hat {p}}_{i}^{O_{i}}}}\right),$

where ${\tilde {p}}=({\tilde {p}}_{1},\ldots ,{\tilde {p}}_{m})$ is the null hypothesis and ${\hat {p}}=({\hat {p}}_{1},\ldots ,{\hat {p}}_{m})$ is the maximum likelihood estimate (MLE) of the parameters given the data. Recall that for the multinomial model, the MLE of ${\hat {p}}_{i}$ given some data is given by

${\hat {p}}_{i}={\frac {O_{i}}{N}}\,.$

Furthermore, we may represent each null hypothesis parameter ${\tilde {p}}_{i}$ as

${\tilde {p}}_{i}={\frac {E_{i}}{N}}\,,$

where $E_{i}$ is the expected count of objects of type i under the null hypothesis. Thus, by substituting the representations of ${\tilde {p}}_{i}$ and ${\hat {p}}_{i}$ in the log-likelihood ratio, the equation simplifies to

$\ln \left({\frac {L({\tilde {p}}|O)}{L({\hat {p}}|O)}}\right)=\ln \left(\prod _{i=1}^{m}\left({\frac {E_{i}}{O_{i}}}\right)^{O_{i}}\right)=\sum _{i=1}^{m}O_{i}\ln \left({\frac {E_{i}}{O_{i}}}\right)$

Finally, multiply by a factor of $-2$ (used to make the *G*-test formula asymptotically equivalent to the Pearson's chi-squared test statistics) to achieve the form

$G=-2\sum _{i=1}^{m}O_{i}\ln \left({\frac {E_{i}}{O_{i}}}\right)=2\sum _{i=1}^{m}O_{i}\ln \left({\frac {O_{i}}{E_{i}}}\right)$

Heuristically, one can imagine $O_{i}$ as continuous and approaching zero, in which case $O_{i}\ln O_{i}\to 0$ , and terms with zero observations can simply be dropped. However the *expected* count in each cell must be strictly greater than zero for each cell ( $E_{i}>0$ for all i ) to apply the method.

## Distribution and use

Given the null hypothesis that the observed frequencies result from random sampling from a distribution with the given expected frequencies, the distribution of the test statistics G is approximately a chi-squared distribution, with the same number of degrees of freedom as in the corresponding chi-squared test.

For very small samples the multinomial test for goodness of fit, and Fisher's exact test for contingency tables, or even Bayesian hypothesis selection are preferable to the *G*-test. McDonald recommends to always use an exact test (exact test of goodness-of-fit, Fisher's exact test) if the total sample size is less than 1 000 .

There is nothing magical about a sample size of 1 000, it's just a nice round number that is well within the range where an exact test, chi-square test, and

G

–test will give almost identical

p

values. Spreadsheets, web-page calculators, and

SAS

shouldn't have any problem doing an exact test on a sample size of 1 000 .

— John H. McDonald (2014)

*G*-tests have been recommended at least since the 1981 edition of *Biometry*, a statistics textbook by Robert R. Sokal and F. James Rohlf.

## Relation to other metrics

### Relation to the chi-squared test

The commonly used chi-squared tests for goodness of fit to a distribution and for independence in contingency tables are in fact approximations of the log-likelihood ratio on which the *G*-tests are based.

The general formula for Pearson's chi-squared test statistic is

$\chi ^{2}=\sum _{i}{\frac {\left(O_{i}-E_{i}\right)^{2}}{E_{i}}}.$

The approximation of the *G*-test statistics by chi-squared test statistics is obtained by a second order Taylor expansion of the natural logarithm around 1 (see the derivation below). We have $G\approx \chi ^{2}$ when the observed counts $O_{i}$ are close to the expected counts $E_{i}$ . When this difference is large, however, the approximation by the chi-squared test statistics begins to break down. Here, the effects of outliers in data will be more pronounced, and this explains the why chi-squared tests fail in situations with little data.

For samples of a reasonable size, the *G*-test and the chi-squared test will lead to the same conclusions. However, the approximation to the theoretical chi-squared distribution for the *G*-test is better than for the Pearson's chi-squared test. In cases where $O_{i}>2\cdot E_{i}$ for some cell case the *G*-test is always better than the chi-squared test.

For testing goodness-of-fit the *G*-test is infinitely more efficient than the chi-squared test in the sense of Bahadur, but the two tests are equally efficient in the sense of Pitman or in the sense of Hodges and Lehmann.

#### Derivation (chi-squared)

Consider

$G=2\sum _{i}{O_{i}\ln \left({\frac {O_{i}}{E_{i}}}\right)},$

and let $O_{i}=E_{i}+\delta _{i}$ with $\textstyle \sum _{i}\delta _{i}=0$ , so that the total number of counts remains the same. Assume that $\delta _{i}=O_{i}-E_{i}$ is small in comparison to $E_{i}$ for all i . To be more precise, notice that $E_{i}=\Theta (n)$ using big *Θ* notation. If $O_{i}=E_{i}+{\mathcal {O}}(n^{1/2})$ using big *O* notation for large n , which should be true under the null hypothesis because of the central limit theorem, then $\delta _{i}={\mathcal {O}}(n^{1/2})$ and

${\frac {\delta _{i}^{3}}{E_{i}^{2}}}={\mathcal {O}}\left({\frac {n^{3/2}}{n^{2}}}\right)={\mathcal {O}}(n^{-1/2})$

follow, which will be used later.

Upon substitution we find,

$G=2\sum _{i}(E_{i}+\delta _{i})\ln \left(1+{\frac {\delta _{i}}{E_{i}}}\right).$

Using the Taylor expansion $\ln(1+x)=x-{\tfrac {1}{2}}x^{2}+{\mathcal {O}}(x^{3})$ yields

$G=2\sum _{i}(E_{i}+\delta _{i})\left({\frac {\delta _{i}}{E_{i}}}-{\frac {1}{2}}{\frac {\delta _{i}^{2}}{E_{i}^{2}}}+{\mathcal {O}}\left({\frac {\delta _{i}^{3}}{E_{i}^{3}}}\right)\right),$

and distributing terms we find,

$G=2\sum _{i}\left(\delta _{i}+{\frac {1}{2}}{\frac {\delta _{i}^{2}}{E_{i}}}+{\mathcal {O}}\left({\frac {\delta _{i}^{3}}{E_{i}^{2}}}\right)\right).$

Now, using $\textstyle \sum _{i}\delta _{i}=0$ and $\delta _{i}=O_{i}-E_{i}$ and ${\mathcal {O}}(\delta _{i}^{3}/E_{i}^{2})={\mathcal {O}}(n^{-1/2})$ for large n , we can write the result,

$G\approx \sum _{i}{\frac {\left(O_{i}-E_{i}\right)^{2}}{E_{i}}}.$

### Relation to Kullback–Leibler divergence

The *G*-test statistic is proportional to the Kullback–Leibler divergence of the theoretical distribution ${\tilde {p}}=({\tilde {p}}_{1},\ldots ,{\tilde {p}}_{m})$ of the null hypothesis from the empirical distribution ${\hat {p}}=({\hat {p}}_{1},\ldots ,{\hat {p}}_{m})$ of the observed data:

${\begin{aligned}G&=2\sum _{i}{O_{i}\cdot \ln \left({\frac {O_{i}}{E_{i}}}\right)}=2N\sum _{i}{{\hat {p}}_{i}\cdot \ln \left({\frac {{\hat {p}}_{i}}{{\tilde {p}}_{i}}}\right)}\\&=2N\,D_{\mathrm {KL} }({\hat {p}}\|{\tilde {p}}),\end{aligned}}$

where N is the total number of observations and ${\tilde {p}}_{i}={\tfrac {E_{i}}{N}}$ and ${\hat {p}}_{i}={\tfrac {O_{i}}{N}}$ are the theoretical and empirical probabilities of objects of type i , respectively.

### Relation to mutual information

For analysis of contingency tables the value of the *G*-test statistics can also be expressed in terms of mutual information.

In this case objects with two-dimensional types $(i,j)$ are considered. Let $O_{ij}$ be the count of objects of type $(i,j)$ , i.e., $O_{ij}$ is the entry in the contingency table in row i and column j . Set

$N=\sum _{ij}O_{ij},\qquad {\hat {p}}_{ij}={\frac {O_{ij}}{N}}\,,\qquad {\hat {p}}_{i\bullet }={\frac {\sum _{j}O_{ij}}{N}}\,,\qquad {\hat {p}}_{\bullet j}={\frac {\sum _{i}O_{ij}}{N}}\,.$

Then the estimated expected count of objects of type $(i,j)$ assuming independence is given by

$E_{ij}=N{\hat {p}}_{i\bullet }{\hat {p}}_{\bullet j}.$

Finally, the *G*-test statistics in this case is given by

$G=2\sum _{ij}O_{ij}\ln \left({\frac {O_{ij}}{E_{ij}}}\right)$

Let $X,Y$ be random variables with joint distribution given by the empirical distribution ${\hat {p}}_{ij}$ of the contingency table, i.e.,

$P(X=i,Y=j)={\hat {p}}_{ij},\qquad P(X=i)={\hat {p}}_{i\bullet },\qquad P(Y=j)={\hat {p}}_{\bullet j}.$

Then the *G*-test statistics can be expressed in several alternative forms:

${\begin{aligned}G&=2N\cdot \sum _{ij}{{\hat {p}}_{ij}\left(\ln({\hat {p}}_{ij})-\ln({\hat {p}}_{i\bullet })-\ln({\hat {p}}_{\bullet j})\right)}\\&=2N\cdot {\Bigl (}H(X)+H(Y)-H(X,Y){\Bigr )}\\&=2N\cdot \operatorname {MI} (X,Y),\end{aligned}}$

where the entropies $H(X)$ and $H(Y)$ are given

$H(X)=-\sum _{i}{\hat {p}}_{i\bullet }\ln({\hat {p}}_{i\bullet }),\qquad H(Y)=-\sum _{j}{\hat {p}}_{\bullet j}\ln({\hat {p}}_{\bullet j})$

and the joint entropy $H(X,Y)$ is given by

$H(X,Y)=-\sum _{ij}{\hat {p}}_{ij}\ln({\hat {p}}_{ij})$

and the mutual information of X and Y is

$\operatorname {MI} (X,Y)=H(X)+H(Y)-H(X,Y).$

It can also be shown that the inverse document frequency weighting commonly used for text retrieval is an approximation of *G* applicable when the row sum for the query is much smaller than the row sum for the remainder of the corpus. Similarly, the result of Bayesian inference applied to a choice of single multinomial distribution for all rows of the contingency table taken together versus the more general alternative of a separate multinomial per row produces results very similar to the *G*-test statistic.

## Application

- The McDonald–Kreitman test in statistical genetics is an application of the *G*-test.
- Dunning introduced the test to the computational linguistics community where it is now widely used.
- The R-scape program (used by Rfam) uses *G*-test to detect co-variation between RNA sequence alignment positions.

## Statistical software

- In R fast implementations can be found in the AMR and Rfast packages. For the AMR package, the command is `g.test` which works exactly like `chisq.test` from base R. R also has the likelihood.test Archived 2013-12-16 at the Wayback Machine function in the Deducer Archived 2012-03-09 at the Wayback Machine package. **Note:** Fisher's *G*-test in the GeneCycle Package of the R programming language (`fisher.g.test`) does not implement the *G*-test as described in this article, but rather Fisher's exact test of Gaussian white-noise in a time series.
- Another R implementation to compute the *G*-test statistic and corresponding p-values is provided by the R package entropy. The commands are `Gstat` for the standard G statistic and the associated p-value and `Gstatindep` for the G statistic applied to comparing joint and product distributions to test independence.
- In SAS, one can conduct *G*-test by applying the `/chisq` option after the `proc freq`.
- In Stata, one can conduct a *G*-test by applying the `lr` option after the `tabulate` command.
- In Java, use `org.apache.commons.math3.stat.inference.GTest`.
- In Python, use `scipy.stats.power_divergence` with `lambda_=0`.
