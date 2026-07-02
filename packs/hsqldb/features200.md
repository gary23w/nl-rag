---
title: "HyperSQL 2.5 New Features"
source: https://hsqldb.org/web/features200.html
domain: hsqldb
license: CC-BY-SA-4.0
tags: hsqldb database, hypersql database, java database, embedded database
fetched: 2026-07-02
---

# HyperSQL 2.5 New Features

| (hsqldb.org Home Page) HSQLDB - 100% Java Database | <Download> <Support> <License> <Features> <FAQ> <Documentation> <How To> <Developers> <Software using HSQLDB> <SourceForge Project Page> |
|---|---|

## New Features in HyperSQL 2.7

Since the release of version 2.0, many new features and enhancements have been introduced in point releases. Regular code reviews, user feedback, and bug fixes resulted in the latest release.

This document lists the enhancements and new features in version 2.0 and beyond. An extensive range of new SQL and JDBC capabilities, increased scalability, and better query optimisation have been achieved by a rewrite of most of the internal components and the addition of some major new ones.

All areas of functionality have been thoroughly tested with an extensive internal test suite and by users with their applications. HyperSQL 2.0 went into alpha release in April 2009 and several RC releases were downloaded over 20000 times before the final release in June 2010. Over 200 users submitted bug reports which were promptly fixed. The same process was repeated again and again over the next 9 years. There were 7 point releases in 2011, followed by another 16 between 2012 and 2024.

An extensive Guide was written over two years to cover all features of the engine in detail. It has been updated with each release to cover the latest features.

### NEW CORE

Fully multithreaded core supports 2PL (two-phased locking) and MVCC (multiversion concurrency control), plus a hybrid 2PL+MVCC transaction control mode. Transactions can be SERIALIZABLE or READ COMMITTED, using strict 2PL concurrency control. Version 2.0 also adds the MVCC modes, SNAPSHOT ISOLATION and READ CONSISTENCY, which are comparable to REPEATABLE READS and READ COMMITTED isolation levels, but with higher concurrency. Many enhancements are introduced to allow maximum multi-threaded concurrency in different isolation modes.

### SCALABILITY

Massive high performance LOB store for BLOBs and CLOBs up to multi-gigabyte size, with total storage capacity of 64 terabytes.

Increased default storage space of 64GB for all CACHED table disk-based data, with fast startup and shutdown. The default can always be extended to 8TB with a connection property. With another connection property at the time of database creation, the maximum can be extended to 256TB.

Large result sets, views and subqueries can now be stored on disk (on the server side) while being generated and accessed. The threshold to store a result on disk, as well as the actual fetch size in client-server configurations can be specified per connection.

Internal and external commands for backing up databases to TAR and GZIP archives.

### QUERY OPTIMISATION

All query conditions, whether in a JOIN or WHERE clause, are now allocated to an index if possible. IN queries are now optimised to use an index if possible. Conditions with OR are optimised if indexes can be used. MAX(), MIN() and ORDER BY with or without LIMIT and OFFSET expressions can use indexes. All indexes can be used in reverse order for these operations. Indexes on multiple columns are used efficiently. All subquery and view access is optimised.

### SQL STORED PROCEDURES AND FUNCTIONS

HyperSQL supports schema-based stored procedures and functions written entirely in SQL. Procedural SQL language includes WHILE loops, IF, CASE WHEN, and exception handling statements. Recursive functions are supported. SQL procedures can return multiple result sets and return values. SQL functions can return single values, arrays, or tables that can be used in SQL queries. User defined aggregate functions written in SQL are supported.

### JAVA STORED PROCEDURES AND FUNCTIONS

HyperSQL supports schema-based stored procedures and functions written entirely in JAVA. Polymorphism is supported. User defined aggregate functions are supported. Java procedures can return multiple result sets and return values. Java functions can can return single values, arrays or even tables that can be used in SQL queries.

### SYSTEM-VERSIONED TABLES AND REPLICATION

HyperSQL supports system-versioned tables, which keep all update history. This feature can be used with the new log-based synchronization capability to keep replicated databases in sync.

### NEW DATA TYPES

Support for BIT, BIT VARYING, CLOB, BLOB, INTERVAL according to the SQL Standards. TIME can now have a fractional second part. TIME WITH TIME ZONE and TIMESTAMP WITH TIME ZONE are supported. The full range of combinations of datetime and interval types is supported. Support for DOMAIN objects with constraints and DISTINCT types.

The UUID data type is now supported.

### ARRAY TYPES

Arrays of most types can be used in table definitions, expressions, function parameters and return types.

### COLLATIONS

Multiple collations can be used for different tables or columns. A collation can be specified for ORDER BY.

### NEW EXPRESSION TYPES

Complete rewrite of scanner and parser classes. Supports all SQL standard identifier and character string literals (Unicode strings and escapes, etc.).

Supports extended CASE WHEN conditions such as CASE X WHEN IN (,,), BETWEEN A AND B, 21, 56, IS NULL THEN ..

UNIQUE(SELECT ..) predicate.

(A,B) OVERLAPS(X,Y) predicated.

Supports Z BETWEEN [SYMMETRIC | ASYMMETRIC] (X, Y) predicate.

Multi-column (A,B,C) IN ((,,), (,,), ) both with literals and queries

Supports (A, B, C) {= | > | < | <> |…}(W,X,Y,Z) predicates.

Supports (A,B,C) IS [NOT] DISTINCT FROM (W,X,Y,Z) predicates

Supports (A,B,C) MATCHES [UNIQUE] [SIMPLE]|[PARTIAL]|[FULL] (SELECT …) predicates.

Supports (A,B,C) {= | < | > | <= | >=} {ANY | ALL} SELECT … predicates.

Supports PERIOD (A, B) { CONTAINS | EQUALS | OVERLAPS | PRECEDES | SUCCEEDS } PERIOD (C, D)

Full Standard syntax and semantics (arithmetic and other operations) of expressions involving INTERVAL types. Supports type casts to INTERVAL types modifiers (e.g. <expression> DAY). Supports WITH TIME ZONE data types, including zone modifiers (i.e. <expression> AT LOCAL | AT TIME ZONE …).

Supports standard SQL grammar, including IS [NOT] {NULL | TRUE | FALSE | UNKNOWN}.

Supports expressions in all LIKE arguments.

### NEW DATA MANIPULATION LANGUAGE FEATURES

Both INSERT and UPDATE command have been enhanced to support multi-row inserts, omission of parentheses, DEFAULT keyword, mix of subquery and row expressions. The powerful MERGE command is fully supported.

INSERT INTO … VALUES (expr,expr, ..), (expr,expr, …), …

INSERT INTO … VALUES expr

INSERT INTO .. DEFAULT VALUES

INSERT INTO … VALUES (expr, DEFAULT, ..)

UPDATE … SET A = DEFAULT, ..

UPDATE … SET (A, B, ..) = (expr, DEFAULT,…), C = expr, (D,E) = (SELECT …)

DELETE ... LIMIT N

MERGE statement with full Standard compliant syntax is supported.

TRUNCATE TABLE is fully supported.

### NEW DATA QUERY LANGUAGE FEATURES

#### SELECT

SELECT has been extensively enhanced, supporting all Standard join types.

The scope of column labels in SELECT queries is now treated according to the SQL Standard. Labels are visible in the ORDER BY expression but not in GROUP BY

Supports TABLE X to introduce the equivalent of SELECT * FROM TABLE X in set operations.

Supports VALUES (,,,), (,,,) as table constructor in joins.

Supports TABLE, LATERAL and UNNEST table constructor in joins.

Supports WITH RECURSIVE for named subqueries allowing recursive queries.

Supports column name list after correlation name SELECT .. FROM A AS B (X,Y,Z) JOIN C…

[LEFT | RIGHT | FULL {OUTER}] JOIN

UNION JOIN

[LEFT | RIGHT | FULL {OUTER}] NATURAL JOIN

[LEFT | RIGHT | FULL {OUTER}] JOIN … USING (A, B, ..)

SELECT * with the above joins now returns the correct column sequence as per SQL Standard

JOIN conditions can now contain any valid boolean expressions.

Support for UNION {ALL|DISTINCT}, INTERSECT {ALL|DISTINCT} and EXCEPT {ALL|DISTINCT}

Support for all the above with CORRESPONDING[(<column list>)}

Support for <joined table>, e.g. SELECT … FROM (table1 OUTER JOIN table2) JOIN table3

Support for NULLS FIRST, NULLS LAST in ORDER BY

Full support for inclusion of set functions (e.g. COUNT, AVG) in subquery conditions contained within a HAVING clause. Includes support for user-defined aggregate functions.

Filters for aggregates, e.g. COUNT (USER_NAME) FILTER (WHERE GENDER IS 'M')

Supports FETCH <row count> ROWS ONLY as SQL Standard alternative to LIMIT at the end of query expression.

### DATA DEFINITION LANGUAGE ENHANCEMENTS

Supports full syntax of SQL TRIGGER definition for row level triggers using SQL procedure statements (as well as Java classes)

CREATE TRIGGER <name> {BEFORE | AFTER} {INSERT | DELETE | UPDATE [OF (<column name>, ..)] ON <table name> [ REFERENCING OLD [ROW] [AS] <old transition variable name> | NEW [ROW] [AS] <new transition variable name>] [FOR EACH ROW] [WHEN (<search condition>)] <sql procedure statement block>

Supports full set of SEQUENCE generator options ([NO] MAXVALUE, [NO] MINVALUE, [NO] CYCLE, etc.) and data types including SMALLINT, INT, BIGINT, DECIMAL, NUMERIC. These are supported in IDENTITY sequences and in normal sequences, including all relevant ALTER COLUMN and ALTER SEQUENCE commands.

Supports GENERATED {BY DEFAULT | ALWAYS} AS IDENTITY in a different column than the PRIMARY KEY column.

A user supplied value or a value returned from a SELECT statement can always be inserted into an identity column. If GENERATED ALWAYS has been specified, then OVERRIDING SYSTEM VALUE must be included in the INSERT statement.

Supports GENERATED ALWAYS AS <expression> for derivative columns that are based on other column values.

Extended CREATE SCHEMA …. statements can include cross references between FOREIGN KEY constraints in different tables.

Supports CREATE TABLE .. (<column list>) AS (<query expression>) WITH [NO] DATA

CREATE TABLE can have mixed column and constraint creation elements. A column definition can include a PRIMARY KEY, UNIQUE, FOREIGN KEY or CHECK constraint,

Similarly, ALTER TABLE … ADD COLUMN can feature constraint definitions.

ALTER TABLE … ALTER COLUMN … SET DATA TYPE … supported.

Supports CASCADE with ALTER TABLE .. DROP COLUMN and ALTER TABLE … DROP CONSTRAINT.

Named NOT NULL constraints now supported in column definition CONSTRAINT C NOT NULL. All NOT NULL constraints are treated as CHECK (C IS NOT NULL) type constraints and listed as such in system tables.

Supports VIEW definitions including tables and sequences in other schemas.

Supports updatable views, including WITH {LOCAL | CASCADED} CHECK OPTION

Supports CREATE SYNONYM for tables, sequences and routines.

### SQL FUNCTIONS

Full set of SQL Standard functions, including correct type handling and application to all supported types (e.g. BINARY, BLOB, CLOB), is now supported.

SUBSTRING for character (CHAR, VARCHAR, CLOB) and binary (BINARY, VARBINARY, BLOB) types. UPPER, LOWER for all character types TRIM for all character types OVERLAY for all character types POSITION CHAR_LENGTH, CHARACTER_LENGTH, OCTET_LENGTH EXTRACT ABS for all number types

An extended set of extra functions is also supported, including:

TO_CHAR, TO_DATE, TRUNCATE, GROUP_CONCAT, ARRAY_AGG REGXP_MATCHES, REGXP_SUBSTRING, REGX_SUBSTRING_ARRAY DECODE, GREATEST, etc.

### JSON CONSTRUCTOR FUNCTIONS

Full set of SQL JSON constructor functions allows building JSON objects with nested elements using SELECT statements.

### OTHER SQL FEATURES

Supports column level SELECT, INSERT and UPDATE access rights, with GRANT and REVOKE on individual columns of tables, including WITH GRANT OPTION. GRANT SELECT(A, D) ON X TO U

Supports row level access rights

Supports SQL STATE with messages defined by the standard.

### COMPATIBILITY FEATURES

Supports several syntax and operation compatibility flags to ease testing and porting applications written against a different database engine. These include PostgreSQL, MySQL, Oracle, MS SQL Server and DB2. New compatibility features have been added in each point release.

The latest version 2.7 is highly compatible with those databases. Even some of the most non-standard syntax constructs such as ON DUPLICATE KEY UPDATE are now supported.

### JDBC FEATURES

Supports getGeneratedKeys() calls in Statement and PreparedStatement.

Supports CallableStatement with multiple result sets and IN and OUT parameters

Supports POSIX functions TIMESTAMPDIFF and TIMESTAMPADD.

Supports Java 8 with JDBC 4.2. All applicable new methods are supported. Tested with Java 8 to 17.

### DATA IMPORT AND EXPORT

Import and export of comma-separated text files as well as SQL data and definition scripts are supported.

### DATA IMPORT AND EXPORT

Import and export of comma-separated text files as well as SQL data and definition scripts are supported.

### CONNECTION POOL

The JDBCPool class offers a fast and simple connection pool dedicated to HSQLDB.

### JEE FEATURES

Supports and implements DataSource, PooledConnection, ConnectionPoolDataSource, XADataSource and XAResource interfaces.

### INFORMATION SCHEMA

Supports SQL Standard INFORMATION SCHEMA views, together with additional views used in JDBC. Alltogther some 90 view are supported. Standard views are supported correctly and reflect the user's permissions on database objects.

### OTHER FEATURES

The Server now supports remote opening of databases.

Supports advanced external user authentication and password complexity checks.

Supports SQL statement logging as well as external framework logging via Log4J and JRE logging.

### SQL STANDARD FEATURE LIST

SQL-92 direct SQL is supported fully to Advanced Level except for deferrable constraint enforcement, ASSERTION, and CHECK constraints that contain subqueries.

All SQL:2003 - SQL:2023 Standard CORE features are supported.

HSQLDB 2.x also supports a large set of SQL:1999, SQL:2003, SQL:2008, SQL:2011, SQL:2016, and SQL:2023 NON-CORE features.

B021 Direct SQL B128 Routine language SQL C011 Call-Level Interface E011 Numeric data types E011 Numeric data types 01 INTEGER and SMALLINT data types E011 Numeric data types 02 REAL, DOUBLE PRECISION, and FLOAT data types E011 Numeric data types 03 DECIMAL and NUMERIC data types E011 Numeric data types 04 Arithmetic operators E011 Numeric data types 05 Numeric comparison E011 Numeric data types 06 Implicit casting among the numeric data types E021 Character data types E021 Character string types 01 CHARACTER data type E021 Character string types 02 CHARACTER VARYING data type E021 Character string types 03 Character literals E021 Character string types 04 CHARACTER_LENGTH function E021 Character string types 05 OCTET_LENGTH function E021 Character string types 06 SUBSTRING function E021 Character string types 07 Character concatenation E021 Character string types 08 UPPER and LOWER functions E021 Character string types 09 TRIM function E021 Character string types 10 Implicit casting among the character string types E021 Character string types 11 POSITION function E021 Character string types 12 Character comparison E031 Identifiers E031 Identifiers 01 Delimited identifiers E031 Identifiers 02 Lower case identifiers E031 Identifiers 03 Trailing underscore E051 Basic query specification E051 Basic query specification 01 SELECT DISTINCT E051 Basic query specification 02 GROUP BY clause E051 Basic query specification 04 GROUP BY can contain columns not in <select list> E051 Basic query specification 05 Select list items can be renamed E051 Basic query specification 06 HAVING clause E051 Basic query specification 07 Qualified * in select list E051 Basic query specification 08 Correlation names in the FROM clause E051 Basic query specification 09 Rename columns in the FROM clause E061 Basic predicates and search conditions E061 Basic predicates and search conditions 01 Comparison predicate E061 Basic predicates and search conditions 02 BETWEEN predicate E061 Basic predicates and search conditions 03 IN predicate with list of values E061 Basic predicates and search conditions 04 LIKE predicate E061 Basic predicates and search conditions 05 LIKE predicate ESCAPE clause E061 Basic predicates and search conditions 06 NULL predicate E061 Basic predicates and search conditions 07 Quantified comparison predicate E061 Basic predicates and search conditions 08 EXISTS predicate E061 Basic predicates and search conditions 09 Subqueries in comparison predicate E061 Basic predicates and search conditions 11 Subqueries in IN predicate E061 Basic predicates and search conditions 12 Subqueries in quantified comparison predicate E061 Basic predicates and search conditions 13 Correlated subqueries E061 Basic predicates and search conditions 14 Search condition E071 Basic query expressions E071 Basic query expressions 01 UNION DISTINCT table operator E071 Basic query expressions 02 UNION ALL table operator E071 Basic query expressions 03 EXCEPT DISTINCT table operator E071 Basic query expressions 05 Columns combined via table operators need not have exactly the same data type E071 Basic query expressions 06 Table operators in subqueries E081 Basic Privileges E081 Basic Privileges 01 SELECT privilege E081 Basic Privileges 02 DELETE privilege E081 Basic Privileges 03 INSERT privilege at the table level E081 Basic Privileges 04 UPDATE privilege at the table level E081 Basic Privileges 05 UPDATE privilege at the column level E081 Basic Privileges 06 REFERENCES privilege at the table level E081 Basic Privileges 07 REFERENCES privilege at the column level E081 Basic Privileges 08 WITH GRANT OPTION E081 Basic Privileges 09 USAGE privilege E081 Basic Privileges 10 EXECUTE privilege E091 Set functions E091 Set functions 01 AVG E091 Set functions 02 COUNT E091 Set functions 03 MAX E091 Set functions 04 MIN E091 Set functions 05 SUM E091 Set functions 06 ALL quantifier E091 Set functions 07 DISTINCT quantifier E101 Basic data manipulation E101 Basic data manipulation 01 INSERT statement E101 Basic data manipulation 03 Searched UPDATE statement E101 Basic data manipulation 04 Searched DELETE statement E111 Single row SELECT statement E121 Basic cursor support 02 ORDER BY columns need not be in select list E121 Basic cursor support 03 Value expressions in ORDER BY clause E131 Null value support (nulls in lieu of values) E141 Basic integrity constraints E141 Basic integrity constraints 01 NOT NULL constraints E141 Basic integrity constraints 02 UNIQUE constraints of NOT NULL columns E141 Basic integrity constraints 03 PRIMARY KEY constraints E141 Basic integrity constraints 04 Basic FOREIGN KEY constraint with the NO ACTION default for both referential delete action and referential update action E141 Basic integrity constraints 06 CHECK constraints E141 Basic integrity constraints 07 Column defaults E141 Basic integrity constraints 08 NOT NULL inferred on PRIMARY KEY E141 Basic integrity constraints 10 Names in a foreign key can be specified in any order E151 Transaction support E151 Transaction support 01 COMMIT statement E151 Transaction support 02 ROLLBACK statement E152 Basic SET TRANSACTION statement E152 Basic SET TRANSACTION statement 01 SET TRANSACTION statement: ISOLATION LEVEL SERIALIZABLE clause E152 Basic SET TRANSACTION statement 02 SET TRANSACTION statement: READ ONLY and READ WRITE clauses E153 Updatable queries with subqueries E161 SQL comments using leading double minus E171 SQLSTATE support E182 Module language F021 Basic information schema F021 Basic information schema 01 COLUMNS view F021 Basic information schema 02 TABLES view F021 Basic information schema 03 VIEWS view F021 Basic information schema 04 TABLE_CONSTRAINTS view F021 Basic information schema 05 REFERENTIAL_CONSTRAINTS view F021 Basic information schema 06 CHECK_CONSTRAINTS view F031 Basic schema manipulation F031 Basic schema manipulation 01 CREATE TABLE statement to create persistent base tables F031 Basic schema manipulation 02 CREATE VIEW statement F031 Basic schema manipulation 03 GRANT statement F031 Basic schema manipulation 04 ALTER TABLE statement: ADD COLUMN clause F031 Basic schema manipulation 13 DROP TABLE statement: RESTRICT clause F031 Basic schema manipulation 16 DROP VIEW statement: RESTRICT clause F031 Basic schema manipulation 19 REVOKE statement: RESTRICT clause F032 CASCADE drop behavior F033 ALTER TABLE statement: DROP COLUMN clause F034 Extended REVOKE statement F034 Extended REVOKE statement 01 REVOKE statement performed by other than the owner of a schema object F034 Extended REVOKE statement 02 REVOKE statement: GRANT OPTION FOR clause F034 Extended REVOKE statement 03 REVOKE statement to revoke a privilege that the grantee has WITH GRANT OPTION F041 Basic joined table F041 Basic joined table 01 Inner join (but not necessarily the INNER keyword) F041 Basic joined table 02 INNER keyword F041 Basic joined table 03 LEFT OUTER JOIN F041 Basic joined table 04 RIGHT OUTER JOIN F041 Basic joined table 05 Outer joins can be nested F041 Basic joined table 07 The inner table in a left or right outer join can also be used in an inner join F041 Basic joined table 08 All comparison operators are supported (rather than just =) F051 Basic date and time F051 Basic date and time 01 DATE data type (including support of DATE literal) F051 Basic date and time 02 TIME data type (including support of TIME literal) with fractional seconds precision of at least 0 F051 Basic date and time 03 TIMESTAMP data type (including support of TIMESTAMP literal) with fractional seconds precision of at least 0 and 6 F051 Basic date and time 04 Comparison predicate on DATE, TIME, and TIMESTAMP data types F051 Basic date and time 05 Explicit CAST between datetime types and character string types F051 Basic date and time 06 CURRENT_DATE F051 Basic date and time 07 LOCALTIME F051 Basic date and time 08 LOCALTIMESTAMP F052 Intervals and datetime arithmetic F053 OVERLAPS predicate F081 UNION and EXCEPT in views F111 Isolation levels other than SERIALIZABLE F111 Isolation levels other than SERIALIZABLE 01 READ UNCOMMITTED isolation level F111 Isolation levels other than SERIALIZABLE 02 READ COMMITTED isolation level F111 Isolation levels other than SERIALIZABLE 03 REPEATABLE READ isolation level F121 Basic diagnostics management 01 GET DIAGNOSTICS statement F131 Grouped operations F131 Grouped operations 01 WHERE, GROUP BY, and HAVING clauses supported in queries with grouped views F131 Grouped operations 02 Multiple tables supported in queries with grouped views F131 Grouped operations 03 Set functions supported in queries with grouped views F131 Grouped operations 04 Subqueries with GROUP BY and HAVING clauses and grouped views F131 Grouped operations 05 Single row SELECT with GROUP BY and HAVING clauses and grouped views F171 Multiple schemas per user F191 Referential delete actions F201 CAST function F221 Explicit defaults F222 INSERT statement: DEFAULT VALUES clause F231 Privilege tables F231 Privilege tables 01 TABLE_PRIVILEGES view F231 Privilege tables 02 COLUMN_PRIVILEGES view F231 Privilege tables 03 USAGE_PRIVILEGES view F251 Domain support F261 CASE expression F261 CASE expression 01 Simple CASE F261 CASE expression 02 Searched CASE F261 CASE expression 03 NULLIF F261 CASE expression 04 COALESCE F262 Extended CASE expression F263 Comma-separated predicates in simple CASE expression F271 Compound character literals F281 LIKE enhancements F291 UNIQUE predicate F301 CORRESPONDING in query expressions F302 INTERSECT table operator F302 INTERSECT table operator 01 INTERSECT DISTINCT table operator F302 INTERSECT table operator 02 INTERSECT ALL table operator F304 EXCEPT ALL table operator F311 Schema definition statement F311 Schema definition statement 01 CREATE SCHEMA F311 Schema definition statement 02 CREATE TABLE for persistent base tables F311 Schema definition statement 03 CREATE VIEW F311 Schema definition statement 04 CREATE VIEW: WITH CHECK OPTION F311 Schema definition statement 05 GRANT statement F312 MERGE statement F321 User authorization F341 Usage tables F361 Subprogram support F381 Extended schema manipulation F381 Extended schema manipulation 01 ALTER TABLE statement: ALTER COLUMN clause F381 Extended schema manipulation 02 ALTER TABLE statement: ADD CONSTRAINT clause F381 Extended schema manipulation 03 ALTER TABLE statement: DROP CONSTRAINT clause F391 Long identifiers F392 Unicode escapes in identifiers F393 Unicode escapes in literals F401 Extended joined table F401 Extended joined table 01 NATURAL JOIN F401 Extended joined table 02 FULL OUTER JOIN F401 Extended joined table 04 CROSS JOIN F402 Named column joins for LOBs, arrays, and multisets F411 Time zone specification F421 National character F441 Extended set function support F442 Mixed column references in set functions F451 Character set definition F461 Named character sets F471 Scalar subquery values F481 Expanded NULL predicate F491 Constraint management F501 Features and conformance views F501 Features and conformance views 01 SQL_FEATURES view F501 Features and conformance views 02 SQL_SIZING view F502 Enhanced documentation tables F502 Enhanced documentation tables 01 SQL_SIZING_PROFILES view F502 Enhanced documentation tables 02 SQL_IMPLEMENTATION_INFO view F502 Enhanced documentation tables 03 SQL_PACKAGES view F531 Temporary tables F555 Enhanced seconds precision F561 Full value expressions F571 Truth value tests F591 Derived tables F641 Row and table constructors F651 Catalog name qualifiers F661 Simple tables F672 Retrospective check constraints F690 Collation support F692 Enhanced collation support F701 Referential update actions F711 ALTER domain F731 INSERT column privileges F741 Referential MATCH types F751 View CHECK enhancements F762 CURRENT_CATALOG F763 CURRENT_SCHEMA F801 Full set function F821 Local table references F850 Top-level <order by clause> in <query expression> F851 <order by clause> in subqueries F852 Top-level <order by clause> in views F855 Nested <order by clause> in <query expression> F856 Nested <fetch first clause> in <query expression> F857 Top-level <fetch first clause> in <query expression> F858 <fetch first clause> in subqueries F859 Top-level <fetch first clause> in views F860 dynamic <fetch first row count> in <fetch first clause> F861 Top-level <result offset clause> in <query expression> F862 <result offset clause> in subqueries F863 Nested <result offset clause> in <query expression> F864 Top-level <result offset clause> in views F865 dynamic <offset row count> in <result offset clause> J621 external Java routines P002 Computational completeness P003 Information Schema views P004 extended CASE statement P006 Multiple assignment P008 Comma-separated predicates in simple CASE statement S011 Distinct data types S011 Distinct data types 01 USER_DEFINED_TYPES view S071 SQL paths in function and type name resolution S091 Basic array support S091 Basic array support 01 Arrays of built-in data types S091 Basic array support 02 Arrays of distinct types S091 Basic array support 03 Array expressions S095 Array constructors by query S096 Optional array bounds S097 Array element assignment S098 ARRAY_AGG S201 SQL-invoked routines on arrays S201 SQL-invoked routines on arrays 01 Array parameters S201 SQL-invoked routines on arrays 02 Array as result type of functions S301 Enhanced UNNEST S401 Distinct types based on array types S403 ARRAY_MAX_CARDINALITY S404 TRIM_ARRAY T011 Timestamp in Information Schema T021 BINARY and VARBINARY data types T022 Advanced BINARY and VARBINARY data type support T023 Compound binary literals T024 Spaces in binary literals T031 BOOLEAN data type T041 Basic LOB data type support T042 Extended LOB data type support T045 BLOB data type T046 CLOB data type T047 POSITION, LENGTH, LOWER, TRIM, UPPER, and SUBSTRING functions for BLOBs T048 Concatenation of LOB data types T049 LOB locator: non-holdable T050 POSITION, LENGTH, LOWER, TRIM, UPPER, and SUBSTRING functions for CLOBs T054 GREATEST and LEAST T055 String padding functions T056 Multi-character TRIM function T061 UCS support T062 Character length units T071 BIGINT data type T101 Enhanced nullability determination T121 WITH (excluding RECURSIVE) in query expression T122 WITH (excluding RECURSIVE) in subquery T131 Recursive query T132 Recursive query in subquery T151 DISTINCT predicate T152 DISTINCT predicate with negation T171 LIKE clause in table definition T172 AS subquery clause in table definition T173 Extended LIKE clause in table definition T174 Identity columns T175 Generated columns T176 Sequence generator support T177 Sequence generator support: simple restart option T178 Identity columns: simple restart option T180 System-versioned tables T191 Referential action RESTRICT T201 Comparable data types for referential constraints T211 Basic trigger capability T211 Basic trigger capability 01 Triggers activated on UPDATE, INSERT, or DELETE of one base table T211 Basic trigger capability 02 BEFORE triggers T211 Basic trigger capability 03 AFTER triggers T211 Basic trigger capability 04 FOR EACH ROW triggers T211 Basic trigger capability 05 Ability to specify a search condition that must be true before the trigger is invoked T211 Basic trigger capability 06 Support for run-time rules for the interaction of triggers and constraints T211 Basic trigger capability 07 TRIGGER privilege T211 Basic trigger capability 08 Multiple triggers for the same event are executed in the order in which they were created in the catalog T212 Enhanced trigger capability T213 INSTEAD OF triggers T231 Sensitive cursors T241 START TRANSACTION statement T261 Chained transactions T271 Savepoints T272 Enhanced savepoint management T281 SELECT privilege with column granularity T285 Enhanced derived column names T301 Functional dependencies T312 OVERLAY function T321 Basic SQL-invoked routines T321 Basic SQL-invoked routines 01 User-defined functions with no overloading T321 Basic SQL-invoked routines 02 User-defined stored procedures with no overloading T321 Basic SQL-invoked routines 03 Function invocation T321 Basic SQL-invoked routines 04 CALL statement T321 Basic SQL-invoked routines 05 RETURN statement T321 Basic SQL-invoked routines 06 ROUTINES view T321 Basic SQL-invoked routines 07 PARAMETERS view T322 Overloading of SQL-invoked functions and procedures T324 Explicit security for SQL routines T326 Table functions T331 Basic roles T332 Extended roles T341 Overloading of SQL-invoked functions and SQL-invoked procedures T351 Bracketed SQL comments (/*...*/ comments) T431 Extended grouping capabilities T432 Nested and concatenated GROUPING SETS T433 Multiargument GROUPING function T434 GROUP BY DISINCT T441 ABS and MOD functions T461 Symmetric BETWEEN predicate T471 Result sets return value T491 LATERAL derived table T501 Enhanced EXISTS predicate T502 Period predicate T551 Optional key words for default syntax T571 Array-returning external SQL-invoked functions T572 Multiset-returning external SQL-invoked functions T581 Regular expression substring function T591 UNIQUE constraints of possibly null columns T621 Enhanced numeric functions T622 Trigonometric functions T624 Common logarithm functions T626 ANY_VALUE   T631 IN predicate with one list element T641 Multiple column assignment T654 SQL-dynamic statements in external routines T655 Cyclically dependent routines T811 Basic SQL/JSON constructor functions T812 SQL/JSON: JSON_OBJECTAGG with no <JSON key uniqueness constraint> T813 SQL/JSON: JSON_ARRAYAGG with ORDER BY T814 Colon in JSON_OBJECT or JSON_OBJECTAGG T830 Enforcing unique keys in SQL/JSON constructor functions T839 Formatted cast of datetimes to/from character strings

(SourceForge Logo)

###### This page last updated 21 October 2021

###### *Contents of this page are ©2001-2021 The HSQL Development Group. All rights reserved.*
