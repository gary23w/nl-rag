---
title: "Kendall's notation"
source: https://en.wikipedia.org/wiki/Kendall%27s_notation
domain: queueing-theory
license: CC-BY-SA-4.0
tags: queueing theory, birth-death process, kendall notation, little's law
fetched: 2026-07-02
---

# Kendall's notation

In queueing theory, a discipline within the mathematical theory of probability, **Kendall's notation** (or sometimes **Kendall notation**) is the standard system used to describe and classify a queueing node. D. G. Kendall proposed describing queueing models using three factors written A/S/*c* in 1953 where A denotes the time between arrivals to the queue, S the service time distribution and *c* the number of service channels open at the node. It has since been extended to A/S/*c*/*K*/*N*/D where *K* is the capacity of the queue, *N* is the size of the population of jobs to be served, and D is the queueing discipline.

When the final three parameters are not specified (e.g. M/M/1 queue), it is assumed *K* = ∞, *N* = ∞ and D = FIFO.

## First example: M/M/1 queue

A M/M/1 queue means that the time between arrivals is Markovian (M), i.e. the inter-arrival time follows an exponential distribution of parameter λ. The second M means that the service time is Markovian: it follows an exponential distribution of parameter μ. The last parameter is the number of service channel, which is one (1).

## Description of the parameters

In this section, we describe the parameters A/S/*c*/*K*/*N*/D from left to right.

### A: The arrival process

A code describing the arrival process. The codes used are:

| Symbol | Name | Description | Examples |
|---|---|---|---|
| M | Markovian or memoryless | Poisson process (or random) arrival process (i.e., exponential inter-arrival times). | M/M/1 queue |
| M*X* | batch Markov | Poisson process with a random variable *X* for the number of arrivals at one time. | MX/MY/1 queue |
| MAP | Markovian arrival process | Generalisation of the Poisson process. |   |
| BMAP | Batch Markovian arrival process | Generalisation of the *MAP* with multiple arrivals |   |
| MMPP | Markov modulated poisson process | Poisson process where arrivals are in "clusters". |   |
| D | Degenerate distribution | A deterministic or fixed inter-arrival time. | D/M/1 queue |
| E*k* | Erlang distribution | An Erlang distribution with *k* as the shape parameter (i.e., sum of *k* i.i.d. exponential random variables). |   |
| G | General distribution | Although *G* usually refers to independent arrivals, some authors prefer to use *GI* to be explicit. |   |
| PH | Phase-type distribution | Some of the above distributions are special cases of the phase-type, often used in place of a general distribution. |   |

### S: The service time distribution

This gives the distribution of time of the service of a customer. Some common notations are:

| Symbol | Name | Description | Examples |
|---|---|---|---|
| M | Markovian or memoryless | Exponential service time. | M/M/1 queue |
| M*Y* | bulk Markov | Exponential service time with a random variable *Y* for the size of the batch of entities serviced at one time. | MX/MY/1 queue |
| D | Degenerate distribution | A deterministic or fixed service time. | M/D/1 queue |
| E*k* | Erlang distribution | An Erlang distribution with *k* as the shape parameter (i.e., sum of *k* i.i.d. exponential random variables). |   |
| G | General distribution | Although *G* usually refers to independent service time, some authors prefer to use *GI* to be explicit. | M/G/1 queue |
| PH | Phase-type distribution | Some of the above distributions are special cases of the phase-type, often used in place of a general distribution. |   |
| MMPP | Markov modulated poisson process | Exponential service time distributions, where the rate parameter is controlled by a Markov chain. |   |

### *c*: The number of servers

The number of service channels (or servers). The M/M/1 queue has a single server and the M/M/c queue *c* servers.

### K: The number of places in the queue

The capacity of queue, or the maximum number of customers allowed in the queue. When the number is at this maximum, further arrivals are turned away. If this number is omitted, the capacity is assumed to be unlimited, or infinite.

Note: This is sometimes denoted

c

+

K

where

K

is the buffer size, the number of places in the queue above the number of servers

c

.

### N: The calling population

The size of calling source. The size of the population from which the customers come. A small population will significantly affect the effective arrival rate, because, as more customers are in system, there are fewer free customers available to arrive into the system. If this number is omitted, the population is assumed to be unlimited, or infinite.

### D: The queue's discipline

The Service Discipline or Priority order that jobs in the queue, or waiting line, are served:

| Symbol | Name | Description |
|---|---|---|
| FIFO/FCFS | First In First Out/First Come First Served | The customers are served in the order they arrived in (used by default). |
| LIFO/LCFS | Last in First Out/Last Come First Served | The customers are served in the reverse order to the order they arrived in. |
| SIRO | Service In Random Order | The customers are served in a random order with no regard to arrival order. |
| PQ | Priority Queuing | There are several options: Preemptive Priority Queuing, Non Preemptive Queuing, Class Based Weighted Fair Queuing, Weighted Fair Queuing. |
| PS | Processor Sharing | The customers are served in the determine order with no regard of arrival order. |

Note

: An alternative notation practice is to record the queue discipline before the population and system capacity, with or without enclosing parenthesis. This does not normally cause confusion because the notation is different.
