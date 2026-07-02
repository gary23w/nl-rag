---
title: "SQLAlchemy"
source: https://en.wikipedia.org/wiki/SQLAlchemy
domain: sqlalchemy-core
license: CC-BY-SA-4.0
tags: python sqlalchemy, sqlalchemy orm, database toolkit python
fetched: 2026-07-02
---

# SQLAlchemy

**SQLAlchemy** is an open-source Python library that provides an SQL toolkit (called "SQLAlchemy Core") and an object–relational mapper (ORM) for database interactions. It allows developers to work with databases using Python objects, enabling efficient and flexible database access.

## Description

SQLAlchemy offers tools for database schema generation, querying, and object-relational mapping. Key features include:

- A comprehensive embedded domain-specific language for SQL in Python called "SQLAlchemy Core" that provides means to construct and execute SQL queries.
- A powerful ORM that allows the mapping of Python classes to database tables.
- Support for database schema migrations.
- Compatibility with multiple database backends.
- Tools for database connection pooling and transaction management.

## History

SQLAlchemy was first released in February 2006. It has evolved to include a wide range of features for database interaction and has gained popularity among Python developers. Notable versions include:

- Version 0.1 (2006): Initial release.
- Version 1.0 (2015): Major enhancements in ORM and SQL expression language.
- Version 1.4 (2021): Introduction of a new ORM API.

## Example

The following example represents an n-to-1 relationship between movies and their directors. It is shown how user-defined Python classes create corresponding database tables, how instances with relationships are created from either side of the relationship, and finally how the data can be queried — illustrating automatically generated SQL queries for both lazy and eager loading.

### Schema definition

Creating two Python classes and corresponding database tables in the DBMS:

```mw
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer)
    directed_by = Column(Integer, ForeignKey("directors.id"))

    director = relation("Director", backref="movies", lazy=False)

    def __init__(self, title=None, year=None):
        self.title = title
        self.year = year

    def __repr__(self):
        return f"Movie({self.title}, {self.year}, {self.director})"

class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"Director({self.name})"

engine = create_engine("dbms://user:pwd@host/dbname")
Base.metadata.create_all(engine)
```

### Data insertion

One can insert a director-movie relationship via either entity:

```mw
Session = sessionmaker(bind=engine)
session = Session()

m1 = Movie("Robocop", 1987)
m1.director = Director("Paul Verhoeven")

d2 = Director("George Lucas")
d2.movies = [Movie("Star Wars", 1977), Movie("THX 1138", 1971)]

try:
    session.add(m1)
    session.add(d2)
    session.commit()
except:
    session.rollback()
```

### Querying

```mw
alldata = session.query(Movie).all()
for somedata in alldata:
    print(somedata)
```

SQLAlchemy issues the following query to the DBMS (omitting aliases):

```mw
SELECT movies.id, movies.title, movies.year, movies.directed_by, directors.id, directors.name
FROM movies LEFT OUTER JOIN directors ON directors.id = movies.directed_by
```

The output:

```mw
Movie('Robocop', 1987L, Director('Paul Verhoeven'))
Movie('Star Wars', 1977L, Director('George Lucas'))
Movie('THX 1138', 1971L, Director('George Lucas'))
```

Setting `lazy=True` (default) instead, SQLAlchemy would first issue a query to get the list of movies and only when needed (lazy) for each director a query to get the name of the corresponding director:

```mw
SELECT movies.id, movies.title, movies.year, movies.directed_by
FROM movies

SELECT directors.id, directors.name
FROM directors
WHERE directors.id = %s
```
