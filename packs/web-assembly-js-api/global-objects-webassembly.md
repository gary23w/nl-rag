---
title: "WebAssembly - WebAssembly"
source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly
domain: web-assembly-js-api
license: CC-BY-SA-4.0
tags: webassembly javascript api, wasm module instantiation, wasm linear memory, compiled web bytecode
fetched: 2026-07-02
---

# WebAssembly

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`WebAssembly`** JavaScript object acts as the namespace for all WebAssembly-related functionality.

Unlike most other global objects, `WebAssembly` is not a constructor (it is not a function object). You can compare it to `Math`, which is also a namespace object for mathematical constants and functions, or to `Intl` which is the namespace object for internationalization constructors and other language-sensitive functions.

## Description

The primary uses for the `WebAssembly` object are:

- Loading WebAssembly code, using the `WebAssembly.instantiate()` function.
- Creating new memory and table instances via the `WebAssembly.Memory()`/`WebAssembly.Table()` constructors.
- Providing facilities to handle errors that occur in WebAssembly via the `WebAssembly.CompileError()`/`WebAssembly.LinkError()`/`WebAssembly.RuntimeError()` constructors.

## Interfaces

**`WebAssembly.CompileError`**

Indicates an error during WebAssembly decoding or validation.

**`WebAssembly.Global`**

Represents a global variable instance, accessible from both JavaScript and importable/exportable across one or more `WebAssembly.Module` instances. This allows dynamic linking of multiple modules.

**`WebAssembly.Instance`**

Is a stateful, executable instance of a `WebAssembly.Module`

**`WebAssembly.LinkError`**

Indicates an error during module instantiation (besides traps from the start function).

**`WebAssembly.Memory`**

An object whose `buffer` property is a resizable `ArrayBuffer` that holds the raw bytes of memory accessed by a WebAssembly `Instance`.

**`WebAssembly.Module`**

Contains stateless WebAssembly code that has already been compiled by the browser and can be efficiently shared with Workers, and instantiated multiple times.

**`WebAssembly.RuntimeError`**

Error type that is thrown whenever WebAssembly specifies a trap.

**`WebAssembly.Table`**

An array-like structure representing a WebAssembly Table, which stores references, such as function references.

**`WebAssembly.Tag`**

An object that represents a type of WebAssembly exception.

**`WebAssembly.Exception`**

A WebAssembly exception object that can be thrown, caught, and rethrown both within and across WebAssembly/JavaScript boundaries.

## Static properties

**`WebAssembly.JSTag`**

A built-in `WebAssembly.Tag` representing exceptions thrown in the JavaScript host — it allows exceptions thrown in JavaScript to be handled from inside a Wasm module.

## Static methods

**`WebAssembly.compile()`**

Compiles a `WebAssembly.Module` from WebAssembly binary code, leaving instantiation as a separate step.

**`WebAssembly.compileStreaming()`**

Compiles a `WebAssembly.Module` directly from a streamed underlying source, leaving instantiation as a separate step.

**`WebAssembly.instantiate()`**

The primary API for compiling and instantiating WebAssembly code, returning both a `Module` and its first `Instance`.

**`WebAssembly.instantiateStreaming()`**

Compiles and instantiates a WebAssembly module directly from a streamed underlying source, returning both a `Module` and its first `Instance`.

**`WebAssembly.validate()`**

Validates a given typed array of WebAssembly binary code, returning whether the bytes are valid WebAssembly code (`true`) or not (`false`).

## Examples

### Stream a Wasm module then compile and instantiate it

The following example (see our instantiate-streaming.html demo on GitHub, and view it live also) directly streams a Wasm module from an underlying source then compiles and instantiates it, the promise fulfilling with a `ResultObject`. Because the `instantiateStreaming()` function accepts a promise for a `Response` object, you can directly pass it a `fetch()` call, and it will pass the response into the function when it fulfills.

```js
const importObject = {
  my_namespace: { imported_func: (arg) => console.log(arg) },
};

WebAssembly.instantiateStreaming(fetch("simple.wasm"), importObject).then(
  (obj) => obj.instance.exports.exported_func(),
);
```

The `ResultObject`'s `.instance` property is then accessed, and the contained exported function invoked.

## Specifications

| Specification |
|---|
| WebAssembly JavaScript Interface # webassembly-namespace |

## Browser compatibility
