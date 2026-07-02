---
title: "Getting started"
source: https://rocksdb.org/docs/getting-started.html
domain: rocksdb
license: CC-BY-SA-4.0
tags: rocksdb, embedded key-value store, lsm storage, log-structured merge-tree
fetched: 2026-07-02
---

## Overview

The RocksDB library provides a persistent key value store. Keys and values are arbitrary byte arrays. The keys are ordered within the key value store according to a user-specified comparator function.

The library is maintained by the Facebook Database Engineering Team, and is based on LevelDB, by Sanjay Ghemawat and Jeff Dean at Google.

This overview gives some simple examples of how RocksDB is used. For the story of why RocksDB was created in the first place, see Dhruba Borthakur’s introductory talk from the Data @ Scale 2013 conference.

## Opening A Database

A rocksdb database has a name which corresponds to a file system directory. All of the contents of database are stored in this directory. The following example shows how to open a database, creating it if necessary:

```c++
1
2
3
4
5
6
7
8
9
10
#include <assert>
#include "rocksdb/db.h"

rocksdb::DB* db;
rocksdb::Options options;
options.create_if_missing = true;
rocksdb::Status status =
  rocksdb::DB::Open(options, "/tmp/testdb", &db);
assert(status.ok());
...
```

If you want to raise an error if the database already exists, add the following line before the rocksdb::DB::Open call:

```c++
1
options.error_if_exists = true;
```

## Status

You may have noticed the `rocksdb::Status` type above. Values of this type are returned by most functions in RocksDB that may encounter an error. You can check if such a result is ok, and also print an associated error message:

```c++
1
2
rocksdb::Status s = ...;
if (!s.ok()) cerr << s.ToString() << endl;
```

## Closing A Database

When you are done with a database, just delete the database object. For example:

```c++
1
2
3
/* open the db as described above */
/* do something with db */
delete db;
```

## Reads And Writes

The database provides Put, Delete, and Get methods to modify/query the database. For example, the following code moves the value stored under `key1` to `key2`.

```c++
1
2
3
4
std::string value;
rocksdb::Status s = db->Get(rocksdb::ReadOptions(), key1, &value);
if (s.ok()) s = db->Put(rocksdb::WriteOptions(), key2, value);
if (s.ok()) s = db->Delete(rocksdb::WriteOptions(), key1);
```

## Further documentation

These are just simple examples of how RocksDB is used. The full documentation is currently on the GitHub wiki.

Here are some specific details about the RocksDB implementation:

- RocksDB Overview
- Immutable BlockBased Table file format
- Log file format
