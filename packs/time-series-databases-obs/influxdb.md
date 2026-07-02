---
title: "InfluxDB"
source: https://en.wikipedia.org/wiki/InfluxDB
domain: time-series-databases-obs
license: CC-BY-SA-4.0
tags: time series storage, metrics retention downsampling, data point compaction, monitoring backend
fetched: 2026-07-02
---

# InfluxDB

**InfluxDB** is a time series database (TSDB) developed by the company InfluxData. It is used for storage and retrieval of time series data in fields such as operations monitoring, application metrics, Internet of Things sensor data, and real-time analytics. It also has support for processing data from Graphite.

The latest version of InfluxDB, 3.x, is written in the Rust programming language. Versions 1.x and 2.x are written in Go.

## History

Y Combinator-backed company Errplane began developing InfluxDB as an open-source project in late 2013 for performance monitoring and alerting. Errplane raised an $8.1M Series A financing led by Mayfield Fund and Trinity Ventures in November 2014. In late 2015, Errplane officially changed its name to InfluxData Inc. InfluxData raised Series B round of funding of $16 million in September 2016. In February 2018, InfluxData closed a $35 million Series C round of funding led by Sapphire Ventures. Another round of $60 million was disclosed in 2019. In February 2023, another $81 million was closed in a Series E round.

## Technical overview

InfluxDB provides an SQL-like language with built-in time-centric functions for querying a data structure composed of measurements, series, and points. Each point consists of several key-value pairs called the fieldset and a timestamp. When grouped together by a set of key-value pairs called the tagset, these define a series. Finally, series are grouped together by a string identifier to form a measurement.

Values can be 64-bit integers, 64-bit floating points, strings, and booleans. Points are indexed by their time and tagset. Retention policies are defined on a measurement and control how data is downsampled and deleted. Continuous Queries run periodically, storing results in a target measurement.

## Events

InfluxData regularly hosts events related to InfluxDB called InfluxDays. The InfluxDays are technical conventions focused on the evolution of InfluxDB on technical and business points of view. Those events take place once a year in three locations: New York, San Francisco or London. The InfluxDays cover a wide variety of different subjects: software engineering and coding talks as well as business-focused and practical workshops. Companies can showcase how they use InfluxDB.

## Line protocol

InfluxDB accepts data via HTTP, TCP, and UDP. It defines a line protocol backwards compatible with Graphite and takes the form:

measurement(,tag_key=tag_val)* field_key=field_val(,field_key_n=field_value_n)* (nanoseconds-timestamp)?

## Licensing

Contributors to InfluxDB need to give InfluxData Inc. the right to license the contributions and the rest of the software in any way, including under a closed-source license. The Contributor License Agreement claims not to be a copyright transfer agreement.

### Closed source clustering components

In May 2016, InfluxData announced that the computer cluster component of InfluxDB would be sold as closed-source software in order to create a sustainable source of funding for the project's development. Community reaction was mixed, with some feeling the move was a "bait and switch".

### InfluxDB 3 changes open source offerings

InfluxDB 3 Core is InfluxData's newest open source product and is intentionally designed to be an “edge data collector”, not a replacement for InfluxDB OSS v1 and v2. InfluxDB 3 Core has a 5 database limit and does not include a data compactor for fast historical querying.

In addition to InfluxDB 3 Core, InfluxDB 3 Enterprise is the commercial version of the open source core project.

Purchasing a software license for InfluxDB 3 Enterprise is required to replace InfluxDB OSS v1 and v2 functionality in a commercial setting, though a free version of InfluxDB 3 Enterprise is available for hobbyist and home use.
