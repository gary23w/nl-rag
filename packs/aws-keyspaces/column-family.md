---
title: "Column family"
source: https://en.wikipedia.org/wiki/Column_family
domain: aws-keyspaces
license: CC-BY-SA-4.0
tags: aws keyspaces, amazon keyspaces, managed cassandra, wide-column database service
fetched: 2026-07-02
---

# Column family

A **column family** is a database object that contains columns of related data. It is a tuple (pair) that consists of a key–value pair, where the key is mapped to a value that is a set of columns. In analogy with relational databases, a column family is as a "table", each key-value pair being a "row". Each column is a tuple (triplet) consisting of a column name, a value, and a timestamp. In a relational database table, this data would be grouped together within a table with other non-related data.

Two types of column families exist:

- Standard column family: contains only columns
- Super column family: contains a map of super columns
