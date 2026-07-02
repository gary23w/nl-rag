---
title: "Bloom (shader effect)"
source: https://en.wikipedia.org/wiki/Bloom_(shader_effect)
domain: bloom-effect
license: CC-BY-SA-4.0
tags: bloom shader effect, light bloom rendering, gaussian blur bloom, glare post-processing
fetched: 2026-07-02
---

# Bloom (shader effect)

**Bloom** (sometimes referred to as **light bloom** or **glow**) is a computer graphics effect used in video games, demos, and high-dynamic-range rendering (HDRR) to reproduce an imaging artifact of real-world cameras. The effect produces fringes (or feathers) of light extending from the borders of bright areas in an image, contributing to the illusion of an extremely bright light overwhelming the camera or eye capturing the scene. It became widely used in video games after an article on the technique was published by the authors of *Tron 2.0* in 2004.

## Theory

There are two recognized potential causes of bloom.

### Imperfect focus

One physical basis of bloom is that, in the real world, lenses can never focus perfectly. Even a perfect lens will convolve the incoming image with an Airy disk (the diffraction pattern produced by passing a point light source through a circular aperture). Under normal circumstances, these imperfections are not noticeable, but an intensely bright light source will cause the imperfections to become visible. As a result, the image of the bright light appears to bleed beyond its natural borders.

The Airy disc function falls off very quickly but has very wide tails (actually, infinitely wide tails). As long as the brightness of adjacent parts of the image are roughly in the same range, the effect of the blurring caused by the Airy disc is not particularly noticeable; but in parts of the image where very bright parts are adjacent to relatively darker parts, the tails of the Airy disc become visible and can extend far beyond the extent of the bright part of the image.

In HDRR images, the effect can be reproduced by convolving the image with a windowed kernel of an Airy disc (for very good lenses), or by applying Gaussian blur (to simulate the effect of a less perfect lens), before converting the image to fixed-range pixels. The effect cannot be fully reproduced in non-HDRR imaging systems, because the amount of bleed depends on how bright the bright part of the image is.

As an example, when a picture is taken indoors, the brightness of outdoor objects seen through a window may be 70 or 80 times brighter than objects inside the room. If exposure levels are set for objects inside the room, the bright image of the windows will bleed past the window frames when convolved with the Airy disc of the camera being used to produce the image.

### CCD sensor saturation

Bloom in digital cameras is caused by an overflow of charge in the photodiodes, which are the light-sensitive elements in the camera's image sensor. When a photodiode is exposed to a very bright light source, the accumulated charge can spill over into adjacent pixels, creating a halo effect. This is known as "charge bleeding."

The bloom effect is more pronounced in cameras with smaller pixels, as there is less room for the charge to dissipate. It can also be exacerbated by high ISO settings, which increase the camera's sensitivity to light and can result in more charge accumulation.

While the bloom effect can be distracting in some images, it can also be used creatively to add a dreamy or otherworldly quality to photos.

## Practical implementation

Current generation gaming systems are able to render 3D graphics using floating-point frame buffers, in order to produce HDR images. To produce the bloom effect, the linear HDRR image in the frame buffer is convolved with a convolution kernel in a post-processing step, before converting to RGB space. The convolution step usually requires the use of a large gaussian kernel that is not practical for realtime graphics, causing programmers to use approximation methods.

## Use in games

Some of the earliest games to use the bloom effect include the pre-rendered CGI game *Riven* (1997), the voxel game *Outcast* (1999), and the real-time 3D polygon games *The Bouncer* (2000) and *Ico* (2001). Bloom was later popularized within the game development community in 2004, when an article on the technique was published by the authors of *Tron 2.0*. Bloom lighting has been used in many games, modifications and game engines such as *Quake Live*, *Cube 2: Sauerbraten* and the Spring game engine.

The effect was popular in 7th-generation games, which were released from 2005 through to the early 2010s. Several games from the period have received criticism for overuse of the technique. The heavy bloom lighting in *RollerCoaster Tycoon 3* (2005) was described as "disgusting" at the time by GameSpot. Gaming Bolt described the trend as a gimmick that had died with the generation, and criticised the heavy use of the technique in major releases of the time such as *The Elder Scrolls IV: Oblivion* (2006), the Xbox 360 port of *Burnout Revenge* (2006), and *Zelda: Twilight Princess* (2006). *Syndicate* (2012) has also been described as featuring "eye-melting" bloom.
