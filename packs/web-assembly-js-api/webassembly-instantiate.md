---
title: "WebAssembly.instantiate() - WebAssembly"
source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate
domain: web-assembly-js-api
license: CC-BY-SA-4.0
tags: webassembly javascript api, wasm module instantiation, wasm linear memory, compiled web bytecode
fetched: 2026-07-02
---

# WebAssembly.instantiate()

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`WebAssembly.instantiate()`** static method allows you to compile and instantiate WebAssembly code. This function has two overloads:

- The primary overload takes the WebAssembly binary code, in the form of a typed array or `ArrayBuffer`, and performs both compilation and instantiation in one step. The returned `Promise` resolves to both a compiled `WebAssembly.Module` and its first `WebAssembly.Instance`.
- The secondary overload takes an already-compiled `WebAssembly.Module` and returns a `Promise` that resolves to an `Instance` of that `Module`. This overload is useful if the `Module` has already been compiled.

**Warning:** This method is not the most efficient way of fetching and instantiating Wasm modules. If at all possible, you should use the newer `WebAssembly.instantiateStreaming()` method instead, which fetches, compiles, and instantiates a module all in one step, directly from the raw bytecode, so doesn't require conversion to an `ArrayBuffer`.

## Syntax

```js
// Taking Wasm binary code
WebAssembly.instantiate(bufferSource)
WebAssembly.instantiate(bufferSource, importObject)
WebAssembly.instantiate(bufferSource, importObject, compileOptions)

// Taking a module object instance
WebAssembly.instantiate(module)
WebAssembly.instantiate(module, importObject)
WebAssembly.instantiate(module, importObject, compileOptions)
```

### Parameters

**`bufferSource`**

A typed array or `ArrayBuffer` containing the binary code of the Wasm module you want to compile.

**`module`**

The `WebAssembly.Module` object to be instantiated.

**`importObject` Optional**

An object containing the values to be imported into the newly-created `Instance`, such as functions or `WebAssembly.Memory` objects. There must be one matching property for each declared import of the compiled module or else a `WebAssembly.LinkError` is thrown.

**`compileOptions` Optional**

An object containing compilation options. Properties can include:

**`builtins` Optional**

An array of strings that enables the usage of JavaScript builtins in the compiled Wasm module. The strings define the builtins you want to enable. Currently the only available value is `"js-string"`, which enables JavaScript string builtins.

**`importedStringConstants` Optional**

A string specifying a namespace for imported global string constants. This property needs to be specified if you wish to use imported global string constants in the Wasm module.

### Return value

If a `bufferSource` is passed, returns a `Promise` that resolves to a `ResultObject` which contains two fields:

- `module`: A `WebAssembly.Module` object representing the compiled WebAssembly module. This `Module` can be instantiated again, shared via `postMessage()`, or cached.
- `instance`: A `WebAssembly.Instance` object that contains all the Exported WebAssembly functions.

If a `module` is passed, returns a `Promise` that resolves to a `WebAssembly.Instance` object.

### Exceptions

- If either of the parameters are not of the correct type or structure, the promise rejects with a `TypeError`.
- If the operation fails, the promise rejects with a `WebAssembly.CompileError`, `WebAssembly.LinkError`, or `WebAssembly.RuntimeError`, depending on the cause of the failure.

## Examples

**Note:** You'll probably want to use `WebAssembly.instantiateStreaming()` in most cases, as it is more efficient than `instantiate()`.

### First overload example

After fetching some WebAssembly bytecode using fetch, we compile and instantiate the module using the `WebAssembly.instantiate()` function, importing a JavaScript function into the WebAssembly Module in the process. We then call an Exported WebAssembly function that is exported by the `Instance`.

```js
const importObject = {
  my_namespace: {
    imported_func(arg) {
      console.log(arg);
    },
  },
};

fetch("simple.wasm")
  .then((response) => response.arrayBuffer())
  .then((bytes) => WebAssembly.instantiate(bytes, importObject))
  .then((result) => result.instance.exports.exported_func());
```

**Note:** You can also find this example at index.html on GitHub (view it live also).

### Second overload example

The following example (see our index-compile.html demo on GitHub, and view it live also) compiles the loaded simple.wasm byte code using the `WebAssembly.compileStreaming()` method and then sends it to a worker using `postMessage()`.

```js
const worker = new Worker("wasm_worker.js");

WebAssembly.compileStreaming(fetch("simple.wasm")).then((mod) =>
  worker.postMessage(mod),
);
```

In the worker (see `wasm_worker.js`) we define an import object for the module to use, then set up an event handler to receive the module from the main thread. When the module is received, we create an instance from it using the `WebAssembly.instantiate()` method and invoke an exported function from inside it.

```js
const importObject = {
  my_namespace: {
    imported_func(arg) {
      console.log(arg);
    },
  },
};

onmessage = (e) => {
  console.log("module received from main thread");
  const mod = e.data;

  WebAssembly.instantiate(mod, importObject).then((instance) => {
    instance.exports.exported_func();
  });
};
```

### Enabling JavaScript builtins and global string imports

This example enables JavaScript string builtins and imported global string constants when compiling and instantiating the Wasm module with `instantiate()`, before running the exported `main()` function (which logs `"hello world!"` to the console). See it running live.

```js
const importObject = {
  // Regular import
  m: {
    log: console.log,
  },
};

const compileOptions = {
  builtins: ["js-string"], // Enable JavaScript string builtins
  importedStringConstants: "string_constants", // Enable imported global string constants
};

fetch("log-concat.wasm")
  .then((response) => response.arrayBuffer())
  .then((bytes) => WebAssembly.instantiate(bytes, importObject, compileOptions))
  .then((result) => result.instance.exports.main());
```

## Specifications

| Specification |
|---|
| WebAssembly JavaScript Interface # dom-webassembly-instantiate |

## Browser compatibility
