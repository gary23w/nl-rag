---
title: "xtdb/README.adoc at main · xtdb/xtdb · GitHub"
source: https://github.com/xtdb/xtdb/blob/main/README.adoc
domain: xtdb
license: CC-BY-SA-4.0
tags: xtdb database, bitemporal database, datalog query, immutable database
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

xtdb

/

xtdb

Public

- Notifications You must be signed in to change notification settings
- Fork 189
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

49 lines (34 loc) · 2.34 KB

Outline

XTDB is an open-source immutable SQL database with comprehensive time-travel. XTDB has been built to simplify application development and address complex data compliance requirements.

Major features:

- Immutable - XTDB is optimised for current-time queries, but you can audit the full history of your database at any point, without needing snapshots or accessing backups.
- 'Bitemporal' - all data is accurately versioned as updates are made ('system' time), but it also allows you to separately record and query when that data is, was, or will become valid in your business domain ('valid' time).
- Dynamic - you don’t need to specify schema up-front before documents (rows with arbitrarily nested data) can be inserted.
- Speaks both SQL and XTQL - a full SQL dialect that implements the bitemporal functionality as specified in the SQL:2011 standard, available over the Postgres wire protocol.
- Cloud native - the ACID, columnar engine is built on Apache Arrow and designed for object storage
- It is written and supported by JUXT.

## Quick links

- Discord Community
- Documentation
- Release notes
- Support: GitHub Discussions | hello@xtdb.com
- Maven releases
- Bibliography
- Developing XTDB
- XTDB v1 Documentation (see the `1.x` branch)

## Inside-out Architecture

XTDB embraces a log as the central point of coordination when running as a distributed system.

> What do we have to gain from turning the database inside out?
> 
> Simpler code, better scalability, better robustness, lower latency, and more flexibility for doing interesting things with data.

— Martin Kleppmann

We would love to hear from you: hello@xtdb.com

## License and Copyright

XTDB is licensed under the Mozilla Public License, version 2 or (at your option) any later version.

Copyright © 2018-2026 JUXT LTD.
