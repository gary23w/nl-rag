---
title: "Sample complexity"
source: https://en.wikipedia.org/wiki/Sample_complexity
domain: learning-theory-pac
license: CC-BY-SA-4.0
tags: probably approximately correct, sample complexity, pac learnable, concept class
fetched: 2026-07-02
---

# Sample complexity

The **sample complexity** of a machine learning algorithm represents the number of training-samples that it needs in order to successfully learn a target function.

More precisely, the sample complexity is the number of training-samples that we need to supply to the algorithm, so that the function returned by the algorithm is within an arbitrarily small error of the best possible function, with probability arbitrarily close to 1.

There are two variants of sample complexity:

- The weak variant fixes a particular input-output distribution;
- The strong variant takes the worst-case sample complexity over all input-output distributions.

The No free lunch theorem, discussed below, proves that, in general, the strong sample complexity is infinite, i.e. that there is no algorithm that can learn the globally-optimal target function using a finite number of training samples.

However, if we are only interested in a particular class of target functions (e.g., only linear functions) then the sample complexity is finite, and it depends linearly on the VC dimension on the class of target functions.

## Definition

Let X be a space which we call the input space, and Y be a space which we call the output space, and let Z denote the product $X\times Y$ . For example, in the setting of binary classification, X is typically a finite-dimensional vector space and Y is the set $\{-1,1\}$ .

Fix a hypothesis space ${\mathcal {H}}$ of functions $h\colon X\to Y$ . A learning algorithm over ${\mathcal {H}}$ is a computable map from Z to ${\mathcal {H}}$ . In other words, it is an algorithm that takes as input a finite sequence of training samples and outputs a function from X to Y . Typical learning algorithms include empirical risk minimization, without or with Tikhonov regularization.

Fix a loss function ${\mathcal {L}}\colon Y\times Y\to \mathbb {R} _{\geq 0}$ , for example, the square loss ${\mathcal {L}}(y,y')=(y-y')^{2}$ , where $h(x)=y'$ . For a given distribution $\rho$ on $X\times Y$ , the **expected risk** of a hypothesis (a function) $h\in {\mathcal {H}}$ is

${\mathcal {E}}(h):=\mathbb {E} _{\rho }[{\mathcal {L}}(h(x),y)]=\int _{X\times Y}{\mathcal {L}}(h(x),y)\,d\rho (x,y)$

In our setting, we have $h={\mathcal {A}}(S_{n})$ , where ${\mathcal {A}}$ is a learning algorithm and $S_{n}=((x_{1},y_{1}),\ldots ,(x_{n},y_{n}))\sim \rho ^{n}$ is a sequence of vectors which are all drawn independently from $\rho$ . Define the optimal risk ${\mathcal {E}}_{\mathcal {H}}^{*}={\underset {h\in {\mathcal {H}}}{\inf }}{\mathcal {E}}(h).$ Set $h_{n}={\mathcal {A}}(S_{n})$ , for each sample size n . $h_{n}$ is a random variable and depends on the random variable $S_{n}$ , which is drawn from the distribution $\rho ^{n}$ . The algorithm ${\mathcal {A}}$ is called **consistent** if ${\mathcal {E}}(h_{n})$ probabilistically converges to ${\mathcal {E}}_{\mathcal {H}}^{*}$ . In other words, for all $\epsilon ,\delta >0$ , there exists a positive integer N , such that, for all sample sizes $n\geq N$ , we have

$\Pr _{\rho ^{n}}[{\mathcal {E}}(h_{n})-{\mathcal {E}}_{\mathcal {H}}^{*}\geq \varepsilon ]<\delta .$ The **sample complexity** of ${\mathcal {A}}$ is then the minimum N for which this holds, as a function of $\rho ,\epsilon$ , and $\delta$ . We write the sample complexity as $N(\rho ,\epsilon ,\delta )$ to emphasize that this value of N depends on $\rho ,\epsilon$ , and $\delta$ . If ${\mathcal {A}}$ is **not consistent**, then we set $N(\rho ,\epsilon ,\delta )=\infty$ . If there exists an algorithm for which $N(\rho ,\epsilon ,\delta )$ is finite, then we say that the hypothesis space ${\mathcal {H}}$ is **learnable**.

In others words, the sample complexity $N(\rho ,\epsilon ,\delta )$ defines the rate of consistency of the algorithm: given a desired accuracy $\epsilon$ and confidence $\delta$ , one needs to sample $N(\rho ,\epsilon ,\delta )$ data points to guarantee that the risk of the output function is within $\epsilon$ of the best possible, with probability at least $1-\delta$ .

In probably approximately correct (PAC) learning, one is concerned with whether the sample complexity is *polynomial*, that is, whether $N(\rho ,\epsilon ,\delta )$ is bounded by a polynomial in $1/\epsilon$ and $1/\delta$ . If $N(\rho ,\epsilon ,\delta )$ is polynomial for some learning algorithm, then one says that the hypothesis space ${\mathcal {H}}$ is **PAC-learnable**. This is a stronger notion than being learnable.

## Unrestricted hypothesis space: infinite sample complexity

One can ask whether there exists a learning algorithm so that the sample complexity is finite in the strong sense, that is, there is a bound on the number of samples needed so that the algorithm can learn any distribution over the input-output space with a specified target error. More formally, one asks whether there exists a learning algorithm ${\mathcal {A}}$ , such that, for all $\epsilon ,\delta >0$ , there exists a positive integer N such that for all $n\geq N$ , we have

$\sup _{\rho }\left(\Pr _{\rho ^{n}}[{\mathcal {E}}(h_{n})-{\mathcal {E}}_{\mathcal {H}}^{*}\geq \varepsilon ]\right)<\delta ,$ where $h_{n}={\mathcal {A}}(S_{n})$ , with $S_{n}=((x_{1},y_{1}),\ldots ,(x_{n},y_{n}))\sim \rho ^{n}$ as above. The No Free Lunch Theorem says that without restrictions on the hypothesis space ${\mathcal {H}}$ , this is not the case, i.e., there always exist "bad" distributions for which the sample complexity is arbitrarily large.

Thus, in order to make statements about the rate of convergence of the quantity $\sup _{\rho }\left(\Pr _{\rho ^{n}}[{\mathcal {E}}(h_{n})-{\mathcal {E}}_{\mathcal {H}}^{*}\geq \varepsilon ]\right),$ one must either

- constrain the space of probability distributions $\rho$ , e.g. via a parametric approach, or
- constrain the space of hypotheses ${\mathcal {H}}$ , as in distribution-free approaches.

## Restricted hypothesis space: finite sample-complexity

The latter approach leads to concepts such as VC dimension and Rademacher complexity which control the complexity of the space ${\mathcal {H}}$ . A smaller hypothesis space introduces more bias into the inference process, meaning that ${\mathcal {E}}_{\mathcal {H}}^{*}$ may be greater than the best possible risk in a larger space. However, by restricting the complexity of the hypothesis space it becomes possible for an algorithm to produce more uniformly consistent functions. This trade-off leads to the concept of regularization.

It is a theorem from VC theory that the following three statements are equivalent for a hypothesis space ${\mathcal {H}}$ :

1. ${\mathcal {H}}$ is PAC-learnable.
2. The VC dimension of ${\mathcal {H}}$ is finite.
3. ${\mathcal {H}}$ is a uniform Glivenko-Cantelli class.

This gives a way to prove that certain hypothesis spaces are PAC learnable, and by extension, learnable.

### An example of a PAC-learnable hypothesis space

$X=\mathbb {R} ^{d},Y=\{-1,1\}$ , and let ${\mathcal {H}}$ be the space of affine functions on X , that is, functions of the form $x\mapsto \langle w,x\rangle +b$ for some $w\in \mathbb {R} ^{d},b\in \mathbb {R}$ . This is the linear classification with offset learning problem. Now, four coplanar points in a square cannot be shattered by any affine function, since no affine function can be positive on two diagonally opposite vertices and negative on the remaining two. Thus, the VC dimension of ${\mathcal {H}}$ is $d+1$ , so it is finite. It follows by the above characterization of PAC-learnable classes that ${\mathcal {H}}$ is PAC-learnable, and by extension, learnable.

### Sample-complexity bounds

Suppose ${\mathcal {H}}$ is a class of binary functions (functions to $\{0,1\}$ ). Then, ${\mathcal {H}}$ is $(\epsilon ,\delta )$ -PAC-learnable with a sample of size: $N=O{\bigg (}{\frac {VC({\mathcal {H}})+\ln {1 \over \delta }}{\epsilon }}{\bigg )}$ where $VC({\mathcal {H}})$ is the VC dimension of ${\mathcal {H}}$ . Moreover, any $(\epsilon ,\delta )$ -PAC-learning algorithm for ${\mathcal {H}}$ must have sample-complexity: $N=\Omega {\bigg (}{\frac {VC({\mathcal {H}})+\ln {1 \over \delta }}{\epsilon }}{\bigg )}$ Thus, the sample-complexity is a linear function of the VC dimension of the hypothesis space.

Suppose ${\mathcal {H}}$ is a class of real-valued functions with range in $[0,T]$ . Then, ${\mathcal {H}}$ is $(\epsilon ,\delta )$ -PAC-learnable with a sample of size: $N=O{\bigg (}T^{2}{\frac {PD({\mathcal {H}})\ln {T \over \epsilon }+\ln {1 \over \delta }}{\epsilon ^{2}}}{\bigg )}$ where $PD({\mathcal {H}})$ is Pollard's pseudo-dimension of ${\mathcal {H}}$ .

## Other settings

In addition to the supervised learning setting, sample complexity is relevant to semi-supervised learning problems including active learning, where the algorithm can ask for labels to specifically chosen inputs in order to reduce the cost of obtaining many labels. The concept of sample complexity also shows up in reinforcement learning, online learning, and unsupervised algorithms, e.g. for dictionary learning.

## Efficiency in robotics

A high sample complexity means that many calculations are needed for running a Monte Carlo tree search. It is equivalent to a model-free brute force search in the state space. In contrast, a high-efficiency algorithm has a low sample complexity. Possible techniques for reducing the sample complexity are metric learning and model-based reinforcement learning.
