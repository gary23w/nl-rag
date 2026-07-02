---
title: "ICC profile"
source: https://en.wikipedia.org/wiki/ICC_profile
domain: color-management
license: CC-BY-SA-4.0
tags: color management, icc profile, color gamut, cie color space
fetched: 2026-07-02
---

# ICC profile

In color management, an **ICC profile** is a set of data that characterizes a color input or output device, or a color space, according to standards promulgated by the International Color Consortium (ICC). Profiles describe the color attributes of a particular device or viewing requirement by defining a mapping between the device source or target color space and a *profile connection space* (PCS). This PCS is either CIELAB (L*a*b*) or CIEXYZ. Mappings may be specified using tables, to which interpolation is applied, or through a series of parameters for transformations.

Every device that captures or displays color can be profiled. Some manufacturers provide profiles for their products, and there are several products that allow an end-user to generate their own color profiles, typically through the use of a tristimulus colorimeter or a spectrophotometer (sometimes called a spectrocolorimeter).

The ICC defines the format precisely but does not define algorithms or processing details. This means there is room for variation between different applications and systems that work with ICC profiles. Two main generations are used: the legacy ICCv2 and the December 2001 ICCv4. The current version of the format specification (ICC.1) is 4.4.

ICC has also published a preliminary specification for iccMAX (ICC.2) or ICCv5, a next-generation color management architecture with significantly expanded functionality and a choice of colorimetric, spectral or material connection space.

## Details

To see how this works in practice, suppose we have a particular RGB and CMYK color space, and want to convert from this RGB to that CMYK. The first step is to obtain the two ICC profiles concerned. To perform the conversion, each RGB triplet is first converted to the Profile connection space (PCS) using the RGB profile. If necessary the PCS is converted between CIELAB and CIEXYZ, a well defined transformation. Then the PCS is converted to the four values of C, M, Y, K required using the second profile.

So a profile is essentially a pair of mappings; one from a color space to the PCS and a second from the PCS to the color space. A mapping might be implemented using tables of color values to be interpolated or be implemented using a series of mathematical formulae.

A profile might define several mappings, according to rendering intent. These mappings allow a choice between closest possible color matching, and remapping the entire color range to allow for different gamuts.

The reference illuminant of the Profile connection space (PCS) is a 16-bit fractional approximation of D50; its white point is XYZ=(0.9642, 1.000, 0.8249). Different source/destination white points are adapted using the Bradford transformation.

Another kind of profile is the device link profile. Instead of mapping between a device color space and a PCS, it maps between two specific device spaces. While this is less flexible, it allows for a more accurate or purposeful conversion of color between devices. For example, a conversion between two CMYK devices could ensure that colors using only black ink convert to target colors using only black ink.

## References in standards

The ICC profile specification, currently being progressed as International Standard ISO 15076-1:2005, is widely referred to in other standards. The following International and *de facto* standards are known to make reference to ICC profiles.

### International standards

- ISO/IEC 10918-1: Coding of still pictures – JPEG
- ISO 12234-2: Electronic still-picture imaging – Removable memory – Part 2: TIFF/EP image data format (ISO TC42)
- ISO 12639:2004 Graphic technology – Prepress digital data exchange – Tag Image File Format for Image Technology (TIFF/IT) (ISO TC130)
- ISO/DIS 12647-1: Graphic Technology – Process control for the production of halftone color separations, proof and production prints – part 1: Parameters and measurement methods (Revision under way in ISO TC130)
- ISO/DIS 12647-2: Graphic Technology – Process control for the production of halftone color separations, proof and production prints – part 2: Offset processes (Revision under way in ISO TC130)
- ISO/CD 12647-3: Graphic technology – Process control for the production of half-tone color separations, proofs and production prints – Part 3: Coldset offset lithography on newsprint
- ISO/CD 12647-4: Graphic technology – Process control for the production of half-tone color separations, proof and production prints – Part 4: Publication gravure printing
- ISO/CD 12647-6: Graphic technology – Process control for the production of half-tone color separations, proof and production prints – Part 6: Flexographic printing
- ISO/IEC 15948: Portable Network Graphics file format (jointly defined with W3C – see www.libpng.org/pub/png/spec/iso)
- ISO/IEC15444: Coding of still pictures – JPEG2000 (ISO JTC 1/SC 2)
- ISO 15930-1:2001 Graphic technology – Prepress digital data exchange – Use of PDF. Part 1: Complete exchange using CMYK data (PDF/X-1 and PDF/X-1a) (ISO TC130)
- ISO 15930-3:2002 Graphic technology – Prepress digital data exchange – Use of PDF. Part 3: Complete exchange suitable for color managed workflows (PDF/X-3) (ISO TC130)
- ISO 15930-4:2003 Graphic technology – Prepress digital data exchange using PDF – Part 4: Complete exchange of CMYK and spot color printing data using PDF 1.4 (PDF/X-1a)
- ISO 15930-5:2003 Graphic technology – Prepress digital data exchange using PDF – Part 5: Partial exchange of printing data using PDF 1.4 (PDF/X-2)
- ISO 15930-6:2003 Graphic technology – Prepress digital data exchange using PDF – Part 6: Complete exchange of printing data suitable for color-managed workflows using PDF 1.4 (PDF/X-3)
- ISO 22028-1:2004 Photography and Graphic Technology – Extended color encodings for digital image storage, manipulation and interchange – Part 1: Architecture and requirements (ISO TC42)
- ISO 12052 / NEMA PS3 Digital Imaging and Communications in Medicine (DICOM)
- ISO 32000-2 PDF Portable Document Format (international standard; originally authored by Adobe Systems, Inc.)

### De facto standards

- PICT standard specifications (file format published by Apple Computer Inc.)
- PostScript Language (EPS file format published by Adobe Systems Inc.)
- JDF v1.1 Revision A (Job Definition format published by the CIP4 consortium available)
- SVG (Scalable Vector Graphics) version 1.1 (file format defined by W3C available from https://www.w3.org/TR/SVG/)
- SWOP (Specifications for Web Offset Publications), used for CMYK print jobs, primarily in the United States
