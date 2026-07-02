---
title: "Lightning Memory-Mapped Database"
source: https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database
domain: lmdb
license: CC-BY-SA-4.0
tags: lmdb, lightning memory-mapped database, memory-mapped file, copy-on-write
fetched: 2026-07-02
---

# Lightning Memory-Mapped Database

**Lightning Memory-Mapped Database** (**LMDB**) is an embedded transactional database in the form of a key-value store. LMDB is written in C with API bindings for several programming languages. LMDB stores arbitrary key/data pairs as byte arrays, has a range-based search capability, supports multiple data items for a single key and has a special mode for appending records (MDB_APPEND) without checking for consistency. LMDB is not a relational database, it is strictly a key-value store like Berkeley DB and DBM.

LMDB may also be used concurrently in a multi-threaded or multi-processing environment, with read performance scaling linearly by design. LMDB databases may have only one writer at a time, however unlike many similar key-value databases, write transactions do *not* block readers, nor do readers block writers. LMDB is also unusual in that multiple applications on the same system may simultaneously open and use the same LMDB store, as a means to scale up performance. Also, LMDB does not require a transaction log (thereby increasing write performance by not needing to write data twice) because it maintains data integrity inherently by design.

## History

LMDB's design was first discussed in a 2009 post to the OpenLDAP developer mailing list, in the context of exploring solutions to the cache management difficulty caused by the project's dependence on Berkeley DB. A specific goal was to replace the multiple layers of configuration and caching inherent to Berkeley DB's design with a single, automatically managed cache under the control of the host operating system.

Development subsequently began, initially as a fork of a similar implementation from the OpenBSD ldapd project. The first publicly available version appeared in the OpenLDAP source repository in June 2011.

The project was known as MDB until November 2012, after which it was renamed in order to avoid conflicts with existing software.

## Technical description

Internally LMDB uses B+ tree data structures. The efficiency of its design and small footprint had the unintended side-effect of providing good write performance as well. LMDB has an API similar to Berkeley DB and dbm. LMDB treats the computer's memory as a single address space, shared across multiple processes or threads using shared memory with copy-on-write semantics (known historically as a single-level store). Most former modern computing architectures had a 32-bit memory address space, imposing a hard limit of 4 GB on the size of any database that directly mapped into a single-level store. However, today's 64-bit processors now mostly implement 48-bit address spaces, giving access to 47-bit addresses or 128 TB of database size, making databases using shared memory useful once again in real-world applications.

Specific noteworthy technical features of LMDB are:

- Its use of B+ tree. With an LMDB instance being in shared memory and the B+ tree block size being set to the OS page size, access to an LMDB store is extremely memory efficient.
- New data is written without overwriting or moving existing data. This guarantees data integrity and reliability without requiring transaction logs or cleanup services.
- The provision of a unique append-write mode (MDB_APPEND) is implemented by allowing the new record to be added directly to the end of the B+ tree. This reduces the number of reads and writes page operations, resulting in greatly-increased performance but requiring the programmer to ensure keys are already in sorted order when storing in the DB.
- Copy-on-write semantics help ensure data integrity as well as providing transactional guarantees and simultaneous access by readers without requiring any locking, even by the current writer. New memory pages required internally during data modifications are allocated through copy-on-write semantics by the underlying OS: the LMDB library itself never actually modifies older data being accessed by readers because it simply cannot do so: any shared-memory updates *automatically* create a completely independent copy of the memory-page being written to.
- As LMDB is memory-mapped, it can return *direct* pointers to memory addresses of keys and values through its API, thereby avoiding unnecessary and expensive copying of memory. This results in greatly-increased performance (especially when the values stored are extremely large), and expands the potential use cases for LMDB.
- LMDB also tracks unused memory pages, using a B+ tree to keep track of pages freed (no longer needed) during transactions. By tracking unused pages, the need for garbage collection (and a garbage collection phase that would consume CPU cycles) is completely avoided. Transactions that need new pages are first given pages from this unused free pages tree; only after these are used up will it expand into formerly unused areas of the underlying memory-mapped file. On a modern filesystem with sparse file support, this helps minimise actual disk usage.

The file format of LMDB is, unlike that of Berkeley DB, architecture-dependent. This means that a conversion must be done before moving a database from a 32-bit machine to a 64-bit machine, or between computers of differing endianness.

### Concurrency

LMDB employs multiversion concurrency control (MVCC) and allows multiple threads within multiple processes to coordinate simultaneous access to a database. Readers scale linearly by design. While write transactions are globally serialized via a mutex, read-only transactions operate in parallel, including in the presence of a write transaction. They are entirely wait free except for the first read-only transaction on a thread. Each thread reading from a database gains ownership of an element in a shared memory array, which it may update to indicate when it is within a transaction. Writers scan the array to determine the oldest database version the transaction must preserve without requiring direct synchronization with active readers.

## Performance

In 2011, Google published software that allowed users to generate micro-benchmarks comparing LevelDB's performance to SQLite and Kyoto Cabinet in different scenarios. In 2012, Symas added support for LMDB and Berkeley DB and made the updated benchmarking software publicly available. The resulting benchmarks showed that LMDB outperformed all other databases in read and batch write operations. SQLite with LMDB excelled in write operations, and particularly so on synchronous/transactional writes.

The benchmarks showed the underlying filesystem as having a big influence on performance. JFS with an external journal performs well, especially compared to other modern systems like Btrfs and ZFS. Zimbra has tested back-mdb vs back-hdb performance in OpenLDAP, with LMDB clearly outperforming the BDB based back-hdb. Many other OpenLDAP users have observed similar benefits.

Since the initial benchmarking work done in 2012, multiple follow-on tests have been conducted with additional database engines for both in-memory and on-disk workloads characterizing the performance across multiple CPUs and record sizes. These tests show that LMDB performance is unmatched on all in-memory workloads and excels in all disk-bound read workloads and disk-bound write workloads using large record sizes. The benchmark driver code was subsequently published on GitHub and further expanded in database coverage.

## Reliability

LMDB was designed to resist data loss in the face of system and application crashes. Its copy-on-write approach never overwrites currently-in-use data. Avoiding overwrites means the structure on disk/storage is always valid, so application or system crashes can never leave the database in a corrupted state. In its default mode, at worst, a crash can lose data from the last not-yet-committed write transaction. Even with all asynchronous modes enabled, it is only an OS catastrophic failure or hardware power-loss event rather than merely an application crash that could potentially result in any data corruption.

Two academic papers from the USENIX OSDI Symposium covered failure modes of DB engines (including LMDB) under a sudden power loss or system crash. The paper from Pillai et al., did not find any failure in LMDB that would occur in the real-world file systems considered; the single failure identified by the study in LMDB only relates to hypothetical file systems. The Mai Zheng et al. paper claims to point out failures in LMDB, but the conclusion depends on whether fsync or fdatasync is utilised. Using fsync ameliorates the problem. The selection of fsync over fdatasync is a compile-time switch that is not the default behavior in current Linux builds of LMDB but is the default on macOS, *BSD, Android, and Windows. Default Linux builds of LMDB are, therefore, the only ones vulnerable to the problem discovered by the zhengmai researchers however, LMDB may simply be rebuilt by Linux users to utilise fsync instead.

When provided with a corrupt database, such as one produced by fuzzing, LMDB may crash. LMDB's author considers the case unlikely to be concerning but has produced a partial fix in a separate branch.

## Open source license

In June 2013, Oracle changed the license of Berkeley DB (a related project) from the Sleepycat license to the Affero General Public License, thus restricting its use in a wide variety of applications. This caused the Debian project to exclude the library from 6.0 onwards. It was also criticized that this license is not friendly to commercial redistributors. The discussion was sparked over whether the same licensing change could happen to LMDB. Author Howard Chu clarified that LMDB is part of the OpenLDAP project, which had its BSD-style license before he joined, and it will stay like it. No copyright is transferred to anybody by checking in, which would make a similar move like Oracle's impossible.

The Berkeley DB license issue has caused major Linux distributions such as Debian to completely phase out their use of Berkeley DB, with a preference for LMDB.

## API and uses

There are wrappers for several programming languages, such as C++, Java, Python, Lua, Rust, Go, Ruby, Objective C, Objective CAML, JavaScript, C#, Perl, PHP, Tcl and Common Lisp. A complete list of wrappers may be found on the main web site.

Howard Chu ported SQLite 3.7.7.1 to use LMDB instead of its original B-tree code, calling the result SQLightning. One cited insert test of 1000 records was 20 times faster (than the original SQLite with its B-Tree implementation). LMDB is available as a backing store for other open source projects including Cyrus SASL, Heimdal Kerberos, and OpenDKIM. It is also available in some other NoSQL projects like MemcacheDB and Mapkeeper. LMDB was used to make the in-memory store Redis persist data on disk. The existing back-end in Redis showed pathological behaviour in rare cases, and a replacement was sought. The baroque API of LMDB was criticized though, forcing a lot of coding to get simple things done. However, its performance and reliability during testing was considerably better than the alternative back-end stores that were tried.

An up-to-date list of applications using LMDB is maintained on the main web site.

## Application support

Many popular free software projects distribute or include support for LMDB, often as the primary or sole storage mechanism.

- The Debian, Ubuntu, Fedora, and OpenSuSE operating systems.
- OpenLDAP for which LMDB was originally developed via back-mdb.
- Postfix via the lmdb_table adapter.
- PowerDNS, a DNS server.
- CFEngine uses LMDB by default since version of 3.6.0.
- Shopify use LMDB in their SkyDB system.
- Knot DNS a high performance DNS server.
- Monero an open source cryptocurrency created in April 2014 that focuses on privacy, decentralisation and scalability.
- Enduro/X middleware uses LMDB for optional XATMI Microservices (SOA) cache. For the first request the actual service is invoked; in the next request client process reads the saved result directly from LMDB.
- Samba Active Directory Domain Controller
- Nano a peer-to-peer, open source cryptocurrency created in 2015 that prioritizes fast and fee-less transactions.
- Meilisearch an open source, lightning-fast, easy-to-use, and hyper-relevant search engine.
- LMDB-IndexedDB is a JavaScript wrapper around IndexedDB to provide support for LMDB in web browsers.

## Technical reviews of LMDB

LMDB makes novel use of well-known computer science techniques such as copy-on-write semantics and B+ trees to provide atomicity and reliability guarantees as well as performance that can be hard to accept, given the library's relative simplicity and that no other similar key-value store database offers the same guarantees or overall performance, even though the authors *explicitly state* in presentations that LMDB is read-optimised not write-optimised. Additionally, as LMDB was primarily developed for use in OpenLDAP, its developers are focused mainly on the development and maintenance of OpenLDAP, not on LMDB per se. The developers limited time spent presenting the first benchmark results was therefore criticized as not stating limitations and for giving a "silver bullet impression" not adequate to address an engineers attitude *(it has to be pointed out that the concerns raised however were later adequately addressed to the reviewer's satisfaction by the key developer behind LMDB.)*

The presentation did spark other database developers to dissect the code in-depth to understand how and why it works. Reviews run from brief to in-depth. Database developer Oren Eini wrote a 12-part series of articles on his analysis of LMDB, beginning July 9, 2013. The conclusion was in the lines of "impressive codebase ... dearly needs some love", mainly because of too long methods and code duplication. This review, conducted by a .NET developer with no former experience of C, concluded on August 22, 2013, with "beyond my issues with the code, the implementation is really quite brilliant. The way LMDB manages to pack so much functionality by not doing things is quite impressive... I learned quite a lot from the project, and it has been frustrating, annoying and fascinating experience".

Multiple other reviews cover LMDB in various languages including Chinese.
