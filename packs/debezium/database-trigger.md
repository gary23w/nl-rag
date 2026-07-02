---
title: "Database trigger"
source: https://en.wikipedia.org/wiki/Database_trigger
domain: debezium
license: CC-BY-SA-4.0
tags: debezium connector, change data capture, database trigger streaming, kafka connect, write ahead logging
fetched: 2026-07-02
---

# Database trigger

A **database trigger** is procedural code that is automatically executed in response to certain events on a particular table or view in a database. The trigger is mostly used for maintaining the integrity of the information on the database. For example, when a new record (representing a new worker) is added to the employees table, new records should also be created in the tables of the taxes, vacations and salaries. Triggers can also be used to log historical data, for example to keep track of employees' previous salaries.

## Triggers in DBMS

Below follows a series of descriptions of how some common DBMS support triggers.

### Oracle

In addition to triggers that fire (and execute PL/SQL code) when data is modified, Oracle 10g supports triggers that fire when schema-level objects (that is, tables) are modified and when user logon or logoff events occur.

#### Schema-level triggers

- After Creation
- Before Alter
- After Alter
- Before Drop
- After Drop
- Before Insert

The four main types of triggers are:

1. Row-level trigger: This gets executed before or after *any column value of a row* changes.
2. Column-level trigger: This gets executed before or after the *specified column* changes.
3. For each row type: This trigger gets executed once for each row of the result set affected by an insert/update/delete.
4. For each statement type: This trigger gets executed only once for the entire result set, but also fires each time the statement is executed.

#### System-level triggers

From Oracle 8i, database events - logons, logoffs, startups - can fire Oracle triggers.

### Microsoft SQL Server

MS SQL Server supports trigger for DML and DDL statement plus special trigger "logon".

The scope of DDL triggers can be a database (CREATE TRIGGER name ON DATABASE ...) or the entire SQL Server instance (CREATE TRIGGER name ON ALL SERVER). When you use the entire instance, you can capture all events executed on commands that have server-level scope as well as any commands that have database-level scope in the SQL instance.

A list of all available firing events in Microsoft SQL Server for DDL triggers is available on Microsoft Docs.

Performing conditional actions in DML triggers (or testing data following modification) is done through accessing the pseudo tables (temporary ones) Inserted and Deleted tables. DML trigger are always "FOR EACH STATEMENT" but can be code at row event ("FOR EACH ROW") using a cursor on the inserted/deleted pseudo tables.

### PostgreSQL

Introduced support for triggers in 1997. The following functionality in SQL:2003 was previously not implemented in PostgreSQL:

- SQL allows triggers to fire on updates to specific columns; As of version 9.0 of PostgreSQL this feature is also implemented in PostgreSQL.
- The standard allows the execution of a number of SQL statements other than SELECT, INSERT, UPDATE, such as CREATE TABLE as the triggered action. This can be done through creating a stored procedure or function to call CREATE TABLE.

Synopsis:

```mw
CREATE TRIGGER name { BEFORE | AFTER } { event [ OR ... ] }
    ON TABLE [ FOR [ EACH ] { ROW | STATEMENT } ]
    EXECUTE PROCEDURE funcname ( arguments )
```

### Firebird

Firebird supports multiple row-level, BEFORE or AFTER, INSERT, UPDATE, DELETE (or any combination of thereof) triggers per table, where they are always "in addition to" the default table changes, and the order of the triggers relative to each other can be specified where it would otherwise be ambiguous (POSITION clause.) Triggers may also exist on views, where they are always "instead of" triggers, replacing the default updatable view logic. (Before version 2.1, triggers on views deemed updatable would run in addition to the default logic.)

Firebird does not raise mutating table exceptions (like Oracle), and triggers will by default both nest and recurse as required (SQL Server allows nesting but not recursion, by default.) Firebird's triggers use NEW and OLD context variables (not Inserted and Deleted tables,) and provide UPDATING, INSERTING, and DELETING flags to indicate the current usage of the trigger.

```mw
{CREATE | RECREATE | CREATE OR ALTER} TRIGGER name FOR {table name | view name}
 [ACTIVE | INACTIVE]
 {BEFORE | AFTER}
 {INSERT [OR UPDATE] [OR DELETE] | UPDATE [OR INSERT] [OR DELETE] | DELETE [OR UPDATE] [OR INSERT] }
 [POSITION n] AS
BEGIN
 ....
END
```

As of version 2.1, Firebird additionally supports the following database-level triggers:

- CONNECT (exceptions raised here prevent the connection from completing)
- DISCONNECT
- TRANSACTION START
- TRANSACTION COMMIT (exceptions raised here prevent the transaction from committing, or preparing if a two-phase commit is involved)
- TRANSACTION ROLLBACK

Database-level triggers can help enforce multi-table constraints, or emulate materialized views. If an exception is raised in a TRANSACTION COMMIT trigger, the changes made by the trigger so far are rolled back and the client application is notified, but the transaction remains active as if COMMIT had never been requested; the client application can continue to make changes and re-request COMMIT.

Syntax for database triggers:

```mw
{CREATE | RECREATE | CREATE OR ALTER} TRIGGER name
 [ACTIVE | INACTIVE] ON
 {CONNECT | DISCONNECT | TRANSACTION START | TRANSACTION COMMIT | TRANSACTION ROLLBACK}
 [POSITION n] AS
BEGIN
 .....
END
```

### MySQL/MariaDB

Limited support for triggers in the MySQL/MariaDB DBMS was added in the 5.0 version of MySQL, launched in 2005.

As of version 8.0, they allow for DDL (Data Definition Language) triggers and for DML (Data Manipulation Language) triggers. They also allow either type of DDL trigger (AFTER or BEFORE) to be used to define triggers. They are created by using the clause *CREATE TRIGGER* and deleted by using the clause *DROP TRIGGER*. The statement called upon an event happens is defined after the clause *FOR EACH ROW*, followed by a keyword (*SET* or *BEGIN*), which indicates whether what follows is an expression or a statement respectively.

### IBM DB2 LUW

IBM DB2 for distributed systems known as DB2 for LUW (LUW means **L**inux, **U**nix, **W**indows) supports three trigger types: Before trigger, After trigger and Instead of trigger. Both statement level and row level triggers are supported. If there are more triggers for same operation on table then firing order is determined by trigger creation data. Since version 9.7 IBM DB2 supports autonomous transactions.

Before trigger is for checking data and deciding if operation should be permitted. If exception is thrown from before trigger then operation is aborted and no data are changed. In DB2 before triggers are read only — you can't modify data in before triggers. After triggers are designed for post processing after requested change was performed. After triggers can write data into tables and unlike some other databases you can write into any table including table on which trigger operates. Instead of triggers are for making views writeable.

Triggers are usually programmed in SQL PL language.

### SQLite

```mw
CREATE [TEMP | TEMPORARY] TRIGGER [IF NOT EXISTS] [database_name .] trigger_name
[BEFORE | AFTER | INSTEAD OF] {DELETE | INSERT | UPDATE [OF column_name [, column_name]...]} 
ON {table_name | view_name}
   [FOR EACH ROW] [WHEN condition is mandatory ]
BEGIN
   ...
END
```

SQLite only supports row-level triggers, not statement-level triggers.

Updateable views, which are not supported in SQLite, can be emulated with INSTEAD OF triggers.

### XML databases

An example of implementation of triggers in non-relational database can be Sedna, that provides support for triggers based on XQuery. Triggers in Sedna were designed to be analogous to SQL:2003 triggers, but natively base on XML query and update languages (XPath, XQuery and XML update language).

A trigger in Sedna is set on any nodes of an XML document stored in database. When these nodes are updated, the trigger automatically executes XQuery queries and updates specified in its body. For example, the following trigger cancels person node deletion if there are any open auctions referenced by this person:

```mw
CREATE TRIGGER "trigger3"
    BEFORE DELETE
    ON doc("auction")/site//person
    FOR EACH NODE
    DO
    {
        if (exists($WHERE//open_auction/bidder/personref/@person=$OLD/@id))
        then ( )
        else $OLD;
    }
```

## Row and statement level triggers

To understand how trigger behavior works, you need to be aware of the two main types of triggers; these are Row and Statement level triggers. The distinction between the two is how many times the code within the trigger is executed, and at what time.

Suppose you have a trigger that is made to be called on an UPDATE to a certain table. Row level triggers would execute once for each row that is affected by the UPDATE. If no rows are affected by the UPDATE command, the trigger **will not** execute any code within the trigger. Statement level triggers will be called once **regardless** of how many rows are affected by the UPDATE. Even if the UPDATE command didn't affect any rows, the code within the trigger will still be executed once.

Using the BEFORE and AFTER options determine when the trigger is called. Suppose you have a trigger that is called on an INSERT to a certain table. If your trigger is using the BEFORE option, the code within the trigger will be executed before the INSERT into the table occurs. A common use of the BEFORE trigger is to verify the input values of the INSERT, or modify the values accordingly. Now let's say we have a trigger that uses AFTER instead. The code within the trigger is executed after the INSERT happens to the table. An example use of this trigger is creating an audit history of who has made inserts into the database, keeping track of the changes made. When using these options you need to keep a few things in mind. The BEFORE option does **not allow** you to modify tables, that is why input validation is a practical use. Using AFTER triggers allows you to modify tables such as inserting into an audit history table.

When creating a trigger to determine if it is statement or row level simply include the FOR EACH ROW clause for a row level, or omit the clause for a statement level. Be cautious of using additional INSERT/UPDATE/DELETE commands within your trigger, because trigger recursion is possible, causing unwanted behavior. In the examples below each trigger is modifying a different table, by looking at what is being modified you can see some common applications of when different trigger types are used.

The following is an Oracle syntax example of a row level trigger that is called AFTER an update FOR EACH ROW affected. This trigger is called on an update to a phone book database. When the trigger is called it adds an entry into a separate table named phone_book_audit. Also take note of triggers being able to take advantage of schema objects like sequences, in this example audit_id_sequence.nexVal is used to generate unique primary keys in the phone_book_audit table.

```mw
CREATE OR REPLACE TRIGGER phone_book_audit
  AFTER UPDATE ON phone_book FOR EACH ROW
BEGIN
  INSERT INTO phone_book_audit 
    (audit_id,audit_change, audit_l_name, audit_f_name, audit_old_phone_number, audit_new_phone_number, audit_date) 
    VALUES
    (audit_id_sequence.nextVal,'Update', :OLD.last_name, :OLD.first_name, :OLD.phone_number, :NEW.phone_number, SYSDATE);
END;
```

Now calling an UPDATE on the phone_book table for people with the last name 'Jones'.

```mw
UPDATE phone_book SET phone_number = '111-111-1111' WHERE last_name = 'Jones';
```

| Audit_ID | Audit_Change | F_Name | L_Name | New_Phone_Number | Old_Phone_Number | Audit_Date |
|---|---|---|---|---|---|---|
| 1 | Update | Jordan | Jones | 111-111-1111 | 098-765-4321 | 02-MAY-14 |
| 2 | Update | Megan | Jones | 111-111-1111 | 111-222-3456 | 02-MAY-14 |

Notice that the phone_number_audit table is now populated with two entries. This is due to the database having two entries with the last name of 'Jones'. Since the update modified two separate row values, the created trigger was called twice; once after each modification.

### After - statement-level trigger

An Oracle syntax statement trigger that is called after an UPDATE to the phone_book table. When the trigger gets called it makes an insert into phone_book_edit_history table

```mw
CREATE OR REPLACE TRIGGER phone_book_history
  AFTER UPDATE ON phone_book
BEGIN
  INSERT INTO phone_book_edit_history 
    (audit_history_id, username, modification, edit_date) 
    VALUES
    (audit_history_id_sequence.nextVal, USER,'Update', SYSDATE);
END;
```

Now doing exactly the same update as the above example, however this time with a statement level trigger.

```mw
UPDATE phone_book SET phone_number = '111-111-1111' WHERE last_name = 'Jones';
```

| Audit_History_ID | Username | Modification | Edit_Date |
|---|---|---|---|
| 1 | HAUSCHBC | Update | 02-MAY-14 |

The result shows that the trigger was only called once, even though the update did change two rows.

### Before each - row-level trigger

This example demonstrates a BEFORE EACH ROW trigger that modifies the INSERT using a WHEN conditional. If the last name is larger than 10 letters, using the SUBSTR function we change the last_name column value to an abbreviation.

```mw
CREATE OR REPLACE TRIGGER phone_book_insert
  BEFORE INSERT ON phone_book FOR EACH ROW
  WHEN (LENGTH(new.last_name) > 10)
BEGIN
    :new.last_name := SUBSTR(:new.last_name,0,1);
END;
```

Now performing an INSERT of someone with a large name.

```mw
INSERT INTO phone_book VALUES
(6, 'VeryVeryLongLastName', 'Erin', 'Minneapolis', 'MN', '989 University Drive', '123-222-4456', 55408, TO_DATE('11/21/1991', 'MM/DD/YYYY'));
```

Person_ID

Last_Name

First_Name

City

State_Abbreviation

Address

Phone_Number

Zip_code

DOB

6

V

Erin

Minneapolis

MN

989 University Drive

123-222-4456

55408

21-NOV-91

The trigger worked as per the result above, modifying the value of the INSERT **before** it was executed.

### Before - statement-level trigger

Using a BEFORE statement trigger is particularly useful when enforcing database restrictions. This example demonstrate how to enforce a restriction upon someone named "SOMEUSER" on the table phone_book.

```mw
CREATE OR REPLACE TRIGGER hauschbc 
  BEFORE INSERT ON SOMEUSER.phone_book
BEGIN
    RAISE_APPLICATION_ERROR (
         num => -20050,
         msg => 'Error message goes here.');
END;
```

Now, when "SOMEUSER" is logged in after attempting any INSERT this error message will show:

```
SQL Error: ORA-20050: Error message goes here.
```

Custom errors such as this one has a restriction on what the num variable can be defined as. Because of the numerous other pre-defined errors this variable must be in the range of −20000 to −20999.
