---
title: "DeviceOrientationEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent
domain: device-orientation
license: CC-BY-SA-4.0
tags: device orientation events, accelerometer motion data, gyroscope rotation rate, device motion sensing
fetched: 2026-07-02
---

# DeviceOrientationEvent

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`DeviceOrientationEvent`** interface of the Device Orientation Events provides web developers with information from the physical orientation of the device running the web page.

## Constructor

**`DeviceOrientationEvent.DeviceOrientationEvent()`**

Creates a new `DeviceOrientationEvent`.

## Static methods

**`DeviceOrientationEvent.requestPermission()`**

Requests the user's permission to access device orientation data. Returns a `Promise` that resolves with a string of `"granted"` or `"denied"`.

## Instance properties

**`DeviceOrientationEvent.absolute` Read only**

A boolean that indicates whether or not the device is providing orientation data absolutely.

**`DeviceOrientationEvent.alpha` Read only**

A number representing the motion of the device around the z axis, express in degrees with values ranging from 0 (inclusive) to 360 (exclusive).

**`DeviceOrientationEvent.beta` Read only**

A number representing the motion of the device around the x axis, express in degrees with values ranging from -180 (inclusive) to 180 (exclusive). This represents a front to back motion of the device.

**`DeviceOrientationEvent.gamma` Read only**

A number representing the motion of the device around the y axis, express in degrees with values ranging from -90 (inclusive) to 90 (exclusive). This represents a left to right motion of the device.

**`DeviceOrientationEvent.webkitCompassHeading` Read only**

A number represents the difference between the motion of the device around the z axis of the world system and the direction of the north, express in degrees with values ranging from 0 to 360.

**`DeviceOrientationEvent.webkitCompassAccuracy` Read only**

The accuracy of the compass means that the deviation is positive or negative. It's usually 10.

## Example

```js
window.addEventListener("deviceorientation", (event) => {
  console.log(`${event.alpha} : ${event.beta} : ${event.gamma}`);
});
```

## Specifications

| Specification |
|---|
| Device Orientation and Motion # deviceorientation |

## Browser compatibility
