---
title: "JSONPath"
source: https://en.wikipedia.org/wiki/JSONPath
domain: jsonpath
license: CC-BY-SA-4.0
tags: jsonpath expression, json path query, json selector syntax, json document query
fetched: 2026-07-02
---

# JSONPath

In computer software, **JSONPath** is a query language for querying values in JSON. The uses of JSONPath include:

- Selecting a specific node in a JSON value
- Retrieving a set of nodes from a JSON value, based on specific criteria
- Navigating through complex JSON values to retrieve the required data.

JSONPath queries are path expressions written as strings, e.g. `$.foo`.

## Example

The JSONPath expression `$.store.books[0]` applied to the following JSON value:

```mw
{
  "store": {
    "books": [
      { "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 399
    }
  }
}
```

selects the first book (by Nigel Rees):

```mw
{
  "author": "Nigel Rees",
  "title": "Sayings of the Century",
  "price": 8.95
}
```

The expression `$.store.books[*].price` extracts the prices of books: 8.95 and 22.99 (since `[*]` selects all the nodes of an array).

The expression `$..price` extracts all the prices: 8.95, 22.99, and 399.

## History

JSONPath was first described in an online article by Stefan Gössner in February 2007. Gössner also published initial implementations in JavaScript and PHP.

Subsequently, over fifty implementations were created in various programming languages. The JSONPath Comparison Project lists many of these implementations and compares their behavior. JSONPath is widely used in the Java ecosystem.

In 2024, the IETF published a standard for JSONPath as RFC 9535.

## Research

- *Scalable Processing of Contemporary Semi-Structured Data on Commodity Parallel Processors - A Compilation-based Approach* describes an optimisation which converts JSONPath queries into parallel programs with bounded memory requirements.
- *Supporting Descendants in SIMD-Accelerated JSONPath* describes an optimisation of JSONPath descendant queries when streaming potentially very large JSON values.
- *τJSONPath: A Temporal Extension of the JSONPath Language for the τJSchema Framework* describes a temporal extension of JSONPath that supports querying the versions of a JSON value over its version history.

## Alternatives

- JMESPath is a query language for JSON with features that go far beyond JSONPath. It has a specification, a compliance test suite, and multiple implementations in various languages.
- JSONata An open source query and transformation language for JSON data inspired by XPath 3.1.
- JSON Pointer defines a string syntax for identifying a single value within a given JSON value of known structure.
- JSONiq is a query and transformation language for JSON.
- XPath 3.1 is an expression language that allows the processing of values conforming to the XDM data model. The version 3.1 of XPath supports JSON as well as XML.
- jq is like sed for JSON data – it can be used to slice and filter and map and transform structured data.
- ZPath is a query language for structured data including JSON, CBOR and XML
