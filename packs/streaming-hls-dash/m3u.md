---
title: "M3U - Wikipedia"
source: https://en.wikipedia.org/wiki/M3U
domain: streaming-hls-dash
license: CC-BY-SA-4.0
tags: adaptive bitrate streaming, http live streaming, mpeg-dash, rtmp streaming
fetched: 2026-07-02
---

# M3U

**M3U** (*MP3 URL*) is a computer file format for a multimedia playlist. One common use of the M3U file format is creating a single-entry playlist file pointing to a stream on the Internet. The created file provides easy access to that stream and is often used in downloads from a website, for emailing, and for listening to Internet radio.

Although originally designed for audio files, such as MP3, it is commonly used to point media players to audio and video sources, including online sources. M3U was originally developed by Fraunhofer for use with their WinPlay3 software, but numerous media players and software applications now support the format.

Careless handling of M3U playlists has been the cause of vulnerabilities in many music players such as VLC media player, iTunes, Winamp, and many others.

## File format

There is no formal specification for the M3U format; it is a *de facto* standard.

An M3U file is a plain text file that specifies the locations of one or more media files. The file is saved with the `m3u` filename extension if the text is encoded in the local system's default non-Unicode encoding (e.g., a Windows codepage), or with the `m3u8` extension if the text is UTF-8 encoded. The `mp3url` extension was originally supported by Winplay3, but fell out of use.

Each entry carries one specification. The specification can be any one of the following:

- an *absolute local pathname*; e.g., C:\My Music\Heavysets.mp3
- a *local pathname* relative to the M3U file location; e.g. Heavysets.mp3
- a URL

Each entry ends with a line break which separates it from the following one. Furthermore, some devices only accept line breaks represented as `CR LF`, but do not recognize a single `LF`.

### Extended M3U

The M3U file can also include comments, prefaced by the `#` character. In **extended M3U**, `#` also introduces extended M3U directives which are terminated by a colon `:` if they support parameters.

| Directive | Description | Example | Required | Standard |
|---|---|---|---|---|
| `#EXTM3U` | file header, must be the first line of the file | `#EXTM3U` | 1× | Yes |
| `#EXTINF:` | track information: runtime in seconds, then optional display title of the following resource. For runtime, a length of -1 or 0 may be used when media is a streaming file with no predefined length. | `#EXTINF:123,Artist Name – Track Title␤ artist - title.mp3` | No | Yes |
| additional properties as key-value pairs | `#EXTINF:123 logo="cover.jpg",Stream Title␤ http://example.org/live.strm` | No | IPTV |   |
| `#PLAYLIST:` | playlist display title | `#PLAYLIST:Music TV` | 1× | IPTV |
| `#EXTGRP:` | begin named grouping | `#EXTGRP:Foreign Channels` | No | IPTV |
| `#EXTALB:` | album information, title in particular | `#EXTALB:Album Title (2009)` | 1× | AL, M3A |
| `#EXTART:` | album artist | `#EXTART:Various` | 1× | AL, M3A |
| `#EXTGENRE:` | album genre | `#EXTGENRE:Jazz Fusion` | 1× | AL |
| `#EXTM3A` | playlist for tracks or chapters of an album in a single file | `#EXTM3A` | 1× | M3A |
| `#EXTBYT:` | file size in bytes | `#EXTBYT:34124` | No | M3A |
| `#EXTBIN:` | binary data follows, usually concatenated MP3s | `#EXTBIN:` | No | M3A |
| `#EXTALBUMARTURL:` | URL of album art image | `#EXTALBUMARTURL:https://example.com/a1b2c3d4.jpg` | No | Jamendo/VLC |
| `#EXTVLCOPT:` | set VLC option; syntax is of the form `*option-name*=*value*` | `#EXTVLCOPT:start-time=32.5` | No | VLC |

### M3U8

The use of UTF-8 encoding is mandatory in M3U playlists with the **M3U8** file extension. The system codepage is usually assumed for `.m3u` but this is often UTF-8 as well nowadays so the distinction has mostly been lost in practice.

### HLS

Apple used the extended M3U format, UTF-8 encoded, as a base for their HTTP Live Streaming (HLS) which was documented in an Independent Submission Stream RFC in 2017 as RFC 8216. Therein, a *master playlist* references segment playlists which usually contain URLs for short parts of the media stream. Some tags only apply to the former type and some only to the latter type of playlist, but they all begin with `#EXT-X-`.

| Directive | Example | Description |
|---|---|---|
| `#EXT-X-START:` | `TIME-OFFSET=0` |   |
| `#EXT-X-INDEPENDENT-SEGMENTS` | Toggle without parameters |   |
| `#EXT-X-PLAYLIST-TYPE:` | `VOD` or `EVENT` |   |
| `#EXT-X-TARGETDURATION:` | `10` | The maximum Media Segment duration in seconds |
| `#EXT-X-VERSION:` | `4` |   |
| `#EXT-X-MEDIA-SEQUENCE:` | `0` | The Media Sequence Number of the first Media Segment appearing in the playlist file |
| `#EXT-X-MEDIA:` | `NAME="English", TYPE=AUDIO, GROUP-ID="audio-stereo-64", LANGUAGE="en", DEFAULT=YES, AUTOSELECT=YES, URI="english.m3u8"` |   |
| `#EXT-X-STREAM-INF:` | `BANDWIDTH=1123000, CODECS="avc1.64001f,mp4a.40.2"` | Parameters have either one combined value or one per stream, separated by commas |
| `#EXT-X-BYTERANGE:` | `1024@256000` |   |
| `#EXT-X-DISCONTINUITY` | toggle without parameters | The segment represents the start of a new period |
| `#EXT-X-DISCONTINUITY-SEQUENCE:` | `2` | Indicates start of numbering of periods |
| `#EXT-X-GAP` | toggle without parameters | The segment represents a "spacer" before a new period |
| `#EXT-X-KEY:` | `METHOD=NONE` | Indicates encryption method used and decryption key |
| `#EXT-X-MAP:` | `URI=MediaInitializationSection` |   |
| `#EXT-X-PROGRAM-DATE-TIME:` | `2010-02-19T14:54:23.031+08:00` | ISO 8601 format |
| `#EXT-X-DATERANGE:` | `ID=foo` |   |
| `#EXT-X-I-FRAMES-ONLY` | i-frame Toggle without parameters |   |
| `#EXT-X-SESSION-DATA:` | `DATA-ID=com.example.movie.title` |   |
| `#EXT-X-SESSION-KEY:` |   |   |
| `#EXT-X-ENDLIST` | End-of-list signal without parameters |   |

### IPTV

With television broadcasting via the internet protocol (IPTV), M3U playlists are frequently used to store the (start) URLs of the streams, so each entry represents a channel. As usual for continuous streams, the length info directly after `#EXTINF:` is set to `-1`. Unlike HLS, other structured information is not provided in separate info lines but with a key–value syntax before the mandatory comma following the length.

```mw
#EXTINF:-1 tvg-id="123" tvg-name="Channel Name" tvg-logo="http://example.com/logo.png" group-title="Examples", Channel Name
rtsp://example.com/stream
```

| Attribute | Example | Description |
|---|---|---|
| Group | `group-title="News"` | named (thematic) group of channels, i.e. a genre |
| `tvg-group="Music/Rock"` | named group of channels, some players support a hierarchical separator within the value |   |
| Logo | `tvg-logo="/logos/channel.png"` | URL to channel logo image file |
| Name | `tvg-name="Channel TV"` | usually the same name repeated after the comma, but can differ to match `display-name` in XMLTV |
| Number | `tvg-chno="12"` | channel number |
| CUID | `tvg-id="1234"` | unique identifier to link EPG info with (e.g. using `channel-id` in XMLTV) |
| Country | `tvg-country="NZ"` | origin country of the channel, possibly using ISO 3166 codes |
| Language | `tvg-language="English"` | main audio language of the channel, possibly using ISO 639 codes |
| Radio | `radio=true` | boolean value to mark audio-only channels |

## Internet media types

The only Internet media type registered for M3U and M3U8 is `application/vnd.apple.mpegurl`, registered in 2009 and only referring to the playlist format as used in HLS applications.

The current proposal for the HLS playlist format acknowledges two media types which it treats as equivalent: `application/vnd.apple.mpegurl` and `audio/mpegurl`. Likewise, these are the two types recommended for HLS use by Microsoft.

For non-HLS applications, no media types were standardized or registered with the IANA, but a number of media types are nonetheless associated with the historical and ongoing use of the M3U and M3U8 formats for general playlists:

- `application/mpegurl`
- `application/x-mpegurl`
- `audio/mpegurl`
- `audio/x-mpegurl`

These types, plus `application/vnd.apple.mpegurl` and `application/vnd.apple.mpegurl.audio`, are supported for HLS applications by (for example) Microsoft's Windows 10 and Internet Explorer 9, and LG's WebOS.

## Example

The following is an example of an M3U playlist file for the Alice in Chains album *Jar of Flies* that was created by Mp3tag with the following custom option settings:

- playlist extended info format = `"%artist% - %title%"`
- playlist filename format = `"%artist%_%album%_00_Playlist.m3u"`
- tag to filename conversion format = `"%artist%_%album%_$num(%track%,2)_%title%"`

```
 #EXTM3U
 #EXTINF:419,Alice in Chains - Rotten Apple
 Alice in Chains_Jar of Flies_01_Rotten Apple.mp3
 #EXTINF:260,Alice in Chains - Nutshell
 Alice in Chains_Jar of Flies_02_Nutshell.mp3
 #EXTINF:255,Alice in Chains - I Stay Away
 Alice in Chains_Jar of Flies_03_I Stay Away.mp3
 #EXTINF:256,Alice in Chains - No Excuses
 Alice in Chains_Jar of Flies_04_No Excuses.mp3
 #EXTINF:157,Alice in Chains - Whale And Wasp
 Alice in Chains_Jar of Flies_05_Whale And Wasp.mp3
 #EXTINF:263,Alice in Chains - Don't Follow
 Alice in Chains_Jar of Flies_06_Don't Follow.mp3
 #EXTINF:245,Alice in Chains - Swing On This
 Alice in Chains_Jar of Flies_07_Swing On This.mp3
```

## Software

### Tag editors

The following tag editor software allows users to edit the ID3 tags in MP3 files, and has support for creating M3U files.

**Linux**

- Kid3, Puddletag.

**Windows**

- Mp3tag, Puddletag.

**macOS**

- Mp3tag.

### Media players

The following media player software supports playing M3U files.

**Multi-platform**

| Programs | Platforms |   |   |   |   |
|---|---|---|---|---|---|
| Windows | macOS | Linux | Android | Other |   |
| Amarok | Yes | No | Yes | No | No |
| Audacious | Yes | No | Yes | No | No |
| Banshee | Yes | Yes | Yes | No | Yes |
| Clementine | Yes | Yes | Yes | No | Yes |
| foobar2000 | Yes | Yes | No | Yes | Yes |
| iTunes | Yes | Yes | No | No | No |
| Kodi | Yes | Yes | Yes | Yes | Yes |
| make_playlist (mkpl) | Yes | Yes | Yes | No | No |
| MOC (Music on Console) | No | No | Yes | No | Yes |
| MPlayer | Yes | Yes | Yes | Yes | Yes |
| mpv | Yes | Yes | Yes | Yes | Yes |
| VLC media player | Yes | Yes | Yes | Yes | Yes |

**Android**

- Astro Player, Kodi, N7Player, Musicolet

**macOS**

- Music, QuickTime Player, IINA

**Nintendo**

- New Nintendo 3DS (including XL and 2DS XL variants) with Internet Browser app
- Nintendo Switch with the YouTube (site-specific) app
- Wii U with the Internet Browser or YouTube app

**Windows**

- foobar2000, JRiver Media Center, JuK, MediaMonkey, PotPlayer, Winamp, Windows Media Player, XMPlay
