---
title: "NDEFReader - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/NDEFReader
domain: web-nfc
license: CC-BY-SA-4.0
tags: web nfc api, near field communication, ndef record message, contactless tag reading
fetched: 2026-07-02
---

# NDEFReader

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

The **`NDEFReader`** interface of the Web NFC API is used to read from and write data to compatible NFC devices, e.g., NFC tags supporting NDEF, when these devices are within the reader's magnetic induction field.

## Constructor

**`NDEFReader()`**

Returns a new `NDEFReader` object.

## Instance methods

*The `NDEFReader` interface inherits the methods of `EventTarget`, its parent interface.*

**`NDEFReader.scan()`**

Activates a reading device and returns a `Promise` that either resolves when an NFC tag read operation is scheduled or rejects if a hardware or permission error is encountered. This method triggers a permission prompt if the "nfc" permission has not been previously granted.

**`NDEFReader.write()`**

Attempts to write an NDEF message to a tag and returns a `Promise` that either resolves when a message has been written to the tag or rejects if a hardware or permission error is encountered. This method triggers a permission prompt if the "nfc" permission has not been previously granted.

## Events

*Inherits events from its parent, `EventTarget`.*

**`reading`**

Fires when a new reading is available from compatible NFC devices.

**`readingerror`**

Fires when a tag is in proximity of a reading device, but cannot be read.

## Examples

### Handling initial reads while writing

The example below shows how to coordinate between a common reading handler and one used specifically for a single write. In order to write, a tag needs to be found and read. This gives you the ability to check whether it is actually a tag that you want to write to. That's why it's recommended that you call `write()` from a reading event.

```js
const ndef = new NDEFReader();
let ignoreRead = false;

ndef.onreading = (event) => {
  if (ignoreRead) {
    return; // write pending, ignore read.
  }

  console.log("We read a tag, but not during pending write!");
};

function write(data) {
  ignoreRead = true;
  return new Promise((resolve, reject) => {
    ndef.addEventListener(
      "reading",
      (event) => {
        // Check if we want to write to this tag, or reject.
        ndef
          .write(data)
          .then(resolve, reject)
          .finally(() => (ignoreRead = false));
      },
      { once: true },
    );
  });
}

await ndef.scan();
try {
  await write("Hello World");
  console.log("We wrote to a tag!");
} catch (err) {
  console.error("Something went wrong", err);
}
```

## Specifications

| Specification |
|---|
| Web NFC # the-ndefreader-object |

## Browser compatibility
