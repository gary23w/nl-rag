---
title: "Additive increase/multiplicative decrease"
source: https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease
domain: tcp-congestion-control
license: CC-BY-SA-4.0
tags: tcp congestion control, cubic tcp, tcp vegas, bufferbloat
fetched: 2026-07-02
---

# Additive increase/multiplicative decrease

The **additive-increase/multiplicative-decrease** (**AIMD**) algorithm is a feedback control algorithm best known for its use in TCP congestion control. AIMD combines linear growth of the congestion window when there is no congestion with an exponential reduction when congestion is detected. Multiple flows using AIMD congestion control will eventually converge to an equal usage of a shared link. The related schemes of multiplicative-increase/multiplicative-decrease (MIMD) and additive-increase/additive-decrease (AIAD) do not reach stability.

## Algorithm

The approach taken is to increase the transmission rate (window size), probing for usable bandwidth, until loss occurs. The policy of additive increase may, for instance, increase the congestion window by a fixed amount every round-trip time. When congestion is detected, the transmitter decreases the transmission rate by a multiplicative factor; for example, cut the congestion window in half after loss. The result is a saw-tooth behavior that represents the process of bandwidth probing.

AIMD requires a binary congestion signal. Most frequently, packet loss serves as the signal; the multiplicative decrease is triggered when a timeout or an acknowledgement message indicates a packet lost. It is also possible for in-network switches/routers to mark congestion (without discarding packets) as in Explicit Congestion Notification (ECN).

### Mathematical formula

Let $w(t)$ be the congestion window size indicating the amount of data in flight during time slot t , a ( $a>0$ ) be the additive increase parameter, and b ( $0<b<1$ ) be the multiplicative decrease factor.

$w(t+1)={\begin{cases}w(t)+a&{\text{ if congestion is not detected}}\\w(t)\times b&{\text{ if congestion is detected}}\end{cases}}$

In TCP, after slow start, the additive increase parameter a is typically one MSS (maximum segment size) per round-trip time, and the multiplicative decrease factor b is typically 1/2.

## Protocols

AIMD congestion avoidance is or was used in:

- Transmission Control Protocol (TCP)
- Scalable TCP (STCP)
- OSI Transport Class 4
- DCCP (in some modes)
- DECnet

## In nature

AIMD has been found to be utilized by diverse biological systems, including maintaining cell-size homeostasis and for synaptic learning and adaptation in neural circuits.
