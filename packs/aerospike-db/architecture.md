---
title: "Architecture overview"
source: https://aerospike.com/docs/database/learn/architecture/
domain: aerospike-db
license: CC-BY-SA-4.0
tags: aerospike database, flash-optimized database, key-value store, real-time database
fetched: 2026-07-02
---

# Architecture overview

> For the complete documentation index see: llms.txt
> 
> All documentation pages available in markdown.

Aerospike is a massively scalable, millisecond latency, distributed database. The architecture satisfies three key objectives:

- Create a flexible, scalable platform for web-scale distributed applications.
- Provide the robustness and reliability expected from traditional databases (as in ACID) .
- Provide operational efficiency with minimal manual involvement.

The Aerospike architecture includes the following three layers:

- The cluster-aware client layer, provided by open source client libraries, implements developer APIs, tracks the cluster state, and knows where data resides in the cluster.
- The clustering and data distribution layer manages inter-node communication (network fabric) and automates fail-over, replication, rack awareness, intelligent rebalancing, data migration, and cross-datacenter replication (XDR).
- The data storage layer stores data reliably in flash SSDs, DRAM (*memory*), or Intel® Optane™ Persistent Memory (PMem) for fast retrieval.

Figure 1: Aerospike architecture

The Aerospike clients are implemented as an open source linkable library available in C, Java, Go, C#, Python, Node.js . To see the complete list, go to clients download.

The Client layer:

- Implements the developer API, the client-server protocol, and talks directly to the cluster.
- Tracks the cluster state and knows where each record is stored, instantly learning of changes to cluster configuration or when cluster nodes go down or join.
- Implements its own TCP/IP connection pool for efficiency. Also detects command failures that have not risen to the level of node failures in the cluster and re-routes those commands to cluster nodes with copies of the data.
- Sends requests directly to the node with the record and retries or reroutes requests as needed, for example during cluster size changes.

Aerospike’s architecture reduces transaction latency, offloads request routing from the cluster, and eliminates the developer’s need to write configuration, data sharding and caching code into their applications. It ensures that applications do not have to be restarted or modified when nodes are brought down or added to the cluster. You do not have to waste time with cluster setup, cluster management, or running proxies.

For more information, see Client architecture.

The Aerospike “shared nothing” architecture is designed to scale linearly while reliably storing terabytes and petabytes of data.

The Distribution layer is designed to eliminate manual operations with the systematic automation of all cluster management functions. It includes three modules:

- Cluster Management Module: Tracks nodes in the cluster. The key algorithm is a Paxos-based gossip-voting process that determines which nodes are considered part of the cluster. Aerospike implements a special active and passive heartbeat to monitor inter-node connectivity.
- Data Migration Module: When you add or remove nodes, Aerospike Database cluster membership is ascertained. Each node uses a distributed hash algorithm to divide the primary index space into data *partitions* and assign owners. The Aerospike Data Migration module intelligently balances data distribution across all nodes in the cluster, ensuring that each bit of data replicates across all cluster nodes and datacenters. This operation is specified in the system replication factor configuration.

- Transaction Processing Module: Reads and writes data on request, and provides the consistency and isolation guarantees. This module is responsible for (Cluster architecture)
  - Sync/Async Replication: For writes with immediate consistency, it propagates changes to all replicas before committing the data and returning the result to the client.
  - Proxy: In rare cases during cluster re-configurations when the Client Layer may be briefly out of date, the Transaction Processing module transparently proxies the request to another node.
  - Resolution of Duplicate Data: For clusters recovering from being partitioned (including when restarting nodes), this module resolves any conflicts between different copies of data. The resolution can be based on either the generation count (version) or the last update time.

Figure 2: Cluster architecture

Once the first is cluster up, you can install additional clusters in other datacenters and setup cross-datacenter replication to ensure that if a datacenter goes down, the remote cluster takes over the workload with minimal or no interruption to users.

For more information, see Clustering and Data distribution.

Aerospike is a multi-model (key-value, document, graph) data store with a schemaless data model. Data flows into policy containers, *namespaces*, which are semantically similar to *databases* in an RDBMS. Within a namespace, data is subdivided into *sets* (RDBMS *tables*) and *records* (RDBMS *rows*). Each record has an indexed *key* unique in the set, and one or more named *bins* (RDBMS *columns*) that hold values associated with the record.

Indexes, including the primary index and optional secondary indexes, are stored by default in DRAM for ultra-fast access. The primary index can also be configured to be stored in Persistent Memory or on an NVMe flash device. Values can be stored either in DRAM or more cost-effectively on SSDs. You can configure each namespace separately, so small namespaces can take advantage of DRAM and larger ones gain the cost benefits of SSDs.

In Aerospike:

- 1 billion keys only take up 64GiB across the cluster. Although keys have no size limitations, each key is efficiently stored in just 64 bytes.
- Native, multi-threaded, multi-core Flash I/O and an Aerospike log structured file system take advantage of low-level SSD read and write patterns. To minimize latency, writes to disk are performed in large blocks. This mechanism bypasses the standard file system, historically tuned to rotational disks.
- The defragmenter and the evictor work together to ensure that there is space in DRAM, that data is never lost, and that data is always written to disk safely.
  - Defragmenter: Tracks the number of active records in each block and reclaims blocks that fall below a minimum level of use.
  - Evictor: Removes expired records and reclaims memory if the system gets beyond a set high-water mark. Expiration times are configured per namespace. Record age is calculated from the last modification. The application can override the default lifetime and specify that a record should never be evicted.

For more information, see Flexible storage.

In a conventional, non-distributed RDBMS, after installation you set up your database schema and create databases and table definitions. The Aerospike Database is different.

In distributed databases, data is distributed between all servers in the cluster. That means you cannot simply log onto a server to access all of your data.

With Aerospike, you create and manage the database:

- By configuring the initial database settings. The Aerospike database is the *namespace*. When you install Aerospike, each node in the cluster must have each namespace configured to specify how to create and replicate the database. The database is created as soon as you restart your server.
- By performing database operations through your application.
  - The database schema is created when your application first references the *sets* and *bins* (tables and fields).
  - The Aerospike Database is a flex-schema—you don’t have to predefine your database schema. For example, to add a new bin (field), your application simply starts storing data in a specified bin. In the Aerospike Database, tasks that might normally be done by a DBA on a command line are done in your application.
- By updating the configuration files as necessary.
  - To change namespace parameters, simply update the configuration file, either dynamically without a restart or by restarting the server with a new configuration file.

To provide quality performance and redundancy, plan and configure how many nodes are required. For more information, see Capacity planning guide.

If you add a node to the cluster or take down a node for upgrading or servicing, the cluster automatically reconfigures. When a node fails, other nodes in the cluster rebalance the workload with minimal impact. For a list of available monitoring utilities, see Monitoring.

With a namespace defined, you can use the Aerospike tools to verify that the database is storing data correctly. In production databases, data is distributed over the cluster. To perform database operations, use the client that instantiates your application. The client is location-aware and knows how to store and retrieve data without affecting performance.

On application compilation, the Aerospike API libraries are included along with the client. The client is a separate thread/process that monitors cluster state to determine data location, which ensures that data is retrieved in a single hop and allows your application to ignore the data distribution details.
