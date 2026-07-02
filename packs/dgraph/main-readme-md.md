---
title: "dgraph/README.md at main · dgraph-io/dgraph · GitHub"
source: https://github.com/hypermodeinc/dgraph/blob/main/README.md
domain: dgraph
license: CC-BY-SA-4.0
tags: dgraph database, distributed graph database, dql query language, graphql database
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

dgraph-io

/

dgraph

Public

- Notifications You must be signed in to change notification settings
- Fork 1.6k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

152 lines (113 loc) · 7.51 KB

Outline

(GitHub Repo stars) (GitHub commit activity) (Go Report Card) (Docker Pulls)

Dgraph is a horizontally scalable and distributed GraphQL database with a graph backend. It provides ACID transactions, consistent replication, and linearizable reads. It's built from the ground up to perform a rich set of queries. Being a native GraphQL database, it tightly controls how the data is arranged on disk to optimize for query performance and throughput, reducing disk seeks and network calls in a cluster.

Dgraph's goal is to provide Google production-level scale and throughput, with low enough latency to serve real-time user queries over terabytes of structured data. Dgraph supports GraphQL query syntax, and responds in JSON and Protocol Buffers over GRPC and HTTP. Dgraph is written using the Go Programming Language.

## Status

Dgraph is at version v25 and is production-ready. Apart from the vast open source community, it is being used in production at multiple Fortune 500 companies.

## Supported Platforms

Dgraph officially supports the Linux/amd64 and Linux/arm64 architectures. In order to take advantage of memory performance gains and other architecture-specific advancements in Linux, we dropped official support for Mac and Windows in 2021, see this blog post for more information. You can still build and use Dgraph on other platforms (for live or bulk loading for instance), but support for platforms other than Linux/amd64 and Linux/arm64 is not available.

Running Dgraph in a Docker environment is the recommended testing and deployment method.

## Install with Docker

If you're using Docker, you can use the official Dgraph image.

```highlight
docker pull dgraph/dgraph:latest
```

For more information on a variety Docker deployment methods including Docker Compose and Kubernetes, see the docs.

## Run a Quick Standalone Cluster

```highlight
docker run -it -p 8080:8080 -p 9080:9080 -v ~/dgraph:/dgraph dgraph/standalone:latest
```

## Install from Source

If you want to install from source, install Go 1.24+ or later and the following dependencies:

### Ubuntu

```highlight
sudo apt-get update
sudo apt-get install build-essential
```

### Build and Install

Then clone the Dgraph repository and use `make install` to install the Dgraph binary in the directory named by the GOBIN environment variable, which defaults to $GOPATH/bin or $HOME/go/bin if the GOPATH environment variable is not set.

```highlight
git clone https://github.com/dgraph-io/dgraph.git
cd dgraph
make setup
make install
```

## Get Started

**To get started with Dgraph, follow:**

- Installation to queries in 4 quick steps.
- Tutorial and presentation videos on YouTube channel.

## Is Dgraph the right choice for me?

- Do you have more than 10 SQL tables connected via foreign keys?
- Do you have sparse data, which doesn't elegantly fit into SQL tables?
- Do you want a simple and flexible schema, which is readable and maintainable over time?
- Do you care about speed and performance at scale?

If the answers to the above are YES, then Dgraph would be a great fit for your application. Dgraph provides NoSQL like scalability while providing SQL like transactions and the ability to select, filter, and aggregate data points. It combines that with distributed joins, traversals, and graph operations, which makes it easy to build applications with it.

## Dgraph compared to other graph DBs

| Features | Dgraph | Neo4j | Janus Graph |
|---|---|---|---|
| Architecture | Sharded and Distributed | Single server (+ replicas in enterprise) | Layer on top of other distributed DBs |
| Replication | Consistent | None in community edition (only available in enterprise) | Via underlying DB |
| Data movement for shard rebalancing | Automatic | Not applicable (all data lies on each server) | Via underlying DB |
| Language | GraphQL inspired | Cypher | Gremlin |
| Protocols | Grpc / HTTP + JSON / RDF | Bolt + Cypher | Websocket / HTTP |
| Transactions | Distributed ACID transactions | Single server ACID transactions | Not typically ACID |
| Full-Text Search | Native support | Native support | Via External Indexing System |
| Regular Expressions | Native support | Native support | Via External Indexing System |
| Geo Search | Native support | External support only | Via External Indexing System |
| License | Apache 2.0 | GPL v3 | Apache 2.0 |

## Users

- **Dgraph official documentation is present at docs.dgraph.io.**
- For general information and questions, visit Github discussions.
- Please see releases tab to find the latest release and corresponding release notes.

## Developers

Please see Contributing to Dgraph for guidelines on contributions.

## Client Libraries

The Dgraph team maintains several officially supported client libraries. There are also libraries contributed by the community unofficial client libraries.

## Contact

- Please use Github discussions for questions, feature requests and discussions.
- Please use GitHub Issues for filing bugs or feature requests.
