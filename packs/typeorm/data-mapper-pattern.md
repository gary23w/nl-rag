---
title: "Data mapper pattern"
source: https://en.wikipedia.org/wiki/Data_mapper_pattern
domain: typeorm
license: CC-BY-SA-4.0
tags: typeorm library, typescript orm, data mapper pattern, entity decorators
fetched: 2026-07-02
---

# Data mapper pattern

In software engineering, the **data mapper pattern** is an architectural pattern. It was named by Martin Fowler in his 2003 book *Patterns of Enterprise Application Architecture*. The interface of an object conforming to this pattern would include functions such as Create, Read, Update, and Delete, that operate on objects that represent domain entity types in a data store.

A Data Mapper is a Data Access Layer that performs bidirectional transfer of data between a persistent data store (often a relational database) and an in-memory data representation (the domain layer). The goal of the pattern is to keep the in-memory representation and the persistent data store independent of each other and the data mapper itself. This is useful when one needs to model and enforce strict business processes on the data in the domain layer that do not map neatly to the persistent data store. The layer is composed of one or more mappers (or Data Access Objects), performing the data transfer. Mapper implementations vary in scope. Generic mappers will handle many different domain entity types; dedicated mappers will handle one or a few.

## Implementations

Implementations of the concept can be found in various frameworks for many programming environments.

### Java/.NET

- MyBatis persistence framework
- Hibernate (NHibernate) persistence framework

### Node.js / TypeScript

- Bookshelf.js library
- TypeORM library
- Massive.js library
- Prisma
- Objection.js library
- MikroORM library
- LDkit Object Graph Mapper (OGM) for RDF data sources

### PHP

- Atlas ORM (data mapper, table data gateway, query builder, and PDO wrapper)
- Doctrine2 Object Relational Mapper (ORM) and the Database Abstraction Layer
- Cycle ORM (PHP DataMapper ORM and Data Modelling Engine)
- CakePHP ORM (PHP DataMapper ORM, query builder, and PDO wrapper)

### Perl

- DBIx

### Python

- SQLAlchemy library
- mincePy library

### Ruby

- DataMapper library (Actually this library implemented the Active Record design pattern, its successor, DataMapper 2 (now ROM) aimed to actually implement the design pattern it was named after)

### Elixir

- Ecto persistence framework
