---
title: "Displacement mapping"
source: https://en.wikipedia.org/wiki/Displacement_mapping
domain: terrain-rendering
license: CC-BY-SA-4.0
tags: terrain rendering, heightmap terrain, geometry clipmap terrain, displacement terrain mesh
fetched: 2026-07-02
---

# Displacement mapping

Displacement mapping in mesh

Displacement mapping with SVG filter effects

**Displacement mapping** is an alternative computer graphics technique in contrast to bump, normal, and parallax mapping, using a texture or height map to cause an effect where the actual geometric position of points over the textured surface are *displaced*, often along the local surface normal, according to the value the texture function evaluates to at each point on the surface. It gives surfaces a sense of depth and detail, permitting in particular self-occlusion, self-shadowing and silhouettes; on the other hand, it is the most costly of this class of techniques owing to the large amount of additional geometry.

For years, displacement mapping was a peculiarity of high-end rendering systems like PhotoRealistic RenderMan, while realtime APIs, like OpenGL and DirectX, were only starting to use this feature. One of the reasons for this is that the original implementation of displacement mapping required an adaptive tessellation of the surface in order to obtain enough micropolygons whose size matched the size of a pixel on the screen.

## Meaning of the term in different contexts

Displacement mapping includes the term mapping which refers to a texture map being used to modulate the displacement strength. The displacement direction is usually the local surface normal. Today, many renderers allow programmable shading which can create high quality (multidimensional) procedural textures and patterns at arbitrarily high frequencies. The use of the term mapping becomes arguable then, as no texture map is involved anymore. Therefore, the broader term **displacement** is often used today to refer to a super concept that also includes displacement based on a texture map.

Renderers using the REYES algorithm, or similar approaches based on micropolygons, have allowed displacement mapping at arbitrary high frequencies since they became available almost 20 years ago.

The first commercially available renderer to implement a micropolygon displacement mapping approach through REYES was Pixar's PhotoRealistic RenderMan. Micropolygon renderers commonly tessellate geometry themselves at a granularity suitable for the image being rendered. That is: the modeling application delivers high-level primitives to the renderer. Examples include true NURBS- or subdivision surfaces. The renderer then tessellates this geometry into micropolygons at render time using view-based constraints derived from the image being rendered.

Other renderers that require the modeling application to deliver objects pre-tessellated into arbitrary polygons or even triangles have defined the term displacement mapping as moving the vertices of these polygons. Often the displacement direction is also limited to the surface normal at the vertex. While conceptually similar, those polygons are usually a lot larger than micropolygons. The quality achieved from this approach is thus limited by the geometry's tessellation density a long time before the renderer gets access to it.

This difference between displacement mapping in micropolygon renderers vs. displacement mapping in a non-tessellating (macro)polygon renderers can often lead to confusion in conversations between people whose exposure to each technology or implementation is limited. Even more so, as in recent years, many non-micropolygon renderers have added the ability to do displacement mapping of a quality similar to that which a micropolygon renderer is able to deliver naturally. To distinguish between the crude pre-tessellation-based displacement these renderers did before, the term **sub-pixel displacement** was introduced to describe this feature.

Sub-pixel displacement commonly refers to finer re-tessellation of geometry that was already tessellated into polygons. This re-tessellation results in micropolygons or often microtriangles. The vertices of these then get moved along their normals to achieve the displacement mapping.

True micropolygon renderers have always been able to do what sub-pixel-displacement achieved only recently, but at a higher quality and in arbitrary displacement directions.

Recent developments seem to indicate that some of the renderers that use sub-pixel displacement move towards supporting higher level geometry too. As the vendors of these renderers are likely to keep using the term sub-pixel displacement, this will probably lead to more obfuscation of what displacement mapping really stands for, in 3D computer graphics.

In reference to Microsoft's proprietary High Level Shader Language, displacement mapping can be interpreted as a kind of "vertex-texture mapping" where the values of the texture map do not alter pixel colors (as is much more common), but instead change the position of vertices. Unlike bump, normal and parallax mapping, all of which can be said to "fake" the behavior of displacement mapping, in this way a genuinely *rough* surface can be produced from a texture. It has to be used in conjunction with adaptive tessellation techniques (that increases the number of rendered polygons according to current viewing settings) to produce highly detailed meshes.
