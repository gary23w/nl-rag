---
title: "Cloud database"
source: https://en.wikipedia.org/wiki/Cloud_database
domain: snowflake
license: CC-BY-SA-4.0
tags: snowflake data cloud, cloud data warehouse, micro-partition, columnar storage
fetched: 2026-07-02
---

# Cloud database

A **cloud database** is a database that typically runs on a cloud computing platform, with access provided as a service. There are two common deployment models: users can run databases on the cloud independently, using a virtual machine image, or they can purchase access to a database service maintained by a cloud database provider. Cloud databases may use either a relational SQL or a NoSQL data model.

Database services handle scalability and high availability, while making the underlying software stack transparent to users.

## Deployment models

There are two primary methods to run a database on a cloud platform:

**Virtual machine image**

Cloud platforms allow users to purchase virtual machine instances for a limited time, on which a database can be run. Users can upload their own machine image with a database installed or use ready-made machine images that include an optimized installation of a database.

**Database-as-a-service (DBaaS)**

With a database as a service (DBaaS) model, users pay a cloud provider for database services and computing resources, which may reduce the operational overhead needed to develop and manage databases.

Users are provided with tools to create and manage database instances, as well as to manage database users. Some cloud providers also offer tools for managing database structures and data.

Many cloud providers offer both relational (e.g.,

Amazon RDS

, SQL Server) and NoSQL (e.g.,

MongoDB

,

Amazon DynamoDB

) databases.

DBaaS is a type of

software as a service

(SaaS).

### Architecture and common characteristics

- Most database services offer web-based consoles that end users can use to provision and configure database instances.
- Database services routinely include a database-manager component that manages the underlying database instances using a service API. The API is exposed to end users and permits them to perform maintenance and scaling operations on their database instances.
- The underlying software stack typically includes the operating system, the database, and third-party software used to manage the database. The service provider is responsible for installing, patching, and updating the underlying software stack, as well as ensuring the overall health and performance of the database.
- Scalability features differ between vendors—some offer auto-scaling, others allow users to scale resources via an API but do not scale automatically.
- Service providers typically commit to a defined level of high availability (e.g., 99.9% or 99.99%). This is achieved through techniques such as data replication and automatic failover to standby instances.

## Data model

The design and development of typical systems often use data management and relational databases as key building blocks. Advanced queries expressed in SQL work well with the strict relationships imposed by relational databases. However, relational database technology was not originally designed for use over distributed systems. This limitation has been addressed through clustering enhancements, although some fundamental operations—such as data synchronization—still require complex and expensive protocols.

Modern relational databases can exhibit poor performance on data-intensive systems. As a result, the NoSQL paradigm has been adopted within database management systems for cloud-based systems. NoSQL storage does not require fixed table schemas, and join operations are typically avoided. NoSQL databases have been shown to provide efficient horizontal scalability, high performance, and ease of integration into cloud applications. Additionally, data models that rely on simplified relay algorithms have been employed in data-intensive cloud mapping applications specific to virtual frameworks.

It is also important to differentiate between cloud databases which are relational (SQL) and those that are non-relational (NoSQL).

**SQL databases**

SQL databases can run in the cloud either on virtual machines or as a managed service, depending on the vendor. While SQL databases are generally easy to scale vertically, horizontal scalability presents a greater challenge.

**NoSQL databases**

NoSQL databases are designed to service heavy read/write loads and can scale up and down easily,

making them well suited to cloud environments. However, many contemporary applications are built around a relational (SQL) data model, so adopting NoSQL databases often requires significant changes to application code.

Some SQL databases have developed NoSQL capabilities, including

JSON

, binary JSON (e.g.

BSON

or similar variants), and key-value store data types.

Multi-model databases combine relational and non-relational capabilities, providing a standard SQL interface to users and applications. Native multi-model databases support multiple data models with a single core, facilitating their use in applications built around SQL.

## Vendors

The following table lists notable database vendors that offer cloud database services, classified by deployment model—machine image or database as a service—and by data model (SQL or NoSQL).

|   | Virtual Machine Deployment | Database as a Service |
|---|---|---|
| SQL Data Model | EDB Postgres Advanced Server IBM Db2 Ingres (database) MariaDB MySQL NuoDB Oracle Database PostgreSQL SAP HANA YugabyteDB TiDB | Amazon Aurora, MySQL-based service Amazon Relational Database Service Clustrix Database as a Service CockroachDB-as-a-Service EnterpriseDB Postgres Plus Cloud Database Google Cloud SQL Heroku PostgreSQL as a Service (shared and dedicated database options) Microsoft Azure SQL Database (MS SQL) Oracle Database Cloud Service SkySQL MariaDB Snowflake Cloud Data Warehouse Xeround Cloud Database* – MySQL front-end (*service no longer available) YugabyteDB TiDB |
| NoSQL Data Model | Apache Cassandra on Amazon EC2 or Google Compute Engine ArangoDB on Amazon EC2, Google Compute or Microsoft Azure Clusterpoint Database Virtual Box VM CouchDB on Amazon EC2 or Google Cloud Platform EDB Postgres Advanced Server Hadoop on Amazon EC2, Google Cloud Platform, or Rackspace MarkLogic on Amazon EC2 or Google Cloud Platform MongoDB on Amazon EC2, Google Compute Engine or Microsoft Azure, VMware, KVM, and other hypervisors. Neo4J on Amazon EC2 or Microsoft Azure ScyllaDB on Amazon EC2 or Google Cloud Platform YugabyteDB | Amazon DynamoDB Amazon SimpleDB Azure Cosmos DB Couchbase Capella Database as a Service Cloudant Data Layer (CouchDB) DataStax Astra DB powered by Apache Cassandra EnterpriseDB Postgres Plus Cloud Database Google Cloud Bigtable Google Cloud Datastore MongoDB Database as a Service (several options) Oracle NoSQL Database Cloud Service ScyllaDB Cloud Amazon DocumentDB YugabyteDB |
