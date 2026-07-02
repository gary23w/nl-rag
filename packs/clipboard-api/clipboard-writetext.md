---
title: "Clipboard: writeText() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText
domain: clipboard-api
license: CC-BY-SA-4.0
tags: clipboard api, async clipboard read write, clipboard item data, programmatic copy paste
fetched: 2026-07-02
---

# Clipboard: writeText() method

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2020.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`writeText()`** method of the `Clipboard` interface writes the specified text to the system clipboard, returning a `Promise` that is resolved once the system clipboard has been updated.

## Syntax

```js
writeText(newClipText)
```

### Parameters

**`newClipText`**

The string to be written to the clipboard.

### Return value

A `Promise` that is resolved once the clipboard's contents have been updated.

### Exceptions

**`NotAllowedError` `DOMException`**

Thrown if writing to the clipboard is not allowed.

## Security considerations

Writing to the clipboard can only be done in a secure context.

Additional security requirements are covered in the Security consideration section of the API overview topic.

## Examples

This example sets the clipboard's contents to the string "<empty clipboard>".

```js
button.addEventListener("click", () => writeClipboardText("<empty clipboard>"));

async function writeClipboardText(text) {
  try {
    await navigator.clipboard.writeText(text);
  } catch (error) {
    console.error(error.message);
  }
}
```

## Specifications

| Specification |
|---|
| Clipboard API and events # dom-clipboard-writetext |

## Browser compatibility
