---
title: "Window: deviceorientation event - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/deviceorientation_event
domain: device-orientation
license: CC-BY-SA-4.0
tags: device orientation events, accelerometer motion data, gyroscope rotation rate, device motion sensing
fetched: 2026-07-02
---

# Window: deviceorientation event

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`deviceorientation`** event is fired when fresh data is available from an orientation sensor about the current orientation of the device as compared to the Earth coordinate frame. This data is gathered from a magnetometer inside the device.

See Orientation and motion data explained for details.

This event is not cancelable and does not bubble.

## Syntax

Use the event name in methods like `addEventListener()`, or set an event handler property.

```js
addEventListener("deviceorientation", (event) => { })

ondeviceorientation = (event) => { }
```

## Event type

A `DeviceOrientationEvent`. Inherits from `Event`.

## Event properties

**`DeviceOrientationEvent.absolute` Read only**

A boolean that indicates whether the device is providing orientation data absolutely.

**`DeviceOrientationEvent.alpha` Read only**

A number representing the motion of the device around the z axis, express in degrees with values ranging from 0 (inclusive) to 360 (exclusive).

**`DeviceOrientationEvent.beta` Read only**

A number representing the motion of the device around the x axis, expressed in degrees with values ranging from -180 (inclusive) to 180 (exclusive). This represents the front to back motion of the device.

**`DeviceOrientationEvent.gamma` Read only**

A number representing the motion of the device around the y axis, expressed in degrees with values ranging from -90 (inclusive) to 90 (exclusive). This represents the left to right motion of the device.

**`DeviceOrientationEvent.webkitCompassHeading` Read only**

A number represents the difference between the motion of the device around the z axis of the world system and the direction of the north, expressed in degrees with values ranging from 0 to 360.

**`DeviceOrientationEvent.webkitCompassAccuracy` Read only**

The accuracy of the compass given as a positive or negative deviation. It's usually 10.

## Examples

```js
if (window.DeviceOrientationEvent) {
  window.addEventListener(
    "deviceorientation",
    (event) => {
      const rotateDegrees = event.alpha; // alpha: rotation around z-axis
      const leftToRight = event.gamma; // gamma: left to right
      const frontToBack = event.beta; // beta: front back motion

      handleOrientationEvent(frontToBack, leftToRight, rotateDegrees);
    },
    true,
  );
}

function handleOrientationEvent(frontToBack, leftToRight, rotateDegrees) {
  // do something amazing
}
```

## Specifications

| Specification |
|---|
| Device Orientation and Motion # deviceorientation |
| Device Orientation and Motion # dom-window-ondeviceorientation |

## Browser compatibility
