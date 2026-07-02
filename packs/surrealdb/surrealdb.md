---
title: "What is SurrealDB"
source: https://surrealdb.com/docs/surrealdb
domain: surrealdb
license: CC-BY-SA-4.0
tags: surrealdb, multi-model database, surrealql query language, document-graph database
fetched: 2026-07-02
---

# What is SurrealDB

SurrealDB is a multi-model database built in Rust designed to unify multiple data models into a single, powerful engine. It combines document, graph, time-series, relational, geospatial and key-value data types into one query language, SurrealQL, with powerful search and retrieval (vector, full-text, hybrid), and real-time and event-driven capabilities, enabling developers to build applications faster and more efficiently.

Sample SurrealQL query

```
SELECT
  ->purchased->product AS history,
  ->reviewed->product[WHERE
    vector::similarity::cosine(
      embedding, [0.1, 0.5, ...]
    ) > 0.8
  ] AS relevant,
  ->prefs[WHERE valid_at <= time::now()] AS prefs
FROM ONLY user:ic7c1frczl1tw552yl4u;
```

Common SurrealDB use cases include AI agents, knowledge graphs, real-time apps (e.g. recommendation engines, fraud detection systems), and any other type of application requiring multiple data types. SurrealDB can also be used as a backend-as-a-service (BaaS) thanks to its support for direct user authentication. Given that it’s a single Rust binary, SurrealDB can also run embedded (in‐app), in the browser (via WebAssembly), in the edge, as single backend node, or in a distributed cluster.

SurrealDB is source-available (see the code here on GitHub) and is also available as a cloud managed service through SurrealDB Cloud.

## Differentiators and advantages

- **Native multi-model:** combines document, graph, time-series, relational, geospatial and key-value data models natively into SurrealQL, without workarounds or added complexity.
- **AI native:** purpose-built for AI and context-aware applications with integrated search and retrieval (vector, full-text, hybrid) that blend semantic, graph, and relational intelligence.
- **Real-time and event-driven:** built-in real-time subscriptions, event triggers, and streaming updates power reactive, real-time experiences - no need for extra layers like Kafka.
- **Powerful developer experience:** SurrealQL is intuitive and combines the best ideas from SQL, NoSQL and graph within a single native syntax. Start schemaless and then make your schema as strictly defined as you like.
- **Rust-powered performance:** high efficiency, memory safety, type safety and concurrency with a single Rust binary.
- **Test and performance coverage:** Internal Rust testing and in-house Rust testing suite confirm thousands of database output assertions on each pull request, along with a crud-bench run to display performance results for each prospective change to the code.
- **Native ACID compliance:** snapshot isolation on every transaction, with immediate consistency after a commit. Opt in to eventual consistency in certain cases if desired.
- **Deployment flexibility:** single Rust binary and storage/compute separation allow SurrealDB to run embedded (in‐app), in the browser (via WebAssembly) or as a traditional back-end in a single node or in a highly-scalable distributed cluster.
- **Secure by design:** built-in security with RBAC, record-level permissions, fine-grained access controls, JWT authentication, multi-tenant isolation and built-in compliance (SOC 2, ISO 27001) keep data protected by default.

More information can be found in our features page.

## Enterprise case studies

SurrealDB is being used at scale in production by small and large organisations, such as:

- **Samsung Ads**, for knowledge graphs in advertising analytics.
- **SiteForge**, to reduce its development cycle, queries, and backend API usage.
- **Verizon**, for its generative AI assistant utilised by field technicians.
- **Tencent**, for infrastructure monitoring, having consolidated 9 tools into one.
- **PolyAI**, for low-latency, customer-controlled RAG across voice AI experiences.

More companies and an overview of the benefits provided by SurrealDB can be found in our case studies page.

## Use cases

SurrealDB is ideal for any application, in particular data intensive applications that require multiple data systems, such as:

- **AI agents:** building Generative AI systems leveraging a single unstructured and structured data layer with vector, graph and real-time capabilities for RAG, Graph RAG, and agent memory.
- **Knowledge graphs:** turning unstructured data into structured, queryable data with a flexible multi-model approach including support for graph relationships.
- **Real-time analytics:** fraud detection systems, recommendation engines and log analytics.
- **Embedded & edge computing:** SurrealDB is a single lightweight Rust binary and can be embedded in industrial environments, run in-memory or in browser.
- **Backend-as-a-Service:** with support for end-user authentication, SurrealDB can also be used as a BaaS for web applications, if desired.
