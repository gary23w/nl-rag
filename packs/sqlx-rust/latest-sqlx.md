---
title: "sqlx"
source: https://docs.rs/sqlx/latest/sqlx/
domain: sqlx-rust
license: CC-BY-SA-4.0
tags: sqlx rust, rust async database, compile-time sql rust, sqlx query macro
fetched: 2026-07-02
---

# Crate sqlx

Source

Expand description

The async SQL toolkit for Rust, built with ❤️ by the LaunchBadge team.

See our README to get started or browse our example projects. Have a question? Check our FAQ or open a discussion.

#### §Runtime Support

SQLx supports both the Tokio and async-std runtimes.

You choose which runtime SQLx uses by default by enabling one of the following features:

- `runtime-async-std`
- `runtime-tokio`

If more than one runtime feature is enabled, the Tokio runtime is used if a Tokio context exists on the current thread, i.e. `tokio::runtime::Handle::try_current()` returns `Ok`; `async-std` is used otherwise.

Note that while SQLx no longer produces a compile error if zero or multiple runtime features are enabled, which is useful for libraries building on top of it, **the use of nearly any async function in the API will panic without at least one runtime feature enabled**.

The chief exception is the SQLite driver, which is runtime-agnostic, including its integration with the query macros. However, `SqlitePool` *does* require runtime support for timeouts and spawning internal management tasks.

#### §TLS Support

For securely communicating with SQL servers over an untrusted network connection such as the internet, you can enable Transport Layer Security (TLS) by enabling one of the following features:

- `tls-native-tls`: Enables the `native-tls` backend which uses the OS-native TLS capabilities:
  - SecureTransport on macOS.
  - SChannel on Windows.
  - OpenSSL on all other platforms.
- `tls-rustls`: Enables the rustls backend, a cross-platform TLS library.
  - Only supports TLS revisions 1.2 and 1.3.
  - If you get `HandshakeFailure` errors when using this feature, it likely means your database server does not support these newer revisions. This might be resolved by enabling or switching to the `tls-native-tls` feature.
  - rustls supports several providers of cryptographic primitives. The default (enabled when you use the `tls-rustls` feature or `tls-rustls-ring`) is the `ring` provider, which has fewer build-time dependencies but also has fewer features. Alternatively, you can use `tls-rustls-aws-lc-rs` to use the `aws-lc-rs` provider, which enables additional cipher suite support at the cost of more onerous build requirements (depending on platform support).

If more than one TLS feature is enabled, the `tls-native-tls` feature takes precedent so that it is only necessary to enable it to see if it resolves the `HandshakeFailure` error without disabling `tls-rustls`.

Consult the user manual for your database to find the TLS versions it supports.

If your connection configuration requires a TLS upgrade but TLS support was not enabled, the connection attempt will return an error.

## Modules

**_config`_unstable-docs`**

(Exported for documentation only) Guide and reference for

sqlx.toml

files.

**any`any`**

SEE DOCUMENTATION BEFORE USE

. Runtime-generic database driver.

**database**

Traits to represent a database driver.

**decode**

Provides

Decode

for decoding values from the database.

**encode**

Provides

Encode

for encoding values for the database.

**error**

Types for working with errors produced by SQLx.

**migrate`migrate`**

**mysql`mysql`**

MySQL

database driver.

**pool**

Provides the connection pool for asynchronous SQLx connections.

**postgres`postgres`**

PostgreSQL

database driver.

**prelude**

Convenience re-export of common traits.

**query**

Types and traits for the

query

family of functions and macros.

**query_builder**

Runtime query-builder API.

**sqlite`_sqlite`**

SQLite

database driver.

**types**

Conversions between Rust and SQL types.

## Macros

**migrate`macros` and `migrate`**

Embeds migrations into the binary by expanding to a static instance of

Migrator

.

**query`macros`**

Statically checked SQL query with

println!()

style syntax.

**query_as`macros`**

A variant of

query!

which takes a path to an explicitly defined struct as the output type.

**query_as_unchecked`macros`**

A variant of

query_as!

which does not check the input or output types. This still does parse the query to ensure it’s syntactically and semantically valid for the current database.

**query_file`macros`**

A variant of

query!

where the SQL query is stored in a separate file.

**query_file_as`macros`**

Combines the syntaxes of

query_as!

and

query_file!

.

**query_file_as_unchecked`macros`**

A variant of

query_file_as!

which does not check the input or output types. This still does parse the query to ensure it’s syntactically and semantically valid for the current database.

**query_file_scalar`macros`**

A variant of

query_scalar!

which takes a file path like

query_file!

.

**query_file_scalar_unchecked`macros`**

A variant of

query_file_scalar!

which does not typecheck bind parameters and leaves the output type to inference. The query itself is still checked that it is syntactically and semantically valid for the database, that it only produces one column and that the number of bind parameters is correct.

**query_file_unchecked`macros`**

A variant of

query_file!

which does not check the input or output types. This still does parse the query to ensure it’s syntactically and semantically valid for the current database.

**query_scalar`macros`**

A variant of

query!

which expects a single column from the query and evaluates to an instance of

QueryScalar

.

**query_scalar_unchecked`macros`**

A variant of

query_scalar!

which does not typecheck bind parameters and leaves the output type to inference. The query itself is still checked that it is syntactically and semantically valid for the database, that it only produces one column and that the number of bind parameters is correct.

**query_unchecked`macros`**

A variant of

query!

which does not check the input or output types. This still does parse the query to ensure it’s syntactically and semantically valid for the current database.

## Structs

**Any`any`**

Opaque database driver. Capable of being used in place of any SQLx database driver. The actual driver used will be selected at runtime, from the connection url.

**AnyConnection**

SEE DOCUMENTATION BEFORE USE

. Runtime-generic database connection.

**AssertSqlSafe**

Assert that a query string is safe to execute on a database connection.

**MySql`mysql`**

MySQL database driver.

**MySqlConnection`mysql`**

A connection to a MySQL database.

**PgConnection`postgres`**

A connection to a PostgreSQL database.

**Pool**

An asynchronous pool of SQLx database connections.

**Postgres`postgres`**

PostgreSQL database driver.

**QueryBuilder**

A builder type for constructing queries at runtime.

**RawSql**

One or more raw SQL statements, separated by semicolons (

;

).

**SqlStr**

A SQL string that is ready to execute on a database connection.

**Sqlite`_sqlite`**

Sqlite database driver.

**SqliteConnection`_sqlite`**

A connection to an open

Sqlite

database.

**Transaction**

An in-progress database transaction or savepoint.

## Enums

**ColumnOrigin**

The possible statuses for our knowledge of the origin of a

Column

.

**Either**

The enum

Either

with variants

Left

and

Right

is a general purpose sum type with two cases.

**Error**

Represents all the ways a method can fail within SQLx.

## Traits

**Acquire**

Acquire connections or transactions from a database in a generic way.

**AnyExecutor`any`**

An alias for

Executor<'_, Database = Any>

.

**Arguments**

A tuple of arguments to be sent to the database.

**Column**

**ColumnIndex**

A type that can be used to index into a

Row

or

Statement

.

**ConnectOptions**

**Connection**

Represents a single database connection.

**Database**

A database driver.

**Decode**

A type that can be decoded from the database.

**Encode**

Encode a single value to be sent to the database.

**Execute**

A type that may be executed against a database connection.

**Executor**

A type that contains or can provide a database connection to use for executing queries against the database.

**FromRow**

A record that can be built from a row returned by the database.

**IntoArguments**

**MySqlExecutor`mysql`**

An alias for

Executor<'_, Database = MySql>

.

**PgExecutor`postgres`**

An alias for

Executor<'_, Database = Postgres>

.

**Row**

Represents a single row from the database.

**SqlSafeStr**

A SQL string that is safe to execute on a database connection.

**SqliteExecutor`_sqlite`**

An alias for

Executor<'_, Database = Sqlite>

.

**Statement**

An explicitly prepared statement.

**Type**

Indicates that a SQL type is supported for a database.

**TypeInfo**

Provides information about a SQL type for the database driver.

**Value**

An owned value from the database.

**ValueRef**

A reference to a single value from the database.

## Functions

**query**

Execute a single SQL query as a prepared statement (transparently cached).

**query_as**

Execute a single SQL query as a prepared statement (transparently cached). Maps rows to Rust types using

FromRow

.

**query_as_with**

Execute a single SQL query, with the given arguments as a prepared statement (transparently cached). Maps rows to Rust types using

FromRow

.

**query_scalar**

Execute a single SQL query as a prepared statement (transparently cached) and extract the first column of each row.

**query_scalar_with**

Execute a SQL query as a prepared statement (transparently cached), with the given arguments, and extract the first column of each row.

**query_with**

Execute a SQL query as a prepared statement (transparently cached), with the given arguments.

**raw_sql**

Execute one or more statements as raw SQL, separated by semicolons (

;

).

## Type Aliases

**AnyPool**

SEE DOCUMENTATION BEFORE USE

. Type alias for

Pool<Any>

.

**MySqlPool`mysql`**

An alias for

Pool

, specialized for MySQL.

**MySqlTransaction`mysql`**

An alias for

Transaction

, specialized for MySQL.

**PgPool`postgres`**

An alias for

Pool

, specialized for Postgres.

**PgTransaction`postgres`**

An alias for

Transaction

, specialized for Postgres.

**Result**

A specialized

Result

type for SQLx.

**SqlitePool`_sqlite`**

An alias for

Pool

, specialized for SQLite.

**SqliteTransaction`_sqlite`**

An alias for

Transaction

, specialized for SQLite.

## Attribute Macros

**test`macros`**

Mark an

async fn

as a test with SQLx support.

## Derive Macros

**Decode**

**Encode**
