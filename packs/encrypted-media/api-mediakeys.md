---
title: "MediaKeys - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MediaKeys
domain: encrypted-media
license: CC-BY-SA-4.0
tags: encrypted media extensions, content decryption module, digital rights management, media key session
fetched: 2026-07-02
---

# MediaKeys

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2019.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`MediaKeys`** interface of Encrypted Media Extensions API represents a set of keys that an associated `HTMLMediaElement` can use for decryption of media data during playback.

## Instance properties

None.

## Instance methods

**`MediaKeys.createSession()`**

Returns a new `MediaKeySession` object, which represents a context for message exchange with a content decryption module (CDM).

**`MediaKeys.getStatusForPolicy()`**

Returns a `Promise` that resolves to a status string indicating whether the CDM would allow the presentation of encrypted media data using the keys, based on specified policy requirements.

**`MediaKeys.setServerCertificate()`**

Returns a `Promise` to a server certificate to be used to encrypt messages to the license server.

## Examples

### Check if keys are usable with HDCP restriction

This example shows how `getStatusForPolicy()` can be used to check if keys can decrypt a particular video format in a setup that has a minimum HDCP version of `2.2`. For more information, see the MediaKeys: getStatusForPolicy() method documentation.

#### HTML

```html
<pre id="log"></pre>
```

```css
#log {
  height: 100px;
  overflow: scroll;
  padding: 0.5rem;
  border: 1px solid black;
}
```

#### JavaScript

```js
const logElement = document.querySelector("#log");
function log(text) {
  logElement.innerText = `${logElement.innerText}${text}\n`;
  logElement.scrollTop = logElement.scrollHeight;
}
```

```js
const config = [
  {
    videoCapabilities: [
      {
        contentType: 'video/mp4; codecs="avc1.640028"',
        encryptionScheme: "cenc",
        robustness: "SW_SECURE_DECODE", // Widevine L3
      },
    ],
  },
];

getMediaStatus(config);

async function getMediaStatus(config) {
  try {
    const mediaKeySystemAccess = await navigator.requestMediaKeySystemAccess(
      "com.widevine.alpha",
      config,
    );
    const mediaKeys = await mediaKeySystemAccess.createMediaKeys();
    const mediaStatus = await mediaKeys.getStatusForPolicy({
      minHdcpVersion: "2.2",
    });
    log(mediaStatus);

    // Get the content or fallback to an alternative if the
    // keys are not usable
    if (mediaStatus === "usable") {
      console.log("HDCP 2.2 can be enforced.");
      // Fetch the high resolution protected content
    } else {
      log("HDCP 2.2 cannot be enforced");
      // Fallback other content, get license, etc.
    }
  } catch (error) {
    log(error);
  }
}
```

#### Results

## Specifications

| Specification |
|---|
| Encrypted Media Extensions # mediakeys-interface |

## Browser compatibility
