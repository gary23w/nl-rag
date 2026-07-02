---
title: "DOMParser - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/DOMParser
domain: dom-parsing-serialization
license: CC-BY-SA-4.0
tags: dom parsing serialization, domparser markup string, xml serializer output, inner html parsing
fetched: 2026-07-02
---

# DOMParser

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`DOMParser`** interface provides the ability to parse XML or HTML source code from a string into a DOM `Document`.

You can perform the opposite operation—converting a DOM tree into XML or HTML source—using the `XMLSerializer` interface.

In the case of an HTML document, you can also replace portions of the DOM with new DOM trees built from HTML by setting the value of the `Element.innerHTML` and `outerHTML` properties. These properties can also be read to fetch HTML fragments corresponding to the corresponding DOM subtree.

Note that `XMLHttpRequest` can parse XML and HTML directly from a URL-addressable resource, returning a `Document` in its `response` property.

**Note:** Be aware that block-level elements like `<p>` will be automatically closed if another block-level element is nested inside and therefore parsed before the closing `</p>` tag.

## Constructor

**`DOMParser()`**

Creates a new `DOMParser` object.

## Instance methods

**`DOMParser.parseFromString()`**

Parses an input `TrustedHTML` instance or string as HTML or XML and returns a `Document`.

## Examples

The documentation for `DOMParser.parseFromString()`, this interface's only method, contains examples for parsing XML, SVG, and HTML strings.

## Specifications

| Specification |
|---|
| HTML # dom-parsing-and-serialization |

## Browser compatibility
