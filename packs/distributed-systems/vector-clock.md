---
title: "Vector clock"
source: https://en.wikipedia.org/wiki/Vector_clock
domain: distributed-systems
license: CC-BY-SA-4.0
tags: distributed system, distributed computing, cap theorem, consistency model, eventual consistency
fetched: 2026-07-02
---

# Vector clock

A **vector clock** is a data structure used for determining the partial ordering of events in a distributed system and detecting causality violations. Just as in Lamport timestamps, inter-process messages contain the state of the sending process's logical clock. A vector clock of a system of *n* processes is a vector (equivalentlly, a 1-dimensional array) of *n* logical clocks, one clock per process. Besides maintaining its own clock, every process also keeps track of the largest value of each of the other processes' clocks that it has so far been informed of.

The clock updates proceed as follows, where $VC_{i}$ denotes the value of the vector clock maintained by process i :

- Initially all clocks are zero.
- Each time a process experiences an internal event, it increments its own logical clock in the vector by one. For instance, upon an event at process i , it updates $VC_{i}[i]\leftarrow VC_{i}[i]+1$ .
- Each time a process sends a message, it increments its own logical clock in the vector by one (as in the bullet above, but not twice for the same event) then it pairs the message with a copy of its own vector and finally sends the pair.
- Each time a process receives a message-vector clock pair, it increments its own logical clock in the vector by one and updates each element in its vector by taking the maximum of the value in its own vector clock and the value in the vector in the received pair (for every element). For example, if process $P_{i}$ receives a message $(m,VC_{j})$ from $P_{j}$ , it first increments its own logical clock in the vector by one $VC_{i}[i]\leftarrow VC_{i}[i]+1$ and then updates its entire vector by setting $VC_{i}[k]\leftarrow \max(VC_{i}[k],VC_{j}[k]),\forall k$ .

## History

Lamport originated the idea of logical Lamport clocks in 1978. However, the logical clocks in that paper were scalars, not vectors. The generalization to vector time was developed several times, apparently independently, by different authors in the early 1980s. At least 6 papers contain the concept. The papers canonically cited in reference to vector clocks are Colin Fidge’s and Friedemann Mattern’s 1988 works, as they (independently) established the name "vector clock" and the mathematical properties of vector clocks.

## Partial ordering property

Vector clocks allow for the partial causal ordering of events. Defining the following:

- $VC(x)$ denotes the vector clock of event x , and $VC(x)_{z}$ denotes the component of that clock for process z .
- $VC(x)<VC(y)\iff \forall z[VC(x)_{z}\leq VC(y)_{z}]\land \exists z'[VC(x)_{z'}<VC(y)_{z'}]$
  - In English: $VC(x)$ is less than $VC(y)$ , if and only if $VC(x)_{z}$ is less than or equal to $VC(y)_{z}$ for all process indices z , and at least one of those relationships is strictly smaller (that is, $VC(x)_{z'}<VC(y)_{z'}$ ).
- $x\to y\;$ denotes that event x happened before event y . It is defined as: if $x\to y\;$ , then $VC(x)<VC(y)$

Properties:

- Asymmetry: if $VC(a)<VC(b)$ , then ¬ $(VC(b)<VC(a))$
- Transitivity: if $VC(a)<VC(b)$ and $VC(b)<VC(c)$ , then $VC(a)<VC(c)$ ; or, if $a\to b\;$ and $b\to c\;$ , then $a\to c\;$

## Relation with other orders

- Let $RT(x)$ be the real time when event x occurs. If $VC(a)<VC(b)$ , then $RT(a)<RT(b)$
- Let $C(x)$ be the Lamport timestamp of event x . If $VC(a)<VC(b)$ , then $C(a)<C(b)$

## Limitations under Byzantine failures

Vector clocks can reliably detect causality in distributed systems subject to crash failures. However, when processes behave arbitrarily or maliciously—as in the Byzantine failure model—causality detection becomes fundamentally impossible , rendering vector clocks ineffective in such environments. This impossibility result holds for all variants of vector clocks, as it stems from core limitations inherent to the problem of causality detection under Byzantine faults.

## Other mechanisms

- In 1984, Wuu and Bernstein described a technique extended from vector clocks known as **Matrix Clocks**. By maintaining a matrix where each row corresponds to the vector clock of a peer, processes can estimate the minimum knowledge held by all other nodes. This allows for the calculation of a "lower bound" on global progress, enabling the safe truncation of operation logs (garbage collection) in replicated databases.
- In 1999, Torres-Rojas and Ahamad developed **Plausible Clocks**, a mechanism that takes less space than vector clocks but that, in some cases, will totally order events that are causally concurrent.
- In 2005, Agarwal and Garg created **Chain Clocks**, a system that tracks dependencies using vectors with size smaller than the number of processes and that adapts automatically to systems with dynamic number of processes.
- In 2008, Almeida *et al.* introduced **Interval Tree Clocks**. This mechanism generalizes Vector Clocks and allows operation in dynamic environments when the identities and number of processes in the computation is not known in advance.
- In 2019, Lum Ramabaja proposed **Bloom Clocks**, a probabilistic data structure based on Bloom filters. Compared to a vector clock, the space used per node is fixed and does not depend on the number of nodes in a system. Comparing two clocks either produces a true negative (the clocks are not comparable), or else a suggestion that one clock precedes the other, with the possibility of a false positive where the two clocks are unrelated. The false positive rate decreases as more storage is allowed.

## Applications

Modern distributed systems utilize variations of vector clocks to enforce causal ordering of transactions without relying on a central wall-clock time. For instance, the Cerberus protocol uses logical clocks to track the state "version" of each shard. When a transaction spans multiple shards, the vector of these logical clocks allows the network to validate that the transaction is interacting with the most current state of all involved assets, enabling atomic composability in an adversarial environment.
