---
title: "SerialPort: open() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/SerialPort/open
domain: web-serial
license: CC-BY-SA-4.0
tags: web serial api, serial port communication, readable writable stream port, serial baud rate config
fetched: 2026-07-02
---

# SerialPort: open() method

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Dedicated Web Workers.

The **`open()`** method of the `SerialPort` interface returns a `Promise` that resolves when the port is opened. By default the port is opened with 8 data bits, 1 stop bit and no parity checking. The `baudRate` parameter is required.

## Syntax

```js
open(options)
```

### Parameters

**`options`**

An object with any of the following values:

**`baudRate`**

A positive, non-zero value indicating the baud rate at which serial communication should be established.

**`bufferSize` Optional**

An unsigned long integer indicating the size of the read and write buffers that are to be established. If not passed, defaults to 255.

**`dataBits` Optional**

An integer value of 7 or 8 indicating the number of data bits per frame. If not passed, defaults to 8.

**`flowControl` Optional**

The flow control type, either `"none"` or `"hardware"`. The default value is `"none"`.

**`parity` Optional**

The parity mode, either `"none"`, `"even"`, or `"odd"`. The default value is `"none"`.

**`stopBits` Optional**

An integer value of 1 or 2 indicating the number of stop bits at the end of the frame. If not passed, defaults to 1.

### Return value

A `Promise`.

### Exceptions

The returned `Promise` rejects with one of the following exceptions:

**`InvalidStateError` `DOMException`**

If `open()` is called when the port is already open.

**`NetworkError` `DOMException`**

If the attempt to open the port failed.

## Examples

Before communicating on a serial port it must be opened. Opening the port allows the site to specify the necessary parameters that control how data is transmitted and received. Developers should check the documentation for the device they are connecting to for the appropriate parameters.

```js
await port.open({ baudRate: 9600 /* pick your baud rate */ });
```

## Specifications

| Specification |
|---|
| Web Serial API # dom-serialport-open |

## Browser compatibility
