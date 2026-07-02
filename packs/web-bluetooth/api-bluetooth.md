---
title: "Bluetooth - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Bluetooth
domain: web-bluetooth
license: CC-BY-SA-4.0
tags: web bluetooth api, bluetooth low energy gatt, gatt service characteristic, bluetooth device pairing
fetched: 2026-07-02
---

# Bluetooth

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

The **`Bluetooth`** interface of the Web Bluetooth API provides methods to query Bluetooth availability and request access to devices.

## Instance properties

*Inherits properties from its parent `EventTarget`.*

## Instance methods

**`Bluetooth.getAvailability()`**

Returns a `Promise` that resolves to a boolean value indicating whether the user agent can support Bluetooth. Some user agents let the user configure an option that specifies what value is returned by this method.

**`Bluetooth.getDevices()`**

Returns a `Promise` that resolves to an array of `BluetoothDevice`s this origin is allowed to access. Permission is obtained via previous calls to `Bluetooth.requestDevice()`.

**`Bluetooth.requestDevice()`**

Returns a `Promise` that resolves to a `BluetoothDevice` object matching the specified options.

## Specifications

| Specification |
|---|
| Web Bluetooth # bluetooth |

## Browser compatibility
