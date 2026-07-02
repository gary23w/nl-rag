---
title: "HIDInputReportEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HIDInputReportEvent
domain: web-hid
license: CC-BY-SA-4.0
tags: web hid api, human interface device, hid report descriptor, raw input output device
fetched: 2026-07-02
---

# HIDInputReportEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Note:** This feature is available in Web Workers, except for Shared Web Workers.

The **`HIDInputReportEvent`** interface of the WebHID API is passed to `inputreport` event of `HIDDevice` when an input report is received from any associated HID device.

## Instance properties

*This interface also inherits properties from `Event`.*

**`HIDInputReportEvent.data` Read only**

A `DataView` containing the data from the input report, excluding the `reportId` if the HID interface uses report IDs.

**`HIDInputReportEvent.device` Read only**

The `HIDDevice` instance that represents the HID interface that sent the input report.

**`HIDInputReportEvent.reportId` Read only**

The one-byte identification prefix for this report, or 0 if the HID interface does not use report IDs.

## Instance methods

*This interface inherits methods from its parent, `Event`.*

## Examples

The following example demonstrates listening for an `inputReport` that will allow the application to detect which button is pressed on a Joy-Con Right device. You can see more examples, and live demos in the article Connecting to uncommon HID devices.

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

## Specifications

| Specification |
|---|
| WebHID API # dom-hidinputreportevent |

## Browser compatibility
