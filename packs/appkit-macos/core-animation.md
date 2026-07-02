---
title: "Core Animation"
source: https://en.wikipedia.org/wiki/Core_Animation
domain: appkit-macos
license: CC-BY-SA-4.0
tags: appkit framework, macos gui, aqua interface, quartz compositor
fetched: 2026-07-02
---

# Core Animation

**Core Animation** is an animation graphics compositing framework used by macOS (Mac OS X Leopard and later), iOS, watchOS, and tvOS to produce animated user interfaces.

## Overview

**Core Animation** provides a way for developers to produce animated user interfaces via an *implicit animation* model as well as an "explicit" model. The developer specifies the original and final states of an object, and Core Animation handles interpolation. This allows animated interfaces to be created with relative ease, as no specific code for the animation is required by the developer.

Core Animation can animate any visual element, and it provides a unified way of accessing Core Image, Core Video, and the other Quartz technologies. Core Animation rendering can be accelerated by a graphics processor (GPU).

Animated sequences execute in a thread independent from the main run loop, allowing application processing to occur while the animation is in progress. In this way, application performance is not affected, and animations can be stopped, reversed, or *retargeted* while in progress.

## History

Core Animation first appeared in Mac OS X Leopard, but actually first emerged from the iPhone software team. It was shown publicly for the first time on August 7, 2006 during WWDC 2006. At the Macworld Expo 2007, Apple announced that the iPhone runs a specially adapted version of OS X and uses Core Animation.
