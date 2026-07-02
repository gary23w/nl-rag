---
title: "Apache Storm"
source: https://en.wikipedia.org/wiki/Apache_Storm
domain: apache-storm
license: CC-BY-SA-4.0
tags: apache storm, real time computation, stream processing, distributed topology, fault tolerance
fetched: 2026-07-02
---

# Apache Storm

**Apache Storm** is a distributed stream processing computation framework written predominantly in the Clojure programming language. Originally created by Nathan Marz and team at BackType, the project was open sourced after being acquired by Twitter. It uses custom created "spouts" and "bolts" to define information sources and manipulations to allow batch, distributed processing of streaming data. The initial release was on 17 September 2011.

A Storm application is designed as a "topology" in the shape of a directed acyclic graph (DAG) with spouts and bolts acting as the graph vertices. Edges on the graph are named streams and direct data from one node to another. Together, the topology acts as a data transformation pipeline. At a superficial level the general topology structure is similar to a MapReduce job, with the main difference being that data is processed in real time as opposed to in individual batches. Additionally, Storm topologies run indefinitely until killed, while a MapReduce job DAG must eventually end.

Storm became an Apache Top-Level Project in September 2014 and was previously in incubation since September 2013.

## Development

Apache Storm is developed under the Apache License, making it available to most companies to use. Git is used for version control and Atlassian Jira for issue tracking, under the Apache Incubator program.

| Version | Release date |
|---|---|
| 2.5.0 | 4 Aug 2023 |
| 2.4.0 | 25 March 2022 |
| 2.3.0 | 27 September 2021 |
| 2.2.0 | 30 June 2020 |
| 2.1.0 | 6 September 2019 |
| 1.2.3 | 18 July 2019 |
| 2.0.0 | 30 May 2019 |
| 1.1.4 | 8 January 2019 |
| 1.2.2 | 4 June 2018 |
| 1.1.3 |   |
| 1.0.7 | 3 May 2018 |
| 1.2.1 | 19 February 2018 |
| 1.2.0 | 15 February 2018 |
| 1.1.2 |   |
| 1.0.6 | 14 February 2018 |
| 1.0.5 | 15 September 2017 |
| 1.1.1 | 1 August 2017 |
| 1.0.4 | 28 July 2017 |
| 1.1.0 | 29 Mar 2017 |
| 1.0.3 | 14 February 2017 |
| 0.10.2 | 14 September 2016 |
| 0.9.7 | 7 September 2016 |
| 1.0.2 | 10 August 2016 |
| 1.0.1 | 6 May 2016 |
| 0.10.1 | 5 May 2016 |
| 1.0.0 | 12 April 2016 |
| 0.10.0 | 5 November 2015 |
| 0.9.6 |   |
| 0.9.5 | 4 June 2015 |
| 0.9.4 | 25 March 2015 |
| 0.9.3 | 25 November 2014 |
| 0.9.2 | 25 June 2014 |
| 0.9.1 | 10 February 2014 |
| Historical (non-Apache) Version | Release date |
| 0.9.0 | 8 December 2013 |
| 0.8.2 | 11 January 2013 |
| 0.8.1 | 6 September 2012 |
| 0.8.0 | 2 August 2012 |
| 0.7.0 | 28 February 2012 |
| 0.6.0 | 15 December 2011 |
| 0.5.0 | 19 September 2011 |

## Apache Storm architecture

The Apache Storm cluster comprises following critical components:

- **Nodes:** There are two types of nodes: Master Nodes and Worker Nodes. A **Master Node** executes a daemon **Nimbus** which assigns tasks to machines and monitors their performances. On the other hand, a Worker Node runs the daemon called **Supervisor** which assigns the tasks to other worker nodes and operates them as per the need. As Storm cannot monitor the state and health of cluster, it deploys ZooKeeper to solve this issue which connects Nimbus with the Supervisors.
- **Components:** Storm has three critical components: Topology, Stream, and Spout. Topology is a network made of Stream and Spout. Stream is an unbounded pipeline of tuples and Spout is the source of the data streams which converts the data into the tuple of streams and sends to the bolts to be processed.

## Peer platforms

Storm is but one of dozens of stream processing engines, for a more complete list see Stream processing. Twitter announced Heron on June 2, 2015 which is API compatible with Storm. There are other comparable streaming data engines such as Spark Streaming and Flink.
