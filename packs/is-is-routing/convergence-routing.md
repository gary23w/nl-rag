---
title: "Convergence (routing)"
source: https://en.wikipedia.org/wiki/Convergence_(routing)
domain: is-is-routing
license: CC-BY-SA-4.0
tags: is-is protocol, link-state routing, interior gateway protocol, network convergence
fetched: 2026-07-02
---

# Convergence (routing)

**Convergence** is the state of a set of routers that have the same topological information about the internetwork in which they operate. For a set of routers to have *converged*, they must have collected all available topology information from each other via the implemented routing protocol, the information they gathered must not contradict any other router's topology information in the set, and it must reflect the real state of the network. In other words: in a converged network all routers "agree" on what the network topology looks like.

Convergence is an important notion for a set of routers that engage in dynamic routing. All interior gateway protocols rely on convergence to function properly. "To have, or be, converged" is the normal state of an operational autonomous system. The Exterior Gateway Routing Protocol BGP typically never converges because the Internet is too big for changes to be communicated fast enough.

## Convergence process

When a routing protocol process is enabled, every participating router will attempt to exchange information about the topology of the network. The extent of this information exchange, the way it is sent and received, and the type of information required vary widely depending on the routing protocol in use, see e.g. RIP, OSPF, BGP4.

A state of convergence is achieved once all routing protocol-specific information has been distributed to all routers participating in the routing protocol process. Any change in the network that affects routing tables will break the convergence temporarily until this change has been successfully communicated to all other routers.

## Convergence time

**Convergence time** is a measure of how fast a group of routers reach the state of convergence. It is one of the main design goals and an important performance indicator for routing protocols, which should implement a mechanism that allows all routers running the protocol to quickly and reliably converge. Of course, the size of the network also plays an important role. A larger network will converge more slowly than a smaller one.

RIP is a routing protocol that converges so slowly that even a network of a few routers can take a couple of minutes to converge. In case of a new route being advertised, triggered updates can speed up RIP's convergence but to flush a route that previously existed takes longer due to the holddown timers in use. OSPF is an example of a fast-converging routing protocol. A network of a few OSPF routers can converge in a matter of seconds.

Certain configuration and hardware conditions will prevent a network from ever converging. For instance, a "flapping" interface (an interface that frequently changes its state between "up" and "down") might cause conflicting information to propagate throughout the network so the routers never agree on its current state. Under certain circumstances it might be desirable to withhold detailed routing information from parts of the network via route aggregation, thereby speeding up convergence of the topological information shared by all routers.
