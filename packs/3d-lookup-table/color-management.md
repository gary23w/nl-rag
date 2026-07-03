---
title: "Color management"
source: https://en.wikipedia.org/wiki/Color_management
domain: 3d-lookup-table
license: CC-BY-SA-4.0
tags: 3d lookup table
fetched: 2026-07-03
---

# Color management

**Color management** is the process of ensuring consistent and accurate colors across various devices, such as monitors, printers, and cameras. It involves the use of color profiles, which are standardized descriptions of how colors should be displayed or reproduced.

Color management is necessary because different devices have different color capabilities and characteristics. For example, a monitor may display colors differently than a printer can reproduce them. Without color management, the same image may appear differently on different devices, leading to inconsistencies and inaccuracies.

To achieve color management, a color profile is created for each device involved in the color workflow. This profile describes the device's color capabilities and characteristics, such as its color gamut (range of colors it can display or reproduce) and color temperature. These profiles are then used to translate colors between devices, ensuring consistent and accurate color reproduction.

Color management is particularly important in industries such as graphic design, photography, and printing, where accurate color representation is crucial. It helps to maintain color consistency throughout the entire workflow, from capturing an image to displaying or printing it.

Parts of color management are implemented in the operating system (OS), helper libraries, the application, and devices. The type of color profile that is typically used is called an ICC profile. A cross-platform view of color management is the use of an ICC-compatible color management system. The International Color Consortium (ICC) is an industry consortium that has defined:

- an open standard for a *Color Matching Module* (CMM) at the OS level
- color profiles for:
  - devices, including DeviceLink profiles that transform one device profile (color space) to another device profile without passing through an intermediate color space, such as L*A*B*, more accurately preserving color
  - *working spaces*, the color spaces in which color data is meant to be manipulated

There are other approaches to color management besides using ICC profiles. This is partly due to history and partly because of other needs than the ICC standard covers. The film and broadcasting industries make use of some of the same concepts, but they frequently rely on more limited boutique solutions. The film industry, for instance, often uses 3D LUTs (lookup table) to represent a complete color transformation for a specific RGB encoding.

At the consumer level, system wide color management is available in most of Apple's products (macOS, iOS, iPadOS, watchOS). Microsoft Windows lacks system wide color management and virtually all applications do not employ color management. Windows' media player API is not color space aware, and if applications want to color manage videos manually, they have to incur significant performance and power consumption penalties. Android supports system wide color management, but most devices ship with color management disabled.

## Overview

1. Characterize. Every color-managed device requires a personalized table, or "color profile," which characterizes the color response of that particular device.
2. Standardize. Each color profile describes these colors relative to a standardized set of reference colors (the "Profile Connection Space").
3. Translate. Color-managed software then uses these standardized profiles to translate color from one device to another. This is usually performed by a color management module (CMM).

## Hardware

### Characterization

To describe the behavior of various output devices, they must be compared (measured) in relation to a standard color space. Often a step called linearization is performed first, to undo the effect of gamma correction that was done to get the most out of limited 8-bit color paths. Instruments used for measuring device colors include colorimeters and spectrophotometers. As an intermediate result, the device gamut is described in the form of scattered measurement data. The transformation of the scattered measurement data into a more regular form, usable by the application, is called *profiling*. Profiling is a complex process involving mathematics, intense computation, judgment, testing, and iteration. After the profiling is finished, an idealized color description of the device is created. This description is called a *profile*.

### Calibration

Calibration is like characterization, except that it can include the adjustment of the device, as opposed to just the measurement of the device. Color management is sometimes sidestepped by calibrating devices to a common standard color space such as sRGB; when such calibration is done well enough, no color translations are needed to get all devices to handle colors consistently. This avoidance of the complexity of color management was one of the goals in the development of sRGB.

## Color profiles

### Embedding

Image formats themselves (such as TIFF, JPEG, PNG, EPS, PDF, and SVG) may contain embedded color profiles but are not required to do so by the image format. The International Color Consortium standard was created to bring various developers and manufacturers together. The ICC standard permits the exchange of output device characteristics and color spaces in the form of metadata. This allows the embedding of color profiles into images as well as storing them in a database or a profile directory.

### Working spaces

Working spaces, such as sRGB, Adobe RGB or ProPhoto are color spaces that facilitate good results while editing. For instance, pixels with equal values of R,G,B should appear neutral. Using a large (gamut) working space will lead to posterization, while using a small working space will lead to clipping. This trade-off is a consideration for the critical image editor.

## Color transformation

Color transformation, or color space conversion, is the transformation of the representation of a color from one color space to another. This calculation is required whenever data is exchanged inside a color-managed chain and carried out by a Color Matching Module. Transforming profiled color information to different output devices is achieved by referencing the profile data into a standard color space. It makes it easier to convert colors from one device to a selected standard color space and from that to the colors of another device. By ensuring that the reference color space covers the many possible colors that humans can see, this concept allows one to exchange colors between many different color output devices. Color transformations can be represented by two profiles (source profile and target profile) or by a devicelink profile. In this process there are approximations involved which make sure that the image keeps its important color qualities and also gives an opportunity to control on how the colors are being changed.

### Profile connection space

In the terminology of the International Color Consortium, a translation between two color spaces can go through a *profile connection space* (PCS): Color Space 1 → PCS (CIELAB or CIEXYZ) → Color space 2; conversions into and out of the PCS are each specified by a profile.

### Gamut mapping

In nearly every translation process, we have to deal with the fact that the color gamut of different devices vary in range which makes an accurate reproduction impossible. They therefore need some rearrangement near the borders of the gamut. Some colors must be shifted to the inside of the gamut, as they otherwise cannot be represented on the output device and would simply be clipped. This so-called gamut mismatch occurs for example, when we translate from the RGB color space with a wider gamut into the CMYK color space with a narrower gamut range. In this example, the dark highly saturated purplish-blue color of a typical computer monitor's "blue" primary is impossible to print on paper with a typical CMYK printer. The nearest approximation within the printer's gamut will be much less saturated. Conversely, an inkjet printer's "cyan" primary, a saturated mid-brightness blue, is outside the gamut of a typical computer monitor. The color management system can utilize various methods to achieve desired results and give experienced users control of the gamut mapping behavior.

#### Rendering intent

When the gamut of source color space exceeds that of the destination, saturated colors are liable to become clipped (inaccurately represented), or more formally burned. The color management module can deal with this problem in several ways. The ICC specification includes four different rendering intents, listed below. Before the actual rendering intent is carried out, one can temporarily simulate the rendering by soft proofing. It is a useful tool as it predicts the outcome of the colors and is available as an application in many color management systems:

***Absolute colorimetric***

Absolute colorimetry and relative colorimetry actually use the same table but differ in the adjustment for the white point media. If the output device has a much larger gamut than the source profile, i.e., all the colors in the source can be represented in the output, using the absolute colorimetry rendering intent would ideally (ignoring noise, precision, etc.) give an exact output of the specified CIELAB values. Perceptually, the colors may appear incorrect, but instrument measurements of the resulting output would match the source. Colors outside of the proof print system's possible color are mapped to the boundary of the color gamut.

Absolute colorimetry is useful to get an exact specified color (e.g., IBM blue), or to quantify the accuracy of mapping methods.

***Relative colorimetric***

The goal in relative colorimetry is to be truthful to the specified color, with only a correction for the media. Relative colorimetry is useful in proofing applications, since it can be used to get an idea of how a print on one device will appear on a different device. Media differences are the only thing that one really should adjust for, although some gamut mapping also needs to be applied. Usually this is done in a way where hue and lightness are maintained at the cost of reduced saturation. By default, in-gamut colors are unchanged, while out-of-gamut colors are clamped.

Relative colorimetric is the default rendering intent on many systems.

***Perceptual***

The perceptual intent smoothly moves out-of-gamut colors into gamut, preserving gradations, but distorts in-gamut colors in the process. Like the saturation intent, the results really depend upon the profile maker. This is even how some of the competitors in this market differentiate themselves. The profile maker tries to make results pleasing on this intent. Perceptual rendering is recommended for color separation.

***Saturation***

The saturation intent is designed to present eye-catching business graphics by preserving the saturation (colorfulness). It is most useful in charts and diagrams, where there is a discrete palette of colors that the designer wants saturated to make them intense, but where specific hue is less important.

In practice, photographers almost always use relative or perceptual intent, as for natural images, absolute causes color cast, while saturation produces unnatural colors. If an entire image is in-gamut, relative is perfect, but when there are out of gamut colors, which is preferable depends on a case-by-case basis. CMMs may offer options for BPC and partial chromatic adaptation.

A black point correction (BPC) is not applied for absolute colorimetric or devicelink profiles. For ICCv4, it is always applied to the perceptual intent. ICCv2 sRGB profiles differ among each other in a number of ways, one of which being whether BPC is applied.

## Implementation

### Color management module

*Color matching module* (also -*method* or -*system*) is a software algorithm that adjusts the numerical values that get sent to or received from different devices so that the perceived color they produce remains consistent. The key issue here is how to deal with a color that cannot be reproduced on a certain device in order to show it through a different device as if it were visually the same color, just as when the reproducible color range between color transparencies and printed matters are different. There is no common method for this process, and the performance depends on the capability of each color matching method.

Some well known CMMs are ColorSync, Adobe CMM, Little CMS, and ArgyllCMS.

### Operating system level

#### Apple

Apple's classic Mac OS and macOS operating systems have provided OS-level color management APIs since 1993, through ColorSync. macOS has added automatic color management (assuming sRGB and DCI-P3 for most things) automatically in the OS, but applications can explicitly target other color spaces if they wish to. System wide color management is used in iOS, iPadOS and watchOS as well.

#### Windows

Microsoft Windows prior to Windows 10 recommends the sRGB color space. Since Windows 10 with High Dynamic Range (HDR) enabled and since Windows 11 with Auto Color Management (ACM) enabled, it recommends the DCI-P3 color space.

Since 1997 color management in Windows is available through an ICC color management system: ICM (Image Color Management).

Beginning with Windows Vista, Microsoft introduced a new color architecture known as WCS (Windows Color System). WCS supplements the ICM system in Windows 2000 and Windows XP, originally written by Heidelberg.

Apps need to be aware of color management and tag the content appropriately to accurately display colors. Otherwise, (unlike macOS) Windows will display the colors to the maximum extent of the display's gamut, resulting in over-saturated colors on wide-gamut displays. To fix this issue, Microsoft includes a new feature called "Auto Color Management" since Windows 11 2022. A few exception is the ICM profile includes the Video Card Gamma Table (VCGT) data, and the VCGT data will be applied globally.

Windows Photo Viewer from Windows 7 (also included in later Windows versions) performs proper color management, however, the newer Windows Photos app in Windows 8, 10, 11 does not perform legacy color management (ICM/WCS) until version v2022.31070.26005.0. Other Windows components, including Microsoft Paint, Snipping Tool, Windows Desktop, Windows Explorer, do not perform legacy color management.

In Windows 8, the DXVA API and the WIC API added support for color space conversion, but in Windows 8 it's still not support wide color gamut.

Unfortunately, the vast majority of personal applications do not use the Windows Color System. For applications that do employ color management (typically web browsers), color management tend to apply for only images and UI, but not videos. This is because Windows' media player API is not color space aware. Thus, browsers (Chrome, Firefox, Edge) are only able to do color management for images but not video. For the same reason, virtually no video players on Windows support color management (including the default Windows Movies & TV app and VLC Media Player), with Media Player Classic Home Cinema being a rare exception.

Windows 10 1607 supports High Dynamic Range (HDR).

Windows 11 22H2 supports Auto Color Management (ACM) which further optimized for OLED and/or wide-color gamut monitors. Applications can be updated to support ACM and wide-color gamut; Microsoft Edge, Google Chrome, Windows Photos and Windows Media Player 2022 are known to support ACM. While ACM can do color space conversion, but actual color management factors (such as color temperature and contrast) are also depend on OSD settings of monitor or TV set, and/or depend on software/driver settings of GPU/monitor.

#### Android

On Android, system wide color management is introduced in Android Oreo 8.1. However, most Android phones are shipped with color management disabled (ex: 'adaptive' color profile on Google Pixel, 'vivid' color profile on Samsung Galaxy). This oversaturates sRGB content to the native display gamut, typically DCI-P3. Users need to manually select the 'natural' color profile to enable color management, enabling accurate display of sRGB and P3 wide color content.

#### Others

Operating systems that use the X Window System for graphics can use ICC profiles, and support for color management on Linux, still less mature than on other platforms, is coordinated through OpenICC at freedesktop.org and makes use of LittleCMS.

### File level

Certain image filetypes (TIFF and Photoshop) include the notion of color channels for specifying the *color mode* of the file. The most commonly used channels are RGB (mainly for display (monitors) but also for some desktop printing) and CMYK (for commercial printing). An additional *alpha* channel may specify a transparency mask value. Some image software (such as Photoshop) perform automatic color separation to maintain color information in CMYK mode using a specified ICC profile such as **US Web Coated (SWOP) v2**.

### Creative software

Adobe software includes its own color management engine - Adobe Color Engine. It is also available as a separate Color Management Module - Adobe CMM for use by non-Adobe applications that supports 3rd-party CMMs.

### Web browsers

As of 2005, most web browsers ignored color profiles. Notable exceptions were Safari, starting with version 2.0, and Firefox starting with version 3. Although disabled by default in Firefox 3.0, ICC v2 and ICC v4 color management could be enabled by using an add-on or setting a configuration option.

As of July 2019, Safari, Chrome and Firefox fully support color management. Most browsers only do color management for images and CSS elements, but not video.

- Firefox: version 3.5 (released in 2011) onwards supports ICC v2 tagged images, and version 8.0 (released in 2011) adds ICC v4 profiles support. Version 89 (released in 2021) and above apply color management to all untagged images and page elements by default.
- Internet Explorer: support ICC profiles from version 9 onwards, but only converts non-sRGB images to the sRGB profile, regardless of the actual monitor colorspace.
- Google Chrome: uses the system provided ICC v2 and v4 support on macOS, and from version 22 (released in 2012) supports ICC v2 profiles by default on other platforms. macOS versions of Chrome correctly render video.
- Safari: has support starting with version 2.0 (released in 2005). Supports v2 and v4 ICC profiles, and correctly renders video.
- Opera: has support since 12.10 (released in 2012) for ICC v4.
- Pale Moon supported ICC v2 from its first release, and v4 since Pale Moon 20.2 (released in 2013).

Regarding mobile browsers, Safari 13.1 (on iOS 13.4.1) recognizes the device color profile and can displays images accordingly. Chrome 83 (on Android 9) ignores the display profile, simply converting all images to sRGB.

As of 2023, Chrome 114, Android Browser 114 and Firefox for Android 115 support multiple colorspaces. The same is valid for their desktop counterparts: Chrome 118, Edge 114, Safari 16.6, Firefox 117 and Opera 100.
