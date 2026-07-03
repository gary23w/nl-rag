---
title: "8-bit color"
source: https://en.wikipedia.org/wiki/8-bit_color
domain: color-depth
license: CC-BY-SA-4.0
tags: color depth
fetched: 2026-07-03
---

# 8-bit color

**8-bit color** graphics are a method of storing image information in a computer's memory or in an image file, so that each pixel is represented by 8 bits (1 byte). The maximum number of colors that can be displayed at any one time is 256 per pixel or 28.

## Color quantization

In order to turn a true color 24-bit image into an 8-bit image, the image must go through a process called color quantization. Color quantization is the process of creating a color map for a less color dense image from a more dense image.

The simplest form of quantization is to simply assign 3 bits to red, 3 bits to green and 2 bits to blue, as the human eye is less sensitive to blue light. This creates a so called **3-3-2** 8-bit color image, arranged like on the following table:

```
Bit    7  6  5  4  3  2  1  0
Data   R  R  R  G  G  G  B  B
```

This process is sub optimal. There could be different groupings of colors that make evenly spreading the colors out inefficient and likely to misrepresent the actual image. An alternative approach is to use a palette, with each of the 256 possible indexes pointing towards a larger color space (ex: 256 colors chosen from 4096). Because the color map doesn't need to have every color in it and just needs to accurately represent the more color dense image, an arbitrary color can be assigned to each of the 256 available color indexes on the map.

Popular approaches for creating these maps (also known as palettes) include the *popularity algorithm* which chooses the 256 most common colors and creates a map from them. The more accurate *median cut* algorithm resorts and divides colors to find the median of different color groups resulting in a more accurate final color map.

## Usage

Because of the low amount of memory and resultant higher speeds of 8-bit color images, 8-bit color was a common ground among computer graphics development until more memory and higher CPU speeds became readily available to consumers. 8-bit color was used in many different applications including:

- The MSX2 series of personal computer
- The Uzebox gaming console
- The Atari Falcon
- The NTSC version of the Atari GTIA
- The Tiki 100 personal computer (limited to 16 simultaneous color display)
- The Research Machines 380Z computer equipped with a High Resolution Graphics board.
- Wearable OS smartwatches with ambient displays
- Many scanners use an 8-bit grey scale as their standard

The VGA standard for graphical interface used a redefinable 256 color (8-bit) color palette, although these were selected from an 18-bit (6-bit per RGB channel, 262,144 colors) gamut. Developed in 1987 by IBM, the VGA interface supported a maximum resolution of 640x480 pixels. Due to this legacy, some image types such as GIF and TIFF use an 8-bit color palette system to store data.

Even though it is now outdated for most consumer applications, 8-bit color encoding can still be useful in imaging systems with limited data bandwidth or memory capacity. For example, both Mars Exploration Rovers used an 8-bit grayscale format for navigation imaging.

## Issues

Due to the nature of the 8-bit system, most images have different color maps. Since an 8-bit color display can not display two images with different color maps at the same time, it is usually impossible to display two different 8-bit images on the same such display at the same time. In practice, in order to avoid this problem, most images do not use the full range of 256 colors. Another problem comes when doing image processing: whenever two images with different color maps are added to each other, the resulting image has to have a new color map created, meaning another quantization operation has to occur, making the resulting image an imperfect version of the expected result.

## 8-bit color today

Currently, most graphics hardware runs in 24-bit truecolor or 32-bit truecolor (24-bit truecolor and an 8-bit alpha channel). However, some remote desktop software (Virtual Network Computing, Remote Desktop Protocol) can switch to 8-bit color to conserve bandwidth. With the comparative low cost and high speeds of modern computers, some image editing is even done in a raw format with anywhere from 12 to 14 bits from each of the camera's image sensor pixels in order to avoid image quality reduction while editing.
