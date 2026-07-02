---
title: "Data dredging"
source: https://en.wikipedia.org/wiki/Data_dredging
domain: multiple-comparisons
license: CC-BY-SA-4.0
tags: multiple comparisons, family-wise error rate, false discovery rate, closed testing
fetched: 2026-07-02
---

# Data dredging

**Data dredging,** also known as **data snooping** or ***p*-hacking**, is the misuse of data analysis to find patterns in data that can be presented as statistically significant, thus dramatically increasing and understating the risk of false positives. This is done by performing many statistical tests on the data and only reporting those that come back with significant results. Thus data dredging is also often a misused or misapplied form of data mining.

The process of data dredging involves testing multiple hypotheses using a single data set by exhaustively searching—perhaps for combinations of variables that might show a correlation, and perhaps for groups of cases or observations that show differences in their mean or in their breakdown by some other variable.

Conventional tests of statistical significance are based on the probability that a particular result would arise if chance alone were at work, and necessarily accept some risk of mistaken conclusions of a certain type (mistaken rejections of the null hypothesis). This level of risk is called the *significance*. When large numbers of tests are performed, some produce false results of this type; hence 5% of randomly chosen hypotheses might be (erroneously) reported to be statistically significant at the 5% significance level, 1% might be (erroneously) reported to be statistically significant at the 1% significance level, and so on, by chance alone. When enough hypotheses are tested, it is virtually certain that some will be reported to be statistically significant (even though this is misleading), since almost every data set with any degree of randomness is likely to contain (for example) some spurious correlations. If they are not cautious, researchers using data mining techniques can be easily misled by these results. The term *p-hacking* (in reference to *p*-values) was coined in a 2014 paper by the three researchers behind the blog Data Colada, which has been focusing on uncovering such problems in social sciences research.

Data dredging is an example of disregarding the multiple comparisons problem. One form is when subgroups are compared without alerting the reader to the total number of subgroup comparisons examined. When misused it is a questionable research practice that can undermine scientific integrity.

## Types

### Drawing conclusions from data

The conventional statistical hypothesis testing procedure using frequentist probability is to formulate a research hypothesis, such as "people in higher social classes live longer", then collect relevant data. Lastly, a statistical significance test is carried out to see how likely the results are by chance alone (also called testing against the null hypothesis).

A key point in proper statistical analysis is to test a hypothesis with evidence (data) that was not used in constructing the hypothesis. This is critical because every data set contains some patterns due entirely to chance. If the hypothesis is not tested on a different data set from the same statistical population, it is impossible to assess the likelihood that chance alone would produce such patterns.

For example, flipping a coin five times with a result of 2 heads and 3 tails might lead one to hypothesize that the coin favors tails by 3/5 to 2/5. If this hypothesis is then tested on the existing data set, it is confirmed, but the confirmation is meaningless. The proper procedure would have been to form in advance a hypothesis of what the tails probability is, and then throw the coin various times to see if the hypothesis is rejected or not. If three tails and two heads are observed, another hypothesis, that the tails probability is 3/5, could be formed, but it could only be tested by a new set of coin tosses. The statistical significance under the incorrect procedure is completely spurious—significance tests do not protect against data dredging.

### Optional stopping

Optional stopping is a practice where one collects data until some stopping criteria is reached. While it is a valid procedure, it is easily misused. The problem is that *p*-value of an optionally stopped statistical test is larger than what it seems. Intuitively, this is because the *p*-value is supposed to be the sum of all events at least as rare as what is observed. With optional stopping, there are even rarer events that are difficult to account for, i.e., not triggering the optional stopping rule, and collect even more data, before stopping. Neglecting these events leads to a *p*-value that's too low. In fact, if the null hypothesis is true, then *any* significance level can be reached if one is allowed to keep collecting data and stop when the desired *p*-value (calculated as if one has always been planning to collect exactly this much data) is obtained. For a concrete example of testing for a fair coin, see *p*-value § Optional stopping.

Or, more succinctly, the proper calculation of *p*-value requires accounting for counterfactuals, that is, what the experimenter *could* have done in reaction to data that *might* have been. Accounting for what might have been is hard, even for honest researchers. One benefit of preregistration is to account for all counterfactuals, allowing the *p*-value to be calculated correctly.

The problem of early stopping is not just limited to researcher misconduct. There is often pressure to stop early if the cost of collecting data is high. Some animal ethics boards even mandate early stopping if the study obtains a significant result midway.

### Post-hoc data replacement

If data is removed *after* some data analysis is already done on it, such as on the pretext of "removing outliers", then it would increase the false positive rate. Outliers should only be removed from a data set after proper identification and agreement or concurrence that there is special cause variation responsible for the unusual data. Replacing "outliers" by replacement data increases the false positive rate further.

### Post-hoc grouping

If a dataset contains multiple features, then one or more of the features can be used as grouping, and potentially create a statistically significant result. For example, if a dataset of patients records their age and sex, then a researcher can consider grouping them by age and check if the illness recovery rate is correlated with age. If it does not work, then the researcher might check if it correlates with sex. If not, then perhaps it correlates with age after controlling for sex, etc. The number of possible groupings grows exponentially with the number of features.

### Hypothesis suggested by non-representative data

Suppose that a study of a random sample of people includes exactly two people with a birthday of August 7: Mary and John. Someone engaged in data dredging might try to find additional similarities between Mary and John. By going through hundreds or thousands of potential similarities between the two, each having a low probability of being true, an unusual similarity can almost certainly be found. Perhaps John and Mary are the only two people in the study who switched minors three times in college. A hypothesis, biased by data dredging, could then be "people born on August 7 have a much higher chance of switching minors more than twice in college."

The data itself taken out of context might be seen as strongly supporting that correlation, since no one with a different birthday had switched minors three times in college. However, if (as is likely) this is a spurious hypothesis, this result will most likely not be reproducible; any attempt to check if others with an August 7 birthday have a similar rate of changing minors will most likely get contradictory results almost immediately.

### Systematic bias

Bias is a systematic error in the analysis. For example, doctors directed HIV patients at high cardiovascular risk to a particular HIV treatment, abacavir, and lower-risk patients to other drugs, preventing a simple assessment of abacavir compared to other treatments. An analysis that did not correct for this bias unfairly penalized abacavir, since its patients were more high-risk so more of them had heart attacks. This problem can be very severe, for example, in the observational study.

Missing factors, unmeasured confounders, and loss to follow-up can also lead to bias. By selecting papers with significant *p*-values, negative studies are selected against, which is publication bias. This is also known as *file drawer bias*, because less significant *p*-value results are left in the file drawer and never published.

### Multiple modelling

Another aspect of the conditioning of statistical tests by knowledge of the data can be seen while using the system or machine analysis and linear regression to observe the frequency of data. A crucial step in the process is to decide which covariates to include in a relationship explaining one or more other variables. There are both statistical (see stepwise regression) and substantive considerations that lead the authors to favor some of their models over others, and there is a liberal use of statistical tests. However, to discard one or more variables from an explanatory relation on the basis of the data means one cannot validly apply standard statistical procedures to the retained variables in the relation as though nothing had happened. In the nature of the case, the retained variables have had to pass some kind of preliminary test (possibly an imprecise intuitive one) that the discarded variables failed. In 1966, Selvin and Stuart compared variables retained in the model to the fish that don't fall through the net—in the sense that their effects are bound to be bigger than those that do fall through the net. Not only does this alter the performance of all subsequent tests on the retained explanatory model, but it may also introduce bias and alter mean square error in estimation.

## Examples

### In meteorology and epidemiology

In meteorology, hypotheses are often formulated using weather data up to the present and tested against future weather data, which ensures that, even subconsciously, future data could not influence the formulation of the hypothesis. Of course, such a discipline necessitates waiting for new data to come in, to show the formulated theory's predictive power versus the null hypothesis. This process ensures that no one can accuse the researcher of hand-tailoring the predictive model to the data on hand, since the upcoming weather is not yet available.

As another example, suppose that observers note that a particular town appears to have a cancer cluster, but lack a firm hypothesis of why this is so. However, they have access to a large amount of demographic data about the town and surrounding area, containing measurements for the area of hundreds or thousands of different variables, mostly uncorrelated. Even if all these variables are independent of the cancer incidence rate, it is highly likely that at least one variable correlates significantly with the cancer rate across the area. While this may suggest a hypothesis, further testing using the same variables but with data from a different location is needed to confirm. Note that a *p*-value of 0.01 suggests that 1% of the time a result at least that extreme would be obtained by chance; if hundreds or thousands of hypotheses (with mutually relatively uncorrelated independent variables) are tested, then one is likely to obtain a *p*-value less than 0.01 for many null hypotheses.

### In pharmaceutical research

The problem of *p*-hacking is worryingly common in pharmaceutical drug development and research. Drugs with no discernible effect can be shown to have a statistically significant effect when hundreds, if not thousands, of analyses are run – on the same data – using different target groups, primary outcome measures, age adjustments, and myriad other variables which can be dropped or selected to obtain a meaningful result. Even where a drug has no measurable effect whatsoever, if enough analyses are run, a strong, statistically meaningful effect will be found (e.g., "the drug significantly improved memory function in women over 40", where memory function was not the original primary outcome being assessed). This does not require any data falsification, nor for inconvenient results to be omitted. Instead, *p*-hacking relies simply on repeated analyses of the same data until the researcher finds the correlation with the "best" *p*-value. The analysis is fine-tuned to the data, rather than the data being manipulated in any way.

## Appearance in media

One example is the chocolate weight loss hoax study conducted by journalist John Bohannon, who explained publicly in a *Gizmodo* article that the study was deliberately conducted fraudulently as a social experiment. This study was widespread in many media outlets around 2015, with many people believing the claim that eating a chocolate bar every day would cause them to lose weight, against their better judgement. This study was published in the Institute of Diet and Health. According to Bohannon, to reduce the *p*-value to below 0.05, taking 18 different variables into consideration when testing was crucial.

## Remedies

While looking for patterns in data is legitimate, applying a statistical test of significance or hypothesis test to the same data until a pattern emerges is prone to abuse. One way to construct hypotheses while avoiding data dredging is to conduct randomized out-of-sample tests. The researcher collects a data set, then randomly partitions it into two subsets, A and B. Only one subset—say, subset A—is examined for creating hypotheses. Once a hypothesis is formulated, it must be tested on subset B, which was not used to construct the hypothesis. Only where B also supports such a hypothesis is it reasonable to believe the hypothesis might be valid. (This is a simple type of cross-validation and is often termed training-test or split-half validation.)

Another remedy for data dredging is to record the number of all significance tests conducted during the study and simply divide one's criterion for significance (alpha) by this number; this is the Bonferroni correction. However, this is a very conservative metric. A family-wise alpha of 0.05, divided in this way by 1,000 to account for 1,000 significance tests, yields a very stringent per-hypothesis alpha of 0.00005. Methods particularly useful in analysis of variance, and in constructing simultaneous confidence bands for regressions involving basis functions are Scheffé's method and, if the researcher has in mind only pairwise comparisons, the Tukey method. To avoid the extreme conservativeness of the Bonferroni correction, more sophisticated selective inference methods are available. The most common selective inference method is the use of Benjamini and Hochberg's false discovery rate controlling procedure: it is a less conservative approach that has become a popular method for control of multiple hypothesis tests.

When neither approach is practical, one can make a clear distinction between data analyses that are confirmatory and analyses that are exploratory. Statistical inference is appropriate only for the former.

Ultimately, the statistical significance of a test and the statistical confidence of a finding are joint properties of data and the method used to examine the data. Thus, if someone says that a certain event has probability of 20% ± 2% 19 times out of 20, this means that if the probability of the event is estimated *by the same method* used to obtain the 20% estimate, the result is between 18% and 22% with probability 0.95. No claim of statistical significance can be made by only looking, without due regard to the method used to assess the data.

Academic journals increasingly shift to the registered report format, which aims to counteract very serious issues such as data dredging and HARKing, which have made theory-testing research very unreliable. For example, *Nature Human Behaviour* has adopted the registered report format, as it "shift[s] the emphasis from the results of research to the questions that guide the research and the methods used to answer them". The *European Journal of Personality* defines this format as follows: "In a registered report, authors create a study proposal that includes theoretical and empirical background, research questions/hypotheses, and pilot data (if available). Upon submission, this proposal will then be reviewed prior to data collection, and if accepted, the paper resulting from this peer-reviewed procedure will be published, regardless of the study outcomes."

Methods and results can also be made publicly available, as in the open science approach, making it yet more difficult for data dredging to take place.
