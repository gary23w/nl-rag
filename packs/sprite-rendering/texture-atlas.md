---
title: "Texture atlas"
source: https://en.wikipedia.org/wiki/Texture_atlas
domain: sprite-rendering
license: CC-BY-SA-4.0
tags: sprite rendering, sprite sheet, texture atlas, sprite compositing
fetched: 2026-07-02
---

# Texture atlas

In computer graphics, a **texture atlas** (also called a **spritesheet** or an **image sprite** in 2D game development) is an image containing multiple smaller images, usually packed together to reduce overall dimensions. An atlas can consist of uniformly-sized images or images of varying dimensions. A sub-image is drawn using custom texture coordinates to pick it out of the atlas.

## Benefits

In an application where many small textures are used frequently, it is often more efficient to store the textures in a texture atlas which is treated as a single unit by the graphics hardware. This reduces both the disk I/O overhead and the overhead of a context switch by increasing memory locality. Careful alignment may be needed to avoid bleeding between sub textures when used with mipmapping and texture compression.

In web development, images are packed into a sprite sheet to reduce the number of image resources that need to be fetched in order to display a page.

## Gallery

- (A texture atlas for a video game)A texture atlas for a video game
- (A texture atlas of glyphs)A texture atlas of glyphs
- (Sprite sheet for the video game Blades of Exile)Sprite sheet for the video game *Blades of Exile*
- (A human model and "skin" from the MakeHuman project, as viewed in the program, Blender)A human model and "skin" from the MakeHuman project, as viewed in the program, Blender
