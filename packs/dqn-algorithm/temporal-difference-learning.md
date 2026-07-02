---
title: "Temporal difference learning"
source: https://en.wikipedia.org/wiki/Temporal_difference_learning
domain: dqn-algorithm
license: CC-BY-SA-4.0
tags: deep q network, value based learning, experience replay, temporal difference
fetched: 2026-07-02
---

# Temporal difference learning

**Temporal difference** (**TD**) **learning** refers to a class of model-free reinforcement learning methods which learn by bootstrapping from the current estimate of the value function. These methods sample from the environment, like Monte Carlo methods, and perform updates based on current estimates, like dynamic programming methods.

While Monte Carlo methods only adjust their estimates once the outcome is known, TD methods adjust predictions to match later, more-accurate predictions about the future, before the outcome is known. This is a form of bootstrapping, as illustrated with the following example:

> Suppose you wish to predict the weather for Saturday, and you have some model that predicts Saturday's weather, given the weather of each day in the week. In the standard case, you would wait until Saturday and then adjust all your models. However, when it is, for example, Friday, you should have a pretty good idea of what the weather would be on Saturday – and thus be able to change, say, Saturday's model before Saturday arrives.

Temporal difference methods are related to the temporal difference model of animal learning.

## Mathematical formulation

The tabular TD(0) method is one of the simplest TD methods. It is a special case of more general stochastic approximation methods. It estimates the state value function of a finite-state Markov decision process (MDP) under a policy $\pi$ . Let $V^{\pi }$ denote the state value function of the MDP with states $(S_{t})_{t\in \mathbb {N} }$ , rewards $(R_{t})_{t\in \mathbb {N} }$ and discount rate $\gamma$ under the policy $\pi$ :

$V^{\pi }(s)=E_{a\sim \pi }\left\{\sum _{t=0}^{\infty }\gamma ^{t}R_{t+1}{\Bigg |}S_{0}=s\right\}.$

We drop the action from the notation for convenience. $V^{\pi }$ satisfies the Bellman Equation:

$V^{\pi }(s)=E_{\pi }\{R_{1}+\gamma V^{\pi }(S_{1})|S_{0}=s\},$

so $R_{1}+\gamma V^{\pi }(S_{1})$ is an unbiased estimate for $V^{\pi }(s)$ . This observation motivates the following algorithm for estimating $V^{\pi }$ .

The algorithm starts by initializing a table $V(s)$ arbitrarily, with one value for each state of the MDP. A positive learning rate $\alpha$ is chosen.

We then repeatedly evaluate the policy $\pi$ , obtain a reward r and update the value function for the current state using the rule:

$V(S_{t})\leftarrow (1-\alpha )V(S_{t})+\underbrace {\alpha } _{\text{learning rate}}[\overbrace {R_{t+1}+\gamma V(S_{t+1})} ^{\text{The TD target}}]$

where $S_{t}$ and $S_{t+1}$ are the current and next states, respectively. The value $R_{t+1}+\gamma V(S_{t+1})$ is known as the TD target, and $R_{t+1}+\gamma V(S_{t+1})-V(S_{t})$ is known as the TD error.

## TD-Lambda

**TD-Lambda** is a learning algorithm invented by Richard S. Sutton based on earlier work on temporal difference learning by Arthur Samuel. This algorithm was famously applied by Gerald Tesauro to create TD-Gammon, a program that learned to play the game of backgammon at the level of expert human players.

The lambda ( $\lambda$ ) parameter refers to the trace decay parameter, with $0\leqslant \lambda \leqslant 1$ . Higher settings lead to longer lasting traces; that is, a larger proportion of credit from a reward can be given to more distant states and actions when $\lambda$ is higher, with $\lambda =1$ producing parallel learning to Monte Carlo RL algorithms.

## In neuroscience

The TD algorithm has also received attention in the field of neuroscience. Researchers discovered that the firing rate of dopamine neurons in the ventral tegmental area (VTA) and substantia nigra (SNc) appear to mimic the error function in the algorithm. The error function reports back the difference between the estimated reward at any given state or time step and the actual reward received. The larger the error function, the larger the difference between the expected and actual reward. When this is paired with a stimulus that accurately reflects a future reward, the error can be used to associate the stimulus with the future reward.

Dopamine cells appear to behave in a similar manner. In one experiment measurements of dopamine cells were made while training a monkey to associate a stimulus with the reward of juice. Initially the dopamine cells increased firing rates when the monkey received juice, indicating a difference in expected and actual rewards. Over time this increase in firing back propagated to the earliest reliable stimulus for the reward. Once the monkey was fully trained, there was no increase in firing rate upon presentation of the predicted reward. Subsequently, the firing rate for the dopamine cells decreased below normal activation when the expected reward was not produced. This mimics closely how the error function in TD is used for reinforcement learning.

The relationship between the model and potential neurological function has produced research attempting to use TD to explain many aspects of behavioral research. It has also been used to study conditions such as schizophrenia or the consequences of pharmacological manipulations of dopamine on learning.
