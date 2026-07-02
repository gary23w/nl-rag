---
title: "HTMLIFrameElement - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement
domain: micro-frontends
license: CC-BY-SA-4.0
tags: micro frontends, frontend composition, separation of concerns, iframe isolation boundary
fetched: 2026-07-02
---

# HTMLIFrameElement

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`HTMLIFrameElement`** interface provides special properties and methods (beyond those of the `HTMLElement` interface it also has available to it by inheritance) for manipulating the layout and presentation of inline frame elements.

## Instance properties

*Inherits properties from its parent, `HTMLElement`*.

**`HTMLIFrameElement.align`**

A string that specifies the alignment of the frame with respect to the surrounding context.

**`HTMLIFrameElement.allow`**

A string that indicates the Permissions Policy specified for this `<iframe>`.

**`HTMLIFrameElement.allowFullscreen`**

A boolean value indicating whether the inline frame is willing to be placed into full screen mode. See Using fullscreen mode for details.

**`HTMLIFrameElement.allowPaymentRequest`**

A boolean value indicating whether the Payment Request API may be invoked inside a cross-origin iframe.

**`HTMLIFrameElement.browsingTopics`**

A boolean property specifying that the selected topics for the current user should be sent with the request for the associated `<iframe>`'s source. This reflects the `browsingtopics` content attribute value.

**`HTMLIFrameElement.contentDocument` Read only**

Returns a `Document`, the active document in the inline frame's nested browsing context.

**`HTMLIFrameElement.contentWindow` Read only**

Returns a WindowProxy, the window proxy for the nested browsing context.

**`HTMLIFrameElement.credentialless`**

A boolean value indicating whether the `<iframe>` is credentialless, meaning that its content is loaded in a new, ephemeral context. This context does not have access to the parent context's shared storage and credentials. In return, the `Cross-Origin-Embedder-Policy` (COEP) embedding rules can be lifted, so documents with COEP set can embed third-party documents that do not. See IFrame credentialless for a deeper explanation.

**`HTMLIFrameElement.csp`**

Specifies the Content Security Policy that an embedded document must agree to enforce upon itself.

**`HTMLIFrameElement.featurePolicy` Read only**

Returns the `FeaturePolicy` interface which provides a simple API for introspecting the Permissions Policies applied to a specific document.

**`HTMLIFrameElement.frameBorder`**

A string that indicates whether to create borders between frames.

**`HTMLIFrameElement.height`**

A string that reflects the `height` HTML attribute, indicating the height of the frame.

**`HTMLIFrameElement.loading`**

A string providing a hint to the browser that the iframe should be loaded immediately (`eager`) or on an as-needed basis (`lazy`). This reflects the `loading` HTML attribute.

**`HTMLIFrameElement.longDesc`**

A string that contains the URI of a long description of the frame.

**`HTMLIFrameElement.marginHeight`**

A string being the height of the frame margin.

**`HTMLIFrameElement.marginWidth`**

A string being the width of the frame margin.

**`HTMLIFrameElement.name`**

A string that reflects the `name` HTML attribute, containing a name by which to refer to the frame.

**`HTMLIFrameElement.privateToken`**

A string representation of an options object representing a private state token operation; this object has the same structure as the `RequestInit` dictionary's `privateToken` property. Mirrors the content of the associated `<iframe>` element's `privateToken` attribute.

**`HTMLIFrameElement.referrerPolicy`**

A string that reflects the `referrerPolicy` HTML attribute indicating which referrer to use when fetching the linked resource.

**`HTMLIFrameElement.sandbox` Read only**

Returns a `DOMTokenList` that reflects the `sandbox` HTML attribute, indicating extra restrictions on the behavior of the nested content.

**`HTMLIFrameElement.scrolling`**

A string that indicates whether the browser should provide scrollbars for the frame.

**`HTMLIFrameElement.src`**

A string that reflects the `src` HTML attribute, containing the address of the content to be embedded. Note that programmatically removing an `<iframe>`'s src attribute (e.g., via `Element.removeAttribute()`) causes `about:blank` to be loaded in the frame in Firefox (from version 65), Chromium-based browsers, and Safari/iOS.

**`HTMLIFrameElement.srcdoc`**

A `TrustedHTML` or string that represents the HTML document loaded into the frame.

**`HTMLIFrameElement.width`**

A string that reflects the `width` HTML attribute, indicating the width of the frame.

## Instance methods

*Also inherits methods from its parent interface, `HTMLElement`.*

**`HTMLIFrameElement.getSVGDocument()`**

Returns the embedded SVG as a `Document`.

## Specifications

| Specification |
|---|
| HTML # htmliframeelement |

## Browser compatibility
