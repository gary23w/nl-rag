---
title: "Event: bubbles property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Event/bubbles
domain: dom-events
license: CC-BY-SA-2.5
tags: dom events, event listener, event bubbling, event delegation, addeventlistener
fetched: 2026-07-02
---

# Event: bubbles property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`bubbles`** read-only property of the `Event` interface indicates whether the event bubbles up through the DOM tree or not.

**Note:** See Event bubbling for more information on bubbling.

## Value

A boolean value, which is `true` if the event bubbles up through the DOM tree.

## Example

```js
function handleInput(e) {
  // Check whether the event bubbles passes the event along
  if (!e.bubbles) {
    passItOn(e);
  }

  // Already bubbling
  doOutput(e);
}
```

## Specifications

| Specification |
|---|
| DOM # ref-for-dom-event-bubbles③ |

## Browser compatibility
