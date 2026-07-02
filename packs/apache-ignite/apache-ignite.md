---
title: "Apache Ignite"
source: https://en.wikipedia.org/wiki/Apache_Ignite
domain: apache-ignite
license: CC-BY-SA-4.0
tags: apache ignite, in-memory data grid, distributed cache, ignite compute grid
fetched: 2026-07-02
---

# Apache Ignite

**Apache Ignite** is a distributed database management system for high-performance computing.

Apache Ignite's database uses RAM as the default storage and processing tier, thus, belonging to the class of in-memory computing platforms. The disk tier is optional but, once enabled, will hold the full data set whereas the memory tier will cache the full or partial data set depending on its capacity.

Data in Ignite is stored in the form of key-value pairs. The database component distributes key-value pairs across the cluster in such a way that every node owns a portion of the overall data set. Data is rebalanced automatically whenever a node is added to or removed from the cluster.

Apache Ignite cluster can be deployed on-premises on commodity hardware, in the cloud (e.g. Microsoft Azure, AWS, Google Compute Engine) or in containerized and provisioning environments such as Kubernetes, Docker, Apache Mesos, VMware.

## History

Apache Ignite was developed by GridGain Systems, Inc. and made open source in 2014. GridGain continues to be the main contributor to the source code, and offers both a commercial version and professional services around Apache Ignite.

Once donated as open source, Ignite was accepted in the Apache Incubator program in October 2014. The Ignite project graduated from the incubator program to become a top-level Apache project on September 18, 2015.

In recent years, Apache Ignite has become one of the top 5 most active projects by some metrics, including user base activity and repository size.

GridGain was founded in 2010 by Nikita Ivanov and Dmitriy Setrakyan in Pleasanton, California. A funding round of $2 to $3 million was disclosed in November, 2011. By 2013 it was located in Foster City, California when it disclosed funding of $10 million.

## Clustering

Apache Ignite clustering component uses a shared nothing architecture. Server nodes are storage and computational units of the cluster that hold both data and indexes and process incoming requests along with computations. Server nodes are also known as data nodes.

Client nodes are connection points from applications and services to the distributed database on a cluster of server nodes. Client nodes are usually embedded in the application code written in Java, C# or C++ that have special libraries developed. On top of its distributed foundation, Apache Ignite supports interfaces including JCache-compliant key-value APIs, ANSI-99 SQL with joins, ACID transactions, as well as MapReduce like computations. Ignite provides ODBC, JDBC and REST drivers as a way to work with the database from other programming languages or tools. The drivers use either client nodes or low-level socket connections internally in order to communicate to the cluster.

## Partitioning and replication

Ignite database organizes data in the form of key-value pairs in distributed "caches" (the cache notion is used for historical reasons because initially, the database supported the memory tier). Generally, each cache represents one entity type such as an employee or organization.

Every cache is split into a fixed set of "partitions" that are evenly distributed among cluster nodes using the rendezvous hashing algorithm. There is always one primary and zero or more backup copies of a partition. The number of copies is configured with a replication factor parameter. If the full replication mode is configured, then every cluster node will store a partition's copy. The partitions are rebalanced automatically if a node is added to or removed from the cluster in order to achieve an even data distribution and spread the workload.

The key-value pairs are kept in the partitions. Apache Ignite maps a pair to a partition by taking the key's value and passing it to a special hash function.

## Memory architecture

The memory architecture in Apache Ignite consists of two storage tiers and is called "durable memory". Internally, it uses paging for memory space management and data reference, similar to the virtual memory of systems like Unix. However, one significant difference between the durable and virtual memory architectures is that the former always keeps the whole data set with indexes on disk (assuming that the disk tier is enabled), while the virtual memory uses the disk when it runs out of RAM, for swapping purposes only.

The first tier of the memory architecture, memory tier, keeps data and indexes in RAM out of Java heap in so-called "off-heap regions". The regions are preallocated and managed by the database on its own which prevents Java heap utilization for storage needs, as a result, helping to avoid long garbage collection pauses. The regions are split into pages of fixed size that store data, indexes, and system metadata.

Apache Ignite is fully operational from the memory tier but it is always possible to use the second tier, disk tier, for the sake of durability. The database comes with its own native persistence and, plus, can use RDBMS, NoSQL or Hadoop databases as its disk tier.

### Native persistence

Apache Ignite native persistence is a distributed and strongly consistent disk store that always holds a superset of data and indexes on disk. The memory tier will only cache as much data as it can depending on its capacity. For example, if there are 1000 entries and the memory tier can fit only 300 of them, then all 1000 will be stored on disk and only 300 will be cached in RAM.

Persistence uses the write-ahead logging (WAL) technique for keeping immediate data modifications on disk. In the background, the store runs the "checkpointing process" which purpose is to copy dirty pages from the memory tier to the partition files. A dirty page is a page that is modified in memory with the modification recorded in WAL but not written to a respective partition file. The checkpointing allows removing outdated WAL segments over the time and reduces cluster restart time replaying only that part of WAL that has not been applied to the partition files.

### Third-party persistence

The native persistence became available starting version 2.1. Before that Apache Ignite supported only third-party databases as its disk tier.

Apache Ignite can be configured as the in-memory tier on top of RDBMS, NoSQL or Hadoop databases speeding up the latter. However, there are some limitations in comparison to the native persistence. For instance, SQL queries will be executed only on the data that is in RAM, thus, requiring to preload all the data set from disk to memory beforehand.

### Swap space

When using pure memory storage, it is possible for the data size to exceed the physical RAM size, leading to Out-Of-Memory Errors (OOMEs). To avoid this, the ideal approach would be to enable Ignite native persistence or use third-party persistence. However, if you do not want to use native or third-party persistence, you can enable swapping, in which case, Ignite in-memory data will be moved to the swap space located on disk. Note that Ignite does not provide its own implementation of swap space. Instead, it takes advantage of the swapping functionality provided by the operating system (OS). When swap space is enabled, Ignites stores data in memory mapped files (MMF) whose content will be swapped to disk by the OS depending on the current RAM consumption

## Consistency

Apache Ignite is a strongly consistent platform that implements two-phase commit protocol. The consistency guarantees are met for both memory and disk tiers. Transactions in Apache Ignite are ACID-compliant and can span multiple cluster nodes and caches. The database supports pessimistic and optimistic concurrency modes, deadlock-free transactions and deadlock detection techniques.

In the scenarios where transactional guarantees are optional, Apache Ignite allows executing queries in the atomic mode that provides better performance.

## Distributed SQL

Apache Ignite can be accessed using SQL APIs exposed via JDBC and ODBC drivers, and native libraries developed for Java, C#, C++ programming languages. Both data manipulation and data definition languages' syntax complies with ANSI-99 specification.

Being a distributed database, Apache Ignite supports both distributed collocated and non-collocated joins. When the data is collocated, joins are executed on the local data of cluster nodes avoiding data movement across the network. Non-collocated joins might move the data sets around the network in order to prepare a consistent result set.

## Machine Learning

Apache Ignite provides machine learning training and inference functionality as well as data preprocessing and model quality estimation. It natively supports classical training algorithms such as Linear Regression, Decision Trees, Random Forest, Gradient Boosting, SVM, K-Means and others. In addition to that, Apache Ignite has a deep integration with TensorFlow. This integrations allows to train neural networks on a data stored in Apache Ignite in a single-node or distributed manner.

The key idea of Apache Ignite Machine Learning toolkit is an ability to perform distributed training and inference instantly without massive data transmissions. It's based on MapReduce approach, resilient to node failures and data rebalances, allows to avoid data transfers and so that speed up preprocessing and model training.
