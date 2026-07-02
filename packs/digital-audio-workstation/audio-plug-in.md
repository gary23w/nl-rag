---
title: "Audio plug-in"
source: https://en.wikipedia.org/wiki/Audio_plug-in
domain: digital-audio-workstation
license: CC-BY-SA-4.0
tags: digital audio workstation, vst plugin, audio plug-in, multitrack recording
fetched: 2026-07-02
---

# Audio plug-in

In computer software, an **audio plug-in** is a plug-in that can add or enhance audio-related functions in a computer program, typically a digital audio workstation. Such functions may include digital signal processing or sound synthesis. Audio plug-ins usually provide their own user interface, which often contains graphical user interface (GUI) widgets that can be used to control and visualize the plug-in's audio parameters.

## Types

There are three broad classes of audio plug-in: those which transform existing audio samples, those which generate new audio samples through sound synthesis, and those which analyze existing audio samples. Although all plug-in types can technically perform audio analysis, only specific formats provide a mechanism for analysis data to be returned to the host.

## Instances

The program used to dynamically load audio plug-ins is called a plug-in host. Example hosts include Bidule, Gig Performer, Mainstage, REAPER, and Sonic Visualiser. Plug-ins can also be used to host other plug-ins. Communication between host and plug-in(s) is determined by a plug-in application programming interface (API). The API declares functions and data structures that the plug-in must define to be usable by a plug-in host. Additionally, a functional specification may be provided, which defines how the plug-in should respond to function calls, and how the host should expect to handle function calls to the plug-in. The specification may also include documentation about the meaning of variables and data structures declared in the API. The API header files, specification, shared libraries, license, and documentation are sometimes bundled together in a software development kit (SDK).

## List of plug-in architectures

| Name | Developer | License | GUI support | Supported types | Supported platforms | Supported DAWs |
|---|---|---|---|---|---|---|
| Rack Extension | Reason Studios | BSD-style | Yes | Transformation, synthesis | macOS, Windows | Reason |
| Virtual Studio Technology | Steinberg | Proprietary or MIT | Yes | Transformation, synthesis | Linux, macOS, Windows | (Most DAWs) |
| Audio Units | Apple | Proprietary | Yes | Transformation, synthesis | iOS, macOS, tvOS | (Most DAWs on Apple Software) |
| Real Time AudioSuite | Avid | Proprietary | Yes | Transformation, synthesis | macOS, Windows | Pro Tools (32-bit only) |
| Avid Audio eXtension | Avid | Proprietary | Yes | Transformation, synthesis | macOS, Windows | Pro Tools |
| TDM | Avid | Proprietary | Yes | Transformation, synthesis | macOS, Windows | Pro Tools (32-bit only) |
| LADSPA | ladspa.org | LGPL | No | Transformation | Linux, macOS, Windows | Ardour, LMMS |
| DSSI | Free software | LGPL, BSD | Yes | Transformation, synthesis | Linux, macOS, Windows | Qtractor, Renoise |
| LV2 | lv2plug.in | ISC | Yes | Transformation, synthesis | Linux, macOS, Windows | Ardour, REAPER |
| DirectX plugin | Microsoft | Proprietary | Yes | Transformation, synthesis | Windows | ACID Pro (v3.0 or later), Adobe Audition, Cakewalk Sonar (v2.0 or later), MAGIX Samplitude, REAPER, Sound Forge, Steinberg (Wavelab, Nuendo, Cubase), OpenMPT |
| VAMP | vamp-plugins.org | BSD-style | No | Analysis | Linux, macOS, Windows | Audacity |
| CLAP | Bitwig and others | MIT-style | Yes | Transformation, synthesis | Linux, macOS, Windows | Bitwig, REAPER, FL Studio, MultitrackStudio, MuLab, QTractor |
| Audio Random Access | Celemony Software | BSD-style |   |   | macOS, Windows | Melodyne |

## Notable audio plug-in companies

- Eventide, Inc
- FabFilter
- iZotope
- Native Instruments
- Neural DSP
- Solid State Logic
- Universal Audio
- ValhallaDSP
- Waves Audio
- Xfer Records
