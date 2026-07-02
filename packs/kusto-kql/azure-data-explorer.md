---
title: "Azure Data Explorer"
source: https://en.wikipedia.org/wiki/Azure_Data_Explorer
domain: kusto-kql
license: CC-BY-SA-4.0
tags: kusto query language, azure data explorer kql, log analytics query, tabular query language
fetched: 2026-07-02
---

# Azure Data Explorer

**Azure Data Explorer** is a fully-managed big data analytics cloud platform and data-exploration service, developed by Microsoft, that ingests structured, semi-structured (like JSON) and unstructured data (like free-text). The service then stores this data and answers analytic ad hoc queries on it with seconds of latency. It is a full-text indexing and retrieval database, including time series analysis capabilities and regular expression evaluation and text parsing.

It is offered as platform as a service (PaaS) as part of Microsoft Azure platform. The product was announced by Microsoft in 2018.

## History

The development of the product began in 2014 as a grassroots incubation project in the Israeli R&D center of Microsoft, with the internal code name 'Kusto' (named after Jacques Cousteau, as a reference to "exploring the ocean of data"). The project aim was to address Azure services' needs for fast and scalable log and telemetry analytics.

In 2016 it became the backend big-data and analytics service for Application Insights Analytics.

The product was announced as a Public Preview product at the Microsoft Ignite 2018 conference, and was announced as a generally available at the Microsoft Ignite conference of February 2019.

In March 2021, "Kusto EngineV3", Azure Data Explorer's next generation storage and query engine, became generally available. It was designed to provide unparalleled performance for ingesting and querying telemetry, logs, and time series data.

## Features

Azure Data Explorer offers an optimized query language and visualizing options of its data with a SQL-like language called KQL (Kusto Query Language).

Azure Data Explorer can ingest 200 MB per second per node. Data Ingestion methods are pipelines and connectors to common services like Azure Event Grid or Azure Event Hub, or programmatic ingestion using SDKs.

Data visualization can be achieved using their native dashboard offering, or with tools like Power BI or Grafana.

## Design

Azure Data Explorer is a distributed database running on a cluster of compute nodes in Microsoft Azure. It is based on relational database management systems (RDBMS), supporting entities such as databases, tables, functions, and columns. It supports complex analytics query operators, such as calculated columns, searching and filtering on rows, group by-aggregates and joins.

The engine service exposes a relational data model: At the top level (cluster) there is a collection of databases, each database contains a collection of tables and stored functions. Each table defines a schema (ordered list of typed fields).

In Azure Data Explorer, unlike a typical relational database management systems (RDBMS), there are no constraints like key uniqueness, primary and foreign key. The necessary relationships are established at query time. The data in Azure Data Explorer generally follows this pattern: Creating Database, Ingesting data, Query the database.
