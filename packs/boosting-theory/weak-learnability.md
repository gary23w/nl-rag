---
title: "Boosting (machine learning)"
source: https://en.wikipedia.org/wiki/Weak_learnability
domain: boosting-theory
license: CC-BY-SA-4.0
tags: boosting meta algorithm, weak learner, adaboost algorithm, margin theory
fetched: 2026-07-02
---

# Boosting (machine learning)

(Redirected from

Weak learnability

)

In machine learning (ML), **boosting** is an ensemble learning method that combines a set of less accurate models (called "weak learners") to create a single, highly accurate model (a "strong learner"). Unlike other ensemble methods that build models in parallel (such as bagging), boosting algorithms build models sequentially. Each new model in the sequence is trained to correct the errors made by its predecessors. This iterative process allows the overall model to improve its accuracy, particularly by reducing bias. Boosting is a popular and effective technique used in supervised learning for both classification and regression tasks.

The theoretical foundation for boosting came from a question posed by Kearns and Valiant (1988, 1989): "Can a set of weak learners create a single strong learner?" A weak learner is defined as a classifier that performs only slightly better than random guessing, whereas a strong learner is a classifier that is highly correlated with the true classification. Robert Schapire's affirmative answer to this question in a 1990 paper led to the development of practical boosting algorithms. The first such algorithm was developed by Schapire, with Freund and Schapire later developing AdaBoost, which remains a foundational example of boosting.

## Algorithms

While boosting is not algorithmically constrained, most boosting algorithms consist of iteratively learning weak classifiers with respect to a distribution and adding them to a final strong classifier. When they are added, they are weighted in a way that is related to the weak learners' accuracy. After a weak learner is added, the data weights are readjusted, known as "re-weighting". Misclassified input data gain a higher weight and examples that are classified correctly lose weight. Thus, future weak learners focus more on the examples that previous weak learners misclassified.

There are many boosting algorithms. The original ones, proposed by Robert Schapire (a recursive majority gate formulation), and Yoav Freund (boost by majority), were not adaptive and could not take full advantage of the weak learners. Schapire and Freund then developed AdaBoost, an adaptive boosting algorithm that won the prestigious Gödel Prize.

Only algorithms that are provable boosting algorithms in the probably approximately correct learning formulation can accurately be called *boosting algorithms*. Other algorithms that are similar in spirit to boosting algorithms are sometimes called "leveraging algorithms", although they are also sometimes incorrectly called boosting algorithms.

The main variation between many boosting algorithms is their method of weighting training data points and hypotheses. AdaBoost is very popular and the most significant historically as it was the first algorithm that could adapt to the weak learners. It is often the basis of introductory coverage of boosting in university machine learning courses. There are many more recent algorithms such as LPBoost, TotalBoost, BrownBoost, xgboost, MadaBoost, LogitBoost, CatBoost and others. Many boosting algorithms fit into the AnyBoost framework, which shows that boosting performs gradient descent in a function space using a convex cost function.

## Object categorization in computer vision

Given images containing various known objects in the world, a classifier can be learned from them to automatically classify the objects in future images. Simple classifiers built based on some image feature of the object tend to be weak in categorization performance. Using boosting methods for object categorization is a way to unify the weak classifiers in a special way to boost the overall ability of categorization.

### Problem of object categorization

Object categorization is a typical task of computer vision that involves determining whether or not an image contains some specific category of object. The idea is closely related with recognition, identification, and detection. Appearance based object categorization typically contains feature extraction, learning a classifier, and applying the classifier to new examples. There are many ways to represent a category of objects, e.g. from shape analysis, bag of words models, or local descriptors such as SIFT, etc. Examples of supervised classifiers are Naive Bayes classifiers, support vector machines, mixtures of Gaussians, and neural networks. However, research has shown that object categories and their locations in images can be discovered in an unsupervised manner as well.

### Status quo for object categorization

The recognition of object categories in images is a challenging problem in computer vision, especially when the number of categories is large. This is due to high intra class variability and the need for generalization across variations of objects within the same category. Objects within one category may look quite different. Even the same object may appear unalike under different viewpoint, scale, and illumination. Background clutter and partial occlusion add difficulties to recognition as well. Humans are able to recognize thousands of object types, whereas most of the existing object recognition systems are trained to recognize only a few, e.g. human faces, cars, simple objects, etc. Research has been very active on dealing with more categories and enabling incremental additions of new categories, and although the general problem remains unsolved, several multi-category objects detectors (for up to hundreds or thousands of categories) have been developed. One means is by feature sharing and boosting.

### Boosting for binary categorization

AdaBoost can be used for face detection as an example of binary categorization. The two categories are faces versus background. The general algorithm is as follows:

1. Form a large set of simple features
2. Initialize weights for training images
3. For T rounds
  1. Normalize the weights
  2. For available features from the set, train a classifier using a single feature and evaluate the training error
  3. Choose the classifier with the lowest error
  4. Update the weights of the training images: increase if classified wrongly by this classifier, decrease if correctly
4. Form the final strong classifier as the linear combination of the T classifiers (coefficient larger if training error is small)

After boosting, a classifier constructed from 200 features could yield a 95% detection rate under a $10^{-5}$ false positive rate.

Another application of boosting for binary categorization is a system that detects pedestrians using patterns of motion and appearance. This work is the first to combine both motion information and appearance information as features to detect a walking person. It takes a similar approach to the Viola-Jones object detection framework.

### Boosting for multi-class categorization

Compared with binary categorization, multi-class categorization looks for common features that can be shared across the categories at the same time. They turn to be more generic edge like features. During learning, the detectors for each category can be trained jointly. Compared with training separately, it generalizes better, needs less training data, and requires fewer features to achieve the same performance.

The main flow of the algorithm is similar to the binary case. What is different is that a measure of the joint training error shall be defined in advance. During each iteration the algorithm chooses a classifier of a single feature (features that can be shared by more categories shall be encouraged). This can be done via converting multi-class classification into a binary one (a set of categories versus the rest), or by introducing a penalty error from the categories that do not have the feature of the classifier.

In the paper "Sharing visual features for multiclass and multiview object detection", A. Torralba et al. used GentleBoost for boosting and showed that when training data is limited, learning via sharing features does a much better job than no sharing, given same boosting rounds. Also, for a given performance level, the total number of features required (and therefore the run time cost of the classifier) for the feature sharing detectors, is observed to scale approximately logarithmically with the number of class, i.e., slower than linear growth in the non-sharing case. Similar results are shown in the paper "Incremental learning of object detectors using a visual shape alphabet", yet the authors used AdaBoost for boosting.

## Convex vs. non-convex boosting algorithms

Boosting algorithms can be based on convex or non-convex optimization algorithms. Convex algorithms, such as AdaBoost and LogitBoost, can be "defeated" by random noise such that they can't learn basic and learnable combinations of weak hypotheses. This limitation was pointed out by Long & Servedio in 2008. However, by 2009, multiple authors demonstrated that boosting algorithms based on non-convex optimization, such as BrownBoost, can learn from noisy datasets and can specifically learn the underlying classifier of the Long–Servedio dataset.
