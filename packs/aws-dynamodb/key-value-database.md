---
title: "Key–value database"
source: https://en.wikipedia.org/wiki/Key-value_database
domain: aws-dynamodb
license: CC-BY-SA-4.0
tags: aws dynamodb, amazon dynamodb, nosql database, key-value store
fetched: 2026-07-02
---

# Key–value database

(Redirected from

Key-value database

)

A **key-value database**, or **key-value store**, is a data storage paradigm designed for storing, retrieving, and managing associative arrays, a data structure more commonly known today as a *dictionary*. Dictionaries contain a collection of *objects*, or *records*, which in turn have many different *fields* within them. These records are stored and retrieved using a *key* that uniquely identifies the record, and is used to find the data within the database.

Key-value databases differ from the better known relational databases (RDB). RDBs pre-define the data structure in the database as a series of tables containing fields with well-defined data types. Exposing the data types to the database program allows it to apply various optimizations. In contrast, key-value systems treat the value as opaque to the database itself, and typically support only simple operations such as storing, retrieving, updating, and deleting a value by its key. This offers considerable flexibility and makes such systems well suited to low-latency, high-throughput workloads dominated by direct key lookups, but less suitable for applications that require complex queries or explicit relationships among records.

A lack of standardization, limited transaction support, and relatively simple query interfaces long restricted many key-value systems to specialized uses, but the rapid move to cloud computing after 2010 helped drive renewed interest in them as part of the broader NoSQL movement. Some graph databases, such as ArangoDB, are also key–value databases internally, adding the concept of relationships (*pointers*) between records as a first-class data type.

## Types and examples

Key–value systems span a wide consistency spectrum, from eventually consistent designs to strongly consistent or serializable ones, and some allow the consistency level to be configured as part of the trade-off against latency and availability. Renewed interest in key–value and other NoSQL systems was driven in part by the demands of big data, distributed, and cloud applications. Their scalability and availability made them attractive for cloud data management, although limited transaction support, low-level query interfaces, and the lack of standardization remained obstacles to wider adoption. Some maintain data in memory (RAM), while others employ solid-state drives or rotating disks.

Some key–value systems add additional structure to their keys. For example, Oracle NoSQL Database organizes records using composite keys with "major" and "minor" components, an arrangement that Oracle compares to a directory-path structure in a file system. More generally, however, key–value stores are defined by their use of unique keys associated with opaque values and by their emphasis on simple key-based operations.

Unix included *dbm* (database manager), a minimal database library written by Ken Thompson for managing associative arrays with a single key and hash-based access. Later implementations and related libraries included sdbm, GNU dbm (gdbm), and Berkeley DB.

A more recent example is RocksDB, a persistent key–value storage engine developed at Facebook and designed for large-scale applications. Other examples include in-memory systems such as Memcached and Redis, and persistent systems such as Berkeley DB, Riak, and Voldemort.
