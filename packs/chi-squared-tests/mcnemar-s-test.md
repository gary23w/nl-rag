---
title: "McNemar's test"
source: https://en.wikipedia.org/wiki/McNemar's_test
domain: chi-squared-tests
license: CC-BY-SA-4.0
tags: chi-squared test, contingency table, goodness of fit, G-test
fetched: 2026-07-02
---

# McNemar's test

**McNemar's test** is a statistical test used on paired nominal data. It is applied to 2 × 2 contingency tables with a dichotomous trait, with matched pairs of subjects, to determine whether the row and column marginal frequencies are equal (that is, whether there is "marginal homogeneity"). It is named after Quinn McNemar, who introduced it in 1947. An application of the test in genetics is the transmission disequilibrium test for detecting linkage disequilibrium.

The commonly used parameters to assess a diagnostic test in medical sciences are sensitivity and specificity. Sensitivity (or recall) is the ability of a test to correctly identify the people with disease. Specificity is the ability of the test to correctly identify those without the disease.

Now presume two tests are performed on the same group of patients. And also presume that these tests have identical sensitivity and specificity. In this situation one is carried away by these findings and presume that both the tests are equivalent. However this may not be the case. For this we have to study the patients with disease and patients without disease (by a reference test). We also have to find out where these two tests disagree with each other. This is precisely the basis of McNemar's test. This test compares the sensitivity and specificity of two diagnostic tests on the same group of patients.

## Definition

The test is applied to a 2 × 2 contingency table, which tabulates the outcomes of two tests on a sample of *N* subjects, as follows.

|   | Test 2 positive | Test 2 negative | Row total |
|---|---|---|---|
| Test 1 positive | *a* | *b* | *a* + *b* |
| Test 1 negative | *c* | *d* | *c* + *d* |
| Column total | *a* + *c* | *b* + *d* | *N* |

The null hypothesis of marginal homogeneity states that the two marginal probabilities for each outcome are the same, i.e. *p**a* + *p**b* = *p**a* + *p**c* and *p**c* + *p**d* = *p**b* + *p**d*.

Thus the null and alternative hypotheses are

${\begin{aligned}H_{0}&:~p_{b}=p_{c}\\H_{1}&:~p_{b}\neq p_{c}\end{aligned}}$

Here *p**a*, etc., denote the theoretical probability of occurrences in cells with the corresponding label.

The McNemar test statistic is:

$\chi ^{2}={(b-c)^{2} \over b+c}.$

Under the null hypothesis, with a sufficiently large number of discordants (cells b and c), $\chi ^{2}$ has a chi-squared distribution with 1 degree of freedom. If the $\chi ^{2}$ result is significant, this provides sufficient evidence to reject the null hypothesis, in favour of the alternative hypothesis that *pb* ≠ *pc*, which would mean that the marginal proportions are significantly different from each other.

### Variations

If either *b* or *c* is small (*b* + *c* < 25) then $\chi ^{2}$ is not well-approximated by the chi-squared distribution. An exact binomial test can then be used, where *b* is compared to a binomial distribution with size parameter *n* = *b* + *c* and *p* = 0.5. Effectively, the exact binomial test evaluates the imbalance in the discordants *b* and *c*. To achieve a two-sided P-value, the P-value of the extreme tail should be multiplied by 2. For *b* ≥ *c*:

${\text{exact-P-value}}=2\sum _{i=b}^{n}{n \choose i}0.5^{i}(1-0.5)^{n-i},$

which is simply twice the binomial distribution cumulative distribution function with *p* = 0.5 and *n* = *b* + *c*.

Edwards proposed the following continuity corrected version of the McNemar test to approximate the binomial exact-P-value:

$\chi ^{2}={(|b-c|-1)^{2} \over b+c}.$

The mid-P McNemar test (mid-p binomial test) is calculated by subtracting half the probability of the observed *b* from the exact one-sided P-value, then double it to obtain the two-sided mid-P-value:

${\text{mid-p-value}}=2\left(\sum _{i=b}^{n}{n \choose i}0.5^{i}(1-0.5)^{n-i}-0.5{n \choose b}0.5^{b}(1-0.5)^{n-b}\right)$

This is equivalent to:

${\text{mid-p-value}}={\text{exact-p-value}}-{n \choose b}0.5^{b}(1-0.5)^{n-b}$

where the second term is the binomial distribution probability mass function and *n* = *b* + *c*. Binomial distribution functions are readily available in common software packages and the McNemar mid-P test can easily be calculated.

The traditional advice has been to use the exact binomial test when *b* + *c* < 25. However, simulations have shown both the exact binomial test and the McNemar test with continuity correction to be overly conservative. When *b* + *c* < 6, the exact-P-value always exceeds the common significance level 0.05. The original McNemar test was most powerful, but often slightly liberal. The mid-P version was almost as powerful as the asymptotic McNemar test and was not found to exceed the nominal significance level.

## Examples

In the first example, a researcher attempts to determine if a drug has an effect on a particular disease. There are 314 patients, and they are diagnosed (disease: *present* or *absent*) before and after using the drug, which means that each sample can be described using 1 out of 4 combinations. Counts of individuals are given in the table, with the diagnosis (disease: *present* or *absent*) before treatment given in the rows, and the diagnosis after treatment in the columns. The test requires the same subjects to be included in the before-and-after measurements (matched pairs).

|   | **After:** present | **After:** absent | Row total |
|---|---|---|---|
| **Before:** present | 101 | 121 | 222 |
| **Before:** absent | 59 | 33 | 92 |
| Column total | 160 | 154 | 314 |

In this example, the null hypothesis of "marginal homogeneity" would mean there was no effect of the treatment. From the above data, the McNemar test statistic:

$\chi ^{2}={(121-59)^{2} \over {121+59}}$

has the value 21.35, which is extremely unlikely to form the distribution implied by the null hypothesis (*p* < 0.001). Thus the test provides strong evidence to reject the null hypothesis of no treatment effect.

A second example illustrates differences between the asymptotic McNemar test and alternatives. The data table is formatted as before, with different numbers in the cells:

|   | **After:** present | **After:** absent | Row total |
|---|---|---|---|
| **Before:** present | 59 | 6 | 65 |
| **Before:** absent | 16 | 80 | 96 |
| Column total | 75 | 86 | 161 |

With these data, the sample size (161 patients) is not small, however results from the McNemar test and other versions are different. The exact binomial test gives *p* = 0.053 and McNemar's test with continuity correction gives $\chi ^{2}$ = 3.68 and *p* = 0.055. The asymptotic McNemar's test gives $\chi ^{2}$ = 4.55 and *p* = 0.033 and the mid-P McNemar's test gives *p* = 0.035. Both the McNemar's test and mid-P version provide stronger evidence for a statistically significant treatment effect in this second example.

### Example implementation in Python

The following is an example implementation using the probability distributions provided by the SciPy package. The implementation uses the mid-P version if *b* + *c* < 25. Otherwise, it uses the asymptotic version, allowing for both the regular form and the continuity corrected form.

```mw
from scipy.stats import binom, chi2

def mcnemar(b: int, c: int, continuity_correction: bool = False) -> float:
    check_valid = lambda n: isinstance(n, int) or (isinstance(n, float) and n.is_integer())
    if not all(map(check_valid, [b, c])):
        raise ValueError("b and c must be integers!")
    n_min, n_max = sorted([b, c])
    corr = int(continuity_correction)
    if (n_min + n_max) < 25:
        pvalue = 2 * binom.cdf(n_min, n_min+n_max, 0.5) - binom.pmf(n_min, n_min+n_max, 0.5)
    else:
        chi2_statistic = (abs(n_min - n_max) - corr) ** 2 / (n_min + n_max)
        pvalue = chi2.sf(chi2_statistic, 1)
    return pvalue
```

It is also worth noting that the above implementation ensures that the smaller of *b*  and *c*  is passed as the first argument to the binomial probability distributions. See "Additional file 1" under the supplementary materials for further reading.

## Discussion

An interesting observation when interpreting McNemar's test is that the elements of the main diagonal do not contribute to the decision about whether (in the above example) pre- or post-treatment condition is more favourable. Thus, the sum *b* + *c* can be small and statistical power of the tests described above can be low even though the number of pairs *a* + *b* + *c* + *d* is large (see second example above).

An extension of McNemar's test exists in situations where independence does not necessarily hold between the pairs; instead, there are clusters of paired data where the pairs in a cluster may not be independent, but independence holds between different clusters. An example is analyzing the effectiveness of a dental procedure; in this case, a pair corresponds to the treatment of an individual tooth in patients who might have multiple teeth treated; the effectiveness of treatment of two teeth in the same patient is not likely to be independent, but the treatment of two teeth in different patients is more likely to be independent.

### Information in the pairings

In the 1970s, it was conjectured that retaining one's tonsils might protect against Hodgkin's lymphoma. John Rice wrote:

> 85 Hodgkin's patients [...] had a sibling of the same sex who was free of the disease and whose age was within 5 years of the patient's. These investigators presented the following table:
> 
> ${\begin{array}{c|c|c}\hline &{\text{Tonsillectomy}}&{\text{No tonsillectomy}}\\\hline {\text{Hodgkins}}&41&44\\\hline {\text{Control}}&33&52\end{array}}$
> 
> They calculated a chi-squared statistic [...] [they] had made an error in their analysis by ignoring the pairings.[...] [their] samples were not independent, because the siblings were paired [...] we set up a table that exhibits the pairings:
> 
> ${\begin{array}{cc}&{\text{Sibling}}\\{\text{Patient}}&{\begin{array}{c|c|c}\hline &{\text{No tonsillectomy}}&{\text{Tonsillectomy}}\\\hline {\text{No tonsillectomy}}&37&7\\\hline {\text{Tonsillectomy}}&15&26\end{array}}\end{array}}$

It is to the second table that McNemar's test can be applied. Notice that the sum of the numbers in the second table is 85—the number of *pairs* of siblings—whereas the sum of the numbers in the first table is twice as big, 170—the number of individuals. The second table gives more information than the first. The numbers in the first table can be found by using the numbers in the second table, but not vice versa. The numbers in the first table give only the marginal totals of the numbers in the second table. McNemar's test allows the 15 and 7 pairs where the siblings had previously had differing treatment to their tonsils to be compared, as being relevant to the hypothesis, while ignoring the less informative 37 and 26 where the siblings had previously both had the treatment or to their tonsils or neither had.

- The binomial sign test gives an exact test for the McNemar's test.
- The Cochran's Q test is an extension of the McNemar's test for more than two "treatments".
- The Liddell's exact test is an exact alternative to McNemar's test.
- The Stuart–Maxwell test is different generalization of the McNemar test, used for testing marginal homogeneity in a square table with more than two rows/columns.
- The Bhapkar's test (1966) is a more powerful alternative to the Stuart–Maxwell test, but it tends to be liberal. Competitive alternatives to the extant methods are available.
- The McNemar's test is a special case of the Cochran–Mantel–Haenszel test; it is equivalent to a CMH test with one stratum for each of the N pairs and, in each stratum, a 2x2 table showing the paired binary responses.
- Multinomial confidence intervals are used for matched pairs binary data.
