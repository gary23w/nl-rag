---
title: "Data exchange"
source: https://en.wikipedia.org/wiki/Data_exchange
domain: messagepack
license: CC-BY-SA-4.0
tags: messagepack format, binary json, compact serialization, binary encoding
fetched: 2026-07-02
---

# Data exchange

**Data exchange** is the process of moving data from one information system to another. It often involves transforming data that is native to the source system into a form that is consumable by the target system or to a standardized form that is consumable by any compatible system. In particular, data exchange allows data to be shared between computer programs.

Data exchange is similar to data integration except that data may be restructured with possible loss of content. There may be no way to transform a particular collection based on exchange constraints. Conversely, there may be multiple ways to transform the data, in which case one option must be identified in order to achieve compatibility between source and target.

There are two main types of data exchange: broadcast and peer-to-peer (a.k.a. unicast). For broadcast, data is transmitted simultaneously to all consumers. Just as a conference call, all participants get the same information from the speaker at the same time. For peer-to-peer, data is sent to a single receiver, defined by a specific address. For example, a letter goes to just one mail box.

## Single-domain

In some domains, a multiple source and target schema (proprietary data formats) may exist. An exchange or interchange format is often developed for a single domain, and then necessary routines (mappings) are written to (indirectly) transform/translate each and every source schema to each and every target schema by using the interchange format as an intermediate step. That requires less work than writing and debugging the many routines that would be required to directly translate each source schema directly to each target schema.

Examples of these transformative interchange formats include:

- Standard Interchange Format for geospatial data;
- Data Interchange Format for spreadsheet data;
- Open Document Format for spreadsheets, charts, presentations and word processing documents;
- GPS eXchange Format or Keyhole Markup Language for describing GPS data;
- GDSII for integrated circuit layout.

## Representation

A data exchange (a.k.a. interchange) language defines a domain-independent way to represent data. These languages have evolved from being markup and display-oriented to support the encoding of metadata that describes the structural attributes of the information.

Practice has shown that certain types of formal languages are better suited for this task than others, since their specification is driven by a formal process instead of particular software implementation. For example, XML is a markup language that was designed to enable the creation of dialects (the definition of domain-specific sublanguages). However, it does not contain domain-specific dictionaries or fact types. Beneficial to a reliable data exchange is the availability of standard dictionaries-taxonomies and tools libraries such as parsers, schema validators, and transformation tools.

### XML

The popularity of XML for data exchange on the World Wide Web has several reasons. First of all, it is closely related to the preexisting standards Standard Generalized Markup Language (SGML) and Hypertext Markup Language (HTML), and as such a parser written to support these two languages can be easily extended to support XML as well. For example, XHTML has been defined as a format that is formal XML, but understood correctly by most (if not all) HTML parsers.

### YAML

YAML was designed to be human-readable and authored via a text editor with notion similar to reStructuredText and wiki syntax. YAML 1.2 also includes a shorthand notion that is compatible with JSON, and as such any JSON document is also valid YAML; this however does not hold the other way.

### REBOL

REBOL was designed to be human-readable and authored via a text editor. It uses a simple free-form syntax with minimal punctuation and a rich set of data types (such as URL, email, date and time, tuple, string, tag) that respect common standards. It is designed to not need any additional meta-language, being designed in a metacircular fashion which is why the parse dialect used for definitions and transformations of REBOL dialects is also itself a dialect of REBOL. REBOL was used as a source of inspiration for JSON.

### Gellish

Gellish English is a formalized subset of natural English (language), which includes a simple grammar and a large, extensible dictionary (taxonomy) that defines the general and domain specific terminology, whereas the concepts are arranged in a hierarchy, which supports inheritance of knowledge and requirements. The dictionary also includes standardized fact types. The terms and relation types together can be used to create and interpret expressions of facts, knowledge, requirements and other information. Gellish can be used in combination with SQL, RDF/XML, OWL and various other meta-languages. The Gellish standard is a combination of ISO 10303-221 (AP221) and ISO 15926.

### List

The following describes and compares popular data exchange languages.

Name

Schemas

Flexible

Semantic verification

Dictionary

Information Model

Synonyms and homonyms

Dialecting

Web standard

Trans-formations

Light-weight

Human readable

Compatibility

RDF

Yes

[1]

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Partial

Subset of

Semantic web

XML

Yes

[2]

Yes

No

No

No

No

Yes

Yes

Yes

No

Yes

subset of

SGML

,

HTML

Atom

Yes

Unknown

Unknown

Unknown

No

Unknown

Yes

Yes

Yes

No

No

XML

dialect

JSON

No

Unknown

Unknown

Unknown

No

Unknown

No

Yes

No

Yes

Yes

subset of

YAML

YAML

No

[3]

Unknown

Unknown

Unknown

No

Unknown

No

No

No

[3]

Yes

Yes

[4]

superset of

JSON

REBOL

Yes

[7]

Yes

No

Yes

No

Yes

Yes

No

Yes

[7]

Yes

Yes

[5]

Gellish

Yes

Yes

Yes

Yes

[8]

No

Yes

Yes

ISO

No

Yes

Partial

[6]

SQL, RDF/XML, OWL

**Columns**

- Schemas – Whether supports representing domain specific data structure definition
- Flexible – Whether supports extension of the semantic expression capabilities without modifying the schema
- Semantic verification – Whether supports semantic verification of the correctness of expressions in the language
- Dictionary – Whether includes a dictionary and a taxonomy (hierarchy) of concepts with inheritance
- Information model – Whether supports an information model
- Synonyms and homonyms – Whether supports the use of synonyms and homonyms in expressions
- Dialecting – Whether is available in multiple natural languages or dialects
- Web standard – Whether is standardized by a recognized body
- Transformations – Whether includes a translation to other standards
- Lightweight – Whether a lightweight version is available
- Human readable – Whether expressions are understandable without training
- Compatibility – Which other tools can be used or are required
