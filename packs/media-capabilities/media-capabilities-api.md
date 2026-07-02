---
title: "Media Capabilities API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Media_Capabilities_API
domain: media-capabilities
license: CC-BY-SA-4.0
tags: media capabilities api, decoding playback ability, media codec support query, smooth power-efficient playback
fetched: 2026-07-02
---

# Media Capabilities API

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **Media Capabilities API** allows developers to determine decoding and encoding abilities of the device, exposing information such as whether media is supported and whether playback should be smooth and power efficient.

## Concepts

There are a myriad of video and audio codecs. Different browsers support different media types and new media types are always being developed. With the Media Capabilities API, developers can ensure each user is getting the best bitrate and storage savings for their browser, device, and OS capabilities.

Whether a device uses hardware or software decoding impacts how smooth and power efficient the video decoding is and how efficient the playback will be. The Media Capabilities API enables developers to determine which codecs are supported and how performant a media file will be both in terms of smoothness and power efficiency.

The Media Capabilities API provide more powerful features than other APIs such as `MediaRecorder.isTypeSupported()` or `HTMLMediaElement.canPlayType()`, which only address general browser support, not performance.

To test support, smoothness, and power efficiency for encoding and decoding video or audio content, you use the `MediaCapabilities` interface's `encodingInfo()` and `decodingInfo()` methods.

## Interfaces

**`MediaCapabilities`**

Provides information about the decoding abilities of the device, system and browser based on codecs, profile, resolution, and bitrates. The information can be used to serve optimal media streams to the user and determine if playback should be smooth and power efficient.

### Extensions to other interfaces

**`Navigator.mediaCapabilities` Read only**

A `MediaCapabilities` object that can expose information about the decoding and encoding capabilities for a given media format and output capabilities.

**`WorkerNavigator.mediaCapabilities` Read only**

A `MediaCapabilities` object that can expose information about the decoding and encoding capabilities for a given media format and output capabilities.

## Examples

### Detect audio file support and expected performance

This example defines an audio configuration then checks to see if the user agent supports decoding that media configuration, and whether it will perform well in terms of smoothness and power efficiency.

```js
if ("mediaCapabilities" in navigator) {
  const audioFileConfiguration = {
    type: "file",
    audio: {
      contentType: "audio/mp3",
      channels: 2,
      bitrate: 132700,
      samplerate: 5200,
    },
  };

  navigator.mediaCapabilities
    .decodingInfo(audioFileConfiguration)
    .then((result) => {
      console.log(
        `This configuration is ${result.supported ? "" : "not "}supported,`,
      );
      console.log(`${result.smooth ? "" : "not "}smooth, and`);
      console.log(`${result.powerEfficient ? "" : "not "}power efficient.`);
    })
    .catch(() => {
      console.log(`decodingInfo error: ${contentType}`);
    });
}
```

## Specifications

| Specification |
|---|
| Media Capabilities # media-capabilities-interface |

## Browser compatibility
