---
title: "Encrypted Media Extensions"
source: https://en.wikipedia.org/wiki/Encrypted_Media_Extensions
domain: encrypted-media
license: CC-BY-SA-4.0
tags: encrypted media extensions, content decryption module, digital rights management, media key session
fetched: 2026-07-02
---

# Encrypted Media Extensions

**Encrypted Media Extensions** (**EME**) is a W3C specification for providing a communication channel between web browsers and the Content Decryption Module (CDM) software which implements digital rights management (DRM). This allows the use of HTML video to play back DRM-wrapped content such as streaming video services without the use of heavy third-party media plugins like Adobe Flash or Microsoft Silverlight (both discontinued). The use of a third-party key management system may be required, depending on whether the publisher chooses to scramble the keys.

EME is based on the Media Source Extensions (MSE) specification, which enables adaptive bitrate streaming in HTML audio and video, e.g. using MPEG-DASH with MPEG-CENC protected content.

EME has been highly controversial because it places a necessarily proprietary, closed decryption component which requires per-browser licensing fees into what might otherwise be an entirely open and free software ecosystem. On July 6, 2017, W3C publicly announced its intention to publish an EME web standard, and did so on September 18. On the same day, the Electronic Frontier Foundation, who joined in 2014 to participate in the decision making, published an open letter resigning from W3C.

## Support

In April 2013, on the Samsung Chromebook, Netflix became the first company to offer HTML video using EME.

As of 2016, the Encrypted Media Extensions interface has been implemented in the Google Chrome, Internet Explorer, Safari, Firefox, and Microsoft Edge browsers.

While backers and the developers of the Firefox web browser were hesitant in implementing the protocol for ethical reasons due to its dependency on proprietary code, Firefox introduced EME support on Windows platforms in May 2015, originally using Adobe's Primetime DRM library, later replaced with the Widevine library (CDM). Firefox's implementation of EME uses an open-source sandbox to load the proprietary DRM modules, which are treated as plug-ins that are loaded when EME-encrypted content is requested. The sandbox was also designed to frustrate the ability for services and the DRM to uniquely track and identify devices. Additionally, it is always possible to disable DRM in Firefox, which then not only disables EME, but also uninstalls the Widevine DRM libraries. Alternately, official Firefox builds that are designated as "EME-free" have been distributed alongside regular Firefox builds as of Firefox 145.0.2.

Netflix supports HTML video using EME with a supported web browser: Chrome, Firefox, Microsoft Edge, Internet Explorer (on Windows 8.1 or newer), or Safari (on OS X Yosemite or newer). YouTube supports the MSE. Available players supporting MPEG-DASH using the MSE and EME are NexPlayer, THEOplayer by OpenTelly, the bitdash MPEG-DASH player, dash.js by DASH-IF or rx-player.

Note that in Firefox and Chrome, EME does not work unless the media is supplied via Media Source Extensions.

Version 4.3 and subsequent versions of Android support EME.

### Content Decryption Modules

- Adobe Primetime CDM (used by old Firefox versions 47 to 51)
- Widevine (used in Chrome and Firefox + their derivatives, including Opera and newest versions of Microsoft Edge)
- PlayReady (used in EdgeHTML-based Microsoft Edge on Windows 10 and Internet Explorer 11 for Windows 8.1 and 10)
- FairPlay (used in Safari since OS X Yosemite)

## Criticism

EME has faced strong criticism from both inside and outside W3C. The major issues for criticism are implementation issues for open-source browsers, entry barriers for new browsers, lack of interoperability, concerns about security, privacy and accessibility, and possibility of legal trouble in the United States due to Chapter 12 of the DMCA.

In July 2020, Reddit started using a fingerprinting mechanism that involves loading every DRM module that browsers can support, and logs what ends up loading as part of the data collected. Users noticed this when Firefox began alerting them that Reddit "required" them to load DRM software to play media, although none of the media on the page actually needed it.

As of 2020, the ways in which EME interferes with open source have become concrete. None of the widely used CDMs are being licensed to independent open-source browser providers without paying a per-browser licensing fee (particularly to Google – for their Widevine CDM, which is used in nearly all recently developed web browsers).
