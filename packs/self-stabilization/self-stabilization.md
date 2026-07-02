---
title: "Self-stabilization"
source: https://en.wikipedia.org/wiki/Self-stabilization
domain: self-stabilization
license: CC-BY-SA-4.0
tags: self stabilizing system, fault tolerant convergence, dijkstra token ring, closure property
fetched: 2026-07-02
---

# Self-stabilization

**Self-stabilization** is a concept of fault-tolerance in distributed systems. Given any initial state, a self-stabilizing distributed system will end up in a correct state in a finite number of execution steps.

At first glance, the guarantee of self stabilization may seem less promising than that of the more traditional fault-tolerance of algorithms, that aim to guarantee that the system always remains in a correct state under certain kinds of state transitions. However, that traditional fault tolerance cannot always be achieved. For example, it cannot be achieved when the system is started in an incorrect state or is corrupted by an intruder. Moreover, because of their complexity, it is very hard to debug and to analyze distributed systems. Hence, it is very hard to prevent a distributed system from reaching an incorrect state. Indeed, some forms of self-stabilization are incorporated into many modern computer and telecommunications networks, since it gives them the ability to cope with faults that were not foreseen in the design of the algorithm.

Many years after the seminal paper of Edsger Dijkstra in 1974, this concept remains important as it presents an important foundation for self-managing computer systems and fault-tolerant systems. As a result, Dijkstra's paper received the 2002 ACM PODC Influential-Paper Award, one of the highest recognitions in the distributed computing community. Moreover, after Dijkstra's death, the award was renamed and is now called the Dijkstra Award.

## History

E.W. Dijkstra in 1974 presented the concept of self-stabilization, prompting further research in this area. His demonstration involved the presentation of self-stabilizing mutual exclusion algorithms. It also showed the first self-stabilizing algorithms that did not rely on strong assumptions on the system. Some previous protocols used in practice did actually stabilize, but only assuming the existence of a clock that was global to the system, and assuming a known upper bound on the duration of each system transition. It was only ten years later when Leslie Lamport pointed out the importance of Dijkstra's work at a 1983 conference called Symposium on Principles of Distributed Computing that researchers directed their attention to this elegant fault-tolerance concept. In his talk, Lamport stated:

> I regard this as Dijkstra's most brilliant work - at least, his most brilliant published paper. It's almost completely unknown. I regard it to be a milestone in work on fault tolerance... I regard self-stabilization to be a very important concept in fault tolerance and to be a very fertile field for research.

Afterwards, Dijkstra's work was awarded ACM-PODC influential paper award, which then became ACM's (the Association for computing Machinery) Dijkstra Prize in Distributed Computing given at the annual ACM-PODC symposium.

## Overview

A distributed algorithm is self-stabilizing if, starting from an arbitrary state, it is guaranteed to converge to a legitimate state and remain in a legitimate set of states thereafter. A state is legitimate if, starting from this state, the algorithm satisfies its specification. The property of self-stabilization enables a distributed algorithm to recover from a transient fault regardless of its nature. Moreover, a self-stabilizing algorithm does not have to be initialized as it eventually starts to behave correctly regardless of its initial state.

Dijkstra's paper, which introduces the concept of self-stabilization, presents an example in the context of a "token ring"—a network of computers ordered in a circle. Here, each computer or processor can "see" the whole state of one processor that immediately precedes it and that this state may imply that the processor "has a token" or it "does not have a token."One of the requirements is that exactly one of them must "hold a token" at any given time. The second requirement prescribes that each node "passes the token" to the computer/processor succeeding it so that the token eventually circulates the ring.

- Not holding a token is a correct state for each computer in this network, since the token can be held by another computer. However, if every computer is in the state of "not holding a token" then the network altogether is not in a correct state.
- Similarly, if more than one computer "holds a token" then this is not a correct state for the network, although it cannot be observed to be incorrect by viewing any computer individually. Since every computer can "observe" only the states of its two neighbors, it is hard for the computers to decide whether the network altogether is in a correct state.

The first self-stabilizing algorithms did not detect errors explicitly in order to subsequently repair them. Instead, they constantly pushed the system towards a legitimate state. Since traditional methods for detecting an error were often very difficult and time-consuming, such a behavior was considered desirable. (The method described in the paper cited above collects a huge amount of information from the whole network to one place; after that, it attempts to determine whether the collected global state is correct; even that determination alone can be a hard task).

### Efficiency improvements

More recently, researchers have presented newer methods for light-weight error detection for self-stabilizing systems using local checking. and for general tasks.

The term *local* refers to a part of a computer network. When local detection is used, a computer in a network is not required to communicate with the entire network in order to detect an error—the error can be detected by having each computer communicate only with its nearest neighbors. These local detection methods simplified the task of designing self-stabilizing algorithms considerably. This is because the error detection mechanism and the recovery mechanism can be designed separately. Newer algorithms based on these detection methods also turned out to be much more efficient. Moreover, these papers suggested rather efficient general transformers to transform non self stabilizing algorithms to become self stabilizing. The idea is to,

1. Run the non self stabilizing protocol, at the same time,
2. detect faults (during the execution of the given protocol) using the above-mentioned detection methods,
3. then, apply a (self stabilizing) "reset" protocol to return the system to some predetermined initial state, and, finally,
4. restart the given (non- self stabilizing) protocol.

The combination of these 4 parts is self stabilizing (as long as there is no trigger of fault during the correction fault phases, e.g.,). Initial self stabilizing protocols were also presented in the above papers. More efficient reset protocols were presented later, e.g.

Additional efficiency was introduced with the notion of time-adaptive protocols. The idea behind these is that when only a small number of errors occurs, the recovery time can (and should) be made short. Dijkstra's original self-stabilization algorithms do not have this property.

A useful property of self-stabilizing algorithms is that they can be composed of layers if the layers do not exhibit any circular dependencies. The stabilization time of the composition is then bounded by the sum of the individual stabilization times of each layer.

New approaches to Dijkstra's work emerged later on such as the case of Krzysztof Apt and Ehsan Shoja's proposition, which demonstrated how self-stabilization can be naturally formulated using the standard concepts of strategic games, particularly the concept of an improvement path. This particular work sought to demonstrate the link between self-stabilization and game theory.

### Time complexity

The time complexity of a self-stabilizing algorithm is measured in (asynchronous) rounds or cycles.

- A *round* is the shortest execution trace in which each processor executes at least one step.
- Similarly, a *cycle* is the shortest execution trace in which each processor executes at least one complete iteration of its repeatedly executed list of commands.

To measure the output stabilization time, a subset of the state variables is defined to be externally visible (the *output*). Certain states of outputs are defined to be correct (legitimate). The set of the outputs of all the components of the system is said to have stabilized at the time that it starts to be correct, provided it stays correct indefinitely, unless additional faults occur. The output stabilization time is the time (the number of (asynchronous) *rounds*) until the output stabilizes.

## Definition

A system is self-stabilizing if and only if:

1. Starting from any state, it is guaranteed that the system will eventually reach a correct state (*convergence*).
2. Given that the system is in a correct state, it is guaranteed to stay in a correct state, provided that no fault happens (*closure*).

A system is said to be *randomized self-stabilizing* if and only if it is self-stabilizing and the expected number of rounds needed to reach a correct state is bounded by some constant k .

Design of self-stabilization in the above-mentioned sense is well known to be a difficult job. In fact, a class of distributed algorithms do not have the property of local checking: the legitimacy of the network state cannot be evaluated by a single process. The most obvious case is Dijkstra's token-ring defined above: no process can detect whether the network state is legitimate or not in the case where more than one token is present in non-neighboring processes. This suggests that self-stabilization of a distributed system is a sort of collective intelligence where each component is taking local actions, based on its local knowledge but eventually this guarantees global convergence at the end.

To help overcome the difficulty of designing self-stabilization as defined above, other types of stabilization were devised. For instance, *weak stabilization* is the property that a distributed system has a possibility to reach its legitimate behavior from every possible state. Weak stabilization is easier to design as it just guarantees a *possibility* of convergence for some runs of the distributed system rather than convergence for every run.

A self-stabilizing algorithm is *silent* if and only if it converges to a global state where the values of communication registers used by the algorithm remain fixed.

An extension of the concept of self-stabilization is that of superstabilization. The intent here is to cope with dynamic distributed systems that undergo topological changes. In classical self-stabilization theory, arbitrary changes are viewed as errors where no guarantees are given until the system has stabilized again. With superstabilizing systems, there is a *passage* predicate that is always satisfied while the system's topology is reconfigured.

A Theory that started within the area of self-stabilization is verifying (in a distributed manner) that the collection of the states of the nodes in a network obeys some predicate. That theory has grown beyond self-stabilization and led to notions such as "distributed NP" (a distributed version of NP (complexity)), distributed Zero Knowledge (a distributed version of Zero Knowledge), etc. The International Colloquium on Structural Information and Communication Complexity (SIRROCO) Prize for Innovation in Distributed Computing of 2024 was awarded for initiating that theory.
