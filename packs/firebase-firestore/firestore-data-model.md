---
title: "Cloud Firestore Data model"
source: https://firebase.google.com/docs/firestore/data-model
domain: firebase-firestore
license: CC-BY-SA-4.0
tags: firebase, cloud firestore, backend as a service, document-oriented database
fetched: 2026-07-02
---

# Cloud Firestore Data model Stay organized with collections Save and categorize content based on your preferences.

Cloud Firestore is a NoSQL, document-oriented database. Unlike a SQL database, there are no tables or rows. Instead, you store data in *documents*, which are organized into *collections*.

Each *document* contains a set of key-value pairs. Cloud Firestore is optimized for storing large collections of small documents.

All documents must be stored in collections. Documents can contain *subcollections* and nested objects, both of which can include primitive fields like strings or complex objects like lists.

Collections and documents are created implicitly in Cloud Firestore. Simply assign data to a document within a collection. If either the collection or document does not exist, Cloud Firestore creates it.

## Documents

In Cloud Firestore, the unit of storage is the document. A document is a lightweight record that contains fields, which map to values. Each document is identified by a name.

A document representing a user `alovelace` might look like this:

- class alovelace `first : "Ada"` `last : "Lovelace"` `born : 1815`

Complex, nested objects in a document are called maps. For example, you could structure the user's name from the example above with a map, like this:

- class alovelace `name :`     `first : "Ada"`     `last : "Lovelace"` `born : 1815`

You may notice that documents look a lot like JSON. In fact, they basically are. There are some differences (for example, documents support extra data types and are limited to the document size limit), but in general, you can treat documents as lightweight JSON records.

## Collections

Documents live in collections, which are simply containers for documents. For example, you could have a `users` collection to contain your various users, each represented by a document:

- collections_bookmark users
  - class alovelace `first : "Ada"` `last : "Lovelace"` `born : 1815`
  - class aturing `first : "Alan"` `last : "Turing"` `born : 1912`

Cloud Firestore is schemaless, so you have complete freedom over what fields you put in each document and what data types you store in those fields. Documents within the same collection can all contain different fields or store different types of data in those fields. However, it's a good idea to use the same fields and data types across multiple documents, so that you can query the documents more easily.

A collection contains documents and nothing else. It can't directly contain raw fields with values, and it can't contain other collections. (See Hierarchical Data for an explanation of how to structure more complex data in Cloud Firestore.)

The names of documents within a collection are unique. You can provide your own keys, such as user IDs, or you can let Cloud Firestore create random IDs for you automatically.

You do not need to "create" or "delete" collections. After you create the first document in a collection, the collection exists. If you delete all of the documents in a collection, it no longer exists.
