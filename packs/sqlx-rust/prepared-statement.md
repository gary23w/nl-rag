---
title: "Prepared statement"
source: https://en.wikipedia.org/wiki/Prepared_statement
domain: sqlx-rust
license: CC-BY-SA-4.0
tags: sqlx rust, rust async database, compile-time sql rust, sqlx query macro
fetched: 2026-07-02
---

# Prepared statement

In database management systems (DBMS), a **prepared statement**, **parameterized statement**, (not to be confused with **parameterized query**) is a feature where the database pre-compiles SQL code and stores the results, separating it from data. Benefits of prepared statements are:

- efficiency, because they can be used repeatedly without re-compiling
- security, by reducing or eliminating SQL injection attacks

A prepared statement takes the form of a pre-compiled template into which constant values are substituted during each execution, and typically use SQL DML statements such as INSERT, SELECT, or UPDATE.

A common workflow for prepared statements is:

1. **Prepare**: The application creates the statement template and sends it to the DBMS. Certain values are left unspecified, called *parameters*, *placeholders* or *bind variables* (labelled "?" below): `INSERT INTO products (name, price) VALUES (?, ?);`
2. **Compile**: The DBMS compiles (parses, optimizes and translates) the statement template, and stores the result without executing it.
3. **Execute**: The application supplies (or *binds*) values for the parameters of the statement template, and the DBMS executes the statement (possibly returning a result). The application may request the DBMS to execute the statement many times with different values. In the above example, the application might supply the values "bike" for the first parameter and "10900" for the second parameter, and then later the values "shoes" and "7400".

The alternative to a prepared statement is calling SQL directly from the application source code in a way that combines code and data. The direct equivalent to the above example is:

```mw
INSERT INTO products (name, price) VALUES ('bike', '10900');
```

Not all optimization can be performed at the time the statement template is compiled, for two reasons: the best plan may depend on the specific values of the parameters, and the best plan may change as tables and indexes change over time.

On the other hand, if a query is executed only once, server-side prepared statements can be slower because of the additional round-trip to the server. Implementation limitations may also lead to performance penalties; for example, some versions of MySQL did not cache results of prepared queries. A stored procedure, which is also precompiled and stored on the server for later execution, has similar advantages. Unlike a stored procedure, a prepared statement is not normally written in a procedural language and cannot use or modify variables or use control flow structures, relying instead on the declarative database query language. Due to their simplicity and client-side emulation, prepared statements are more portable across vendors.

## Software support

Major DBMSs, including SQLite, MySQL, Oracle, IBM Db2, Microsoft SQL Server and PostgreSQL support prepared statements. Prepared statements are normally executed through a non-SQL binary protocol for efficiency and protection from SQL injection, but with some DBMSs such as MySQL prepared statements are also available using a SQL syntax for debugging purposes.

A number of programming languages support prepared statements in their standard libraries and will emulate them on the client side even if the underlying DBMS does not support them, including Java's JDBC, Perl's DBI, PHP's PDO and Python's DB-API. Client-side emulation can be faster for queries which are executed only once, by reducing the number of round trips to the server, but is usually slower for queries executed many times. It resists SQL injection attacks equally effectively.

Many types of SQL injection attacks can be eliminated by *disabling literals*, effectively requiring the use of prepared statements; as of 2007 only H2 supports this feature.

## Examples

### C++

In C++ MySQL Connector/C++ X DevAPI, preparation is done implicitly using the library's API.

```mw
import <mysqlx/xdevapi.h>
import std;

using mysqlx::Schema;
using mysqlx::Session;
using mysqlx::Table;

int main() {
    try {
        Session session("localhost", 33060, "user", "password");
        Schema db = session.getSchema("testdb");
        Table users = db.getTable("users");

        users.insert("name", "age")
            .values("Alice", 30)
            .execute();
    } catch (const mysqlx::Error& e) {
        std::println(stderr, "MySQL error: {}", e.what());
    }
}
```

### C# ADO.NET

This example uses C# and ADO.NET:

```mw
namespace Wikipedia.Examples;

using System;
using System.Data;

using Microsoft.Data.SqlClient;

public class Example
{
    static void Main(string[] args)
    {
        using (SqlCommand command = connection.CreateCommand())
        {
            command.CommandText = "SELECT * FROM users WHERE USERNAME = @username AND ROOM = @room";
            command.Parameters.AddWithValue("@username", username);
            command.Parameters.AddWithValue("@room", room);

            using (SqlDataReader dataReader = command.ExecuteReader())
            {
                // ...
            }
        }
    }
}
```

ADO.NET `SqlCommand` will accept any type for the `value` parameter of `AddWithValue`, and type conversion occurs automatically. Note the use of "named parameters" (i.e. `"@username"`) rather than `"?"`—this allows you to use a parameter multiple times and in any arbitrary order within the query command text.

However, the AddWithValue method should not be used with variable length data types, like varchar and nvarchar. This is because .NET assumes the length of the parameter to be the length of the given value, rather than getting the actual length from the database via reflection. The consequence of this is that a different query plan is compiled and stored for each different length. In general, the maximum number of "duplicate" plans is the product of the lengths of the variable length columns as specified in the database. For this reason, it is important to use the standard Add method for variable length columns:

`command.Parameters.Add(ParamName, VarChar, ParamLength).Value = ParamValue`, where ParamLength is the length as specified in the database.

Since the standard Add method needs to be used for variable length data types, it is a good habit to use it for all parameter types.

### Go

```mw
// Define a BookModel type which wraps a sql.DB connection pool.
type BookModel struct {
	DB *sql.DB
}

// This will insert a new book into the database.
func (m *BookModel) Insert(title, author string) (int, error) {
	stmt := "INSERT INTO book (title, author, created) VALUES(?, ?, UTC_TIMESTAMP())"
    
    // The "Exec" function will automatically prepare the statement for you,
    // which requires an additional round-trip to the database.
    //
    // It is possible to avoid prepared statements, if you are sure they are not needed.
    // See ExecerContext for details. https://pkg.go.dev/database/sql/driver#ExecerContext
    //
    // Other functions such as "Query" work the same way,
    // and have an equivalent interface.
	result, err := m.DB.Exec(stmt, title, author)
	if err != nil {
		return 0, err
	}

	id, err := result.LastInsertId() // Not supported in the Postgres driver -- use RETURNING instead.
	if err != nil {
		return 0, err
	}

	// The ID returned has the type int64, so we convert it to an int type
	// before returning.
    //
    // Keep in mind, on 32-bit machines, this can potentially truncate the value.
    // It is usually more safe to return int64 from your function directly,
    // which is still supported on 32-bit machines.
	return int(id), nil
}
```

The placeholder parameter syntax differs depending on your database. MySQL, SQL Server and SQLite use the ? notation, but PostgreSQL uses the $N notation. For example, if you were using PostgreSQL instead you would write:

```mw
_, err := m.DB.Exec("INSERT INTO ... VALUES ($1, $2, $3)", ...)
```

### Java JDBC

This example uses Java and JDBC:

```mw
package org.wikipedia.examples;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import com.mysql.jdbc.jdbc2.optional.MysqlDataSource;

public class Main {

    public static void main(String[] args) throws SQLException {
        MysqlDataSource ds = new MysqlDataSource();
        ds.setDatabaseName("mysql");
        ds.setUser("root");

        try (Connection conn = ds.getConnection()) {
            try (Statement stmt = conn.createStatement()) {
                stmt.executeUpdate("CREATE TABLE IF NOT EXISTS products (name VARCHAR(40), price INT)");
            }

            try (PreparedStatement stmt = conn.prepareStatement("INSERT INTO products VALUES (?, ?)")) {
                stmt.setString(1, "bike");
                stmt.setInt(2, 10900);
                stmt.executeUpdate();
                stmt.setString(1, "shoes");
                stmt.setInt(2, 7400);
                stmt.executeUpdate();
                stmt.setString(1, "phone");
                stmt.setInt(2, 29500);
                stmt.executeUpdate();
            }

            try (PreparedStatement stmt = conn.prepareStatement("SELECT * FROM products WHERE name = ?")) {
                stmt.setString(1, "shoes");
                ResultSet rs = stmt.executeQuery();
                rs.next();
                System.out.println(rs.getInt(2));
            }
        }
    }
}
```

Java `PreparedStatement` provides "setters" (`setInt(int), setString(String), setDouble(double),` etc.) for all major built-in data types.

### PHP PDO

This example uses PHP and PDO:

```mw
<?php

// Connect to a database named "mysql", with the password "root"
$connection = new PDO('mysql:host=127.0.0.1;dbname=test;charset=utf8mb4', 'root');

// Execute a request on the connection, which will create
// a table "products" with two columns, "name" and "price"
$connection->exec('CREATE TABLE IF NOT EXISTS products (name VARCHAR(40), price INT)');

// Prepare a query to insert multiple products into the table
$statement = $connection->prepare('INSERT INTO products VALUES (?, ?)');
$products  = [
    ['bike', 10900],
    ['shoes', 7400],
    ['phone', 29500],
];

// Iterate through the products in the "products" array, and
// execute the prepared statement for each product
foreach ($products as $product) {
    $statement->execute($product);
}

// Prepare a new statement with a named parameter
$statement = $connection->prepare('SELECT * FROM products WHERE name = :name');
$statement->execute([
    ':name' => 'shoes',
]);

// Use array destructuring to assign the product name and its price
// to corresponding variables
[ $product, $price ] = $statement->fetch();

// Display the result to the user
echo "The price of the product {$product} is \${$price}.";
```

### Perl DBI

This example uses Perl and DBI:

```mw
#!/usr/bin/env perl -w
use strict;
use DBI;

my ($db_name, $db_user, $db_password) = ('my_database', 'moi', 'Passw0rD');
my $dbh = DBI->connect("DBI:mysql:database=$db_name", $db_user, $db_password,
    { RaiseError => 1, AutoCommit => 1})
    or die "ERROR (main:DBI->connect) while connecting to database $db_name: " .
        $DBI::errstr . "\n";

$dbh->do('CREATE TABLE IF NOT EXISTS products (name VARCHAR(40), price INT)');

my $sth = $dbh->prepare('INSERT INTO products VALUES (?, ?)');
$sth->execute(@$_) foreach ['bike', 10900], ['shoes', 7400], ['phone', 29500];

$sth = $dbh->prepare("SELECT * FROM products WHERE name = ?");
$sth->execute('shoes');
print "$$_[1]\n" foreach $sth->fetchrow_arrayref;
$sth->finish;

$dbh->disconnect;
```

### Python DB-API

This example uses Python and DB-API:

```mw
import mysql.connector

with mysql.connector.connect(database="mysql", user="root") as conn:
    with conn.cursor(prepared=True) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS products (name VARCHAR(40), price INT)")
        params: list[tuple[str, int]] = [("bike", 10900), ("shoes", 7400), ("phone", 29500)]
        cursor.executemany("INSERT INTO products VALUES (%s, %s)", params)
        params = ("shoes",)
        cursor.execute("SELECT * FROM products WHERE name = %s", params)
        print(cursor.fetchall()[0][1])
```

### Magic Direct SQL

This example uses Direct SQL from Fourth generation language like eDeveloper, uniPaaS and magic XPA from Magic Software Enterprises

```mw
Virtual username  Alpha 20   init: 'sister'
Virtual password  Alpha 20   init: 'yellow'

SQL Command:   SELECT * FROM users WHERE USERNAME=:1 AND PASSWORD=:2

Input Arguments: 
1:  username
2:  password
```

### PureBasic

PureBasic (since v5.40 LTS) can manage 7 types of link with the following commands

```
SetDatabaseBlob, SetDatabaseDouble, SetDatabaseFloat, SetDatabaseLong, SetDatabaseNull, SetDatabaseQuad, SetDatabaseString
```

There are 2 different methods depending on the type of database

For **SQLite**, **ODBC**, **MariaDB/Mysql** use: ?

```mw
SetDatabaseString(#Database, 0, "test")  
If DatabaseQuery(#Database, "SELECT * FROM employee WHERE id=?")    
  ; ...
EndIf
```

For **PostgreSQL** use: $1, $2, $3, ...

```mw
SetDatabaseString(#Database, 0, "Smith") ; -> $1 
SetDatabaseString(#Database, 1, "Yes")   ; -> $2
SetDatabaseLong  (#Database, 2, 50)      ; -> $3

If DatabaseQuery(#Database, "SELECT * FROM employee WHERE id=$1 AND active=$2 AND years>$3")    
  ; ...
EndIf
```
