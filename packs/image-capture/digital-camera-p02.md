---
title: "Digital camera (part 2/2)"
source: https://en.wikipedia.org/wiki/Digital_camera
domain: image-capture
license: CC-BY-SA-4.0
tags: image capture api, camera photo capture, grab video frame, camera track settings
fetched: 2026-07-02
part: 2/2
---

## Image data storage

Many camera phones and most stand alone digital cameras store image data in flash memory cards or other removable media. Most stand-alone cameras use SD format, while a few use CompactFlash, CFexpress or other types. In January 2012, a faster XQD card format was announced. In early 2014, some high end cameras have two hot-swappable memory slots. Photographers can swap one of the memory card with camera-on. Each memory slot can accept either Compact Flash or SD Card. All new Sony cameras also have two memory slots, one for its Memory Stick and one for SD Card, but not hot-swapable.

The approximate count of remaining photos until space exhaustion is calculated by the firmware throughout use and indicated in the viewfinder, to prepare the user for an impending necessary hot swap of the memory card, and/or file offload.

A few cameras used other removable storage such as Microdrives (very small hard disk drives), CD single (185 MB), and 3.5" floppy disks (e. g. Sony Mavica). Other unusual formats include:

- Onboard (internal) flash memory — Cheap cameras and cameras secondary to the device's main use (such as a camera phone). Some have small capacities such as 100 Megabytes and less, where intended use is buffer storage for uninterrupted operation during a memory card hot swap.
- SuperDisk (LS120) used in two Panasonic digital cameras, the PV-SD4090 and PV-SD5000, which allowed them to use both SuperDisk and 3.5" floppy disks
- PC Card hard drives – early professional cameras (discontinued)
- PC Card flash memory cards
- Thermal printer — known only in the Casio Petit Colle ZR-1 and ZR-10 which printed images immediately rather than storing
- Zink technology — printing images immediately rather than storing
- PocketZip — media used in the Agfa ePhoto CL30 Clik!

- (Mini CD) Mini CD
- (Microdrive (CF-II)) Microdrive (CF-II)
- (USB flash drive) USB flash drive
- (3.5" floppy disks) 3.5" floppy disks
- (Sony's Proprietary Memory Stick) Sony's Proprietary Memory Stick

Most manufacturers of digital cameras do not provide drivers and software to allow their cameras to work with Linux or other free software. Still, many cameras use the standard USB mass storage and/or Media Transfer Protocol, and are thus widely supported. Other cameras are supported by the gPhoto project, and many computers are equipped with a memory card reader.

### File formats

The Joint Photography Experts Group standard (JPEG) is the most common file format for storing image data. Other file types include Tagged Image File Format (TIFF), High Efficiency Image File Format (HEIF), and various Raw image formats.

Many cameras, especially high-end ones, support a raw image format. A raw image is the unprocessed set of pixel data directly from the camera's sensor, often saved in a proprietary format. Adobe Systems has released the DNG format, a royalty-free raw image format used by at least 10 camera manufacturers.

Raw files initially had to be processed in specialized image editing programs, but over time many mainstream editing programs, such as Google's Picasa, have added support for raw images. Rendering to standard images from raw sensor data allows more flexibility in making major adjustments without losing image quality or retaking the picture.

Formats for movies are AVI, DV, MPEG, MOV (often containing motion JPEG), WMV, and ASF (basically the same as WMV). Recent formats include MP4, which is based on the QuickTime format and uses newer compression algorithms to allow longer recording times in the same space.

Other formats that are used in cameras (but not for pictures) are the Design Rule for Camera Format (DCF), an ISO specification, used in almost all camera since 1998, which defines an internal file structure and naming. Also used is the Digital Print Order Format (DPOF), which dictates what order images are to be printed in and how many copies. The DCF 1998 defines a logical file system with 8.3 filenames and makes the usage of either FAT12, FAT16, FAT32 or exFAT mandatory for its physical layer to maximize platform interoperability.

Most cameras include Exif data that provides metadata about the picture. Exif data may include aperture, exposure time, focal length, date and time taken. Some are able to tag the location.

### Directory and file structure

To guarantee interoperability, DCF specifies the file system for image and sound files to be used on formatted DCF media (like removable or non-removable memory) as FAT12, FAT16, FAT32, or exFAT. Media with a capacity of more than 2 GB must be formatted using FAT32 or exFAT.

The filesystem in a digital camera contains a **DCIM** (**Digital Camera IMages**) directory, which can contain multiple subdirectories with names such as "123ABCDE" that consist of a unique directory number (in the range 100...999) and five alphanumeric characters, which may be freely chosen and often refer to a camera maker. These directories contain files with names such as "ABCD1234.JPG" that consist of four alphanumeric characters (often "100_", "DSC0", "DSCF", "IMG_", "MOV_", or "P000"), followed by a number. Handling of directories with possibly user-created duplicate numbers may vary among camera firmwares.

DCF 2.0 adds support for DCF optional files recorded in an optional color space (that is, Adobe RGB rather than sRGB). Such files must be indicated by a leading "_" (as in "_DSC" instead of "100_" or "DSC0").

### Thumbnail files

To enable loading many images in miniature view quickly and efficiently, and to retain meta data, some vendors' firmwares generate accompanying low-resolution thumbnail files for videos and raw photos. For example, those of Canon cameras end with `.THM`. JPEG can already store a thumbnail image standalone.


## Batteries

Digital cameras have become smaller over time, resulting in an ongoing need to develop a battery small enough to fit in the camera and yet able to power it for a reasonable length of time.

Digital cameras use either proprietary or standard consumer batteries. As of March 2014, most cameras use proprietary lithium-ion batteries while some use standard AA batteries or primarily use a proprietary Lithium-ion rechargeable battery pack but have an optional AA battery holder available.

### Proprietary

The most common class of battery used in digital cameras is proprietary battery formats. These are built to a manufacturer's custom specifications. Almost all proprietary batteries are lithium-ion. In addition to being available from the OEM, aftermarket replacement batteries are commonly available for most camera models.

### Standard consumer batteries

Digital cameras which use off-the-shelf batteries are typically designed to be able to use both single-use disposable and rechargeable batteries, but not with both types in use at the same time. The most common off-the-shelf battery size used is AA. CR2, CR-V3 batteries, and AAA batteries are also used in some cameras. The CR2 and CR-V3 batteries are lithium based, intended for a single use. Rechargeable RCR-V3 lithium-ion batteries are also available as an alternative to non-rechargeable CR-V3 batteries.

Some battery grips for DSLRs come with a separate holder to accommodate AA cells as an external power source.


## Conversion of film cameras to digital

When digital cameras became common, many photographers asked whether their film cameras could be converted to digital. The answer was not immediately clear, as it differed among models. For the majority of 35 mm film cameras the answer is no, the reworking and cost would be too great, especially as lenses have been evolving as well as cameras. For most a conversion to digital, to give enough space for the electronics and allow a liquid crystal display to preview, would require removing the back of the camera and replacing it with a custom built digital unit.

Many early professional SLR cameras, such as the Kodak DCS series, were developed from 35 mm film cameras. The technology of the time, however, meant that rather than being digital "backs" the bodies of these cameras were mounted on large, bulky digital units, often bigger than the camera portion itself. These were factory built cameras, however, not aftermarket conversions.

A notable exception is the Nikon E2 and Nikon E3, using additional optics to convert the 35 mm format to a 2/3 CCD-sensor.

A few 35 mm cameras have had digital camera backs made by their manufacturer, Leica being a notable example with the Leica R8–R9. Medium format and large format cameras (those using film stock greater than 35 mm), have a low unit production, and typical digital backs for them cost over $10,000. These cameras also tend to be highly modular, with handgrips, film backs, winders, and lenses available separately to fit various needs.

The very large sensor these backs use leads to enormous image sizes. For example, Phase One's P45 39 MP image back creates a single TIFF image of size up to 224.6 MB, and even greater pixel counts are available. Medium format digitals such as this are geared more towards studio and portrait photography than their smaller DSLR counterparts; the ISO speed in particular tends to have a maximum of 400, versus 6400 for some DSLR cameras. (Canon EOS-1D Mark IV and Nikon D3S have ISO 12800 plus Hi-3 ISO 102400 with the Canon EOS-1Dx's ISO of 204800).

### Digital camera backs

In the industrial and high-end professional photography market, some camera systems use modular (removable) image sensors. For example, some medium format SLR cameras, such as the Mamiya 645D series, allow installation of either a digital camera back or a traditional photographic film back.

- Area array
  - CCD
  - CMOS
- Linear array
  - CCD (monochrome)
  - 3-strip CCD with color filters

Linear array cameras are also called scan backs.

- Single-shot
- Multi-shot (three-shot, usually)

Most earlier digital camera backs used linear array sensors, moving vertically to digitize the image. Many of them only capture grayscale images. The relatively long exposure times, in the range of seconds or even minutes generally limit scan backs to studio applications, where all aspects of the photographic scene are under the photographer's control.

Some other camera backs use CCD arrays similar to typical cameras. These are called single-shot backs.

Since it is much easier to manufacture a high-quality linear CCD array with only thousands of pixels than a CCD matrix with millions, very high resolution linear CCD camera backs were available much earlier than their CCD matrix counterparts. For example, you could buy an (albeit expensive) camera back with over 7,000 pixel horizontal resolution in the mid-1990s. However, as of 2004, it is still difficult to buy a comparable CCD matrix camera of the same resolution. Rotating line cameras, with about 10,000 color pixels in its sensor line, are able, as of 2005, to capture about 120,000 lines during one full 360-degree rotation, thereby creating a single digital image of 1,200 Megapixels.

Most modern digital camera backs use CCD or CMOS matrix sensors. The matrix sensor captures the entire image frame at once, instead of incrementing scanning the frame area through the prolonged exposure. For example, Phase One produces a 39 million pixel digital camera back with a 49.1 × 36.8 mm CCD in 2008. This CCD array is a little smaller than a frame of 120 film and much larger than a 35 mm frame (36 × 24 mm). In comparison, consumer digital cameras use arrays ranging from 36 × 24 mm (full frame on high end consumer DSLRs) to 1.28 × 0.96 mm (on camera phones) CMOS sensor.
