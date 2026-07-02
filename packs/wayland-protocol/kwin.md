---
title: "KWin"
source: https://en.wikipedia.org/wiki/KWin
domain: wayland-protocol
license: CC-BY-SA-4.0
tags: wayland protocol, wayland compositor, weston reference, display server
fetched: 2026-07-02
---

# KWin

**KWin** is a Wayland compositor and an X window manager. It is released as a part of KDE Plasma, for which it is the default window manager. KWin can also be used on its own or with other desktop environments.

KWin can be configured by scripting using QML or QtScript, both of which are based on ECMAScript.

## History

| Name | Version | Details |
|---|---|---|
| KWM | 1.0 |   |
| KWin | 2.0 | Extended support for themes and window effects. |
| 3.0 | Improved support for the extended ICCCM standards from freedesktop.org. |   |
| 4.0 | Compositing support and Compiz-like effects. |   |
| 4.4 (02/2010) | Maximizing and tiling by snapping to the screen-edges, grouping and tabbing. |   |
| 4.5 | Tiling. (removed in version 4.10) |   |
| 4.9 | Incompatible API change. |   |
| 4.11 | Last release based on KDE Platform 4, added experimental Wayland support. |   |
| 5.0 | First release based on KDE Frameworks 5 and Qt 5. |   |
| 5.12 | Released February 2018, KWin/X11 got feature frozen, meaning no new X11 specific features will be added. Martin Flöser stated that new features are easy and straight forward with the Wayland back-end, but require considerably more development to add the same feature to the X11 back-end. |   |

## Look and feel

There are many window decorations for KWin, including the current default Breeze (shown below), the previous default Oxygen, Microsoft Windows-like Redmond, and Keramik.

## Compositing

Currently available compositing backends include OpenGL 1.2, OpenGL 2.0, OpenGL 3.1 and OpenGL ES 2.0.

### Included effects

As of KDE 4.3, the following effects are built-in:

#### Accessibility

| Name | Description |
|---|---|
| Invert | Inverts the color of the desktop and windows |
| Looking glass | A screen magnifier that looks like a fish eye lens |
| Magnifier | Magnify the section of the screen that is near the mouse cursor |
| Sharpen | Makes the entire desktop look sharper |
| Snap Helper | Helps locate the centre of the screen when moving a window |
| Track mouse | Display a mouse cursor locating effect when activated |
| Zoom | Magnify the entire desktop |

#### Appearance

| Name | Description |
|---|---|
| Explosion | Make windows explode when they are closed |
| Fade | Make windows smoothly fade in and out when they are shown or hidden |
| Fade Desktop | Fade between virtual desktops when switching between them |
| Fall apart | Close windows fall into pieces |
| Highlight Windows | Highlight the appropriate window when hovering over taskbar entries |
| Login | Smoothly fade to the desktop when logging in |
| Logout | Desaturate the desktop when displaying the logout dialog |
| Magic Lamp | Simulate a magic lamp when minimizing windows |
| Minimize animation | Animate the minimizing of windows |
| Mouse mark | Allows you to draw lines over your desktop |
| Scale In | Animate the appearance of windows |
| Sheet | Make modal dialogues smoothly fly in and out when shown or hidden |
| Slide | Slide windows across the screen when switching virtual desktops |
| Sliding popups | Sliding animation for Plasma Popups |
| Taskbar Thumbnails | Display window thumbnails when hovering over taskbar entries |
| Thumbnail aside | Display window thumbnails on the edge of the screen |
| Translucency | Make windows translucent under different conditions |
| Wobbly windows | Deform windows while they are moving |

#### Candy

| Name | Description |
|---|---|
| Snow | Simulate snow falling on the desktop |

#### Focus

| Name | Description |
|---|---|
| Dialog parent | Darkens the parent windows of the currently active dialogue |
| Dim Inactive | Darken inactive windows |
| Dim screen for administrator mode | Darkens the entire screen when requesting root privileges |
| Slide Back | Slide back windows losing focus |

#### Tools

| Name | Description |
|---|---|
| Show FPS | Show kwins performance in the corner of the screen |
| Show Paint | Highlight areas of the desktop that have been recently updated |

#### Window management

| Name | Description |
|---|---|
| Box switch | Removed in latest versions, no longer available. |
| Cover switch | Removed in latest versions, no longer available. |
| Desktop grid | Zoom out so all desktops are displayed side-by-side in a grid |
| Flip switch | Removed in latest versions, no longer available. |
| Present windows | Zoom out until open windows can be displayed side by side |
| Resize Window | Effect to outline geometry while resizing a window |
