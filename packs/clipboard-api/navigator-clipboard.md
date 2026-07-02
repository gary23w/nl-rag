---
title: "Navigator: clipboard property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/clipboard
domain: clipboard-api
license: CC-BY-SA-4.0
tags: clipboard api, async clipboard read write, clipboard item data, programmatic copy paste
fetched: 2026-07-02
---

# Navigator: clipboard property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2020.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`clipboard`** read-only property of the `Navigator` interface returns a `Clipboard` object used to read and write the clipboard's contents.

This is the entry point to the Clipboard API, which can be used to implement cut, copy, and paste features within a web application.

## Value

The `Clipboard` object used to access the system clipboard.

## Examples

The following code uses `navigator.clipboard` to access the system clipboard in order to read text contents from the clipboard.

```js
navigator.clipboard
  .readText()
  .then(
    (clipText) => (document.querySelector(".clip-text").innerText = clipText),
  );
```

This snippet replaces the contents of the element whose class is `"clip-text"` with the text contents of the clipboard. Perhaps this code is being used in a browser extension that displays the current clipboard contents, automatically updating periodically or when specific events fire.

If the clipboard is empty or doesn't contain text, the `"clip-text"` element's contents are cleared. This happens because `readText()` returns an empty string if the clipboard is empty or doesn't contain text.

## Specifications

| Specification |
|---|
| Clipboard API and events # navigator-clipboard |

## Browser compatibility
