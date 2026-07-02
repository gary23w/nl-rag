---
title: "HIDDevice - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HIDDevice
domain: web-hid
license: CC-BY-SA-4.0
tags: web hid api, human interface device, hid report descriptor, raw input output device
fetched: 2026-07-02
---

# HIDDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Note:** This feature is available in Web Workers, except for Shared Web Workers.

The **`HIDDevice`** interface of the WebHID API represents a HID Device. It provides properties for accessing information about the device, methods for opening and closing the connection, and the sending and receiving of reports.

## Instance properties

This interface also inherits properties from `EventTarget`.

**`HIDDevice.opened` Read only**

Returns a `Boolean`, true if the device has an open connection.

**`HIDDevice.vendorId` Read only**

Returns the vendorId of the HID device.

**`HIDDevice.productId` Read only**

Returns the productId of the HID device.

**`HIDDevice.productName` Read only**

Returns a string containing the product name of the HID device.

**`HIDDevice.collections` Read only**

Returns an array of report formats for the HID device.

### Events

**`inputreport`**

Fires when a report is sent from the device.

## Instance methods

This interface also inherits methods from `EventTarget`.

**`HIDDevice.open()`**

Opens a connection to this HID device, and returns a `Promise` which resolves once the connection has been successful.

**`HIDDevice.close()`**

Closes the connection to this HID device, and returns a `Promise` which resolves once the connection has been closed.

**`HIDDevice.forget()`**

Closes the connection to this HID device and resets access permission, and returns a `Promise` which resolves once the permission was reset.

**`HIDDevice.sendReport()`**

Sends an output report to this HID Device, and returns a `Promise` which resolves once the report has been sent.

**`HIDDevice.sendFeatureReport()`**

Sends a feature report to this HID device, and returns a `Promise` which resolves once the report has been sent.

**`HIDDevice.receiveFeatureReport()`**

Receives a feature report from this HID device in the form of a `Promise` which resolves with a `DataView`. This allows typed access to the contents of this message.

## Examples

The following example demonstrates listening for an `inputreport` event that will allow the application to detect which button is pressed on a Joy-Con Right device.

```js
device.addEventListener("inputreport", (event) => {
  const { data, device, reportId } = event;

  // Handle only the Joy-Con Right device and a specific report ID.
  if (device.productId !== 0x2007 && reportId !== 0x3f) return;

  const value = data.getUint8(0);
  if (value === 0) return;

  const someButtons = { 1: "A", 2: "X", 4: "B", 8: "Y" };
  console.log(`User pressed button ${someButtons[value]}.`);
});
```

In the following example `sendFeatureReport` is used to make a device blink.

```js
const reportId = 1;
for (let i = 0; i < 10; i++) {
  // Turn off
  await device.sendFeatureReport(reportId, Uint32Array.from([0, 0]));
  await new Promise((resolve) => setTimeout(resolve, 100));
  // Turn on
  await device.sendFeatureReport(reportId, Uint32Array.from([512, 0]));
  await new Promise((resolve) => setTimeout(resolve, 100));
}
```

You can see more examples, and live demos in the article Connecting to uncommon HID devices.

## Specifications

| Specification |
|---|
| WebHID API # dom-hiddevice |

## Browser compatibility
