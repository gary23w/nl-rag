---
title: "KurrentDB/README.md at master · kurrent-io/KurrentDB · GitHub"
source: https://github.com/EventStore/EventStore/blob/master/README.md
domain: eventstore-db
license: CC-BY-SA-4.0
tags: eventstoredb, event sourcing database, event stream database, cqrs pattern
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

kurrent-io

/

KurrentDB

Public

- Notifications You must be signed in to change notification settings
- Fork 679
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

187 lines (125 loc) · 7.01 KB

Outline

- What is Kurrent
- What is KurrentDB
- What is Kurrent Cloud
- Licensing
- Documentation
- Getting started with KurrentDB
- Getting started with Kurrent Cloud
- Client libraries
- Deployment
- Communities
- Contributing
- Building KurrentDB
- More resources

## What is Kurrent

Event Store – the company and the product – are rebranding as Kurrent.

- The flagship product will be referred to as “the Kurrent event-native data platform” or “the Kurrent platform” or simply “Kurrent"
- EventStoreDB will be referred to as KurrentDB
- Event Store Cloud will now be called Kurrent Cloud

Read more about the rebrand in the rebrand FAQ.

## What is KurrentDB

KurrentDB is a database that's engineered for modern software applications and event-driven architectures. Its event-native design simplifies data modeling and preserves data integrity while the integrated streaming engine solves distributed messaging challenges and ensures data consistency.

Download the latest version. For more product information visit the website.

## What is Kurrent Cloud?

Kurrent Cloud is a fully managed cloud offering that's designed to make it easy for developers to build and run highly available and secure applications that incorporate KurrentDB without having to worry about managing the underlying infrastructure. You can provision KurrentDB clusters in AWS, Azure, and GCP, and connect these services securely to your own cloud resources.

For more details visit the website.

## Licensing

View KurrentDB's licensing information.

## Docs

For guidance on installation, development, deployment, and administration, see the User Documentation.

## Getting started with KurrentDB

Follow the getting started guide.

## Getting started with Kurrent Cloud

Kurrent can manage KurrentDB for you, so you don't have to run your own clusters. See the online documentation: Getting started with Kurrent Cloud.

## Client libraries

This guide shows you how to get started with KurrentDB by setting up an instance or cluster and configuring it. KurrentDB supports the gRPC protocol.

### KurrentDB supported clients

- Python: pyeventsourcing/kurrentdbclient
- Node.js (javascript/typescript): kurrent-io/KurrentDB-Client-NodeJS
- Java: (kurrent-io/KurrentDB-Client-Java
- .NET: kurrent-io/EventStore-Client-Dotnet
- Go: kurrent-io/KurrentDB-Client-Go
- Rust: kurrent-io/KurrentDB-Client-Rust
- Read more in the gRPC clients documentation

### Community supported clients

- Elixir: NFIBrokerage/spear
- Ruby: yousty/event_store_client

Read more in the documentation.

### Legacy clients (support ends with EventStoreDB v23.10 LTS)

- .NET: EventStoreDB-Client-Dotnet-Legacy

## Deployment

- Kurrent Cloud - steps to get started in Kurrent Cloud.
- Self-managed - steps to host KurrentDB yourself.

## Communities

Join our global community of developers.

- Discuss
- Discord (Kurrent)
- Discord (ddd-cqrs-es)

## Contributing

Development is done on the `master` branch. We attempt to do our best to ensure that the history remains clean and to do so, commits are automatically squashed into a single logical commit when pull requests are merged.

If you want to switch to a particular release, you can check out the release branch for that particular release. For example: `git checkout release/v25.0`

- Create an issue
- Documentation
- Contributing guide

## Building KurrentDB

KurrentDB is written in a mixture of C# and JavaScript. It can run on Windows, Linux and macOS (using Docker) using the .NET Core runtime.

**Prerequisites**

- .NET SDK 10.0

Once you've installed the prerequisites for your system, you can launch a `Release` build of KurrentDB as follows:

```
dotnet build -c Release src
```

To start a single node, you can then run:

```
dotnet ./src/KurrentDB/bin/Release/net10.0/KurrentDB.dll --dev --db ./tmp/data --index ./tmp/index --log ./tmp/log
```

### Running the tests

You can launch the tests as follows:

```
dotnet test --solution src/KurrentDB.sln
```

### Build KurrentDB Docker image

You can also build a Docker image by running the command:

```
docker build --tag mykurrentdb . \
--build-arg CONTAINER_RUNTIME={container-runtime}
--build-arg RUNTIME={runtime}
```

For instance:

```
docker build --tag mykurrentdb . \
--build-arg CONTAINER_RUNTIME=noble \
--build-arg RUNTIME=linux-x64
```

***Note:*** Because of the Docker issue, if you're building a Docker image on Windows, you may need to set the `DOCKER_BUILDKIT=0` environment variable. For instance, running in PowerShell:

```
$env:DOCKER_BUILDKIT=0; docker build --tag mykurrentdb . `
--build-arg CONTAINER_RUNTIME=noble `
--build-arg RUNTIME=linux-x64
```

Currently, we support the following configurations:

1. Noble:

- `CONTAINER_RUNTIME=noble`
- `RUNTIME=linux-x64`

You can verify the built image by running:

```
docker run --rm mykurrentdb --insecure --what-if
```

## More resources

- Release notes
- Beginners Guide to Event Sourcing
- Articles
- Webinars
- Contact us
