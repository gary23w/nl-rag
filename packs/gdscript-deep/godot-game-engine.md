---
title: "Godot (game engine)"
source: https://en.wikipedia.org/wiki/Godot_(game_engine)
domain: gdscript-deep
license: CC-BY-SA-4.0
tags: gdscript language, godot engine, game engine, duck typing, scripting language
fetched: 2026-07-02
---

# Godot (game engine)

**Godot** (/ˈɡɒdoʊ/ ⓘ *GOD-oh*, /ɡəˈdoʊ/ ⓘ *gə-DOH*, or /ˈɡoʊdɒt/ *GOH-dot*) is an open source game engine released under the MIT License. It was initially developed in Buenos Aires by Argentine software developers Juan Linietsky and Ariel Manzur for several companies in Latin America prior to its public release in 2014. The development environment runs on many platforms, and can export to several more. It is designed to create both 2D and 3D games targeting PC, mobile, web, and virtual, augmented, and mixed reality platforms and can also be used to develop non-game software.

## Features

Godot allows video game developers to create both 3D and 2D games using multiple programming languages, such as C++, C#, Python and GDScript. It makes use of a hierarchy of nodes to facilitate the development experience. Classes can be derived from a node type to create more specialized node types that inherit behavior. Nodes are organized inside of "scenes", which are reusable, instantiable, inheritable, and nestable groups of nodes. Nodes are connected by signals, which can transmit data objects. All game resources, including scripts and graphical assets, are saved as part of the computer's file system (rather than in a database). This storage solution is intended to facilitate collaboration between game development teams using software version control systems.

The engine enables developers to create both 2D and 3D games across desktop, mobile, browser, and console platforms without licensing fees. The engine has received updates such as a path-tracing renderer for 3D graphics, improving its capabilities for realistic rendering. It has visual scripting, cross-platform deployment, and virtual reality integration.

### Supported platforms

The engine supports deployment to multiple platforms and allows specification of texture compression and resolution settings for each platform. The website provides binaries only for the editor platforms, and exporting projects to other platforms is done within the Godot editor.

The Godot editor, used for creating Godot games, supports the following platforms:

- Desktop platforms Linux, macOS, Windows distributed on the Godot website, on Steam, on Epic, and on Itch.
- Web platform HTML5, WebAssembly with the web editor.
- Android phones and tablets (available as of Godot 3.6+ and 4.3+).
- A port of the Godot editor called Xogot runs on iPadOS.

The created games can be exported to run on the following platforms:

- Desktop platforms Linux, macOS, Windows
- Mobile platforms Android, iOS
- Web platform HTML5, WebAssembly (C# not available for the web yet)
- Virtual reality and augmented reality platforms, including HTC Vive, Valve Index, Oculus Rift, Oculus Go, Oculus/Meta Quest, all Windows Mixed Reality headsets, Apple ARKit.

The Godot engine can be run on consoles, although popular consoles are not officially supported since it is not compatible with the engine's open-source license. Games can be ported to consoles through third-party companies, including W4 Games, a commercial company founded by Godot coders. For CPU architectures, Godot officially supports x86 on all desktop platforms (both 32-bit and 64-bit where available) and has official ARM support on macOS, Linux, mobile platforms, and standalone Meta platforms (both 32-bit and 64-bit where available).

Godot also supports a mobile XR port for Meta Quest devices running Horizon OS, allowing developers to create immersive applications directly on the headset without the use of a traditional computer.

### Scripting

Godot supports a variety of programming languages for making games, including the integrated language GDScript, C++ and C#. Additionally, the engine includes GDNative (GDExtension as of Godot 4.x), a facility for creating bindings with other languages. Officially-supported GDNative/GDExtension languages include C and C++. Community-supported languages include Rust, Nim, Swift, and JavaScript. Visual coding was originally supported by the built-in language VisualScript, designed to be a visual equivalent to GDScript. VisualScript was removed from the core engine in Godot 4.0. Godot games running in the browser can interface with the browser's JavaScript code.

The Godot editor includes a text editor with auto indentation, syntax highlighting and code completion and folding. It also features a debugger with the ability to set breakpoints and program stepping.

#### GDScript

Godot has its own built-in scripting language, GDScript, a high-level, gradually typed programming language which is syntactically similar to Python. Unlike Python, GDScript is optimized for Godot's scene-based architecture and can specify strict typing of variables. Godot's developers have stated that many alternative third-party scripting languages such as Lua, Python, and Squirrel were tested before deciding that using a custom language allowed for superior optimization and editor integration.

GDScript is a continuously evolving scripting language, and changes and additions to it have been implemented for each major new release of Godot. Typed arrays and typed dictionaries were added in 4.0 and 4.4 respectively. The optional static types allow the C++ back end to apply optimizations that result in notably increased performance; statically typed GDScript has been observed to run more than 40% faster in release builds.

A simple "Hello world" program can be written like so:

```mw
func _ready():
	print("Hello World")
```

A simple variable with either dynamic or static typing can be written as:

```mw
	var hello = 12
    var bye: int = 13
```

And a constant can be written as:

```mw
	const HELLO = 12
    const BYE: int = 13
```

An example of a more complex program that generates the Fibonacci sequence is:

```mw
func _ready() -> void:
	var nterms: int = 5
	print("Fibonacci sequence:")
	for i: int in range(nterms):
		print(fibonacci(i))

func fibonacci(n: int) -> int:
	if n <= 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
```

### Rendering

Godot 3.x's graphics engine uses either OpenGL ES or Vulkan is supported in newer versions; Metal support also exists on Apple platforms. The engine supports normal mapping, specularity, dynamic shadows using shadow maps, baked and dynamic global illumination, and full-screen post-processing effects like bloom, depth of field, high-dynamic-range rendering, and gamma correction. A simplified shader language, similar to GLSL, is also incorporated. Shaders can be used for materials and post-processing. Alternatively, they can be created by manipulating nodes in a visual editor.

Godot also includes a separate 2D graphics engine that can operate independently of the 3D engine, but both can also work at the same time on the same display, so as to make complex mixes between 2D and 3D. The 2D engine supports features such as lights, shadows, shaders, tile sets, parallax scrolling, polygons, animations, physics, and particles. It is also possible to mix 2D and 3D using a "viewport node".

To support the UI and 2D Vector graphics assets support, Godot has integrated a 3rd party library, ThorVG.

### Other features

Godot contains an animation system with a GUI for skeletal animation, blending, animation trees, morphing, and real-time cutscenes. Godot has its own in-house physics engine, and as of Godot 4.x allows third parties to integrate their own physics via GDExtension. In Godot 3.x, the Bullet physics engine is included and used by default. With Godot 4.4, the Jolt Physics engine was added, though not used as the default engine until the release of Godot 4.6.

The engine has been used in educational settings and by independent developers due to its free licensing and cross-platform support.

## History

### Closed source era (2001–2014)

Juan 'reduz' Linietsky and Ariel 'punto' Manzur co-founded Codenix in 1999, a game development consulting company. As early as 2001, they began work on an engine then code-named "Larvotor" which was licensed to third-party companies in Argentina. Over the course of the following ten years, the engine was renamed to "Legacy", "NG3D", "Larvita" and finally to "Godot". The name "Godot" was chosen in reference to Samuel Beckett's play *Waiting for Godot*, as it represents the never-ending wish of adding new features in the engine, which would get it closer to an exhaustive product, even though it never would. Linietsky and Manzur joined OKAM and the company worked with a number of studios in the closed-source era including Square Enix. Linietsky indicated that their work was hampered by political and economic instability in Argentina at the time however.

### Free and open source era (2014–present)

By 2014 Linietsky was planning on moving away from Argentina, and he released the source code for Godot to the public on GitHub under the MIT License. Godot joined the Software Freedom Conservancy (SFC) on 4 November 2015. On 22 June 2016, Godot received a $20,000 Mozilla Open Source Support (MOSS) "Mission Partners" award to be used to add WebSockets, WebAssembly and WebGL 2.0 support.

The 3.0 update for Godot involved addressing a long list of desired features requiring a major refactor of the engine that had been commercially impossible while in the closed-source era. With Miguel de Icaza's support, Godot received a $24,000 donation from Microsoft in 2017 to implement C# as a scripting language in Godot. A Patreon was launched, which enabled Linietsky and Verschelde to work on the project full time. The 3.0 version launched in 2018. The 3.1 update added an OpenGL ES 2.0 renderer aimed at mobile hardware, as mobile support for ES 3.0 by manufacturers was then limited.

In 2019 two teams were formed, with Linietsky's team focusing on the Vulkan branch (later released as 4.0) and Verschelde's team covering further updates to the 3.x branch. Linietsky indicated that part of the issue was that the 3.x branch was built with older architectural principles in mind, such as single-core processors. Thus, the intention was to redevelop the core architecture for 4.0 and account for modern principles. In 2020, Godot received a $250,000 Epic Games award to improve graphics rendering and the engine's built-in game development language, GDScript. The 4.0 branch released in alpha form in early 2022, and was polished over the course of the year. That August, Linietsky and several other members of the Godot team established W4 Games to offer commercial services based on the engine, including console ports that cannot be included in its open-source codebase. In November, Godot announced plans to transition from the SFC to its own newly-formed Godot Foundation.

The full release of the 4.0 update with Vulkan support occurred in 2023, as well as the arrival of the Godot engine on the Epic Games Store. The version on Epic is identical to others in terms of both content and licensing, with the storefront simply used as a means of distribution and for updating. However, the .NET/C# support version of the engine is not available on Epic Games Store, nor Itch and Steam as well. In September, Unity Technologies announced major changes to licensing for the Unity engine including the addition of "runtime fees" that would charge users on installation of Unity games. As a result, some developers switched from Unity to Godot, and Re-Logic donated $100,000 to Godot, and further announced that it would be donating $1,000 a month going forward, in the interest of supporting an open-source alternative to Unity. Two years later, Emilio Coppola of the Godot Foundation stated that the amount of contributions "doubled" as a result of the shift.

In 2025, the Godot Foundation released an initial beta of the Godot Asset Store, intended as a replacement to the extant asset library. In June 2026, it replaced the asset library as part of version 4.7.

## Reception

In April 2026, Marcus Chen of *Tech Insider* compared Godot and Unity in various aspects. In terms of raw performance, Chen opined that Godot was more suited for video games with 2D graphics—as Unity's 2D rendering implementation was simulated in 3D—or simple 3D graphics, such as low poly, while Unity handled projects having a high graphical fidelity with better performance due to its Universal Render Pipeline. Chen noted that Godot's GDScript was similar to pseudocode and more accessible than Unity's main programming language C#, which Godot also supported in addition to C++ and Python. He also highlighted the free and open source nature of Godot also contrasted Unity's pay model, making the former relevant for developers with limited or zero budgets. Conversely, video game console support and third-party tool support were noted as advantageous for Unity. Additionally, due to its longer presence on the market, Unity was reported by Chen to feature more available assets in its asset store and a larger job market.

An in-depth performance comparison between Unity and Godot was made in May 2026 by Studio Interrupt founder Thomas Grové, who created the same project across the two engines. Grové concluded that Unity had a higher rendering performance, while Godot saw significant advantages in project loading and compiling speeds as well as having a file size of 164 megabytes, compared to Unity's 20 gigabytes.

## Version history

Godot reached version 1.0 on 15 December 2014, marking the first stable release and the addition of lightmapping, navmesh support, and more shaders. Version 1.1 was released on 21 May 2015, adding improved auto-completion in the code editor, a visual shader editor, a new API to the operating system for managing screens and windows, improved 2D physics and a rewritten 2D engine, better Blender Collada support, and a new dark theme.

Godot 2.0 was released on 23 February 2016, adding better scene instancing and inheritance, a new file system browser, multiple scene editing, and an enhanced debugger. This was followed by version 2.1 in August 2016, which introduced an asset database, profiler, and plugin API.

**Godot 3**

Version 3.0 was released on 29 January 2018, adding a new PBR renderer implemented in OpenGL ES 3.0, virtual reality compatibility, and C# support (via Mono) thanks to a $24,000 donation from Microsoft. Version 3.0 also added the Bullet physics engine in addition to the engine's built-in 3D physics back end and was the first version of Godot to be included in Debian.

Godot 3.1 was released on 13 March 2019, with the most notable features being the addition of statically typed § GDScript, a script class system for GDScript, and an OpenGL ES 2.0 renderer. Godot 3.2 was released on 29 January 2020, with the most notable features being massive documentation improvements, greatly improved C# support, and support for glTF 2.0 files.

The lead developer, Juan Linietsky, spent most of his time working on a separate Vulkan branch that would later be merged into master for 4.0, so work on 3.2 was mostly done by other contributors.

Godot 3.3 was released on 21 April 2021, with features such as ARM support on macOS, Android App Bundles support, MP3 support, Autodesk FBX support, WebXR support, and a web editor.

Godot 3.4 was released on 6 November 2021 after six months of development, implementing missing features or bug fixes that are critical for publishing 2D and 3D games with Godot 3 and making existing features more optimized and reliable.

Godot 3.5 was released on 5 August 2022 after nine months of development. Just like Godot 3.4, it was focused on implementing missing features or bug fixes important for 2D and 3D video games made with Godot 3. Features include physics interpolation in 3D, asynchronous shader compilation, and more.

Godot 3.x was placed on a much slower schedule upon the initial distribution of the 4.0 beta, and as such Godot 3.6 was released on 9 September 2024 after two years of development. The new release added 2D physics interpolation and hierarchical culling, and 3D mesh merging, level of detail, tighter shadow culling, ORM materials, and more.

**Godot 4**

Godot 4 was released on 1 March 2023. It is a major update that overhauls the rendering system, adds support for Vulkan graphics API, improves GDScript performance and usability, enhances physics and animation systems, and introduces many other features and bug fixes. The development of Godot 4 started in 2019 with a rewrite of the renderer to use Vulkan by Linietsky. In 2020, several contributors joined the development team and worked on various aspects of Godot 4, such as GDScript improvements, physics engine overhaul, animation system rewrite, editor usability enhancements and more.

The first alpha version of Godot 4 was released for testing by early adopters in January 2022. It included new features such as SDF-based global illumination, GPU-based particles, and dynamic soft shadows. In September 2022, Godot 4 reached beta stage. It also added support for WebXR, C# support for Android and iOS, and new audio features. On 1 March 2023, Godot 4 was officially released as a stable version after several beta builds and bug fixes.

This was followed by Godot 4.1 later in 2023, which added experimental scene multithreading, editor enhancements, and C# improvements. Godot 4.2 was released at 30 November 2023, implementing a rework of the animation tool and particle system, improvements to the import pipeline, and added support for FSR 2.2.

Godot 4.3 was released on 15 August 2024, and added GPU synchronization via acyclic graphs, render pipeline compositor effects, and improved 3D animation retargeting.

Godot 4.4 was released on 5 March 2025, and introduced integration with the Jolt physics engine. This was followed by Godot 4.5 in September 2025, and introduced several features such as stencil buffer support and a rework of the TileMapLayer Collision System that merges placed cell shapes into bigger collision shapes whenever possible. Version 4.6 was released in January 2026, adding the ability to be built as a standalone library and a new default theme. In June 2026, version 4.7 was released, including high dynamic range support, area lights, and drawable textures.

### Release history

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

| Version | Release date | Notes |
|---|---|---|
| Unsupported: 1.0 | December 2014 | First stable release |
| Unsupported: 1.1 | May 2015 | Added improved auto-completion in the code editor, a visual shader editor, a rewritten 2D engine, and new 2D navigation polygon support. |
| Unsupported: 2.0 | February 2016 | Updated UI and added an enhanced debugger. |
| Unsupported: 2.1 | August 2016 | Introduced an asset database, profiler, and plugin API. |
| Unsupported: 3.0 | January 2018 | Added a new PBR renderer and Mono (C#) support. Added Bullet as the default physics engine. |
| Unsupported: 3.1 | March 2019 | Added statically typed GDScript, a script class system for GDScript, and an OpenGL ES 2.0 renderer. |
| Unsupported: 3.2 | January 2020 | Added support for glTF 2.0 files, OpenGL ES 2.0 batching, C# support for iOS, and massive documentation improvements. |
| Unsupported: 3.3 | April 2021 | Added ARM support on macOS, Android AAB support, MP3 support, FBX support, WebXR support, and a web editor. |
| Unsupported: 3.4 | November 2021 | Added a new theme editor, ACES Fitted tonemapper, PWA support, physical input support, and glTF 2.0 export support. |
| Unsupported: 3.5 | August 2022 | Added editor support on Android, asynchronous shader compilation, physics interpolation, material overlay, and improved the navigation system. |
| Supported: 3.6 | September 2024 | Adds 2D physics interpolation, better culling, mesh merging, discrete LOD, transparent object sorting in 3D, and many editor improvements. LTS release. |
| Unsupported: 4.0 | March 2023 | Adds support for the Vulkan graphics API. Switches from Mono to .NET 6 CoreCLR. Introduces SDF-based global illumination, along with several editor changes and performance optimizations. |
| Unsupported: 4.1 | July 2023 | Added experimental scene multithreading, editor enhancements, and C# improvements. |
| Unsupported: 4.2 | November 2023 | Rework of animation tool and particle system, improvement on import pipeline, support for FSR 2.2. |
| Unsupported: 4.3 | August 2024 | GPU synchronization via acyclic graphs, render pipeline compositor effects, improved 3D animation retargeting. |
| Unsupported: 4.4 | March 2025 | Interactive in-game editing, Ubershaders, Jolt physics. |
| Unsupported: 4.5 | September 2025 | Wayland support, NativeAOT support, rework of 3d physics interpolation, GUI updates, stencil buffer, specular occlusion, shader precompiling. |
| Supported: 4.6 | January 2026 | Building Godot as a library, ObjectDB profiling, rotation snapping and a modernized theme. |
| Latest version: 4.7 | June 2026 | HDR support, drawable textures, area lights, virtual joysticks. |

## Usage

Many games by OKAM Studio have been made using Godot, including *Dog Mendonça & Pizza Boy*, which uses the Escoria adventure game extension. Additionally, it has been used in West Virginia's high school curriculum, due to its ease of use for non-programmers and already-existing learning materials. *Battlefield 6* uses Godot for its user-generated content creation platform, "*Battlefield Portal*".

### Notable video games made with Godot

| Year of release | Title | Developer | Notes |
|---|---|---|---|
| 2015/2016 | *Deponia* | Daedalic Entertainment | iOS and PlayStation 4 ports |
| 2016 | *The Interactive Adventures of Dog Mendonça & Pizzaboy* | OKAM Studio |   |
| 2018 | *Hardcoded* | Ghosthug Games |   |
| 2019 | *Commander Keen in Keen Dreams* | id Software/Lone Wolf Technology | First Nintendo Switch port only, not to be confused with the *Definitive Edition*. |
| 2021 | *Cruelty Squad* | Consumer Softproducts |   |
| *Sonic Colors: Ultimate* | Sonic Team/Blind Squirrel Games | A modified version of Godot was used |   |
| 2021 – 2022 | *Carol Reed Mysteries* series | MDNA Games |   |
| 2022 | *The Case of the Golden Idol* | Color gray games |   |
| *Dome Keeper* | Bippinbits |   |   |
| 2023 | *Brotato* | Blobfish |   |
| *Buckshot Roulette* | Mike Klubnika |   |   |
| *Cassette Beasts* | Bytten Studio |   |   |
| *Luck Be a Landlord* | TrampolineTales |   |   |
| 2024 | *Arctic Eggs* | The Water Museum |   |
| *Backpack Battles* | PlayWithFurcifer |   |   |
| *Halls of Torment* | Chasing Carrots |   |   |
| *The Rise of the Golden Idol* | Color Gray Games |   |   |
| *Until Then* | Polychroma Games |   |   |
| *Webfishing* | lamedeveloper |   |   |
| 2025 | *Action Game Maker* | Gotcha Gotcha Games | By the creators of *RPG Maker* |
| *Battlefield 6* | Battlefield Studios | Used for the *Battlefield Portal* map editor |   |
| *Brother Hai's Pho Restaurant* | marisa0704 |   |   |
| *Kingdoms of the Dump* | Roach Games |   |   |
| *The Roottrees are Dead* | Evil Trout | Remastered version |   |
| 2026 | *Free Stars: Children of Infinity* | Pistol Shrimp Games |   |
| *Lucid Blocks* | Lucy B. Locks |   |   |
| *Slay the Spire 2* | Mega Crit |   |   |
| *Road to Vostok* | Road to Vostok | Originally being developed with the Unity engine, but switched to Godot due to Unity's runtime fee |   |
| *Bow-wow Battle* | M.Katsu |   |   |

The engine has been used in commercial projects, including Sega's development of *Sonic Colors Ultimate*.

## Key people

### Juan Linietsky

**Juan Linietsky** (born 1976) is an Argentine software developer and game engine designer, best known as the co-creator and long-time lead developer of Godot. Linietsky was born in 1976 in Buenos Aires, Argentina. He developed an interest in programming and video games from an early age.

In 2007, Linietsky co-founded the Godot Engine project together with Manzur, aiming to provide a free and open-source alternative to proprietary game engines. He has served as the lead developer since the project's inception, managing the engine's architecture and development roadmap.

### Ariel Manzur

**Ariel Manzur** is an Argentine software developer, best known as the co‑founder of Godot. Manzur was born in Buenos Aires. From a young age he developed an interest in computing and video game technology, eventually focusing on tools that could be shared and extended by other programmers and designers.
