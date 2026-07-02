---
title: "Winnow (algorithm)"
source: https://en.wikipedia.org/wiki/Winnow_(algorithm)
domain: computational-learning
license: CC-BY-SA-4.0
tags: computational learning theory, mistake bound model, query learning, statistical learning theory
fetched: 2026-07-02
---

# Winnow (algorithm)

The **winnow algorithm** is a technique from machine learning for learning a linear classifier from labeled examples. It is very similar to the perceptron algorithm. However, the perceptron algorithm uses an additive weight-update scheme, while Winnow uses a multiplicative scheme that allows it to perform much better when many dimensions are irrelevant (hence its name winnow). It is a simple algorithm that scales well to high-dimensional data. During training, Winnow is shown a sequence of positive and negative examples. From these it learns a decision hyperplane that can then be used to label novel examples as positive or negative. The algorithm can also be used in the online learning setting, where the learning and the classification phase are not clearly separated.

## Algorithm

The basic algorithm, Winnow1, is as follows. The instance space is $X=\{0,1\}^{n}$ , that is, each instance is described as a set of Boolean-valued features. The algorithm maintains non-negative weights $w_{i}$ for $i\in \{1,\ldots ,n\}$ , which are initially set to 1, one weight for each feature. When the learner is given an example $(x_{1},\ldots ,x_{n})$ , it applies the typical prediction rule for linear classifiers:

- **If** $\sum _{i=1}^{n}w_{i}x_{i}>\Theta$ , **then** predict 1
- **Otherwise** predict 0

Here $\Theta$ is a real number that is called the *threshold*. Together with the weights, the threshold defines a dividing hyperplane in the instance space. Good bounds are obtained if $\Theta =n/2$ (see below).

For each example with which it is presented, the learner applies the following update rule:

- If an example is correctly classified, do nothing.
- If an example is predicted incorrectly and the correct result was 0, for each feature $x_{i}=1$ , the corresponding weight $w_{i}$ is set to 0 (demotion step). $\forall x_{i}=1,w_{i}=0$
- If an example is predicted incorrectly and the correct result was 1, for each feature $x_{i}=1$ , the corresponding weight $w_{i}$ multiplied by α(promotion step). $\forall x_{i}=1,w_{i}=\alpha w_{i}$

A typical value for α is 2.

There are many variations to this basic approach. *Winnow2* is similar except that in the demotion step the weights are divided by α instead of being set to 0. *Balanced Winnow* maintains two sets of weights, and thus two hyperplanes. This can then be generalized for multi-label classification.

## Mistake bounds

In certain circumstances, it can be shown that the number of mistakes Winnow makes as it learns has an upper bound that is independent of the number of instances with which it is presented. If the Winnow1 algorithm uses $\alpha >1$ and $\Theta \geq 1/\alpha$ on a target function that is a k -literal monotone disjunction given by $f(x_{1},\ldots ,x_{n})=x_{i_{1}}\lor \cdots \lor x_{i_{k}}$ , then for any sequence of instances the total number of mistakes is bounded by: $\alpha k(\log _{\alpha }\Theta +1)+{\frac {n}{\Theta }}$ .
