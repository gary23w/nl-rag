---
title: "Frame rate"
source: https://en.wikipedia.org/wiki/Frame_rate
domain: paint-timing
license: CC-BY-SA-4.0
tags: paint timing api, first contentful paint, first paint metric, render performance milestone
fetched: 2026-07-02
---

# Frame rate

**Frame rate**, commonly expressed in **frame/s**, **frames per second**, or **FPS**, is typically the frequency (rate) at which consecutive images (frames) are captured or displayed. This definition applies to film and video cameras, computer animation, and motion capture systems. In these contexts, frame rate may be used interchangeably with **frame frequency** and **refresh rate**, which are expressed in hertz (Hz). Additionally, in the context of computer graphics performance, FPS is the rate at which a system, particularly a GPU, is able to generate frames, and refresh rate is the frequency at which a display shows completed frames.

## Human vision

The temporal sensitivity and resolution of human vision vary depending on the type and characteristics of the visual stimulus, and it differs between individuals. The human visual system can process 10 to 12 images per second and perceive them individually, while higher rates are perceived as motion. Modulated light (such as a computer display) is perceived as stable by the majority of participants in studies when the rate is higher than 50 FPS. This perception of modulated light as steady is known as the flicker fusion threshold. However, when the modulated light is non-uniform and contains an image, the flicker fusion threshold can be much higher, in the hundreds of hertz. With regard to image recognition, people have been found to recognize a specific image in an unbroken series of different images, each of which lasts as little as 13 milliseconds. Persistence of vision sometimes accounts for very short single-millisecond visual stimulus having a perceived duration of between 100 ms and 400 ms. Multiple stimuli that are very short are sometimes perceived as a single stimulus, such as a 10 ms green flash of light immediately followed by a 10 ms red flash of light perceived as a single yellow flash of light.

## Film and video

### Silent film

Early silent films had stated frame rates anywhere from 16 to 24 frames per second (FPS), but since the cameras were hand-cranked, the rate often changed during the scene to fit the mood. Projectionists could also change the frame rate in the theater by adjusting a rheostat controlling the voltage powering the film-carrying mechanism in the projector. Film companies often intended for theaters to show their silent films at a higher frame rate than that at which they were filmed. These frame rates were enough for the sense of motion, but it was perceived as jerky motion. To minimize the perceived flicker, projectors employed dual- and triple-blade shutters, so each frame was displayed two or three times, increasing the flicker rate to 48 or 72 FPS and reducing eye strain. Thomas Edison said that 46 frames per second was the minimum needed for the eye to perceive motion: "Anything less will strain the eye." In the mid to late 1920s, the frame rate for silent film increased to 20–26 FPS.

### Sound film

When sound film was introduced in 1926, variations in film speed were no longer tolerated, as the human ear is more sensitive than the eye to changes in frequency. Many theaters had shown silent films at 22 to 26 FPS, which is why the industry chose 24 FPS for sound film as a compromise. From 1927 to 1930, as various studios updated equipment, the rate of 24 FPS became standard for 35 mm sound film. At 24 FPS, the film travels through the projector at a rate of 456 millimetres (18.0 in) per second. This allowed simple two-blade shutters to give a projected series of images at 48 per second, satisfying Edison's recommendation. Many modern 35 mm film projectors use three-blade shutters to give 72 images per second—each frame is flashed on screen three times.

### Animation

In drawn animation, moving characters are often animated *on twos*, meaning one drawing is displayed for every two frames of film. Since film typically runs at 24 frames per second, this results in a display of only 12 drawings per second. Even though the image update rate is low, the fluidity is satisfactory for most subjects. However, when a character is required to perform a quick movement, it is usually necessary to revert to animating *on ones*, as *twos* are too slow to convey the motion adequately. A blend of the two techniques keeps the eye fooled and controls production cost.

Animation for most Saturday morning cartoons, first introduced in the mid-1960s, was produced as cheaply as possible and was most often shot on *threes* or even *fours*, i.e., three or four frames per drawing. This translates to only 8 or 6 drawings per second, respectively. Anime is also usually drawn on threes or twos.

### Modern video standards

Due to the mains frequency of electric grids, analog television broadcast was developed with frame rates of 50 FPS (most of the world) or 60 FPS (Canada, US, Mexico, Philippines, Japan, South Korea). The frequency of the electricity grid was extremely stable and therefore it was logical to use for synchronization.

The introduction of color television technology made it necessary to lower that 60 FPS frequency by 0.1% to avoid "dot crawl", a display artifact appearing on legacy black-and-white displays, showing up on highly color-saturated surfaces. It was found that by lowering the frame rate by 0.1%, the undesirable effect was minimized.

As of 2025, video transmission standards in North America, Japan, and South Korea are still based on 60/1.001 ≈ 59.94 images per second. Two sizes of images are typically used: 1920 × 1080 (1080i interlaced or 1080p progressive) and 1280 × 720 (720p). Confusingly, *interlaced* formats are customarily stated at half their image rate, 29.97/25 FPS, and *double* their image height, but these statements are purely custom; in each format, 60 images per second are produced. A resolution of 1080i produces 59.94 or 50 1920 × 540 images, each squashed to half-height in the photographic process and stretched back to fill the screen on playback in a television set. The 720p format produces 59.94/50 or 29.97/25 1280 × 720 images, not squeezed, so that no expansion or squeezing of the image is necessary. This confusion was industry-wide in the early days of digital video software, with much software being written incorrectly, the developers believing that only 29.97 images were expected each second. While it was true that each picture element was polled and sent only 29.97 times per second, the pixel location immediately below that one was polled 1/60 of a second later, part of a completely separate image for the next 1/60-second frame.

At its native 24 FPS rate, film could not be displayed on 60 FPS video without the necessary pulldown process, often leading to *judder*: to convert 24 frames per second into 60 frames per second, every odd frame is repeated, playing twice, while every even frame is tripled. This creates uneven motion, appearing stroboscopic. Other conversions have similar uneven frame doubling. Newer video standards support 120, 240, or 300 frames per second, so frames can be evenly sampled for standard frame rates such as 24, 48 and 60 FPS film or 25, 30, 50 or 60 FPS video. Of course these higher frame rates may also be displayed at their native rates.

### Electronic camera specifications

In electronic camera specifications, frame rate refers to the maximum possible rate frames that can be captured (e.g. if the exposure time were set to near-zero), but in practice, other settings (such as exposure time) may reduce the actual frequency to a lower number than the specification frame rate.

## Computer games

In computer video games, frame rate plays an important part in the experience as, unlike film, games are rendered in real-time. 60 frames per second has for a long time been considered the minimum frame rate for smoothly animated game play. Video games designed for PAL markets, before the sixth generation of video game consoles, had lower frame rates by design due to the 50 Hz output. This noticeably made fast-paced games, such as racing or fighting games, run slower; less frequently developers accounted for the frame rate difference and altered the game code to achieve (nearly) identical pacing across both regions, with varying degrees of success. Computer monitors marketed to competitive PC gamers can hit 360, 500 FPS, or more. High frame rates make action scenes look less blurry, such as sprinting through the wilderness in an open world game, spinning rapidly to face an opponent in a first-person shooter, or keeping track of details during an intense fight in a multiplayer online battle arena. Input latency is also reduced. Some people may have difficulty perceiving the differences between high frame rates, though.

Frame time is related to frame rate, but it measures the time between frames. A game could maintain an average of 60 frames per second but appear choppy because of a poor frame time. Game reviews sometimes average the worst 1% of frame rates, reported as the 99th percentile, to measure how choppy the game appears. A small difference between the average frame rate and 99th percentile would generally indicate a smooth experience. To mitigate the choppiness of poorly optimized games, players can set frame rate caps closer to their 99% percentile.

When a game's frame rate is different from the display's refresh rate, screen tearing can occur. Vsync mitigates this, but it caps the frame rate to the display's refresh rate, increases input lag, and introduces judder. Variable refresh rate displays automatically set their refresh rate equal to the game's frame rate, as long as it is within the display's supported range.

## Frame rate up-conversion

Low frame rate video

Video with 4 times increased frame rate

Frame rate up-conversion (FRC) is the process of increasing the temporal resolution of a video sequence by synthesizing one or more intermediate frames between two consecutive frames. A low frame rate causes aliasing, yields abrupt motion artifacts, and degrades the video quality. Consequently, the temporal resolution is an important factor affecting video quality. Algorithms for FRC are widely used in applications, including visual quality enhancement, video compression and slow-motion video generation.

### Methods

Most FRC methods can be categorized into optical flow or kernel-based and pixel hallucination-based methods.

#### Flow-based FRC

Flow-based methods linearly combine predicted optical flows between two input frames to approximate flows from the target intermediate frame to the input frames. They also propose flow reversal (projection) for more accurate image warping. Moreover, there are algorithms that give different weights of overlapped flow vectors depending on the object depth of the scene via a flow projection layer.

#### Pixel hallucination-based FRC

Pixel hallucination-based methods use deformable convolution to the center frame generator by replacing optical flows with offset vectors. There are algorithms that also interpolate middle frames with the help of deformable convolution in the feature domain. However, since these methods directly hallucinate pixels, unlike the flow-based FRC methods, the predicted frames tend to be blurry when fast-moving objects are present.
