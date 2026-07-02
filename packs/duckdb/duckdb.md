---
title: "DuckDB"
source: https://en.wikipedia.org/wiki/DuckDB
domain: duckdb
license: CC-BY-SA-4.0
tags: duckdb, embedded analytics, olap engine, apache parquet
fetched: 2026-07-02
---

# DuckDB

**DuckDB** is an open-source column-oriented Relational Database Management System (RDBMS). It is designed to provide high performance on complex queries against large databases in embedded configuration, such as combining tables with hundreds of columns and billions of rows. Unlike other embedded databases (for example, SQLite) DuckDB is not focusing on transactional (OLTP) applications and instead is specialized for online analytical processing (OLAP) workloads. The project has over 6 million downloads per month.

## History

DuckDB was originally developed by Mark Raasveldt and Hannes Mühleisen at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. The project co-founders designed DuckDB to address the need for an in-process OLAP database solution. DuckDB was first released in 2019. DuckDB version 1.0.0 was released on June 3, 2024, under the codename SnowDuck.

| Version | Codename | Release date | Key features |
|---|---|---|---|
| 1.0.0 | SnowDuck | June 3, 2024 | First stable production release; backward-compatible storage format guaranteed |
| 1.1.0 | Eatoni | September 9, 2024 | Parallel streaming of query results; improved foreign key index performance |
| 1.2.0 | Histrionicus | February 2025 | CSV reader rewrite; new C API for extensions; CLI autocomplete |
| 1.3.0 | Ossivalis | May 2025 | HyperLogLog adaptive hash table sizing; Parquet reader/writer rewrite |
| 1.4.0 | Andium | September 2025 | **LTS release**; AES-256 encryption; MERGE INTO; official Docker images |
| 1.5.0 | Variegata | March 9, 2026 | Built-in GEOMETRY type; VARIANT type; new CLI; Azure write support; DuckLake v0.4 |
| 1.5.1 | — | March 23, 2026 | Bug fixes: CLI non-interactive shell, ART index, Iceberg v3, S3 globbing |

## Features

DuckDB uses a vectorized query processing engine. DuckDB is special amongst database management systems because it does not have any external dependencies and can be built with just a C++17 compiler. DuckDB also deviates from the traditional client–server model by running inside a host process (it has bindings, for example, for a Python interpreter with the ability to directly place data into NumPy arrays). DuckDB's SQL parser is derived from the pg_query library developed by Lukas Fittl, which is itself derived from PostgreSQL's SQL parser that has been stripped down as much as possible. DuckDB uses a single-file storage format to store data on disk, designed to support efficient scans and bulk updates, appends and deletes. DuckDB is also compiled to WebAssembly using emscripten which enables DuckDB to run SQL in browser-based analytics tools.

## Comparison

DuckDB in its OLAP niche does not compete with the traditional DBMS like MSSQL, PostgreSQL and Oracle database. While using SQL for queries, DuckDB targets serverless applications and provides extremely fast responses using either Apache Parquet files or its own format for storage. These attributes make it a popular choice for large dataset analysis in interactive mode.

## Commercial use

DuckDB is used at Facebook, Google, and Airbnb.

DuckDB co-author Mühleisen also runs a support and consultancy firm for the software, DuckLabs. The company has chosen not to take venture capital funding, stating "We feel investment would force the project direction towards monetization, and we would much prefer keeping DuckDB open and available for as many people as possible". Another company, MotherDuck, has received $100 million funding for its data platform based on DuckDB, with investors including Andreessen Horowitz.

The company DuckLabs was formerly known as DuckDB Labs.

## DuckDB Foundation

The independent non-profit DuckDB Foundation safeguards the long-term maintenance and development of DuckDB. The foundation holds much of the intellectual property of the project and is funded by charitable donations. The DuckDB Foundation's statutes ensure DuckDB remains open-source under the MIT license in perpetuity.

## Language support

In addition to the native C and C++ APIs, DuckDB supports a range of programming languages.

| Language | Notes | Reference |
|---|---|---|
| Java | The Java API is implemented using JNI. Integration with the Apache Arrow format is provided. |   |
| Python | The Python API implements support for the Pandas, Apache Arrow and Polars data analysis packages. |   |
| Rust | The Rust API is distributed as a rust crate that exposes an elegant wrapper over the native C API. |   |
| Node.JS | Node API |   |
| R | R API |   |
| Julia | Julia API |   |
| Swift | Swift API |   |
| WebAssembly | WASM API |   |
| Go | Go API |   |

## Extensions

DuckDB's architecture supports extensions, allowing additional functionality to be added dynamically. Many popular extensions are maintained by the core DuckDB team, and there are over 30 community extensions maintained by third parties.

DuckDB's architecture supports dynamically loaded extensions. Core extensions maintained by the DuckDB team include:

- **httpfs** — remote file access via HTTP, HTTPS, and S3-compatible object storage (including Azure write support since v1.5)
- **spatial** — geospatial functions (ST_* family); GEOMETRY became a built-in core type in v1.5
- **iceberg** — Apache Iceberg table read/write, including REST catalog support
- **delta** — Delta Lake table read/write via the Delta Kernel
- **ducklake** — lakehouse format storing all metadata in a SQL database with ACID semantics; supports time travel, schema evolution, and multi-table transactions

There are also over 30 community extensions maintained by third parties, covering use cases from graph queries (SQL/PGQ) to Kafka integration and ML inference. A full list is available at the DuckDB Community Extensions registry.
