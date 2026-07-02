---
title: "2.1. Introduction to Replication"
source: https://docs.couchdb.org/en/stable/replication/intro.html
domain: couchdb
license: CC-BY-SA-4.0
tags: couchdb, apache couchdb, document-oriented database, eventual consistency
fetched: 2026-07-02
---

# 2.1. Introduction to Replication

One of CouchDB’s strengths is the ability to synchronize two copies of the same database. This enables users to distribute data across several nodes or data centers, but also to move data more closely to clients.

Replication involves a source and a destination database, which can be on the same or on different CouchDB instances. The aim of replication is that at the end of the process, all active documents in the source database are also in the destination database and all documents that were deleted in the source database are also deleted in the destination database (if they even existed).

## 2.1.1. Transient and Persistent Replication

There are two different ways to set up a replication. The first one that was introduced into CouchDB leads to a replication that could be called *transient*. Transient means that there are no documents backing up the replication. So after a restart of the CouchDB server the replication will disappear. Later, the _replicator database was introduced, which keeps documents containing your replication parameters. Such a replication can be called *persistent*. Transient replications were kept for backward compatibility. Both replications can have different replication states.

## 2.1.2. Triggering, Stopping and Monitoring Replications

A persistent replication is controlled through a document in the _replicator database, where each document describes one replication process (see Replication Settings). For setting up a transient replication the api endpoint /_replicate can be used. A replication is triggered by sending a JSON object either to the `_replicate` endpoint or storing it as a document into the `_replicator` database.

If a replication is currently running its status can be inspected through the active tasks API (see /_active_tasks, Replication Status and /_scheduler/jobs).

For document based-replications, /_scheduler/docs can be used to get a complete state summary. This API is preferred as it will show the state of the replication document before it becomes a replication job.

For transient replications there is no way to query their state when the job is finished.

A replication can be stopped by deleting the document, or by updating it with its `cancel` property set to `true`.

## 2.1.3. Replication Procedure

During replication, CouchDB will compare the source and the destination database to determine which documents differ between the source and the destination database. It does so by following the Changes Feeds on the source and comparing the documents to the destination. Changes are submitted to the destination in batches where they can introduce conflicts. Documents that already exist on the destination in the same revision are not transferred. As the deletion of documents is represented by a new revision, a document deleted on the source will also be deleted on the target.

A replication task will finish once it reaches the end of the changes feed. If its `continuous` property is set to true, it will wait for new changes to appear until the task is canceled. Replication tasks also create checkpoint documents on the destination to ensure that a restarted task can continue from where it stopped, for example after it has crashed.

When a replication task is initiated on the sending node, it is called *push* replication, if it is initiated by the receiving node, it is called *pull* replication.

## 2.1.4. Master - Master replication

One replication task will only transfer changes in one direction. To achieve master-master replication, it is possible to set up two replication tasks in opposite direction. When a change is replicated from database A to B by the first task, the second task from B to A will discover that the new change on B already exists in A and will wait for further changes.

## 2.1.5. Controlling which Documents to Replicate

There are three options for controlling which documents are replicated, and which are skipped:

1. Defining documents as being local.
2. Using Selector Objects.
3. Using Filter Functions.

Local documents are never replicated (see Local (non-replicating) Documents).

Selector Objects can be included in a replication document (see Replication Settings). A selector object contains a query expression that is used to test whether a document should be replicated.

Filter Functions can be used in a replication (see Replication Settings). The replication task evaluates the filter function for each document in the changes feed. The document is only replicated if the filter returns `true`.

Note

Using a selector provides performance benefits when compared with using a Filter Functions. You should use Selector Objects where possible.

Note

When using replication filters that depend on the document’s content, deleted documents may pose a problem, since the document passed to the filter will not contain any of the document’s content. This can be resolved by adding a `_deleted:true` field to the document instead of using the DELETE HTTP method, paired with the use of a validate document update handler to ensure the fields required for replication filters are always present. Take note, though, that the deleted document will still contain all of its data (including attachments)!

## 2.1.6. Migrating Data to Clients

Replication can be especially useful for bringing data closer to clients. PouchDB implements the replication algorithm of CouchDB in JavaScript, making it possible to make data from a CouchDB database available in an offline browser application, and synchronize changes back to CouchDB.
