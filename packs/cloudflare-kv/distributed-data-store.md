---
title: "Distributed data store"
source: https://en.wikipedia.org/wiki/Distributed_data_store
domain: cloudflare-kv
license: CC-BY-SA-4.0
tags: cloudflare kv, workers kv, edge key-value, distributed key-value store
fetched: 2026-07-02
---

# Distributed data store

A **distributed data store** is a computer network where information is stored on more than one node, often in a replicated fashion. It is usually specifically used to refer to either a distributed database where users store information on a *number of nodes*, or a computer network in which users store information on a *number of peer network nodes*.

## Distributed databases

Distributed databases are usually non-relational databases that enable a quick access to data over a large number of nodes. Some distributed databases expose rich query abilities while others are limited to a key-value store semantics. Examples of limited distributed databases are Google's Bigtable, which is much more than a distributed file system or a peer-to-peer network, Amazon's Dynamo and Microsoft Azure Storage.

As the ability of arbitrary querying is not as important as the availability, designers of distributed data stores have increased the latter at an expense of consistency. But the high-speed read/write access results in reduced consistency, as it is not possible to guarantee both consistency and availability on a partitioned network, as stated by the CAP theorem.

## Peer network node data stores

In peer network data stores, the user can usually reciprocate and allow other users to use their computer as a storage node as well. Information may or may not be accessible to other users depending on the design of the network.

Most peer-to-peer networks do not have distributed data stores in that the user's data is only available when their node is on the network. However, this distinction is somewhat blurred in a system such as BitTorrent, where it is possible for the originating node to go offline but the content to continue to be served. Still, this is only the case for individual files requested by the redistributors, as contrasted with networks such as Hyphanet, Winny, Share and Perfect Dark where any node may be storing any part of the files on the network.

Distributed data stores typically use an error detection and correction technique. Some distributed data stores (such as Parchive over NNTP) use forward error correction techniques to recover the original file when parts of that file are damaged or unavailable. Others try again to download that file from a different mirror.

## Examples

### Distributed non-relational databases

| Product | License | High availability | Notes |
|---|---|---|---|
| Apache Accumulo | AL2 |   |   |
| Aerospike | AGPL |   |   |
| Apache Cassandra | AL2 | Yes | formerly used by Facebook |
| Apache Ignite | AL2 |   |   |
| Bigtable | Proprietary |   | used by Google |
| Couchbase | AL2 |   | used by LinkedIn, PayPal, and eBay |
| CrateDB | AL2 | Yes |   |
| Apache Druid | AL2 |   | used by Netflix, and Yahoo |
| Dynamo | Proprietary |   | used by Amazon |
| etcd | AL2 | Yes |   |
| Hazelcast | AL2, Proprietary |   |   |
| HBase | AL2 | Yes | formerly used by Facebook |
| Hypertable | GPL 2 |   | Baidu |
| MongoDB | SSPL |   |   |
| MySQL NDB Cluster | GPL 2 | Yes | SQL and NoSQL APIs |
| Riak | AL2 | Yes |   |
| Redis | BSD License | Yes |   |
| ScyllaDB | AGPL |   |   |
| Voldemort | AL2 |   | used by LinkedIn |

### Peer network node data stores

- BitTorrent
- Blockchain (database)
- Chord project
- Freenet
- GNUnet
- IPFS
- Mnet
- Napster
- NNTP (the distributed data storage protocol used for Usenet news)
- Unity, of the software Perfect Dark
- Share
- Siacoin
- DeNet
- Storage@home
- Tahoe-LAFS
- Winny
- ZeroNet
