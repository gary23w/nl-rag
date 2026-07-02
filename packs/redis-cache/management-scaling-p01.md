---
title: "Scale with Redis Cluster (part 1/2)"
source: https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/
domain: redis-cache
license: CC-BY-SA-4.0
tags: redis, in-memory data store, key-value cache, in-memory database
fetched: 2026-07-02
part: 1/2
---

# Scale with Redis Cluster

Horizontal scaling with Redis Cluster

| Redis Open Source |
|---|

Redis scales horizontally with a deployment topology called Redis Cluster. This topic will teach you how to set up, test, and operate Redis Cluster in production. You will learn about the availability and consistency characteristics of Redis Cluster from the end user's point of view.

If you plan to run a production Redis Cluster deployment or want to understand better how Redis Cluster works internally, consult the Redis Cluster specification. To learn how Redis Enterprise handles scaling, see Linear Scaling with Redis Enterprise.


## Redis Cluster 101

Redis Cluster provides a way to run a Redis installation where data is automatically sharded across multiple Redis nodes. Redis Cluster also provides some degree of availability during partitions—in practical terms, the ability to continue operations when some nodes fail or are unable to communicate. However, the cluster will become unavailable in the event of larger failures (for example, when the majority of masters are unavailable).

So, with Redis Cluster, you get the ability to:

- Automatically split your dataset among multiple nodes.
- Continue operations when a subset of the nodes are experiencing failures or are unable to communicate with the rest of the cluster.

#### Redis Cluster TCP ports

Every Redis Cluster node requires two open TCP connections: a Redis TCP port used to serve clients, e.g., 6379, and second port known as the *cluster bus port*. By default, the cluster bus port is set by adding 10000 to the data port (e.g., 16379); however, you can override this in the `cluster-port` configuration.

Cluster bus is a node-to-node communication channel that uses a binary protocol, which is more suited to exchanging information between nodes due to little bandwidth and processing time. Nodes use the cluster bus for failure detection, configuration updates, failover authorization, and so forth. Clients should never try to communicate with the cluster bus port, but rather use the Redis command port. However, make sure you open both ports in your firewall, otherwise Redis cluster nodes won't be able to communicate.

For a Redis Cluster to work properly you need, for each node:

1. The client communication port (usually 6379) used to communicate with clients and be open to all the clients that need to reach the cluster, plus all the other cluster nodes that use the client port for key migrations.
2. The cluster bus port must be reachable from all the other cluster nodes.

If you don't open both TCP ports, your cluster will not work as expected.

#### Redis Cluster and Docker

Currently, Redis Cluster does not support NATted environments and in general environments where IP addresses or TCP ports are remapped.

Docker uses a technique called *port mapping*: programs running inside Docker containers may be exposed with a different port compared to the one the program believes to be using. This is useful for running multiple containers using the same ports, at the same time, in the same server.

To make Docker compatible with Redis Cluster, you need to use Docker's *host networking mode*. Please see the `--net=host` option in the Docker documentation for more information.

#### Redis Cluster data sharding

Redis Cluster does not use consistent hashing, but a different form of sharding where every key is conceptually part of what we call a **hash slot**.

There are 16384 hash slots in Redis Cluster, and to compute the hash slot for a given key, we simply take the CRC16 of the key modulo 16384.

Every node in a Redis Cluster is responsible for a subset of the hash slots, so, for example, you may have a cluster with 3 nodes, where:

- Node A contains hash slots from 0 to 5500.
- Node B contains hash slots from 5501 to 11000.
- Node C contains hash slots from 11001 to 16383.

This makes it easy to add and remove cluster nodes. For example, if I want to add a new node D, I need to move some hash slots from nodes A, B, C to D. Similarly, if I want to remove node A from the cluster, I can just move the hash slots served by A to B and C. Once node A is empty, I can remove it from the cluster completely.

Moving hash slots from a node to another does not require stopping any operations; therefore, adding and removing nodes, or changing the percentage of hash slots held by a node, requires no downtime.

Redis Cluster supports multiple key operations as long as all of the keys involved in a single command execution (or whole transaction, or Lua script execution) belong to the same hash slot. The user can force multiple keys to be part of the same hash slot by using a feature called *hash tags*.

Hash tags are documented in the Redis Cluster specification, but the gist is that if there is a substring between {} brackets in a key, only what is inside the string is hashed. For example, the keys `user:{123}:profile` and `user:{123}:account` are guaranteed to be in the same hash slot because they share the same hash tag. As a result, you can operate on these two keys in the same multi-key operation.

#### Redis Cluster master-replica model

To remain available when a subset of master nodes are failing or are not able to communicate with the majority of nodes, Redis Cluster uses a master-replica model where every hash slot has from 1 (the master itself) to N replicas (N-1 additional replica nodes).

In our example cluster with nodes A, B, C, if node B fails the cluster is not able to continue, since we no longer have a way to serve hash slots in the range 5501-11000.

However, when the cluster is created (or at a later time), we add a replica node to every master, so that the final cluster is composed of A, B, C that are master nodes, and A1, B1, C1 that are replica nodes. This way, the system can continue if node B fails.

Node B1 replicates B, and B fails, the cluster will promote node B1 as the new master and will continue to operate correctly.

However, note that if nodes B and B1 fail at the same time, Redis Cluster will not be able to continue to operate.

#### Redis Cluster consistency guarantees

Redis Cluster does not guarantee **strong consistency**. In practical terms this means that under certain conditions it is possible that Redis Cluster will lose writes that were acknowledged by the system to the client.

The first reason why Redis Cluster can lose writes is because it uses asynchronous replication. This means that during writes the following happens:

- Your client writes to the master B.
- The master B replies OK to your client.
- The master B propagates the write to its replicas B1, B2 and B3.

As you can see, B does not wait for an acknowledgement from B1, B2, B3 before replying to the client, since this would be a prohibitive latency penalty for Redis, so if your client writes something, B acknowledges the write, but crashes before being able to send the write to its replicas, one of the replicas (that did not receive the write) can be promoted to master, losing the write forever.

This is very similar to what happens with most databases that are configured to flush data to disk every second, so it is a scenario you are already able to reason about because of past experiences with traditional database systems not involving distributed systems. Similarly you can improve consistency by forcing the database to flush data to disk before replying to the client, but this usually results in prohibitively low performance. That would be the equivalent of synchronous replication in the case of Redis Cluster.

Basically, there is a trade-off to be made between performance and consistency.

Redis Cluster has support for synchronous writes when absolutely needed, implemented via the `WAIT` command. This makes losing writes a lot less likely. However, note that Redis Cluster does not implement strong consistency even when synchronous replication is used: it is always possible, under more complex failure scenarios, that a replica that was not able to receive the write will be elected as master.

There is another notable scenario where Redis Cluster will lose writes, that happens during a network partition where a client is isolated with a minority of instances including at least a master.

Take as an example our 6 nodes cluster composed of A, B, C, A1, B1, C1, with 3 masters and 3 replicas. There is also a client, that we will call Z1.

After a partition occurs, it is possible that in one side of the partition we have A, C, A1, B1, C1, and in the other side we have B and Z1.

Z1 is still able to write to B, which will accept its writes. If the partition heals in a very short time, the cluster will continue normally. However, if the partition lasts enough time for B1 to be promoted to master on the majority side of the partition, the writes that Z1 has sent to B in the meantime will be lost.

Note:

There is a

maximum window

to the amount of writes Z1 will be able to send to B: if enough time has elapsed for the majority side of the partition to elect a replica as master, every master node in the minority side will have stopped accepting writes.

This amount of time is a very important configuration directive of Redis Cluster, and is called the **node timeout**.

After node timeout has elapsed, a master node is considered to be failing, and can be replaced by one of its replicas. Similarly, after node timeout has elapsed without a master node to be able to sense the majority of the other master nodes, it enters an error state and stops accepting writes.


## Redis Cluster configuration parameters

We are about to create an example cluster deployment. Before we continue, let's introduce the configuration parameters that Redis Cluster introduces in the `redis.conf` file.

- **cluster-enabled `<yes/no>`**: If yes, enables Redis Cluster support in a specific Redis instance. Otherwise the instance starts as a standalone instance as usual.
- **cluster-config-file `<filename>`**: Note that despite the name of this option, this is not a user editable configuration file, but the file where a Redis Cluster node automatically persists the cluster configuration (the state, basically) every time there is a change, in order to be able to re-read it at startup. The file lists things like the other nodes in the cluster, their state, persistent variables, and so forth. Often this file is rewritten and flushed on disk as a result of some message reception.
- **cluster-node-timeout `<milliseconds>`**: The maximum amount of time a Redis Cluster node can be unavailable, without it being considered as failing. If a master node is not reachable for more than the specified amount of time, it will be failed over by its replicas. This parameter controls other important things in Redis Cluster. Notably, every node that can't reach the majority of master nodes for the specified amount of time, will stop accepting queries.
- **cluster-slave-validity-factor `<factor>`**: If set to zero, a replica will always consider itself valid, and will therefore always try to failover a master, regardless of the amount of time the link between the master and the replica remained disconnected. If the value is positive, a maximum disconnection time is calculated as the *node timeout* value multiplied by the factor provided with this option, and if the node is a replica, it will not try to start a failover if the master link was disconnected for more than the specified amount of time. For example, if the node timeout is set to 5 seconds and the validity factor is set to 10, a replica disconnected from the master for more than 50 seconds will not try to failover its master. Note that any value different than zero may result in Redis Cluster being unavailable after a master failure if there is no replica that is able to failover it. In that case the cluster will return to being available only when the original master rejoins the cluster.
- **cluster-migration-barrier `<count>`**: Minimum number of replicas a master will remain connected with, for another replica to migrate to a master which is no longer covered by any replica. See the appropriate section about replica migration in this tutorial for more information.
- **cluster-require-full-coverage `<yes/no>`**: If this is set to yes, as it is by default, the cluster stops accepting writes if some percentage of the key space is not covered by any node. If the option is set to no, the cluster will still serve queries even if only requests about a subset of keys can be processed.
- **cluster-allow-reads-when-down `<yes/no>`**: If this is set to no, as it is by default, a node in a Redis Cluster will stop serving all traffic when the cluster is marked as failed, either when a node can't reach a quorum of masters or when full coverage is not met. This prevents reading potentially inconsistent data from a node that is unaware of changes in the cluster. This option can be set to yes to allow reads from a node during the fail state, which is useful for applications that want to prioritize read availability but still want to prevent inconsistent writes. It can also be used for when using Redis Cluster with only one or two shards, as it allows the nodes to continue serving writes when a master fails but automatic failover is impossible.
