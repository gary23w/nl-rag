---
title: "Data control language"
source: https://en.wikipedia.org/wiki/Row-level_security
domain: supabase-platform
license: CC-BY-SA-4.0
tags: supabase platform, supabase postgres, firebase alternative supabase, backend as a service supabase
fetched: 2026-07-02
---

# Data control language

(Redirected from

Row-level security

)

A **data control language** (**DCL**) is a syntax similar to a computer programming language used to control access to data stored in a database (authorization). In particular, it is a component of Structured Query Language (SQL). Data Control Language is one of the logical groups in SQL Commands. SQL is the standard language for relational database management systems. SQL statements are used to perform tasks such as insert data to a database, delete or update data in a database, or retrieve data from a database.

Though database systems use SQL, they also have their own additional proprietary extensions that are usually only used on their system. For example, Microsoft SQL server uses Transact-SQL (T-SQL), which is an extension of SQL. Similarly, Oracle uses PL-SQL, which an Oracle-specific SQL extension. However, the standard SQL commands such as "Select", "Insert", "Update", "Delete", "Create", and "Drop" can be used to accomplish almost everything that one needs to do with a database.

Examples of DCL commands include the SQL commands:

- GRANT to allow specified users to perform specified tasks.
- REVOKE to remove the user accessibility to database object.

The operations for which privileges may be granted to or revoked from a user or role apply to both the Data definition language (DDL) and the Data manipulation language (DML), and may include CONNECT, SELECT, INSERT, UPDATE, DELETE, EXECUTE, and USAGE.

## Microsoft SQL Server

In Microsoft SQL Server there are four groups of SQL commands:

- Data Manipulation Language (DML)
- Data Definition Language (DDL)
- Data Control Language (DCL)
- Transaction Control Language (TCL)

DCL commands are used for access control and permission management for users in the database. With them we can easily allow or deny some actions for users on the tables or records (row level security).

DCL commands are:

**GRANT**

gives specified permissions for the table (and other objects) to, or assigns a specified role with certain permissions to, specified groups or users of a database;

**REVOKE**

takes away specified permissions for the table (and other objects) to, or takes away a specified role with certain permissions to, specified groups or users of a database;

**DENY**

denies a specified permission to a security object.

For example: GRANT can be used to give privileges to user to do SELECT, INSERT, UPDATE and DELETE on a specific table or multiple tables.

The REVOKE command is used to take a privilege away (default) or revoking specific command like UPDATE or DELETE based on requirements.

### Example

```mw
Grant SELECT,INSERT,UPDATE,DELETE on Employees To User1

Revoke INSERT On Employees To User1

Deny Update On Employees to User1
```

In the first example, GRANT gives privileges to user User1 to do SELECT, INSERT, UPDATE and DELETE on the table named Employees.

In the second example, REVOKE removes User1's privileges to use the INSERT command on the table Employees.

DENY is a specific command. We can conclude that every user has a list of privilege which is denied or granted so command DENY is there to explicitly ban you some privileges on the database objects.:

## Oracle Database

Oracle Database divide SQL commands to different types. They are:

- Data Definition Language (DDL) Statements
- Data Manipulation Language (DML) Statements
- Transaction Control Statements
- Session Control Statements
- System Control Statement
- Embedded SQL Statements

For details refer Oracle-TCL

Data definition language (DDL) statements let you perform these tasks:

- Create, alter, and drop schema objects
- Grant and revoke privileges and roles
- Analyze information on a table, index, or cluster
- Establish auditing options
- Add comments to the data dictionary

So Oracle Database DDL commands include the **Grant** and **Revoke** privileges which is actually part of Data control Language in Microsoft SQL server.

### Example

```mw
GRANT SELECT, INSERT, UPDATE, DELETE ON db1.Employee TO user1;

REVOKE SELECT, INSERT, UPDATE, DELETE ON db1.Employee FROM user1;
```

### Transaction Control Statements in Oracle

Transaction control statements manage changes made by DML statements. The transaction control statements are:

- COMMIT
- ROLLBACK
- SAVEPOINT
- SET TRANSACTION
- SET CONSTRAINT

## MySQL

MySQL server they divide SQL statements into different type of statement

- Data Definition Statements
- Data Manipulation Statements
- Transactional and Locking Statements
- Replication Statements
- Prepared Statements
- Compound Statement Syntax
- Database Administration Statements
- Utility Statements
- Account Management Statements

For details refer MySQL Transactional statements

The **Grant** and **Revoke** statements are part of Account Management Statements.

The GRANT statement enables system administrators to grant privileges and roles, which can be granted to user accounts and roles. These syntax restrictions apply:

- GRANT cannot mix granting both privileges and roles in the same statement. A given GRANT statement must grant either privileges or roles.
- The ON clause distinguishes whether the statement grants privileges or roles:
- With ON, the statement grants privileges.
- Without ON, the statement grants roles.
- It is permitted to assign both privileges and roles to an account, but you must use separate GRANT statements, each with syntax appropriate to what is to be granted.

The REVOKE statement enables system administrators to revoke privileges and roles, which can be revoked from user accounts and roles.

### Examples

```mw
REVOKE INSERT ON *.* FROM 'jeffrey'@'localhost';

REVOKE 'role1', 'role2' FROM 'user1'@'localhost', 'user2'@'localhost';

REVOKE SELECT ON world.* FROM 'role3';

GRANT ALL ON db1.* TO 'jeffrey'@'localhost';

GRANT 'role1', 'role2' TO 'user1'@'localhost', 'user2'@'localhost';

GRANT SELECT ON world.* TO 'role3';
```

In PostgreSQL, executing DCL is transactional, and can be rolled back.

**Grant** and **Revoke** are the SQL statements are used to control the privileges given to the users in a Databases.

SQLite does not have any DCL commands as it does not have usernames or logins. Instead, SQLite depends on file-system permissions to define who can open and access a database.
