---
title: "Actor-critic algorithm"
source: https://en.wikipedia.org/wiki/Actor-critic_algorithm
domain: actor-critic
license: CC-BY-SA-4.0
tags: actor critic method, policy gradient method, advantage estimation, value function
fetched: 2026-07-02
---

# Actor-critic algorithm

The **actor-critic algorithm** (AC) is a family of reinforcement learning (RL) algorithms that combine policy-based RL algorithms such as policy gradient methods, and value-based RL algorithms such as value iteration, Q-learning, SARSA, and TD learning.

An AC algorithm consists of two main components: an "**actor**" that determines which actions to take according to a policy function, and a "**critic**" that evaluates those actions according to a value function. Some AC algorithms are on-policy, some are off-policy. Some apply to either continuous or discrete action spaces. Some work in both cases.

## Overview

The actor-critic methods can be understood as an improvement over pure policy gradient methods like REINFORCE via introducing a baseline.

### Actor

The **actor** uses a policy function $\pi (a|s)$ , while the critic estimates either the value function $V(s)$ , the action-value Q-function $Q(s,a),$ the advantage function $A(s,a)$ , or any combination thereof.

The actor is a parameterized function $\pi _{\theta }$ , where $\theta$ are the parameters of the actor. The actor takes as argument the state of the environment s and produces a probability distribution $\pi _{\theta }(\cdot |s)$ .

If the action space is discrete, then $\sum _{a}\pi _{\theta }(a|s)=1$ . If the action space is continuous, then $\int _{a}\pi _{\theta }(a|s)da=1$ .

The goal of policy optimization is to improve the actor. That is, to find some $\theta$ that maximizes the expected episodic reward $J(\theta )$ : $J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{t=0}^{T}\gamma ^{t}r_{t}\right]$ where $\gamma$ is the discount factor, $r_{t}$ is the reward at step t , and T is the time-horizon (which can be infinite).

The goal of policy gradient method is to optimize $J(\theta )$ by gradient ascent on the policy gradient $\nabla J(\theta )$ .

As detailed on the policy gradient method page, there are many unbiased estimators of the policy gradient: $\nabla _{\theta }J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{0\leq j\leq T}\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})\cdot \Psi _{j}{\Big |}S_{0}=s_{0}\right]$ where ${\textstyle \Psi _{j}}$ is a linear sum of the following:

- ${\textstyle \sum _{0\leq i\leq T}(\gamma ^{i}R_{i})}$ .
- ${\textstyle \gamma ^{j}\sum _{j\leq i\leq T}(\gamma ^{i-j}R_{i})}$ : the **REINFORCE** algorithm.
- ${\textstyle \gamma ^{j}\sum _{j\leq i\leq T}(\gamma ^{i-j}R_{i})-b(S_{j})}$ : the **REINFORCE with baseline** algorithm. Here b is an arbitrary function.
- ${\textstyle \gamma ^{j}\left(R_{j}+\gamma V^{\pi _{\theta }}(S_{j+1})-V^{\pi _{\theta }}(S_{j})\right)}$ : TD(1) learning.
- ${\textstyle \gamma ^{j}Q^{\pi _{\theta }}(S_{j},A_{j})}$ .
- ${\textstyle \gamma ^{j}A^{\pi _{\theta }}(S_{j},A_{j})}$ : **Advantage Actor-Critic (A2C)**.
- ${\textstyle \gamma ^{j}\left(R_{j}+\gamma R_{j+1}+\gamma ^{2}V^{\pi _{\theta }}(S_{j+2})-V^{\pi _{\theta }}(S_{j})\right)}$ : TD(2) learning.
- ${\textstyle \gamma ^{j}\left(\sum _{k=0}^{n-1}\gamma ^{k}R_{j+k}+\gamma ^{n}V^{\pi _{\theta }}(S_{j+n})-V^{\pi _{\theta }}(S_{j})\right)}$ : TD(n) learning.
- ${\textstyle \gamma ^{j}\sum _{n=1}^{\infty }{\frac {\lambda ^{n-1}}{1-\lambda }}\cdot \left(\sum _{k=0}^{n-1}\gamma ^{k}R_{j+k}+\gamma ^{n}V^{\pi _{\theta }}(S_{j+n})-V^{\pi _{\theta }}(S_{j})\right)}$ : TD(λ) learning, also known as **GAE (generalized advantage estimate)**. This is obtained by an exponentially decaying sum of the TD(n) learning terms.

### Critic

In the unbiased estimators given above, certain functions such as $V^{\pi _{\theta }},Q^{\pi _{\theta }},A^{\pi _{\theta }}$ appear. These are approximated by the **critic**. Since these functions all depend on the actor, the critic must learn alongside the actor. The critic is learned by value-based RL algorithms.

For example, if the critic is estimating the state-value function $V^{\pi _{\theta }}(s)$ , then it can be learned by any value function approximation method. Let the critic be a function approximator $V_{\phi }(s)$ with parameters $\phi$ .

The simplest example is TD(1) learning, which trains the critic to minimize the TD(1) error: $\delta _{i}=R_{i}+\gamma V_{\phi }(S_{i+1})-V_{\phi }(S_{i})$ The critic parameters are updated by gradient descent on the squared TD error: $\phi \leftarrow \phi -\alpha \nabla _{\phi }(\delta _{i})^{2}=\phi +\alpha \delta _{i}\nabla _{\phi }V_{\phi }(S_{i})$ where $\alpha$ is the learning rate. Note that the gradient is taken with respect to the $\phi$ in $V_{\phi }(S_{i})$ only, since the $\phi$ in $\gamma V_{\phi }(S_{i+1})$ constitutes a moving target, and the gradient is not taken with respect to that. This is a common source of error in implementations that use automatic differentiation, and requires "stopping the gradient" at that point.

Similarly, if the critic is estimating the action-value function $Q^{\pi _{\theta }}$ , then it can be learned by Q-learning or SARSA. In SARSA, the critic maintains an estimate of the Q-function, parameterized by $\phi$ , denoted as $Q_{\phi }(s,a)$ . The temporal difference error is then calculated as $\delta _{i}=R_{i}+\gamma Q_{\theta }(S_{i+1},A_{i+1})-Q_{\theta }(S_{i},A_{i})$ . The critic is then updated by $\theta \leftarrow \theta +\alpha \delta _{i}\nabla _{\theta }Q_{\theta }(S_{i},A_{i})$ The advantage critic can be trained by training both a Q-function $Q_{\phi }(s,a)$ and a state-value function $V_{\phi }(s)$ , then let $A_{\phi }(s,a)=Q_{\phi }(s,a)-V_{\phi }(s)$ . Although, it is more common to train just a state-value function $V_{\phi }(s)$ , then estimate the advantage by $A_{\phi }(S_{i},A_{i})\approx \sum _{j\in 0:n-1}\gamma ^{j}R_{i+j}+\gamma ^{n}V_{\phi }(S_{i+n})-V_{\phi }(S_{i})$ Here, n is a positive integer. The higher n is, the more lower is the bias in the advantage estimation, but at the price of higher variance.

The **Generalized Advantage Estimation (GAE)** introduces a hyperparameter $\lambda$ that smoothly interpolates between Monte Carlo returns ( $\lambda =1$ , high variance, no bias) and 1-step TD learning ( $\lambda =0$ , low variance, high bias). This hyperparameter can be adjusted to pick the optimal bias-variance trade-off in advantage estimation. It uses an exponentially decaying average of n-step returns with $\lambda$ being the decay strength.

## Variants

- **Asynchronous Advantage Actor-Critic (A3C)**: Parallel and asynchronous version of A2C.
- **Soft Actor-Critic (SAC)**: Incorporates entropy maximization for improved exploration.
- **Deep Deterministic Policy Gradient (DDPG)**: Specialized for continuous action spaces.
