---
title: "Online optimization"
source: https://en.wikipedia.org/wiki/Online_optimization
domain: regret-minimization
license: CC-BY-SA-4.0
tags: regret minimization, multi armed bandit, no regret dynamics, thompson sampling
fetched: 2026-07-02
---

# Online optimization

**Online optimization** is a field of optimization theory, more popular in computer science and operations research, that deals with optimization problems having no or incomplete knowledge of the future (online). These kinds of problems are denoted as online problems and are seen as opposed to the classical optimization problems where complete information is assumed (offline). The research on online optimization can be distinguished into online problems where multiple decisions are made sequentially based on a piece-by-piece input and those where a decision is made only once. A famous online problem where a decision is made only once is the Ski rental problem. In general, the output of an online algorithm is compared to the solution of a corresponding offline algorithm which is necessarily always optimal and knows the entire input in advance (competitive analysis).

In many situations, present decisions (for example, resource allocation) must be made with incomplete knowledge of the future or distributional assumptions on the future are not reliable. In such cases, online optimization can be used, which is different from other approaches such as robust optimization, stochastic optimization and Markov decision processes.

## Online problems

A problem exemplifying the concepts of online algorithms is the Canadian traveller problem. The goal of this problem is to minimize the cost of reaching a target in a weighted graph where some of the edges are unreliable and may have been removed from the graph. However, whether an edge has been removed (*failed*) is only revealed to *the traveller* when they reach one of the edge's endpoints. The worst case for this problem is simply that all of the unreliable edges fail and the problem reduces to the usual shortest path problem. An alternative analysis of the problem can be made with the help of competitive analysis. For this method of analysis, the offline algorithm knows in advance which edges will fail and the goal is to minimize the ratio between the online and offline algorithms' performance. This problem is PSPACE-complete.

Many formal problems offer more than one *online algorithm* as a solution:

- *k*-server problem
- Job shop scheduling problem
- List update problem
- Bandit problem
- Secretary problem
- Search games
- Ski rental problem
- Linear search problem
- Portfolio selection problem
- Online matching
