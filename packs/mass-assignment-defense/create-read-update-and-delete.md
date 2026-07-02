---
title: "Create, read, update and delete"
source: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
domain: mass-assignment-defense
license: CC-BY-SA-4.0
tags: mass assignment vulnerability, object binding allowlist, auto binding overposting, parameter binding control
fetched: 2026-07-02
---

# Create, read, update and delete

In computer programming, **create, read, update, and delete** (**CRUD**) are the four basic operations (actions) of persistent storage. CRUD is also sometimes used to describe user interface conventions that facilitate viewing, searching, and changing information using computer-based forms and reports.

## History

The term *CRUD* was likely first popularized in 1983 by James Martin in his book *Managing the data-base environment*.

## Conceptual

Data can be put in a *location/area* of a storage mechanism.

- The fundamental feature of a storage location is that its *content* is both *readable* and *updatable*.
- Before a storage location can be read or updated it needs to be *created*; that is allocated and initialized with content.
- At some later point, the storage location may need to be *destructed*; that is finalized and deallocated.

Together these four operations make up the basic operations of storage management known as CRUD: *Create*, *Read*, *Update* and *Delete*.

## Use cases

### Databases

The acronym CRUD refers to the major operations which are implemented by databases. Each letter in the acronym can be mapped to a standard Structured Query Language (SQL) statement.

| CRUD | SQL |
|---|---|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

Although relational databases are a common persistence layer in software applications, numerous other persistence layers exist. CRUD functionality can for example be implemented with document databases, object databases, XML databases, text files, or binary files.

Some big data systems do not implement UPDATE, but have only a timestamped INSERT (journaling), storing a completely new version of the object each time.

### RESTful APIs

The acronym CRUD also appears in the discussion of RESTful APIs. Each letter in the acronym may be mapped to a Hypertext Transfer Protocol (HTTP) method:

| CRUD | HTTP |
|---|---|
| Create | POST |
| Read | GET |
| Update | PUT to replace, PATCH to modify |
| Delete | DELETE |

In HTTP, the POST (create), GET (read), PUT (update), PATCH (partial update), and DELETE methods correspond to CRUD operations as they have storage management semantics, meaning that they let user agents directly manipulate the states of target resources. However, POST is not limited to resource creation and may also be used for process-oriented operations whose semantics exceed the scope of CRUD.

### User interface

CRUD is also relevant at the user interface level of most applications. For example, in address book software, the basic storage unit is an individual *contact entry*. As a bare minimum, the software must allow the user to:

- *Create*, or add new entries
- *Read*, retrieve, search, or view existing entries
- *Update*, or edit existing entries
- *Delete*, deactivate, or remove existing entries

Because these operations are so fundamental, they are often documented and described under one comprehensive heading such as "contact management" or "document management" in general.

## Other variations

Other variations of CRUD include:

- ABCD (add, browse, change, delete)
- CRUDL (create, read, update, delete, list)
- BREAD (browse, read, edit, add, delete)
- DAVE (delete, add, view, edit)
- CRAP (create, replicate, append, process)
- MACD (Move, Add, Change, Delete)
