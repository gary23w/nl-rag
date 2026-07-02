---
title: "Tables and Table Clusters (part 1/4)"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/tables-and-table-clusters.html
domain: oracle-database
license: CC-BY-SA-4.0
tags: oracle database, oracle rdbms, pl/sql, oracle corporation
fetched: 2026-07-02
part: 1/4
---

## 2 Tables and Table Clusters

This chapter provides an introduction to schema objects and discusses tables, which are the most common types of schema objects.

This chapter contains the following sections:

- Introduction to Schema Objects
- Overview of Tables
- Overview of Table Clusters
- Overview of Attribute-Clustered Tables
- Overview of Temporary Tables
- Overview of External Tables
- Overview of Object Tables

- Introduction to Schema Objects A database schema is a logical container for data structures, called schema objects. Examples of schema objects are tables and indexes. You create and manipulate schema objects with SQL.
- Overview of Tables A table is the basic unit of data organization in an Oracle database.
- Overview of Table Clusters A **table cluster** is a group of tables that share common columns and store related data in the same blocks.
- Overview of Attribute-Clustered Tables An attribute-clustered table is a heap-organized table that stores data in close proximity on disk based on user-specified clustering directives. The directives specify columns in single or multiple tables.
- Overview of Temporary Tables A **temporary table** holds data that exists only for the duration of a transaction or session.
- Overview of External Tables An **external table** accesses data in external sources as if this data were in a table in the database.
- Overview of Blockchain Tables A **blockchain table** is an append-only table designed for centralized blockchain applications.
- Overview of Immutable Tables Immutable tables are read-only tables that prevent unauthorized data modifications by insiders and accidental data modifications resulting from human errors.
- Overview of Object Tables An **object table** is a special kind of table in which each row represents an object.

**Parent topic:** Oracle Relational Data Structures


### Introduction to Schema Objects

A database schema is a logical container for data structures, called schema objects. Examples of schema objects are tables and indexes. You create and manipulate schema objects with SQL.

A database user account has a password and specific database privileges. Each user account owns a single schema, which has the same name as the user. The schema contains the data for the user owning the schema. For example, the `hr` user account owns the `hr` schema, which contains schema objects such as the `employees` table. In a production database, the schema owner usually represents a database application rather than a person.

Within a schema, each schema object of a particular type has a unique name. For example, `hr.employees` refers to the table `employees` in the `hr` schema. Figure 2-1 depicts a schema owner named `hr` and schema objects within the `hr` schema.

Figure 2-1 HR Schema

Description of "Figure 2-1 HR Schema"

This section contains the following topics:

- Schema Object Types
- Schema Object Storage
- Schema Object Dependencies
- SYS and SYSTEM Schemas
- Sample Schemas

- Schema Object Types Oracle SQL enables you to create and manipulate many other types of schema objects.
- Schema Object Storage Some schema objects store data in a type of logical storage structure called a segment. For example, a nonpartitioned heap-organized table or an index creates a segment.
- Schema Object Dependencies Some schema objects refer to other objects, creating a schema object dependency.
- SYS and SYSTEM Schemas All Oracle databases include default administrative accounts.
- Sample Schemas An Oracle database may include **sample schemas**, which are a set of interlinked schemas that enable Oracle documentation and Oracle instructional materials to illustrate common database tasks.

See Also:

"Overview of Database Security" to learn more about users and privileges

**Parent topic:** Tables and Table Clusters

#### Schema Object Types

Oracle SQL enables you to create and manipulate many other types of schema objects.

The principal types of schema objects are shown in the following table.

Table 2-1 Schema Objects

| Object | Description | To Learn More |
|---|---|---|
| Table | A table stores data in rows. Tables are the most important schema objects in a relational database. | "Overview of Tables" |
| Indexes | Indexes are schema objects that contain an entry for each indexed row of the table or table cluster and provide direct, fast access to rows. Oracle Database supports several types of index. An index-organized table is a table in which the data is stored in an index structure. | "Indexes and Index-Organized Tables" |
| Partitions | Partitions are pieces of large tables and indexes. Each partition has its own name and may optionally have its own storage characteristics. | "Overview of Partitions" |
| Views | Views are customized presentations of data in one or more tables or other views. You can think of them as stored queries. Views do not actually contain data. | "Overview of Views" |
| Sequences | A sequence is a user-created object that can be shared by multiple users to generate integers. Typically, you use sequences to generate primary key values. | "Overview of Sequences" |
| Dimensions | A dimension defines a parent-child relationship between pairs of column sets, where all the columns of a column set must come from the same table. Dimensions are commonly used to categorize data such as customers, products, and time. | "Overview of Dimensions" |
| Synonyms | A synonym is an alias for another schema object. Because a synonym is simply an alias, it requires no storage other than its definition in the data dictionary. | "Overview of Synonyms" |
| PL/SQL subprograms and packages | PL/SQL is the Oracle procedural extension of SQL. A PL/SQL subprogram is a named PL/SQL block that can be invoked with a set of parameters. A PL/SQL package groups logically related PL/SQL types, variables, and subprograms. | "PL/SQL Subprograms" |

Other types of objects are also stored in the database and can be created and manipulated with SQL statements but are not contained in a schema. These objects include database user account, roles, contexts, and dictionary objects.

See Also:

- *Oracle Database Administrator’s Guide* to learn how to manage schema objects
- *Oracle Database SQL Language Reference* for more about schema objects and database objects

**Parent topic:** Introduction to Schema Objects

#### Schema Object Storage

Some schema objects store data in a type of logical storage structure called a segment. For example, a nonpartitioned heap-organized table or an index creates a segment.

Other schema objects, such as views and sequences, consist of metadata only. This topic describes only schema objects that have segments.

Oracle Database stores a schema object logically within a tablespace. There is no relationship between schemas and tablespaces: a tablespace can contain objects from different schemas, and the objects for a schema can be contained in different tablespaces. The data of each object is physically contained in one or more data files.

The following figure shows a possible configuration of table and index segments, tablespaces, and data files. The data segment for one table spans two data files, which are both part of the same tablespace. A segment cannot span multiple tablespaces.

Figure 2-2 Segments, Tablespaces, and Data Files

Description of "Figure 2-2 Segments, Tablespaces, and Data Files"

See Also:

- "Logical Storage Structures" to learn about tablespaces and segments
- *Oracle Database Administrator’s Guide* to learn how to manage storage for schema objects

**Parent topic:** Introduction to Schema Objects

#### Schema Object Dependencies

Some schema objects refer to other objects, creating a schema object dependency.

For example, a view contains a query that references tables or views, while a PL/SQL subprogram invokes other subprograms. If the definition of object A references object B, then A is a dependent object on B, and B is a referenced object for A.

Oracle Database provides an automatic mechanism to ensure that a dependent object is always up to date with respect to its referenced objects. When you create a dependent object, the database tracks dependencies between the dependent object and its referenced objects. When a referenced object changes in a way that might affect a dependent object, the database marks the dependent object invalid. For example, if a user drops a table, no view based on the dropped table is usable.

An invalid dependent object must be recompiled against the new definition of a referenced object before the dependent object is usable. Recompilation occurs automatically when the invalid dependent object is referenced.

As an illustration of how schema objects can create dependencies, the following sample script creates a table `test_table` and then a procedure that queries this table:

```
CREATE TABLE test_table ( col1 INTEGER, col2 INTEGER );

CREATE OR REPLACE PROCEDURE test_proc
AS
BEGIN
 FOR x IN ( SELECT col1, col2 FROM test_table )
 LOOP
   -- process data
   NULL;
 END LOOP;
END;
/
```

The following query of the status of procedure `test_proc` shows that it is valid:

```
SQL> SELECT OBJECT_NAME, STATUS FROM USER_OBJECTS WHERE OBJECT_NAME = 'TEST_PROC';
 
OBJECT_NAME STATUS
----------- -------
TEST_PROC   VALID
```

After adding the `col3` column to `test_table`, the procedure is still valid because the procedure has no dependencies on this column:

```
SQL> ALTER TABLE test_table ADD col3 NUMBER;
 
Table altered.
 
SQL> SELECT OBJECT_NAME, STATUS FROM USER_OBJECTS WHERE OBJECT_NAME = 'TEST_PROC';
 
OBJECT_NAME STATUS
----------- -------
TEST_PROC   VALID
```

However, changing the data type of the `col1` column, which the `test_proc` procedure depends on, invalidates the procedure:

```
SQL> ALTER TABLE test_table MODIFY col1 VARCHAR2(20);
 
Table altered.
 
SQL> SELECT OBJECT_NAME, STATUS FROM USER_OBJECTS WHERE OBJECT_NAME = 'TEST_PROC';
 
OBJECT_NAME STATUS
----------- -------
TEST_PROC   INVALID
```

Running or recompiling the procedure makes it valid again, as shown in the following example:

```
SQL> EXECUTE test_proc
 
PL/SQL procedure successfully completed.
 
SQL> SELECT OBJECT_NAME, STATUS FROM USER_OBJECTS WHERE OBJECT_NAME = 'TEST_PROC';
 
OBJECT_NAME STATUS
----------- -------
TEST_PROC   VALID
```

See Also:

*Oracle Database Administrator’s Guide* and *Oracle Database Development Guide* to learn how to manage schema object dependencies

**Parent topic:** Introduction to Schema Objects

#### SYS and SYSTEM Schemas

All Oracle databases include default administrative accounts.

Administrative accounts are highly privileged and are intended only for DBAs authorized to perform tasks such as starting and stopping the database, managing memory and storage, creating and managing database users, and so on.

The `SYS` administrative account is automatically created when a database is created. This account can perform all database administrative functions. The `SYS` schema stores the base tables and views for the data dictionary. These base tables and views are critical for the operation of Oracle Database. Tables in the `SYS` schema are manipulated only by the database and must never be modified by any user.

The `SYSTEM` administrative account is also automatically created when a database is created. The `SYSTEM` schema stores additional tables and views that display administrative information, and internal tables and views used by various Oracle Database options and tools. Never use the `SYSTEM` schema to store tables of interest to nonadministrative users.

See Also:

- "User Accounts"
- "Connection with Administrator Privileges"
- *Oracle Database Administrator’s Guide* to learn about `SYS`, `SYSTEM`, and other administrative accounts

**Parent topic:** Introduction to Schema Objects

#### Sample Schemas

An Oracle database may include **sample schemas**, which are a set of interlinked schemas that enable Oracle documentation and Oracle instructional materials to illustrate common database tasks.

The `hr` sample schema contains information about employees, departments and locations, work histories, and so on. The following illustration depicts an entity-relationship diagram of the tables in `hr`. Most examples in this manual use objects from this schema.

Figure 2-3 HR Schema

Description of "Figure 2-3 HR Schema"

See Also:

*Oracle Database Sample Schemas* to learn how to install the sample schemas

**Parent topic:** Introduction to Schema Objects
