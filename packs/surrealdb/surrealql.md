---
title: "SurrealQL"
source: https://surrealdb.com/docs/surrealql
domain: surrealdb
license: CC-BY-SA-4.0
tags: surrealdb, multi-model database, surrealql query language, document-graph database
fetched: 2026-07-02
---

# SurrealQL

SurrealQL is SurrealDB's query language. Syntax is broadly SQL-like, with extensions for nested fields, graph edges, record IDs, and other SurrealDB-specific constructs.

For a guided introduction, see Learn: Querying.

## Examples

A minimal query can follow a familiar SQL shape:

```
SELECT name,
       metadata
FROM   user
WHERE  age >= 18; 
```

Projections can include nested objects and graph traversals:

```
SELECT name,
       metadata.{
          date_registered,
          last_login
       },
       ->wrote->post AS posts
FROM user
WHERE age >= 18;
```

Further detail is organised under Statements and the other sections in this reference.
