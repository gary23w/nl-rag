---
title: "Level of detail (computer graphics)"
source: https://en.wikipedia.org/wiki/Level_of_detail_(computer_graphics)
domain: terrain-rendering
license: CC-BY-SA-4.0
tags: terrain rendering, heightmap terrain, geometry clipmap terrain, displacement terrain mesh
fetched: 2026-07-02
---

# Level of detail (computer graphics)

In computer graphics, **level of detail** (**LOD**) refers to the complexity of a 3D model representation. LOD can be decreased as the model moves away from the viewer or according to other metrics such as object importance, viewpoint-relative speed or position. LOD techniques increase the efficiency of rendering by decreasing the workload on graphics pipeline stages, usually vertex transformations. The reduced visual quality of the model is often unnoticed because of the small effect on object appearance when distant or moving fast.

Although most of the time LOD is applied to geometry detail only, the basic concept can be generalized. Recently, LOD techniques also included shader management to keep control of pixel complexity. A form of level of detail management has been applied to texture maps for years, under the name of mipmapping, also providing higher rendering quality.

It is commonplace to say that "an object has been *LOD-ed*" when the object is simplified by the underlying *LOD-ing algorithm* as well as a 3D modeler manually creating LOD models.

## Historical reference

The origin[1] of all the LOD algorithms for 3D computer graphics can be traced back to an article by James H. Clark in the October 1976 issue of *Communications of the ACM*. At the time, computers were monolithic and rare, and graphics were being driven by researchers. The hardware itself was completely different, both architecturally and performance-wise. As such, many differences could be observed with regard to today's algorithms but also many common points.

The original algorithm presented a much more generic approach to what will be discussed here. After introducing some available algorithms for geometry management, it is stated that most fruitful gains came from *"...structuring the environments being rendered"*, allowing to exploit faster transformations and clipping operations.

The same environment structuring is now proposed as a way to control varying detail thus avoiding unnecessary computations, yet delivering adequate visual quality:

> For example, a dodecahedron looks like a sphere from a sufficiently large distance and thus can be used to model it so long as it is viewed from that or a greater distance. However, if it must ever be viewed more closely, it will look like a dodecahedron. One solution to this is simply to define it with the most detail that will ever be necessary. However, then it might have far more detail than is needed to represent it at large distances, and in a complex environment with many such objects, there would be too many polygons (or other geometric primitives) for the visible surface algorithms to efficiently handle.

The proposed algorithm envisions a tree data structure which encodes in its arcs both transformations and transitions to more detailed objects. In this way, each node encodes an object and according to a fast heuristic, the tree is descended to the leaves which provide each object with more detail. When a leaf is reached, other methods could be used when higher detail is needed, such as Catmull's recursive subdivision[2].

> The significant point, however, is that in a complex environment, the amount of information presented about the various objects in the environment varies according to the fraction of the field of view occupied by those objects.

The paper then introduces clipping (not to be confused with culling although often similar), various considerations on the *graphical working set* and its impact on performance, interactions between the proposed algorithm and others to improve rendering speed.

## Well known approaches

Although the algorithm introduced above covers a whole range of level of detail management techniques, real world applications usually employ specialized methods tailored to the information being rendered. Depending on the requirements of the situation, two main methods are used:

The first method, **discrete level of detail** (**DLOD**), involves creating multiple, discrete versions of the original geometry with decreased levels of geometric detail. At runtime, the full-detail models are substituted for the models with reduced detail as necessary. Due to the discrete nature of the levels, there may be visual popping when one model is exchanged for another. This may be mitigated by alpha blending or morphing between states during the transition.

The second method, **continuous level of detail** (**CLOD**), uses a structure which contains a continuously variable spectrum of geometric detail. The structure can then be probed to smoothly choose the appropriate level of detail required for the situation. A significant advantage of this technique is the ability to locally vary the detail; for instance, the side of a large object nearer to the view may be presented in high detail, while simultaneously reducing the detail on its distant side.

In both cases, LODs are chosen based on some heuristic which is used to judge how much detail is being lost by the reduction in detail, such as by evaluation of the LOD's geometric error relative to the full-detail model. Objects are then displayed with the minimum amount of detail required to satisfy the heuristic, which is designed to minimize geometric detail as much as possible to maximize performance while maintaining an acceptable level of visual quality.

### Details on discrete LOD

The basic concept of discrete LOD (DLOD) is to provide various models to represent the same object. Obtaining those models requires an external algorithm which is often non-trivial and subject of many polygon reduction techniques. Successive LOD-ing algorithms will simply assume those models are available.

DLOD algorithms are often used in performance-intensive applications with small data sets which can easily fit in memory. Although out-of-core algorithms could be used, the information granularity is not well suited to this kind of application. This kind of algorithm is usually easier to get working, providing both faster performance and lower CPU usage because of the few operations involved.

DLOD methods are often used for "stand-alone" moving objects, possibly including complex animation methods. A different approach is used for geomipmapping,[3] a popular terrain rendering algorithm because this applies to terrain meshes which are both graphically and topologically different from "object" meshes. Instead of computing an error and simplify the mesh according to this, geomipmapping takes a fixed reduction method, evaluates the error introduced and computes a distance at which the error is acceptable. Although straightforward, the algorithm provides decent performance.

### A discrete LOD example

As a simple example, consider a sphere. A discrete LOD approach would cache a certain number of models to be used at different distances. Because the model can trivially be procedurally generated by its mathematical formulation, using a different number of sample points distributed on the surface is sufficient to generate the various models required. This pass is not a LOD-ing algorithm.

| Image | (A finely tassellated wireframe sphere featuring over 5000 sample points.) | (A highly tassellated wireframe sphere, almost 2900 points.) | (A wireframe sphere with roughly 1600 sample points.) | (A wireframe sphere with almost 700 vertices, good when viewed from a distance.) | (A wireframe sphere with less than 150 sample points but still enough for far away objects.) |
|---|---|---|---|---|---|
| Vertices | ~5500 | ~2880 | ~1580 | ~670 | 140 |
| Notes | Maximum detail, for closeups |   |   |   | Minimum detail, very far objects |

To simulate a realistic transform bound scenario, an ad-hoc written application can be used. The use of simple algorithms and minimum fragment operations ensures that CPU bounding does not occur. Each frame, the program will compute each sphere's distance and choose a model from a pool according to this information. To easily show the concept, the distance at which each model is used is hard coded in the source. A more involved method would compute adequate models according to the usage distance chosen.

OpenGL is used for rendering due to its high efficiency in managing small batches, storing each model in a display list thus avoiding communication overheads. Additional vertex load is given by applying two directional light sources ideally located infinitely far away.

The following table compares the performance of LOD aware rendering and a full detail (*brute force*) method.

|   | Brute | DLOD | Comparison |
|---|---|---|---|
| Rendered images | (Scene at maximum detail.) | (Same scene as above with lodding enabled.) | (Almost black difference image shows no easily noticeable difference.) |
| Render time | 27.27 ms | 1.29 ms | 21 × reduction |
| Scene vertices | 2,328,480 | 109,440 | 21 × reduction |

### Hierarchical LOD

Because hardware is geared towards large amounts of detail, rendering low polygon objects may score sub-optimal performances. HLOD avoids the problem by grouping different objects together[4]. This allows for higher efficiency as well as taking advantage of proximity considerations. HLODs represent entire branches of a scene graph, so rendering one lets the renderer skip that node's descendants and simplify whole portions of a large scene at once.[5]

## Practical applications

### Video games

LOD is especially useful in 3D video games. Video game developers want to provide players with large worlds but are always constrained by hardware, frame rate and the real-time nature of video game graphics. With the advent of 3D games in the 1990s, a lot of video games simply did not render distant structures or objects. Only nearby objects would be rendered and more distant parts would gradually fade, essentially implementing distance fog. Video games using LOD rendering avoid this fog effect and can render larger areas. Some notable early examples of LOD rendering in 3D video games include *The Killing Cloud*, *Spyro the Dragon*, *Crash Bandicoot: Warped*, *Unreal Tournament* and *Serious Sam: The First Encounter*. Most modern 3D games use a combination of LOD rendering techniques, using different models for large structures and distance culling for environment details like grass and trees. The effect is sometimes still noticeable, for example when the player character flies over the virtual terrain or uses a sniper scope for long distance viewing. Especially grass and foliage will seem to pop-up when getting closer, also known as foliage culling. LOD can also be used to render fractal terrain in real time. Unreal Engine 5's *Nanite* system essentially implements level-of-detail within meshes instead of just objects as a whole.

### In GIS and 3D city modelling

LOD is found in GIS and 3D city models as a similar concept. It indicates how thoroughly real-world features have been mapped and how much the model adheres to its real-world counterpart. Besides the geometric complexity, other metrics such as spatio-semantic coherence, resolution of the texture and attributes can be considered in the LOD of a model. The standard CityGML contains one of the most prominent LOD categorizations.

The analogy of "LOD-ing" in GIS is referred to as generalization.

### Rendering and modeling software

- MeshLab an open source mesh processing tool that is able to accurately simplify 3D polygonal meshes.
- Polygon Cruncher a commercial software from Mootools that reduces the number of polygons of objects without changing their appearance.
- Simplygon a commercial mesh processing package for remeshing general input meshes into real-time renderable meshes.
