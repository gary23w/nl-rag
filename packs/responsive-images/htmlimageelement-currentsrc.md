---
title: "HTMLImageElement: currentSrc property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/currentSrc
domain: responsive-images
license: CC-BY-SA-4.0
tags: responsive images, srcset image candidates, image-set css function, adaptive image sizes
fetched: 2026-07-02
---

# HTMLImageElement: currentSrc property

The **`currentSrc`** read-only property of the `HTMLImageElement` interface indicates the URL of the image selected by the browser to load.

## Value

A string indicating the full URL of the image currently selected by the browser to load. If the image uses the `srcset` attribute, `currentSrc` lets you determine which image from the set of provided images was selected by the browser. The property's value is unrelated to whether the image has successfully loaded or not.

## Examples

### Testing which image is loaded

In this example, two different sizes are provided for an image of a clock. One is 200px wide and the other is 400px wide. The `sizes` attribute is provided to indicate that the image should be drawn at 50% of the document width if the viewport is under 400px wide; otherwise, the image is drawn at 90% width of the document.

#### HTML

```html
<img
  src="/en-US/docs/Web/HTML/Reference/Elements/img/clock-demo-400px.png"
  alt="Clock"
  srcset="
    /en-US/docs/Web/HTML/Reference/Elements/img/clock-demo-200px.png 200w,
    /en-US/docs/Web/HTML/Reference/Elements/img/clock-demo-400px.png 400w
  "
  sizes="(width <= 400px) 50%, 90%" />
```

#### JavaScript

```js
const clockImage = document.querySelector("img");
const p = document.createElement("p");

p.textContent = clockImage.currentSrc.endsWith("200px.png")
  ? "Using the 200px image!"
  : "Using the 400px image.";
document.body.appendChild(p);
```

#### Result

## Specifications

| Specification |
|---|
| HTML # dom-img-currentsrc-dev |

## Browser compatibility
