---
title: "MonoGame"
source: https://en.wikipedia.org/wiki/MonoGame
domain: monogame
license: CC-BY-SA-4.0
tags: monogame framework, xna framework, c sharp game framework, monogame content
fetched: 2026-07-02
---

# MonoGame

**MonoGame** is a free and open source C# framework used by game developers to make games for multiple platforms and other systems. It is also used to make Windows and Windows Phone games run on other systems. It supports iOS, iPadOS, Android, macOS, Linux, PlayStation 4, PlayStation 5, PlayStation Vita, Xbox One, Xbox Series X/S and Nintendo Switch. It implements the Microsoft XNA 4 application programming interface (API). It has been used in several notable games, including *Bastion*, *Celeste*, *Barotrauma*, *Fez*, and *Stardew Valley.*

## History

MonoGame is a derivative of XNA Touch (September 2009) started by José Antonio Farias and Silver Sprite by Bill Reiss. The first official release of MonoGame was version 2.0 with a downloadable version 0.7 that was available from CodePlex. These early versions only supported 2D sprite-based games. The last official 2D-only version was released as 2.5.1 in June 2012.

Since mid-2013, the framework has begun to be extended beyond XNA4 with the addition of new features like RenderTarget3D, support for multiple GameWindows, and a new cross-platform command line content building tool.

As of 2025, MonoGame continues to be used by indie developers for cross-platform 2D and 3D games, including recent releases on Steam and Xbox.

## Architecture

MonoGame attempts to fully implement the XNA 4 API. It accomplishes this across Microsoft platforms using SharpDX and DirectX. When targeting non-Microsoft platforms, platform-specific capabilities are utilized by way of the OpenTK library. When targeting OS X, iOS, and/or Android, the Xamarin platform runtime is necessary. This runtime provides a tuned OpenTK implementation that allows the MonoGame team to focus on the core graphics tuning of the platform.

The graphics capabilities of MonoGame come from either OpenGL, OpenGL ES, or DirectX. Since MonoGame version 3, OpenGL 2 has been the focus for capabilities. The earlier releases of MonoGame (2.5) used OpenGL 1.x for graphics rendering. Utilizing OpenGL 2 allowed MonoGame to support shaders, enabling more advanced rendering capabilities on the platform.

Content management and distribution continue to follow the XNA 4 ContentManager model. The MonoGame team has created a new content building capability that can integrate with Microsoft Visual Studio to deliver the same content building capabilities to Windows 8 Desktop that Windows 7 users used in Microsoft XNA.

## Games

| Game | Year | Developer | Publisher |
|---|---|---|---|
| *Apotheon* | 2015 | Alientrap |   |
| *Axiom Verge* | 2015 | Thomas Happ Games LLC |   |
| *Barotrauma* | 2023 | Undertow Games | Daedalic Entertainment |
| *Bastion* | 2011 | Supergiant Games | Warner Bros. Interactive Entertainment |
| Bury Me, My Love | 2017 | The Pixel Hunt | Arte France |
| *Carrion* | 2020 | Phobia Game Studio | Devolver Digital |
| *Capsized* | 2013 | Alientrap |   |
| *Celeste* | 2018 | Maddy Thorson |   |
| *Chasm* | 2018 | Bit Kid, Inc. |   |
| *Cobalt Core* | 2023 | Rocket Rat Games | Brace Yourself Games |
| *Duck Game* | 2014 | Landon Podbielski | Adult Swim Games |
| *Dust: An Elysian Tail* | 2014 | Humble Hearts |   |
| *Escape Goat* | 2011 | MagicalTimeBean |   |
| *Fez* | 2013 | Polytron Corporation | Trapdoor Microsoft Studios |
| *Flinthook* | 2017 | Tribute Games |   |
| *Infinite Flight* | 2011 | Flying Development Studio |   |
| *Terraria* | 2011 | Re-Logic | 505 Games |
| *Jump King* | 2019 | Nexile | Nexile Ukiyo Publishing |
| *Kynseed* | 2022 | PixelCount Studios |   |
| *Mercenary Kings* | 2013 | Tribute Games |   |
| Nazdar! The Game | 2023 | Michal Škoula |   |
| *Owlboy* | 2016 | D-Pad Studio |   |
| *Pyre* | 2017 | Supergiant Games |   |
| *Retro Bowl* | 2020 | New Star Games |   |
| *Salt and Sanctuary* | 2016 | Ska Studios |   |
| *Score Rush Extended* | 2016 | Xona Games | Reverb Communications |
| *Skulls of the Shogun* | 2013 | 17-BIT | Microsoft Studios |
| *Solar 2* | 2011 | Jay Watts | Murudai |
| *Stardew Valley* | 2016 | ConcernedApe |   |
| *Super Blood Hockey* | 2017 | Loren Lemcke |   |
| Tiny Life | 2023 | Ellpeck Games | Top Hat Studios, Inc. |
| *TowerFall* | 2013 | Maddy Thorson |   |
| *Transistor* | 2014 | Supergiant Games |   |
| *Unrailed!* | 2020 | Indoor Astronaut | Daedalic Entertainment |
| *Wizorb* | 2011 | Tribute Games |   |
| Woon | TBA | Tour De Pizza | Tour De Pizza |
