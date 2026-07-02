---
title: "scylladb/README.md at master · scylladb/scylladb · GitHub"
source: https://github.com/scylladb/scylladb/blob/master/README.md
domain: scylladb
license: CC-BY-SA-4.0
tags: scylladb, wide-column store, seastar framework, apache cassandra
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

scylladb

/

scylladb

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

112 lines (76 loc) · 5.16 KB

Outline

# Scylla

(Slack) (Twitter)

## What is Scylla?

Scylla is the real-time big data database that is API-compatible with Apache Cassandra and Amazon DynamoDB. Scylla embraces a shared-nothing approach that increases throughput and storage capacity to realize order-of-magnitude performance improvements and reduce hardware costs.

For more information, please see the ScyllaDB web site.

## Build Prerequisites

Scylla is fairly fussy about its build environment, requiring very recent versions of the C++23 compiler and of many libraries to build. The document HACKING.md includes detailed information on building and developing Scylla, but to get Scylla building quickly on (almost) any build machine, Scylla offers a frozen toolchain. This is a pre-configured Docker image which includes recent versions of all the required compilers, libraries and build tools. Using the frozen toolchain allows you to avoid changing anything in your build machine to meet Scylla's requirements - you just need to meet the frozen toolchain's prerequisites (mostly, Docker or Podman being available).

## Building Scylla

Building Scylla with the frozen toolchain `dbuild` is as easy as:

```highlight
$ git submodule update --init --force --recursive
$ ./tools/toolchain/dbuild ./configure.py
$ ./tools/toolchain/dbuild ninja build/release/scylla
```

For further information, please see:

- Developer documentation for more information on building Scylla.
- Build documentation on how to build Scylla binaries, tests, and packages.
- Docker image build documentation for information on how to build Docker images.

## Running Scylla

To start Scylla server, run:

```highlight
$ ./tools/toolchain/dbuild ./build/release/scylla --workdir tmp --smp 1 --developer-mode 1
```

This will start a Scylla node with one CPU core allocated to it and data files stored in the `tmp` directory. The `--developer-mode` is needed to disable the various checks Scylla performs at startup to ensure the machine is configured for maximum performance (not relevant on development workstations). Please note that you need to run Scylla with `dbuild` if you built it with the frozen toolchain.

For more run options, run:

```highlight
$ ./tools/toolchain/dbuild ./build/release/scylla --help
```

## Testing

(Build with the latest Seastar) (Check Reproducible Build) (clang-nightly)

See test.py manual.

## Scylla APIs and compatibility

By default, Scylla is compatible with Apache Cassandra and its API - CQL. There is also support for the API of Amazon DynamoDB™, which needs to be enabled and configured in order to be used. For more information on how to enable the DynamoDB™ API in Scylla, and the current compatibility of this feature as well as Scylla-specific extensions, see Alternator and Getting started with Alternator.

## Documentation

Documentation can be found here. Seastar documentation can be found here. User documentation can be found here.

## Training

Training material and online courses can be found at Scylla University. The courses are free, self-paced and include hands-on examples. They cover a variety of topics including Scylla data modeling, administration, architecture, basic NoSQL concepts, using drivers for application development, Scylla setup, failover, compactions, multi-datacenters and how Scylla integrates with third-party applications.

## Contributing to Scylla

If you want to report a bug or submit a pull request or a patch, please read the contribution guidelines.

If you are a developer working on Scylla, please read the developer guidelines.

## Contact

- The community forum and Slack channel are for users to discuss configuration, management, and operations of ScyllaDB.
- The developers mailing list is for developers and people interested in following the development of ScyllaDB to discuss technical topics.
