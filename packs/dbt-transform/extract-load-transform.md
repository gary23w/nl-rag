---
title: "Extract, load, transform"
source: https://en.wikipedia.org/wiki/Extract,_load,_transform
domain: dbt-transform
license: CC-BY-SA-4.0
tags: data build tool, sql transformation, analytics engineering, elt modeling, materialized view
fetched: 2026-07-02
---

# Extract, load, transform

**Extract, load, transform** (**ELT**) is an alternative to extract, transform, load (ETL) used with data lake implementations. In contrast to ETL, in ELT models the data is not transformed on entry to the data lake, but stored in its original raw format. This enables faster loading times. However, ELT requires sufficient processing power within the data processing engine to carry out the transformation on demand, to return the results in a timely manner. Since the data is not processed on entry to the data lake, the query and schema do not need to be defined a priori (although often the schema will be available during load since many data sources are extracts from databases or similar structured data systems and hence have an associated schema). ELT is a data pipeline model.

## Benefits

Some of the benefits of an ELT process include speed and the ability to handle both structured and unstructured data.

## Cloud data lake components

### Common storage options

- AWS
  - Simple Storage Service (S3)
  - Amazon RDS
- Azure
  - Azure Blob Storage
- GCP
  - Google Storage (GCS)

### Querying

- AWS
  - Redshift Spectrum
  - Athena
  - EMR (Presto)
- Azure
  - Azure Data Lake
- GCP
  - BigQuery
