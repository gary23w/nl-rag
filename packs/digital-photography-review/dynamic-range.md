---
title: "Dynamic range"
source: https://en.wikipedia.org/wiki/Dynamic_range
domain: digital-photography-review
license: CC-BY-SA-4.0
tags: digital photography review
fetched: 2026-07-03
---

# Dynamic range

**Dynamic range** (abbreviated **DR**, **DNR**, or **DYR**) is the ratio between the largest and smallest measurable values of a specific quantity. It is often used in the context of signals, like sound and light. It is measured either as a ratio or as a base-10 (decibel) or base-2 (doublings, bits or stops) logarithmic value of the ratio between the largest and smallest signal values.

Electronically reproduced audio and video is often processed to fit the original material with a wide dynamic range into a narrower recorded dynamic range for easier storage and reproduction. This process is called dynamic range compression.

## Human perception

| Factor (power) | Decibels (10×log10 power) | Stops (log2 power) |
|---|---|---|
| **1** | **0** | **0** |
| **2** | 3.01 | **1** |
| 3.16 | **5** | 1.66 |
| **4** | 6.02 | **2** |
| **5** | 6.99 | 2.32 |
| **8** | 9.03 | **3** |
| **10** | **10** | 3.32 |
| **16** | 12.0 | **4** |
| **20** | 13.0 | 4.32 |
| 31.6 | **15** | 4.98 |
| **32** | 15.1 | **5** |
| **50** | 17.0 | 5.64 |
| **100** | **20** | 6.64 |
| **1,000** | **30** | 9.97 |
| **1,024** | 30.1 | **10** |
| **10,000** | **40** | 13.3 |
| **100,000** | **50** | 16.6 |
| **1,000,000** | **60** | 19.9 |
| **1,048,576** | 60.2 | **20** |
| **100,000,000** | **80** | 26.6 |
| **1,073,741,824** | 90.3 | **30** |
| **10,000,000,000** | **100** | 33.2 |

The human senses of sight and hearing have a relatively high dynamic range. However, a human cannot perform these feats of perception at both extremes of the scale at the same time. The human eye takes time to adjust to different light levels, and its dynamic range in a given scene is actually quite limited due to optical glare. The instantaneous dynamic range of human audio perception is similarly subject to masking so that, for example, a whisper cannot be heard in loud surroundings.

A human is capable of hearing (and usefully discerning) anything from a quiet murmur in a soundproofed room to the loudest heavy metal concert. Such a difference can exceed 100 dB which represents a factor of 100,000 in amplitude and a factor of 10,000,000,000 in power. The dynamic range of human hearing is roughly 140 dB, varying with frequency, from the threshold of hearing (around −9 dB SPL at 3 kHz) to the threshold of pain (from 120 to 140 dB SPL). This wide dynamic range cannot be perceived all at once, however; the tensor tympani, stapedius muscle, and outer hair cells all act as mechanical dynamic range compressors to adjust the sensitivity of the ear to different ambient levels.

A human can see objects in starlight or in bright sunlight, even though on a moonless night objects receive one billionth (10−9) of the illumination they would on a bright sunny day; a dynamic range of 90 dB. Change of sensitivity is achieved in part through adjustments of the iris and slow chemical changes, which take some time.

In practice, it is difficult for humans to achieve the full dynamic experience using electronic equipment. For example, a good quality liquid-crystal display (LCD) has a dynamic range limited to around 1000:1, and some of the latest CMOS image sensors as of May 2010 have measured dynamic ranges of about 23,000:1. Paper reflectance can produce a dynamic range of about 100:1. A professional video camera such as the Sony Digital Betacam achieves a dynamic range of greater than 90 dB in audio recording.

## Audio

Audio engineers use *dynamic range* to describe the ratio of the amplitude of the loudest possible undistorted signal to the noise floor, say of a microphone or loudspeaker. Dynamic range is therefore the signal-to-noise ratio (SNR) for the case where the signal is the loudest possible for the system. For example, if the ceiling of a device is 5 V (rms) and the noise floor is 10 μV (rms) then the dynamic range is 500000:1, or 114 dB:

$20\times \log _{10}\left({\frac {\rm {5\,V}}{10\,\mu \mathrm {V} }}\right)=20\times \log _{10}(500000)=20\times 5.7=114\,\mathrm {dB}$

In digital audio theory the dynamic range is limited by quantization error. The maximum achievable dynamic range for a digital audio system with *Q*-bit uniform quantization is calculated as the ratio of the largest sine-wave rms to rms noise is:

$\mathrm {DR_{ADC}} =20\times \log _{10}\left({\frac {2^{Q}}{1}}\right)=\left(6.02\cdot Q\right)\ \mathrm {dB} \,\!$

However, the usable dynamic range may be greater, as a properly dithered recording device can record signals well below the noise floor.

The 16-bit compact disc has a theoretical undithered dynamic range of about 96 dB; however, the *perceived* dynamic range of 16-bit audio can be 120 dB or more with noise-shaped dither, taking advantage of the frequency response of the human ear.

Digital audio with undithered 20-bit quantization is theoretically capable of 120 dB dynamic range, while 24-bit digital audio affords 144 dB dynamic range. Most Digital audio workstations process audio with 32-bit floating-point representation which affords even higher dynamic range and so loss of dynamic range is no longer a concern in terms of digital audio processing. Dynamic range limitations typically result from improper gain staging, recording technique including ambient noise and intentional application of dynamic range compression.

Dynamic range in analog audio is the difference between low-level thermal noise in the electronic circuitry and high-level signal saturation resulting in increased distortion and, if pushed higher, clipping. Multiple noise processes determine the noise floor of a system. Noise can be picked up from microphone self-noise, preamp noise, wiring and interconnection noise, media noise, etc.

Early 78 rpm phonograph discs had a dynamic range of up to 40 dB, soon reduced to 30 dB and worse due to wear from repeated play. Vinyl microgroove phonograph records typically yield 55-65 dB, though the first play of the higher-fidelity outer rings can achieve a dynamic range of 70 dB.

German magnetic tape in 1941 was reported to have had a dynamic range of 60 dB, though modern-day restoration experts of such tapes note 45-50 dB as the observed dynamic range. Ampex tape recorders in the 1950s achieved 60 dB in practical usage, In the 1960s, improvements in tape formulation processes resulted in 7 dB greater range, and Ray Dolby developed the Dolby A-Type noise reduction system that increased low- and mid-frequency dynamic range on magnetic tape by 10 dB, and high-frequency by 15 dB, using companding (compression and expansion) of four frequency bands. The peak of professional analog magnetic recording tape technology reached 90 dB dynamic range in the midband frequencies at 3% distortion, or about 80 dB in practical broadband applications. The Dolby SR noise reduction system gave a 20 dB further increased range resulting in 110 dB in the midband frequencies at 3% distortion.

Compact Cassette tape performance ranges from 50 to 56 dB depending on tape formulation, with type IV tape tapes giving the greatest dynamic range, and systems such as XDR, dbx and Dolby noise reduction system increasing it further. Specialized bias and record head improvements by Nakamichi and Tandberg combined with Dolby C noise reduction yielded 72 dB dynamic range for the cassette.

A dynamic microphone is able to withstand high sound intensity and can have a dynamic range of up to 140 dB. Condenser microphones are also rugged but their dynamic range may be limited by the overloading of their associated electronic circuitry. Practical considerations of acceptable distortion levels in microphones combined with typical practices in a recording studio result in a useful dynamic range of 125 dB.

In 1981, researchers at Ampex determined that a dynamic range of 118 dB on a dithered digital audio stream was necessary for subjective noise-free playback of music in quiet listening environments.

Since the early 1990s, it has been recommended by several authorities, including the Audio Engineering Society, that measurements of dynamic range be made with an audio signal present, which is then filtered out in the noise floor measurement used in determining dynamic range. This avoids questionable measurements based on the use of blank media, or muting circuits.

The term *dynamic range* may be confusing in audio production because it has two conflicting definitions, particularly in the understanding of the loudness war phenomenon. *Dynamic range* may refer to micro-dynamics, related to crest factor, whereas the European Broadcasting Union, in EBU3342 Loudness Range, defines *dynamic range* as the difference between the quietest and loudest volume, a matter of macro-dynamics.

## Electronics

In electronics dynamic range is used in the following contexts:

- Specifies the ratio of a maximum level of a parameter, such as power, current, voltage or frequency, to the minimum detectable value of that parameter. (See Audio system measurements.)
- In a transmission system, the ratio of the overload level (the maximum signal power that the system can tolerate without distortion of the signal) to the noise level of the system.
- In digital systems or devices, the ratio of maximum and minimum signal levels required to maintain a specified bit error ratio.
- Optimization of bit width of digital data path (according to the dynamic ranges of signal) can reduce the area, cost, and power consumption of digital circuits and systems while improving their performance. Optimal bit width for a digital data path is the smallest bit width that can satisfy the required signal-to-noise ratio and also avoid overflow.

In audio and electronics applications, the ratio involved is often large enough that it is converted to a logarithm and specified in decibels.

## Metrology

In metrology, such as when performed in support of science, engineering or manufacturing objectives, dynamic range refers to the range of values that can be measured by a sensor or metrology instrument. Often this dynamic range of measurement is limited at one end of the range by saturation of a sensing signal sensor or by physical limits that exist on the motion or other response capability of a mechanical indicator. The other end of the dynamic range of measurement is often limited by one or more sources of random noise or uncertainty in signal levels that may be described as defining the sensitivity of the sensor or metrology device. When digital sensors or sensor signal converters are a component of the sensor or metrology device, the dynamic range of measurement will be also related to the number of binary digits (bits) used in a digital numeric representation in which the measured value is linearly related to the digital number. For example, a 12-bit digital sensor or converter can provide a dynamic range in which the ratio of the maximum measured value to the minimum measured value is up to 212 = 4096.

Metrology systems and devices may use several basic methods to increase their basic dynamic range. These methods include averaging and other forms of filtering, correction of receivers characteristics, repetition of measurements, nonlinear transformations to avoid saturation, etc. In more advance forms of metrology, such as multiwavelength digital holography, interferometry measurements made at different scales (different wavelengths) can be combined to retain the same low-end resolution while extending the upper end of the dynamic range of measurement by orders of magnitude.

## Music

In music, dynamic range describes the difference between the quietest and loudest volume of an instrument, part or piece of music. In modern recording, this range is often limited through dynamic range compression, which allows for louder volume, but can make the recording sound less exciting or live.

The dynamic range of music as normally perceived in a concert hall does not exceed 80 dB, and human speech is normally perceived over a range of about 40 dB.

## Photography

A scene demanding high dynamic range, taken with the

Nikon D7000

digital camera, capable of 13.9 stops of dynamic range per

DxOMark

.

The unedited version of the digital photo is to the left, while the shadows have been

pushed

heavily in

Photoshop

to produce the final image on the right. The better the dynamic range of the camera, the more an exposure can be pushed without significantly increasing

noise

.

Photographers use *dynamic range* to describe the luminance range of a scene being photographed, or the limits of luminance range that a given digital camera or film can capture, or the opacity range of developed film images, or the reflectance range of images on photographic papers.

The dynamic range of digital photography is comparable to the capabilities of photographic film and both are comparable to the capabilities of the human eye.

There are photographic techniques that support even higher dynamic range.

- Graduated neutral density filters are used to decrease the dynamic range of scene luminance that can be captured on photographic film (or on the image sensor of a digital camera): The filter is positioned in front of the lens at the time the exposure is made; the top half is dark and the bottom half is clear. The dark area is placed over a scene's high-intensity region, such as the sky. The result is more even exposure in the focal plane, with increased detail in the shadows and low-light areas. Though this does not increase the fixed dynamic range available at the film or sensor, it stretches usable dynamic range in practice.
- High-dynamic-range imaging overcomes the limited dynamic range of the sensor by selectively combining multiple exposures of the same scene in order to retain detail in light and dark areas. Tone mapping maps the image differently in shadow and highlights in order to better distribute the lighting range across the image. The same approach has been used in chemical photography to capture an extremely wide dynamic range: A three-layer film with each underlying layer at one hundredth (10−2) the sensitivity of the next higher one has, for example, been used to record nuclear-weapons tests.

Consumer-grade image file formats sometimes restrict dynamic range. The most severe dynamic-range limitation in photography may not involve encoding, but rather reproduction to, say, a paper print or computer screen. In that case, not only local tone mapping but also *dynamic range adjustment* can be effective in revealing detail throughout light and dark areas: The principle is the same as that of dodging and burning (using different lengths of exposures in different areas when making a photographic print) in the chemical darkroom. The principle is also similar to gain riding or automatic level control in audio work, which serves to keep a signal audible in a noisy listening environment and to avoid peak levels that overload the reproducing equipment, or which are unnaturally or uncomfortably loud.

If a camera sensor is incapable of recording the full dynamic range of a scene, high-dynamic-range (HDR) techniques may be used in postprocessing, which generally involve combining multiple exposures using software.

| Device | Stops | Contrast ratio | Optical density |
|---|---|---|---|
| Glossy photograph paper | 7 (7–7+2⁄3) | 128:1 | 2.1 |
| LCD | 9.5 (9–11) | 720:1 (510:1 – 2000:1) | 2.9 (2.7 – 3.3) |
| Typical cellphone camera | ~10 | varies |   |
| Negative film (Kodak VISION3) | 13 | 8200:1 | 3.9 |
| Human eye | 10–14 | 1000:1 – 16000:1 | 3 – 4.2 |
| OLED or quantum dot | 13.2 – 20.9 | 9400:1 – 1960000:1 | 4 – 6.3 |
| High-end DSLR camera (Nikon D850) | 14.8 | 28500:1 | 4.5 |
| Digital cinema camera (Red Weapon 8k) | > 16.5 | >92700:1 | >5 |
