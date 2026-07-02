---
title: "Reverberation"
source: https://en.wikipedia.org/wiki/Reverberation
domain: audio-reverb-algorithms
license: CC-BY-SA-4.0
tags: audio reverb algorithm, artificial reverberation, comb filter reverb, reverberation dsp
fetched: 2026-07-02
---

# Reverberation

In acoustics, **reverberation** (commonly shortened to **reverb**) is a persistence of sound after it is produced. It is often created when a sound is reflected on surfaces, causing multiple reflections that build up and then decay as the sound is absorbed by the surfaces of objects in the space – which could include furniture, people, and air. This is most noticeable when the sound source stops but the reflections continue, their amplitude decreasing, until zero is reached.

Reverberation is frequency dependent: the length of the decay, or reverberation time, receives special consideration in the architectural design of spaces which need to have specific reverberation times to achieve optimum performance for their intended activity. In comparison to a distinct echo, that is detectable at a minimum of 50 to 100 ms after the previous sound, reverberation is the occurrence of reflections that arrive in a sequence of less than approximately 50 ms. As time passes, the amplitude of the reflections gradually reduces to non-noticeable levels. Reverberation is not limited to indoor spaces as it exists in forests and other outdoor environments where reflection exists.

Reverberation occurs naturally when a person sings, talks, or plays an instrument acoustically in a hall or performance space with sound-reflective surfaces. Reverberation is applied artificially by using reverb effects, which simulate reverb through means including echo chambers, vibrations sent through metal, and digital processing.

Although reverberation can add naturalness to recorded sound by adding a sense of space, it can also reduce speech intelligibility, especially when noise is also present. People with hearing loss, including users of hearing aids, frequently report difficulty in understanding speech in reverberant, noisy situations. Reverberation is also a significant source of mistakes in automatic speech recognition.

*Dereverberation* is the process of reducing the level of reverberation in a sound or signal.

## Reverberation time

**Reverberation time** is a measure of the time required for the sound to "fade away" in an enclosed area after the source of the sound has stopped.

When it comes to accurately measuring reverberation time with a meter, the term *T60* (an abbreviation for reverberation time 60 dB) is used. T60 provides an objective reverberation time measurement. It is defined as the time it takes for the sound pressure level to reduce by 60 dB, measured after the generated test signal is abruptly ended.

Reverberation time is frequently stated as a single value if measured as a wideband signal (20 Hz to 20 kHz). However, being frequency-dependent, it can be more precisely described in terms of frequency bands (one octave, 1/3 octave, 1/6 octave, etc.). Being frequency dependent, the reverberation time measured in narrow bands will differ depending on the frequency band being measured. For precision, it is important to know what ranges of frequencies are being described by a reverberation time measurement.

In the late 19th century, Wallace Clement Sabine started experiments at Harvard University to investigate the impact of absorption on the reverberation time. Using a portable wind chest and organ pipes as a sound source, a stopwatch and his ears, he measured the time from interruption of the source to inaudibility (a difference of roughly 60 dB). He found that the reverberation time is proportional to room dimensions and inversely proportional to the amount of absorption present.

The optimum reverberation time for a space in which music is played depends on the type of music that is to be played in the space. Rooms used for speech typically need a shorter reverberation time so that speech can be understood more clearly. If the reflected sound from one syllable is still heard when the next syllable is spoken, it may be difficult to understand what was said. "Cat", "cab", and "cap" may all sound very similar. If on the other hand the reverberation time is too short, tonal balance and loudness may suffer. Reverberation effects are often used in studios to add depth to sounds. Reverberation changes the perceived spectral structure of a sound but does not alter the pitch.

Basic factors that affect a room's reverberation time include the size and shape of the enclosure as well as the materials used in the construction of the room. Every object placed within the enclosure can also affect this reverberation time, including people and their belongings.

### Measurement

Historically, reverberation time could only be measured using a level recorder (a plotting device which graphs the noise level against time on a ribbon of moving paper). A loud noise is produced, and as the sound dies away the trace on the level recorder will show a distinct slope. Analysis of this slope reveals the measured reverberation time. Some modern digital sound level meters can carry out this analysis automatically.

Several methods exist for measuring reverberation time. An impulse can be measured by creating a sufficiently loud noise (which must have a defined cut-off point). Impulse noise sources such as a blank pistol shot or balloon burst may be used to measure the impulse response of a room.

Alternatively, a random noise signal such as pink noise or white noise may be generated through a loudspeaker, and then turned off. This is known as the interrupted method, and the measured result is known as the interrupted response.

A two-port measurement system can also be used to measure noise introduced into a space and compare it to what is subsequently measured in the space. Consider sound reproduced by a loudspeaker into a room. A recording of the sound in the room can be made and compared to what was sent to the loudspeaker. The two signals can be compared mathematically. This two port measurement system uses a Fourier transform to mathematically derive the impulse response of the room. From the impulse response, the reverberation time can be calculated. Using a two-port system allows reverberation time to be measured with signals other than loud impulses. Music or recordings of other sounds can be used. This allows measurements to be taken in a room after the audience is present.

Under some restrictions, even simple sound sources like handclaps can be used for measurement of reverberation

Reverberation time is usually stated as a decay time and is measured in seconds. There may or may not be any statement of the frequency band used in the measurement. Decay time is the time it takes the signal to diminish 60 dB below the original sound. It is often difficult to inject enough sound into the room to measure a decay of 60 dB, particularly at lower frequencies. If the decay is linear, it is sufficient to measure a drop of 20 dB and multiply the time by 3, or a drop of 30 dB and multiply the time by 2. These are the so-called T20 and T30 measurement methods.

The RT60 reverberation time measurement is defined in the ISO 3382-1 standard for performance spaces, the ISO 3382-2 standard for ordinary rooms, and the ISO 3382-3 for open-plan offices, as well as the ASTM E2235 standard.

The concept of reverberation time implicitly supposes that the decay rate of the sound is exponential, so that the sound level diminishes regularly, at a rate of so many dB per second. It is not often the case in real rooms, depending on the disposition of reflective, dispersive and absorbing surfaces. Moreover, successive measurement of the sound level often yields very different results, as differences in phase in the exciting sound build up in notably different sound waves. In 1965, Manfred R. Schroeder published "A new method of Measuring Reverberation Time" in the *Journal of the Acoustical Society of America*. He proposed to measure, not the power of the sound, but the energy, by integrating it. This made it possible to show the variation in the rate of decay and to free acousticians from the necessity of averaging many measurements.

### Sabine equation

Sabine's reverberation equation was developed in the late 1890s in an empirical fashion. He established a relationship between the *T*60 of a room, its volume, and its total absorption (in sabins). This is given by the equation:

$T_{60}={\frac {24\ln 10^{1}}{c_{20}}}{\frac {V}{Sa}}\approx 0.1611\,\mathrm {s} \mathrm {m} ^{-1}{\frac {V}{Sa}}$

.

where *c*20 is the speed of sound in the room (at 20 °C), *V* is the volume of the room in m3, *S* total surface area of room in m2, *a* is the average absorption coefficient of room surfaces, and the product *Sa* is the total absorption in sabins.

The total absorption in sabins (and hence reverberation time) generally changes depending on frequency (which is defined by the acoustic properties of the space). The equation does not take into account room shape or losses from the sound traveling through the air (important in larger spaces). Most rooms absorb less sound energy in the lower frequency ranges resulting in longer reverb times at lower frequencies.

Sabine concluded that the reverberation time depends upon the reflectivity of sound from various surfaces available inside the hall. If the reflection is coherent, the reverberation time of the hall will be longer; the sound will take more time to die out.

The reverberation time *RT*60 and the volume *V* of the room have great influence on the critical distance *d*c (conditional equation):

$d_{\mathrm {c} }\approx 0{.}057\cdot {\sqrt {\frac {V}{RT_{60}}}}$

where critical distance $d_{c}$ is measured in meters, volume V is measured in m³, and reverberation time *RT*60 is measured in seconds.

### Eyring equation

Eyring's reverberation time equation was proposed by Carl F. Eyring of Bell Labs in 1930. This equation aims to better estimate the reverberation time in small rooms with relatively large quantities of sound absorption, identified by Eyring as "dead" rooms. These rooms tend to have lower reverberation times than larger, more acoustically live rooms. Eyring's equation is similar in form to Sabine's equation, but includes modifications to logarithmically scale the absorption term. The units and variables within the equation are the same as those defined for Sabine's equation. The Eyring reverberation time is given by the equation:

$T_{60}\approx -0.161\ {\frac {V}{S\ln(1-a)}}$

.

Eyring's equation was developed from first principles using an image source model of sound reflection, as opposed to Sabine's empirical approach. The experimental results obtained by Sabine generally agree with Eyring's equation since the two formulae become identical for very live rooms, the type in which Sabine worked. However, Eyring's equation becomes more valid for smaller rooms with large quantities of absorption. As a result, the Eyring equation is often implemented to estimate the reverberation time in recording studio control rooms or other critical listening environments with high quantities of sound absorption. The Sabine equation tends to over-predict reverberation time for small rooms with high amounts of absorption. For this reason, reverberation time calculators available for smaller recording studio environments, such as home recording studios, often use Eyring's equation.

### Absorption coefficient

The absorption coefficient of a material is a number between 0 and 1 which indicates the proportion of sound which is absorbed by the surface compared to the proportion which is reflected back to the room. A large, fully open window would offer no reflection as any sound reaching it would pass straight out and no sound would be reflected. This would have an absorption coefficient of 1. Conversely, a thick, smooth painted concrete ceiling would be the acoustic equivalent of a mirror and have an absorption coefficient very close to 0.

Absorption coefficients are frequency-dependent and are typically reported at the standard octave band centre frequencies of 125, 250, 500, 1000, 2000, and 4000 Hz. A single-number rating called the weighted sound absorption coefficient (*α*w) can be derived from the frequency-dependent values according to ISO 11654.

The standard laboratory method for measuring absorption coefficients is ISO 354, which uses a reverberation room and determines the random-incidence absorption coefficient from the change in reverberation time after placing a test specimen in the room. An alternative method using an impedance tube (ISO 10534-2) measures the normal-incidence absorption coefficient for small material samples. Values measured in a reverberation room can exceed 1.0 because edge diffraction effects increase the effective absorbing area beyond the physical dimensions of the specimen.

## In music

*The Atlantic* described reverberation as "arguably the oldest and most universal sound effect in music", used in music as early as 10th-century plainsong.

Gregorian chant may have developed in response to the long reverberation time of cathedrals, limiting the number of notes that could be sung before blending chaotically.

Artificial reverberation is applied to sound using reverb effects. These simulate reverb through means including echo chambers, vibrations sent through metal, and digital processing.
