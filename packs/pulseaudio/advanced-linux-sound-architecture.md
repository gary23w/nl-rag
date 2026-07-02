---
title: "Advanced Linux Sound Architecture"
source: https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture
domain: pulseaudio
license: CC-BY-SA-4.0
tags: pulseaudio server, alsa sound, sound server, open sound system
fetched: 2026-07-02
---

# Advanced Linux Sound Architecture

**Advanced Linux Sound Architecture** (**ALSA**) is a software framework and part of the Linux kernel that provides an application programming interface (API) for sound card device drivers.

Some of the goals of the ALSA project at its inception were automatic configuration of sound-card hardware and graceful handling of multiple sound devices in a system. ALSA is released under GPL-2.0-or-later and LGPL-2.1-or-later.

On Linux, sound servers, like sndio, PulseAudio, JACK (low-latency professional-grade audio editing and mixing) and PipeWire, and higher-level APIs (e.g., OpenAL, SDL audio, etc.) work on top of ALSA and its sound card device drivers. ALSA succeeded the older Linux port of the Open Sound System (OSS).

## History

The project to develop ALSA was led by Jaroslav Kysela, and was based on the Linux device driver for the Gravis Ultrasound sound card. It started in 1998 and was developed separately from the Linux kernel until it was introduced in the 2.5 development series in 2002 (2.5.4–2.5.5).

In the 2.6 version, it replaced the previous system, Open Sound System (OSS), by default (although a backwards-compatibility layer does exist).

ALSA has a larger and more complex API than OSS, so it can be more difficult to develop an application that uses ALSA as its sound technology. While ALSA may be configured to provide an OSS emulation layer, such functionality is no longer available or is not installed by default in many Linux distributions.

## Features

ALSA was designed with some features which were not, at the time of its conception, supported by OSS:

- Hardware-based MIDI synthesis.
- Hardware mixing of multiple channels.
- Full-duplex operation.
- Multiprocessor-friendly, thread-safe device drivers.

Besides the sound device drivers, ALSA bundles a user-space library for application developers who want to use driver features through an interface that is higher-level than the interface provided for direct interaction with the kernel drivers. Unlike the kernel API, which tries to reflect the capabilities of the hardware directly, ALSA's user-space library presents an abstraction that remains as standardized as possible across disparate underlying hardware elements. This goal is achieved in part by using software plug-ins; for example, many modern sound cards or built-in sound chips do not have a "master volume" control. Instead, for these devices, the user space library provides a software volume control using the "softvol" plug-in, and ordinary application software need not care whether such a control is implemented by underlying hardware or software emulation of such underlying hardware.

### Applications

Additional to the software framework internal to the Linux kernel, the ALSA project also provides the command-line tools and utilities `alsactl`, `amixer`, `arecord/aplay` and `alsamixer`, an ncurses-based TUI.

There also are GUIs programmed by third-party developers, such as GNOME-ALSAmixer (using GTK), Kmix, XFCE4-mixer, LXpanel, QasHctl, QasMixer, Pavucontrol, AconnectGUI, tapiir, polarbear, ALSAmixerGUI (using FLTK), ZynAddSubFX, Yoshimi, and even more.

## Concepts

Typically, ALSA supports up to eight *cards*, numbered 0 through 7; each card is a physical or logical kernel device capable of input and output. Furthermore, each card may also be addressed by its *id*, which is an explanatory string such as "*Headset*" or "*ICH9*".

A card has *devices*, numbered starting at 0; a device may be of *playback* type, meaning it outputs sound from the computer, or some other type such as *capture*, *control*, *timer*, or *sequencer*; device number 0 is used by default when no particular device is specified.

A device may have *subdevices*, numbered starting at 0; a subdevice represents some relevant sound endpoint for the device, such as a speaker pair. If the subdevice is not specified, or if subdevice number −1 is specified, then any available subdevice is used.

A card's *interface* is a description of an ALSA protocol for accessing the card; possible interfaces include: *hw*, *plughw*, *default*, and *plug:dmix*. The *hw* interface provides direct access to the kernel device, but no software mixing or stream adaptation support. The *plughw* and *default* enable sound output where the *hw* interface would produce an error.

An application typically describes sound output by combining all of the aforementioned specifications together in a *device string*, which has one of the following forms (which are case-sensitive):

- *interface:card,device,subdevice*
- *interface:CARD=1,DEV=3,SUBDEV=2*.

An ALSA *stream* is a data flow representing sound; the most common stream format is PCM that must be produced in such a way as to match the characteristics or parameters of the hardware, including:

- *sampling rate*: often 44.1 kHz on home stereos, or 48 kHz on home theaters, yet up to 88.2 kHz, 96 kHz, or even 192 kHz for hi-fi audio production or reproduction.
- *sample width*: measured in some number of bits per sample (such as 8, 16, 24, or 32 bits/sample)
- *sample encoding*: such as endianness
- *number of channels*: 1 for mono, 2 for stereo, or 6 for AC-3/IEC958

## Implementations

The ALSA System on Chip (ASoC) layer aims to provide better support for ALSA on embedded systems that use a system-on-chip (SoC) design.

Open Sound System version 4 is able to emulate ALSA.

QNX uses a sound system derived from, but not directly compatible with ALSA. The header file and library names are still "asound", same as the ALSA names. ALSA API uses ioctl() calls in a way not allowed in the QNX kernel.
