---
title: "Barnard's test"
source: https://en.wikipedia.org/wiki/Barnard's_test
domain: fishers-exact-test
license: CC-BY-SA-4.0
tags: Fisher exact test, hypergeometric distribution, Barnard test, exact test
fetched: 2026-07-02
---

# Barnard's test

In statistics, **Barnard’s test** is an exact test used in the analysis of 2 × 2 contingency tables with one margin fixed. Barnard’s tests are really a class of hypothesis tests, also known as unconditional exact tests for two independent binomials. These tests examine the association of two categorical variables and are often a more powerful alternative than Fisher's exact test for 2 × 2 contingency tables. While first published in 1945 by G.A. Barnard, the test did not gain popularity due to the computational difficulty of calculating the p value and Fisher’s specious disapproval. Nowadays, even for sample sizes *n* ~ 1 million, computers can often implement Barnard’s test in a few seconds or less.

## Purpose and scope

Barnard’s test is used to test the independence of rows and columns in a 2 × 2 contingency table. The test assumes each response is independent. Under independence, there are three types of study designs that yield a 2 × 2 table, and Barnard's test applies to the second type.

To distinguish the different types of designs, suppose a researcher is interested in testing whether a novel treatment quickly heals an infection.

1. One possible study design would be to sample 100 infected subjects, and for each subject see if they got the novel treatment or the old, standard treatment, and see if the infection is still present after a set time. This type of design is common in cross-sectional studies, or ‘field observations’ such as epidemiology.
2. Another possible study design would be to give 50 infected subjects the novel treatment, 50 infected subjects the standard treatment, and see if the infection is still present after a set time. This type of design is common in clinical trials.
3. The final possible study design would be to give 50 infected subjects the novel treatment, 50 infected subjects the standard treatment, and stop the experiment once a pre-determined number of subjects has healed from the infection. This type of design is rare, but has the same structure as the *lady tasting tea* study that led R.A. Fisher to create Fisher's exact test.

Although the results of each design of experiment can be laid out in nearly identical-appearing 2 × 2 tables, their statistics are different, and hence the criteria for a "significant" result are different for each:

1. The probability of a 2 × 2 table under the first study design is given by the multinomial distribution; where the total number of samples taken is the only statistical constraint. This is a form of uncontrolled experiment, or "field observation", where experimenter simply "takes the data as it comes".
2. The second study design is given by the product of two independent binomial distributions; the totals in one of the margins (either the row totals or the column totals) are constrained by the experimental design, but the totals in other margin are free. This is by far the most common form of experimental design, where the experimenter constrains part of the experiment, say by assigning half of the subjects to be provided with a new medicine and the other half to receive an older, conventional medicine, but has no control over the numbers of individuals in each controlled category who either recover or succumb to the illness.
3. The third design is given by the hypergeometric distribution; where both the total numbers in each column and row are constrained. For example an individual is allowed to taste 8 cups of soda, but must assign four to each category "brand X" and "brand Y", so that both the row totals and the column totals are constrained to four.

The operational difference between Barnard’s exact test and Fisher’s exact test is how they handle the nuisance parameter(s) of the common success probability, when calculating the p value. Fisher's exact test avoids estimating the nuisance parameter(s) by conditioning on both margins, an approximately ancillary statistic that constrains the possible outcomes. The problem with that Fisher's procedure is that it excludes some of the outcomes which are possibilities when there is no constraint on the total numbers in each column and row. Barnard’s test considers all legitimate possible values of the nuisance parameter(s) and chooses the value(s) that maximizes the p value. The theoretical difference between the tests is that Barnard’s test uses the double-binomially distributed, whereas Fisher’s test, because of the conditioning, uses the hypergeometric, which means that the estimated p values it produces are not correct; in general they are too large, making Fisher's test too 'conservative': Prone to unnecessary type II errors (excessive numbers of false negatives). However, even when the data come from double-binomial distribution, the conditioning (that leads to using the hypergeometric distribution for calculating the Fisher's exact p value) produces a valid test, if one accepts that Fisher's test will necessarily miss some positive results. Barnard's test is not biased in this way, and is more suitable for a broader range of experiment types, including those which are most common, in which there is no experimental constraint on one of either the row sum or the column sum of the table.

Both tests bound the type I error rate at the α level, and hence are technically 'valid'. However, for the design of almost all actually conducted experiments Barnard’s test is much more powerful than Fisher’s test, because it considers more ‘as or more extreme’ tables, by *not* imposing a constraint ('conditioning') on the second margin, which the procedure for Fisher’s test requires and is not often used in experimental designs. In fact, a variant of Barnard’s test, called Boschloo's test, is uniformly more powerful than Fisher’s test. Barnard’s test has been used alongside Fisher's exact test in project management research.

## Criticisms

Under pressure from Fisher, Barnard retracted his test in a published paper, however many researchers prefer Barnard’s exact test over Fisher's exact test for analyzing 2 × 2 contingency tables, since its statistics are more powerful for the vast majority of experimental designs, whereas Fisher’s exact test statistics are conservative, meaning the significance shown by its p values are too high, leading the experimenter to dismiss as insignificant results that would be statistically significant using the double-binomial statistics of Barnard's tests rather than the often overly-conservative hypergeometric statistics of Fisher's 'exact' test. Barnard's tests are not appropriate in the rare case of an experimental design that constrains both marginal results (e.g. ‘taste tests’); although rare, experimentally imposed constraints on both marginal totals make the true sampling distribution for the table hypergeometric.

Barnard's test can be applied to larger tables, but the computation time increases and the power advantage quickly decreases. It remains unclear which test statistic is preferred when implementing Barnard's test; however, most test statistics yield uniformly more powerful tests than Fisher's exact test.
