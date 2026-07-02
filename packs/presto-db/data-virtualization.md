---
title: "Data virtualization"
source: https://en.wikipedia.org/wiki/Data_virtualization
domain: presto-db
license: CC-BY-SA-4.0
tags: presto query engine, distributed sql engine, massively parallel processing, interactive analytics, query optimization
fetched: 2026-07-02
---

# Data virtualization

**Data virtualization** is an approach to data management that allows an application to retrieve and manipulate data without requiring technical details about the data, such as how it is formatted at source, or where it is physically located, and can provide a single customer view (or single view of any other entity) of the overall data.

Unlike the traditional extract, transform, load ("ETL") process, the data remains in place, and real-time access is given to the source system for the data. This reduces the risk of data errors, of the workload moving data around that may never be used, and it does not attempt to impose a single data model on the data (an example of heterogeneous data is a federated database system). The technology also supports the writing of transaction data updates back to the source systems. To resolve differences in source and consumer formats and semantics, various abstraction and transformation techniques are used. This concept and software is a subset of data integration and is commonly used within business intelligence, service-oriented architecture data services, cloud computing, enterprise search, and master data management.

## Applications, benefits and drawbacks

The defining feature of data virtualization is that the data used remains in its original locations and real-time access is established to allow analytics across multiple sources. This aids in resolving some technical difficulties such as compatibility problems when combining data from various platforms, lowering the risk of error caused by faulty data, and guaranteeing that the newest data is used. Furthermore, avoiding the creation of a new database containing personal information can make it easier to comply with privacy regulations. As a result, data virtualization creates new possibilities for data use.

Building on this, data virtualization's real value, particularly for users, is its declarative approach. Unlike traditional data integration methods that require specifying every step of integration, this approach can be less error-prone and more efficient. Traditional methods are tedious, especially when adapting to changing requirements, involving changes at multiple steps. Data virtualization, in contrast, allows users to simply describe the desired outcome. The software then automatically generates the necessary steps to achieve this result. If the desired outcome changes, updating the description suffices, and the software adjusts the intermediate steps accordingly. This flexibility can accelerate processes by up to five times, underscoring the primary advantage of data virtualization.

However, with data virtualization, the connection to all necessary data sources must be operational as there is no local copy of the data, which is one of the main drawbacks of the approach. Connection problems occur more often in complex systems where one or more crucial sources will occasionally be unavailable. Smart data buffering, such as keeping the data from the most recent few requests in the virtualization system buffer can help to mitigate this issue.

Moreover, because data virtualization solutions may use large numbers of network connections to read the original data and server virtualised tables to other solutions over the network, system security requires more consideration than it does with traditional data lakes. In a conventional data lake system, data can be imported into the lake by following specific procedures in a single environment. When using a virtualization system, the environment must separately establish secure connections with each data source, which is typically located in a different environment from the virtualization system itself.

Security of personal data and compliance with regulations can be a major issue when introducing new services or attempting to combine various data sources. When data is delivered for analysis, data virtualisation can help to resolve privacy-related problems. Virtualization makes it possible to combine personal data from different sources without physically copying them to another location while also limiting the view to all other collected variables. However, virtualization does not eliminate the requirement to confirm the security and privacy of the analysis results before making them more widely available. Regardless of the chosen data integration method, all results based on personal level data should be protected with the appropriate privacy requirements.

## Data virtualization and data warehousing

Some enterprise landscapes are filled with disparate data sources including multiple data warehouses, data marts, and/or data lakes, even though a Data Warehouse, if implemented correctly, should be unique and a single source of truth. Data virtualization can efficiently bridge data across data warehouses, data marts, and data lakes without having to create a whole new integrated physical data platform. Existing data infrastructure can continue performing their core functions while the data virtualization layer just leverages the data from those sources. This aspect of data virtualization makes it complementary to all existing data sources and increases the availability and usage of enterprise data.

Data virtualization may also be considered as an alternative to ETL and data warehousing but for performance considerations it's not really recommended for a very large data warehouse. Data virtualization is inherently aimed at producing quick and timely insights from multiple sources without having to embark on a major data project with extensive ETL and data storage. However, data virtualization may be extended and adapted to serve data warehousing requirements also. This will require an understanding of the data storage and history requirements along with planning and design to incorporate the right type of data virtualization, integration, and storage strategies, and infrastructure/performance optimizations (e.g., streaming, in-memory, hybrid storage).

## Examples

- The Phone House—the trading name for the European operations of UK-based mobile phone retail chain Carphone Warehouse—implemented Denodo's data virtualization technology between its Spanish subsidiary's transactional systems and the Web-based systems of mobile operators.
- Novartis implemented TIBCO's data virtualization tool to enable its researchers to quickly combine data from both internal and external sources into a searchable virtual data store.
- The storage-agnostic Primary Data (defunct, reincarnated as Hammerspace) was a data virtualization platform that enabled applications, servers, and clients to transparently access data while it was migrated between direct-attached, network-attached, private and public cloud storage.
- Linked Data can use a single hyperlink-based Data Source Name (DSN) to provide a connection to a virtual database layer that is internally connected to a variety of back-end data sources using ODBC, JDBC, OLE DB, ADO.NET, SOA-style services, and/or REST patterns.
- Database virtualization may use a single ODBC-based DSN to provide a connection to a similar virtual database layer.
- Alluxio, an open-source virtual distributed file system (VDFS), started at the University of California, Berkeley's AMPLab. The system abstracts data from various file systems and object stores.

## Functionality

Data Virtualization software provides some or all of the following capabilities:

- Abstraction – Abstract the technical aspects of stored data, such as location, storage structure, API, access language, and storage technology.
- Virtualized Data Access – Connect to different data sources and make them accessible from a common logical data access point.
- Data transformation – Transform, improve quality, reformat, aggregate etc. source data for consumer use.
- Data federation – Combine result sets from across multiple source systems.
- Data delivery – Publish result sets as views and/or data services executed by client application or users when requested.

Data virtualization software may include functions for development, operation, and/or management.

A metadata engine collects, stores and analyzes information about data and metadata (data about data) in use within a domain.

Benefits include:

- Reduce risk of data errors
- Reduce systems workload through not moving data around
- Increase speed of access to data on a real-time basis
- Allows for query processing pushed down to data source instead of in middle tier
- Most systems enable self-service creation of virtual databases by end users with access to source systems
- Increase governance and reduce risk through the use of policies
- Reduce data storage required
- Accelerate processes up to five times through the declarative approach

Drawbacks include:

- May impact Operational systems response time, particularly if under-scaled to cope with unanticipated user queries or not tuned early on.
- Does not impose a heterogeneous data model, meaning the user has to interpret the data, unless combined with Data Federation and business understanding of the data
- Requires a defined Governance approach to avoid budgeting issues with the shared services
- Not suitable for recording the historic snapshots of data. A data warehouse is better for this
- Change management "is a huge overhead, as any changes need to be accepted by all applications and users sharing the same virtualization kit"
- Designers should always keep performance considerations in mind

Avoid usage:

- For accessing Operational Data Systems (Performance and Operational Integrity issues)
- For federating or centralizing all data of the organization (Security and hacking issues)
- For building very large virtual Data warehouse (Performance issues)
- As an ETL process (Governance and performance issues)
- If you have only one or two data sources to virtualize

## History

Enterprise information integration (EII) (first coined by Metamatrix), now known as Red Hat JBoss Data Virtualization, and federated database systems are terms used by some vendors to describe a core element of data virtualization: the capability to create relational JOINs in a federated VIEW.

## Technology

Some data virtualization solutions and vendors:

- AnalyticsCreator
- IBM data Virtualization
- Actifio Copy Data Virtualization
- Capsenta Ultrawrap, acquired by data.world 2019
- Data Virtuality
- DataWerks
- Delphix Data Virtualization Platform
- Microsoft Gluent Data Platform
- Querona
- Red Hat JBoss Enterprise Application Platform Data Virtualization (discontinued)
- Stone Bond Technologies Enterprise Enabler Data Virtualization Platform
- Stratio Generative AI Data Fabric
- Teiid, part of JBoss Developer Studio
- TIBCO Data Virtualization
- Veritas Provisioning File System / Data Virtualization Veritas Technologies
- Virtual Data Platform
- XAware

Another more up-to-date list with user rankings is compiled by Gartner.
