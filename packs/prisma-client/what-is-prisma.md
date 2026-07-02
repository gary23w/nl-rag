---
title: "What is Prisma ORM? (Overview)"
source: https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma
domain: prisma-client
license: CC-BY-SA-4.0
tags: prisma client, type-safe orm, prisma schema, database migration engine
fetched: 2026-07-02
---

# What is Prisma ORM? (Overview)

Introduction

# What is Prisma ORM?

This page gives a high-level overview of what Prisma ORM is and how it works. It's a great starting point for Prisma newcomers!

Prisma ORM is an open-source next-generation ORM. It consists of the following parts:

- **Prisma Client**: Auto-generated and type-safe query builder for Node.js & TypeScript
- **Prisma Migrate**: Migration system
- **Prisma Studio**: GUI to view and edit data in your database. **Prisma Studio** is the only part of Prisma ORM that is not open source. You can only run Prisma Studio locally.

Prisma Client can be used in *any* Node.js (supported versions) or TypeScript backend application (including serverless applications and microservices). This can be a REST API, a GraphQL API, a gRPC API, or anything else that needs a database.

## How does Prisma ORM work?

### The Prisma schema

Every project that uses a tool from the Prisma ORM toolkit starts with a Prisma schema. The Prisma schema allows developers to define their *application models* in an intuitive data modeling language. It also contains the connection to a database and defines a *generator*:

```
datasource db {
  provider = "postgresql"
}

generator client {
provider = "prisma-client"
output = "./generated"
}

model Post {
id Int @id @default(autoincrement())
title String
content String?
published Boolean @default(false)
author User? @relation(fields: [authorId], references: [id])
authorId Int?
}

model User {
id Int @id @default(autoincrement())
email String @unique
name String?
posts Post[]
}
```

> **Note**: The Prisma schema has powerful data modeling features. For example, it allows you to define "Prisma-level" relation fields which will make it easier to work with relations in the Prisma Client API. In the case above, the `posts` field on `User` is defined only on "Prisma-level", meaning it does not manifest as a foreign key in the underlying database.

In this schema, you configure three things:

- **Data source**: Specifies your database connection. Database connection URLs are configured in `prisma.config.ts`.
- **Generator**: Indicates that you want to generate Prisma Client
- **Data model**: Defines your application models

### Configuring database connections

Database connection URLs are configured in a `prisma.config.ts` file. Create a `prisma.config.ts` file in your project root:

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: "tsx ./prisma/seed.ts",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

When using Prisma CLI commands, environment variables are not automatically loaded. You'll need to use a package like `dotenv` to load environment variables from a `.env` file, or ensure your environment variables are set in your shell.

### The Prisma schema data model

On this page, the focus is on the data model. You can learn more about Data sources and Generators on the respective docs pages.

#### Functions of Prisma schema data models

The data model is a collection of models. A model has two major functions:

- Represent a table in relational databases or a collection in MongoDB
- Provide the foundation for the queries in the Prisma Client API

#### Getting a data model

There are two major workflows for "getting" a data model into your Prisma schema:

- Manually writing the data model and mapping it to the database with Prisma Migrate
- Generating the data model by introspecting a database

Once the data model is defined, you can generate Prisma Client which will expose CRUD and more queries for the defined models. If you're using TypeScript, you'll get full type-safety for all queries (even when only retrieving the subsets of a model's fields).

### Accessing your database with Prisma Client

#### Generating Prisma Client

The first step when using Prisma Client is installing the `@prisma/client` and `prisma` npm packages:

```
bun add prisma --dev
```

```
bun add @prisma/client
```

Then, you can run `prisma generate`:

```
bunx prisma generate
```

The `prisma generate` command reads your Prisma schema and *generates* Prisma Client code. The code is generated into the path specified in the `output` field of your generator block (e.g., `./generated` as shown in the schema example above).

After you change your data model, you'll need to manually re-generate Prisma Client by running `prisma generate` to ensure the generated code gets updated.

#### Using Prisma Client to send queries to your database

Once Prisma Client has been generated, you can import it in your code and send queries to your database. This is what the setup code looks like.

##### Import and instantiate Prisma Client

```
import { PrismaClient } from "./generated/client";

const prisma = new PrismaClient();
```

Now you can start sending queries via the generated Prisma Client API, here are a few sample queries. Note that all Prisma Client queries return *plain old JavaScript objects*.

Learn more about the available operations in the Prisma Client API reference.

##### Retrieve all `User` records from the database

```
// Run inside `async` function
const allUsers = await prisma.user.findMany();
```

##### Include the `posts` relation on each returned `User` object

```
// Run inside `async` function
const allUsers = await prisma.user.findMany({
  include: { posts: true },
});
```

##### Filter all `Post` records that contain `"prisma"`

```
// Run inside `async` function
const filteredPosts = await prisma.post.findMany({
  where: {
    OR: [{ title: { contains: "prisma" } }, { content: { contains: "prisma" } }],
  },
});
```

##### Create a new `User` and a new `Post` record in the same query

```
// Run inside `async` function
const user = await prisma.user.create({
  data: {
    name: "Alice",
    email: "alice@prisma.io",
    posts: {
      create: { title: "Join us for Prisma Day 2020" },
    },
  },
});
```

##### Update an existing `Post` record

```
// Run inside `async` function
const post = await prisma.post.update({
  where: { id: 42 },
  data: { published: true },
});
```

#### Usage with TypeScript

Note that when using TypeScript, the result of this query will be *statically typed* so that you can't accidentally access a property that doesn't exist (and any typos are caught at compile-time). Learn more about leveraging Prisma Client's generated types on the Advanced usage of generated types page in the docs.

## Typical Prisma ORM workflows

As mentioned above, there are two ways for "getting" your data model into the Prisma schema. Depending on which approach you choose, your main Prisma ORM workflow might look different.

### Prisma Migrate

With **Prisma Migrate**, Prisma ORM's integrated database migration tool, the workflow looks as follows:

1. Manually adjust your Prisma schema data model
2. Migrate your development database using the `prisma migrate dev` CLI command
3. Use Prisma Client in your application code to access your database

(Typical workflow with Prisma Migrate)

To learn more about the Prisma Migrate workflow, see:

- Deploying database changes with Prisma Migrate

- Developing with Prisma Migrate

### SQL migrations and introspection

If for some reason, you can not or do not want to use Prisma Migrate, you can still use introspection to update your Prisma schema from your database schema. The typical workflow when using **SQL migrations and introspection** is slightly different:

1. Manually adjust your database schema using SQL or a third-party migration tool
2. (Re-)introspect your database
3. Optionally (re-)configure your Prisma Client API
4. (Re-)generate Prisma Client
5. Use Prisma Client in your application code to access your database

(Introspect workflow)

To learn more about the introspection workflow, please refer the introspection section.

Edit on GitHub

Prisma ORM

Learn about Prisma ORM

Why Prisma ORM?

Learn about the motivation for Prisma ORM and how it compares to other Node.js and TypeScript database tools like ORMs and SQL query builders.
