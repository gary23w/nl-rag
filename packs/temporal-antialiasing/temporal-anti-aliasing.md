---
title: "Temporal anti-aliasing"
source: https://en.wikipedia.org/wiki/Temporal_anti-aliasing
domain: temporal-antialiasing
license: CC-BY-SA-4.0
tags: temporal antialiasing, taa rendering, temporal reprojection, motion vector rendering
fetched: 2026-07-02
---

# Temporal anti-aliasing

**Temporal anti-aliasing** (**TAA**) refers to two distinct forms of anti-aliasing in computer graphics. The commonly understood meaning is a specific technique that removes spatial aliasing from an image, using data from multiple frames, and is used in video games and real-time rendering. The older meaning is a general class of techniques that remove temporal aliasing and create motion blur.

## Spatial aliasing

The modern definition of TAA is a spatial anti-aliasing technique for real-time computer graphics that reuses information from previously rendered frames to remove aliasing, such as jaggies, from the current frame. The term *temporal anti-aliasing* is somewhat of a misnomer, and this technique is formally referred to as *temporally-amortized supersampling.* It is also known as TXAA (an implementation by Nvidia) or *Temporal Super-Sampling Anti-Aliasing* (TSSAA). This method can achieve results comparable to supersampling, at a small fraction of the computational cost, but produces soft images and can cause ghosting. TAA popularized in video games in the 2010s, with two early examples being Halo: Reach and Crysis 2, and is now the most common form of spatial anti-aliasing in real-time rendering and game engines.

### Implementation

Each pixel is sampled at a slightly different position each frame, which is achieved by adding a 2D offset to each frame, a "jitter" that shifts the image by a fraction of the size of a pixel, horizontally and vertically. The jitter changes each frame, following a pattern (such as a Halton sequence) so that every point in the image is sampled evenly over time.

Old frames are blended into the current frame, accumulating historical rendering data, approaching the result of supersampling over time. Changes to the scene—such as moving objects, camera motion, or changes in lighting—often mean that the history for any given pixel may be somewhere else on screen, be invalid, or may not exist at all. Failure to account for these changes results in ghosting.

To account for movement, velocity vectors are maintained in the G-buffer, allowing the location of each pixel in the previous frame to be calculated. The pixel at that location in the previous frame is accumulated into a history buffer, at its new location. This is called *reprojection*. Accurate velocities are required to prevent smearing.

Often, the historical data for a pixel will become invalid due to changes in occlusion, such as the pixel having recently become visible after being blocked by an object last frame. This causes ghosting unless it is detected: One method is to compare the depth of the historical position to the depth values in the current pixel's neighborhood. Color can also be useful for validating the history of a pixel, since a sudden change in color can indicate new lighting conditions or an incorrect pixel velocity.

A drawback of TAA is that it does not work well with transparent objects, particles, or reflections, because they can produce incorrect velocity vectors. In the case of transparency, this is because only one velocity vector can typically be stored per pixel. Dithering can be used to simulate opacity, a technique known as *screen-door transparency*, which works with TAA and is smoothed out over time by it.

### Comparison to other methods

Ghosting and blurriness are two disadvantages specific to TAA, though both can be significantly reduced with proper implementation. TAA requires more engine- and game-specific tuning than other anti-aliasing methods to achieve acceptable results; poorly-tuned implementations can severely exacerbate TAA's issues in some situations.

Brute force supersampling (rendering at a higher resolution and downsampling), which is considered a gold standard for spatial anti-aliasing, is very costly compared to TAA, which can produce comparable results in many situations.

Multisample anti-aliasing (MSAA), which was previously the most common real-time spatial anti-aliasing method, does not work well with deferred shading, which is needed for a number of common rendering techniques. Several post-processing anti-aliasing methods were developed to overcome this limitation, such as fast approximate anti-aliasing (FXAA), and morphological anti-aliasing (MLAA). These methods can have poor temporal stability, such as causing flickering artifacts. TAA generally reduces aliasing better than these methods, is more temporally stable, and still works with deferred shading.

Deep learning super sampling (DLSS), developed by Nvidia, operates on similar principles to TAA. Like TAA, it uses information from past frames to produce the current frame. Unlike TAA, DLSS does not sample every pixel in every frame. Instead, it samples different pixels in different frames and uses pixels sampled in past frames to fill in the unsampled pixels in the current frame. DLSS uses machine learning to combine samples in the current frame and past frames, and it can be thought of as an advanced TAA implementation.

## Temporal aliasing

The traditional definition of TAA is the removal of temporal aliasing. A photograph collects light over a period of time, called an exposure. This can result in moving objects exhibiting motion blur, which is sometimes a desirable effect. In computer graphics, images are often rendered at a single instant in time, ignoring the effects of motion, for convenience. This results in temporal aliasing: moving objects can appear to jump or flash between frames as their position changes. This effect can be mitigated, but not eliminated, by using a higher refresh rate display, and increasing the frame rate to match the refresh rate. Another approach, analogous to spatial supersampling, is to simulate motion blur by rendering many instants in time, integrating them into each frame.

Aliasing is a result of the sampling theorem of signal processing: To avoid it, a signal must be sampled at a rate at least twice the highest frequency present in the signal. An example of temporal aliasing is the wagon-wheel effect, where spinning objects can appear to move slowly, stop, or reverse.

Temporal aliasing can also affect film and video. The shutter behavior of the sampling system (the camera) strongly influences aliasing, because the window function of the exposure (its shape over time) determines how well bandlimited the image signal is before sampling. Different window functions can be chosen to reduce temporal aliasing.
