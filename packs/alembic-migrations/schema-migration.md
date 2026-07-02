---
title: "Schema migration"
source: https://en.wikipedia.org/wiki/Schema_migration
domain: alembic-migrations
license: CC-BY-SA-4.0
tags: python alembic, alembic migrations, schema migration python
fetched: 2026-07-02
---

# Schema migration

In software engineering, a **schema migration** (also **database migration**, **database change management**) refers to the management of version-controlled, incremental and sometimes reversible changes to relational database schemas. A schema migration is performed on a database whenever it is necessary to update or revert that database's schema to some newer or older version.

Migrations are performed programmatically by using a *schema migration tool*. When invoked with a specified desired schema version, the tool automates the successive application or reversal of an appropriate sequence of schema changes until it is brought to the desired state.

Most schema migration tools aim to minimize the impact of schema changes on any existing data in the database. Despite this, preservation of data in general is not guaranteed because schema changes such as the deletion of a database column can destroy data (i.e. all values stored under that column for all rows in that table are deleted). Instead, the tools help to preserve the meaning of the data or to reorganize existing data to meet new requirements. Since meaning of the data often cannot be encoded, the configuration of the tools usually needs manual intervention.

## Risks and benefits

Schema migration allows for fixing mistakes and adapting the data as requirements change. They are an essential part of software evolution, especially in agile environments (see below).

Applying a schema migration to a production database is always a risk. Development and test databases tend to be smaller and cleaner. The data in them is better understood, and if everything else fails, the amount of data is small enough for a human to process. Production databases are usually huge, old and full of surprises. The surprises can come from many sources:

- Corrupt data that was written by old versions of the software and not cleaned properly
- Implied dependencies in the data which no one knows about anymore
- People directly changing the database without using the designated tools
- Bugs in the schema migration tools
- Mistakes in assumptions how data should be migrated

For these reasons, the migration process needs a high level of discipline, thorough testing and a sound backup strategy.

## Migration strategies

In the steady state, one version of an application only understands one version of a schema. So the most basic strategy is to shut down the application, execute the schema migration, and then start the newer version of the application. While simple, this strategy causes a downtime. Depending on the criticality of the system and its usage patterns, downtimes of various duration may be tolerated, but in some cases none may be tolerated at all. In those cases, one of the following zero-downtime strategies may be used.

### Dual writing

These are the general steps of dual writing (also called double writing):

1. Prepare the schema so that it can hold data in both the old and new formats. This might mean adding a new version of a column or a table, without affecting existing data.
2. Deploy a new version of the application which writes data in both the old and new formats (hence the name dual writing). It's important to ensure consistency of these writes. After this point, all newly written data will exist in both old and new formats.
3. Execute a backfill in the database: copy data from the old format to the new format that existed previously, and hasn't been updated recently, so it's not dual written yet. After this point, the database has a complete replica of the data in both the old and new formats.
4. Deploy a new version of the application which switches to reading data in the new format, and stops dual writing. In distributed systems, it's important to switch the reading path before stopping dual writing, so this step may be divided into two.
5. Remove the old format data from the schema.

### Dual reading

Dual reading (also called double reading) is similar to dual writing, with the following steps:

1. Prepare the schema so that it can hold data in both the old and new formats. Same as above.
2. Deploy a new version of the application which tries to read both the old and new formats (hence the name dual reading), and works with whichever format is currently present.
3. Deploy another version of the application which stops writing the old format and starts writing the new format instead. Everything should continue working normally as the dual reading will recognize that it has to read the new format for newly written rows.
4. Execute a backfill in the database: for all data that was written in the old format, move it over to the new format.
5. Deploy an application change once more that stops reading the old data.
6. Remove the old format data from the schema.

### Dual reading and writing

In this combined approach, the application is changed to both dual read and dual write. Since both individual strategies ensure that the database can remain online without interruption, the combined approach achieves the same as well. This strategy allows for more fine grained control over the backfill, which can be divided into smaller batches, and feature flags may be used to toggle both the reading and writing paths more freely and separately from each other. This can also be useful when regular dual writing alone can't be guaranteed to happen in consistent transactions.

### Comparison

- All strategies above achieve a zero-downtime migration.
- Dual writing has the advantage that the old and new version of the data live side by side, so comparisons can be run between them to ensure consistency before committing to the new format. This, however, comes at the cost of doubling the storage requirements.
- With dual reading only one version of every piece of data exists at any point in time, so there's no increase in storage requirements.
- The combined approach allows doing the backfill in smaller batches so the storage increase can be controlled, but this comes at the cost of added complexity.

## Schema migration in agile software development

When developing software applications backed by a database, developers typically develop the application source code in tandem with an evolving database schema. The code typically has rigid expectations of what columns, tables and constraints are present in the database schema whenever it needs to interact with one, so only the version of database schema against which the code was developed is considered fully compatible with that version of source code.

In software testing, while developers may mock the presence of a compatible database system for unit testing, in any level of testing higher than this (e.g. integration testing or system testing) it is common for developers to test their application against a local or remote test database schematically compatible with the version of source code under test. In advanced applications, the migration itself can be subject to migration testing.

With schema migration technology, data models no longer need to be fully designed up-front, and are more capable of being adapted with changing project requirements throughout the software development lifecycle.

### Relation to revision control systems

Teams of software developers usually use version control systems to manage and collaborate on changes made to versions of source code. Different developers can develop on divergent, relatively older or newer branches of the same source code to make changes and additions during development.

Supposing that the software under development interacts with a database, every version of the source code can be associated with at least one database schema with which it is compatible.

Under good software testing practice, schema migrations can be performed on test databases to ensure that their schema is compatible to the source code. To streamline this process, a schema migration tool is usually invoked as a part of an automated software build as a prerequisite of the automated testing phase.

Schema migration tools can be said to solve versioning problems for database schemas just as version control systems solve versioning problems for source code. In practice, many schema migration tools actually rely on a textual representation of schema changes (such as files containing SQL statements) such that the version history of schema changes can effectively be stored alongside program source code within VCS. This approach ensures that the information necessary to recover a compatible database schema for a particular code branch is recoverable from the source tree itself. Another benefit of this approach is the handling of concurrent conflicting schema changes; developers may simply use their usual text-based conflict resolution tools to reconcile differences.

### Relation to schema evolution

Schema migration tooling could be seen as a facility to track the history of an evolving schema (i.e. schema evolution).

### Advantages

Developers no longer need to remove the entire test database in order to create a new test database from scratch (e.g. using schema creation scripts from DDL generation tools). Further, if generation of test data costs a lot of time, developers can avoid regenerating test data for small, non-destructive changes to the schema.
