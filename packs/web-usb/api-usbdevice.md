---
title: "USBDevice - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/USBDevice
domain: web-usb
license: CC-BY-SA-4.0
tags: web usb api, usb device access, usb interface endpoint, usb transfer control
fetched: 2026-07-02
---

# USBDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`USBDevice`** interface of the WebUSB API provides access to metadata about a paired USB device and methods for controlling it.

## Instance properties

**`USBDevice.configuration` Read only**

A `USBConfiguration` object for the currently selected interface for a paired USB device.

**`USBDevice.configurations` Read only**

An `Array` of device-specific interfaces for controlling a paired USB device.

**`USBDevice.deviceClass` Read only**

One of three properties that identify USB devices for the purpose of loading a USB driver that will work with that device. The other two properties are `USBDevice.deviceSubclass` and `USBDevice.deviceProtocol`.

**`USBDevice.deviceProtocol` Read only**

One of three properties that identify USB devices for the purpose of loading a USB driver that will work with that device. The other two properties are `USBDevice.deviceClass` and `USBDevice.deviceSubclass`.

**`USBDevice.deviceSubclass` Read only**

One of three properties that identify USB devices for the purpose of loading a USB driver that will work with that device. The other two properties are `USBDevice.deviceClass` and `USBDevice.deviceProtocol`.

**`USBDevice.deviceVersionMajor` Read only**

The major version number of the device in a semantic versioning scheme.

**`USBDevice.deviceVersionMinor` Read only**

The minor version number of the device in a semantic versioning scheme.

**`USBDevice.deviceVersionSubminor` Read only**

The patch version number of the device in a semantic versioning scheme.

**`USBDevice.manufacturerName` Read only**

The name of the organization that manufactured the USB device.

**`USBDevice.opened` Read only**

Indicates whether a session has been started with a paired USB device.

**`USBDevice.productId` Read only**

The manufacturer-defined code that identifies a USB device.

**`USBDevice.productName` Read only**

The manufacturer-defined name that identifies a USB device.

**`USBDevice.serialNumber` Read only**

The manufacturer-defined serial number for the specific USB device.

**`USBDevice.usbVersionMajor` Read only**

One of three properties that declare the USB protocol version supported by the device. The other two properties are `USBDevice.usbVersionMinor` and `USBDevice.usbVersionSubminor`.

**`USBDevice.usbVersionMinor` Read only**

One of three properties that declare the USB protocol version supported by the device. The other two properties are `USBDevice.usbVersionMajor` and `USBDevice.usbVersionSubminor`.

**`USBDevice.usbVersionSubminor` Read only**

One of three properties that declare the USB protocol version supported by the device. The other two properties are `USBDevice.usbVersionMajor` and `USBDevice.usbVersionMinor`.

**`USBDevice.vendorId` Read only**

The official usb.org-assigned vendor ID.

## Instance methods

**`USBDevice.claimInterface()`**

Returns a `Promise` that resolves when the requested interface is claimed for exclusive access.

**`USBDevice.clearHalt()`**

Returns a `Promise` that resolves when a halt condition is cleared.

**`USBDevice.controlTransferIn()`**

Returns a `Promise` that resolves with a `USBInTransferResult` when a command or status operation has been transmitted to the USB device.

**`USBDevice.controlTransferOut()`**

Returns a `Promise` that resolves with a `USBOutTransferResult` when a command or status operation has been transmitted from the USB device.

**`USBDevice.close()`**

Returns a `Promise` that resolves when all open interfaces are released and the device session has ended.

**`USBDevice.forget()`**

Returns a `Promise` that resolves after all open interfaces are released, the device session has ended, and the permission is reset.

**`USBDevice.isochronousTransferIn()`**

Returns a `Promise` that resolves with a `USBIsochronousInTransferResult` when time sensitive information has been transmitted to the USB device.

**`USBDevice.isochronousTransferOut()`**

Returns a `Promise` that resolves with a `USBIsochronousOutTransferResult` when time sensitive information has been transmitted from the USB device.

**`USBDevice.open()`**

Returns a `Promise` that resolves when a device session has started.

**`USBDevice.releaseInterface()`**

Returns a `Promise` that resolves when a claimed interface is released from exclusive access.

**`USBDevice.reset()`**

Returns a `Promise` that resolves when the device is reset and all app operations canceled and their promises rejected.

**`USBDevice.selectAlternateInterface()`**

Returns a `Promise` that resolves when the specified alternative endpoint is selected.

**`USBDevice.selectConfiguration()`**

Returns a `Promise` that resolves when the specified configuration is selected.

**`USBDevice.transferIn()`**

Returns a `Promise` that resolves with a `USBInTransferResult` when bulk or interrupt data is received from the USB device.

**`USBDevice.transferOut()`**

Returns a `Promise` that resolves with a `USBOutTransferResult` when bulk or interrupt data is sent to the USB device.

## Specifications

| Specification |
|---|
| WebUSB API # device-usage |

## Browser compatibility
