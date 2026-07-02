---
title: "SQLAlchemy Unified Tutorial"
source: https://docs.sqlalchemy.org/en/20/tutorial/index.html
domain: sqlalchemy-core
license: CC-BY-SA-4.0
tags: python sqlalchemy, sqlalchemy orm, database toolkit python
fetched: 2026-07-02
---

# SQLAlchemy Unified Tutorial

Release:

2.0.51

| Release Date: June 15, 2026

# SQLAlchemy 2.0 Documentation

- **Previous:** Overview
- **Next:** Establishing Connectivity - the Engine
- **Up:** Home
- **On this page:**

# SQLAlchemy Unified Tutorial

About this document

The SQLAlchemy Unified Tutorial is integrated between the Core and ORM components of SQLAlchemy and serves as a unified introduction to SQLAlchemy as a whole. For users of SQLAlchemy within the 1.x series, in the 2.0 style of working, the ORM uses Core-style querying with the `select()` construct, and transactional semantics between Core connections and ORM sessions are equivalent. Take note of the blue border styles for each section, that will tell you how “ORM-ish” a particular topic is!

Users who are already familiar with SQLAlchemy, and especially those looking to migrate existing applications to work under the SQLAlchemy 2.0 series within the 1.4 transitional phase should check out the SQLAlchemy 2.0 - Major Migration Guide document as well.

For the newcomer, this document has a **lot** of detail, however by the end they will be considered an **Alchemist**.

SQLAlchemy is presented as two distinct APIs, one building on top of the other. These APIs are known as **Core** and **ORM**.

**SQLAlchemy Core** is the foundational architecture for SQLAlchemy as a “database toolkit”. The library provides tools for managing connectivity to a database, interacting with database queries and results, and programmatic construction of SQL statements.

Sections that are **primarily Core-only** will not refer to the ORM. SQLAlchemy constructs used in these sections will be imported from the `sqlalchemy` namespace. As an additional indicator of subject classification, they will also include a **dark blue border on the right**. When using the ORM, these concepts are still in play but are less often explicit in user code. ORM users should read these sections, but not expect to be using these APIs directly for ORM-centric code.

**SQLAlchemy ORM** builds upon the Core to provide optional **object relational mapping** capabilities. The ORM provides an additional configuration layer allowing user-defined Python classes to be **mapped** to database tables and other constructs, as well as an object persistence mechanism known as the **Session**. It then extends the Core-level SQL Expression Language to allow SQL queries to be composed and invoked in terms of user-defined objects.

Sections that are **primarily ORM-only** should be **titled to include the phrase “ORM”**, so that it’s clear this is an ORM related topic. SQLAlchemy constructs used in these sections will be imported from the `sqlalchemy.orm` namespace. Finally, as an additional indicator of subject classification, they will also include a **light blue border on the left**. Core-only users can skip these.

**Most** sections in this tutorial discuss **Core concepts that are also used explicitly with the ORM**. SQLAlchemy 2.0 in particular features a much greater level of integration of Core API use within the ORM.

For each of these sections, there will be **introductory text** discussing the degree to which ORM users should expect to be using these programming patterns. SQLAlchemy constructs in these sections will be imported from the `sqlalchemy` namespace with some potential use of `sqlalchemy.orm` constructs at the same time. As an additional indicator of subject classification, these sections will also include **both a thinner light border on the left, and a thicker dark border on the right**. Core and ORM users should familiarize with concepts in these sections equally.

## Tutorial Overview

The tutorial will present both concepts in the natural order that they should be learned, first with a mostly-Core-centric approach and then spanning out into more ORM-centric concepts.

The major sections of this tutorial are as follows:

- Establishing Connectivity - the Engine - all SQLAlchemy applications start with an `Engine` object; here’s how to create one.
- Working with Transactions and the DBAPI - the usage API of the `Engine` and its related objects `Connection` and `Result` are presented here. This content is Core-centric however ORM users will want to be familiar with at least the `Result` object.
- Working with Database Metadata - SQLAlchemy’s SQL abstractions as well as the ORM rely upon a system of defining database schema constructs as Python objects. This section introduces how to do that from both a Core and an ORM perspective.
- Working with Data - here we learn how to create, select, update and delete data in the database. The so-called CRUD operations here are given in terms of SQLAlchemy Core with links out towards their ORM counterparts. The SELECT operation that is introduced in detail at Using SELECT Statements applies equally well to Core and ORM.
- Data Manipulation with the ORM covers the persistence framework of the ORM; basically the ORM-centric ways to insert, update and delete, as well as how to handle transactions.
- Working with ORM Related Objects introduces the concept of the `relationship()` construct and provides a brief overview of how it’s used, with links to deeper documentation.
- Further Reading lists a series of major top-level documentation sections which fully document the concepts introduced in this tutorial.

### Version Check

This tutorial is written using a system called doctest. All of the code excerpts written with a `>>>` are actually run as part of SQLAlchemy’s test suite, and the reader is invited to work with the code examples given in real time with their own Python interpreter.

If running the examples, it is advised that the reader performs a quick check to verify that we are on **version 2.0** of SQLAlchemy:

```pycon+sql
>>> import sqlalchemy
>>> sqlalchemy.__version__  
2.0.0
```

Previous:

Overview

Next:

Establishing Connectivity - the Engine

©

Copyright

2007-2026, the SQLAlchemy authors and contributors.

**flambé!** the dragon and ***The Alchemist*** image designs created and generously donated by Rotem Yaari.

Created using

Sphinx

9.1.0. Documentation last generated: Thu 25 Jun 2026 09:35:36 AM EDT
