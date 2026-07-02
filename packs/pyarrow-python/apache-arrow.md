---
title: "Apache Arrow"
source: https://en.wikipedia.org/wiki/Apache_Arrow
domain: pyarrow-python
license: CC-BY-SA-4.0
tags: python pyarrow, apache arrow python, columnar data python
fetched: 2026-07-02
---

# Apache Arrow

**Apache Arrow** is a language-agnostic software framework for developing data analytics applications that process columnar data. It contains a standardized column-oriented memory format that is able to represent flat and hierarchical data for efficient analytic operations on modern CPU and GPU hardware. This reduces or eliminates factors that limit the feasibility of working with large sets of data, such as the cost, volatility, or physical constraints of dynamic random-access memory.

## Interoperability

Arrow can be used with Apache Parquet, Apache Spark, NumPy, PySpark, pandas and other data processing libraries. The project includes native software libraries written in C, C++, C#, Go, Java, JavaScript, Julia, MATLAB, Python (PyArrow), R, Ruby, and Rust. Arrow allows for zero-copy reads and fast data access and interchange without serialization overhead between these languages and systems.

## Applications

Arrow has been used in diverse domains, including analytics, genomics, and cloud computing.

### Comparison to Apache Parquet and ORC

Apache Parquet and Apache ORC are popular examples of on-disk columnar data formats. Arrow is designed as a complement to these formats for processing data in-memory. The hardware resource engineering trade-offs for in-memory processing vary from those associated with on-disk storage. The Arrow and Parquet projects include libraries that allow for reading and writing data between the two formats.

## Governance

Apache Arrow was announced by The Apache Software Foundation on February 17, 2016, with development led by a coalition of developers from other open source data analytics projects. The initial codebase and Java library was seeded by code from Apache Drill.
