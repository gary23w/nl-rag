---
title: "NDEFMessage - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/NDEFMessage
domain: web-nfc
license: CC-BY-SA-4.0
tags: web nfc api, near field communication, ndef record message, contactless tag reading
fetched: 2026-07-02
---

# NDEFMessage

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

The **`NDEFMessage`** interface of the Web NFC API represents the content of an NDEF message that has been read from or could be written to an NFC tag. An instance is acquired by calling the `NDEFMessage()` constructor or from the `NDEFReadingEvent.message` property, which is passed to the `reading` event.

## Constructor

**`NDEFMessage()`**

Creates a new `NDEFMessage` object, initialized with the given NDEF records.

## Attributes

**`NDEFMessage.records` Read only**

Returns the list of NDEF records contained in the message.

## Specifications

| Specification |
|---|
| Web NFC # dom-ndefmessage |

## Browser compatibility
