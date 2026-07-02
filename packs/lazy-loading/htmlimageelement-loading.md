---
title: "HTMLImageElement: loading property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/loading
domain: lazy-loading
license: CC-BY-SA-4.0
tags: lazy loading images, intersection observer, loading attribute, deferred asset loading
fetched: 2026-07-02
---

# HTMLImageElement: loading property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

The **`loading`** property of the `HTMLImageElement` interface provides a hint to the browser on how to handle the loading of the image which is currently outside the window's visual viewport. This helps to optimize the loading of the document's contents by postponing loading the image until it's expected to be needed, rather than immediately during the initial page load. It reflects the `<img>` element's `loading` content attribute.

## Value

A string whose value is one of `eager` or `lazy`. For their meanings, see the HTML `<img>` reference.

## Examples

### Basic usage

The `addImageToList()` function shown below adds a photo thumbnail to a list of items, using lazy-loading to avoid loading the image from the network until it's actually needed.

```js
function addImageToList(url) {
  const list = document.querySelector("div.photo-list");

  const newItem = document.createElement("div");
  newItem.className = "photo-item";

  const newImg = document.createElement("img");
  newImg.loading = "lazy";
  newImg.width = 320;
  newImg.height = 240;
  newImg.src = url;

  newItem.appendChild(newImg);
  list.appendChild(newItem);
}
```

## Specifications

| Specification |
|---|
| HTML # dom-img-loading |

## Browser compatibility
