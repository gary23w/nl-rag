---
title: "USB - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/USB
domain: web-usb
license: CC-BY-SA-4.0
tags: web usb api, usb device access, usb interface endpoint, usb transfer control
fetched: 2026-07-02
---

# USB

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`USB`** interface of the WebUSB API provides attributes and methods for finding and connecting USB devices from a web page.

Use `navigator.usb` to get access to the `USB` object.

The USB interface inherits from `EventTarget`.

## Instance properties

None.

## Instance methods

**`USB.getDevices()`**

Returns a `Promise` that resolves with an array of `USBDevice` objects for paired attached devices.

**`USB.requestDevice()`**

Returns a `Promise` that resolves with an instance of `USBDevice` if the specified device is found. Calling this function triggers the user agent's pairing flow.

## Events

**`connect`**

Fired whenever a previously paired device is connected.

**`disconnect`**

Fired whenever a paired device is disconnected.

## Specifications

| Specification |
|---|
| WebUSB API # usb |

## Browser compatibility
