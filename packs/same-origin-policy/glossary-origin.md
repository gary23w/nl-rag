---
title: "Origin - Glossary"
source: https://developer.mozilla.org/en-US/docs/Glossary/Origin
domain: same-origin-policy
license: CC-BY-SA-4.0
tags: same-origin policy, web origin model, cross-origin isolation, document domain property
fetched: 2026-07-02
---

# Origin

Web content's **origin** is defined by the *scheme* (protocol), *hostname* (domain), and *port* of the URL used to access it. Two objects have the same origin only when the scheme, hostname, and port all match.

Some operations are restricted to same-origin content, and this restriction can be lifted using CORS.

## Opaque origin

An opaque origin is a special type of browser-internal value that obscures the true origin of a resource (opaque origins are always serialized as `null`). They are used by the browser to ensure resource isolation as they are never considered equal to any other origin — including other opaque origins.

Opaque origins are applied in cases where the true origin of a resource is sensitive, cannot be safely used for security checks, or does not exist. A resource with an opaque origin will have its `Origin` HTTP header in requests set to `null`. It will also fail same-origin checks with any other resource, and hence be restricted to only those operations available to cross-origin resources.

Common cases where opaque origins are used include:

- A document within an iframe that has the sandbox attribute set, and does not include the `allow-same-origin` flag.
- `file:` URLs are usually treated as opaque origins so that files on the file system cannot read each other.
- Documents created programmatically using APIs like `DOMImplementation.createDocument()`.

## Examples

These are same origin because they have the same scheme (`http`) and hostname (`example.com`), and the different file path does not matter:

- `http://example.com/app1/index.html`
- `http://example.com/app2/index.html`

These are same origin because a server delivers HTTP content through port 80 by default:

- `http://example.com:80`
- `http://example.com`

These are not same origin because they use different schemes:

- `http://example.com/app1`
- `https://example.com/app2`

These are not same origin because they use different hostnames:

- `http://example.com`
- `http://www.example.com`
- `http://myapp.example.com`

These are not same origin because they use different ports:

- `http://example.com`
- `http://example.com:8080`
