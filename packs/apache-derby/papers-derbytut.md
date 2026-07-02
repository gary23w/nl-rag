---
title: "Apache Derby Tutorial"
source: https://db.apache.org/derby/papers/DerbyTut/
domain: apache-derby
license: CC-BY-SA-4.0
tags: apache derby, java embedded database, javadb, relational database
fetched: 2026-07-02
---

# Apache Derby Tutorial

Font size:

# Apache Derby Tutorial

- Overview
- Intended Audience
- Tutorial Topics
- Next Steps
  - More Information
  - Using Derby with other Products

## Overview

Apache Derby, an Apache DB subproject, is a relational database implemented in Java. Its footprint is so small you can easily embed it in any Java-based solution. In addition to its embedded framework, Derby supports a more familiar client/server framework with the Derby Network Server. This tutorial introduces Derby's basic features and walks you through using both frameworks; first the embedded framework using the Derby Embedded JDBC driver, then the Network Server framework using the Derby Network Client JDBC driver.

## Intended Audience

This tutorial is intended for new Derby users who have had at least light exposure to SQL, Java, and JDBC.

## Tutorial Topics

This tutorial is organized into the sections below:

1. Install Software shows how to:
  - Install the Apache Derby software.
  - Configure your environment to use the Derby Embedded JDBC driver.
  - Verify your installation with the sysinfo tool.
2. ij Basics shows how to use the ij tool with the embedded Derby JDBC driver to create a database and execute SQL queries.
3. Embedded Derby shows how to compile and run a simple Java application that uses the Derby Embedded JDBC driver.
4. Derby Network Server show how to:
  - Start the Derby Network Server.
  - Configure your environment to use the Derby Network Client JDBC driver.
  - Compile and run a simple Java application that uses the network server.

## Next Steps

After completing the four steps in this tutorial, you'll understand the basics of how to use Derby in the embedded and Network Server frameworks.

### More Information

More information about Derby is on the Derby web site and on the Derby Wiki. Please post any problems or questions to the derby-user@db.apache.org mail list.

### Using Derby with other Products

Below is a partial list of resources on the Derby web site that show how to use Derby with another product:

- **Tools**:
  - DdlUtils
  - Eclipse
- **Data Mappers**:
  - iBATIS
  - JPOX JDO
  - Torque
- **Web Applications**:
  - Geronimo
  - Tomcat 5.0
  - Tomcat 5.5
  - WebSphere

More products that work with Derby are summarized on the UsesOfDerby Wiki page.

*Last updated: April 30, 2008*
