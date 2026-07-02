---
title: "Equal-cost multi-path routing"
source: https://en.wikipedia.org/wiki/Equal-cost_multi-path_routing
domain: ecmp-routing
license: CC-BY-SA-4.0
tags: equal-cost multipath, load sharing, path hashing, flow distribution
fetched: 2026-07-02
---

# Equal-cost multi-path routing

**Equal-cost multi-path routing** (**ECMP**) is a routing strategy where packet forwarding to a single destination can occur over multiple best paths with equal routing priority. Multi-path routing can be used in conjunction with most routing protocols because it is a per-hop local decision made independently at each router. It can substantially increase bandwidth by load-balancing traffic over multiple paths; however, there may be significant problems in deploying it in practice.

## History

Load balancing by per-packet multipath routing was generally disfavored due to the impact of rapidly changing latency, packet reordering and maximum transmission unit (MTU) differences within a network flow, which could disrupt the operation of many Internet protocols, most notably TCP and path MTU discovery. RFC 2992 analyzed one particular multipath routing strategy involving the assignment of flows through hashing flow-related data in the packet header. This solution is designed to avoid these problems by sending all packets from any particular network flow through the same path while balancing multiple flows over multiple paths in general.
