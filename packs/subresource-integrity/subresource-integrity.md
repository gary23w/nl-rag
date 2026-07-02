---
title: "Subresource Integrity"
source: https://en.wikipedia.org/wiki/Subresource_Integrity
domain: subresource-integrity
license: CC-BY-SA-4.0
tags: subresource integrity, integrity attribute, cdn tamper protection, cryptographic hash digest
fetched: 2026-07-02
---

# Subresource Integrity

**Subresource Integrity** or **SRI** is a W3C recommendation to provide a method to protect website delivery. Specifically, it validates assets served by a third party, such as a content delivery network (CDN). This ensures these assets have not been compromised for hostile purposes.

To use SRI, a website author wishing to include a resource from a third party can specify a cryptographic hash of the resource in addition to the location of the resource. Browsers fetching the resource can then compare the hash provided by the website author with the hash computed from the resource. If the hashes don't match, the resource is discarded.

A sample `script` element with `integrity` and `crossorigin` attribute used by the SRI:

```mw
<script src="https://cdn.example.com/app.js"
        integrity="sha384-+/M6kredJcxdsqkczBUjMLvqyHb1K/JThDXWsBVxMEeZHEaMKEOEct339VItX1zB"
        crossorigin="anonymous">
</script>
```
