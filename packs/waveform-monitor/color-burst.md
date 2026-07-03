---
title: "Color burst"
source: https://en.wikipedia.org/wiki/Color_burst
domain: waveform-monitor
license: CC-BY-SA-4.0
tags: waveform monitor
fetched: 2026-07-03
---

# Color burst

The **color burst** is one part of the composite sync used in analog television signals. It consists of a "packet" of the sine wave chroma subcarrier and is used as a reference to decode color information in the video. By synchronizing an oscillator with the color burst at the back porch (beginning) of each scan line, a television receiver is able to restore the suppressed carrier of the chrominance (color) signals, and in turn decode the color information.

## Explanation

In NTSC, the color burst frequency is exactly 315/88 = 3.57954 MHz with a phase of 180°. PAL uses a frequency of exactly 4.43361875 MHz, with its phase alternating between 135° and 225° from line to line. Since the color burst signal has a known amplitude, it is sometimes used as a reference level when compensating for amplitude variations in the overall signal.

SECAM is unique in not having a color burst signal, since the chrominance signals are encoded using FM rather than QAM, thus the signal phase is immaterial and no reference point is needed.

## Rationale for NTSC Color burst frequency

The original black and white NTSC television standard specified a frame rate of 30 Hz and 525 lines per frame, or 15750 lines per second. The audio was frequency modulated 4.5 MHz above the video signal. Because this was black and white, the video consisted only of luminance (brightness) information. Although all of the space in between was occupied, the line-based nature of the video information meant that the luminance data was not spread uniformly across the frequency domain; it was concentrated at multiples of the line rate. Plotting the video signal on a spectrogram gave a signature that looked like the teeth of a comb or a gear, rather than smooth and uniform.

RCA discovered that if the chrominance (color) information, which had a similar spectrum, was modulated on a carrier that was a half-integer multiple of the line rate, its signal peaks would fit neatly between the peaks of the luminance data and interference was minimized. It was not eliminated, but what remained was not readily apparent to human eyes. (Modern televisions attempt to reduce this interference further using a comb filter.)

To provide sufficient bandwidth for the chrominance signal, yet interfere only with the highest-frequency (and thus least perceptible) portions of the luminance signal, a chrominance subcarrier near 3.6 MHz was desirable. 227.5 = 455/2 times the line rate was close to the right number, and 455's small factors (5 × 7 × 13) make a divider easy to construct.

However, additional interference could come from the audio signal. To minimize interference there, it was similarly desirable to make the distance between the chrominance carrier frequency and the audio carrier frequency a half-integer multiple of the line rate. The sum of these two half-integers implies that the distance between the frequency of the luminance carrier and audio carrier must be an integer multiple of the line rate. However, the original NTSC standard, with a 4.5 MHz carrier spacing and a 15750 Hz line rate, did not meet this requirement: the audio was 285.714 times the line rate.

While existing black and white receivers could not decode a signal with a different audio carrier frequency, they could easily use the copious timing information in the video signal to decode a slightly slower line rate. Thus, the new color television standard reduced the line rate by a factor of 1.001 to 1/286 of the 4.5 MHz audio subcarrier frequency, or about 15734.2657 Hz. This reduced the frame rate to 30/1.001 ≈ 29.9700 Hz, and placed the color subcarrier at 227.5/286 = 455/572 = 35/44 of the 4.5 MHz audio subcarrier.

## Crystals

An NTSC or PAL television's color decoder contains a color burst crystal oscillator.

Because so many analog color TVs were produced from the 1960s to the early 2000s, economies of scale drove down the cost of color burst crystals, so they were often used in various other applications, such as oscillators for microprocessors or for amateur radio: 3.5795 MHz has since become a common QRP calling frequency in the 80-meter band, and its doubled frequency of 7.159 MHz is a common calling frequency in the 40-meter band. Tripling this frequency is also how FM radio circuits came to use a nominally 10.7 MHz intermediate frequency in superheterodyne conversion.

| Component | Frequency | Ratio |
|---|---|---|
| Intellivision CPU | 0.8949 MHz | ⁠1/4⁠*f* |
| TRS-80 Color Computer CPU (normal speed) |   |   |
| Apple II CPU (short cycles only, one in 65 cycles is longer) | 1.0227 MHz | ⁠2/7⁠*f* |
| VIC-20 CPU |   |   |
| Commodore 64 CPU |   |   |
| Commodore 128 CPU (SLOW & C64 compatible modes) |   |   |
| Atari 2600 CPU | 1.1932 MHz | ⁠1/3⁠*f* |
| Intel 8253 interval timer in IBM PC (remains in use today) |   |   |
| Fairchild Video Entertainment System CPU | 1.7898 MHz | ⁠1/2⁠*f* |
| Odyssey 2 CPU |   |   |
| Atari 8-bit computers and Atari 7800 CPU |   |   |
| Plus/4 CPU |   |   |
| Nintendo Entertainment System CPU |   |   |
| TRS-80 Color Computer 3 CPU (fast mode) |   |   |
| Commodore 128 CPU (FAST & CP/M modes) | 2.0454 MHz | ⁠4/7⁠*f* |
| Super NES CPU | 2.6847 MHz | ⁠3/4⁠*f* |
| 3.5795 MHz | *f* |   |
| Master System CPU | *f* |   |
| MSX CPU |   |   |
| Amateur radio Tx/Rx crystal for 80m band |   |   |
| ColecoVision CPU |   |   |
| Yamaha OPL and OPL2 FM synthesis sound chips |   |   |
| ACPI power management timer |   |   |
| IBM Personal Computer 5150 CPU | 4.7727 MHz | ⁠4/3⁠*f* |
| Amiga CPU | 7.1591 MHz | 2*f* |
| Tandy 1000 SX CPU (and many other IBM PC-XT clones) |   |   |
| TurboGrafx-16 CPU |   |   |
| Yamaha TX81Z synthesizer CPU |   |   |
| Amateur radio Tx/Rx crystal for 40m band |   |   |
| Genesis CPU | 7.6705 MHz | ⁠15/7⁠*f* |
| Intermediate frequency of FM radio superheterodyne circuits | 10.7386 MHz | 3*f* |
| High Precision Event Timer (typical) | 14.3181 MHz | 4*f* |

| Component | Frequency | Ratio |
|---|---|---|
| Commodore 64 CPU | 0.9852 MHz | ⁠2/9⁠*f* |
| Commodore 128 CPU (SLOW & C64 compatible modes) |   |   |
| Atari 2600 CPU | 1.182298 MHz | ⁠4/15⁠*f* |
| VIC-20 CPU | 1.1084 MHz | ⁠1/4⁠*f* |
| Nintendo Entertainment System CPU | 1.662607 MHz | ⁠3/8⁠*f* |
| Atari 8-bit computers CPU | 1.7734475 MHz | ⁠2/5⁠*f* |
| Dendy (famiclone) CPU |   |   |
| Commodore 128 CPU (FAST & CP/M modes) | 1.9704 MHz | ⁠4/9⁠*f* |
| Super Nintendo Entertainment System CPU | 2.6601712 MHz | ⁠3/5⁠*f* |
| 3.546895 MHz | ⁠4/5⁠*f* |   |
| Commodore Amiga CPU | 7.09379 MHz | ⁠8/5⁠*f* |
