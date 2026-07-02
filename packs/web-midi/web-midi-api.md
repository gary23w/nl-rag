---
title: "Web MIDI API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API
domain: web-midi
license: CC-BY-SA-4.0
tags: web midi api, midi message port, midi input output, musical instrument digital interface
fetched: 2026-07-02
---

# Web MIDI API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The Web MIDI API connects to and interacts with Musical Instrument Digital Interface (MIDI) Devices.

The interfaces deal with the practical aspects of sending and receiving MIDI messages. Therefore, the API can be used for musical and non-musical uses, with any MIDI device connected to your computer.

## Interfaces

**`MIDIInputMap`**

Represents all of the available MIDI input ports.

**`MIDIOutputMap`**

Represents all of the available MIDI output ports.

**`MIDIAccess`**

Provides the methods to list input and output devices, and to access an individual device.

**`MIDIPort`**

Represents an individual MIDI port.

**`MIDIInput`**

Provides a method for dealing with MIDI messages from an input port.

**`MIDIOutput`**

Queues messages to the linked MIDI port. Messages can be sent immediately or after a specified delay.

**`MIDIMessageEvent`**

The event passed to the `MIDIInput` `midimessage` event.

**`MIDIConnectionEvent`**

The event passed to the `MIDIAccess` `statechange` and `MIDIPort` `statechange` events, when a port becomes available or unavailable.

## Security requirements

Access to the API is requested using the `navigator.requestMIDIAccess()` method.

- The method must be called in a secure context.
- Access may be gated by the `midi` HTTP Permission Policy.
- The user must explicitly grant permission to use the API through a user-agent specific mechanism, or have previously granted permission. Note that if access is denied by a permission policy it cannot be granted by a user permission.

The permission status can be queried using the Permissions API method `navigator.permissions.query()`, passing a permission descriptor with the `midi` permission and (optional) `sysex` property:

```js
navigator.permissions.query({ name: "midi", sysex: true }).then((result) => {
  if (result.state === "granted") {
    // Access granted.
  } else if (result.state === "prompt") {
    // Using API will prompt for permission
  }
  // Permission was denied by user prompt or permission policy
});
```

## Examples

### Gaining access to the MIDI port

The `navigator.requestMIDIAccess()` method returns a promise that resolves to a `MIDIAccess` object, which can then be used to access a MIDI device. The method must be called in a secure context.

```js
let midi = null; // global MIDIAccess object
function onMIDISuccess(midiAccess) {
  console.log("MIDI ready!");
  midi = midiAccess; // store in the global (in real usage, would probably keep in an object instance)
}

function onMIDIFailure(msg) {
  console.error(`Failed to get MIDI access - ${msg}`);
}

navigator.requestMIDIAccess().then(onMIDISuccess, onMIDIFailure);
```

### Listing inputs and outputs

In this example the list of input and output ports are retrieved and printed to the console.

```js
function listInputsAndOutputs(midiAccess) {
  for (const entry of midiAccess.inputs) {
    const input = entry[1];
    console.log(
      `Input port [type:'${input.type}']` +
        ` id:'${input.id}'` +
        ` manufacturer:'${input.manufacturer}'` +
        ` name:'${input.name}'` +
        ` version:'${input.version}'`,
    );
  }

  for (const entry of midiAccess.outputs) {
    const output = entry[1];
    console.log(
      `Output port [type:'${output.type}'] id:'${output.id}' manufacturer:'${output.manufacturer}' name:'${output.name}' version:'${output.version}'`,
    );
  }
}
```

### Handling MIDI Input

This example prints all MIDI input messages to the console.

```js
function onMIDIMessage(event) {
  let str = `MIDI message received at timestamp ${event.timeStamp}[${event.data.length} bytes]: `;
  for (const character of event.data) {
    str += `0x${character.toString(16)} `;
  }
  console.log(str);
}

function startLoggingMIDIInput(midiAccess) {
  midiAccess.inputs.forEach((entry) => {
    entry.onmidimessage = onMIDIMessage;
  });
}
```

## Specifications

| Specification |
|---|
| Web MIDI API |

## Browser compatibility

### api.Navigator.requestMIDIAccess

### http.headers.Permissions-Policy.midi

### api.Permissions.permission_midi
