---
title: "File - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/File
domain: multer-upload
license: CC-BY-SA-4.0
tags: multer upload, multipart form data handling, file upload middleware, express file parsing
fetched: 2026-07-02
---

# File

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`File`** interface provides information about files and allows JavaScript in a web page to access their content.

`File` objects are generally retrieved from a `FileList` object returned as a result of a user selecting files using the `<input>` element, or from a drag and drop operation's `DataTransfer` object.

A `File` object is a specific kind of `Blob`, and can be used in any context that a Blob can. In particular, the following APIs accept both `Blob`s and `File` objects:

- `FileReader`
- `URL.createObjectURL()`
- `Window.createImageBitmap()` and `WorkerGlobalScope.createImageBitmap()`
- the `body` option to `fetch()`
- `XMLHttpRequest.send()`

See Using files from web applications for more information and examples.

## Constructor

**`File()`**

Returns a newly constructed `File`.

## Instance properties

*The `File` interface also inherits properties from the `Blob` interface.*

**`File.lastModified` Read only**

Returns the last modified time of the file, in millisecond since the UNIX epoch (January 1st, 1970 at Midnight).

**`File.lastModifiedDate` Read only**

Returns the last modified `Date` of the file referenced by the `File` object.

**`File.name` Read only**

Returns the name of the file referenced by the `File` object.

**`File.webkitRelativePath` Read only**

Returns the path the URL of the `File` is relative to.

## Instance methods

*The `File` interface also inherits methods from the `Blob` interface.*

## Specifications

| Specification |
|---|
| File API # file-section |

## Browser compatibility
