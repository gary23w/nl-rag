---
title: "surrealdb/README.md at main · surrealdb/surrealdb · GitHub"
source: https://github.com/surrealdb/surrealdb/blob/main/README.md
domain: surrealdb
license: CC-BY-SA-4.0
tags: surrealdb, multi-model database, surrealql query language, document-graph database
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

surrealdb

/

surrealdb

Public

- Notifications You must be signed in to change notification settings
- Fork 1.3k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

469 lines (354 loc) · 27.7 KB

Outline

(Discord)   (X)   (Dev)   (LinkedIn)   (YouTube)

(Blog)   (Github)   (LinkedIn)   (X)   (YouTube)   (Dev)   (Discord)   (Stack Overflow)

## What is SurrealDB?

SurrealDB is a multi-model database built in Rust designed to unify multiple data models into a single engine. SurrealDB combines document, graph, relational, time-series, geospatial and key-value data types with powerful search and retrieval functionalities (full-text, vector, hybrid) and real-time and event-driven capabilities, enabling developers to build powerful applications faster and more efficiently. SurrealDB can also be used as a backend-as-a-service given its support for end user authentication. Given that it’s a single Rust binary, SurrealDB can run embedded (in‐app), in the browser (via WebAssembly), in the edge, self-hosted as single backend node, or in a distributed cluster in the cloud.

SurrealDB is used for data-intensive systems such as applications requiring multiple data types, data layer for AI agents, knowledge graphs, real-time apps (e.g. recommendation engines, fraud detection systems) and embedded/edge systems. With SurrealDB, you can simplify your database and API infrastructure, reduce development time, and build secure, performant apps quickly and cost-effectively.

**Key features of SurrealDB include:**

- **Reduces development time**: SurrealDB simplifies your database and API stack by removing the need for most server-side components, allowing you to build secure, performant apps faster and cheaper.
- **Multi-model**: native multi-model support for document, graph, relational (enforcing schema and schemaless), time-series, geospatial and retrieval (full-text, vector, hybrid). This is offered natively through SurrealQL, SurrealDB's SQL-like intuitive query language.
- **Real-time collaborative API backend service:** SurrealDB functions as both a database and an API backend service, enabling real-time collaboration.
- **Support for multiple querying languages:** SurrealDB supports SQL querying from client devices, GraphQL, ACID transactions, WebSocket connections, structured and unstructured data, graph querying, full-text and vector indexing, and geospatial querying.
- **Granular access control**: SurrealDB provides row-level permissions-based access control, giving you the ability to manage data access with precision.

View the features, the latest releases, and documentation.

(Surrealist)

## Contents

- Database, API, and permissions
- Tables, documents, and graph
- Advanced inter-document relations and analysis. No JOINs. No pain.
- Simple schema definition for frontend and backend development
- Connect and query directly from web-browsers and client devices
- Query the database with the tools you want
- Realtime live queries and data changes direct to application
- Scale effortlessly to hundreds of nodes for high-availability and scalability
- Extend your database with JavaScript functions
- Designed to be embedded or to run distributed in the cloud

## Features

- Database server, or embedded library
- Multi-row, multi-table ACID transactions
- Single-node, or highly-scalable distributed mode
- Record links and directed typed graph connections
- Store structured and unstructured data
- Incrementally computed views for pre-computed advanced analytics
- Realtime-API layer, and security permissions built in
- Store and model data in any way with tables, documents, and graph
- Simple schema definition for frontend and backend development
- Connect and query directly from web-browsers and client devices
- Use embedded JavaScript functions for custom advanced functionality
- MCP (Model Context Protocol) server for LLM and AI-agent integration

## Documentation

For guidance on installation, development, deployment, and administration, take a look at the following resources:

- Documentation: https://surrealdb.com/docs
- SurrealDB University: https://surrealdb.com/learn
- Aeon's Surreal Renaissance (interactive book): https://surrealdb.com/learn/book

## Getting started

Getting started with SurrealDB is as easy as starting up the SurrealDB database server, choosing your platform, and integrating its SDK into your code. You can easily get started with your platform of choice by reading one of our tutorials.

**Server side code**

**Client side apps**

## SurrealDB Cloud

SurrealDB is available as a managed cloud service. Forget about infrastructure operations, monitoring, backups or capacity planning. SurrealDB Cloud allows you to focus on building great products using the power and flexibility of SurrealDB in just a few clicks. Grow from prototype to enterprise-scale. The SurrealDB Cloud scalable architecture allows your database to evolve as your application grows, ensuring you are always ahead of demand. However if you want to deploy SurrealDB yourself, keep reading below.

## Installation

SurrealDB is designed to be simple to install and simple to run - using just one command from your terminal. In addition to traditional installation, SurrealDB can be installed and run with HomeBrew, Docker, or using any other container orchestration tool such as Docker Compose, Docker Swarm, Rancher, or in Kubernetes.

#### Install on macOS

The quickest way to get going with SurrealDB on macOS is to use Homebrew. This will install both the command-line tools, and the SurrealDB server as a single executable. If you don't use Homebrew, follow the instructions for Linux below to install SurrealDB.

```highlight
brew install surrealdb/tap/surreal
```

If you want to test a version with the latest features, published every night, install the `nightly` version:

```highlight
brew install surrealdb/tap/surreal-nightly
```

#### Install on Linux

The easiest and preferred way to get going with SurrealDB on Unix operating systems is to install and use the SurrealDB command-line tool. Run the following command in your terminal and follow the on-screen instructions.

```highlight
curl --proto '=https' --tlsv1.2 -sSf https://install.surrealdb.com | sh
```

If you want to run a beta release, before the next version is released, the `beta` version:

```highlight
curl --proto '=https' --tlsv1.2 -sSf https://install.surrealdb.com | sh -s -- --beta
```

If you want to test a version with the latest features, published every night, install the `nightly` version:

```highlight
curl --proto '=https' --tlsv1.2 -sSf https://install.surrealdb.com | sh -s -- --nightly
```

#### Install on Windows

The easiest and preferred way to get going with SurrealDB on Windows is to install and use the SurrealDB command-line tool. Run the following command in your terminal and follow the on-screen instructions.

```highlight
iwr https://windows.surrealdb.com -useb | iex
```

If you want to test a version with the latest features, published every night, install the `nightly` version:

```highlight
iex "& { $(irm https://windows.surrealdb.com) } -Nightly"
```

#### Run using Docker

Docker can be used to manage and run SurrealDB database instances without the need to install any command-line tools. The SurrealDB docker container contains the full command-line tools for importing and exporting data from a running server, or for running a server itself.

```highlight
docker run --rm --pull always --name surrealdb -p 8000:8000 surrealdb/surrealdb:latest start
```

For just getting started with a development server running in memory, you can pass the container a basic initialization to set the user and password as root and enable logging.

```highlight
docker run --rm --pull always --name surrealdb -p 8000:8000 surrealdb/surrealdb:latest start --log info --user root --pass root memory
```

## Quick look

With strongly-typed data types, data can be fully modelled right in the database.

```highlight
UPDATE person SET
    waist = <int> "34",
    height = <float> 201,
    score = <decimal> 0.3 + 0.3 + 0.3 + 0.1
;
```

Store dynamically computed fields which are calculated when retrieved.

```highlight
DEFINE FIELD can_drive ON TABLE person COMPUTED time::now() > birthday + 18y;
CREATE person SET birthday = d"2007-06-22";
;
```

Easily work with unstructured or structured data, in schema-less or schema-full mode.

```highlight
-- Create a schemafull table
DEFINE TABLE user SCHEMAFULL;

-- Specify fields on the user table
DEFINE FIELD name ON TABLE user TYPE object;
DEFINE FIELD name.first ON TABLE user TYPE string;
DEFINE FIELD name.last ON TABLE user TYPE string;
DEFINE FIELD email ON TABLE user TYPE string ASSERT string::is_email($value);

-- Add a unique index on the email field preventing duplicate values
DEFINE INDEX email ON TABLE user COLUMNS email UNIQUE;

-- Create a new event whenever a user changes their email address
DEFINE EVENT email ON TABLE user WHEN $before.email != $after.email THEN (
    CREATE event SET user = $value, time = time::now(), value = $after.email, action = 'email_changed'
);
```

Connect records together with fully directed graph edge connections.

```highlight
-- Add a graph edge between user:tobie and article:surreal
RELATE user:tobie->write->article:surreal
    SET time.written = time::now()
;

-- Add a graph edge between specific users and developers
LET $from = (SELECT users FROM company:surrealdb);
LET $devs = (SELECT * FROM user WHERE tags CONTAINS 'developer');
RELATE $from->like->$devs UNIQUE
    SET time.connected = time::now()
;
```

Query data flexibly with advanced expressions and graph queries.

```highlight
-- Select a nested array, and filter based on an attribute
SELECT emails[WHERE active = true] FROM person;

-- Select all 1st, 2nd, and 3rd level people who this specific person record knows, or likes, as separate outputs
SELECT ->knows->(? AS f1)->knows->(? AS f2)->(knows, likes AS e3 WHERE influencer = true)->(? AS f3) FROM person:tobie;

-- Select all person records (and their recipients), who have sent more than 5 emails
SELECT *, ->sent->email->to->person FROM person WHERE count(->sent->email) > 5;

-- Select other products purchased by people who purchased this laptop
SELECT <-purchased<-person->purchased->product FROM product:laptop;

-- Select products purchased by people in the last 3 weeks who have purchased the same products that we purchased
SELECT ->purchased->product<-purchased<-person->(purchased WHERE created_at > time::now() - 3w)->product FROM person:tobie;
```

Store GeoJSON geographical data types, including points, lines and polygons.

```highlight
UPDATE city:london SET
    centre = (-0.118092, 51.509865),
    boundary = {
        type: "Polygon",
        coordinates: [[
            [-0.38314819, 51.37692386], [0.1785278, 51.37692386],
            [0.1785278, 51.61460570], [-0.38314819, 51.61460570],
            [-0.38314819, 51.37692386]
        ]]
    }
;
```

Write custom embedded logic using JavaScript functions.

```highlight
CREATE film SET
    ratings = [
        { rating: 6, user: user:bt8e39uh1ouhfm8ko8s0 },
        { rating: 8, user: user:bsilfhu88j04rgs0ga70 },
    ],
    featured = function() {
        return this.ratings.filter(r => {
            return r.rating >= 7;
        }).map(r => {
            return { ...r, rating: r.rating * 10 };
        });
    }
;
```

Specify granular access permissions for client and application access.

```highlight
-- Specify access permissions for the 'post' table
DEFINE TABLE post SCHEMALESS
    PERMISSIONS
        FOR select
            -- Published posts can be selected
            WHERE published = true
            -- A user can select all their own posts
            OR user = $auth.id
        FOR create, update
            -- A user can create or update their own posts
            WHERE user = $auth.id
        FOR delete
            -- A user can delete their own posts
            WHERE user = $auth.id
            -- Or an admin can delete any posts
            OR $auth.admin = true
;
```

## Why SurrealDB?

### Database, API, and permissions

SurrealDB combines the database layer, the querying layer, and the API and authentication layer into one platform. Advanced table-based and row-based customisable access permissions allow for granular data access patterns for different types of users. There's no need for custom backend code and security rules with complicated database development.

### Tables, documents, and graph

As a multi-model database, SurrealDB enables developers to use multiple techniques to store and model data, without having to choose a method in advance. With the use of tables, SurrealDB has similarities with relational databases, but with the added functionality and flexibility of advanced nested fields and arrays. Inter-document record links allow for simple to understand and highly-performant related queries without the use of JOINs, eliminating the N+1 query problem.

### Advanced inter-document relations and analysis. No JOINs. No pain.

With full graph database functionality SurrealDB enables more advanced querying and analysis. Records (or vertices) can be connected to one another with edges, each with its own record properties and metadata. Simple extensions to traditional SQL queries allow for multi-table, multi-depth document retrieval, efficiently in the database, without the use of complicated JOINs and without bringing the data down to the client.

### Simple schema definition for frontend and backend development

With SurrealDB, specify your database and API schema in one place, and define column rules and constraints just once. Once a schema is defined, database access is automatically granted to the relevant users. No more custom API code, and no more GraphQL integration. Simple, flexible, and ready for production in minutes not months.

### Connect and query directly from web-browsers and client devices

Connect directly to SurrealDB from any end-user client device. Run SurrealQL queries directly within web-browsers, ensuring that users can only view or modify the data that they are allowed to access. Highly-performant WebSocket connections allow for efficient bi-directional queries, responses and notifications.

### Query the database with the tools you want

Your data, your choice. SurrealDB is designed to be flexible to use, with support for SurrealQL, GraphQL (coming soon), CRUD support over REST, and JSON-RPC querying and modification over WebSockets. With direct-to-client connection with in-built permissions, SurrealDB speeds up the development process, and fits in seamlessly into any tech stack.

### Realtime live queries and data changes direct to application

SurrealDB keeps every client device in-sync with data modifications pushed in realtime to the clients, applications, end-user devices, and server-side libraries. Live SQL queries allow for advanced filtering of the changes to which a client subscribes, and efficient data formats, including DIFFing and PATCHing enable highly-performant web-based data syncing.

### Scale effortlessly to hundreds of nodes for high-availability and scalability

SurrealDB can be run as a single in-memory node, or as part of a distributed cluster - offering highly-available and highly-scalable system characteristics. Designed from the ground up to run in a distributed environment, SurrealDB makes use of special techniques when handling multi-table transactions, and document record IDs - with no use of table or row locks.

### Extend your database with JavaScript functions

Embedded JavaScript functions allow for advanced, custom functionality, with computation logic being moved to the data layer. This improves upon the traditional approach of moving data to the client devices before applying any computation logic, ensuring that only the necessary data is transferred remotely. These advanced JavaScript functions, with support for the ES2020 standard, allow any developer to analyse the data in ever more simple-yet-advanced ways.

### Designed to be embedded or to run distributed in the cloud

Built entirely in Rust as a single library, SurrealDB is designed to be used as both an embedded database library with advanced querying functionality, and as a database server which can operate in a distributed cluster. With low memory usage and cpu requirements, the system requirements have been specifically thought through for running in all types of environment.

## Community

Join our growing community around the world, for help, ideas, and discussions regarding SurrealDB.

- View our official Blog
- Chat live with us on Discord
- Follow us on X
- Connect with us on LinkedIn
- Join the discussion on Reddit
- Visit us on YouTube
- Join our Dev community
- Questions tagged #surrealdb on Stack Overflow

## Contributing

We would    for you to get involved with SurrealDB development! If you wish to help, you can learn more about how you can contribute to this project in the contribution guide.

**For maintainers**: See the release process documentation for information about performing releases.

## Security

For security issues, view our vulnerability policy, view our Trust and Security page, and kindly email us at security@surrealdb.com instead of posting a public issue on GitHub.

## License

Source code for SurrealDB is variously licensed under a number of different licenses. A copy of each license can be found in each repository.

- Libraries and SDKs, each located in its own distinct repository, are released under either the Apache License 2.0 or MIT License.
- Certain core database components, each located in its own distinct repository, are released under the Apache License 2.0.
- Core database code for SurrealDB, located in this repository, is released under the Business Source License 1.1.

For more information, see the licensing information.
