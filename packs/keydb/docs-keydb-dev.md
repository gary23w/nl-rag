---
title: "KeyDB"
source: https://docs.keydb.dev/
domain: keydb
license: CC-BY-SA-4.0
tags: keydb database, multithreaded redis fork, in-memory data store, key-value cache
fetched: 2026-07-02
---

### Download

See download options available for KeyDB including Docker, DEB/RPM packages, different build options, and community provided distribution methods

### github

Go directly to github to see source code, create issues/PRs, or if you like the project give it a star or follow us!

### Features

New to KeyDB? Check out some of the features KeyDB has to offer

### Docs

Docs is a place where you can find instructions, examples, and theory related to using KeyDB

### Blog

Check out our blog where we take an in depth look at different topics, features, and comparisons of KeyDB

### News

A place to see te latest announcements and news related to everything KeyDB.

# KeyDB Speeds Up The User Experience For Any Project

### *Whether you're starting small or serving millions of users, KeyDB enables you to provide a fast and reliable experience to your users*

### High Throughput

KeyDB is meant to handle heavy workloads with a single node benchmarking at over 1 million ops/sec. KeyDB is a multithreaded database and will outperform Redis on a per-node basis.

### Low Latency

By keeping data in-memory, KeyDB can serve up data with submillisecond latencies.

### A Variety of Data Structures

A variety of data structures are supported such as strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, geospatial indexes, and streams

### Multiple Persistence Options

Periodically dump the dataset to disk or by appending each command to a disk-based log. Durability preferences for RDB and AOF persistence are configurable

### Scalable to Any Workload

While a single KeyDB node scales vertically, you can scale horizonally through active-replication, or cluster-mode (sharded dataset) to meet much larger workloads.

### High Availability

High availability setups are simple with active-replica nodes that do not require sentinel nodes for failover. HA setups are also available for sharded cluster-mode configurations with automatic failover

# Open Source Features That Set Us Apart

### *While KeyDB maintains parity with the vanilla Redis feature set, it offers some major open source advancements*

### MVCC Non-Blocking Architecture

With an MVCC implementation at the underlying architecture, KeyDB can query individual snapshots of the database, avoiding otherwise blocking calls such as SCAN and KEYS. Such queries can now be called concurrently at scale without reducing overall performance of existing workloads

### Cross Region Multi-Master Support

Run multiple master nodes replicated asynchronously to eachother with a last write wins methodology. This enables support of a single replicated dataset where all nodes are masters with no need for sentinel monitoring nodes for failover.

### Better EXPIRation

KeyDB offers Subkey EXPIREs which enables expiration of members within a set. EXPIREs now also have near real time active deletion that removes major lags associated with old models of removing expired keys.

### TLS Encryption

KeyDB offers TLS support that can operate at 7x the throughput of Redis + TLS While TLS encryption adds additional CPU overhead, KeyDB’s multithreaded architecture enables more worker threads to prevent any decline in performance.

### ModJS

Create your own commands with KeyDB’s open source javascript module. Built on the powerful V8 JIT engine, ModJS is faster than LUA and supports many node.js modules to offer extensive library support for common tasks

### More in Store...

Exciting features are on their way! **FLASH storage** is scheduled for release in Q3, we are also working on **JSON support, multi-tenant support, and RAFT**. Check out our roadmap for details
