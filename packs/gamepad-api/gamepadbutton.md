---
title: "GamepadButton - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/GamepadButton
domain: gamepad-api
license: CC-BY-SA-4.0
tags: gamepad api, game controller input, gamepad button axes, gamepad connected event
fetched: 2026-07-02
---

# GamepadButton

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`GamepadButton`** interface defines an individual button of a gamepad or other controller, allowing access to the current state of different types of buttons available on the control device.

A `GamepadButton` object is returned by querying any value of the array returned by the `buttons` property of the `Gamepad` interface.

## Instance properties

**`GamepadButton.pressed` Read only**

A boolean value indicating whether the button is currently pressed (`true`) or unpressed (`false`).

**`GamepadButton.touched` Read only**

A boolean value indicating whether the button is currently touched (`true`) or not touched (`false`).

**`GamepadButton.value` Read only**

A double value used to represent the current state of analog buttons, such as the triggers on many modern gamepads. The values are normalized to the range 0.0 —1.0, with 0.0 representing a button that is not pressed, and 1.0 representing a button that is fully pressed.

## Example

The button values in the following example are stored as an array of `GamepadButton` objects. This simple example checks to see if the `GamepadButton.value` of a button is greater than `0`, or if the `GamepadButton.pressed` property indicates the button has been pressed.

```js
function gameLoop() {
  const gp = navigator.getGamepads()[0];

  if (gp.buttons[0].value > 0 || gp.buttons[0].pressed) {
    b--;
  } else if (gp.buttons[1].value > 0 || gp.buttons[1].pressed) {
    a++;
  } else if (gp.buttons[2].value > 0 || gp.buttons[2].pressed) {
    b++;
  } else if (gp.buttons[3].value > 0 || gp.buttons[3].pressed) {
    a--;
  }

  ball.style.left = `${a * 2}px`; // ball is a UI widget
  ball.style.top = `${b * 2}px`;

  requestAnimationFrame(gameLoop);
}
```

## Specifications

| Specification |
|---|
| Gamepad # gamepadbutton-interface |

## Browser compatibility
