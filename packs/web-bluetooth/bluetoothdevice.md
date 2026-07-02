---
title: "BluetoothDevice - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/BluetoothDevice
domain: web-bluetooth
license: CC-BY-SA-4.0
tags: web bluetooth api, bluetooth low energy gatt, gatt service characteristic, bluetooth device pairing
fetched: 2026-07-02
---

# BluetoothDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The BluetoothDevice interface of the Web Bluetooth API represents a Bluetooth device inside a particular script execution environment.

## Instance properties

**`BluetoothDevice.id` Read only**

A string that uniquely identifies a device.

**`BluetoothDevice.name` Read only**

A string that provides a human-readable name for the device.

**`BluetoothDevice.gatt` Read only**

A reference to the device's `BluetoothRemoteGATTServer`.

## Instance methods

**`BluetoothDevice.watchAdvertisements()`**

A `Promise` that resolves to `undefined` or is rejected with an error if advertisements can't be shown for any reason.

**`BluetoothDevice.forget()`**

Provides a way for the page to revoke access to a device the user has granted access to.

## Events

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

**`gattserverdisconnected`**

Fired on a device when an active GATT connection is lost.

## Specifications

| Specification |
|---|
| Web Bluetooth # bluetoothdevice-interface |

## Browser compatibility
