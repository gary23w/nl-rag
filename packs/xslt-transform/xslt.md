---
title: "XSLT"
source: https://en.wikipedia.org/wiki/XSLT
domain: xslt-transform
license: CC-BY-SA-4.0
tags: xslt transformation, xsl transformations, xml transformation language, stylesheet transformation
fetched: 2026-07-02
---

# XSLT

**XSLT** (**Extensible Stylesheet Language Transformations**) is a language originally designed for transforming XML documents into other XML documents, or other formats such as HTML for web pages, plain text, or XSL Formatting Objects. These formats can be subsequently converted to formats such as PDF, PostScript, and PNG. Support for JSON and plain-text transformation was added in later updates to the XSLT 1.0 specification.

XSLT 3.0 implementations support Java, .NET, C/C++, Python, PHP and NodeJS. An XSLT 3.0 JavaScript library can also be hosted within the web browser. Modern web browsers also include native support for XSLT 1.0. XSLT has become obsolete in the browser due to better technologies. Google Chrome will remove its XSLT implementation to make the browser more secure.

The XSLT document transformation specifies how to transform an XML document into new document (usually XML, but other formats, such as plain text are supported). Typically, input documents are XML files, but anything from which the processor can build an XQuery and XPath Data Model can be used, such as relational database tables or geographical information systems.

While XSLT was originally designed as a special-purpose language for XML transformation, the language is Turing-complete, making it theoretically capable of arbitrary computations.

## History

XSLT is influenced by functional languages, and by text-based pattern matching languages like SNOBOL and AWK. Its most direct predecessor is DSSSL, which did for SGML what XSLT does for XML.

- XSLT 1.0: XSLT was part of the World Wide Web Consortium (W3C)'s eXtensible Stylesheet Language (XSL) development effort of 1998–1999, a project that also produced XSL-FO and XPath. Some members of the standards committee that developed XSLT, including James Clark, the editor, had previously worked on DSSSL. XSLT 1.0 was published as a W3C recommendation in November 1999. Despite its age, XSLT 1.0 is still widely used (as of 2018), since later versions are not supported natively in web browsers or for environments like LAMP.
- XSLT 2.0: after an abortive attempt to create a version 1.1 in 2001, the XSL working group joined forces with the XQuery working group to create XPath 2.0, with a richer data model and type system based on XML Schema. Building on this is XSLT 2.0, developed under the editorship of Michael Kay, which reached recommendation status in January 2007. The most important innovations in XSLT 2.0 include:
  - String manipulation using regular expressions
  - Functions and operators for manipulating dates, times, and durations
  - Multiple output documents
  - Grouping (creating hierarchic structure from flat input sequences)
  - A richer type system and stronger type checking
- XSLT 3.0: became a W3C Recommendation on 8 June 2017. The main new features are:
  - Streaming transformations: in previous versions the entire input document had to be read into memory before it could be processed, and output could not be written until processing had finished. XSLT 3.0 allows XML streaming which is useful for processing documents too large to fit in memory or when transformations are chained in XML Pipelines.
  - Packages, to improve the modularity of large stylesheets.
  - Improved handling of dynamic errors with, for example, an xsl:try instruction.
  - Support for maps and arrays, enabling XSLT to handle JSON as well as XML.
  - Functions can now be arguments to other (higher-order) functions.

## Design and processing model

The XSLT processor takes one or more XML source documents, plus one or more XSLT stylesheets, and processes them to produce one or multiple output documents. In contrast to widely implemented imperative programming languages like C, XSLT is declarative. The basic processing paradigm is pattern matching. Rather than listing an imperative sequence of actions to perform in a stateful environment, template rules only define how to handle a node matching a particular XPath-like pattern, if the processor should happen to encounter one, and the contents of the templates effectively comprise functional expressions that directly represent their evaluated form: the result tree, which is the basis of the processor's output.

A typical processor behaves as follows. First, assuming a stylesheet has already been read and prepared, the processor builds a source tree from the input XML document. It then processes the source tree's root node, finds the best-matching template for that node in the stylesheet, and evaluates the template's contents. Instructions in each template generally direct the processor to either create nodes in the result tree, or to process more nodes in the source tree in the same way as the root node. Finally the result tree is serialized as XML or HTML text.

## XPath

XSLT uses XPath to identify subsets of the source document tree and perform calculations. XPath also provides a range of functions, which XSLT itself further augments.

XSLT 1.0 uses XPath 1.0, while XSLT 2.0 uses XPath 2.0. XSLT 3.0 will work with either XPath 3.0 or 3.1. In the case of 1.0 and 2.0, the XSLT and XPath specifications were published on the same date. With 3.0, however, they were no longer synchronized; XPath 3.0 became a Recommendation in April 2014, followed by XPath 3.1 in February 2017; XSLT 3.0 followed in June 2017.

## XQuery compared

XSLT functionalities overlap with those of XQuery, which was initially conceived as a query language for large collections of XML documents.

The XSLT 2.0 and XQuery 1.0 standards were developed by separate working groups within W3C, working together to ensure a common approach where appropriate. They share the same data model, type system, and function library, and both include XPath 2.0 as a sublanguage.

The two languages, however, are rooted in different traditions and serve the needs of different communities. XSLT was primarily conceived as a stylesheet language whose primary goal was to render XML for the human reader on screen, on the web (as a web template language), or on paper. XQuery was primarily conceived as a database query language in the tradition of SQL.

Because the two languages originate in different communities, XSLT is stronger in its handling of narrative documents with more flexible structure, while XQuery is stronger in its data handling, for example when performing relational joins.

## Media types

The `<output>` element can optionally take the attribute `media-type`, which allows one to set the media type (or MIME type) for the resulting output, for example: `<xsl:output output="xml" media-type="application/xml"/>`. The XSLT 1.0 recommendation recommends the more general attribute types `text/xml` and `application/xml` since for a long time there was no registered media type for XSLT. During this time `text/xsl` became the de facto standard. In XSLT 1.0 it was not specified how the `media-type` values should be used.

With the release of the XSLT 2.0, the W3C recommended in 2007 the registration of the MIME media type `application/xslt+xml` and it was later registered with the Internet Assigned Numbers Authority.

Pre-1.0 working drafts of XSLT used `text/xsl` in their embedding examples, and this type was implemented and continued to be promoted by Microsoft in Internet Explorer and MSXML circa 2012. It is also widely recognized in the `xml-stylesheet` processing instruction by other browsers. In practice, therefore, users wanting to control transformation in the browser using this processing instruction were obliged to use this unregistered media type.

## Examples

These examples use the following incoming XML document:

```mw
<?xml version="1.0" ?>
<persons>
  <person username="JS1">
    <name>John</name>
    <family-name>Smith</family-name>
  </person>
  <person username="MI1">
    <name>Morka</name>
    <family-name>Ismincius</family-name>
  </person>
</persons>
```

### Example 1 (transforming XML to XML)

This XSLT stylesheet provides templates to transform the XML document:

```mw
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/persons">
    <root>
      <xsl:apply-templates select="person"/>
    </root>
  </xsl:template>

  <xsl:template match="person">
    <name username="{@username}">
      <xsl:value-of select="name" />
    </name>
  </xsl:template>

</xsl:stylesheet>
```

Its evaluation results in a new XML document, having another structure:

```mw
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <name username="JS1">John</name>
  <name username="MI1">Morka</name>
</root>
```

### Example 2 (transforming XML to XHTML)

Processing the following example XSLT file

```mw
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns="http://www.w3.org/1999/xhtml">

  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>

  <xsl:template match="/persons">
    <html>
      <head> <title>Testing XML Example</title> </head>
      <body>
        <h1>Persons</h1>
        <ul>
          <xsl:apply-templates select="person">
            <xsl:sort select="family-name" />
          </xsl:apply-templates>
        </ul>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="person">
    <li>
      <xsl:value-of select="family-name"/><xsl:text>, </xsl:text><xsl:value-of select="name"/>
    </li>
  </xsl:template>

</xsl:stylesheet>
```

with the XML input file shown above results in the following XHTML (whitespace has been adjusted here for clarity):

```mw
<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head> <title>Testing XML Example</title> </head>
  <body>
    <h1>Persons</h1>
      <ul>
        <li>Ismincius, Morka</li>
        <li>Smith, John</li>
      </ul>
  </body>
</html>
```

This XHTML generates the output below when rendered in a web browser.

In order for a web browser to be able to apply an XSL transformation to an XML document on display, an XML stylesheet processing instruction can be inserted into XML. So, for example, if the stylesheet in Example 2 above were available as "example2.xsl", the following instruction could be added to the original incoming XML:

```mw
<?xml-stylesheet href="example2.xsl" type="text/xsl" ?>
```

In this example, `text/xsl` is technically incorrect according to the W3C specifications (which say the type should be `application/xslt+xml`), but it is the only media type that is widely supported across browsers as of 2009, and the situation is unchanged in 2021.

## Processor implementations

- RaptorXML from Altova is an XSLT 3.0 processor available in the XMLSpy development toolkit and as a free-standing server implementation, invoked using a REST interface.
- IBM offers XSLT processing embedded in a special-purpose hardware appliance under the Datapower brand.
- libxslt is a free library released under the MIT License that can be reused in commercial applications. It is based on libxml and implemented in C for speed and portability. It supports XSLT 1.0 and EXSLT extensions.
  - It can be used at the command line via xsltproc which is included in macOS and many Linux distributions, and can be used on Windows via Cygwin.
  - The WebKit and Blink layout engines, used for example in the Safari and Chrome web browsers respectively, uses the libxslt library to do XSL transformations.
  - Bindings exist for Python, Perl, Ruby, PHP, Common Lisp, Tcl, and C++.
- Microsoft provides two XSLT processors (both XSLT 1.0 only). The earlier processor MSXML provides COM interfaces; from MSXML 4.0 it also includes the command line utility `msxsl.exe`. The .NET runtime includes a separate built-in XSLT processor in its `System.Xml.Xsl` library.
- Saxon is an XSLT 3.0 and XQuery 3.1 processor with open-source and proprietary versions for stand-alone operation and for Java, JavaScript and .NET. A separate product Saxon-JS offers XSLT 3.0 processing on Node.js and in the browser.
- xjslt is an open-source XSLT 2.0 compiler for JavaScript supporting Node.js and the browser.
- Xalan is an open source XSLT 1.0 processor from the Apache Software Foundation available for Java and C++. A variant of the Xalan processor is included as the default XSLT processor in the standard Java distribution from Oracle.
- Web browsers: Safari, Chrome (removal in progress), Firefox, Opera and Internet Explorer all support XSLT 1.0 (only).

### Performance

Most early XSLT processors were interpreters. More recently, code generation is increasingly common, using portable intermediate languages (such as Java bytecode or .NET Common Intermediate Language) as the target. However, even the interpretive products generally offer separate analysis and execution phases, allowing an optimized expression tree to be created in memory and reused to perform multiple transformations. This gives substantial performance benefits in online publishing applications, where the same transformation is applied many times per second to different source documents. This separation is reflected in the design of XSLT processing APIs (such as JAXP).

Early XSLT processors had very few optimizations. Stylesheet documents were read into Document Object Models and the processor would act on them directly. XPath engines were also not optimized. Increasingly, however, XSLT processors use optimization techniques found in functional programming languages and database query languages, such as static rewriting of an expression tree (e.g., to move calculations out of loops), and lazy pipelined evaluation to reduce the memory footprint of intermediate results (and allow "early exit" when the processor can evaluate an expression such as `following-sibling::*[1]` without a complete evaluation of all subexpressions). Many processors also use tree representations that are significantly more efficient (in both space and time) than general-purpose DOM implementations.

In June 2014, Debbie Lockett and Michael Kay introduced an open-source benchmarking framework for XSLT processors called XT-Speedo.
