---
title: "Cairo (graphics)"
source: https://en.wikipedia.org/wiki/Cairo_(graphics)
domain: gtk-toolkit
license: CC-BY-SA-4.0
tags: gtk toolkit, gobject type system, glib library, gnome widgets
fetched: 2026-07-02
---

# Cairo (graphics)

**Cairo** (stylized as **cairo**) is an open-source graphics library that provides a vector graphics-based, device-independent API for two-dimensional drawing. Written in C, it supports output to multiple backends including X11, Quartz, Win32, SVG, PDF, and PostScript. Cairo uses hardware acceleration when available.

Cairo is used by GTK (versions 2.8 through 3.x), the Gecko layout engine in Mozilla Firefox, WebKit, Poppler, and Inkscape, among other projects. The library is dual-licensed under the GNU Lesser General Public License version 2.1 and the Mozilla Public License 1.1.

The name derives from the project's original name "Xr," interpreted as the Greek letters chi and rho, which together sound like "Cairo."

## History

Keith Packard and Carl Worth created the project for use in the X Window System, originally naming it **Xr** (later **Xr/Xc**). The name was changed in July 2003 to emphasize that the library was cross-platform and not tied to X11.

Cairo 1.0 was released in 2005, providing a stable API. Version 1.2 (2006) added PDF and SVG backend support. Version 1.4 (2007) improved font handling and added the `cairo_push_group` API for offscreen rendering. Version 1.10 (2010) introduced the recording surface, which captures drawing operations for later replay, and the `cairo_region` API.

In 2022, several legacy backends were removed, including BeOS, OS/2, DirectFB, and the OpenGL backend (which had been inactive for a decade).

GTK adopted Cairo for rendering in version 2.8 (2005), and GTK 3.0 (2011) used Cairo for all rendering. GTK 4 (2020) shifted to Vulkan and OpenGL renderers via GSK, reducing Cairo's role.

## Architecture

### Drawing model

Cairo uses a three-layer drawing model based on Porter-Duff compositing:

1. A **mask** is constructed from vector primitives (paths, rectangles, glyphs, Bezier curves).
2. A **source** provides color data, which may be a solid color, gradient, bitmap pattern, or another surface.
3. The source is painted through the mask onto a **destination surface**, which represents the output backend.

This approach differs from Scalable Vector Graphics (SVG), which attaches style attributes directly to shapes.

### Backends

Cairo supports output to multiple backends ("surfaces"):

- **Display servers**: X Window System (via Xlib and XCB), Quartz (macOS), Win32 GDI
- **Image formats**: PNG, in-memory image buffers
- **Document formats**: PDF, PostScript, SVG

Legacy backends for BeOS, OS/2, DirectFB, and OpenGL (direct and via glitz) were removed in 2022-2023. Experimental backends have been developed for OpenVG, Qt, Skia, and Direct2D.

### Language bindings

Bindings exist for C++, C# and other CLI languages, Delphi, Haskell, Julia, Lua, Perl, PHP, Python, Ruby, Rust, Scheme, and Smalltalk.

### Complex text layout

Cairo handles Latin and CJK fonts but does not directly support complex text layout scripts that require glyph shaping. The developers recommend using Pango for complex text, which integrates with Cairo for rendering.

## Software using Cairo

- GTK used Cairo for all rendering in version 3.x; GTK 4 uses it in a reduced role.
- The Mozilla Gecko layout engine adopted Cairo in Gecko 1.9 (Firefox 3) for rendering web content and the user interface.
- WebKit uses Cairo for rendering in its GTK and EFL ports.
- The Poppler PDF rendering library uses Cairo for antialiased output.
- Inkscape uses Cairo for its outline mode display and for PDF and PostScript export.
- The Mono Project uses Cairo to implement its GDI+ (libgdiplus) and System.Drawing backends.
- R uses Cairo for PDF, PostScript, and SVG plot output when available.
- RRDtool replaced its internal graphics library with Cairo and Pango in version 1.3 (2008).
- Gnuplot 4.4 uses Cairo for PDF and PNG output.

### Example

A simple program that generates an SVG file using Cairo:

```mw
#include <cairo-svg.h>
#include <stdio.h>

int main(int argc, char **argv) {
    cairo_surface_t *surface = cairo_svg_surface_create("Cairo_example.svg", 100.0, 100.0);
    cairo_t *cr = cairo_create(surface);

    /* Draw the squares in the background */
    for (int x = 0; x < 10; ++x)
        for (int y = 0; y < 10; ++y)
            cairo_rectangle(cr, x * 10.0, y * 10.0, 5, 5);

    cairo_pattern_t *pattern = cairo_pattern_create_radial(50, 50, 5, 50, 50, 50);
    cairo_pattern_add_color_stop_rgb(pattern, 0, 0.75, 0.15, 0.99);
    cairo_pattern_add_color_stop_rgb(pattern, 0.9, 1, 1, 1);

    cairo_set_source(cr, pattern);
    cairo_fill(cr);

    /* Writing in the foreground */
    cairo_set_font_size (cr, 15);
    cairo_select_font_face (cr, "Georgia", CAIRO_FONT_SLANT_NORMAL, CAIRO_FONT_WEIGHT_BOLD);
    cairo_set_source_rgb (cr, 0, 0, 0);

    cairo_move_to(cr, 10, 25);
    cairo_show_text(cr, "Hallo");

    cairo_move_to(cr, 10, 75);
    cairo_show_text(cr, "Wikipedia!");

    cairo_destroy(cr);
    cairo_surface_destroy(surface);
}
```
