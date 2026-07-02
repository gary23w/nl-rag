---
title: "General MIDI"
source: https://en.wikipedia.org/wiki/General_MIDI
domain: midi-protocol
license: CC-BY-SA-4.0
tags: midi protocol, general midi, midi sequencer, musical note event
fetched: 2026-07-02
---

# General MIDI

**General MIDI** (also known as **GM** or **GM 1**) is a standardized specification for electronic musical instruments that respond to MIDI messages. GM was developed by the American MIDI Manufacturers Association (MMA) and the Japan MIDI Standards Committee (JMSC) and first published in 1991. The official specification is available in English from the MMA, bound together with the MIDI 1.0 specification, and in Japanese from the Association of Musical Electronic Industry (AMEI).

GM imposes several requirements beyond the more abstract MIDI 1.0 specification. While MIDI 1.0 by itself provides a communication protocol which ensures that different instruments can interoperate at a fundamental level – for example, that pressing keys on a MIDI keyboard will cause an attached MIDI sound module to play musical notes – GM goes further in two ways. First, GM requires that all compliant MIDI instruments meet a certain minimal set of features, such as being able to play at least 24 notes simultaneously (polyphony). Second, GM attaches specific interpretations to many parameters and control messages which were left unspecified in the MIDI 1.0 specification. For example, assigning one of the 128 possible MIDI *Program Number*s selects an instrument. With MIDI 1.0, the assignment could be to an arbitrary instrument; but with GM, a program number assigns a specific *instrument name*. This helps ensure that playback of MIDI files sounds more consistent between different devices compliant with the GM specification. However, it still leaves the actual *sounds* of each instrument up to the supplier to implement; one manufacturer's French horn, say, could be brighter, or more mellow, than another's.

The GM 1 specification was extended by General MIDI 2 in 1999; however, GM 1 is still commonly used. General MIDI was widely supported by computer game developers in the 1990s.

## General MIDI 1 requirements

To be GM 1 compatible, sound generating devices (keyboards, hardware or software synthesizers, sound cards) are required to meet the General MIDI System Level 1 performance specification:

| Criterion | Requirement |
|---|---|
| Voices | Allow 24 voices to be available simultaneously for both melodic and percussive sounds (alternatively, allow 16 melodic and 8 percussive voices). All voices respond to note velocity. |
| Channels | Support all 16 channels simultaneously, each assignable to different instruments. Channel 10 is reserved for percussion. Support polyphony (multiple simultaneous notes) on each channel. |
| Instruments | Support a minimum of 128 MIDI Program Numbers (conforming to the GM 1 Instrument Patch Map) and 47 percussion sounds (conforming to the GM 1 Percussion Key Map). |
| Channel messages | Support for controller number 1, 7, 10, 11, 64, 100, 101, 121 and 123; support for channel pressure and pitch bend controllers. |
| Other messages | Respond to the data entry controller and the RPNs for fine and coarse tuning and pitch bend range, as well as all General MIDI Level 1 System Messages. |

## Parameter interpretations

GM Instruments must also obey the following conventions for program and controller events:

### Program change events

In MIDI, the instrument sound or "program" for each of the 16 possible MIDI channels is selected with the Program Change message, which has a Program Number parameter. The following table shows which instrument sound corresponds to each of the 128 possible GM Program Numbers. There are 128 program numbers. The numbers can be displayed as values 1 to 128, or, alternatively, as 0 to 127. The 0 to 127 numbering is usually only used internally by the synthesizer; the vast majority of MIDI devices, digital audio workstations and professional MIDI sequencers display these Program Numbers as shown in the table (1–128).

#### Piano

- 1 Acoustic Grand Piano *or* Piano 1
- 2 Bright Acoustic Piano *or* Piano 2
- 3 Electric Grand Piano *or* Piano 3 (usually modeled after Yamaha CP-70)
- 4 Honky-tonk Piano
- 5 Electric Piano 1 (usually a Rhodes or Wurlitzer piano)
- 6 Electric Piano 2 (usually an FM piano patch, often chorused)
- 7 Harpsichord (often with a fixed velocity level)
- 8 Clavinet

#### Chromatic Percussion

- 9 Celesta
- 10 Glockenspiel
- 11 Music Box
- 12 Vibraphone
- 13 Marimba
- 14 Xylophone
- 15 Tubular Bells
- 16 Dulcimer *or* Santoor

#### Organ

- 17 Drawbar Organ *or* Organ 1
- 18 Percussive Organ *or* Organ 2
- 19 Rock Organ *or* Organ 3
- 20 Church Organ
- 21 Reed Organ
- 22 Accordion
- 23 Harmonica
- 24 Bandoneon *or* Tango Accordion

#### Guitar

- 25 Acoustic Guitar (*nylon*)
- 26 Acoustic Guitar (*steel*)
- 27 Electric Guitar (*jazz*)
- 28 Electric Guitar (*clean*, often chorused, resembling a Stratocaster run through a Roland Jazz Chorus amplifier)
- 29 Electric Guitar (*muted*)
- 30 Overdriven Guitar
- 31 Distortion Guitar
- 32 Guitar Harmonics

#### Bass

On synthesizers, samplers and other electronic devices, bass sounds are often set one octave lower than other instruments.

- 33 Acoustic Bass
- 34 Electric Bass (*finger*)
- 35 Electric Bass (*picked*)
- 36 Fretless Bass
- 37 Slap Bass 1
- 38 Slap Bass 2
- 39 Synth Bass 1
- 40 Synth Bass 2

#### Strings

- 41 Violin
- 42 Viola
- 43 Cello
- 44 Contrabass
- 45 Tremolo Strings
- 46 Pizzicato Strings
- 47 Orchestral Harp
- 48 Timpani

#### Ensemble

- 49 String Ensemble 1 (often in marcato)
- 50 String Ensemble 2 (slower attack than String Ensemble 1)
- 51 Synth Strings 1
- 52 Synth Strings 2
- 53 Choir Aahs
- 54 Voice Oohs (or *Doos*)
- 55 Synth Voice *or* Synth Choir
- 56 Orchestra Hit

#### Brass

- 57 Trumpet
- 58 Trombone
- 59 Tuba
- 60 Muted Trumpet
- 61 French Horn
- 62 Brass Section
- 63 Synth Brass 1
- 64 Synth Brass 2

#### Reed

- 65 Soprano Sax
- 66 Alto Sax
- 67 Tenor Sax
- 68 Baritone Sax
- 69 Oboe
- 70 English Horn
- 71 Bassoon
- 72 Clarinet

#### Pipe

- 73 Piccolo
- 74 Flute
- 75 Recorder
- 76 Pan Flute
- 77 Blown bottle
- 78 Shakuhachi
- 79 Whistle
- 80 Ocarina

#### Synth Lead

- 81 Lead 1 (square, often chorused)
- 82 Lead 2 (*sawtooth* or *saw*, often chorused)
- 83 Lead 3 (*calliope*, usually resembling a woodwind)
- 84 Lead 4 (*chiff*)
- 85 Lead 5 (*charang*, a guitar-like lead)
- 86 Lead 6 (*voice*, derived from "synth voice" with faster attack)
- 87 Lead 7 (*fifths*)
- 88 Lead 8 (*bass and lead* or *solo lead* or sometimes mistakenly called "brass and lead")

#### Synth Pad

- 89 Pad 1 (*new age*, pad stacked with a bell, often derived from "Fantasia" patch from Roland D-50)
- 90 Pad 2 (*warm*, a mellower pad with slow attack)
- 91 Pad 3 (*polysynth* or *poly*, a saw-like percussive pad resembling an early 1980s polyphonic synthesizer)
- 92 Pad 4 (*choir*, identical to "synth voice" with longer decay)
- 93 Pad 5 (*bowed glass* or *bowed*, a sound resembling a glass harmonica)
- 94 Pad 6 (*metallic*, often created from a piano or guitar sample played with the attack removed)
- 95 Pad 7 (*halo*, choir-like pad, often with a filter effect)
- 96 Pad 8 (*sweep*, pad with a pronounced "wah" filter effect)

#### Synth Effects

- 97 FX 1 (*rain*, a bright pluck with echoing pulses that decreases in pitch)
- 98 FX 2 (*soundtrack*, a bright perfect fifth pad)
- 99 FX 3 (*crystal*, a synthesized bell sound)
- 100 FX 4 (*atmosphere*, usually a classical guitar-like sound)
- 101 FX 5 (*brightness*, bright pad stacked with choir or bell)
- 102 FX 6 (*goblins*, a slow-attack pad with chirping or murmuring sounds)
- 103 FX 7 (*echoes* or *echo drops*, similar to "rain")
- 104 FX 8 (*sci-fi* or *star theme*, usually an electric guitar-like pad)

#### Ethnic

- 105 Sitar
- 106 Banjo
- 107 Shamisen
- 108 Koto
- 109 Kalimba
- 110 Bag pipe
- 111 Fiddle
- 112 Shanai

#### Percussive

- 113 Tinkle Bell
- 114 Agogô *or* cowbell
- 115 Steel Drums
- 116 Woodblock
- 117 Taiko Drum *or* Surdo
- 118 Melodic Tom
- 119 Synth Drum (a synthesized tom-tom derived from Simmons electronic drum)
- 120 Reverse Cymbal

#### Sound Effects

- 121 Guitar Fret Noise
- 122 Breath Noise
- 123 Seashore
- 124 Bird Tweet
- 125 Telephone Ring
- 126 Helicopter
- 127 Applause
- 128 Gunshot

### Percussion

In GM standard MIDI files, channel 10 is reserved for percussion instruments only. Notes recorded on channel 10 always produce percussion sounds when transmitted to a keyboard or synth module which uses the GM standard. Each distinct note number specifies a unique percussive instrument, rather than the sound's pitch.

If a MIDI file is programmed to the General MIDI protocol, then the results are predictable, but timbre and sound fidelity may vary depending on the quality of the GM synthesizer. The General MIDI standard includes 47 percussive sounds, using note numbers 35-81 (of the possible 128 numbers from 0–127), as follows:

- 35 Acoustic Bass Drum *or* Low Bass Drum
- 36 Electric Bass Drum *or* High Bass Drum
- 37 Side Stick
- 38 Acoustic Snare
- 39 Hand Clap
- 40 Electric Snare *or* Rimshot
- 41 Low Floor Tom
- 42 Closed Hi-hat
- 43 High Floor Tom
- 44 Pedal Hi-hat
- 45 Low Tom
- 46 Open Hi-hat
- 47 Low-Mid Tom
- 48 High-Mid Tom
- 49 Crash Cymbal 1
- 50 High Tom
- 51 Ride Cymbal 1
- 52 Chinese Cymbal
- 53 Ride Bell
- 54 Tambourine
- 55 Splash Cymbal
- 56 Cowbell
- 57 Crash Cymbal 2
- 58 Vibraslap
- 59 Ride Cymbal 2
- 60 High Bongo
- 61 Low Bongo
- 62 Mute High Conga
- 63 Open High Conga
- 64 Low Conga
- 65 High Timbale
- 66 Low Timbale
- 67 High Agogô
- 68 Low Agogô
- 69 Cabasa
- 70 Maracas
- 71 Short Whistle
- 72 Long Whistle
- 73 Short Güiro
- 74 Long Güiro
- 75 Claves
- 76 High Woodblock
- 77 Low Woodblock
- 78 Mute Cuíca
- 79 Open Cuíca
- 80 Mute Triangle
- 81 Open Triangle

The standard does not specify program change numbers for different drum sets.

### Controller events

In MIDI, adjustable parameters for each of the 16 possible MIDI channels may be set with the Control Change (CC) message, which has a Control Number parameter and a Control Value parameter (expressed in a range from 0 to 127). GM also specifies which operations should be performed by multiple Control Numbers.

| CC Function 0 Pitch bend (MSB/LSB) 1 Modulation wheel 7 Channel volume 10 Channel pan 11 Expression controller 64 Sustain pedal 66 Sostenuto pedal 67 Soft pedal 121 Reset all controllers 123 All notes off/on |
|---|

### RPN

GM defines several Registered Parameters, which act like Controllers but are addressed in a different way. In MIDI, every Registered Parameter is assigned a Registered Parameter Number or RPN. Registered Parameters are usually called RPNs for short.

Setting Registered Parameters requires sending (numbers are decimal):

1. two Control Change messages using Control Numbers 101 and 100 to select the parameter, followed by
2. any number of Data Entry messages of one or two bytes (MSB = Controller #6, LSB = Controller #38), and finally
3. an "End of RPN" message

The following global Registered Parameter Numbers (RPNs) are standardized (the parameter is specified by RPN LSB/MSB pair and the value is set by Data Entry LSB/MSB pair):

- 0,0 Pitch bend range
- 1,0 Channel Fine tuning
- 2,0 Channel Coarse tuning

An example of an RPN control sequence to set coarse tuning to A440 (parm 2, value 64) is `101:0`, `100:2`, `6:64`, `101:127`, `100:127`.

### System Exclusive messages

Two GM System Exclusive ("SysEx") messages are defined: one to enable and disable General MIDI compatibility mode (for synthesizers that also have non-GM modes); and the other to set the synthesizer's master volume.

## GS extensions

Roland GS is a superset of the General MIDI standard that added several proprietary extensions. The most notable addition was the ability to address multiple banks of programs (instrument sounds) by using an additional pair of Bank Select controllers to specify up to 16384 "variation" sounds (cc#0 is Bank Select MSB, and cc#32 is Bank Select LSB). Other most notable features were 9 Drum kits with 14 additional drum sounds each, simultaneous Percussion Kits – up to 2 (Channels 10/11), Control Change messages for controlling the send level of sound effect blocks (cc#91-94), entering additional parameters (cc#98-101), portamento, sostenuto, soft pedal (cc#65-67), and model-specific SysEx messages for setting various parameters of the synth engine. The 14 additional drum sounds are numbered 27-34 and 82–87, bracketing the 47 General MIDI standard sounds numbered 35–81, and are as follows:

- 27 High Q *or* Filter Snap
- 28 Slap Noise
- 29 Scratch Push
- 30 Scratch Pull
- 31 Drum sticks
- 32 Square Click
- 33 Metronome Click
- 34 Metronome Bell
- 82 Shaker
- 83 Jingle Bell
- 84 Belltree
- 85 Castanets
- 86 Mute Surdo
- 87 Open Surdo

GS was introduced in 1991 with the Roland Sound Canvas line, which was also Roland's first General MIDI synth module.

## XG extensions

Yamaha XG is a superset of the General MIDI standard that added several proprietary extensions. The most notable additions were the 352 added instruments and 32 notes polyphony.

XG was introduced in 1994 with the Yamaha MU-series line of sound modules and PSR line of digital keyboards.

## General MIDI Level 2

In 1999, the official GM standard was updated to include more controllers, patches, RPNs and SysEx messages, in an attempt to reconcile the conflicting and proprietary Roland GS and Yamaha XG additions. Here's a quick overview of the GM2 changes in comparison to GM/GS:

- Number of Notes – minimum 32 simultaneous notes
- Simultaneous Percussion Kits – up to 2 (Channels 10/11)
- Up to 16384 variation banks are allowed, each containing a version of the 128 Melodic Sounds (the exact use of these banks is up to the individual manufacturer.)
- 9 GS Drum kits are included
- Additional Control Change introduced, called "Sound Controllers 1–10":

| CC Default function 70 Sound Variation 71 Timbre/Harmonic Intensity (filter resonance) 72 Release Time 73 Attack Time 74 Brightness (cutoff frequency) | CC Default function 75 Decay Time 76 Vibrato Rate 77 Vibrato Depth 78 Vibrato Delay 79 Metronome Rate |
|---|---|

- Registered Parameter Numbers (RPNs)
  - Modulation Depth Range (Vibrato Depth Range)
- Universal SysEx messages
  - Master Volume, Fine Tuning, Coarse Tuning
  - Reverb Type, Time
  - Chorus Type, Mod Rate, Mod Depth, Feedback, Send to Reverb
  - Controller Destination Setting
  - Scale/Octave Tuning Adjust
  - Key-Based Instrument Controllers
  - GM2 System On SysEx message

Additional melodic instruments can be accessed by setting CC#0 to 121 and then using CC#32 to select the bank before a Program Change.
