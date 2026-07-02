---
title: "Graph database"
source: https://en.wikipedia.org/wiki/Graph_database
domain: janusgraph
license: CC-BY-SA-4.0
tags: janusgraph, distributed graph database, apache tinkerpop, gremlin query language
fetched: 2026-07-02
---

# Graph database

A **graph database** (**GDB**) is a database that uses graph structures for semantic queries with nodes, edges, and properties to represent and store data. A key concept of the system is the graph (or edge or relationship). The graph relates the data items in the store to a collection of nodes and edges, the edges representing the relationships between the nodes. The relationships allow data in the store to be linked together directly and, in many cases, retrieved with one operation. Graph databases hold the relationships between data as a priority. Querying relationships is fast because they are perpetually stored in the database. Relationships can be intuitively visualized using graph databases, making them useful for heavily inter-connected data.

Graph databases are commonly referred to as a NoSQL database. Graph databases are similar to 1970s network model databases in that both represent general graphs, but network-model databases operate at a lower level of abstraction and lack easy traversal over a chain of edges.

The underlying storage mechanism of graph databases can vary. Relationships are first-class citizens in a graph database and can be labeled, directed, and given properties. Some depend on a relational engine and store the graph data in a table (although a table is a logical element, therefore this approach imposes a level of abstraction between the graph database management system and physical storage devices). Others use a key–value store or document-oriented database for storage, making them inherently NoSQL structures.

As of 2021, no graph query language has been universally adopted in the same way as SQL was for relational databases. There is a wide variety of systems used, many of which are tightly tied to one product. Early standardization efforts led to multi-vendor query languages like Gremlin, SPARQL, and Cypher. In September 2019 a proposal for a project to create a new standard graph query language (ISO/IEC 39075 Information Technology — Database Languages — GQL) was approved by members of ISO/IEC Joint Technical Committee 1(ISO/IEC JTC 1). GQL is intended to be a declarative database query language, like SQL. In addition to having query language interfaces, some graph databases are accessed through application programming interfaces (APIs).

Graph databases differ from graph compute engines. Graph databases are technologies that are translations of the relational online transaction processing (OLTP) databases. On the other hand, graph compute engines are used in online analytical processing (OLAP) for bulk analysis. Graph databases attracted considerable attention in the 2000s, due to the successes of major technology corporations using proprietary graph databases, along with the introduction of open-source graph databases.

One study concluded that an RDBMS was "comparable" in performance to existing graph analysis engines at executing graph queries.

## History

In the mid-1960s, navigational databases such as IBM's IMS supported tree-like structures in its hierarchical model, but the strict tree structure could be circumvented with virtual records.

Graph structures could be represented in network model databases from the late 1960s. CODASYL, which had defined COBOL in 1959, defined the Network Database Language in 1969.

Labeled graphs could be represented in graph databases from the mid-1980s, such as the Logical Data Model.

Commercial object databases (ODBMSs) emerged in the early 1990s. In 2000, the Object Data Management Group published a standard language for defining object and relationship (graph) structures in their ODMG'93 publication.

In the mid-to-late 2000s, commercial graph databases with ACID guarantees such as Neo4j and Oracle Spatial and Graph became available.

In the 2010s, commercial ACID graph databases that could be scaled horizontally became available. Further, SAP HANA brought in-memory and columnar technologies to graph databases. Also in the 2010s, multi-model databases that supported graph models (and other models such as relational database or document-oriented database) became available, such as OrientDB, ArangoDB, and MarkLogic (starting with its 7.0 version). During this time, graph databases of various types have become especially popular with social network analysis with the advent of social media companies. Also during the decade, cloud-based graph databases such as Amazon Neptune and Neo4j AuraDB became available.

## Background

Based on graph theory, graph databases store data in a way that reflects how it is conceptually understood, using nodes to represent entities and edges to represent the relationships between them.

It consists of a set of objects, such as a node or an edge.

- **Nodes** represent entities or instances such as people, businesses, accounts, or any other item to be tracked. They are roughly the equivalent of a record, relation, or row in a relational database, or a document in a document-store database.
- **Edges**, also termed *graphs* or *relationships*, are the lines that connect nodes to other nodes; representing the relationship between them. Meaningful patterns emerge when examining the connections and interconnections of nodes, properties and edges. The edges can either be directed or undirected. In an undirected graph, an edge connecting two nodes has a single meaning. In a directed graph, the edges connecting two different nodes have different meanings, depending on their direction. Edges are the key concept in graph databases, representing an abstraction that is not directly implemented in a relational model or a document-store model**.**
- **Properties** are information associated to nodes. For example, if *Wikipedia* were one of the nodes, it might be tied to properties such as *website*, *reference material*, or *words that starts with the letter w*, depending on which aspects of *Wikipedia* are germane to a given database.

## Graph models

### Labeled-property graph

A labeled-property graph model is represented by a set of nodes, relationships, properties, and labels. Both nodes of data and their relationships are named and can store properties represented by key–value pairs. Nodes can be labelled to be grouped. The edges representing the relationships have two qualities: they always have a start node and an end node, and are directed; making the graph a directed graph. Relationships can also have properties. This is useful in providing additional metadata and semantics to relationships of the nodes. Direct storage of relationships allows a constant-time traversal.

### Resource Description Framework (RDF)

In an RDF graph model, each addition of information is represented with a separate node. For example, imagine a scenario where a user has to add a name property for a person represented as a distinct node in the graph. In a labeled-property graph model, this would be done with an addition of a name property into the node of the person. However, in an RDF, the user has to add a separate node called `hasName` connecting it to the original person node. Specifically, an RDF graph model is composed of nodes and arcs. An RDF graph notation or a statement is represented by: a node for the subject, a node for the object, and an arc for the predicate. A node may be left blank, a literal and/or be identified by a URI. An arc may also be identified by a URI. A literal for a node may be of two types: plain (untyped) and typed. A plain literal has a lexical form and optionally a language tag. A typed literal is made up of a string with a URI that identifies a particular datatype. A blank node may be used to accurately illustrate the state of the data when the data does not have a URI.

## Properties

Graph databases are a powerful tool for graph-like queries. For example, computing the shortest path between two nodes in the graph. Other graph-like queries can be performed over a graph database in a natural way (for example graph's diameter computations or community detection).

Graphs are flexible, meaning it allows the user to insert new data into the existing graph without loss of application functionality. There is no need for the designer of the database to plan out extensive details of the database's future use cases.

### Storage

The underlying storage mechanism of graph databases can vary. Some depend on a relational engine and "store" the graph data in a table (although a table is a logical element, therefore this approach imposes another level of abstraction between the graph database, the graph database management system and the physical devices where the data is actually stored). Others use a key–value store or document-oriented database for storage, making them inherently NoSQL structures. A node would be represented as any other document store, but edges that link two different nodes hold special attributes inside its document; a _from and _to attributes.

### Index-free adjacency

Data lookup performance is dependent on the access speed from one particular node to another. Because index-free adjacency enforces the nodes to have direct physical RAM addresses and physically point to other adjacent nodes, it results in a fast retrieval. A native graph system with index-free adjacency does not have to move through any other type of data structures to find links between the nodes. Directly related nodes in a graph are stored in the cache once one of the nodes are retrieved, making the data lookup even faster than the first time a user fetches a node. However, such advantage comes at a cost. Index-free adjacency sacrifices the efficiency of queries that do not use graph traversals. Native graph databases use index-free adjacency to process CRUD operations on the stored data.

## Applications

Multiple categories of graphs by kind of data have been recognised. Gartner suggests the five broad categories of graphs:

- Social graph: this is about the connections between people; examples include Facebook, Twitter, and the idea of six degrees of separation
- Intent graph: this deals with reasoning and motivation.
- Consumption graph: also known as the "payment graph", the consumption graph is heavily used in the retail industry. E-commerce companies such as Amazon, eBay and Walmart use consumption graphs to track the consumption of individual customers.
- Interest graph: this maps a person's interests and is often complemented by a social graph. It has the potential to follow the previous revolution of web organization by mapping the web by interest rather than indexing webpages.
- Mobile graph: this is built from mobile data. Mobile data in the future may include data from the web, applications, digital wallets, GPS, and Internet of Things (IoT) devices.

## Comparison with relational databases

Since Edgar F. Codd's 1970 paper on the relational model, relational databases have been the de facto industry standard for large-scale data storage systems. Relational models require a strict schema and data normalization which separates data into many tables and removes any duplicate data within the database. Data is normalized in order to preserve data consistency and support ACID transactions. However this imposes limitations on how relationships can be queried.

One of the relational model's design motivations was to achieve a fast row-by-row access. Problems arise when there is a need to form complex relationships between the stored data. Although relationships can be analyzed with the relational model, complex queries performing many join operations on many different attributes over several tables are required. In working with relational models, foreign key constraints should also be considered when retrieving relationships, causing additional overhead.

Compared with relational databases, graph databases are often faster for associative data sets and map more directly to the structure of object-oriented applications. They can scale more naturally to large datasets as they do not typically need join operations, which can often be expensive. As they depend less on a rigid schema, they are marketed as more suitable to manage ad hoc and changing data with evolving schemas.

Conversely, relational database management systems are typically faster at performing the same operation on large numbers of data elements, permitting the manipulation of the data in its natural structure. Despite the graph databases' advantages and recent popularity over relational databases, it is recommended the graph model itself should not be the sole reason to replace an existing relational database. A graph database may become relevant if there is an evidence for performance improvement by orders of magnitude and lower latency.

### Examples

The relational model gathers data together using information in the data. For example, one might look for all the "users" whose phone number contains the area code "311". This would be done by searching selected datastores, or tables, looking in the selected phone number fields for the string "311". This can be a time-consuming process in large tables, so relational databases offer indexes, which allow data to be stored in a smaller sub-table, containing only the selected data and a unique key (or primary key) of the record. If the phone numbers are indexed, the same search would occur in the smaller index table, gathering the keys of matching records, and then looking in the main data table for the records with those keys. Usually, a table is stored in a way that allows a lookup via a key to be very fast.

Relational databases do not *inherently* contain the idea of fixed relationships between records. Instead, related data is linked to each other by storing one record's unique key in another record's data. For example, a table containing email addresses for users might hold a data item called `userpk`, which contains the primary key of the user record it is associated with. In order to link users and their email addresses, the system first looks up the selected user records primary keys, looks for those keys in the `userpk` column in the email table (or, more likely, an index of them), extracts the email data, and then links the user and email records to make composite records containing all the selected data. This operation, termed a join, can be computationally expensive. Depending on the complexity of the query, the number of joins, and indexing various keys, the system may have to search through multiple tables and indexes and then sort it all to match it together.

In contrast, graph databases directly store the relationships between records. Instead of an email address being found by looking up its user's key in the `userpk` column, the user record contains a pointer that directly refers to the email address record. That is, having selected a user, the pointer can be followed directly to the email records, there is no need to search the email table to find the matching records. This can eliminate the costly join operations. For example, if one searches for all of the email addresses for users in area code "311", the engine would first perform a conventional search to find the users in "311", but then retrieve the email addresses by following the links found in those records. A relational database would first find all the users in "311", extract a list of the primary keys, perform another search for any records in the email table with those primary keys, and link the matching records together. For these types of common operations, graph databases would theoretically be faster.

The true value of the graph approach becomes evident when one performs searches that are more than one level deep. For example, consider a search for users who have "subscribers" (a table linking users to other users) in the "311" area code. In this case a relational database has to first search for all the users with an area code in "311", then search the subscribers table for any of those users, and then finally search the users table to retrieve the matching users. In contrast, a graph database would search for all the users in "311", then follow the backlinks through the subscriber relationship to find the subscriber users. This avoids several searches, look-ups, and the memory usage involved in holding all of the temporary data from multiple records needed to construct the output. In terms of big O notation, this query would be $O(\log n)+O(1)$ time – i.e., proportional to the logarithm of the size of the data. In contrast, the relational version would be multiple $O(\log n)$ lookups, plus the $O(n)$ time needed to join all of the data records.

The relative advantage of graph retrieval grows with the complexity of a query. For example, one might want to know "that movie about submarines with the actor who was in that movie with that other actor that played the lead in *Gone With the Wind*". This first requires the system to find the actors in *Gone With the Wind*, find all the movies they were in, find all the actors in all of those movies who were not the lead in *Gone With the Wind*, and then find all of the movies they were in, finally filtering that list to those with descriptions containing "submarine". In a relational database, this would require several separate searches through the movies and actors tables, doing another search on submarine movies, finding all the actors in those movies, and then comparing the (large) collected results. In contrast, the graph database would walk from *Gone With the Wind* to Clark Gable, gather the links to the movies he has been in, gather the links out of those movies to other actors, and then follow the links out of those actors back to the list of movies. The resulting list of movies can then be searched for "submarine". All of this can be done via one search.

*Properties* add another layer of abstraction to this structure that also improves many common queries. Properties are essentially labels that can be applied to any record, or in some cases, edges as well. For example, one might label Clark Gable as "actor", which would then allow the system to quickly find all the records that are actors, as opposed to director or camera operator. If labels on edges are allowed, one could also label the relationship between *Gone With the Wind* and Clark Gable as "lead", and by performing a search on people that are "lead" "actor" in the movie *Gone With the Wind*, the database would produce Vivien Leigh, Olivia de Havilland and Clark Gable. The equivalent SQL query would have to rely on added data in the table linking people and movies, adding more complexity to the query syntax. These sorts of labels may improve search performance under certain circumstances, but are generally more useful in providing added semantic data for end users.

Relational databases are very well suited to flat data layouts, where relationships between data are only one or two levels deep. For example, an accounting database might need to look up all the line items for all the invoices for a given customer, a three-join query. Graph databases are aimed at datasets that contain many more links. They are especially well suited to social networking systems, where the "friends" relationship is essentially unbounded. These properties make graph databases naturally suited to types of searches that are increasingly common in online systems, and in big data environments. For this reason, graph databases are becoming very popular for large online systems like Facebook, Google, Twitter, and similar systems with deep links between records.

To further illustrate, imagine a relational model with two tables: a `people` table (which has a `person_id` and `person_name` column) and a `friend` table (with `friend_id` and `person_id`, which is a foreign key from the `people` table). In this case, searching for all of Jack's friends would result in the following SQL query.

```mw
SELECT p2.person_name 
FROM people p1 
JOIN friend ON (p1.person_id = friend.person_id)
JOIN people p2 ON (p2.person_id = friend.friend_id)
WHERE p1.person_name = 'Jack';
```

The same query may be translated into --

- Cypher, a graph database query languageMATCH (p1:person {name: 'Jack'})-[:FRIEND_WITH]-(p2:person) RETURN p2.name

- Gremlin, an imperative style graph query language maintained by Apache TinkerPop and used by many graph databasesg.V().hasLabel("person").has("name", "Jack"). out("friendsWith"). hasLabel("person"). values("name")
- SPARQL, an RDF graph database query language standardized by W3C and used in multiple RDF Triple and Quad stores
  - Long form PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?name WHERE { ?s a foaf:Person . ?s foaf:name "Jack" . ?s foaf:knows ?o . ?o foaf:name ?name . }
  - Short form PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?name WHERE { ?s foaf:name "Jack" ; foaf:knows ?o . ?o foaf:name ?name . }
- SPASQL, a hybrid database query language, that extends SQL with SPARQLSELECT people.name FROM ( SPARQL PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?name WHERE { ?s foaf:name "Jack" ; foaf:knows ?o . ?o foaf:name ?name . } ) AS people ;

The above examples are a simple illustration of a basic relationship query. They condense the idea of relational models' query complexity that increases with the total amount of data. In comparison, a graph database query is easily able to sort through the relationship graph to present the results.

There are also results that indicate simple, condensed, and declarative queries of the graph databases do not necessarily provide good performance in comparison to the relational databases. While graph databases offer an intuitive representation of data, relational databases offer better results when set operations are needed.

## List of graph databases

The following is a list of notable graph databases:

| Name | Current version | Latest release date (YYYY-MM-DD) | Software license | Programming language | Description |
|---|---|---|---|---|---|
| Aerospike | 7.0 | 2024-05-15 | Proprietary | C | Aerospike Graph is a highly scalable, low-latency property graph database built on Aerospike's proven real-time data platform. Aerospike Graph combines the enterprise capabilities of the Aerospike Database with the property graph data model via the Apache Tinkerpop graph compute engine. |
| AllegroGraph | 7.0.0 | 2022-12-20 | Proprietary, clients: Eclipse Public License v1 | C#, C, Common Lisp, Java, Python | Resource Description Framework (RDF) and graph database. |
| Amazon Neptune | 1.4.7.0 | 2026-03-03 | Proprietary | Not disclosed | Amazon Neptune is a fully managed graph database by Amazon.com. It is used as a web service, and is part of Amazon Web Services. Supports popular graph models property graph and W3C's RDF, and their respective query languages Apache TinkerPop, Gremlin, SPARQL, and openCypher. |
| Altair Graph Studio | 6.3 | 2025-12 | Proprietary | C, C++ | AnzoGraph DB is a massively parallel native Graph Online Analytics Processing (GOLAP) style database built to support SPARQL and Cypher Query Language to analyze trillions of relationships. AnzoGraph DB is designed for interactive analysis of large sets of semantic triple data, but also supports labeled properties under proposed W3C standards. |
| ArangoDB | 3.12.4.2 | 2025-04-09 | Business Source License 1.1 and Arango Community License | C++, JavaScript, .NET, Java, Python, Node.js, PHP, Scala, Go, Ruby, Elixir | NoSQL native graph database system developed by ArangoDB Inc, supporting three data models (key/value, documents, graphs, vector), with one database core and a unified query language called AQL (ArangoDB Query Language). Provides scalability and high availability via datacenter-to-datacenter replication, auto-sharding, automatic failover, and other capabilities. |
| Azure Cosmos DB |   | 2017 | Proprietary | Not disclosed | Multi-modal database which supports graph concepts using the Apache Gremlin query language |
| DataStax Enterprise Graph | v6.0.1 | 2018-06 | Proprietary | Java | Distributed, real-time, scalable database; supports Tinkerpop, and integrates with Cassandra |
| Google Spanner Graph | N/A | 2025-01 | Proprietary | C++ | A horizontally scalable, multi-model database that provides a native graph experience on top of Spanner; supports the ISO GQL standard and openCypher for matching patterns and traversing relationships; designed for global consistency and trillions of edges. |
| GUN (Graph Universe Node) | 0.2020.1240 | 2024 | Open source, MIT License, Apache 2.0, zlib License | JavaScript | An open source, offline-first, real-time, decentralized, graph database written in JavaScript for the web browser. It is implemented as a peer-to-peer network featuring multi-master replication with a custom commutative replicated data type (CRDT). |
| InfiniteGraph | 2021.2 | 2021-05 | Proprietary, commercial, free 50GB version | Java, C++, 'DO' query language | A distributed, cloud-enabled and massively scalable graph database for complex, real-time queries and operations. Its Vertex and Edge objects have unique 64-bit object identifiers that considerably speed up graph navigation and pathfinding operations. It supports batch or streaming updates to the graph alongside concurrent, parallel queries. InfiniteGraph's 'DO' query language enables both value based queries, as well as complex graph queries. InfiniteGraph is goes beyond graph databases to also support complex object queries. |
| JanusGraph | 1.1.0 | 2024-11-07 | Apache 2 | Java | Open source, scalable, distributed across a multi-machine cluster graph database under The Linux Foundation; supports various storage backends (Apache Cassandra, Apache HBase, Google Cloud Bigtable, Oracle Berkeley DB); supports global graph data analytics, reporting, and extract, transform, load (ETL) through integration with big data platforms (Apache Spark, Apache Giraph, Apache Hadoop); supports geo, numeric range, and full-text search via external index storages (Elasticsearch, Apache Solr, Apache Lucene). |
| MarkLogic | 8.0.4 | 2015 | Proprietary, freeware developer version | Java | Multi-model NoSQL database that stores documents (JSON and XML) and semantic graph data (RDF triples); also has a built-in search engine. |
| Microsoft SQL Server 2017 | RC1 |   | Proprietary | SQL/T-SQL, R, Python | Offers graph database abilities to model many-to-many relationships. The graph relationships are integrated into Transact-SQL, and use SQL Server as the foundational database management system. |
| NebulaGraph | 3.8.0 | 2024-05 | Open Source Edition is under Apache 2.0, Common Clause 1.0 | C++, Go, Java, Python | A scalable open-source distributed graph database for storing and handling billions of vertices and trillions of edges with milliseconds of latency. It is designed based on a shared-nothing distributed architecture for linear scalability. |
| Neo4j | 2026.05.0 | 2026-05-28 | GPLv3 Community Edition, commercial and AGPLv3 options for enterprise and advanced editions | Java, .NET, JavaScript, Python, Go, Ruby, PHP, R, Erlang/Elixir, C/C++, Clojure, Perl, Haskell | Open-source, supports ACID, has high-availability clustering for enterprise deployments, and comes with a web-based administration that includes full transaction support and visual node-link graph explorer; accessible from most programming languages using its built-in REST web API interface, and a proprietary Bolt protocol with official drivers. |
| Ontotext GraphDB | 11.3.3 | 2026-04-23 | Proprietary, Standard and Enterprise Editions are commercial, Free Edition is freeware | Java | Graph database with RDF and SPARQL support, also available as a high-availability cluster. Integrates OpenRefine for ingestion and reconciliation of tabular data and ontop for Ontology-Based Data Access. Connects to Lucene, SOLR and Elasticsearch for Full text and Faceted search, and Kafka for event and stream processing. Supports OGC GeoSPARQL. Provides JDBC access to Knowledge Graphs. |
| OpenLink Virtuoso | 8.2 | 2018-10 | Open Source Edition is GPLv2, Enterprise Edition is proprietary | C, C++ | Multi-model (Hybrid) relational database management system (RDBMS) that supports both SQL and SPARQL for declarative (Data Definition and Data Manipulation) operations on data modelled as SQL tables and/or RDF Graphs. Also supports indexing of RDF-Turtle, RDF-N-Triples, RDF-XML, JSON-LD, and mapping and generation of relations (SQL tables or RDF graphs) from numerous document types including CSV, XML, and JSON. May be deployed as a local or embedded instance (as used in the NEPOMUK Semantic Desktop), a one-instance network server, or a shared-nothing elastic-cluster multiple-instance networked server |
| Oracle RDF Graph; part of Oracle Database | 21c | 2020 | Proprietary | SPARQL, SQL | RDF Graph capabilities as features in multi-model Oracle Database: RDF Graph: comprehensive W3C RDF graph management in Oracle Database with native reasoning and triple-level label security. ACID, high-availability, enterprise scale. Includes visualization, RDF4J, and native end Sparql end point. |
| Oracle Property Graph; part of Oracle Database | 21c | 2020 | Proprietary; Open Source language specification | PGQL, Java, Python | Property Graph; consisting of a set of objects or vertices, and a set of arrows or edges connecting the objects. Vertices and edges can have multiple properties, which are represented as key–value pairs. Includes PGQL, an SQL-like graph query language and an in-memory analytic engine (PGX) nearly 60 prebuilt parallel graph algorithms. Includes REST APIs and graph visualization. |
| OrientDB | 3.2.28 | 2024-02 | Community Edition is Apache 2, Enterprise Edition is commercial | Java | Second-generation distributed graph database with the flexibility of documents in one product (i.e., it is both a graph database and a document NoSQL database); licensed under open-source Apache 2 license; and has full ACID support; it has a multi-master replication; supports schema-less, -full, and -mixed modes; has security profiling based on user and roles; supports a query language similar to SQL. It has HTTP REST and JSON API. |
| RedisGraph | 2.0.20 | 2020-09 | Redis Source Available License,AGPLv3,SSPL | C | In-memory, queryable Property Graph database which uses sparse matrices to represent the adjacency matrix in graphs and linear algebra to query the graph. |
| SAP HANA | 2.0 SPS 05 | 2020-06 | Proprietary | C, C++, Java, JavaScript and SQL-like language | In-memory ACID transaction supported property graph |
| Sparksee | 5.2.0 | 2015 | Proprietary, commercial, freeware for evaluation, research, development | C++ | High-performance scalable database management system from Sparsity Technologies; main trait is its query performance for retrieving and exploring large networks; has bindings for Java, C++, C#, Python, and Objective-C; version 5 is the first graph mobile database. |
| Teradata Aster | 7 | 2016 | Proprietary | Java, SQL, Python, C++, R | Massive parallel processing (MPP) database incorporating patented engines supporting native SQL, MapReduce, and graph data storage and manipulation; provides a set of analytic function libraries and data visualization |
| TerminusDB | 11.0.6 | 2023-05-03 | Apache 2 | Prolog, Rust, Python, JSON-LD | Document-oriented knowledge graph, focusing on versioned data. |
| TigerGraph | 4.1.2 | 2024-12-20 | Proprietary | C++ | Massive parallel processing (MPP) native graph database management system |
| TypeDB | 2.14.0 | 2022-11 | Free, GNU AGPLv3, Proprietary | Java, Python, JavaScript | TypeDB is a strongly-typed database software with an extensible type system. |

## Graph query-programming languages

- AQL (ArangoDB Query Language): a SQL-like query language used in ArangoDB for both documents and graphs
- Cypher Query Language (Cypher): a graph query declarative language for Neo4j that enables ad hoc and programmatic (SQL-like) access to the graph.
- GQL: ISO standard defined for graph query language
- Gremlin: a graph programming language that is a part of Apache TinkerPop open-source project
- SPARQL: a query language for RDF databases that can retrieve and manipulate data stored in RDF format
- regular path queries, a theoretical language for queries on graph databases
