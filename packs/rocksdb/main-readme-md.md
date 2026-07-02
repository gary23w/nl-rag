---
title: "rocksdb/README.md at main · facebook/rocksdb · GitHub"
source: https://github.com/facebook/rocksdb/blob/main/README.md
domain: rocksdb
license: CC-BY-SA-4.0
tags: rocksdb, embedded key-value store, lsm storage, log-structured merge-tree
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

facebook

/

rocksdb

Public

- Notifications You must be signed in to change notification settings
- Fork 6.9k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

29 lines (20 loc) · 1.65 KB

Outline

## RocksDB: A Persistent Key-Value Store for Flash and RAM Storage

(CircleCI Status)

RocksDB is developed and maintained by Facebook Database Engineering Team. It is built on earlier work on LevelDB by Sanjay Ghemawat (sanjay@google.com) and Jeff Dean (jeff@google.com)

This code is a library that forms the core building block for a fast key-value server, especially suited for storing data on flash drives. It has a Log-Structured-Merge-Database (LSM) design with flexible tradeoffs between Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and Space-Amplification-Factor (SAF). It has multi-threaded compactions, making it especially suitable for storing multiple terabytes of data in a single database.

Start with example usage here: https://github.com/facebook/rocksdb/tree/main/examples

See the github wiki for more explanation.

The public interface is in `include/`. Callers should not include or rely on the details of any other header files in this package. Those internal APIs may be changed without warning.

Questions and discussions are welcome on the RocksDB Developers Public Facebook group and email list on Google Groups.

## License

RocksDB is dual-licensed under both the GPLv2 (found in the COPYING file in the root directory) and Apache 2.0 License (found in the LICENSE.Apache file in the root directory). You may select, at your option, one of the above-listed licenses.
