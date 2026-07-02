---
title: "Frequency modulation synthesis"
source: https://en.wikipedia.org/wiki/Frequency_modulation_synthesis
domain: audio-synthesis
license: CC-BY-SA-4.0
tags: sound synthesis, subtractive synthesis, fm synthesis, wavetable synthesis
fetched: 2026-07-02
---

# Frequency modulation synthesis

| A 220 Hz carrier tone *fc* modulated by a 440 Hz modulating tone *fm*, with various choices of frequency modulation index, *β*. The time domain signals are illustrated above, and the corresponding spectra are shown below (spectrum amplitudes in dB). |
|---|
| Waveforms for each *β* |
| Spectra for each *β* |

**Frequency modulation synthesis** (or **FM synthesis**) is a form of sound synthesis whereby the frequency of a waveform is changed by modulating its frequency with a modulator. The (instantaneous) frequency of an oscillator is altered in accordance with the amplitude of a modulating signal.

Developed in the 1960s by researchers at Stanford University, then commercialized through digital instruments such as the Yamaha GS-1 and popularized by the Yamaha DX7 in the 1980s, FM synthesis has had a lasting influence on recorded music, electronic music, popular music, and video game music. It became closely associated with the sound of the 1980s, while related Yamaha FM chips gave many arcade games, home computers, game consoles, sound cards, and early mobile phone ringtones their characteristic timbres.

Its spread from Stanford University computer-music research into studios, homes, arcades, and consumer devices has made FM synthesis one of the most widely heard forms of digital synthesis of the late-20th century.

## Applications

FM synthesis can create both harmonic and inharmonic sounds. To synthesize harmonic sounds, the modulating signal must have a harmonic relationship to the original carrier signal. As the amount of frequency modulation increases, the sound grows progressively complex. Through the use of modulators with frequencies that are non-integer multiples of the carrier signal (i.e. inharmonic), inharmonic bell-like and percussive spectra can be created.

FM synthesis using analog oscillators may result in pitch instability. However, FM synthesis can also be implemented digitally, which is more stable and became standard practice.

### In synthesizers

Digital FM synthesis (equivalent to phase modulation using the time integration of instantaneous frequency) was the basis of several musical instruments beginning as early as 1974. Yamaha built the first prototype digital synthesizer in 1974, based on FM synthesis, before commercially releasing the Yamaha GS-1 in 1980. The Synclavier I, manufactured by New England Digital Corporation beginning in 1978, had an optional digital FM synthesis module (later built into the Synclavier II) which could be added on to the synthesizer, using an FM synthesis algorithm licensed from Yamaha. Yamaha's groundbreaking Yamaha DX7 synthesizer, released in 1983, brought FM to the forefront of synthesis in the mid-1980s.

### In PCs, arcades, game consoles, and mobile phones

FM synthesis also became the usual setting for games and software up until the mid-nineties. Sound cards for IBM PC compatible systems like the AdLib and Sound Blaster popularized Yamaha chips like the OPL2 and OPL3. Other computers such as the Sharp X68000 and MSX (Yamaha CX5M computer unit) utilize the OPM sound chip (with later CX5M units using the similar OPP sound chip). The NEC PC-88 and PC-98 computers use either the OPN and OPNA sound chips.

For arcade systems and game consoles, the OPM was widely used in many arcade boards from the 1980s and 1990s (including Sega's System 16 and Capcom's CP System arcade boards); the similar OPN was also used in some arcade boards in the 1980s. OPNB was notably used in SNK's Neo Geo arcade (MVS) and home console (AES) machines, as well as being used as the main basic sound generator in Taito's arcade boards (with a variant of the OPNB being used in several arcade boards such as the Taito Z System board). The related OPN2 was used in Sega's Mega Drive (Genesis), Fujitsu's FM Towns Marty, and some of Sega's arcade boards (e.g. Sega System C-2 and Sega System 32) as one of its sound generator chips.

FM synthesis was also used on a wide range of mobile phones in the 2000s to play ringtones and other sounds, using the Yamaha SMAF format.

## History

### Don Buchla (mid-1960s)

Don Buchla implemented FM on his instruments in the mid-1960s, prior to Chowning's patent. His 158, 258 and 259 dual oscillator modules had a specific FM control voltage input, and the model 208 (Music Easel) had a modulation oscillator hard-wired to allow FM as well as AM of the primary oscillator. These early applications used analog oscillators, and this capability was also followed by other modular synthesizers and portable synthesizers including Minimoog and ARP Odyssey.

### John Chowning (late-1960s–1970s)

By the mid-20th century, frequency modulation (FM), a means of carrying sound, had been understood for decades and was being used to broadcast radio transmissions. FM synthesis was developed since 1967 at Stanford University, California, by John Chowning, through his exploration of digital synthesis and spatialization, inspired by the new possibilities of digital sound as described by Max Mathews. His algorithm was licensed to Japanese company Yamaha in 1973. The implementation commercialized by Yamaha (US Patent 4018121 Apr 1977 or U.S. Patent 4,018,121) is actually based on phase modulation, but the results end up being equivalent mathematically as both are essentially a special case of quadrature amplitude modulation.

### 1970s–1980s

#### Expansions by Yamaha

Yamaha's engineers began adapting Chowning's algorithm for use in a commercial digital synthesizer, adding improvements such as the "key scaling" method to avoid the introduction of "distortion that normally occurred in analog systems during frequency modulation", though it would take several years before Yamaha released their FM digital synthesizers. In the 1970s, Yamaha were granted a number of patents, under the company's former name "Nippon Gakki Seizo Kabushiki Kaisha", evolving Chowning's work. Yamaha built the first prototype FM digital synthesizer in 1974.

Yamaha eventually commercialized FM synthesis technology with the Yamaha GS-1, the first FM digital synthesizer, released in 1980. FM synthesis was the basis of some of the early generations of digital synthesizers, most notably those from Yamaha, as well as New England Digital Corporation under license from Yamaha. Yamaha's DX7 synthesizer, released in 1983, was ubiquitous throughout the 1980s.

Several other models by Yamaha provided variations and evolutions of FM synthesis during that decade; cheaper implementations of Yamaha's FM synthesis chips can be found in the consumer grade PortaSound/PortaTone series of home keyboards from the mid-1980s, occasionally featuring Yamaha FM chips from the low-cost OPL series (e.g. YM3812, YM2413).

Yamaha had patented its hardware implementation of FM in the 1970s, allowing it to nearly monopolize the market for FM technology until the mid-1990s.

Casio developed a related form of synthesis called phase distortion synthesis, used in its CZ range of synthesizers. It had a similar (but slightly differently derived) sound quality to the DX series.

### 1990s

#### Free use of FM synthesis after patent expiration

With the expiration of the Stanford University FM patent in 1995, digital FM synthesis can now be implemented freely by other manufacturers. The FM synthesis patent brought Stanford $20 million before it expired, making it (in 1994) "the second most lucrative licensing agreement in Stanford's history".

Today, FM is mostly found in software-based synths such as Native Instruments' FM8 or Image-Line's Sytrus plug-ins, but it has also been incorporated into the synthesis repertoire of some modern digital synthesizers, usually coexisting as an option alongside other methods of synthesis such as subtractive, sample-based synthesis, additive synthesis, and other techniques. The degree of complexity of the FM in such hardware synths may vary from simple 2-operator FM, to the highly flexible 6-operator engines of the Korg Kronos and Alesis Fusion, to creation of FM in extensively modular engines such as those in the latest synthesisers by Kurzweil Music Systems.

#### Later use of FM and other technologies: Realtime Convolution & Modulation (AFM + Sample) and Formant Shaping Synthesis

The Yamaha SY77, Yamaha SY99 and FS1R synthesizers marketed their highly powerful FM abilities as counterparts to sample-based synthesis and formant synthesis respectively. New hardware synths specifically marketed for their FM capabilities disappeared from the market after the release of FS1R in 1999, however, well-developed FM synthesis options are a feature of Nord Lead synths manufactured by Clavia, the Alesis Fusion range, the Korg Oasys and Kronos and the Modor NF-1. Various other synthesizers offer limited FM abilities to supplement their main engines.

The FS1R had 16 operators, 8 standard FM operators and 8 additional operators that used a noise source rather than an oscillator as its sound source. By adding in tuneable noise sources the FS1R could model the sounds produced in the human voice and in a wind instrument, along with making percussion instrument sounds. The FS1R also contained an additional wave form called the Formant wave form. Formants can be used to model resonating body instrument sounds like the cello, violin, acoustic guitar, bassoon, English horn, or human voice. Formants can even be found in the harmonic spectrum of several brass instruments.

### 2000s–present

#### Additional improvements: Variable Phase Modulation, FM-X Synthesis, Altered FM, etc.

In 2016, Korg released the Korg Volca FM, a, 3-voice, 6 operators FM iteration of the Korg Volca series of compact, affordable desktop modules. Korg has also released the opsix (2020) and opsix SE (2023), integrating 6 operators FM synthesis with subtractive, analogue modeling, additive, semi-modular and Waveshaping.

Yamaha released the Montage in 2016, which combines a 128-voice sample-based engine with a 128-voice FM engine. This iteration of FM is called FM-X, and features 8 operators; each operator has a choice of several basic wave forms, but each wave form has several parameters to adjust its spectrum. It was then followed by the more affordable Yamaha MODX in 2018, with 64-voice, 8 operators FM-X architecture in addition to a 128-voice sample-based engine. The MODX+ released in 2022 increased the number of voices of the FM-X engine to 128, the same as with the Montage. The Montage was succeeded by the Montage M in 2023, which uses the same 128-voice, 8 operators FM-X engine alongside a 128-voice sample-based engine and a newly introduced 16-voice 3 oscillator analog-based engine known as AN-X.

Elektron launched the Digitone in 2018, which is an 8-voice, 4 operators FM synth featuring Elektron's renowned sequence engine.

FM-X synthesis was first introduced with the Yamaha Montage synthesizers in 2016. FM-X uses 8 operators. Each FM-X operator has a set of multi-spectral wave forms to choose from, which means each FM-X operator can be equivalent to a stack of 3 or 4 DX7 FM operators. The list of selectable wave forms includes sine waves, the All1 and All2 wave forms, the Odd1 and Odd2 wave forms, and the Res1 and Res2 wave forms. The sine wave selection works the same as the DX7 wave forms. The All1 and All2 wave forms are a saw-tooth wave form. The Odd1 and Odd2 wave forms are pulse or square waves. These two types of wave forms can be used to model the basic harmonic peaks in the bottom of the harmonic spectrum of most instruments. The Res1 and Res2 wave forms move the spectral peak to a specific harmonic and can be used to model either triangular or rounded groups of harmonics further up in the spectrum of an instrument. Combining an All1 or Odd1 wave form with multiple Res1 (or Res2) wave forms (and adjusting their amplitudes) can model the harmonic spectrum of an instrument or sound.

Combining sets of 8 FM operators with multi-spectral wave forms was first introduced in the FS1R, released in 1999 by Yamaha. It was able to achieve similar results to that of FM-X using 8 noise operators.

## Spectral analysis

There are multiple variations of FM synthesis, including:

- Various operator arrangements (known as "FM Algorithms" in Yamaha terminology)
  - 2 operators
  - Serial FM (multiple stages)
  - Parallel FM (multiple modulators, multiple-carriers),
  - Mix of them
- Various waveform of operators
  - Sinusoidal waveform
  - Other waveforms
- Additional modulation
  - Linear FM
  - Exponential FM (preceded by the anti-logarithm conversion for CV/oct. interface of analog synthesizers)
  - Oscillator sync with FM

*etc*.

As the basic of these variations, we analyze the spectrum of 2 operators (linear FM synthesis using two sinusoidal operators) on the following.

### 2 operators

The spectrum generated by FM synthesis with one modulator is expressed as follows:

For modulation signal $m(t)=B\,\sin(\omega _{m}t)\,$ , the carrier signal is:

${\begin{aligned}FM(t)&\ =\ A\,\sin \left(\,\int _{0}^{t}\left(\omega _{c}+B\,\sin(\omega _{m}\,\tau )\right)d\tau \right)\\&\ =\ A\,\sin \left(\omega _{c}\,t-{\frac {B}{\omega _{m}}}\left(\cos(\omega _{m}\,t)-1\right)\right)\\&\ =\ A\,\sin \left(\omega _{c}\,t+{\frac {B}{\omega _{m}}}\left(\sin(\omega _{m}\,t-\pi /2)+1\right)\right)\\\end{aligned}}$

If we were to ignore the constant phase terms on the carrier $\phi _{c}=B/\omega _{m}\,$ and the modulator $\phi _{m}=-\pi /2\,$ , finally we would get the following expression, as seen on Chowning 1973 and Roads 1996, p. 232:

${\begin{aligned}FM(t)&\ \approx \ A\,\sin \left(\omega _{c}\,t+\beta \,\sin(\omega _{m}\,t)\right)\\&\ =\ A\left(J_{0}(\beta )\sin(\omega _{c}\,t)+\sum _{n=1}^{\infty }J_{n}(\beta )\left[\,\sin((\omega _{c}+n\,\omega _{m})\,t)\ +\ (-1)^{n}\sin((\omega _{c}-n\,\omega _{m})\,t)\,\right]\right)\\&\ =\ A\sum _{n=-\infty }^{\infty }J_{n}(\beta )\,\sin((\omega _{c}+n\,\omega _{m})\,t)\end{aligned}}$

where $\omega _{c}\,,\,\omega _{m}\,$ are angular frequencies ( $\,\omega =2\pi f\,$ ) of carrier and modulator, $\beta =B/\omega _{m}\,$ is frequency modulation index, and amplitudes $J_{n}(\beta )\,$ is $n\,$ -th Bessel function of first kind, respectively.
