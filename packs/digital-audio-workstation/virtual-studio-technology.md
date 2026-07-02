---
title: "Virtual Studio Technology"
source: https://en.wikipedia.org/wiki/Virtual_Studio_Technology
domain: digital-audio-workstation
license: CC-BY-SA-4.0
tags: digital audio workstation, vst plugin, audio plug-in, multitrack recording
fetched: 2026-07-02
---

# Virtual Studio Technology

**Virtual Studio Technology** (**VST**) is an open source audio plug-in software interface that integrates virtual instruments and effects units into digital audio workstations. VST and similar technologies use digital signal processing to simulate traditional recording studio hardware in software. Thousands of plugins exist, both commercial and freeware, and many audio applications support VST under license from its creator, Steinberg.

## Overview

VST plugins generally run within a digital audio workstation (DAW), to provide additional functionality, though a few standalone plugin hosts exist that support VST. Most VST plugins are either instruments (VSTi) or effects (VSTfx), although other categories exist—for example spectrum analyzers and various meters. VST plugins usually provide a custom graphical user interface that displays controls similar to physical switches and knobs on audio hardware. Some (often older) plugins rely on the host application for their user interface.

VST instruments include software simulation emulations of well-known hardware synthesizers and samplers. These typically emulate the look of the original equipment as well as its sonic characteristics. This lets musicians and recording engineers use virtual versions of devices that otherwise might be difficult and expensive to obtain.

VST instruments receive notes as digital information via MIDI, and output digital audio. Effect plugins receive digital audio and process it through to their outputs. (Some effect plugins also accept MIDI input—for example, MIDI sync to modulate the effect in sync with the tempo). MIDI messages can control both instrument and effect plugin parameters. Most host applications can route the audio output from one VST to the audio input of another VST (*chaining*). For example, the output of a VST synthesizer can be sent through a VST reverb effect.

## History

Steinberg released the VST interface specification and SDK in 1996. They released it at the same time as Steinberg Cubase 3.02, which included the first VST format plugins: Espacial (a reverb), Choirus (a chorus effect), Stereo Echo, and Auto-Panner.

Steinberg updated the VST interface specification to version 2.0 in 1999. One addition was the ability for plugins to receive MIDI data. This supported the introduction of *Virtual Studio Technology Instrument (VSTi)* format plugins. VST Instruments can act as standalone software synthesizers, samplers, or drum machines.

Neon was the first available VST Instrument (included with Cubase VST 3.7). It was a 16-voice, 2-oscillator virtual analog synthesizer.

In 2006, the VST interface specification was updated to version 2.4. Changes included the ability to process audio with 64-bit precision. A free-software replacement was developed for LMMS that would be used later by other free-software projects.

VST 3.0 came out in 2008. Changes included:

- Audio Inputs for VST Instruments
- Multiple MIDI inputs/outputs
- Optional SKI (Steinberg Kernel Interface) integration

VST 3.5 came out in February 2011. Changes included *note expression*, which provides extensive articulation information in individual note events in a polyphonic arrangement. According to Steinberg, this supports performance flexibility and a more natural playing feel.

In October 2011, Celemony Software and PreSonus released Audio Random Access (ARA), an extension for audio plug-in interfaces, such as VST, allowing greater integration between audio plug-ins and DAW software.

In September, 2013, Steinberg discontinued maintenance of the VST 2 SDK. In December, Steinberg stopped distributing the SDK. The higher versions are continued.

VST 3.6.7 came out in March, 2017. It includes a preview version of VST3 for Linux platform, the VST3 part of the SDK gets a dual license: "Proprietary Steinberg VST3" or the "Open-source GPLv3".

VST 3.8.0, released in October 2025, changed the licensing to open source under an MIT license.

## VST plugins

There are three types of VST plugins:

- **VST instruments** generate audio. They are generally either virtual synthesizers or virtual samplers. Many recreate the look and sound of famous hardware synthesizers. Better known VST instruments include Discovery, Nexus, Sylenth1, Massive, Omnisphere, FM8, Absynth, Reaktor, Gladiator, Serum and Vanguard.
- **VST effects** process rather than generate audio—and perform the same functions as hardware audio processors such as reverbs and phasers. Other monitoring effects provide visual feedback of the input signal without processing the audio. Most hosts allow multiple effects to be chained. Audio monitoring devices such as spectrum analyzers and meters represent audio characteristics (frequency distribution, amplitude, etc.) visually.
- **VST MIDI effects** process MIDI messages (for example, transpose or arpeggiate) and route the MIDI data to other VST instruments or to hardware devices.

## VST hosts

A VST host is a software application or hardware device that VST plugins run under. The host application presents the plugin UIs and routes digital audio and MIDI to and from the plugins.

Examples of VST hosts include media players such as JRiver Media Center and foobar2000.

Stand-alone *dedicated hosts* provide a host environment for VST plugins rather than use the plugins to extend their own capabilities. These are usually optimized for live performance use, with features like fast song configuration switching.

VST plugins can be hosted in incompatible environments using a translation layer, or shim. For example, FL Studio only supports its own internal plugin architecture, but an available native "wrapper" loads VST plugins, among others. FXpansion offers a VST-to-RTAS (Real Time AudioSuite) wrapper that lets VST plugins run in Pro Tools, and a VST-to-Audio Units wrapper lets VST plugins run in Logic Pro.

### Hardware

Hardware VST hosts can load special versions of VST plugins. These units are portable and usable without a computer, though some of them require a computer for editing. Other hardware options include PCI/PCIe cards designed for audio processing, which take over audio processing from the computer's CPU and free up RAM.

Some hardware hosts accept VSTs and VSTis, and either run Windows-compatible music applications like Cubase, Live, Pro Tools, Logic etc., or run their own DAW. Other are VST Hosts only and require a separate DAW application. *Origin* from Arturia is a hardware DSP system that houses several VST software synthesizers in one machine, like Jupiter 50/80 from Roland. Using appropriate software, audio data can also be sent over a network, so the main host runs on one computer, and VST plugins on peripheral machines.

## Standard

The VST plugin standard is the audio plugin standard created by Steinberg to allow any third-party developers to create VST plugins for use within VST host applications. VST requires separate installations for Windows, macOS, and Linux. The short history of commercial environments for Linux means few developers have targeted this platform.

## Presets

VST plugins often have many controls, and therefore need a method of managing presets (sets of control settings).

Steinberg Cubase VST introduced two file formats for storing presets: an FXP file stores a single preset, while an FXB file stores a whole bank of presets. These formats have since been adopted by many other VST hosts, although Cubase itself switched to a new system of preset management with Cubase 4.0.

Many VST plugins have their own method of loading and saving presets, which do not necessarily use the standard FXP/FXB formats.

## Competing technologies

- Apple's Audio Units
- Digidesign's Real Time AudioSuite
- LADSPA, DSSI for Linux
- LV2, a cross-platform, open source, permissively licensed audio plugin standard
- Microsoft's DirectX plugin
- Mark of the Unicorn's Motu Audio System
- JACK Audio Connection Kit, an open-source sound server allowing flexible audio routing between apps
- CLever Audio Plug-in (CLAP), a MIT-licensed alternative to VST3

## Programming languages

Steinberg's VST SDK is a set of C++ classes based around an underlying C API. The SDK can be downloaded from their website.

In addition, Steinberg has developed the VST GUI, which is another set of C++ classes, which can be used to build a graphical interface. There are classes for buttons, sliders and displays, etc. Note that these are low-level C++ classes and the look and feel still have to be created by the plugin manufacturer. VST GUI is part of the VST SDK and is also available as a SourceForge project.

There are also several ports to other programming languages available from third parties.

Many commercial and open-source VSTs are written using the Juce C++ framework instead of direct calls to the VST SDK because this allows multi-format (VST, Audio Units and Real Time AudioSuite) binaries to be built from a single codebase.
