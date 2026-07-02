---
title: "Additive synthesis"
source: https://en.wikipedia.org/wiki/Additive_synthesis
domain: audio-synthesis
license: CC-BY-SA-4.0
tags: sound synthesis, subtractive synthesis, fm synthesis, wavetable synthesis
fetched: 2026-07-02
---

# Additive synthesis

**Additive synthesis** is a sound synthesis technique that creates timbre by adding sine waves together.

The timbre of musical instruments can be considered in the light of Fourier theory to consist of multiple harmonic or inharmonic *partials* or overtones. Each partial is a sine wave of different frequency and amplitude that swells and decays over time due to modulation from an ADSR envelope or low-frequency oscillator.

Additive synthesis most directly generates sound by adding the output of multiple sine wave generators. Alternative implementations may use pre-computed wavetables or the inverse fast Fourier transform.

## Explanation

The sounds that are heard in everyday life are not characterized by a single frequency. Instead, they consist of a sum of pure sine frequencies, each one at a different amplitude. When humans hear these frequencies simultaneously, we can recognize the sound. This is true for both "non-musical" sounds (e.g. water splashing, leaves rustling, etc.) and for "musical sounds" (e.g. a piano note, a bird's tweet, etc.). This set of parameters (frequencies, their relative amplitudes, and how the relative amplitudes change over time) are encapsulated by the *timbre* of the sound. Fourier analysis is the technique that is used to determine these exact timbre parameters from an overall sound signal; conversely, the resulting set of frequencies and amplitudes is called the Fourier series of the original sound signal.

In the case of a musical note, the lowest frequency of its timbre is designated as the sound's fundamental frequency. For simplicity, we often say that the note is playing at that fundamental frequency (e.g. "middle C is 261.6 Hz"), even though the sound of that note consists of many other frequencies as well. The set of the remaining frequencies is called the overtones (or the harmonics, if their frequencies are integer multiples of the fundamental frequency) of the sound. In other words, the fundamental frequency alone is responsible for the pitch of the note, while the overtones define the timbre of the sound. The overtones of a piano playing middle C will be quite different from the overtones of a violin playing the same note; that's what allows us to differentiate the sounds of the two instruments. There are even subtle differences in timbre between different versions of the same instrument (for example, an upright piano vs. a grand piano).

Additive synthesis aims to exploit this property of sound in order to construct timbre from the ground up. By adding together pure frequencies (sine waves) of varying frequencies and amplitudes, we can precisely define the timbre of the sound that we want to create.

## Definitions

Harmonic additive synthesis is closely related to the concept of a Fourier series which is a way of expressing a periodic function as the sum of sinusoidal functions with frequencies equal to integer multiples of a common fundamental frequency. These sinusoids are called harmonics, overtones, or generally, partials. In general, a Fourier series contains an infinite number of sinusoidal components, with no upper limit to the frequency of the sinusoidal functions and includes a DC component (one with frequency of 0 Hz). Frequencies outside of the human audible range can be omitted in additive synthesis. As a result, only a finite number of sinusoidal terms with frequencies that lie within the audible range are modeled in additive synthesis.

A waveform or function is said to be periodic if

$y(t)=y(t+P)$

for all t and for some period P .

The Fourier series of a periodic function is mathematically expressed as:

${\begin{aligned}y(t)&={\frac {a_{0}}{2}}+\sum _{k=1}^{\infty }\left[a_{k}\cos(2\pi kf_{0}t)-b_{k}\sin(2\pi kf_{0}t)\right]\\&={\frac {a_{0}}{2}}+\sum _{k=1}^{\infty }r_{k}\cos \left(2\pi kf_{0}t+\phi _{k}\right)\\\end{aligned}}$

where

- $f_{0}=1/P$ is the fundamental frequency of the waveform and is equal to the reciprocal of the period,
- $a_{k}=r_{k}\cos(\phi _{k})=2f_{0}\int _{0}^{P}y(t)\cos(2\pi kf_{0}t)\,dt,\quad k\geq 0$
- $b_{k}=r_{k}\sin(\phi _{k})=-2f_{0}\int _{0}^{P}y(t)\sin(2\pi kf_{0}t)\,dt,\quad k\geq 1$
- $r_{k}={\sqrt {a_{k}^{2}+b_{k}^{2}}}$ is the amplitude of the k th harmonic,
- $\phi _{k}=\operatorname {atan2} (b_{k},a_{k})$ is the phase offset of the k th harmonic. atan2 is the four-quadrant arctangent function,

Being inaudible, the DC component, $a_{0}/2$ , and all components with frequencies higher than some finite limit, $Kf_{0}$ , are omitted in the following expressions of additive synthesis.

### Harmonic form

The simplest harmonic additive synthesis can be mathematically expressed as:

| $y(t)=\sum _{k=1}^{K}r_{k}\cos \left(2\pi kf_{0}t+\phi _{k}\right),$ |   | 1 |
|---|---|---|

where $y(t)$ is the synthesis output, $r_{k}$ , $kf_{0}$ , and $\phi _{k}$ are the amplitude, frequency, and the phase offset, respectively, of the k th harmonic partial of a total of K harmonic partials, and $f_{0}$ is the fundamental frequency of the waveform and the frequency of the musical note.

### Time-dependent amplitudes

|   | Example of harmonic additive synthesis in which each harmonic has a time-dependent amplitude. The fundamental frequency is 440 Hz. Problems listening to this file? See Media help |
|---|---|

More generally, the amplitude of each harmonic can be prescribed as a function of time, $r_{k}(t)$ , in which case the synthesis output is

| $y(t)=\sum _{k=1}^{K}r_{k}(t)\cos \left(2\pi kf_{0}t+\phi _{k}\right)$ . |   | 2 |
|---|---|---|

Each envelope $r_{k}(t)\,$ should vary slowly relative to the frequency spacing between adjacent sinusoids. The bandwidth of $r_{k}(t)$ should be significantly less than $f_{0}$ .

### Inharmonic form

Additive synthesis can also produce inharmonic sounds (which are aperiodic waveforms) in which the individual overtones need not have frequencies that are integer multiples of some common fundamental frequency. While many conventional musical instruments have harmonic partials (e.g. an oboe), some have inharmonic partials (e.g. bells). Inharmonic additive synthesis can be described as

$y(t)=\sum _{k=1}^{K}r_{k}(t)\cos \left(2\pi f_{k}t+\phi _{k}\right),$

where $f_{k}$ is the constant frequency of k th partial.

|   | Example of inharmonic additive synthesis in which both the amplitude and frequency of each partial are time-dependent. Problems listening to this file? See Media help |
|---|---|

### Time-dependent frequencies

In the general case, the instantaneous frequency of a sinusoid is the derivative (with respect to time) of the argument of the sine or cosine function. If this frequency is represented in hertz, rather than in angular frequency form, then this derivative is divided by $2\pi$ . This is the case whether the partial is harmonic or inharmonic and whether its frequency is constant or time-varying.

In the most general form, the frequency of each non-harmonic partial is a non-negative function of time, $f_{k}(t)$ , yielding

| $y(t)=\sum _{k=1}^{K}r_{k}(t)\cos \left(2\pi \int _{0}^{t}f_{k}(u)\ du+\phi _{k}\right).$ |   | 3 |
|---|---|---|

### Broader definitions

*Additive synthesis* more broadly may mean sound synthesis techniques that sum simple elements to create more complex timbres, even when the elements are not sine waves. For example, F. Richard Moore listed additive synthesis as one of the "four basic categories" of sound synthesis alongside subtractive synthesis, nonlinear synthesis, and physical modeling. In this broad sense, pipe organs, which also have pipes producing non-sinusoidal waveforms, can be considered as a variant form of additive synthesizers. Summation of principal components and Walsh functions have also been classified as additive synthesis.

## Implementation methods

Modern-day implementations of additive synthesis are mainly digital. (See section *Discrete-time equations* for the underlying discrete-time theory)

### Oscillator bank synthesis

Additive synthesis can be implemented using a bank of sinusoidal oscillators, one for each partial.

### Wavetable synthesis

In the case of harmonic, quasi-periodic musical tones, wavetable synthesis can be as general as time-varying additive synthesis, but requires less computation during synthesis. As a result, an efficient implementation of time-varying additive synthesis of harmonic tones can be accomplished by use of *wavetable synthesis*.

#### Group additive synthesis

Group additive synthesis is a method to group partials into harmonic groups (having different fundamental frequencies) and synthesize each group separately with *wavetable synthesis* before mixing the results.

### Inverse FFT synthesis

An inverse fast Fourier transform can be used to efficiently synthesize frequencies that evenly divide the transform period or "frame". By careful consideration of the DFT frequency-domain representation it is also possible to efficiently synthesize sinusoids of arbitrary frequencies using a series of overlapping frames and the inverse fast Fourier transform.

## Additive analysis/resynthesis

It is possible to analyze the frequency components of a recorded sound giving a "sum of sinusoids" representation. This representation can be re-synthesized using additive synthesis. One method of decomposing a sound into time varying sinusoidal partials is short-time Fourier transform (STFT)-based McAulay-Quatieri Analysis.

By modifying the sum of sinusoids representation, timbral alterations can be made prior to resynthesis. For example, a harmonic sound could be restructured to sound inharmonic, and vice versa. Sound hybridisation or "morphing" has been implemented by additive resynthesis.

Additive analysis/resynthesis has been employed in a number of techniques including Sinusoidal Modelling, Spectral Modelling Synthesis (SMS), and the Reassigned Bandwidth-Enhanced Additive Sound Model. Software that implements additive analysis/resynthesis includes: SPEAR, LEMUR, LORIS, SMSTools, ARSS.

### Products

Additive re-synthesis using timbre-frame concatenation:

Concatenation with crossfades (on Synclavier)

Concatenation with spectral envelope interpolation (on Vocaloid)

New England Digital Synclavier had a resynthesis feature where samples could be analyzed and converted into "timbre frames" which were part of its additive synthesis engine. Technos Acxel, launched in 1987, utilized the additive analysis/resynthesis model, in an FFT implementation.

Also a vocal synthesizer, Vocaloid have been implemented on the basis of additive analysis/resynthesis: its spectral voice model called Excitation plus Resonances (EpR) model is extended based on Spectral Modeling Synthesis (SMS), and its diphone concatenative synthesis is processed using *spectral peak processing* (SPP) technique similar to modified phase-locked vocoder (an improved phase vocoder for formant processing). Using these techniques, spectral components (*formants*) consisting of purely harmonic partials can be appropriately transformed into desired form for sound modeling, and sequence of short samples (*diphones* or *phonemes*) constituting desired phrase, can be smoothly connected by interpolating matched partials and formant peaks, respectively, in the inserted transition region between different samples. (See also Dynamic timbres)

## Applications

### Musical instruments

Additive synthesis is used in electronic musical instruments. It is the principal sound generation technique used by Eminent organs.

### Speech synthesis

In linguistics research, harmonic additive synthesis was used in the 1950s to play back modified and synthetic speech spectrograms.

Later, in the early 1980s, listening tests were carried out on synthetic speech stripped of acoustic cues to assess their significance. Time-varying formant frequencies and amplitudes derived by linear predictive coding were synthesized additively as pure tone whistles. This method is called sinewave synthesis. Also the composite sinusoidal modeling (CSM) used on a singing speech synthesis feature on the Yamaha CX5M (1984), is known to use a similar approach which was independently developed during 1966–1979. These methods are characterized by extraction and recomposition of a set of significant spectral peaks corresponding to the several resonance modes occurring in the oral cavity and nasal cavity, in a viewpoint of acoustics. This principle was also utilized on a physical modeling synthesis method, called modal synthesis.

## History

Lord Kelvin

's

Tide-predicting machine

Harmonic synthesizer

Harmonic analyzer

Harmonic analysis was discovered by Joseph Fourier, who published an extensive treatise of his research in the context of heat transfer in 1822. The theory found an early application in prediction of tides. Around 1876, William Thomson (later ennobled as Lord Kelvin) constructed a mechanical tide predictor. It consisted of a *harmonic analyzer* and a *harmonic synthesizer*, as they were called already in the 19th century. The analysis of tide measurements was done using James Thomson's *integrating machine*. The resulting Fourier coefficients were input into the synthesizer, which then used a system of cords and pulleys to generate and sum harmonic sinusoidal partials for prediction of future tides. In 1910, a similar machine was built for the analysis of periodic waveforms of sound. The synthesizer drew a graph of the combination waveform, which was used chiefly for visual validation of the analysis.

Helmholtz resonator

Tone-generator utilizing it

Georg Ohm applied Fourier's theory to sound in 1843. The line of work was greatly advanced by Hermann von Helmholtz, who published his eight years worth of research in 1863. Helmholtz believed that the psychological perception of tone color is subject to learning, while hearing in the sensory sense is purely physiological. He supported the idea that perception of sound derives from signals from nerve cells of the basilar membrane and that the elastic appendages of these cells are sympathetically vibrated by pure sinusoidal tones of appropriate frequencies. Helmholtz agreed with the finding of Ernst Chladni from 1787 that certain sound sources have inharmonic vibration modes.

Rudolph Koenig

's sound analyzer and synthesizer

sound synthesizer

sound analyzer

In Helmholtz's time, electronic amplification was unavailable. For synthesis of tones with harmonic partials, Helmholtz built an electrically excited array of tuning forks and acoustic resonance chambers that allowed adjustment of the amplitudes of the partials. Built at least as early as in 1862, these were in turn refined by Rudolph Koenig, who demonstrated his own setup in 1872. For harmonic synthesis, Koenig also built a large apparatus based on his *wave siren*. It was pneumatic and utilized cut-out tonewheels, and was criticized for low purity of its partial tones. Also tibia pipes of pipe organs have nearly sinusoidal waveforms and can be combined in the manner of additive synthesis.

In 1938, with significant new supporting evidence, it was reported on the pages of Popular Science Monthly that the human vocal cords function like a fire siren to produce a harmonic-rich tone, which is then filtered by the vocal tract to produce different vowel tones. By the time, the additive Hammond organ was already on market. Most early electronic organ makers thought it too expensive to manufacture the plurality of oscillators required by additive organs, and began instead to build subtractive ones. In a 1940 Institute of Radio Engineers meeting, the head field engineer of Hammond elaborated on the company's new *Novachord* as having a *"subtractive system"* in contrast to the original Hammond organ in which *"the final tones were built up by combining sound waves"*. Alan Douglas used the qualifiers *additive* and *subtractive* to describe different types of electronic organs in a 1948 paper presented to the Royal Musical Association. The contemporary wording *additive synthesis* and *subtractive synthesis* can be found in his 1957 book *The electrical production of music*, in which he categorically lists three methods of forming of musical tone-colours, in sections titled *Additive synthesis*, *Subtractive synthesis*, and *Other forms of combinations*.

A typical modern additive synthesizer produces its output as an electrical, analog signal, or as digital audio, such as in the case of software synthesizers, which became popular around year 2000.

### Timeline

The following is a timeline of historically and technologically notable analog and digital synthesizers and devices implementing additive synthesis.

| Research implementation or publication | Commercially available | Company or institution | Synthesizer or synthesis device | Description | Audio samples |
|---|---|---|---|---|---|
| 1900 | 1906 | New England Electric Music Company | Telharmonium | The first polyphonic, touch-sensitive music synthesizer. Implemented sinuosoidal additive synthesis using tonewheels and alternators. Invented by Thaddeus Cahill. | *no known recordings* |
| 1933 | 1935 | Hammond Organ Company | Hammond Organ | An electronic additive synthesizer that was commercially more successful than Telharmonium. Implemented sinusoidal additive synthesis using tonewheels and magnetic pickups. Invented by Laurens Hammond. | Model Aⓘ |
| 1950 or earlier |   | Haskins Laboratories | Pattern Playback | A speech synthesis system that controlled amplitudes of harmonic partials by a spectrogram that was either hand-drawn or an analysis result. The partials were generated by a multi-track optical tonewheel. | samples Archived 25 January 2012 at the Wayback Machine |
| 1958 |   |   | ANS | An additive synthesizer that played microtonal spectrogram-like scores using multiple multi-track optical tonewheels. Invented by Evgeny Murzin. A similar instrument that utilized electronic oscillators, the *Oscillator Bank*, and its input device *Spectrogram* were realized by Hugh Le Caine in 1959. | 1964 modelⓘ |
| 1963 |   | MIT |   | An off-line system for digital spectral analysis and resynthesis of the attack and steady-state portions of musical instrument timbres by David Luce. |   |
| 1964 |   | University of Illinois | Harmonic Tone Generator | An electronic, harmonic additive synthesis system invented by James Beauchamp. | samples (info) |
| 1974 or earlier | 1974 | RMI | Harmonic Synthesizer | The first synthesizer product that implemented additive synthesis using digital oscillators. The synthesizer also had a time-varying analog filter. RMI was a subsidiary of Allen Organ Company, which had released the first commercial digital church organ, the *Allen Computer Organ*, in 1971, using digital technology developed by North American Rockwell. | 1 2 3 4 |
| 1974 |   | EMS (London) | Digital Oscillator Bank | A bank of digital oscillators with arbitrary waveforms, individual frequency and amplitude controls, intended for use in analysis-resynthesis with the digital *Analysing Filter Bank* (AFB) also constructed at EMS. Also known as: *DOB*. | in The New Sound of Music |
| 1976 | 1976 | Fairlight | Qasar M8 | An all-digital synthesizer that used the fast Fourier transform to create samples from interactively drawn amplitude envelopes of harmonics. | samples |
| 1977 |   | Bell Labs | Digital Synthesizer | A real-time, digital additive synthesizer that has been called the first true digital synthesizer. Also known as: *Alles Machine*, *Alice*. | sample Archived 26 July 2011 at the Wayback Machine (info Archived 24 August 2011 at the Wayback Machine) |
| 1979 | 1979 | New England Digital | Synclavier II | A commercial digital synthesizer that enabled development of timbre over time by smooth cross-fades between waveforms generated by additive synthesis. | Jon Appleton - Sashasonjonⓘ |
|   | 1996 | Kawai | K5000 | A commercial digital synthesizer workstation capable of polyphonic, digital additive synthesis of up to 128 sinusodial waves, as well as combing PCM waves. |   |

## Discrete-time equations

In digital implementations of additive synthesis, discrete-time equations are used in place of the continuous-time synthesis equations. A notational convention for discrete-time signals uses brackets i.e. $y[n]\,$ and the argument $n\,$ can only be integer values. If the continuous-time synthesis output $y(t)\,$ is expected to be sufficiently bandlimited; below half the sampling rate or $f_{\mathrm {s} }/2\,$ , it suffices to directly sample the continuous-time expression to get the discrete synthesis equation. The continuous synthesis output can later be reconstructed from the samples using a digital-to-analog converter. The sampling period is $T=1/f_{\mathrm {s} }\,$ .

Beginning with (**3**),

$y(t)=\sum _{k=1}^{K}r_{k}(t)\cos \left(2\pi \int _{0}^{t}f_{k}(u)\ du+\phi _{k}\right)$

and sampling at discrete times $t=nT=n/f_{\mathrm {s} }\,$ results in

${\begin{aligned}y[n]&=y(nT)=\sum _{k=1}^{K}r_{k}(nT)\cos \left(2\pi \int _{0}^{nT}f_{k}(u)\ du+\phi _{k}\right)\\&=\sum _{k=1}^{K}r_{k}(nT)\cos \left(2\pi \sum _{i=1}^{n}\int _{(i-1)T}^{iT}f_{k}(u)\ du+\phi _{k}\right)\\&=\sum _{k=1}^{K}r_{k}(nT)\cos \left(2\pi \sum _{i=1}^{n}(Tf_{k}[i])+\phi _{k}\right)\\&=\sum _{k=1}^{K}r_{k}[n]\cos \left({\frac {2\pi }{f_{\mathrm {s} }}}\sum _{i=1}^{n}f_{k}[i]+\phi _{k}\right)\\\end{aligned}}$

where

$r_{k}[n]=r_{k}(nT)\,$

is the discrete-time varying amplitude envelope

$f_{k}[n]={\frac {1}{T}}\int _{(n-1)T}^{nT}f_{k}(t)\ dt\,$

is the discrete-time

backward difference

instantaneous frequency.

This is equivalent to

$y[n]=\sum _{k=1}^{K}r_{k}[n]\cos \left(\theta _{k}[n]\right)$

where

${\begin{aligned}\theta _{k}[n]&={\frac {2\pi }{f_{\mathrm {s} }}}\sum _{i=1}^{n}f_{k}[i]+\phi _{k}\\&=\theta _{k}[n-1]+{\frac {2\pi }{f_{\mathrm {s} }}}f_{k}[n]\\\end{aligned}}$

for all

$n>0\,$

and

$\theta _{k}[0]=\phi _{k}.\,$
