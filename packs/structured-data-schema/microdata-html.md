---
title: "Microdata (HTML)"
source: https://en.wikipedia.org/wiki/Microdata_(HTML)
domain: structured-data-schema
license: CC-BY-SA-4.0
tags: structured data markup, schema microdata, json-ld linked data, rdfa annotation
fetched: 2026-07-02
---

# Microdata (HTML)

**Microdata** is a part of the WHATWG HTML specification that defines how to include metadata within existing web page content. Search engines, web crawlers, and browsers can extract and process Microdata from a web page and use it to provide a richer browsing experience for users. Search engines benefit greatly from direct access to Microdata because it allows them to understand the information on web pages and provide more relevant results to users. Microdata uses a supporting vocabulary to describe an item and name-value pairs to assign values to its properties. Microdata is an attempt to provide a simpler way of annotating HTML elements with machine-readable tags than the similar approaches of using RDFa and microformats.

In 2013, because the W3C HTML Working Group failed to find someone to serve as an editor for the **Microdata HTML** specification, its development was terminated with a 'Note'. However, since that time, two new editors were selected, and five newer versions of the working draft have been published, the most recent being Working Draft 26 April 2018.

## Vocabularies

Microdata vocabularies do not provide the semantics, or meaning of an Item. Web developers can design a custom vocabulary or use vocabularies available on the web. A collection of commonly used markup vocabularies are provided by Schema.org schemas which include: *Person*, "*Place*", *Event*, *Organization*, *Product*, *Review*, *Review-aggregate*, *Breadcrumb*, *Offer*, *Offer-aggregate*. The website schema.org was established by search engine operators like Google, Microsoft, Yahoo!, and Yandex, which use microdata markup to improve search results.

For some purposes, an ad-hoc vocabulary is adequate. For others, a vocabulary will need to be designed. Where possible, authors are encouraged to re-use existing vocabularies, as this makes content re-use easier.

## Localization

In some cases, search engines covering specific regions may provide locally-specific extensions of microdata. For example, Yandex, a major search engine in Russia, supports microformats such as hCard (company contact information), hRecipe (food recipe), hReview (market reviews) and hProduct (product data) and provides its own format for definition of the terms and encyclopedic articles. This extension was made in order to solve transliteration problems between the Cyrillic and Latin alphabets. After the implementation of additional parameters from Schema's vocabulary, indexation of information in Russian-language web-pages became more successful.

## Global attributes

- `itemscope` – Creates the Item and indicates that descendants of this element contain information about it.
- `itemtype` – A valid URL of a vocabulary that describes the item and its properties' context.
- `itemid` – Indicates a unique identifier of the item.
- `itemprop` – Indicates that its containing tag holds the value of the specified item property. The property's name and value context are described by the item's vocabulary. Properties values usually consist of string values, but can also use URLs using the `a` element and its `href` attribute, the `img` element and its `src` attribute, or other elements that link to or embed external resources.
- `itemref` – Properties that are not descendants of the element with the `itemscope` attribute can be associated with the item using this attribute. Provides a list of element IDs (not `itemid`s) with additional properties elsewhere in the document.
- `datetime` – Indicates date or duration as specified by ISO 8601 standard.

## Example

The following HTML5 markup may be found on a typical “About” page containing information about a person:

```mw
<div> Hello, my name is John Doe, I am a graduate research assistant at
the University of Dreams.
My friends call me Johnny. 
You can visit my homepage at <a href="http://www.example.com/~JohnnyD">www.example.com/~JohnnyD</a>.
I live at 1234 Peach Drive, Warner Robins, Georgia.</div>
```

Here is the same markup with added Schema.org Microdata:

```mw
<div itemscope itemtype="http://schema.org/Person"> 
	Hello, my name is 
	<span itemprop="name">John Doe</span>, 
	I am a 
	<span itemprop="jobTitle">graduate research assistant</span> 
	at the 
	<span itemprop="affiliation">University of Dreams</span>. 
	My friends call me 
	<span itemprop="additionalName">Johnny</span>. 
	You can visit my homepage at 
	<a href="http://www.example.com/~JohnnyD" itemprop="url">www.example.com/~JohnnyD</a>. 
	<div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
		I live at 
		<span itemprop="streetAddress">1234 Peach Drive</span>,
		<span itemprop="addressLocality">Warner Robins</span>,
		<span itemprop="addressRegion">Georgia</span>.
	</div>
</div>
```

As the above example shows, Microdata items can be nested. In this case, an item of type http://schema.org/PostalAddress is nested inside an item of type http://schema.org/Person.

The following text shows how Google parses the Microdata from the above example code. Developers can test pages containing Microdata using Google's *Rich Snippet Testing Tool*.

```
Item
   Type: http://schema.org/Person
   name = John Doe
   jobTitle = graduate research assistant
   affiliation = University of Dreams
   additionalName = Johnny
   url = http://www.example.com/~JohnnyD
   address = Item(1)
Item 1
   Type: http://schema.org/PostalAddress
   streetAddress = 1234 Peach Drive
   addressLocality = Warner Robins
   addressRegion = Georgia
```

The same machine-readable terms can be used not only in HTML Microdata, but also in other annotations such as RDFa or JSON-LD in the markup, or in an external RDF file in a serialization such as RDF/XML, Notation3, or Turtle.

## Support

- Servers: Google can use microdata in its result pages. It was the preferred snippet format for the Google+ social network.
- Browsers: As of July 2021, no major browser supports the Microdata DOM API. Opera supported it from 11.60 (released in 2011), but since removed its implementation. Firefox removed it in version 49.
