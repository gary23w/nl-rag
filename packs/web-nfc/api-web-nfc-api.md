---
title: "Web NFC API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Web_NFC_API
domain: web-nfc
license: CC-BY-SA-4.0
tags: web nfc api, near field communication, ndef record message, contactless tag reading
fetched: 2026-07-02
---

# Web NFC API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

The Web NFC API allows exchanging data over NFC via light-weight NFC Data Exchange Format (NDEF) messages.

**Note:** Devices and tags have to be formatted and recorded specifically to support NDEF record format to be used with Web NFC. Low-level operations are currently not supported by the API, however there is a public discussion about API that would add such functionality.

## Interfaces

**`NDEFMessage`**

Interface that represents NDEF messages that can be received from or sent to a compatible tag via a `NDEFReader` object. A message is composed of metadata and NDEF Records.

**`NDEFReader`**

Interface that enables reading and writing messages from compatible NFC tags. The messages are represented as `NDEFMessage` objects.

**`NDEFRecord`**

Interface that represents NDEF records that can be included in an NDEF message.

## Specifications

| Specification |
|---|
| Web NFC # the-ndefreader-object |

## Browser compatibility
