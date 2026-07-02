---
title: "Hypertext Application Language"
source: https://en.wikipedia.org/wiki/Hypertext_Application_Language
domain: hal-hypermedia
license: CC-BY-SA-4.0
tags: hal hypermedia, hypertext application language, hypermedia api format, hyperlinked resources
fetched: 2026-07-02
---

# Hypertext Application Language

**Hypertext Application Language** (**HAL**) is a convention for defining hypermedia such as links to external resources within JSON or XML code. It is documented in an Internet Draft (a "work in progress"), with the latest version 11 published the 10th of October 2023. The standard was initially proposed in June 2012, specifically for use with JSON, and has since become available in two variations, JSON and XML. The two associated MIME types are application/hal+xml and application/hal+json.

HAL was created to be simple to use and easily applicable across different domains by avoiding the need to impose any requirements on how the project be structured. Maintaining this minimal impact approach, HAL has enabled developers to create general-purpose libraries which can be incorporated on any API that uses HAL.

APIs that adopt HAL simplify the use of open source libraries and make it possible to interact with the API using JSON or XML. The alternative would be having to develop a proprietary format which in turn forces developers to learn how to use yet another foreign format.

## Convention

HAL is structured in such a way as to represent elements based on two concepts: Resources and Links. Resources consist of URI links, embedded resources, your standard data (be it JSON or XML), and non URI links. Links have a target URI, as well as the name of the link (referred to as 'rel'), as well as optional properties designed to be mindful of deprecation and content negotiation.

## Example

General Resource

```mw
{
  "_links": {
    "self": {
      "href": "http://example.com/api/book/hal-cookbook"
    }
  },
  "id": "hal-cookbook",
  "name": "HAL Cookbook"
}
```

Embedded resource

```mw
{
  "_links": {
    "self": {
      "href": "http://example.com/api/book/hal-cookbook"
    }
  },
  "_embedded": {
    "author": {
      "_links": {
        "self": {
          "href": "http://example.com/api/author/shahadat"
        }
      },
      "id": "shahadat",
      "name": "Shahadat Hossain Khan",
      "homepage": "http://author-example.com"
    }
  },
  "id": "hal-cookbook",
  "name": "HAL Cookbook"
}
```

Collections

```mw
{
  "_links": {
    "self": {
      "href": "http://example.com/api/book/hal-cookbook"
    },
    "next": {
      "href": "http://example.com/api/book/hal-case-study"
    },
    "prev": {
      "href": "http://example.com/api/book/json-and-beyond"
    },
    "first": {
      "href": "http://example.com/api/book/catalog"
    },
    "last": {
      "href": "http://example.com/api/book/upcoming-books"
    }
  },
  "_embedded": {
    "author": {
      "_links": {
        "self": {
          "href": "http://example.com/api/author/shahadat"
        }
      },
      "id": "shahadat",
      "name": "Shahadat Hossain Khan",
      "homepage": "http://author-example.com"
    }
  },
  "id": "hal-cookbook",
  "name": "HAL Cookbook"
}
```
