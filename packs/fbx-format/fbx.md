---
title: "FBX - Wikipedia"
source: https://en.wikipedia.org/wiki/FBX
domain: fbx-format
license: CC-BY-SA-4.0
tags: fbx format, autodesk fbx, 3d model exchange, fbx interchange
fetched: 2026-07-02
---

# FBX

**FBX** (from *Filmbox*) is a proprietary file format (`.fbx`) developed by Kaydara and owned by Autodesk since 2006. It is used to provide interoperability between digital content creation applications. FBX is also part of Autodesk Gameware, a series of video game middleware.

## History

FBX originated as a replacement file format for Canadian company Kaydara's Filmbox, a software for recording data from motion capture devices. Prior to 1996, Filmbox 1.0 used a file format called FLM. The format only supported motion data, user preferences and a list of devices used in the capturing of the motion data. This data was a serialized version of the libraries (binary dump), containing read/write memory data. This method of storing data did not work well with different versions of Filmbox. There was also demand from early adopters of Filmbox to implement a target character in a scene with the motion capture data, to enable the visualization of the data in a 3D view with display markers.

In 1996, Kaydara released a new native file format with Filmbox 1.5 called FBX, which used an object-based model, allowing for the storing of motion, along with 2D, 3D, audio, and video data. The format saw wider support from other 3D software packages such as Cinema 4D, SoftImage 3D, PowerAnimator, LightWave 3D, 3D Studio MAX and TurboCAD.

Filmbox was renamed MotionBuilder in 2002 with the release of version 4.0. In 2003, Kaydara launched FBX for Apple's QuickTime Viewer. Alias announced its intention to acquire Kaydara on August 8, 2004, reaching an agreement in September. A Software Development Kit was developed in 2005 to standardize the object model and allow other software developers to provide plug-ins of their own. Alias was acquired by Autodesk on January 10, 2006. Later in 2006, support for properties was added to FBX.

## Limitations

The FBX file format is proprietary; however, the format description is exposed in the FBX Extensions SDK which provides header files for the FBX readers and writers.

There are two FBX SDK bindings for C++ and Python supplied by Autodesk. Blender includes a Python import and export script for FBX, written without using the FBX SDK and The OpenEnded Group's Field includes a Java-based library for loading and extracting parts from a FBX file.

The Godot game engine can import FBX files without using the FBX SDK. In Godot 3.2 this was handled by the Assimp library. This was rewritten in Godot 3.3, and replaced by a fork of Facebook's FBX2glTF utility in Godot 4.0. Support for the open-source ufbx importer was added for the Godot 4.3 release. Godot 4.3 allows both ufbx and FBX2glTF to work in tandem by keeping the previously used importer for a given file as the default importer for that file, however new FBX files in the same project will, by default, use ufbx.

## File format

The FBX can be represented on-disk as either binary or ASCII data; its SDK supports reading and writing both.

While neither of the formats is documented, the ASCII format is a tree structured document with clearly named identifiers. For the FBX binary file format, the Blender Foundation published an unofficial specification, as well as a higher level unofficial spec (work in progress) for how actual data is laid out in FBX (independent of ASCII or binary format).

List of FBX versions (and alternate names in brackets):

- 6.x (FBX 2006, FBX 2009, FBX 2010)
- 7.1 (FBX 2011)
- 7.2 (FBX 2012)
- 7.3 (FBX 2013)
- 7.4 (FBX 2014)
- 7.5 (FBX 2016.1.2)
