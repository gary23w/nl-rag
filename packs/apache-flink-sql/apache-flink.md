---
title: "Apache Flink"
source: https://en.wikipedia.org/wiki/Apache_Flink
domain: apache-flink-sql
license: CC-BY-SA-4.0
tags: apache flink, flink sql, stateful stream processing, dataflow engine
fetched: 2026-07-02
---

# Apache Flink

**Apache Flink** is an open-source, unified stream-processing and batch-processing framework developed by the Apache Software Foundation. The core of Apache Flink is a distributed streaming data-flow engine written in Java and Scala. Flink executes arbitrary dataflow programs in a data-parallel and pipelined (hence task parallel) manner. Flink's pipelined runtime system enables the execution of bulk/batch and stream processing programs. Furthermore, Flink's runtime supports the execution of iterative algorithms natively.

Flink provides a high-throughput, low-latency streaming engine as well as support for event-time processing and state management. Flink applications are fault-tolerant in the event of machine failure and support exactly-once semantics. Programs can be written in Java, Python, and SQL and are automatically compiled and optimized into dataflow programs that are executed in a cluster or cloud environment.

Flink does not provide its own data-storage system, but provides data-source and sink connectors to systems such as Apache Doris, Amazon Kinesis, Apache Kafka, HDFS, Apache Cassandra, and ElasticSearch.

## Development

Apache Flink is developed under the Apache License 2.0 by the Apache Flink Community within the Apache Software Foundation. The project is driven by 127 committers and over 1354 contributors.

## Overview

Apache Flink's dataflow programming model provides event-at-a-time processing on both finite and infinite datasets. At a basic level, Flink programs consist of streams and transformations. “Conceptually, a stream is a (potentially never-ending) flow of data records, and a transformation is an operation that takes one or more streams as input, and produces one or more output streams as a result.”

Apache Flink includes two core APIs: a DataStream API for bounded or unbounded streams of data and a DataSet API for bounded data sets. Flink also offers a Table API, which is a SQL-like expression language for relational stream and batch processing that can be easily embedded in Flink's DataStream and DataSet APIs. The highest-level language supported by Flink is SQL, which is semantically similar to the Table API and represents programs as SQL query expressions.

### Programming Model and Distributed Runtime

Upon execution, Flink programs are mapped to streaming dataflows. Every Flink dataflow starts with one or more sources (a data input, e.g., a message queue or a file system) and ends with one or more sinks (a data output, e.g., a message queue, file system, or database). An arbitrary number of transformations can be performed on the stream. These streams can be arranged as a directed, acyclic dataflow graph, allowing an application to branch and merge dataflows.

Flink offers ready-built source and sink connectors with Apache Kafka, Amazon Kinesis, HDFS, Apache Cassandra, and more.

Flink programs run as a distributed system within a cluster and can be deployed in a standalone mode as well as on YARN, Mesos, Docker-based setups along with other resource management frameworks.

### State: Checkpoints, Savepoints, and Fault-tolerance

Apache Flink includes a lightweight fault tolerance mechanism based on distributed checkpoints. A checkpoint is an automatic, asynchronous snapshot of the state of an application and the position in a source stream. In the case of a failure, a Flink program with checkpointing enabled will, upon recovery, resume processing from the last completed checkpoint, ensuring that Flink maintains exactly-once state semantics within an application. The checkpointing mechanism exposes hooks for application code to include external systems into the checkpointing mechanism as well (like opening and committing transactions with a database system).

Flink also includes a mechanism called savepoints, which are manually-triggered checkpoints. A user can generate a savepoint, stop a running Flink program, then resume the program from the same application state and position in the stream. Savepoints enable updates to a Flink program or a Flink cluster without losing the application's state . As of Flink 1.2, savepoints also allow to restart an application with a different parallelism—allowing users to adapt to changing workloads.

### DataStream API

Flink's DataStream API enables transformations (e.g. filters, aggregations, window functions) on bounded or unbounded streams of data. The DataStream API includes more than 20 different types of transformations and is available in Java and Scala.

A simple example of a stateful stream processing program is an application that emits a word count from a continuous input stream and groups the data in 5-second windows:

```mw
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

case class WordCount(word: String, count: Int)

object WindowWordCount {
  def main(args: Array[String]) {

    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val text = env.socketTextStream("localhost", 9999)

    val counts = text.flatMap { _.toLowerCase.split("\\W+") filter { _.nonEmpty } }
      .map { WordCount(_, 1) }
      .keyBy("word")
      .timeWindow(Time.seconds(5))
      .sum("count")

    counts.print

    env.execute("Window Stream WordCount")
  }
}
```

#### Apache Beam - Flink Runner

Apache Beam “provides an advanced unified programming model, allowing (a developer) to implement batch and streaming data processing jobs that can run on any execution engine.” The Apache Flink-on-Beam runner is the most feature-rich according to a capability matrix maintained by the Beam community.

data Artisans, in conjunction with the Apache Flink community, worked closely with the Beam community to develop a Flink runner.

### DataSet API

Flink's DataSet API enables transformations (e.g., filters, mapping, joining, grouping) on bounded datasets. The DataSet API includes more than 20 different types of transformations. The API is available in Java, Scala and an experimental Python API. Flink's DataSet API is conceptually similar to the DataStream API. This API is deprecated at Flink version 2.0

### Table API and SQL

Flink's Table API is a SQL-like expression language for relational stream and batch processing that can be embedded in Flink's Java and Scala DataSet and DataStream APIs. The Table API and SQL interface operate on a relational Table abstraction. Tables can be created from external data sources or from existing DataStreams and DataSets. The Table API supports relational operators such as selection, aggregation, and joins on Tables.

Tables can also be queried with regular SQL. The Table API and SQL offer equivalent functionality and can be mixed in the same program. When a Table is converted back into a DataSet or DataStream, the logical plan, which was defined by relational operators and SQL queries, is optimized using Apache Calcite and is transformed into a DataSet or DataStream program.

## Flink Forward

Flink Forward is an annual conference about Apache Flink. The first edition of Flink Forward took place in 2015 in Berlin. The two-day conference had over 250 attendees from 16 countries. Sessions were organized in two tracks with over 30 technical presentations from Flink developers and one additional track with hands-on Flink training.

In 2016, 350 participants joined the conference and over 40 speakers presented technical talks in 3 parallel tracks. On the third day, attendees were invited to participate in hands-on training sessions.

In 2017, the event expanded to San Francisco, as well. The conference day was dedicated to technical talks on how Flink is used in the enterprise, Flink system internals, ecosystem integrations with Flink, and the future of the platform. It featured keynotes, talks from Flink users in industry and academia, and hands-on training sessions on Apache Flink.

In 2020, following the COVID-19 pandemic, Flink Forward's spring edition which was supposed to be hosted in San Francisco was canceled. Instead, the conference was hosted virtually, starting on April 22 and concluding on April 24, featuring live keynotes, Flink use cases, Apache Flink internals, and other topics on stream processing and real-time analytics.

In 2024 Flink Forward returned to Berlin, its birth place, for the 10th anniversary. The conference highlighted the new Flink 2.0 plans, where Java 8 is dropped and a new state backend is introduced. Flink CDC was also introduced, allowing no code yaml authored flows. There was also a session on Flink's adoption of OpenLineage.

## History

In 2010, the research project "Stratosphere: Information Management on the Cloud" led by Volker Markl (funded by the German Research Foundation (DFG)) was started as a collaboration of Technische Universität Berlin, Humboldt-Universität zu Berlin, and Hasso-Plattner-Institut Potsdam. Flink started from a fork of Stratosphere's distributed execution engine and it became an Apache Incubator project in March 2014. In December 2014, Flink was accepted as an Apache top-level project.

| Version | Original release date | Latest version | Release date |
|---|---|---|---|
| Unsupported: 0.9 | 2015-06-24 | 0.9.1 | 2015-09-01 |
| Unsupported: 0.10 | 2015-11-16 | 0.10.2 | 2016-02-11 |
| Unsupported: 1.0 | 2016-03-08 | 1.0.3 | 2016-05-11 |
| Unsupported: 1.1 | 2016-08-08 | 1.1.5 | 2017-03-22 |
| Unsupported: 1.2 | 2017-02-06 | 1.2.1 | 2017-04-26 |
| Unsupported: 1.3 | 2017-06-01 | 1.3.3 | 2018-03-15 |
| Unsupported: 1.4 | 2017-12-12 | 1.4.2 | 2018-03-08 |
| Unsupported: 1.5 | 2018-05-25 | 1.5.6 | 2018-12-26 |
| Unsupported: 1.6 | 2018-08-08 | 1.6.3 | 2018-12-22 |
| Unsupported: 1.7 | 2018-11-30 | 1.7.2 | 2019-02-15 |
| Unsupported: 1.8 | 2019-04-09 | 1.8.3 | 2019-12-11 |
| Unsupported: 1.9 | 2019-08-22 | 1.9.2 | 2020-01-30 |
| Unsupported: 1.10 | 2020-02-11 | 1.10.3 | 2021-01-29 |
| Unsupported: 1.11 | 2020-07-06 | 1.11.6 | 2021-12-16 |
| Unsupported: 1.12 | 2020-12-10 | 1.12.7 | 2021-12-16 |
| Unsupported: 1.13 | 2021-05-03 | 1.13.6 | 2022-02-18 |
| Unsupported: 1.14 | 2021-09-29 | 1.14.6 | 2022-09-28 |
| Unsupported: 1.15 | 2022-05-05 | 1.15.4 | 2023-03-15 |
| Unsupported: 1.16 | 2022-10-28 | 1.16.3 | 2023-11-29 |
| Unsupported: 1.17 | 2023-03-23 | 1.17.2 | 2023-11-29 |
| Unsupported: 1.18 | 2023-10-24 | 1.18.1 | 2024-01-19 |
| Supported: 1.19 | 2024-03-18 | 1.19.2 | 2025-02-12 |
| Supported: 1.20 (LTS) | 2024-08-02 | 1.20.3 | 2025-09-25 |
| Supported: 2.0 | 2025-03-19 | 2.0.1 | 2025-10-30 |
| Supported: 2.1 | 2025-07-29 | 2.1.1 | 2025-10-30 |
| Latest version: 2.2 | 2025-12-03 | 2.2.0 | 2025-12-03 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

*Release Dates*

- 12/2025: Apache Flink 2.2 (12/2025: v2.2.0)
- 07/2025: Apache Flink 2.1 (10/2025: v2.1.1)
- 03/2025: Apache Flink 2.0 (10/2025: v2.0.1)
- 08/2024: Apache Flink 1.20 (09/2025: v1.20.3)
- 03/2024: Apache Flink 1.19 (06/2024: v1.19.1, 02/2025: v1.19.2)
- 10/2023: Apache Flink 1.18 (01/2024: v1.18.1)
- 03/2023: Apache Flink 1.17 (05/2023: v1.17.1; 11/2023: v1.17.2)
- 10/2022: Apache Flink 1.16 (01/2023: v1.16.1; 05/2023: v1.16.2; 11/2023: v1.16.3)
- 05/2022: Apache Flink 1.15 (07/2022: v1.15.1; 08/2022: v1.15.2; 11/2022: v1.15.3; 03/2023: v1.15.4)
- 09/2021: Apache Flink 1.14 (12/2021: v1.14.2; 01/2022: v1.14.3; 03/2022: v1.14.4; 06/2022: v1.14.5; 09/2022: v1.14.6)
- 05/2021: Apache Flink 1.13 (05/2021: v1.13.1; 08/2021: v1.13.2; 10/2021: v1.13.3; 12/2021: v1.13.5; 02/2022: v1.13.6)
- 12/2020: Apache Flink 1.12 (01/2021: v1.12.1; 03/2021: v1.12.2; 04/2021: v1.12.3; 05/2021: v1.12.4; 08/2021: v1.12.5; 12/2021: v1.12.7)
- 07/2020: Apache Flink 1.11 (07/2020: v1.11.1; 09/2020: v1.11.2; 12/2020: v1.11.3; 08/2021: v1.11.4; 12/2021: v1.11.6)
- 02/2020: Apache Flink 1.10 (05/2020: v1.10.1; 08/2020: v1.10.2; 01/2021: v1.10.3)
- 08/2019: Apache Flink 1.9 (10/2019: v1.9.1; 01/2020: v1.9.2)
- 04/2019: Apache Flink 1.8 (07/2019: v1.8.1; 09/2019: v1.8.2; 12/2019: v1.8.3)
- 11/2018: Apache Flink 1.7 (12/2018: v1.7.1; 02/2019: v1.7.2)
- 08/2018: Apache Flink 1.6 (09/2018: v1.6.1; 10/2018: v1.6.2; 12/2018: v1.6.3; 02/2019: v1.6.4)
- 05/2018: Apache Flink 1.5 (07/2018: v1.5.1; 07/2018: v1.5.2; 08/2018: v1.5.3; 09/2018: v1.5.4; 10/2018: v1.5.5; 12/2018: v1.5.6)
- 12/2017: Apache Flink 1.4 (02/2018: v1.4.1; 03/2018: v1.4.2)
- 06/2017: Apache Flink 1.3 (06/2017: v1.3.1; 08/2017: v1.3.2; 03/2018: v1.3.3)
- 02/2017: Apache Flink 1.2 (04/2017: v1.2.1)
- 08/2016: Apache Flink 1.1 (08/2016: v1.1.1; 09/2016: v1.1.2; 10/2016: v1.1.3; 12/2016: v1.1.4; 03/2017: v1.1.5)
- 03/2016: Apache Flink 1.0 (04/2016: v1.0.1; 04/2016: v1.0.2; 05/2016: v1.0.3)
- 11/2015: Apache Flink 0.10 (11/2015: v0.10.1; 02/2016: v0.10.2)
- 06/2015: Apache Flink 0.9 (09/2015: v0.9.1)
  - 04/2015: Apache Flink 0.9-milestone-1

*Apache Incubator Release Dates*

- 01/2015: Apache Flink 0.8-incubating
- 11/2014: Apache Flink 0.7-incubating
- 08/2014: Apache Flink 0.6-incubating (09/2014: v0.6.1-incubating)
- 05/2014: Stratosphere 0.5 (06/2014: v0.5.1; 07/2014: v0.5.2)

*Pre-Apache Stratosphere Release Dates*

- 01/2014: Stratosphere 0.4 (version 0.3 was skipped)
- 08/2012: Stratosphere 0.2
- 05/2011: Stratosphere 0.1 (08/2011: v0.1.1)

The 1.14.1, 1.13.4, 1.12.6, 1.11.5 releases, which were supposed to only contain a Log4j upgrade to 2.15.0, were skipped because CVE-2021-45046 was discovered during the release publication.
