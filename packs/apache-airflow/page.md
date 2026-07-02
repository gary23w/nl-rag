---
title: "Documentation"
source: https://airflow.apache.org/docs/
domain: apache-airflow
license: CC-BY-SA-4.0
tags: apache airflow, workflow orchestration, directed acyclic graph, task scheduling, pipeline automation
fetched: 2026-07-02
---

# Documentation

## Apache Airflow®

Apache Airflow Core, which includes webserver, scheduler, CLI and other components that are needed for minimal Airflow installation. Read Apache Airflow documentation »

## Apache Airflow CTL (airflowctl)

Apache Airflow CTL (airflowctl) is a command-line interface (CLI) for Apache Airflow that interacts exclusively with the Airflow REST API. It provides a secure, auditable, and consistent way to manage Airflow deployments — without direct access to the metadata database. Read airflowctl documentation »

## Task SDK

The Task SDK provides python-native interfaces for defining DAGs, executing tasks in isolated subprocesses and interacting with Airflow resources (e.g., Connections, Variables, XComs, Metrics, Logs, and OpenLineage events) at runtime. The goal of task-sdk is to decouple DAG authoring from Airflow internals (Scheduler, API Server, etc.), providing a forward-compatible, stable interface for writing and maintaining DAGs across Airflow versions. Read Task SDK documentation »

## Docker stack

Airflow has an official Dockerfile and Docker image published in DockerHub as a convenience package for installation. You can extend and customize the image according to your requirements and use it in your own deployments. Read Docker stack documentation »

## Helm Chart

Airflow has an official Helm Chart that will help you set up your own Airflow on a cloud/on-prem Kubernetes environment and leverage its scalable nature to support a large group of users. Thanks to Kubernetes, we are not tied to a specific cloud provider. Read Helm Chart documentation »

## Python API Client

Airflow releases official Python API client that can be used to easily interact with Airflow REST API from Python code. See the client repository

## Providers packages

Providers packages include integrations with third party projects. They are versioned and released independently of the Apache Airflow core. Read Providers documentation »

### Active providers

- `Airbyte`
- `Akeyless`
- `Alibaba`
- `Amazon`
- `Apache Beam`
- `Apache Cassandra`
- `Apache Drill`
- `Apache Druid`
- `Apache Flink`
- `Apache HDFS`
- `Apache Hive`
- `Apache Iceberg`
- `Apache Impala`
- `Apache Kafka`
- `Apache Kylin`
- `Apache Livy`
- `Apache Pig`
- `Apache Pinot`
- `Apache Spark`
- `Apache Tinkerpop`
- `Apprise`
- `ArangoDB`
- `Asana`
- `Atlassian Jira`
- `Celery`
- `ClickHouse`
- `Cloudant`
- `CNCF Kubernetes`
- `Cohere`
- `Common AI`
- `Common Compat`
- `Common IO`
- `Common Messaging`
- `Common SQL`
- `Databricks`
- `Datadog`
- `dbt Cloud`
- `Dingding`
- `Discord`
- `Docker`
- `Edge3`
- `Elasticsearch`
- `Exasol`
- `FAB (Flask-AppBuilder)`
- `Facebook`
- `File Transfer Protocol (FTP)`
- `Git`
- `GitHub`
- `Google`
- `gRPC`
- `Hashicorp`
- `Hypertext Transfer Protocol (HTTP)`
- `IBM Cloudant`
- `Influx DB`
- `Informatica`
- `Internet Message Access Protocol (IMAP)`
- `Java Database Connectivity (JDBC)`
- `Jenkins`
- `Keycloak`
- `Microsoft Azure`
- `Microsoft SQL Server (MSSQL)`
- `Microsoft PowerShell Remoting Protocol (PSRP)`
- `Microsoft Windows Remote Management (WinRM)`
- `MongoDB`
- `MySQL`
- `Neo4j`
- `ODBC`
- `OpenAI`
- `OpenFaaS`
- `OpenLineage`
- `Open Search`
- `Opsgenie`
- `Oracle`
- `Pagerduty`
- `Papermill`
- `PgVector`
- `Pinecone`
- `PostgreSQL`
- `Presto`
- `Qdrant`
- `Redis`
- `Salesforce`
- `Samba`
- `Segment`
- `Sendgrid`
- `SFTP`
- `Singularity`
- `Slack`
- `SMTP`
- `Snowflake`
- `SQLite`
- `SSH`
- `Standard`
- `Tableau`
- `Telegram`
- `Teradata`
- `Trino`
- `Vertica`
- `Vespa`
- `Weaviate`
- `Yandex`
- `YDB`
- `Zendesk`

### Suspended providers

These providers are currently suspended from releases and we are not actively testing their compatibility with latest Airflow releases. You can still use the released versions of these providers if you need to and in case the reason for suspension is resolved, the provider might be resumed by a PR of a community member who will resolve the suspension reason. It the provider is suspended for quite some time, the community might make a decision about removing it.

More about the suspension/resuming process can be found in the Community provider’s lifecycle documentation page.

- No suspended providers at the moment

### Removed providers

These providers are no longer supported and have been removed from the codebase, you can however still use the released versions of these providers if you need to.

More about the removal process can be found in the Community provider’s lifecycle documentation page.

- `Apache Sqoop`
- `Dask Executor`
- `Plexus`
- `Qubole`
- `Tabular`
