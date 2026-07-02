---
title: "Document-oriented database"
source: https://en.wikipedia.org/wiki/Document-oriented_database
domain: aws-documentdb
license: CC-BY-SA-4.0
tags: aws documentdb, amazon documentdb, managed document database, mongodb-compatible database
fetched: 2026-07-02
---

# Document-oriented database

A **document-oriented database**, or **document store**, is a computer program and data storage system designed for storing, retrieving, and managing document-oriented information, also known as semi-structured data.

Document-oriented databases are one of the main categories of NoSQL databases, and the popularity of the term "document-oriented database" has grown alongside the adoption of NoSQL itself. XML databases are a subclass of document-oriented databases optimized for XML documents. Graph databases are similar, but add another layer, the *relationship*, which allows them to link documents for rapid traversal.

Document-oriented databases are conceptually an extension of the key–value store, another type of NoSQL database. In key-value stores, data is treated as opaque by the database, whereas document-oriented systems exploit the internal structure of documents to extract metadata and optimize storage and queries. Although in practice the distinction can be minimal due to modern tooling, document stores are designed to provide a richer programming experience with modern programming techniques.

Document databases differ significantly from traditional relational databases (RDBs). Relational databases store data in predefined tables, often requiring an object to be split across multiple tables. In contrast, document databases store all information for a given object in a single document, with each document potentially having a unique structure. This design eliminates the need for object-relational mapping when loading data into the database.

## Documents

The central concept of a document-oriented database is the notion of a *document*. Although implementations vary in their specific definitions, document-oriented databases generally treat documents as self-contained units that encapsulate and encode data in a standardized format. Common encoding formats include XML, YAML, JSON, as well as binary representations such as BSON.

Documents in a document store are equivalent to the programming concept of an object. They are not required to adhere to a fixed schema, and documents within the same collection may contain different fields or structures. Fields may be optional, and documents of the same logical type may differ in composition. For example, the following illustrates a document encoded in JSON:

```mw
{
    "firstName": "Bob", 
    "lastName": "Smith",
    "address": {
        "type": "Home",
        "street1":"5 Oak St.",
        "city": "Boys",
        "state": "AR",
        "zip": "32225",
        "country": "US"
    },
    "hobby": "sailing",
    "phone": {
        "type": "Cell",
        "number": "(555)-123-4567"
    }
}
```

A second document might be encoded in XML as:

```mw
<contact>
  <firstname>Bob</firstname>
  <lastname>Smith</lastname>
  <phone type="Cell">(123) 555-0178</phone>
  <phone type="Work">(890) 555-0133</phone>
  <address>
    <type>Home</type>
    <street1>123 Back St.</street1>
    <city>Boys</city>
    <state>AR</state>
    <zip>32225</zip>
    <country>US</country>
  </address>
</contact>
```

The two example documents share some structural elements but also contain unique fields. The structure, text, and other data within each document are collectively referred to as the document's content and can be accessed or modified using retrieval or editing operations. Unlike relational databases, in which each record contains the same fields and unused fields are left empty, document-oriented databases do not require uniform fields across documents. This design allows new information to be added to some documents without affecting the structure of others.

Document databases often support the storage of additional metadata alongside the document content. Such metadata may relate to organizational features, security, indexing, or other implementation-specific features.

### CRUD operations

The core operations supported by a document-oriented database for manipulating documents are similar to those in other databases. Although terminology is not perfectly standardized, these operations are generally recognized as Create, Read, Update, and Delete (CRUD).

- Creation (C): Adds a new document to the database.
- Retrieval (R): Retrieves documents or fields based on queries.
- Update (U): Modifies the contents of existing documents.
- Deletion (D): Removes documents from the database.

### Keys

Documents in a document-oriented database are addressed via a unique identifier. This identifier, often a string, URI, or path, can be used to retrieve the document from the database. Most document stores maintain an index on the key to optimize retrieval, and in some implementations the key is required when creating or inserting a new document.

### Retrieval

In addition to key-based access, document-oriented databases typically provide an API or query language that enables retrieval based on document content or associated metadata. For example, a query may return all documents with a specific field matching a given value. The available query features, indexing options, and performance characteristics vary across implementations.

Document stores differ from key-value stores in that they exploit the internal structure and metadata of stored documents. In many key-value stores, values are treated as opaque or "black-box" data, meaning the database system does not interpret their internal structure. By contrast, document-oriented databases can classify and interpret document content. This enables queries that distinguish between types of data––for example, retrieving all phone numbers containing "555" without also matching a postal code such as "55555."

### Editing

Document databases typically provide mechanisms for updating or editing the content or metadata of a document. Updates may involve replacing the entire document or modifying individual elements or fields within the document.

### Organization

Document database implementations support a variety of methods for organizing documents, including:

- **Collections:** Groups of documents. Depending on the implementation, a document may be required to belong to a single collection or may be allowed in multiple collections.
- **Tags and non-visible metadata:** Additional data stored outside the main document content.
- **Directory hierarchies:** Documents organized in a tree-like structure, often based on path or URI.

These organizational structures may differ between logical and physical representations (e.g. on disk or in memory).

## Relationship to other databases

### Relationship to key-value stores

A document-oriented database can be viewed as a specialized form of key-value store, which is itself a category of NoSQL database. In a basic key-value store, the stored value is typically treated as opaque by the database system. By contrast, a document-oriented database provides APIs or a query and update language that allows queries and modifications based on the internal structure of the document. For users who do not require advanced query, retrieval, or update capabilities, the distinction between document-oriented databases and key-value stores may be minimal.

Some search engine and information retrieval systems, such as Apache Solr and Elasticsearch, provide document storage and support core document operations. As a result, they may meet certain functional definitions of a document-oriented database, although their primary design goals differ.

### Relationship to relational databases

In a relational database, data is organized into predefined types represented as tables. Each table contains rows (records) with a fixed set of columns (fields), so all records in a table share the same structure. Administrators typically define indexes on selected fields to improve query performance. A central principle of relational database design is database normalization, in which data that might otherwise be repeated is stored in separate tables and linked using keys. When records in different tables are related, a foreign key is used to associate them.

For example, an address book application may store a contact's name, image, phone numbers, mailing addresses, and email addresses. In a normalized relational design, separate tables might be created for contacts, phone numbers, and email addresses. The phone number table would include a foreign key referencing the associated contact. To reconstruct a complete contact record, the database retrieves related information from each table using the foreign keys and combines it into a single record.

In contrast, a document-oriented database stores all data related to an object within a single document, and stored in the database as a single entry. In the address book example,the contact's name, image, and contact information may be stored together in one document. The document is retrieved using a unique key, and all related information is returned together, without needing to look up multiple tables.

A key difference between the document-oriented and relational models is that the data formats are not predefined in the document case. In most cases, any sort of document can be stored in a database, and documents can change in type and form over time. For example, a new field such as COUNTRY_FLAG can be added to new documents as they are inserted without affecting existing documents. To aid retrieval, document-oriented systems generally allow the administrator to provide hints to the database for locating certain types of information. These hints work in a similar fashion to indexes in relational databases. Many systems also allow additional metadata outside the content of the document itself, such as tagging entries as part of an address book, which enables retrieval of related information, for instance, all the address book entries. This provides functionality similar to a table, but separates the concept (categories of data) from its physical implementation (tables).

In the traditional normalized relational model, objects in the database are represented as separate rows of data, with no inherent structure beyond what is defined in the tables. This can create difficulties when translating programming objects to and from their corresponding database rows, a challenge known as object-relational impedance mismatch. In contrast, document stores often map programming objects directly into the database, preserving much of their internal structure. Databases using this approach are frequently described as NoSQL systems.

## Implementations

| Name | Publisher | License | Languages supported | Notes | RESTful API |
|---|---|---|---|---|---|
| Aerospike | Aerospike | AGPL and Proprietary | C, C#, Java, Scala, Python, Node.js, PHP, Go, Rust, Spring Framework | Aerospike is a flash-optimized and in-memory distributed key value NoSQL database which also supports a document store model. | Yes |
| AllegroGraph | Franz, Inc. | Proprietary | Java, Python, Common Lisp, Ruby, Scala, C#, Perl | The database platform supports document store and graph data models in a single database. Supports JSON, JSON-LD, RDF, full-text search, ACID, two-phase commit, Multi-Master Replication, Prolog and SPARQL. | Yes |
| ArangoDB | ArangoDB | Business Source Licence | C, C#, Java, Python, Node.js, PHP, Scala, Go, Ruby, Elixir | The database system supports document store as well as key/value and graph data models with one database core and a unified query language AQL (ArangoDB Query Language). | Yes |
| BaseX | BaseX Team | BSD License | Java, XQuery | Support for XML, JSON and binary formats; client-/server based architecture; concurrent structural and full-text searches and updates. | Yes |
| Caché | InterSystems Corporation | Proprietary | Java, C#, Node.js | Commonly used in Health, Business and Government applications. | Yes |
| Cloudant | Cloudant, Inc. | Proprietary | Erlang, Java, Scala, and C | Distributed database service based on BigCouch, the company's open source fork of the Apache-backed CouchDB project. Uses JSON model. | Yes |
| Clusterpoint Database | Clusterpoint Ltd. | Proprietary with free download | JavaScript, SQL, PHP, C#, Java, Python, Node.js, C, C++, | Distributed document-oriented XML / JSON database platform with ACID-compliant transactions; high-availability data replication and sharding; built-in full-text search engine with relevance ranking; JS/SQL query language; GIS; Available as pay-per-use database as a service or as an on-premise free software download. | Yes |
| Couchbase Server | Couchbase, Inc. | Business Source Licence | C, C#, Java, Python, Node.js, PHP, SQL, Go, Spring Framework, LINQ | Distributed NoSQL Document Database, JSON model and SQL based Query Language. | Yes |
| CouchDB | Apache Software Foundation | Apache License | Any language that can make HTTP requests | JSON over REST/HTTP with Multi-Version Concurrency Control and limited ACID properties. Uses map and reduce for views and queries. | Yes |
| CrateDB | Crate.io, Inc. | Apache License | Java | Use familiar SQL syntax for real time distributed queries across a cluster. Based on Lucene / Elasticsearch ecosystem with built-in support for binary objects (BLOBs). | Yes |
| Cosmos DB | Microsoft | Proprietary | C#, Java, Python, Node.js, JavaScript, SQL | Platform-as-a-Service offering, part of the Microsoft Azure platform. Builds upon and extends the earlier Azure DocumentDB. | Yes |
| DocumentDB | Amazon Web Services | Proprietary online service | various, REST | fully managed MongoDB v3.6-compatible database service | Yes |
| DynamoDB | Amazon Web Services | Proprietary | Java, JavaScript, Node.js, Go, C# .NET, Perl, PHP, Python, Ruby, Rust, Haskell, Erlang, Django, and Grails | fully managed proprietary NoSQL database service that supports key–value and document data structures | Yes |
| Elasticsearch | Shay Banon | Dual-licensed under Server Side Public License and Elastic license. | Java | JSON, Search engine. | Yes |
| eXist | eXist | LGPL | XQuery, Java | XML over REST/HTTP, WebDAV, Lucene Fulltext search, binary data support, validation, versioning, clustering, triggers, URL rewriting, collections, ACLS, XQuery Update | Yes |
| Informix | IBM | Proprietary, with no-cost editions | Various (Compatible with MongoDB API) | RDBMS with JSON, replication, sharding and ACID compliance. | Yes |
| Jackrabbit | Apache Foundation | Apache License | Java | Java Content Repository implementation | ? |
| HCL Notes (HCL Domino) | HCL | Proprietary | LotusScript, Java, Notes Formula Language | MultiValue | Yes |
| MarkLogic | MarkLogic Corporation | Proprietary with free developer download | Java, JavaScript, Node.js, XQuery, SPARQL, XSLT, C++ | Distributed document-oriented database for JSON, XML, and RDF triples. Built-in full-text search, ACID transactions, high availability and disaster recovery, certified security. | Yes |
| MongoDB | MongoDB, Inc | Server Side Public License for the DBMS, Apache 2 License for the client drivers | C, C++, C#, Java, Kotlin, Perl, PHP, Python, Go, Node.js, Ruby, Rust, Scala, Swift | Document database with replication and sharding, BSON store (binary format JSON). | Yes |
| MUMPS Database | ? | Proprietary and AGPL | MUMPS | Commonly used in health applications. | ? |
| ObjectDatabase++ | Ekky Software | Proprietary | C++, C#, TScript | Binary Native C++ class structures | ? |
| OpenLink Virtuoso | OpenLink Software | GPLv2 and Proprietary | C++, C#, Java, SPARQL | Middleware and database engine hybrid | Yes |
| OrientDB | Orient Technologies | Apache License | Java | JSON over HTTP, SQL support, ACID transactions | Yes |
| Oracle NoSQL Database | Oracle Corp | Apache License and Proprietary | C, C#, Java, Python, node.js, Go | Shared nothing, horizontally scalable database with support for schema-less JSON, fixed schema tables, and key/value pairs. Also supports ACID transactions. | Yes |
| Qizx | Qualcomm | Proprietary | REST, Java, XQuery, XSLT, C, C++, Python | Distributed document-oriented XML database with integrated full-text search; support for JSON, text, and binaries. | Yes |
| RavenDB | RavenDB Ltd. | AGPL, commercial and free | C#, C++, Java, NodeJS, Python, Ruby, PHP and Go | RavenDB is an open-source document-oriented cross-platform database written in C#, developed by RavenDB Ltd. Supported on Windows, Linux, Mac OS, AWS, Azure, and GCP | Yes |
| RedisJSON | Redis | Redis Source Available License (RSAL) | Python | JSON with integrated full-text search. | Yes |
| RethinkDB | ? | Apache License | C++, Python, JavaScript, Ruby, Java | Distributed document-oriented JSON database with replication and sharding. | No |
| SAP HANA | SAP | Proprietary | SQL-like language | ACID transaction supported, JSON only | Yes |
| Sedna | sedna.org | Apache License | C++, XQuery | XML database | No |
| SimpleDB | Amazon Web Services | Proprietary online service | Erlang |   | ? |
| Apache Solr | Apache Software Foundation | Apache License | Java | JSON, CSV, XML, and a few other formats. Search engine. | Yes |
| TerminusDB | TerminusDB | Apache License | Python, Node.js, JavaScript | The database system supports document store as well as graph data models with one database core and a unified, datalog based query language WOQL (Web Object Query Language). | Yes |

### XML database implementations

Most XML databases are document-oriented databases.
