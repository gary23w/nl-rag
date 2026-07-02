---
title: "DeviceMotionEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent
domain: device-orientation
license: CC-BY-SA-4.0
tags: device orientation events, accelerometer motion data, gyroscope rotation rate, device motion sensing
fetched: 2026-07-02
---

# DeviceMotionEvent

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`DeviceMotionEvent`** interface of the Device Orientation Events provides web developers with information about the speed of changes for the device's position and orientation.

**Warning:** Currently, Firefox and Chrome do not handle the coordinates the same way. Take care about this while using them.

## Constructor

**`DeviceMotionEvent()`**

Creates a new `DeviceMotionEvent`.

## Static methods

**`DeviceMotionEvent.requestPermission()`**

Requests the user's permission to access device motion data from the accelerometer and gyroscope sensors. Returns a `Promise` that resolves with a string of `"granted"` or `"denied"`.

## Instance properties

**`DeviceMotionEvent.acceleration` Read only**

An object giving the acceleration of the device on the three axis X, Y and Z. Acceleration is expressed in m/s².

**`DeviceMotionEvent.accelerationIncludingGravity` Read only**

An object giving the acceleration of the device on the three axis X, Y and Z with the effect of gravity. Acceleration is expressed in m/s².

**`DeviceMotionEvent.rotationRate` Read only**

An object giving the rate of change of the device's orientation on the three orientation axis alpha, beta and gamma. Rotation rate is expressed in degrees per seconds.

**`DeviceMotionEvent.interval` Read only**

A number representing the interval of time, in milliseconds, at which data is obtained from the device.

## Example

```js
window.addEventListener("devicemotion", (event) => {
  console.log(`${event.acceleration.x} m/s2`);
});
```

## Specifications

| Specification |
|---|
| Device Orientation and Motion # devicemotion |

## Browser compatibility
