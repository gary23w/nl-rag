---
title: "SMPTE color bars"
source: https://en.wikipedia.org/wiki/Color_bars
domain: waveform-monitor
license: CC-BY-SA-4.0
tags: waveform monitor
fetched: 2026-07-03
---

# SMPTE color bars

(Redirected from

Color bars

)

**SMPTE color bars** are a television test pattern used where the NTSC video standard is utilized, including countries in North America. The Society of Motion Picture and Television Engineers (SMPTE) refers to the pattern as **Engineering Guideline (EG) 1-1990**. Its components are a known standard, and created by test pattern generators. Comparing it as received to the known standard gives video engineers an indication of how an NTSC video signal has been altered by recording or transmission and what adjustments must be made to bring it back to specification. It is also used for setting a television monitor or receiver to reproduce NTSC chrominance and luminance information correctly.

A precursor to the SMPTE test pattern was conceived by Norbert D. Larky (1927–2018) and David D. Holmes (1926–2006) of RCA Laboratories and first published in RCA Licensee Bulletin LB-819 on February 7, 1951. U.S. patent 2,742,525 Color Test Pattern Generator (since expired) was awarded on April 17, 1956, to Larky and Holmes. Later, the EIA published a standard, **RS-189A**, which in 1976 became **EIA-189A**, which described a Standard Color Bar Signal, intended for use as a test signal for adjustment of color monitors, adjustment of encoders, and rapid checks of color television transmission systems. In 1977, A. A. Goldberg, of the CBS Technology Center, described an improved color bar test signal developed at the center by Hank Mahler (1936–2021) that was then submitted to the SMPTE TV Video Technology Committee for consideration as a SMPTE recommended practice. This improved test signal was published as the standard **SMPTE ECR 1-1978**. Its development by CBS was awarded a Technology & Engineering Emmy Award in 2002. CBS did not file a patent application on the test signal, thereby putting it into the public domain for general use by the industry.

An extended version of the SMPTE color bars, **SMPTE RP 219:2002** was introduced to test HDTV signals (see subsection).

Although color bars were originally designed to calibrate analog NTSC equipment, they remain widely used in transmission and within modern digital television facilities. In that context color bars are used to maintain accurate chroma and luminance levels in CRT, LCD, LED, plasma, and other video displays, as well as duplication, satellite, fiber-optic and microwave transmission, and television and webcast equipment.

In a survey of the top standards of the organizations' first 100 years, SMPTE EG-1 was voted as the 5th-most important SMPTE standard.

## SMPTE ECR 1-1978 (SDTV)

In a SMPTE color bar image, the top two-thirds of the television picture contain seven vertical bars of 75% intensity. In order from left to right, the colors are white or gray, yellow, cyan, green, magenta, red, and blue. The choice of white or gray depends on whether that bar's luminance is 100% or not. This sequence runs through all seven possible combinations that use at least one of the three basic color components of green, red, and blue, with blue cycling on and off between every bar, red cycling on and off every two bars, and green on for the leftmost four bars and off for the rightmost three. Because green contributes the largest share of luminance, followed by red, then blue, this sequence of bars thus appears on a waveform monitor in luminance mode as a downward staircase from left to right. The graticule of a vectorscope is etched with boxes showing the permissible regions where the traces from these seven bars are supposed to fall if the signal is properly adjusted.

Below the main set of seven bars is a strip of blue, magenta, cyan, and white or gray castellations. When a television receiver is set to filter out all colors except for blue, these castellations, combined with the main set of color bars, are used to adjust the color controls; they appear as four solid blue bars, with no visible distinction between the bars and the castellations if the color controls are properly adjusted.

The bottom section contains a square of 100% intensity white and a rectangle of 7.5% intensity black, for use in setting the luminance range. More modern versions of the pattern feature a *PLUGE pulse*. The white square lines up so that it is below the yellow and cyan bars, and on a waveform monitor this will show up with the white bar overlapping the peak of the yellow and cyan chroma at 100 IRE units. The *pluge* (short for picture line-up generation equipment) pulse is positioned within the black rectangle, below the red bar (it is present in the illustration but may be hard to see). It comprises three small vertical bars, a rightmost one with intensity 4% above black level (11.5 IRE), a middle one with intensity exactly equal to black (7.5 IRE), and a leftmost one with intensity 4% below black (super-black or *blacker than black*, 3.5 IRE). The pluge pulse aids in adjusting the bottom of the luminance range to avoid either washing out the black tones into grays or collapsing picture information into the signal clipping that occurs a small distance below the black level (known as *crushing the blacks*). When a monitor is properly adjusted, the rightmost pluge bar should be just barely visible, while the left two should appear indistinguishable from each other and completely black. Also in the bottom section are two sections that contain -In-phase and +Quadrature signals (see YIQ), centered on black level and having the same gain as the color burst signal; these show up on the pattern as a square of very dark blue, and a square of very dark purple. On a vectorscope, they appear as two short lines ninety degrees apart. These are used to ensure that the television receiver is properly demodulating the 3.58 MHz color subcarrier portion of the signal. The vectors for the -I and +Q blocks should fall exactly on the I and Q axes on the vectorscope if the chrominance signal is demodulated properly.

These bars give rise to the former portion of the casual term *bars and tone*. Typically, a television network, TV station, or other originator of video programming transmits SMPTE color bars together with a continuous 1,000 Hz sine wave before sending program material, in order to assert ownership of the transmission line or medium, and so that receiving stations and intermediary telecommunications providers may adjust their equipment. Likewise, producers of television programs typically record *bars and tone* at the beginning of a videotape or other recording medium so that the playback equipment can be calibrated. Often, the name or callsign of the TV station, other information such as a real-time clock, or another signal source is graphically superimposed over the bars.

### Analog NTSC

Values of 75% (75/7.5/75/7.5) SMPTE ECR 1-1978 color bars as analog NTSC signals:

| Color | Luma | Chrominance Range | Chrominance Phase |   |   |
|---|---|---|---|---|---|
| IRE | mV | IRE p-p | mV p-p | ° |   |
| Gray | 76.9 | 549.1 | 0.0 | 0.0 | - |
| Yellow | 69.0 | 492.6 | 62.1 | 443.3 | 167.1° |
| Cyan | 56.1 | 400.9 | 87.7 | 626.6 | 283.7° |
| Green | 48.2 | 344.5 | 81.9 | 585.2 | 241.3° |
| Magenta | 36.2 | 258.2 | 81.9 | 585.2 | 61.3° |
| Red | 28.2 | 201.7 | 87.7 | 626.6 | 103.7° |
| Blue | 15.4 | 110.1 | 62.1 | 443.3 | 347.1° |
| -I | 7.5 | 53.6 | 40.0 | 285.7 | 303.0° |
| White | 100.0 | 714.3 | 0.0 | 0.0 | - |
| +Q | 7.5 | 53.6 | 40.0 | 285.7 | 33.0° |
| Super-black | 3.5 | 25.5 | 0.0 | 0.0 | - |
| Black | 7.5 | 53.6 | 0.0 | 0.0 | - |
| 4% Above Black Level | 11.5 | 81.5 | 0.0 | 0.0 | - |

***Note:** IRE units apply to both NTSC composite video and broadcast signals while mV values only apply to NTSC composite video. Values sourced from the Tektronix TSG95 test pattern generator manual*

### Digital video

For digital video sources, the 10-bit YCbCr values for SD color bars are based on the SMPTE formula for Y from the NTSC system (Y = 0.299R + 0.587G + 0.114B). The following table show the expected digital values, for example when measured using a signal analyzer.

| **10-bit YCbCr values for SD 75% color bars** |   |   |   |
|---|---|---|---|
| Color | ***Y*** | ***Cb*** | ***Cr*** |
| White | 940 | 512 | 512 |
| Yellow | 646 | 176 | 567 |
| Cyan | 525 | 625 | 176 |
| Green | 450 | 289 | 231 |
| Magenta | 335 | 735 | 793 |
| Red | 260 | 399 | 848 |
| Blue | 139 | 848 | 457 |
| Black | 64 | 512 | 512 |

**Note:** Values sourced from "*Leader Teleproduction Test Volume 3 Number 4 - Digital Video Levels*"

The colors below are presented using sRGB transfer of CSS. Since sRGB is the standard colorspace for webpages and computer screens, this gives only an idea of the intended colors. They are not completely representative of how they look on TV displays, since these follow the ITU-R BT.1886 standard, specifying a different gamma correction value, and thus colors below will look darker on such a display, and those darker colors will be the reference ones. The off-by-one errors (for example 254 instead of 255 and 1 instead of 0) happen because the 8 bit Y'CbCr values were used when decoding to R'G'B', if you use 10-bit Y'CbCr that does not happen.

Y'CbCr values of 75% (100/0/75/0) SMPTE ECR 1-1978 color bars (0.75 * 219 + 16 = 180) using BT.709-2 matrix coefficients as written in RP 219:2002:

| COLOR | 8-bit Studio R'G'B' | 10-bit Studio R'G'B' | 8-bit Y'CbCr | 10-bit Y'CbCr | 12-bit Y'CbCr |
|---|---|---|---|---|---|
| 40% Gray | 104-104-104 | 414-414-414 | 104-128-128 | 414-512-512 | 1658-2048-2048 |
| 75% White | 180-180-180 | 721-721-721 | 180-128-128 | 721-512-512 | 2884-2048-2048 |
| 75% Yellow | 180-180-16 | 721-721-64 | 168-44-136 | 674-176-543 | 2694-704-2171 |
| 75% Cyan | 16-180-180 | 64-721-721 | 145-147-44 | 581-589-176 | 2325-2356-704 |
| 75% Green | 16-180-16 | 64-721-64 | 133-63-52 | 534-253-207 | 2136-1012-827 |
| 75% Magenta | 180-16-180 | 721-64-721 | 63-193-204 | 251-771-817 | 1004-3084-3269 |
| 75% Red | 180-16-16 | 721-64-64 | 51-109-212 | 204-435-848 | 815-1740-3392 |
| 75% Blue | 16-16-180 | 64-64-721 | 28-212-120 | 111-848-481 | 446-3392-1925 |
| 75% Black | 16-16-16 | 64-64-64 | 16-128-128 | 64-512-512 | 256-2048-2048 |
| 100% White | 235-235-235 | 940-940-940 | 235-128-128 | 940-512-512 | 3760-2048-2048 |
| +Q | 72-16-118 | 288-64-472 | 35-174-152 | 141-697-606 | 564-2787-2425 |
| +I | 106-52-16 | 424-208-64 | 61-103-157 | 245-412-629 | 982-1648-2516 |
| -I | 16-70-106 | 64-280-424 | 61-153-99 | 244-612-395 | 976-2448-1580 |

The source data for 10-bit and 12-bit Y'CbCr is 8-bit Studio R'G'B', so 10-bit data is not just a bitshift operation (that means multiply by 4) from 8-bit Y'CbCr, as usually the case. For example, for 75% Blue 28-212-120 would be just 112-848-480, but it is actually 111-848-481.

Per ITU-R BT.2111-2 TABLE 2

## SMPTE RP 219:2002 (HDTV version)

An extended version of SMPTE Color Bars signal, developed by the Japanese Association of Radio Industries and Businesses as **ARIB STD-B28** and standardized as **SMPTE RP 219:2002** (High-Definition, Standard-Definition Compatible Color Bar Signal) was introduced to test HDTV signal with an aspect ratio of 16:9 that can be down converted to a SDTV color bar signal with an aspect ratio of either 4:3 or 16:9. The Color Bar signal is generated with unconventionally slow rise and fall time value to facilitate video level control and monitor color adjustments of HDTV and SDTV equipment.

Digital test images generated following the **RP 219:2002** specifications and adapted to perfectly fit 114 standard and non-standard resolutions for both 16bpp and 8bpp, are freely available in the COLOR dataset of the TESTIMAGES archive.

Later **RP 219:2002** became **RP 219-1:2014**, with **RP 219-2:2016** and **ARIB STD-B66** adding details for UHD. **ITU-R Rec. BT.2111** and **ARIB STD-B72** further added versions with PQ / HLG HDR transfer functions and wide color gamut (BT.2020), which additionally have 100% saturated colors at the top and BT.709 bars at right bottom and left bottom; the 75% gray horizontal bar in the middle is changed to grayscale stair steps.

### Values

The values of 100% (100/0/100/0) **SMPTE RP 219:2002** color bars (1.00 * 219 + 16 = 235) using BT.709 matrix coefficients (only white and black are the same using BT.601 matrix), taken from the standard:

| COLOR | 8-bit Studio R'G'B' | 8-bit Y'CbCr | 10-bit Y'CbCr | 12-bit Y'CbCr |
|---|---|---|---|---|
| 100% White | 235-235-235 | 235-128-128 | 940-512-512 | 3760-2048-2048 |
| 100% Yellow | 235-235-16 | 219-16-138 | 877-64-553 | 3507-256-2212 |
| 100% Cyan | 16-235-235 | 188-154-16 | 754-615-64 | 3015-2459-256 |
| 100% Red | 235-16-16 | 63-102-240 | 250-409-960 | 1001-1637-3840 |
| 100% Blue | 16-16-235 | 32-240-118 | 127-960-471 | 509-3840-1884 |
| 100% Black | 16-16-16 | 16-128-128 | 64-512-512 | 256-2048-2048 |

ITU-R **Rec. BT.1729** specified the last two 100% colors, green and magenta. It also specified all 100% colors for BT.601 matrix, not only BT.709.
