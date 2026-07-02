---
title: "sqlite3 (part 2/3)"
source: https://docs.python.org/3/library/sqlite3.html
domain: python
license: PSF-2.0
tags: python, pytest, cpython, pip
fetched: 2026-07-02
part: 2/3
---

## Reference

### Module functions

**sqlite3.connect(*database*, *timeout=5.0*, *detect_types=0*, *isolation_level='DEFERRED'*, *check_same_thread=True*, *factory=sqlite3.Connection*, *cached_statements=128*, *uri=False*, ***, *autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL*)**

Open a connection to an SQLite database.

**Parameters:**

- **database** (path-like object) – The path to the database file to be opened. You can pass `":memory:"` to create an SQLite database existing only in memory, and open a connection to it.
- **timeout** (*float*) – How many seconds the connection should wait before raising an `OperationalError` when a table is locked. If another connection opens a transaction to modify a table, that table will be locked until the transaction is committed. Default five seconds.
- **detect_types** (*int*) – Control whether and how data types not natively supported by SQLite are looked up to be converted to Python types, using the converters registered with `register_converter()`. Set it to any combination (using `|`, bitwise or) of `PARSE_DECLTYPES` and `PARSE_COLNAMES` to enable this. Column names take precedence over declared types if both flags are set. By default (`0`), type detection is disabled.
- **isolation_level** (*str**|**None*) – Control legacy transaction handling behaviour. See `Connection.isolation_level` and Transaction control via the isolation_level attribute for more information. Can be `"DEFERRED"` (default), `"EXCLUSIVE"` or `"IMMEDIATE"`; or `None` to disable opening transactions implicitly. Has no effect unless `Connection.autocommit` is set to `LEGACY_TRANSACTION_CONTROL` (the default).
- **check_same_thread** (*bool*) – If `True` (default), `ProgrammingError` will be raised if the database connection is used by a thread other than the one that created it. If `False`, the connection may be accessed in multiple threads; write operations may need to be serialized by the user to avoid data corruption. See `threadsafety` for more information.
- **factory** (*Connection*) – A custom subclass of `Connection` to create the connection with, if not the default `Connection` class.
- **cached_statements** (*int*) – The number of statements that `sqlite3` should internally cache for this connection, to avoid parsing overhead. By default, 128 statements.
- **uri** (*bool*) – If set to `True`, *database* is interpreted as a URI with a file path and an optional query string. The scheme part *must* be `"file:"`, and the path can be relative or absolute. The query string allows passing parameters to SQLite, enabling various How to work with SQLite URIs.
- **autocommit** (*bool*) – Control **PEP 249** transaction handling behaviour. See `Connection.autocommit` and Transaction control via the autocommit attribute for more information. *autocommit* currently defaults to `LEGACY_TRANSACTION_CONTROL`. The default will change to `False` in a future Python release.

**Return type:**

*Connection*

Raises an auditing event `sqlite3.connect` with argument `database`.

Raises an auditing event `sqlite3.connect/handle` with argument `connection_handle`.

Changed in version 3.4: Added the *uri* parameter.

Changed in version 3.7: *database* can now also be a path-like object, not only a string.

Changed in version 3.10: Added the `sqlite3.connect/handle` auditing event.

Changed in version 3.12: Added the *autocommit* parameter.

Changed in version 3.13: Positional use of the parameters *timeout*, *detect_types*, *isolation_level*, *check_same_thread*, *factory*, *cached_statements*, and *uri* is deprecated. They will become keyword-only parameters in Python 3.15.

**sqlite3.complete_statement(*statement*)**

Return `True` if the string *statement* appears to contain one or more complete SQL statements. No syntactic verification or parsing of any kind is performed, other than checking that there are no unclosed string literals and the statement is terminated by a semicolon.

For example:

```pycon
>>> sqlite3.complete_statement("SELECT foo FROM bar;")
True
>>> sqlite3.complete_statement("SELECT foo")
False
```

This function may be useful during command-line input to determine if the entered text seems to form a complete SQL statement, or if additional input is needed before calling `execute()`.

See `runsource()` in Lib/sqlite3/__main__.py for real-world use.

**sqlite3.enable_callback_tracebacks(*flag*, */*)**

Enable or disable callback tracebacks. By default you will not get any tracebacks in user-defined functions, aggregates, converters, authorizer callbacks etc. If you want to debug them, you can call this function with *flag* set to `True`. Afterwards, you will get tracebacks from callbacks on `sys.stderr`. Use `False` to disable the feature again.

Note

Errors in user-defined function callbacks are logged as unraisable exceptions. Use an `unraisable hook handler` for introspection of the failed callback.

**sqlite3.register_adapter(*type*, *adapter*, */*)**

Register an *adapter* callable to adapt the Python type *type* into an SQLite type. The adapter is called with a Python object of type *type* as its sole argument, and must return a value of a type that SQLite natively understands.

**sqlite3.register_converter(*typename*, *converter*, */*)**

Register the *converter* callable to convert SQLite objects of type *typename* into a Python object of a specific type. The converter is invoked for all SQLite values of type *typename*; it is passed a `bytes` object and should return an object of the desired Python type. Consult the parameter *detect_types* of `connect()` for information regarding how type detection works.

Note: *typename* and the name of the type in your query are matched case-insensitively.

### Module constants

**sqlite3.LEGACY_TRANSACTION_CONTROL**

Set `autocommit` to this constant to select old style (pre-Python 3.12) transaction control behaviour. See Transaction control via the isolation_level attribute for more information.

**sqlite3.PARSE_DECLTYPES**

Pass this flag value to the *detect_types* parameter of `connect()` to look up a converter function using the declared types for each column. The types are declared when the database table is created. `sqlite3` will look up a converter function using the first word of the declared type as the converter dictionary key. For example:

```sql
CREATE TABLE test(
   i integer primary key,  ! will look up a converter named "integer"
   p point,                ! will look up a converter named "point"
   n number(10)            ! will look up a converter named "number"
 )
```

This flag may be combined with `PARSE_COLNAMES` using the `|` (bitwise or) operator.

Note

Generated fields (for example `MAX(p)`) are returned as `str`. Use `PARSE_COLNAMES` to enforce types for such queries.

**sqlite3.PARSE_COLNAMES**

Pass this flag value to the *detect_types* parameter of `connect()` to look up a converter function by using the type name, parsed from the query column name, as the converter dictionary key. The query column name must be wrapped in double quotes (`"`) and the type name must be wrapped in square brackets (`[]`).

```sql
SELECT MAX(p) as "p [point]" FROM test;  ! will look up converter "point"
```

This flag may be combined with `PARSE_DECLTYPES` using the `|` (bitwise or) operator.

**sqlite3.SQLITE_OK**

**sqlite3.SQLITE_DENY**

**sqlite3.SQLITE_IGNORE**

Flags that should be returned by the *authorizer_callback* callable passed to `Connection.set_authorizer()`, to indicate whether:

- Access is allowed (`SQLITE_OK`),
- The SQL statement should be aborted with an error (`SQLITE_DENY`)
- The column should be treated as a `NULL` value (`SQLITE_IGNORE`)

**sqlite3.apilevel**

String constant stating the supported DB-API level. Required by the DB-API. Hard-coded to `"2.0"`.

**sqlite3.paramstyle**

String constant stating the type of parameter marker formatting expected by the `sqlite3` module. Required by the DB-API. Hard-coded to `"qmark"`.

Note

The `named` DB-API parameter style is also supported.

**sqlite3.sqlite_version**

Version number of the runtime SQLite library as a `string`.

**sqlite3.sqlite_version_info**

Version number of the runtime SQLite library as a `tuple` of `integers`.

**sqlite3.threadsafety**

Integer constant required by the DB-API 2.0, stating the level of thread safety the `sqlite3` module supports. This attribute is set based on the default threading mode the underlying SQLite library is compiled with. The SQLite threading modes are:

1. **Single-thread**: In this mode, all mutexes are disabled and SQLite is unsafe to use in more than a single thread at once.
2. **Multi-thread**: In this mode, SQLite can be safely used by multiple threads provided that no single database connection is used simultaneously in two or more threads.
3. **Serialized**: In serialized mode, SQLite can be safely used by multiple threads with no restriction.

The mappings from SQLite threading modes to DB-API 2.0 threadsafety levels are as follows:

| SQLite threading mode | **threadsafety** | SQLITE_THREADSAFE | DB-API 2.0 meaning |
|---|---|---|---|
| single-thread | 0 | 0 | Threads may not share the module |
| multi-thread | 1 | 2 | Threads may share the module, but not connections |
| serialized | 3 | 1 | Threads may share the module, connections and cursors |

Changed in version 3.11: Set *threadsafety* dynamically instead of hard-coding it to `1`.

**sqlite3.SQLITE_DBCONFIG_DEFENSIVE**

**sqlite3.SQLITE_DBCONFIG_DQS_DDL**

**sqlite3.SQLITE_DBCONFIG_DQS_DML**

**sqlite3.SQLITE_DBCONFIG_ENABLE_FKEY**

**sqlite3.SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER**

**sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION**

**sqlite3.SQLITE_DBCONFIG_ENABLE_QPSG**

**sqlite3.SQLITE_DBCONFIG_ENABLE_TRIGGER**

**sqlite3.SQLITE_DBCONFIG_ENABLE_VIEW**

**sqlite3.SQLITE_DBCONFIG_LEGACY_ALTER_TABLE**

**sqlite3.SQLITE_DBCONFIG_LEGACY_FILE_FORMAT**

**sqlite3.SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE**

**sqlite3.SQLITE_DBCONFIG_RESET_DATABASE**

**sqlite3.SQLITE_DBCONFIG_TRIGGER_EQP**

**sqlite3.SQLITE_DBCONFIG_TRUSTED_SCHEMA**

**sqlite3.SQLITE_DBCONFIG_WRITABLE_SCHEMA**

These constants are used for the `Connection.setconfig()` and `getconfig()` methods.

The availability of these constants varies depending on the version of SQLite Python was compiled with.

Added in version 3.12.

See also

**https://www.sqlite.org/c3ref/c_dbconfig_defensive.html**

SQLite docs: Database Connection Configuration Options

Deprecated since version 3.12, removed in version 3.14: The `version` and `version_info` constants.

### Connection objects

***class*sqlite3.Connection**

Each open SQLite database is represented by a `Connection` object, which is created using `sqlite3.connect()`. Their main purpose is creating `Cursor` objects, and Transaction control.

See also

- How to use connection shortcut methods
- How to use the connection context manager

Changed in version 3.13: A `ResourceWarning` is emitted if `close()` is not called before a `Connection` object is deleted.

An SQLite database connection has the following attributes and methods:

**cursor(*factory=Cursor*)**

Create and return a `Cursor` object. The cursor method accepts a single optional parameter *factory*. If supplied, this must be a callable returning an instance of `Cursor` or its subclasses.

**blobopen(*table*, *column*, *rowid*, */*, ***, *readonly=False*, *name='main'*)**

Open a `Blob` handle to an existing BLOB.

**Parameters:**

- **table** (*str*) – The name of the table where the blob is located.
- **column** (*str*) – The name of the column where the blob is located.
- **rowid** (*int*) – The row id where the blob is located.
- **readonly** (*bool*) – Set to `True` if the blob should be opened without write permissions. Defaults to `False`.
- **name** (*str*) – The name of the database where the blob is located. Defaults to `"main"`.

**Raises:**

**OperationalError** – When trying to open a blob in a `WITHOUT ROWID` table.

**Return type:**

Blob

Note

The blob size cannot be changed using the `Blob` class. Use the SQL function `zeroblob` to create a blob with a fixed size.

Added in version 3.11.

**commit()**

Commit any pending transaction to the database. If `autocommit` is `True`, or there is no open transaction, this method does nothing. If `autocommit` is `False`, a new transaction is implicitly opened if a pending transaction was committed by this method.

**rollback()**

Roll back to the start of any pending transaction. If `autocommit` is `True`, or there is no open transaction, this method does nothing. If `autocommit` is `False`, a new transaction is implicitly opened if a pending transaction was rolled back by this method.

**close()**

Close the database connection. If `autocommit` is `False`, any pending transaction is implicitly rolled back. If `autocommit` is `True` or `LEGACY_TRANSACTION_CONTROL`, no implicit transaction control is executed. Make sure to `commit()` before closing to avoid losing pending changes.

**execute(*sql*, *parameters=()*, */*)**

Create a new `Cursor` object and call `execute()` on it with the given *sql* and *parameters*. Return the new cursor object.

**executemany(*sql*, *parameters*, */*)**

Create a new `Cursor` object and call `executemany()` on it with the given *sql* and *parameters*. Return the new cursor object.

**executescript(*sql_script*, */*)**

Create a new `Cursor` object and call `executescript()` on it with the given *sql_script*. Return the new cursor object.

**create_function(*name*, *narg*, *func*, ***, *deterministic=False*)**

Create or remove a user-defined SQL function.

**Parameters:**

- **name** (*str*) – The name of the SQL function.
- **narg** (*int*) – The number of arguments the SQL function can accept. If `-1`, it may take any number of arguments.
- **func** (callback | None) – A callable that is called when the SQL function is invoked. The callable must return a type natively supported by SQLite. Set to `None` to remove an existing SQL function.
- **deterministic** (*bool*) – If `True`, the created SQL function is marked as deterministic, which allows SQLite to perform additional optimizations.

Changed in version 3.8: Added the *deterministic* parameter.

Example:

```pycon
>>> import hashlib
>>> def md5sum(t):
...     return hashlib.md5(t).hexdigest()
>>> con = sqlite3.connect(":memory:")
>>> con.create_function("md5", 1, md5sum)
>>> for row in con.execute("SELECT md5(?)", (b"foo",)):
...     print(row)
('acbd18db4cc2f85cedef654fccc4a4d8',)
>>> con.close()
```

Changed in version 3.13: Passing *name*, *narg*, and *func* as keyword arguments is deprecated. These parameters will become positional-only in Python 3.15.

**create_aggregate(*name*, *n_arg*, *aggregate_class*)**

Create or remove a user-defined SQL aggregate function.

**Parameters:**

- **name** (*str*) – The name of the SQL aggregate function.
- **n_arg** (*int*) – The number of arguments the SQL aggregate function can accept. If `-1`, it may take any number of arguments.
- **aggregate_class** (class | None) – A class must implement the following methods: `step()`: Add a row to the aggregate. `finalize()`: Return the final result of the aggregate as a type natively supported by SQLite. The number of arguments that the `step()` method must accept is controlled by *n_arg*. Set to `None` to remove an existing SQL aggregate function.

Example:

```python
class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.execute("CREATE TABLE test(i)")
cur.execute("INSERT INTO test(i) VALUES(1)")
cur.execute("INSERT INTO test(i) VALUES(2)")
cur.execute("SELECT mysum(i) FROM test")
print(cur.fetchone()[0])

con.close()
```

Changed in version 3.13: Passing *name*, *n_arg*, and *aggregate_class* as keyword arguments is deprecated. These parameters will become positional-only in Python 3.15.

**create_window_function(*name*, *num_params*, *aggregate_class*, */*)**

Create or remove a user-defined aggregate window function.

**Parameters:**

- **name** (*str*) – The name of the SQL aggregate window function to create or remove.
- **num_params** (*int*) – The number of arguments the SQL aggregate window function can accept. If `-1`, it may take any number of arguments.
- **aggregate_class** (class | None) – A class that must implement the following methods: `step()`: Add a row to the current window. `value()`: Return the current value of the aggregate. `inverse()`: Remove a row from the current window. `finalize()`: Return the final result of the aggregate as a type natively supported by SQLite. The number of arguments that the `step()` and `value()` methods must accept is controlled by *num_params*. Set to `None` to remove an existing SQL aggregate window function.

**Raises:**

**NotSupportedError** – If used with a version of SQLite older than 3.25.0, which does not support aggregate window functions.

Added in version 3.11.

Example:

```python
# Example taken from https://www.sqlite.org/windowfunctions.html#udfwinfunc
class WindowSumInt:
    def __init__(self):
        self.count = 0

    def step(self, value):
        """Add a row to the current window."""
        self.count += value

    def value(self):
        """Return the current value of the aggregate."""
        return self.count

    def inverse(self, value):
        """Remove a row from the current window."""
        self.count -= value

    def finalize(self):
        """Return the final value of the aggregate.

        Any clean-up actions should be placed here.
        """
        return self.count

con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE test(x, y)")
values = [
    ("a", 4),
    ("b", 5),
    ("c", 3),
    ("d", 8),
    ("e", 1),
]
cur.executemany("INSERT INTO test VALUES(?, ?)", values)
con.create_window_function("sumint", 1, WindowSumInt)
cur.execute("""
    SELECT x, sumint(y) OVER (
        ORDER BY x ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_y
    FROM test ORDER BY x
""")
print(cur.fetchall())
con.close()
```

**create_collation(*name*, *callable*, */*)**

Create a collation named *name* using the collating function *callable*. *callable* is passed two `string` arguments, and it should return an `integer`:

- `1` if the first is ordered higher than the second
- `-1` if the first is ordered lower than the second
- `0` if they are ordered equal

The following example shows a reverse sorting collation:

```python
def collate_reverse(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1

con = sqlite3.connect(":memory:")
con.create_collation("reverse", collate_reverse)

cur = con.execute("CREATE TABLE test(x)")
cur.executemany("INSERT INTO test(x) VALUES(?)", [("a",), ("b",)])
cur.execute("SELECT x FROM test ORDER BY x COLLATE reverse")
for row in cur:
    print(row)
con.close()
```

Remove a collation function by setting *callable* to `None`.

Changed in version 3.11: The collation name can contain any Unicode character. Earlier, only ASCII characters were allowed.

**interrupt()**

Call this method from a different thread to abort any queries that might be executing on the connection. Aborted queries will raise an `OperationalError`.

**set_authorizer(*authorizer_callback*)**

Register callable *authorizer_callback* to be invoked for each attempt to access a column of a table in the database. The callback should return one of `SQLITE_OK`, `SQLITE_DENY`, or `SQLITE_IGNORE` to signal how access to the column should be handled by the underlying SQLite library.

The first argument to the callback signifies what kind of operation is to be authorized. The second and third argument will be arguments or `None` depending on the first argument. The 4th argument is the name of the database (“main”, “temp”, etc.) if applicable. The 5th argument is the name of the inner-most trigger or view that is responsible for the access attempt or `None` if this access attempt is directly from input SQL code.

Please consult the SQLite documentation about the possible values for the first argument and the meaning of the second and third argument depending on the first one. All necessary constants are available in the `sqlite3` module.

Passing `None` as *authorizer_callback* will disable the authorizer.

Changed in version 3.11: Added support for disabling the authorizer using `None`.

Changed in version 3.13: Passing *authorizer_callback* as a keyword argument is deprecated. The parameter will become positional-only in Python 3.15.

**set_progress_handler(*progress_handler*, *n*)**

Register callable *progress_handler* to be invoked for every *n* instructions of the SQLite virtual machine. This is useful if you want to get called from SQLite during long-running operations, for example to update a GUI.

If you want to clear any previously installed progress handler, call the method with `None` for *progress_handler*.

Returning a non-zero value from the handler function will terminate the currently executing query and cause it to raise a `DatabaseError` exception.

Changed in version 3.13: Passing *progress_handler* as a keyword argument is deprecated. The parameter will become positional-only in Python 3.15.

**set_trace_callback(*trace_callback*)**

Register callable *trace_callback* to be invoked for each SQL statement that is actually executed by the SQLite backend.

The only argument passed to the callback is the statement (as `str`) that is being executed. The return value of the callback is ignored. Note that the backend does not only run statements passed to the `Cursor.execute()` methods. Other sources include the transaction management of the `sqlite3` module and the execution of triggers defined in the current database.

Passing `None` as *trace_callback* will disable the trace callback.

Note

Exceptions raised in the trace callback are not propagated. As a development and debugging aid, use `enable_callback_tracebacks()` to enable printing tracebacks from exceptions raised in the trace callback.

Added in version 3.3.

Changed in version 3.13: Passing *trace_callback* as a keyword argument is deprecated. The parameter will become positional-only in Python 3.15.

**enable_load_extension(*enabled*, */*)**

Enable the SQLite engine to load SQLite extensions from shared libraries if *enabled* is `True`; else, disallow loading SQLite extensions. SQLite extensions can define new functions, aggregates or whole new virtual table implementations. One well-known extension is the fulltext-search extension distributed with SQLite.

Note

The `sqlite3` module is not built with loadable extension support by default, because some platforms (notably macOS) have SQLite libraries which are compiled without this feature. To get loadable extension support, you must pass the `--enable-loadable-sqlite-extensions` option to **configure**.

Raises an auditing event `sqlite3.enable_load_extension` with arguments `connection`, `enabled`.

Added in version 3.2.

Changed in version 3.10: Added the `sqlite3.enable_load_extension` auditing event.

```python3
con.enable_load_extension(True)

# Load the fulltext search extension
con.execute("select load_extension('./fts3.so')")

# alternatively you can load the extension using an API call:
# con.load_extension("./fts3.so")

# disable extension loading again
con.enable_load_extension(False)

# example from SQLite wiki
con.execute("CREATE VIRTUAL TABLE recipe USING fts3(name, ingredients)")
con.executescript("""
    INSERT INTO recipe (name, ingredients) VALUES('broccoli stew', 'broccoli peppers cheese tomatoes');
    INSERT INTO recipe (name, ingredients) VALUES('pumpkin stew', 'pumpkin onions garlic celery');
    INSERT INTO recipe (name, ingredients) VALUES('broccoli pie', 'broccoli cheese onions flour');
    INSERT INTO recipe (name, ingredients) VALUES('pumpkin pie', 'pumpkin sugar flour butter');
    """)
for row in con.execute("SELECT rowid, name, ingredients FROM recipe WHERE name MATCH 'pie'"):
    print(row)
```

**load_extension(*path*, */*, ***, *entrypoint=None*)**

Load an SQLite extension from a shared library. Enable extension loading with `enable_load_extension()` before calling this method.

**Parameters:**

- **path** (*str*) – The path to the SQLite extension.
- **entrypoint** (*str**|**None*) – Entry point name. If `None` (the default), SQLite will come up with an entry point name of its own; see the SQLite docs Loading an Extension for details.

Raises an auditing event `sqlite3.load_extension` with arguments `connection`, `path`.

Added in version 3.2.

Changed in version 3.10: Added the `sqlite3.load_extension` auditing event.

Changed in version 3.12: Added the *entrypoint* parameter.

**iterdump(***, *filter=None*)**

Return an iterator to dump the database as SQL source code. Useful when saving an in-memory database for later restoration. Similar to the `.dump` command in the **sqlite3** shell.

**Parameters:**

**filter** (*str**|**None*) – An optional `LIKE` pattern for database objects to dump, e.g. `prefix_%`. If `None` (the default), all database objects will be included.

Example:

```python
# Convert file example.db to SQL dump file dump.sql
con = sqlite3.connect('example.db')
with open('dump.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
con.close()
```

See also

How to handle non-UTF-8 text encodings

Changed in version 3.13: Added the *filter* parameter.

**backup(*target*, ***, *pages=-1*, *progress=None*, *name='main'*, *sleep=0.250*)**

Create a backup of an SQLite database.

Works even if the database is being accessed by other clients or concurrently by the same connection.

**Parameters:**

- **target** (*Connection*) – The database connection to save the backup to.
- **pages** (*int*) – The number of pages to copy at a time. If equal to or less than `0`, the entire database is copied in a single step. Defaults to `-1`.
- **progress** (callback | None) – If set to a callable, it is invoked with three integer arguments for every backup iteration: the *status* of the last iteration, the *remaining* number of pages still to be copied, and the *total* number of pages. Defaults to `None`.
- **name** (*str*) – The name of the database to back up. Either `"main"` (the default) for the main database, `"temp"` for the temporary database, or the name of a custom database as attached using the `ATTACH DATABASE` SQL statement.
- **sleep** (*float*) – The number of seconds to sleep between successive attempts to back up remaining pages.

Example 1, copy an existing database into another:

```python
def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

src = sqlite3.connect('example.db')
dst = sqlite3.connect('backup.db')
with dst:
    src.backup(dst, pages=1, progress=progress)
dst.close()
src.close()
```

Example 2, copy an existing database into a transient copy:

```python
src = sqlite3.connect('example.db')
dst = sqlite3.connect(':memory:')
src.backup(dst)
dst.close()
src.close()
```

Added in version 3.7.

See also

How to handle non-UTF-8 text encodings

**getlimit(*category*, */*)**

Get a connection runtime limit.
