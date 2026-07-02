---
title: "Gossip protocol"
source: https://en.wikipedia.org/wiki/Gossip_protocol
domain: distributed-systems
license: CC-BY-SA-4.0
tags: distributed system, distributed computing, cap theorem, consistency model, eventual consistency
fetched: 2026-07-02
---

# Gossip protocol

A **gossip protocol** or **epidemic protocol** is a procedure or process of computer peer-to-peer communication that is based on the way epidemics spread. Some distributed systems use peer-to-peer gossip to ensure that data is disseminated to all members of a group. Some ad-hoc networks have no central registry and the only way to spread common data is to rely on each member to pass it along to their neighbors.

## Communication

The concept of *gossip communication* can be illustrated by the analogy of office workers spreading rumors. Let's say each hour the office workers congregate around the water cooler. Each employee pairs off with another, chosen at random, and shares the latest gossip. At the start of the day, Dave starts a new rumor: he comments to Bob that he believes that Charlie dyes his mustache. At the next meeting, Bob tells Alice, while Dave repeats the idea to Eve. After each water cooler rendezvous, the number of individuals who have heard the rumor roughly doubles (though this doesn't account for gossiping twice to the same person; perhaps Dave tries to tell the story to Frank, only to find that Frank already heard it from Alice). Computer systems typically implement this type of protocol with a form of random "peer selection": with a given frequency, each machine picks another machine at random and shares any rumors.

## Variants and styles

There are probably hundreds of variants of specific gossip-like protocols because each use-scenario is likely to be customized to the organization's specific needs.

For example, a gossip protocol might employ some of these ideas:

- The core of the protocol involves periodic, pairwise, inter-process interactions.
- The information exchanged during these interactions is of bounded size.
- When agents interact, the state of at least one agent changes to reflect the state of the other.
- Reliable communication is not assumed.
- The frequency of the interactions is low compared to typical message latencies so that the protocol costs are negligible.
- There is some form of randomness in the peer selection. Peers might be selected from the full set of nodes or from a smaller set of neighbors.
- Due to the replication there is an implicit redundancy of the delivered information.

## Protocol types

It is useful to distinguish two prevailing styles of gossip protocol:

- **Dissemination protocols** (or rumor-mongering protocols). These use gossip to spread information; they basically work by flooding agents in the network, but in a manner that produces bounded worst-case loads:
  1. *Event dissemination protocols* use gossip to carry out multicasts. They report events, but the gossip occurs periodically and events don't actually trigger the gossip. One concern here is the potentially high latency from when the event occurs until it is delivered.
  2. *Background data dissemination protocols* continuously gossip about information associated with the participating nodes. Typically, propagation latency isn't a concern, perhaps because the information in question changes slowly or there is no significant penalty for acting upon slightly stale data.
- **Protocols that compute aggregates**. These compute a network-wide aggregate by sampling information at the nodes in the network and combining the values to arrive at a system-wide value – the largest value for some measurement nodes are making, smallest, etc. The key requirement is that the aggregate must be computable by fixed-size pairwise information exchanges; these typically terminate after a number of rounds of information exchange logarithmic in the system size, by which time an all-to-all information flow pattern will have been established. As a side effect of aggregation, it is possible to solve other kinds of problems using gossip; for example, there are gossip protocols that can arrange the nodes in a gossip overlay into a list sorted by node-id (or some other attribute) in logarithmic time using aggregation-style exchanges of information. Similarly, there are gossip algorithms that arrange nodes into a tree and compute aggregates such as "sum" or "count" by gossiping in a pattern biased to match the tree structure.

Many protocols that predate the earliest use of the term "gossip" fall within this rather inclusive definition. For example, Internet routing protocols often use gossip-like information exchanges. A gossip substrate can be used to implement a standard routed network: nodes "gossip" about traditional point-to-point messages, effectively pushing traffic through the gossip layer. Bandwidth permitting, this implies that a gossip system can potentially support any classic protocol or implement any classical distributed service. However, such a broadly inclusive interpretation is rarely intended. More typically gossip protocols are those that specifically run in a regular, periodic, relatively lazy, symmetric and decentralized manner; the high degree of symmetry among nodes is particularly characteristic. Thus, while one could run a 2-phase commit protocol over a gossip substrate, doing so would be at odds with the spirit, if not the wording, of the definition.

The term *convergently consistent* is sometimes used to describe protocols that achieve exponentially rapid spread of information. For this purpose, a protocol must propagate any new information to all nodes that will be affected by the information within time logarithmic in the size of the system (the "mixing time" must be logarithmic in system size).

## Examples

Suppose that we want to find the object that most closely matches some search pattern, within a network of unknown size, but where the computers are linked to one another and where each machine is running a small *agent* program that implements a gossip protocol.

- To start the search, a user would ask the local agent to begin to gossip about the search string. (We're assuming that agents either start with a known list of peers, or retrieve this information from some kind of a shared store.)
- Periodically, at some rate (let's say ten times per second, for simplicity), each agent picks some other agent at random, and gossips with it. Search strings known to A will now also be known to B, and vice versa. In the next "round" of gossip A and B will pick additional random peers, maybe C and D. This round-by-round doubling phenomenon makes the protocol very robust, even if some messages get lost, or some of the selected peers are the same or already know about the search string.
- On receipt of a search string for the first time, each agent checks its local machine for matching documents.
- Agents also gossip about the best match, to date. Thus, if A gossips with B, after the interaction, A will know of the best matches known to B, and vice versa. Best matches will "spread" through the network.

If the messages might get large (for example, if many searches are active all at the same time), a size limit should be introduced. Also, searches should "age out" of the network.

It follows that within logarithmic time in the size of the network (the number of agents), any new search string will have reached all agents. Within an additional delay of the same approximate length, every agent will learn where the best match can be found. In particular, the agent that started the search will have found the best match.

For example, in a network with 25,000 machines, we can find the best match after about 30 rounds of gossip: 15 to spread the search string and 15 more to discover the best match. A gossip exchange could occur as often as once every tenth of a second without imposing undue load, hence this form of network search could search a big data center in about three seconds.

In this scenario, searches might automatically age out of the network after, say, 10 seconds. By then, the initiator knows the answer and there is no point in further gossip about that search.

Gossip protocols have also been used for achieving and maintaining distributed database consistency or with other types of data in consistent states, counting the number of nodes in a network of unknown size, spreading news robustly, organizing nodes according to some structuring policy, building so-called overlay networks, computing aggregates, sorting the nodes in a network, electing leaders, etc.

## Epidemic algorithms

Gossip protocols can be used to propagate information in a manner rather similar to the way that a viral infection spreads in a biological population. Indeed, the mathematics of epidemics are often used to model the mathematics of gossip communication. The term *epidemic algorithm* is sometimes employed when describing a software system in which this kind of gossip-based information propagation is employed.
