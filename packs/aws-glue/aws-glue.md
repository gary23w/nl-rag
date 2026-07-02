---
title: "AWS Glue"
source: https://en.wikipedia.org/wiki/AWS_Glue
domain: aws-glue
license: CC-BY-SA-4.0
tags: aws glue, amazon glue, managed etl service, serverless data integration
fetched: 2026-07-02
---

# AWS Glue

**AWS Glue** is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It was introduced in August 2017.

## Overview

The primary purpose of Glue is to scan other services in the same Virtual Private Cloud (or equivalent accessible network element even if not provided by AWS), particularly S3. The jobs are billed according to compute time, with a minimum count of 1 minute. Glue discovers the source data to store associated meta-data (e.g. the table's schema of field names, types lengths) in the AWS Glue Data Catalog (which is then accessible via AWS console or APIs).

## Languages supported

Scala and Python are officially supported as of 2020.

## Catalog interrogation via API

The catalog can be read in AWS console (via browser) and via API divided into topics including:

- Database API
- Table API
- Partition API
- Connection API
- User-Defined Function API
- Importing an Athena Catalog to AWS Glue
