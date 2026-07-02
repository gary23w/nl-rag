---
title: "Thompson sampling"
source: https://en.wikipedia.org/wiki/Thompson_sampling
domain: multi-armed-bandit
license: CC-BY-SA-4.0
tags: multi armed bandit, exploration exploitation tradeoff, thompson sampling, regret minimization
fetched: 2026-07-02
---

# Thompson sampling

**Thompson sampling**, named after William Rae Thompson, is a heuristic for choosing actions that address the exploration–exploitation dilemma in the multi-armed bandit problem. It consists of choosing the action that maximizes the expected reward with respect to a randomly drawn belief.

## Description

Consider a set of contexts ${\mathcal {X}}$ , a set of actions ${\mathcal {A}}$ , and rewards in $\mathbb {R}$ . The aim of the player is to play actions under the various contexts, such as to maximize the cumulative rewards. Specifically, in each round, the player obtains a context $x\in {\mathcal {X}}$ , plays an action $a\in {\mathcal {A}}$ and receives a reward $r\in \mathbb {R}$ following a distribution that depends on the context and the issued action.

The elements of Thompson sampling are as follows:

1. a likelihood function $P(r|\theta ,a,x)$ ;
2. a set $\Theta$ of parameters $\theta$ of the distribution of r ;
3. a prior distribution $P(\theta )$ on these parameters;
4. past observations triplets ${\mathcal {D}}=\{(x;a;r)\}$ ;
5. a posterior distribution $P(\theta |{\mathcal {D}})\propto P({\mathcal {D}}|\theta )P(\theta )$ , where $P({\mathcal {D}}|\theta )$ is the likelihood function.

Thompson sampling consists of playing the action $a^{\ast }\in {\mathcal {A}}$ according to the probability that it maximizes the expected reward; action $a^{\ast }$ is chosen with probability

$\int \mathbb {I} \left[\mathbb {E} (r|a^{\ast },x,\theta )=\max _{a'}\mathbb {E} (r|a',x,\theta )\right]P(\theta |{\mathcal {D}})d\theta ,$

where $\mathbb {I}$ is the indicator function.

In practice, the rule is implemented by sampling. In each round, parameters $\theta ^{\ast }$ are sampled from the posterior $P(\theta |{\mathcal {D}})$ , and an action $a^{\ast }$ chosen that maximizes $\mathbb {E} [r|\theta ^{\ast },a^{\ast },x]$ , i.e. the expected reward given the sampled parameters, the action, and the current context. Conceptually, this means that the player instantiates their beliefs randomly in each round according to the posterior distribution, and then acts optimally according to them. In most practical applications, it is computationally onerous to maintain and sample from a posterior distribution over models. As such, Thompson sampling is often used in conjunction with approximate sampling techniques.

## History

Thompson sampling was originally described by Thompson in 1933. It was subsequently rediscovered numerous times independently in the context of multi-armed bandit problems. A first proof of convergence for the bandit case has been shown in 1997. The first application to Markov decision processes was in 2000. A related approach (see Bayesian control rule) was published in 2010. In 2010 it was also shown that Thompson sampling is *instantaneously self-correcting*. Asymptotic convergence results for contextual bandits were published in 2011. Thompson Sampling has been widely used in many online learning problems including A/B testing in website design and online advertising, and accelerated learning in decentralized decision making. A Double Thompson Sampling (D-TS) algorithm has been proposed for dueling bandits, a variant of traditional MAB, where feedback comes in the form of pairwise comparison.

## Relationship to other approaches

### Probability matching

Probability matching is a decision strategy in which predictions of class membership are proportional to the class base rates. Thus, if in the training set positive examples are observed 60% of the time, and negative examples are observed 40% of the time, the observer using a probability-matching strategy will predict (for unlabeled examples) a class label of "positive" on 60% of instances, and a class label of "negative" on 40% of instances.

### Bayesian control rule

A generalization of Thompson sampling to arbitrary dynamical environments and causal structures, known as **Bayesian control rule**, has been shown to be the optimal solution to the adaptive coding problem with actions and observations. In this formulation, an agent is conceptualized as a mixture over a set of behaviours. As the agent interacts with its environment, it learns the causal properties and adopts the behaviour that minimizes the relative entropy to the behaviour with the best prediction of the environment's behaviour. If these behaviours have been chosen according to the maximum expected utility principle, then the asymptotic behaviour of the Bayesian control rule matches the asymptotic behaviour of the perfectly rational agent.

The setup is as follows. Let $a_{1},a_{2},\ldots ,a_{T}$ be the actions issued by an agent up to time T , and let $o_{1},o_{2},\ldots ,o_{T}$ be the observations gathered by the agent up to time T . Then, the agent issues the action $a_{T+1}$ with probability:

$P(a_{T+1}|{\hat {a}}_{1:T},o_{1:T}),$

where the "hat"-notation ${\hat {a}}_{t}$ denotes the fact that $a_{t}$ is a causal intervention (see Causality), and not an ordinary observation. If the agent holds beliefs $\theta \in \Theta$ over its behaviors, then the Bayesian control rule becomes

$P(a_{T+1}|{\hat {a}}_{1:T},o_{1:T})=\int _{\Theta }P(a_{T+1}|\theta ,{\hat {a}}_{1:T},o_{1:T})P(\theta |{\hat {a}}_{1:T},o_{1:T})\,d\theta$

,

where $P(\theta |{\hat {a}}_{1:T},o_{1:T})$ is the posterior distribution over the parameter $\theta$ given actions $a_{1:T}$ and observations $o_{1:T}$ .

In practice, the Bayesian control amounts to sampling, at each time step, a parameter $\theta ^{\ast }$ from the posterior distribution $P(\theta |{\hat {a}}_{1:T},o_{1:T})$ , where the posterior distribution is computed using Bayes' rule by only considering the (causal) likelihoods of the observations $o_{1},o_{2},\ldots ,o_{T}$ and ignoring the (causal) likelihoods of the actions $a_{1},a_{2},\ldots ,a_{T}$ , and then by sampling the action $a_{T+1}^{\ast }$ from the action distribution $P(a_{T+1}|\theta ^{\ast },{\hat {a}}_{1:T},o_{1:T})$ .

### Upper-confidence-bound (UCB) algorithms

Thompson sampling and upper-confidence bound algorithms share a fundamental property that underlies many of their theoretical guarantees. Roughly speaking, both algorithms allocate exploratory effort to actions that might be optimal and are in this sense "optimistic". Leveraging this property, one can translate regret bounds established for UCB algorithms to Bayesian regret bounds for Thompson sampling or unify regret analysis across both these algorithms and many classes of problems.
