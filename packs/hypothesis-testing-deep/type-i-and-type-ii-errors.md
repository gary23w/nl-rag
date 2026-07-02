---
title: "Type I and type II errors"
source: https://en.wikipedia.org/wiki/Type_I_and_type_II_errors
domain: hypothesis-testing-deep
license: CC-BY-SA-4.0
tags: hypothesis test, null hypothesis, statistical power, likelihood ratio test
fetched: 2026-07-02
---

# Type I and type II errors

**Type I error**, or a **false positive**, is the incorrect rejection of a true null hypothesis in statistical hypothesis testing. A **type II error**, or a **false negative**, is the incorrect acceptance of a false null hypothesis.

An analysis commits a Type I error when some baseline assumption is incorrectly rejected because of new, misleading information. Meanwhile, a Type II error is made when such an assumption is maintained, due to flawed or insufficient data, when better measurements would have shown it to be untrue. For example, in the context of medical testing, if we consider the null hypothesis to be "This patient does not have the disease," a diagnosis that the disease is present when it is not is a Type I error, while a diagnosis that the patient does not have the disease when it is present would be a Type II error. The manner in which a null hypothesis frames contextually default expectations influences the specific ways in which type I errors and type II errors manifest, and this varies by context and application. Generally the risk of such errors cannot be entirely eliminated, only traded-off between the two types, by for example changing the significance threshold.

Knowledge of type I errors and type II errors is applied widely in fields of medical science, biometrics and computer science. Minimising these errors is an object of study within statistical theory, though complete elimination of either is impossible when relevant outcomes are not determined by known, observable, causal processes.

## Definition

### Statistical background

In statistical test theory, the notion of a statistical error is an integral part of hypothesis testing. The test goes about choosing about two competing propositions called null hypothesis, denoted by ${\textstyle H_{0}}$ and alternative hypothesis, denoted by ${\textstyle H_{1}}$ . This is conceptually similar to the judgement in a court trial. The null hypothesis corresponds to the position of the defendant: just as he is presumed to be innocent until proven guilty, so is the null hypothesis presumed to be true until the data provide convincing evidence against it. The alternative hypothesis corresponds to the position against the defendant. Specifically, the null hypothesis also involves the absence of a difference or the absence of an association. Thus, the null hypothesis can never be that there is a difference or an association.

If the result of the test corresponds with reality, then a correct decision has been made. However, if the result of the test does not correspond with reality, then an error has occurred. There are two situations in which the decision is wrong. The null hypothesis may be true, whereas we reject ${\textstyle H_{0}}$ . On the other hand, the alternative hypothesis ${\textstyle H_{1}}$ may be true, whereas we do not reject ${\textstyle H_{0}}$ . Two types of error are distinguished: type I error and type II error.

### Type I error

The first kind of error is the mistaken rejection of a null hypothesis as the result of a test procedure. This kind of error is called a type I error (false positive) and is sometimes called an error of the first kind. In terms of the courtroom example, a type I error corresponds to convicting an innocent defendant.

### Type II error

The second kind of error is the failure to reject the null hypothesis as the result of a test procedure. This sort of error is called a type II error (false negative) and is also referred to as an error of the second kind. In terms of the courtroom example, a type II error corresponds to acquitting a criminal.

### Crossover error rate

The crossover error rate (CER) is the point at which type I errors and type II errors are equal. A system with a lower CER value provides more accuracy than a system with a higher CER value. With all else being equal, having the rate of type I errors and type II errors being equal (i.e. the CER) will result in the lowest overall error rate.

### False positive and false negative

In terms of false positives and false negatives, a positive result corresponds to rejecting the null hypothesis, while a negative result corresponds to failing to reject the null hypothesis; "false" means the conclusion drawn is incorrect. Thus, a type I error is equivalent to a false positive, and a type II error is equivalent to a false negative.

### Table of error types

Tabulated relations between truth/falseness of the null hypothesis and outcomes of the test:

| Table of error types | Null hypothesis ( ${\textstyle {\boldsymbol {H_{0}}}}$ ) is |   |   |
|---|---|---|---|
| True | False |   |   |
| Decision about null hypothesis ( ${\textstyle {\boldsymbol {H_{0}}}}$ ) | Not reject | Correct inference (true negative) (probability = ${\textstyle 1-\alpha }$ ) | Type II error (false negative) (probability = ${\textstyle \beta }$ ) |
| Reject | Type I error (false positive) (probability = *${\textstyle \alpha }$*) | Correct inference (true positive) (probability = ${\textstyle 1-\beta }$ ) |   |

## Error rate

A perfect test would have zero false positives and zero false negatives. However, statistical methods are probabilistic, and it cannot be known for certain whether statistical conclusions are correct. Whenever there is uncertainty, there is the possibility of making an error. Considering this, all statistical hypothesis tests have a probability of making type I and type II errors.

- The type I error rate is the probability of rejecting the null hypothesis given that it is true. The test is designed to keep the type I error rate below a prespecified bound called the significance level, usually denoted by the Greek letter α (alpha) and is also called the alpha level. Usually, the significance level is set to 0.05 (5%), implying that it is acceptable to have a 5% probability of incorrectly rejecting the true null hypothesis.
- The rate of the type II error is denoted by the Greek letter β (beta) and related to the power of a test, which equals 1−β.

These two types of error rates are traded off against each other: for any given sample set, the effort to reduce one type of error generally results in increasing the other type of error.

### The quality of hypothesis test

The same idea can be expressed in terms of the rate of correct results and therefore used to minimize error rates and improve the quality of hypothesis test. To reduce the probability of committing a type I error, making the alpha value more stringent is both simple and efficient. For example, setting the alpha value at 0.01, instead of 0.05. To decrease the probability of committing a type II error, which is closely associated with analyses' power, either increasing the test's sample size or relaxing the alpha level, ex. setting the alpha level to 0.1 instead of 0.05, could increase the analyses' power. A test statistic is robust if the type I error rate is controlled.

Varying different threshold (cut-off) values could also be used to make the test either more specific or more sensitive, which in turn elevates the test quality. For example, imagine a medical test, in which an experimenter might measure the concentration of a certain protein in the blood sample. The experimenter could adjust the threshold (black vertical line in the figure) and people would be diagnosed as having diseases if any number is detected above this certain threshold. According to the image, changing the threshold would result in changes in false positives and false negatives, corresponding to movement on the curve.

## Example

Since in a real experiment it is impossible to avoid all type I and type II errors, it is important to consider the amount of risk one is willing to take to falsely reject H0 or accept H0. The solution to this question would be to report the p-value or significance level α of the statistic. For example, if the p-value of a test statistic result is 0.0596, then there is a probability of 5.96% that we falsely reject H0 given it is true. Or, if we say, the statistic is performed at level α, like 0.05, then we allow to falsely reject H0 at 5%. A significance level α of 0.05 is relatively common, but there is no general rule that fits all scenarios.

### Vehicle speed measuring

The speed limit of a freeway in the United States is 120 kilometers per hour (75 mph). A device is set to measure the speed of passing vehicles. Suppose that the device will conduct three measurements of the speed of a passing vehicle, recording as a random sample X1, X2, X3. The traffic police will or will not fine the drivers depending on the average speed ${\bar {X}}$ . That is to say, the test statistic

$T={\frac {X_{1}+X_{2}+X_{3}}{3}}={\bar {X}}$

In addition, we suppose that the measurements X1, X2, X3 are modeled as normal distribution N(μ,2). Then, T should follow N(μ,2/ ${\sqrt {3}}$ ) and the parameter μ represents the true speed of passing vehicle. In this experiment, the null hypothesis H0 and the alternative hypothesis H1 should be

H0: μ=120 against H1: μ>120.

If we perform the statistic level at α=0.05, then a critical value c should be calculated to solve

$P\left(Z\geqslant {\frac {c-120}{\frac {2}{\sqrt {3}}}}\right)=0.05$

According to change-of-units rule for the normal distribution. Referring to Z-table, we can get

${\frac {c-120}{\frac {2}{\sqrt {3}}}}=1.645\Rightarrow c=121.9$

Here, the critical region. That is to say, if the recorded speed of a vehicle is greater than critical value 121.9, the driver will be fined. However, there are still 5% of the drivers are falsely fined since the recorded average speed is greater than 121.9 but the true speed does not pass 120, which we say, a type I error.

The type II error corresponds to the case that the true speed of a vehicle is over 120 kilometers per hour but the driver is not fined. For example, if the true speed of a vehicle μ=125, the probability that the driver is not fined can be calculated as

$P=(T<121.9|\mu =125)=P\left({\frac {T-125}{\frac {2}{\sqrt {3}}}}<{\frac {121.9-125}{\frac {2}{\sqrt {3}}}}\right)=\phi (-2.68)=0.0036$

which means, if the true speed of a vehicle is 125, the driver has the probability of 0.36% to avoid the fine when the statistic is performed at level α=0.05, since the recorded average speed is lower than 121.9. If the true speed is closer to 121.9 than 125, then the probability of avoiding the fine will also be higher.

The tradeoffs between type I error and type II error should also be considered. That is, in this case, if the traffic police do not want to falsely fine innocent drivers, the level α can be set to a smaller value, like 0.01. However, if that is the case, more drivers whose true speed is over 120 kilometers per hour, like 125, would be more likely to avoid the fine.

## Etymology

The terms "type I error" and "type II error" originate from a 1933 paper by Neyman and Pearson.

### Null hypothesis

It is standard practice for statisticians to conduct tests in order to determine whether or not a "speculative hypothesis" concerning the observed phenomena of the world (or its inhabitants) can be supported. The results of such testing determine whether a particular set of results agrees reasonably (or does not agree) with the speculated hypothesis.

On the basis that it is always assumed, by statistical convention, that the speculated hypothesis is wrong, and the so-called "null hypothesis" that the observed phenomena simply occur by chance (and that, as a consequence, the speculated agent has no effect) – the test will determine whether this hypothesis is right or wrong. This is why the hypothesis under test is often called the null hypothesis (most likely, coined by Fisher (1935, p. 19)), because it is *this* hypothesis that is to be either nullified or not nullified by the test. When the null hypothesis is nullified, it is possible to conclude that data support the "alternative hypothesis" (which is the original speculated one).

The consistent application by statisticians of Neyman and Pearson's convention of representing "the hypothesis to be tested" (or "the hypothesis to be nullified") with the expression *H*0 has led to circumstances where many understand the term "the null hypothesis" as meaning "the nil hypothesis" – a statement that the results in question have arisen through chance. This is not necessarily the case – the key restriction, as per Fisher (1966), is that "the null hypothesis must be exact, that is free from vagueness and ambiguity, because it must supply the basis of the 'problem of distribution', of which the test of significance is the solution." As a consequence of this, in experimental science the null hypothesis is generally a statement that a particular treatment has no effect; in observational science, it is that there is *no difference* between the value of a particular measured variable, and that of an experimental prediction.

### Statistical significance

If the probability of obtaining a result as extreme as the one obtained, supposing that the null hypothesis were true, is lower than a pre-specified cut-off probability (for example, 5%), then the result is said to be statistically significant and the null hypothesis is rejected.

British statistician Sir Ronald Aylmer Fisher (1890–1962) stressed that the null hypothesis

> is never proved or established, but is possibly disproved, in the course of experimentation. Every experiment may be said to exist only in order to give the facts a chance of disproving the null hypothesis.

— Fisher, 1935, p.19

### Type S and M errors

To address issues with null hypothesis testing, Andrew Gelman, John Carlin and others have suggested Type S and Type M errors to add to consideration of significant results.

Type S errors are errors of sign. The Type S error rate corresponds to the probability that if a significant result is obtained, the effect is estimated in the wrong direction of the true effect. This can occur often with low powered testing setups.

Type M errors are errors of magnitude. This is addressed through an "exaggeration factor", an assessment of the expected ratio of the absolute values of the estimate to the true value, conditional on a significant result being obtained. This is important because using a significance test to screen results in selection bias, which can lead to drastically overestimating effect sizes.

## Application domains

### Medicine

In the practice of medicine, the differences between the applications of screening and testing are considerable.

#### Medical screening

Screening involves relatively cheap tests that are given to large populations, none of whom manifest any clinical indication of disease (e.g., Pap smears).

Testing involves far more expensive, often invasive, procedures that are given only to those who manifest some clinical indication of disease, and are most often applied to confirm a suspected diagnosis.

For example, most states in the US require newborns to be screened for phenylketonuria and hypothyroidism, among other congenital disorders.

- Hypothesis: "The newborns have phenylketonuria and hypothyroidism".
- Null hypothesis (H0): "The newborns do not have phenylketonuria and hypothyroidism".
- Type I error (false positive): The true fact is that the newborns do not have phenylketonuria and hypothyroidism but we consider they have the disorders according to the data.
- Type II error (false negative): The true fact is that the newborns have phenylketonuria and hypothyroidism but we consider they do not have the disorders according to the data.

Although they display a high rate of false positives, the screening tests are considered valuable because they greatly increase the likelihood of detecting these disorders at a far earlier stage.

The simple blood tests used to screen possible blood donors for HIV and hepatitis have a significant rate of false positives; however, physicians use much more expensive and far more precise tests to determine whether a person is actually infected with either of these viruses.

Perhaps the most widely discussed false positives in medical screening come from the breast cancer screening procedure mammography. The US rate of false positive mammograms is up to 15%, the highest in world. One consequence of the high false positive rate in the US is that, in any 10-year period, half of the American women screened receive a false positive mammogram. False positive mammograms are costly, with over $100 million spent annually in the U.S. on follow-up testing and treatment. They also cause women unneeded anxiety. As a result of the high false positive rate in the US, as many as 90–95% of women who get a positive mammogram do not have the condition. The lowest rate in the world is in the Netherlands, 1%. The lowest rates are generally in Northern Europe where mammography films are read twice and a high threshold for additional testing is set (the high threshold decreases the power of the test).

The ideal population screening test would be cheap, easy to administer, and produce zero false negatives, if possible. Such tests usually produce more false positives, which can subsequently be sorted out by more sophisticated (and expensive) testing.

#### Medical testing

False negatives and false positives are significant issues in medical testing.

- Hypothesis: "The patients have the specific disease".
- Null hypothesis (H0): "The patients do not have the specific disease".
- Type I error (false positive): The true fact is that the patients do not have a specific disease but the physician judges the patient is ill according to the test reports.
- Type II error (false negative): The true fact is that the disease is actually present but the test reports provide a falsely reassuring message to patients and physicians that the disease is absent.

False positives can also produce serious and counter-intuitive problems when the condition being searched for is rare, as in screening. If a test has a false positive rate of one in ten thousand, but only one in a million samples (or people) is a true positive, most of the positives detected by that test will be false. The probability that an observed positive result is a false positive may be calculated using Bayes' theorem.

False negatives produce serious and counter-intuitive problems, especially when the condition being searched for is common. If a test with a false negative rate of only 10% is used to test a population with a true occurrence rate of 70%, many of the negatives detected by the test will be false.

This sometimes leads to inappropriate or inadequate treatment of both the patient and their disease. A common example is relying on cardiac stress tests to detect coronary atherosclerosis, even though cardiac stress tests are known to only detect limitations of coronary artery blood flow due to advanced stenosis.

### Biometrics

Biometric matching, such as for fingerprint recognition, facial recognition or iris recognition, is susceptible to type I and type II errors.

- Hypothesis: "The input does not identify someone in the searched list of people".
- Null hypothesis: "The input does identify someone in the searched list of people".
- Type I error (false reject rate): The true fact is that the person is someone in the searched list but the system concludes that the person is not according to the data.
- Type II error (false match rate): The true fact is that the person is not someone in the searched list but the system concludes that the person is someone whom we are looking for according to the data.

The probability of type I errors is called the "false reject rate" (FRR) or false non-match rate (FNMR), while the probability of type II errors is called the "false accept rate" (FAR) or false match rate (FMR).

If the system is designed to rarely match suspects then the probability of type II errors can be called the "false alarm rate". On the other hand, if the system is used for validation (and acceptance is the norm) then the FAR is a measure of system security, while the FRR measures user inconvenience level.

### Law

In criminal legal proceedings, there is enormous emphasis on ensuring that if any error is committed it will be Type II error (letting an otherwise-culpable criminal defendant go free) rather than type I error (punishing an innocent person for a crime he or she did not commit). This emphasis is the reason for high burdens of proof (guilty beyond a reasonable doubt), careful scrutiny of the prosecution's characterizations of inculpatory evidence or testimony, and skepticism or exclusion as to evidence that may be more prejudicial than probative (the Rule 403 balancing test).

Substantial scholarship dating back centuries discusses the grave consequences of miscarriages of justice in criminal proceedings, not only for the defendant, but for the perception of fairness of the entire judicial system and trust from community stakeholders that allegations of criminal activity will be heard seriously but also fairly. English jurist William Blackstone invented Blackstone's ratio of 10:1 to describe the concept that a fair system might let ten guilty defendants walk free rather than let more than one innocent person be jailed.

In recent years, legal scholarship and mainstream jurisprudence has adopted the Type I and Type II error taxonomy to have a more rigorous vocabulary with which to discuss judicial mistakes and wrongful convictions. The U.S. Supreme Court used the Type I vs. Type II taxonomy in its discussion of errors in *Ballew v. Georgia* and judges and law professors increasingly use this dichotomous designation rather than the more casual "wrongly convicted" or "erroneously acquitted," which were terms used often in earlier scholarship.

Recent scholarship and judicial concern often centers on the size and unanimity of juries as safeguards against Type I error (incorrectly convicting the innocent defendant).

Small juries of less than twelve have been criticized by the U.S. Supreme Court for being more likely to produce Type I errors; meanwhile, some judges have also criticized the empaneling of more than the typical twelve jurors as problematic (Judge Anderson of the Wisconsin Court of Appeals wrote a notable dissent on this topic in 1993: "Absent a legislative pronouncement of public policy permitting a defendant to acquiesce to be tried by a jury greater than twelve, it is plain error to permit more than twelve jurors to deliberate."). As to unanimity, on April 20, 2020, the U.S. Supreme Court ruled the Sixth Amendment requires a unanimous jury verdict to convict a defendant of a serious offense, citing concern around Type I error as among the primary reasons for requiring unanimous verdicts in serious criminal matters.

### Security screening

False positives are routinely found every day in airport security screening, which are ultimately visual inspection systems. The installed security alarms are intended to prevent weapons being brought onto aircraft; yet they are often set to such high sensitivity that they alarm many times a day for minor items, such as keys, belt buckles, loose change, mobile phones, and tacks in shoes.

- Hypothesis: "The item is a weapon".
- Null hypothesis: "The item is not a weapon".
- Type I error (false positive): The true fact is that the item is not a weapon but the system still sounds an alarm.
- Type II error (false negative) The true fact is that the item is a weapon but the system keeps silent at this time.

The ratio of false positives (identifying an innocent traveler as a terrorist) to true positives (detecting a would-be terrorist) is, therefore, very high; and because almost every alarm is a false positive, the positive predictive value of these screening tests is very low.

The relative cost of false results determines the likelihood that test creators allow these events to occur. As the cost of a false negative in this scenario is extremely high (not detecting a bomb being brought onto a plane could result in hundreds of deaths) whilst the cost of a false positive is relatively low (a reasonably simple further inspection) the most appropriate test is one with a low statistical specificity but high statistical sensitivity (one that allows a high rate of false positives in return for minimal false negatives).

### Computers

The notions of false positives and false negatives have a wide currency in the realm of computers and computer applications, including computer security, spam filtering, malware, optical character recognition, and many others.

For example, in the case of spam filtering:

- Hypothesis: "The message is spam".
- Null hypothesis: "The message is not spam".
- Type I error (false positive): Spam filtering or spam blocking techniques wrongly classify a legitimate email message as spam and, as a result, interfere with its delivery.
- Type II error (false negative): Spam email is not detected as spam, but is classified as non-spam.

While most anti-spam tactics can block or filter a high percentage of unwanted emails, doing so without creating significant false-positive results is a much more demanding task. A low number of false negatives is an indicator of the efficiency of spam filtering.
