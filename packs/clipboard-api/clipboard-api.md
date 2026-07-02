---
title: "Clipboard API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API
domain: clipboard-api
license: CC-BY-SA-4.0
tags: clipboard api, async clipboard read write, clipboard item data, programmatic copy paste
fetched: 2026-07-02
---

# Clipboard API

The **Clipboard API** provides the ability to respond to clipboard commands (cut, copy, and paste), as well as to asynchronously read from and write to the system clipboard.

**Note:** Use this API in preference to the deprecated `document.execCommand()` method for accessing the clipboard.

**Note:** This API is *not available* in Web Workers (not exposed via `WorkerNavigator`).

## Concepts and usage

The *system clipboard* is a data buffer belonging to the operating system hosting the browser, which is used for short-term data storage and/or data transfers between documents or applications. It is usually implemented as an anonymous, temporary data buffer, sometimes called the *paste buffer*, that can be accessed from most or all programs within the environment via defined programming interfaces.

The Clipboard API allows users to programmatically read and write text and other kinds of data to and from the system clipboard in secure contexts, provided the user has met the criteria outlined in the Security considerations.

Events are fired as the result of `cut`, `copy`, and `paste` operations modifying the clipboard. The events have a default action, for example the `copy` action copies the current selection to the system clipboard by default. The default action can be overridden by the event handler — see each of the events for more information.

There is also a `clipboardchange` event fired directly on the `Clipboard` object whenever the system clipboard's contents are changed. This is useful for notifying apps of a change to the system clipboard, for example if they have their own clipboard that needs to be kept in sync.

## Interfaces

**`Clipboard` Secure context**

Provides an interface for reading and writing text and data to or from the system clipboard. The specification refers to this as the 'Async Clipboard API'.

**`ClipboardChangeEvent`**

Represents events fired whenever the contents of the system clipboard are changed.

**`ClipboardEvent`**

Represents events providing information related to modification of the clipboard, that is `cut`, `copy`, and `paste` events. The specification refers to this as the 'Clipboard Event API'.

**`ClipboardItem` Secure context**

Represents a single item format, used when reading or writing data.

### Extensions to other interfaces

The Clipboard API extends the following APIs, adding the listed features.

**`Navigator.clipboard` Read only Secure context**

Returns a `Clipboard` object that provides read and write access to the system clipboard.

**`Element` `copy` event**

An event fired whenever the user initiates a copy action.

**`Element` `cut` event**

An event fired whenever the user initiates a cut action.

**`Element` `paste` event**

An event fired whenever the user initiates a paste action.

## Security considerations

The Clipboard API allows users to programmatically read and write text and other kinds of data to and from the system clipboard in secure contexts.

When reading from the clipboard, the specification requires that a user has recently interacted with the page (transient user activation) and that the call is made as a result of the user interacting with a browser or OS "paste element" (such as choosing "Paste" on a native context menu). In practice, browsers often allow read operations that do not satisfy these requirements, while placing other requirements instead (such as a permission or per-operation prompt). For writing to the clipboard the specification expects that the page has been granted the Permissions API `clipboard-write` permission, and the browser may also require transient user activation. Browsers may place additional restrictions over use of the methods to access the clipboard.

The `clipboardchange` event is only fired with sticky activation or after the `clipboard-read` permission is granted.

Browser implementations have diverged from the specification. The differences are captured in the Browser compatibility section and the current state is summarized below:

Chromium browsers:

- If a read isn't allowed by the spec and the document has focus, it triggers a request to use permission `clipboard-read`, and succeeds if the permission is granted (either because the user accepted the prompt, or because the permission was granted already).
- Writing requires either the `clipboard-write` permission or transient activation. If the permission is granted, it persists, and further transient activation is not required.
- The HTTP Permissions-Policy permissions `clipboard-read` and `clipboard-write` must be allowed for `<iframe>` elements that access the clipboard.

Firefox & Safari:

- If a read isn't allowed by the spec but transient user activation is still met, it triggers a user prompt in the form of an ephemeral context menu with a single "Paste" option (which becomes enabled after 1 second) and succeeds if the user chooses the option.
- Writing requires transient activation.
- The paste-prompt is suppressed if reading same-origin clipboard content, but not cross-origin content.
- The `clipboard-read` and `clipboard-write` permissions are not supported (and not planned to be supported) by Firefox or Safari.

Firefox web extensions:

- Reading is available to extensions with the web extension `clipboardRead` permission. With this permission, the extension doesn't require transient activation or use the paste prompt. From Firefox 147, reading is also available without the permission in a secure context, with transient activation, and after the user clicks the paste prompt in an ephemeral context menu.
- Writing is available in a secure context and with transient activation. However, with the web extension `clipboardWrite` permission transient activation is not required.

## Examples

### Accessing the clipboard

The system clipboard is accessed through the `Navigator.clipboard` global.

This snippet fetches the text from the clipboard and appends it to the first element found with the class `editor`. Since `readText()` returns an empty string if the clipboard isn't text, this code is safe.

```js
navigator.clipboard
  .readText()
  .then(
    (clipText) => (document.querySelector(".editor").innerText += clipText),
  );
```

## Specifications

| Specification |
|---|
| Clipboard API and events # clipboard-interface |
| Clipboard API and events # clipboardchangeevent |
| Clipboard API and events # clipboard-event-interfaces |
| Clipboard API and events # clipboarditem |

## Browser compatibility

### api.Clipboard

### api.ClipboardChangeEvent

### api.ClipboardEvent

### api.ClipboardItem
