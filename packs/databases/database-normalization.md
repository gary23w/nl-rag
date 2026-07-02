---
title: "Database normalization"
source: https://en.wikipedia.org/wiki/Database_normalization
domain: databases
license: CC-BY-SA-4.0 / PostgreSQL
tags: postgres, postgresql, relational database, transaction, acid, database index
fetched: 2026-07-02
---

# Database normalization

**Database normalization** is the process of structuring a relational database in accordance with a series of ***normal forms*** to reduce data redundancy and improve data integrity. It was first proposed by British computer scientist Edgar F. Codd as part of his relational model.

Normalization entails organizing the columns (attributes) and tables (relations) of a database to ensure that their dependencies are properly enforced by database integrity constraints. It is accomplished by applying some formal rules either by a process of *synthesis* (creating a new database design) or *decomposition* (improving an existing database design).

## Objectives

A basic objective of the first normal form defined by Codd in 1970 was to permit data to be queried and manipulated using a "universal data sub-language" grounded in first-order logic. An example of such a language is SQL, though it is one that Codd regarded as seriously flawed.

The objectives of normalization beyond 1NF (first normal form) were stated by Codd as:

> 1. To free the collection of relations from undesirable insertion, update and deletion dependencies.
> 2. To reduce the need for restructuring the collection of relations, as new types of data are introduced, and thus increase the life span of application programs.
> 3. To make the relational model more informative to users.
> 4. To make the collection of relations neutral to the query statistics, where these statistics are liable to change as time goes by.

— E.F. Codd, "Further Normalisation of the Data Base Relational Model"

When an attempt is made to modify (update, insert into, or delete from) a relation, the following undesirable side effects may arise in relations that have not been sufficiently normalized:

**Insertion anomaly**

There are circumstances in which certain facts cannot be recorded at all. For example, each record in a "Faculty and Their Courses" relation might contain a Faculty ID, Faculty Name, Faculty Hire Date, and Course Code. Therefore, the details of any faculty member who teaches at least one course can be recorded, but a newly hired faculty member who has not yet been assigned to teach any courses cannot be recorded, except by setting the Course Code to

null

.

**Update anomaly**

The same information can be expressed on multiple rows; therefore updates to the relation may result in logical inconsistencies. For example, each record in an "Employees' Skills" relation might contain an Employee ID, Employee Address, and Skill; thus a change of address for a particular employee may need to be applied to multiple records (one for each skill). If the update is only partially successful – the employee's address is updated on some records but not others – then the relation is left in an inconsistent state. Specifically, the relation provides conflicting answers to the question of what this particular employee's address is.

**Deletion anomaly**

Under certain circumstances, the deletion of data representing certain facts necessitates the deletion of data representing completely different facts. The "Faculty and Their Courses" relation described in the previous example suffers from this type of anomaly, for if a faculty member temporarily ceases to be assigned to any courses, the last of the records on which that faculty member appears must be deleted, effectively also deleting the faculty member, unless the Course Code field is set to null.

### Minimize redesign when extending the database structure

A fully normalized database can be extended to accommodate new types of data with minimal changes to its existing structure. As a result, applications interacting with the database are minimally affected.

Normalized relations and the relationships between them mirror real-world concepts and their interrelationships.

## Normal forms

Codd introduced the concept of normalization and what is now known as the first normal form (1NF) in 1970. Codd went on to define the second normal form (2NF) and third normal form (3NF) in 1971, and Codd and Raymond F. Boyce defined the Boyce–Codd normal form (BCNF) in 1974.

Ronald Fagin introduced the fourth normal form (4NF) in 1977 and the fifth normal form (5NF) in 1979. Christopher J. Date introduced the sixth normal form (6NF) in 2003.

Informally, a relational database relation is often described as "normalized" if it meets third normal form. Most 3NF relations are free of insertion, updation, and deletion anomalies.

The normal forms (from least normalized to most normalized) are:

- UNF: Unnormalized form
- 1NF: First normal form
- 2NF: Second normal form
- 3NF: Third normal form
- EKNF: Elementary key normal form
- BCNF: Boyce–Codd normal form
- 4NF: Fourth normal form
- ETNF: Essential tuple normal form
- 5NF: Fifth normal form
- DKNF: Domain-key normal form
- 6NF: Sixth normal form

Constraint

(informal description in parentheses)

UNF

(1970)

1NF

(1970)

2NF

(1971)

3NF

(1971)

EKNF

(1982)

BCNF

(1974)

4NF

(1977)

ETNF

(2012)

5NF

(1979)

DKNF

(1981)

6NF

(2003)

Unique rows (no duplicate records)

Scalar columns (columns cannot contain relations or composite values)

Every non-prime attribute has a full

functional dependency

on each

candidate key

(attributes depend on the

whole

of every key)

Every non-trivial functional dependency either begins with a

superkey

or ends with a prime attribute (attributes depend

only

on candidate keys)

Every non-trivial functional dependency either begins with a superkey or ends with an

elementary prime attribute

(a stricter form of 3NF)

—

N/a

Every non-trivial functional dependency begins with a superkey (a stricter form of 3NF)

—

N/a

Every non-trivial

multivalued dependency

begins with a superkey

—

N/a

Every

join dependency

has a superkey component

—

N/a

Every join dependency has only superkey components

—

N/a

Every constraint is a consequence of domain constraints and key constraints

Every join dependency is trivial

## Example

Normalization is a database design technique, which is used to design a relational database table up to higher normal form. The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.

That means that, having data in unnormalized form (the least normalized) and aiming to achieve the highest level of normalization, the first step would be to ensure compliance to the first normal form, the second step would be to ensure compliance to the second normal form, and so forth in the order mentioned above, until the data conforms to the sixth normal form.

However, normal forms beyond 4NF are mainly of academic interest, as the problems they exist to solve rarely appear in practice.

*The data in the following example was intentionally designed to contradict most of the normal forms. In practice, it is often possible to skip some of the normalization steps because the data is already normalized to some extent. Fixing a violation of one normal form also often fixes a violation of a higher normal form. In the example, one table has been chosen for normalization at each step, meaning that at the end, some tables might not be sufficiently normalized.*

### Initial data

Let a database table exist with the following structure, describing a book:

Title

Author

Author Nationality

Format

Price

Subject

Pages

Thickness

Publisher

Publisher Country

Genre ID

Genre Name

Beginning MySQL Database Design and Optimization

Chad Russell

American

Hardcover

49.99

| MySQL |
|---|
| Database |
| Design |

520

Thick

Apress

USA

1

Tutorial

For this example it is assumed that each book has only one author.

A table that conforms to the relational model has a primary key which uniquely identifies a row. In our example, the primary key is a composite key of **{Title, Format}**, indicated by underlining:

Title

Author

Author Nationality

Format

Price

Subject

Pages

Thickness

Publisher

Publisher Country

Genre ID

Genre Name

Beginning MySQL Database Design and Optimization

Chad Russell

American

Hardcover

49.99

| MySQL |
|---|
| Database |
| Design |

520

Thick

Apress

USA

1

Tutorial

### Satisfying 1NF

In the first normal form each field contains a single value. A field may not contain a set of values or a nested record. **Subject** contains a set of subject values, meaning it does not comply. To solve the problem, the subjects are extracted into a separate **Subject** table:

Book

Title

Author

Author Nationality

Format

Price

Pages

Thickness

Publisher

Publisher Country

Genre ID

Genre Name

Beginning MySQL Database Design and Optimization

Chad Russell

American

Hardcover

49.99

520

Thick

Apress

USA

1

Tutorial

| Title | Subject name |
|---|---|
| Beginning MySQL Database Design and Optimization | MySQL |
| Beginning MySQL Database Design and Optimization | Database |
| Beginning MySQL Database Design and Optimization | Design |

Instead of one table in unnormalized form, there are now two tables conforming to the 1NF.

### Satisfying 2NF

Recall that the **Book** table below has a composite key of **{Title, Format}**, which will not satisfy 2NF if some subset of that key is a determinant. At this point in our design the **key** is not finalized as the primary key, so it is called a candidate key. Consider the following table:

Book

Title

Format

Author

Author Nationality

Price

Pages

Thickness

Publisher

Publisher Country

Genre ID

Genre Name

Beginning MySQL Database Design and Optimization

Hardcover

Chad Russell

American

49.99

520

Thick

Apress

USA

1

Tutorial

Beginning MySQL Database Design and Optimization

E-book

Chad Russell

American

22.34

520

Thick

Apress

USA

1

Tutorial

The Relational Model for Database Management: Version 2

E-book

E.F.Codd

British

13.88

538

Thick

Addison-Wesley

USA

2

Popular science

The Relational Model for Database Management: Version 2

Paperback

E.F.Codd

British

39.99

538

Thick

Addison-Wesley

USA

2

Popular science

All of the attributes that are not part of the candidate key depend on *Title*, but only *Price* also depends on *Format*. To conform to 2NF and remove duplicates, every non-candidate-key attribute must depend on the whole candidate key, not just part of it.

To normalize this table, make **{Title}** a (simple) candidate key (the primary key) so that every non-candidate-key attribute depends on the whole candidate key, and remove *Price* into a separate table so that its dependency on *Format* can be preserved:

Book

Title

Author

Author Nationality

Pages

Thickness

Publisher

Publisher Country

Genre ID

Genre Name

Beginning MySQL Database Design and Optimization

Chad Russell

American

520

Thick

Apress

USA

1

Tutorial

The Relational Model for Database Management: Version 2

E.F.Codd

British

538

Thick

Addison-Wesley

USA

2

Popular science

| Title | Format | Price |
|---|---|---|
| Beginning MySQL Database Design and Optimization | Hardcover | 49.99 |
| Beginning MySQL Database Design and Optimization | E-book | 22.34 |
| The Relational Model for Database Management: Version 2 | E-book | 13.88 |
| The Relational Model for Database Management: Version 2 | Paperback | 39.99 |

Now, both the **Book** and **Price** tables conform to 2NF.

### Satisfying 3NF

The **Book** table still has a transitive functional dependency ({Author Nationality} is dependent on {Author}, which is dependent on {Title}). Similar violations exist for publisher ({Publisher Country} is dependent on {Publisher}, which is dependent on {Title}) and for genre ({Genre Name} is dependent on {Genre ID}, which is dependent on {Title}). Hence, the **Book** table is not in 3NF. To resolve this, we can place {Author Nationality}, {Publisher Country}, and {Genre Name} in their own respective tables, thereby eliminating the transitive functional dependencies:

| Title | Author | Pages | Thickness | Publisher | Genre ID |
|---|---|---|---|---|---|
| Beginning MySQL Database Design and Optimization | Chad Russell | 520 | Thick | Apress | 1 |
| The Relational Model for Database Management: Version 2 | E.F.Codd | 538 | Thick | Addison-Wesley | 2 |

| Price Title Format Price Beginning MySQL Database Design and Optimization Hardcover 49.99 Beginning MySQL Database Design and Optimization E-book 22.34 The Relational Model for Database Management: Version 2 E-book 13.88 The Relational Model for Database Management: Version 2 Paperback 39.99 |
|---|

| Author | Nationality |
|---|---|
| Chad Russell | American |
| E.F.Codd | British |

| Publisher | Country |
|---|---|
| Apress | USA |
| Addison-Wesley | USA |

| Genre ID | Name |
|---|---|
| 1 | Tutorial |
| 2 | Popular science |

### Satisfying EKNF

The elementary key normal form (EKNF) falls strictly between 3NF and BCNF and is not much discussed in the literature. It is intended *"to capture the salient qualities of both 3NF and BCNF"* while avoiding the problems of both (namely, that 3NF is "too forgiving" and BCNF is "prone to computational complexity"). Since it is rarely mentioned in literature, it is not included in this example.

### Satisfying 4NF

Assume the database is owned by a book retailer franchise that has several franchisees that own shops in different locations. And therefore the retailer decided to add a table that contains data about availability of the books at different locations:

| Franchisee ID | Title | Location |
|---|---|---|
| 1 | Beginning MySQL Database Design and Optimization | California |
| 1 | Beginning MySQL Database Design and Optimization | Florida |
| 1 | Beginning MySQL Database Design and Optimization | Texas |
| 1 | The Relational Model for Database Management: Version 2 | California |
| 1 | The Relational Model for Database Management: Version 2 | Florida |
| 1 | The Relational Model for Database Management: Version 2 | Texas |
| 2 | Beginning MySQL Database Design and Optimization | California |
| 2 | Beginning MySQL Database Design and Optimization | Florida |
| 2 | Beginning MySQL Database Design and Optimization | Texas |
| 2 | The Relational Model for Database Management: Version 2 | California |
| 2 | The Relational Model for Database Management: Version 2 | Florida |
| 2 | The Relational Model for Database Management: Version 2 | Texas |
| 3 | Beginning MySQL Database Design and Optimization | Texas |

As this table structure consists of a compound primary key, it does not contain any non-key attributes and it is already in BCNF (and therefore also satisfies all the previous normal forms). However, assuming that all available books are offered in each area, the **Title** is not unambiguously bound to a certain **Location** and therefore the table does not satisfy 4NF.

That means that, to satisfy the fourth normal form, this table needs to be decomposed as well:

| Franchisee – Book Franchisee ID Title 1 Beginning MySQL Database Design and Optimization 1 The Relational Model for Database Management: Version 2 2 Beginning MySQL Database Design and Optimization 2 The Relational Model for Database Management: Version 2 3 Beginning MySQL Database Design and Optimization | Franchisee – Location Franchisee ID Location 1 California 1 Florida 1 Texas 2 California 2 Florida 2 Texas 3 Texas |
|---|---|

Now, every record is unambiguously identified by a superkey, therefore 4NF is satisfied.

### Satisfying ETNF

Suppose the franchisees can also order books from different suppliers. Let the relation also be subject to the following constraint:

- If a certain **supplier** supplies a certain **title**
- and the **title** is supplied to the **franchisee**
- and the **franchisee** is being supplied by the **supplier,**
- then the **supplier** supplies the **title** to the **franchisee**.

| Supplier ID | Title | Franchisee ID |
|---|---|---|
| 1 | Beginning MySQL Database Design and Optimization | 1 |
| 2 | The Relational Model for Database Management: Version 2 | 2 |
| 3 | Learning SQL | 3 |

This table is in 4NF, but the Supplier ID is equal to the join of its projections: **{{Supplier ID, Title}, {Title, Franchisee ID}, {Franchisee ID, Supplier ID}}.** No component of that join dependency is a superkey (the sole superkey being the entire heading), so the table does not satisfy the ETNF and can be further decomposed:

| Supplier – Book Supplier ID Title 1 Beginning MySQL Database Design and Optimization 2 The Relational Model for Database Management: Version 2 3 Learning SQL | Book – Franchisee Title Franchisee ID Beginning MySQL Database Design and Optimization 1 The Relational Model for Database Management: Version 2 2 Learning SQL 3 | Franchisee – Supplier Supplier ID Franchisee ID 1 1 2 2 3 3 |
|---|---|---|

The decomposition produces ETNF compliance.

### Satisfying 5NF

To spot a table not satisfying the 5NF, it is usually necessary to examine the data thoroughly. Suppose the table from 4NF example with a little modification in data and let's examine if it satisfies 5NF:

| Franchisee ID | Title | Location |
|---|---|---|
| 1 | Beginning MySQL Database Design and Optimization | California |
| 1 | Learning SQL | California |
| 1 | The Relational Model for Database Management: Version 2 | Texas |
| 2 | The Relational Model for Database Management: Version 2 | California |

Decomposing this table lowers redundancies, resulting in the following two tables:

| Franchisee – Book Franchisee ID Title 1 Beginning MySQL Database Design and Optimization 1 Learning SQL 1 The Relational Model for Database Management: Version 2 2 The Relational Model for Database Management: Version 2 | Franchisee – Location Franchisee ID Location 1 California 1 Texas 2 California |
|---|---|

The query joining these tables would return the following data:

| Franchisee ID | Title | Location |
|---|---|---|
| 1 | Beginning MySQL Database Design and Optimization | California |
| 1 | Learning SQL | California |
| 1 | The Relational Model for Database Management: Version 2 | California |
| 1 | The Relational Model for Database Management: Version 2 | Texas |
| 1 | Learning SQL | Texas |
| 1 | Beginning MySQL Database Design and Optimization | Texas |
| 2 | The Relational Model for Database Management: Version 2 | California |

The JOIN returns three more rows than it should; adding another table to clarify the relation results in three separate tables:

| Franchisee – Book Franchisee ID Title 1 Beginning MySQL Database Design and Optimization 1 Learning SQL 1 The Relational Model for Database Management: Version 2 2 The Relational Model for Database Management: Version 2 | Franchisee – Location Franchisee ID Location 1 California 1 Texas 2 California | Location – Book Location Title California Beginning MySQL Database Design and Optimization California Learning SQL California The Relational Model for Database Management: Version 2 Texas The Relational Model for Database Management: Version 2 |
|---|---|---|

What will the JOIN return now? It actually is not possible to join these three tables. That means it was not possible to decompose the **Franchisee – Book – Location** without data loss, therefore the table already satisfies 5NF.

**Disclaimer** – the data used demonstrates the principle, but fails to remain true. In this case the data would best be decomposed into the following, with a surrogate key which we will call 'Store ID':

| Store – Book Store ID Title 1 Beginning MySQL Database Design and Optimization 1 Learning SQL 2 The Relational Model for Database Management: Version 2 3 The Relational Model for Database Management: Version 2 | Store – Franchisee – Location Store ID Franchisee ID Location 1 1 California 2 1 Texas 3 2 California |   |
|---|---|---|

The JOIN will now return the expected result:

| Store ID | Title | Franchisee ID | Location |
|---|---|---|---|
| 1 | Beginning MySQL Database Design and Optimization | 1 | California |
| 1 | Learning SQL | 1 | California |
| 2 | The Relational Model for Database Management: Version 2 | 1 | Texas |
| 3 | The Relational Model for Database Management: Version 2 | 2 | California |

C.J. Date has argued that only a database in 5NF is truly "normalized".

### Satisfying DKNF

Let's have a look at the **Book** table from previous examples and see if it satisfies the domain-key normal form:

| Title | **Pages** | Thickness | *Genre ID* | *Publisher ID* |
|---|---|---|---|---|
| Beginning MySQL Database Design and Optimization | 520 | Thick | *1* | *1* |
| The Relational Model for Database Management: Version 2 | 538 | Thick | *2* | *2* |
| Learning SQL | 338 | Slim | *1* | *3* |
| SQL Cookbook | 636 | Thick | *1* | *3* |

Logically, **Thickness** is determined by number of pages. That means it depends on **Pages** which is not a key. Let's set an example convention saying a book up to 350 pages is considered "slim" and a book over 350 pages is considered "thick".

This convention is technically a constraint but it is neither a domain constraint nor a key constraint; therefore we cannot rely on domain constraints and key constraints to keep the data integrity.

In other words – nothing prevents us from putting, for example, "Thick" for a book with only 50 pages – and this makes the table violate DKNF.

To solve this, a table holding enumeration that defines the **Thickness** is created, and that column is removed from the original table:

| Thickness Enum Thickness Min pages Max pages Slim 1 350 Thick 351 999,999,999,999 | Book – Pages – Genre – Publisher Title Pages *Genre ID* *Publisher ID* Beginning MySQL Database Design and Optimization 520 *1* *1* The Relational Model for Database Management: Version 2 538 *2* *2* Learning SQL 338 *1* *3* SQL Cookbook 636 *1* *3* |
|---|---|

That way, the domain integrity violation has been eliminated, and the table is in DKNF.

Normalization does not prevent all cases of impossible/conflicting/unpredictable output. In this example, Min/Max pages of 1/350, 200/999,999,999,999 would lead to unpredictable results. It would therefore be better to specify and use only Min pages.

### Satisfying 6NF

A simple and intuitive definition of the sixth normal form is that *"a table is in 6NF when **the row contains the Primary Key, and at most one other attribute"*****.**

That means, for example, the **Publisher** table designed while creating the 1NF:

| Publisher ID | Name | Country |
|---|---|---|
| 1 | Apress | USA |

needs to be further decomposed into two tables:

| Publisher Publisher ID Name 1 Apress | Publisher country Publisher ID Country 1 USA |
|---|---|

The obvious drawback of 6NF is the proliferation of tables required to represent the information on a single entity. If a table in 5NF has one primary key column and N attributes, representing the same information in 6NF will require N tables; multi-field updates to a single conceptual record will require updates to multiple tables; and inserts and deletes will similarly require operations across multiple tables. For this reason, in databases intended to serve online transaction processing (OLTP) needs, 6NF should not be used.

However, in data warehouses, which do not permit interactive updates and which are specialized for fast query on large data volumes, certain DBMSs use an internal 6NF representation – known as a columnar data store. In situations where the number of unique values of a column is far less than the number of rows in the table, column-oriented storage allow significant savings in space through data compression. Columnar storage also allows fast execution of range queries (e.g., show all records where a particular column is between X and Y, or less than X.)

In all these cases, however, the database designer does not have to perform 6NF normalization manually by creating separate tables. Some DBMSs that are specialized for warehousing, such as Sybase IQ, use columnar storage by default, but the designer still sees only a single multi-column table. Other DBMSs, such as Microsoft SQL Server 2012 and later, let you specify a "columnstore index" for a particular table.
