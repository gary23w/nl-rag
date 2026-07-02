---
title: "HTMLImageElement: decoding property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decoding
domain: lazy-loading
license: CC-BY-SA-4.0
tags: lazy loading images, intersection observer, loading attribute, deferred asset loading
fetched: 2026-07-02
---

# HTMLImageElement: decoding property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

- Learn more
- See full compatibility

The **`decoding`** property of the `HTMLImageElement` interface provides a hint to the browser as to how it should decode the image. More specifically, whether it should wait for the image to be decoded before presenting other content updates or not. It reflects the `<img>` element's `decoding` content attribute.

## Value

A string whose value is one of `sync`, `async`, or `auto`. For their meanings, see the HTML `<img>` reference.

## Examples

In the below example, you'll likely get an empty image shown on the page as the image is downloaded. Setting `decoding` won't prevent that.

```js
const img = new Image();
img.decoding = "sync";
img.src = "img/logo.png";
document.body.appendChild(img);
```

Inserting an image after download can make the `decoding` property more relevant:

```js
async function loadImage(url, elem) {
  return new Promise((resolve, reject) => {
    elem.onload = () => resolve(elem);
    elem.onerror = reject;
    elem.src = url;
  });
}

const img = new Image();
await loadImage("img/logo.png", img);
// Using `sync` can ensure other content is only updated with the image
img.decoding = "sync";
document.body.appendChild(img);
const p = document.createElement("p");
p.textContent = "Image is fully loaded!";
document.body.appendChild(p);
```

A better solution, however, is to use the `HTMLImageElement.decode()` method to solve this problem. It provides a way to asynchronously decode an image, delaying inserting it into the DOM until it is fully downloaded and decoded, thereby avoiding the empty image problem mentioned above. This is particularly useful if you're dynamically swapping an existing image for a new one, and also prevents unrelated paints outside of this code from being held up while the image is decoding.

Using `img.decoding = "async"` may avoid holding up other content from displaying if the decoding time is long:

```js
const img = new Image();
img.decoding = "async";
img.src = "img/logo.png";
document.body.appendChild(img);
```

## Specifications

| Specification |
|---|
| HTML # dom-img-decoding |

## Browser compatibility
