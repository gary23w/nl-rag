---
title: "Data stream management system"
source: https://en.wikipedia.org/wiki/Data_stream_management_system
domain: stream-processing-concepts
license: CC-BY-SA-4.0
tags: stream processing, event stream processing, data stream management system, windowing state, complex event processing
fetched: 2026-07-02
---

# Data stream management system

A **data stream management system** (DSMS) is a computer software system to manage continuous data streams. It is similar to a database management system (DBMS), which is, however, designed for static data in conventional databases. A DBMS also offers a flexible query processing so that the information needed can be expressed using queries. However, in contrast to a DBMS, a DSMS executes a *continuous query* that is not only performed once, but is permanently installed. Therefore, the query is continuously executed until it is explicitly uninstalled. Since most DSMS are data-driven, a continuous query produces new results as long as new data arrive at the system. This basic concept is similar to complex event processing so that both technologies are partially coalescing.

## Functional principle

One important feature of a DSMS is the possibility to handle potentially infinite and rapidly changing data streams by offering flexible processing at the same time, although there are only limited resources such as main memory. The following table provides various principles of DSMS and compares them to traditional DBMS.

| Database management system (DBMS) | Data stream management system (DSMS) |
|---|---|
| Persistent data (relations) | Volatile data streams |
| Random access | Sequential access |
| One-time queries | Continuous queries |
| (Theoretically) unlimited secondary storage | Limited main memory |
| Only the current state is relevant | Consideration of the order of the input |
| Relatively low update rate | Potentially extremely high update rate |
| Little or no time requirements | Real-time requirements |
| Assumes exact data | Assumes outdated/inaccurate data |
| Plannable query processing | Variable data arrival and data characteristics |

## Processing and streaming models

One of the biggest challenges for a DSMS is to handle potentially infinite data streams using a fixed amount of memory and no random access to the data. There are different approaches to limit the amount of data in one pass, which can be divided into two classes. For the one hand, there are compression techniques that try to summarize the data and for the other hand there are window techniques that try to portion the data into (finite) parts.

### Synopses

The idea behind compression techniques is to maintain only a synopsis of the data, but not all (raw) data points of the data stream. The algorithms range from selecting random data points called sampling to summarization using histograms, wavelets or sketching. One simple example of a compression is the continuous calculation of an average. Instead of memorizing each data point, the synopsis only holds the sum and the number of items. The average can be calculated by dividing the sum by the number. However, it should be mentioned that synopses cannot reflect the data accurately. Thus, a processing that is based on synopses may produce inaccurate results.

### Windows

Instead of using synopses to compress the characteristics of the whole data streams, window techniques only look on a portion of the data. This approach is motivated by the idea that only the most recent data are relevant. Therefore, a window continuously cuts out a part of the data stream, e.g. the last ten data stream elements, and only considers these elements during the processing. There are different kinds of such windows like sliding windows that are similar to FIFO lists or tumbling windows that cut out disjoint parts. Furthermore, the windows can also be differentiated into element-based windows, e.g., to consider the last ten elements, or time-based windows, e.g., to consider the last ten seconds of data. There are also different approaches to implementing windows. There are, for example, approaches that use timestamps or time intervals for system-wide windows or buffer-based windows for each single processing step. Sliding-window query processing is also suitable to being implemented in parallel processors by exploiting parallelism between different windows and/or within each window extent.

## Query processing

Since there are a lot of prototypes, there is no standardized architecture. However, most DSMS are based on the query processing in DBMS by using declarative languages to express queries, which are translated into a plan of operators. These plans can be optimized and executed. A query processing often consists of the following steps.

### Formulation of continuous queries

The formulation of queries is mostly done using declarative languages like SQL in DBMS. Since there are no standardized query languages to express continuous queries, there are a lot of languages and variations. However, most of them are based on SQL, such as the Continuous Query Language (CQL), StreamSQL and ESP. There are also graphical approaches where each processing step is a box and the processing flow is expressed by arrows between the boxes.

The language strongly depends on the processing model. For example, if windows are used for the processing, the definition of a window has to be expressed. In StreamSQL, a query with a sliding window for the last 10 elements looks like follows:

```mw
SELECT AVG(price) FROM examplestream [SIZE 10 ADVANCE 1 TUPLES] WHERE value > 100.0
```

This stream continuously calculates the average value of "price" of the last 10 tuples, but only considers those tuples whose prices are greater than 100.0.

In the next step, the declarative query is translated into a logical query plan. A query plan is a directed graph where the nodes are operators and the edges describe the processing flow. Each operator in the query plan encapsulates the semantic of a specific operation, such as filtering or aggregation. In DSMSs that process relational data streams, the operators are equal or similar to the operators of the Relational algebra, so that there are operators for selection, projection, join, and set operations. This operator concept allows the very flexible and versatile processing of a DSMS.

### Optimization of queries

The logical query plan can be optimized, which strongly depends on the streaming model. The basic concepts for optimizing continuous queries are equal to those from database systems. If there are relational data streams and the logical query plan is based on relational operators from the Relational algebra, a query optimizer can use the algebraic equivalences to optimize the plan. These may be, for example, to push selection operators down to the sources, because they are not so computationally intensive like join operators.

Furthermore, there are also cost-based optimization techniques like in DBMS, where a query plan with the lowest costs is chosen from different equivalent query plans. One example is to choose the order of two successive join operators. In DBMS this decision is mostly done by certain statistics of the involved databases. But, since the data of a data streams is unknown in advance, there are no such statistics in a DSMS. However, it is possible to observe a data stream for a certain time to obtain some statistics. Using these statistics, the query can also be optimized later. So, in contrast to a DBMS, some DSMS allows to optimize the query even during runtime. Therefore, a DSMS needs some plan migration strategies to replace a running query plan with a new one.

### Transformation of queries

Since a logical operator is only responsible for the semantics of an operation but does not consist of any algorithms, the logical query plan must be transformed into an executable counterpart. This is called a physical query plan. The distinction between a logical and a physical operator plan allows more than one implementation for the same logical operator. The join, for example, is logically the same, although it can be implemented by different algorithms like a Nested loop join or a Sort-merge join. Notice, these algorithms also strongly depend on the used stream and processing model. Finally, the query is available as a physical query plan.

### Execution of queries

Since the physical query plan consists of executable algorithms, it can be directly executed. For this, the physical query plan is installed into the system. The bottom of the graph (of the query plan) is connected to the incoming sources, which can be everything like connectors to sensors. The top of the graph is connected to the outgoing sinks, which may be for example a visualization. Since most DSMSs are data-driven, a query is executed by pushing the incoming data elements from the source through the query plan to the sink. Each time when a data element passes an operator, the operator performs its specific operation on the data element and forwards the result to all successive operators.

## Examples

- AURORA, StreamBase Systems, Inc. Archived 23 March 2009 at the Wayback Machine
- Hortonworks DataFlow
- IBM Streams
- NIAGARA Query Engine
- NiagaraST: A Research Data Stream Management System at Portland State University
- Odysseus, an open source Java-based framework for Data Stream Management Systems
- Pipeline DB
- PIPES Archived 24 December 2016 at the Wayback Machine, webMethods Business Events
- QStream
- SAS Event Stream Processing
- SQLstream
- STREAM
- StreamGlobe
- StreamInsight
- TelegraphCQ
- WSO2 Stream Processor
