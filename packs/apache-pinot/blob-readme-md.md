---
title: "pinot/README.md at master · apache/pinot · GitHub"
source: https://github.com/apache/pinot/blob/master/README.md
domain: apache-pinot
license: CC-BY-SA-4.0
tags: apache pinot, real-time olap datastore, low-latency analytics, columnar storage
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

apache

/

pinot

Public

- Notifications You must be signed in to change notification settings
- Fork 1.5k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

197 lines (134 loc) · 12.5 KB

Outline

(Unit Tests) (Integration Tests) (Quickstart Tests) (Compatibility Checks) (Release) (codecov.io) (Join the chat at https://communityinviter.com/apps/apache-pinot/apache-pinot) (Twitter Follow) (License) (Ask DeepWiki)

- What is Apache Pinot?
  - Features
  - When should I use Pinot?
  - Contributing to Pinot
  - Apache Pinot YouTube Channel
  - Building Pinot
  - Deploying Pinot to Kubernetes
  - Join the Community
  - Documentation
  - License

# What is Apache Pinot?

Apache Pinot is a real-time distributed OLAP datastore, built to deliver scalable real-time analytics with low latency. It can ingest from batch data sources (such as Hadoop HDFS, Amazon S3, Azure ADLS, Google Cloud Storage) as well as stream data sources (such as Apache Kafka).

Pinot was built by engineers at LinkedIn and Uber and is designed to scale up and out with no upper bound. Performance always remains constant based on the size of your cluster and an expected query per second (QPS) threshold.

For getting started guides, deployment recipes, tutorials, and more, please visit our project documentation at https://docs.pinot.apache.org.

(Apache Pinot)

## Features

Pinot was originally built at LinkedIn to power rich interactive real-time analytic applications such as Who Viewed Profile, Company Analytics, Talent Insights, and many more. UberEats Restaurant Manager is another example of a customer facing Analytics App. At LinkedIn, Pinot powers 50+ user-facing products, ingesting millions of events per second and serving 100k+ queries per second at millisecond latency.

- **Fast Queries**: Filter and aggregate petabyte data sets with P90 latencies in the tens of milliseconds—fast enough to return live results interactively in the UI.
- **High Concurrency**: With user-facing applications querying Pinot directly, it can serve hundreds of thousands of concurrent queries per second.
- **SQL Query Interface**: The highly standard SQL query interface is accessible through a built-in query editor and a REST API.
- **Versatile Joins**: Perform arbitrary fact/dimension and fact/fact joins on petabyte data sets.
- **Column-oriented**: a column-oriented database with various compression schemes such as Run Length, Fixed Bit Length.
- **Pluggable indexing**: pluggable indexing technologies including timestamp, inverted, StarTree, Bloom filter, range, text, JSON, and geospatial options.
- **Stream and batch ingest**: Ingest from Apache Kafka, Apache Pulsar, and AWS Kinesis in real time. Batch ingest from Hadoop, Spark, AWS S3, and more. Combine batch and streaming sources into a single table for querying.
- **Upsert during real-time ingestion**: update the data at-scale with consistency
- **Built-in Multitenancy**: Manage and secure data in isolated logical namespaces for cloud-friendly resource management.
- **Built for Scale**: Pinot is horizontally scalable and fault-tolerant, adaptable to workloads across the storage and throughput spectrum.
- **Cloud-native on Kubernetes**: Helm chart provides a horizontally scalable and fault-tolerant clustered deployment that is easy to manage using Kubernetes.

(Apache Pinot query console)

## When should I use Pinot?

Pinot is designed to execute real-time OLAP queries with low latency on massive amounts of data and events. In addition to real-time stream ingestion, Pinot also supports batch use cases with the same low latency guarantees. It is suited in contexts where fast analytics, such as aggregations, are needed on immutable data, possibly, with real-time data ingestion. Pinot works very well for querying time series data with lots of dimensions and metrics.

Example query:

```highlight
SELECT sum(clicks), sum(impressions) FROM AdAnalyticsTable
  WHERE
       ((daysSinceEpoch >= 17849 AND daysSinceEpoch <= 17856)) AND
       accountId IN (123456789)
  GROUP BY
       daysSinceEpoch TOP 100
```

## Contributing to Pinot

Want to contribute to Apache Pinot? 👋🍷

Want to join the ranks of open source committers to Apache Pinot? Then check out the Contribution Guide for how you can get involved in the code.

If you have a bug or an idea for a new feature, browse the open issues to see what we’re already working on before opening a new one.

We also tagged some beginner issues new contributors can tackle.

## Apache Pinot YouTube Channel

Share Your Pinot Videos with the Community!

Have a Pinot use case, tutorial, or conference/meetup recording to share? We’d love to feature it on the Pinot OSS YouTube channel! Drop your video or a link to your session in the #pinot-youtube-channel on Pinot Slack, and we’ll showcase it for the community!

## Building Pinot

```
# Clone a repo
$ git clone https://github.com/apache/pinot.git
$ cd pinot

# Pinot services require JDK 21+ to build and run
# Java/JDBC clients and SPI artifacts continue to target Java 11 bytecode

# Build Pinot
# -Pbin-dist is required to build the binary distribution
# -Pbuild-shaded-jar is required to build the shaded jar, which is necessary for some features like spark connectors
$ ./mvnw clean install -DskipTests -Pbin-dist -Pbuild-shaded-jar

# Run the Quick Demo
$ cd build/
$ bin/quick-start-batch.sh
```

For UI development setup refer this doc.

Normal Pinot builds are done using the `./mvnw clean install` command.

However this command can take a long time to run.

For faster builds it is recommended to use `./mvnw verify -Ppinot-fastdev`, which disables some plugins that are not actually needed for development.

More detailed instructions can be found at Quick Demo section in the documentation.

### macOS Build Requirements

If you're building Pinot on macOS and encounter issues with the gRPC Java plugin during the build process, you may need to configure the protobuf Maven plugin to use a specific executable path. This is a known issue on macOS ARM (Apple Silicon) systems.

#### Automatic Profile Activation (macOS ARM64)

Pinot's Maven build now includes dedicated profiles for Apple Silicon (ARM64) Macs to ensure reliable protobuf compilation with Homebrew-installed binaries:

- **Primary profile:** Activates automatically if `/opt/homebrew/bin/protoc-gen-grpc-java` exists (default for Apple Silicon Macs).
- **Fallback profile:** Activates if `/usr/local/bin/protoc-gen-grpc-java` exists and the primary path does not (for Intel Macs or custom Homebrew setups).

You do **not** need to manually edit the `pom.xml` or set the plugin executable path. The correct profile will be selected based on your system and Homebrew installation.

##### To install the required tools:

```highlight
brew install protobuf
brew install protoc-gen-grpc-java
```

If you installed Homebrew to a non-default location, ensure the `protoc-gen-grpc-java` binary is available in either `/opt/homebrew/bin/` or `/usr/local/bin/`.

To verify which profile is active, run:

```highlight
./mvnw help:active-profiles
```

If you encounter issues, check that the `protoc-gen-grpc-java` binary is present in one of the expected locations and is executable.

## Deploying Pinot to Kubernetes

Please refer to Running Pinot on Kubernetes in our project documentation. Pinot also provides Kubernetes integrations with the interactive query engine, Trino, and the data visualization tool, Apache Superset.

## Join the Community

- Ask questions on Apache Pinot Slack
- Please join Apache Pinot mailing lists dev-subscribe@pinot.apache.org (subscribe to pinot-dev mailing list) dev@pinot.apache.org (posting to pinot-dev mailing list) users-subscribe@pinot.apache.org (subscribe to pinot-user mailing list) users@pinot.apache.org (posting to pinot-user mailing list)
- Apache Pinot Meetup Group: https://www.meetup.com/apache-pinot/

## Documentation

Check out Pinot documentation for a complete description of Pinot's features.

- Quick Demo
- Pinot Architecture
- Pinot Query Language

## License

Apache Pinot is under Apache License, Version 2.0
