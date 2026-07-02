---
title: "WebRTC"
source: https://en.wikipedia.org/wiki/WebRTC
domain: webrtc-datachannel
license: CC-BY-SA-4.0
tags: webrtc datachannel, peer-to-peer data channel, browser peer connection, webrtc data transfer
fetched: 2026-07-02
---

# WebRTC

**WebRTC** (**Web Real-Time Communication**) is a free and open-source project providing web browsers and mobile applications with real-time communication (RTC) via application programming interfaces (APIs). It allows audio and video communication and streaming to work inside web pages by allowing direct peer-to-peer communication, eliminating the need to install plugins or download native apps.

Supported by Apple, Google, Microsoft, Mozilla, and Opera, WebRTC specifications have been published by the World Wide Web Consortium (W3C) and the Internet Engineering Task Force (IETF).

ICE, STUN and TURN are the NAT traversal techniques used to connect to remote peers.

## History

In May 2010, Google bought Global IP Solutions or GIPS, a VoIP and videoconferencing software company that had developed many components required for RTC, such as codecs and echo cancellation techniques. Google open-sourced the GIPS technology and engaged with relevant standards bodies at the IETF and W3C to ensure industry consensus. In May 2011, Google released an open-source project for browser-based real-time communication known as WebRTC. This has been followed by ongoing work to standardize the relevant protocols in the IETF and browser APIs in the W3C.

In January 2011, Ericsson Labs built the first implementation of WebRTC using a modified WebKit library. In October 2011, the W3C published its first draft for the spec. WebRTC milestones include the first cross-browser video call (February 2013), first cross-browser data transfers (February 2014), and as of July 2014 Google Hangouts was "kind of" using WebRTC.

The W3C draft API was based on preliminary work done in the WHATWG. It was referred to as the ConnectionPeer API, and a pre-standards concept implementation was created at Ericsson Labs. The WebRTC Working Group expects this specification to evolve significantly based on:

- Outcomes of ongoing exchanges in the companion RTCWEB group at IETF to define the set of protocols that, together with this document, define real-time communications in web browsers. While no one signaling protocol is mandated, SIP over WebSockets (RFC 7118) is often used partially due to the applicability of SIP to most of the envisaged communication scenarios as well as the availability of open-source software such as JsSIP.
- Privacy issues that arise when exposing local capabilities and local streams
- Technical discussions within the group, on implementing data channels in particular
- Experience gained through early experimentation
- Feedback from other groups and individuals

In November 2017, the WebRTC 1.0 specification transitioned from Working Draft to Candidate Recommendation.

In January 2021, the WebRTC 1.0 specification transitioned from Candidate Recommendation to Recommendation.

## Design

Major components of WebRTC include several JavaScript APIs:

- `getUserMedia` acquires the audio and video media (e.g., by accessing a device's camera and microphone).
- `RTCPeerConnection` enables audio and video communication between peers. It performs signal processing, codec handling, peer-to-peer communication, security, and bandwidth management.
- `RTCDataChannel` allows bidirectional communication of arbitrary data between peers. The data is transported using SCTP over DTLS. It uses the same API as WebSockets and has very low latency.

The WebRTC API also includes a statistics function:

- `getStats` allows the web application to retrieve a set of statistics about WebRTC sessions. These statistics data are being described in a separate W3C document.

The WebRTC API includes **no provisions for signaling**, that is discovering peers to connect to and determine how to establish connections among them. Applications use Interactive Connectivity Establishment for connections and are responsible for managing sessions, possibly relying on any of Session Initiation Protocol, Extensible Messaging and Presence Protocol (XMPP), Message Queuing Telemetry Transport, Matrix, or another protocol. Signaling may depend on one or more servers.

RFC 7478 requires implementations to provide PCMA/PCMU (RFC 3551), Telephone Event as DTMF (RFC 4733), and Opus (RFC 6716) audio codecs as minimum capabilities. The PeerConnection, data channel and media capture browser APIs are detailed in the W3C specification.

W3C is developing ORTC (Object Real-Time Communications) for WebRTC.

## Applications

WebRTC allows browsers to stream files directly to one another, reducing or entirely removing the need for server-side file hosting. WebTorrent uses a WebRTC transport to enable peer-to-peer file sharing using the BitTorrent protocol in the browser. Some file-sharing websites use it to allow users to send files directly to one another in their browsers, although this requires the uploader to keep the tab open until the file has been downloaded. A few CDNs, such as the Microsoft-owned Peer5, use the client's bandwidth to upload media to other connected peers, enabling each peer to act as an edge server.

Although initially developed for web browsers, WebRTC has applications for non-browser devices, including mobile platforms and IoT devices. Examples include browser-based VoIP telephony, also called cloud phones or web phones, which allow calls to be made and received from within a web browser, replacing the requirement to download and install a softphone.

## Support

WebRTC is supported by the following browsers (incomplete list; oldest supported version specified):

- Desktop PC
  - Microsoft Edge 12+
  - Google Chrome 28+
  - Mozilla Firefox 22+
  - Safari 11+
  - Opera 18+
  - Vivaldi 1.9+
  - Brave
- Android
  - Google Chrome 28+ (enabled by default since 29)
  - Mozilla Firefox 24+
  - Opera Mobile 12+
- ChromeOS
- Firefox OS
- BlackBerry 10
- iOS
  - MobileSafari/WebKit (iOS 11+)
- Tizen 3.0

### Codec support across browsers

WebRTC establishes a standard set of codecs which all compliant browsers are required to implement (underlined). Some browsers may also support other codecs.

| Codec name | Profile | Browser compatibility |
|---|---|---|
| H.264 | Constrained Baseline (CB) | Chrome, Edge, Firefox, Safari (12.1+) |
| VP8 | - | Chrome (52+), Edge, Firefox, Safari |
| VP9 | - | Chrome (48+), Firefox |
| AV1 | - | Chrome (113+), Firefox (136+) |

| Codec name | Browser compatibility |
|---|---|
| Opus | Chrome, Firefox, Safari |
| G.711 PCM (A-law) | Chrome, Firefox, Safari |
| G.711 PCM (μ-law) | Chrome, Firefox, Safari |
| G.722 | Chrome, Firefox, Safari |
| iLBC | Chrome, Safari |
| iSAC | Chrome, Safari |

## Vulnerability

In January 2015, TorrentFreak reported a serious security flaw in browsers supporting WebRTC, that compromised the security of VPN tunnels by exposing a user's true IP address. The IP address read requests are not visible in the browser's developer console, and they are not blocked by most ad blocking, privacy and security add-ons, enabling online tracking despite precautions.

It has been reported that the cause of the address leak is not a bug that can be patched, but is foundational to the way WebRTC operates; however, there are several solutions to mitigate the problem. WebRTC leakage can be tested for, and solutions are offered for most browsers. WebRTC can be disabled, if not required, in most browsers. The uBlock Origin add-on can fix this problem (as some browsers now fix this problem by themselves, from uBlock Origin v1.38 onwards this option has been disabled on these browsers).

## Limitations

Like HTTP3/QUIC, WebRTC cannot be tunneled over TOR because TOR doesn't support UDP, thus most WebRTC applications don't work without bypassing TOR or using TURN servers.
