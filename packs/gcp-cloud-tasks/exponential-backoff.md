---
title: "Exponential backoff"
source: https://en.wikipedia.org/wiki/Exponential_backoff
domain: gcp-cloud-tasks
license: CC-BY-SA-4.0
tags: gcp cloud tasks, task queue gcp, asynchronous execution gcp, distributed task dispatch
fetched: 2026-07-02
---

# Exponential backoff

**Exponential backoff** is an algorithm that uses feedback to multiplicatively decrease the rate of some process, in order to gradually find an acceptable rate. These algorithms find usage in a wide range of systems and processes, with wireless networks and computer networks being particularly notable.

## Exponential backoff algorithm

An exponential backoff algorithm is a form of closed-loop control system that reduces the rate of a controlled process in response to adverse events. For example, if a mobile app fails to connect to its server, the mobile app might try again 1 second later, then if it fails again, 2 seconds later, then 4, etc. Each time, the pause is multiplied by a fixed amount (in this case, 2). In this case, the adverse event is failing to connect to the server. Other examples of adverse events include collisions of network traffic, packet loss, an error response from a service, or an explicit request to reduce the rate (i.e., *back off*).

The rate reduction can be modelled as an exponential function:

$t=b^{c}$

or

$f={\frac {1}{b^{c}}}$

Here, *t* is the time delay applied between actions, *b* is the multiplicative factor or *base*, and *c* is the number of adverse events observed. Alternatively, *f* is the frequency (or rate) of the process (i.e., number of actions per unit of time). The value of *c* is incremented each time an adverse event is observed, leading to an exponential rise in delay and, therefore, an inversely proportionate rate. An exponential backoff algorithm where *b* = 2 is referred to as a *binary* exponential backoff algorithm.

When the rate has been reduced in response to an adverse event, it usually does not remain at that reduced level forever. If no adverse events are observed for some period of time, often referred to as the *recovery time* or *cooling-off period*, the rate may be increased again. The time period that must elapse before attempting to increase the rate again may, itself, be determined by an exponential backoff algorithm. Typically, recovery of the rate occurs more slowly than reduction of the rate due to backoff and often requires careful tuning to avoid oscillation of the rate. The exact recovery behaviour is implementation-specific and may be informed by any number of environmental factors.

The mechanism by which rate reduction is achieved in a system may be more complex than a simple time delay. In some cases, the value *t* may refer to an upper bound on the time delay, rather than a specific time delay value. The name *exponential backoff* refers to the exponential growth characteristic of the backoff, rather than an exact numeric relationship between adverse event counts and delay times.

## Rate limiting

Exponential backoff is commonly utilised as part of rate limiting mechanisms in computer systems such as web services, to help enforce fair distribution of access to resources and prevent network congestion. Each time a service informs a client that it is sending requests too frequently, the client reduces its rate by some predetermined factor until the client's request rate reaches an acceptable equilibrium. The service may enforce rate limiting by refusing to respond to requests when the client is sending them too frequently, so that misbehaving clients are not allowed to exceed their allotted resources.

A benefit of utilising an exponential backoff algorithm over a fixed rate limit is that rate limits through exponential backoff can be achieved dynamically without providing any prior information to the client. In the event that resources are unexpectedly constrained, e.g., due to heavy load or a service disruption, backoff requests and error responses from the service can automatically decrease the request rate from clients. This can help maintain some level of availability rather than overloading the service. In addition, quality of service can be prioritised to certain clients based on their individual importance, e.g., by reducing the backoff for emergency calls on a telephone network during periods of high load.

In a simple version of the algorithm, messages are delayed by a predetermined (non-random) time. For example, in SIP protocol over unreliable transport (such as UDP) the client retransmits requests at an interval that starts at T1 seconds (usually 500 ms, which is the estimate of the round-trip time) and doubles after every retransmission until it reaches T2 seconds (which defaults to 4 s). This results in retransmission intervals of 500 ms, 1 s, 2 s, 4 s, 4 s then 4 s.

## Collision avoidance

Exponential backoff algorithms can be used to avoid network collisions. In a point-to-multipoint or statistical time-division multiplexed network, multiple senders communicate over a single shared channel. If two senders attempt to transmit a message at the same time, or *talk over* each other, a collision occurs and the messages are damaged or lost. Each sender can then back off before attempting to retransmit the same message again.

A deterministic exponential backoff algorithm is unsuitable for this use case since each sender would back off for the same time period, leading them to retransmit simultaneously and cause another collision. Instead, for purposes of collision avoidance, the time between retransmissions is randomized and the exponential backoff algorithm sets the *range* of delay values that are possible. The time delay is usually measured in slots, which are fixed-length periods of time on the network. In a binary exponential backoff algorithm (i.e., one where $b=2$ ), after c collisions, each retransmission is delayed by a random number of slot times between 0 and $2^{c}-1$ . After the first collision, each sender will wait 0 or 1 slot times. After the second collision, the senders will wait anywhere from 0 to 3 slot times (inclusive). After the third collision, the senders will wait anywhere from 0 to 7 slot times (inclusive), and so forth. As the number of retransmission attempts increases, the number of possibilities for delay increases exponentially. This decreases the probability of a collision but increases the average latency.

Exponential backoff is utilised during retransmission of frames in carrier-sense multiple access with collision avoidance (CSMA/CA) and carrier-sense multiple access with collision detection (CSMA/CD) networks, where this algorithm is part of the channel access method used to send data on these networks. In Ethernet networks, the algorithm is commonly used to schedule retransmissions after collisions. The retransmission is delayed by an amount of time derived from the slot time (for example, the time it takes to send 512 bits; i.e., 512 bit-times) and the number of attempts to retransmit.

### Example

This example is from the Ethernet protocol, where a sending host is able to know when a collision has occurred (that is, another host has tried to transmit), when it is sending a frame. If both hosts attempted to re-transmit as soon as a collision occurred, there would be yet another collision — and the pattern would continue forever. The hosts must choose a random value within an acceptable range to ensure that this situation doesn't happen. An exponential backoff algorithm is therefore used. The value 51.2 μs is used as an example here because it is the slot time for a 10 Mbit/s Ethernet line. However, 51.2 μs could be replaced by any positive value, in practice.

1. When a collision first occurs, send a *jamming signal* to prevent further data from being sent.
2. Resend a frame after either 0 seconds or 51.2 μs, chosen at random.
3. If that fails, resend the frame after either 0 s, 51.2 μs, 102.4 μs, or 153.6 μs.
4. If that still fails, resend the frame after k · 51.2 μs, where k is a random integer between 0 and 23 − 1.
5. For further failures, after the *c*th failed attempt, resend the frame after k · 51.2 μs, where k is a random integer between 0 and 2*c* − 1.

## History and theory

In a seminal paper published in AFIPS 1970, Norman Abramson presented the idea of multiple users, on different islands, sharing a single radio channel (i.e., a single frequency) to access the main computer at the University of Hawaii without any time synchronization. Packet collisions at the receiver of the main computer are treated by senders after a timeout as detected errors. Each sender not receiving a positive acknowledgement from the main computer would retransmit its lost packet. Abramson assumed that the sequence of packets transmitted into the shared channel is a Poisson process at rate G, which is the sum of the rate S of new packet arrivals to senders and the rate of retransmitted packets into the channel. Assuming steady state, he showed that the channel throughput rate is $S=Ge^{-2G}$ with a maximum value of 1/(2e) = 0.184 in theory.

Larry Roberts considered a time-slotted ALOHA channel with each time slot long enough for a packet transmission time. (A satellite channel using the TDMA protocol is time slotted.) Using the same Poisson process and steady state assumptions as Abramson, Larry Roberts showed that the maximum throughput rate is 1/e = 0.368 in theory. Roberts was the program manager of the ARPANET research project. Inspired by the slotted ALOHA idea, Roberts initiated a new ARPANET Satellite System (ASS) project to include satellite links in the ARPANET.

Simulation results by Abramson, his colleagues, and others showed that an ALOHA channel, slotted or not, is unstable and would sometimes go into congestion collapse. How much time until congestion collapse depended on the arrival rate of new packets as well as other unknown factors. In 1971, Larry Roberts asked Professor Leonard Kleinrock and his Ph.D. student, Simon Lam, at UCLA to join the Satellite System project of ARPANET. Simon Lam would work on the stability, performance evaluation, and adaptive control of slotted ALOHA for his Ph.D. dissertation research. The first paper he co-authored with Kleinrock was ARPANET Satellite System (ASS) Note 12 disseminated to the ASS group in August 1972. In this paper, a slot chosen randomly over an interval of K slots was used for retransmission. A new result from the model is that increasing K increases channel throughput, which converges to 1/e as K increases to infinity. This model retained the assumptions of Poisson arrivals and steady state and was not intended for understanding statistical behaviour and congestion collapse.

### Stability and adaptive backoff

To understand stability, Lam created a discrete-time Markov chain model for analyzing the statistical behaviour of slotted ALOHA in chapter 5 of his dissertation. The model has three parameters: *N*, *s*, and *p*. *N* is the total number of users. At any time, each user may be idle or blocked. Each user has at most one packet to transmit in the next time slot. An idle user generates a new packet with probability *s* and transmits it in the next time slot immediately. A blocked user transmits its backlogged packet with probability *p*, where 1/*p* = (*K*+1)/2 to keep the average retransmission interval the same. The throughput-delay results of the two retransmission methods were compared by extensive simulations and found to be essentially the same.

Lam’s model provides mathematically rigorous answers to the stability questions of slotted ALOHA, as well as an efficient algorithm for computing the throughput-delay performance for any stable system. There are 3 key results, shown below, from Lam’s Markov chain model in Chapter 5 of his dissertation (also published jointly with Professor Len Kleinrock, in IEEE Transactions on Communications).)

1. Slotted ALOHA with Poisson arrivals (i.e., infinite *N*) is inherently unstable, because a stationary probability distribution does not exist. (Reaching steady state was a key assumption used in the models of Abramson and Roberts.)
2. For slotted ALOHA with a finite *N* and a finite *K*, the Markov chain model can be used to determine whether the system is stable or unstable for a given input rate (*N*×*s*) and, if it is stable, compute its average packet delay and channel throughput rate.
3. Increasing *K* increases the maximum number of users that can be accommodated by a stable slotted ALOHA channel.

#### Corollary

For a finite (*N* × *s*), an unstable channel for the current *K* value can be made stable by increasing *K* to a sufficiently large value, to be referred to as its *K*(*N*,*s*).

### Heuristic RCP for adaptive backoff

Lam used Markov decision theory and developed optimal control policies for slotted ALOHA, but these policies require all blocked users to know the current state (number of blocked users) of the Markov chain. In 1973, Lam decided that instead of using a complex protocol for users to estimate the system state, he would create a simple algorithm for each user to use its own local information, i.e., the number of collisions its backlogged packet has encountered. Applying the above Corollary, Lam invented the following class of adaptive backoff algorithms (named Heuristic RCP).

A Heuristic RCP algorithm consists of the following steps: (1) Let *m* denote the number of previous collisions incurred by a packet at a user as the feedback information in its control loop. For a new packet, *K*(0) is initialized to 1. (2) The packet’s retransmission interval *K*(*m*) increases as *m* increases (until the channel becomes stable, as implied by the above Corollary). For implementation, with *K*(0)=1, as m increases, *K*(*m*) can be increased by multiplication (or by addition).

#### Observation

Binary Exponential Backoff (BEB) used in Ethernet several years later is a special case of Heuristic RCP with $K(m)=2^{m}$ .

BEB is very easy to implement. It is, however, not optimal for many applications because BEB uses 2 as the only multiplier, which provides no flexibility for optimization. In particular, for a system with a large number of users, BEB increases *K*(*m*) too slowly. On the other hand, for a system with a small number of users, a fairly small *K* is sufficient for the system to be stable, and backoff would not be necessary.

To illustrate an example of a multiplicative RCP that uses several multipliers, see the bottom row in Table 6.3 on page 214 in Chapter 6 of Lam’s dissertation, or the bottom row in Table III on page 902 in the Lam-Kleinrock paper. In this example:

1. A new packet is transmitted immediately, *m*=0, *K*(0)=1
2. For a packet with 1 previous collision, *K*(1) = *K*(0) × 10 = 10 (The multiplier jumps up directly to *K** = 10 which was found to be the optimum *K* value at steady state for this particular system (slotted ALOHA for a satellite channel).
3. For a packet with 2 previous collisions, *K*(2) = *K*(1) × 10 = 100 (one more collision, *K* jumps up 10 times).
4. *K*(3) = *K*(2) × 2 = 200
5. *K*(*m*)=*K*(*m*−1) for *m*≥4

For this example, *K*=200 is sufficient for a stable slotted ALOHA system with *N* equal to about 400, which follows from result 3 above Corollary. There is no need to increase *K* any further.

## Truncated exponential backoff

The 'truncated' variant of the algorithm introduces a limit on *c*. This simply means that after a certain number of increases, the exponentiation stops. Without a limit on *c*, the delay between transmissions may become undesirably long if a sender repeatedly observes adverse events, e.g., due to a degradation in network performance. In a randomized system, this may occur by chance, leading to unpredictable latency; longer delays due to unbounded increases in *c* are exponentially less probable, but they are effectively inevitable on a busy network due to the law of truly large numbers. Limiting *c* helps to reduce the possibility of unexpectedly long transmission latencies and improve recovery times after a transient outage.

For example, if the ceiling is set at *i* = 10 in a truncated binary exponential backoff algorithm, (as it is in the IEEE 802.3 CSMA/CD standard), then the maximum delay is 1023 slot times, i.e. 210 − 1.

Selecting an appropriate backoff limit for a system involves striking a balance between collision probability and latency. By increasing the ceiling, there is an exponential reduction in the probability of collision on each transmission attempt. At the same time, increasing the limit also exponentially increases the range of possible latency times for a transmission, leading to less deterministic performance and an increase in the average latency. The optimal limit value for a system is specific to both the implementation and environment.

## Expected backoff

Given a uniform distribution of backoff times, the expected backoff time is the mean of the possibilities. After *c* collisions in a binary exponential backoff algorithm, the delay is randomly chosen from [0, 1, ..., *N*] slots, where *N* = 2*c* − 1, and the expected backoff time (in slots) is

$\operatorname {E} (c)={\frac {1}{N+1}}\sum _{i=0}^{N}i={\frac {1}{N+1}}{\frac {N(N+1)}{2}}={\frac {N}{2}}.$

For example, the expected backoff time for the third (*c* = 3) collision, one could first calculate the maximum backoff time, *N*:

$N=2^{c}-1$

$N=2^{3}-1=8-1$

$N=7,$

and then calculate the mean of the backoff time possibilities:

$\operatorname {E} (c)={\frac {1}{N+1}}\sum _{i=0}^{N}i={\frac {1}{N+1}}{\frac {N(N+1)}{2}}={\frac {N}{2}}={\frac {2^{c}-1}{2}}$

.

which is, for the example, *E*(3) = 3.5 slots.
