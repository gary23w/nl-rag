---
title: "Apache Beam"
source: https://en.wikipedia.org/wiki/Apache_Beam
domain: apache-beam
license: CC-BY-SA-4.0
tags: apache beam, dataflow programming, unified batch streaming, data pipeline, windowing semantics
fetched: 2026-07-02
---

# Apache Beam

**Apache Beam** is an open source unified programming model to define and execute data processing pipelines, including ETL, batch and stream (continuous) processing. Beam Pipelines are defined using one of the provided SDKs and executed in one of the Beam's supported *runners* (distributed processing back-ends) including Apache Flink, Apache Samza, Apache Spark, and Google Cloud Dataflow.

## History

Apache Beam is one implementation of the Dataflow model paper. The Dataflow model is based on previous work on distributed processing abstractions at Google, in particular on FlumeJava and Millwheel.

Google released an open SDK implementation of the Dataflow model in 2014 and an environment to execute Dataflows locally (non-distributed) as well as in the Google Cloud Platform service.

### Timeline

Apache Beam makes minor releases every 6 weeks.

| Version | Release date |
|---|---|
| Latest version: 2.74.0 | 2026-06-02 |
| Supported: 2.73.0 | 2026-04-29 |
| Supported: 2.72.0 | 2026-03-30 |
| Supported: 2.71.0 | 2026-01-22 |
| Supported: 2.70.0 | 2025-12-16 |
| Supported: 2.69.0 | 2025-10-28 |
| Supported: 2.68.0 | 2025-09-22 |
| Supported: 2.67.0 | 2025-08-12 |
| Supported: 2.66.0 | 2025-07-01 |
| Supported: 2.65.0 | 2025-05-12 |
| Supported: 2.64.0 | 2025-03-31 |
| Supported: 2.63.0 | 2025-02-18 |
| Supported: 2.62.0 | 2025-01-21 |
| Supported: 2.61.0 | 2024-11-25 |
| Supported: 2.60.0 | 2024-10-17 |
| Supported: 2.59.0 | 2024-09-11 |
| Supported: 2.58.1 | 2024-08-15 |
| Supported: 2.58.0 | 2024-08-06 |
| Supported: 2.57.0 | 2024-06-26 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |

| Version | Release date |
|---|---|
| Unsupported: 2.56.0 | 2024-05-01 |
| Unsupported: 2.55.0 | 2024-03-25 |
| Unsupported: 2.54.0 | 2024-02-14 |
| Unsupported: 2.53.0 | 2024-01-04 |
| Unsupported: 2.52.0 | 2023-11-17 |
| Unsupported: 2.51.0 | 2023-10-11 |
| Unsupported: 2.50.0 | 2023-08-30 |
| Unsupported: 2.49.0 | 2023-07-17 |
| Unsupported: 2.48.0 | 2023-05-31 |
| Unsupported: 2.47.0 | 2023-05-10 |
| Unsupported: 2.46.0 | 2023-03-10 |
| Unsupported: 2.45.0 | 2023-02-15 |
| Unsupported: 2.44.0 | 2023-01-12 |
| Unsupported: 2.43.0 | 2022-11-17 |
| Unsupported: 2.42.0 | 2022-10-17 |
| Unsupported: 2.41.0 | 2022-08-23 |
| Unsupported: 2.40.0 | 2022-06-27 |
| Unsupported: 2.39.0 | 2022-05-25 |
| Unsupported: 2.38.0 | 2022-04-20 |
| Unsupported: 2.37.0 | 2022-03-04 |
| Unsupported: 2.36.0 | 2022-02-07 |
| Unsupported: 2.35.0 | 2021-12-29 |
| Unsupported: 2.34.0 | 2021-11-11 |
| Unsupported: 2.33.0 | 2021-10-07 |
| Unsupported: 2.32.0 | 2021-08-25 |
| Unsupported: 2.31.0 | 2021-07-08 |
| Unsupported: 2.30.0 | 2021-06-09 |
| Unsupported: 2.29.0 | 2021-04-27 |
| Unsupported: 2.28.0 | 2021-02-22 |
| Unsupported: 2.27.0 | 2021-01-08 |
| Unsupported: 2.26.0 | 2020-12-11 |
| Unsupported: 2.25.0 | 2020-10-23 |
| Unsupported: 2.24.0 | 2020-09-18 |
| Unsupported: 2.23.0 | 2020-07-29 |
| Unsupported: 2.22.0 | 2020-06-08 |
| Unsupported: 2.21.0 | 2020-05-27 |
| Unsupported: 2.20.0 | 2020-04-15 |
| Unsupported: 2.19.0 | 2020-02-04 |
| Unsupported: 2.18.0 | 2020-01-23 |
| Unsupported: 2.17.0 | 2020-01-06 |
| Unsupported: 2.16.0 | 2019-10-07 |
| Unsupported: 2.15.0 | 2019-08-22 |
| Unsupported: 2.14.0 | 2019-08-01 |
| Unsupported: 2.13.0 | 2019-05-22 |
| Unsupported: 2.12.0 | 2019-04-25 |
| Unsupported: 2.11.0 | 2019-02-26 |
| Unsupported: 2.10.0 | 2019-02-01 |
| Unsupported: 2.9.0 | 2018-12-13 |
| Unsupported: 2.8.0 | 2018-10-29 |
| Unsupported: 2.7.0 (LTS) | 2018-10-03 |
| Unsupported: 2.6.0 | 2018-08-08 |
| Unsupported: 2.5.0 | 2018-06-26 |
| Unsupported: 2.4.0 | 2018-03-20 |
| Unsupported: 2.3.0 | 2018-01-30 |
| Unsupported: 2.2.0 | 2017-12-02 |
| Unsupported: 2.1.0 | 2017-08-23 |
| Unsupported: 2.0.0 | 2017-05-17 |
| Unsupported: 0.6.0 | 2017-03-11 |
| Unsupported: 0.5.0 | 2017-02-02 |
| Unsupported: 0.4.0 | 2016-12-29 |
| Unsupported: 0.3.0 | 2016-10-31 |
| Unsupported: 0.2.0 | 2016-08-08 |
| Unsupported: 0.1.0 | 2016-06-15 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |
