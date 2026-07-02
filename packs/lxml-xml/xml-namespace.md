---
title: "XML namespace"
source: https://en.wikipedia.org/wiki/XML_namespace
domain: lxml-xml
license: CC-BY-SA-4.0
tags: python lxml, lxml xml parsing, xpath python
fetched: 2026-07-02
---

# XML namespace

**XML namespaces** are used for providing uniquely named elements and attributes in an XML document. They are defined in a W3C recommendation. An XML instance may contain element or attribute names from more than one XML vocabulary. If each vocabulary is given a namespace, the ambiguity between identically named elements or attributes can be resolved.

A simple example would be to consider an XML instance that contained references to a customer and an ordered product. Both the customer element and the product element could have a child element named **id**. References to the **id** element would therefore be ambiguous; placing them in different namespaces would remove the ambiguity.

## Namespace names

A *namespace name* is a uniform resource identifier (URI). Typically, the URI chosen for the namespace of a given XML vocabulary describes a resource under the control of the author or organization defining the vocabulary, such as a URL for the author's Web server. However, the namespace specification does not require nor suggest that the namespace URI be used to retrieve information; it is simply treated by an XML parser as a string. For example, the document at http://www.w3.org/1999/xhtml itself does not contain any code. It simply describes the XHTML namespace to human readers. Using a URI (such as "http://www.w3.org/1999/xhtml") to identify a namespace, rather than a simple string (such as "xhtml"), reduces the probability of different namespaces using duplicate identifiers.

Although the term *namespace URI* is widespread, the W3C Recommendation refers to it as the *namespace name*. The specification is not entirely prescriptive about the precise rules for namespace names (it does not explicitly say that parsers must reject documents where the namespace name is not a valid Uniform Resource Identifier), and many XML parsers allow any character string to be used. In version 1.1 of the recommendation, the namespace name becomes an Internationalized Resource Identifier, which licenses the use of non-ASCII characters that in practice were already accepted by nearly all XML software. The term *namespace URI* persists, however, not only in popular usage, but also in many other specifications from W3C and elsewhere.

Following publication of the Namespaces recommendation, there was an intensive debate about how a relative URI should be handled, with some intensely arguing that it should simply be treated as a character string, and others arguing with conviction that it should be turned into an absolute URI by resolving it against the base URI of the document. The result of the debate was a ruling from W3C that relative URIs were deprecated.

The use of URIs taking the form of URLs in the http scheme (such as *http://www.w3.org/1999/xhtml*) is common, despite the absence of any formal relationship with the HTTP protocol. The Namespaces specification does not say what should happen if such a URL is dereferenced (that is, if software attempts to retrieve a document from this location). One convention adopted by some users is to place an RDDL document at the location. In general, however, users should assume that the namespace URI is simply a name, not the address of a document on the Web.

## Namespace declaration

An XML namespace is declared using the reserved XML attribute `xmlns` or `xmlns:*prefix*`, the value of which must be a valid namespace name.

For example, the following declaration maps the "xhtml:" prefix to the XHTML namespace:

```
xmlns:xhtml="http://www.w3.org/1999/xhtml"
```

Any element or attribute whose name starts with the prefix "xhtml:" is considered to be in the XHTML namespace, if it or an ancestor has the above namespace declaration.

It is also possible to declare a default namespace. For example:

```
xmlns="http://www.w3.org/1999/xhtml"
```

In this case, any element without a namespace prefix is considered to be in the XHTML namespace, if it or an ancestor has the above default namespace declaration.

If there is no default namespace declaration in scope, the namespace name has no value. In that case, an element without an explicit namespace prefix is considered not to be in any namespace.

Attributes are never subject to the default namespace. An attribute without an explicit namespace prefix is considered not to be in any namespace.

## Namespaces in APIs and XML object models

Different specifications have taken different approaches on how namespace information is presented to applications.

Nearly all programming models allow the name of an element or attribute node to be retrieved as a three-part name: the local name, the namespace prefix, and the namespace URI. Applications should avoid attaching any significance to the choice of prefix, but the information is provided because it can be helpful to human readers. Names are considered equal if the namespace URI and local name match.

In addition, most models provide some way of determining which namespaces have been declared for a given element. This information is needed because some XML vocabularies allow qualified names (containing namespace prefixes) to appear in the content of elements or attributes, as well as in their names. There are three main ways this information can be provided:

- As attribute nodes named "xmlns" or "xmlns:xxx", exactly as the namespaces are written in the source XML document. This is the model presented by DOM.
- As namespace declarations: distinguished from attributes, but corresponding one-to-one with the relevant attributes in the source XML document. This is the model presented by JDOM.
- As in-scope namespace bindings: in this model, the application is able to determine which namespaces are in scope for any given element, but is not able to determine which elements contain the actual declarations. This is the model used in XPath, XSLT, and XQuery.
