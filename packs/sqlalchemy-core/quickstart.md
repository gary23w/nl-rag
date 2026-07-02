---
title: "ORM Quick Start"
source: https://docs.sqlalchemy.org/en/20/orm/quickstart.html
domain: sqlalchemy-core
license: CC-BY-SA-4.0
tags: python sqlalchemy, sqlalchemy orm, database toolkit python
fetched: 2026-07-02
---

# ORM Quick Start

Release:

2.0.51

| Release Date: June 15, 2026

# SQLAlchemy 2.0 Documentation

- **Previous:** SQLAlchemy ORM
- **Next:** ORM Mapped Class Configuration
- **Up:** Home
- **On this page:**

# ORM Quick Start

For new users who want to quickly see what basic ORM use looks like, here’s an abbreviated form of the mappings and examples used in the SQLAlchemy Unified Tutorial. The code here is fully runnable from a clean command line.

As the descriptions in this section are intentionally **very short**, please proceed to the full SQLAlchemy Unified Tutorial for a much more in-depth description of each of the concepts being illustrated here.

Changed in version 2.0: The ORM Quickstart is updated for the latest **PEP 484**-aware features using new constructs including `mapped_column()`. See the section ORM Declarative Models for migration information.

## Declare Models

Here, we define module-level constructs that will form the structures which we will be querying from the database. This structure, known as a Declarative Mapping, defines at once both a Python object model, as well as database metadata that describes real SQL tables that exist, or will exist, in a particular database:

```
>>> from typing import List
>>> from typing import Optional
>>> from sqlalchemy import ForeignKey
>>> from sqlalchemy import String
>>> from sqlalchemy.orm import DeclarativeBase
>>> from sqlalchemy.orm import Mapped
>>> from sqlalchemy.orm import mapped_column
>>> from sqlalchemy.orm import relationship

>>> class Base(DeclarativeBase):
...     pass

>>> class User(Base):
...     __tablename__ = "user_account"
...
...     id: Mapped[int] = mapped_column(primary_key=True)
...     name: Mapped[str] = mapped_column(String(30))
...     fullname: Mapped[Optional[str]]
...
...     addresses: Mapped[List["Address"]] = relationship(
...         back_populates="user", cascade="all, delete-orphan"
...     )
...
...     def __repr__(self) -> str:
...         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

>>> class Address(Base):
...     __tablename__ = "address"
...
...     id: Mapped[int] = mapped_column(primary_key=True)
...     email_address: Mapped[str]
...     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
...
...     user: Mapped["User"] = relationship(back_populates="addresses")
...
...     def __repr__(self) -> str:
...         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

The mapping starts with a base class, which above is called `Base`, and is created by making a simple subclass against the `DeclarativeBase` class.

Individual mapped classes are then created by making subclasses of `Base`. A mapped class typically refers to a single particular database table, the name of which is indicated by using the `__tablename__` class-level attribute.

Next, columns that are part of the table are declared, by adding attributes that include a special typing annotation called `Mapped`. The name of each attribute corresponds to the column that is to be part of the database table. The datatype of each column is taken first from the Python datatype that’s associated with each `Mapped` annotation; `int` for `INTEGER`, `str` for `VARCHAR`, etc. Nullability derives from whether or not the `Optional[]` (or its equivalent) type modifier is used. More specific typing information may be indicated using SQLAlchemy type objects in the right side `mapped_column()` directive, such as the `String` datatype used above in the `User.name` column. The association between Python types and SQL types can be customized using the type annotation map.

The `mapped_column()` directive is used for all column-based attributes that require more specific customization. Besides typing information, this directive accepts a wide variety of arguments that indicate specific details about a database column, including server defaults and constraint information, such as membership within the primary key and foreign keys. The `mapped_column()` directive accepts a superset of arguments that are accepted by the SQLAlchemy `Column` class, which is used by SQLAlchemy Core to represent database columns.

All ORM mapped classes require at least one column be declared as part of the primary key, typically by using the `Column.primary_key` parameter on those `mapped_column()` objects that should be part of the key. In the above example, the `User.id` and `Address.id` columns are marked as primary key.

Taken together, the combination of a string table name as well as a list of column declarations is known in SQLAlchemy as table metadata. Setting up table metadata using both Core and ORM approaches is introduced in the SQLAlchemy Unified Tutorial at Working with Database Metadata. The above mapping is an example of what’s known as Annotated Declarative Table configuration.

Other variants of `Mapped` are available, most commonly the `relationship()` construct indicated above. In contrast to the column-based attributes, `relationship()` denotes a linkage between two ORM classes. In the above example, `User.addresses` links `User` to `Address`, and `Address.user` links `Address` to `User`. The `relationship()` construct is introduced in the SQLAlchemy Unified Tutorial at Working with ORM Related Objects.

Finally, the above example classes include a `__repr__()` method, which is not required but is useful for debugging. Mapped classes can be created with methods such as `__repr__()` generated automatically, using dataclasses. More on dataclass mapping at Declarative Dataclass Mapping.

## Create an Engine

The `Engine` is a **factory** that can create new database connections for us, which also holds onto connections inside of a Connection Pool for fast reuse. For learning purposes, we normally use a SQLite memory-only database for convenience:

```
>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite://", echo=True)
```

Tip

The `echo=True` parameter indicates that SQL emitted by connections will be logged to standard out.

A full intro to the `Engine` starts at Establishing Connectivity - the Engine.

## Emit CREATE TABLE DDL

Using our table metadata and our engine, we can generate our schema at once in our target SQLite database, using a method called `MetaData.create_all()`:

```pycon+sql
>>> Base.metadata.create_all(engine)
BEGIN (implicit)
PRAGMA main.table_...info("user_account")
...
PRAGMA main.table_...info("address")
...
CREATE TABLE user_account (
    id INTEGER NOT NULL,
    name VARCHAR(30) NOT NULL,
    fullname VARCHAR,
    PRIMARY KEY (id)
)
...
CREATE TABLE address (
    id INTEGER NOT NULL,
    email_address VARCHAR NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES user_account (id)
)
...
COMMIT
```

A lot just happened from that bit of Python code we wrote. For a complete overview of what’s going on on with Table metadata, proceed in the Tutorial at Working with Database Metadata.

## Create Objects and Persist

We are now ready to insert data in the database. We accomplish this by creating instances of `User` and `Address` classes, which have an `__init__()` method already as established automatically by the declarative mapping process. We then pass them to the database using an object called a Session, which makes use of the `Engine` to interact with the database. The `Session.add_all()` method is used here to add multiple objects at once, and the `Session.commit()` method will be used to flush any pending changes to the database and then commit the current database transaction, which is always in progress whenever the `Session` is used:

```pycon+sql
>>> from sqlalchemy.orm import Session

>>> with Session(engine) as session:
...     spongebob = User(
...         name="spongebob",
...         fullname="Spongebob Squarepants",
...         addresses=[Address(email_address="[email protected]")],
...     )
...     sandy = User(
...         name="sandy",
...         fullname="Sandy Cheeks",
...         addresses=[
...             Address(email_address="[email protected]"),
...             Address(email_address="[email protected]"),
...         ],
...     )
...     patrick = User(name="patrick", fullname="Patrick Star")
...
...     session.add_all([spongebob, sandy, patrick])
...
...     session.commit()
BEGIN (implicit)
INSERT INTO user_account (name, fullname) VALUES (?, ?) RETURNING id
[...] ('spongebob', 'Spongebob Squarepants')
INSERT INTO user_account (name, fullname) VALUES (?, ?) RETURNING id
[...] ('sandy', 'Sandy Cheeks')
INSERT INTO user_account (name, fullname) VALUES (?, ?) RETURNING id
[...] ('patrick', 'Patrick Star')
INSERT INTO address (email_address, user_id) VALUES (?, ?) RETURNING id
[...] ('[email protected]', 1)
INSERT INTO address (email_address, user_id) VALUES (?, ?) RETURNING id
[...] ('[email protected]', 2)
INSERT INTO address (email_address, user_id) VALUES (?, ?) RETURNING id
[...] ('[email protected]', 2)
COMMIT
```

Tip

It’s recommended that the `Session` be used in context manager style as above, that is, using the Python `with:` statement. The `Session` object represents active database resources so it’s good to make sure it’s closed out when a series of operations are completed. In the next section, we’ll keep a `Session` opened just for illustration purposes.

Basics on creating a `Session` are at Executing with an ORM Session and more at Basics of Using a Session.

Then, some varieties of basic persistence operations are introduced at Inserting Rows using the ORM Unit of Work pattern.

## Simple SELECT

With some rows in the database, here’s the simplest form of emitting a SELECT statement to load some objects. To create SELECT statements, we use the `select()` function to create a new `Select` object, which we then invoke using a `Session`. The method that is often useful when querying for ORM objects is the `Session.scalars()` method, which will return a `ScalarResult` object that will iterate through the ORM objects we’ve selected:

```pycon+sql
>>> from sqlalchemy import select

>>> session = Session(engine)

>>> stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

>>> for user in session.scalars(stmt):
...     print(user)
BEGIN (implicit)
SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
WHERE user_account.name IN (?, ?)
[...] ('spongebob', 'sandy')
User(id=1, name='spongebob', fullname='Spongebob Squarepants')
User(id=2, name='sandy', fullname='Sandy Cheeks')
```

The above query also made use of the `Select.where()` method to add WHERE criteria, and also used the `ColumnOperators.in_()` method that’s part of all SQLAlchemy column-like constructs to use the SQL IN operator.

More detail on how to select objects and individual columns is at Selecting ORM Entities and Columns.

## SELECT with JOIN

It’s very common to query amongst multiple tables at once, and in SQL the JOIN keyword is the primary way this happens. The `Select` construct creates joins using the `Select.join()` method:

```pycon+sql
>>> stmt = (
...     select(Address)
...     .join(Address.user)
...     .where(User.name == "sandy")
...     .where(Address.email_address == "[email protected]")
... )
>>> sandy_address = session.scalars(stmt).one()
SELECT address.id, address.email_address, address.user_id
FROM address JOIN user_account ON user_account.id = address.user_id
WHERE user_account.name = ? AND address.email_address = ?
[...] ('sandy', '[email protected]')
>>> sandy_address
Address(id=2, email_address='[email protected]')
```

The above query illustrates multiple WHERE criteria which are automatically chained together using AND, as well as how to use SQLAlchemy column-like objects to create “equality” comparisons, which uses the overridden Python method `ColumnOperators.__eq__()` to produce a SQL criteria object.

Some more background on the concepts above are at The WHERE clause and Explicit FROM clauses and JOINs.

## Make Changes

The `Session` object, in conjunction with our ORM-mapped classes `User` and `Address`, automatically track changes to the objects as they are made, which result in SQL statements that will be emitted the next time the `Session` flushes. Below, we change one email address associated with “sandy”, and also add a new email address to “patrick”, after emitting a SELECT to retrieve the row for “patrick”:

```pycon+sql
>>> stmt = select(User).where(User.name == "patrick")
>>> patrick = session.scalars(stmt).one()
SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
WHERE user_account.name = ?
[...] ('patrick',)
>>> patrick.addresses.append(Address(email_address="[email protected]"))
SELECT address.id AS address_id, address.email_address AS address_email_address, address.user_id AS address_user_id
FROM address
WHERE ? = address.user_id
[...] (3,)
>>> sandy_address.email_address = "[email protected]"

>>> session.commit()
UPDATE address SET email_address=? WHERE address.id = ?
[...] ('[email protected]', 2)
INSERT INTO address (email_address, user_id) VALUES (?, ?)
[...] ('[email protected]', 3)
COMMIT
```

Notice when we accessed `patrick.addresses`, a SELECT was emitted. This is called a lazy load. Background on different ways to access related items using more or less SQL is introduced at Loader Strategies.

A detailed walkthrough on ORM data manipulation starts at Data Manipulation with the ORM.

## Some Deletes

All things must come to an end, as is the case for some of our database rows - here’s a quick demonstration of two different forms of deletion, both of which are important based on the specific use case.

First we will remove one of the `Address` objects from the “sandy” user. When the `Session` next flushes, this will result in the row being deleted. This behavior is something that we configured in our mapping called the delete cascade. We can get a handle to the `sandy` object by primary key using `Session.get()`, then work with the object:

```pycon+sql
>>> sandy = session.get(User, 2)
BEGIN (implicit)
SELECT user_account.id AS user_account_id, user_account.name AS user_account_name, user_account.fullname AS user_account_fullname
FROM user_account
WHERE user_account.id = ?
[...] (2,)
>>> sandy.addresses.remove(sandy_address)
SELECT address.id AS address_id, address.email_address AS address_email_address, address.user_id AS address_user_id
FROM address
WHERE ? = address.user_id
[...] (2,)
```

The last SELECT above was the lazy load operation proceeding so that the `sandy.addresses` collection could be loaded, so that we could remove the `sandy_address` member. There are other ways to go about this series of operations that won’t emit as much SQL.

We can choose to emit the DELETE SQL for what’s set to be changed so far, without committing the transaction, using the `Session.flush()` method:

```pycon+sql
>>> session.flush()
DELETE FROM address WHERE address.id = ?
[...] (2,)
```

Next, we will delete the “patrick” user entirely. For a top-level delete of an object by itself, we use the `Session.delete()` method; this method doesn’t actually perform the deletion, but sets up the object to be deleted on the next flush. The operation will also cascade to related objects based on the cascade options that we configured, in this case, onto the related `Address` objects:

```pycon+sql
>>> session.delete(patrick)
SELECT user_account.id AS user_account_id, user_account.name AS user_account_name, user_account.fullname AS user_account_fullname
FROM user_account
WHERE user_account.id = ?
[...] (3,)
SELECT address.id AS address_id, address.email_address AS address_email_address, address.user_id AS address_user_id
FROM address
WHERE ? = address.user_id
[...] (3,)
```

The `Session.delete()` method in this particular case emitted two SELECT statements, even though it didn’t emit a DELETE, which might seem surprising. This is because when the method went to inspect the object, it turns out the `patrick` object was expired, which happened when we last called upon `Session.commit()`, and the SQL emitted was to re-load the rows from the new transaction. This expiration is optional, and in normal use we will often be turning it off for situations where it doesn’t apply well.

To illustrate the rows being deleted, here’s the commit:

```pycon+sql
>>> session.commit()
DELETE FROM address WHERE address.id = ?
[...] (4,)
DELETE FROM user_account WHERE user_account.id = ?
[...] (3,)
COMMIT
```

The Tutorial discusses ORM deletion at Deleting ORM Objects using the Unit of Work pattern. Background on object expiration is at Expiring / Refreshing; cascades are discussed in depth at Cascades.

## Learn the above concepts in depth

For a new user, the above sections were likely a whirlwind tour. There’s a lot of important concepts in each step above that weren’t covered. With a quick overview of what things look like, it’s recommended to work through the SQLAlchemy Unified Tutorial to gain a solid working knowledge of what’s really going on above. Good luck!

Previous:

SQLAlchemy ORM

Next:

ORM Mapped Class Configuration

©

Copyright

2007-2026, the SQLAlchemy authors and contributors.

**flambé!** the dragon and ***The Alchemist*** image designs created and generously donated by Rotem Yaari.

Created using

Sphinx

9.1.0. Documentation last generated: Thu 25 Jun 2026 09:35:36 AM EDT
