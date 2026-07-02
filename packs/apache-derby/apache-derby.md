---
title: "Apache Derby"
source: https://en.wikipedia.org/wiki/Apache_Derby
domain: apache-derby
license: CC-BY-SA-4.0
tags: apache derby, java embedded database, javadb, relational database
fetched: 2026-07-02
---

# Apache Derby

**Apache Derby** (previously distributed as **IBM Cloudscape**) is a (retired) relational database management system (RDBMS) developed by the Apache Software Foundation that can be embedded in Java programs and used for online transaction processing. It has a 3.5 MB disk-space footprint.

Apache Derby is developed as an open source project under the Apache 2.0 license. For a time, Oracle distributed the same binaries under the name **Java DB**. In June 2015 they announced that for JDK 9 they would no longer be doing so. In October 2025 Derby developers voted to retire the project and stop supporting it.

## History

Apache Derby originated at Cloudscape Inc, an Oakland, California, start-up founded in 1996 by Nat Wyatt and Howard Torf to develop Java database technology. The first release of the database engine, then called JBMS, was in 1997. Subsequently, the product was renamed Cloudscape and releases were made about every six months.

In 1999, Informix Software, Inc., acquired Cloudscape, Inc. In 2001 IBM acquired the database assets of Informix Software, including Cloudscape. The database engine was re-branded to IBM Cloudscape and releases continued, mainly focusing on embedded use with IBM's Java products and middleware.

In August 2004, IBM contributed the code to the Apache Software Foundation as Derby, an incubator project sponsored by the Apache DB project. In July 2005 the Derby project graduated from the Apache incubator and is now being developed as a sub-project of the DB Top Level Project at Apache. Prior to Derby's graduation from incubation, Sun joined the Derby project with an intent to use Derby as a component in their own products, and with the release of Java 6 in December 2006, Sun started packaging Derby in the JDK branded as Java DB.

In March 2007, IBM announced that they would withdraw marketing and support for the Cloudscape product, but would continue to contribute to the Apache Derby project.

The Java DB database is Oracle's supported distribution of Apache Derby.

## Technologies

### Derby embedded database engine

The core of the technology, Derby's database engine, is a full-functioned relational embedded database-engine, supporting JDBC and SQL as programming APIs. It uses IBM Db2 SQL syntax.

### Derby Network Server

The Derby network server increases the reach of the Derby database engine by providing traditional client server functionality. The network server allows clients to connect over TCP/IP using the standard DRDA protocol. The network server allows the Derby engine to support networked JDBC, ODBC/CLI, Perl.

### Embedded Network Server

An embedded database can be configured to act as a hybrid server/embedded RDBMS; to also accept TCP/IP connections from other clients in addition to clients in the same JVM.

### Database utilities

- ij: a tool that allows SQL scripts to be executed against any JDBC database.
- dblook: Schema extraction tool for a Derby database.
- sysinfo: Utility to display version numbers and class path.
