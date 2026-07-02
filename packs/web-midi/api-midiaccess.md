---
title: "MIDIAccess - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MIDIAccess
domain: web-midi
license: CC-BY-SA-4.0
tags: web midi api, midi message port, midi input output, musical instrument digital interface
fetched: 2026-07-02
---

# MIDIAccess

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`MIDIAccess`** interface of the Web MIDI API provides methods for listing MIDI input and output devices, and obtaining access to those devices.

`MIDIAccess` is a transferable object.

## Instance properties

**`MIDIAccess.inputs` Read only**

Returns an instance of `MIDIInputMap` which provides access to any available MIDI input ports.

**`MIDIAccess.outputs` Read only**

Returns an instance of `MIDIOutputMap` which provides access to any available MIDI output ports.

**`MIDIAccess.sysexEnabled` Read only**

A boolean attribute indicating whether system exclusive support is enabled on the current MIDIAccess instance.

### Events

**`statechange`**

Called whenever a new MIDI port is added or an existing port changes state.

## Examples

The `Navigator.requestMIDIAccess()` method returns a promise that resolves with a `MIDIAccess` object. Information about the input and output ports is returned.

When a port changes state, information about that port is printed to the console.

```js
navigator.requestMIDIAccess().then((access) => {
  // Get lists of available MIDI controllers
  const inputs = access.inputs.values();
  const outputs = access.outputs.values();

  access.onstatechange = (event) => {
    // Print information about the (dis)connected MIDI controller
    console.log(event.port.name, event.port.manufacturer, event.port.state);
  };
});
```

## Specifications

| Specification |
|---|
| Web MIDI API # midiaccess-interface |

## Browser compatibility
