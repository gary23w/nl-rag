---
title: "HTTP Live Streaming"
source: https://en.wikipedia.org/wiki/HTTP_Live_Streaming
domain: streaming-hls-dash
license: CC-BY-SA-4.0
tags: adaptive bitrate streaming, http live streaming, mpeg-dash, rtmp streaming
fetched: 2026-07-02
---

# HTTP Live Streaming

**HTTP Live Streaming** (also known as **HLS**) is an HTTP-based adaptive bitrate streaming communications protocol developed by Apple Inc. and released in 2009. Support for the protocol is widespread in media players, web browsers, mobile devices, and streaming media servers. As of 2022, an annual video industry survey has consistently found it to be the most popular streaming format.

HLS resembles MPEG-DASH in that it works by breaking the overall stream into a sequence of small HTTP-based file downloads, each downloading one short chunk of an overall potentially unbounded transport stream. A list of available streams, encoded at different bit rates, is sent to the client using an extended M3U playlist.

Based on standard HTTP transactions, HTTP Live Streaming can traverse any firewall or proxy server that lets through standard HTTP traffic, unlike UDP-based protocols such as RTP. This also allows content to be offered from conventional HTTP servers and delivered over widely available HTTP-based content delivery networks. The standard also includes a standard encryption mechanism and secure-key distribution using HTTPS, which together provide a simple DRM system. Later versions of the protocol also provide for trick-mode fast-forward and rewind and for integration of subtitles.

Apple has documented HTTP Live Streaming as an Internet Draft (Individual Submission), the first stage in the process of publishing it as a Request for Comments (RFC). As of December 2015, the authors of that document have requested the RFC Independent Stream Editor (ISE) to publish the document as an informational (non-standard) RFC outside of the IETF consensus process. In August 2017, RFC 8216 was published to describe version 7 of the protocol.

## Architecture

HTTP Live Streaming uses a conventional web server, that implements support for HTTP Live Streaming (HLS), to distribute audiovisual content and requires specific software, such as OBS to fit the content into a proper format (codec) for transmission in real time over a network. The service architecture comprises:

**Server**

Codify and encapsulate the input video flow in a proper format for the delivery. Then it is prepared for distribution by segmenting it into different files. In the process of intake, the video is encoded and segmented to generate video fragments and index file.

- Encoder: codify video files in H.264 format and audio in AAC, MP3, AC-3 or EAC-3. This is encapsulated by MPEG-2 Transport Stream (MPEG-TS) or MPEG-4 Part 14 (MP4) to carry it.
- Segmenter: divides the stream into fragments of equal length. It also creates an index file that contains references of the fragmented files, saved as .m3u8.

**Distributor**

Formed by a standard web server, accepts requests from clients and delivers all the resources (.m3u8 playlist file and .ts segment files) needed for

streaming

.

**Client**

Request and download all the files and resources, assembling them so that they can be presented to the user as a continuous flow video. The client software downloads first the index file through a

URL

and then the several media files available. The playback software assembles the sequence to allow continued display to the user.

## Features

HTTP Live Streaming provides mechanisms for players to adapt to unreliable network conditions without causing user-visible playback stalling. For example, on an unreliable wireless network, HLS allows the player to use a lower quality video, thus reducing bandwidth usage. HLS videos can be made highly available by providing multiple servers for the same video, allowing the player to swap seamlessly if one of the servers fails.

### Adaptability

To enable a player to adapt to the bandwidth of the network, the original video is encoded in several distinct quality levels. The server serves an index, called a *master playlist*, of these encodings, called *variant streams*. The player can then choose between the variant streams during playback, changing back and forth seamlessly as network conditions change.

### Using fragmented MP4

At WWDC 2016 Apple announced the inclusion of byte-range addressing for fragmented MP4 files, or fMP4, allowing content to be played via HLS without the need to multiplex it into MPEG-2 Transport Stream. The industry considered this as a step towards compatibility between HLS and MPEG-DASH.

### Low Latency HLS

Two unrelated HLS extensions with a *Low Latency* name and corresponding acronym exist:

- Apple Low Latency HLS (ALHLS) which was announced by Apple at WWDC2019
- Community LHLS (LHLS) which predated Apple's publication and is allegedly simpler

The remainder of this section describes Apple's ALHLS. It reduces the glass-to-glass delay when streaming via HLS by reducing the time to start live stream playbacks and maintain that time during a live-streaming event. It works by adding partial media segment files into the mix, much like MPEG-CMAF's fMP4. Unlike CMAF, ALHLS also supports partial MPEG-2 TS transport files. A partial media segment is a standard segment (e.g. 6 seconds) split into equal segments of less than a second (e.g. 200 milliseconds). The standard first segment is replaced by the series of partial segments. Subsequent segments are of the standard size. HTTP/2 is required to push the segments along with the playlist, reducing the overhead of establishing repeated HTTP/TCP connections.

Other features include:

- Playlist Delta Updates: only sending what changed between playlists, which typically fit in a single MTU making it more efficient to load the playlists which, with large DVR windows, can be quite large.
- Blocking of playlist reload: when requesting live media playlists, wait until the first segment is also ready, and return both at the same time (saving additional HTTP/TCP requests)
- Rendition Reports: add metadata to other media renditions to make switching between ABR faster
- New tags added: EXT-X-SERVER-CONTROL / EXT-X-PART / EXT-X-SKIP / EXT-X-RENDITION-REPORT
- URL QUERY_STRING ?_HLS callbacks added

Apple also added new tools: *tsrecompressor* produces and encodes a continuous low latency stream of audio and video. The *mediastreamsegmenter* tool is now available in a low-latency version. It is an HLS segmenter that takes in a UDP/MPEG-TS stream from tsrecompressor and generates a media playlist, including the new tags above.

Support for low-latency HLS is available in tvOS 13 beta, and iOS & iPadOS 14. On April 30, 2020, Apple added the low latency specifications to the second edition of the main HLS specification.

### Dynamic ad insertion

Dynamic ad insertion is supported in HLS using splice information based on SCTE-35 specification. The SCTE-35 splice message is inserted into the media playlist file using the EXT-X-DATERANGE tag. Each SCTE-35 splice_info_section() is represented by an EXT-X-DATERANGE tag with a SCTE35-CMD attribute. A SCTE-35 splice out/in pair signaled by the splice_insert() commands is represented by one or more EXT-X-DATERANGE tags carrying the same ID attribute. The SCTE-35 splice out command should have the SCTE35-OUT attribute and the splice in command should have the SCTE35-IN attribute.

Between the two EXT-X-DATERANGE tags that contain the SCTE35-OUT and SCTE35-IN attributes respectively, there may be a sequence of media segment URIs. These media segments normally represent ad programs that can be replaced by the local or customized ad. The ad replacement does not require the replacement of the media files, only the URIs in the playlist need to be changed to point to different ad programs. The ad replacement can be done on the origin server or on the client's media-playing device.

## Server implementations

Notable server implementations supporting HTTP Live Streaming include:

- Adobe Media Server supports HLS for iOS devices (HLS) and Protected HTTP Live Streaming (PHLS).
- Akamai supports HLS for live and on-demand streams.
- AT&T supports HLS in all formats live or on-demand.
- Ant Media Server support HLS and Low Latency HLS for live and on-demand streams.
- Axis Communication IP cameras supports HLS via CamStreamer App ACAP
- Instart supports HLS for on-demand streams.
- Amazon CloudFront supports HLS for on-demand streams.
- Bitmovin supports HLS for on-demand and live streaming.
- CDNetworks supports HLS for live and on-demand streams.
- Cisco Systems: supports full end-to-end delivery for Live/TSTV/VOD/HLS and Cloud DVR services.
- Cloudflare supports HLS for live and on-demand streams.
- EdgeCast Networks supports cross-device streaming using HLS.
- Fastly supports HLS for live and on-demand streams.
- Helix Universal Server from RealNetworks supports iPhone OS 3.0 and later for live and on-demand HTTP Live or On-Demand streaming of H.264 and AAC content to iPhone, iPad and iPod.
- IIS Media Services from Microsoft supports live and on-demand Smooth Streaming and HTTP Live Streaming.
- Level 3 supports HLS live and on-demand streams.
- Limelight Networks supports HLS for some accounts.
- Nginx with the nginx-rtmp-module supports HLS in live mode. Commercial version Nginx Plus, which includes *ngx_http_hls_module* module, also supports HLS/HDS VOD.
- Nimble Streamer supports HLS in live and VOD mode, Apple Low Latency HLS spec is also supported.
- Node.js with the hls-server package supports hls encoding to live mode and local files conversion.
- OvenMediaEngine is an open source project that supports Low Latency HLS (LL-HLS) and HLS for live streaming.
- PeerTube supports HLS
- Storm Streaming Server supports HLS as backup mode for its Media Source Extensions player
- Tata Communications CDN supports HLS for live and on-demand streams.
- TVersity supports HLS in conjunction with on-the-fly transcoding for playback of any video content on iOS devices.
- Ustream supports HLS delivery of live broadcasts. The ingested stream is re-transcoded if the original audio and video codec falls outside HLS requirements.
- VLC Media Player supports HLS for serving live and on-demand streams as of version 2.0.
- Wowza Streaming Engine from *Wowza Media Systems* supports HLS and encrypted HLS for live (with DVR), on-demand streaming and Apple Low Latency HLS spec.

## Usage

- Google added HTTP Live Streaming support in Android 3.0 (Honeycomb).
- HP added HTTP Live Streaming support in webOS 3.0.5.
- Microsoft added support for HTTP Live Streaming in EdgeHTML rendering engine in Windows 10 in 2015.
- Microsoft added support for HTTP Live Streaming in IIS Media Services 4.0.
- Yospace added HTTP Live Streaming support in Yospace HLS Player and SDK for flash version 1.0.
- Sling Media added HTTP Live Streaming support to its Slingboxes and its SlingPlayer apps.
- In 2014/15, the BBC introduced HLS-AAC streams for its live internet radio and on-demand audio services, and supports those streams with its iPlayer Radio clients.
- Twitch uses HTTP Live Streaming (HLS) to transmit and scale the live streaming to many concurrent viewers, also supporting multiple variants (e.g., 1080p, 720p, etc.).

## Supported players and servers

HTTP Live Streaming is natively supported in the following operating systems:

- Windows 10 version 1507 to 2004 (Microsoft Edge Legacy) (no longer supported)
- Windows 11 Media Player
- macOS 10.6+ (Safari and QuickTime)
- iOS 3.0+ (Safari)
- Android 4.1+ (Google Chrome)

Windows 10 used to have native support for HTTP Live Streaming in EdgeHTML, a proprietary browser engine that was used in Microsoft Edge (now referred to as Edge Legacy) before the transition to the Chromium-based Blink browser engine. Edge Legacy was included in Windows 10 up till version 2004. It was replaced by Edge Chromium in version 20H2. Along with Windows 11, Microsoft released an updated Media Player that supports HLS natively.

### Clients

| Client | Platform | Live Streaming | DRM | As of Version | Editor |
|---|---|---|---|---|---|
| Safari (web browser) | macOS, iOS | Yes | Yes | 6.0+ Has full HLS support. | Apple |
| Microsoft Edge (web browser) | Windows 10 | Native support on Edge Legacy.Support via Media Source Extensions on Edge Chromium. | Yes | Supported natively on Edge Legacy's engine EdgeHTML from version 12 to 18. No native support on Edge Chromium from version 79 to present. | Microsoft |
| Google Chrome (web browser) / Chromium | Windows, macOS, Linux, Android, iOS | OS-dependent support on Android/iOS.Support via Media Source Extensions on other OS. | Yes | 30+ Android and iOS have OS-dependent native support. Other platforms require Media Source Extensions. | Google |
| Firefox (web browser) | Windows, macOS, Linux, Android, iOS | OS-dependent support on Android/iOS.Support via Media Source Extensions on other OS. | Yes | 50.0+ for Android and 57.0 for others, 59.0 has enhanced support for Android Other platforms require Media Source Extensions. | Mozilla |
| QuickTime Player (media player) | macOS | Yes | Yes | 10.0+ Has full HLS support. | Apple |
| iTunes (music player) | Windows, macOS | Yes | Yes | 10.1+ Has full HLS support. To play a HLS stream, go to File > Open Stream and replace "http://" with "itls://" (for video streams) or "itals://" (for audio streams) in the stream URL. | Apple |
| Windows Media Player (2022) (media player) | Windows 10, Windows 11 | Yes | Yes | Does not include the original Win32 version of Windows Media Player. | Microsoft |
| StreamS HiFi Radio (radio player) | iOS, tvOS iPhone, iPad, and AppleTV | Yes | Yes | 7.3+ Plays Internet Radio Streams HLS Audio - 100% Compliant AAC-LC/HE-AAC/xHE-AAC 2.0 Stereo/5.1-7.1 Surround ES - Elementary Stream ADTS fMP4 - Fragmented ISO MP4 Displays Synchronous Realtime Metadata and Graphics | StreamS/Modulation Index LLC |
| VLC media player (media player) | Windows, macOS, Linux, Android, iOS, Windows Phone | Yes | Unknown | VLC 2.x has partial support up to HLS version 3 (otherwise will load as M3U playlist, individual chunks sequence).VLC 3.0 has full HLS support. | VideoLAN |
| Media Player Classic Home Cinema (media player) | Windows | Yes | Yes |   | Gabest, Doom9 forum users |
| PotPlayer (media player) | Windows | Yes | Yes |   | Daum Communications |
| MPlayer / SMPlayer / mpv (media player) | Windows, macOS, Linux, BSD | Yes | Yes |   | Ricardo Villalba |
| GOM Player (media player) | Windows | Yes | Yes |   | Gretech |
| Cameleon (live video streaming software) | Windows, macOS | Yes | Unknown |   | Yatko |
| Audacious (software) (music player) | Windows, Linux | Yes | Yes |   | Audacious |
| Radio Tray (radio player) | Linux | Yes | Yes |   | Carlos Ribeiro |
| Kodi (software) (home entertainment application) | Windows, macOS, Linux, Android, iOS | Yes | Partial | 12.0 Alpha 5 and later DRM support requires a monthly/nightly build | XBMC Foundation |
| MythTV (home entertainment application) | Windows, macOS, Linux, FreeBSD | Yes | Yes | 0.26 | MythTV |
| JRiver Media Center (home entertainment application) | Windows, macOS | Yes | Yes |   | JRiver |
| XiiaLive (radio player) | Android, iOS | Yes | Yes | 3.0+ Plays internet radio streams (audio only). | Visual Blasters LLC |
| Tunein radio (radio player) | Android, iOS | Yes | Yes | 3.3+ Plays internet radio streams (audio only). | TuneIn |
| myTuner Radio (radio player) | Android, iOS, Windows Phone, Windows 8, macOS | Yes | Yes | Plays internet radio streams (audio only). | AppGeneration Software |
| Internet Radio Player (radio player) | Android | Yes | Yes | Plays internet radio streams (audio only). | MuserTech |
| GuguRadio (radio player) | iOS | Yes | Yes | Plays internet radio streams (audio only). | Leon Fan |
| AIMP (media player) | Windows, Android | Yes | Unknown | 4.10+ (build 1827) Plays internet radio streams (audio only). | Artem Izmaylov |
| Mini Stream Player (media player) | Android | Yes | Yes |   | JogiApp |
| MX Player (media player) | Android | Yes | Yes |   | J2 Interactive |
| TV Streams (media player) | macOS, iOS, tvOS | Yes | Yes | v7.1 | Tiago Martinho |
| HP Touchpad | WebOS | Yes | Yes | 3.0.5 | HP |
| Amino x4x STB | Amino set-top boxes | Yes | Yes | 2.5.2 Aminet | Aminocom.com |
| Dune HD TV | Dune HD set-top boxes | Yes | Yes | TV series | dunehd.com |
| CTU Systems Ltd | CTU Systems Ltd Eludo Play Out System | Yes | Yes | TV series | ctusystems.com |
| nangu.TV | Motorola set-top boxes | Yes | Yes | 2.0 | nangu.TV |
| Roku Digital Video Player | Roku set-top boxes | Yes | Yes | Roku OS / SDK 2.6 | Roku |
| Telebreeze Player | HTML, Android, iOS, Windows, MacOS, Roku, MAG Infomir, Samsung Tizen, LG WebOS, Google Chromecast, tvOS, Amazon Fire TV, AndroidTV | Yes | Yes |   | Telebreeze |
| bitdash (SDK) | HTML5 or Flash, Web and Mobile | Yes | Yes | Version 3.0+ | bitmovin |
| 3ivx (SDK) | Windows 8, Windows Phone 8 & Xbox One | Yes | Yes | 2.0 | 3ivx |
| THEOplayer | HTML5, SDK (Android, iOS, Android TV, tvOS, Chromecast, WebOS, FireTV, Tizen) | Yes | Yes |   | THEO Technologies |
| OvenPlayer | HTML5 | Yes | Yes | 0.10.0+ | AirenSoft |
| Viblast Player (SDK) | HTML5, iOS, Android | Yes | Partial |   | Viblast Ltd |
| Flowplayer (SDK) | Adobe Flash, iOS, Android, HTML5 (hlsjs plugin) | Yes | Yes | The Flash HLS plugin is available from GitHub. | Flowplayer Ltd |
| JW Player (SDK) | Adobe Flash, iOS, Android, HTML5 | Yes | Yes | HLS is provided in all JW Player versions as of JW8 (latest) | JW Player |
| Radiant Media Player (SDK) | Adobe Flash, HTML5 | Yes | Yes | 1.5.0 | Radiant Media Player |
| Yospace (SDK) | Adobe Flash | Yes | Yes | 2.1 | Yospace |
| Onlinelib (SDK) | Adobe Flash | Yes | Yes | 2.0 | Onlinelib.de |
| VODOBOX HLS Player (online service) | Adobe Flash, HTML5, iOS, Android | Yes | Yes |   | Vodobox |
| NexPlayer (SDK) | HTML5 (MSE Browsers), Android (mobile, TV, STB), iOS, Chromecast, Windows, Mac, Linux, Tizen, WebOS | Yes | Yes |   | NexStreaming |
| ffplay/avplay (multimedia framework) |   | Yes | Partial |   | FFmpeg/Libav |
| GPAC (multimedia framework) |   | Yes | No | 0.5.0 | Telecom ParisTech inc. |
| QuickPlayer (SDK) | Android, iOS, Windows 7, 8, 8,1 and 10 | Yes | Yes |   | Squadeo |
| hls.js (MSE) | MSE Browsers | Yes | Unknown |   | Dailymotion open source |
| hasplayer.js (MSE) | MSE Browsers | Yes | Unknown |   | open source |
| Hola Player (video player) | HTML5, Adobe Flash, iOS, Android | Yes | Yes | All versions | Hola Ltd open source |
| Shaka Player (SDK) | HTML5 (MSE Browsers) | Coming soon | Partial | 2.1 | Open Source |
| Fluid Player (Video Player) | HTML5 (MSE Browsers) | Yes | Yes | 2.2.0+ | Fluid Player OSS |
| Video.js | MSE Browsers. Flash with flashls source handler fallback. | Yes | Yes |   | Open source |
| foobar2000 (audio player) | Windows | Yes | Unknown | 1.6.1 | Peter Pawłowski |
| QMPlay2 (media player) | Windows, macOS, Linux | Yes | Unknown | It has VU meters and a spectrum analyzer | Open source |

### Servers

| Product | Technology | As Of Version | Editor | Free | Notes |
|---|---|---|---|---|---|
| ANEVIA Genova Live | Bundled software for transcoding to H.264 & HEVC, and packaging to HLS, MPEG-DASH, MS Smooth Streaming |   | Anevia | No |   |
| AvProxy | Light software for live streaming Input and output streams : HTTP(S), HLS(S)/AES-128, UDP, RTP, MPTS demux | 2.19 |   | Yes | Proprietary but free for use |
| bitcodin |   | SaaS | bitmovin | No |   |
| VLC |   | 1.2 |   | Yes |   |
| Video Cloud |   | SaaS | Brightcove | No |   |
| IIS Media Services |   | 4.0 | Microsoft | No |   |
| Antik Media Streamer | Ingest Module (UDP/HTTP Transport Stream, Backup Stream with auto-switching, stream status monitoring and logging), Stream replication UDP/HTTP, HLS streaming, Video archive with snapshots, Server-side Timeshift, time zone shifting with multiple time zones, Stream Encryption using AES and key-rotation (with Antik Key Server) | 3.0 | Antik technology | No |   |
| Adobe Media Server | Live and VOD streaming as origin and edge server | 5.0 | Adobe | No |   |
| Ant Media Server | Supports HLS and Low Latency HLS in standalone and cluster modes. It can ingest WebRTC, RTMP, RTSP and can create HLS and Low Latency HLS playback endpoints | 2.11 | Ant Media | No | HLS is a out of the box feature in Community and Enterprise Editions. Low Latency HLS is a plugin that is compatible in Community and Enterprise Editions. |
| Evostream Media Server | Cross-platform including embedded systems such as encoders, IP cameras, DVRs, and more. Supports: Adobe Flash RTMP, RTMPS, LiveFLV, full transcoder for creating lower bitrate streams, HTTP Live Streaming (HLS) for streaming to iPhones, iPads and Androids, HTTP Dynamic Streaming (HDS) for Adobe Air, Microsoft Smooth Streaming (MSS) for Microsoft devices, RTSP with RTP or MPEG-TS, MPEG-TS (unicast/multicast), compatible Live Encoding, strong security for your content ( Verimatrix DRM, HLS AES encryption, Stream Aliasing, Watermarking), built-in clustering mechanism and more. | 1.6.5 | EvoStream | No |   |
| MythTV |   | 0.25 | MythTV | Yes |   |
| MACNETIX VOD-Server |   | 3.0 | MACNETIX | No |   |
| Anevia NEA Live Servers | Transcapsulation: from one input, several outputs (HLS, MS Smooth Streaming, ADS Flash, MPEG-DASH) |   | Anevia | No |   |
| Packet Ship OverView:Origin Server | Capture from IPTV multicast and chunking to HLS for multi-bandwidth live streams, with AES encryption | 2.1 | Packet Ship | No |   |
| nangu.TV Streamers | on-the-fly adaptation: content is stored once enabling several outputs (HLS, MS Smooth Streaming, ADS Flash, MPEG-DASH) |   | nangu.TV | No |   |
| TVersity Media Server |   | 1.9 | TVersity | No | Pro Edition only |
| Helix Universal Server | Live + VOD HLS with Verimatrix DRM integration, ABR, Multi-Resolution, AES encryption | 15.0+ | RealNetworks | No | High performance HLS (12,000+ concurrent devices) |
| Wowza Streaming Engine | Live and VOD streaming as origin and edge server with DVR, DRM Integration and Transcoding for adaptive delivery. Outputs to MPEG-DASH, HLS, HDS, Smooth Streaming, RTMP, and RTSP. Supports Apple Low Latency HLS. | 2.0+ | Wowza Media Systems | No |   |
| Unified Streaming Platform | Muxes media content from one unified source to multiple outputs (Smooth Streaming, HDS, HLS and MPEG-DASH) |   | Unified Streaming | No |   |
| VODOBOX Live Server | Outputs HTTP Live Streaming with Adaptive bitrate streaming (up to 6 simultaneous qualities). Video codecs : AVC H.264 / HEVC H.265 Audio codecs : MP3 / AAC Transport layers : HTTP / FTP / Amazon AWS S3 / Microsoft Azure Web Storage / writing to disk (NetBios / Samba) Hostings : internal HTTP Web server and/or external Web servers (ex: Apache HTTP server, Microsoft IIS, Nginx, etc.) | 1.0 | Vodobox | Yes | Supports input live streams from DVB-T devices, satellite receivers (Dreambox), IP streams (RTSP, RTMP, MMS, HTTP), Microsoft DirectShow drivers (video capture cards, live production software, camera). Encoder is compliant with Intel Quick Sync Video and Nvidia NVENC hardware acceleration. |
| Flixwagon Platform Video Server |   |   | Flixwagon | No |   |
| StreamCoder Live Encoder | Realtime video encoder (inputs : DVB/IP stream or video signal). Supports multi-bitrates and multi-languages |   | Ektacom | No |   |
| Apache HTTP Server |   |   | Apache Software Foundation | Yes |   |
| Unreal Media Server |   | 9.5 | Unreal Streaming Technologies | No | Latency of live streams can be as low as 2.5 seconds over the Internet |
| Nimble Streamer | RTMP / RTSP / Icecast / MPEG-TS to ABR HLS. MP4 / MP3 to VOD HLS. Apple Low Latency HLS spec is supported. | 1.0.0-x | WMSPanel | No |   |
| Nginx-rtmp-module | Free module for nginx server with support of HLS live streaming. Compliant with iOS and Android. | 0.9.x | Roman Arutyunyan | Yes |   |
| Nginx Plus | VOD HLS as origin |   | NGINX, Inc. | No |   |
| OvenMediaEngine | Supports Low Latency HLS (HLSv7+), HLS (HLSv3+), ABR LL-HLS, and ABR HLS for live streaming | 0.16.0+ | AirenSoft | Yes | GNU Affero General Public License |
| Flussonic Media Server | Multi-platform support for HTTP, RTSP, RTMP, DASH, Time Shifting, DVR Functions with Unlimited Rewind Capabilities HLS streaming specific to iOS platform support. | 3.0+ | Flussonic, LLC. | No | Supporting a magnitude of features with full HTTP support. |
| VBrick Distributed Media Engine ("DME") |   | 2.0 | VBrick Systems, Inc. | No | Live and stored HLS. Live can be transmuxed from several input mux including RTP, RTMP, and MPEG-TS using H.264 encoding |
| Telebreeze Coder / Media Server | Input streams and interfaces: UDP, TCP, RTP, HLS, HTTP, RTMP (MPEG-TS) Output Streams: HLS, HTTP, UDP Preprocessing: Resize, Deinterlace, Frame Rate Conversion, Audio Resampling, Logo Rendering |   | Telebreeze | No |   |
| LEADTOOLS Media Streaming Server SDK | Converts files on the fly to Adobe HDS, Apple HLS, MPEG-DASH, Microsoft Smooth Streaming, RTSP. | 19.0 | LEAD Technologies | No |   |
| MC-ROUTE | Multifunctional software for live stream routing and protocol conversion | 4.4 | Teracue | No | Supported protocols: TS over UDP, RTP, TCP, HLS, HTTP, RTSP/RTP |
| Direkt router | Live hardware decoder with SDI, NDI out and transcoding | 4.1 | Intinor | No | Supported protocols in: TS over UDP, RTP, TCP, HLS, HTTP, RTMP out: UDP, RTP, TCP, RTMP |
| Elecard CodecWorks | Professional platform for real-time encoding and transcoding into HEVC/H.265, AVC/H.264 and MPEG-2 video supporting adaptive bitrate streaming via HLS and MPEG-DASH protocols. | 4.6 | Elecard | No | Supported protocols: TS over UDP/RTP/SRT, RTMP Output, HLS, MPEG-DASH output, UDP/RTP/SRT, NDI |
| TAC - Teracue Application Cloud | Professional stream routing and real-time encoding/transcoding platform supporting various audio and video codec and streaming protocols | 1.0 | Teracue | No | Supported protocols IN and OUT: UDP, RTP, RTSP, RTMP, TCP (Client/Server), HLS, HTTP, FEC, SRT Supported protocols IN only: SDVoE and NDI |
| Peertube | A free and open-source, decentralized, ActivityPub federated video platform using HLS peer-to-peer technology to reduce load on individual servers when viewing videos. | 1.3.0 |   | Yes | Videos are made available via HTTP to download, but playback favors a peer-to-peer playback using HLS. |

### Live Encoders

| Product | Technology | As Of Version | Editor | Free | Supported Protocols |
|---|---|---|---|---|---|
| ENC-400 Series | Live hardware encoder with SDI or HDMI | 1.0 | Teracue | No | TS over UDP, RTP, TCP, RTP/RTSP, RTMP push, HLS |
| WELLAV NB100 | Live Streamcast with SDI or HDMI, CVBS | 1.0 | Wellav Technologies | No | TS UDP, RTP, RTP/RTSP, RTMP, HLS |
| ZyPerMX4 | Live hardware encoder with 4 HDMI inputs | 2.14 | ZeeVee | No | TS over UDP, RTP, H.264/MPEG-4 AVC, HLS, RTMP, RTSP |
| ZyPerMX2 | Live hardware encoder with 2 HDMI inputs | 2.14 | ZeeVee | No | TS over UDP, RTP, H.264/MPEG-4 AVC, HLS, RTMP, RTSP |
| Elecard CodecWorks | Live software encoder with up to 8 SDI/HDMI or NDI inputs | 4.6 | Elecard | No | TS UDP, RTP, SRT, RTMP push, HLS, Mpeg-DASH |
| StreamS Live Encoder | Live software/hardware audio encoder with professional interface options | 3.0 | StreamS | No | HLS/DASH ES, fMP4, FTP, FTPS, HTTP, HTTPS, DAV, DAVS, Akamai, Amazon S3, Microsoft BLOB, Google Cloud AAC-LC/HE-AAC/xHE-AAC - Synchronous Realtime Now Playing and Control Metadata and Graphics |

### VOD encoders

| Product | Technology | As Of Version | Editor | Free | Notes |
|---|---|---|---|---|---|
| VODOBOX HLS Encoder | Converts video files into pre-encoded HLS Adaptive bitrate streaming, ready to be hosted and broadcast through Apache HTTP server / Microsoft IIS / Nginx Web servers. Supports AVC H.264 / HEVC H.265 / MPEG-TS / Fragmented MP4 / Alternate Audio / Alternate Subtitles. | 1.0 | Vodobox | Yes | Transcodes classic video files (avi, mp4, m2ts, mkv, ...) into HLS streams with multi-qualities for VOD or replay usage. Hardware encoding can be accelerated by Intel Quick Sync Video and Nvidia NVENC technologies. |
| MediaGoom HLS Packager | Convert mp4 files encoded with multibitrate to HLS chunks. | 0.1 | Mediagoom | Yes | Support both Linux and Windows. |
