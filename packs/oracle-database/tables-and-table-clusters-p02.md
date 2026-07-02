---
title: "Tables and Table Clusters (part 2/4)"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/tables-and-table-clusters.html
domain: oracle-database
license: CC-BY-SA-4.0
tags: oracle database, oracle rdbms, pl/sql, oracle corporation
fetched: 2026-07-02
part: 2/4
---

### Overview of Tables

A table is the basic unit of data organization in an Oracle database.

A table describes an entity, which is something of significance about which information must be recorded. For example, an employee could be an entity.

Oracle Database tables fall into the following basic categories:

- Relational tables Relational tables have simple columns and are the most common table type. Example 2-1 shows a `CREATE TABLE` statement for a relational table.
- Object tables The columns correspond to the top-level attributes of an object type. See "Overview of Object Tables".

You can create a relational table with the following organizational characteristics:

- A heap-organized table does not store rows in any particular order. The `CREATE TABLE` statement creates a heap-organized table by default.
- An index-organized table orders rows according to the primary key values. For some applications, index-organized tables enhance performance and use disk space more efficiently. See "Overview of Index-Organized Tables".
- An external table is a read-only table whose metadata is stored in the database but whose data is stored outside the database. See "Overview of External Tables".

A table is either permanent or temporary. A permanent table definition and data persist across sessions. A temporary table definition persists in the same way as a permanent table definition, but the data exists only for the duration of a transaction or session. Temporary tables are useful in applications where a result set must be held temporarily, perhaps because the result is constructed by running multiple operations.

This topic contains the following topics:

- Columns
- Rows
- Example: CREATE TABLE and ALTER TABLE Statements
- Oracle Data Types
- Integrity Constraints
- Table Storage
- Table Compression

- Columns A table definition includes a table name and set of columns.
- Rows A row is a collection of column information corresponding to a record in a table.
- Example: CREATE TABLE and ALTER TABLE Statements The Oracle SQL statement to create a table is `CREATE TABLE`.
- Oracle Data Types Each column has a data type, which is associated with a specific storage format, constraints, and valid range of values. The data type of a value associates a fixed set of properties with the value.
- Integrity Constraints An **integrity constraint** is a named rule that restrict the values for one or more columns in a table.
- Table Storage Oracle Database uses a **data segment** in a tablespace to hold table data.
- Table Compression The database can use table compression to reduce the amount of storage required for the table.

See Also:

*Oracle Database Administrator’s Guide* to learn how to manage tables

**Parent topic:** Tables and Table Clusters

#### Columns

A table definition includes a table name and set of columns.

A column identifies an attribute of the entity described by the table. For example, the column `employee_id` in the `employees` table refers to the employee ID attribute of an employee entity.

In general, you give each column a column name, a data type, and a width when you create a table. For example, the data type for `employee_id` is `NUMBER(6)`, indicating that this column can only contain numeric data up to 6 digits in width. The width can be predetermined by the data type, as with `DATE`.

- Virtual Columns A table can contain a **virtual column**, which unlike a nonvirtual column does not consume disk space.
- Invisible Columns An invisible column is a user-specified column whose values are only visible when the column is explicitly specified by name. You can add an invisible column to a table without affecting existing applications, and make the column visible if necessary.

**Parent topic:** Overview of Tables

##### Virtual Columns

A table can contain a **virtual column**, which unlike a nonvirtual column does not consume disk space.

The database derives the values in a virtual column on demand by computing a set of user-specified expressions or functions. For example, the virtual column `income` could be a function of the `salary` and `commission_pct` columns.

See Also:

*Oracle Database Administrator’s Guide* to learn how to manage virtual columns

**Parent topic:** Columns

##### Invisible Columns

An invisible column is a user-specified column whose values are only visible when the column is explicitly specified by name. You can add an invisible column to a table without affecting existing applications, and make the column visible if necessary.

In general, invisible columns help migrate and evolve online applications. A use case might be an application that queries a three-column table with a `SELECT *` statement. Adding a fourth column to the table would break the application, which expects three columns of data. Adding a fourth invisible column makes the application function normally. A developer can then alter the application to handle a fourth column, and make the column visible when the application goes live.

The following example creates a table `products` with an invisible column `count`, and then makes the invisible column visible:

```
CREATE TABLE products ( prod_id INT, count INT INVISIBLE );
ALTER TABLE products MODIFY ( count VISIBLE );
```

See Also:

- *Oracle Database Administrator’s Guide* to learn how to manage invisible columns
- *Oracle Database SQL Language Reference* for more information about invisible columns

**Parent topic:** Columns

#### Rows

A row is a collection of column information corresponding to a record in a table.

For example, a row in the `employees` table describes the attributes of a specific employee: employee ID, last name, first name, and so on. After you create a table, you can insert, query, delete, and update rows using SQL.

**Parent topic:** Overview of Tables

#### Example: CREATE TABLE and ALTER TABLE Statements

The Oracle SQL statement to create a table is `CREATE TABLE`.

Example 2-1 CREATE TABLE employees

The following example shows the `CREATE TABLE` statement for the `employees` table in the `hr` sample schema. The statement specifies columns such as `employee_id`, `first_name`, and so on, specifying a data type such as `NUMBER` or `DATE` for each column.

```
CREATE TABLE employees
    ( employee_id    NUMBER(6)
    , first_name     VARCHAR2(20)
    , last_name      VARCHAR2(25)
         CONSTRAINT     emp_last_name_nn  NOT NULL
    , email          VARCHAR2(25)
        CONSTRAINT     emp_email_nn  NOT NULL
    , phone_number   VARCHAR2(20)
    , hire_date      DATE
        CONSTRAINT     emp_hire_date_nn  NOT NULL
    , job_id         VARCHAR2(10)
        CONSTRAINT     emp_job_nn  NOT NULL
    , salary         NUMBER(8,2)
    , commission_pct NUMBER(2,2)
    , manager_id     NUMBER(6)
    , department_id  NUMBER(4)
    , CONSTRAINT     emp_salary_min
                     CHECK (salary > 0)
    , CONSTRAINT     emp_email_uk
                     UNIQUE (email)
    ) ;
```

Example 2-2 ALTER TABLE employees

The following example shows an `ALTER TABLE` statement that adds integrity constraints to the `employees` table. Integrity constraints enforce business rules and prevent the entry of invalid information into tables.

```
ALTER TABLE employees
ADD ( CONSTRAINT     emp_emp_id_pk
                       PRIMARY KEY (employee_id)
    , CONSTRAINT     emp_dept_fk
                       FOREIGN KEY (department_id)
                         REFERENCES departments
    , CONSTRAINT     emp_job_fk
                       FOREIGN KEY (job_id)
                         REFERENCES jobs (job_id)
    , CONSTRAINT     emp_manager_fk
                       FOREIGN KEY (manager_id)
                         REFERENCES employees
    ) ;
```

Example 2-3 Rows in the employees Table

The following sample output shows 8 rows and 6 columns of the `hr.employees` table.

```
EMPLOYEE_ID FIRST_NAME  LAST_NAME      SALARY COMMISSION_PCT DEPARTMENT_ID
----------- ----------- ------------- ------- -------------- -------------
        100 Steven      King            24000                           90
        101 Neena       Kochhar         17000                           90
        102 Lex         De Haan         17000                           90
        103 Alexander   Hunold           9000                           60
        107 Diana       Lorentz          4200                           60
        149 Eleni       Zlotkey         10500             .2            80
        174 Ellen       Abel            11000             .3            80
        178 Kimberely   Grant            7000            .15
```

The preceding output illustrates some of the following important characteristics of tables, columns, and rows:

- A row of the table describes the attributes of one employee: name, salary, department, and so on. For example, the first row in the output shows the record for the employee named Steven King.
- A column describes an attribute of the employee. In the example, the `employee_id` column is the primary key, which means that every employee is uniquely identified by employee ID. Any two employees are guaranteed not to have the same employee ID.
- A non-key column can contain rows with identical values. In the example, the salary value for employees 101 and 102 is the same: `17000`.
- A foreign key column refers to a primary or unique key in the same table or a different table. In this example, the value of `90` in `department_id` corresponds to the `department_id` column of the `departments` table.
- A field is the intersection of a row and column. It can contain only one value. For example, the field for the department ID of employee 103 contains the value `60`.
- A field can lack a value. In this case, the field is said to contain a null value. The value of the `commission_pct` column for employee 100 is null, whereas the value in the field for employee 149 is `.2`. A column allows nulls unless a `NOT` `NULL` or primary key integrity constraint has been defined on this column, in which case no row can be inserted without a value for this column.

See Also:

*Oracle Database SQL Language Reference* for `CREATE TABLE` syntax and semantics

**Parent topic:** Overview of Tables

#### Oracle Data Types

Each column has a data type, which is associated with a specific storage format, constraints, and valid range of values. The data type of a value associates a fixed set of properties with the value.

These properties cause Oracle Database to treat values of one data type differently from values of another. For example, you can multiply values of the `NUMBER` data type, but not values of the `RAW` data type.

When you create a table, you must specify a data type for each of its columns. Each value subsequently inserted in a column assumes the column data type.

Oracle Database provides several built-in data types. The most commonly used data types fall into the following categories:

- Character Data Types
- Numeric Data Types
- Datetime Data Types
- Rowid Data Types
- Format Models and Data Types

Other important categories of built-in types include raw, large objects (LOBs), and collections. PL/SQL has data types for constants and variables, which include `BOOLEAN`, reference types, composite types (records), and user-defined types.

- Character Data Types Character data types store alphanumeric data in strings. The most common character data type is `VARCHAR2`, which is the most efficient option for storing character data.
- Numeric Data Types The Oracle Database numeric data types store fixed and floating-point numbers, zero, and infinity. Some numeric types also store values that are the undefined result of an operation, which is known as "not a number" or `NaN`.
- Datetime Data Types The datetime data types are `DATE` and `TIMESTAMP`. Oracle Database provides comprehensive time zone support for time stamps.
- Rowid Data Types Every row stored in the database has an address– an internal representation to locate that row within the database. Oracle Database uses a `ROWID` data type to store the address (rowid) of every row in the database.
- Format Models and Data Types A format model is a character literal that describes the format of datetime or numeric data stored in a character string. A format model does not change the internal representation of the value in the database.

See Also:

- "Overview of LOBs"
- *Oracle Database SQL Language Reference* to learn about built-in SQL data types
- *Oracle Database PL/SQL Packages and Types Reference* to learn about PL/SQL data types
- *Oracle Database Development Guide* to learn how to use the built-in data types

**Parent topic:** Overview of Tables

##### Character Data Types

Character data types store alphanumeric data in strings. The most common character data type is `VARCHAR2`, which is the most efficient option for storing character data.

The byte values correspond to the character encoding scheme, generally called a character set. The database character set is established at database creation. Examples of character sets are 7-bit ASCII, EBCDIC, and Unicode UTF-8.

The length semantics of character data types are measurable in bytes or characters. The treatment of strings as a sequence of bytes is called byte semantics. This is the default for character data types. The treatment of strings as a sequence of characters is called character semantics. A character is a code point of the database character set.

- VARCHAR2 and CHAR Data Types The `VARCHAR2` data type stores variable-length character literals. A literal is a fixed data value.
- NCHAR and NVARCHAR2 Data Types The `NCHAR` and `NVARCHAR2` data types store Unicode character data.

See Also:

- "Character Sets"
- *Oracle Database Get Started with Oracle Database Development* for a brief introduction to data types
- *Oracle Database Development Guide* to learn how to choose a character data type

**Parent topic:** Oracle Data Types

###### VARCHAR2 and CHAR Data Types

The

VARCHAR2

data type stores variable-length character literals. A

literal

is a fixed data value.

For example, `'LILA'`, `'St. George Island'`, and `'101'` are all character literals; `5001` is a numeric literal. Character literals are enclosed in single quotation marks so that the database can distinguish them from schema object names.

Note:

This manual uses the terms text literal, character literal, and string interchangeably.

When you create a table with a `VARCHAR2` column, you specify a maximum string length. In Example 2-1, the `last_name` column has a data type of `VARCHAR2(25)`, which means that any name stored in the column has a maximum of 25 bytes.

For each row, Oracle Database stores each value in the column as a variable-length field unless a value exceeds the maximum length, in which case the database returns an error. For example, in a single-byte character set, if you enter 10 characters for the `last_name` column value in a row, then the column in the row piece stores only 10 characters (10 bytes), not 25. Using `VARCHAR2` reduces space consumption.

In contrast to `VARCHAR2`, `CHAR` stores fixed-length character strings. When you create a table with a `CHAR` column, the column requires a string length. The default is 1 byte. The database uses blanks to pad the value to the specified length.

Oracle Database compares `VARCHAR2` values using nonpadded comparison semantics and compares `CHAR` values using blank-padded comparison semantics.

See Also:

*Oracle Database SQL Language Reference* for details about blank-padded and nonpadded comparison semantics

**Parent topic:** Character Data Types

###### NCHAR and NVARCHAR2 Data Types

The

NCHAR

and

NVARCHAR2

data types store Unicode character data.

Unicode is a universal encoded character set that can store information in any language using a single character set. `NCHAR` stores fixed-length character strings that correspond to the national character set, whereas `NVARCHAR2` stores variable length character strings.

You specify a national character set when creating a database. The character set of `NCHAR` and `NVARCHAR2` data types must be either `AL16UTF16` or `UTF8`. Both character sets use Unicode encoding.

When you create a table with an `NCHAR` or `NVARCHAR2` column, the maximum size is always in character length semantics. Character length semantics is the default and only length semantics for `NCHAR` or `NVARCHAR2`.

See Also:

*Oracle Database Globalization Support Guide* for information about Oracle's globalization support feature

**Parent topic:** Character Data Types

##### Numeric Data Types

The Oracle Database numeric data types store fixed and floating-point numbers, zero, and infinity. Some numeric types also store values that are the undefined result of an operation, which is known as "not a number" or `NaN`.

Oracle Database stores numeric data in variable-length format. Each value is stored in scientific notation, with 1 byte used to store the exponent. The database uses up to 20 bytes to store the mantissa, which is the part of a floating-point number that contains its significant digits. Oracle Database does not store leading and trailing zeros.

- NUMBER Data Type The `NUMBER` data type stores fixed and floating-point numbers. The database can store numbers of virtually any magnitude. This data is guaranteed to be portable among different operating systems running Oracle Database. The `NUMBER` data type is recommended for most cases in which you must store numeric data.
- Floating-Point Numbers Oracle Database provides two numeric data types exclusively for floating-point numbers: `BINARY_FLOAT` and `BINARY_DOUBLE`.

**Parent topic:** Oracle Data Types

###### NUMBER Data Type

The `NUMBER` data type stores fixed and floating-point numbers. The database can store numbers of virtually any magnitude. This data is guaranteed to be portable among different operating systems running Oracle Database. The `NUMBER` data type is recommended for most cases in which you must store numeric data.

You specify a fixed-point number in the form `NUMBER``(``p``,``s``)`, where `p` and `s` refer to the following characteristics:

- Precision The precision specifies the total number of digits. If a precision is not specified, then the column stores the values exactly as provided by the application without any rounding.
- Scale The scale specifies the number of digits from the decimal point to the least significant digit. Positive scale counts digits to the right of the decimal point up to and including the least significant digit. Negative scale counts digits to the left of the decimal point up to but not including the least significant digit. If you specify a precision without a scale, as in `NUMBER(6)`, then the scale is 0.

In Example 2-1, the `salary` column is type `NUMBER(8,2)`, so the precision is 8 and the scale is 2. Thus, the database stores a salary of 100,000 as `100000.00`.

**Parent topic:** Numeric Data Types

###### Floating-Point Numbers

Oracle Database provides two numeric data types exclusively for floating-point numbers: `BINARY_FLOAT` and `BINARY_DOUBLE`.

These types support all of the basic functionality provided by the `NUMBER` data type. However, whereas `NUMBER` uses decimal precision, `BINARY_FLOAT` and `BINARY_DOUBLE` use binary precision, which enables faster arithmetic calculations and usually reduces storage requirements.

`BINARY_FLOAT` and `BINARY_DOUBLE` are approximate numeric data types. They store approximate representations of decimal values, rather than exact representations. For example, the value 0.1 cannot be exactly represented by either `BINARY_DOUBLE` or `BINARY_FLOAT`. They are frequently used for scientific computations. Their behavior is similar to the data types `FLOAT` and `DOUBLE` in Java and XMLSchema.

See Also:

*Oracle Database SQL Language Reference* to learn about precision, scale, and other characteristics of numeric types

**Parent topic:** Numeric Data Types

##### Datetime Data Types

The datetime data types are `DATE` and `TIMESTAMP`. Oracle Database provides comprehensive time zone support for time stamps.

- DATE Data Type The `DATE` data type stores date and time. Although datetimes can be represented in character or number data types, `DATE` has special associated properties.
- TIMESTAMP Data Type The `TIMESTAMP` data type is an extension of the `DATE` data type.

**Parent topic:** Oracle Data Types

###### DATE Data Type

The `DATE` data type stores date and time. Although datetimes can be represented in character or number data types, `DATE` has special associated properties.

The database stores dates internally as numbers. Dates are stored in fixed-length fields of 7 bytes each, corresponding to century, year, month, day, hour, minute, and second.

Note:

Dates fully support arithmetic operations, so you add to and subtract from dates just as you can with numbers.

The database displays dates according to the specified format model. A format model is a character literal that describes the format of a datetime in a character string. The standard date format is `DD-MON-RR`, which displays dates in the form `01-JAN-11`.

`RR` is similar to `YY` (the last two digits of the year), but the century of the return value varies according to the specified two-digit year and the last two digits of the current year. Assume that in 1999 the database displays `01-JAN-11`. If the date format uses `RR`, then `11` specifies `2011`, whereas if the format uses `YY`, then `11` specifies `1911`. You can change the default date format at both the database instance and session level.

Oracle Database stores time in 24-hour format—`HH:MI:SS`. If no time portion is entered, then by default the time in a date field is `00:00:00 A.M`. In a time-only entry, the date portion defaults to the first day of the current month.

See Also:

- *Oracle Database Development Guide* for more information about centuries and date format masks
- *Oracle Database SQL Language Reference* for information about datetime format codes
- *Oracle Database Development Guide* to learn how to perform arithmetic operations with datetime data types

**Parent topic:** Datetime Data Types

###### TIMESTAMP Data Type

The `TIMESTAMP` data type is an extension of the `DATE` data type.

`TIMESTAMP` stores fractional seconds in addition to the information stored in the `DATE` data type. The `TIMESTAMP` data type is useful for storing precise time values, such as in applications that must track event order.

The `DATETIME` data types `TIMESTAMP WITH TIME ZONE` and `TIMESTAMP WITH LOCAL TIME ZONE` are time-zone aware. When a user selects the data, the value is adjusted to the time zone of the user session. This data type is useful for collecting and evaluating date information across geographic regions.

See Also:

*Oracle Database SQL Language Reference* for details about the syntax of creating and entering data in time stamp columns

**Parent topic:** Datetime Data Types

##### Rowid Data Types

Every row stored in the database has an address– an internal representation to locate that row within the database. Oracle Database uses a `ROWID` data type to store the address (rowid) of every row in the database.

Rowids fall into the following categories:

- Physical rowids store the addresses of rows in heap-organized tables, table clusters, and table and index partitions.
- Logical rowids store the addresses of rows in index-organized tables.
- Foreign rowids are identifiers in foreign tables, such as DB2 tables accessed through a gateway. They are not standard Oracle Database rowids.

A data type called the universal rowid, or urowid, supports all types of rowids.

- Use of Rowids Oracle Database uses rowids internally for the construction of indexes.
- ROWID Pseudocolumn Every table in an Oracle database has a pseudocolumn named `ROWID`.

**Parent topic:** Oracle Data Types

###### Use of Rowids

Oracle Database uses rowids internally for the construction of indexes.

A B-tree index, which is the most common type, contains an ordered list of keys divided into ranges. Each key is associated with a rowid that points to the associated row's address for fast access.

End users and application developers can also use rowids for several important functions:

- Rowids are a fast means of re-accessing a row if its `rowid` has previously been retrieved with a SELECT statement.
- Rowids provide the ability to see how a table is organized.

While you can create tables with columns defined using the `ROWID` data type, you should not store rowids with the intention of using them to access data at a later stage. Using rowids in this manner may yield unpredictable or incorrect results. The `rowid` for a row may change for a number of reasons which may be user initiated or internally by the database engine. You cannot depend on the `rowid` to be pointing to the same row or a valid row at all after any of these operations has occurred.

**Parent topic:** Rowid Data Types

###### ROWID Pseudocolumn

Every table in an Oracle database has a pseudocolumn named `ROWID`.

A pseudocolumn behaves like a table column, but is not actually stored in the table. You can select from pseudocolumns, but you cannot insert, update, or delete their values. A pseudocolumn is also similar to a SQL function without arguments. Functions without arguments typically return the same value for every row in the result set, whereas pseudocolumns typically return a different value for each row.

Values of the `ROWID` pseudocolumn are strings representing the address of each row. These strings have the data type `ROWID`. This pseudocolumn is not evident when listing the structure of a table by executing `SELECT` or `DESCRIBE`, nor does the pseudocolumn consume space. However, the rowid of each row can be retrieved with a SQL query using the reserved word `ROWID` as a column name.

The following example queries the `ROWID` pseudocolumn to show the rowid of the row in the `employees` table for employee 100:

```
SQL> SELECT ROWID FROM employees WHERE employee_id = 100;

ROWID
------------------
AAAPecAAFAAAABSAAA
```

See Also:

- "Rowid Format"
- *Oracle Database Development Guide* to learn how to identify rows by address
- *Oracle Database SQL Language Reference* to learn about rowid types

**Parent topic:** Rowid Data Types

##### Format Models and Data Types

A format model is a character literal that describes the format of datetime or numeric data stored in a character string. A format model does not change the internal representation of the value in the database.

When you convert a character string into a date or number, a format model determines how the database interprets the string. In SQL, you can use a format model as an argument of the `TO_CHAR` and `TO_DATE` functions to format a value to be returned from the database or to format a value to be stored in the database.

The following statement selects the salaries of the employees in Department 80 and uses the `TO_CHAR` function to convert these salaries into character values with the format specified by the number format model `'$99,990.99'`:

```
SQL> SELECT last_name employee, TO_CHAR(salary, '$99,990.99') AS "SALARY"
  2  FROM   employees
  3  WHERE  department_id = 80 AND last_name = 'Russell';
 
EMPLOYEE                  SALARY
------------------------- -----------
Russell                    $14,000.00
```

The following example updates a hire date using the `TO_DATE` function with the format mask `'YYYY MM DD'` to convert the string `'1998 05 20'` to a `DATE` value:

```
SQL> UPDATE employees
  2  SET hire_date = TO_DATE('1998 05 20','YYYY MM DD')
  3  WHERE last_name = 'Hunold';
```

See Also:

*Oracle Database SQL Language Reference* to learn more about format models

**Parent topic:** Oracle Data Types

#### Integrity Constraints

An **integrity constraint** is a named rule that restrict the values for one or more columns in a table.

Data integrity rules prevent invalid data entry into tables. Also, constraints can prevent the deletion of a table when certain dependencies exist.

If a constraint is enabled, then the database checks data as it is entered or updated. Oracle Database prevents data that does not conform to the constraint from being entered. If a constraint is disabled, then Oracle Database allows data that does not conform to the constraint to enter the database.

In Example 2-1, the `CREATE TABLE` statement specifies `NOT NULL` constraints for the `last_name`, `email`, `hire_date`, and `job_id` columns. The constraint clauses identify the columns and the conditions of the constraint. These constraints ensure that the specified columns contain no null values. For example, an attempt to insert a new employee without a job ID generates an error.

You can create a constraint when or after you create a table. You can temporarily disable constraints if needed. The database stores constraints in the data dictionary.

See Also:

- "Data Integrity" to learn about integrity constraints
- "Overview of the Data Dictionary" to learn about the data dictionary
- *Oracle Database SQL Language Reference* to learn about SQL constraint clauses

**Parent topic:** Overview of Tables

#### Table Storage

Oracle Database uses a **data segment** in a tablespace to hold table data.

A segment contains extents made up of data blocks. The data segment for a table (or cluster data segment, for a table cluster) is located in either the default tablespace of the table owner or in a tablespace named in the `CREATE TABLE` statement.

- Table Organization By default, a table is organized as a heap, which means that the database places rows where they fit best rather than in a user-specified order. Thus, a heap-organized table is an unordered collection of rows.
- Row Storage The database stores rows in data blocks. Each row of a table containing data for less than 256 columns is contained in one or more row pieces.
- Rowids of Row Pieces A **rowid** is effectively a 10-byte physical address of a row.
- Storage of Null Values A null is the absence of a value in a column. Nulls indicate missing, unknown, or inapplicable data.

See Also:

"User Segments" to learn about the types of segments and how they are created

**Parent topic:** Overview of Tables

##### Table Organization

By default, a table is organized as a heap, which means that the database places rows where they fit best rather than in a user-specified order. Thus, a heap-organized table is an unordered collection of rows.

Note:

Index-organized tables use a different principle of organization.

As users add rows, the database places the rows in the first available free space in the data segment. Rows are not guaranteed to be retrieved in the order in which they were inserted.

The `hr.departments` table is a heap-organized table. It has columns for department ID, name, manager ID, and location ID. As rows are inserted, the database stores them wherever they fit. A data block in the table segment might contain the unordered rows shown in the following example:

```
50,Shipping,121,1500
120,Treasury,,1700
70,Public Relations,204,2700
30,Purchasing,114,1700
130,Corporate Tax,,1700
10,Administration,200,1700
110,Accounting,205,1700
```

The column order is the same for all rows in a table. The database usually stores columns in the order in which they were listed in the `CREATE TABLE` statement, but this order is not guaranteed. For example, if a table has a column of type `LONG`, then Oracle Database always stores this column last in the row. Also, if you add a new column to a table, then the new column becomes the last column stored.

A table can contain a virtual column, which unlike normal columns does not consume space on disk. The database derives the values in a virtual column on demand by computing a set of user-specified expressions or functions. You can index virtual columns, collect statistics on them, and create integrity constraints. Thus, virtual columns are much like nonvirtual columns.

See Also:

- "Overview of Index-Organized Tables"
- *Oracle Database SQL Language Reference* to learn about virtual columns

**Parent topic:** Table Storage

##### Row Storage

The database stores rows in data blocks. Each row of a table containing data for less than 256 columns is contained in one or more row pieces.

If possible, Oracle Database stores each row as one row piece. However, if all of the row data cannot be inserted into a single data block, or if an update to an existing row causes the row to outgrow its data block, then the database stores the row using multiple row pieces.

Rows in a table cluster contain the same information as rows in nonclustered tables. Additionally, rows in a table cluster contain information that references the cluster key to which they belong.

See Also:

"Data Block Format" to learn about the components of a data block

**Parent topic:** Table Storage

##### Rowids of Row Pieces

A **rowid** is effectively a 10-byte physical address of a row.

Every row in a heap-organized table has a rowid unique to this table that corresponds to the physical address of a row piece. For table clusters, rows in different tables that are in the same data block can have the same rowid.

Oracle Database uses rowids internally for the construction of indexes. For example, each key in a B-tree index is associated with a rowid that points to the address of the associated row for fast access. Physical rowids provide the fastest possible access to a table row, enabling the database to retrieve a row in as little as a single I/O.

See Also:

- "Rowid Format" to learn about the structure of a rowid
- "Overview of B-Tree Indexes" to learn about the types and structure of B-tree indexes

**Parent topic:** Table Storage

##### Storage of Null Values

A null is the absence of a value in a column. Nulls indicate missing, unknown, or inapplicable data.

Nulls are stored in the database if they fall between columns with data values. In these cases, they require 1 byte to store the length of the column (zero). Trailing nulls in a row require no storage because a new row header signals that the remaining columns in the previous row are null. For example, if the last three columns of a table are null, then no data is stored for these columns.

See Also:

*Oracle Database SQL Language Reference* to learn more about null values

**Parent topic:** Table Storage

#### Table Compression

The database can use table compression to reduce the amount of storage required for the table.

Compression saves disk space, reduces memory use in the database buffer cache, and in some cases speeds query execution. Table compression is transparent to database applications.

- Basic Table Compression and Advanced Row Compression Dictionary-based table compression provides good compression ratios for heap-organized tables.
- Hybrid Columnar Compression With Hybrid Columnar Compression, the database stores the same column for a group of rows together. The data block does not store data in row-major format, but uses a combination of both row and columnar methods.

**Parent topic:** Overview of Tables

##### Basic Table Compression and Advanced Row Compression

Dictionary-based table compression provides good compression ratios for heap-organized tables.

Oracle Database supports the following types of dictionary-based table compression:

- Basic table compression This type of compression is intended for bulk load operations. The database does not compress data modified using conventional DML. You must use direct path INSERT operations, `ALTER TABLE . . . MOVE` operations, or online table redefinition to achieve basic table compression.
- Advanced row compression This type of compression is intended for OLTP applications and compresses data manipulated by any SQL operation. The database achieves a competitive compression ratio while enabling the application to perform DML in approximately the same amount of time as DML on an uncompressed table.

For the preceding types of compression, the database stores compressed rows in row major format. All columns of one row are stored together, followed by all columns of the next row, and so on. The database replaces duplicate values with a short reference to a symbol table stored at the beginning of the block. Thus, information that the database needs to re-create the uncompressed data is stored in the data block itself.

Compressed data blocks look much like normal data blocks. Most database features and functions that work on regular data blocks also work on compressed blocks.

You can declare compression at the tablespace, table, partition, or subpartition level. If specified at the tablespace level, then all tables created in the tablespace are compressed by default.

Example 2-4 Table-Level Compression

The following statement applies advanced row compression to the `orders` table:

```
ALTER TABLE oe.orders ROW STORE COMPRESS ADVANCED;
```

Example 2-5 Partition-Level Compression

The following example of a partial `CREATE TABLE` statement specifies advanced row compression for one partition and basic table compression for the other partition:

```
CREATE TABLE sales (
    prod_id     NUMBER     NOT NULL,
    cust_id     NUMBER     NOT NULL, ... )
 PCTFREE 5 NOLOGGING NOCOMPRESS
 PARTITION BY RANGE (time_id)
 ( partition sales_2013 VALUES LESS THAN(TO_DATE(...)) ROW STORE COMPRESS BASIC,
   partition sales_2014 VALUES LESS THAN (MAXVALUE) ROW STORE COMPRESS ADVANCED );
```

See Also:

- "Row Format" to learn how values are stored in a row
- "Data Block Compression" to learn about the format of compressed data blocks
- "SQL*Loader" to learn about using SQL*Loader for direct path loads
- *Oracle Database Administrator’s Guide* and *Oracle Database Performance Tuning Guide* to learn about table compression

**Parent topic:** Table Compression

##### Hybrid Columnar Compression

With Hybrid Columnar Compression, the database stores the same column for a group of rows together. The data block does not store data in row-major format, but uses a combination of both row and columnar methods.

Storing column data together, with the same data type and similar characteristics, dramatically increases the storage savings achieved from compression. The database compresses data manipulated by any SQL operation, although compression levels are higher for direct path loads. Database operations work transparently against compressed objects, so no application changes are required.

Note:

Hybrid Column Compression and In-Memory Column Store (IM column store) are closely related. The primary difference is that Hybrid Column Compression optimizes disk storage, whereas the IM column store optimizes memory storage.

- Types of Hybrid Columnar Compression If your underlying storage supports Hybrid Columnar Compression, then you can specify different types of compression, depending on your requirements.
- Compression Units Hybrid Columnar Compression uses a logical construct called a **compression unit** to store a set of rows.
- DML and Hybrid Columnar Compression Hybrid Columnar Compression has implications for row locking in different types of DML operations.

See Also:

"In-Memory Area" to learn more about the IM column store

**Parent topic:** Table Compression

###### Types of Hybrid Columnar Compression

If your underlying storage supports Hybrid Columnar Compression, then you can specify different types of compression, depending on your requirements.

The compression options are:

- Warehouse compression This type of compression is optimized to save storage space, and is intended for data warehouse applications.
- Archive compression This type of compression is optimized for maximum compression levels, and is intended for historical data and data that does not change.

Hybrid Columnar Compression is optimized for data warehousing and decision support applications on Oracle Exadata storage. Oracle Exadata maximizes the performance of queries on tables that are compressed using Hybrid Columnar Compression, taking advantage of the processing power, memory, and Infiniband network bandwidth that are integral to the Oracle Exadata storage server.

Other Oracle storage systems support Hybrid Columnar Compression, and deliver the same space savings as on Oracle Exadata storage, but do not deliver the same level of query performance. For these storage systems, Hybrid Columnar Compression is ideal for in-database archiving of older data that is infrequently accessed.

**Parent topic:** Hybrid Columnar Compression

###### Compression Units

Hybrid Columnar Compression uses a logical construct called a **compression unit** to store a set of rows.

When you load data into a table, the database stores groups of rows in columnar format, with the values for each column stored and compressed together. After the database has compressed the column data for a set of rows, the database fits the data into the compression unit.

For example, you apply Hybrid Columnar Compression to a `daily_sales` table. At the end of every day, you populate the table with items and the number sold, with the item ID and date forming a composite primary key. The following table shows a subset of the rows in `daily_sales`.

Table 2-2 Sample Table daily_sales

| Item_ID | Date | Num_Sold | Shipped_From | Restock |
|---|---|---|---|---|
| 1000 | 01-JUN-18 | 2 | WAREHOUSE1 | Y |
| 1001 | 01-JUN-18 | 0 | WAREHOUSE3 | N |
| 1002 | 01-JUN-18 | 1 | WAREHOUSE3 | N |
| 1003 | 01-JUN-14 | 0 | WAREHOUSE2 | N |
| 1004 | 01-JUN-18 | 2 | WAREHOUSE1 | N |
| 1005 | 01-JUN-18 | 1 | WAREHOUSE2 | N |

Assume that this subset of rows is stored in one compression unit. Hybrid Columnar Compression stores the values for each column together, and then uses multiple algorithms to compress each column. The database chooses the algorithms based on a variety of factors, including the data type of the column, the cardinality of the actual values in the column, and the compression level chosen by the user.

As shown in the following graphic, each compression unit can span multiple data blocks. The values for a particular column may or may not span multiple blocks.

Figure 2-4 Compression Unit

Description of "Figure 2-4 Compression Unit"

If Hybrid Columnar Compression does not lead to space savings, then the database stores the data in the `DBMS_COMPRESSION.COMP_BLOCK` format. In this case, the database applies OLTP compression to the blocks, which reside in a Hybrid Columnar Compression segment.

See Also:

- "Row Locks (TX)"
- *Oracle Database Licensing Information User Manual* to learn about licensing requirements for Hybrid Columnar Compression
- *Oracle Database Administrator’s Guide* to learn how to use Hybrid Columnar Compression
- *Oracle Database SQL Language Reference* for `CREATE TABLE` syntax and semantics
- *Oracle Database PL/SQL Packages and Types Reference* to learn about the `DBMS_COMPRESSION` package

**Parent topic:** Hybrid Columnar Compression

###### DML and Hybrid Columnar Compression

Hybrid Columnar Compression has implications for row locking in different types of DML operations.

Direct Path Loads and Conventional Inserts

When loading data into a table that uses Hybrid Columnar Compression, you can use either conventional inserts or direct path loads. Direct path loads lock the entire table, which reduces concurrency.

Oracle Database 12c Release 2 (12.2) adds support for conventional array inserts into the Hybrid Columnar Compression format. The advantages of conventional array inserts are:

- Inserted rows use row-level locks, which increases concurrency.
- Automatic Data Optimization (ADO) and Heat Map support Hybrid Columnar Compression for row-level policies. Thus, the database can use Hybrid Columnar Compression for eligible blocks even when DML activity occurs on other parts of the segment.

When the application uses conventional array inserts, Oracle Database stores the rows in compression units when the following conditions are met:

- The table is stored in an ASSM tablespace.
- The compatibility level is 12.2.0.1 or later.
- The table definition satisfies the existing Hybrid Columnar Compression table constraints, including no columns of type `LONG`, and no row dependencies.

Conventional inserts generate redo and undo. Thus, compression units created by conventional DML statement are rolled back or committed along with the DML. The database automatically performs index maintenance, just as for rows that are stored in conventional data blocks.

Updates and Deletes

By default, the database locks all rows in the compression unit if an update or delete is applied to any row in the unit. To avoid this issue, you can choose to enable row-level locking for a table. In this case, the database only locks rows that are affected by the update or delete operation.

See Also:

- "Automatic Segment Space Management"
- "Row Locks (TX)"
- *Oracle Database Administrator’s Guide* to learn how to perform conventional inserts
- *Oracle Database SQL Language Reference* to learn about the `INSERT` statement

**Parent topic:** Hybrid Columnar Compression
