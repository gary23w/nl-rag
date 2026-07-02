---
title: "XSL - Wikipedia"
source: https://en.wikipedia.org/wiki/XSL
domain: xslt-stylesheet
license: CC-BY-SA-4.0
tags: xslt stylesheet, xsl transformations, xml stylesheet language, xpath expressions
fetched: 2026-07-02
---

# XSL

In computing, the term **Extensible Stylesheet Language** (**XSL**) is used to refer to a family of languages used to transform and render XML documents (e.g., XSL is used to determine how to display a XML document as a webpage).

Historically, the W3C XSL Working Group produced a draft specification under the name "XSL", which eventually split into three parts:

1. XSL Transformation (XSLT): an XML language for transforming XML documents
2. XSL Formatting Objects (XSL-FO): an XML language for specifying the visual formatting of an XML document
3. XML Path Language (XPath): a non-XML language used by XSLT, and also available for use in non-XSLT contexts, for addressing the parts of an XML document.

As a result, the term "XSL" is now used with a number of different meanings:

- Sometimes it refers to XSLT: this usage is best avoided. However, "xsl" is used both as the conventional namespace prefix for the XSLT namespace, and as the conventional filename suffix for files containing XSLT stylesheet modules
- Sometimes it refers to XSL-FO: this usage can be justified by the fact that the XSL-FO specification carries the title *Extensible Stylesheet Language (XSL)*; however, the term XSL-FO is less likely to be misunderstood
- Sometimes it refers to both languages considered together, or to the working group that developed both languages
- Sometimes, especially in the Microsoft world, it refers to a now-obsolete variant of XSLT developed and shipped by Microsoft as part of MSXML before the W3C specification was finalized

## History

XSL began as an attempt to bring the functionality of DSSSL, particularly in the area of print and high-end typesetting, to XML.

In response to a submission from Arbortext, Inso, and Microsoft, a W3C working group on *XSL* started operating in December 1997, with Sharon Adler and Steve Zilles as co-chairs, with James Clark acting as editor (and unofficially as chief designer), and Chris Lilley as the W3C staff contact. The group released a first public Working Draft on 18 August 1998. XSLT and XPath became W3C Recommendations on 16 November 1999 and XSL-FO reached Recommendation status on 15 October 2001.

## The XSL family

### XSL Transformations

The original version of XSLT (1.0) was published in November 1999, and was widely implemented. Some of the early implementations have fallen into disuse, but notable implementations actively used in 2023 include those integrated into the mainstream web browsers, as well as Altova's RaptorXML, libxslt, Saxon, the Microsoft .NET implementation **System.Xml.Xsl**, and Xalan which is integrated into the Oracle JVM. These products all have a high level of conformance to the specification, though they also offer proprietary vendor extensions, and some of them omit support for optional features such as disable-output-escaping.

Subsequent versions of XSLT include XSLT 2.0 (January 2007) and XSLT 3.0 (June 2017); there is work in progress on a version 4.0. These versions have not been as widely implemented as 1.0: the main implementations in widespread use in 2023 are Saxon (available in various versions for different platforms, including web browsers), and Altova's RaptorXML.

### XSL Formatting Objects

Support for XSL Formatting Objects is available in a number of products:

- the XEP package from RenderX has near 100% support for XSL-FO 1.0
- XSLFormatter from Antenna House also has near 100% support for the XSL-FO 1.0 specification and has 100% support for all new features within the XSL-FO 1.1 specification
- XINC from Lunasil has a great amount of support for the XSL-FO 1.0 specification
- FOP from the Apache project can render a portion of the XSL formatting objects 1.0 specification to PDF
- XML2PDF Formatting Engine Server from AltSoft has near 100% support for the XSL-FO 1.1

These products support output in a number of file formats, to varying degrees:

- Portable Document Format
- PostScript
- SVG
- MIF
- PCL
- text files

### XPath

XML Path Language (XPath), itself part of the XSL family, functions within XSLT as a means of navigating an XML document.

Another W3C project, XQuery, aims to provide similar capabilities for querying XML documents using XPath.
