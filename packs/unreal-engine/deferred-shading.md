---
title: "Deferred shading"
source: https://en.wikipedia.org/wiki/Deferred_shading
domain: unreal-engine
license: CC-BY-SA-4.0
tags: unreal engine, unreal game engine, epic games engine, unreal blueprint
fetched: 2026-07-02
---

# Deferred shading

In the field of 3D computer graphics, **deferred shading** is a screen-space shading technique that is performed on a second rendering pass, after the vertex and pixel shaders are rendered. It was first suggested by Michael Deering in 1988.

On the first pass of a deferred shader, only data that is required for shading computation is gathered. Positions, normals, and materials for each surface are rendered into the geometry buffer (G-buffer) using "render to texture". After this, a pixel shader computes the direct and indirect lighting at each pixel using the information of the texture buffers in screen space.

Screen space directional occlusion can be made part of the deferred shading pipeline to give directionality to shadows and interreflections.

## Advantages

The primary advantage of deferred shading is the decoupling of scene geometry from lighting. Only one geometry pass is required, and each light is only computed for those pixels that it actually affects. This gives the ability to render many lights in a scene without a significant performance hit. There are some other advantages claimed for the approach. These include simpler management of complex lighting resources, ease of managing other complex shader resources, and the simplification of the software rendering pipeline.

## Disadvantages

One key disadvantage of deferred rendering is the inability to handle transparency within the algorithm, although this problem is a generic one in Z-buffered scenes and it tends to be handled by delaying and sorting the rendering of transparent portions of the scene. Depth peeling can be used to achieve order-independent transparency in deferred rendering, but at the cost of additional batches and g-buffer size. Modern hardware, supporting DirectX 10 and later, is often capable of performing batches fast enough to maintain interactive frame rates. When order-independent transparency is desired (commonly for consumer applications) deferred shading is no less effective than forward shading using the same technique.

Another serious disadvantage is the difficulty with using multiple materials. It's possible to use many different materials, but it requires more data to be stored in the G-buffer, which is already quite large and takes up a large amount of the memory bandwidth.

One more disadvantage is that, due to separating the lighting stage from the geometric stage, hardware anti-aliasing does not produce correct results anymore since interpolated subsamples would result in nonsensical position, normal, and tangent attributes. One of the usual techniques to overcome this limitation is using edge detection on the final image and then applying blur over the edges, however recently more advanced post-process edge-smoothing techniques have been developed, such as MLAA (used in *Killzone 3* and *Dragon Age II*, among others), FXAA (used in *Crysis 2*, *FEAR 3*, *Duke Nukem Forever*), SRAA, DLAA (used in *Star Wars: The Force Unleashed II*), and post MSAA (used in *Crysis 2* as default anti-aliasing solution). Although it is not an edge-smoothing technique, temporal anti-aliasing (used in *Halo: Reach and Unreal Engine*) can also help give edges a smoother appearance. DirectX 10 introduced features allowing shaders to access individual samples in multi-sampled render targets (and depth buffers in version 10.1), giving users of this API access to hardware anti-aliasing in deferred shading. These features also allow them to correctly apply HDR luminance mapping to anti-aliased edges, where in earlier versions of the API any benefit of anti-aliasing may have been lost.

## Deferred lighting in commercial games

Use of the technique has increased in video games because of the control it enables in terms of using a large amount of dynamic lights and reducing the complexity of required shader instructions. Some examples of games using deferred lighting are:

- *Alan Wake*
- *Assassin's Creed III*
- *BioShock Infinite*
- *Black Mesa*
- *Blur*
- *Brink*
- *Crackdown* and *Crackdown 2*
- *Crysis 2*
- *Dead Space*, *Dead Space 2* and *Dead Space 3*
- *Deus Ex: Human Revolution*
- *Dragon's Dogma*
- *Guild Wars 2*
- *Halo: Reach*
- *inFamous* and *inFamous 2*
- *LittleBigPlanet*
- *Metal Gear Solid V: Ground Zeroes*
- *Metal Gear Solid V: The Phantom Pain*
- *Minecraft*
- *Red Dead Redemption*
- *Resistance series*
- *Rochard*
- *Shift 2: Unleashed*
- *StarCraft II*
- *Uncharted* and *Uncharted 2*
- *Vanquish*
- *Ghost of Tsushima*

## Deferred shading in commercial games

In comparison to deferred lighting, this technique is not very popular due to high memory size and bandwidth requirements, especially on seventh generation consoles where graphic memory size and bandwidth are limited and often bottlenecks.

- *Amnesia: The Dark Descent*
- *Battlefield 3*
- *Dota 2*
- *Dungeons*
- *Digital Combat Simulator (DCS) World 2.5*
- *Grand Theft Auto IV*
- *Killzone 2* and *Killzone 3*
- *Mafia II*
- *Miner Wars 2081*
- *Metro 2033*
- *Rift*
- *Shrek*
- *Splinter Cell: Conviction*
- The *S.T.A.L.K.E.R.* game series: *Shadow of Chernobyl*, *Clear Sky* and *Call of Pripyat*
- *Tabula Rasa*
- *Trine*
- *Trine 2*
- *Viva Pinata*

## Game engines featuring deferred shading or rendering techniques

- *AnvilNext*
- *Chrome Engine*
- *CryEngine 3*
- *Fox Engine*
- *Frostbite 2*
- *GameStart*
- *Haemimont Games Engine (HGE)*
- *I-Novae*
- *Leadwerks*
- *MT Framework*
- *Rockstar Advanced Game Engine*
- *Torque 3D*
- *Unity*
- *Unreal Engine 4*
- *Vision*
- *Creation Engine as of Fallout 4 and Skyrim SE*
- *Fusion Engine (early Illusion Engine) as of Mafia III and Mafia: Definitive Edition*

- Raylib
- X-Ray Engine

## History

The idea of deferred shading was originally introduced by Michael Deering and his colleagues in a paper published in 1988 titled *The triangle processor and normal vector shader: a VLSI system for high performance graphics*. Although the paper never uses the word "deferred", a key concept is introduced; each pixel is shaded only once after depth resolution. Deferred shading as we know it today, using G-buffers, was introduced in a paper by Saito and Takahashi in 1990, although they too do not use the word "deferred". The first deferred shaded video game was *Shrek*, an Xbox launch title shipped in 2001. Around 2004, implementations on commodity graphics hardware started to appear. The technique later gained popularity for applications such as video games, finally becoming mainstream around 2008 to 2010.
