---
title: "Font rasterization"
source: https://en.wikipedia.org/wiki/Font_rasterization
domain: nuklear-ui
license: CC-BY-SA-4.0
tags: nuklear library, single header gui, immediate mode c, minimal state ui
fetched: 2026-07-02
---

# Font rasterization

**Font rasterization** is the process of converting text from a vector description (as found in scalable fonts such as TrueType fonts) to a raster or bitmap description. This often involves some anti-aliasing on screen text to make it smoother and easier to read. It may also involve hinting—information embedded in the font data that optimizes rendering details for particular character sizes.

## Types of rasterization

The simplest form of rasterization is simple line-drawing with no anti-aliasing of any kind. In Microsoft's terminology, this is called *bi-level* (and more popularly "black and white") rendering because no intermediate shades (of gray) are used to draw the glyphs. (In fact, any two colors can be used as foreground and background.) This form of rendering is also called aliased or "jagged". This is the fastest rendering method in the sense that it requires the least computational effort. However, it has the disadvantage that rendered glyphs may lose definition and become hard to recognize at small sizes. Therefore, many font data files (such as TrueType) contain hints that help the rasterizer decide where to render pixels for particularly troublesome areas in the glyphs, or sets of hand-tweaked bitmaps to use at specific pixel sizes. As a prototypical example, all versions of Microsoft Windows prior to Windows 95 (e.g. Windows 3.1) only provided this type of built-in rasterizer.

Simple rasterization without anti-aliasing

Rasterization with anti-aliasing without hinting

Rasterization with anti-aliasing with hinting. Here pixels are forced to fall into integral pixel coordinates whenever possible.

Rasterization with hinting and subpixel rendering for an RGB flat panel display

A more complicated approach is to use standard anti-aliasing techniques from computer graphics. This can be thought of as determining, for each pixel at the edges of the character, how much of that pixel the character occupies, and drawing that pixel with that degree of opacity. For example, when drawing a black (000000) letter on a white (FFFFFF) background, if a pixel ideally should be half filled (perhaps by a diagonal line from corner to corner) it is drawn 50% gray (BCBCBC). Over-simple application of this procedure can produce blurry glyphs. For example, if the letter includes a vertical line that should be one pixel wide but falls exactly between two pixels, it appears on screen as a two-pixel-wide gray line. This blurriness trades clarity for accuracy. However, modern systems often force lines to fall within integral pixel coordinates, which makes glyphs look sharper, but also makes lines slightly wider or thinner than they would have looked on a printed sheet of paper.

Most computer displays have pixels made up of multiple subpixels (typically one each for red, green, and blue, which are combined to produce the full range of colours). In some cases, particularly with flat panel displays, it is possible to exploit this by rendering at the subpixel resolution rather than using whole pixels, which can increase the effective resolution of the screen. This is generally known as subpixel rendering. One proprietary implementation of subpixel rendering is Microsoft's ClearType.

## Currently used rasterization systems

In modern operating systems, rasterization is normally provided by a shared library common to many applications. Such a shared library may be built into the operating system or the desktop environment, or may be added later. In principle, each application may use a different font rasterization library, but in practice most systems attempt to standardize on a single library.

Microsoft Windows has supported subpixel rendering since Windows XP. On the other hand, the standard Microsoft rasterizer without ClearType is an example of one that prioritizes type designer's intent of clarity; by forcing text into integral coordinate positions, following the type designer's intent of hinting, and even not antialiasing certain fonts at certain sizes, following the type designer's intent of the gasp table, it becomes easier to read on the screen, but may appear somewhat different when printed. This has changed with Direct2D/DirectWrite shipping on Windows 7 and Windows Vista platform update, allowing subpixel text positioning to 1/16 pixel sizes.

Mac OS X's Quartz is distinguished by the use of subpixel positioning; it does not force glyphs into exact pixel locations, instead using various antialiasing techniques, including subpixel rendering, to position characters and lines to appear further from the type designer's intent of hinting and closer to the original outline. The result is that the on-screen display looks extremely similar to printed output, but can occasionally be difficult to read at smaller point sizes. The Quartz renderer has, since macOS Mojave, removed subpixel rendering, relying purely on greyscale anti-aliasing instead. This change is acceptable to HiDPI "retina" screens, but makes text on external monitors harder to read.

Most other systems use the FreeType library, which depending on the settings, can fall anywhere between Microsoft's and Apple's implementations; it supports hinting and anti-aliasing, and optionally performs subpixel rendering and positioning. FreeType also offers some features not present in either implementation such as color-balanced subpixel rendering and gamma correction.

Applications may also bring their own font rendering solutions. Graphics frameworks like Skia Graphics Engine (used by Google Chrome) occasionally use their own font renderer. Video games and other 3D applications may also need faster, GPU-based renderers such as various SDF-based renderers and "Slug".
