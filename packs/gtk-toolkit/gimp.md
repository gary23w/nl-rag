---
title: "GIMP"
source: https://en.wikipedia.org/wiki/GIMP
domain: gtk-toolkit
license: CC-BY-SA-4.0
tags: gtk toolkit, gobject type system, glib library, gnome widgets
fetched: 2026-07-02
---

# GIMP

The **GNU Image Manipulation Program**, commonly known by its acronym **GIMP** (/ɡɪmp/ ⓘ *GHIMP*; always stylized in capitals; formerly, **The GIMP**), is a free and open-source raster graphics editor.

It is commonly used for photo retouching, image editing, free-hand drawing, and converting between different image file formats.

GIMP is freely available on Microsoft Windows, Linux and macOS. It is licensed under the GNU General Public License (GPL 3.0 or later). The project is a non-profit supported by a community of volunteers. Users are encouraged to contribute.

GIMP supports plugins and scripting, allowing users to extend its features and automate tasks. While it is not primarily designed for drawing, some artists and creators still use it for that purpose.

## History

In 1995, Spencer Kimball and Peter Mattis began developing GIMP as a semester project at University of California, Berkeley for the eXperimental Computing Facility*.* The software was originally named the General Image Manipulation Program. Kimball and Mattis formed the acronym GIMP by adding the letter G to "-IMP," inspired by a reference to "the gimp" in the 1994 film *Pulp Fiction*.

GIMP's first public release, version 0.54, came out in 1996. It attracted many users, and a community of contributors grew around it. These contributors produced tutorials, shared artwork, and introduced improved workflows and techniques.

During a visit to UC Berkeley in 1997, Richard Stallman of the GNU Project met with Kimball and Mattis where they asked him if they could change "General" in the program's name to "GNU". Stallman approved, and GIMP became part of the GNU software collection.

The initial release worked only on Unix-based systems such as Linux, SGI IRIX and HP-UX. Since then, GIMP has been ported to other operating systems, including Microsoft Windows (1997, GIMP 1.1) and macOS.

A GUI toolkit called GTK (at the time known as the GIMP ToolKit) was developed to facilitate the development of GIMP. The development of the GIMP ToolKit has been attributed to Peter Mattis becoming disenchanted with the Motif toolkit GIMP originally used. Motif was used up to GIMP 0.60.

### Mascot

Wilber, the official mascot of GIMP, was created using GIMP by Tuomas Kuosmanen, known as *tigert*, on 25 September 1997.

Over time, other GIMP developers contributed additional accessories for Wilber, which are included in the *Wilber Construction Kit*. The kit is available in GIMP's source code at `/docs/Wilber_Construction_Kit.xcf.gz`.

## Development

GIMP is primarily developed by volunteers as a free and open source software project associated with both the GNU and GNOME projects. Development takes place in a public git source code repository, on public mailing lists and in public chat channels on the GIMPNET IRC network.

New features are held in public separate source code branches and merged into the main (or development) branch when the GIMP team is sure they won't damage existing functions. Sometimes this means that features that appear complete do not get merged or take months or years before they become available in GIMP.

GIMP itself is released as source code. After a source code release, installers and packages are made for different operating systems by parties who might not be in contact with the maintainers of GIMP.

The version number used in GIMP is expressed in a *major-minor-micro* format, with each number carrying a specific meaning: the first (major) number is incremented only for major developments (and is currently 3). The second (minor) number is incremented with each release of new features, with odd numbers reserved for in-progress development versions and even numbers assigned to stable releases; the third (micro) number is incremented before and after each release (resulting in even numbers for releases, and odd numbers for development snapshots) with any bug fixes subsequently applied and released for a stable version.

Previously, GIMP applied for several positions in the Google Summer of Code (GSoC). From 2006 to 2009 there have been nine GSoC projects that have been listed as successful, although not all successful projects have been merged into GIMP immediately. The healing brush and perspective clone tools and Ruby bindings were created as part of the 2006 GSoC and can be used in version 2.8.0 of GIMP, although there were three other projects that were completed and are later available in a stable version of GIMP; those projects being Vector Layers (end 2008 in 2.8 and master), and a JPEG 2000 plug-in (mid 2009 in 2.8 and master). Several of the GSoC projects were completed in 2008, but have been merged into a stable GIMP release later in 2009 to 2014 for Version 2.8.xx and 2.10.x. Some of them needed some more code work for the master tree.

Second public Development 2.9-Version was 2.9.4 with many deep improvements after initial Public Version 2.9.2. Third Public 2.9-Development version is Version 2.9.6. One of the new features is removing the 4 GB size limit of XCF file. Increase of possible threads to 64 is also an important point for modern parallel execution in actual AMD Ryzen and Intel Xeon processors. Version 2.9.8 included many bug fixes and improvements in gradients and clips. Improvements in performance and optimization beyond bug hunting were the development targets for 2.10.0. MacOS Beta is available with Version 2.10.4.

The first release candidate for version 3.0, RC1, was released on 6 November 2024. After several more months of development, version 3.0 was completed and released on 16 March 2025. This represented the completion of seven years of development to complete a major overhaul of many of GIMP's features and dependencies.

GIMP developers meet during the annual Libre Graphics Meeting. Interaction designers from OpenUsability have also contributed to GIMP.

## Distribution

The current version of GIMP works with numerous operating systems, including Linux, macOS and Windows. Many Linux distributions, such as Fedora Linux and Debian, include GIMP as a part of their desktop operating systems.

GIMP began to host its own downloads after discontinuing use of SourceForge in 2013. The website later repossessed GIMP's dormant account and hosted advertising-laden versions of GIMP for Windows.

In 2022, GIMP was published on the Microsoft Store for Windows.

## Features

Tools used to perform image editing can be accessed via the toolbox, through menus and dialogue windows. They include filters and brushes, as well as transformation, selection, layer and masking tools. GIMP's developers have asserted that it has, or at least aspire to it having, similar functionality to Photoshop, but has a different user interface.

### Color

There are several ways of selecting colors, including palettes, color choosers and using an eyedropper tool to select a color on the canvas. The built-in color choosers include RGB/HSV/LAB/LCH selector or scales, water-color selector, CMYK selector and a color-wheel selector. Colors can also be selected using hexadecimal color codes, as used in HTML color selection. GIMP has native support for indexed color and RGB color spaces; other color spaces are supported using decomposition, where each channel of the new color space becomes a black-and-white image. CMYK, LAB and HSV (hue, saturation, value) are supported this way. Color blending can be achieved using the Blend tool, by applying a gradient to the surface of an image and using GIMP's color modes. Gradients are also integrated into tools such as the brush tool, when the user paints this way the output color slowly changes. There are a number of default gradients included with GIMP; a user can also create custom gradients with tools provided. Gradient plug-ins are also available.

### Selections and paths

GIMP selection tools include a rectangular and circular selection tool, free select tool, and fuzzy select tool (also known as magic wand). More advanced selection tools include the select by color tool for selecting contiguous regions of color—and the scissors select tool, which creates selections semi-automatically between areas of highly contrasting colors. GIMP also supports a quick mask mode where a user can use a brush to paint the area of a selection. Visibly this looks like a red colored overlay being added or removed. The foreground select tool is an implementation of Simple interactive object extraction (SIOX), a method used to perform the extraction of foreground elements, such as a person or a tree in focus. The Paths Tool allows a user to create vectors (also known as Bézier curves). Users can use paths to create complex selections, including around natural curves. They can paint (or "stroke") the paths with brushes, patterns, or various line styles. Users can name and save paths for reuse.

### Image editing

There are many tools that can be used for editing images in GIMP. The more common tools include a paint brush, pencil, airbrush, eraser and ink tools used to create new or blended pixels. The Bucket Fill tool can be used to fill a selection with a color or pattern. The Blend tool can be used to fill a selection with a color gradient. These color transitions can be applied to large regions or smaller custom path selections.

GIMP also provides "smart" tools that use a more complex algorithm to do things that otherwise would be time-consuming or impossible. These include:

- Clone tool, which copies pixels using a brush
- Healing brush, which copies pixels from an area and corrects tone and color
- Perspective clone tool, which works like the clone tool but corrects for distance changes
- Blur and sharpen tools
- The Smudge tool can be used to subtly smear a selection where it stands
- Dodge and burn tool is a brush that makes target pixels lighter (dodges) or darker (burns)

### Layers, layer masks and channels

An image being edited in GIMP can consist of many layers in a stack. The user manual suggests that "A good way to visualize a GIMP image is as a stack of transparencies," where in GIMP terminology, each level (analogous to a transparency) is called a layer. Each layer in an image is made up of several channels. In an RGB image, there are normally 3 or 4 channels, each consisting of a red, green and blue channel. Color sublayers look like slightly different gray images, but when put together they make a complete image. The fourth channel that may be part of a layer is the alpha channel (or layer mask). This channel measures opacity where a whole or part of an image can be completely visible, partially visible or invisible. Each layer has a layer mode that can be set to change the colors in the image.

Text layers can be created using the text tool, allowing a user to write on an image. Text layers can be transformed in several ways, such as converting them to a path or selection.

Since GIMP 3.2, there are "link layers", which are linked duplicates to external source files. Link layers automatically update changes that are made to the source files.

### Automation, scripts and plug-ins

GIMP has approximately 150 standard effects and filters, including Drop Shadow, Blur, Motion Blur and Noise.

GIMP operations can be automated with scripting languages. The Script-Fu is a Scheme-based language implemented using a TinyScheme interpreter built into GIMP. GIMP can also be scripted in Perl, Python (Python-Fu), or Tcl, using interpreters external to GIMP. New features can be added to GIMP not only by changing program code (GIMP core), but also by creating plug-ins. These are external programs that are executed and controlled by the main GIMP program. MathMap is an example of a plug-in written in C.

There is support for several methods of sharpening and blurring images, including the blur and sharpen tool. The unsharp mask tool is used to sharpen an image selectively – it sharpens only those areas of an image that are sufficiently detailed. The Unsharp Mask tool is considered to give more targeted results for photographs than a normal sharpening filter. The Selective Gaussian Blur tool works in a similar way, except it blurs areas of an image with little detail.

GIMP-ML is an extension for machine learning with 15 filters.

### GEGL

The *Generic Graphics Library* (*GEGL*) was first introduced in GIMP 2.6 to improve how the software processes images. Initially GIMP used GEGL for high bit-depth color operations, helping reduce data loss when adjusting colors.

GIMP 2.8 was limited to 8-bit color, which is much lower than the 12-bit or higher depth that most digital cameras produce. GIMP 2.10 introduced full support for high bit-depth color, and hardware acceleration was enabled through OpenCL for some tasks.

GIMP 3.0 introduces non-destructive filters, allowing users to apply effects without permanently changing the original image. This means they can be edited, toggled on or off, or removed after being applied. Third-party filters are also supported, though they will not be retained if the necessary plugins are missing.

### CTX

CTX is a rasterizer for vector graphics introduced in GIMP 3.0. It allows certain simple shapes, such as lines and circles, to be converted into vector objects.

### File formats

GIMP supports importing and exporting with a large number of different file formats. GIMP's native format XCF is designed to store all information GIMP can contain about an image; XCF is named after the e*X*perimental *C*omputing *F*acility at UC Berkeley where GIMP was authored. Import and export capability can be extended to additional file formats by means of plug-ins. XCF file size is extended to more than 4 GB since 2.9.6 and the new stable tree 2.10.x.

|   | File formats |
|---|---|
| Import and export | GIMP has import and export support for image formats such as BMP, JPEG, PNG, WebP, GIF, TIFF and HEIF, along with the file formats of several other applications such as Autodesk flic animations, Corel PaintShop Pro images, and Adobe Photoshop documents. Other formats with read/write support include PostScript documents, X bitmap image, xwd, and Zsoft PCX. GIMP can also read and write path information from SVG files and read/write ICO Windows icon files. |
| Import only | GIMP can import Adobe PDF documents and the raw image formats used by many digital cameras, but cannot save to these formats. An open source plug-in, UFRaw (or community supported fork nUFRAW), adds full raw compatibility, and has been noted several times for being updated for new camera models more quickly than Adobe's UFRaw support. |
| Export only | GIMP can export to MNG layered image files (Linux version only) and HTML (as a table with colored cells), C source code files (as an array) and ASCII art (using a plug-in to represent images with characters and punctuation making up images), though it cannot read these formats. |

## Professional reviews

Lifewire reviewed GIMP favorably in March 2019, writing that "for those who have never experienced Photoshop, GIMP is simply a very powerful image manipulation program," and "if you're willing to invest some time learning it, it can be a very good graphics tool."

GIMP's fitness for use in professional environments is regularly reviewed; it is often compared to and suggested as a possible replacement for Adobe Photoshop.

The single-window mode introduced in GIMP 2.8 was reviewed in 2012 by Ryan Paul of *Ars Technica*, who noted that it made the user experience feel "more streamlined and less cluttered". Michael Burns, writing for *Macworld* in 2014, described the single-window interface of GIMP 2.8.10 as a "big improvement".

## Versions

| Version | Latest version | Initial release | Significant changes and notes |
|---|---|---|---|
| Unsupported: 1.0 | 1.0.4 | 1998-06-05 | Initial stable version. Switch from Motif to GTK+ 1.x. Support for image layers. Introduction of the XCF file format. New memory manager with disk caching of tiles to support large images. New plug-in/extension API and introduction of the Procedural Database (PDB). Introduction of Script-Fu. |
| Unsupported: 1.2 | 1.2.5 | 2000-12-25 | Improvements to the user interface |
| Unsupported: 2.0 | 2.0.6 | 2004-03-23 | Switch to GTK+ 2.x graphical toolkit. Introduction of tabs and docks system, improvements to Script-Fu scripting, text re-editing, CMYK color support. |
| Unsupported: 2.2 | 2.2.17 | 2004-12-19 | Plugin support, keyboard shortcut editor, previews for transform tools. New GIMP hardware controllers support. Improvements to drag and drop and copy and paste to other applications. The last major version to support Windows 98/Me. |
| Unsupported: 2.4 | 2.4.7 | 2007-10-24 | Color management support, scalable brushes, new and rewritten selection tools and crop tools. Many user interface changes including full screen editing and a new icon theme. Increased file format support. Improved printing quality. Improved interface for external device input. |
| Unsupported: 2.6 | 2.6.12 | 2008-10-01 | Partial implementation of GEGL, and first iteration of UI re-design. The last major version to support Windows 2000. |
| Unsupported: 2.8 | 2.8.22 | 2012-05-03 | Single-window mode. Multi-column dock windows. Other UI improvements. Save/Export separation. Layer groups. Tools drawn with Cairo. On canvas text editing. Simple math in size entries. Various improvements. The last major version to support Windows XP and Vista. |
| Unsupported: 2.10 | 2.9.2 | 2018-04-27 | GEGL port. New and improved tools. File format support improvements. Better color management. Layers blending improvements. Metadata improvements. Improved UI with new themes. On-canvas gradient editing. Wayland support on Linux. Support for new image format's (OpenEXR, RGBE, WebP, HGT). Basic HiDPI support. |
| 2.10.4 | 2018-07-04 | Simple horizon straightening. Asynchronous fonts loading. |   |
| 2.10.6 | 2018-08-19 | Vertical text layer. New filters. |   |
| 2.10.10 | 2019-04-07 | Line art detection. |   |
| 2.10.18 | 2020-02-24 | New 3D transform tool. |   |
| 2.10.24 | 2021-03-29 | File format improvements (HEIF, PSP, TIFF, JPEG, PNG, PDF, DDS, BMP, PSD). "Negative Darkroom" for negatives. Re-added support Windows Vista. |   |
| 2.10.32 | 2022-06-14 | Features backported from 2.99.8, like TIFF support improvements and JPEG XL support. |   |
| 2.10.34 | 2023-02-27 | Features backported from 2.99.14. File format improvements. Template selector in Canvas Size dialog backported from 2.99.6. Improved color-picking. Various macOS improvements. GEGL and babl improvements. Experimental ARM builds for Windows. |   |
| 2.10.36 | 2023-11-05 | Support for ASE and ACB palettes. FG to transparent transition. Better image ratio support for GIFs. Various bugfixes and other enhancements. The last major version to support Windows Vista, 7, 8 and 8.1. |   |
| 2.10.38 | 2024-05-05 | Features backported from 2.99.x. Improved support for Windows tablets. |   |
| Supported: 3.0 | 3.0.6 | 2025-03-16 | Complete port from GTK+ 2.x to GTK+ 3. GIMP now runs natively on Wayland. Better scaling on HiDPI screens. Non-destructive editing. Multiple layer selection support. Text tool improvements. Major usability improvements. XCF saving of native GIMP data improvements. Newer image formats like QOI and JPEG XL are now supported. |
| Latest version: 3.2 | 3.2.0 | 2026-03-14 | Two new non-destructive layers (*Link Layers, Vector Layers*). Users can now apply filters to channels non-destructively. 20 new brushes, including a much-requested arrow brush. The Text Editor now supports common shortcuts. Stability improvements. User Experience improvements. Welcome Dialog improvements. |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

## Forks and derivatives

Because of the free and open-source nature of GIMP, several forks, variants and derivatives of the computer program have been created to fit the needs of their creators. While GIMP is cross-platform, variants of GIMP may not be. These variants are neither hosted nor linked on the GIMP site. The GIMP site does not host GIMP builds for Windows or Unix-like operating systems either, although it does include a link to a Windows build.

### Forks

- CinePaint, formerly Film Gimp, is a fork of GIMP version 1.0.4, used for frame-by-frame retouching of feature films. CinePaint supports up to 32-bit IEEE-floating point color depth per channel, as well as color management and HDR. CinePaint is used primarily within the film industry due mainly to its support of high-fidelity image formats. It is available for BSD, Linux, and macOS.
- GIMP classic is a patch against GIMP v2.6.8 source code created to undo changes made to the user interface in GIMP v2.4 through v2.6. A build of GIMP classic for Ubuntu is available. As of March 2011, a new patch could be downloaded that patches against the experimental GIMP v2.7.
- GIMP Portable is a portable version of GIMP for Microsoft Windows XP or later that preserves brushes and presets between computers.
- GIMPshop was a derivative of GIMP that aimed to replicate Adobe Photoshop in some form. Development of GIMPshop was halted in 2006. The lead developer, Scott Moschella, abandoned the project after somebody registered the domain name "gimpshop.com" and claimed to be an official site taking donations, despite having no affiliation with Moschella.
- GimPhoto is a fork that features a Photoshop-esque UI, similar to GIMPshop. Further modifications are possible with the GimPad tool. GimPhoto stands at version 24.1 for Linux and Windows (based on GIMP v2.4.3) and version 26.1 on macOS (based on GIMP v2.6.8). Installers are included for Windows 7, 8.1, and 10; macOS 10.6+; Ubuntu 14 and Fedora; as well as source code. Only one developer is at work in this project, and as a result, fast updates are rare and there are no plans to update it to GIMP 2.8.x or above.
- McGimp was an independent port for macOS that aimed to run GIMP directly on this platform, and integrated multiple plug-ins intended to optimize photos.
- Seashore is a port for macOS, which aims to have a simpler UI based on Cocoa.
- Glimpse is a discontinued fork of GIMP, started due to complaints over the word "gimp" being derogatory towards disabled people.

## Extensions

GIMP's functionality can be extended with plugins. Notable ones include:

- GIMP-ML, which provides machine learning-based image enhancement. GIMP-ML with python 3 is next target in development.
- GIMP Animation Package (GAP), official plugin for creating animations. GAP can save animations in several formats, including GIF and AVI.
- Resynthesizer, which provides content-aware fill. Original part of Paul Harrison's PhD thesis, now maintained by Lloyd Konneker.
- G'MIC, which adds image filters and effects.
