---
title: "Committed information rate"
source: https://en.wikipedia.org/wiki/Committed_information_rate
domain: traffic-shaping
license: CC-BY-SA-4.0
tags: traffic shaping, token bucket, leaky bucket, traffic policing
fetched: 2026-07-02
---

# Committed information rate

In a Frame Relay network, **committed information rate** (**CIR**) is the bandwidth for a virtual circuit guaranteed by an internet service provider to work under normal conditions. **Committed data rate** (**CDR**) is the payload portion of the CIR.

At any given time, the available bandwidth *should not* fall below this committed figure. The bandwidth is usually expressed in kilobits per second (kbit/s).

Above the CIR, an allowance of burstable bandwidth is often given, whose value can be expressed in terms of an additional rate, known as the excess information rate (EIR), or as its absolute value, peak information rate (PIR). The provider guarantees that the connection will always support the CIR rate, and sometimes the EIR rate provided that there is adequate bandwidth. The PIR, i.e. the CIR plus EIR, is either equal to or less than the speed of the access port into the network. Frame Relay carriers define and package CIRs differently, and CIRs are adjusted with experience.
