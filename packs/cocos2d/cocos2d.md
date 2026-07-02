---
title: "Cocos2d"
source: https://en.wikipedia.org/wiki/Cocos2d
domain: cocos2d
license: CC-BY-SA-4.0
tags: cocos2d framework, cocos game engine, cocos creator, cocos2d sprite
fetched: 2026-07-02
---

# Cocos2d

**Cocos2d** is an open-source game development framework for creating 2D games and other graphical software for iOS, Android, Windows, macOS, Linux, HarmonyOS, OpenHarmony and web platforms. It is written in C++ and provides bindings for various programming languages, including C++, C#, Lua, and JavaScript. The framework offers a wide range of features, including physics, particle systems, skeletal animations, tile maps, and others.

Cocos2d was first released in 2008, and was originally written in Python. It contains many branches with the best known being Cocos2d-ObjC (formerly known as Cocos2d-iPhone), Cocos2d-x, Cocos2d-JS and Cocos2d-XNA. There are also many third-party tools, editors and libraries made by the Cocos2d community, such as particle editors, spritesheet editors, font editors, and level editors, like SpriteBuilder and CocoStudio.

## Sprites and scenes

All versions of Cocos2d work using the basic primitive known as a sprite. A sprite can be thought of as a simple 2D image, but can also be a container for other sprites. In Cocos2D, sprites are arranged together to form a scene, like a game level or a menu. Sprites can be manipulated in code based on events or actions or as part of animations. The sprites can be moved, rotated, scaled, have their image changed, etc.

## Features

### Animation

Cocos2D provides basic animation primitives that can work on sprites using a set of actions and timers. They can be chained and composed together to form more complex animations. Most Cocos2D implementations let you manipulate the size, scale, position, and other effects of the sprite. Some versions of Cocos2D let you also animate particle effects, image filtering effects via shaders (warp, ripple, etc.).

### GUI

Cocos2D provides primitives to represent common GUI elements in game scenes. This includes things like text boxes, labels, menus, buttons, and other common elements.

### Physics system

Many Cocos2D implementations come with support for common 2D physics engines like Box2D and Chipmunk.

### Audio

Various versions of Cocos2D have audio libraries that wrap OpenAL or other libraries to provide full audio capabilities. Features are dependent on the implementation of Cocos2D.

### Scripting support

Support binding to JavaScript, Lua, and other engines exist for Cocos2D. For example, Cocos2d JavaScript Binding (JSB) for C/C++/Objective-C is the wrapper code that sits between native code and JavaScript code using Mozilla's SpiderMonkey. With JSB, you can accelerate your development process by writing your game using easy and flexible JavaScript.

### Editor support

#### End of life support

- SpriteBuilder: Previously known as CocosBuilder, SpriteBuilder is an IDE for Cocos2D-SpriteBuilder apps. SpriteBuilder is free and its development was sponsored by Apportable, who also sponsored the free Cocos2D-SpriteBuilder, Cocos3D, and Chipmunk physics projects. It was available as a free app in the Mac App Store. Its latest official version is 1.4. Its latest unofficial version is 1.5 which is compatible with cocos2d-objC 3.4.9. It supports Objective-C.
- CocoStudio: a proprietary toolkit based on Cocos2d-x, containing UI Editor, Animation Editor, Scene Editor and Data Editor, together forming a complete system; the former two are tools mainly for artists while the latter are two mainly for designers. This is a proprietary project developed by Chukong Technologies. Its latest version is 3.10 which is compatible with cocos2d-X 3.10. It supports C++. In April 2016 it was deprecated and replaced with Cocos Creator.

#### Current support

- Cocos Creator, which is a proprietary unified game development tool for Cocos2d-X. As of August 2017, it supports JavaScript and TypeScript only and does not support neither C++ nor Lua. It was based on the free Fireball-X. C++ and Lua support for creator is under alpha-stage development since April 2017.
- SpriteBuilderX, a free scene editor for Cocos2d-X with C++ support and runs on macOS only.
- X-Studio, a proprietary scene editor for Cocos2d-X with Lua support and runs on Windows only.
- CCProjectGenerator: a project generator for Cocos2d-ObjC 3.5 that generates Swift or Objective-C projects for Xcode.

## Supported platforms and languages

| Branch | Target Platform | API Language |
|---|---|---|
| Cocos2d | Windows, OS X, Linux | Python 2.6, 2.7 or 3.3+, Objective-C |
| Cocos2d-x | iOS, Android, Tizen, Windows, Windows Phone 8, Linux, Mac OS X | C++, Lua, JavaScript |
| Cocos2d-ObjC | iOS, Mac OS X, tvOS | Objective-C, Swift |
| Cocos2d-html5 | HTML5-ready browsers | JavaScript |
| Cocos2d-xna | Windows Phone 7 & 8, Windows 7 & 8, Xbox 360 | C# |
| Cocos Creator | Android, iOS, HarmonyOS | C#, C++, TypeScript, JavaScript |

## History

### Cocos2d (Python)

February 2008, in the village of Los Cocos, near Córdoba, Argentina, Ricardo Quesada, a game developer, and Lucio Torre created a 2D game engine for Python with several of their developer friends. They named it "Los Cocos" after its birthplace. A month later, the group released the version 0.1 and changed its name to "Cocos2d".

### Cocos2d-iPhone

Attracted by the potential of the new Apple App Store for the iPhone, Quesada rewrote Cocos2d in Objective-C and in June 2008 released "Cocos2d for iPhone" v0.1, the predecessor of the later Cocos2d family.

Cocos2D-ObjC (formerly known as Cocos2D-iPhone and Cocos2D-SpriteBuilder), is maintained by Lars Birkemose.

Also, the English designer Michael Heald designed a new logo for Cocos2d (the Cocos2d logo was previously a running coconut).

### Cocos2d-x

November 2010, a developer from China named Zhe Wang branched Cocos2d-x based on Cocos2d. Cocos2d-x is also a free engine under MIT License, and it allows for compiling and running on multiple platforms with one code base.

In 2013, Quesada left cocos2d-iPhone and joined in cocos2d-x team. In March 2017, Quesada was laid off from the Chukong company. In 2015, there are 4 cocos2d branches being actively maintained.

Cocos2d-x & Cocos2d-html5 is maintained and sponsored by developers at Chukong Technologies. Chukong is also developing CocoStudio, which is a WYSIWYG editor for Cocos2d-x and Cocos2D-html5, and a free Cocos3d-x fork of the Cocos3D project.

### Other ports, forks, and bindings

Cocos2d has been ported into various programming languages and to all kinds of platforms. Among them there are:

- ShinyCocos, in Ruby
- Cocos2d-Android, in Java for Android
- Cocos2d-windows, in C++ for Windows XP and Windows 7
- CocosNet, in C# based on Mono
- Cocos2d-javascript, in JavaScript for web browsers
- Cocos2d-XNA was born in cocos2d-x community for supporting Windows Phone 7, but now it's branched to an independent project using C# and mono to run on multiple platforms. Jacob Anderson at Totally Evil Entertainment is leading this branch.
- Cocos3d works as an extension on cocos2d-iPhone, written in Objective-C. Bill Hollings at Brenwill Workshop Ltd is leading this branch.
- Axmol Engine is an open-source, C++ multi-platform engine designed for mobile devices, desktop, and Xbox, well-suited for 2D game development. It was launched in November 2019 as a fork of Cocos2d-x v4.0.

## Games developed with cocos2d

- *FarmVille*
- *Plague Inc.*
- *Geometry Dash* (cocos2d-x)
- *Legendary Wars*
- *Miitomo* (cocos2d-x)
- *Badland* (cocos2d-iphone)
- *Shadow Fight 2* (cocos2d-x)
- *Cookie Run: OvenBreak*
- *Fire Emblem Heroes*
- *Magia Record*
- *Harry Potter: Hogwarts Mystery* (cocos2d-x)
- *FlyMe2theMoon* (cocos2d)
- *Pokémon: Magikarp Jump*
- *Chrono Trigger* (Steam and mobile versions)
