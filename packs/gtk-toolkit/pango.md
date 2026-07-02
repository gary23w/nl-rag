---
title: "Pango"
source: https://en.wikipedia.org/wiki/Pango
domain: gtk-toolkit
license: CC-BY-SA-4.0
tags: gtk toolkit, gobject type system, glib library, gnome widgets
fetched: 2026-07-02
---

# Pango

**Pango** (stylized as Παν語) is a text (i.e. glyph) layout engine library which works with the HarfBuzz shaping engine for displaying multi-language text.

Full-function rendering of text and cross-platform support is achieved when Pango is used with platform APIs or third-party libraries, such as Uniscribe and FreeType, as text rendering backends. Pango-processed text will appear similar under different operating systems.

Pango is a special-purpose library for text and not a general-purpose graphics rendering library such as Cairo, with which Pango can be used. The Cairo documentation recommends Pango be used to "render" text rather than Cairo for all but the simplest text "rendering".

## History and naming

The name pango comes from Greek *pan* (παν, 'all') and Japanese *go* (語, 'language').

In January 2000, the merger of the GScript and GnomeText projects was named Pango.

Pango version 1.0.0 was released 11 March 2002.

## Support for OpenType features

Pango 1.17 and newer support the 'locl' feature tag that allows localized glyphs to be used for the same Unicode code point. Assuming you have Verdana version 5.01 installed, which supports the 'locl' feature for the latn/ROM (Romanian) script, a quick demonstration (on Linux) is:

```mw
for lang in en ro
do
    pango-view \
        --font="Verdana 64" \
        --text "şţ vs. șț in $lang" \
        --language=$lang
done
```

For an explanation of the substitutions rules for Romanian, see this discussion.

Setting the locale via the POSIX environment variable, e.g. LANG=ro_RO.UTF-8 will also cause Pango to use 'locl' font feature. Finally, you can change the language on the fly in the same text using Pango markup, e.g.:

```mw
pango-view \
    --font="Verdana 24" \
    --markup \
    --text 'In the same text: şţ(en) and <span lang="ro">şţ(ro).</span>'
```

Since 1.37.1, Pango added more attributes to provide complete support for processing OpenType feature.

## Major users

Pango has been integrated into most Linux distributions. The GTK UI toolkit uses Pango for all of its text rendering. The Linux versions of the Mozilla Firefox web browser and Mozilla Thunderbird mail client use Pango for text rendering.
