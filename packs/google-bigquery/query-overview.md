---
title: "Overview of BigQuery analytics"
source: https://cloud.google.com/bigquery/docs/query-overview
domain: google-bigquery
license: CC-BY-SA-4.0
tags: bigquery, google bigquery, cloud data warehouse, massively parallel processing
fetched: 2026-07-02
---

# Overview of BigQuery analytics

Stay organized with collections

Save and categorize content based on your preferences.

# Overview of BigQuery analytics

This document provides an overview of how BigQuery processes queries and an overview of several features that are useful for understanding and analyzing your data.

BigQuery is optimized to run analytic queries on large datasets, including terabytes of data in seconds and petabytes in minutes. Understanding BigQuery capabilities and how it processes queries can help you maximize your data analysis investments.

## Analytic workflows

BigQuery supports several data analysis workflows:

- **Ad hoc analysis.** BigQuery uses GoogleSQL, the SQL dialect in BigQuery, to support ad hoc analysis. You can run queries in the Google Cloud console or through third-party tools that integrate with BigQuery.
- **Geospatial analysis.** BigQuery uses geography data types and GoogleSQL geography functions to let you analyze and visualize geospatial data. For information about these data types and functions, see Introduction to geospatial analytics.
- **Graph analysis.** BigQuery Graph lets you model your data as a graph with nodes and edges. You can use Graph Query Language (GQL) to find complex, hidden relationships between data points that would be challenging to find using SQL.
- **Search for data.** You can index your data to perform flexible, optimized searches on unstructured text or semi-structured JSON data.
- **Search for Google Cloud resources.** Use natural language search (Preview) to discover Google Cloud resources from within BigQuery.
- **Machine learning.** BigQuery ML uses GoogleSQL queries to let you create and execute machine learning (ML) models in BigQuery.
- **Business intelligence.** BigQuery BI Engine is a fast, in-memory analysis service that lets you build rich, interactive dashboards and reports without compromising performance, scalability, security, or data freshness.
- **AI assistance.** You can use Gemini in BigQuery to prepare and explore your data, generate SQL queries and Python code, and visualize your results.

## Data exploration

BigQuery can help you understand your data before you start writing SQL queries. Use the following features if you want to find data, are unfamiliar with your data, don't know which questions to ask, or need help writing SQL:

- **Knowledge Catalog.** Find Google Cloud resources from within BigQuery, such as datasets and tables.
- **Table explorer.** Visually explore the range and frequency of values in your table and interactively build queries.
- **Data insights.** Generate natural language questions about your data, along with the SQL queries to answer those questions.
- **Data profile scan.** See statistical characteristics of your data, including average, unique, maximum, and minimum values.
- **Data canvas.** Query your data using natural language, visualize results with charts, and ask follow-up questions.

## Queries

The primary way to analyze data in BigQuery is to run a SQL query. The GoogleSQL dialect supports SQL:2011 and includes extensions that support geospatial analysis and ML.

### Data sources

BigQuery lets you query the following types of data sources:

- **Data stored in BigQuery.** You can load data into BigQuery, modify existing data by using data manipulation language (DML) statements, or write query results to a table. You can query historical data from a point in time within your time travel window. You can query data stored in single-region or multi-region locations. A query that accesses data stored in more than one location can be treated as a global query (Preview). Queries that reference data in multiple locations are always treated as global queries, even if one region is a single-region location and the other is a multi-region location that contains the single-region location.
- **External data.** You can query various external data sources such as Cloud Storage, or database services such as Spanner or Cloud SQL. For information about how to set up connections to external sources, see Introduction to external data sources
- **Multi-cloud data.** You can query data that's stored in other public clouds such as AWS or Azure. For information on how to set up connections to Amazon Simple Storage Service (Amazon S3) or Azure Blob Storage, see Introduction to BigQuery Omni.
- **Public datasets.** You can analyze any of the datasets that are available in the public dataset marketplace.
- **BigQuery sharing (formerly Analytics Hub).** You can publish and subscribe to BigQuery datasets and Pub/Sub topics to share data across organizational boundaries. For more information, see Introduction to BigQuery sharing.

### Types of queries

You can query BigQuery data by using one of the following query job types:

- **Interactive query jobs**. By default, BigQuery runs queries as interactive query jobs, which are intended to start executing as quickly as possible.
- **Batch query jobs**. Batch queries have lower priority than interactive queries. When a project or reservation is using all of its available compute resources, batch queries are more likely to be queued and remain in the queue. After a batch query starts running, the batch query runs the same as an interactive query. For more information, see query queues.
- **Continuous query jobs**. With these jobs, the query runs continuously, letting you analyze incoming data in BigQuery in real time and then write the results to a BigQuery table, or export the results to Bigtable or Pub/Sub. You can use this capability to perform time sensitive tasks, such as creating and immediately acting on insights, applying real time machine learning (ML) inference, and building event-driven data pipelines.

You can run query jobs by using the following methods:

- Compose and run a query in the Google Cloud console.
- Run the `bq query` command in the bq command-line tool.
- Programmatically call the `jobs.query` or `jobs.insert` method in the BigQuery REST API.
- Use the BigQuery client libraries.

### Multi-statement queries

You can run multiple statements in a sequence, with shared state, by using multi-statement queries. Multi-statement queries are often used in stored procedures and support procedural language statements, which let you define variables and implement control flow.

### Saved and shared queries

BigQuery lets you save queries and share queries with others.

When you save a query, it can be private (visible only to you), shared at the project level (visible to specific principals), or public (anyone can view it). For more information, see Work with saved queries.

### How BigQuery processes queries

Several processes occur when BigQuery runs a query:

- **Execution tree.** When you run a query, BigQuery generates an *execution tree* that breaks the query into stages. These stages contain steps that can run in parallel.
- **Shuffle tier.** Stages communicate with one another by using a fast, distributed *shuffle tier* that stores intermediate data produced by the workers of a stage. When possible, the shuffle tier leverages technologies such as a petabit network and RAM to quickly move data to worker nodes.
- **Query plan.** When BigQuery has all the information that it needs to run a query, it generates a *query plan*. You can view the query plan in the Google Cloud console and use it to troubleshoot or optimize query performance.
- **Query execution graph.** You can review the query plan information in graphical format for any query, whether running or completed, and see performance insights to help you optimize your queries.
- **Query monitoring and dynamic planning.** Besides the workers that perform the work of the query plan itself, additional workers monitor and direct the overall progress of work throughout the system. As the query progresses, BigQuery might dynamically adjust the query plan to adapt to the results of the various stages.
- **Query results.** When a query is complete, BigQuery writes the results to persistent storage and returns them to the user. This design lets BigQuery serve cached results the next time that query is run.

### Query concurrency and performance

The performance of queries that are run repeatedly on the same data can vary because of the shared nature of the BigQuery environment, use of cached query results, or because BigQuery dynamically adjusts the query plan while the query runs. For a typical busy system where many queries run concurrently, BigQuery uses several processes to smooth out variances in query performance:

- BigQuery runs many queries in parallel and can queue queries to run when resources are available.
- As queries start and finish, BigQuery redistributes resources fairly between new and running queries. This process ensures that query performance doesn't depend on the order in which queries are submitted but rather on the number of queries run at a given time.

### Query optimization

When you run a query, you can view the query plan in the Google Cloud console. You can also request execution details by using the `INFORMATION_SCHEMA.JOBS*` views or the `jobs.get` REST API method.

The query plan includes details about query stages and steps. These details can help you identify ways to improve query performance. For example, if you notice a stage that writes a lot more output than other stages, it might mean that you need to filter earlier in the query.

For more information about the query plan and query optimization, see the following resources:

- To learn more about the query plan and see examples of how the plan information can help you to improve query performance, see Query plan and timeline.
- For more information about query optimization in general, see Introduction to optimizing query performance.

### Query monitoring

Monitoring and logging are crucial for running reliable applications in the cloud. BigQuery workloads are no exception, especially if your workload has high volumes or is mission critical. BigQuery provides various metrics, logs, and metadata views to help you monitor your BigQuery usage.

For more information, see the following resources:

- To learn about monitoring options in BigQuery, see Introduction to BigQuery monitoring.
- To learn about audit logs and how to analyze query behavior, see BigQuery audit logs.

### Query pricing

BigQuery offers two pricing models for analytics:

- **On-demand pricing.** You pay for the data scanned by your queries. You have a fixed, query-processing capacity for each project, and your cost is based on the number of bytes processed.
- **Capacity-based pricing.** You purchase dedicated query-processing capacity.

For information about the two pricing models and to learn more about making reservations for capacity-based pricing, see Introduction to reservations.

### Quotas and query cost controls

BigQuery enforces project-level quotas on running queries. For information on query quotas, see Quotas and limits.

To control query costs, BigQuery provides several options, including custom quotas and billing alerts. For more information, see Creating custom cost controls.

## Data analytics features

BigQuery supports both descriptive and predictive analytics and helps you explore your data with AI powered tools, SQL, machine learning, notebooks, and other third-party integrations.

### BigQuery Studio

BigQuery Studio helps you discover, analyze, and run inference on data in BigQuery with the following features:

- A robust SQL editor that provides code completion and generation, query validation, and estimation of bytes processed.
- Embedded Python notebooks built using Colab Enterprise. Notebooks provide one-click Python development runtimes, and built-in support for BigQuery DataFrames.
- A PySpark editor that lets you create stored Python procedures for Apache Spark.
- Asset management and version history for code assets such as notebooks and saved queries, built on top of Dataform.
- Assistive code development in the SQL editor and in notebooks, built on top of Gemini generative AI (Preview).
- Knowledge Catalog features for data discovery, and data profiling and data quality scans.
- The ability to view job history on a per-user or per-project basis.
- The ability to analyze saved query results by connecting to other tools such as Looker and Google Sheets, and to export saved query results for use in other applications.

### BigQuery ML

BigQuery ML lets you use SQL in BigQuery to perform machine learning (ML) and predictive analytics. For more information, see Introduction to BigQuery ML.

The Conversational Analytics Agent lets you chat with your data using conversational language. This agent consists of one or more data sources and a set of use case-specific instructions for processing that data. Conversation analytics supports the use of some BigQuery ML functions.

### Analytics tools integration

In addition to running queries in BigQuery, you can analyze your data with various analytics and business intelligence tools that integrate with BigQuery, such as the following:

- **Looker.** Looker is an enterprise platform for business intelligence, data applications, and embedded analytics. The Looker platform works with many datastores including BigQuery. For information on how to connect Looker to BigQuery, see Using Looker.
- **Data Studio.** After you run a query, you can launch Data Studio directly from BigQuery in the Google Cloud console. Then, in Data Studio you can create visualizations and explore the data that's returned from the query. For information about Data Studio, see Data Studio overview.
- **Connected Sheets.** You can also launch Connected Sheets directly from BigQuery in the console. Connected Sheets runs BigQuery queries on your behalf either upon your request or on a defined schedule. Results of those queries are saved in your spreadsheet for analysis and sharing. For information about Connected Sheets, see Using connected sheets.
- **Tableau.** You can connect to a dataset from Tableau. Use BigQuery to power your charts, dashboards, and other data visualizations.

### Third-party tool integration

Several third-party analytics tools work with BigQuery. For example, you can connect Tableau to BigQuery data and use its visualization tools to analyze and share your analysis. For more information on considerations when using third-party tools, see Third-party tool integration.

ODBC and JDBC drivers are available and can be used to integrate your application with BigQuery. The intent of these drivers is to help users leverage the power of BigQuery with existing tooling and infrastructure. For information on latest release and known issues, see ODBC and JDBC drivers for BigQuery.

The pandas libraries like `pandas-gbq` let you interact with BigQuery data in Jupyter notebooks. For information about this library and how it compares with using the BigQuery Python client library, see Comparison with `pandas-gbq`.

You can also use BigQuery with other notebooks and analysis tools. For more information, see Programmatic analysis tools.

For a full list of BigQuery analytics and broader technology partners, see the Partners list on the BigQuery product page.

## What's next

- For an introduction and overview of supported SQL statements, see Introduction to SQL in BigQuery.
- To learn about the GoogleSQL syntax used for querying data in BigQuery, see Query syntax in GoogleSQL.
- Learn how to run a query in BigQuery.
- Learn more about optimizing query performance.
- Learn about getting started with notebooks.
- Learn how to schedule a recurring query.

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-29 UTC.
