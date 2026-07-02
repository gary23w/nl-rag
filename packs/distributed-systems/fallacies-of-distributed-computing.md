---
title: "Fallacies of distributed computing"
source: https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing
domain: distributed-systems
license: CC-BY-SA-4.0
tags: distributed system, distributed computing, cap theorem, consistency model, eventual consistency
fetched: 2026-07-02
---

# Fallacies of distributed computing

The **fallacies of distributed computing** are a set of assertions made by L. Peter Deutsch and others at Sun Microsystems describing false assumptions that programmers new to distributed applications invariably make.

## The fallacies

The originally listed fallacies are

1. The network is reliable;
2. Latency is zero;
3. Bandwidth is infinite;
4. The network is secure;
5. Topology doesn't change;
6. There is one administrator;
7. Transport cost is zero;
8. The network is homogeneous;

## The effects of the fallacies

1. Software applications are written with little error-handling on networking errors. During a network outage, such applications may stall or infinitely wait for an answer packet, permanently consuming memory or other resources. When the failed network becomes available, those applications may also fail to retry any stalled operations or require a (manual) restart.
2. Ignorance of network latency, and of the packet loss it can cause, induces application- and transport-layer developers to allow unbounded traffic, greatly increasing dropped packets and wasting bandwidth.
3. Ignorance of bandwidth limits on the part of traffic senders can result in bottlenecks.
4. Complacency regarding network security results in being blindsided by malicious users and programs that continually adapt to security measures.
5. Changes in network topology can have effects on both bandwidth and latency issues, and therefore can have similar problems.
6. Multiple administrators, as with subnets for rival companies, may institute conflicting policies of which senders of network traffic must be aware in order to complete their desired paths.
7. The "hidden" costs of building and maintaining a network or subnet are non-negligible and must consequently be noted in budgets to avoid vast shortfalls.
8. If a system assumes a homogeneous network, then it can lead to the same problems that result from the first three fallacies.

## History

The list of fallacies originated at Sun Microsystems. L. Peter Deutsch, one of the original Sun "Fellows", first created a list of seven fallacies in 1994; incorporating four fallacies Bill Joy and Dave Lyon had already identified in "The Fallacies of Networked Computing". Around 1997, James Gosling, another Sun Fellow and the inventor of Java, added the eighth fallacy.

In an episode of "Software Engineering Radio" Peter Deutsch added a ninth fallacy: "It's really an expansion of number 4. It extends beyond the boundaries of the physical network. ... The party you are communicating with is trustworthy."

Later in 2020, Mark Richards and Neal Ford expanded upon the original "Fallacies of Distributed Computing" by introducing three additional fallacies to address contemporary challenges in distributed systems:

- Versioning is simple
- Compensating updates always work
- Observability is optional
