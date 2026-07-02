---
title: "Jakarta Persistence"
source: https://en.wikipedia.org/wiki/Jakarta_Persistence
domain: hibernate-orm
license: CC-BY-SA-4.0
tags: hibernate orm, jpa persistence, hql query, java persistence
fetched: 2026-07-02
---

# Jakarta Persistence

**Jakarta Persistence**, also known as **JPA** (abbreviated from the former name **Java Persistence API**) is a Jakarta EE application programming interface specification that describes the management of relational data in enterprise Java applications.

Persistence in this context covers three areas:

- The API itself, defined in the `jakarta.persistence` package (`javax.persistence` for Jakarta EE 8 and below)
- The Jakarta Persistence Query Language (JPQL; formerly Java Persistence Query Language)
- Object/relational metadata

## History

The final release date of the JPA 1.0 specification was 11 May 2006 as part of Java Community Process JSR 220. The JPA 2.0 specification was released 10 December 2009 (the Java EE 6 platform requires JPA 2.0). The JPA 2.1 specification was released 22 April 2013 (the Java EE 7 platform requires JPA 2.1). The JPA 2.2 specification was released in the summer of 2017. The reference implementation for JPA 1 and 2 was EclipseLink.

Jakarta Persistence 3.1 was released in the spring of 2022 as part of Jakarta EE 10. Jakarta Persistence 3.2 was released in spring 2024, targeting inclusion in Jakarta EE 11. EclipseLink and Hibernate are compatible implementations.

## Entities

A persistence entity is a lightweight Java class with its state typically persisted to a table in a relational database. Instances of such an entity correspond to individual rows in the table. Entities typically have relationships with other entities, and these relationships are expressed through object/relational mapping (ORM) metadata. This metadata may be specified directly in the entity class file by using annotations or in a separate XML descriptor file distributed with the application.

### Example

An example entity class with ORM metadata declared using annotations (import statements and setters/getters are omitted for simplicity).

```mw
@Entity
public class Person {
    @Id
    private long id;
    private String firstName;
    private String lastName;
    private int age;
}
```

The `@Entity` annotation declares that the class represents an entity. `@Id` declares the attribute which acts as the primary key of the entity. Additional annotations may be used to declare additional metadata (for example changing the default table name in the `@Table` annotation), or to create associations between entities.

## Query Language

The Jakarta Persistence Query Language (JPQL; formerly Java Persistence Query Language) makes queries against entities stored in a relational database. Queries resemble SQL queries in syntax but operate against entity objects rather than directly with database tables.

## Motivation

Prior to the introduction of EJB 3.0 specification, many enterprise Java developers used lightweight persistent objects provided by either persistence frameworks (such as Hibernate) or data access objects (DAO) instead of by using entity beans. This is because entity beans, in previous EJB specifications, called for much complicated code and imposed a heavy resource footprint, and they could be used only on Java EE application servers because of interconnections and dependencies in the source code between beans and DAO objects or persistence frameworks. Thus, many of the features originally presented in third-party persistence frameworks were incorporated into the Java Persistence API, and projects such as Hibernate and TopLink Essentials have become implementations of the Java Persistence API specification.

### Enterprise Beans

The EJB 3.0 specification (itself part of the Java EE 5 platform) included a definition of the Java Persistence API. However, developers do not need an EJB container or a Java EE application server to run applications that use this persistence API. Future versions of the Java Persistence API will be defined in a separate JSR and specification rather than in the EJB JSR/specification.

The Java Persistence API replaces the persistence solution of EJB 2.0 CMP (Container-Managed Persistence).

### Java Data Objects API

The Java Persistence API was developed in part to unify the Java Data Objects API and the EJB 2.0 Container Managed Persistence (CMP) API. Most products supporting each of the two APIs support the Java Persistence API.

The Java Persistence API specifies persistence only for relational database management systems by focusing on object-relational mapping (ORM). Some JPA providers support other database models, though this is outside the scope of JPA's design. The introduction section of the JPA specification states: "The technical objective of this work is to provide an object/relational mapping facility for the Java application developer using a Java domain model to manage a relational database."

The Java Data Objects specification supports ORM as well as persistence to other types of database models, for example, flat file databases and NoSQL databases, including document databases, graph databases any many other datastores.

### Hibernate

Hibernate, founded by Gavin King, provides an open source object-relational mapping framework for Java. Versions 3.2 and later provide an implementation for the Java Persistence API. King represented JBoss on JSR 220, the JCP expert group charged with developing JPA. This led to ongoing controversy and speculation surrounding the relationship between JPA and Hibernate. Sun Microsystems stated that ideas came from several frameworks, including Hibernate and Java Data Objects.

### Spring Data JPA

The Spring Data JPA is an implementation of the repository abstraction that is a key building block of domain-driven design based on the Java application framework Spring. It transparently supports all available JPA implementations and supports CRUD operations as well as the convenient execution of database queries.

## Version history

### JPA 2.0

Development of a new version of JPA 2.0 was started in July 2007 in the Java Community Process as JSR 317. JPA 2.0 was approved as final on 10 December 2009. The focus of JPA 2.0 was to address features that were present in some of the popular ORM vendors but could not gain consensus approval for JPA 1.0.

Main features included were:

- Expanded object-relational mapping functionality
  - Support for collections of embedded objects, linked in the ORM with a many-to-one relationship
  - Ordered lists
  - Combinations of access types
- A criteria query API
- Standardization of SQL Hints
- Standardization of additional metadata to support DDL generation
- Support for validation
- Shared object cache support.

Vendors supporting JPA 2.0:

- Batoo JPA
- DataNucleus (formerly JPOX)
- EclipseLink (formerly Oracle TopLink)
- IBM, for WebSphere Application Server
- JBoss with Hibernate
- ObjectDB
- OpenJPA
- OrientDB
- Versant Corporation JPA (object database)

### JPA 2.1

Development of JPA version 2.1 began in July 2011 as JSR 338. JPA 2.1 was approved as final on 22 May 2013.

Main features included were:

- Converters, which allow custom code conversions between database and object types
- Criteria update/delete to allow bulk updates and deletes through the Criteria API
- Entity graphs for partial or specified fetching or merging of objects.
- JPQL/Criteria enhancements such as arithmetic subqueries, generic database functions, join ON clause and the TREAT option.
- Schema generation
- Support for stored procedures

Vendors supporting JPA 2.1:

- DataNucleus
- EclipseLink
- Hibernate
- OpenJPA (from version 2.2.0)

### JPA 2.2

Development of JPA 2.2, a maintenance release, began in 2017 under JSR 338. The maintenance review was approved on 19 June 2017.

Main features included were:

- The addition of @Repeatable to all relevant annotations
- Support for JPA annotations to be used in metaannotations
- Streaming for query results
- The ability for AttributeConverters to be CDI-injectable
- Support for Java 8 date and time types

Vendors supporting JPA 2.2:

- DataNucleus (from version 5.1)
- EclipseLink (from version 2.7)
- Hibernate (from version 5.3)
- OpenJPA (from version 3.0)

### Jakarta Persistence 3.0

The JPA was renamed as Jakarta Persistence in 2019 and version 3.0 was released in 2020. This included the renaming of packages and properties from javax.persistence to jakarta.persistence.

Vendors supporting Jakarta Persistence 3.0:

- DataNucleus (from version 6.0)
- EclipseLink (from version 3.0)
- Hibernate (from version 5.5)
- OpenJPA (from version 4.0)

### Jakarta Persistence 3.1

Version 3.1 was released in 2022. It is part of Jakarta EE 10, and thus requires at least Java 11 to run. It adds better UUID handling, various new JPQL functions for math and date/time handling, and other small changes.

Vendors supporting Jakarta Persistence 3.1:

- DataNucleus (from version 6.0)
- EclipseLink (from version 4.0)
- Hibernate (from version 6.0)
- OpenJPA (from version 4.0)

### Jakarta Persistence 3.2

Version 3.2 was released in 2024. It introduced a large number of API improvements along with some improvements to the query language.

Vendors supporting Jakarta Persistence 3.2:

- EclipseLink (from version 5.0)
- Hibernate (from version 7.0)
