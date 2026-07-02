---
title: "Navigator: share() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share
domain: web-share-api
license: CC-BY-SA-4.0
tags: web share api, native share sheet, share target registration, shared file payload
fetched: 2026-07-02
---

# Navigator: share() method

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`share()`** method of the `Navigator` interface invokes the native sharing mechanism of the device to share data such as text, URLs, or files. The available *share targets* depend on the device, but might include the clipboard, contacts and email applications, websites, Bluetooth, etc.

The method resolves a `Promise` with `undefined`. On Windows this happens when the share popup is launched, while on Android the promise resolves once the data has successfully been passed to the *share target*.

The Web Share API is gated by the web-share permission policy. The `share()` method will throw exceptions if the permission is supported but has not been granted.

## Syntax

```js
share(data)
```

### Parameters

**`data` Optional**

An object containing data to share.

Properties that are unknown to the user agent are ignored; share data is only assessed on properties understood by the user agent. All properties are optional but at least one known data property must be specified.

Possible values are:

**`url` Optional**

A string representing a URL to be shared.

**`text` Optional**

A string representing text to be shared.

**`title` Optional**

A string representing a title to be shared. May be ignored by the target.

**`files` Optional**

An array of `File` objects representing files to be shared. See below for shareable file types.

### Return value

A `Promise` that resolves with `undefined`, or rejected with one of the Exceptions given below.

### Exceptions

The `Promise` may be rejected with one of the following `DOMException` values:

**`InvalidStateError` `DOMException`**

The document is not fully active, or other sharing operations are in progress.

**`NotAllowedError` `DOMException`**

A `web-share` Permissions Policy has been used to block the use of this feature, the window does not have transient activation, or a file share is being blocked due to security considerations.

**`TypeError`**

The specified share data cannot be validated. Possible reasons include:

- The `data` parameter was omitted completely or only contains properties with unknown values. Note that any properties that are not recognized by the user agent are ignored.
- A URL is badly formatted.
- Files are specified but the implementation does not support file sharing.
- Sharing the specified data would be considered a "hostile share" by the user-agent.

**`AbortError` `DOMException`**

The user canceled the share operation or there are no share targets available.

**`DataError` `DOMException`**

There was a problem starting the share target or transmitting the data.

## Shareable file types

The following is a list of usually shareable file types. However, you should always test with `navigator.canShare()` if sharing would succeed.

- Application
  - `.pdf` - `application/pdf`
- Audio
  - `.flac` - `audio/flac`
  - `.m4a` - `audio/x-m4a`
  - `.mp3` - `audio/mpeg` (also accepts `audio/mp3`)
  - `.oga` - `audio/ogg`
  - `.ogg` - `audio/ogg`
  - `.opus` - `audio/ogg`
  - `.wav` - `audio/wav`
  - `.weba` - `audio/webm`
- Image
  - `.avif` - `image/avif`
  - `.bmp` - `image/bmp`
  - `.gif` - `image/gif`
  - `.ico` - `image/x-icon`
  - `.jfif` - `image/jpeg`
  - `.jpeg` - `image/jpeg`
  - `.jpg` - `image/jpeg`
  - `.pjp` - `image/jpeg`
  - `.pjpeg` - `image/jpeg`
  - `.png` - `image/png`
  - `.svg` - `image/svg+xml`
  - `.svgz` - `image/svg+xml`
  - `.tif` - `image/tiff`
  - `.tiff` - `image/tiff`
  - `.webp` - `image/webp`
  - `.xbm` - `image/x-xbitmap`
- Text
  - `.css` - `text/css`
  - `.csv` - `text/csv`
  - `.ehtml` - `text/html`
  - `.htm` - `text/html`
  - `.html` - `text/html`
  - `.shtm` - `text/html`
  - `.shtml` - `text/html`
  - `.text` - `text/plain`
  - `.txt` - `text/plain`
- Video
  - `.m4v` - `video/mp4`
  - `.mp4` - `video/mp4`
  - `.mpeg` - `video/mpeg`
  - `.mpg` - `video/mpeg`
  - `.ogm` - `video/ogg`
  - `.ogv` - `video/ogg`
  - `.webm` - `video/webm`

## Security

This method requires that the current document have the web-share Permissions Policy and transient activation. (It must be triggered off a UI event like a button click and cannot be launched at arbitrary points by a script.) Further, the method must specify valid data that is supported for sharing by the native implementation.

## Examples

### Sharing a URL

The example below shows a button click invoking the Web Share API to share MDN's URL. This is taken from our Web share test (see the source code).

#### HTML

The HTML just creates a button to trigger the share, and a paragraph in which to display the result of the test.

```html
<p><button>Share MDN!</button></p>
<p class="result"></p>
```

#### JavaScript

```js
const shareData = {
  title: "MDN",
  text: "Learn web development on MDN!",
  url: "https://developer.mozilla.org",
};

const btn = document.querySelector("button");
const resultPara = document.querySelector(".result");

// Share must be triggered by "user activation"
btn.addEventListener("click", async () => {
  try {
    await navigator.share(shareData);
    resultPara.textContent = "MDN shared successfully";
  } catch (err) {
    resultPara.textContent = `Error: ${err}`;
  }
});
```

#### Result

Click the button to launch the share dialog on your platform. Text will appear below the button to indicate whether the share was successful or provide an error code.

### Sharing files

To share files, first test for and call `navigator.canShare()`. Then include the list of files in the call to `navigator.share()`.

#### HTML

```html
<div>
  <label for="files">Select images to share:</label>
  <input id="files" type="file" accept="image/*" multiple />
</div>
<button id="share" type="button">Share your images!</button>
<output id="output"></output>
```

#### JavaScript

Note that the data object passed to the `navigator.canShare()` only includes the `files` property, as the `title` and `text` shouldn't matter.

```js
const input = document.getElementById("files");
const output = document.getElementById("output");

document.getElementById("share").addEventListener("click", async () => {
  const files = input.files;

  if (files.length === 0) {
    output.textContent = "No files selected.";
    return;
  }

  // feature detecting navigator.canShare() also implies
  // the same for the navigator.share()
  if (!navigator.canShare) {
    output.textContent = `Your browser doesn't support the Web Share API.`;
    return;
  }

  if (navigator.canShare({ files })) {
    try {
      await navigator.share({
        files,
        title: "Images",
        text: "Beautiful images",
      });
      output.textContent = "Shared!";
    } catch (error) {
      output.textContent = `Error: ${error.message}`;
    }
  } else {
    output.textContent = `Your system doesn't support sharing these files.`;
  }
});
```

#### Result

## Specifications

| Specification |
|---|
| Web Share API # share-method |

## Browser compatibility
