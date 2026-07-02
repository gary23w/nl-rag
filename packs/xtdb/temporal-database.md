---
title: "Temporal database"
source: https://en.wikipedia.org/wiki/Temporal_database
domain: xtdb
license: CC-BY-SA-4.0
tags: xtdb database, bitemporal database, datalog query, immutable database
fetched: 2026-07-02
---

# Temporal database

A **temporal database** stores data relating to time instances. It offers temporal data types and stores information relating to past, present and future time. Temporal databases can be uni-temporal, bi-temporal or tri-temporal.

More specifically the temporal aspects usually include valid time, transaction time and/or decision time.

- **Valid time** is the time period during or event time at which a fact is true in the real world.
- **Transaction time** is the time at which a fact was recorded in the database.
- **Decision time** is the time at which the decision was made about the fact. Used to keep a history of decisions about valid times.

## Types

### Uni-temporal

A uni-temporal database has one axis of time, either the validity range or the system time range.

### Bi-temporal

A bi-temporal database has two axes of time:

- Valid time
- Transaction time or decision time

### Tri-temporal

A tri-temporal database has three axes of time:

- Valid time
- Transaction time
- Decision time

This approach introduces additional complexities.

Temporal databases are in contrast to current databases (not to be confused with currently available databases), which store only facts which are believed to be true at the current time.

## Features

Temporal databases support managing and accessing temporal data by providing one or more of the following features:

- A time period datatype, including the ability to represent time periods with no end (infinity or forever)
- The ability to define valid and transaction time period attributes and bitemporal relations
- System-maintained transaction time
- Temporal primary keys, including non-overlapping period constraints
- Temporal constraints, including non-overlapping uniqueness and referential integrity
- Update and deletion of temporal records with automatic splitting and coalescing of time periods
- Temporal queries at current time, time points in the past or future, or over durations
- Predicates for querying time periods, often based on Allen's interval relations

## History

With the development of SQL and its attendant use in real-life applications, database users realized that when they added date columns to key fields, some issues arose. For example, if a table has a primary key and some attributes, adding a date to the primary key to track historical changes can lead to creation of more rows than intended. Deletes must also be handled differently when rows are tracked in this way. In 1992, this issue was recognized but standard database theory was not yet up to resolving this issue, and neither was the then-newly formalized SQL-92 standard.

Richard Snodgrass proposed in 1992 that temporal extensions to SQL be developed by the temporal database community. In response to this proposal, a committee was formed to design extensions to the 1992 edition of the SQL standard (ANSI X3.135.-1992 and ISO/IEC 9075:1992); those extensions, known as TSQL2, were developed during 1993 by this committee. In late 1993, Snodgrass presented this work to the group responsible for the American National Standard for Database Language SQL, ANSI Technical Committee X3H2 (now known as NCITS H2). The preliminary language specification appeared in the March 1994 ACM SIGMOD Record. Based on responses to that specification, changes were made to the language, and the definitive version of the TSQL2 Language Specification was published in September, 1994

An attempt was made to incorporate parts of TSQL2 into the new SQL standard SQL:1999, called SQL3. Parts of TSQL2 were included in a new substandard of SQL3, ISO/IEC 9075-7, called SQL/Temporal. The TSQL2 approach was heavily criticized by Chris Date and Hugh Darwen. The ISO project responsible for temporal support was canceled near the end of 2001.

As of December 2011, ISO/IEC 9075, Database Language SQL:2011 Part 2: SQL/Foundation included clauses in table definitions to define "application-time period tables" (valid time tables), "system-versioned tables" (transaction time tables) and "system-versioned application-time period tables" (bitemporal tables). A substantive difference between the TSQL2 proposal and what was adopted in SQL:2011 is that there are no hidden columns in the SQL:2011 treatment, nor does it have a new data type for intervals; instead two columns with datestamps (DS) or date-timestamps (DTS) can be bound together using a `PERIOD FOR` declaration. Another difference is replacement of the controversial (prefix) statement modifiers from TSQL2 with a set of temporal predicates.

Other features of SQL:2011 standard related to temporal databases are automatic time period splitting, temporal primary keys, temporal referential integrity, temporal predicates with Allen's interval algebra and time-sliced and sequenced queries.

## Example

For illustration, consider the following short biography of a fictional man, John Doe:

John Doe was born on 1975-04-03 in the Kids Hospital of Medicine County, as son of Jack Doe and Jane Doe who lived in Smallville. Jack Doe proudly registered the birth of his first-born on April 4, 1975 at the Smallville City Hall. John grew up as a joyful boy, turned out to be a brilliant student and graduated with honors in 1993. After graduation, he went to live on his own in Bigtown. Although he moved out on 1994-08-26, he forgot to register the change of address officially. It was only at the turn of the seasons that his mother reminded him that he had to register, which he did a few days later on 1994-12-27. Although John had a promising future, his story ends tragically. John Doe was accidentally hit by a truck on 2001-04-01. The coroner reported his date of death on the very same day.

### Using a non-temporal database

To store the life of John Doe in a current (non-temporal) database we use a table `person (name, address)`. (In order to simplify, `name` is defined as the primary key of `person`.)

John's father officially reported his birth on 1975-04-04. On this date a Smallville official inserted the following entry in the database: `Person(John Doe, Smallville)`. Note that the date itself is not stored in the database.

After graduation, John moves out, but forgets to register his new address. John's entry in the database is not changed until 1994-12-27, when he finally reports it. A Bigtown official updates his address in the database. The `person` table now contains `Person(John Doe, Bigtown)`. Note that the information of John living in Smallville has been overwritten, so it is no longer possible to retrieve that information from the database. An official accessing the database on 1994-12-28, would be told that John lives in Bigtown. More technically: if a database administrator ran the query `SELECT ADDRESS FROM PERSON WHERE NAME='John Doe'` on 1994-12-26, the result would be `Smallville`. Running the same query 2 days later would result in `Bigtown`.

Until his death, the database would state that he lived in Bigtown. On 2001-04-01, the coroner deletes the John Doe entry from the database. After this, running the above query would return no result at all.

| Date | Real world event | Database action | What the database shows |
|---|---|---|---|
| 1975-04-03 | John is born | Nothing | There is no person called John Doe |
| 1975-04-04 | John's father officially reports John's birth | Inserted:Person(John Doe, Smallville) | John Doe lives in Smallville |
| 1994-08-26 | After graduation, John moves to Bigtown, but forgets to register his new address | Nothing | John Doe lives in Smallville |
| 1994-12-26 | Nothing | Nothing | John Doe lives in Smallville |
| 1994-12-27 | John registers his new address | Updated:Person(John Doe, Bigtown) | John Doe lives in Bigtown |
| 2001-04-01 | John dies | Deleted:Person(John Doe) | There is no person called John Doe |

### Using a single axis: valid time or transaction time

Valid time is the time for which a fact is true in the real world. A valid time period may be in the past, span the current time, or occur in the future.

For the example above, to record valid time, the `person` table has two fields added, `valid_from` and `valid_to`. These specify the period when a person's address is valid in the real world. On 1975-04-04, John's father registered his son's birth. An official then inserts a new entry into the database stating that John lives in Smallville from April 3. Note that although the data was inserted on the fourth, the database states that the information is valid since the third. The official does not yet know if or when John will move to another place, so the `valid_to` field is set to infinity (∞). The entry in the database is:

| Name | City | Valid from | Valid to |
|---|---|---|---|
| John Doe | Smallville | 1975-04-03 | ∞ |

On 1994-12-27, John reports his new address in Bigtown where he has been living since 1994-08-26. A new database entry is made to record this fact:

| Name | City | Valid from | Valid to |
|---|---|---|---|
| John Doe | Bigtown | 1994-08-26 | ∞ |

The original entry `Person (John Doe, Smallville, 1975-04-03, ∞)` is not deleted, but has the `valid_to` attribute updated to reflect that it is now known that John stopped living in Smallville on 1994-08-26. The database now contains two entries for John Doe:

| Name | City | Valid from | Valid to |
|---|---|---|---|
| John Doe | Smallville | 1975-04-03 | 1994-08-26 |
| John Doe | Bigtown | 1994-08-26 | ∞ |

When John dies his current entry in the database is updated stating that John does not live in Bigtown any longer. The database now looks like this:

| Name | City | Valid from | Valid to |
|---|---|---|---|
| John Doe | Smallville | 1975-04-03 | 1994-08-26 |
| John Doe | Bigtown | 1994-08-26 | 2001-04-01 |

### Using two axes: valid time and transaction time

Transaction time records the time period during which a database entry is accepted as correct. This enables queries that show the state of the database at a given time. Transaction time periods can only occur in the past or up to the current time. In a transaction time table, records are never deleted. Only new records can be inserted, and existing ones updated by setting their transaction end time to show that they are no longer current.

To enable transaction time in the example above, two more fields are added to the Person table: `transaction_from` and `transaction_to`. Here, `transaction_from` is the time a transaction was made, and `transaction_to` is the time that the transaction was superseded (which may be infinity if it has not yet been superseded). This makes the table into a bitemporal table.

What happens if the person's address as stored in the database is incorrect? Suppose an official accidentally entered the wrong address or date? Or, suppose the person lied about their address for some reason. Upon discovery of the error, the officials update the database to correct the information recorded.

For example, from 1995-06-01 to 2000-09-03, John Doe moved to Beachy. But to avoid paying Beachy's exorbitant residence tax, he never reported it to the authorities. Later during a tax investigation, it is discovered on 2-Feb-2001 that he was in fact in Beachy during those dates. To record this fact, the existing entry about John living in Bigtown must be split into two separate records, and a new record inserted recording his residence in Beachy. The database would then appear as follows:

| Name | City | Valid from | Valid to |
|---|---|---|---|
| John Doe | Smallville | 1975-04-03 | 1994-08-26 |
| John Doe | Bigtown | 1994-08-26 | 1995-06-01 |
| John Doe | Beachy | 1995-06-01 | 2000-09-03 |
| John Doe | Bigtown | 2000-09-03 | 2001-04-01 |

However, this leaves no record that the database ever claimed that he lived in Bigtown during 1995-06-01 to 2000-09-03. This might be important to know for auditing reasons, or to use as evidence in the official's tax investigation. Transaction time allows capturing this changing knowledge in the database, since entries are never directly modified or deleted. Instead, each entry records when it was entered and when it was superseded (or logically deleted). The database contents then look like this:

| Name | City | Valid from | Valid to | Entered | Superseded |
|---|---|---|---|---|---|
| John Doe | Smallville | 1975-04-03 | ∞ | 1975-04-04 | 1994-12-27 |
| John Doe | Smallville | 1975-04-03 | 1994-08-26 | 1994-12-27 | ∞ |
| John Doe | Bigtown | 1994-08-26 | ∞ | 1994-12-27 | 2001-02-02 |
| John Doe | Bigtown | 1994-08-26 | 1995-06-01 | 2001-02-02 | ∞ |
| John Doe | Beachy | 1995-06-01 | 2000-09-03 | 2001-02-02 | ∞ |
| John Doe | Bigtown | 2000-09-03 | ∞ | 2001-02-02 | 2001-04-01 |
| John Doe | Bigtown | 2000-09-03 | 2001-04-01 | 2001-04-01 | ∞ |

The database records not only what happened in the real world, but also what was officially recorded at different times.

### Using three axes: valid time, decision time, and transaction time

Decision time is an alternative to the transaction time period for recording the time at which a database entry may be accepted as correct. This enables queries that show the officially recognized facts at a given time, even if there was a delay in committing those facts to the database. Support for decision time preserves the entire history and prevents the loss of information during updates.

Decision time periods can only occur in the past or up to the transaction time. As in a transaction time table, records are never deleted. Only new records can be inserted, and existing ones updated by setting their decision end time to show that they are no longer current.

To enable decision time, two more fields are added to a database table: `decision_from` and `decision_to`. Here, `decision_from` is the time a decision was made, and `decision_to` is the time that the decision was superseded (which may be infinity if it has not yet been superseded). When combined with transaction time, this makes the table into a tritemporal table. The following is a list of real events that occurred between the 1964 and 1976 United States presidential elections:

| Date | Decision maker | Real world event |
|---|---|---|
| 1964-11-03 | Electoral College | Election of 1964 |
| 1968-11-05 | Electoral College | Election of 1968 |
| 1972-11-07 | Electoral College | Election of 1972 |
| 1973-10-10 | Spiro Agnew | Agnew resigns |
| 1973-10-12 | Richard Nixon | Nixon nominates Ford |
| 1973-12-06 | Congress | Congress confirms Ford |
| 1974-08-09 | Richard Nixon | Nixon resigns |
| 1974-08-20 | Gerald Ford | Ford nominates Rockefeller |
| 1974-12-19 | Congress | Congress confirms Rockefeller |
| 1976-11-02 | Electoral College | Election of 1976 |

In this example, a constant 7-day delay is assumed between the decision time and the transaction time when the data is committed to the database. Given those conditions, the database would have contained the following information after the election in 1976:

|   | Valid | Decision | Transaction |   |   |   |   |
|---|---|---|---|---|---|---|---|
| President | Vice | From | To | From | To | From | To |
| Johnson | Humphrey | 1965-01-20 | 1969-01-20 | 1964-11-03 | ∞ | 1964-11-10 | ∞ |
| Nixon | Agnew | 1969-01-20 | 1973-01-20 | 1968-11-05 | ∞ | 1968-11-12 | ∞ |
| Nixon | Agnew | 1973-01-20 | 1977-01-20 | 1972-11-07 | ∞ | 1972-11-14 | 1973-10-17 |
| Nixon | Agnew | 1973-01-20 | 1977-01-20 | 1972-11-07 | 1973-10-10 | 1973-10-17 | ∞ |
| Nixon | Agnew | 1973-01-20 | 1973-10-10 | 1973-10-10 | ∞ | 1973-10-17 | ∞ |
| Nixon | (Vacant) | 1973-10-10 | 1977-01-20 | 1973-10-10 | ∞ | 1973-10-17 | 1973-12-13 |
| Nixon | Ford | ∞ | 1977-01-20 | 1973-10-12 | ∞ | 1973-10-19 | 1973-12-13 |
| Nixon | (Vacant) | 1973-10-10 | 1977-01-20 | 1973-10-10 | 1973-12-06 | 1973-12-13 | ∞ |
| Nixon | (Vacant) | 1973-10-10 | 1973-12-06 | 1973-12-06 | ∞ | 1973-12-13 | ∞ |
| Nixon | Ford | ∞ | 1977-01-20 | 1973-10-12 | 1973-12-06 | 1973-12-13 | ∞ |
| Nixon | Ford | 1973-12-06 | 1977-01-20 | 1973-12-06 | ∞ | 1973-12-13 | 1974-08-15 |
| Nixon | Ford | 1973-12-06 | 1977-01-20 | 1973-12-06 | 1974-08-08 | 1974-08-15 | ∞ |
| Nixon | Ford | 1973-12-06 | 1974-08-09 | 1974-10-08 | ∞ | 1974-08-15 | ∞ |
| Ford | (Vacant) | 1974-08-09 | 1977-01-20 | 1974-10-08 | ∞ | 1974-08-15 | 1974-12-26 |
| Ford | Rockefeller | ∞ | 1977-01-20 | 1974-10-20 | ∞ | 1974-08-27 | 1974-12-26 |
| Ford | (Vacant) | 1974-08-09 | 1977-01-20 | 1974-10-08 | 1974-12-19 | 1974-12-26 | ∞ |
| Ford | (Vacant) | 1974-08-09 | 1974-12-19 | 1974-12-19 | ∞ | 1974-12-26 | ∞ |
| Ford | Rockefeller | ∞ | 1977-01-20 | 1974-08-20 | 1974-12-19 | 1974-12-26 | ∞ |
| Ford | Rockefeller | 1974-12-19 | 1977-01-20 | 1974-12-19 | ∞ | 1974-12-26 | ∞ |
| Carter | Mondale | 1977-01-20 | 1981-01-20 | 1976-11-02 | ∞ | 1976-11-09 | ∞ |

Given the 7-day delayed table above, the question "who was president and vice president for the valid time of 1977-01-01" (which given the 7-day delay could provide data for 1976-12-25) would be:

- Nixon/Agnew when using a decision time and transaction time of 1972-11-14
- Nixon/(Vacant) when using a decision time and transaction time of 1973-10-17
- Nixon/Ford when using a decision time and transaction time of 1974-08-08
- Ford/(Vacant) when using a decision time of 1974-08-08 and transaction time of current
- Ford/Rockefeller when using a decision time and transaction time of current

## Bitemporal modelling

A bitemporal model contains both valid and transaction time. This provides both *historical* and *rollback* information. Historical information (e.g.: "Where did John live in 1992?") is provided by the valid time. Rollback (e.g.: "In 1992, where did the database believe John lived?") is provided by the transaction time. The answers to these example questions may not be the same – the database may have been altered since 1992, causing the queries to produce different results.

The valid time and transaction time do not have to be the same for a single fact. For example, consider a temporal database storing data about the 18th century. The valid time of these facts is somewhere between 1701 and 1800. The transaction time would show when the facts were inserted into the database (for example 1998-01-21).

## Schema evolution

A challenging issue is the support of temporal queries in a transaction time database under evolving schema. In order to achieve perfect archival quality it is of key importance to store the data under the schema version under which they first appeared. However, even the most simple temporal query rewriting the history of an attribute value would be required to be manually rewritten under each of the schema versions, potentially hundreds as in the case of MediaWiki. This process would be particularly taxing for users. A proposed solution is to provide automatic query rewriting, although this is not part of SQL or similar standards.

Approaches to minimize the complexities of schema evolution are to:

- Use a semi-structured database/NoSQL database which reduces the complexities of modeling attribute data but provides no features for handling multiple time axes.
- Use a database capable of storing both semi-structured data for attributes and structured data for time axes (e.g., SnowflakeDB, PostgreSQL)

## Implementations in notable products

The following implementations provide temporal features in a relational database management system (RDBMS).

- MariaDB version 10.3.4 added support for SQL:2011 standard as "System-Versioned Tables".
- Oracle Database – Oracle Workspace Manager is a feature of Oracle Database which enables application developers and DBAs to manage current, proposed and historical versions of data in the same database.
- PostgreSQL version 9.2 added native ranged data types that are capable of implementing all of the features of the pgFoundry temporal contributed extension. The PostgreSQL range types are supported by numerous native operators and functions.
- Teradata provides two products. Teradata version 13.10 and Teradata version 14 have temporal features based on TSQL2 built into the database.
- IBM Db2 version 10 added a feature called "time travel query" which is based on the temporal capabilities of the SQL:2011 standard.
- Microsoft SQL Server introduced Temporal Tables as a feature for SQL Server 2016. The feature is described in a video on Microsoft's "Channel 9" web site.

Non-relational, NoSQL database management systems that provide temporal features including the following:

- TerminusDB is a fully featured open source graph database that natively supports version control, time-travel queries and diffing functions. It has an immutable layer architecture based on delta encoding and succinct data structures.
- MarkLogic introduced bitemporal data support in version 8.0. Time stamps for Valid and System time are stored in JSON or XML documents.

Temporal databases were one of the earliest forms of data version control, and influenced the development of modern data versioning systems.

### Alternatives

Slowly changing dimensions can be used to model temporal relations.
