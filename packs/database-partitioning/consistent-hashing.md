---
title: "Consistent hashing"
source: https://en.wikipedia.org/wiki/Consistent_hashing
domain: database-partitioning
license: CC-BY-SA-4.0
tags: database partitioning, table partitioning, data striping, horizontal partitioning
fetched: 2026-07-02
---

# Consistent hashing

In computer science, **consistent hashing** is a special kind of hashing technique such that when a hash table is resized, only $n/m$ keys need to be remapped on average where n is the number of keys and m is the number of slots. Consistent hashing evenly distributes cache keys across shards, even if some of the shards crash or become unavailable. In contrast, in most traditional hash tables, a change in the number of array slots causes nearly all keys to be remapped because the mapping between the keys and the slots is defined by a modular operation.

Consistent hashing is used by Content Delivery Networks because it is useful for distributing requests for content from a rotating population of web servers. Tim Berners-Lee credits consistent hashing algorithms, and Daniel Lewin as their inventor, with solving the slashdotting problem which plagued the World Wide Web in the 1990s.

## History

The term "consistent hashing" was introduced by David Karger *et al.* at MIT for use in distributed caching, particularly for the web. This academic paper from 1997 in Symposium on Theory of Computing introduced the term "consistent hashing" as a way of distributing requests among a changing population of web servers. Each slot is then represented by a server in a distributed system or cluster. The addition of a server and the removal of a server (during scalability or outage) requires only $num\_keys/num\_slots$ items to be re-shuffled when the number of slots (i.e. servers) change. The authors mention linear hashing and its ability to handle sequential server addition and removal, while consistent hashing allows servers to be added and removed in an arbitrary order. The paper was later re-purposed to address technical challenge of keeping track of a file in peer-to-peer networks such as a distributed hash table.

Teradata used this technique in their distributed database, released in 1986, although they did not use this term. Teradata still uses the concept of a hash table to fulfill exactly this purpose. Akamai Technologies was founded in 1998 by the scientists Daniel Lewin and F. Thomson Leighton (co-authors of the article coining "consistent hashing"). In Akamai's content delivery network, consistent hashing is used to balance the load within a cluster of servers, while a stable marriage algorithm is used to balance load across clusters.

Consistent hashing has also been used to reduce the impact of partial system failures in large web applications to provide robust caching without incurring the system-wide fallout of a failure. Consistent hashing is also the cornerstone of distributed hash tables (DHTs), which employ hash values to partition a keyspace across a distributed set of nodes, then construct an overlay network of connected nodes that provide efficient node retrieval by key.

Rendezvous hashing, designed in 1996, is a simpler and more general technique . It achieves the goals of consistent hashing using the very different highest random weight (HRW) algorithm.

## Basic technique

In the problem of load balancing, for example, when a BLOB has to be assigned to one of n servers on a cluster, a standard hash function could be used in such a way that we calculate the hash value for that BLOB, assuming the resultant value of the hash is $\beta$ , we perform modular operation with the number of servers ( n in this case) to determine the server in which we can place the BLOB: $\zeta =\beta \ \%\ n$ ; hence the BLOB will be placed in the server whose ${\text{server ID}}$ is successor of $\zeta$ in this case. However, when a server is added or removed during outage or scaling (when n changes), all the BLOBs in every server should be reassigned and moved due to rehashing, but this operation is expensive.

Consistent hashing was designed to avoid the problem of having to reassign every BLOB when a server is added or removed throughout the cluster. The central idea is to use a hash function that maps both the BLOB and servers to a unit circle, usually $2\pi$ radians. For example, $\zeta =\Phi \ \%\ 360$ (where $\Phi$ is hash of a BLOB or server's identifier, like IP address or UUID). Each BLOB is then assigned to the next server that appears on the circle in clockwise order. Usually, binary search algorithm or linear search is used to find a "spot" or server to place that particular BLOB in $O(\log N)$ or $O(N)$ complexities respectively; and in every iteration, which happens in clockwise manner, an operation $\zeta \ \leq \ \Psi$ (where $\Psi$ is the value of the server within the cluster) is performed to find the server to place the BLOB. This provides an even distribution of BLOBs to servers. But, more importantly, if a server fails and is removed from the circle, only the BLOBs that were mapped to the failed server need to be reassigned to the next server in clockwise order. Likewise, if a new server is added, it is added to the unit circle, and only the BLOBs mapped to that server need to be reassigned.

Importantly, when a server is added or removed, the vast majority of the BLOBs maintain their prior server assignments, and the addition of $n^{th}$ server only causes $1/n$ fraction of the BLOBs to relocate. Although the process of moving BLOBs across cache servers in the cluster depends on the context, commonly, the newly added cache server identifies its "predecessor" and moves all the BLOBs, whose mapping belongs to this server (i.e. whose hash value is less than that of the new server), from it. However, in the case of web page caches, in most implementations there is no involvement of moving or copying, assuming the cached BLOB is small enough. When a request hits a newly added cache server, a cache miss happens and a request to the actual web server is made and the BLOB is cached locally for future requests. The redundant BLOBs on the previously used cache servers would be removed as per the cache eviction policies.

### Implementation

Let $h_{b}(x)$ and $h_{s}(x)$ be the hash functions used for the BLOB and server's unique identifier respectively. In practice, a binary search tree (BST) is used to dynamically maintain the ${\text{server ID}}$ within a cluster or hashring, and to find the successor or minimum within the BST, tree traversal is used.

**Inserting x into the cluster**

Let

$\beta$

be the hash value of a BLOB such that,

$h_{b}(x)=\beta \ \%\ 360$

where

$x\in \mathrm {BLOB}$

and

$h_{b}(x)=\zeta$

. To insert

x

, find the successor of

$\zeta$

in the BST of

${\text{server ID}}$

s. If

$\zeta$

is larger than all of the

${\text{server ID}}$

s, the BLOB is placed in the server with smallest

${\text{server ID}}$

value.

**Deleting x from the cluster**

Find the successor of

$\zeta$

in the BST, remove the BLOB from the returned

${\text{server ID}}$

. If

$\zeta$

has no successor, remove the BLOB from the smallest of the

${\text{server ID}}$

s.

**Insert a server into cluster**

Let

$\Phi$

be the hash value of a server's identifier such that,

$h_{s}(x)=\Phi \ \%\ 360$

where

$x\in \{{\text{IP address, UUID}}\}$

and

$h_{s}(x)=\theta$

. Move all the BLOBs, whose hash value is smaller than

$\theta$

, from the server whose

${\text{server ID}}$

is successor of

$\theta$

. If

$\theta$

is largest of all the

${\text{server ID}}$

s, move the relevant BLOBs from the smallest of the

${\text{server ID}}$

s into

$\theta$

.

**Delete a server from cluster**

Find the successor of

$\theta$

in the BST, move the BLOBs from

$\theta$

into its successor server. If

$\theta$

doesn't have a successor, move the BLOBs into the smallest of the

${\text{server ID}}$

s.

### Variance reduction

To avoid skewness of multiple nodes within the radian, which happen due to lack of uniform distribution of the servers within the cluster, multiple labels are used. Those duplicate labels are called "virtual nodes" i.e. multiple labels which point to a single "real" label or server within the cluster. The amount of virtual nodes or duplicate labels used for a particular server within a cluster is called the "weight" of that particular server.

## Practical extensions

A number of extensions to the basic technique are needed for effectively using consistent hashing for load balancing in practice. In the basic scheme above, if a server fails, all its BLOBs are reassigned to the next server in clockwise order, potentially doubling the load of that server. This may not be desirable. To ensure a more even redistribution of BLOBs on server failure, each server can be hashed to multiple locations on the unit circle. When a server fails, the BLOBs assigned to each of its replicas on the unit circle will get reassigned to a different server in clockwise order, thus redistributing the BLOBs more evenly. Another extension concerns a situation where a single BLOB gets "hot" and is accessed a large number of times and will have to be hosted in multiple servers. In this situation, the BLOB may be assigned to multiple contiguous servers by traversing the unit circle in clockwise order. A more complex practical consideration arises when two BLOBs are hashed near each other in the unit circle and both get "hot" at the same time. In this case, both BLOBs will use the same set of contiguous servers in the unit circle. This situation can be ameliorated by each BLOB choosing a different hash function for mapping servers to the unit circle.

## Comparison with rendezvous hashing and other alternatives

Rendezvous hashing, designed in 1996, is a simpler and more general technique, and permits fully distributed agreement on a set of k options out of a possible set of n options. It can in fact be shown that consistent hashing is a special case of rendezvous hashing. Because of its simplicity and generality, rendezvous hashing is now being used in place of Consistent Hashing in many applications.

If key values will always increase monotonically, an alternative approach using a hash table with monotonic keys may be more suitable than consistent hashing.

## Complexity

|   | Classic hash table | Consistent hashing |
|---|---|---|
| add a node | $O(K)$ | $O(K/N+\log N)$ |
| remove a node | $O(K)$ | $O(K/N+\log N)$ |
| lookup a key | $O(1)$ | $O(\log N)$ |
| add a key | $O(1)$ | $O(\log N)$ |
| remove a key | $O(1)$ | $O(\log N)$ |

The $O(K/N)$ is an average cost for redistribution of keys and the $O(\log N)$ complexity for consistent hashing comes from the fact that a binary search among nodes angles is required to find the next node on the ring.

## Examples

Known examples of consistent hashing use include:

- Couchbase automated data partitioning
- OpenStack's Object Storage Service Swift
- Partitioning component of Amazon's storage system Dynamo
- Data partitioning in Apache Cassandra
- Data partitioning in ScyllaDB
- Data partitioning in Voldemort
- Akka's consistent hashing router
- Riak, a distributed key-value database
- Gluster, a network-attached storage file system
- Akamai content delivery network
- Discord chat application
- Load balancing gRPC requests to a distributed cache in SpiceDB
- Chord algorithm
- MinIO object storage system
