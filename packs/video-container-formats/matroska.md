---
title: "Matroska"
source: https://en.wikipedia.org/wiki/Matroska
domain: video-container-formats
license: CC-BY-SA-4.0
tags: media container, matroska mkv, mp4 container, quicktime file format
fetched: 2026-07-02
---

# Matroska

**Matroska** (styled **Matroška**) is a project to create a container format that can hold an unlimited number of video, audio, picture, or subtitle tracks in one file. The **Matroska Multimedia Container** is similar in concept to other containers like AVI, MP4, or Advanced Systems Format (ASF), but is an open standard.

Matroska file extensions are *.mkv* for video (which may include audio, subtitles and chapters), *.mk3d* for stereoscopic video, *.mka* for audio-only files (which may include subtitles), and *.mks* for subtitles only.

## History

The project was announced on 6 December 2002 as a fork of the Multimedia Container Format (MCF), after disagreements between MCF lead developer Lasse Kärkkäinen and soon-to-be Matroska founder Steve Lhomme about the use of the Extensible Binary Meta Language (EBML) instead of a binary format. This coincided with a 6-month coding break by the MCF's lead developer for his military service, during which most of the community quickly migrated to the new project.

In 2010, it was announced that the WebM audio/video format would be based on a profile of the Matroska container format together with VP8 video and Vorbis audio.

On 31 October 2014, Microsoft confirmed that Windows 10 would support HEVC and Matroska out of the box, according to a statement from Gabriel Aul, the leader of Microsoft Operating Systems Group's Data and Fundamentals Team. Windows 10 Technical Preview Build 9860 added platform level support for HEVC and Matroska.

In October 2024, Matroska was formally specified in and published as RFC 9559.

## Name and logo

"Matroska" is derived from *matryoshka* (Russian: матрёшка [mɐˈtrʲɵʂkə]), the Russian name for the hollow wooden dolls, better known in English as Russian nesting dolls, which open to expose another smaller doll, that in turn opens to expose another doll, and so on. The logo writes it as "Matroška"; the letter š, an "s" with a caron over it, represents the "sh" sound (/ʂ/) in various languages.

## Design

The use of EBML allows extension for future format changes. The Matroska team has expressed some of their long-term goals on Doom9.org and Hydrogenaudio forums. Thus, the following are "goals", not necessarily existing features, of Matroska:

- Creating a modern, flexible, extensible, cross-platform multimedia container format
- Developing robust streaming support (both this format and the WebM subset are streamable)
- Developing a menu system similar to that of DVDs based on EBML (as of July 2019, there is only a mostly empty draft)
- Developing a set of tools for the creation and editing of Matroska files (MKVToolNix, for example)
- Developing libraries to allow developers to add Matroska support to their applications (made open source by Matroska developers)
- Working with hardware manufacturers to include Matroska support in embedded multimedia devices

## Development

Matroska is supported by a non-profit organization registered in France. It is a royalty-free open standard that is free to use, with the specification being freely available for both private and commercial use. The Matroska development team licenses its libraries under the LGPL, with parsing and playback libraries available under BSD licenses.

## Support

Software supporting Matroska include all ffmpeg-based ones, including, notably, mplayer, mpv, VLC, Foobar2000, Media Player Classic-HC, Google Chrome, Mozilla Firefox, Blender, Kdenlive, HandBrake, MKVToolNix as well as YouTube (which uses WebM extensively), and OBS Studio.

Outside of ffmpeg, Windows 10 supports Matroska natively as well. Earlier versions relied on codec packs (like K-Lite Codec Pack or Combined Community Codec Pack) to integrate ffmpeg (via ffdshow) and other additions into Windows' native DirectShow.
