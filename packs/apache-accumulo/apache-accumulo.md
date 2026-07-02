---
title: "Apache Accumulo"
source: https://en.wikipedia.org/wiki/Apache_Accumulo
domain: apache-accumulo
license: CC-BY-SA-4.0
tags: apache accumulo, wide-column store, cell-level security, bigtable clone
fetched: 2026-07-02
---

# Apache Accumulo

**Apache Accumulo** is a highly scalable sorted, distributed key-value store based on Google's Bigtable. It is a system built on top of Apache Hadoop, Apache ZooKeeper, and Apache Thrift. Written in Java, Accumulo has cell-level access labels and server-side programming mechanisms. According to DB-Engines ranking, Accumulo is the third most popular NoSQL wide column store behind Apache Cassandra and HBase and the 67th most popular database engine of any type (complete) as of 2018.

## History

Accumulo was created in 2008 by the US National Security Agency and contributed to the Apache Foundation as an incubator project in September 2011.

On March 21, 2012, Accumulo graduated from incubation at Apache, making it a top-level project.

### Controversy

In June 2012, the US Senate Armed Services Committee (SASC) released the Draft 2012 Department of Defense (DoD) Authorization Bill, which included references to Apache Accumulo. In the draft bill SASC required DoD to evaluate whether Apache Accumulo could achieve commercial viability before implementing it throughout DoD. Specific criteria were not included in the draft language, but the establishment of commercial entities supporting Apache Accumulo could be considered a success factor.

## Main features

### Cell-level security

Apache Accumulo extends the Bigtable data model, adding a new element to the key called Column Visibility. This element stores a logical combination of security labels that must be satisfied at query time in order for the key and value to be returned as part of a user request. This allows data of varying security requirements to be stored in the same table, and allows users to see only those keys and values for which they are authorized.

### Server-side programming

In addition to Cell-Level Security, Apache Accumulo provides a server-side programming mechanism called Iterators that allows users to perform additional processing at the Tablet Server. The range of operations that can be applied is equivalent to those that can be implemented within a MapReduce Combiner function, which produces an aggregate value for several key-value pairs.

### User key ordering

Apache Accumulo orders entries in order of user keys, and exposes an iterator over a key range. This allows locality of reference not available from some other distributed stores (including Cassandra and Voldemort that order by hash of the user key).

## Papers

- 2011 YCSB++: Benchmarking and Performance Debugging Advanced Features in Scalable Table Stores by Carnegie Mellon University and the National Security Agency.
- 2012 Driving Big Data With Big Compute by MIT Lincoln Laboratory.
- 2013 D4M 2.0 Schema:A General Purpose High Performance Schema for the Accumulo Database by MIT Lincoln Laboratory.
- 2013 Spatio-temporal Indexing in Non-relational Distributed Databases by CCRi
