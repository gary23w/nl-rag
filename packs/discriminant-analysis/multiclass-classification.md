---
title: "Multiclass classification"
source: https://en.wikipedia.org/wiki/Multiclass_classification
domain: discriminant-analysis
license: CC-BY-SA-4.0
tags: linear discriminant analysis, discriminant function, linear classifier, multiclass classification
fetched: 2026-07-02
---

# Multiclass classification

In machine learning and statistical classification, **multiclass classification** or **multinomial classification** is the problem of classifying instances into one of three or more classes (classifying instances into one of two classes is called binary classification). For example, deciding on whether an image is showing a banana, peach, orange, or an apple is a multiclass classification problem, with four possible classes (banana, peach, orange, apple), while deciding on whether an image contains an apple or not is a binary classification problem (with the two possible classes being: apple, no apple).

While many classification algorithms (e.g., decision trees, k-NN, neural networks and multinomial logistic regression) naturally permit the use of more than two classes, some are by nature binary algorithms (e.g., classical binary support vector machine) and require decomposition strategies such as one-vs-all, one-vs-one, or ECOC to solve multiclass problems.

Multiclass classification should not be confused with multi-label classification, where multiple labels are to be predicted for each instance (e.g., predicting that an image contains both an apple and an orange, in the previous example).

## Better-than-random multiclass models

From the confusion matrix of a multiclass model, we can determine whether a model does better than chance. Let $K\geq 3$ be the number of classes, ${\mathcal {O}}$ a set of observations, ${\hat {y}}:{\mathcal {O}}\to \{1,...,K\}$ a model of the target variable $y:{\mathcal {O}}\to \{1,...,K\}$ and $n_{i,j}$ be the number of observations in the set $\{y=i\}\cap \{{\hat {y}}=j\}$ . We note $n_{i.}=\sum _{j}n_{i,j}$ , $n_{.j}=\sum _{i}n_{i,j}$ , $n=\sum _{j}n_{.j}=\sum _{i}n_{i.}$ , $\lambda _{i}={\frac {n_{i.}}{n}}$ and $\mu _{j}={\frac {n_{.j}}{n}}$ . It is assumed that the confusion matrix $(n_{i,j})_{i,j}$ contains at least one non-zero entry in each row, that is $\lambda _{i}>0$ for any i . Finally we call "normalized confusion matrix" the matrix of conditional probabilities $(\mathbb {P} ({\hat {y}}=j\mid y=i))_{i,j}=\left({\frac {n_{i,j}}{n_{i.}}}\right)_{i,j}$ .

### Intuitive explanation

The lift is a way of measuring the deviation from independence of two events A and B  :

$\mathrm {Lift} (A,B)={\frac {\mathbb {P} (A\cap B)}{\mathbb {P} (A)\mathbb {P} (B)}}={\frac {\mathbb {P} (A\mid B)}{\mathbb {P} (A)}}={\frac {\mathbb {P} (B\mid A)}{\mathbb {P} (B)}}$

We have $\mathrm {Lift} (A,B)>1$ if and only if events A and B occur simultaneously with a greater probability than if they were independent. In other words, if one of the two events occurs, the probability of observing the other event increases.

A first condition to satisfy is to have $\mathrm {Lift} (y=i,{\hat {y}}=i)\geq 1$ for any i . And the quality of a model (better or worse than chance) does not change if we over- or undersample the dataset, that is if we multiply each row $R_{i}$ of the confusion matrix by a constant $c_{i}$ . Thus the second condition is that the necessary and sufficient conditions for doing better than chance need only depend on the normalized confusion matrix.

The condition on lifts can be reformulated with One versus Rest binary models : for any i , we define the binary target variable $y_{i}$ which is the indicator of event $\{y=i\}$ , and the binary model ${\hat {y}}_{i}$ of $y_{i}$ which is the indicator of event $\{{\hat {y}}=i\}$ . Each of the ${\hat {y}}_{i}$ models is a "One versus Rest" model. $\mathrm {Lift} (y=i,{\hat {y}}=i)$ only depends on the events $\{y=i\}$ and $\{{\hat {y}}=i\}$ , so merging or not merging the other classes doesn't change its value. We therefore have $\mathrm {Lift} (y=i,{\hat {y}}=i)=\mathrm {Lift} (y_{i}=1,{\hat {y}}_{i}=1)$ and the first condition is that all binary One versus Rest models are better than chance.

#### Example

If $K=2$ and 2 is the class of interest , the normalized confusion matrix is ${\begin{pmatrix}\mathrm {specificity} &1-\mathrm {specificity} \\1-\mathrm {sensitivity} &\mathrm {sensitivity} \end{pmatrix}}$ and we have $\mathrm {Lift} (y=1,{\hat {y}}=1)-1={\frac {\mathbb {P} (y={\hat {y}}=1)}{\lambda _{1}\mu _{1}}}-1={\frac {n_{1,1}n}{n_{1.}n_{.1}}}-1$ $={\frac {n_{1,1}(n_{1,1}+n_{1,2}+n_{2,1}+n_{2,2})-(n_{1,1}+n_{1,2})(n_{1,1}+n_{2,1})}{n_{1.}n_{.1}}}={\frac {n_{1,1}n_{2,2}-n_{1,2}n_{2,1}}{n_{1.}n_{.1}}}$ . Thus $\mathrm {Lift} (y=1,{\hat {y}}=1)\geq 1\iff n_{1,1}n_{2,2}-n_{1,2}n_{2,1}\geq 0$ . Similarly, by swapping the roles of 1 and 2, we find that $\mathrm {Lift} (y=2,{\hat {y}}=2)\geq 1\iff n_{1,1}n_{2,2}-n_{1,2}n_{2,1}\geq 0$ . Dividing by $n_{1.}n_{2.}$ we find that the necessary and sufficient condition on the normalized confusion matrix is $\mathrm {sensitivity} \ \mathrm {specificity} -(1-\mathrm {sensitivity} )(1-\mathrm {specificity} )\geq 0\iff \mathrm {sensitivity} +\mathrm {specificity} -1\geq 0\iff J\geq 0$ . This brings us back to the classical binary condition: Youden's J must be positive (or zero for random models).

### Random models

A random model is a model that is independent of the target variable. This property is easily reformulated with the confusion matrix.

**Proposition**—The model ${\hat {y}}$ of y is random if and only if the confusion matrix is of rank 1.

Proof

${\hat {y}}$ is a random model of y if and only if we have $\mathbb {P} (\{y=i\}\cap \{{\hat {y}}=j\})=\mathbb {P} (y=i)\mathbb {P} ({\hat {y}}=j)$ for any i and j , which is equivalent to $n_{i,j}n=n_{i.}n_{.j}$ for any i and j . All the columns of the confusion matrix are then proportional to the non-zero vector $(n_{i.})_{i}$ , which implies that the confusion matrix is of rank 1.

Conversely, if this matrix is of rank 1, the non-zero columns of the matrix are proportional to each other, and therefore proportional to their sum $(n_{i.})_{i}$ . So there exists a family of numbers $(\beta _{j})_{j}$ such that $n_{i,j}=n_{i.}\beta _{j}$ for any i and j . Summing this equations over i gives $n_{.j}=\beta _{j}n$ , hence $n_{i,j}n=n_{i.}n_{.j}$ for any i and j .

This proposition shows that the model ${\hat {y}}$ of y is uninformative if and only if there are two families of numbers $(\alpha _{i})_{i}$ and $(\beta _{j})_{j}$ such that $\mathbb {P} (\{y=i\}\cap \{{\hat {y}}=j\})=\alpha _{i}\beta _{j}$ for any i and j .

### Multiclass likelihood ratios and diagnostic odds ratios

We define generalized likelihood ratios calculated from the normalized confusion matrix: for any i and $j\not =i$ , let $\mathrm {LR} _{i,j}={\frac {\mathbb {P} ({\hat {y}}=j\mid y=j)}{\mathbb {P} ({\hat {y}}=j\mid y=i)}}$ . When $K=2$ , if 2 is the class of interest,, we find the classical likelihood ratios $\mathrm {LR} _{1,2}=\mathrm {LR} _{+}$ and $\mathrm {LR} _{2,1}={\frac {1}{\mathrm {LR} _{-}}}$ . Multiclass diagnostic odds ratios can also be defined using the formula $\mathrm {DOR} _{i,j}=\mathrm {DOR} _{j,i}=\mathrm {LR} _{i,j}\mathrm {LR} _{j,i}={\frac {n_{i,i}n_{j,j}}{n_{i,j}n_{j,i}}}={\frac {\mathbb {P} ({\hat {y}}=j\mid y=j)/\mathbb {P} ({\hat {y}}=i\mid y=j)}{\mathbb {P} ({\hat {y}}=j\mid y=i)/\mathbb {P} ({\hat {y}}=i\mid y=i)}}$

**Theorem**—For any j ,

$\mathbb {P} ({\hat {y}}=j\mid y=j)-\mu _{j}=\sum _{i}\lambda _{i}(\mathbb {P} ({\hat {y}}=j\mid y=j)-\mathbb {P} ({\hat {y}}=j\mid y=i))$

Equivalently, if all $n_{i,j}$ are non-zero:

${\frac {1}{\mathrm {Lift} (y=j,{\hat {y}}=j)}}=\sum _{i}{\frac {\lambda _{i}}{\mathrm {LR} _{i,j}}}$

Proof

$\mathbb {P} ({\hat {y}}=j\mid y=j)-\mathbb {P} ({\hat {y}}=j)=\mathbb {P} ({\hat {y}}=j\mid y=j)-\sum _{i}\lambda _{i}\mathbb {P} ({\hat {y}}=j\mid y=i)$ $=\sum _{i}\lambda _{i}(\mathbb {P} ({\hat {y}}=j\mid y=j)-\mathbb {P} ({\hat {y}}=j\mid y=i))$ . By dividing by $\mathbb {P} ({\hat {y}}=j\mid y=j)$ and subtracting 1, we deduce the second formulation.

**Corollary**—If all probabilities $\mathbb {P} ({\hat {y}}=k\mid y=l)$ are fixed, for any i and j we have

$\lim _{\lambda _{i}\to 1}(\mathbb {P} ({\hat {y}}=j\mid y=j)-\mu _{j})=\mathbb {P} ({\hat {y}}=j\mid y=j)-\mathbb {P} ({\hat {y}}=j\mid y=i)$

Equivalently, if all $n_{i,j}$ are non-zero:

$\lim _{\lambda _{i}\to 1}\mathrm {Lift} (y=j,{\hat {y}}=j)=\mathrm {LR} _{i,j}$

We saw above that a better-than-chance model (or a random model) must verify $\mathrm {Lift} (y=i,{\hat {y}}=i)\geq 1$ for any i and $\lambda _{i}$ . According to the previous corollary, likelihood ratios are thus greater than or equal to 1. Conversely, if the likelihood ratios are greater than or equal to 1, the theorem shows that we have $\mathrm {Lift} (y=i,{\hat {y}}=i)\geq 1$ for any i and $\lambda _{i}$ .

### Definition of better-than-chance multiclass models

A model ${\hat {y}}$ of y outperforms chance if the following conditions are met:

- For any j , we have $\max _{i}\mathbb {P} ({\hat {y}}=j\mid y=i)=\mathbb {P} ({\hat {y}}=j\mid y=j)$ .
- There are i and j distinct such that $\mathbb {P} ({\hat {y}}=j\mid y=i)<\mathbb {P} ({\hat {y}}=j\mid y=j)$ .

If all the entries of the confusion matrix are non-zero, this means that all the likelihood ratios are greater than or equal to 1, and at least one of these inegalities is strict. A model that satisfies the first condition but not the second is random, since we then have $\mathbb {P} (\{{\hat {y}}=j\}\cap \{y=i\})=\mathbb {P} (y=i)\mathbb {P} ({\hat {y}}=j\mid y=i)=\mathbb {P} (y=i)\mathbb {P} ({\hat {y}}=j\mid y=j)=\alpha _{i}\beta _{j}$ for any i and j .

We can rewrite the first condition in a more familiar way, noting x the observed value of ${\hat {y}}$ , $\theta$ the value to be estimated of y and ${\hat {\theta }}(x)$ the set $argmax_{\theta }\mathbb {P} (x\mid \theta )$ : for any x we have $x\in {\hat {\theta }}(x)$ . We deduce that *a model is better-than-random or random if and only if it is a maximum likelihood estimator of the target variable*.

### Applications

#### Multiclass balanced accuracy

The performance of a better-than-chance model can be estimated using multiclass versions of metrics such as balanced accuracy or Youden's J .

**Definition**— $\mathrm {Balanced\ accuracy} ={\frac {1}{K}}\sum _{i}\mathbb {P} ({\hat {y}}=i\mid y=i)$ $\mathrm {J} ={\frac {1}{K-1}}(K\,\mathrm {balanced\ accuracy} -1)={\frac {1}{K-1}}\sum _{i}\mu _{i}(\mathrm {Lift} (y=i,{\hat {y}}=i)-1)$

If $\mathrm {balanced\ accuracy} =1$ , in other words $J=1$ , the model is perfect. And for any random model, we have $\mathrm {balanced\ accuracy} ={\frac {1}{K}}$ (if, for example, we draw a uniform random number from the K labels, we have exactly one chance in K of predicting the correct value of the target variable).

On a balanced data set ( $\lambda _{i}={\frac {1}{K}}$ for any i ), balanced accuracy is equal to the rate of well-classified observations. On any data set, if a model does better than chance, we have $J\geq 0$ and $\mathrm {balanced\ accuracy} \geq {\frac {1}{K}}$ . But the converse is not true when $K>2$ , as we can see from this example: the confusion matrix ${\begin{pmatrix}0&3&0\\1&2&0\\0&0&3\end{pmatrix}}$ is that of a bad model (=worse than chance) since $\mathrm {LR} _{2,1}=0$ . However, 5 of the 9 observations are correctly classified. This also shows that poor model performance on one of the modalities is not compensated for by good performance on the other modalities.

#### ROC space

The set of normalized confusion matrices is called the ROC space, a subspace of ${\mathopen {[}}0,1{\mathclose {]}}^{m^{2}}$ . If E denotes the subset of the ROC space made up of random models or models that do better than chance, one can show that the topological boundary of E is the set of elements of E for which at least one of the likelihood ratios is equal to 1. And random models are those models whose likelihood ratios are all equal to 1. When $K=2$ , the boundary between models that do better than chance and bad models is equal to the set of random models (see article on the roc curve for more details), but it is strictly larger as soon as $K>2$ . And if $K=3$ , we can calculate the volume occupied by bad models in the ROC space: they occupy 90% of this space, whereas it's only 50% when $K=2$ .

## General algorithmic strategies

The existing multi-class classification techniques can be categorised into

- transformation to binary
- extension from binary
- hierarchical classification.

### Transformation to binary

This section discusses strategies for reducing the problem of multiclass classification to multiple binary classification problems. It can be categorized into *one vs rest* and *one vs one*. The techniques developed based on reducing the multi-class problem into multiple binary problems can also be called problem transformation techniques.

#### One-vs.-rest

One-vs.-rest (OvR or *one-vs.-all*, OvA or *one-against-all*, OAA) strategy involves training a single classifier per class, with the samples of that class as positive samples and all other samples as negatives. This strategy requires the base classifiers to produce a real-valued score for its decision (see also scoring rule), rather than just a class label; discrete class labels alone can lead to ambiguities, where multiple classes are predicted for a single sample.

In pseudocode, the training algorithm for an OvR learner constructed from a binary classification learner L is as follows:

Inputs:

- L, a learner (training algorithm for binary classifiers)
- samples X
- labels y where yi ∈ {1, … K} is the label for the sample Xi

Output:

- a list of classifiers fk for k ∈ {1, …, K}

Procedure:

- For each k in {1, …, K}
  - Construct a new label vector z where *z**i* = *y**i* if *y**i* = *k* and *z**i* = 0 otherwise
  - Apply L to X, z to obtain fk

Making decisions means applying all classifiers to an unseen sample x and predicting the label k for which the corresponding classifier reports the highest confidence score:

${\hat {y}}={\underset {k\in \{1\ldots K\}}{\arg \!\max }}\;f_{k}(x)$

Although this strategy is popular, it is a heuristic that suffers from several problems. Firstly, the scale of the confidence values may differ between the binary classifiers. Second, even if the class distribution is balanced in the training set, the binary classification learners see unbalanced distributions because typically the set of negatives they see is much larger than the set of positives. However, empirical studies have shown one-vs-rest can perform competitively with more sophisticated multiclass methods.

#### One-vs.-one

In the *one-vs.-one* (OvO) reduction, one trains *K* (*K* − 1) / 2 binary classifiers for a K-way multiclass problem; each receives the samples of a pair of classes from the original training set, and must learn to distinguish these two classes. At prediction time, a voting scheme is applied: all *K* (*K* − 1) / 2 classifiers are applied to an unseen sample and the class that got the highest number of "+1" predictions gets predicted by the combined classifier.

Like OvR, OvO suffers from ambiguities in that some regions of its input space may receive the same number of votes.

### Extension from binary

This section discusses strategies of extending the existing binary classifiers to solve multi-class classification problems. Several algorithms have been developed based on neural networks, decision trees, k-nearest neighbors, naive Bayes, support vector machines and extreme learning machines to address multi-class classification problems. These types of techniques can also be called algorithm adaptation techniques.

#### Neural networks

Multiclass perceptrons provide a natural extension to the multi-class problem. Instead of just having one neuron in the output layer, with binary output, one could have N binary neurons leading to multi-class classification. In practice, the last layer of a neural network is usually a softmax function layer, which is the algebraic simplification of N logistic classifiers, normalized per class by the sum of the N-1 other logistic classifiers. Neural Network-based classification has brought significant improvements and scopes for thinking from different perspectives.

##### Extreme learning machines

Extreme learning machines (ELM) is a special case of single hidden layer feed-forward neural networks (SLFNs) wherein the input weights and the hidden node biases can be chosen at random. Many variants and developments are made to the ELM for multiclass classification.

#### k-nearest neighbours

k-nearest neighbors kNN is considered among the oldest non-parametric classification algorithms. To classify an unknown example, the distance from that example to every other training example is measured. The k smallest distances are identified, and the most represented class by these k nearest neighbours is considered the output class label.

#### Naive Bayes

Naive Bayes is a successful classifier based upon the principle of maximum a posteriori (MAP). This approach is naturally extensible to the case of having more than two classes, and was shown to perform well in spite of the underlying simplifying assumption of conditional independence.

#### Decision trees

Decision tree learning is a powerful classification technique. The tree tries to infer a split of the training data based on the values of the available features to produce a good generalization. The algorithm can naturally handle binary or multiclass classification problems. The leaf nodes can refer to any of the K classes concerned.

#### Support vector machines

Support vector machines are based upon the idea of maximizing the margin i.e. maximizing the minimum distance from the separating hyperplane to the nearest example. The basic SVM supports only binary classification, but extensions have been proposed to handle the multiclass classification case as well. In these extensions, additional parameters and constraints are added to the optimization problem to handle the separation of the different classes.

#### Multi expression programming

Multi expression programming (MEP) is an evolutionary algorithm for generating computer programs (that can be used for classification tasks too). MEP has a unique feature: it encodes multiple programs into a single chromosome. Each of these programs can be used to generate the output for a class, thus making MEP naturally suitable for solving multi-class classification problems.

### Hierarchical classification

Hierarchical classification tackles the multi-class classification problem by dividing the output space into a tree. Each parent node is divided into multiple child nodes and the process is continued until each child node represents only one class. Several methods have been proposed based on hierarchical classification.

## Learning paradigms

Based on learning paradigms, the existing multi-class classification techniques can be classified into batch learning and online learning. Batch learning algorithms require all the data samples to be available beforehand. It trains the model using the entire training data and then predicts the test sample using the found relationship. The online learning algorithms, on the other hand, incrementally build their models in sequential iterations. In iteration t, an online algorithm receives a sample, xt and predicts its label ŷt using the current model; the algorithm then receives yt, the true label of xt and updates its model based on the sample-label pair: (xt, yt). Recently, a new learning paradigm called progressive learning technique has been developed. The progressive learning technique is capable of not only learning from new samples but also capable of learning new classes of data and yet retain the knowledge learnt thus far.

## Evaluation

The performance of a multi-class classification system is often assessed by comparing the predictions of the system against reference labels with an evaluation metric. Common evaluation metrics are Accuracy or macro F1.
