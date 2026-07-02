---
title: "XSL Formatting Objects"
source: https://en.wikipedia.org/wiki/XSL_Formatting_Objects
domain: xslt-transform
license: CC-BY-SA-4.0
tags: xslt transformation, xsl transformations, xml transformation language, stylesheet transformation
fetched: 2026-07-02
---

# XSL Formatting Objects

**XSL-FO** (**XSL Formatting Objects**) is a markup language for XML document formatting that is most often used to generate PDF files. XSL-FO is part of XSL (Extensible Stylesheet Language), a set of W3C technologies designed for the transformation and formatting of XML data. The other parts of XSL are XSLT and XPath. Version 1.1 of XSL-FO was published in 2006.

XSL-FO is considered feature complete by W3C: the last update for the Working Draft was in January 2012, and its Working Group closed in November 2013.

## Basics

Unlike the combination of HTML and CSS, XSL-FO is a unified presentational language. It has no semantic markup as this term is used in HTML. And, unlike CSS which modifies the default presentation of an external XML or HTML document, it stores all of the document's data within itself.

The general idea behind XSL-FO's use is that the user writes a document, not in FO, but in an XML language. XHTML, DocBook, and TEI are all possible examples. Then, the user obtains an XSLT transform, either by writing one themselves or by finding one for the document type in question. This XSLT transform converts the XML into XSL-FO.

Once the XSL-FO document is generated, it is then passed to an application called an FO processor. FO processors convert the XSL-FO document into something that is readable, printable or both. The most common output of XSL-FO is a PDF file or as PostScript, but some FO processors can output to other formats like RTF files or even just a window in the user's GUI displaying the sequence of pages and their contents.

The XSLT language itself was originally conceived only for this purpose; it is now in widespread use for more general XML transformations. This transformation step is taken so much for granted in XSL-FO that it is not uncommon for people to call the XSLT that turns XML into XSL-FO the actual XSL-FO document itself. Even tutorials on XSL-FO tend to be written with XSLT commands around the FO processing instructions.

The XSLT transformation step is exceptionally powerful. It allows for the automatic generation of a table of contents, linked references, an index, and various other possibilities.

An XSL-FO document is not like a PDF or a PostScript document. It does not definitively describe the layout of the text on various pages. Instead, it describes what the pages look like and where the various contents go. From there, an FO processor determines how to position the text within the boundaries described by the FO document. The XSL-FO specification even allows different FO processors to have varying responses with regard to the resultant generated pages.

For example, some FO processors can hyphenate words to minimize space when breaking a line, while others choose not to. Different processors may even use different hyphenation algorithms, ranging from very simple to more complex hyphenation algorithms that take into account whether the previous or next line also is hyphenated. These will change, in some borderline cases quite substantially, the layout of the various pages. There are other cases where the XSL-FO specification explicitly allows FO processors some degree of choice with regard to layout.

This differentiation between FO processors, creating inconsistent results between processors is often not a concern. This is because the general purpose behind XSL-FO is to generate paged, printed media. XSL-FO documents themselves are usually used as intermediaries, mostly to generate either PDF files or a printed document as the final form to be distributed. This is as opposed to how HTML is generated and distributed as a final form directly to the user. Distributing the final PDF rather than the formatting language input (whether HTML/CSS or XSL-FO) means on the one hand that recipients aren't affected by the unpredictability resulting from differences among formatting language interpreters, while on the other hand means that the document cannot easily adapt to different recipient needs, such as different page size or preferred font size, or tailoring for on-screen versus on-paper versus audio presentation.

## Language concepts

The XSL-FO language was designed for paged media; as such, the concept of pages is an integral part of XSL-FO's structure.

FO works best for what could be called "content-driven" design. This is the standard method of layout for books, articles, legal documents, and so forth. It involves a single flowing span of fairly contiguous text, with various repeating information built into the margins of a page. This is as opposed to "layout-driven" design, which is used in newspapers or magazines. If content in those documents does not fit in the required space, some of it is trimmed away until it does fit. XSL-FO does not easily handle the tight restrictions of magazine layout; indeed, in many cases, it lacks the ability to express some forms of said layout.

Despite the basic nature of the language's design, it is capable of a great deal of expressiveness. Tables, lists, side floats, and a variety of other features are available. These features are comparable to CSS's layout features, though some of those features are expected to be built by the XSLT.

## Document structure

XSL-FO documents are XML documents, but they do not have to conform to any DTD or schema. Instead, they conform to a syntax defined in the XSL-FO specification.

XSL-FO documents contain two required sections. The first section details a list of named page layouts. The second section is a list of document data, with markup, that uses the various page layouts to determine how the content fills the various pages.

Page layouts define the properties of the page. They can define the directions for the flow of text, so as to match the conventions for the language in question. They define the size of a page as well as the margins of that page. More importantly, they can define sequences of pages that allow for effects where the odd and even pages look different. For example, one can define a page layout sequence that gives extra space to the inner margins for printing purposes; this allows more space to be given to the margin where the book will be bound.

The document data portion is broken up into a sequence of flows, where each flow is attached to a page layout. The flows contain a list of blocks which, in turn, each contain a list of text data, inline markup elements, or a combination of the two. Content may also be added to the margins of the document, for page numbers, chapter headings and the like.

Blocks and inline elements function in much the same way as for CSS, though some of the rules for padding and margins differ between FO and CSS. The direction, relative to the page orientation, for the progression of blocks and inlines can be fully specified, thus allowing FO documents to function under languages that are read different from English. The language of the FO specification, unlike that of CSS 2.1, uses direction-neutral terms like start and end rather than left and right when describing these directions.

XSL-FO's basic content markup is derived from CSS and its cascading rules. As such, many attributes in XSL-FO propagate into the child elements unless explicitly overridden.

## Capabilities of XSL-FO v1.0

XSL-FO is capable of a great deal of textual layout functionality. In addition to the information as specified above, XSL-FO's language allows for the specification of the following.

### Multiple columns

A page can be defined to have multiple columns. When this is the case, blocks flow from one column into the next by default. Individual blocks can be set to span all columns, creating a textual break in the page. The columns above this break will flow into each other, as will the columns below the break. But no text is allowed to flow from the above section to the below section.

Because of the nature of XSL-FO's page specification, multiple pages may actually have different numbers and widths of columns. As such, text can flow from a 3 column page to a 5 column page to a 1 column page quite easily.

All FO features work within the restrictions of a multi-column page.

We can span multiple columns by specifying two attributes i.e.,. span, padding-after .

### Lists

An XSL-FO list is, essentially, two sets of blocks stacked side by side. An entry consists of a block on the "left", or start inline direction, and a block sequence on the "right", or end inline direction. The block on the left is conceptually what would be the number or bullet in a list. However, it could just as easily be a string of text, as one might see in a glossary entry. The block on the right works as expected. Both of these blocks can be block containers, or have multiple blocks in a single list entry.

Numbering of XSL-FO lists, when they are numbered, is expected to be done by the XSLT, or whatever other process, that generated the XSL-FO document. As such, number lists are to be explicitly numbered in XSL-FO.

The user can specify Widow and Orphan for blocks or for the flow itself, and allow the attributes to cascade into child blocks. Additionally, blocks can be specified to be kept together on a single page. For example, an image block and the description of that image can be set to never be separated. The FO processor will do its best to adhere to these commands, even if it requires creating a great deal of empty space on a page.
