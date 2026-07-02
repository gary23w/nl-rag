---
title: "Understanding Snowflake Table Structures"
source: https://docs.snowflake.com/en/user-guide/tables-micro-partitions
domain: snowflake
license: CC-BY-SA-4.0
tags: snowflake data cloud, cloud data warehouse, micro-partition, columnar storage
fetched: 2026-07-02
---

# Understanding Snowflake Table Structures

All data in Snowflake is stored in database tables, logically structured as collections of columns and rows. To best utilize Snowflake tables, particularly large tables, it is helpful to have an understanding of the physical structure behind the logical structure.

These topics describe *micro-partitions* and *data clustering*, two of the principal concepts utilized in Snowflake physical table structures. They also provide guidance for explicitly defining *clustering keys* for very large tables (in the multi-terabyte range) to help optimize table maintenance and query performance.

**Next Topics:**

- Micro-partitions & Data Clustering
- Clustering Keys & Clustered Tables
- Automatic Clustering
- Manual Reclustering — Deprecated
