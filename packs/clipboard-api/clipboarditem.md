---
title: "ClipboardItem - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem
domain: clipboard-api
license: CC-BY-SA-4.0
tags: clipboard api, async clipboard read write, clipboard item data, programmatic copy paste
fetched: 2026-07-02
---

# ClipboardItem

Baseline

2024

*

Newly available

Since June 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`ClipboardItem`** interface of the Clipboard API represents a single item format, used when reading or writing clipboard data using `Clipboard.read()` and `Clipboard.write()` respectively.

The **`ClipboardItem`** interface enables developers to use a single type to represent a range of different data formats.

**Note:** The `read()` and `write()` methods can be used to work with text strings and arbitrary data items represented by `Blob` instances. However, if you are solely working with text, it is more convenient to use the `Clipboard.readText()` and `Clipboard.writeText()` methods.

## Constructor

**`ClipboardItem()`**

Creates a new **`ClipboardItem`** object, with the MIME type as the key and the data as the value.

## Instance properties

**`types` Read only**

Returns an `Array` of MIME types available within the **`ClipboardItem`**.

**`presentationStyle` Read only**

Returns one of the following: `"unspecified"`, `"inline"` or `"attachment"`.

## Static methods

**`ClipboardItem.supports()`**

Checks whether a given MIME type is supported by the clipboard. This enables a website to detect whether a MIME type is supported before attempting to write data.

## Instance methods

**`getType()`**

Returns a `Promise` that resolves with a `Blob` of the requested MIME type, or an error if the MIME type is not found.

## Examples

### Writing text to the clipboard

In this example we first define two constants containing references to a `<p>` element containing some text and a `<button>` element.

Next, we define a function called `copyToClipboard()`. This starts off by storing a `"text/plain"` MIME type in a constant, then creating an object called `clipboardItemData` that contains one property with a key equal to the MIME type and a value of the text we want to copy to the clipboard (the content of the `<p>` element, in this case). Because we are working with text, we can pass it in directly rather than having to create a `Blob`.

We construct a new `ClipboardItem` object using the `ClipboardItem()` constructor, and pass it into the `Clipboard.write()` method to copy the text to the clipboard.

Finally, we add an event listener to the `<button>` so that it runs the function when pressed.

```js
const textSource = document.querySelector("p");
const copyBtn = document.querySelector("button");

async function copyToClipboard() {
  const type = "text/plain";
  const clipboardItemData = {
    [type]: textSource.textContent,
  };
  const clipboardItem = new ClipboardItem(clipboardItemData);
  await navigator.clipboard.write([clipboardItem]);
}

copyBtn.addEventListener("click", copyToClipboard);
```

### Writing an image to the clipboard

Here we use `supports()` to check whether the `image/svg+xml` MIME data type is supported. If it is, we fetch an SVG image with the Fetch API, and then read it into a `Blob`, which we can use to create a `ClipboardItem` that is written to the clipboard.

```js
async function writeClipImg() {
  try {
    if (ClipboardItem.supports("image/svg+xml")) {
      const imgURL = "/my-image.svg";
      const data = await fetch(imgURL);
      const blob = await data.blob();
      await navigator.clipboard.write([
        new ClipboardItem({
          [blob.type]: blob,
        }),
      ]);
      console.log("Fetched image copied.");
    } else {
      console.log("SVG images are not supported by the clipboard.");
    }
  } catch (err) {
    console.error(err.name, err.message);
  }
}
```

### Reading from the clipboard

Here we're returning all items on the clipboard via the `clipboard.read()` method. Then utilizing the `ClipboardItem.types` property to set the `getType()` argument and return the corresponding blob object.

```js
async function getClipboardContents() {
  try {
    const clipboardItems = await navigator.clipboard.read();

    for (const clipboardItem of clipboardItems) {
      for (const type of clipboardItem.types) {
        const blob = await clipboardItem.getType(type);
        // we can now use blob here
      }
    }
  } catch (err) {
    console.error(err.name, err.message);
  }
}
```

## Specifications

| Specification |
|---|
| Clipboard API and events # clipboarditem |

## Browser compatibility
