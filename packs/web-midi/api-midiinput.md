---
title: "MIDIInput - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MIDIInput
domain: web-midi
license: CC-BY-SA-4.0
tags: web midi api, midi message port, midi input output, musical instrument digital interface
fetched: 2026-07-02
---

# MIDIInput

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`MIDIInput`** interface of the Web MIDI API receives messages from a MIDI input port.

## Instance properties

*This interface doesn't implement any specific properties, but inherits properties from `MIDIPort`.*

## Instance methods

*This interface doesn't implement any specific methods, but inherits methods from `MIDIPort`.*

### Events

**`midimessage`**

Fired when the current port receives a MIDI message.

## Examples

In the following example the name of each `MIDIInput` is printed to the console. Then, `midimessage` events are listened for on all input ports. When a message is received the `MIDIMessageEvent.data` property is printed to the console.

```js
inputs.forEach((input) => {
  console.log(input.name); /* inherited property from MIDIPort */
  input.onmidimessage = (message) => {
    console.log(message.data);
  };
});
```

## Specifications

| Specification |
|---|
| Web MIDI API # midiinput-interface |

## Browser compatibility
