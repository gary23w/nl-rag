---
title: "MonetDB"
source: https://en.wikipedia.org/wiki/MonetDB
domain: monetdb
license: CC-BY-SA-4.0
tags: monetdb database, column-oriented dbms, in-memory analytics, columnar storage
fetched: 2026-07-02
---

# MonetDB

**MonetDB** is an open-source column-oriented relational database management system (RDBMS) originally developed at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. It is designed to provide high performance on complex SQL queries against large databases, such as combining tables with hundreds of columns and billions of rows. MonetDB has been applied in high-performance applications for online analytical processing, data mining, geographic information system (GIS), Resource Description Framework (RDF), text retrieval and sequence alignment processing.

## History

Data mining projects in the 1990s required improved analytical database support. This resulted in a CWI spin-off called Data Distilleries, which used early MonetDB implementations in its analytical suite. Data Distilleries eventually became a subsidiary of SPSS in 2003, which in turn was acquired by IBM in 2009.

MonetDB in its current form was first created in 2002 by doctoral student Peter Boncz and professor Martin L. Kersten as part of the 1990s' MAGNUM research project at University of Amsterdam. It was initially called simply Monet, after the French impressionist painter Claude Monet. The first version under an open-source software license (a modified version of the Mozilla Public License) was released on September 30, 2004. When MonetDB version 4 was released into the open-source domain, many extensions to the code base were added by the MonetDB/CWI team, including a new SQL front end, supporting the SQL:2003 standard.

MonetDB introduced innovations in all layers of the DBMS: a storage model based on vertical fragmentation, a modern CPU-tuned query execution architecture that often gave MonetDB a speed advantage over the same algorithm over a typical interpreter-based RDBMS. It was one of the first database systems to tune query optimization for CPU caches. MonetDB includes automatic and self-tuning indexes, run-time query optimization, and a modular software architecture.

By 2008, a follow-on project called X100 (MonetDB/X100) started, which evolved into the VectorWise technology. VectorWise was acquired by Actian Corporation, integrated with the Ingres database and sold as a commercial product.

In 2011 a major effort to renovate the MonetDB codebase was started. As part of it, the code for the MonetDB 4 kernel and its XQuery components were frozen. In MonetDB 5, parts of the SQL layer were pushed into the kernel. The resulting changes created a difference in internal APIs, as it transitioned from MonetDB Instruction Language (MIL) to MonetDB Assembly Language (MAL). Older, no-longer maintained top-level query interfaces were also removed. First was XQuery, which relied on MonetDB 4 and was never ported to version 5. The experimental Jaql interface support was removed with the October 2014 release. With the July 2015 release, MonetDB gained support for read-only data sharding and persistent indices. In this release the deprecated streaming data module DataCell was also removed from the main codebase in an effort to streamline the code. In addition, the license has been changed into the Mozilla Public License, version 2.0.

## Architecture

MonetDB architecture is represented in three layers, each with its own set of optimizers. The front end is the top layer, providing query interface for SQL, with SciQL and SPARQL interfaces under development. Queries are parsed into domain-specific representations, like relational algebra for SQL, and optimized. The generated logical execution plans are then translated into MonetDB Assembly Language (MAL) instructions, which are passed to the next layer. The middle or back-end layer provides a number of cost-based optimizers for the MAL. The bottom layer is the database kernel, which provides access to the data stored in Binary Association Tables (BATs). Each BAT is a table consisting of an Object-identifier and value columns, representing a single column in the database.

MonetDB internal data representation also relies on the memory addressing ranges of contemporary CPUs using demand paging of memory mapped files, and thus departing from traditional DBMS designs involving complex management of large data stores in limited memory.

### Query Recycling

Query recycling is an architecture for reusing the byproducts of the operator-at-a-time paradigm in a column store DBMS. Recycling makes use of the generic idea of storing and reusing the results of expensive computations. Unlike low-level instruction caches, query recycling uses an optimizer to pre-select instructions to cache. The technique is designed to improve query response times and throughput, while working in a self-organizing fashion. The authors from the CWI Database Architectures group, composed of Milena Ivanova, Martin Kersten, Niels Nes and Romulo Goncalves, won the "Best Paper Runner Up" at the ACM SIGMOD 2009 conference for their work on Query Recycling.

### Database Cracking

MonetDB was one of the first databases to introduce Database Cracking. Database Cracking is an incremental partial indexing and/or sorting of the data. It directly exploits the columnar nature of MonetDB. Cracking is a technique that shifts the cost of index maintenance from updates to query processing. The query pipeline optimizers are used to massage the query plans to crack and to propagate this information. The technique allows for improved access times and self-organized behavior. Database Cracking received the ACM SIGMOD 2011 J.Gray best dissertation award.

## Components

A number of extensions exist for MonetDB that extend the functionality of the database engine. Due to the three-layer architecture, top-level query interfaces can benefit from optimizations done in the backend and kernel layers.

### SQL

MonetDB/SQL is a top-level extension, which provides complete support for transactions in compliance with the SQL:2003 standard.

### GIS

MonetDB/GIS is an extension to MonetDB/SQL with support for the Simple Features Access standard of Open Geospatial Consortium (OGC).

### SciQL

SciQL an SQL-based query language for science applications with arrays as first class citizens. SciQL allows MonetDB to effectively function as an array database. SciQL is used in the European Union PlanetData Archived 2014-05-30 at the Wayback Machine and TELEIOS project, together with the Data Vault technology, providing transparent access to large scientific data repositories. Data Vaults map the data from the distributed repositories to SciQL arrays, allowing for improved handling of spatio-temporal data in MonetDB. SciQL will be further extended for the Human Brain Project.

### Data Vaults

Data Vault is a database-attached external file repository for MonetDB, similar to the SQL/MED standard. The Data Vault technology allows for transparent integration with distributed/remote file repositories. It is designed for scientific data data exploration and mining, specifically for remote sensing data. There is support for the GeoTIFF (Earth observation), FITS (astronomy), MiniSEED (seismology) and NetCDF formats. The data is stored in the file repository in the original format, and loaded in the database in a lazy fashion, only when needed. The system can also process the data upon ingestion, if the data format requires it. As a result, even very large file repositories can be efficiently analyzed, as only the required data is processed in the database. The data can be accessed through either the MonetDB SQL or SciQL interfaces. The Data Vault technology was used in the European Union's TELEIOS project, which was aimed at building a virtual observatory for Earth observation data. Data Vaults for FITS files have also been used for processing astronomical survey data for The INT Photometric H-Alpha Survey (IPHAS)

#### SAM/BAM

MonetDB has a SAM/BAM module for efficient processing of sequence alignment data. Aimed at the bioinformatics research, the module has a SAM/BAM data loader and a set of SQL UDFs for working with DNA data. The module uses the popular SAMtools library.

### RDF/SPARQL

MonetDB/RDF is a SPARQL-based extension for working with linked data, which adds support for RDF and allowing MonetDB to function as a triplestore. Under development for the Linked Open Data 2 project.

### R integration

**MonetDB/R** module allows for UDFs written in R to be executed in the SQL layer of the system. This is done using the native R support for running embedded in another application, inside the RDBMS in this case. Previously the **MonetDB.R** connector allowed the using MonetDB data sources and process them in an R session. The newer R integration feature of MonetDB does not require data to be transferred between the RDBMS and the R session, reducing overhead and improving performance. The feature is intended to give users access to functions of the R statistical software for in-line analysis of data stored in the RDBMS. It complements the existing support for C UDFs and is intended to be used for in-database processing.

### Python integration

Similarly to the embedded R UDFs in MonetDB, the database now has support for UDFs written in Python/NumPy. The implementation uses Numpy arrays (themselves Python wrappers for C arrays), as a result there is limited overhead - providing a functional Python integration with speed matching native SQL functions. The Embedded Python functions also support mapped operations, allowing user to execute Python functions in parallel within SQL queries. The practical side of the feature gives users access to Python/NumPy/SciPy libraries, which can provide a large selection of statistical/analytical functions.

### MonetDB embedded

Following the release of an embedded driver for R and R UDFs in MonetDB (MonetDB/R), the authors created an embedded version of MonetDB in R called **MonetDBLite**, embedded versions for Python and Java followed. They are distributed as embeddable packages, removing the need to manage a database server, required for the previous API integrations. The DBMS runs within the process itself, eliminating socket communication and serialisation overhead - greatly improving efficiency. The idea behind it is to easily embed an SQLite-like package with the performance of an in-memory optimized columnar store.

### Former extensions

A number of former extensions have been deprecated and removed from the stable code base over time. Some notable examples include an XQuery extension removed in MonetDB version 5; a JAQL extension, and a streaming data extension called *Data Cell*.

## MonetDB Foundation

The MonetDB Foundation is the independent non-profit organisation behind MonetDB. The foundation holds the intellectual property (IP) of MonetDB and is dedicated to advance the development and long-term maintenance of MonetDB. The foundation is funded by charitable donations.
