---
title: "Active record pattern"
source: https://en.wikipedia.org/wiki/Active_record_pattern
domain: masonite-python
license: CC-BY-SA-4.0
tags: masonite python framework, developer friendly python, python web framework, masonite service container
fetched: 2026-07-02
---

# Active record pattern

In software engineering, the **active record pattern** is an architectural pattern. It is found in software that stores in-memory object data in relational databases. It was named by Martin Fowler in his 2003 book *Patterns of Enterprise Application Architecture*. The interface of an object conforming to this pattern would include functions such as Insert, Update, and Delete, plus properties that correspond more or less directly to the columns in the underlying database table.

The Active Record pattern is a Data Access Layer that performs bidirectional transfer of data between a persistent data store (often a relational database) and an in-memory data representation (the domain layer). A database table or view is wrapped into a class. Thus, an object instance is tied to a single row in the table. After creation of an object, a new row is added to the table upon save. Any object loaded gets its information from the database. When an object is updated, the corresponding row in the table is also updated. The wrapper class implements accessor methods or properties for each column in the table or view.

This pattern is commonly used by object persistence tools and in object–relational mapping (ORM). Typically, foreign key relationships will be exposed as an object instance of the appropriate type via a property.

## Implementations

Implementations of the concept can be found in various frameworks for many programming environments. For example, if there is a table `parts` in a database with columns `name` (string type) and `price` (number type), and the Active Record pattern is implemented in the class `Part`, the pseudo-code

```mw
Part part = new Part("Sample part", 123.45);
```

will create a new row in the `parts` table with the given values, and is roughly equivalent to the SQL command

```mw
INSERT INTO parts (name, price) VALUES ('Sample part', 123.45);
```

Conversely, the class can be used to query the database:

```mw
Part b = parts.stream()
    .filter(p -> "gearbox".equals(p.getName()))
    .findFirst()
    .orElse(null);
```

This will find a new `Part` object based on the first matching row from the `parts` table whose `name` column has the value "gearbox". The SQL command used might be similar to the following, depending on the SQL implementation details of the database:

```mw
SELECT * FROM parts WHERE name = 'gearbox' LIMIT 1; -- MySQL or PostgreSQL
```

Various libraries implement an active record pattern framework, such as POCO C++ Libraries in library `Poco::ActiveRecord`.

## Example

This is a simple example of an active record object `User`, in Java. Here the `User` class is both the model and data access object and provides `save()`, `find()`, and `delete()` methods.

```mw
package org.wikipedia.examples;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class User {
    private int id;
    private String name;
    private String email;

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void save() {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password")) {
            if (this.id == 0) {
                String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
                try (PreparedStatement stmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
                    stmt.setString(1, this.name);
                    stmt.setString(2, this.email);
                    stmt.executeUpdate();
                    ResultSet rs = stmt.getGeneratedKeys();
                    if (rs.next()) {
                        this.id = rs.getInt(1);
                    }
                }
            } else {
                String sql = "UPDATE users SET name = ?, email = ? WHERE id = ?";
                try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                    stmt.setString(1, this.name);
                    stmt.setString(2, this.email);
                    stmt.setInt(3, this.id);
                    stmt.executeUpdate();
                }
            }
        } catch (SQLException e) {
            System.err.printf("A SQLException occurred: %s%n", e.getMessage());
            e.printStackTrace();
        }
    }

    public static User find(int id) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password")) {
            String sql = "SELECT * FROM users WHERE id = ?";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setInt(1, id);
                ResultSet rs = stmt.executeQuery();
                if (rs.next()) {
                    User user = new User(rs.getString("name"), rs.getString("email"));
                    user.setId(rs.getInt("id"));
                    return user;
                }
            }
        } catch (SQLException e) {
            System.err.printf("A SQLException occurred: %s%n", e.getMessage());
            e.printStackTrace();
        }
        return null;
    }

    public void delete() {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password")) {
            String sql = "DELETE FROM users WHERE id = ?";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setInt(1, this.id);
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            System.err.printf("A SQLException occurred: %s%n", e.getMessage());
            e.printStackTrace();
        }
    }
}
```

## Criticism

### Single responsibility principle and separation of concerns

Another critique of the active record pattern is that, due to the strong coupling of database interaction and application logic, an active record object does not follow the single responsibility principle and separation of concerns. This is opposed to multitier architecture, which properly addresses these practices. Because of this, the active record pattern is best and most often employed in simple applications that are all forms-over-data with CRUD functionality, or only as one part of an architecture. Typically that part is data access and why several ORMs implement the active record pattern.
