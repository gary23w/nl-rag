---
title: "crossorigin HTML attribute - HTML"
source: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin
domain: subresource-integrity
license: CC-BY-SA-4.0
tags: subresource integrity, integrity attribute, cdn tamper protection, cryptographic hash digest
fetched: 2026-07-02
---

# `crossorigin` HTML attribute

The **`crossorigin`** attribute, valid on the `<audio>`, `<img>`, `<link>`, `<script>`, and `<video>` elements, provides support for CORS, defining how the element handles cross-origin requests, thereby enabling the configuration of the CORS requests for the element's fetched data. Depending on the element, the attribute can be a CORS settings attribute.

The `crossorigin` content attribute on media elements is a CORS settings attribute.

These attributes are enumerated, and have the following possible values:

**`anonymous`**

Request uses CORS headers and credentials flag is set to `'same-origin'`. There is no exchange of **user credentials** via cookies, client-side TLS certificates or HTTP authentication, unless destination is the same origin.

**`use-credentials`**

Request uses CORS headers, credentials flag is set to `'include'` and **user credentials** are always included.

**`""`**

Setting the attribute name to an empty value, like `crossorigin` or `crossorigin=""`, is the same as `anonymous`.

An invalid keyword and an empty string will be handled as the `anonymous` keyword.

By default (that is, when the attribute is not specified), CORS is not used at all. The user agent will not ask for permission for full access to the resource and in the case of a cross-origin request, certain limitations will be applied based on the type of element concerned:

| Element | Restrictions |
|---|---|
| `img`, `audio`, `video` | When resource is placed in `<canvas>`, element is marked as *tainted*. |
| `script` | Access to error logging via `window.onerror` will be limited. |
| `link` | Request with no appropriate `crossorigin` header may be discarded. |

**Note:** The `crossorigin` attribute is not supported for `rel="icon"` in Chromium-based browsers. See the open Chromium issue.

## Examples

### `crossorigin` with the `<script>` element

You can use the following `<script>` element to tell a browser to execute the `https://example.com/example-framework.js` script without sending user-credentials.

```html
<script
  src="https://example.com/example-framework.js"
  crossorigin="anonymous"></script>
```

### Web manifest with credentials

The `use-credentials` value must be used when fetching a manifest that requires credentials, even if the file is from the same origin.

```html
<link rel="manifest" href="/app.webmanifest" crossorigin="use-credentials" />
```

## Specifications

| Specification |
|---|
| HTML # cors-settings-attributes |

## Browser compatibility

### html.elements.audio.crossorigin

### html.elements.img.crossorigin

### html.elements.link.crossorigin

### html.elements.script.crossorigin

### html.elements.video.crossorigin
