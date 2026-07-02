---
title: "Encrypted Media Extensions API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Encrypted_Media_Extensions_API
domain: encrypted-media
license: CC-BY-SA-4.0
tags: encrypted media extensions, content decryption module, digital rights management, media key session
fetched: 2026-07-02
---

# Encrypted Media Extensions API

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2019.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **Encrypted Media Extensions API** provides interfaces for controlling the playback of content which is subject to a digital restrictions management scheme.

Access to this API is provided through `Navigator.requestMediaKeySystemAccess()`.

## Interfaces

**`MediaEncryptedEvent`**

Represents a specific `encrypted` event thrown when a `HTMLMediaElement` encounters some initialization data.

**`MediaKeyMessageEvent`**

Contains the content and related data when the content decryption module (CDM) generates a message for the session.

**`MediaKeys`**

Represents a set of keys that an associated `HTMLMediaElement` can use for decryption of media data during playback.

**`MediaKeySession`**

Represents a context for message exchange with a content decryption module (CDM).

**`MediaKeyStatusMap`**

A read-only map of media key statuses by key IDs.

**`MediaKeySystemAccess`**

Provides access to a key system for decryption and/or a content protection provider.

### Extensions to other interfaces

The Encrypted Media Extensions API extends the following APIs, adding the listed features.

#### HTMLMediaElement

**`HTMLMediaElement.mediaKeys` Read only**

Provides a `MediaKeys` object that represents the set of keys that the element can use for decryption of media data during playback.

**`HTMLMediaElement.setMediaKeys()`**

Sets the `MediaKeys` that will be used to decrypt media during playback.

**`encrypted` event**

Event that is fired on a `HTMLMediaElement` when initialization data is encountered in the media, indicating that it is encrypted.

#### Navigator

**`Navigator.requestMediaKeySystemAccess()`**

Returns a `Promise` that fulfils to a `MediaKeySystemAccess` object that can be used to access a particular media key system, which can in turn be used to create keys for decrypting a media stream.

## Specifications

| Specification |
|---|
| Encrypted Media Extensions # navigator-extension-requestmediakeysystemaccess |

## Browser compatibility
