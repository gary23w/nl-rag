---
title: "IndexedDB"
source: https://en.wikipedia.org/wiki/Indexed_Database_API
domain: indexeddb
license: CC-BY-SA-2.5
tags: indexeddb, indexed database api, client-side database, object store
fetched: 2026-07-02
---

# IndexedDB

(Redirected from

Indexed Database API

)

The **Indexed Database API** (commonly referred to as **IndexedDB**) is a JavaScript application programming interface (API) provided by web browsers for managing a NoSQL database of objects. It is a standard maintained by the World Wide Web Consortium (W3C).

As an alternative to the Web storage standard, IndexedDB can provide more storage capacity. Web storage has fixed limits per website, but IndexedDB limits are "usually quite large, if they exist at all".

Use cases for IndexedDB include caching web application data for offline availability. Some browser modules, such as devtools or extensions, may also use it for storage.

## History

Support for IndexedDB was added to Firefox version 4 (March 2011), Google Chrome version 11, Internet Explorer version 10, Safari version 8, and Microsoft Edge version 12.

Web SQL Database was a prior API developed by Apple. But Firefox refused to add support for it and argued against it becoming a standard because it would codify the quirks of SQLite. WebSQL was deprecated in favor of IndexedDB.

*IndexedDB 1.0* became a W3C Recommendation on January 8, 2015. *IndexedDB 2.0* became a W3C Recommendation on January 30, 2018. *IndexedDB 3.0* was released as a First Public Working Draft on 11 March 2021 and remains as a Working Draft as of April 2026.

## Performance

Because IndexedDB is running inside of the security sandbox of a browser, all operations have to go through various security layers which decreases the performance of IndexedDB. With IndexedDB 2.0 the getAll() method was added which allows to improve performance on bulk read operations.
