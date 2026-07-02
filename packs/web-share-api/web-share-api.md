---
title: "Web Share API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Web_Share_API
domain: web-share-api
license: CC-BY-SA-4.0
tags: web share api, native share sheet, share target registration, shared file payload
fetched: 2026-07-02
---

# Web Share API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **Web Share API** provides a mechanism for sharing text, links, files, and other content to an arbitrary *share target* selected by the user.

**Note:** This API is *not available* in Web Workers (not exposed via `WorkerNavigator`).

**Note:** This API should not be confused with the Web Share Target API, which allows a website to specify itself as a share target.

## Concepts and usage

The **Web Share API** allows a site to share text, links, files, and other content to user-selected share targets, utilizing the sharing mechanisms of the underlying operating system. These share targets typically include the system clipboard, email, contacts or messaging applications, and Bluetooth or Wi-Fi channels.

The API has just two methods. The `navigator.canShare()` method may be used to first validate whether some data is "shareable", prior to passing it to `navigator.share()` for sending.

The `navigator.share()` method invokes the native sharing mechanism of the underlying operating system and passes the specified data. It requires transient activation, and hence must be triggered off a UI event like a button click. Further, the method must specify valid data that is supported for sharing by the native implementation.

The Web Share API is gated by the web-share Permissions Policy. If the policy is supported but has not been granted, both methods will indicate that the data is not shareable.

## Interfaces

### Extensions to other interfaces

**`navigator.canShare()`**

Returns a boolean indicating whether the specified data is shareable.

**`navigator.share()`**

Returns a `Promise` that resolves if the passed data was successfully sent to a share target. This method must be called on a button click or other user activation (requires transient activation).

## Example

The code below shows how you can share a link using `navigator.share()`, triggered off a button click.

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

The above example is taken from our Web share test (see the source code). You can also see this as a live example in `navigator.share()`.

## Specifications

| Specification |
|---|
| Web Share API |

## Browser compatibility

### api.Navigator.share

### api.Navigator.canShare
