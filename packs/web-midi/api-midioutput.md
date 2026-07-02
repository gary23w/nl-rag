---
title: "MIDIOutput - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MIDIOutput
domain: web-midi
license: CC-BY-SA-4.0
tags: web midi api, midi message port, midi input output, musical instrument digital interface
fetched: 2026-07-02
---

# MIDIOutput

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`MIDIOutput`** interface of the Web MIDI API provides methods to add messages to the queue of an output device, and to clear the queue of messages.

## Instance properties

*This interface doesn't implement any specific properties, but inherits properties from `MIDIPort`.*

## Instance methods

*This interface also inherits methods from `MIDIPort`.*

**`MIDIOutput.send()`**

Queues a message to be sent to the MIDI port.

**`MIDIOutput.clear()`**

Clears any pending send data from the queue.

## Examples

The following example sends a middle C immediately on MIDI channel 1.

```js
function sendMiddleC(midiAccess, portID) {
  const noteOnMessage = [0x90, 60, 0x7f]; // note on, middle C, full velocity
  const output = midiAccess.outputs.get(portID);
  output.send(noteOnMessage); // sends the message.
}
```

## Specifications

| Specification |
|---|
| Web MIDI API # MIDIOutput |

## Browser compatibility
