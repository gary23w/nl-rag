---
title: "HID - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HID
domain: web-hid
license: CC-BY-SA-4.0
tags: web hid api, human interface device, hid report descriptor, raw input output device
fetched: 2026-07-02
---

# HID

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Note:** This feature is available in Web Workers, except for Shared Web Workers.

The **`HID`** interface provides methods for connecting to *HID devices*, listing attached HID devices and event handlers for connected HID devices.

## Instance properties

*This interface also inherits properties of its parent, `EventTarget`.*

## Instance methods

*This interface also inherits methods of its parent, `EventTarget`.*

**`getDevices()`**

Returns a `Promise` that resolves with an array of connected HID devices that the user has previously been granted access to in response to a `requestDevice()` call.

**`requestDevice()`**

Returns a `Promise` that resolves with an array of connected `HIDDevice` objects. Calling this function will trigger the user agent's permission flow in order to gain permission to access one selected device from the returned list of devices.

### Events

**`connect`**

Fired when an HID device is connected.

**`disconnect`**

Fired when an HID device is disconnected.

## Specifications

| Specification |
|---|
| WebHID API # dom-hid |

## Browser compatibility
