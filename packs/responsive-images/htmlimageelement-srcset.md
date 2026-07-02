---
title: "HTMLImageElement: srcset property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/srcset
domain: responsive-images
license: CC-BY-SA-4.0
tags: responsive images, srcset image candidates, image-set css function, adaptive image sizes
fetched: 2026-07-02
---

# HTMLImageElement: srcset property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`srcset`** property of the `HTMLImageElement` interface identifies one or more *image candidate strings*, separated using commas (`,`), each specifying image resources to use under given circumstances. Each image candidate string contains an image URL and an optional width or pixel density descriptor that indicates the conditions under which that candidate should be used instead of the image specified by the `src` property. It reflects the `<img>` element's `srcset` content attribute.

The `srcset` property, along with the `sizes` property, are a crucial component in designing responsive websites, as they can be used together to make pages that use appropriate images for the rendering situation.

## Value

A string. For more information about the syntax of the `srcset` attribute, see the HTML `<img>` reference.

## Examples

### Setting the srcset attribute

```js
const img = new Image();
img.srcset =
  "/en-US/docs/Web/HTML/Reference/Elements/img/clock-demo-400px.png 2x, /en-US/docs/Web/HTML/Reference/Elements/img/clock-demo-200px.png";
img.alt = "An example picture";
```

## Specifications

| Specification |
|---|
| HTML # dom-img-srcset |

## Browser compatibility
