---
title: "Phaser (game framework)"
source: https://en.wikipedia.org/wiki/Phaser_(game_framework)
domain: phaser-framework
license: CC-BY-SA-4.0
tags: phaser framework, phaser game framework, html5 game framework, phaser scene
fetched: 2026-07-02
---

# Phaser (game framework)

**Phaser** is a 2D game framework used for making HTML5 games for desktop and mobile. It is free software developed by Photon Storm.

Phaser uses both a canvas and WebGL renderer internally and can automatically swap between them based on browser support. This allows for fast rendering across desktop and mobile. It uses the Pixi.js library for rendering.

Games can be deployed to iOS, Android and native desktop apps via third-party tools like Apache Cordova.

## History

Richard Davey announced the first release of Phaser on a blog post in April 2013. Version 1.0 was released in September 2013, incorporating the Pixi.js library for rendering.

The last official version of Phaser 2 was 2.6.2, but to allow improvements to the stable version while working on Phaser 3, a new repository was created: Phaser CE (Community Edition).

The last official version of Phaser 3 was 3.90.0. Most elements and features of the framework were rebuilt from scratch using a fully modular structure and data-orientated approach. Phaser 3 included a brand-new custom WebGL renderer designed for modern 2D games. Since then, much of the documentation and examples for users has been completed, and the majority of features have been implemented.

Development of Phaser 4 was announced August 19, 2019. It mainly focuses on a rewrite of the renderer designed for performant and modern 2D games, while keeping the API mostly the same. The first version of Phaser 4 was released on April 10th, 2026.

## Architecture and features

Phaser can run in any web browser that supports the canvas element. Games made with phaser are developed either in JavaScript or TypeScript. A web server is required to load resources like images, sounds, and other game files, as browsers require web pages to access files only from the same origin.

### Rendering

Phaser can be either rendered in WebGL or a canvas element, with an option to use WebGL if the browser supports it, or if a device does not support it, it will fall back to Canvas.

### Physics

Phaser ships with three physics systems: Arcade Physics, Ninja Physics and P2.JS.

Arcade Physics is for high-speed AABB collision only. Ninja Physics allows for complex tiles and slopes, which are adequate for level scenery, and P2.JS is a full-body physics system, which supports constraints, springs, and polygon among others.

As of phaser 3.6, there are two major physics engines. These are called Arcade and Matter. There is also a less known engine similar to Arcade called Impact.

Arcade is probably the most used out of the three, since it is fast and easy to use. It uses axis-aligned (not rotated) rectangles and circles for collision detection on top of all basic physics engine features, like gravity, acceleration and drag. Its downside is that its features are limited. Complex hitboxes can be very difficult to make out of the supported shapes and multiple objects in close proximity can cause stability issues.

Matter is the more advanced physics engine but its complexity also rises with the added features. Matter is capable of simulating very realistic full-body physics. It supports a multitude of features such as rigid, compound and composite bodies, elastic collisions, stable stacking and physical properties like mass and density.

Impact holds many similarities to Arcade but brings some useful advantages. For example, Impact can have slopes in its tilemaps, which is not possible with Arcade's axis-aligned rectangles. However, the downside to this is that developers have to use the Impact engine's developer's own "Weltmeister" editor for creating tilemaps.

### Animation

Phaser supports spritesheets and texture atlases, which include multiple frames or character animations. Developers can use frame sequences to craft animations. Phaser's animation sequence capability allows developers to effortlessly create animation sequences for sprites, including control over looping, speed, and frame rates. From simple character movements to complex special effect animations. Furthermore, Phaser offers a built-in tweening engine for crafting smooth transition animations. This is particularly useful for effects like fading, scaling, rotating, and can also be used for other complex special effect animations.

### Audio

Phaser allows developers to manage and play web audio and HTML5 audio, providing a rich set of audio effect control options, including volume, mute, looping, fading in and out, and sound positioning. These attributes can be adjusted as needed. Additionally, Phaser supports preloading of audio files, ensuring sound plays without delay, ready for immediate playback, delivering a better gaming experience.

## Comparison with other lightweight game engines

Phaser vs. Cocos2d-x: Cocos2d-x is a cross-platform 2D/3D game development framework. Compared with Phaser, it supports more native platforms, such as iOS and Android. However, Phaser is based on HTML5, which makes it easier to integrate with modern web technologies and is suitable for rapid iteration and deployment of web platforms.

Phaser vs. Unity: Unity is a well-known game development engine in the industry, supporting both 2D and 3D game development. Compared with Phaser, Unity provides more powerful editor tools and wider platform support. But Phaser is relatively lightweight, and the entry barrier may be lower for beginners, especially those who only want to focus on web game development.

Phaser vs. Three.js: Three.js is a cross-browser Javascript and application programming interface used to create and display animated 3D computer graphics in a web browser using WebGL. It is more general than Phaser. Instead, Phaser focuses more on browser-side game development.
