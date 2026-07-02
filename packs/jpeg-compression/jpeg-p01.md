---
title: "JPEG (part 1/2)"
source: https://en.wikipedia.org/wiki/JPEG
domain: jpeg-compression
license: CC-BY-SA-4.0
tags: jpeg compression, discrete cosine transform, jpeg 2000, lossy image
fetched: 2026-07-02
part: 1/2
---

# JPEG

Checked


## Page version status

This is an accepted version of this page

This is the

latest accepted revision

,

reviewed

on

16 June 2026

.

**JPEG** (/ˈdʒeɪpɛɡ/ *JAY-peg*, short for **Joint Photographic Experts Group** and sometimes retroactively referred to as **JPEG 1**) is a commonly used method of lossy compression for digital images, particularly for those images produced by digital photography. The degree of compression can be adjusted, allowing a selectable trade off between storage size and image quality. JPEG typically achieves 10:1 compression with a loss in image quality that, while perceptible, is widely agreed upon to be acceptable. Since its introduction in 1992, JPEG has been the most widely used image compression standard in the world, and the most widely used digital image format, with several billion JPEG images produced every day as of 2015.

The Joint Photographic Experts Group created the standard in 1992, based on the discrete cosine transform (DCT) algorithm. JPEG was largely responsible for the proliferation of digital images and digital photos across the Internet and later social media. JPEG compression is used in a number of image file formats. JPEG/Exif is the most common image format used by digital cameras and other photographic image capture devices; along with JPEG/JFIF, it is the most common format for storing and transmitting photographic images on the World Wide Web. These format variations are often not distinguished and are simply called JPEG.

The MIME media type for JPEG is "image/jpeg", except in older Internet Explorer versions, which provide a MIME type of "image/pjpeg" when uploading JPEG images. JPEG files usually have a filename extension of "jpg" or "jpeg". JPEG/JFIF supports a maximum image size of 65,535×65,535 pixels, hence up to 4 gigapixels for an aspect ratio of 1:1. In 2000, the JPEG group introduced a format intended to be a successor, JPEG 2000, but it was unable to replace the original JPEG as the dominant image standard.


## History

### Background

The original JPEG specification published in 1992 implements processes from various earlier research papers and patents cited by the CCITT (now ITU-T) and Joint Photographic Experts Group.

The basis for JPEG's lossy compression algorithm is the discrete cosine transform (DCT), which was first proposed by Nasir Ahmed as an image compression technique in 1972. Ahmed published the DCT algorithm with T. Natarajan and K. R. Rao in a 1974 paper, which is cited in the JPEG specification.

The JPEG specification cites patents from several companies. The following patents provided the basis for its arithmetic coding algorithm.

- IBM
  - U.S. patent 4,652,856 – 4 February 1986 – Kottappuram M. A. Mohiuddin and Jorma J. Rissanen – Multiplication-free multi-alphabet arithmetic code
  - U.S. patent 4,905,297 – 27 February 1990 – G. Langdon, J. L. Mitchell, W. B. Pennebaker, and Jorma J. Rissanen – Arithmetic coding encoder and decoder system
  - U.S. patent 4,935,882 – 19 June 1990 – W. B. Pennebaker and J. L. Mitchell – Probability adaptation for arithmetic coders
- Mitsubishi Electric
  - JP H02202267  (1021672) – 21 January 1989 – Toshihiro Kimura, Shigenori Kino, Fumitaka Ono, Masayuki Yoshida – Coding system
  - JP H03247123  (2-46275) – 26 February 1990 – Tomohiro Kimura, Shigenori Kino, Fumitaka Ono, and Masayuki Yoshida – Coding apparatus and coding method

The JPEG specification also cites three other patents from IBM. Other companies cited as patent holders include AT&T (two patents) and Canon Inc. Absent from the list is U.S. patent 4,698,672, filed by Compression Labs' Wen-Hsiung Chen and Daniel J. Klenke in October 1986. The patent describes a DCT-based image compression algorithm, and would later be a cause of controversy in 2002 (see *Patent controversy* below). However, the JPEG specification did cite two earlier research papers by Wen-Hsiung Chen, published in 1977 and 1984.

### JPEG standard

"JPEG" stands for Joint Photographic Experts Group, the name of the committee that created the JPEG standard and other still picture coding standards. The "Joint" stood for ISO TC97 WG8 and CCITT SGVIII. Founded in 1986, the group developed the JPEG standard during the late 1980s. The group published the JPEG standard in 1992.

In 1987, ISO TC 97 became ISO/IEC JTC 1 and, in 1992, CCITT became ITU-T. Currently on the JTC1 side, JPEG is one of two sub-groups of ISO/IEC Joint Technical Committee 1, Subcommittee 29, Working Group 1 (ISO/IEC JTC 1/SC 29/WG 1) – titled as *Coding of still pictures*. On the ITU-T side, ITU-T SG16 is the respective body. The original JPEG Group was organized in 1986, issuing the first JPEG standard in 1992, which was approved in September 1992 as **ITU-T Recommendation T.81** and, in 1994, as **ISO/IEC 10918-1**.

The JPEG standard specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image, but not the file format used to contain that stream. The Exif and JFIF standards define the commonly used file formats for interchange of JPEG-compressed images.

JPEG standards are formally named as *Information technology – Digital compression and coding of continuous-tone still images*. ISO/IEC 10918 consists of the following parts:

| Part | ISO/IEC standard | ITU-T Rec. | First public release date | Latest amendment | Title | Description |
|---|---|---|---|---|---|---|
| Part 1 | ISO/IEC 10918-1:1994 | T.81 (09/92) | Sep 18, 1992 |   | Requirements and guidelines |   |
| Part 2 | ISO/IEC 10918-2:1995 | T.83 (11/94) | Nov 11, 1994 |   | Compliance testing | Rules and checks for software conformance (to Part 1). |
| Part 3 | ISO/IEC 10918-3:1997 | T.84 (07/96) | Jul 3, 1996 | Apr 1, 1999 | Extensions | Set of extensions to improve the Part 1, including the **Still Picture Interchange File Format** (SPIFF). |
| Part 4 | ISO/IEC 10918-4:2024 | T.86 (06/98) | Jun 18, 1998 |   | Appn Markers | methods for registering some of the parameters used to extend JPEG |
| Part 5 | ISO/IEC 10918-5:2013 | T.871 (05/11) | May 14, 2011 |   | JPEG File Interchange Format (JFIF) | A popular format which has been the de facto file format for images encoded by the JPEG standard. In 2009, the JPEG Committee formally established an Ad Hoc Group to standardize JFIF as JPEG Part 5. |
| Part 6 | ISO/IEC 10918-6:2013 | T.872 (06/12) | Jun 2012 |   | Application to printing systems | Specifies a subset of features and application tools for the interchange of images encoded according to the ISO/IEC 10918-1 for printing. |
| Part 7 | ISO/IEC 10918-7:2023 | T.873 (06/21) | May 2019 | November 2023 | Reference Software | Provides reference implementations of the JPEG core coding system |

Ecma International TR/98 specifies the JPEG File Interchange Format (JFIF); the first edition was published in June 2009.

### Patent controversy

In 2002, Forgent Networks asserted that it owned and would enforce patent rights on the JPEG technology, arising from a patent that had been filed on 27 October 1986, and granted on 6 October 1987: U.S. patent 4,698,672 by Compression Labs' Wen-Hsiung Chen and Daniel J. Klenke. While Forgent did not own Compression Labs at the time, Chen later sold Compression Labs to Forgent, before Chen went on to work for Cisco. This led to Forgent acquiring ownership over the patent. Forgent's 2002 announcement created a furor reminiscent of Unisys' attempts to assert its rights over the GIF image compression standard.

The JPEG committee investigated the patent claims in 2002 and were of the opinion that they were invalidated by prior art, a view shared by various experts.

Between 2002 and 2004, Forgent was able to obtain about US$105 million by licensing their patent to some 30 companies. In April 2004, Forgent sued 31 other companies to enforce further license payments. In July of the same year, a consortium of 21 large computer companies filed a countersuit, with the goal of invalidating the patent. In addition, Microsoft launched a separate lawsuit against Forgent in April 2005. In February 2006, the United States Patent and Trademark Office agreed to re-examine Forgent's JPEG patent at the request of the Public Patent Foundation. On 26 May 2006, the USPTO found the patent invalid based on prior art. The USPTO also found that Forgent knew about the prior art, yet it intentionally avoided telling the Patent Office. This made any appeal to reinstate the patent highly unlikely to succeed.

Forgent also possesses a similar patent granted by the European Patent Office in 1994, though it is unclear how enforceable it is.

As of 27 October 2006, the U.S. patent's 20-year term appears to have expired, and in November 2006, Forgent agreed to abandon enforcement of patent claims against use of the JPEG standard.

The JPEG committee has as one of its explicit goals that their standards (in particular their baseline methods) be implementable without payment of license fees, and they have secured appropriate license rights for their JPEG 2000 standard from over 20 large organizations.

Beginning in August 2007, another company, Global Patent Holdings, LLC claimed that its patent (U.S. patent 5,253,341) issued in 1993, is infringed by the downloading of JPEG images on either a website or through e-mail. If not invalidated, this patent could apply to any website that displays JPEG images. The patent was under reexamination by the U.S. Patent and Trademark Office from 2000 to 2007; in July 2007, the Patent Office revoked all of the original claims of the patent but found that an additional claim proposed by Global Patent Holdings (claim 17) was valid. Global Patent Holdings then filed a number of lawsuits based on claim 17 of its patent.

In its first two lawsuits following the reexamination, both filed in Chicago, Illinois, Global Patent Holdings sued the Green Bay Packers, CDW, Motorola, Apple, Orbitz, OfficeMax, Caterpillar, Kraft and Peapod as defendants. A third lawsuit was filed on 5 December 2007, in South Florida against ADT Security Services, AutoNation, Florida Crystals Corp., HearUSA, MovieTickets.com, Ocwen Financial Corp. and Tire Kingdom, and a fourth lawsuit on 8 January 2008, in South Florida against the Boca Raton Resort & Club. A fifth lawsuit was filed against Global Patent Holdings in Nevada. That lawsuit was filed by Zappos.com, Inc., which was allegedly threatened by Global Patent Holdings, and sought a judicial declaration that the '341 patent is invalid and not infringed.

Global Patent Holdings had also used the '341 patent to sue or threaten outspoken critics of broad software patents, including Gregory Aharonian and the anonymous operator of a website blog known as the "Patent Troll Tracker." On 21 December 2007, patent lawyer Vernon Francissen of Chicago asked the U.S. Patent and Trademark Office to reexamine the sole remaining claim of the '341 patent on the basis of new prior art.

On 5 March 2008, the U.S. Patent and Trademark Office agreed to reexamine the '341 patent, finding that the new prior art raised substantial new questions regarding the patent's validity. In light of the reexamination, the accused infringers in four of the five pending lawsuits have filed motions to suspend (stay) their cases until completion of the U.S. Patent and Trademark Office's review of the '341 patent. On 23 April 2008, a judge presiding over the two lawsuits in Chicago, Illinois granted the motions in those cases. On 22 July 2008, the Patent Office issued the first "Office Action" of the second reexamination, finding the claim invalid based on nineteen separate grounds. On 24 November 2009, a Reexamination Certificate was issued cancelling all claims.

Beginning in 2011 and continuing as of early 2013, an entity known as Princeton Digital Image Corporation, based in Eastern Texas, began suing large numbers of companies for alleged infringement of U.S. patent 4,813,056. Princeton claims that the JPEG image compression standard infringes the '056 patent and has sued large numbers of websites, retailers, camera and device manufacturers and resellers. The patent was originally owned and assigned to General Electric. The patent expired in December 2007, but Princeton has sued large numbers of companies for "past infringement" of this patent. (Under U.S. patent laws, a patent owner can sue for "past infringement" up to six years before the filing of a lawsuit, so Princeton could theoretically have continued suing companies until December 2013.) As of March 2013, Princeton had suits pending in New York and Delaware against more than 55 companies. General Electric's involvement in the suit is unknown, although court records indicate that it assigned the patent to Princeton in 2009 and retains certain rights in the patent.


## Typical use

The JPEG compression algorithm operates at its best on photographs and paintings of realistic scenes with smooth variations of tone and color. For web usage, where reducing the amount of data used for an image is important for responsive presentation, JPEG's compression benefits make JPEG popular. JPEG/Exif is also the most common format saved by digital cameras.

However, JPEG is not well suited for line drawings and other textual or iconic graphics, where the sharp contrasts between adjacent pixels can cause noticeable artifacts. Such images are better saved in a lossless graphics format such as TIFF, GIF, PNG, or a raw image format. The JPEG standard includes a lossless coding mode, but that mode is not supported in most products.

As the typical use of JPEG is a lossy compression method, which reduces the image fidelity, it is inappropriate for exact reproduction of imaging data (such as some scientific and medical imaging applications and certain technical image processing work).

JPEG is also not well suited to files that will undergo multiple edits, as some image quality is lost each time the image is recompressed, particularly if the image is cropped or shifted, or if encoding parameters are changed – see digital generation loss for details. To prevent image information loss during sequential and repetitive editing, the first edit can be saved in a lossless format, subsequently edited in that format, then finally published as JPEG for distribution.


## JPEG compression

JPEG uses a lossy form of compression based on the discrete cosine transform (DCT). This mathematical operation converts each frame/field of the video source from the spatial (2D) domain into the frequency domain (a.k.a. transform domain). A perceptual model based loosely on how the human psychovisual system discards high-frequency information, i.e. sharp transitions in intensity, and color hue. In the transform domain, the process of reducing information is called quantization. In simpler terms, quantization is a method for optimally reducing a large number scale (with different occurrences of each number) into a smaller one, and the transform-domain is a convenient representation of the image because the high-frequency coefficients, which contribute less to the overall picture than other coefficients, are characteristically small-values with high compressibility. The quantized coefficients are then sequenced and losslessly packed into the output bitstream. Nearly all software implementations of JPEG permit user control over the compression ratio (as well as other optional parameters), allowing the user to trade off picture-quality for smaller file size. In embedded applications (such as miniDV, which uses a similar DCT-compression scheme), the parameters are pre-selected and fixed for the application.

The compression method is usually lossy, meaning that some original image information is lost and cannot be restored, possibly affecting image quality. There is an optional lossless mode defined in the JPEG standard. However, this mode is not widely supported in products.

There is also an interlaced *progressive* JPEG format, in which data is compressed in multiple passes of progressively higher detail. This is ideal for large images that will be displayed while downloading over a slow connection, allowing a reasonable preview after receiving only a portion of the data. However, support for progressive JPEGs is not universal. When progressive JPEGs are received by programs that do not support them (such as versions of Internet Explorer before Windows 7) the software displays the image only after it has been completely downloaded.

There are also many medical imaging, traffic and camera applications that create and process 12-bit JPEG images both grayscale and color. 12-bit JPEG format is included in an Extended part of the JPEG specification. The libjpeg codec supports 12-bit JPEG and there even exists a high-performance version.

### Lossless editing

Several alterations to a JPEG image can be performed losslessly (that is, without recompression and the associated quality loss) as long as the image size is a multiple of 1 MCU block (Minimum Coded Unit) (usually 16 pixels in both directions, for 4:2:0 chroma subsampling). Utilities that implement this include:

- jpegtran and its GUI, Jpegcrop.
- IrfanView using "JPG Lossless Crop (PlugIn)" and "JPG Lossless Rotation (PlugIn)", which require installing the JPG_TRANSFORM plugin.
- FastStone Image Viewer using "Lossless Crop to File" and "JPEG Lossless Rotate".
- XnViewMP using "JPEG lossless transformations".
- ACDSee supports lossless rotation (but not lossless cropping) with its "Force lossless JPEG operations" option.

Blocks can be rotated in 90-degree increments, flipped in the horizontal, vertical and diagonal axes and moved about in the image. Not all blocks from the original image need to be used in the modified one.

The top and left edge of a JPEG image must lie on an 8 × 8 pixel block boundary (or 16 × 16 pixel for larger MCU sizes), but the bottom and right edge need not do so. This limits the possible **lossless crop** operations, and prevents flips and rotations of an image whose bottom or right edge does not lie on a block boundary for all channels (because the edge would end up on top or left, where – as aforementioned – a block boundary is obligatory).

Rotations where the image is not a multiple of 8 or 16, which value depends upon the chroma subsampling, are not lossless. Rotating such an image causes the blocks to be recomputed which results in loss of quality.

When using lossless cropping, if the bottom or right side of the crop region is not on a block boundary, then the rest of the data from the partially used blocks will still be present in the cropped file and can be recovered. It is also possible to transform between baseline and progressive formats without any loss of quality, since the only difference is the order in which the coefficients are placed in the file.

Furthermore, several JPEG images can be losslessly joined, as long as they were saved with the same quality and the edges coincide with block boundaries.


## JPEG files

The file format known as "JPEG Interchange Format" (JIF) is specified in Annex B of the standard. However, this "pure" file format is rarely used, primarily because of the difficulty of programming encoders and decoders that fully implement all aspects of the standard and because of certain shortcomings of the standard:

- Color space definition
- Component sub-sampling registration
- Pixel aspect ratio definition.

Several additional standards have evolved to address these issues. The first of these, released in 1992, was the JPEG File Interchange Format (JFIF), followed in recent years by Exchangeable image file format (Exif) and ICC color profiles. Both of these formats use the actual JIF byte layout, consisting of different *markers*, but in addition, employ one of the JIF standard's extension points, namely the *application markers*: JFIF uses APP0, while Exif uses APP1. Within these segments of the file that were left for future use in the JIF standard and are not read by it, these standards add specific metadata.

Thus, in some ways, JFIF is a cut-down version of the JIF standard in that it specifies certain constraints (such as not allowing all the different encoding modes), while in other ways, it is an extension of JIF due to the added metadata. The documentation for the original JFIF standard states:

> JPEG File Interchange Format is a minimal file format which enables JPEG bitstreams to be exchanged between a wide variety of platforms and applications. This minimal format does not include any of the advanced features found in the TIFF JPEG specification or any application specific file format. Nor should it, for the only purpose of this simplified format is to allow the exchange of JPEG compressed images.

Image files that employ JPEG compression are commonly called "JPEG files", and are stored in variants of the JIF image format. Most image capture devices (such as digital cameras) that output JPEG are actually creating files in the Exif format, the format that the camera industry has standardized on for metadata interchange. On the other hand, since the Exif standard does not allow color profiles, most image editing software stores JPEG in JFIF format, and includes the APP1 segment from the Exif file to include the metadata in an almost-compliant way; the JFIF standard is interpreted somewhat flexibly.

Strictly speaking, the JFIF and Exif standards are incompatible, because each specifies that its marker segment (APP0 or APP1, respectively) appear first. In practice, most JPEG files contain a JFIF marker segment that precedes the Exif header. This allows older readers to correctly handle the older format JFIF segment, while newer readers also decode the following Exif segment, being less strict about requiring it to appear first.

### JPEG filename extensions

The most common filename extensions for files employing JPEG compression are **`.jpg`** and **`.jpeg`**, though `.jpe`, `.jfif` and `.jif` are also used. It is also possible for JPEG data to be embedded in other file types – TIFF encoded files often embed a JPEG image as a thumbnail of the main image; and MP3 files can contain a JPEG of cover art in the ID3v2 tag.

### Color profile

Many JPEG files embed an ICC color profile (color space). Commonly used color profiles include sRGB and Adobe RGB. Because these color spaces use a non-linear transformation, the dynamic range of an 8-bit JPEG file is about 11 stops; see gamma curve.

If the image doesn't specify color profile information (*untagged*), the color space is assumed to be sRGB for the purposes of display on webpages.


## Syntax and structure

A JPEG image consists of a sequence of *segments*, each beginning with a *marker*, each of which begins with a 0xFF byte, followed by a byte indicating what kind of marker it is. Some markers consist of just those two bytes; others are followed by two bytes (high then low), indicating the length of marker-specific payload data that follows. (The length includes the two bytes for the length, but not the two bytes for the marker.) Some markers are followed by entropy-coded data; the length of such a marker does not include the entropy-coded data. Note that consecutive 0xFF bytes are used as fill bytes for padding purposes, although this fill byte padding should only ever take place for markers immediately following entropy-coded scan data (see JPEG specification section B.1.1.2 and E.1.2 for details; specifically "In all cases where markers are appended after the compressed data, optional 0xFF fill bytes may precede the marker").

Within the entropy-coded data, after any 0xFF byte, a 0x00 byte is inserted by the encoder before the next byte, so that there does not appear to be a marker where none is intended, preventing framing errors. Decoders must skip this 0x00 byte. This technique, called byte stuffing (see JPEG specification section F.1.2.3), is only applied to the entropy-coded data, not to marker payload data. Note however that entropy-coded data has a few markers of its own; specifically the Reset markers (0xD0 through 0xD7), which are used to isolate independent chunks of entropy-coded data to allow parallel decoding, and encoders are free to insert these Reset markers at regular intervals (although not all encoders do this).

| Short name | Bytes | Payload | Name | Comments |
|---|---|---|---|---|
| SOI | 0xFF, 0xD8 | *none* | Start Of Image |   |
| SOF0 | 0xFF, 0xC0 | *variable size* | Start Of Frame (baseline DCT) | Indicates that this is a baseline DCT-based JPEG, and specifies the width, height, number of components, and component subsampling (e.g., 4:2:0). |
| SOF2 | 0xFF, 0xC2 | *variable size* | Start Of Frame (progressive DCT) | Indicates that this is a progressive DCT-based JPEG, and specifies the width, height, number of components, and component subsampling (e.g., 4:2:0). |
| DHT | 0xFF, 0xC4 | *variable size* | Define Huffman Table(s) | Specifies one or more Huffman tables. |
| DQT | 0xFF, 0xDB | *variable size* | Define Quantization Table(s) | Specifies one or more quantization tables. |
| DRI | 0xFF, 0xDD | 4 bytes | Define Restart Interval | Specifies the interval between RST*n* markers, in Minimum Coded Units (MCUs). This marker is followed by two bytes indicating the fixed size so it can be treated like any other variable size segment. |
| SOS | 0xFF, 0xDA | *variable size* | Start Of Scan | Begins a top-to-bottom scan of the image. In baseline DCT JPEG images, there is generally a single scan. Progressive DCT JPEG images usually contain multiple scans. This marker specifies which slice of data it will contain, and is immediately followed by entropy-coded data. |
| RST*n* | 0xFF, 0xD*n* (*n*=0..7) | *none* | Restart | Inserted every *r* macroblocks, where *r* is the restart interval set by a DRI marker. Not used if there was no DRI marker. The low three bits of the marker code cycle in value from 0 to 7. |
| APP*n* | 0xFF, 0xE*n* | *variable size* | Application-specific | For example, an Exif JPEG file uses an APP1 marker to store metadata, laid out in a structure based closely on TIFF. |
| COM | 0xFF, 0xFE | *variable size* | Comment | Contains a text comment. |
| EOI | 0xFF, 0xD9 | *none* | End Of Image |   |

There are other *Start Of Frame* markers that introduce other kinds of JPEG encodings.

Since several vendors might use the same APP*n* marker type, application-specific markers often begin with a standard or vendor name (e.g., "Exif" or "Adobe") or some other identifying string.

At a restart marker, block-to-block predictor variables are reset, and the bitstream is synchronized to a byte boundary. Restart markers provide means for recovery after bitstream error, such as transmission over an unreliable network or file corruption. Since the runs of macroblocks between restart markers may be independently decoded, these runs may be decoded in parallel.
