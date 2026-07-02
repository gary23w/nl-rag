---
title: "Fisher's exact test"
source: https://en.wikipedia.org/wiki/Fisher's_exact_test
domain: fishers-exact-test
license: CC-BY-SA-4.0
tags: Fisher exact test, hypergeometric distribution, Barnard test, exact test
fetched: 2026-07-02
---

# Fisher's exact test

**Fisher's exact test** (also the **Fisher–Irwin test**) is a statistical significance test used in the analysis of contingency tables. Although in practice it is employed when sample sizes are small, it is valid for all sample sizes. The test assumes that all row and column sums of the contingency table were fixed by design and tends to be conservative and underpowered outside of this setting. It is one of a class of exact tests, so called because the significance of the deviation from a null hypothesis (e.g., *p*-value) can be calculated exactly, rather than relying on an approximation that becomes exact in the limit as the sample size grows to infinity, as with many statistical tests.

The test is named after its inventor, Ronald Fisher, who is said to have devised the test following a comment from Muriel Bristol, who claimed to be able to detect whether the tea or the milk was added first to her cup. He tested her claim in the "lady tasting tea" experiment.

## Purpose and scope

The test is useful for categorical data that result from classifying objects in two different ways; it is used to examine the significance of the association (contingency) between the two kinds of classification. So in Fisher's original example, one criterion of classification could be whether milk or tea was put in the cup first; the other could be whether Bristol thinks that the milk or tea was put in first. We want to know whether these two classifications are associated—that is, whether Bristol really can tell whether milk or tea was poured in first. Most uses of the Fisher test involve, like this example, a 2 × 2 contingency table (discussed below). The *p*-value from the test is computed as if the margins of the table are fixed, i.e. as if, in the tea-tasting example, Bristol knows the number of cups with each treatment (milk or tea first) and will therefore provide guesses with the correct number in each category. As pointed out by Fisher, this leads under a null hypothesis of independence to a hypergeometric distribution of the numbers in the cells of the table. This setting is however rare in scientific practice and the test is conservative, when one or both margins are random variables themselves.

With large samples, a chi-squared test (or better yet, a G-test) can be used in this situation. However, the significance value it provides is only an approximation, because the sampling distribution of the test statistic that is calculated is only approximately equal to the theoretical chi-squared distribution. The approximation is poor when sample sizes are small, or the data are very unequally distributed among the cells of the table, resulting in the cell counts predicted on the null hypothesis (the "expected values") being low. The usual rule for deciding whether the chi-squared approximation is good enough is that the chi-squared test is not suitable when the expected values in any of the cells of a contingency table are below 5, or below 10 when there is only one degree of freedom (this rule is now known to be overly conservative). In fact, for small, sparse, or unbalanced data, the exact and asymptotic *p*-values can be quite different and may lead to opposite conclusions concerning the hypothesis of interest. In contrast the Fisher exact test is, as its name states, exact as long as the experimental procedure keeps the row and column totals fixed, and it can therefore be used regardless of the sample characteristics. It becomes difficult to calculate with large samples or well-balanced tables, but fortunately these are exactly the conditions where the chi-squared test is appropriate.

For hand calculations, the test is feasible only in the case of a 2 × 2 contingency table. However the principle of the test can be extended to the general case of an *m* × *n* table, and some statistical packages provide a calculation (sometimes using a Monte Carlo method to obtain an approximation) for the more general case.

The test can also be used to quantify the *overlap* between two sets. For example, in enrichment analyses in statistical genetics one set of genes may be annotated for a given phenotype and the user may be interested in testing the overlap of their own set with those. In this case a 2 × 2 contingency table may be generated and Fisher's exact test applied through identifying

1. Genes that are provided in both lists
2. Genes that are provided in the first list and not the second
3. Genes that are provided in the second list and not the first
4. Genes that are not provided in either list

The test assumes genes in either list are taken from a broader set of genes (e.g. all remaining genes). A *p*-value may then be calculated, summarizing the significance of the overlap between the two lists.

## Derivation

|   | Class I | Class II | *Row Total* |
|---|---|---|---|
| Blue | ***a*** | ***b*** | *a + b* |
| Red | ***c*** | ***d*** | *c + d* |
| *Column Total* | *a + c* | *b + d* | *a + b + c + d (=n)* |

Derivation

We set up the following probability model underlying Fisher's exact test.

Suppose we have ${\textstyle a+b}$ blue balls, and ${\textstyle c+d}$ red balls. We throw them together into a black box, shake well, then remove them one by one until we have pulled out exactly ${\textstyle a+c}$ balls. We call these balls "class I" and the ${\textstyle b+d}$ remaining balls "class II".

The question is to calculate the probability that exactly ${\textstyle a}$ blue balls are in class I. Every other entry in the table is fixed once we fill in one entry of the table.

Suppose we pretend that every ball is labelled, and before we start pulling out the balls, we permutate them uniformly randomly, then pull out the first ${\textstyle a+c}$ balls. This gives us ${\textstyle n!}$ possibilities.

Of these possibilities, we condition on the case where the first ${\textstyle a+c}$ balls contain exactly ${\textstyle a}$ blue balls. To count these possibilities, we do the following: first select uniformly at random a subset of size ${\textstyle a}$ among the ${\textstyle a+c}$ class-I balls with ${\textstyle {\binom {a+c}{a}}}$ possibilities, then select uniformly at random a subset of size ${\textstyle b}$ among the ${\textstyle b+d}$ class-II balls with ${\textstyle {\binom {b+d}{b}}}$ possibilities.

The two selected sets would be filled with blue balls. The rest would be filled with red balls.

Once we have selected the sets, we can populate them with an arbitrary ordering of the ${\textstyle a+b}$ blue balls. This gives us ${\textstyle (a+b)!}$ possibilities. Same for the red balls, with ${\textstyle (c+d)!}$ possibilities.

In full, we have ${\binom {a+c}{a}}{\binom {b+d}{b}}(a+b)!(c+d)!$ possibilities.

Thus the probability of this event is ${\frac {{\binom {a+c}{a}}{\binom {b+d}{b}}(a+b)!(c+d)!}{n!}}={\frac {{\binom {a+c}{a}}{\binom {b+d}{b}}}{\binom {n}{a+b}}}$

Another derivation:

Derivation

Suppose each blue ball and red ball has an equal and independent probability ${\textstyle p}$ of being in class I, and ${\textstyle 1-p}$ of being in class II. Then the number of class-I blue balls is binomially distributed. The probability there are exactly ${\textstyle a}$ of them is ${\textstyle {\binom {a+b}{a}}p^{a}(1-p)^{b}}$ , and the probability there are exactly ${\textstyle c}$ of red class I balls is ${\textstyle {\binom {c+d}{c}}p^{c}(1-p)^{d}}$ .

The probability that there are precisely ${\textstyle a+c}$ of class I balls, regardless of number of red or blue balls in it, is ${\textstyle {\binom {n}{a+c}}p^{a+c}(1-p)^{b+d}}$ .

Observe that conditional on the value of ${\textstyle a+c}$ every set of ${\textstyle a+c}$ balls has the same probability of being selected - independently of ${\textstyle p}$ (i.e. ${\textstyle a+c}$ is a sufficient statistic for ${\textstyle p}$ ), and so the data has the same distribution as in the original model where we just draw ${\textstyle a+c}$ balls.

Finally, we compute that conditional on having ${\textstyle a+c}$ class I balls, the conditional probability of having a table as shown is ${\frac {{\binom {a+c}{a}}{\binom {b+d}{b}}}{\binom {n}{a+b}}}.$

## Example

For example, a sample of teenagers might be divided into male and female on one hand and those who are and are not currently studying for a statistics exam on the other. For example, we hypothesize that the proportion of studying students is higher among the women than among the men, and we want to test whether any difference in proportions that we observe is significant.

The data might look like this:

|   | Men | Women | *Row total* |
|---|---|---|---|
| Studying | **1** | **9** | *10* |
| Not-studying | **11** | **3** | *14* |
| *Column total* | *12* | *12* | *24* |

The question we ask about these data is: Knowing that 10 of these 24 teenagers are studying and that 12 of the 24 are female, and assuming the null hypothesis that men and women are equally likely to study, what is the probability that these 10 teenagers who are studying would be so unevenly distributed between the women and the men? If we were to choose 10 of the teenagers at random, what is the probability that 9 or more of them would be among the 12 women and only 1 or fewer from among the 12 men?

### First example

Before we proceed with the Fisher test, we first introduce some notations. We represent the cells by the letters *a, b, c* and *d*, call the totals across rows and columns *marginal totals*, and represent the grand total by *n*. So the table now looks like this:

|   | Men | Women | *Row Total* |
|---|---|---|---|
| Studying | ***a*** | ***b*** | *a + b* |
| Non-studying | ***c*** | ***d*** | *c + d* |
| *Column Total* | *a + c* | *b + d* | *a + b + c + d (=n)* |

Fisher showed that conditional on the margins of the table, *a* is distributed as a hypergeometric distribution with *a+c* draws from a population with *a+b* successes and *c+d* failures. The probability of obtaining such set of values is given by:

$p={\frac {\displaystyle {{a+b} \choose {a}}\displaystyle {{c+d} \choose {c}}}{\displaystyle {{n} \choose {a+c}}}}={\frac {\displaystyle {{a+b} \choose {b}}\displaystyle {{c+d} \choose {d}}}{\displaystyle {{n} \choose {b+d}}}}={\frac {(a+b)!~(c+d)!~(a+c)!~(b+d)!}{a!~~b!~~c!~~d!~~n!}}$

where ${\tbinom {n}{k}}$ is the binomial coefficient and the symbol ! indicates the factorial operator. This can be seen as follows. If the marginal totals (i.e. $a+b$ , $c+d$ , $a+c$ , and $b+d$ ) are known, only a single degree of freedom is left: the value e.g. of a suffices to deduce the other values. Now, $p=p(a)$ is the probability that a elements are positive in a random selection (without replacement) of $a+c$ elements from a larger set containing n elements in total out of which $a+b$ are positive, which is precisely the definition of the hypergeometric distribution.

With the data above (using the first of the equivalent forms), this gives:

$p={{\tbinom {10}{1}}{\tbinom {14}{11}}}/{\tbinom {24}{12}}={\tfrac {10!~14!~12!~12!}{1!~9!~11!~3!~24!}}\approx 0.001346076$

### Second example

The formula above gives the exact hypergeometric probability of observing this particular arrangement of the data, assuming the given marginal totals, on the null hypothesis that men and women are equally likely to be studiers. To put it another way, if we assume that the probability that a man is a studier is ${\mathfrak {p}}$ , the probability that a woman is a studier is also ${\mathfrak {p}}$ , and we assume that both men and women enter our sample independently of whether or not they are studiers, then this hypergeometric formula gives the conditional probability of observing the values *a, b, c, d* in the four cells, conditionally on the observed marginals (i.e., assuming the row and column totals shown in the margins of the table are given). This remains true even if men enter our sample with different probabilities than women. The requirement is merely that the two classification characteristics—gender, and studier (or not)—are not associated.

For example, suppose we knew probabilities $P,Q,{\mathfrak {p,q}}$ with $P+Q={\mathfrak {p}}+{\mathfrak {q}}=1$ such that (male studier, male non-studier, female studier, female non-studier) had respective probabilities $(P{\mathfrak {p}},P{\mathfrak {q}},Q{\mathfrak {p}},Q{\mathfrak {q}})$ for each individual encountered under our sampling procedure. Then still, were we to calculate the distribution of cell entries conditional given marginals, we would obtain the above formula in which neither ${\mathfrak {p}}$ nor P occurs. Thus, we can calculate the exact probability of any arrangement of the 24 teenagers into the four cells of the table, but Fisher showed that to generate a significance level, we need consider only the cases where the marginal totals are the same as in the observed table, and among those, only the cases where the arrangement is as extreme as the observed arrangement, or more so. (Barnard's test relaxes this constraint on one set of the marginal totals.) In the example, there are 11 such cases. Of these only one is more extreme in the same direction as our data; it looks like this:

|   | Men | Women | *Row Total* |
|---|---|---|---|
| Studying | **0** | **10** | *10* |
| Non-studying | **12** | **2** | *14* |
| *Column Total* | *12* | *12* | *24* |

For this table (with extremely unequal studying proportions) the probability is ${p={\tbinom {10}{0}}{\tbinom {14}{12}}}/{\tbinom {24}{12}}\approx 0.000033652$ .

### p-value tests

In order to calculate the significance of the observed data, i.e. the total probability of observing data as extreme or more extreme if the null hypothesis is true, we have to calculate the values of *p* for both these tables, and add them together. This gives a one-tailed test, with *p* approximately 0.001346076 + 0.000033652 = 0.001379728. For example, in the R statistical computing environment, this value can be obtained as `fisher.test(rbind(c(1,9),c(11,3)), alternative="less")$p.value`, or in Python, using `scipy.stats.fisher_exact(table=[[1,9],[11,3]], alternative="less")` (where one receives both the prior odds ratio and the *p*-value). This value can be interpreted as the sum of evidence provided by the observed data—or any more extreme table—for the null hypothesis (that there is no difference in the proportions of studiers between men and women). The smaller the value of *p*, the greater the evidence for rejecting the null hypothesis; so here the evidence is strong that men and women are not equally likely to be studiers.

For a two-tailed test we must also consider tables that are equally extreme, but in the opposite direction. Unfortunately, classification of the tables according to whether or not they are 'as extreme' is problematic. An approach used by the `fisher.test` function in R is to compute the *p*-value by summing the probabilities for all tables with probabilities less than or equal to that of the observed table. In the example here, the 2-sided *p*-value is twice the 1-sided value—but in general these can differ substantially for tables with small counts, unlike the case with test statistics that have a symmetric sampling distribution.

## Applications

Fisher's exact test is a standard tool in genomics for identifying statistically under- or over-represented sets of genes. For example, sets of differentially expressed genes can be tested for significant overlap with predefined functional categories such as Gene Ontology terms, providing insight into biological processes that may be implicated in an experiment.

In text analytics, Fisher's exact test has been used to quantify whether a given word is statistically associated with a particular document within a corpus. The negative logarithm of the resulting *p*-value has been shown to be closely related to the TF–IDF term-weighting scheme from information retrieval.

## Controversies

Fisher's test gives exact *p*-values, but some authors have argued that it is conservative, i.e. that its actual rejection rate is below the nominal significance level. The apparent contradiction stems from the combination of a discrete statistic with fixed significance levels. Consider the following proposal for a significance test at the 5%-level: reject the null hypothesis for each table to which Fisher's test assigns a *p*-value equal to or smaller than 5%. Because the set of all tables is discrete, there may not be a table for which equality is achieved. If $\alpha _{e}$ is the largest *p*-value smaller than 5% which can actually occur for some table, then the proposed test effectively tests at the $\alpha _{e}$ -level. For small sample sizes, $\alpha _{e}$ might be significantly lower than 5%. While this effect occurs for any discrete statistic (not just in contingency tables, or for Fisher's test), it has been argued that the problem is compounded by the fact that Fisher's test conditions on the marginals. To avoid the problem, many authors discourage the use of fixed significance levels when dealing with discrete problems.

The decision to condition on the margins of the table is also controversial. The *p*-values derived from Fisher's test come from the distribution that conditions on the margin totals. In this sense, the test is exact only for the conditional distribution and not the original table where the margin totals may change from experiment to experiment. It is possible to obtain an exact *p*-value for the 2×2 table when the margins are not held fixed. Barnard's test, for example, allows for random margins. However, some authors (including, later, Barnard himself) have criticized Barnard's test based on this property. They argue that the marginal success total is an (almost) ancillary statistic, containing (almost) no information about the tested property.

The act of conditioning on the marginal success rate from a 2×2 table can be shown to ignore some information in the data about the unknown odds ratio. The argument that the marginal totals are (almost) ancillary implies that the appropriate likelihood function for making inferences about this odds ratio should be conditioned on the marginal success rate. Whether this lost information is important for inferential purposes is the essence of the controversy.

## Alternatives

An alternative exact test, Barnard's exact test, has been developed and proponents of it suggest that this method is more powerful, particularly in 2×2 tables. Furthermore, Boschloo's test is an exact test that is uniformly more powerful than Fisher's exact test by construction.

Most modern statistical packages will calculate the significance of Fisher tests, in some cases even where the chi-squared approximation would also be acceptable. The actual computations as performed by statistical software packages will as a rule differ from those described above, because numerical difficulties may result from the large values taken by the factorials. A simple, somewhat better computational approach relies on a gamma function or log-gamma function, but methods for accurate computation of hypergeometric and binomial probabilities remains an active research area.

For stratified categorical data the Cochran–Mantel–Haenszel test must be used instead of Fisher's test.

Choi et al. propose a *p*-value derived from the likelihood ratio test based on the conditional distribution of the odds ratio given the marginal success rate. This *p*-value is inferentially consistent with classical tests of normally distributed data as well as with likelihood ratios and support intervals based on this conditional likelihood function. It is also readily computable.
