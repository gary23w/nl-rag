---
title: "Rolling shutter"
source: https://en.wikipedia.org/wiki/Rolling_shutter
domain: image-sensors-cmos
license: CC-BY-SA-4.0
tags: image sensor, active-pixel sensor, bayer filter, rolling shutter
fetched: 2026-07-02
---

# Rolling shutter

**Rolling shutter** is a process of image capture in which a still picture (in a still camera) or each frame of a video (in a video camera) is captured not by taking a snapshot of the entire scene at a single instant in time but rather by scanning across the scene rapidly, vertically, horizontally or rotationally. Thus, not all parts of the image of the scene are recorded at the same instant – however, during playback, the entire image of the scene is displayed at once, as if it represents a single instant in time. This produces predictable distortions of fast-moving objects or rapid flashes of light, referred to as **rolling shutter effect**. This process contrasts with global shutter, in which the entire frame is captured at the same instant.

The rolling shutter can be either mechanical or electronic. The advantage of this electronic rolling shutter is that the image sensor can continue to gather photons during the acquisition process, thus effectively increasing sensitivity. It is found on many digital still and video cameras using CMOS sensors. The effect is most noticeable when imaging extreme conditions of motion or the fast flashing of light. While some CMOS sensors use a global shutter, the majority found in the consumer market use a rolling shutter.

CCDs (charge-coupled devices) are alternatives to CMOS sensors, which are generally more sensitive and more expensive. CCD-based cameras often use global shutters, which take a snapshot representing a “relative” single instant in time and therefore do not suffer from the motion artifacts caused by rolling shutters.

## Distortion effects

Rolling shutters can cause such effects as:

- **Wobble**. This phenomenon (also known as the **jello effect**) appears when the camera is vibrating, in situations such as hand-held shots at telephoto settings, or when shooting from a moving vehicle. The rolling shutter causes the image to wobble unnaturally.
- **Skew**. The image bends diagonally in one direction or another as the camera or subject moves from one side to another, exposing different parts of the image at different times. Skew is a minor manifestation of the wobble phenomenon described above.
- **Spatial aliasing**. Vertically adjacent pixels are sampled in violation of the sampling theorem, when the camera or object motion is too rapid. One example of this is imaging of a quickly rotating propeller. The smear of each blade is caused by the propeller rotating at the same or near the same speed that the frame is read by the camera. Viewed perpendicular to a fan spinning clockwise, the blades on the left side appear thinner than usual while the blades on the right side appear thicker, and can even appear as if they aren't connected at the center.
- **Temporal aliasing**, including **partial exposure**. If a camera flash goes on for only part of the time of the exposure, the illumination of the flash may only be present for some rows of pixels in a given frame. For example, the top third of the picture may be brightly lit by a flash, while the bottom two-thirds of the picture is dark and unlit, as the flash was off by the time that part of the CMOS was sequenced. The difference between the two distinct parts of the frame can look odd. Similar problems can arise with fluorescent lighting, strobe effects, lightning, or any extreme situation where very fast motion or very fast bursts of light are seen in the time between when the CMOS chip sequentially records a frame.

The effects of a rolling shutter can prove difficult for visual effects filming. The process of matchmoving establishes perspective in a scene based on a single point in time, but this is difficult with a rolling shutter that provides multiple points in time within the same frame. Final results depend on the readout speed of the sensor and the nature of the scene being filmed; as a rule of thumb, higher-end cinema cameras will have faster readout speeds and therefore milder rolling shutter artifacts than low-end cameras.

Images and video that suffer from rolling shutter distortion can be improved by algorithms that do rolling shutter *rectification*, or rolling shutter *compensation*. How to do this is an active area of research.

This effect can be used as a side channel attack to gain secret keys from certain smart card readers: The attacker films the power LED of the reader while the reader is performing a cryptographic operation, then analyzes the video footage to identify brief voltage fluctuations. Due to the effect of the rolling shutter, the footage will reveal fluctuations at a resolution several orders of magnitude greater than the frame rate of the video camera. With knowledge about the algorithm used and its implementation in the chip, the attacker can then derive the key. Analyzing video footage is equivalent to measuring power consumption with an oscilloscope, but less invasive.

Distortion examples

- (A photo exhibiting partial exposure. Lighting conditions changed between the exposure of the top and bottom parts of the photo.) A photo exhibiting *partial exposure*. Lighting conditions changed between the exposure of the top and bottom parts of the photo.
- (Simulated effect of a rolling shutter on a spinning disc, (click for animation)) Simulated effect of a rolling shutter on a spinning disc (click for animation)
- (Skewing in a photograph taken from a car moving at 80 km/h (50 mph). Objects in the foreground, such as the fence and gate, have become skewed, while more distant objects in the background, such as the cliff, appear normal.) Skewing in a photograph taken from a car moving at 80 km/h (50 mph). Objects in the foreground, such as the fence and gate, have become skewed, while more distant objects in the background, such as the cliff, appear normal.
- (A similar example as seen in Une Delage au Grand Prix de l'Automobile Club de France de 1912) A similar example as seen in *Une Delage au Grand Prix de l'Automobile Club de France de 1912*
- (A Eurocopter EC-120 helicopter – the rotor blades seem to be swept back more than usual due to the rolling-shutter effect.) A Eurocopter EC-120 helicopter – the rotor blades seem to be swept back more than usual due to the rolling-shutter effect.
