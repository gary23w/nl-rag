---
title: "Riak"
source: https://en.wikipedia.org/wiki/Riak
domain: riak
license: CC-BY-SA-4.0
tags: riak, distributed key-value store, eventual consistency, consistent hashing
fetched: 2026-07-02
---

# Riak

**Riak** (pronounced "ree-ack" ) is a distributed NoSQL key-value data store that offers high availability, fault tolerance, operational simplicity, and scalability. Riak moved to an entirely open-source project in August 2017, with many of the licensed Enterprise Edition features being incorporated. Riak implements the principles from Amazon's Dynamo paper with heavy influence from the CAP theorem. Written in Erlang, Riak has fault-tolerant data replication and automatic data distribution across the cluster for performance and resilience.

Riak has a pluggable backend for its core storage, with the default storage backend being Bitcask. LevelDB is also supported, with other options (such as the pure-Erlang Leveled) available depending on the version.

Riak was originally developed by engineers employed by Basho Technologies and maintained by them until 2017 when the rights were sold to bet365 after Basho went into receivership.

## Main features

**Fault-tolerant availability**

Riak replicates key/value stores across a cluster of nodes with a default n_val of three. In the case of node outages due to

network partition

or hardware failures, data can still be written to a neighboring node beyond the initial three, and read-back due to its "masterless" peer-to-peer architecture.

**Queries**

Riak provides a

REST-ful

API

through HTTP and

Protocol Buffers

for basic PUT, GET, POST, and DELETE functions. More complex queries are also possible, including secondary indexes, search (via

Apache Solr

), and

MapReduce

. MapReduce has native support for both

JavaScript

(using the

SpiderMonkey

runtime) and Erlang.

**Predictable latency**

Riak distributes data across nodes with hashing and can provide latency profile, even in the case of multiple node failures.

**Storage options**

Keys/values can be stored in memory, disk, or both.

**Multi-datacenter replication**

Multi-Datacenter replication (MDC) provides uni-directional and bi-direction replication of data between Riak clusters, whether locally for resilience or globally for faster regional access. Uni-directional replication is useful for read-only sinks such as backups and Disaster Recovery sites. Bi-directional replication allows for multiple Riak cluster to have eventually consistent data across vast distances. Complex replication scenarios such as chains, hub-and-spoke and mesh networks are possible due to the Cascades feature, which allows replication of data between clusters that are not directly connected. There are two primary modes of operation: fullsync and realtime. Fullsync mode ensures that all data on the source cluster is replicated to the sink cluster. Only the metadata and changes are transferred, making this fast and efficient. Realtime mode sends updates made to a source cluster to the sink cluster in realtime. These modes are designed to work together for best performance All multi-datacenter replication occurs over multiple concurrent TCP connections to maximize performance and network utilization.

**Tunable consistency**

Option to choose between eventual and strong consistency for each bucket.

## Main products

All versions of Riak are now entirely open-source and free, and include the extra features that Basho charged license fees for.

Basho operated a freemium model, wherein they provided free versions of Riak in the form of Riak Core, Riak KV, Riak CS and Riak TS but made their money from licensing more advanced features and SLA-based support. The extra features from the Enterprise Editions have since been integrated into the open source version of Riak KV, as of Riak KV release 2.2.6. and Riak CS 2.1.2

### Riak Core and Riak Core Lite

#### Riak Core

riak_core is the distributed systems framework that underpins Riak, forming the foundation for all Riak versions. It is being maintained as part of Riak.

#### Riak Core Lite

riak_core_lite is intended for general use as a base for creating distributed systems.

### Riak KV (Key-Value)

Riak KV is a distributed NoSQL database designed to deliver maximum data availability by distributing data across multiple servers, meaning that if one client can reach one server, it should be able to read and write data. KV went through a few names in its lifetime, starting as Riak then Riak DS (for Data Store) and finally Riak KV (for Key-Value).

When Basho Technologies went into receivership in 2017 KV development was picked up by the open source community and has continued into 2021, with 2.2.6 released in 2018 being the first community release of KV. This release integrated some features that were originally restricted to Basho's Enterprise versions of Riak.

Version 2.9.0 was the first major community release by the open source community, releasing in November 2019, with version 3.0.1 following on August 20, 2020. Development has continued since then with the latest release being version 3.0.7.

#### Removed features

The current version of Riak no longer supports some features in the Enterprise edition of Riak, including:

- SNMP/JMX support

#### Separated features in Riak KV 3.0+

The following features of Riak KV 2.x have been removed by default from the Riak build. Specific builds including these features are available.

- Yokozuna

### Riak CS (Cloud Storage)

Originally known as Riak Moss(Riak Multi-tenant Object Storage System - MOSS) but named as Riak CS (Cloud Storage) when released, Riak CS was first publicly released in January 2012.

Riak CS (Cloud Storage) is object storage software built on top of Riak KV, Riak's distributed database. Riak CS is designed to provide simple, highly-available, distributed cloud storage at any scale, and can be used to build cloud architectures or as storage infrastructure for heavy-duty applications and services.

Riak CS also includes an application called Stanchion which is used to manage the serialization of requests. This enables Riak CS to manage globally unique entities like users and bucket names. Serialization in this context means that the entire cluster agrees upon a single value for any globally unique entity at any given time; when that value is changed, the new value must be recognized throughout the entire cluster.

Riak CS was briefly rebranded as Riak S2 to make it more obviously compatible with Amazon S3 but the name did not catch on and it reverted to Riak CS.

In 2021 development for Riak CS was resumed with contributions from TI Tokyo.

### Riak TS (Time Series)

Riak TS is an extension to Riak KV optimized for time series data, in that:

- it supports structured data, with table definition (with a `CREATE TABLE` call) required before data can be written;
- data slices from contiguous regions in its primary index (“quanta”) are stored on the same partition;
- CRUD operations are optimized for speed, at the expense of consistency.

A limited subset of SQL commands was implemented in Riak TS. There is no provision for consistency guarantees between tables (no foreign indexes). In `SELECT` statements, `WHERE` clause is supported but `HAVING` is not. `ORDER BY` was to appear in a version that was never released.

Riak TS existed as a collection of branches (in separate components of Riak KV such as riak_kv, riak_pb, etc.) and not as product with a repository of its own. It was developed by a dedicated team consisting of Gordon Guthrie (leader), Andy Till and Andrei Zavada, with occasional contributions from other developers.

Riak TS was conceived, along with Riak Data Platform project, as an attempt to diversify Basho's product line, an undertaking many insiders regard as misguided and eventually contributing to Basho's demise.

## Licensing and support

Riak was originally licensed using a freemium model: open source versions of Riak KV, Riak CS and Riak TS are available, but end users can pay for additional features and support. However, since Basho entered receivership and bet365 (purchasers of all IP) made all Riak products fully open source, all the premium features are now available in the open source versions. Since Basho's demise, community ad-hoc and paid support options have arisen.

## Language support

Riak has official drivers for Ruby, Java, Erlang and Python. There are also numerous community-supported drivers for other programming languages.

## Community development

After bet365 purchased the Riak IP, the Riak products were made full open source and work to integrate premium features into the open source versions was completed with the 2.2.6 release.

## History

Riak was originally written by Andy Gross and Justin Sheehy at Basho Technologies to power a web Sales Force Automation application by former engineers and executives from Akamai. There was more interest in the datastore technology than the applications built on it, so the company decided to build a business around Riak itself, gaining adoption throughout the Fortune 100 and becoming a foundation to many of the world's fastest-growing Web-based, mobile and social networking applications, as well as cloud service providers. Releases after graduation include

### Riak KV

Riak 1.0 was released September 10, 2011

| Version! | Date Released | Changes |
|---|---|---|
| 1.0 | September 10, 2011 | Inition 1.0 Release |
| 1.1 | February 21, 2012 | Added Riaknostic, enhanced error logging and reporting, improved resiliency for large clusters, and a new graphical operations and monitoring interface called Riak Control. |
| 1.4 | July 10, 2013 | Added counters, secondary indexing improvements, reduced object storage overhead, handoff progress reporting, and enhancements to MDC replication |
| 2.0 | September 2, 2014 | Added new data types including sets, maps, registers, and flags simplifying application development. Strong consistency by bucket, full-text integration with Apache Solr, Security, and reduced replicas for Secondary sites. |
| 2.1 | April 16, 2015 | Added an optimization for many write-heavy workloads – “write once” buckets – buckets whose entries are intended to be written exactly once, and never updated or over-written. |
| 2.2 | November 17, 2016 | added Support for Debian 8 and Ubuntu 16.04, Solr integration improvements. |
| 2.2.6 | May 21, 2018 | The first community release. Added support for Multi-Datacentre Replication which was not part of open-source Riak before, added a grow-only set data type, improved data distribution over nodes and cleaned up production test issues. |
| 2.9.0 | November 20, 2019 | Added early support for TicTac Active Anti-Entropy, support for a new Riak specific backend called Leveled. |
| 2.9.1 | February 17, 2020 | Implements next-gen replication, various changes to tombstones and bucket listing. |
| 2.9.7 | August 16, 2020 | Improved Active Anti-Entropy and improved Riak's overall stability. |
| 2.9.8 | December 7, 2020 | Improved leveled functions |
| 2.9.9 | August 6, 2021 | Leveled stability improvements |
| 3.0.1 | August 20, 2020 | Adds support for OTP 20, 21, 22 but is not backwards compatible with previous OTP versions. |
| 3.0.2 | January 5, 2021 | Implements backend changes from 2.9.8, adds a `range_check` in the Tictac AAE based full-sync replication |
| 3.0.6 | May 8, 2021 | Adds location-awareness to cluster management, along with bug fixes from 3.0.3 and 3.0.4. |
| 3.0.7 | July 21, 2021 | Reverts Riak erlang runtime system in interactive mode, rather than the embedded mode it was changed to previously. |
| 3.0.8 | October 12, 2021 | Support flushing of disk writes, implement read-repair for key ranges to accelerate recovery after known node outage |
| 3.0.9 | November 12, 2021 | Improve latency and expand statistics of secondary-index queries, including information about result counts and overall query time |
| 3.0.10 | March 30, 2022 | Improve memory management in leveled backend, add peer discovery without configuration changes, allow configuration of Erlang VM memory and scheduler settings via `riak.conf` |
| 3.0.11 | October 11, 2022 | Fix a bottleneck in secondary index queries with the leveled backend and > 1000 queries per second |
| 3.0.12 | December 20, 2022 | Improve memory management in the leveled backend, update leveldb snappy compression for wider platform support, introduce the `reip_manual` console command |
| 3.2.0 | January 1, 2023 | Support Erlang/OTP 22, 24, and 25, update to Erlang/OTP's new logging API, update packaging to include support for Alpine Linux and FreeBSD |
| 3.0.13 | February 4, 2023 | Improve reliability of handoffs, add administrative helper functions to `riak_client` |
| 3.0.14 | February 13, 2023 | Fix an issue related to handling back-pressure correctly in the leveled backend, add support for handing off reap requests via the `handoff_deletes` option |
| 3.0.15 | February 15, 2023 | Correct an issue introduced with the `auto_check` feature for TictacAAE full-sync introduced in 3.0.10 |

### Riak CS

Riak CS was made open source on March 20, 2013

| Version! | Date Released | Changes |
|---|---|---|
| 0.0.3 | January 26, 2012 | The first public release of Riak CS. Known as Riak MOSS at the time. |
| 0.1.0 | February 25, 2012 | Bucket-level Access control, user record changes, Stanchion is now required. |
| 1.0.0 | April 2, 2012 | Fixes some process/socket leaks, adds a fix to prevent deadlock conditions, new subsystem for user access & storage usage calculations. |
| 1.0.1 | April 18, 2012 | Fixes a bug that caused requests to hang if a node in the cluster was unavailable |
| 1.1.0 | August 20, 2012 | Updates user creation, configuration options for anonymous users, more user account controls for admins, Garbage collection for deleted objects, improved performance. |
| 1.2.0 | October 23, 2012 | Early support for Multi-datacenter replication, support for riak_test integration, bug fixes. |
| 1.2.1 | January 23, 2016 | Add reduce phase for listing bucket contents to provide backpressure when executing the MapReduce job, Use prereduce during storage calculations, fixed incorrect 404 error when attempting to list contents of nonexistent bucket. |
| 1.2.2 | November 8, 2012 | Full support for MDC replication, fixed process leaks. |
| 1.3.0 | March 20, 2013 | Support for multi-part file uploads, bucket polices for restricted principles/conditions, range header. More administrative command controls, support for FreeBSD, SmartOS and Solaris Packaging. |
| 1.3.1 | April 4, 2013 | Bug fixes |
| 1.4.0 | August 12, 2013 | Early support for Swift API/Keystone Authentication, improved performance, bug fixes. |
| 1.5.0 | July 31, 2014 | Adds a multibag technical preview, new debug command, streamlines commands to new `riak-cs admin` command, improved garbage collection, updated lager, new API - Multiple objects, warning logs for manifests, siblings etc. |
| 1.5.1 | September 10, 2014 | Adds Bucket restrictions, adds sleep interval for manifest updates, updates riak-cs-debug, changes to bucket resolution. |
| 1.5.2 | October 9, 2014 | Improved logging for failures with Riak, Changes to log output for access stats, adds a script for invalid garbage collection manifest repairs. |
| 1.5.3 | December 12, 2014 | Add `read_before_last_manifest_write` option, Adds configurable timeouts for CS interactions with Riak |
| 1.5.4 | March 13, 2015 | Disable backpressure sleep, Fixes an incorrect path rewrite in S3 API |
| 2.0.0 | March 27, 2015 | Updates Riak CS to work with Riak 2.0.5, Changes gc_max_workers to gc.max_workers and changed default setting, early support for AWS v4 authentication, adds cuttlefish, storage optimisations. |
| 2.1.0 | October 14, 2015 | Final Basho release - Backwards compatible with KV 2.0.5, 21.1, Adds a large number of new metrics for health monitoring purposes along with storage usage metrics. Replaced commands with riak-cs-admin equivalents. Garbage collection improvements. |
| 2.1.1 | October 14, 2015 | Compatible with KV 2.1.3, 2.1.4, 2.2.x and 2.9.x |
| 2.1.2 | April 9, 2019 | First post-basho release. |

### Riak TS

Riak TS was originally released in October 2015

| Version! | Date Released | Changes |
|---|---|---|
| 1.2.0 | February 23, 2016 | Implements Riak_shell to allow SWQL commands & logging in a single shell in Riak TS. Bug fixes, Multi-Datacenter replication and riak search not supported. |
| 1.3.0 | May 4, 2016 | Open sources Riak TS, adds a HTTP API, additional SQL commands and support for MDC replication for enterprise users |
| 1.3.1 | July 5, 2016 | Addresses Data loss bug in 1.3.0. |
| 1.4.0 | August 24, 2016 | Adds new SQL features, Rolling upgrade/downgrade support, Global data expiry (per cluster). |
| 1.5.0 | December 20, 2016 | Expands SQL implementation, Improves data storage and improved overall performance. |
| 1.5.1 | January 24, 2017 | Bug fixes from 1.5.0 |
| 1.5.2 | February 21, 2017 | Bug Fixes from 1.5.1 |

## Users

Notable users include AT&T, Comcast, GitHub, Best Buy, UK National Health Services (NHS), The Weather Channel, and Riot Games.
