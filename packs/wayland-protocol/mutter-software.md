---
title: "Mutter (software)"
source: https://en.wikipedia.org/wiki/Mutter_(software)
domain: wayland-protocol
license: CC-BY-SA-4.0
tags: wayland protocol, wayland compositor, weston reference, display server
fetched: 2026-07-02
---

# Mutter (software)

**Mutter** is a display server and window manager for the Wayland protocol ("compositor"). It is the default window manager for GNOME.

Mutter was initially a compositing window manager designed and implemented for the X Window System, but then evolved to be a Wayland compositor. It became the default window manager in GNOME 3, replacing Metacity, which used GTK for rendering. The name "Mutter" is a combination of "Metacity" and "Clutter".

## Window management

Mutter can function as a standalone window manager for GNOME-like desktops, and serves as the primary window manager for the GNOME Shell, which is an integral part of GNOME since version 3. Mutter is extensible with plug-ins, and supports numerous visual effects. GNOME Shell is written as a plug-in to Mutter.

## Release history

- Support for HiDPI was added to version 3.13 of Mutter by Adel Gadllah.

- In version 3.13.2 logind integration replaced mutter-launch.

- In version 3.13.3 (June 24, 2014) the server side bits of `wl_touch_interface` were implemented by Carlos Garnacho.
- Support for X11 was disabled at compile-time in GNOME 49 and officially dropped with the X11 session code removed GNOME 50, rendering Mutter exclusively a Wayland compositor. GNOME 49 and later can still run most X11 apps on the Wayland session via XWayland.

## Forks

### Muffin

Muffin is a fork of Mutter by the Linux Mint team for their Cinnamon desktop environment. Cinnamon's shell, a fork of GNOME Shell, is written as a plugin for Muffin.
