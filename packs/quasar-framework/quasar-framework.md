---
title: "Quasar Framework"
source: https://en.wikipedia.org/wiki/Quasar_Framework
domain: quasar-framework
license: CC-BY-SA-4.0
tags: quasar framework, vue component library, single codebase deploy, material vue controls
fetched: 2026-07-02
---

# Quasar Framework

**The Quasar Framework** (commonly referred to as **Quasar**; pronounced /ˈkweɪ.zɑːr/) is an open-source Vue.js based framework for building apps with a single codebase. It can be deployed on the Web as a SPA, PWA, SSR, to a Mobile App, using Cordova for iOS & Android, and to a Desktop App, using Electron for Mac, Windows, and Linux. Quasar was created by Razvan Stoenescu and is maintained by a small team of developers (also known as the "core team") and contributors. Most from the core team currently work at various companies such as Lenovo, IntelliView Technologies Inc. and AG Development Services.

## Overview

Quasar focuses on building VueJS user interfaces quickly. The user only needs to write one authoritative source of code for all platforms: responsive desktop/mobile websites (SPA, SSR + SPA client takeover, SSR + PWA client takeover), PWAs (Progressive Web Apps), mobile apps (that look native) and multi-platform desktop apps (through Electron) and also browser extensions.

Quasar is designed with performance, responsiveness and inter-operability in mind.

## History

Quasar was created by Razvan Stoenescu after working for IBM and Lenovo using constantly new and different software tools to create all the separate types of iOS apps, Android apps, web applications, Windows Desktop apps, Apple Desktop apps, and PWAs. He later summed up his thought process: "I longed for a single framework that would remove all the complexity and produce all these different flavors of apps … from a SINGLE codebase. Unable to locate such a mythical tool, I decided to build it."

The first source code commit to the project was dated 2015, and Quasar stable 1.0 release was released in July 2019. The first Quasar conference took place in July 2020. Quasar v2 (with Vue.js 3) went stable in 2.0.0 release in June 2021.

## Features

### Components

Quasar apps are built using Vue Single File Components and Quasar Components. Vue Single file components contain multiple sections: template (HTML), script (Javascript) and style (CSS/Stylus/SASS/SCSS/Less) - all in the same file. The code snippet below contains an example of the structure of a Vue Single File Component:

```mw
<template>
  <!-- you define your Vue template here -->
</template>

<script setup>
// This is where your Javascript goes
// to define your Vue component, which
// can be a Layout, a Page or your own
// component used throughout the app.
</script>

<style>
/* This is where your CSS goes */
</style>
```

Quasar components are HTML tags that begin with `q` and link to the `/quasar.config` file.

## Ecosystem

The core library comes with tools and libraries both developed by the core team and contributors.

### Official tooling

Quasar Framework consists of several key components:

**Quasar CLI**

A command-line interface tool that facilitates the creation and development of cross-platform applications. It provides a global environment for app initialization and management.

**Quasar App**

The local development and build environment within the Quasar CLI. It includes:

- A development server for real-time previewing of changes
- Build systems for deploying applications to multiple platforms, including:
  - Web
  - Progressive Web Applications (PWA)
  - Server-Side Rendering (SSR)
  - Cordova
  - Capacitor
  - Electron
  - Browser Extensions

**Quasar UI**

A comprehensive library of user interface components designed for use within Quasar applications.
