---
title: "Partition (database)"
source: https://en.wikipedia.org/wiki/Partition_(database)
domain: quicksort-algorithm
license: CC-BY-SA-4.0
tags: quicksort algorithm, divide and conquer, partition scheme, quickselect algorithm
fetched: 2026-07-02
---

# Partition (database)

A **partition** is a division of a logical database or its constituent elements into distinct independent parts. Database partitioning refers to intentionally breaking a large database into smaller ones for scalability purposes, distinct from network partitions which are a type of network fault between nodes. In a partitioned database, each piece of data belongs to exactly one partition, effectively making each partition a small database of its own. Database partitioning is normally done for manageability, performance or availability reasons, or for load balancing. It is popular in distributed database management systems, where each partition may be spread over multiple nodes, with users at the node performing local transactions on the partition. This increases performance for sites that have regular transactions involving certain views of data, whilst maintaining availability and security.

Partitioning enables distribution of datasets across multiple disks and query loads across multiple processors. For queries that operate on a single partition, each node executes queries independently on its local partition, enabling linear scaling of query throughput with additional nodes. More complex queries can be parallelized across multiple nodes, though this presents additional challenges.

## History

Database partitioning emerged in the 1980s with systems like Teradata and NonStop SQL. The approach was later adopted by NoSQL databases and Hadoop-based data warehouses. While implementations vary between transactional and analytical workloads, the core principles of partitioning remain consistent across both use cases.

## Terminology

Different DBMSs use varying terminology for partitioning:

- **Shard** in MongoDB, Elasticsearch, and SolrCloud
- **Region** in HBase
- **Tablet** in Bigtable
- **vnode** in Cassandra and Riak
- **vBucket** in Couchbase

## Partitioning and Replication

Partitioning is commonly implemented alongside replication, storing partition copies across multiple nodes. Each record belongs to one partition but may exist on multiple nodes for fault tolerance. In leader-follower replication systems, nodes can simultaneously serve as leaders for some partitions and followers for others.

## Load Balancing and Hot Spots

Partitioning aims to distribute data and query load evenly across nodes. With ideal distribution, system capacity scales linearly with added nodes—ten nodes should process ten times the data and throughput of a single node. Uneven distribution, termed *skew*, reduces partitioning efficiency. Partitions with excessive load are called *hot spots*.

Several strategies address hot spots:

- Random record assignment to nodes, at the cost of retrieval complexity
- Key-range partitioning with optimized boundaries
- Hash-based partitioning for even load distribution

## Partitioning criteria

Current high-end relational database management systems provide for different criteria to split the database. They take a *partitioning key* and assign a partition based on certain criteria. Some common criteria include:

- **Range partitioning**: assigns continuous key ranges to partitions, analogous to encyclopedia volumes. Known range boundaries enable direct request routing. Boundaries can be set manually or automatically for balanced distribution. While this enables efficient range scans, certain access patterns create hot spots. For instance, in sensor networks using timestamp keys, writes concentrate in the current time period's partition. Using compound keys—such as prefixing timestamps with sensor identifiers—can distribute this load. An example could be a partition for all rows where the "zipcode" column has a value between 70000 and 79999.
- **List partitioning**: a partition is assigned a list of values. If the partitioning key has one of these values, the partition is chosen. For example, all rows where the column `Country` is either `Iceland`, `Norway`, `Sweden`, `Finland` or `Denmark` could build a partition for the Nordic countries.
- **Composite partitioning**: allows for certain combinations of the above partitioning schemes, by for example first applying a range partitioning and then a hash partitioning. Consistent hashing could be considered a composite of hash and list partitioning where the hash reduces the key space to a size that can be listed.
- **Round-robin partitioning**: the simplest strategy, it ensures uniform data distribution. With `n` partitions, the `i`th tuple in insertion order is assigned to partition `(i mod n)`. This strategy enables the sequential access to a relation to be done in parallel. However, the direct access to individual tuples, based on a predicate, requires accessing the entire relation.
- **Hash partitioning**: applies a hash function to convert skewed data into uniform distributions for even load distribution across partitions. While this effectively prevents hot spots, it sacrifices range query efficiency as adjacent keys scatter across partitions. Common implementations include MD5 in Cassandra and MongoDB. Some systems, like Cassandra, combine approaches using compound primary keys: hashing the first component for partitioning while maintaining sort order for remaining components within partitions.

In any partitioning scheme, data is typically arranged so that each piece of data (record, row, or document) belongs to exactly one partition. While some databases support operations that span multiple partitions, this single-partition association is fundamental to the partitioning concept.

## Partitioning methods

The partitioning can be done by either building separate smaller databases (each with its own tables, indices, and transaction logs), or by splitting selected elements, for example just one table.

### Horizontal partitioning

Horizontal partitioning involves putting different rows into different tables. For example, customers with ZIP codes less than 50000 are stored in CustomersEast, while customers with ZIP codes greater than or equal to 50000 are stored in CustomersWest. The two partition tables are then CustomersEast and CustomersWest, while a view with a union might be created over both of them to provide a complete view of all customers.

### Vertical partitioning

Vertical partitioning involves creating tables with fewer columns and using additional tables to store the remaining columns. Generally, this practice is known as normalization. However, vertical partitioning extends further, and partitions columns even when already normalized. This type of partitioning is also called "row splitting", since rows get split by their columns, and might be performed explicitly or implicitly. Distinct physical machines might be used to realize vertical partitioning: storing infrequently used or very wide columns, taking up a significant amount of memory, on a different machine, for example, is a method of vertical partitioning. A common form of vertical partitioning is to split static data from dynamic data, since the former is faster to access than the latter, particularly for a table where the dynamic data is not used as often as the static. Creating a view across the two newly created tables restores the original table with a performance penalty, but accessing the static data alone will show higher performance. A columnar database can be regarded as a database that has been vertically partitioned until each column is stored in its own table.
