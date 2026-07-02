---
title: "MariaDB"
source: https://en.wikipedia.org/wiki/MariaDB
domain: mariadb
license: CC-BY-SA-4.0
tags: mariadb, aria storage engine, galera cluster, innodb engine
fetched: 2026-07-02
---

# MariaDB

**MariaDB** is a free and open-source relational database management system (RDBMS) sharing a common heritage with MySQL, from which it was forked in 2009 by original MySQL developers following Oracle Corporation's acquisition of Sun Microsystems, with the intent to keep it free and open-source software under the GNU General Public License.

MariaDB originated as a drop-in replacement for MySQL; the two databases have diverged since version 5.6 in some features, syntax, and behaviour. Over sixteen years of independent development, MariaDB has evolved into a distinct database with capabilities spanning transactional, analytical, and AI workloads.

The *MariaDB Foundation* is a non-profit organisation that safeguards the open-source development of MariaDB independently of any commercial entity. *MariaDB plc* is a commercial entity providing enterprise products, support, and cloud services, owns the MariaDB trademark, and is the largest contributor to MariaDB's codebase.

Michael "Monty" Widenius, one of the founders of MySQL AB and the creator of MySQL and MariaDB, serves as the CTO of both MariaDB Foundation and MariaDB plc.

## Name and logo

MariaDB is named after founder Michael Widenius' younger daughter, Maria. MySQL is named after his other daughter, My. Its logo consists of a sea lion, that Monty Widenius chose based on his encounter with live sea lions while snorkeling with his daughter in the Galápagos Islands.

## History

### Origins and MySQL compatibility (2009–2012)

MariaDB was created in 2009 by Michael "Monty" Widenius and other original developers of MySQL, following Oracle Corporation's declaration of an acquisition of Sun Microsystems, which had owned MySQL since 2008. Concerned that Oracle would restrict MySQL's open-source development, Widenius and co-developers forked the codebase to ensure it remained freely available under the GNU General Public License.

The first release, MariaDB 5.1.38, was published on 29 October 2009. Following Oracle's acquisition, large numbers of the MySQL engineering team left Oracle and joined the MariaDB project through Widenius's company Monty Program Ab. The company used the Hacking Business Model and was thus co-owned by all the employees.

Early versions used version numbers that mirrored MySQL — 5.1, 5.2, 5.3, and 5.5 — to signal drop-in compatibility. MariaDB published 5.2 and 5.3 releases that MySQL itself skipped. The primary focus of this period was on improving the optimizer and storage engines: the Aria engine was developed as a crash-safe replacement for MyISAM, and additional engines including FederatedX, OQGraph, and PBXT were introduced or improved.

The Wikimedia Foundation migrated Wikipedia's databases to MariaDB in 2013. Google and Mozilla were also prominent first users. The first major distribution to ship MariaDB as the default database was openSUSE 12.3 (2013), followed by Fedora 19 later that year.

### Independent development (2012–present)

In 2012, the developers announced that MariaDB would move to a new 10.y.x version series, explicitly signalling that the project was developing independently rather than tracking MySQL releases.

The MariaDB 10.y.x series, beginning with 10.0 in 2014, established several capabilities that distinguished MariaDB from MySQL, including synchronous multi-master clustering through Galera Cluster and an Oracle compatibility mode enabling PL/SQL stored procedure syntax. The first long-term support (LTS) release was 10.6 in 2021.

The MariaDB 11.y.x series began in 2022, with its most significant development being native vector search capabilities introduced in 2024, enabling AI-oriented workloads without requiring a separate extension. These became generally available in the 11.8 LTS release in May 2025.

The MariaDB 12.y.x series began with MariaDB 12.0 in August 2025, introducing a rolling release track alongside the established LTS model. The series has seen a growing number of outside contributors; the May 2026 releases received contributions from 57 external (non MariaDB plc) contributors.

MariaDB 13.0 was released as a preview rolling release in March 2026, with themes including expanded procedural SQL, engine and performance improvements, and enhanced observability. The release incorporated a notable number of community-contributed pull requests.

MariaDB's roadmap is collaboratively shaped by MariaDB plc and community input. Contributors can propose features or file items directly in the project's JIRA issue tracker.

## Technical features

### MySQL compatibility

The two main features that distinguish MariaDB and MySQL from PostgreSQL are the usage of threads instead of processes, and integrated, wide support for replication setups, both local and global. This includes geo-distributed replication and multi-master setups via Galera Cluster.

MariaDB's API and protocol are compatible with those used by MySQL, including support for native non-blocking operations and progress reporting. Most connectors, libraries, and applications built for MySQL work with MariaDB. The official MariaDB connectors are licensed under the LGPL, permitting use in commercial applications without copyleft requirements, and are widely used by OS distributions to connect to both MariaDB and MySQL.

The on-disk format of MySQL and MariaDB were identical up to MySQL 5.7. MySQL 8.0 changed the on-disk format, including removing the `.frm` schema files, changing the default authentication protocol, and removing and changing several other features, meaning that moving data between MySQL 8.0+ and MariaDB requires a dump and restore. All main user-visible features largely share the same syntax, making it relatively straightforward to migrate from MySQL to MariaDB. Replication between MySQL and MariaDB in both directions remains possible.

Some features diverge further, including GTID replication format and JSON storage implementation.

MariaDB includes a built-in thread pool in all editions, including the community release, managing connections through a small pool of worker threads rather than a one-thread-per-connection model. MySQL's thread pool is available only in the commercial MySQL Enterprise Edition.

### Oracle compatibility

Oracle compatibility mode (`sql_mode=ORACLE`), available since MariaDB 10.3. The mode is designed to support incremental migration from Oracle Database, allowing applications to be ported on a per-feature or per-application basis rather than requiring a complete rewrite. Oracle mode enables PL/SQL stored procedure syntax, Oracle-compatible `NULL` handling, and Oracle-style functions including `NVL()` and `DECODE()`. In many cases, Oracle applications can be run unchanged with MariaDB by replacing Oracle's ODBC or JDBC connector with the MariaDB connector. Oracle mode was originally developed in collaboration with DBS Bank.

Sequences, created with `CREATE SEQUENCE`, are first-class database objects independent of any specific table, supporting descending sequences and fine-grained caching control; MySQL has no equivalent `CREATE SEQUENCE` statement.

### Transactions and concurrency

MariaDB provides fully ACID-compliant transactions with support for multiple isolation levels: read uncommitted, read committed, repeatable read, and serialisable. The default storage engine, InnoDB, implements multiversion concurrency control (MVCC), allowing readers and writers to operate concurrently without blocking each other. From MariaDB 11.8, snapshot isolation defaults to strict mode, ensuring transactions see a consistent view of the database from their start time.

### Storage engines

MariaDB supports a pluggable storage engine architecture, allowing different engines to be selected per table to match workload requirements — a broader range than the InnoDB-focused default of MySQL.

- InnoDB — the default engine, providing ACID-compliant transactions, row-level locking, foreign key support, and crash recovery.
- Aria — a crash-safe engine used internally for temporary tables and system tables, with crash recovery through a write-ahead transaction log.
- MyRocks — based on RocksDB, a log-structured merge-tree engine developed by Meta, offering higher write throughput and better compression for write-heavy workloads.
- Heap/Memory — an in-memory storage engine for fast temporary data storage; data is lost on server restart.
- Spider — a sharding engine that distributes data across multiple MariaDB instances, allowing them to be queried transparently as a single table; supports partitioning and XA transactions.
- CONNECT — allows MariaDB to query external data sources including CSV, ODBC, JDBC, MongoDB, and other formats as standard SQL tables.
- DuckDB — a pluggable storage engine that brings DuckDB's columnar analytical engine inside MariaDB Server.

### Pluggable architecture

Beyond storage engines, MariaDB has a set of pluggable APIs. Plugin categories include:

- Authentication methods
- Full-text search — including Mroonga for CJK languages
- Audit — logging database activity for security and compliance
- Encryption key management — including integration with HashiCorp Vault and AWS Key Management
- Monitoring and statistical plugins
- Password validation
- Handler socket — a high-speed API for using InnoDB tables as a key–value store
- Compression methods — bzip2, lz4, lzma, lzo, and snappy
- Pluggable data types — including inet, json, uuid, and mysql_json
- User-defined functions — loadable in C, C++, or Rust. Both simple and group-by functions are supported.

Plugins can be loaded or replaced at runtime without rebuilding the server.

### Analytics

MariaDB supports analytical workloads through ColumnStore, a columnar storage engine that stores data by column rather than by row, reducing I/O for aggregation queries and making it suited to data warehouse and business intelligence use cases. Standard SQL analytical capabilities including window functions and common table expressions are supported across all storage engines. The MariaDB Enterprise edition from MariaDB plc can use Exasol to speed up analytical queries.

### SQL language

MariaDB supports standard SQL including stored procedures, functions, triggers, views, window functions, and the `JSON` data type with a comprehensive set of document storage and querying functions.

System-versioned tables, conforming to the SQL:2011 standard, automatically record the complete history of every row. Historical data can be queried using the `FOR SYSTEM_TIME AS OF` clause to retrieve the state of a table at any past point in time, without manually maintained audit tables or triggers.

The `INSTANT` algorithm for `ALTER TABLE` allows column additions, drops, and default changes to complete in microseconds by updating only metadata, without rebuilding the table. Since MariaDB 11.2, non-instant schema changes run non-blocking by default, allowing concurrent reads and writes during the operation.

### Replication and high availability

MariaDB supports primary-replica replication using a binary log, with asynchronous and semi-synchronous modes. Multi-source replication allows a replica to receive changes from multiple primary servers simultaneously, and parallel replication reduces lag by applying changes concurrently.

Galera Cluster is a synchronous multi-master replication solution built directly into the MariaDB server, allowing writes to any node while maintaining consistency across the cluster.

### Security

MariaDB supports role-based access control, allowing sets of privileges to be assigned to named roles and granted to users, simplifying permission management in large deployments.

Authentication is handled through a plugin architecture supporting multiple methods, including `mysql_native_password`, ED25519 using elliptic-curve cryptography, and PARSEC (Password Authentication using Response Signed with Elliptic Curve), introduced in MariaDB 11.6. MariaDB supports table-level encryption and integration with HashiCorp Vault for key management.

### Connectivity

MariaDB provides official connectors for C, C++, Java, Python, Node.js, ODBC, and R2DBC, licensed under the LGPL, permitting use in commercial applications without copyleft requirements. MariaDB uses the MySQL client–server protocol, maintaining wire-level compatibility with MySQL client libraries.

MariaDB 11.7 introduced a native `VECTOR` data type with HNSW indexing for nearest neighbour search, enabling vector database workloads including retrieval-augmented generation (RAG) without requiring a separate extension or plugin. The implementation uses SIMD hardware acceleration (AVX2 and AVX512 on x86; NEON on ARM) and became generally available in MariaDB 11.8 LTS in May 2025. MariaDB Vector is integrated with major AI application frameworks including LangChain, LlamaIndex, Spring AI, and LangChain4j. MySQL Community Edition has supported the `VECTOR` data type since MySQL 9.0 but not vector search indexes.

## Licensing

The MariaDB Foundation mentions that "MariaDB Server will remain Free and Open Source Software licensed under GPLv2, independent of any commercial entities."

## Versioning

MariaDB version numbers follow MySQL's numbering scheme up to version 5.5. Thus, MariaDB 5.5 offers all of the MySQL 5.5 features. There exists a gap in MySQL versions between 5.1 and 5.5, while MariaDB issued 5.2 and 5.3 point releases.

Since specific new features have been developed in MariaDB, the developers decided that a major version number change was necessary.

| Version | Original release date | Latest version | Release date | Status | End of Life |
|---|---|---|---|---|---|
| Unsupported: 5.1 LTS | 29 October 2009 (2009-10-29) | 5.1.67 | 2013-01-30 | Stable (GA) | Unsupported: Feb 2015 |
| Unsupported: 5.2 LTS | 10 April 2010 (2010-04-10) | 5.2.14 | 2013-01-30 | Stable (GA) | Unsupported: Nov 2015 |
| Unsupported: 5.3 LTS | 26 July 2011 (2011-07-26) | 5.3.12 | 2013-01-30 | Stable (GA) | Unsupported: Mar 2017 |
| Unsupported: 5.5 LTS | 25 February 2012 (2012-02-25) | 5.5.68 | 2020-05-12 | Stable (GA) | Unsupported: Apr 2020 |
| Unsupported: 10.0 LTS | 12 November 2012 (2012-11-12) | 10.0.38 | 2019-01-31 | Stable (GA) | Unsupported: Mar 2019 |
| Unsupported: 10.1 LTS | 30 June 2014 (2014-06-30) | 10.1.48 | 2020-11-04 | Stable (GA) | Unsupported: Oct 2020 |
| Unsupported: 10.2 LTS | 18 April 2016 (2016-04-18) | 10.2.44 | 2022-05-21 | Stable (GA) | Unsupported: May 2022 |
| Unsupported: 10.3 LTS | 16 April 2017 (2017-04-16) | 10.3.39 | 2023-05-10 | Stable (GA) | Unsupported: May 2023 |
| Unsupported: 10.4 LTS | 9 November 2018 (2018-11-09) | 10.4.34 | 2024-05-17 | Stable (GA) | Unsupported: Jun 2024 |
| Unsupported: 10.5 LTS | 3 December 2019 (2019-12-03) | 10.5.29 | 2025-05-08 | Stable (GA) | Unsupported: Jun 2025 |
| Supported: 10.6 LTS | 26 April 2021 (2021-04-26) | 10.6.27 | 2026-05-28 | Stable (GA) | Supported: Jul 2026 |
| Unsupported: 10.7 | 17 September 2021 (2021-09-17) | 10.7.8 | 2023-02-06 | Stable (GA) | Unsupported: Feb 2023 |
| Unsupported: 10.8 | 22 December 2021 (2021-12-22) | 10.8.8 | 2023-05-10 | Stable (GA) | Unsupported: May 2023 |
| Unsupported: 10.9 | 23 March 2022 (2022-03-23) | 10.9.8 | 2023-08-14 | Stable (GA) | Unsupported: Aug 2023 |
| Unsupported: 10.10 | 23 June 2022 (2022-06-23) | 10.10.7 | 2023-11-14 | Stable (GA) | Unsupported: Nov 2023 |
| Supported: 10.11 LTS | 26 September 2022 (2022-09-26) | 10.11.18 | 2026-05-28 | Stable (GA) | Supported: Feb 2028 |
| Unsupported: 11.0 | 27 December 2022 (2022-12-27) | 11.0.6 | 2024-05-17 | Stable (GA) | Unsupported: Jun 2024 |
| Unsupported: 11.1 | 27 March 2023 (2023-03-27) | 11.1.6 | 2024-08-14 | Stable (GA) | Unsupported: Aug 2024 |
| Unsupported: 11.2 | 20 June 2023 (2023-06-20) | 11.2.6 | 2024-11-04 | Stable (GA) | Unsupported: Nov 2024 |
| Supported: 11.4 LTS | 24 December 2023 (2023-12-24) | 11.4.12 | 2026-05-29 | Stable (GA) | Supported: May 2029 |
| Supported: 11.8 LTS | 18 December 2024 (2024-12-18) | 11.8.8 | 2026-05-29 | Stable (GA) | Supported: June 2028 |
| Latest version: 12.3 LTS | 22 December 2025 (2025-12-22) | 12.3.2 | 2026-05-29 | Stable (GA) | Latest version: Q2 2029 |
| Future version: Rolling | 7 August 2025 (2025-08-07) | 13.0.1 | 2026-05-29 | Release Candidate (RC) | Future version: Q3 2026 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version **LTS** = *Long-Term Support* (every Q2 of the year) **RR** = *Rolling Release* (every three months) |   |   |   |   |   |

## MariaDB Foundation

The MariaDB Foundation is a non-profit organisation founded in December 2012 to oversee and safeguard the open-source development of the MariaDB database server, independently of any commercial entity. The Foundation is incorporated in Delaware, USA, and is funded through corporate and individual sponsorships, with MariaDB plc being the primary code contributor. Its work is guided by three core principles: openness of the codebase to contributions based on technical merit, increasing adoption of MariaDB across users and platforms, and ensuring long-term continuity of the project independently of commercial interests.

### History of MariaDB Foundation

#### Founding and early governance challenges (2012–2014)

In December 2012, MySQL Ab founders Michael Widenius, David Axmark, and Allan Larsson announced the formation of the MariaDB Foundation to oversee the development of MariaDB, which had been forked in 2009 from MySQL.

At the time of founding, the Foundation aimed to establish a governance model similar to that of the Eclipse Foundation, and appointed the Eclipse Foundation's Executive Director Mike Milinkovich as an advisor to lead the transition.

Simon Phipps became the Foundation's first CEO in April 2013 but resigned in 2014 when the MariaDB trademark was transferred to SkySQL (later renamed MariaDB Corporation Ab). He later said: "I quit as soon as it was obvious the company was not going to allow an independent foundation."

The Foundation's first formal sponsor was MariaDB plc (then known as MariaDB Corporation Ab), which joined in 2014 after initial agreements on the division of roles between the Foundation and the Corporation. The MariaDB trademark is owned by MariaDB plc and used under licence by the Foundation. In 2013, Google tasked one of its engineers to work at the Foundation, reflecting early industry support for the project.

#### Establishment (2015–2021)

Otto Kekäläinen served as CEO from January 2015 to September 2018. Eric Herman, a developer at Booking.com and former MySQL and Sun employee, joined the Foundation board in May 2015 and was elected Chair in November 2016. Arjen Lentz was briefly appointed CEO in October 2018 before leaving in December 2018. Kaj Arnö joined as CEO on 1 February 2019.

In October 2020, the Foundation began publishing its board meeting minutes openly by default. In December 2021, the board declined to create a Diamond Sponsorship tier that would have granted MariaDB Corporation the right to block other sponsors, affirming the Foundation's operational independence from its primary commercial supporter.

#### Organisational maturation (2022–present)

A significant change in the MariaDB ecosystem came in December 2022, when MariaDB plc listed on the New York Stock Exchange. In 2024 K1 Investment Management completed an acquisition of the company taking it private.

At the time, the Foundation strengthened its own governance: in November 2023, the board formalised safeguards including limiting any single corporation to one direct board seat and requiring a supermajority vote for changes to the Foundation's mission. Arnö later reflected that the preceding years had been challenging for the Foundation's relationship with MariaDB plc, and that the arrival of new management had restored positive dynamics. Following the change of ownership, the Foundation and MariaDB plc began rebuilding their working relationship, conducting shared strategy sessions around cooperation and openness.

Kaj Arnö served as CEO until February 2025, when he was elected Chairman of the Board and became Executive Chairman, succeeding Eric Herman, who had served as Chair since November 2016. Anna Widenius was confirmed as CEO at the same time. The Foundation also signed a Memorandum of Understanding with MariaDB plc in 2025, formally recognising it as the Primary Code Contributor for 2022–2024.

### Purpose and activities

The Foundation states that its staff contribute to MariaDB Server through feature design, code review, documentation, and porting and packaging across platforms, and that it works to assist new contributors to the project. It promotes MariaDB at conferences and through community engagement.

The Foundation publishes board meeting minutes and financial reports. Technical decisions are made by contributors through open mailing list discussions, with the board responsible for organisational strategy.

The Foundation organises a range of community events. MariaDB Server Fest is a recurring developer-focused event series held in multiple cities across Europe, Asia and the Americas, sometimes co-located with major open-source events such as FOSDEM in Brussels, Belgium.

### Sponsors and members

The Foundation organises its sponsors into tiers. Diamond sponsors include Amazon and DBS; Platinum sponsors include IBM, Intel, and MariaDB plc; and Gold sponsors include more than 30 organisations, among them Hetzner, IONOS, Automattic, and Nextcloud.

In addition to financial sponsorship, some sponsors contribute directly to the codebase. Amazon has become one of the largest code-contributing corporations outside MariaDB plc, including contributions to MariaDB Vector.

## MariaDB plc

MariaDB plc (formerly MariaDB Corporation Ab) is a database software company and the primary contributor to the MariaDB database server. It develops the MariaDB Enterprise Platform, database connectors, and MariaDB Cloud, a cloud database service. The company is headquartered in Silicon Valley and Dublin, Ireland, and has been privately owned by private equity firm K1 Investment Management since September 2024.

### History of MariaDB plc

#### Founding and mergers (2010–2014)

The company was founded in 2010 as SkySQL Corporation Ab by Patrik Backman, Ralf Wahlsten, Kaj Arnö, Max Mether, Ulf Sandberg, Mick Carney, and Michael "Monty" Widenius. It merged with Monty Program Ab on 23 April 2013. On 1 October 2014 the combined entity was renamed MariaDB Corporation Ab to reflect its role as the main driving force behind the development of MariaDB Server.

MariaDB Corporation was funded with a combined total of approximately $123M across A-series (2012), B-series (2013–2016), and C-series (2017–2022) funding rounds. A-series investors included OpenOcean and Tesi (Finnish Industry Investment Ltd). The B-series was led by Intel, which invested $20M in 2013. In January 2016, Michael Howard was named CEO, with Michael Widenius continuing as CTO. The C-series was led by Alibaba with a $27M investment in 2017, alongside a €25M loan by the European Investment Bank.

In March 2020, MariaDB Corporation launched SkySQL, a database-as-a-service (DBaaS) built on the MariaDB Enterprise Platform and hosted on Google Cloud Platform. The offering combined transactional and analytical workloads—including distributed SQL and columnar storage—in a single managed cloud service, distinguishing it from competing hosted offerings such as Amazon RDS and Microsoft Azure's MariaDB service.

#### NYSE listing and restructuring (2022–2024)

In February 2022 the company announced its intention to list on the New York Stock Exchange (NYSE) via a merger with a special-purpose acquisition company, completing the listing in December 2022 under the ticker symbol MRDB and adopting the name MariaDB plc, alongside a D-series fundraising round targeting $104M. The share price declined sharply in the years that followed. In October 2023, the company restructured, discontinuing its SkySQL cloud database service and laying off staff. SkySQL was spun off as an independent company in December 2023.

#### K1 ownership (2024–present)

In September 2024, K1 Investment Management completed a tender offer for all outstanding shares for approximately $37 million, taking the company private and appointing Rohit de Souza as CEO. The new management subsequently worked to rebuild the company's relationship with the open-source community, including the MariaDB Foundation. In August 2025, MariaDB plc reacquired SkySQL.

### Acquisitions of MariaDB plc

- March 2018 — MammothDB, a Bulgarian analytics database company, whose technology was integrated into the MariaDB AX analytics offering.
- September 2018 — Clustrix, a distributed database company whose technology became MariaDB Xpand, a distributed SQL storage engine for horizontal scalability.
- May 2025 — Codership Oy, the Finnish company behind Galera Cluster, the synchronous multi-master replication technology built into MariaDB Server. The acquisition brought the Galera development team under MariaDB plc.
- August 2025 — SkySQL, the cloud database service originally spun off from MariaDB in December 2023, was reacquired to restore managed cloud offerings under a single vendor.
- March 2026 — GridGain, the original developer of Apache Ignite and provider of an in-memory computing platform, acquired to enable sub-millisecond data access for AI and real-time analytical workloads, offering a SQL-integrated alternative to standalone caches such as Redis.

### Products of MariaDB plc

MariaDB plc contributes to MariaDB Server and develops the MariaDB database connectors (C, C++, Java, Node.js, ODBC, Python, R2DBC) licensed under the LGPL, allowing use in commercial applications without the copyleft requirements of MySQL's GPL connectors.

As of June 2026, MariaDB lists its Enterprise Platform products as including:

- MariaDB Enterprise Server — an enhanced version of the community server supporting transactional, analytical, and vector workloads.
- MariaDB MaxScale — a database proxy providing high availability, scalability, and security.
- MariaDB Enterprise Cluster — an active-active replication solution for high availability and automated failover using Galera Cluster.
- MariaDB Enterprise Kubernetes Operator — automates MariaDB deployment management in Kubernetes environments.
- MariaDB Enterprise Manager — a monitoring and management tool with centralised topology views and metric exports.
- MariaDB Exa — an integration with a columnar massively parallel processing analytics engine for high-performance analytics on live transactional data.
- MariaDB AI RAG — a retrieval-augmented generation service enabling AI-generated answers grounded in the user's own data.
- MariaDB MCP Server — connects MariaDB databases to generative AI tools via the Model Context Protocol for semantic search and database operations.
- In-Memory Cache, powered by GridGain — an in-memory computing layer built on Apache Ignite for sub-millisecond latency data access.
- MariaDB Cloud — a fully managed database-as-a-service with provisioned and serverless deployment options.

### Notable customers of MariaDB plc

- DBS Bank, a large bank in Southeast Asia — uses MariaDB for payment services and commercial banking operations, with over 30 applications in production since 2017.
- Nokia — uses MariaDB in containerised database deployments at Nokia Networks.
- Virgin Media O2 — uses MariaDB for cloud database services.
- Samsung SDS — migrated from Oracle Database to MariaDB.

## Notable users

### Organisations

- Google — internal databases.
- Wikimedia Foundation — databases powering Wikipedia and other Wikimedia projects, since 2013.
- ServiceNow — enterprise IT service platform handling over 25 billion database queries per hour.
- Mozilla — internal databases.
- DBS Bank — payment services and commercial banking operations, with over 30 applications in production since 2017.

### Operating systems and distributions

MariaDB is the default database in many of the major Linux distributions and several BSD operating systems, having replaced MySQL as distributions adopted it through the 2010s. These include Mageia (from Mageia 2 in 2012), Arch Linux (from 2013), Fedora (from Fedora 19 in 2013), openSUSE (from openSUSE 12.3 Dartmouth in 2013), Slackware Linux (from Slackware 14.1 in 2013), CentOS (from CentOS 7 in 2014), Manjaro (from 0.8.11 in 2014), Red Hat Enterprise Linux (from RHEL 7 in June 2014), SUSE Linux Enterprise Server (from SLES 12 in 2014), OpenBSD (from OpenBSD 5.7 in 2015), and Debian (from Debian 9 in 2017). Beyond Linux and BSD, the OpenSolaris-derived OpenIndiana has used MariaDB as its default MySQL provider since 2013.

### Open-source projects

As of September 2025, MariaDB is used by more WordPress installations than MySQL, accounting for 54% of WordPress database deployments according to official WordPress statistics. Drupal lists MariaDB as its recommended database for Drupal 10, 11, and 12 in its official documentation. Nextcloud recommends MariaDB over MySQL in its official administration manual.

## Service implementations

Some notable vendors offer MariaDB as a managed cloud database service:

- Amazon Relational Database Service (RDS) — managed MariaDB on Amazon Web Services.
- MariaDB Cloud — the official Database-as-a-Service from MariaDB plc, with provisioned and serverless deployment options.
- TencentDB for MariaDB — managed MariaDB on Tencent Cloud.
- Ionos — managed MariaDB on the Ionos cloud; also bundled as the default database in Ionos web hosting packages.
- Kinsta — managed WordPress hosting running MariaDB.
- INGATE — managed MariaDB hosted in Germany.
- Hetzner — managed servers include MariaDB as the default database server.
- Railway — developer cloud platform offering one-click MariaDB deployment.
