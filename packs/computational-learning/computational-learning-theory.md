---
title: "Computational learning theory"
source: https://en.wikipedia.org/wiki/Computational_learning_theory
domain: computational-learning
license: CC-BY-SA-4.0
tags: computational learning theory, mistake bound model, query learning, statistical learning theory
fetched: 2026-07-02
---

# Computational learning theory

In computer science, **computational learning theory** (or just **learning theory**) is a subfield of artificial intelligence devoted to studying the design and analysis of machine learning algorithms.

## Overview

Theoretical results in machine learning often focus on a type of inductive learning known as supervised learning. In supervised learning, an algorithm is provided with labeled samples. For instance, the samples might be descriptions of mushrooms, with labels indicating whether they are edible or not. The algorithm uses these labeled samples to create a classifier. This classifier assigns labels to new samples, including those it has not previously encountered. The goal of the supervised learning algorithm is to optimize performance metrics, such as minimizing errors on new samples.

In addition to performance bounds, computational learning theory studies the time complexity and feasibility of learning. In computational learning theory, a computation is considered feasible if it can be done in polynomial time. There are two kinds of time complexity results:

- Positive results – Showing that a certain class of functions is learnable in polynomial time.
- Negative results – Showing that certain classes cannot be learned in polynomial time.

Negative results often rely on commonly believed, but yet unproven assumptions, such as:

- Computational complexity – P ≠ NP (the P versus NP problem);
- Cryptographic – One-way functions exist.

There are several different approaches to computational learning theory based on making different assumptions about the inference principles used to generalise from limited data. This includes different definitions of probability (see frequency probability, Bayesian probability) and different assumptions on the generation of samples. The different approaches include:

- Exact learning, proposed by Dana Angluin;
- Probably approximately correct learning (PAC learning), proposed by Leslie Valiant;
- VC theory, proposed by Vladimir Vapnik and Alexey Chervonenkis;
- Inductive inference as developed by Ray Solomonoff;
- Algorithmic learning theory, from the work of E. Mark Gold;
- Online machine learning, from the work of Nick Littlestone.

While its primary goal is to understand learning abstractly, computational learning theory has led to the development of practical algorithms. For example, PAC theory inspired boosting, VC theory led to support vector machines, and Bayesian inference led to belief networks.
