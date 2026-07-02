---
title: "Anisotropic filtering"
source: https://en.wikipedia.org/wiki/Anisotropic_filtering
domain: mipmapping
license: CC-BY-SA-4.0
tags: mipmap texture, trilinear filtering, anisotropic filtering, texture filtering
fetched: 2026-07-02
---

# Anisotropic filtering

In 3D computer graphics, **anisotropic filtering** (**AF**) is a technique that improves the appearance of textures, especially on surfaces viewed at sharp angles. It helps make textures look sharper and more detailed by reducing blur and aliasing that can occur when surfaces are angled away from the viewer. Anisotropic filtering works by applying different amounts of filtering in different directions, unlike simpler methods like bilinear and trilinear filtering which filter equally in all directions.

While it requires more processing power than these simpler methods, anisotropic filtering became a standard feature in most graphics cards in the late 1990s and is now commonly used in games and other 3D applications, often with user-adjustable settings.

## Comparison to isotropic algorithms

Anisotropic filtering enhances texture sharpness, counteracting the blur introduced by mipmapping, a common anti-aliasing technique. Anisotropic filtering can therefore be said to maintain crisp texture detail at all viewing orientations while providing fast anti-aliased texture filtering.

In traditional isotropic mipmapping, downsizing at each level halves the resolution on each axis simultaneously. As a result, when rendering a horizontal plane at an oblique angle to the camera, the minification would provide an insufficient horizontal resolution due to the reduction of image frequency in the vertical axis. That is, when sampling to avoid aliasing on a high-frequency axis, the other texture axes will be similarly downsampled and therefore potentially blurred.

With mipmap anisotropic filtering, a texture of resolution 256px × 256px would not only be downsampled to 128px × 128px, but also to other non-square resolutions, such as 256px × 128px and 32px × 128px. These *anisotropically downsampled* images can be probed when the texture-mapped image frequency is different for each texture axis. Then, one axis is not blurred due to the screen frequency of another axis, and aliasing is still avoided.

Mipmapping and its associated axis-alignment constraints mean it is suboptimal for true anisotropic filtering and is used here for illustrative purposes only. More general anisotropic filtering methods support anisotropic probes that are not necessarily axis-aligned in texture space, allowing for diagonal anisotropy.

## Degree of anisotropy

Different degrees or ratios of anisotropic filtering can be applied during rendering. This degree refers to the maximum ratio of anisotropy supported by the filtering process. For example, 4:1 (pronounced “4-to-1”) anisotropic filtering will continue to sharpen more oblique textures beyond the range sharpened by 2:1.

In practice, this means that in highly oblique texturing situations, a 4:1 filter will be twice as sharp as a 2:1 filter (it will display frequencies double that of the 2:1 filter). However, most of the scene will not require the 4:1 filter; only the more oblique and usually more distant pixels will require the sharper filtering. This means that as the degree of anisotropic filtering continues to double there are diminishing returns in terms of visible quality with fewer and fewer rendered pixels affected, and the results become less obvious to the viewer; only a relatively few highly oblique pixels, mostly on more distant geometry, will display visibly sharper textures in the scene with the higher degree of anisotropic filtering. The performance penalty also diminishes because fewer pixels require the data fetches of greater anisotropy.

Current hardware rendering implementations set an upper bound on this ratio due to the additional hardware complexity and the aforementioned diminishing returns. Applications and users are able to adjust the ratio through driver and software settings up to the threshold.

## Implementation

True anisotropic filtering probes the texture anisotropically on the fly on a per-pixel basis for any orientation of anisotropy.

In graphics hardware, typically when the texture is sampled anisotropically, several probes (texel samples) of the texture around the center point are taken on a sample pattern mapped according to the projected shape of the texture at that pixel. Earlier software methods have used summed-area tables.

Each anisotropic filtering probe is often in itself a filtered mipmap sample, which adds more sampling to the process. Sixteen trilinear anisotropic samples might require 128 samples from the stored texture, as trilinear mipmap filtering needs to take four samples for each of the two mipmaps and then anisotropic sampling (at 16-tap) needs to take sixteen of these trilinear filtered probes.

However, this level of filtering complexity is not required all the time. There are commonly available methods to reduce the amount of work the video rendering hardware must do.

The anisotropic filtering method most commonly implemented on graphics hardware is the composition of the filtered pixel values from only one line of mipmap samples. In general, the method of building a texture filter result from multiple probes filling a projected pixel sampling into texture space is referred to as "footprint assembly", even where implementation details vary.

## Performance and optimization

The sample count required can make anisotropic filtering extremely bandwidth-intensive. Multiple textures are common; each texture sample could be four bytes or more, so each anisotropic pixel could require 512 bytes from texture memory, although texture compression is commonly used to reduce this.

A video display device can easily contain over two million pixels, and desired application framerates are often upwards of 60 frames per second. As a result, the required texture memory bandwidth may grow to large values. Ranges of hundreds of gigabytes per second of pipeline bandwidth for texture rendering operations is not unusual where anisotropic filtering operations are involved.

Fortunately, several factors mitigate in favor of better performance:

- The probes themselves share cached texture samples, both inter-pixel and intra-pixel.
- Even with 16-tap anisotropic filtering, not all 16 taps are always needed because only distant *highly oblique* pixel fills tend to be highly anisotropic.
- Highly anisotropic pixel fill tends to cover small regions of the screen (i.e. generally under 10%)
- Texture magnification filters (as a general rule) require no anisotropic filtering.
