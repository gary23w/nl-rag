---
title: "Fast approximate anti-aliasing"
source: https://en.wikipedia.org/wiki/Fast_approximate_anti-aliasing
domain: anti-aliasing-graphics
license: CC-BY-SA-4.0
tags: anti-aliasing, multisample anti-aliasing, temporal anti-aliasing, fxaa filter
fetched: 2026-07-02
---

# Fast approximate anti-aliasing

**Fast approximate anti-aliasing** (**FXAA**) is a screen-space anti-aliasing algorithm created by Timothy Lottes at Nvidia.

FXAA 3 is released under a public domain license. A later version, FXAA 3.11, is released under a 3-clause BSD license.

## Algorithm description

1. The input data is the rendered image and optionally the luminance data.
2. Acquire the luminance data. This data could be passed into the FXAA algorithm from the rendering step as an alpha channel embedded into the image to be antialiased, calculated from the rendered image, or approximated by using the green channel as the luminance data.
3. Find high contrast pixels by using a high pass filter that uses the luminance data. Low contrast pixels that are found are excluded from being further altered by FXAA. The high pass filter that excludes low contrast pixels can be tuned to balance speed and sensitivity.
4. Use contrast between adjacent pixels to heuristically find edges, and determine whether the edges are in the horizontal or vertical directions. The blend direction of a pixel will be perpendicular to the detected edge direction on that pixel.
5. Calculate one blend factor for a high-contrast pixel by analyzing the luminance data in the 3x3 grid of pixels with the pixel in question being the center pixel.
6. Search along the detected edge to determine how long that edge goes for and what direction the actual edge goes when the detected horizontal or vertical edge ends in order to take into account the actual edge's direction in order to calculate a second blend factor. This step can be tuned for more quality by increasing the search resolution and how far the search goes before the search for the edge's end gives up, or for more speed by reducing both.
7. Blend the pixel using the chosen blend direction and the maximum of both of the blend factors that were calculated.

## Comparison

The main advantage of this technique over conventional spatial anti-aliasing is that it does not require large amounts of computing power. It achieves this by smoothing undesirable jagged edges ("jaggies") as pixels, according to how they appear on-screen, rather than analyzing the 3D model itself, as in conventional spatial anti-aliasing. Since it is not based on the actual geometry, it will smooth not only edges between triangles, but also edges inside alpha-blended textures, or those resulting from pixel shader effects, which are immune to the effects of multisample anti-aliasing (MSAA).

The downsides are that high contrast texture maps are blurred, effect that can be reduced by adjusting the "subpix filtering", that FXAA must be applied *before* rendering the HUD elements of a game lest it affect them too, and that polygonal details smaller than one pixel that would have been captured and rendered by MSAA and SSAA cannot be captured and rendered by FXAA alone.

FXAA includes a specific sub-pixel low-pass filter pass to reduce shimmering and aliasing in shader results such as shadows and specular highlights. This stage uses a low-pass filter on 3x3 neighborhoods to dampen high-frequency artifacts, helping to reduce "shimmering" or "stipple" aliasing in moving images.
