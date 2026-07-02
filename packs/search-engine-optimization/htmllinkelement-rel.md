---
title: "HTMLLinkElement: rel property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLLinkElement/rel
domain: search-engine-optimization
license: CC-BY-SA-4.0
tags: search engine optimization, meta description tag, canonical link relation, web crawler indexing
fetched: 2026-07-02
---

# HTMLLinkElement: rel property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`rel`** property of the `HTMLLinkElement` interface reflects the `rel` attribute. It is a string containing a space-separated list of link types indicating the relationship between the resource represented by the `<link>` element and the current document.

The most common use of this attribute is to specify a link to an external style sheet: the property is set to `stylesheet`, and the `href` attribute is set to the URL of an external style sheet to format the page.

## Value

A string.

## Examples

```js
const links = document.getElementsByTagName("link");
for (const link of links) {
  console.log(link);
}
```

## Specifications

| Specification |
|---|
| HTML # dom-link-rel |

## Browser compatibility
