---
title: "Apache ZooKeeper"
source: https://en.wikipedia.org/wiki/Apache_ZooKeeper
domain: apache-mesos
license: CC-BY-SA-4.0
tags: apache mesos, cluster manager, resource scheduling, datacenter orchestration
fetched: 2026-07-02
---

# Apache ZooKeeper

**Apache ZooKeeper** is an open-source server for highly reliable distributed coordination of cloud applications. It is a project of the Apache Software Foundation.

ZooKeeper is essentially a service for distributed systems offering a hierarchical key-value store, which is used to provide a distributed configuration service, synchronization service, and naming registry for large distributed systems (see *Use cases*). ZooKeeper was a sub-project of Hadoop but is now a top-level Apache project in its own right.

## Overview

ZooKeeper's architecture supports high availability through redundant services. Clients can ask another ZooKeeper leader if the first fails to answer. ZooKeeper nodes store their data in a hierarchical name space, like a file system or a tree data structure. Clients can read from and write to the nodes and in this way have a shared configuration service. ZooKeeper can be viewed as an atomic broadcast system, through which updates are totally ordered. The ZooKeeper Atomic Broadcast (ZAB) protocol is the core of the system.

ZooKeeper is used by companies including Yelp, Rackspace, Yahoo, Odnoklassniki, Reddit, NetApp SolidFire, Meta, Twitter and eBay as well as open source enterprise search systems like Solr and distributed database systems like Apache Pinot.

ZooKeeper is modeled after Google's Chubby lock service and was originally developed at Yahoo! for streamlining the processes running on big-data clusters by storing the status in local log files on the ZooKeeper servers. These servers communicate with client machines to deliver the required information. ZooKeeper was developed to address issues that emerged during the deployment of distributed big-data applications.

Some of the prime features of Apache ZooKeeper are:

- Reliable System: the system keeps working even if some nodes stop working.
- Simple Architecture: there is a shared hierarchical namespace which helps coordinating the processes.
- Fast Processing: especially fast in "read-dominant" workloads (i.e. workloads in which reads are much more common than writes).
- Scalable: performance can be improved by adding nodes.

## Architecture

Some common terminologies regarding the ZooKeeper architecture:

- Node: the systems installed on the cluster
- ZNode: the nodes where the status is updated by other nodes in cluster
- Client applications: the tools that interact with the distributed applications
- Server applications: allow the client applications to interact using a common interface

The services in the cluster are replicated and stored on a set of servers (called an "ensemble"), each of which maintains an in-memory database containing the entire data tree of state as well as a transaction log and snapshots stored persistently. Multiple client applications can connect to a server, and each client maintains a TCP connection through which it sends requests and heartbeats and receives responses and watch events for monitoring.

## Use cases

Typical use cases for ZooKeeper are:

- Naming service
- Configuration management
- Data Synchronization
- Leader election
- Message queue
- Notification system

## Client libraries

In addition to the client libraries included with the ZooKeeper distribution, several third-party libraries, including Apache Curator and Kazoo, extend ZooKeeper's capabilities. These libraries offer enhanced ease of use, additional features and support for a broader range of programming languages.

## Apache projects using ZooKeeper

- Apache Hadoop
- Apache Accumulo
- Apache HBase
- Apache Hive
- Apache Kafka (up to version 4.0.0)
- Apache Drill
- Apache Solr
- Apache Spark
- Apache NiFi
- Apache Druid
- Apache Helix
- Apache Pinot
- Apache Bookkeeper
- Apache Pulsar
