---
title: "Prisma schema"
source: https://www.prisma.io/docs/orm/prisma-schema/overview
domain: prisma-orm
license: CC-BY-SA-4.0
tags: prisma orm, prisma schema, prisma client, typescript orm
fetched: 2026-07-02
---

# Prisma schema

Overview

# Overview of Prisma Schema

The Prisma schema is the main method of configuration when using Prisma. It is typically called schema.prisma and contains your database connection and data model

The Prisma Schema (or *schema* for short) is the main method of configuration for your Prisma ORM setup. It consists of the following parts:

- **Data sources**: Specify the details of the data sources Prisma ORM should connect to (e.g. a PostgreSQL database)
- **Generators**: Specifies what clients should be generated based on the data model (e.g. Prisma Client)
- **Data model definition**: Specifies your application models (the shape of the data per data source) and their relations

It is typically a single file called `schema.prisma` (or multiple files with `.prisma` file extension) that is stored in a defined but customizable location. You can also organize your Prisma schema in multiple files if you prefer that.

See the Prisma schema API reference for detailed information about each section of the schema.

Whenever a `prisma` command is invoked, the CLI typically reads some information from the schema, e.g.:

- `prisma generate`: Reads *all* above mentioned information from the Prisma schema to generate the correct data source client code (e.g. Prisma Client).
- `prisma migrate dev`: Reads the data sources and data model definition to create a new migration.

You can also use environment variables inside the schema to provide configuration options when a CLI command is invoked.

## Example

The following is an example of a Prisma Schema that specifies:

- A data source (PostgreSQL or MongoDB)
- A generator (Prisma Client)
- A data model definition with two models (with one relation) and one `enum`
- Several native data type attributes (`@db.VarChar(255)`, `@db.ObjectId`)

```
datasource db {
  provider = "postgresql"
}

generator client {
  provider = "prisma-client"
  output   = "./generated"
}

model User {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  email     String   @unique
  name      String?
  role      Role     @default(USER)
  posts     Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  published Boolean  @default(false)
  title     String   @db.VarChar(255)
  author    User     @relation(fields: [authorId], references: [id])
  authorId  Int
}

enum Role {
  USER
  ADMIN
}
```

## Syntax

Prisma Schema files are written in Prisma Schema Language (PSL). See the data sources, generators, data model definition and of course Prisma Schema API reference pages for details and examples.

### VS Code

Syntax highlighting for PSL is available via a VS Code extension (which also lets you auto-format the contents of your Prisma schema and indicates syntax errors with red squiggly lines). Learn more about setting up Prisma ORM in your editor.

### GitHub

PSL code snippets on GitHub can be rendered with syntax highlighting as well by using the `.prisma` file extension or annotating fenced code blocks in Markdown with `prisma`:

````
```prisma
model User {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  email     String   @unique
  name      String?
}
```
````

## Accessing environment variables from the schema

You can use environment variables to provide configuration options when a CLI command is invoked, or a Prisma Client query is run.

Hardcoding URLs directly in your schema is possible but is discouraged because it poses a security risk. Using environment variables in the schema allows you to **keep secrets out of the schema** which in turn **improves the portability of the schema** by allowing you to use it in different environments.

Environment variables can be accessed using the `env()` function:

```
datasource db {
  provider = "postgresql"
}
```

You can use the `env()` function in the following places:

- A datasource url
- Generator binary targets

See Environment variables for more information about how to use an `.env` file during development.

There are three types of comments that are supported in Prisma Schema Language:

- `// comment`: This comment is for the reader's clarity and is not present in the abstract syntax tree (AST) of the schema.
- `/// comment`: These comments will show up in the abstract syntax tree (AST) of the schema as descriptions to AST nodes. Tools can then use these comments to provide additional information. All comments are attached to the next available node - free-floating comments are not supported and are not included in the AST.
- `/* block comment */`: These comments will show up in the abstract syntax tree, similarly to `///` comments.

Here are some different examples:

```
/// This comment will get attached to the `User` node in the AST
model User {
  /// This comment will get attached to the `id` node in the AST
  id     Int   @default(autoincrement())
  // This comment is just for you
  weight Float /// This comment gets attached to the `weight` node
}

// This comment is just for you. It will not
// show up in the AST.

/// This comment will get attached to the
/// Customer node.
model Customer {
  /**
   * ...and so will this comment
   */
}
```

## Auto formatting

Prisma ORM supports formatting `.prisma` files automatically. There are two ways to format `.prisma` files:

- Run the `prisma format` command.
- Install the Prisma VS Code extension and invoke the VS Code format action - manually or on save.

There are no configuration options - formatting rules are fixed (similar to Golang's `gofmt` but unlike Javascript's `prettier`):

### Formatting rules

#### Configuration blocks are aligned by their = sign

```
block _ {
  key      = "value"
  key2     = 1
  long_key = true
}
```

#### Field definitions are aligned into columns separated by 2 or more spaces

```
block _ {
  id          String       @id
  first_name  LongNumeric  @default
}
```

#### Empty lines resets block alignment and formatting rules

```
block _ {
  key   = "value"
  key2  = 1
  key10 = true

  long_key   = true
  long_key_2 = true
}
```

```
block _ {
  id  String  @id
              @default

  first_name  LongNumeric  @default
}
```

#### Multiline field attributes are properly aligned with the rest of the field attributes

```
block _ {
  id          String       @id
                           @default
  first_name  LongNumeric  @default
}
```

#### Block attributes are sorted to the end of the block

```
block _ {
  key   = "value"

  @@attribute
}
```

Edit on GitHub

API patterns

How to use Prisma ORM with REST APIs, GraphQL servers, and fullstack frameworks

Data sources

Data sources enable Prisma to connect to your database. This page explains how to configure data sources in your Prisma schema
