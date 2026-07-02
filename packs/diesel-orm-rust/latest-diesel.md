---
title: "diesel"
source: https://docs.rs/diesel/latest/diesel/
domain: diesel-orm-rust
license: CC-BY-SA-4.0
tags: diesel orm, rust orm library, diesel query builder, rust database schema
fetched: 2026-07-02
---

# Crate diesel

Source

Expand description

## §Diesel

Diesel is an ORM and query builder designed to reduce the boilerplate for database interactions. If this is your first time reading this documentation, we recommend you start with the getting started guide. We also have many other long form guides.

## §Where to find things

### §Declaring your schema

For Diesel to validate your queries at compile time it requires you to specify your schema in your code, which you can do with the `table!` macro. `diesel print-schema` can be used to automatically generate these macro calls (by connecting to your database and querying its schema).

### §Getting started

Queries usually start from either a table, or a function like `update`. Those functions can be found here.

Diesel provides a `prelude` module, which exports most of the typically used traits and types. We are conservative about what goes in this module, and avoid anything which has a generic name. Files which use Diesel are expected to have `use diesel::prelude::*;`.

### §Constructing a query

The tools the query builder gives you can be put into these three categories:

- “Query builder methods” are things that map to portions of a whole query (such as `ORDER` and `WHERE`). These methods usually have the same name as the SQL they map to, except for `WHERE` which is called `filter` in Diesel (To not conflict with the Rust keyword). These methods live in the `query_dsl` module.
- “Expression methods” are things you would call on columns or other individual values. These methods live in the `expression_methods` module You can often find these by thinking “what would this be called” if it were a method and typing that into the search bar (e.g. `LIKE` is called `like` in Diesel). Most operators are named based on the Rust function which maps to that operator in `std::ops` (For example `==` is called `.eq`, and `!=` is called `.ne`).
- “Bare functions” are normal SQL functions such as `sum`. They live in the `dsl` module. Diesel only supports a very small number of these functions. You can declare additional functions you want to use with the `define_sql_function!` macro.

### §Serializing and Deserializing

Types which represent the result of a SQL query implement a trait called `Queryable`.

Diesel maps “Rust types” (e.g. `i32`) to and from “SQL types” (e.g. `diesel::sql_types::Integer`). You can find all the types supported by Diesel in the `sql_types` module. These types are only used to represent a SQL type. You should never put them on your `Queryable` structs.

To find all the Rust types which can be used with a given SQL type, see the documentation for that SQL type.

To find all the SQL types which can be used with a Rust type, go to the docs for either `ToSql` or `FromSql`, go to the “Implementors” section, and find the Rust type you want to use.

### §How to read diesels compile time error messages

Diesel is known for generating large complicated looking errors. Usually most of these error messages can be broken down easily. The following section tries to give an overview of common error messages and how to read them. As a general note it’s always useful to read the complete error message as emitted by rustc, including the `required because of …` part of the message. Your IDE might hide important parts!

The following error messages are common:

- `the trait bound (diesel::sql_types::Integer, …, diesel::sql_types::Text): load_dsl::private::CompatibleType<YourModel, Pg> is not satisfied` while trying to execute a query: This error indicates a mismatch between what your query returns and what your model struct expects the query to return. The fields need to match in terms of field order, field type and field count. If you are sure that everything matches, double check the enabled diesel features (for support for types from other crates) and double check (via `cargo tree`) that there is only one version of such a shared crate in your dependency tree. Consider using `#[derive(Selectable)]` + `#[diesel(check_for_backend(diesel::pg::Pg))]` to improve the generated error message.
- `the trait bound i32: diesel::Expression is not satisfied` in the context of `Insertable` model structs: This error indicates a type mismatch between the field you are trying to insert into the database and the actual database type. These error messages contain a line like `= note: required for i32 to implement AsExpression<diesel::sql_types::Text>` that show both the provided rust side type (`i32` in that case) and the expected database side type (`Text` in that case).
- `the trait bound i32: AppearsOnTable<users::table> is not satisfied` in the context of `AsChangeset` model structs: This error indicates a type mismatch between the field you are trying to update and the actual database type. Double check your type mapping.
- `the trait bound SomeLargeType: QueryFragment<Sqlite, SomeMarkerType> is not satisfied` while trying to execute a query. This error message indicates that a given query is not supported by your backend. This usually means that you are trying to use SQL features from one SQL dialect on a different database system. Double check your query that everything required is supported by the selected backend. If that’s the case double check that the relevant feature flags are enabled (for example, `returning_clauses_for_sqlite_3_35` for enabling support for returning clauses in newer sqlite versions)
- `the trait bound posts::title: SelectableExpression<users::table> is not satisfied` while executing a query: This error message indicates that you’re trying to select a field from a table that does not appear in your from clause. If your query joins the relevant table via `left_join` you need to call `.nullable()` on the relevant column in your select clause.

### §Getting help

If you run into problems, Diesel has an active community. Open a new discussion thread at diesel github repository and we will try to help you

## §Crate feature flags

The following feature flags are considered to be part of diesels public API. Any feature flag that is not listed here is **not** considered to be part of the public API and can disappear at any point in time:

- `sqlite`: This feature enables the diesel sqlite backend. Enabling this feature requires per default a compatible copy of `libsqlite3` for your target architecture. Alternatively, you can add `libsqlite3-sys` with the `bundled` feature as a dependency to your crate so SQLite will be bundled:`[dependencies] libsqlite3-sys = { version = "0.29", features = ["bundled"] }`
- `postgres`: This feature enables the diesel postgres backend. This features implies `postgres_backend` Enabling this feature requires a compatible copy of `libpq` for your target architecture. Alternatively, you can add `pq-sys` with the `bundled` feature as a dependency to your crate so libpq will be bundled:`[dependencies] pq-sys = { version = "0.6", features = ["bundled"] } openssl-sys = { version = "0.9.100", features = ["vendored"] }`
- `mysql`: This feature enables the diesel mysql backend. This feature implies `mysql_backend`. Enabling this feature requires a compatible copy of `libmysqlclient` for your target architecture. Alternatively, you can add `mysqlclient-sys` with the `bundled` feature as a dependency to your crate so libmysqlclient will be bundled:`[dependencies] mysqlclient-sys = { version = "0.5", features = ["bundled"] } openssl-sys = { version = "0.9.100", features = ["vendored"] }`
- `postgres_backend`: This feature enables those parts of diesels postgres backend, that are not dependent on `libpq`. Diesel does not provide any connection implementation with only this feature enabled. This feature can be used to implement a custom implementation of diesels `Connection` trait for the postgres backend outside of diesel itself, while reusing the existing query dsl extensions for the postgres backend
- `mysql_backend`: This feature enables those parts of diesels mysql backend, that are not dependent on `libmysqlclient`. Diesel does not provide any connection implementation with only this feature enabled. This feature can be used to implement a custom implementation of diesels `Connection` trait for the mysql backend outside of diesel itself, while reusing the existing query dsl extensions for the mysql backend
- `returning_clauses_for_sqlite_3_35`: This feature enables support for `RETURNING` clauses in the sqlite backend. Enabling this feature requires sqlite 3.35.0 or newer.
- `32-column-tables`: This feature enables support for tables with up to 32 columns. This feature is enabled by default. Consider disabling this feature if you write a library crate providing general extensions for diesel or if you do not need to support tables with more than 16 columns and you want to minimize your compile times.
- `64-column-tables`: This feature enables support for tables with up to 64 columns. It implies the `32-column-tables` feature. Enabling this feature will increase your compile times.
- `128-column-tables`: This feature enables support for tables with up to 128 columns. It implies the `64-column-tables` feature. Enabling this feature will increase your compile times significantly.
- `i-implement-a-third-party-backend-and-opt-into-breaking-changes`: This feature opens up some otherwise private API, that can be useful to implement a third party `Backend` or write a custom `Connection` implementation. **Do not use this feature for any other usecase**. By enabling this feature you explicitly opt out diesel stability guarantees. We explicitly reserve us the right to break API’s exported under this feature flag in any upcoming minor version release. If you publish a crate depending on this feature flag consider to restrict the supported diesel version to the currently released minor version.
- `serde_json`: This feature flag enables support for (de)serializing json values from the database using types provided by `serde_json`.
- `chrono`: This feature flags enables support for (de)serializing date/time values from the database using types provided by `chrono`
- `uuid`: This feature flag enables support for (de)serializing uuid values from the database using types provided by `uuid`
- `network-address`: This feature flag enables support for (de)serializing IP values from the database using types provided by `ipnetwork`.
- `ipnet-address`: This feature flag enables support for (de)serializing IP values from the database using types provided by `ipnet`.
- `numeric`: This feature flag enables support for (de)serializing numeric values from the database using types provided by `bigdecimal`
- `r2d2`: This feature flag enables support for the `r2d2` connection pool implementation.
- `extras`: This feature enables the feature flagged support for any third party crate. This implies the following feature flags: `serde_json`, `chrono`, `uuid`, `network-address`, `numeric`, `r2d2`
- `with-deprecated`: This feature enables items marked as `#[deprecated]`. It is enabled by default. disabling this feature explicitly opts out diesels stability guarantee.
- `without-deprecated`: This feature disables any item marked as `#[deprecated]`. Enabling this feature explicitly opts out the stability guarantee given by diesel. This feature overrides the `with-deprecated`. Note that this may also remove items that are not shown as `#[deprecated]` in our documentation, due to various bugs in rustdoc. It can be used to check if you depend on any such hidden `#[deprecated]` item.

By default the following features are enabled:

- `with-deprecated`
- `32-column-tables`

## Re-exports

**`pub use crate::result::Error::NotFound;`**

**`pub use crate::prelude::*;`**

## Modules

**associations**

Traits related to relationships between multiple tables.

**backend**

Types which represent various database backends

**connection**

Types related to database connections

**data_types**

Structs to represent the primitive equivalent of SQL types where there is no existing Rust primitive, or where using it would be confusing (such as date and time types). This module will re-export all backend specific data structures when compiled against that backend.

**deserialize**

Types and traits related to deserializing values from the database

**dsl**

Includes various helper types and bare functions which are named too generically to be included in prelude, but are often used when using Diesel.

**expression**

AST types representing various typed SQL expressions.

**expression_methods**

Adds various methods to construct new expressions. These traits are exported by default, and implemented automatically.

**helper_types**

Provide helper types for concisely writing the return type of functions. As with iterators, it is unfortunately difficult to return a partially constructed query without exposing the exact implementation of the function. Without higher kinded types, these various DSLs can’t be combined into a single trait for boxing purposes.

**migration**

Representation of migrations

**mysql`mysql_backend`**

Provides types and functions related to working with MySQL

**pg`postgres_backend`**

Provides types and functions related to working with PostgreSQL

**prelude**

Re-exports important traits and types. Meant to be glob imported when using Diesel.

**query_builder**

Contains traits responsible for the actual construction of SQL statements

**query_dsl**

Traits that construct SELECT statements

**query_source**

Types related to describing schema, and interactions between tables.

**r2d2`r2d2`**

Connection pooling via r2d2.

**result**

Errors, type aliases, and functions related to working with

Result

.

**row**

Contains the

Row

trait

**serialize**

Types and traits related to serializing values for the database

**sql_types**

Types which represent a SQL data type.

**sqlite`sqlite`**

Provides types and functions related to working with SQLite

**upsert**

Types and functions related to PG’s and Sqlite’s

ON CONFLICT

clause

## Macros

**alias**

Declare a new alias for a table

**allow_columns_to_appear_in_same_group_by_clause**

Allow two or more columns which are otherwise unrelated to be used together in a group by clause.

**allow_tables_to_appear_in_same_query**

Allow two or more tables which are otherwise unrelated to be used together in a query.

**infix_operator**

Useful for libraries adding support for new SQL types. Apps should never need to call this.

**joinable**

Allow two tables to be referenced in a join query without providing an explicit

ON

clause.

**numeric_expr**

Indicates that an expression allows all numeric operators. If you create new SQL functions that return a numeric type, you should invoke this macro that type. Unfortunately, Rust disallows us from automatically implementing

Add

for types which implement

Expression

, under its orphan rules.

**operator_allowed**

Implements the Rust operator for a given type. If you create a new SQL function, which returns a type that you’d like to use an operator on, you should invoke this macro. Unfortunately, Rust disallows us from automatically implementing

Add

and other traits from

std::ops

, under its orphan rules.

**postfix_operator**

Useful for libraries adding support for new SQL types. Apps should never need to call this.

**prefix_operator**

Useful for libraries adding support for new SQL types. Apps should never need to call this.

**table**

Specifies that a table exists, and what columns it has. This will create a new public module, with the same name, as the name of the table. In this module, you will find a unit struct named

table

, and a unit struct with the name of each column.

## Functions

**copy_from`postgres_backend` and `postgres`**

Creates a

COPY FROM

statement

**copy_to`postgres_backend` and `postgres`**

Creates a

COPY TO

statement

**debug_query**

Takes a query

QueryFragment

expression as an argument and returns a type that implements

fmt::Display

and

fmt::Debug

to show the query.

**delete**

Creates a

DELETE

statement.

**insert_into**

Creates an

INSERT

statement for the target table.

**insert_or_ignore_into**

Creates an

INSERT [OR] IGNORE

statement.

**replace_into**

Creates a

REPLACE

statement.

**select**

Creates a bare select statement, with no from clause. Primarily used for testing diesel itself, but likely useful for third party crates as well. The given expressions must be selectable from anywhere.

**sql_query**

Construct a full SQL query using raw SQL.

**update**

Creates an

UPDATE

statement.

## Derive Macros

**MultiConnection**

This derives implements

diesel::Connection

and related traits for an enum of connections to different databases.
