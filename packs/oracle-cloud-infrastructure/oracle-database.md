---
title: "Oracle Database"
source: https://en.wikipedia.org/wiki/Oracle_Database
domain: oracle-cloud-infrastructure
license: CC-BY-SA-4.0
tags: oracle cloud infrastructure, oci compute, oracle cloud database, enterprise cloud oracle
fetched: 2026-07-02
---

# Oracle Database

**Oracle Database** (marketed since 2025 as **Oracle AI Database**, and also referred to as **Oracle DBMS** or simply **Oracle**) is a proprietary relational database management system (RDBMS) developed and marketed by Oracle Corporation. First released in 1979, it was among the earliest commercially available databases to use SQL, and as of 2026 it is ranked as the most popular database management system in the DB-Engines ranking.

It is commonly used for online transaction processing (OLTP), data warehousing (DW), and mixed database workloads. As a converged database, it supports multiple data models within a single engine, including relational, JSON document, XML, spatial, graph, text, and vector data, all queryable through SQL.

Oracle Database runs on-premises, on Oracle engineered systems such as Oracle Exadata, on Oracle Cloud Infrastructure, and as a managed Autonomous Database service. It is also offered inside Microsoft Azure, Google Cloud, and Amazon Web Services data centers through Oracle's multicloud offerings. The current long-term release is Oracle AI Database 26ai, which was introduced in October 2025.

## History

Larry Ellison and his two friends and former co-workers, Bob Miner and Ed Oates, started a consultancy called Software Development Laboritories (SDL) in 1977, later Oracle Corporation. SDL developed the original version of the Oracle software. The name *Oracle* comes from the code-name of a Central Intelligence Agency-funded project Ellison has worked on while formerly employed by Ampex; the CIA was Oracle's first customer, and allowed the company to use the code name for the new product.

Ellison wanted his database to be compatible with IBM System R, but that company's Don Chamberlin declined to release its error codes. By 1985 Oracle advertised, however, that "Programs written for SQL/DS or DB2 will run unmodified" on the many non-IBM mainframes, minicomputers, and microcomputers its database supported "Because all versions of ORACLE *are* identical".

### Growth and the internet era

Oracle Corporation held its initial public offering on March 12, 1986. The company grew rapidly during the 1980s, though a financial setback in 1990 led to its first quarterly loss and significant layoffs before the business recovered. Oracle7, released in 1992, matured the product into a leading enterprise relational database management system, adding persistent PL/SQL stored procedures and triggers, a cost-based query optimizer, and improved administration tools.

### Clustering, grid, and cloud computing

Oracle Database 12c (2013) introduced the multitenant architecture and the In-Memory Column Store, with "c" denoting "cloud". In 2017 Oracle announced Oracle Autonomous Database, a self-managing cloud service, with the first services becoming available in 2018. Beyond the on-premises editions, Oracle Autonomous Database automates provisioning, tuning, patching, and scaling and is offered in data-warehousing and transaction-processing variants.

## Releases and versions

Oracle products follow a custom release-numbering and -naming convention. The "ai" in the current release, Oracle AI Database 26ai, stands for "Artificial Intelligence". Previous releases (e.g. Oracle Database 19c, 10g, and Oracle9i Database) have used suffixes of "c", "g", and "i" which stand for "Cloud", "Grid", and "Internet" respectively. Prior to the release of Oracle8i Database, no suffixes featured in Oracle AI Database naming conventions. There was no v1 of Oracle AI Database, as Ellison "knew no one would want to buy version 1". For some database releases, Oracle also provides an Express Edition (XE) that is free to use.

Oracle AI Database release numbering has used the following codes:

| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version **LTR** = *Long-Term Release*, **IR** = *Innovation Release* |   |   |   |   |
|---|---|---|---|---|
| Oracle Database Version | Initial Release Version | Initial Release Date | Terminal Version | Marquee Features |
| Latest version: Oracle AI Database 26ai (LTR) | 23.26.0 | Starting with Release Update 23.26.0, released in October 2025, Oracle Database 23ai is replaced by Oracle AI Database 26ai. Applying Release Update 23.26.0 to an existing Oracle Database 23ai deployment converts it to Oracle AI Database 26ai without requiring a separate database upgrade or application re-certification |   | AI is natively architected into Oracle AI Database and SQL; unifies all major data models and workloads in a single converged engine; Model Context Protocol (MCP) Server support; Oracle Unified Memory Core for agent context across multiple data types; AI Semantic Models; unified relational, JSON, and graph data model; Private Agent Factory and Select AI Agent; Oracle Vectors on Ice for Apache Iceberg tables; Autonomous AI Lakehouse; Deep Data Security; Private AI Services Container |
| Supported: Oracle Database 23ai (LTR) | 23.4.0 | From Release Update 23.26.0 onward, 23ai is replaced by Oracle AI Database 26ai On May 2, 2024, Oracle Database 23ai was released on Oracle Cloud Infrastructure (OCI) as cloud services, including OCI Exadata Database Service, OCI Exadata Database Cloud@Customer, and OCI Base Database Service. It is also available in Always Free Autonomous Database. Oracle Database 23c (previously released in 2023) was renamed to Oracle Database 23ai (23.4) due to the significant additional engineering effort to add features that bring AI capabilities to the data in Oracle AI Database. Oracle Database 23c (23.2 and 23.3) was released in 2023: April 2023 (Linux) Oracle Database Free - Developer Release September 2023 Oracle AI Database on Base Database Service |   | AI Vector Search (includes new Vector data type, Vector indexes, and Vector SQL operators/functions), JSON Relational Duality, JSON Schema Validation, Transactional Microservices Support, OKafka, Operational Property Graphs, Support for SQL/PGQ, Schema Privileges, Developer Role, In-database SQL Firewall, TLS 1.3 Support, Integration with Azure Active Directory OAuth2, True Cache for mid-tier caching, Readable Per-PDB Standby, Globally Distributed Database with active-active RAFT-based replication, Real-time SQL Plan Management, Priority Transactions, SQL Syntax Simplification, Schema Annotations, Data Use Case Domains, Column Value Lock-free Reservations |
| Supported: Oracle Database 21c (IR) | 21.1.0 | December 2020 (cloud) August 2021 (Linux) |   | Blockchain Tables, Multilingual Engine - JavaScript Execution in the Database, Binary JSON Data Type, Per-PDB Data Guard Physical Standby (aka Multitenant Data Guard), Per-PDB GoldenGate Change Capture, Self-Managing In-Memory, In-Memory Hybrid Columnar Scan, In-Memory Vector Joins with SIMD, Sharding Advisor Tool, Property Graph Visualization Studio, Automatic Materialized Views, Automatic Zone Maps, SQL Macros, Gradual Password Rollover |
| Supported: Oracle Database 19c (LTR) | 19.1.0 // 12.2.0.3 | February 2019 (Exadata) April 2019 (Linux) June 2019 (cloud) |   | Active Data Guard DML Redirection, Automatic Index Creation, Real-Time Statistics Maintenance, SQL Queries on Object Stores, In-Memory for IoT Data Streams, Hybrid Partitioned Tables, Automatic SQL Plan Management, SQL Quarantine, Zero-Downtime Grid Infrastructure Patching, Finer-Granularity Supplemental Logging, Automated PDB Relocation |
| Unsupported: Oracle Database 18c (IR) | 18.1.0 // 12.2.0.2 | February 2018 (cloud, Exadata) July 2018 (other) | 18.17.0 January 2022 | Polymorphic Table Functions, Active Directory Integration, Transparent Application Continuity, Approximate Top-N Query Processing, PDB Snapshot Carousel, Online Merging of Partitions and Subpartitions |
| Unsupported: Oracle Database 12*c* Release 2 | 12.2.0.1 March 2017 | August 2016 (cloud) March 2017 (on-premises) | 12.2.0.1 March 2017 | Native Sharding, Zero Data Loss Recovery Appliance, Exadata Cloud Service, Cloud at Customer |
| Unsupported: Oracle Database 12*c* Release 1 | 12.1.0.1 | July 2013 | 12.1.0.2 July 2014 | Multitenant architecture, In-Memory Column Store, Native JSON, SQL Pattern Matching, Database Cloud Service |
| Unsupported: Oracle Database 11*g* Release 2 | 11.2.0.1 | September 2009 | 11.2.0.4 August 2013 | Edition-Based Redefinition, Data Redaction, Hybrid Columnar Compression, Cluster File System, Golden Gate Replication, Database Appliance |
| Unsupported: Oracle Database 11*g* Release 1 | 11.1.0.6 | September 2007 | 11.1.0.7 September 2008 | Active Data Guard, Secure Files, Exadata |
| Unsupported: Oracle Database 10*g* Release 2 | 10.2.0.1 | July 2005 | 10.2.0.5 April 2010 | Real Application Testing, Database Vault, Online Indexing, Advanced Compression, Data Guard Fast-Start Failover, Transparent Data Encryption |
| Unsupported: Oracle Database 10*g* Release 1 | 10.1.0.2 | 2003 | 10.1.0.5 February 2006 | Automated Database Management, Automatic Database Diagnostic Monitor, Grid infrastructure, Oracle ASM, Flashback Database |
| Unsupported: Oracle9*i* Database Release 2 | 9.2.0.1 | 2002 | 9.2.0.8 April 2007 | Advanced Queuing, Data Mining, Streams, Logical Standby |
| Unsupported: Oracle9*i* Database | 9.0.1.0 | 2001 | 9.0.1.5 December 2003 | Oracle Real Application Clusters (RAC), Oracle XML DB |
| Unsupported: Oracle8*i* Database | 8.1.5.0 | 1998 | 8.1.7.4 August 2000 | Native internet protocols and Java, Virtual Private Database |
| Unsupported: Oracle8 Database | 8.0.3 | June 1997 | 8.0.6 | Recovery Manager, Partitioning. First version available for Linux. |
| Unsupported: Oracle 7.3 | 7.3.0 | February 1996 | 7.3.4 | Object-relational database |
| Unsupported: Oracle 7.2 | 7.2.0 | May 1995 |   | Shared Server, XA Transactions, Transparent Application Failover |
| Unsupported: Oracle 7.1 | 7.1.0 | May 1994 |   | Parallel SQL Execution. First version available for Windows NT. |
| Unsupported: Oracle7 | 7.0.12 | June 1992 |   | Distributed 2-phase commit, PL/SQL stored procedures, triggers, shared cursors, cost-based optimizer |
| Unsupported: Oracle 6.2 | 6.2.0 |   |   | Oracle Parallel Server |
| Unsupported: Oracle v6 | 6.0.17 | 1988 | 6.0.37 | Row-level locking, SMP scalability / performance, storing of undo in database, online backup and recovery, B*Tree indexes, PL/SQL executed from compiled programs (C etc.). First version available for Novell Netware 386. |
| Unsupported: Oracle v5 | 5.0.22 (5.1.17) | 1985 | 5.1.22 | C2 security certification. Support for distributed database systems and client/server computing. First version available for OS/2. Correlated sub-queries. DOS version supports extended memory. |
| Unsupported: Oracle v4 | 4.1.4.0 | 1984 | 4.1.4.4 | Multiversion read consistency. Halloween Problem solved. Improved concurrency. First version available for MS-DOS and IBM mainframe. |
| Unsupported: Oracle v3 | 3.1.3 | 1983 |   | Concurrency control, data distribution, and scalability. Re-written in C for portability to other operating systems, including UNIX. |
| Unsupported: Oracle v2 | 2.3 | 1979 |   | First commercially available SQL RDBMS. Basic SQL queries, simple joins and `CONNECT BY` joins. Atomic role-level SQL statements. Rudimentary concurrency control and database integrity. No query optimizer. Written in assembly language for the PDP-11 to run in 128KB of RAM. Ran on PDP-11 and VAX/VMS in PDP-11 compatibility mode. |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version **LTR** = *Long-Term Release*, **IR** = *Innovation Release* |   |   |   |   |

The Introduction to Oracle AI Database includes a brief history on some of the key innovations introduced with each major release of Oracle AI Database.

See My Oracle Support (MOS) note *Release Schedule of Current Database Releases (Doc ID 742060.1)* for the current Oracle AI Database releases and their patching end dates.

## Patch updates and security alerts

Prior to Oracle Database 18c, Oracle Corporation released Critical Patch Updates (CPUs) and Security Patch Updates (SPUs) and Security Alerts to close security vulnerabilities. These releases are issued quarterly; some of these releases have updates issued prior to the next quarterly release.

Starting with Oracle Database 18c, Oracle Corporation releases Release Updates (RUs) and Release Update Revisions (RURs). RUs usually contain security, regression (bug), optimizer, and functional fixes which may include feature extensions as well. RURs include all fixes from their corresponding RU but only add new security and regression fixes. However, no new optimizer or functional fixes are included.
