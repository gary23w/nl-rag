---
title: "Policy gradient method"
source: https://en.wikipedia.org/wiki/Policy_gradient_method
domain: ppo-algorithm
license: CC-BY-SA-4.0
tags: proximal policy optimization, policy gradient method, on policy learning, reinforcement learning
fetched: 2026-07-02
---

# Policy gradient method

**Policy gradient methods** are a class of reinforcement learning algorithms and a sub-class of policy optimization methods. Unlike value-based methods which learn a value function to derive a policy, policy optimization methods directly learn a policy function $\pi$ that selects actions without consulting a value function. For policy gradient to apply, the policy function $\pi _{\theta }$ is parameterized by a differentiable parameter $\theta$ .

## Overview

In policy-based RL, the actor is a parameterized policy function $\pi _{\theta }$ , where $\theta$ are the parameters of the actor. The actor takes as argument the state of the environment s and produces a probability distribution $\pi _{\theta }(\cdot \mid s)$ .

If the action space is discrete, then $\sum _{a}\pi _{\theta }(a\mid s)=1$ . If the action space is continuous, then $\int _{a}\pi _{\theta }(a\mid s)\mathrm {d} a=1$ .

The goal of policy optimization is to find some $\theta$ that maximizes the expected episodic reward $J(\theta )$ : $J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{t=0}^{T}\gamma ^{t}R_{t}{\Big |}S_{0}=s_{0}\right]$ where $\gamma$ is the discount factor, $R_{t}$ is the reward at step t , $s_{0}$ is the starting state, and T is the time-horizon (which can be infinite).

The **policy gradient** is defined as $\nabla _{\theta }J(\theta )$ . Different policy gradient methods stochastically estimate the policy gradient in different ways. The goal of any policy gradient method is to iteratively maximize $J(\theta )$ by gradient ascent. Since the key part of any policy gradient method is the stochastic estimation of the policy gradient, they are also studied under the title of "Monte Carlo gradient estimation".

## REINFORCE

### Policy gradient

The **REINFORCE algorithm**, introduced by Ronald J. Williams in 1992, was the first policy gradient method. It is based on the identity for the policy gradient $\nabla _{\theta }J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{t=0}^{T}\nabla _{\theta }\ln \pi _{\theta }(A_{t}\mid S_{t})\;\sum _{t=0}^{T}(\gamma ^{t}R_{t}){\Big |}S_{0}=s_{0}\right]$ which can be improved via the "causality trick", i.e. by only weighting each action by rewards from that timestep onward, $\nabla _{\theta }J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{t=0}^{T}\nabla _{\theta }\ln \pi _{\theta }(A_{t}\mid S_{t})\sum _{\tau =t}^{T}(\gamma ^{\tau }R_{\tau }){\Big |}S_{0}=s_{0}\right]$

**Lemma**—The expectation of the score function is zero, conditional on any present or past state. That is, for any $0\leq i\leq j\leq T$ and any state $s_{i}$ , we have $\mathbb {E} _{\pi _{\theta }}[\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})|S_{i}=s_{i}]=0.$

Further, if ${\textstyle \Psi _{i}}$ is a random variable that is independent of ${\textstyle A_{i},S_{i+1},A_{i+1},\dots }$ , then $\mathbb {E} _{\pi _{\theta }}[\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})\cdot \Psi _{i}|S_{i}=s_{i}]=0.$

Proofs

Proof of the lemma

Use the reparameterization trick.

${\begin{aligned}\mathbb {E} _{\pi _{\theta }}[\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})|S_{i}=s_{i}]&=\sum _{s}Pr(S_{j}=s|S_{i}=s_{i})\sum _{a}\pi _{\theta }(a|s)\nabla _{\theta }\ln \pi _{\theta }(a|s)\\&=\sum _{s}Pr(S_{j}=s|S_{i}=s_{i})\sum _{a}\pi _{\theta }(a|s){\frac {\nabla _{\theta }\pi _{\theta }(a|s)}{\pi _{\theta }(a|s)}}\\&=\sum _{s}Pr(S_{j}=s|S_{i}=s_{i})\sum _{a}\nabla _{\theta }\pi _{\theta }(a|s)\\&=\sum _{s}Pr(S_{j}=s|S_{i}=s_{i})\nabla _{\theta }\sum _{a}\pi _{\theta }(a|s)\end{aligned}}$ Since the policy $\pi _{\theta }(a|s)$ is a probability distribution over actions for a given state, ${\textstyle \sum _{a}\pi _{\theta }(a|s)=1}$ . ${\begin{aligned}\mathbb {E} _{\pi _{\theta }}[\nabla _{\theta }\ln \pi _{\theta }(A|S)]&=\sum _{s}Pr(S_{j}=s|S_{i}=s_{i})\nabla _{\theta }(1)\\&=\sum _{s}Pr(S_{j}=s|S_{i}=s_{i})0\\&=0\end{aligned}}$

By the tower law and the previous lemma.

${\begin{aligned}\mathbb {E} _{\pi _{\theta }}\left[\Psi _{i}\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j}){\Big |}S_{i}=s_{i}\right]&=\mathbb {E} _{\pi _{\theta }}\left[\mathbb {E} _{\pi _{\theta }}[\Psi _{i}\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})|S_{j}]{\Big |}S_{i}=s_{i}\right]\\&=\mathbb {E} _{\pi _{\theta }}\left[\Psi _{i}\mathbb {E} _{\pi _{\theta }}[\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})|S_{j}]{\Big |}S_{i}=s_{i}\right]\\&=\mathbb {E} _{\pi _{\theta }}\left[\Psi _{i}0{\Big |}S_{i}=s_{i}\right]\\&=0\end{aligned}}$

Proof of the two identities

Applying the reparameterization trick,

${\begin{aligned}\nabla _{\theta }J(\theta )&=\nabla _{\theta }\mathbb {E} _{\pi _{\theta }}\left[\sum _{i\in 0:T}\gamma ^{i}R_{i}{\Big |}S_{0}=s_{0}\right]\\&=\mathbb {E} _{\pi _{\theta }}\left[\left(\sum _{i\in 0:T}\gamma ^{i}R_{i}\right)\nabla _{\theta }\ln(\pi _{\theta }(A_{0},A_{1},\dots ,A_{T}|S_{0},S_{1},\dots ,S_{T})){\Big |}S_{0}=s_{0}\right]\\&=\mathbb {E} _{\pi _{\theta }}\left[\left(\sum _{i\in 0:T}\gamma ^{i}R_{i}\right)\sum _{j\in 0:T}\nabla _{\theta }\ln(\pi _{\theta }(A_{j}|S_{j})){\Big |}S_{0}=s_{0}\right]\\&=\mathbb {E} _{\pi _{\theta }}\left[\sum _{i,j\in 0:T}(\gamma ^{i}R_{i})\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j}){\Big |}S_{0}=s_{0}\right]\end{aligned}}$ which is the first equation.

By the lemma, $\mathbb {E} _{\pi _{\theta }}\left[(\gamma ^{i}R_{i})\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j}){\Big |}S_{0}=s_{0}\right]=0$ for any ${\textstyle 0\leq i<j\leq T}$ . Plugging this into the previous formula, we zero out a whole triangle of terms, to get ${\begin{aligned}\nabla _{\theta }J(\theta )&=\mathbb {E} _{\pi _{\theta }}\left[\sum _{0\leq j\leq i\leq T}(\gamma ^{i}R_{i})\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j}){\Big |}S_{0}=s_{0}\right]\\&=\mathbb {E} _{\pi _{\theta }}\left[\sum _{j\in 0:T}\nabla _{\theta }\ln \pi _{\theta }(A_{j}|S_{j})\sum _{i\in j:T}(\gamma ^{i}R_{i}){\Big |}S_{0}=s_{0}\right]\end{aligned}}$ which is the second equation.

Thus, we have an unbiased estimator of the policy gradient: $\nabla _{\theta }J(\theta )\approx {\frac {1}{N}}\sum _{n=1}^{N}\left[\sum _{t=0}^{T}\nabla _{\theta }\ln \pi _{\theta }(A_{t,n}\mid S_{t,n})\sum _{\tau =t}^{T}(\gamma ^{\tau -t}R_{\tau ,n})\right]$ where the index n ranges over N rollout trajectories using the policy $\pi _{\theta }$ .

The score function $\nabla _{\theta }\ln \pi _{\theta }(A_{t}\mid S_{t})$ can be interpreted as the direction in the parameter space that increases the probability of taking action $A_{t}$ in state $S_{t}$ . The policy gradient, then, is a weighted average of all possible directions to increase the probability of taking any action in any state, but weighted by reward signals, so that if taking a certain action in a certain state is associated with high reward, then that direction would be highly reinforced, and vice versa.

### Algorithm

The REINFORCE algorithm is a loop:

1. Rollout N trajectories in the environment, using $\pi _{\theta _{t}}$ as the policy function.
2. Compute the policy gradient estimation: $g_{i}\leftarrow {\frac {1}{N}}\sum _{n=1}^{N}\left[\sum _{t=0}^{T}\nabla _{\theta _{t}}\ln \pi _{\theta }(A_{t,n}\mid S_{t,n})\sum _{\tau =t}^{T}(\gamma ^{\tau }R_{\tau ,n})\right]$
3. Update the policy by gradient ascent: $\theta _{i+1}\leftarrow \theta _{i}+\alpha _{i}g_{i}$

Here, $\alpha _{i}$ is the learning rate at update step i .

## Variance reduction

REINFORCE is an **on-policy** algorithm, meaning that the trajectories used for the update must be sampled from the current policy $\pi _{\theta }$ . This can lead to high variance in the updates, as the returns $R(\tau )$ can vary significantly between trajectories. Many variants of REINFORCE have been introduced, under the title of **variance reduction**.

### REINFORCE with baseline

A common way for reducing variance is the **REINFORCE with baseline** algorithm, based on the following identity: $\nabla _{\theta }J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{t=0}^{T}\nabla _{\theta }\ln \pi _{\theta }(A_{t}|S_{t})\left(\sum _{\tau =t}^{T}(\gamma ^{\tau }R_{\tau })-b(S_{t})\right){\Big |}S_{0}=s_{0}\right]$ for any function $b:{\text{States}}\to \mathbb {R}$ . This can be proven by applying the previous lemma.

The algorithm uses the modified gradient estimator $g_{i}\leftarrow {\frac {1}{N}}\sum _{n=1}^{N}\left[\sum _{t=0}^{T}\nabla _{\theta _{t}}\ln \pi _{\theta }(A_{t,n}|S_{t,n})\left(\sum _{\tau =t}^{T}(\gamma ^{\tau }R_{\tau ,n})-b_{i}(S_{t,n})\right)\right]$ and the original REINFORCE algorithm is the special case where $b_{i}\equiv 0$ .

### Actor-critic methods

If ${\textstyle b_{i}}$ is chosen well, such that ${\textstyle b_{i}(S_{t})\approx \sum _{\tau =t}^{T}(\gamma ^{\tau }R_{\tau })=\gamma ^{t}V^{\pi _{\theta _{i}}}(S_{t})}$ , this could significantly decrease variance in the gradient estimation. That is, the baseline should be as close to the **value function** $V^{\pi _{\theta _{i}}}(S_{t})$ as possible, approaching the ideal of: $\nabla _{\theta }J(\theta )=\mathbb {E} _{\pi _{\theta }}\left[\sum _{t=0}^{T}\nabla _{\theta }\ln \pi _{\theta }(A_{t}|S_{t})\left(\sum _{\tau =t}^{T}(\gamma ^{\tau }R_{\tau })-\gamma ^{t}V^{\pi _{\theta }}(S_{t})\right){\Big |}S_{0}=s_{0}\right]$ Note that, as the policy $\pi _{\theta _{t}}$ updates, the value function $V^{\pi _{\theta _{i}}}(S_{t})$ updates as well, so the baseline should also be updated. One common approach is to train a separate function that estimates the value function, and use that as the baseline. This is one of the actor-critic methods, where the policy function is the actor and the value function is the critic.

The **Q-function** $Q^{\pi }$ can also be used as the critic, since $\nabla _{\theta }J(\theta )=E_{\pi _{\theta }}\left[\sum _{0\leq t\leq T}\gamma ^{t}\nabla _{\theta }\ln \pi _{\theta }(A_{t}|S_{t})\cdot Q^{\pi _{\theta }}(S_{t},A_{t}){\Big |}S_{0}=s_{0}\right]$ by a similar argument using the tower law.

Subtracting the value function as a baseline, we find that the **advantage function** $A^{\pi }(S,A)=Q^{\pi }(S,A)-V^{\pi }(S)$ can be used as the critic as well: $\nabla _{\theta }J(\theta )=E_{\pi _{\theta }}\left[\sum _{0\leq t\leq T}\gamma ^{t}\nabla _{\theta }\ln \pi _{\theta }(A_{t}|S_{t})\cdot A^{\pi _{\theta }}(S_{t},A_{t}){\Big |}S_{0}=s_{0}\right]$ In summary, there are many unbiased estimators for ${\textstyle \nabla _{\theta }J_{\theta }}$ , all in the form of: $\nabla _{\theta }J(\theta )=E_{\pi _{\theta }}\left[\sum _{0\leq t\leq T}\nabla _{\theta }\ln \pi _{\theta }(A_{t}|S_{t})\cdot \Psi _{t}{\Big |}S_{0}=s_{0}\right]$ where ${\textstyle \Psi _{t}}$ is any linear sum of the following terms:

- ${\textstyle \sum _{0\leq \tau \leq T}(\gamma ^{\tau }R_{\tau })}$ : never used.
- ${\textstyle \gamma ^{t}\sum _{t\leq \tau \leq T}(\gamma ^{\tau -t}R_{\tau })}$ : used by the REINFORCE algorithm.
- ${\textstyle \gamma ^{t}\sum _{t\leq \tau \leq T}(\gamma ^{\tau -t}R_{\tau })-b(S_{t})}$ : used by the REINFORCE with baseline algorithm.
- ${\textstyle \gamma ^{t}\left(R_{t}+\gamma V^{\pi _{\theta }}(S_{t+1})-V^{\pi _{\theta }}(S_{t})\right)}$ : 1-step TD learning.
- ${\textstyle \gamma ^{t}Q^{\pi _{\theta }}(S_{t},A_{t})}$ .
- ${\textstyle \gamma ^{t}A^{\pi _{\theta }}(S_{t},A_{t})}$ .

Some more possible ${\textstyle \Psi _{t}}$ are as follows, with very similar proofs.

- ${\textstyle \gamma ^{t}\left(R_{t}+\gamma R_{t+1}+\gamma ^{2}V^{\pi _{\theta }}(S_{t+2})-V^{\pi _{\theta }}(S_{t})\right)}$ : 2-step TD learning.
- ${\textstyle \gamma ^{t}\left(\sum _{k=0}^{n-1}\gamma ^{k}R_{t+k}+\gamma ^{n}V^{\pi _{\theta }}(S_{t+n})-V^{\pi _{\theta }}(S_{t})\right)}$ : n-step TD learning.
- ${\textstyle \gamma ^{t}\sum _{n=1}^{\infty }{\frac {\lambda ^{n-1}}{1-\lambda }}\cdot \left(\sum _{k=0}^{n-1}\gamma ^{k}R_{t+k}+\gamma ^{n}V^{\pi _{\theta }}(S_{t+n})-V^{\pi _{\theta }}(S_{t})\right)}$ : TD(λ) learning, also known as **GAE (generalized advantage estimate)**. This is obtained by an exponentially decaying sum of the n-step TD learning ones.

## Natural policy gradient

The natural policy gradient method is a variant of the policy gradient method, proposed by Sham Kakade in 2001. Unlike standard policy gradient methods, which depend on the choice of parameters $\theta$ (making updates coordinate-dependent), the natural policy gradient aims to provide a coordinate-free update, which is geometrically "natural".

### Motivation

Standard policy gradient updates $\theta _{i+1}=\theta _{i}+\alpha \nabla _{\theta }J(\theta _{i})$ solve a constrained optimization problem: ${\begin{cases}\max _{\theta _{i+1}}J(\theta _{i})+(\theta _{i+1}-\theta _{i})^{T}\nabla _{\theta }J(\theta _{i})\\\|\theta _{i+1}-\theta _{i}\|\leq \alpha \cdot \|\nabla _{\theta }J(\theta _{i})\|\end{cases}}$ While the objective (linearized improvement) is geometrically meaningful, the Euclidean constraint $\|\theta _{i+1}-\theta _{i}\|$ introduces coordinate dependence. To address this, the natural policy gradient replaces the Euclidean constraint with a Kullback–Leibler divergence (KL) constraint: ${\begin{cases}\max _{\theta _{i+1}}J(\theta _{i})+(\theta _{i+1}-\theta _{i})^{T}\nabla _{\theta }J(\theta _{i})\\{\bar {D}}_{KL}(\pi _{\theta _{i+1}}\|\pi _{\theta _{i}})\leq \epsilon \end{cases}}$ where the KL divergence between two policies is **averaged** over the state distribution under policy $\pi _{\theta _{i}}$ . That is, ${\bar {D}}_{KL}(\pi _{\theta _{i+1}}\|\pi _{\theta _{i}}):=\mathbb {E} _{s\sim \pi _{\theta _{i}}}[D_{KL}(\pi _{\theta _{i+1}}(\cdot |s)\|\pi _{\theta _{i}}(\cdot |s))]$ This ensures updates are invariant to invertible affine parameter transformations.

### Fisher information approximation

For small $\epsilon$ , the KL divergence is approximated by the Fisher information metric: ${\bar {D}}_{KL}(\pi _{\theta _{i+1}}\|\pi _{\theta _{i}})\approx {\frac {1}{2}}(\theta _{i+1}-\theta _{i})^{T}F(\theta _{i})(\theta _{i+1}-\theta _{i})$ where $F(\theta )$ is the Fisher information matrix of the policy, defined as: $F(\theta )=\mathbb {E} _{s,a\sim \pi _{\theta }}\left[\nabla _{\theta }\ln \pi _{\theta }(a|s)\left(\nabla _{\theta }\ln \pi _{\theta }(a|s)\right)^{T}\right]$ This transforms the problem into a problem in quadratic programming, yielding the natural policy gradient update: $\theta _{i+1}=\theta _{i}+\alpha F(\theta _{i})^{-1}\nabla _{\theta }J(\theta _{i})$ The step size $\alpha$ is typically adjusted to maintain the KL constraint, with ${\textstyle \alpha \approx {\sqrt {\frac {2\epsilon }{(\nabla _{\theta }J(\theta _{i}))^{T}F(\theta _{i})^{-1}\nabla _{\theta }J(\theta _{i})}}}}$ .

Inverting $F(\theta )$ is computationally intensive, especially for high-dimensional parameters (e.g., neural networks). Practical implementations often use approximations.

## Trust Region Policy Optimization (TRPO)

**Trust Region Policy Optimization** (TRPO) is a policy gradient method that extends the natural policy gradient approach by enforcing a trust region constraint on policy updates. Developed by Schulman et al. in 2015, TRPO improves upon the natural policy gradient method.

The natural gradient descent is theoretically optimal, *if* the objective is truly a quadratic function, but this is only an approximation. TRPO's line search and KL constraint attempts to restrict the solution to within a "trust region" in which this approximation does not break down. This makes TRPO more robust in practice.

### Formulation

Like natural policy gradient, TRPO iteratively updates the policy parameters $\theta$ by solving a constrained optimization problem specified coordinate-free: ${\begin{cases}\max _{\theta }L(\theta ,\theta _{i})\\{\bar {D}}_{KL}(\pi _{\theta }\|\pi _{\theta _{i}})\leq \epsilon \end{cases}}$ where

- $L(\theta ,\theta _{i})=\mathbb {E} _{s,a\sim \pi _{\theta _{i}}}\left[{\frac {\pi _{\theta }(a|s)}{\pi _{\theta _{i}}(a|s)}}A^{\pi _{\theta _{i}}}(s,a)\right]$ is the **surrogate advantage**, measuring the performance of $\pi _{\theta }$ relative to the old policy $\pi _{\theta _{i}}$ .
- $\epsilon$ is the trust region radius.

Note that in general, other surrogate advantages are possible: $L(\theta ,\theta _{i})=\mathbb {E} _{s,a\sim \pi _{\theta _{i}}}\left[{\frac {\pi _{\theta }(a|s)}{\pi _{\theta _{i}}(a|s)}}\Psi ^{\pi _{\theta _{i}}}(s,a)\right]$ where $\Psi$ is any linear sum of the previously mentioned type. Indeed, OpenAI recommended using the Generalized Advantage Estimate, instead of the plain advantage $A^{\pi _{\theta }}$ .

The surrogate advantage $L(\theta ,\theta _{t})$ is designed to align with the policy gradient $\nabla _{\theta }J(\theta )$ . Specifically, when $\theta =\theta _{t}$ , **$\nabla _{\theta }L(\theta ,\theta _{t})$** equals the policy gradient derived from the advantage function: $\nabla _{\theta }J(\theta )=\mathbb {E} _{(s,a)\sim \pi _{\theta }}\left[\nabla _{\theta }\ln \pi _{\theta }(a|s)\cdot A^{\pi _{\theta }}(s,a)\right]=\nabla _{\theta }L(\theta ,\theta _{t})$ However, when $\theta \neq \theta _{i}$ , this is not necessarily true. Thus it is a "surrogate" of the real objective.

As with natural policy gradient, for small policy updates, TRPO approximates the surrogate advantage and KL divergence using Taylor expansions around $\theta _{t}$ : ${\begin{aligned}L(\theta ,\theta _{i})&\approx g^{T}(\theta -\theta _{i}),\\{\bar {D}}_{\text{KL}}(\pi _{\theta }\|\pi _{\theta _{i}})&\approx {\frac {1}{2}}(\theta -\theta _{i})^{T}H(\theta -\theta _{i}),\end{aligned}}$ where:

- $g=\nabla _{\theta }L(\theta ,\theta _{i}){\big |}_{\theta =\theta _{i}}$ is the policy gradient.
- $F=\nabla _{\theta }^{2}{\bar {D}}_{\text{KL}}(\pi _{\theta }\|\pi _{\theta _{i}}){\big |}_{\theta =\theta _{i}}$ is the Fisher information matrix.

This reduces the problem to a quadratic optimization, yielding the natural policy gradient update: $\theta _{i+1}=\theta _{i}+{\sqrt {\frac {2\epsilon }{g^{T}F^{-1}g}}}F^{-1}g.$ So far, this is essentially the same as natural gradient method. However, TRPO improves upon it by two modifications:

- Use conjugate gradient method to solve for x in $Fx=g$ iteratively without explicit matrix inversion.
- Use backtracking line search to ensure the trust-region constraint is satisfied. Specifically, it backtracks the step size to ensure the KL constraint and policy improvement. That is, it tests each of the following test-solutions $\theta _{i+1}=\theta _{i}+{\sqrt {\frac {2\epsilon }{x^{T}Fx}}}x,\;\theta _{i}+\alpha {\sqrt {\frac {2\epsilon }{x^{T}Fx}}}x,\;\theta _{i}+\alpha ^{2}{\sqrt {\frac {2\epsilon }{x^{T}Fx}}}x,\;\dots$ until it finds one that both satisfies the KL constraint ${\bar {D}}_{KL}(\pi _{\theta _{i+1}}\|\pi _{\theta _{i}})\leq \epsilon$ and results in a higher $L(\theta _{i+1},\theta _{i})\geq L(\theta _{i},\theta _{i})$ . Here, $\alpha \in (0,1)$ is the backtracking coefficient.

## Proximal Policy Optimization (PPO)

A further improvement is proximal policy optimization (PPO), which avoids even computing $F(\theta )$ and $F(\theta )^{-1}$ via a first-order approximation using clipped probability ratios.

Specifically, instead of maximizing the surrogate advantage $\max _{\theta }L(\theta ,\theta _{t})=\mathbb {E} _{s,a\sim \pi _{\theta _{t}}}\left[{\frac {\pi _{\theta }(a|s)}{\pi _{\theta _{t}}(a|s)}}A^{\pi _{\theta _{t}}}(s,a)\right]$ under a KL divergence constraint, it directly inserts the constraint into the surrogate advantage: $\max _{\theta }\mathbb {E} _{s,a\sim \pi _{\theta _{t}}}\left[{\begin{cases}\min \left({\frac {\pi _{\theta }(a|s)}{\pi _{\theta _{t}}(a|s)}},1+\epsilon \right)A^{\pi _{\theta _{t}}}(s,a)&{\text{ if }}A^{\pi _{\theta _{t}}}(s,a)>0\\\max \left({\frac {\pi _{\theta }(a|s)}{\pi _{\theta _{t}}(a|s)}},1-\epsilon \right)A^{\pi _{\theta _{t}}}(s,a)&{\text{ if }}A^{\pi _{\theta _{t}}}(s,a)<0\end{cases}}\right]$ and PPO maximizes the surrogate advantage by stochastic gradient descent, as usual.

In words, gradient-ascending the new surrogate advantage function means that, at some state $s,a$ , if the advantage is positive: $A^{\pi _{\theta _{t}}}(s,a)>0$ , then the gradient should direct $\theta$ towards the direction that increases the probability of performing action a under the state s . However, as soon as $\theta$ has changed so much that $\pi _{\theta }(a|s)\geq (1+\epsilon )\pi _{\theta _{t}}(a|s)$ , then the gradient should stop pointing it in that direction. And similarly if $A^{\pi _{\theta _{t}}}(s,a)<0$ . Thus, PPO avoids pushing the parameter update too hard, and avoids changing the policy too much.

To be more precise, to update $\theta _{t}$ to $\theta _{t+1}$ requires multiple update steps on the same batch of data. It would initialize $\theta =\theta _{t}$ , then repeatedly apply gradient descent (such as the Adam optimizer) to update $\theta$ until the surrogate advantage has stabilized. It would then assign $\theta _{t+1}$ to $\theta$ , and do it again.

During this inner-loop, the first update to $\theta$ would not hit the $1-\epsilon ,1+\epsilon$ bounds, but as $\theta$ is updated further and further away from $\theta _{t}$ , it eventually starts hitting the bounds. For each such bound hit, the corresponding gradient becomes zero, and thus PPO avoid updating $\theta$ too far away from $\theta _{t}$ .

This is important, because the surrogate loss assumes that the state-action pair $s,a$ is sampled from what the agent would see if the agent runs the policy $\pi _{\theta _{t}}$ , but policy gradient should be on-policy. So, as $\theta$ changes, the surrogate loss becomes more and more *off*-policy. This is why keeping $\theta$ *proximal* to $\theta _{t}$ is necessary.

If there is a reference policy $\pi _{\text{ref}}$ that the trained policy should not diverge too far from, then additional KL divergence penalty can be added: $-\beta \mathbb {E} _{s,a\sim \pi _{\theta _{t}}}\left[\log \left({\frac {\pi _{\theta }(a|s)}{\pi _{\text{ref}}(a|s)}}\right)\right]$ where $\beta$ adjusts the strength of the penalty. This has been used in training reasoning language models with reinforcement learning from human feedback. The KL divergence penalty term can be estimated with lower variance using the equivalent form (see f-divergence for details): $-\beta \mathbb {E} _{s,a\sim \pi _{\theta _{t}}}\left[\log \left({\frac {\pi _{\theta }(a|s)}{\pi _{\text{ref}}(a|s)}}\right)+{\frac {\pi _{\text{ref}}(a|s)}{\pi _{\theta }(a|s)}}-1\right]$

### Group Relative Policy Optimization (GRPO)

The Group Relative Policy Optimization (GRPO) is a minor variant of PPO that omits the value function estimator V . Instead, for each state s , it samples multiple actions $a_{1},\dots ,a_{G}$ from the policy $\pi _{\theta _{t}}$ , then calculate the group-relative advantage $A^{\pi _{\theta _{t}}}(s,a_{j})={\frac {r(s,a_{j})-\mu }{\sigma }}$ where $\mu ,\sigma$ are the mean and standard deviation of $r(s,a_{1}),\dots ,r(s,a_{G})$ . That is, it is the standard score of the rewards.

Then, it maximizes the PPO objective, averaged over all actions: $\max _{\theta }{\frac {1}{G}}\sum _{i=1}^{G}\mathbb {E} _{(s,a_{1},\dots ,a_{G})\sim \pi _{\theta _{t}}}\left[{\begin{cases}\min \left({\frac {\pi _{\theta }(a_{i}|s)}{\pi _{\theta _{t}}(a_{i}|s)}},1+\epsilon \right)A^{\pi _{\theta _{t}}}(s,a_{i})&{\text{ if }}A^{\pi _{\theta _{t}}}(s,a_{i})>0\\\max \left({\frac {\pi _{\theta }(a_{i}|s)}{\pi _{\theta _{t}}(a_{i}|s)}},1-\epsilon \right)A^{\pi _{\theta _{t}}}(s,a_{i})&{\text{ if }}A^{\pi _{\theta _{t}}}(s,a_{i})<0\end{cases}}\right]$ Intuitively, each policy update step in GRPO makes the policy more likely to respond to each state with an action that performed relatively better than other actions tried at that state, and less likely to respond with one that performed relatively worse.

As before, the KL penalty term can be applied to encourage the trained policy to stay close to a reference policy. GRPO was first proposed in the context of training reasoning language models by researchers at DeepSeek.

## Policy Optimization and the Mirror Descent perspective (MDPO)

Methods like TRPO, PPO and natural policy gradient share a common idea - while the policy should be updated in the direction of the policy gradient, the update should be done in a safe and stable manner, typically measured by some distance with respect to the policy before the update.

A similar notion of update stability is found in proximal convex optimization techniques like Mirror Descent. There, ${\textstyle \mathbf {x} }$ , the proposed minimizer of ${\textstyle f}$ in some constraint set ${\textstyle {\mathcal {C}}}$ , is iteratively updated in the direction of the gradient ${\textstyle \nabla f}$ , with a proximity penalty with respect to the current ${\textstyle \mathbf {x} _{t}}$ measured by some Bregman divergence ${\textstyle B_{\omega }}$ , which can formalized by the following formula: $\mathbf {x} _{t+1}\in \arg \min _{\mathbf {x} \in {\mathcal {C}}}\nabla f(\mathbf {x} _{t})^{T}(\mathbf {x} -\mathbf {x} _{t})+{\frac {1}{\eta _{t}}}B_{\omega }(x,x_{t}),$ where ${\textstyle \eta _{t}}$ controls the proximity between consecutive iterates, similar to the learning rate in gradient descent.

This leads to reconsidering the policy update procedure as an optimization procedure aimed at finding an optimal policy, in the (non-convex) optimization landscape of the underlying Markov decision process (MDP). This optimization viewpoint of using the policy gradient is termed Mirror Descent Policy Optimization (MDPO), leading to the following update when the KL is the chosen Bregman divergence: $\pi _{t+1}\in \arg \max _{\pi }\mathbb {E} _{s,a\sim \pi }\left[A^{\pi _{t}}(s,a)\right]+{\frac {1}{\eta _{t}}}D_{KL}(\pi ||\pi _{t})$ With a parameterized policy ${\textstyle \pi _{\theta }}$ , the MDPO loss becomes: $\max _{\theta }L(\theta ,\theta _{t})=\mathbb {E} _{s,a\sim \pi _{\theta _{t}}}\left[{\frac {\pi _{\theta }(a|s)}{\pi _{\theta _{t}}(a|s)}}A^{\pi _{\theta _{t}}}(s,a)\right]+{\frac {1}{\eta _{t}}}D_{KL}(\pi _{\theta }||\pi _{\theta _{t}})$ This objective can be used together with other common techniques like the clipping done in PPO. In fact, the KL divergence penalty also appears in the original PPO paper, suggesting the MDPO perspective as a theoretical unification of the main derivation concepts behind many concurrent policy gradient techniques.
