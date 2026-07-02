---
title: "Query plan"
source: https://en.wikipedia.org/wiki/Query_plan
domain: materialized-view
license: CC-BY-SA-4.0
tags: materialized view, query result cache, view maintenance, query optimization
fetched: 2026-07-02
---

# Query plan

A **query plan** (or **query execution plan**) is a sequence of steps used to access data in a SQL relational database management system. This is a specific case of the relational model concept of access plans.

Since SQL is declarative, there are typically many alternative ways to execute a given query, with widely varying performance. When a query is submitted to the database, the query optimizer evaluates some of the different, correct possible plans for executing the query and returns what it considers the best option. Because query optimizers are imperfect, database users and administrators sometimes need to manually examine and tune the plans produced by the optimizer to get better performance.

## Generating query plans

A given database management system may offer one or more mechanisms for returning the plan for a given query. Some packages feature tools which will generate a graphical representation of a query plan. Other tools allow a special mode to be set on the connection to cause the DBMS to return a textual description of the query plan. Another mechanism for retrieving the query plan involves querying a virtual database table after executing the query to be examined. In Oracle, for instance, this can be achieved using the EXPLAIN PLAN statement.

### Graphical plans

The Microsoft SQL Server Management Studio tool, which ships with Microsoft SQL Server, for example, shows this graphical plan when executing this two-table join example against an included sample database:

```mw
SELECT *
FROM HumanResources.Employee AS e
    INNER JOIN Person.Contact AS c
    ON e.ContactID = c.ContactID
ORDER BY c.LastName
```

The UI allows exploration of various attributes of the operators involved in the query plan, including the operator type, the number of rows each operator consumes or produces, and the expected cost of each operator's work.

### Textual plans

The textual plan given for the same query in the screenshot is shown here:

```mw
StmtText
----
  |--Sort(ORDER BY:([c].[LastName] ASC))
       |--Nested Loops(Inner Join, OUTER REFERENCES:([e].[ContactID], [Expr1004]) WITH UNORDERED PREFETCH)
            |--Clustered Index Scan(OBJECT:([AdventureWorks].[HumanResources].[Employee].[PK_Employee_EmployeeID] AS [e]))
            |--Clustered Index Seek(OBJECT:([AdventureWorks].[Person].[Contact].[PK_Contact_ContactID] AS [c]),
               SEEK:([c].[ContactID]=[AdventureWorks].[HumanResources].[Employee].[ContactID] as [e].[ContactID]) ORDERED FORWARD)
```

It indicates that the query engine will do a scan over the primary key index on the Employee table and a matching seek through the primary key index (the ContactID column) on the Contact table to find matching rows. The resulting rows from each side will be shown to a nested loops join operator, sorted, then returned as the result set to the connection.

In order to tune the query, the user must understand the different operators that the database may use, and which ones might be more efficient than others while still providing semantically correct query results.

## Database tuning

Reviewing the query plan can present opportunities for new indexes or changes to existing indexes. It can also show that the database is not properly taking advantage of existing indexes (see query optimizer).

## Query tuning

A query optimizer will not always choose the most efficient query plan for a given query. In some databases the query plan can be reviewed, problems found, and then the query optimizer gives hints on how to improve it. In other databases, alternatives to express the same query (other queries that return the same results) can be tried. Some query tools can generate embedded hints in the query, for use by the optimizer.

Some databases - like Oracle - provide a **plan table** for query tuning. This plan table will return the cost and time for executing a query. Oracle offers two optimization approaches:

1. CBO or Cost Based Optimization
2. RBO or Rule Based Optimization

RBO is slowly being deprecated. For CBO to be used, all the tables referenced by the query must be analyzed. To analyze a table, a DBA can launch code from the DBMS_STATS package.

Other tools for query optimization include:

1. SQL Trace
2. Oracle Trace and TKPROF
3. Microsoft SMS (SQL) Execution Plan
4. Tableau Performance Recording (all DB)
