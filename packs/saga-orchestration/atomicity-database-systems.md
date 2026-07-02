---
title: "Atomicity (database systems)"
source: https://en.wikipedia.org/wiki/Atomicity_(database_systems)
domain: saga-orchestration
license: CC-BY-SA-4.0
tags: saga distributed transaction, compensating transaction pattern, distributed transaction coordination, saga choreography orchestration
fetched: 2026-07-02
---

# Atomicity (database systems)

In database systems, **atomicity** (/ˌætəˈmɪsəti/; from Ancient Greek: ἄτομος, romanized: *átomos*, lit. 'undividable') is the property of a database transaction consisting of an *indivisible* and *irreducible* series of database operations such that either *all* occur, or *none* occur. It is one of the ACID transaction properties: Atomicity, Consistency, Isolation, Durability. A guarantee of atomicity prevents partial database updates from occurring, because they can cause greater problems than rejecting the whole series outright. As a consequence, an **atomic transaction** cannot be observed to be in progress by another database client: at one moment in time, it has not yet happened, and at the next it has already occurred in whole (or nothing happened if the transaction was cancelled in progress).

An example of transaction atomicity could be a digital monetary transfer from bank account A to account B. It consists of two operations, debiting the money from account A and crediting it to account B. Performing both of these operations inside of an atomic transaction ensures that the database remains in a consistent state, if either operation fails there will not be any unaccountable credits or debits affecting either account.

The same term is also used in the definition of First normal form in database systems, where it instead refers to the concept that the values for fields may not consist of multiple smaller values to be decomposed, such as a string into which multiple names, numbers, dates, or other types may be packed.

## Orthogonality

Atomicity does not behave completely orthogonally with regard to the other ACID properties of transactions. For example, isolation relies on atomicity to roll back the enclosing transaction in the event of an isolation violation such as a deadlock; consistency also relies on atomicity to roll back the enclosing transaction in the event of a consistency violation by an illegal transaction.

As a result of this, a failure to detect a violation and roll back the enclosing transaction may cause an isolation or consistency failure.

## Implementation

Typically, systems implement Atomicity by providing some mechanism to indicate which transactions have started and which finished; or by keeping a copy of the data before any changes occurred (Read-copy-update). Several filesystems have developed methods for avoiding the need to keep multiple copies of data, using journaling (see journaling file system). Databases usually implement this using some form of logging/journaling to track changes. The system synchronizes the logs (often the metadata) as necessary after changes have successfully taken place. Afterwards, crash recovery ignores incomplete entries. Although implementations vary depending on factors such as concurrency issues, the principle of atomicity – i.e. complete success or complete failure – remain.

Ultimately, any application-level implementation relies on operating-system functionality. At the file-system level, POSIX-compliant systems provide system calls such as `open(2)` and `flock(2)` that allow applications to atomically open or lock a file. At the process level, POSIX Threads provide adequate synchronization primitives.

The hardware level requires atomic operations such as Test-and-set, Fetch-and-add, Compare-and-swap, or Load-Link/Store-Conditional, together with memory barriers. Portable operating systems cannot simply block interrupts to implement synchronization, since hardware that lacks concurrent execution such as hyper-threading or multi-processing is now extremely rare.

In distributed and sharded databases, atomicity is complicated by network latency and the potential for partial failures. While traditional distributed systems often employ locking protocols (like 2PC) to ensure cross-shard atomicity, these can introduce performance bottlenecks. Recent research into distributed ledger consensus suggests alternative models, such as "braided synchronization". This technique, utilized in protocols like Cerberus, intertwines the consensus phases of multiple shards to enforce atomic guarantees without a global ordering of all transactions.
