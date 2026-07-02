---
title: "Heightmap"
source: https://en.wikipedia.org/wiki/Heightmap
domain: tilemap
license: CC-BY-SA-4.0
tags: tilemap rendering, tile-based game, tile map layer, isometric tilemap
fetched: 2026-07-02
---

# Heightmap

In computer graphics, a **heightmap** or **heightfield** is a raster image used mainly as Discrete Global Grid in secondary elevation modeling. Each pixel stores values, such as surface elevation data, for display in 3D computer graphics. A heightmap can be used in bump mapping to calculate where this 3D data would create shadow in a material, in displacement mapping to displace the actual geometric position of points over the textured surface, or for terrain where the heightmap is converted into a 3D mesh.

A heightmap contains one channel interpreted as a distance of displacement or "height" from the "floor" of a surface and sometimes visualized as luma of a grayscale image, with black representing minimum height and white representing maximum height. When the map is rendered, the designer can specify the amount of displacement for each unit of the height channel, which corresponds to the “contrast” of the image. Heightmaps can be stored by themselves in existing grayscale image formats, with or without specialized metadata, or in specialized file formats such as Daylon Leveller, GenesisIV and Terragen documents.

One may also exploit the use of individual color channels to increase detail. For example, a standard RGB 8-bit image can only show 256 values of grey and hence only 256 heights. By using colors, a greater number of heights can be stored (for a 24-bit image, 2563 = 16,777,216 heights can be represented (2564 = 4,294,967,296 if the alpha channel is also used)). This technique is especially useful where height varies slightly over a large area. Using only grey values, because the heights must be mapped to only 256 values, the rendered terrain appears flat, with "steps" in certain places.

Heightmaps are commonly used in geographic information systems, where they are called digital elevation models.

## Creation

Heightmaps can be created by hand with a classical paint program or a special terrain editor. These editors visualize the terrain in 3D and allow the user to modify the surface. Normally there are tools to raise, lower, smooth or erode the terrain. Another way to create a terrain is to use a terrain generation algorithm. This can be for example a 2D simplex noise function or by diffusion-limited aggregation. Another method is to reconstruct heightmaps from real world data, for example using synthetic aperture radar.

## Use

Heightmaps are widely used in terrain rendering software and modern video games. Heightmaps are an ideal way to store digital terrain elevations; compared to a regular polygonal mesh, they require substantially less memory for a given level of detail. Most modern 3D computer modelling programs are capable of using data from heightmaps in the form of bump, normal, or displacement maps to quickly and precisely create complex terrain and other surfaces.

In the earliest games using software rendering, the elements often represented heights of columns of voxels rendered with ray casting. In most newer games, the elements represent the height coordinate of polygons in a mesh.

### Rendering software

- Terragen – terrain renderer
- Picogen – terrain renderer and heightmap creation tool
- Materialize – Free PBR (Physically Based Rendering) creation tool

### Generating software

### Trivia

Although the terms heightmap and heightfield are often indistinguishable from each other, there is still a small difference in the terms. Heightmap comes from the mathematical term 'map' and heightfield comes from the mathematical term 'vector field'. Heightmap is the more correct description because most heightfields are not a (vector) field in mathematical terms but they are always a map (in mathematical terms as well as in the visual representation).
