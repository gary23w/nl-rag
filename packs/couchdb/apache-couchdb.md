---
title: "Apache CouchDB"
source: https://en.wikipedia.org/wiki/Apache_CouchDB
domain: couchdb
license: CC-BY-SA-4.0
tags: couchdb, apache couchdb, document-oriented database, eventual consistency
fetched: 2026-07-02
---

# Apache CouchDB

**Apache CouchDB** is an open-source document-oriented NoSQL database, implemented in Erlang.

CouchDB uses multiple formats and protocols to store, transfer, and process its data. It uses JSON to store data, JavaScript as its query language using MapReduce, and HTTP for an API.

CouchDB was first released in 2005 and later became an Apache Software Foundation project in 2008.

Unlike a relational database, a CouchDB database does not store data and relationships in tables. Instead, each database is a collection of independent documents. Each document maintains its own data and self-contained schema. An application may access multiple databases, such as one stored on a user's mobile phone and another on a server. Document metadata contains revision information, making it possible to merge any differences that may have occurred while the databases were disconnected.

CouchDB implements a form of multiversion concurrency control (MVCC) so it does not lock the database file during writes. Conflicts are left to the application to resolve. Resolving a conflict generally involves first merging data into one of the documents, then deleting the stale one.

Other features include document-level ACID semantics with eventual consistency, (incremental) MapReduce, and (incremental) replication. One of CouchDB's distinguishing features is multi-master replication, which allows it to scale across machines to build high-performance systems. A built-in Web application called Fauxton (formerly Futon) helps with administration.

## History

*Couch* is an acronym for *cluster of unreliable commodity hardware*. The CouchDB project was created in April 2005 by Damien Katz, a former Lotus Notes developer at IBM. He self-funded the project for almost two years and released it as an open-source project under the GNU General Public License.

In February 2008, it became an Apache Incubator project and was offered under the Apache License instead. A few months after, it graduated to a top-level project. This led to the first stable version being released in July 2010.

In early 2012, Katz left the project to focus on Couchbase Server.

Since Katz's departure, the Apache CouchDB project has continued, releasing 1.2 in April 2012 and 1.3 in April 2013. In July 2013, the CouchDB community merged the codebase for BigCouch, Cloudant's clustered version of CouchDB, into the Apache project. The BigCouch clustering framework is included in the current release of Apache CouchDB.

Native clustering is supported at version 2.0.0. And the new Mango Query Server provides a simple JSON-based way to perform CouchDB queries without JavaScript or MapReduce. Also in version 2.0.0 was the introduction of Fauxton, the new built-in web interface, to replace Futon, the old built-in web interface.

## Main features

**ACID Semantics**

CouchDB provides

ACID

semantics.

It does this by implementing a form of

Multi-Version Concurrency Control

, meaning that CouchDB can handle a high volume of concurrent readers and writers without conflict.

**Built for Offline**

CouchDB can replicate to devices (like smartphones) that can go offline and handle data sync for you when the device is back online.

**Distributed Architecture with Replication**

CouchDB was designed with bi-directional replication (or synchronization) and off-line operation in mind. That means multiple replicas can have their own copies of the same data, modify it, and then sync those changes at a later time.

**Document Storage**

CouchDB stores data as "documents", as one or more field/value pairs expressed as

JSON

. Field values can be simple things like strings, numbers, or dates; but

ordered lists

and

associative arrays

can also be used. Every document in a CouchDB database has a unique id and there is no required document schema.

**Eventual Consistency**

CouchDB guarantees

eventual consistency

to be able to provide both availability and partition tolerance.

**Map/Reduce Views and Indexes**

The stored data is structured using views. In CouchDB, each view is constructed by a

JavaScript

function that acts as the Map half of a

map

/reduce operation. The function takes a document and transforms it into a single value that it returns. CouchDB can index views and keep those indexes updated as documents are added, removed, or updated.

**HTTP API**

All items have a unique URI that gets exposed via HTTP. It uses the

HTTP methods

POST, GET, PUT and DELETE for the four basic

CRUD

(Create, Read, Update, Delete) operations on all resources.

CouchDB also offers a built-in administration interface accessible via Web called Fauxton.

## Use cases and production deployments

Replication and synchronization capabilities of CouchDB make it ideal for using it in mobile devices, where network connection is not guaranteed, and the application must keep on working offline.

CouchDB is well suited for applications with accumulating, occasionally changing data, on which pre-defined queries are to be run and where versioning is important (CRM, CMS systems, by example). Master-master replication is an especially interesting feature, allowing easy multi-site deployments.

### Users

Users of CouchDB include:

- CERN uses CouchDB as database for the Data Management System at the Large Hadron Collider.
- Red Cross use the application iDAT for completing casework electronically in disaster areas. Here CouchDB is used as multi-node peer-to-peer offline-first database.
- IBM Cloud services are based at a fundamental level on CouchDB.
- United Airlines uses CouchDB for the in-flight entertainment systems in over 3,000 planes.
- Amadeus IT Group, for some of their back-end systems.
- Credit Suisse, for internal use at commodities department for their marketplace framework.
- Meebo, for their social platform (Web and applications). Meebo was acquired by Google and most products were shut down on July 12, 2012.
- npm uses CouchDB as replicating database for their package registry.
- Sophos, for some of their back-end systems.
- BBC, for a dynamic CMS-Platform.
- Canonical began using it in 2009 for its synchronization service "Ubuntu One", but stopped using it in November 2011.
- CANAL+ for international on-demand platform at CANAL+ Overseas.
- Protogrid, as storage back-end for their rapid application development framework

## Data manipulation: documents and views

CouchDB manages a collection of JSON documents. The documents are organised via views. Views are defined with aggregate functions and filters are computed in parallel, much like MapReduce.

Views are generally stored in the database and their indexes are updated continuously. CouchDB supports a view system using external socket servers and a JSON-based protocol. As a consequence, view servers have been developed in a variety of languages (JavaScript is the default, but there are also PHP, Ruby, Python and Erlang).

### Accessing data via HTTP

Applications interact with CouchDB via HTTP. The following demonstrates a few examples using cURL, a command-line utility. These examples assume that CouchDB is running on localhost (127.0.0.1) on port 5984.

| Action | Request | Response |
|---|---|---|
| Accessing server information | curl http://127.0.0.1:5984/ | { "couchdb": "Welcome", "version":"1.1.0" } |
| Creating a database named **wiki** | curl -X PUT http://127.0.0.1:5984/wiki | {"ok": true} |
| Attempting to create a second database named **wiki** | curl -X PUT http://127.0.0.1:5984/wiki | { "error":"file_exists", "reason":"The database could not be created, the file already exists." } |
| Retrieve information about the **wiki** database | curl http://127.0.0.1:5984/wiki | { "db_name": "wiki", "doc_count": 0, "doc_del_count": 0, "update_seq": 0, "purge_seq": 0, "compact_running": false, "disk_size": 79, "instance_start_time": "1272453873691070", "disk_format_version": 5 } |
| Delete the database **wiki** | curl -X DELETE http://127.0.0.1:5984/wiki | {"ok": true} |
| Create a document, asking CouchDB to supply a document id | curl -X POST -H "Content-Type: application/json" --data \ '{ "text" : "Wikipedia on CouchDB", "rating": 5 }' \ http://127.0.0.1:5984/wiki | { "ok": true, "id": "123BAC", "rev": "946B7D1C" } |
| get a list of databases | curl http://127.0.0.1:5984/_all_dbs | ["_replicator","_users","wiki"] |

## Open source components

CouchDB includes a number of other open source projects as part of its default package.

| Component | Description | License |
|---|---|---|
| Erlang | Erlang is a general-purpose concurrent programming language and runtime system. The sequential subset of Erlang is a functional language with strict evaluation, single assignment, and dynamic typing | Apache 2.0 (Release 18.0 and later) Erlang Public License (Earlier releases) |
| ICU | International Components for Unicode (ICU) is an open-source project of mature C/C++ and Java libraries for Unicode support, software internationalization and software globalization | Unicode License |
| jQuery | jQuery is a lightweight cross-browser JavaScript library that emphasizes interaction between JavaScript and HTML | MIT License |
| OpenSSL | OpenSSL is an open-source implementation of the SSL and TLS protocols. The core library (written in the C programming language) implements the basic cryptographic functions and provides various utility functions | Apache 1.0 and the four-clause BSD License |
| SpiderMonkey | SpiderMonkey is a performant JavaScript engine maintained by the Mozilla Foundation. It contains an interpreter, a JIT compiler and a garbage collector | MPL 2.0 |
