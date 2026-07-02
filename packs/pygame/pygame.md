---
title: "Pygame"
source: https://en.wikipedia.org/wiki/Pygame
domain: pygame
license: CC-BY-SA-4.0
tags: pygame library, python game library, pygame surface, sdl python
fetched: 2026-07-02
---

# Pygame

**Pygame** is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

## History

Pygame was originally written by Pete Shinners to replace PySDL after its development stalled. It has been a community project since 2000 and is released under the free software GNU Lesser General Public License (which "provides for Pygame to be distributed with open source and commercial software").

## Development of version 2

Pygame version 2 was planned as "Pygame Reloaded" in 2009, but development and maintenance of Pygame completely stopped until the end of 2016 with version 1.9.1. After the release of version 1.9.5 in March 2019, development of a new version 2 was active on the roadmap.

Pygame 2.0 released on 28 October 2020, Pygame's 20th anniversary.

## Features

Pygame uses the Simple DirectMedia Layer (SDL) library, with the intention of allowing real-time computer game development without the low-level mechanics of the C programming language and its derivatives. This is based on the assumption that the most expensive functions inside games can be abstracted from the game logic, making it possible to use a high-level programming language, such as Python, to structure the game.

Other features that SDL does have include vector math, collision detection, 2D sprite scene graph management, MIDI support, camera, pixel-array manipulation, transformations, filtering, advanced freetype font support, and drawing.

Applications using Pygame can run on Android phones and tablets with the use of Pygame Subset for Android (pgs4a). Sound, vibration, keyboard, and accelerometer are supported on Android.

## Community

Following disagreements between former core developers and the repository owner, a fork known as pygame-ce (Community Edition) was created.

There is a regular competition, called PyWeek, to write games using Python (and usually but not necessarily, Pygame). The community has created many tutorials for Pygame.

## Sample code

The following code makes an image of a raccoon("raccoon.png") bounce when hitting an edge.

```mw
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
clock.tick(30)
black = 0, 0, 0
raccoon = pygame.image.load("raccoon.png")
raccoon = pygame.transform.scale(raccoon, (200, 140))
raccoonrect = raccoon.get_rect()
velocity = [1, 1]

while True:
    raccoonrect = raccoonrect.move(velocity)
    if raccoonrect.left < 0 or raccoonrect.right > 1280:
        velocity[0] = -velocity[0]
        raccoon = pygame.transform.flip(raccoon, True, False)
    if raccoonrect.top < 0 or raccoonrect.bottom > 720:
        velocity[1] = -velocity[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # screen update
    screen.fill(black)
    screen.blit(raccoon, raccoonrect)
    pygame.display.flip()
```

## Notable games using Pygame

- *Frets on Fire*
- *Dangerous High School Girls in Trouble!*
