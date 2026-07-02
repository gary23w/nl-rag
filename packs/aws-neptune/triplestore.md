---
title: "Triplestore"
source: https://en.wikipedia.org/wiki/Triplestore
domain: aws-neptune
license: CC-BY-SA-4.0
tags: aws neptune, amazon neptune, managed graph database, knowledge graph service
fetched: 2026-07-02
---

# Triplestore

A **triplestore** or **RDF store** is a purpose-built database for the storage and retrieval of triples through semantic queries. A triple is a data entity composed of subject–predicate–object, like "Bob is 35" (i.e., Bob's age measured in years is 35) or "Bob knows Fred".

Much like a relational database, information in a triplestore is stored and retrieved via a query language. SPARQL is the W3C-standardized query language for querying RDF data, and is implemented by most actively maintained RDF triplestores. Unlike a relational database, a triplestore is optimized for the storage and retrieval of triples. In addition to queries, triples can usually be imported and exported using the Resource Description Framework (RDF) and other formats.

## Implementations

Some triplestores have been built as database engines from scratch, while others have been built on top of existing commercial relational database engines (such as SQL-based) or NoSQL document-oriented database engines. Like the early development of online analytical processing (OLAP) databases, this intermediate approach allowed large and powerful database engines to be constructed for little programming effort in the initial phases of triplestore development. A difficulty with implementing triplestores over SQL is that although "triples" may thus be "stored", implementing efficient querying of a graph-based RDF model (such as mapping from SPARQL) onto SQL queries is difficult.

Adding a name to the triple makes a "quad store" or named graph.

A graph database has a more generalized structure than a triplestore, using graph structures with nodes, edges, and properties to represent and store data. Graph databases and triplestores differ in their data models, query languages and typical use cases. Triplestores are specialized for storing and querying RDF data.
