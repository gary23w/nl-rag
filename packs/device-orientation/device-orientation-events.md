---
title: "Device orientation events - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Device_orientation_events
domain: device-orientation
license: CC-BY-SA-4.0
tags: device orientation events, accelerometer motion data, gyroscope rotation rate, device motion sensing
fetched: 2026-07-02
---

# Device orientation events

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

Device orientation events are events that allow you to detect a device's physical orientation, as well as allowing you to detect the device's motion.

## Concepts and usage

Mobile devices commonly have sensors such as gyroscopes, compasses, and accelerometers that can enable applications running on the device to detect the device's orientation and motion.

The device orientation events enable you to write web applications that can change their behavior based on the orientation of the user's device, and that can react when the user moves their device.

Some typical features for which you might want to use the device orientation events include:

- in web-based games, to enable the user to control the motion of characters or objects in the game by tilting and moving the device
- in mapping applications, to re-orient a map based on the device's position, or to provide turn-by-turn directions that update with the user's movements
- for gesture recognition — for example, recognizing a "shake" gesture and using it to perform some action such as clearing an input area when the user shakes the device

Some user agents require explicit permission before providing access to sensor data. In those environments, `DeviceMotionEvent.requestPermission()` and `DeviceOrientationEvent.requestPermission()` can be used to request this permission from a transient user activation such as a button click. See Requesting permission for more details.

**Note:** This API is widely supported on mobile browsers. While some desktop-only browsers may have limitations due to hardware differences, these constraints are rarely significant given the API's primary usage on sensor-equipped devices.

## Interfaces

**`DeviceMotionEvent`**

Represents changes in the acceleration of a device, as well as the rotation rate.

**`DeviceMotionEventAcceleration`**

Represents the amount of acceleration the device is experiencing along all three axes

**`DeviceMotionEventRotationRate`**

Represents the rate at which the device is rotating around all three axes.

**`DeviceOrientationEvent`**

Represents changes in the physical orientation of a device.

### Extensions to other interfaces

**`devicemotion` event**

Fired at a regular interval to indicate the amount of physical force of acceleration the device is receiving at that time, and the rate of rotation of the device.

**`deviceorientation` event**

Fired when fresh data is available from the device about the current orientation of the device as compared to the Earth coordinate frame.

**`deviceorientationabsolute` event**

Fired when absolute device orientation changes.

## Specifications

| Specification |
|---|
| Device Orientation and Motion |

## Browser compatibility

### api.Window.deviceorientation_event

### api.Window.devicemotion_event

### api.Window.deviceorientationabsolute_event

### api.DeviceOrientationEvent

### api.DeviceMotionEvent

### api.DeviceMotionEventAcceleration

### api.DeviceMotionEventRotationRate
