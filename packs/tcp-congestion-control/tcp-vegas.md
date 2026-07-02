---
title: "TCP Vegas"
source: https://en.wikipedia.org/wiki/TCP_Vegas
domain: tcp-congestion-control
license: CC-BY-SA-4.0
tags: tcp congestion control, cubic tcp, tcp vegas, bufferbloat
fetched: 2026-07-02
---

# TCP Vegas

**TCP Vegas** is a TCP congestion avoidance algorithm that emphasizes packet delay, rather than packet loss, as a signal to help determine the rate at which to send packets. It was developed at the University of Arizona by Lawrence Brakmo and Larry L. Peterson and introduced in 1994.

TCP Vegas was one of the first delay-based congestion control algorithms, representing a paradigm shift from traditional loss-based approaches. Unlike TCP Reno which waits for packet loss to indicate congestion, Vegas monitors changes in round-trip time to proactively detect network congestion before buffers overflow and packets are dropped. This approach allows Vegas to maintain smaller queue sizes and achieve lower latency compared to loss-based algorithms.

TCP Vegas detects congestion at an incipient stage based on increasing Round-Trip Time (RTT) values of the packets in the connection unlike other flavors such as Reno, New Reno, etc., which detect congestion only after it has actually happened via packet loss. The algorithm depends heavily on accurate calculation of the Base RTT value. If it is too small then throughput of the connection will be less than the bandwidth available while if the value is too large then it will overrun the connection.

A lot of research is going on regarding the fairness provided by the linear increase/decrease mechanism for congestion control in Vegas. One interesting caveat is when Vegas is inter-operated with other versions like Reno. In this case, performance of Vegas degrades because Vegas reduces its sending rate before Reno, as it detects congestion early and hence gives greater bandwidth to co-existing TCP Reno flows. This unfairness issue arises because Vegas interprets the increased queuing delay caused by aggressive Reno flows as congestion and backs off, while Reno continues to increase its window until packet loss occurs.

TCP Vegas is one of several *flavors* of TCP congestion avoidance algorithms. It is one of a series of efforts at TCP tuning that adapt congestion control and system behaviors to new challenges faced by increases in available bandwidth in Internet components on networks like Internet2.

TCP Vegas has been implemented in the Linux kernel, in FreeBSD, in Solaris. Despite its implementation in major operating systems, TCP Vegas has seen limited deployment in production environments. Linux included Vegas support starting with kernel 2.4.13 in 2001, where it can be enabled through the sysctl interface. However, due to the fairness issues when competing with loss-based algorithms and the need for accurate RTT measurements, Vegas is rarely enabled by default. The algorithm has found more success in controlled environments such as data centers and private networks where all hosts can use the same congestion control algorithm. Some modern algorithms, including TCP BBR developed by Google, have drawn inspiration from Vegas's delay-based approach while attempting to address its shortcomings. Research continues on hybrid approaches that combine Vegas's proactive congestion detection with mechanisms to ensure fair competition with loss-based algorithms.
