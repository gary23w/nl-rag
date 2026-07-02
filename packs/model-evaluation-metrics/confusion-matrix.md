---
title: "Confusion matrix"
source: https://en.wikipedia.org/wiki/Confusion_matrix
domain: model-evaluation-metrics
license: CC-BY-SA-4.0
tags: model evaluation metrics, precision and recall, confusion matrix, cross validation
fetched: 2026-07-02
---

# Confusion matrix

A **confusion matrix**, also known as **error matrix**, is a specific table layout that allows visualization of the performance of a person or an algorithm on a specific task. In audiology these matrices measure how a person can hear specific words or sounds. In machine learning these matrices show the success of the learning system both in supervised learning and unsupervised learning, where they are usually called **matching matrix**.

Each row of the matrix represents the instances in an actual class while each column represents the instances in a predicted class, or vice versa – both variants are found in the literature. The diagonal of the matrix therefore represents all instances that are correctly predicted. The name stems from the fact that it makes it easy to identify whether the system is confusing two classes (i.e., commonly mislabeling one class as another). The confusion matrix has its origins in human perceptual studies of auditory stimuli. It was adapted for machine learning studies and used by Frank Rosenblatt, among other early researchers, to compare human and machine classifications of visual (and later auditory) stimuli.

It is a special kind of contingency table, with two dimensions ("actual" and "predicted"), and identical sets of "classes" in both dimensions (each combination of dimension and class is a variable in the contingency table).

## Example

Given a sample of 12 individuals, 8 that have been diagnosed with cancer and 4 that are cancer-free, where individuals with cancer belong to class 1 (positive) and non-cancer individuals belong to class 0 (negative), we can display that data as follows:

Individual number

1

2

3

4

5

6

7

8

9

10

11

12

Actual classification

1

1

1

1

1

1

1

1

0

0

0

0

Assume that we have a classifier that distinguishes between individuals with and without cancer in some way, we can take the 12 individuals and run them through the classifier. The classifier then makes 9 accurate predictions and misses 3: 2 individuals with cancer wrongly predicted as being cancer-free (sample 1 and 2), and 1 person without cancer that is wrongly predicted to have cancer (sample 9).

Individual number

1

2

3

4

5

6

7

8

9

10

11

12

Actual classification

1

1

1

1

1

1

1

1

0

0

0

0

Predicted classification

0

0

1

1

1

1

1

1

1

0

0

0

Notice, that if we compare the actual classification set to the predicted classification set, there are 4 different outcomes that could result in any particular column:

1. The actual classification is positive and the predicted classification is positive (1,1). This is called a true positive result because the positive sample was correctly identified by the classifier.
2. The actual classification is positive and the predicted classification is negative (1,0). This is called a false negative result because the positive sample is incorrectly identified by the classifier as being negative.
3. The actual classification is negative and the predicted classification is positive (0,1). This is called a false positive result because the negative sample is incorrectly identified by the classifier as being positive.
4. The actual classification is negative and the predicted classification is negative (0,0). This is called a true negative result because the negative sample gets correctly identified by the classifier.

We can then perform the comparison between actual and predicted classifications and add this information to the table, making correct results appear in green so they are more easily identifiable.

Individual number

1

2

3

4

5

6

7

8

9

10

11

12

Actual classification

1

1

1

1

1

1

1

1

0

0

0

0

Predicted classification

0

0

1

1

1

1

1

1

1

0

0

0

Result

FN

FN

TP

TP

TP

TP

TP

TP

FP

TN

TN

TN

The template for any binary confusion matrix uses the four kinds of results discussed above (true positives, false negatives, false positives, and true negatives) along with the positive and negative classifications. The four outcomes can be formulated in a 2×2 *confusion matrix*, as follows:

|   |   | **Predicted condition** |   |
|---|---|---|---|
| Total population = P + N | **Positive (PP)** | **Negative (PN)** |   |
| **Actual condition** | **Positive (P)** | **True positive (TP)** | **False negative (FN)** |
| **Negative (N)** | **False positive (FP)** | **True negative (TN)** |   |
| Sources: |   |   |   |

The color convention of the three data tables above were picked to match this confusion matrix, in order to easily differentiate the data.

Now, we can simply total up each type of result, substitute into the template, and create a confusion matrix that will concisely summarize the results of testing the classifier:

|   |   | **Predicted condition** |   |
|---|---|---|---|
| Total 8 + 4 = 12 | **Cancer** 7 | **Non-cancer** 5 |   |
| **Actual condition** | **Cancer** 8 | 6 | 2 |
| **Non-cancer** 4 | 1 | 3 |   |

In this confusion matrix, of the 8 samples with cancer, the system judged that 2 were cancer-free, and of the 4 samples without cancer, it predicted that 1 did have cancer. All correct predictions are located in the diagonal of the table (highlighted in green), so it is easy to visually inspect the table for prediction errors, as values outside the diagonal will represent them. By summing up the 2 rows of the confusion matrix, one can also deduce the total number of positive (P) and negative (N) samples in the original dataset, i.e. $P=TP+FN$ and $N=FP+TN$ .

## Table of confusion

In predictive analytics, a **table of confusion** (sometimes also called a **confusion matrix**) is a table with two rows and two columns that reports the number of *true positives*, *false negatives*, *false positives*, and *true negatives*. This allows more detailed analysis than simply observing the proportion of correct classifications (accuracy). Accuracy will yield misleading results if the data set is unbalanced; that is, when the numbers of observations in different classes vary greatly.

For example, if there were 95 cancer samples and only 5 non-cancer samples in the data, a particular classifier might classify all the observations as having cancer. The overall accuracy would be 95%, but in more detail the classifier would have a 100% recognition rate (sensitivity) for the cancer class but a 0% recognition rate for the non-cancer class. F1 score is even more unreliable in such cases, and here would yield over 97.4%, whereas informedness removes such bias and yields 0 as the probability of an informed decision for any form of guessing (here always guessing cancer).

According to Davide Chicco and Giuseppe Jurman, the most informative metric to evaluate a confusion matrix is the Matthews correlation coefficient (MCC).

Other metrics can be included in a confusion matrix, each of them having their significance and use.

|   |   | **Predicted condition** | Sources: |   |   |
|---|---|---|---|---|---|
| Total population = P + N | **Predicted positive** | **Predicted negative** | Informedness, bookmaker informedness (BM) = TPR + TNR − 1 | Prevalence threshold (PT) = ⁠√TPR × FPR − FPR/TPR − FPR⁠ |   |
| **Actual condition** | **Real Positive (P)** | **True positive** (TP), hit | **False negative** (FN), miss, underestimation | True positive rate (TPR), recall, sensitivity (SEN), probability of detection, hit rate, power = ⁠TP/P⁠ = 1 − FNR | False negative rate (FNR), miss rate type II error = ⁠FN/P⁠ = 1 − TPR |
| **Real Negative (N)** | **False positive** (FP), false alarm, overestimation | **True negative** (TN), correct rejection | False positive rate (FPR), probability of false alarm, fall-out type I error = ⁠FP/N⁠ = 1 − TNR | True negative rate (TNR), specificity (SPC), selectivity = ⁠TN/N⁠ = 1 − FPR |   |
|   | Prevalence = ⁠P/P + N⁠ | Positive predictive value (PPV), precision = ⁠TP/TP + FP⁠ = 1 − FDR | False omission rate (FOR) = ⁠FN/TN + FN⁠ = 1 − NPV | Positive likelihood ratio (LR+) = ⁠TPR/FPR⁠ | Negative likelihood ratio (LR−) = ⁠FNR/TNR⁠ |
| Accuracy (ACC) = ⁠TP + TN/P + N⁠ | False discovery rate (FDR) = ⁠FP/TP + FP⁠ = 1 − PPV | Negative predictive value (NPV) = ⁠TN/TN + FN⁠ = 1 − FOR | Markedness (MK), deltaP (Δp) = PPV + NPV − 1 | Diagnostic odds ratio (DOR) = ⁠LR+/LR−⁠ = ⁠TP × TN/FP × FN⁠ |   |
| Balanced accuracy (BA) = ⁠TPR + TNR/2⁠ | F1 score = ⁠2 PPV × TPR/PPV + TPR⁠ = ⁠2 TP/2 TP + FP + FN⁠ | Fowlkes–Mallows index (FM) = √PPV × TPR | *phi* or Matthews correlation coefficient (MCC) = √TPR × TNR × PPV × NPV - √FNR × FPR × FOR × FDR | Threat score (TS), critical success index (CSI), Jaccard index = ⁠TP/TP + FN + FP⁠ |   |

1. the number of real positive cases in the data
2. A test result that correctly indicates the presence of a condition or characteristic
3. Type II error: A test result which wrongly indicates that a particular condition or attribute is absent
4. the number of real negative cases in the data
5. A test result that correctly indicates the absence of a condition or characteristic
6. Type I error: A test result which wrongly indicates that a particular condition or attribute is present

Some researchers have argued that the confusion matrix, and the metrics derived from it, do not truly reflect a model's *knowledge*. In particular, the confusion matrix cannot show whether correct predictions were reached through sound reasoning or merely by chance (a problem known in philosophy as epistemic luck). It also does not capture situations where the facts used to make a prediction later change or turn out to be wrong (defeasibility). This means that while the confusion matrix is a useful tool for measuring classification performance, it may give an incomplete picture of a model’s true reliability.

## Confusion matrices with more than two categories

Confusion matrix is not limited to binary classification and can be used in multi-class classifiers as well. The confusion matrices discussed above have only two conditions: positive and negative. For example, the table below summarizes communication of a whistled language between two speakers, with zero values omitted for clarity.

| Perceived vowelVowel produced | i | e | a | o | u |
|---|---|---|---|---|---|
| i | **15** |   | 1 |   |   |
| e | 1 |   | 1 |   |   |
| a |   |   | **79** | 5 |   |
| o |   |   | 4 | **15** | 3 |
| u |   |   |   | 2 | **2** |

## Confusion matrices in multi-label and soft-label classification

Confusion matrices are not limited to single-label classification (where only one class is present) or hard-label settings (where classes are either fully present, 1, or absent, 0). They can also be extended to Multi-label classification (where multiple classes can be predicted at once) and soft-label classification (where classes can be partially present).

One such extension is the **Transport-based Confusion Matrix (TCM)**, which builds on the theory of optimal transport and the principle of maximum entropy. TCM applies to single-label, multi-label, and soft-label settings. It retains the familiar structure of the standard confusion matrix: a square matrix sized by the number of classes, with diagonal entries indicating correct predictions and off-diagonal entries indicating confusion. In the single-label case, TCM is identical to the standard confusion matrix.

TCM follows the same reasoning as the standard confusion matrix: if class A is overestimated (its predicted value is greater than its label value) and class B is underestimated (its predicted value is less than its label value), A is considered confused with B, and the entry (B, A) is increased. If a class is both predicted and present, it is correctly identified, and the diagonal entry (A, A) increases. Optimal transport and maximum entropy are used to determine the extent to which these entries are updated.

TCM enables clearer comparison between predictions and labels in complex classification tasks, while maintaining a consistent matrix format across settings.
