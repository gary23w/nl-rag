---
title: "Dynamic Adaptive Streaming over HTTP"
source: https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP
domain: media-source-extensions
license: CC-BY-SA-4.0
tags: media source extensions, source buffer append, adaptive streaming buffer, segmented media playback
fetched: 2026-07-02
---

# Dynamic Adaptive Streaming over HTTP

**Dynamic Adaptive Streaming over HTTP** (**DASH**), also known as **MPEG-DASH**, is an adaptive bitrate streaming technique that enables high quality streaming of media content over the Internet delivered from conventional HTTP web servers.

Similar to Apple's HTTP Live Streaming (HLS) solution, MPEG-DASH works by breaking the content into a sequence of small segments, which are served over HTTP. Each segment contains a short interval of playback time of content that is potentially many hours in duration, such as a movie or the live broadcast of a sport event. The content is made available at a variety of different bit rates, i.e., alternative segments encoded at different bit rates covering aligned short intervals of playback time. While the content is being played back by an MPEG-DASH client, the client uses a bit rate adaptation (ABR) algorithm to automatically select the segment with the highest bit rate possible that can be downloaded in time for playback without causing stalls or re-buffering events in the playback. Thus, an MPEG-DASH client can seamlessly adapt to changing network conditions and provide high quality playback with few stalls or re-buffering events.

MPEG-DASH is the first adaptive bit-rate HTTP-based streaming solution that is an international standard. MPEG-DASH should not be confused with a transport protocol — the transport protocol that MPEG-DASH uses depends on which version of HTTP is used: TCP is the transport over which HTTP and HTTP/2 run, while HTTP/3 runs over QUIC (which in turn runs over UDP). MPEG-DASH uses existing HTTP web server infrastructure that is used for delivery of essentially all World Wide Web content. It allows devices like Internet-connected televisions, TV set-top boxes, desktop computers, smartphones, tablets, etc. to receive multimedia content (video, TV, radio, etc.) delivered via the Internet, coping with variable Internet receiving conditions. Standardizing an adaptive streaming solution is meant to provide confidence to the market that the solution can be adopted for universal deployment, compared to similar but more proprietary solutions like Smooth Streaming by Microsoft, or HDS by Adobe. Unlike HDS, or Smooth Streaming, DASH is codec-agnostic, which means it can use content encoded with any coding format, such as H.265, H.264, VP9, etc.

## Standardization

MPEG-DASH technology was developed under MPEG. Work on DASH started in 2010; it became a Draft International Standard in January 2011, and an International Standard in November 2011. The MPEG-DASH standard was published in April, 2012 but has been revised in 2019 and then once more in 2022 as [1].

DASH is a technology related to Adobe Systems HTTP Dynamic Streaming, Apple Inc. HTTP Live Streaming (HLS) and Microsoft Smooth Streaming. DASH is based on Adaptive HTTP streaming (AHS) in 3GPP Release 9 and on HTTP Adaptive Streaming (HAS) in Open IPTV Forum Release 2. As part of their collaboration with MPEG, 3GPP Release 10 has adopted DASH (with specific codecs and operating modes) for use over wireless networks.

The DASH Industry Forum (DASH-IF) further promotes and catalyzes the adoption of MPEG-DASH and helps transition it from a specification into a real business. It consists of major streaming and media companies, including Microsoft, Netflix, Google, Ericsson, Samsung, Adobe, etc. and creates guidelines on the usage of DASH for different use cases in practice.

MPEG-DASH is integrated in other standards, e.g. MPEG-DASH is supported in HbbTV (as of Version 1.5).

## Overview

DASH is an adaptive bitrate streaming technology where a multimedia file is partitioned into one or more segments and delivered to a client using HTTP. A media presentation description (MPD) describes segment information (timing, URL, media characteristics like video resolution and bit rates), and can be organized in different ways such as SegmentList, SegmentTemplate, SegmentBase and SegmentTimeline, depending on the use case. Segments can contain any media data, however the specification provides specific guidance and formats for use with two types of containers: ISO base media file format (e.g. MP4 file format) or MPEG-2 Transport Stream.

An early predecessor of DASH was an HTTP web server based streaming system called SProxy, developed and deployed in the Hewlett Packard Laboratories in 2006. It showed how to use HTTP range requests to break the content into small segments. SProxy showed the effectiveness of segment based streaming, gaining Internet penetration in the presence of the wide deployment of firewalls (which are prone to blocking novel protocols), and reducing the unnecessary traffic transmission if a user chooses to terminate the streaming session earlier before reaching the end.

DASH is audio/video codec agnostic. One or more representations (i.e., versions at different resolutions or bit rates) of multimedia files are typically available, and selection can be made based on network conditions, device capabilities and user preferences, enabling adaptive bitrate streaming and QoE (Quality of Experience) fairness. DASH standard does not specify the adaptive bitrate streaming (ABR) logic. The current MPEG-DASH reference client dash.js offers both buffer-based (BOLA) and hybrid (DYNAMIC) bit rate adaptation algorithms. DASH is also agnostic to the underlying application layer protocol. Thus, DASH can be used with other application protocols besides HTTP, e.g., DASH over CCN.

On July 27, 2015, MPEG LA announced a call for MPEG-DASH-related patents in order to create a single patent pool for this technology. MPEG LA announced its MPEG-DASH patent portfolio licence. MPEG-LA claims that the included patents are essential to the MPEG Dynamic Adaptive Streaming over HTTP standard.

## Implementations

MPEG-DASH is available natively on Android through the ExoPlayer, on Samsung Smart TVs 2012+, LG Smart TV 2012+, Sony TV 2012+, Philips NetTV 4.1+, Panasonic Viera 2013+ and Chromecast. YouTube as well as Netflix already support MPEG-DASH, and different MPEG-DASH players are available.

While MPEG-DASH isn't directly supported in HTML5, there are JavaScript implementations of MPEG-DASH which allow using MPEG-DASH in web browsers using the HTML5 Media Source Extensions (MSE). There are also JavaScript implementations such as the bitdash player which support DRM for MPEG-DASH using the HTML5 Encrypted Media Extensions. In combination with WebGL, the HTML5-based adaptive bitrate streaming of MPEG-DASH enables also the efficient streaming of 360° video for live and on-demand use cases.

### Clients and libraries

- Shaka Player, is the open source DASH HTML5 video player from Google for Low Bandwidth Connections.
- VLC media player 3.0 shipped a new client plugin for MP4/MPEG and Live streams.
- The cross-platform FOSS multimedia framework GStreamer has supported MPEG-DASH and WebM DASH since at least v1.4.
- The open-source library libdash is platform independent and runs on mobile platforms such as Android, iOS, Windows Phone.
- bitmovin provides the bitdash MPEG-DASH player for HTML5 and Flash.
- VideoJS is an open-source HTML5 video player, supports HLS, DASH, WebM, and progressive MP4 for Live and VOD streaming.
- Clappr is an open-source HTML5 video player, uses HTMLVideoElement, supports DASH, HLS, progressive, ad insertion, dynamic overlays, picture-in-picture

### Servers

Note that no specific support is required from the server for DASH content, with the exception of Live Streaming.

- Wowza Streaming Engine has support MPEG-DASH playback with DVR and provides DASH Stream Target publishing to Akamai.
- Brightcove Zencoder has support for MPEG-DASH transmuxing/transcoding.
- Elemental Technologies video processing solutions support DASH.
- Helix Universal Server has support for DASH in various modes.
- Nimble Streamer has live and VOD MPEG-DASH support. For VOD it supports both H.265 and H.264 codecs
- Unified Origin supports MPEG-DASH.

### Services

- Akamai CDN supports DASH.
- Amazon CloudFront CDN supports DASH.
- Amazon Web Services Elastic Transcoder has support for MPEG-DASH.
- Azure Media Services platform has support for MPEG-DASH.
- Bitmovin provides the cloud-based transcoding service bitcodin.com which supports MPEG-DASH.
- CloudFlare Stream supports transcoding into DASH in VP9 before serving to the end user.
- Cloudinary provides automatic transcoding with support for MPEG-DASH.
- Lumen CDN supports DASH.
- Limelight Networks CDN supports DASH.
- Project Shield CDN supports DASH.
- Tata Communications CDN supports DASH.
- DogalZeka MS2 Alarm Monitoring, Transcoding and Recording DASH input/output support.
- Resi Live Stream Platform supports ingest, transcoding and CDN delivery of MPEG-DASH.

### Content generators

- ITEC's DASHEncoder.
- MP4Box and its multimedia framework from GPAC at Télécom Paris
- dashcast from Télécom Paris supports MPEG-DASH live streaming
- MediaGoom MPEG-DASH Packager
- Bento4 opensource tools and SDK

### Other

- ITEC offers a validation service for MPEG-DASH Media Presentation Description (MPD) files
- Multiple DASH datasets are offered by the Institute of Information Technology (ITEC) at Alpen-Adria University Klagenfurt, the GPAC group at Telecom ParisTech and Digital TV Labs.
- The BBC has DASH test streams, including DASH over HTTP/2.
- Widevine DRM supports DASH and Encrypted Media Extensions.
- Mividi provides software tool for analyzing and monitoring live MPEG-DASH streams.

## Supported players and servers

### Clients

Windows 10 used to have native support for DASH streaming in EdgeHTML, a proprietary browser engine that was used in Microsoft Edge (now referred to as Edge Legacy) before the transition to the Chromium-based Blink browser engine. Edge Legacy was included in Windows 10 up till version 2004. It was replaced by Edge Chromium in version 20H2.

DASH support on other browsers & operating systems is available via Media Source Extensions.

| Product | Product type | Platform | Live streaming | DRM-free | As of version | Editor |
|---|---|---|---|---|---|---|
| Microsoft Edge | Web browser | Windows 10 | Native support on Edge Legacy.Support via Media Source Extensions on Edge Chromium. | No | Supported natively on Edge Legacy's engine EdgeHTML from version 12 to 18. No native support on Edge Chromium from version 79 to present. | Microsoft |
| VLC media player | Media player | Windows, macOS, Linux, Android, iOS, Windows Phone | Yes | Yes | v3.0 | VideoLAN |
| Media Player Classic - Home Cinema (MPC-HC) Media Player Classic - Black Edition (MPC-BE) | Media player | Windows | Yes | Yes | v2.0.0 (MPC-HC) v1.5.0 (MPC-BE) Support for playback of DASH streams may be unstable. | MPC-HC Community Forum, Alexander Vodiannikov |
| MX Player | Media player | Android | Yes | No | v1.9.18 Support for playback of DASH streams is currently unstable. | J2 Interactive |
| NexPlayer | SDK | HTML5 (MSE Browsers), Android (mobile, TV, STB), iOS, Chromecast, Windows, Mac, Linux, Tizen, WebOS | Yes | No | — | NexStreaming |
| Dash.js | SDK | HTML5 (MSE Browsers) | Yes | No | — | Dash Industry Forum |
| Shaka Player | SDK | HTML5 (MSE Browsers) | Yes | No | — | Google |
| Rx-Player | SDK | HTML5 (MSE Browsers) | Yes | No | — | Canal+ |
| bitdash | SDK | HTML5 (MSE Browsers), Android, LG TVs, Samsung TVs, Xbox One, Universal Windows Platform | Yes | No | — | Bitmovin |
| PRESTOplay | SDK | HTML5 (MSE Browsers), Android, iOS, Windows, Mac | Yes | No | — | castLabs |
| THEOplayer | SDK | HTML5 (MSE Browsers), Android (mobile, TV, STB), iOS, Chromecast, Windows, Mac, Linux, Tizen, WebOS | Yes | No | — | THEO Technologies NV |
| Viblast Player | SDK | HTML5 (MSE Browsers), Android, iOS | Yes | No | — | Viblast Team |
| Radiant Media Player | SDK | HTML5 (MSE Browsers), Android, iOS, Windows, Mac, Linux | Yes | No | — | Radiant Media Player |
| Videogular | SDK | HTML5 (MSE Browsers) | Yes | No | — |   |
| Fluid Player | SDK | HTML5 (MSE Browsers) | Yes | No | — | ExoClick |
| GStreamer | Multimedia framework | — | Yes | No | 1.4 | GStreamer Team |
| Libdash | Multimedia framework | — | Yes | No | — | bitmovin, ITEC Team |
| GPAC | Multimedia framework | — | Yes | No | — | Telecom ParisTech inc. |

## Patent holders

| Organization | Patents |
|---|---|
| Maxell | 15 |
| The Netherlands Organisation for Applied Scientific Research (TNO) | 8 |
| Nippon Telegraph and Telephone (NTT) | 5 |
| Fraunhofer | 4 |
| Columbia University | 4 |
| Amotech Co., Ltd. | 2 |
| AVerMedia Technologies, Inc. | 2 |
| Cable Television Laboratories, Inc. | 2 |
| Helios Streaming, LLC | 2 |
| JVC Kenwood | 1 |
| Lough Corrib Intellectual Property Limited | 1 |
