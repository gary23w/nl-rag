---
title: "Weighted fair queueing"
source: https://en.wikipedia.org/wiki/Weighted_fair_queueing
domain: queue-management
license: CC-BY-SA-4.0
tags: active queue management, weighted fair queueing, random early detection, congestion avoidance
fetched: 2026-07-02
---

# Weighted fair queueing

**Weighted fair queueing** (**WFQ**) is a network scheduling algorithm. WFQ is both a packet-based implementation of the generalized processor sharing (GPS) policy, and a natural extension of fair queuing (FQ). Whereas FQ shares the link's capacity in equal subparts, WFQ allows schedulers to specify, for each flow, which fraction of the capacity will be given.

Weighted fair queuing is also known as packet-by-packet GPS (PGPS or P-GPS) since it approximates generalized processor sharing "to within one packet transmission time, regardless of the arrival patterns."

## Parametrization and fairness

Like other GPS-like scheduling algorithms, the choice of the weights is left to the network administrator. There is no unique definition of what is "fair" (see Fair queuing § Fairness for further discussion).

By regulating the WFQ weights dynamically, WFQ can be utilized for controlling the quality of service, for example, to achieve guaranteed data rate.

Proportionally fair behavior can be achieved by setting the weights to $w_{i}=1/c_{i}$ , where $c_{i}$ is the cost per data bit of data flow i . For example, in CDMA spread spectrum cellular networks, the cost may be the required energy (the interference level), and in dynamic channel allocation systems, the cost may be the number of nearby base station sites that can not use the same frequency channel, in view to avoid co-channel interference.

## Algorithm

In WFQ, a scheduler handling N flows is configured with one weight $w_{i}$ for each flow. Then, the flow of number i will achieve an average data rate of ${\frac {w_{i}}{(w_{1}+w_{2}+...+w_{N})}}R$ , where R is the link rate. A WFQ scheduler where all weights are equal is a FQ scheduler.

Like all fair-queuing schedulers, each flow is protected from the others, and it can be proved that if a data flow is leaky bucket constrained, an end-to-end delay bound can be guaranteed.

The algorithm of WFQ is very similar to the one of FQ. For each packet, a virtual theoretical departure date will be computed, defined as the departure date if the scheduler was a perfect GPS scheduler. Then, each time the output link is idle, the packet with the smallest date is selected for emission.

The pseudo code can be obtained simply from the one of FQ by replacing the computation of the virtual departure time by

```
packet.virFinish = virStart + packet.size / Ri
```

with $R_{i}={\frac {w_{i}}{(w_{1}+w_{2}+...+w_{N})}}R$ .

## WFQ as a GPS approximation

WFQ, under the name PGPS, has been designed as "an excellent approximation to GPS", and it has been proved that it approximates GPS "to within one packet transmission time, regardless of the arrival patterns."

Since WFQ implementation is similar to fair queuing, it has the same *O(log(n))* complexity, where *n* is the number of flows. This complexity comes from the need to select the queue with the smallest virtual finish time each time a packet is sent.

After WFQ, several other implementations of GPS have been defined.

- Even if WFQ is at most "one packet" late w.r.t. the ideal GPS policy, it can be arbitrarily ahead. The *Worst-case Fair Weighted Fair Queueing* (WF2Q) fixes it by adding a virtual start of service to each packet, and selects a packet only if its virtual start of service is not less than the current time.
- The selection of the queue with minimal virtual finish time can be hard to implement at wire speed. Then, other approximations of GPS have been defined with less complexity, like deficit round robin.

## History

The introduction of parameters to share the bandwidth in an arbitrary way in mentioned at the end of as a possible extension to FQ. The term *weighted* first appears in.
