---
title: "Gamepad API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API
domain: gamepad-api
license: CC-BY-SA-4.0
tags: gamepad api, game controller input, gamepad button axes, gamepad connected event
fetched: 2026-07-02
---

# Gamepad API

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **Gamepad API** is a way for developers to access and respond to signals from gamepads and other game controllers in a simple, consistent way. It contains three interfaces, two events and one specialist function, to respond to gamepads being connected and disconnected, and to access other information about the gamepads themselves, and what buttons and other controls are currently being pressed.

## Interfaces

**`Gamepad`**

Represents a gamepad/controller connected to the computer.

**`GamepadButton`**

Represents a button on one of the connected controllers.

**`GamepadEvent`**

The event object representing events fired that are related to gamepads.

### Experimental Gamepad extensions

**`GamepadHapticActuator`**

Represents hardware in the controller designed to provide haptic feedback to the user (if available), most commonly vibration hardware.

**`GamepadPose`**

Represents the pose of a controller (e.g., position and orientation in 3D space) in the case of a WebVR controller. This is *not* used by the newer WebXR standard.

### Extensions to other interfaces

#### Navigator

**`Navigator.getGamepads()`**

An extension to the `Navigator` object that returns an array of `Gamepad` objects, one for each connected gamepad.

#### Window events

**`gamepadconnected`**

An event that will fire when a gamepad is connected.

**`gamepaddisconnected`**

An event that will fire when a gamepad is disconnected.

## Tutorials and guides

- Using the Gamepad API
- Implementing controls using the Gamepad API

## Specifications

| Specification |
|---|
| Gamepad # gamepad-interface |
| Gamepad Extensions # partial-gamepad-interface |

## Browser compatibility
