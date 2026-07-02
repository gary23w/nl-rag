---
title: "Wavetable synthesis"
source: https://en.wikipedia.org/wiki/Wavetable_synthesis
domain: audio-synthesis
license: CC-BY-SA-4.0
tags: sound synthesis, subtractive synthesis, fm synthesis, wavetable synthesis
fetched: 2026-07-02
---

# Wavetable synthesis

**Wavetable synthesis** is a sound synthesis technique used to create quasi-periodic waveforms often used in the production of musical tones or notes. It uses a series of waveforms that are digitized as a series of amplitude values. Each waveform normally consists of a single cycle of the wave. Many such digitized waves are collected and stored in a table, often containing a series of slightly modified versions of an original "pure" tone.

To produce output, the system selects a starting point within the table and a length, and the system loops through that section of the stored waveforms and plays it repeatedly. Each amplitude value is read from memory in turn, often stored in ROM. The series of numbers being read is sent into an digital-to-analog converter, which converts the value into an electrical signal to produce an audible signal. Most systems include the capability to mix multiple samples together to produce more complex output.

One example of the technique is in the Waldorf Microwave synthesizer which had loadable wavetables. One consisted of the statement "nineteen twenty" from a voice synthesizer. By selecting different starting points and lengths within this sample, a wide variety of sounds can be produced.

## Development

Wavetable synthesis was invented by Max Mathews in 1958 as part of MUSIC II. MUSIC II “had four-voice polyphony and was capable of generating sixteen wave shapes via the introduction of a wavetable oscillator.”

Hal Chamberlin discussed wavetable synthesis in Byte's September 1977 issue. Wolfgang Palm of Palm Products GmbH (PPG) developed his version in the late 1970s and published it in 1979. The technique has since been used as the primary synthesis method in synthesizers built by PPG and Waldorf Music and as an auxiliary synthesis method by Ensoniq and Access. It is currently used in hardware synthesizers from Waldorf Music and in software synthesizers for PCs and tablets, including apps offered by PPG and Waldorf, among others.

It was also independently developed by Michael McNabb, who used it in his 1978 composition *Dreamsong*.

## Principle

Electronic synthesizers using digital techniques generally produce sounds by producing a digital value, a number, and then sending that value to an digital-to-analog converter (DAC) that produces a scaled output voltage. For instance, to produce a triangle wave or sawtooth, systems used a register containing a starting value, normally zero, and then periodically increase or decrease the value using an adder or phase accumulator. The value in the register is continually sent to the DAC to produce output. The pitch of the resulting sound can be changed by how rapidly the adder is called.

Wavetable synthesis is a relatively simple modification of this sort of system. Instead of the value at any particular instantly being periodically modified by a simple function like addition, the specific value for any instant is read from memory containing a series of values making up multiple arbitrary, single-cycle waveforms. This allows the waveform to have any shape, not just simple ones like triangles or sines. With that exception, the system is otherwise the same; values are read into the register at a rate that produces the desired pitch, and the output of the register is used to feed a DAC that produces the output signal. In order to produce a different sound, all that has to be changed is a single value pointing to the starting point of the waveform in memory.

Because the table contains many different waveforms, playing a longer sample that includes several different waveforms may result in odd side-effects when the system crosses the boundaries between the individual waveforms. Digital interpolation between adjacent waveforms allows for dynamic and smooth changes of the timbre of the tone produced. Additional effects can be provided by reading the waveform forward or backward, and further controlled in a number of ways, for example, by use of an LFO, envelope, pressure or velocity.

Many wavetables used in PPG and Ensoniq synthesizers can simulate the methods used by analog synthesizers, such as pulse-width modulation by utilising a number of square waves of different duty cycles. In this way, when the wavetable is swept, the duty cycle of the pulse wave will appear to change over time. As the early Ensoniq wavetable synthesizers had non resonant filters (the PPG Wave synthesizers used Curtis analogue resonant filters), some wavetables contained highly resonant waveforms to overcome this limitation of the filters.

### Confusion with sample-based synthesis (S&S) and Digital Wave Synthesis

In 1992, with the introduction of the Creative Labs Sound Blaster 16 the term "wavetable" started to be (incorrectly) applied as a marketing term to their sound card. However, these sound cards did not employ any form of wavetable synthesis, but rather PCM samples and FM synthesis.

S&S (Sample and Synthesis) and Digital Wave Synthesis was the main method of sound synthesis utilised by digital synthesizers starting in the mid 1980s with synthesizers such as Sequential Circuits Prophet VS, Korg DW-6000/8000 (DW standing for Digital Wave), Roland D-50 and Korg M1 through to current synthesizers.

Ableton addressed some confusion in an article:

> Wait, so isn't this just sampled synthesis? Let's pause here to address a common confusion. While sampled synthesis involves the use of a static digital sample, wavetable synthesis allows for the (optional) evolution of a waveform; this is to say, while wavetable synths can sound like sampled synthesis, the evolving option (which is enabled by default on most classic wavetable sounds) differentiates it.

## User wavetables

The creation of new wavetables was previously a difficult process unless supported by specialized editing facilities and (near) real-time playback of edited wavetables on the synthesizer. Such editors often required the use of extra hardware devices like the PPG Waveterm or were only present in expensive models like the Waldorf WAVE. More commonly, pre-computed wavetables could be added via memory cards or sent to the synthesizer via MIDI. Today, wavetables can be created more easily by software and auditioned directly on a computer. Since all waveforms used in wavetable synthesis are periodic, the time-domain and frequency-domain representation are exact equivalents of each other and both can be used simultaneously to define waveforms and wavetables.

### Practical use

During playback, the sound produced can be harmonically changed by moving to another point in the wavetable, usually under the control of an envelope generator or low-frequency oscillator but frequently by any number of modulators (matrix modulation). Doing this modifies the harmonic content of the output wave in real time, producing sounds that can imitate acoustic instruments or be totally abstract, which is where this method of sound creation excels. The technique is especially useful for evolving synth pads, where the sound changes slowly over time.

It is often necessary to 'audition' each position in a wavetable and to scan through it, forwards and backwards, in order to make good use of it, though selecting random wavetables, start positions, end positions and directions of scan can also produce satisfying musical results. It is worth noting that most wavetable synthesizers also employ other synthesis methods to further shape the output waveform, such as subtractive synthesis (filters), phase modulation, frequency modulation and AM (ring) modulation.

## Table-lookup synthesis

An example of

lookup table

, where the data at addresses from 63 to 67 are zoomed.

(based on Figure 2.1 on

Nelson 2000

)

On Csound, it is called *f-table* (function table), and used for various purposes including: wavetable-lookup synthesis, waveshaping, MIDI note mapping, and storing ordered pitch-class sets.

An example of the content of

f-table

visually shown: a single-cycle

sinusoidal wave

.

**Table-lookup synthesis** (or **Wavetable-lookup synthesis**) (Roads 1996) is a class of sound synthesis methods using the waveform tables by table-lookup, called "table-lookup oscillator" technique. The length of waveforms or samples may be varied by each sound synthesis method, from a single-cycle up to several minutes.

### Terminologies

The term "*waveform table*" (or "*wave shape table*" as equivalent) is often abbreviated to "wavetable", and its derived term "*wavetable oscillator*" seems to be almost the same as "*table-lookup oscillator*" mentioned above, although the word "wave" (or "waveform", "wave shape") may possibly imply a nuance of single-cycle waveform.

However, the derived term "*wavetable synthesis*" seems slightly confused by the later developments of derived algorithm.

**(1) Wavetable synthesis**

Its original meaning is essentially the same as "

table-lookup synthesis

",

and possibly several actions on waveform(s) may be expected. ⇒

See

(2), (3)

**(2) Wavetable-modification algorithm**

For example,

Karplus–Strong string synthesis

is a simple class of "

wavetable-modification algorithm

" known as

digital waveguide synthesis

.

**(3) Multiple wavetable synthesis**

In the late-1970s, Michael McNabb

and

Wolfgang Palm

independently developed the multiple wavetable extension on the table-lookup synthesis

which was typically used on

PPG Wave

and known as

wavetable sweeping

.

Later, it was referred as "

multiple wavetable synthesis

" by

Horner, Beauchamp & Haken 1993

.

**(4) Sample-based synthesis**

Simultaneously, since the late-1970s,

sample-based synthesis

using relatively long samples instead of single-cycle waveforms has become pervasive due to the introduction of the

Fairlight CMI

and

E-mu

Emulator

.

### Background

On the above four terminologies for the classes of sound synthesis methods — *i.e.*, (1) *Wavetable synthesis*, (2) *Wavetable-modification algorithm*, (3) *Multiple wavetable synthesis*, and (4) *Sample-based synthesis* — if these had been appropriately used to distinguish each other, any confusions could be avoided, but it seems failed historically. In the 1990s at the latest, several influential sample-based synthesis products were marketed under the trade names similar to "wavetable synthesis" (including Gravis Ultrasound wavetable card, Creative Wave Blaster wavetable daughterboard, and Microsoft GS Wavetable SW Synth), and these confusions have further affected industry standards (including MPEG-4 Structured Audio *algorithmic and wavetable synthesis*, and AC97 *optional hw acceleration wavetable synth*). In the mid-2000s, confusion in terminology cropped up yet-again. A subclass of generic wavetable synthesis, *i.e.* McNabb and Palm's multiple wavetable synthesis, tends to be erroneously referred as if it was a generic class of whole wavetable synthesis family, exclusively.

As a result, the difficulty of maintaining consistency between concepts and terminology during rapid technological development is noteworthy. For this reason the term "Table-lookup synthesis" is explained at length in this article.
