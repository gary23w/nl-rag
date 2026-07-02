---
title: "Gamepad - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Gamepad
domain: gamepad-api
license: CC-BY-SA-4.0
tags: gamepad api, game controller input, gamepad button axes, gamepad connected event
fetched: 2026-07-02
---

# Gamepad

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`Gamepad`** interface of the Gamepad API defines an individual gamepad or other controller, allowing access to information such as button presses, axis positions, and id.

A Gamepad object can be returned in one of two ways: via the `gamepad` property of the `gamepadconnected` and `gamepaddisconnected` events, or by grabbing any position in the array returned by the `Navigator.getGamepads()` method.

**Note:** The support of gamepad features varies across different combinations of platforms and controllers. Even if the controller supports a certain feature (for example, haptic feedback), the platform may not support it for that controller.

## Instance properties

**`Gamepad.axes` Read only**

An array representing the controls with axes present on the device (e.g., analog thumb sticks).

**`Gamepad.buttons` Read only**

An array of `gamepadButton` objects representing the buttons present on the device.

**`Gamepad.connected` Read only**

A boolean indicating whether the gamepad is still connected to the system.

**`Gamepad.displayId` Read only**

Returns the `VRDisplay.displayId` of an associated `VRDisplay` (if relevant) — the `VRDisplay` that the gamepad is controlling the displayed scene of.

**`Gamepad.hand` Read only**

An enum defining what hand the controller is being held in, or is most likely to be held in.

**`Gamepad.hapticActuators` Read only**

An array containing `GamepadHapticActuator` objects, each of which represents haptic feedback hardware available on the controller.

**`Gamepad.vibrationActuator` Read only**

A `GamepadHapticActuator` object, which represents haptic feedback hardware available on the controller.

**`Gamepad.id` Read only**

A string containing identifying information about the controller.

**`Gamepad.index` Read only**

An integer that is auto-incremented to be unique for each device currently connected to the system.

**`Gamepad.mapping` Read only**

A string indicating whether the browser has remapped the controls on the device to a known layout.

**`Gamepad.pose` Read only**

A `GamepadPose` object representing the pose information associated with a WebVR controller (e.g., its position and orientation in 3D space).

**`Gamepad.timestamp` Read only**

A `DOMHighResTimeStamp` representing the last time the data for this gamepad was updated.

## Example

```js
window.addEventListener("gamepadconnected", (e) => {
  console.log(
    "Gamepad connected at index %d: %s. %d buttons, %d axes.",
    e.gamepad.index,
    e.gamepad.id,
    e.gamepad.buttons.length,
    e.gamepad.axes.length,
  );
});
```

## Specifications

| Specification |
|---|
| Gamepad # gamepad-interface |
| Gamepad Extensions # partial-gamepad-interface |

## Browser compatibility
