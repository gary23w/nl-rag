---
title: "gel/README.md at master · geldata/gel · GitHub"
source: https://github.com/geldata/gel/blob/master/README.md
domain: edgedb
license: CC-BY-SA-4.0
tags: edgedb, gel database, graph-relational database, edgeql query language
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

geldata

/

gel

Public

- Notifications You must be signed in to change notification settings
- Fork 450
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

214 lines (178 loc) · 6.43 KB

Outline

# Gel

Learn: build an app with Gel

•

Website

•

Docs

•

Blog

•

Discord

•

Twitter

## What is Gel?

Gel is a new kind of database that takes the best parts of relational databases, graph databases, and ORMs. We call it a **graph-relational database**.

### 🧩 Types, not tables 🧩

Schema is the foundation of your application. It should be something you can read, write, and understand.

Forget foreign keys; tabular data modeling is a relic of an older age, and it isn't compatible with modern languages. Instead, Gel thinks about schema the same way you do: as **object types** containing **properties** connected by **links**.

```highlight
type Person {
  required name: str;
}

type Movie {
  required title: str;
  multi actors: Person;
}
```

This example is intentionally simple, but Gel supports everything you'd expect from your database: a strict type system, indexes, constraints, computed properties, stored procedures...the list goes on. Plus it gives you some shiny new features too: link properties, schema mixins, and best-in-class JSON support. Read the schema docs for details.

### 🌳 Objects, not rows 🌳

Gel's super-powered query language EdgeQL is designed as a ground-up redesign of SQL. EdgeQL queries produce rich, structured objects, not flat lists of rows. Deeply fetching related objects is painless...bye, bye, JOINs.

```highlight
select Movie {
  title,
  actors: {
    name
  }
}
filter .title = "The Matrix"
```

EdgeQL queries are also *composable*; you can use one EdgeQL query as an expression inside another. This property makes things like *subqueries* and *nested mutations* a breeze.

```highlight
insert Movie {
  title := "The Matrix Resurrections",
  actors := (
    select Person
    filter .name in {
      'Keanu Reeves',
      'Carrie-Anne Moss',
      'Laurence Fishburne'
    }
  )
}
```

There's a lot more to EdgeQL: a comprehensive standard library, computed properties, polymorphic queries, `with` blocks, transactions, and much more. Read the EdgeQL docs for the full picture.

### 🦋 More than a mapper 🦋

While Gel solves the same problems as ORM libraries, it's so much more. It's a full-fledged database with a powerful and elegant query language, a migrations system, a suite of client libraries in different languages, a command line tool, and a managed cloud service. The goal is to rethink every aspect of how developers model, migrate, manage, and query their database.

Here's a taste-test of Gel's next-level developer experience: you can install our CLI, spin up an instance, and open an interactive EdgeQL shell with just three commands.

```
$ curl --proto '=https' --tlsv1.2 -sSf https://geldata.com/sh | sh
$ edgedb project init
$ edgedb
edgedb> select "Hello world!"
```

Windows users: use this Powershell command to install the CLI.

```
PS> iwr https://geldata.com/ps1 -useb | iex
```

## Get started

To start learning about Gel, check out the following resources:

- **The quickstart**. If you're just starting out, the 10-minute quickstart guide is the fastest way to get up and running.
- **Gel Cloud 🌤️**. The best most effortless way to host your Gel database in the cloud.

- **The docs.** Jump straight into the docs for schema modeling or EdgeQL!

## Contributing

PRs are always welcome! To get started, follow this guide to build Gel from source on your local machine.

File an issue 👉 Start a Discussion 👉 Join the discord 👉

## License

The code in this repository is developed and distributed under the Apache 2.0 license. See LICENSE for details.
