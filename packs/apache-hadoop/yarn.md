---
title: "Apache Hadoop"
source: https://en.wikipedia.org/wiki/YARN
domain: apache-hadoop
license: CC-BY-SA-4.0
tags: apache hadoop, hadoop distributed file system, map reduce, distributed storage, yarn resource manager
fetched: 2026-07-02
---

# Apache Hadoop

(Redirected from

YARN

)

**Apache Hadoop** (/həˈduːp/) is a collection of open-source software utilities for reliable, scalable, distributed computing. It provides a software framework for distributed storage and processing of big data using the MapReduce programming model. Hadoop was originally designed for computer clusters built from commodity hardware, which is still the common use. It has since also found use on clusters of higher-end hardware. All the modules in Hadoop are designed with a fundamental assumption that hardware failures are common occurrences and should be automatically handled by the framework.

## Overview

The core of Apache Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part which is a MapReduce programming model. Hadoop splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel. This approach takes advantage of data locality, where nodes manipulate the data they have access to. This allows the dataset to be processed faster and more efficiently than it would be in a more conventional supercomputer architecture that relies on a parallel file system where computation and data are distributed via high-speed networking.

The base Apache Hadoop framework is composed of the following modules:

- *Hadoop Common* - contains libraries and utilities needed by other Hadoop modules;
- *Hadoop Distributed File System (HDFS)* - a distributed file-system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster;
- *Hadoop YARN* - (introduced in 2012) is a platform responsible for managing computing resources in clusters and using them for scheduling users' applications;
- *Hadoop MapReduce* - an implementation of the MapReduce programming model for large-scale data processing.
- *Hadoop Ozone* - (introduced in 2020) An object store for Hadoop

The term *Hadoop* is often used for both base modules and sub-modules and also the *ecosystem*, or collection of additional software packages that can be installed on top of or alongside Hadoop, such as Apache Pig, Apache Hive, Apache HBase, Apache Phoenix, Apache Spark, Apache ZooKeeper, Apache Impala, Apache Flume, Apache Sqoop, Apache Oozie, and Apache Storm.

Apache Hadoop's MapReduce and HDFS components were inspired by Google papers on MapReduce and Google File System.

The Hadoop framework itself is mostly written in the Java programming language, with some native code in C and command line utilities written as shell scripts. Perl language can be easily used with Hadoop Streaming to implement the map and reduce parts of the user's program.

## History

According to its co-founders, Doug Cutting and Mike Cafarella, the idea of Hadoop was conceived in the Google File System paper that was published in October 2003. The concept was extended in the Google paper *"MapReduce: Simplified Data Processing on Large Clusters".* Development started on the Apache Nutch project, but was moved to the new Hadoop subproject in January 2006. Doug Cutting, who was working at Yahoo! at the time, named it after his son's toy elephant. The initial code that was factored out of Nutch consisted of about 5,000 lines of code for HDFS and about 6,000 lines of code for MapReduce.

In March 2006, Owen O'Malley was the first committer to add to the Hadoop project; Hadoop 0.1.0 was released in April 2006. It continues to evolve through contributions that are being made to the project. The first design document for the Hadoop Distributed File System was written by Dhruba Borthakur in 2007.

| Version | Original release date | Latest version | Release date |
|---|---|---|---|
| Unsupported: 0.10 |   | 0.10.1 | 2007-01-11 |
| Unsupported: 0.11 |   | 0.11.2 | 2007-02-16 |
| Unsupported: 0.12 | 2007-03-02 | 0.12.3 | 2007-04-06 |
| Unsupported: 0.13 | 2007-06-04 | 0.13.1 | 2007-07-23 |
| Unsupported: 0.14 | 2007-09-04 | 0.14.4 | 2007-11-26 |
| Unsupported: 0.15 | 2007-10-29 | 0.15.3 | 2008-01-18 |
| Unsupported: 0.16 | 2008-02-07 | 0.16.4 | 2008-05-05 |
| Unsupported: 0.17 | 2008-05-20 | 0.17.2 | 2008-08-19 |
| Unsupported: 0.18 | 2008-08-22 | 0.18.3 | 2009-01-29 |
| Unsupported: 0.19 | 2008-11-21 | 0.19.2 | 2009-07-23 |
| Unsupported: 0.20 | 2009-04-22 | 0.20.205.0 | 2011-10-17 |
| Unsupported: 0.21 | 2011-05-11 | 0.21.0 |   |
| Unsupported: 0.22 | 2011-12-10 | 0.22.0 |   |
| Unsupported: 0.23 | 2011-11-11 | 0.23.11 | 2014-06-27 |
| Unsupported: 1.0 | 2011-12-27 | 1.0.4 | 2012-10-12 |
| Unsupported: 1.1 | 2012-10-13 | 1.1.2 | 2013-02-15 |
| Unsupported: 1.2 | 2013-05-13 | 1.2.1 | 2013-08-01 |
| Unsupported: 2.0 | 2012-05-23 | 2.0.6-alpha | 2013-08-23 |
| Unsupported: 2.1 | 2013-08-25 | 2.1.1-beta | 2013-09-23 |
| Unsupported: 2.2 | 2013-12-11 | 2.2.0 |   |
| Unsupported: 2.3 | 2014-02-20 | 2.3.0 |   |
| Unsupported: 2.4 | 2014-04-07 | 2.4.1 | 2014-06-30 |
| Unsupported: 2.5 | 2014-08-11 | 2.5.2 | 2014-11-19 |
| Unsupported: 2.6 | 2014-11-18 | 2.6.5 | 2016-10-08 |
| Unsupported: 2.7 | 2015-04-21 | 2.7.7 | 2018-05-31 |
| Unsupported: 2.8 | 2017-03-22 | 2.8.5 | 2018-09-15 |
| Unsupported: 2.9 | 2017-12-17 | 2.9.2 | 2018-11-19 |
| Supported: 2.10 | 2019-10-29 | 2.10.2 | 2022-05-31 |
| Unsupported: 3.0 | 2017-12-13 | 3.0.3 | 2018-05-31 |
| Unsupported: 3.1 | 2018-04-06 | 3.1.4 | 2020-08-03 |
| Latest version: 3.2 | 2019-01-16 | 3.2.4 | 2022-07-22 |
| Latest version: 3.3 | 2020-07-14 | 3.3.6 | 2023-06-23 |
| Latest version: 3.4 | 2024-03-17 | 3.4.0 | 2024-07-17 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

## Architecture

Hadoop consists of the *Hadoop Common* package, which provides file system and operating system level abstractions, a MapReduce engine (either MapReduce/MR1 or YARN/MR2) and the Hadoop Distributed File System (HDFS). The Hadoop Common package contains the Java Archive (JAR) files and scripts needed to start Hadoop.

For effective scheduling of work, every Hadoop-compatible file system should provide location awareness, which is the name of the rack, specifically the network switch where a worker node is. Hadoop applications can use this information to execute code on the node where the data is, and, failing that, on the same rack/switch to reduce backbone traffic. HDFS uses this method when replicating data for data redundancy across multiple racks. This approach reduces the impact of a rack power outage or switch failure; if any of these hardware failures occurs, the data will remain available.

A small Hadoop cluster includes a single master and multiple worker nodes. The master node consists of a Job Tracker, Task Tracker, NameNode, and DataNode. A slave or *worker node* acts as both a DataNode and TaskTracker, though it is possible to have data-only and compute-only worker nodes. These are normally used only in nonstandard applications.

Hadoop requires the Java Runtime Environment (JRE) 1.6 or higher. The standard startup and shutdown scripts require that Secure Shell (SSH) be set up between nodes in the cluster.

In a larger cluster, HDFS nodes are managed through a dedicated NameNode server to host the file system index, and a secondary NameNode that can generate snapshots of the namenode's memory structures, thereby preventing file-system corruption and loss of data. Similarly, a standalone JobTracker server can manage job scheduling across nodes. When Hadoop MapReduce is used with an alternate file system, the NameNode, secondary NameNode, and DataNode architecture of HDFS are replaced by the file-system-specific equivalents.

### File systems

#### Hadoop distributed file system

The *Hadoop distributed file system* (HDFS) is a distributed, scalable, and portable file system written in Java for the Hadoop framework. A Hadoop instance is divided into HDFS and MapReduce. HDFS is used for storing the data and MapReduce is used for processing data. HDFS has five services:

1. Name Node
2. Secondary Name Node
3. Job Tracker
4. Data Node
5. Task Tracker

Top three are Master Services/Daemons/Nodes and bottom two are Slave Services. Master Services can communicate with each other and in the same way Slave services can communicate with each other. Name Node is a master node and Data node is its corresponding Slave node and can talk with each other.

**Name Node:** HDFS consists of only one Name Node that is called the Master Node. The master node can track files, manage the file system and has the metadata of all of the stored data within it. In particular, the name node contains the details of the number of blocks, locations of the data node that the data is stored in, where the replications are stored, and other details. The name node has direct contact with the client.

**Data Node:** A Data Node stores data in it as blocks. This is also known as the slave node and it stores the actual data into HDFS which is responsible for the client to read and write. These are slave daemons. Every Data node sends a Heartbeat message to the Name node every 3 seconds and conveys that it is alive. In this way when Name Node does not receive a heartbeat from a data node for 2 minutes, it will take that data node as dead and starts the process of block replications on some other Data node.

**Secondary Name Node:** This is only to take care of the checkpoints of the file system metadata which is in the Name Node. This is also known as the checkpoint Node. It is the helper Node for the Name Node. The secondary name node instructs the name node to create & send fsimage & editlog file, upon which the compacted fsimage file is created by the secondary name node.

**Job Tracker:** Job Tracker receives the requests for Map Reduce execution from the client. Job tracker talks to the Name Node to know about the location of the data that will be used in processing. The Name Node responds with the metadata of the required processing data.

**Task Tracker:** It is the Slave Node for the Job Tracker and it will take the task from the Job Tracker. It also receives code from the Job Tracker. Task Tracker will take the code and apply on the file. The process of applying that code on the file is known as Mapper.

Hadoop cluster has nominally a single namenode plus a cluster of datanodes, although redundancy options are available for the namenode due to its criticality. Each datanode serves up blocks of data over the network using a block protocol specific to HDFS. The file system uses TCP/IP sockets for communication. Clients use remote procedure calls (RPC) to communicate with each other.

HDFS stores large files (typically in the range of gigabytes to terabytes) across multiple machines. It achieves reliability by replicating the data across multiple hosts, and hence theoretically does not require redundant array of independent disks (RAID) storage on hosts (but to increase input-output (I/O) performance some RAID configurations are still useful). With the default replication value, 3, data is stored on three nodes: two on the same rack, and one on a different rack. Data nodes can talk to each other to rebalance data, to move copies around, and to keep the replication of data high. HDFS is not fully POSIX-compliant, because the requirements for a POSIX file-system differ from the target goals of a Hadoop application. The trade-off of not having a fully POSIX-compliant file-system is increased performance for data throughput and support for non-POSIX operations such as Append.

In May 2012, high-availability capabilities were added to HDFS, letting the main metadata server called the NameNode manually fail-over onto a backup. The project has also started developing automatic fail-overs.

The HDFS file system includes a so-called *secondary namenode*, a misleading term that some might incorrectly interpret as a backup namenode when the primary namenode goes offline. In fact, the secondary namenode regularly connects with the primary namenode and builds snapshots of the primary namenode's directory information, which the system then saves to local or remote directories. These checkpointed images can be used to restart a failed primary namenode without having to replay the entire journal of file-system actions, then to edit the log to create an up-to-date directory structure. Because the namenode is the single point for storage and management of metadata, it can become a bottleneck for supporting a huge number of files, especially a large number of small files. HDFS Federation, a new addition, aims to tackle this problem to a certain extent by allowing multiple namespaces served by separate namenodes. Moreover, there are some issues in HDFS such as small file issues, scalability problems, Single Point of Failure (SPoF), and bottlenecks in huge metadata requests. One advantage of using HDFS is data awareness between the job tracker and task tracker. The job tracker schedules map or reduce jobs to task trackers with an awareness of the data location. For example: if node A contains data (a, b, c) and node X contains data (x, y, z), the job tracker schedules node A to perform map or reduce tasks on (a, b, c) and node X would be scheduled to perform map or reduce tasks on (x, y, z). This reduces the amount of traffic that goes over the network and prevents unnecessary data transfer. When Hadoop is used with other file systems, this advantage is not always available. This can have a significant impact on job-completion times as demonstrated with data-intensive jobs.

HDFS was designed for mostly immutable files and may not be suitable for systems requiring concurrent write operations.

HDFS can be mounted directly with a Filesystem in Userspace (FUSE) virtual file system on Linux and some other Unix systems.

File access can be achieved through the native Java API, the Thrift API (generates a client in a number of languages e.g. C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, Smalltalk, and OCaml), the command-line interface, the HDFS-UI web application over HTTP, or via 3rd-party network client libraries.

HDFS is designed for portability across various hardware platforms and for compatibility with a variety of underlying operating systems. The HDFS design introduces portability limitations that result in some performance bottlenecks, since the Java implementation cannot use features that are exclusive to the platform on which HDFS is running. Due to its widespread integration into enterprise-level infrastructure, monitoring HDFS performance at scale has become an increasingly important issue. Monitoring end-to-end performance requires tracking metrics from datanodes, namenodes, and the underlying operating system. There are currently several monitoring platforms to track HDFS performance, including Hortonworks, Cloudera, and Datadog.

#### Other file systems

Hadoop works directly with any distributed file system that can be mounted by the underlying operating system by simply using a `file://` URL; however, this comes at a price – the loss of locality. To reduce network traffic, Hadoop needs to know which servers are closest to the data, information that Hadoop-specific file system bridges can provide.

In May 2011, the list of supported file systems bundled with Apache Hadoop were:

- HDFS: Hadoop's own rack-aware file system. This is designed to scale to tens of petabytes of storage and runs on top of the file systems of the underlying operating systems.
- Apache Hadoop Ozone: HDFS-compatible object store targeting optimized for billions of small files.
- FTP file system: This stores all its data on remotely accessible FTP servers.
- Amazon S3 (Amazon Simple Storage Service) object storage: This is targeted at clusters hosted on the Amazon Elastic Compute Cloud server-on-demand infrastructure. There is no rack-awareness in this file system, as it is all remote.
- Windows Azure Storage Blobs (WASB) file system: This is an extension of HDFS that allows distributions of Hadoop to access data in Azure blob stores without moving the data permanently into the cluster.

A number of third-party file system bridges have also been written, none of which are currently in Hadoop distributions. However, some commercial distributions of Hadoop ship with an alternative file system as the default – specifically IBM and MapR.

- In 2009, IBM discussed running Hadoop over the IBM General Parallel File System. The source code was published in October 2009.
- In April 2010, Parascale published the source code to run Hadoop against the Parascale file system.
- In April 2010, Appistry released a Hadoop file system driver for use with its own CloudIQ Storage product.
- In June 2010, HP discussed a location-aware IBRIX Fusion file system driver.
- In May 2011, MapR Technologies Inc. announced the availability of an alternative file system for Hadoop, MapR FS, which replaced the HDFS file system with a full random-access read/write file system.

### JobTracker and TaskTracker: the MapReduce engine

Atop the file systems comes the MapReduce Engine, which consists of one *JobTracker*, to which client applications submit MapReduce jobs. The JobTracker pushes work to available *TaskTracker* nodes in the cluster, striving to keep the work as close to the data as possible. With a rack-aware file system, the JobTracker knows which node contains the data, and which other machines are nearby. If the work cannot be hosted on the actual node where the data resides, priority is given to nodes in the same rack. This reduces network traffic on the main backbone network. If a TaskTracker fails or times out, that part of the job is rescheduled. The TaskTracker on each node spawns a separate Java virtual machine (JVM) process to prevent the TaskTracker itself from failing if the running job crashes its JVM. A heartbeat is sent from the TaskTracker to the JobTracker every few minutes to check its status. The Job Tracker and TaskTracker status and information is exposed by Jetty and can be viewed from a web browser.

Known limitations of this approach are:

1. The allocation of work to TaskTrackers is very simple. Every TaskTracker has a number of available *slots* (such as "4 slots"). Every active map or reduce task takes up one slot. The Job Tracker allocates work to the tracker nearest to the data with an available slot. There is no consideration of the current system load of the allocated machine, and hence its actual availability.
2. If one TaskTracker is very slow, it can delay the entire MapReduce job – especially towards the end, when everything can end up waiting for the slowest task. With speculative execution enabled, however, a single task can be executed on multiple slave nodes.

#### Scheduling

By default Hadoop uses FIFO scheduling, and optionally 5 scheduling priorities to schedule jobs from a work queue. In version 0.19 the job scheduler was refactored out of the JobTracker, while adding the ability to use an alternate scheduler (such as the *Fair scheduler* or the *Capacity scheduler*, described next).

##### Fair scheduler

The fair scheduler was developed by Facebook. The goal of the fair scheduler is to provide fast response times for small jobs and quality of service (QoS) for production jobs. The fair scheduler has three basic concepts.

1. Jobs are grouped into pools.
2. Each pool is assigned a guaranteed minimum share.
3. Excess capacity is split between jobs.

By default, jobs that are uncategorized go into a default pool. Pools have to specify the minimum number of map slots, reduce slots, as well as a limit on the number of running jobs.

##### Capacity scheduler

The capacity scheduler was developed by Yahoo. The capacity scheduler supports several features that are similar to those of the fair scheduler.

1. Queues are allocated a fraction of the total resource capacity.
2. Free resources are allocated to queues beyond their total capacity.
3. Within a queue, a job with a high level of priority has access to the queue's resources.

There is no preemption once a job is running.

### Difference between Hadoop 1 and Hadoop 2 (YARN)

The biggest difference between Hadoop 1 and Hadoop 2 is the addition of YARN (Yet Another Resource Negotiator), which replaced the MapReduce engine in the first version of Hadoop. YARN strives to allocate resources to various applications effectively. It runs two daemons, which take care of two different tasks: the *resource manager*, which does job tracking and resource allocation to applications, the *application master*, which monitors progress of the execution.

### Difference between Hadoop 2 and Hadoop 3

There are important features provided by Hadoop 3. For example, while there is one single *namenode* in Hadoop 2, Hadoop 3, enables having multiple name nodes, which solves the single point of failure problem.

In Hadoop 3, there are containers working in principle of Docker, which reduces time spent on application development.

One of the biggest changes is that Hadoop 3 decreases storage overhead with erasure coding.

Also, Hadoop 3 permits usage of GPU hardware within the cluster, which is a very substantial benefit to execute deep learning algorithms on a Hadoop cluster.

### Other applications

The HDFS is not restricted to MapReduce jobs. It can be used for other applications, many of which are under development at Apache. The list includes the HBase database, the Apache Mahout machine learning system, and the Apache Hive data warehouse. Theoretically, Hadoop could be used for any workload that is batch-oriented rather than real-time, is very data-intensive, and benefits from parallel processing. It can also be used to complement a real-time system, such as lambda architecture, Apache Storm, Flink, and Spark Streaming.

Commercial applications of Hadoop include:

- Log or clickstream analysis
- Marketing analytics
- Machine learning and data mining
- Image processing
- XML message processing
- Web crawling
- Archival work for compliance, including of relational and tabular data

## Prominent use cases

On 19 February 2008, Yahoo! Inc. launched what they claimed was the world's largest Hadoop production application. The Yahoo! Search Webmap is a Hadoop application that runs on a Linux cluster with more than 10,000 cores and produced data that was used in every Yahoo! web search query. There are multiple Hadoop clusters at Yahoo! and no HDFS file systems or MapReduce jobs are split across multiple data centers. Every Hadoop cluster node bootstraps the Linux image, including the Hadoop distribution. Work that the clusters perform is known to include the index calculations for the Yahoo! search engine. In June 2009, Yahoo! made the source code of its Hadoop version available to the open-source community.

In 2010, Facebook claimed that they had the largest Hadoop cluster in the world with 21 PB of storage. In June 2012, they announced the data had grown to 100 PB and later that year they announced that the data was growing by roughly half a PB per day.

As of 2013, Hadoop adoption had become widespread: more than half of the Fortune 50 companies used Hadoop.

## Papers

Influential papers on the birth, growth, and curation of Hadoop and big data processing include: Jeffrey Dean, Sanjay Ghemawat (2004) MapReduce: Simplified Data Processing on Large Clusters, Google. This paper inspired Doug Cutting to develop an open-source implementation of the Map-Reduce framework. He named it Hadoop, after his son's toy elephant.

- Michael Franklin, Alon Halevy, David Maier (2005) From Databases to Dataspaces: A New Abstraction for Information Management. The authors highlight the need for storage systems to accept all data formats and to provide APIs for data access that evolve based on the storage system's understanding of the data.
- Fay Chang et al. (2006) Bigtable: A Distributed Storage System for Structured Data, Google.
- Robert Kallman et al. (2008) H-store: a high-performance, distributed main memory transaction processing system
