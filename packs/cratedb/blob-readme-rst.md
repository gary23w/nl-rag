---
title: "crate/README.rst at master · crate/crate · GitHub"
source: https://github.com/crate/crate/blob/master/README.rst
domain: cratedb
license: CC-BY-SA-4.0
tags: cratedb database, distributed sql database, lucene search database, columnar storage
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

crate

/

crate

Public

- Notifications You must be signed in to change notification settings
- Fork 601
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

165 lines (117 loc) · 6.92 KB

Outline

Help us improve CrateDB by taking our User Survey!

## About

CrateDB is a distributed SQL database that makes it simple to store and analyze massive amounts of data in real-time.

CrateDB offers the benefits of an SQL database *and* the scalability and flexibility typically associated with NoSQL databases. Modest CrateDB clusters can ingest tens of thousands of records per second without breaking a sweat. You can run ad-hoc queries using standard SQL. CrateDB's blazing-fast distributed query execution engine parallelizes query workloads across the whole cluster.

CrateDB is well suited to containerization, can be scaled horizontally using ephemeral virtual machines (e.g., Kubernetes, AWS, and Azure) with no shared state. You can deploy and run CrateDB on any sort of network — from personal computers to multi-region hybrid clouds and the edge.

## Features

- Use standard SQL via the PostgreSQL wire protocol or an HTTP API.
- Dynamic table schemas and queryable objects provide document-oriented features in addition to the relational features of SQL.
- Support for time-series data, real-time full-text search, geospatial data types and search capabilities.
- Horizontally scalable, highly available and fault-tolerant clusters that run very well in virtualized and containerized environments.
- Extremely fast distributed query execution.
- Auto-partitioning, auto-sharding, and auto-replication.
- Self-healing and auto-rebalancing.
- User-defined functions (UDFs) can be used to extend the functionality of CrateDB.

## Screenshots

CrateDB provides an Admin UI:

(Screenshots of the CrateDB Admin UI)

## Try CrateDB

Run CrateDB via the official Docker Image:

```highlight
sh$ docker run --publish 4200:4200 --publish 5432:5432 --env CRATE_HEAP_SIZE=1g crate '-Cdiscovery.type=single-node'
```

Or visit the installation documentation to see all the available download and install options.

Once you're up and running, head over to the introductory docs. To interact with CrateDB, you can use the Admin UI sql console or the CrateDB shell CLI tool. Alternatively, review the list of recommended clients and tools that work with CrateDB.

For container-specific documentation, check out the CrateDB on Docker how-to guide or the CrateDB on Kubernetes how-to guide.

## Contributing

This project is primarily maintained by Crate.io, but we welcome community contributions!

See the developer docs and the contribution docs for more information.

## Security

The CrateDB team and community take security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

If you think you discovered a security flaw, please follow the guidelines at SECURITY.md.

## Help

Looking for more help?

- Try one of our beginner tutorials, how-to guides, or consult the reference manual.
- Check out our support channels.
- Crate.io also offers CrateDB Cloud, a fully-managed *CrateDB Database as a Service* (DBaaS). The CrateDB Cloud Tutorials will get you started.
