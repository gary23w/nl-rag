---
title: "HyperSQL User Guide"
source: https://hsqldb.org/doc/2.0/guide/index.html
domain: hsqldb
license: CC-BY-SA-4.0
tags: hsqldb database, hypersql database, java database, embedded database
fetched: 2026-07-02
---

# HyperSQL User Guide

## HyperSQL Database Engine 2.7.4

| Edited by The HSQL Development Group Edited by Blaine Simpson The HSQL Development Group Edited by Fred Toussi The HSQL Development Group Copyright 2002-2024 Blaine Simpson, Fred Toussi and The HSQL Development Group. Permission is granted to distribute this document without any alteration under the terms of the HSQLDB license. You are not allowed to distribute or display this document on the web in an altered form. 2024-10-25 |   |
|---|---|

**Table of Contents**

**Preface**

**Available formats for this document**

**1. Running and Using HyperSQL**

**Introduction**

**The HSQLDB Jar**

**Running Database Access Tools**

**A HyperSQL Database**

**In-Process Access to Database Catalogs**

**Server Modes**

**HyperSQL HSQL Server**

**HyperSQL HTTP Server**

**HyperSQL HTTP Servlet**

**Connecting to a Database Server**

**Security Considerations**

**Using Multiple Databases**

**Accessing the Data**

**Closing the Database**

**Creating a New Database**

**2. SQL Language**

**SQL Standards Support**

**Definition Statements (DDL and others)**

**Data Manipulation Statements (DML)**

**Data Query Statements (DQL)**

**Calling User Defined Procedures and Functions**

**Setting Properties for the Database and the Session**

**General Operations on Database**

**Transaction Statements**

**Comments in Statements**

**Statements in SQL Routines**

**SQL Data and Tables**

**Case Sensitivity**

**Persistent Tables**

**Temporary Tables**

**Short Guide to Data Types**

**Data Types and Operations**

**Numeric Types**

**Boolean Type**

**Character String Types**

**Binary String Types**

**Bit String Types**

**Lob Data**

**Storage and Handling of Java Objects**

**Type Length, Precision and Scale**

**Datetime types**

**Interval Types**

**Arrays**

**Array Definition**

**Array Reference**

**Array Operations**

**3. Schemas and Database Objects**

**Overview**

**Schemas and Schema Objects**

**Names and References**

**Character Sets**

**Collations**

**Distinct Types**

**Domains**

**Number Sequences**

**Tables**

**Views**

**Constraints**

**Assertions**

**Triggers**

**Routines**

**Indexes**

**Synonyms**

**Statements for Schema Definition and Manipulation**

**Common Elements and Statements**

**Renaming Objects**

**Commenting Objects**

**Schema Creation**

**Table Creation**

**Temporal System-Versioned Tables and SYSTEM_TIME Period**

**Table Settings**

**Table Manipulation**

**View Creation and Manipulation**

**Domain Creation and Manipulation**

**Trigger Creation**

**Routine Creation**

**Sequence Creation**

**SQL Procedure Statement**

**Other Schema Objects Creation and Alteration**

**The Information Schema**

**References to Database Objects**

**Predefined Character Sets, Collations and Domains**

**Views in INFORMATION SCHEMA**

**Visibility of Information**

**Name Information**

**Data Type Information**

**Product Information**

**Operations Information**

**SQL Standard Views**

**4. Built In Functions**

**Overview**

**String and Binary String Functions**

**JSON Functions**

**Numeric Functions**

**Date Time and Interval Functions**

**Functions to Report the Time Zone.**

**Functions to Report the Current Datetime**

**Functions to Extract an Element of a Datetime**

**Functions for Datetime Arithmetic**

**Functions to Convert or Format a Datetime**

**Array Functions**

**General Functions**

**System Functions**

**5. Data Access and Change**

**Overview**

**Cursors And Result Sets**

**Columns and Rows**

**Navigation**

**Updatability**

**Sensitivity**

**Holdability**

**Autocommit**

**JDBC Overview**

**JDBC Parameters**

**JDBC and Data Change Statements**

**JDBC Callable Statement**

**JDBC Returned Values**

**Cursor Declaration**

**Syntax Elements**

**Literals**

**References, etc.**

**Value Expression**

**Predicates**

**Aggregate Functions**

**Other Syntax Elements**

**Data Access Statements**

**Select Statement**

**Table**

**Subquery**

**Query Specification**

**Table Expression**

**Joined Table**

**Selection**

**Projection**

**Computed Columns**

**Naming**

**Grouping Operations**

**Aggregation**

**Set Operations**

**With Clause and Recursive Queries**

**Query Expression**

**Ordering**

**Slicing**

**Indexes Used in SELECT and DML Statements**

**Data Change Statements**

**Delete Statement**

**Truncate Statement**

**Insert Statement**

**Update Statement**

**Merge Statement**

**Diagnostics and State**

**6. Sessions and Transactions**

**Overview**

**Session Attributes and Variables**

**Session Attributes**

**Session Variables**

**Session Tables**

**Transactions and Concurrency Control**

**Two Phase Locking**

**Two Phase Locking with Snapshot Isolation**

**Lock Contention in 2PL**

**Locks in SQL Routines and Triggers**

**MVCC**

**Choosing the Transaction Model**

**Schema and Database Change**

**Simultaneous Access to Tables**

**Viewing Sessions**

**Session and Transaction Control Statements**

**7. Text Tables**

**Overview**

**The Implementation**

**Definition of Tables**

**Scope and Reassignment**

**Null Values in Columns of Text Tables**

**Configuration**

**Disconnecting Text Tables**

**Text File Usage**

**Text File Global Properties**

**Transactions**

**8. Access Control**

**Overview**

**Authorizations and Access Control**

**Built-In Roles and Users**

**Listing Users and Roles**

**Access Rights**

**Simple Access Control**

**Fine-Grained Data Access Control**

**Statements for Authorization and Access Control**

**9. SQL-Invoked Routines**

**Overview**

**Routine Definition**

**Routine Characteristics**

**SQL Language Routines (PSM)**

**Advantages and Disadvantages**

**Routine Statements**

**Compound Statement**

**Table Variables**

**Variables**

**Cursors**

**Handlers**

**Assignment Statement**

**Select Statement : Single Row**

**Formal Parameters**

**Iterated Statements**

**Iterated FOR Statement**

**Conditional Statements**

**Return Statement**

**Control Statements**

**Raising Exceptions**

**Routine Polymorphism**

**Returning Data From Procedures**

**Recursive Routines**

**Java Language Routines (SQL/JRT)**

**Polymorphism**

**Java Language Procedures**

**Java Static Methods**

**Legacy Support**

**Securing Access to Classes and Routines**

**Warning**

**User-Defined Aggregate Functions**

**Definition of Aggregate Functions**

**SQL PSM Aggregate Functions**

**Java Aggregate Functions**

**10. Triggers**

**Overview**

**BEFORE Triggers**

**AFTER Triggers**

**INSTEAD OF Triggers**

**Trigger Properties**

**Trigger Event**

**Granularity**

**Trigger Action Time**

**References to Rows**

**Trigger Condition**

**Trigger Action in SQL**

**Trigger Action in Java**

**Trigger Creation**

**11. System Management**

**Modes of Operation**

**Deployment Types**

**Database Types**

**Tables**

**Large Objects**

**Deployment context**

**Indexes and Query Speed**

**Query Processing and Optimisation**

**Indexes and Conditions**

**Indexes and Operations**

**Indexes and ORDER BY, OFFSET and LIMIT**

**ACID, Persistence and Reliability**

**Atomicity, Consistency, Isolation, Durability**

**System Operations**

**Temporal System-Versioned Tables**

**Replicated Databases**

**Using Table Spaces**

**Checking Database Tables and Indexes**

**Backing Up and Restoring Database Catalogs**

**Making Online Backups**

**Offline Backup Utility Syntax**

**Making Offline Backups**

**Examining Backups**

**Restoring a Backup**

**Encrypted Databases**

**Creating and Accessing an Encrypted Database**

**Speed Considerations**

**Security Considerations**

**Monitoring Database Operations**

**External Statement Level Monitoring**

**Internal Statement Level Monitoring**

**Internal Event Monitoring**

**Log4J and JDK logging**

**Server Operation Monitoring**

**Database Security**

**Basic Security Recommendations**

**Beyond Security Defaults**

**Authentication Control**

**Statements**

**System Operations**

**Data Management Statements**

**Database Settings**

**SQL Conformance Settings**

**Cache, Persistence and Files Settings**

**Authentication Settings**

**12. Deployment Guide**

**Memory and Disk Use**

**Table Memory Allocation**

**Data Cache Memory Allocation**

**Result Set Memory Allocation**

**Temporary Memory Use During Operations**

**Object Pool Memory Allocation**

**Lob Memory Usage**

**Using NIO File Access**

**Disk Space Use**

**Using HyperSQL Without Logging Data Change**

**Bulk Inserts, Updates and Deletes**

**Managing Database Connections**

**Application Development and Testing**

**Tweaking the Mode of Operation**

**Embedded Databases in Desktop Applications**

**Embedded Databases in Server Applications**

**Mixed Mode : Embedding a HyperSQL Server (Listener)**

**Server Databases**

**Upgrading Databases**

**Manual Changes to the *.script File**

**Backward Compatibility Issues**

**HyperSQL Dependency Settings for Applications**

**What version to Pull**

**Range Versioning**

**13. Compatibility With Other DBMS**

**Compatibility Overview**

**PostgreSQL Compatibility**

**MySQL Compatibility**

**Firebird Compatibility**

**Apache Derby Compatibility**

**Oracle Compatibility**

**DB2 Compatibility**

**MS SQLServer and Sybase Compatibility**

**14. Properties**

**Connection URL**

**Variables in Connection URL**

**Connection Properties**

**Properties for Individual Connections**

**Properties for the Database**

**SQL Conformance Properties**

**Database Operations Properties**

**Database File and Memory Properties**

**Crypt Properties**

**System Properties**

**15. HyperSQL Network Listeners (Servers)**

**Listeners**

**HyperSQL Server**

**HyperSQL HTTP Server**

**HyperSQL HTTP Servlet**

**Server and Web Server Properties**

**Starting a Server from your Application**

**Shutting down a Server from your Application**

**Allowing a Connection to Open or Create a Database**

**Specifying Database Properties at Server Start**

**TLS Encryption**

**Requirements**

**Encrypting your JDBC connection**

**Making a Private-key Keystore**

**Automatic Server or WebServer startup on UNIX**

**Network Access Control**

**16. HyperSQL on UNIX**

**Purpose**

**Installation**

**Setting up Database Catalog and Listener**

**Accessing your Database**

**Create additional Accounts**

**Shutdown**

**Running Hsqldb as a System Daemon**

**Portability of `hsqldb` init script**

**Init script Setup Procedure**

**Troubleshooting the Init Script**

**Upgrading**

**17. HyperSQL via ODBC**

**Overview**

**Unix / Linux Installation**

**Windows Installation**

**Settings**

**Samples**

**Table of Settings**

**A. Lists of Keywords**

**List of SQL Standard Keywords**

**List of SQL Keywords Disallowed as HyperSQL Identifiers**

**Special Function Keywords**

**B. HyperSQL Database Files and Recovery**

**Database Files**

**States**

**Procedures**

**Clean Shutdown**

**Startup**

**Restore**

**C. Building HSQLDB Jars**

**Purpose**

**Building with Gradle**

**Building with Ant**

**Obtaining Ant**

**Building HSQLDB with Ant**

**Building with IDE Compilers**

**HyperSQL CodeSwitcher**

**Building Documentation**

**D. HyperSQL with OpenOffice**

**HyperSQL with OpenOffice**

**Using OpenOffice / LibreOffice as a Database Tool**

**Converting .odb files to use with HyperSQL Server**

**OpenOffice / LibreOffice Extensions for HyperSQL**

**E. HyperSQL File Links**

**SQL Index**

**General Index**

**List of Tables**

**1. Available formats of this document**

**2.1. List of SQL types**

**4.1. TO_CHAR (number) format elements**

**4.2. TO_CHAR, TO_DATE and TO_TIMESTAMP format elements**

**14.1. Memory Database URL**

**14.2. File Database URL**

**14.3. Resource Database URL**

**14.4. Server Database URL**

**14.5. User and Password**

**14.6. Closing old ResultSet when Statement is reused**

**14.7. Column Names in JDBC ResultSet**

**14.8. In-memory LOBs from JDBC ResultSet**

**14.9. Empty batch in JDBC PreparedStatement**

**14.10. Automatic Shutdown**

**14.11. OpenOffice and Libre Office usage**

**14.12. Validity Check Property**

**14.13. Creating New Database Check Property**

**14.14. Execution of Multiple SQL Statements etc.**

**14.15. SQL Keyword Use as Identifier**

**14.16. SQL Keyword Starting with the Underscore or Containing Dollar Characters**

**14.17. Reference to Columns Names**

**14.18. String Size Declaration**

**14.19. Truncation of trailing spaces from string**

**14.20. Type Enforcement in Comparison and Assignment**

**14.21. Foreign Key Triggered Data Change**

**14.22. Use of LOB for LONGVAR Types**

**14.23. Type of string literals in CASE WHEN**

**14.24. Concatenation with NULL**

**14.25. NULL in Multi-Column UNIQUE Constraints**

**14.26. Truncation or Rounding in Type Conversion**

**14.27. Decimal Scale of Division and AVG Values**

**14.28. Support for NaN values**

**14.29. Sort order of NULL values**

**14.30. Sort order of NULL values with DESC**

**14.31. String Comparison with Padding**

**14.32. Default Locale Language Collation**

**14.33. Case-Insensitive Varchar columns**

**14.34. Lowercase column identifiers in ResultSet**

**14.35. Storage of Live Java Objects**

**14.36. Names of System Indexes Used for Constraints**

**14.37. DB2 Style Syntax**

**14.38. MSSQL Style Syntax**

**14.39. MySQL Style Syntax**

**14.40. Oracle Style Syntax**

**14.41. PostgreSQL Style Syntax**

**14.42. Maximum Iterations of Recursive Queries**

**14.43. Default Table Type**

**14.44. Transaction Control Mode**

**14.45. Default Isolation Level for Sessions**

**14.46. Transaction Rollback in Deadlock**

**14.47. Transaction Rollback on Interrupt**

**14.48. Interval Types**

**14.49. Temporary Result Rows in Memory**

**14.50. Opening Database as Read Only**

**14.51. Opening Database Without Modifying the Files**

**14.52. Event Logging**

**14.53. SQL Logging**

**14.54. Table Spaces for Cached Tables**

**14.55. Huge database files and tables**

**14.56. Use of NIO for Disk Table Storage**

**14.57. Use of NIO for Disk Table Storage**

**14.58. Internal Backup of the .data File**

**14.59. Unused Space Recovery**

**14.60. Rows Cached In Memory**

**14.61. Size of Rows Cached in Memory**

**14.62. Size Scale of Disk Table Storage**

**14.63. Size Scale of LOB Storage**

**14.64. Compression of BLOB and CLOB data**

**14.65. Use of Lock File**

**14.66. Logging Data Change Statements**

**14.67. Automatic Checkpoint Frequency**

**14.68. Automatic Defrag at Checkpoint**

**14.69. Compression of the .script file**

**14.70. Logging Data Change Statements Frequency**

**14.71. Logging Data Change Statements Frequency**

**14.72. Recovery Log Processing**

**14.73. Default Properties for TEXT Tables**

**14.74. Forcing Garbage Collection**

**14.75. Crypt Property For LOBs**

**14.76. Cipher Key for Encrypted Database**

**14.77. Cipher Initialization Vector for Encrypted Database**

**14.78. Crypt Provider Encrypted Database**

**14.79. Cipher Specification for Encrypted Database**

**14.80. Logging Framework**

**14.81. Text Tables**

**14.82. Java Functions**

**15.1. common server and webserver properties**

**15.2. server properties**

**15.3. webserver properties**

**17.1. Settings List**

**List of Examples**

**1.1. Java code to connect to the local hsql Server**

**1.2. Java code to connect to the local http Server**

**1.3. Java code to connect to the local secure SSL hsqls: and https: Servers**

**1.4. specifying a connection property to shutdown the database when the last connection is closed**

**1.5. specifying a connection property to disallow creating a new database**

**3.1. inserting the next sequence value into a table row**

**3.2. numbering returned rows of a SELECT in sequential order**

**3.3. using the last value of a sequence**

**3.4. Column values which satisfy a 2-column UNIQUE constraint**

**6.1. User-defined Session Variables**

**6.2. User-defined Temporary Session Tables**

**6.3. Setting Transaction Characteristics**

**6.4. Locking Tables**

**6.5. Rollback**

**6.6. Setting Session Characteristics**

**6.7. Setting Session Authorization**

**6.8. Setting Session Time Zone**

**11.1. Using CACHED tables for the LOB schema**

**11.2. Creating a system-versioned table**

**11.3. Displaying DbBackup Syntax**

**11.4. Offline Backup Example**

**11.5. Listing a Backup with DbBackup**

**11.6. Restoring a Backup with DbBackup**

**11.7. SQL Log Example**

**11.8. Finding foreign key rows with no parents after a bulk import**

**12.1. Using CACHED tables for the LOB schema**

**12.2. MainInvoker Example**

**12.3. Sample Range Ivy Dependency**

**12.4. Sample Range Maven Dependency**

**12.5. Sample Range Gradle Dependency**

**12.6. Sample Range ivy.xml loaded by Ivyxml plugin**

**12.7. Sample Range Groovy Dependency, using Grape**

**15.1. Exporting certificate from the server's keystore**

**15.2. Adding a certificate to the client keystore**

**15.3. Specifying your own trust store to a JDBC client**

**15.4. Getting a pem-style private key into a JKS keystore**

**15.5. Validating and Testing an ACL file**

**16.1. example sqltool.rc stanza**

**C.1. Buiding the standard HSQLDB jar file with Ant**

**C.2. Example source code before CodeSwitcher is run**

**C.3. CodeSwitcher command line invocation**

**C.4. Source code after CodeSwitcher processing**
