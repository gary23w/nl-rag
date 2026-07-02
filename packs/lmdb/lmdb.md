---
title: "LMDB"
source: https://www.symas.com/lmdb
domain: lmdb
license: CC-BY-SA-4.0
tags: lmdb, lightning memory-mapped database, memory-mapped file, copy-on-write
fetched: 2026-07-02
---

## Embedded Database LMDB

An ultra-fast, ultra-compact, crash-proof, key-value, embedded data store

## Lightning Memory-Mapped Database

Symas LMDB is an extraordinarily fast, memory-efficient database we developed for the OpenLDAP Project. With memory-mapped files, LMDB has the read performance of a pure in-memory database while retaining the persistence of standard disk-based databases.

Bottom line, with only 32KB of object code, LMDB may seem tiny. But it’s the right 32KB. Compact and efficient are two sides of a coin; that’s part of what makes LMDB so powerful.

## Explore Capabilities

Ordered-map interface

keys are always sorted; range lookups are supported Fully transactional

full ACID semantics with MVCC Reader/writer transactions

readers don’t block writers; writers don’t block readers Fully serialized writers

writes are always deadlock-free Extremely cheap read transactions

can be performed using no mallocs or any other blocking calls Multi-thread and multi-process concurrency supported

environments may be opened by multiple processes on the same host Multiple sub-databases may be created

transactions cover all sub-databases Memory-mapped

allows for zero-copy lookup and iteration Maintenance-free

no external process or background cleanup or compaction required Crash-proof

no logs or crash recovery procedures required No application-level caching

LMDB fully exploits the operating system’s buffer cache 32KB of object code and 6KLOC of C

fits in CPU L1 cache for maximum performance

## Where To Get It

Download LMDB

The source is managed by Symas’s gitlab repo:

## Symas LMDB Support

Symas offers fixed-price, Gold support or Enterprise source level support to those using LMDB in their applications. Please contact Sales by phone or email for additional information.

## Community

Search the discussions on the OpenLDAP mailing lists.

Development occurs in the OpenLDAP Project‘s git repo in the mdb.master branch. A clone of just the LMDB code is also available on Github.

## Symas LMDB Tech Info

Symas LMDB has been written about, talked about, and utilized in a variety of impressive products and publications. We invite you to learn more on this specific “Technical Information” page.

## Porting and Professional Services

Thinking about switching your application to LMDB? Call us. We will be happy to provide developer support or porting services to help you transition your application to LMDB.
