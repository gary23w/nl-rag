---
title: "F-score"
source: https://en.wikipedia.org/wiki/F-score
domain: model-evaluation
license: CC-BY-SA-4.0
tags: model evaluation, cross validation, confusion matrix, precision recall, roc curve
fetched: 2026-07-02
---

# F-score

In statistical analysis of binary classification and information retrieval systems, the **F-score** or **F-measure** is a measure of predictive performance. It is calculated from the precision and recall of the test, where the precision is the number of true positive results divided by the number of all samples predicted to be positive, including those not identified correctly, and the recall is the number of true positive results divided by the number of all samples that should have been identified as positive. Precision is also known as positive predictive value, and recall is also known as sensitivity in diagnostic binary classification.

The **F1** score is the harmonic mean of the precision and recall. It thus symmetrically represents both precision and recall in one metric. The more generic $F_{\beta }$ score applies additional weights, valuing one of precision or recall more than the other.

The highest possible value of an F-score is 1.0, indicating perfect precision and recall, and the lowest possible value is 0, if the precision or the recall is zero.

## Etymology

The name F-measure is believed to be named after a different F function in Van Rijsbergen's book, when introduced to the Fourth Message Understanding Conference (MUC-4, 1992).

## Definition

The traditional F-measure or balanced F-score (**F1 score**) is the harmonic mean of precision and recall:

$F_{1}={\frac {2}{\mathrm {recall} ^{-1}+\mathrm {precision} ^{-1}}}=2{\frac {\mathrm {precision} \cdot \mathrm {recall} }{\mathrm {precision} +\mathrm {recall} }}={\frac {2\mathrm {TP} }{2\mathrm {TP} +\mathrm {FP} +\mathrm {FN} }}$

With precision = TP / (TP + FP) and recall = TP / (TP + FN), it follows that the numerator of *F*1 is the sum of their numerators and the denominator of *F*1 is the sum of their denominators.

If FP=FN

$F_{1}={\frac {2\mathrm {TP} }{2\mathrm {TP} +2\mathrm {FP} }}={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FP} }}$

or

$F_{1}={\frac {2\mathrm {TP} }{2\mathrm {TP} +2\mathrm {FN} }}={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FN} }}$

So, F1 = precision = recall

If TP=FP=FN

$F_{1}={\frac {2\mathrm {TP} }{2\mathrm {TP} +2\mathrm {FP} }}={\frac {2\mathrm {TP} }{4\mathrm {TP} }}={\frac {1}{2}}=0.5$

or

$F_{1}={\frac {2\mathrm {TP} }{2\mathrm {TP} +2\mathrm {FN} }}={\frac {2\mathrm {TP} }{4\mathrm {TP} }}={\frac {1}{2}}=0.5$

To see it as a harmonic mean, note that $F_{1}^{-1}={\frac {1}{2}}(\mathrm {recall} ^{-1}+\mathrm {precision} ^{-1})$ .

### Fβ score

A more general F score, $F_{\beta }$ , that uses a positive real factor $\beta$ , where $\beta$ is chosen such that recall is considered $\beta$ times as important as precision, is:

$F_{\beta }={\frac {\beta ^{2}+1}{(\beta ^{2}\cdot \mathrm {recall} ^{-1})+\mathrm {precision} ^{-1}}}={\frac {(1+\beta ^{2})\cdot \mathrm {precision} \cdot \mathrm {recall} }{(\beta ^{2}\cdot \mathrm {precision} )+\mathrm {recall} }}$

To see that as a weighted harmonic mean, note that $F_{\beta }^{-1}={\frac {1}{\beta +\beta ^{-1}}}(\beta \cdot \mathrm {recall} ^{-1}+\beta ^{-1}\cdot \mathrm {precision} ^{-1})$ .

In terms of Type I and type II errors this becomes:

$F_{\beta }={\frac {(1+\beta ^{2})\cdot \mathrm {TP} }{(1+\beta ^{2})\cdot \mathrm {TP} +\beta ^{2}\cdot \mathrm {FN} +\mathrm {FP} }}\,={\frac {(1+\beta ^{2})\cdot \mathrm {TP} }{(\mathrm {TP} +\mathrm {FN} )\cdot \beta ^{2}+(\mathrm {TP} +\mathrm {FP} )}}\,$

Two commonly used values for $\beta$ are 2, which weighs recall higher than precision, and 1/2, which weighs recall lower than precision.

The F-measure was derived so that $F_{\beta }$ "measures the effectiveness of retrieval with respect to a user who attaches $\beta$ times as much importance to recall as precision". It is based on Van Rijsbergen's effectiveness measure

$E=1-\left({\frac {\alpha }{p}}+{\frac {1-\alpha }{r}}\right)^{-1}$

Their relationship is: $F_{\beta }=1-E$ where $\alpha ={\frac {1}{1+\beta ^{2}}}$

## Diagnostic testing

This is related to the field of binary classification where recall is often termed "sensitivity".

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

## Dependence of the F-score on class imbalance

Precision-recall curve, and thus the $F_{\beta }$ score, explicitly depends on the ratio r of positive to negative test cases. This means that comparison of the F-score across different problems with differing class ratios is problematic. One way to address this issue (see e.g., Siblini et al., 2020) is to use a standard class ratio $r_{0}$ when making such comparisons.

## Applications

The F-score is often used in the field of information retrieval for measuring search, document classification, and query classification performance. It is particularly relevant in applications which are primarily concerned with the positive class and where the positive class is rare relative to the negative class.

Earlier works focused primarily on the F1 score, but with the proliferation of large scale search engines, performance goals changed to place more emphasis on either precision or recall and so $F_{\beta }$ is seen in wide application.

The F-score is also used in machine learning. However, the F-measures do not take true negatives into account, hence measures such as the Matthews correlation coefficient, Informedness or Cohen's kappa may be preferred to assess the performance of a binary classifier.

The F-score has been widely used in the natural language processing literature, such as in the evaluation of named entity recognition and word segmentation.

## Properties

The F1 score is the Dice coefficient of the set of retrieved items and the set of relevant items.

- The F1-score of a classifier which always predicts the positive class converges to 1 as the probability of the positive class increases.
- The F1-score of a classifier which always predicts the positive class is equal to 2 * proportion_of_positive_class / ( 1 + proportion_of_positive_class ), since the recall is 1, and the precision is equal to the proportion of the positive class.
- If the scoring model is uninformative (cannot distinguish between the positive and negative class) then the optimal threshold is 0 so that the positive class is always predicted.
- F1 score is concave in the true positive rate.

## Criticism

David Hand and others criticize the widespread use of the F1 score since it gives equal importance to precision and recall. In practice, different types of mis-classifications incur different costs. In other words, the relative importance of precision and recall is an aspect of the problem.

According to Davide Chicco and Giuseppe Jurman, the F1 score is less truthful and informative than the Matthews correlation coefficient (MCC) in binary evaluation classification.

David M W Powers has pointed out that F1 ignores the True Negatives and thus is misleading for unbalanced classes, while kappa and correlation measures are symmetric and assess both directions of predictability - the classifier predicting the true class and the true class predicting the classifier prediction, proposing separate multiclass measures Informedness and Markedness for the two directions, noting that their geometric mean is correlation.

Another source of critique of F1 is its lack of symmetry. It means it may change its value when dataset labeling is changed - the "positive" samples are named "negative" and vice versa. This criticism is met by the P4 metric definition, which is sometimes indicated as a symmetrical extension of F1.

Finally, Ferrer and Dyrland et al. argue that the expected cost (or its counterpart, the expected utility) is the only principled metric for evaluation of classification decisions, having various advantages over the F-score and the MCC. Both works show that the F-score can result in wrong conclusions about the absolute and relative quality of systems.

## Difference from Fowlkes–Mallows index

While the F-measure is the harmonic mean of recall and precision, the Fowlkes–Mallows index is their geometric mean.

## Extension to multi-class classification

The F-score is also used for evaluating classification problems with more than two classes (Multiclass classification). A common method is to average the F-score over each class, aiming at a balanced measurement of performance.

### Macro F1

*Macro F1* is a macro-averaged F1 score aiming at a balanced performance measurement. To calculate macro F1, two different averaging-formulas have been used: the F1 score of (arithmetic) class-wise precision and recall means or the arithmetic mean of class-wise F1 scores, where the latter exhibits more desirable properties.

### Micro F1

*Micro F1* is the harmonic mean of *micro precision* and *micro recall*. In single-label multi-class classification, micro precision equals micro recall, thus micro F1 is equal to both. However, contrary to a common misconception, micro F1 does not generally equal *accuracy*, because accuracy takes true negatives into account while micro F1 does not.
