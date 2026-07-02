---
title: "Blob - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Blob
domain: sharp-imaging
license: CC-BY-SA-4.0
tags: sharp imaging, high performance image processing, image resize pipeline, libvips binding
fetched: 2026-07-02
---

# Blob

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`Blob`** interface represents a blob, which is a file-like object of immutable, raw data; they can be read as text or binary data, or converted into a `ReadableStream` so its methods can be used for processing the data.

Blobs can represent data that isn't necessarily in a JavaScript-native format. The `File` interface is based on `Blob`, inheriting blob functionality and expanding it to support files on the user's system.

## Using blobs

To construct a `Blob` from other non-blob objects and data, use the `Blob()` constructor. To create a blob that contains a subset of another blob's data, use the `slice()` method. To obtain a `Blob` object for a file on the user's file system, see the `File` documentation.

The APIs accepting `Blob` objects are also listed in the `File` documentation.

## Constructor

**`Blob()`**

Returns a newly created `Blob` object which contains a concatenation of all of the data in the array passed into the constructor.

## Instance properties

**`Blob.size` Read only**

The size, in bytes, of the data contained in the `Blob` object.

**`Blob.type` Read only**

A string indicating the MIME type of the data contained in the `Blob`. If the type is unknown, this string is empty.

## Instance methods

**`Blob.arrayBuffer()`**

Returns a promise that resolves with an `ArrayBuffer` containing the entire contents of the `Blob` as binary data.

**`Blob.bytes()`**

Returns a promise that resolves with a `Uint8Array` containing the contents of the `Blob`.

**`Blob.slice()`**

Returns a new `Blob` object containing the data in the specified range of bytes of the blob on which it's called.

**`Blob.stream()`**

Returns a `ReadableStream` that can be used to read the contents of the `Blob`.

**`Blob.text()`**

Returns a promise that resolves with a string containing the entire contents of the `Blob` interpreted as UTF-8 text.

## Examples

### Creating a blob

The `Blob()` constructor can create blobs from other objects. For example, to construct a blob from a JSON string:

```js
const obj = { hello: "world" };
const blob = new Blob([JSON.stringify(obj, null, 2)], {
  type: "application/json",
});
```

The following example creates a JavaScript typed array and creates a new `Blob` containing the typed array's data. It then calls `URL.createObjectURL()` to convert the blob into a URL.

```html
<p>
  This example creates a typed array containing the ASCII codes for the space
  character through the letter Z, then converts it to an object URL. A link to
  open that object URL is created. Click the link to see the decoded object URL.
</p>
```

The main piece of this code for example purposes is the `typedArrayToURL()` function, which creates a `Blob` from the given typed array and returns an object URL for it. Having converted the data into an object URL, it can be used in a number of ways, including as the value of the `<img>` element's `src` attribute (assuming the data contains an image, of course).

```js
function showViewLiveResultButton() {
  if (window.self !== window.top) {
    // Ensure that if our document is in a frame, we get the user
    // to first open it in its own tab or window. Otherwise, this
    // example won't work.
    const p = document.querySelector("p");
    p.textContent = "";
    const button = document.createElement("button");
    button.textContent = "View live result of the example code above";
    p.append(button);
    button.addEventListener("click", () => window.open(location.href));
    return true;
  }
  return false;
}

if (!showViewLiveResultButton()) {
  function typedArrayToURL(typedArray, mimeType) {
    return URL.createObjectURL(
      new Blob([typedArray.buffer], { type: mimeType }),
    );
  }
  const bytes = new Uint8Array(59);

  for (let i = 0; i < 59; i++) {
    bytes[i] = 32 + i;
  }

  const url = typedArrayToURL(bytes, "text/plain");
  const link = document.createElement("a");

  link.href = url;
  link.innerText = "Open the array URL";
  document.body.appendChild(link);
}
```

### Extracting data from a blob

One way to read content from a `Blob` is to use a `FileReader`. The following code reads the content of a `Blob` as a typed array:

```js
const reader = new FileReader();
reader.addEventListener("loadend", () => {
  // reader.result contains the contents of blob as a typed array
});
reader.readAsArrayBuffer(blob);
```

Another way to read content from a `Blob` is to use a `Response`. The following code reads the content of a `Blob` as text:

```js
const text = await new Response(blob).text();
```

Or by using `Blob.text()`:

```js
const text = await blob.text();
```

By using other methods of `FileReader`, it is possible to read the contents of a Blob as a string or a data URL.

## Specifications

| Specification |
|---|
| File API # blob-section |

## Browser compatibility
