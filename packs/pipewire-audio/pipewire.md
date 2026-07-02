---
title: "PipeWire"
source: https://en.wikipedia.org/wiki/PipeWire
domain: pipewire-audio
license: CC-BY-SA-4.0
tags: pipewire server, jack audio connection kit, audio latency, multimedia routing
fetched: 2026-07-02
---

# PipeWire

**PipeWire** is a low-level server and multimedia framework for handling audio and video streams on Linux. Created by Wim Taymans at Red Hat, it aims to unify audio and video processing by providing low-latency capture and playback functionality. PipeWire facilitates advanced multimedia routing and pipeline processing, and is designed to replace and be compatible with existing sound systems.

## History

In 2015, Taymans started work on PipeWire. It was based on ideas from several existing projects, including one called PulseVideo by William Manley. According to Red Hat's Christian Schaller, it drew many of its ideas from an early PulseVideo prototype by Manley and builds upon some of the code that was merged into GStreamer due to that effort. A goal of the project was to improve handling of video on Linux in the same way that PulseAudio improved handling of audio.

Although a separate project from PulseAudio, Taymans initially considered using the name "PulseVideo" for the new project. By June 2015, the name "Pinos" was being used, after the city Pinos de Alhaurin in Spain, where Taymans used to live.

Initially, Pinos only handled video streams. By early 2017, Taymans had started working on integrating audio streams. Taymans wanted to support both consumer and professional audio use cases, and consulted Paul Davis (JACK developer) and Robin Gareus (Ardour developer) for advice on implementation for professional audio. At this time, the name "PipeWire" was adopted for the project.

In November 2018, PipeWire was re-licensed from the LGPL to the MIT License.

In April 2021, Fedora Linux 34 became the first Linux distribution to ship PipeWire for audio by default. A year later, Pop!_OS adopted it as the default audio server in version 22.04. It was made the default audio server in Ubuntu beginning with version 22.10. In 2023, it was adopted as the default audio server for the GNOME desktop environment in Debian 12 Bookworm.

## Features

The project aims include:

- To work well in sandboxed environments for secure multimedia handling.
- To provide secure methods for screenshotting and screencasting on Wayland compositors.
- To unify audio and video processing, supporting applications based on PulseAudio, JACK, ALSA and GStreamer.
- To provide real time multimedia processing.
- To offer minimal latency for both audio and video capture and playback.
- To offer multi-process architecture allowing multimedia content sharing between applications.
