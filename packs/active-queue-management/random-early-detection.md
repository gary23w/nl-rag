---
title: "Random early detection"
source: https://en.wikipedia.org/wiki/Random_early_detection
domain: active-queue-management
license: CC-BY-SA-4.0
tags: active queue management, random early detection, controlled delay, weighted fair queueing
fetched: 2026-07-02
---

# Random early detection

**Random early detection** (**RED**), also known as **random early discard** or **random early drop**, is a queuing discipline for a network scheduler suited for congestion avoidance.

In the conventional tail drop algorithm, a router or other network component buffers as many packets as it can, and simply drops the ones it cannot buffer. If buffers are constantly full, the network is congested. Tail drop distributes buffer space unfairly among traffic flows. Tail drop can also lead to TCP global synchronization as all TCP connections "hold back" simultaneously, and then step forward simultaneously. Networks become under-utilized and flooded—alternately, in waves.

RED addresses these issues by pre-emptively dropping packets before the buffer becomes completely full. It uses predictive models to decide which packets to drop. It was invented in the early 1990s by Sally Floyd and Van Jacobson.

## Operation

RED monitors the average queue size and drops (or marks when used in conjunction with ECN) packets based on statistical probabilities. If the buffer is almost empty, then all incoming packets are accepted. As the queue grows, the probability for dropping an incoming packet grows too. When the buffer is full, the probability has reached 1 and all incoming packets are dropped.

RED is more fair than tail drop, in the sense that it does not possess a bias against bursty traffic that uses only a small portion of the bandwidth. The more a host transmits, the more likely it is that its packets are dropped as the probability of a host's packet being dropped is proportional to the amount of data it has in a queue. Early detection helps avoid TCP global synchronization.

## Problems with classic RED

According to Van Jacobson, "there are not one, but two bugs in classic RED." Improvements to the algorithm were developed, and a draft paper was prepared, but the paper was never published, and the improvements were not widely disseminated or implemented. There has been some work in trying to finish off the research and fix the bugs.

Pure RED does not accommodate quality of service (QoS) differentiation. Weighted RED (WRED) and RED with In and Out (RIO) provide early detection with QoS considerations.

## Other variants

### WRED

In weighted RED you can have different probabilities for different priorities (IP precedence, DSCP) and/or queues.

### ARED

The adaptive RED or active RED (ARED) algorithm infers whether to make RED more or less aggressive based on the observation of the average queue length. If the average queue length oscillates around *min* threshold then early detection is too aggressive. On the other hand, if the average queue length oscillates around *max* threshold then early detection is being too conservative. The algorithm changes the probability according to how aggressively it senses it has been discarding traffic.

See Srikant for an in-depth account on these techniques and their analysis.

### RRED

Robust random early detection (RRED) algorithm was proposed to improve the TCP throughput against Denial-of-Service (DoS) attacks, particularly Low-rate Denial-of-Service (LDoS) attacks. Experiments have confirmed that the existing RED-like algorithms are notably vulnerable under Low-rate Denial-of-Service (LDoS) attacks due to the oscillating TCP queue size caused by the attacks. RRED algorithm can significantly improve the performance of TCP under Low-rate Denial-of-Service attacks.
