---
title: "SAP HANA"
source: https://en.wikipedia.org/wiki/SAP_HANA
domain: sap-erp
license: CC-BY-SA-4.0
tags: sap erp, sap hana, abap language, sap enterprise software
fetched: 2026-07-02
---

# SAP HANA

**SAP HANA** (German: *HochleistungsANalyseAnwendung*, lit. 'High-performance ANalysis Application') is an in-memory, column-oriented, relational database management system developed and marketed by SAP SE. Its primary function as the software running a database server is to store and retrieve data as requested by the applications. In addition, it performs advanced analytics (predictive analytics, spatial data processing, text analytics, text search, streaming analytics, graph data processing) and includes extract, transform, load (ETL) capabilities as well as an application server.

## History

As of 2005 SAP SE did not commercialize its own proprietary database technology. Many customers ran SAP applications on non-SAP databases from vendors such as Oracle Corporation and Software AG. During the early development of SAP HANA, a number of technologies were developed or acquired by SAP, including TREX search engine (in-memory column-oriented search engine), P*TIME (in-memory online transaction processing (OLTP) Platform acquired by SAP in 2005), and MaxDB with its in-memory liveCache engine.

The first major demonstration of the platform was in 2011: teams from SAP SE, the Hasso Plattner Institute and Stanford University demonstrated an application architecture for real-time analytics and aggregation using the name HYRISE. Former SAP SE executive, Vishal Sikka, mentioned this architecture as "Hasso's New Architecture". Before the name "HANA" stabilized, people referred to this product as "New Database". The software was previously called "SAP High-Performance Analytic Appliance".

A first research paper on HYRISE was published in November 2010. The research engine is later released open source in 2013, and was reengineered in 2016 to become HYRISE2 in 2017.

The first product shipped in late November 2010. By mid-2011, the technology had attracted interest but more experienced business customers considered it to be "in early days". HANA support for SAP NetWeaver Business Warehouse (BW) was announced in September 2011 for availability by November.

In 2012, SAP promoted aspects of cloud computing. In October 2012, SAP announced a platform as a service offering called the SAP HANA Cloud Platform and a variant called SAP HANA One that used a smaller amount of memory.

In May 2013, a managed private cloud offering called the HANA Enterprise Cloud service was announced.

In May 2013, Business Suite on HANA became available, enabling customers to run SAP Enterprise Resource Planning functions on the HANA platform.

S/4HANA, released in 2015, written specifically for the HANA platform, combines functionality for ERP, CRM, SRM and others into a single HANA system. S/4HANA is intended to be a simplified business suite, replacing earlier generation ERP systems. While it is likely that SAP will focus its innovations on S/4HANA, some customers using non-HANA systems have raised concerns of being locked into SAP products. Since S/4HANA requires an SAP HANA system to run, customers running SAP business suite applications on hardware not certified by SAP would need to migrate to a SAP-certified HANA database should they choose the features offered by S/4HANA.

Rather than versioning, the software utilizes service packs, referred to as Support Package Stacks (SPS), for updates. Support Package Stacks are released every 6 months.

In November 2016 SAP announced SAP HANA 2, which offers enhancements to multiple areas such as database management and application management and includes two new cloud services: Text Analysis and Earth Observation Analysis. HANA customers can upgrade to HANA 2 from SPS10 and above. Customers running SPS9 and below must first upgrade to SPS12 before upgrading to HANA 2 SPS01.

## Architecture

### Overview

The key distinctions between HANA and previous generation SAP systems are that it is a column-oriented, in-memory database, that combines OLAP and OLTP operations into a single system; thus in general SAP HANA is an "online transaction and analytical processing" (OLTAP) system, also known as a hybrid transactional/analytical processing (HTAP). Storing data in main memory rather than on disk provides faster data access and, by extension, faster querying and processing. While storing data in-memory confers performance advantages, it is a more costly form of data storage. Observing data access patterns, up to 85% of data in an enterprise system may be infrequently accessed therefore it can be cost-effective to store frequently accessed, or "hot", data in-memory while the less frequently accessed "warm" data is stored on disk, an approach SAP began to support in 2016 and termed "Dynamic tiering".

Column-oriented systems store all data for a single column in the same location, rather than storing all data for a single row in the same location (row-oriented systems). This can enable performance improvements for OLAP queries on large datasets and allows greater vertical compression of similar types of data in a single column. If the read times for column-stored data is fast enough, consolidated views of the data can be performed on the fly, removing the need for maintaining aggregate views and its associated data redundancy.

Although row-oriented systems have traditionally been favored for OLTP, in-memory storage opens techniques to develop hybrid systems suitable for both OLAP and OLTP capabilities, removing the need to maintain separate systems for OLTP and OLAP operations.

The index server performs session management, authorization, transaction management and command processing. The database has both a row store and a columnar store. Users can create tables using either store, but the columnar store has more capabilities and is most frequently used. The index server also manages persistence between cached memory images of database objects, log files and permanent storage files. The XS engine allows web applications to be built.

SAP HANA Information Modeling (also known as SAP HANA Data Modeling) is a part of HANA application development. Modeling is the methodology to expose operational data to the end user. Reusable virtual objects (named calculation views) are used in the modelling process.

### MVCC

SAP HANA manages concurrency through the use of multiversion concurrency control (MVCC), which gives every transaction a snapshot of the database at a point in time. When an MVCC database needs to update an item of data, it will not overwrite the old data with new data, but will instead mark the old data as obsolete and add the newer version.

## Big data

In a scale-out environment, HANA can keep volumes of up to a petabyte of data in memory while returning query results in under a second. However, RAM is still much more expensive than disk space, so the scale-out approach is only feasible for certain time critical use cases.

## Analytics

SAP HANA includes a number of analytic engines for various kinds of data processing. The Business Function Library includes a number of algorithms made available to address common business data processing algorithms such as asset depreciation, rolling forecast and moving average. The Predictive Analytics Library includes native algorithms for calculating common statistical measures in areas such as clustering, classification and time series analysis.

HANA incorporates the open source statistical programming language R as a supported language within stored procedures.

The column-store database offers graph database capabilities. The graph engine processes the Cypher Query Language and also has a visual graph manipulation via a tool called Graph Viewer. Graph data structures are stored directly in relational tables in HANA's column store. Pre-built algorithms in the graph engine include pattern matching, neighborhood search, single shortest path, and strongly connected components. Typical usage situations for the Graph Engine include examples like supply chain traceability, fraud detection, and logistics and route planning.

HANA also includes a spatial database engine which implements spatial data types and SQL extensions for CRUD operations on spatial data. HANA is certified by the Open Geospatial Consortium, and it integrates with ESRI's ArcGIS geographic information system.

In addition to numerical and statistical algorithms, HANA can perform text analytics and enterprise text search. HANA's search capability is based on “fuzzy” fault-tolerant search, much like modern web-based search engines. Results include a statistical measure for how relevant search results are, and search criteria can include a threshold of accuracy for results. Analyses available include identifying entities such as people, dates, places, organizations, requests, problems, and more. Such entity extraction can be catered to specific use cases such as Voice of the Customer (customer's preferences and expectations), Enterprise (i.e. mergers and acquisitions, products, organizations), and Public Sector (public persons, events, organizations). Custom extraction and dictionaries can also be implemented.

## Application development

Besides the database and data analytics capabilities, SAP HANA is a web-based application server, hosting user-facing applications tightly integrated with the database and analytics engines of HANA. The "XS Advanced Engine" (XSA) natively works with Node.js and JavaEE languages and runtimes. XSA is based on Cloud Foundry architecture and thus supports the notion of “Bring Your Own Language”, allowing developers to develop and deploy applications written in languages and in runtimes other than those XSA implements natively, as well as deploying applications as microservices. XSA also allows server-side JavaScript with SAP HANA XS Javascript (XSJS).

Supporting the application server is a suite of application lifecycle management tools allowing development deployment and monitoring of user-facing applications.

## Deployment

HANA can be deployed on-premises or in the cloud from a number of cloud service providers.

HANA can be deployed on-premises as a new appliance from a certified hardware vendor. Alternatively, existing hardware components such as storage and network can be used as part of the implementation, an approach which SAP calls "Tailored Data Center Integration (TDI)". HANA is certified to run on multiple operating systems including SUSE Linux Enterprise Server and Red Hat Enterprise Linux. Supported hardware platforms for on-premise deployment include Intel 64 and POWER Systems. The system is designed to support both horizontal and vertical scaling.

Multiple cloud providers offer SAP HANA on an Infrastructure as a Service basis, including:

- SAP Cloud Infrastructure
- Amazon Web Services
- Microsoft Azure
- Google Cloud Platform
- IBM Softlayer
- Huawei FusionSphere

SAP also offer their own cloud services in the form of:

- SAP HANA Enterprise Cloud, a private managed cloud
- SAP Business Technology Platform (previously known as SAP Cloud Platform and HANA Cloud Platform), Platform as a service

## Editions

SAP HANA licensing is primarily divided into two categories.

**Runtime License:**

Used to run SAP applications such as SAP Business Warehouse powered by SAP HANA and SAP S/4HANA.

**Full Use License:**

Used to run both SAP and non-SAP applications. This licensing can be used to create custom applications.

As part of the full use license, features are grouped as editions targeting various use cases.

- **Base Edition:** Provides core database features and development tools but does not support SAP applications.
- **Platform Edition:** Base edition plus spatial, predictive, R server integration, search, text, analytics, graph engines and additional packaged business libraries.
- **Enterprise Edition:** Platform edition plus additional bundled components for some of the data loading capabilities and the rule framework.

In addition, capabilities such as streaming and ETL are licensed as additional options.

As of March 9, 2017, SAP HANA is available in an **Express Edition**; a streamlined version which can run on laptops and other resource-limited environments. The license for SAP HANA, express edition is free of charge, even for productive use up to 32 GB of RAM. Additional capacity increases can be purchased up to 128 GB of RAM.
