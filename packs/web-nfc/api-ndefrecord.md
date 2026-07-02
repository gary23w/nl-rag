---
title: "NDEFRecord - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/NDEFRecord
domain: web-nfc
license: CC-BY-SA-4.0
tags: web nfc api, near field communication, ndef record message, contactless tag reading
fetched: 2026-07-02
---

# NDEFRecord

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

The **`NDEFRecord`** interface of the Web NFC API provides data that can be read from, or written to, compatible NFC devices, e.g., NFC tags supporting NDEF.

## Constructor

**`NDEFRecord()`**

Returns a new `NDEFRecord`.

## Instance properties

**`NDEFRecord.recordType` Read only**

Returns the record type of the record. Records must have either a standardized well-known type name such as `"empty"`, `"text"`, `"url"`, `"smart-poster"`, `"absolute-url"`, `"mime"`, or `"unknown"` or else an external type name, which consists of a domain name and custom type name separated by a colon (":").

**`NDEFRecord.mediaType` Read only**

Returns the MIME type of the record. This value will be `null` if `recordType` is not equal to `"mime"`.

**`NDEFRecord.id` Read only**

Returns the record identifier, which is an absolute or relative URL used to identify the record.

**Note:** The uniqueness of the identifier is enforced only by the generator of the record.

**`NDEFRecord.data` Read only**

Returns a `DataView` containing the raw bytes of the record's payload.

**`NDEFRecord.encoding` Read only**

Returns the encoding of a textual payload, or `null` otherwise.

**`NDEFRecord.lang` Read only**

Returns the language of a textual payload, or `null` if one was not supplied.

## Instance methods

**`NDEFRecord.toRecords()`**

Converts `NDEFRecord.data` to a sequence of records. This allows parsing the payloads of record types which may contain nested records, such as smart poster and external type records.

## Specifications

| Specification |
|---|
| Web NFC # dom-ndefrecord |

## Browser compatibility
