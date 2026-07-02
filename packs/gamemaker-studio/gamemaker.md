---
title: "GameMaker"
source: https://en.wikipedia.org/wiki/GameMaker
domain: gamemaker-studio
license: CC-BY-SA-4.0
tags: gamemaker studio, gamemaker language, yoyo games, gml scripting
fetched: 2026-07-02
---

# GameMaker

**GameMaker** (originally **Animo**, **Game Maker** (until 2011) and **GameMaker Studio**) is a series of cross-platform game engines created by Mark Overmars in 1999 and developed by YoYo Games since 2007. The latest iteration of *GameMaker* was released in 2026.

GameMaker accommodates the creation of cross-platform and multi-genre video games using a custom drag-and-drop visual programming language or a scripting language known as Game Maker Language (GML), which can be used to develop more advanced games. GameMaker was originally designed to allow novice programmers to be able to make computer games without much programming knowledge by use of these actions. Recent versions of software also focus on appealing to advanced developers.

## Overview

GameMaker is primarily intended for making games with 2D graphics, allowing out-of-box use of raster graphics, vector graphics (via SWF), and 2D skeletal animations (via Esoteric Software's Spine) along with a large standard library for drawing graphics and 2D primitives. While the software allows for limited use of 3D graphics, this is in the form of vertex buffer and matrix functions, and as such not intended for novice users.

The engine uses Direct3D on Windows, UWP, and Xbox One; OpenGL on macOS and Linux; OpenGL ES on Android and iOS, WebGL or 2d canvas on HTML5, and proprietary APIs on consoles.

The engine's primary element is an IDE with built-in editors for raster graphics, level design, scripting, paths, and shaders (GLSL or HLSL). Additional functionality can be implemented in software's scripting language or platform-specific native extensions. In GameMaker Studio 2, users can choose whether to export the game as an NSIS installer, or a .zip file containing the game, the data.win file, and any files added under the "Included Files" tab in the editor.

### Supported platforms

GameMaker supports building for Microsoft Windows, macOS, Ubuntu, HTML5, Android, iOS, Amazon Fire TV, Android TV, Raspberry Pi, Microsoft UWP, PlayStation 4, Nintendo Switch and Xbox One; support for PlayStation 5 and Xbox Series X|S was announced in February 2021 though an "Enterprise" license is needed to build games for these consoles. In past, GameMaker supported building for Windows Phone (deprecated in favor of UWP), Tizen, PlayStation 3, and PlayStation Vita (not supported in GMS2 "largely for business reasons"). PlayStation Portable support was demonstrated in May 2010, but never made publicly available (with only a small selection of titles using it).

Between 2007 and 2011, YoYo Games maintained a custom web player plugin for GameMaker games before releasing it as open-source mid-2011 and eventually deprecating it in favor of HTML5 export.

Prior to August 2021, users had to obtain a single-purchase license for one of five different platforms, excluding consoles, depending on the target platform they wanted to publish on (such as desktop or mobile). An annual license was required to publish for consoles, which was also contained in an all-encompassing annual Ultimate license that covered all supported platforms. Yoyo Games announced a change to the licensing approach in August 2021, allowing GameMaker to be used for free to learn, and eliminating the single-purchase options. Instead, it simplified the license scheme to only two tiers, one that supported publishing on all non-console platforms, and a higher tier that added in console platform publishing support at a lower rate than the prior Ultimate license. These changes were aided by the financial investment of Opera into YoYo Games to help reduce costs for GameMaker users. On 22 November 2023, GameMaker announced that it would be "free for non-commercial use on all platforms (excluding console)," and the current subscription system would be replaced by a one-time license.

## GameMaker Language

GameMaker Language (GML) is GameMaker's scripting language. It is an imperative, dynamically typed language commonly likened to JavaScript and C-like languages. The language's default mode of operation on native platforms is via a stack machine; it can also be source-to-source compiled to C++ via LLVM for higher performance. On HTML5, GML is source-to-source compiled to JavaScript with optimizations and minification applied in non-debug builds.

### GML Visual

GML Visual (originally called "Drag and Drop") is GameMaker's visual scripting tool. GML Visual allows developers to perform common tasks (like instantiating objects, calling functions, or working with files and data structures) without having to write a single line of code. It is largely aimed at novice users.

While historically GML Visual remained fairly limited in what can be comfortably done with it, GameMaker Studio 2 had seen an overhaul to the system, allowing more tasks to be done with GML Visual, and having it translate directly to code (with an in-IDE preview for users interested in migrating to code).

## History

GameMaker was originally developed by Mark Overmars. The program was first released on 15 November 1999 under the name of Animo (at the time, it was just a graphics tool with limited visual scripting capabilities). The first versions of the program were being developed in Delphi. Subsequent releases saw the name changed to Game Maker and software moving towards more general-purpose 2D game development.

Versions 5.0 and below were freeware; version 5.1 introduced an optional registration fee; version 5.3 (January 2004) introduced a number of new features for registered users, including particle systems, networking, and possibility to extend games using DLLs. Version 6.0 (October 2004) introduced limited functionality for use of 3D graphics, as well as migrating the runtime's drawing pipeline from VCL to DirectX. Growing public interest led Overmars to seek help in expanding the program, which led to partnership with YoYo Games in 2007. From this point onward, development was handled by YoYo Games while Overmars retained a position as one of the company's directors. Version 7.0 was the first to emerge under this partnership. The first macOS compatible version of the program was released in 2009, allowing games to be made for two operating systems with minimal changes.

Version 8.1 (April 2011) saw the name changed to GameMaker (lacking a space) to avoid any confusion with the 1991 software *Game-Maker*. September 2011 saw the initial release of "GameMaker: HTML5" - a new version of software with capability to export games for web browsers along with desktop. GameMaker: Studio entered public beta in March 2012 and enjoyed a full release in May 2012. This version also had the runtime rewritten in C++ to address performance concerns with previous versions. Initial supported platforms included Windows, Mac, HTML5, Android, and iOS. Additional platforms and features were introduced over the years following; Late 2012 there was an accident with anti-piracy measures misfiring for some legitimate users.

In February 2015, GameMaker was acquired by Playtech together with YoYo Games. Announcement reassured that GameMaker will be further improved and states plans to appeal to broader demographic, including more advanced developers. November 2016 saw the initial release of GameMaker Studio 2 beta, with full release in March 2017. This version sports a completely redesigned IDE (rewritten in C#) and a number of new editor and runtime features.

In August 2020, major update 2.3 was released, bringing a host of new features to IDE, runtime, and the scripting language. In January 2021, YoYo Games was sold to Opera Software for roughly 10 million USD. The development team of GameMaker remains the same, and has not caused any major development changes to GameMaker Studio. In August 2021, YoYo Games announced that they would be changing their licenses to offer a free version of the GameMaker engine. In January 2022, YoYo Games changed GameMaker Studio 2's numbering scheme so the version corresponds to the year and the month it was released (For example, 2022.1 for January 2022). In April 2022, YoYo Games dropped the *GameMaker Studio 2* name in order to match its new version numbering scheme, changing it to simply GameMaker.

## Reception

Douglas Clements of *Indie Game Magazine* wrote that the program "[s]implifies and streamlines game development" and is "easy for beginners yet powerful enough to grow as you develop", though noting that "resource objects have to be gathered if unable to create" and that licensing between Steam and the YoYo Games website is "convoluted".

## Use in schools

GameMaker was used in schools because of its drag and drop programming interface. It preceded programming environments which were developed for educational use such as Scratch and Walter Bender's Turtle Blocks. Its use in schools was preceded by Logo but Logo was text based rather than drag and drop. For teachers using GameMaker, it shared a Constructionist learning theory with Logo.
