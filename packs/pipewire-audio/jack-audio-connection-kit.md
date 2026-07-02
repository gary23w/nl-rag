---
title: "JACK Audio Connection Kit"
source: https://en.wikipedia.org/wiki/JACK_Audio_Connection_Kit
domain: pipewire-audio
license: CC-BY-SA-4.0
tags: pipewire server, jack audio connection kit, audio latency, multimedia routing
fetched: 2026-07-02
---

# JACK Audio Connection Kit

**JACK Audio Connection Kit** (or **JACK**; a recursive acronym) is a professional sound server API and pair of daemon implementations to provide real-time, low-latency connections for both audio and MIDI data between applications. JACK was developed by a community of open-source developers led by Paul Davis (who won an Open Source Award in 2004 for this work) and has been a key piece of infrastructure and the de facto standard for professional audio software on Linux since its inception in 2002. The server is free software, licensed under GPL-2.0-or-later, while the library is licensed under LGPL-2.1-or-later.

## Implementations

The JACK API is standardized by consensus, and two compatible implementations exist: jack1, which is implemented in plain C and has been in maintenance mode for a while, and jack2 (originally jackdmp), a re-implementation in C++ originally led by Stéphane Letz, which introduced multi-processor scalability and support for operating systems other than Linux.

JACK can be used with ALSA, PortAudio, CoreAudio, FFADO and OSS as hardware back-ends. Additionally, a dummy driver (useful if no sound output is desired, e.g. for offline rendering) and an Audio-over-UDP driver exist. One or both implementations can run on Linux, macOS, Solaris, Windows, iOS, FreeBSD, OpenBSD and NetBSD.

The JACK API is also implemented by PipeWire for backwards compatibility as a complete drop-in replacement provider for JACK clients, mapping JACK API calls to equivalent PipeWire calls. If used as a replacement for ALSA and PulseAudio as well, it can unify the different sound servers and APIs that might be typically found on a machine, and allow better integration between different software. PipeWire also claims to add a number of features and fix a number of limitations compared to JACK. The use of PipeWire as the default implementation of JACK is the default on Fedora 34 and newer.

## Low-latency scheduling

The scheduling requirements of JACK to achieve sufficiently low latencies were one of the driving forces behind the real-time optimization effort for the Linux kernel 2.6 series, whose initial latency performance had been disappointing compared to the older 2.4 series. Real-time tuning work culminated in numerous scheduling improvements to the mainline kernel and the creation of an -rt branch for more intrusive optimizations in the release 2.6.24, and later the CONFIG_PREEMPT_RT patch.

## Applications with JACK support
