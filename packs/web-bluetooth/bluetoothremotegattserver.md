---
title: "BluetoothRemoteGATTServer - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/BluetoothRemoteGATTServer
domain: web-bluetooth
license: CC-BY-SA-4.0
tags: web bluetooth api, bluetooth low energy gatt, gatt service characteristic, bluetooth device pairing
fetched: 2026-07-02
---

# BluetoothRemoteGATTServer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`BluetoothRemoteGATTServer`** interface of the Web Bluetooth API represents a GATT Server on a remote device.

## Instance properties

**`BluetoothRemoteGATTServer.connected` Read only**

A boolean value that returns true while this script execution environment is connected to `this.device`. It can be false while the user agent is physically connected.

**`BluetoothRemoteGATTServer.device` Read only**

A reference to the `BluetoothDevice` running the server.

## Instance methods

**`BluetoothRemoteGATTServer.connect()`**

Causes the script execution environment to connect to `this.device`.

**`BluetoothRemoteGATTServer.disconnect()`**

Causes the script execution environment to disconnect from `this.device`.

**`BluetoothRemoteGATTServer.getPrimaryService()`**

Returns a promise to the primary `BluetoothRemoteGATTService` offered by the Bluetooth device for a specified `BluetoothServiceUUID`.

**`BluetoothRemoteGATTServer.getPrimaryServices()`**

Returns a promise to a list of primary `BluetoothRemoteGATTService` objects offered by the Bluetooth device for a specified `BluetoothServiceUUID`.

## Specifications

| Specification |
|---|
| Web Bluetooth # bluetoothgattremoteserver-interface |

## Browser compatibility
