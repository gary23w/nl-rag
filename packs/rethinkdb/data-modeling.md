---
title: "Data modeling in RethinkDB"
source: https://rethinkdb.com/docs/data-modeling/
domain: rethinkdb
license: CC-BY-SA-4.0
tags: rethinkdb, reql query, document-oriented database, distributed database
fetched: 2026-07-02
---

# Data modeling in RethinkDB

There are two ways to model relationships between documents in RethinkDB:

- By using **embedded arrays**.
- By linking documents stored in **multiple tables** (similar to traditional relational database systems).

Let’s explore the advantages and disadvantages of each approach. We’ll use a simple blog database that stores information about authors and their posts to demonstrate them.

(Data Modeling Illustration)

# Using embedded arrays

We can model the relationship between authors and posts by using embedded arrays as follows. Consider this example document in the table `authors`:

```json
{
  "id": "7644aaf2-9928-4231-aa68-4e65e31bf219",
  "name": "William Adama", "tv_show": "Battlestar Galactica",
  "posts": [
    {"title": "Decommissioning speech", "content": "The Cylon War is long over..."},
    {"title": "We are at war", "content": "Moments ago, this ship received..."},
    {"title": "The new Earth", "content": "The discoveries of the past few days..."}
  ]
}
```

The `authors` table contains a document for each author. Each document contains information about the relevant author and a field `posts` with an array of posts for that author. In this case the query to retrieve all authors with their posts is simple:

```python
# Retrieve all authors with their posts
r.db("blog").table("authors").run()

# Retrieve a single author with her posts
r.db("blog").table("authors").get(AUTHOR_ID).run()
```

# Linking documents in multiple tables

You can use a relational data modeling technique and create two tables to store your data. A typical document in the `authors` table would look like this:

```json
{
  "id": "7644aaf2-9928-4231-aa68-4e65e31bf219",
  "name": "William Adama",
  "tv_show": "Battlestar Galactica"
}
```

A typical document in the `posts` table would look like this:

```json
{
  "id": "064058b6-cea9-4117-b92d-c911027a725a",
  "author_id": "7644aaf2-9928-4231-aa68-4e65e31bf219",
  "title": "Decommissioning speech",
  "content": "The Cylon War is long over..."
}
```

Every post contains an `author_id` field that links each post to its author. We can retrieve all posts for a given author as follows:

```python
# If we have a secondary index on `author_id` in the table `posts`
r.db("blog").table("posts").
  get_all("7644aaf2-9928-4231-aa68-4e65e31bf219", index="author_id").
  run()

# If we didn't build a secondary index on `author_id`
r.db("blog").table("posts").
  filter({"author_id": "7644aaf2-9928-4231-aa68-4e65e31bf219"}).
  run()
```

In a relational database, we’d use a `JOIN` here; in RethinkDB, we use the `eq_join` command. To get all posts along with the author information for William Adama:

```python
# In order for this query to work, we need to have a secondary index
# on the `author_id` field of the table `posts`.
r.db("blog").table("authors").get_all("7644aaf2-9928-4231-aa68-4e65e31bf219").eq_join(
    'id',
    r.db("blog").table("posts"),
    index='author_id'
).zip().run()
```

Note that the values for `author_id` correspond to the `id` field of the author, which allows us to link the documents.

# Read more

There’s a separate article, Table joins in RethinkDB, with much more information about the multiple-table approach, including how to do the ReQL equivalents of inner, outer and cross joins. If you aren’t sure which schema to use, ask us on Stack Overflow or join the `#rethinkdb` IRC channel on Freenode.
