---
title: "Clipboard - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Clipboard
domain: clipboard-api
license: CC-BY-SA-4.0
tags: clipboard api, async clipboard read write, clipboard item data, programmatic copy paste
fetched: 2026-07-02
---

# Clipboard

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`Clipboard`** interface of the Clipboard API provides read and write access to the contents of the system clipboard. This allows a web application to implement cut, copy, and paste features.

The system clipboard is exposed through the global `Navigator.clipboard` property.

All of the Clipboard API methods operate asynchronously; they return a `Promise` which is resolved once the clipboard access has been completed. The promise is rejected if clipboard access is denied.

All the methods require a secure context. Additional requirements for using the API are discussed in the Security consideration section of the API overview topic.

## Instance methods

*`Clipboard` is based on the `EventTarget` interface, and includes its methods.*

**`read()`**

Requests arbitrary data (such as images) from the clipboard, returning a `Promise` that resolves with an array of `ClipboardItem` objects containing the clipboard's contents.

**`readText()`**

Requests text from the system clipboard, returning a `Promise` that is fulfilled with a string containing the clipboard's text once it's available.

**`write()`**

Writes arbitrary data to the system clipboard, returning a `Promise` that resolves when the operation completes.

**`writeText()`**

Writes text to the system clipboard, returning a `Promise` that is resolved once the text is fully copied into the clipboard.

## Events

**`clipboardchange`**

Fired when the system clipboard contents are changed in any way, for example via a system copy command, or via an API method such as `Clipboard.writeText()`.

## Specifications

| Specification |
|---|
| Clipboard API and events # clipboard-interface |

## Browser compatibility
