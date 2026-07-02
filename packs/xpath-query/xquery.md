---
title: "XQuery"
source: https://en.wikipedia.org/wiki/XQuery
domain: xpath-query
license: CC-BY-SA-4.0
tags: xpath query, xml path language, xml node selection, xpath expression
fetched: 2026-07-02
---

# XQuery

**XQuery** (**XML Query**) is a query language and functional programming language designed to query and transform collections of structured and unstructured data, primarily in the form of XML. It also supports text data and, through implementation-specific extensions, other formats like binary and relational data.

The language was developed by the XML Query working group of the W3C, with version 1.0 becoming a W3C Recommendation in January 2007. XQuery development is closely coordinated with the development of XSLT by the XSL Working Group. Both groups jointly maintain XPath, a shared component of XQuery and XSLT. XQuery extends XPath with features like FLWOR (For, Let, Where, Order by, Return) expressions, making it semantically similar to SQL but optimized for hierarchical rather than relational data.

XQuery 3.1, published in March 2017, added support for JSON and introduced maps, arrays, and additional higher-order functions, significantly expanding the language's capabilities for modern data processing.

XQuery is implemented by many database systems, XML databases, and XML processors, including BaseX, eXist, MarkLogic, Saxon, and Berkeley DB XML, making it a cornerstone technology for processing XML data in enterprise software applications.

## Features

XQuery's mission is to:

> "provide flexible query facilities to extract data from real and virtual documents on the World Wide Web, therefore finally providing the needed interaction between the Web world and the database world. Ultimately, collections of XML files will be accessed like databases."

It is a functional, side effect-free, expression-oriented programming language with a simple type system, summed up by Kilpeläinen:

> All XQuery expressions operate on sequences, and evaluate to sequences. *Sequences* are ordered lists of items. *Items* can be either *nodes*, which represent components of XML documents, or *atomic values*, which are instances of XML Schema base types like xs:integer or xs:string. Sequences can also be empty, or consist of a single item only. No distinction is made between a single item and a singleton sequence. (...) XQuery/XPath sequences differ from lists in languages like Lisp and Prolog by excluding nested sequences. Designers of XQuery may have considered nested sequences unnecessary for the manipulation of document contents. Nesting, or hierarchy of document structures is instead represented by nodes and their child-parent relationships

XQuery provides the means to extract and manipulate data from XML documents or any data source that can be viewed as XML, such as relational databases or office documents.

XQuery contains a superset of XPath expression syntax to address specific parts of an XML document. It supplements this with a SQL-like "FLWOR expression" for performing joins. A FLWOR expression is constructed from the five clauses after which it is named: FOR, LET, WHERE, ORDER BY, RETURN.

The language also provides syntax allowing new XML documents to be constructed. Where the element and attribute names are known in advance, an XML-like syntax can be used; in other cases, expressions referred to as dynamic node constructors are available. All these constructs are defined as expressions within the language, and can be arbitrarily nested.

The language is based on the XQuery and XPath Data Model (XDM) which uses a tree-structured model of the information content of an XML document, containing seven kinds of nodes: document nodes, elements, attributes, text nodes, comments, processing instructions, and namespaces.

XDM also models all values as sequences (a singleton value is considered to be a sequence of length one). The items in a sequence can either be XML nodes or atomic values. Atomic values may be integers, strings, Booleans, and so on: the full list of types is based on the primitive types defined in XML Schema.

Features for updating XML documents or databases, and full text search capability, are not part of the core language, but are defined in add-on extension standards: XQuery Update Facility 1.0 supports update feature and XQuery and XPath Full Text 1.0 supports full text search in XML documents.

XQuery 3.0 adds support for full functional programming, in that functions are values that can be manipulated (stored in variables, passed to higher-order functions, and dynamically called).

## Examples

The sample XQuery code below lists the unique speakers in each act of Shakespeare's play Hamlet, encoded in hamlet.xml

```mw
<html>
<body>
{
  for $act in doc("hamlet.xml")//ACT
  let $speakers := distinct-values($act//SPEAKER)
  return
    <div>
      <h1>{ string($act/TITLE) }</h1>
      <ul>
      {
        for $speaker in $speakers
        return <li>{ $speaker }</li>
      }
      </ul>
    </div>
}
</body>
</html>
```

All XQuery constructs for performing computations are expressions. There are no statements, even though some of the keywords appear to suggest statement-like behaviors. To execute a function, the expression within the body is evaluated and its value is returned. Thus to write a function to double an input value, one simply writes:

```mw
declare function local:doubler($x) { $x * 2 }
```

To write a full query saying 'Hello World', one writes the expression:

```mw
"Hello World"
```

This style is common in functional programming languages.

## Applications

Below are a few examples of how XQuery can be used:

1. Extracting information from a database for use in a web service.
2. Generating summary reports on data stored in an XML database.
3. Searching textual documents on the Web for relevant information and compiling the results.
4. Selecting and transforming XML data to XHTML to be published on the Web.
5. Pulling data from databases to be used for the application integration.
6. Splitting up an XML document that represents multiple transactions into multiple XML documents.

## XQuery and XSLT compared

### Scope

Although XQuery was initially conceived as a query language for large collections of XML documents, it is also capable of transforming individual documents. As such, its capabilities overlap with XSLT, which was designed expressly to allow input XML documents to be transformed into HTML or other formats.

The XSLT 2.0 and XQuery standards were developed by separate working groups within W3C, working together to ensure a common approach where appropriate. They share the same data model (XDM), type system, and function library, and both include XPath 2.0 as a sublanguage.

### Origin

The two languages, however, are rooted in different traditions and serve the needs of different communities. XSLT was primarily conceived as a stylesheet language whose primary goal was to render XML for the human reader on screen, on the web (as web template language), or on paper. XQuery was primarily conceived as a database query language in the tradition of SQL.

Because the two languages originate in different communities, XSLT is stronger in its handling of narrative documents with more flexible structure, while XQuery is stronger in its data handling (for example, when performing relational joins).

### Versions

XSLT 1.0 appeared as a Recommendation in 1999, whereas XQuery 1.0 only became a Recommendation in early 2007; as a result, XSLT is still much more widely used. Both languages have similar expressive power, though XSLT 2.0 has many features that are missing from XQuery 1.0, such as grouping, number and date formatting, and greater control over XML namespaces. Many of these features were planned for XQuery 3.0.

Any comparison must take into account the version of XSLT. XSLT 1.0 and XSLT 2.0 are very different languages. XSLT 2.0, in particular, has been heavily influenced by XQuery in its move to strong typing and schema-awareness.

### Strengths and weaknesses

Usability studies have shown that XQuery is easier to learn than XSLT, especially for users with previous experience of database languages such as SQL. This can be attributed to the fact that XQuery is a smaller language with fewer concepts to learn, and to the fact that programs are more concise. It is also true that XQuery is more orthogonal, in that any expression can be used in any syntactic context. By contrast, XSLT is a two-language system in which XPath expressions can be nested in XSLT instructions but not vice versa.

XSLT is currently stronger than XQuery for applications that involve making small changes to a document (for example, deleting all the NOTE elements). Such applications are generally handled in XSLT by use of a coding pattern that involves an identity template that copies all nodes unchanged, modified by specific templates that modify selected nodes. XQuery has no equivalent to this coding pattern, though in future versions it will be possible to tackle such problems using the update facilities in the language that are under development.

XQuery 1.0 lacked any kind of mechanism for dynamic binding or polymorphism; this has been remedied with the introduction of functions as first-class values in XQuery 3.0. The absence of this capability starts to become noticeable when writing large applications, or when writing code that is designed to be reusable in different environments. XSLT offers two complementary mechanisms in this area: the dynamic matching of template rules, and the ability to override rules using `xsl:import`, that make it possible to write applications with multiple customization layers.

The absence of these facilities from XQuery 1.0 was a deliberate design decision: it has the consequence that XQuery is very amenable to static analysis, which is essential to achieve the level of optimization needed in database query languages. This also makes it easier to detect errors in XQuery code at compile time.

The fact that XSLT 2.0 uses XML syntax makes it rather verbose in comparison to XQuery 1.0. However, many large applications take advantage of this capability by using XSLT to read, write, or modify stylesheets dynamically as part of a processing pipeline. The use of XML syntax also enables the use of XML-based tools for managing XSLT code. By contrast, XQuery syntax is more suitable for embedding in traditional programming languages such as Java (see XQuery API for Java) or C#. If necessary, XQuery code can also be expressed in an XML syntax called XQueryX. The XQueryX representation of XQuery code is rather verbose and not convenient for humans, but can easily be processed with XML tools, for example transformed with XSLT stylesheets.

## Versions and extensions

### Versions

- **XQuery 1.0** became a W3C Recommendation on January 23, 2007.
- **XQuery 3.0** became a W3C Recommendation on April 8, 2014.
- **XQuery 3.1** became a W3C Recommendation on March 21, 2017.

### W3C extensions

The World Wide Web Consortium (W3C) developed two major extensions to XQuery:

- XQuery 1.0 and XPath 2.0 Full-Text, which extends XQuery with full-text search capabilities
- XQuery Update Facility, which enables data modification in XQuery

Both became W3C Recommendations as extensions to XQuery 1.0. Efforts to adapt them for XQuery 3.0 were abandoned due to resource constraints.

A scripting (procedural) extension for XQuery was proposed but never completed.

The EXPath Community Group develops extensions for XQuery and related standards (XPath, XSLT, XProc, and XForms). The following extensions are available:

- **Packaging System**, for managing XQuery libraries and modules.
- **File Module**, for file system operations.
- **Binary Module**, for handling binary data.
- **Web Applications**, for building web-based applications

### Third-party extensions

JSONiq is an extension of XQuery that adds support to extract and transform data from JSON documents. JSONiq is a superset of XQuery 3.0. It is published under the Creative Commons Attribution-ShareAlike 3.0 license.

XQuery 3.1 de facto deprecates JSONiq as it has added full support for JSON.

The EXQuery project develops standards around creating portable XQuery applications. The following standards are currently available:

- RESTXQ
