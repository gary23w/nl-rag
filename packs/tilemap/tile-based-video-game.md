---
title: "Tile-based video game"
source: https://en.wikipedia.org/wiki/Tile-based_video_game
domain: tilemap
license: CC-BY-SA-4.0
tags: tilemap rendering, tile-based game, tile map layer, isometric tilemap
fetched: 2026-07-02
---

# Tile-based video game

A **tile-based video game**, or **grid-based video game**, is a type of video game where the playing area consists of small square (or, much less often, rectangular, parallelogram, or hexagonal) graphic images referred to as *tiles* laid out in a grid. That the screen is made of such tiles is a technical distinction, and may not be obvious to people playing the game. The complete set of tiles available for use in a playing area is called a *tileset*. Tile-based games usually simulate a top-down, side view, or 2.5D view of the playing area, and are almost always two-dimensional.

Much video game hardware from the late 1970s through the mid-1990s has native support for displaying tiled screens with little interaction from the CPU.

## Overview

Tile-based games are not a distinct video game genre. The term refers to the technology that the hardware or game engine uses for its visual representation. For example, *Pac-Man* is an action game, *Ultima* is a role-playing video game and *Civilization* is a turn-based strategy game, but all three render the world as tiles. *Ultima III* and *Civilization* draw the tiles via software, while the maze in the original arcade version of *Pac-Man* is made of tiles displayed by the game's graphics hardware. Tiles allow developers to build with a set of reusable components instead of drawing everything individually.

Tile-based video games usually use a texture atlas for performance reasons. They also store metadata about the tiles, such as collision, damage, and entities, either with a 2-dimensional array mapping the tiles, or a second texture atlas mirroring the visual one but coding metadata by colour. This approach allows for simple, visual map data, letting level designers create entire worlds with a tile reference sheet and perhaps a text editor, a paint program, or a simple level editor (many older games included the editor in the game). Examples of tile-based game engine/IDEs include RPG Maker, Game Maker, Construct, and Godot.

Variations include level data using "material tiles" that are procedurally transformed into the final tile graphics, and groupings of tiles as larger-scale "supertiles" or "chunks," allowing large tiled worlds to be constructed under heavy memory constraints. Ultima 7 uses a "tile," "chunk" and "superchunk" three-layer system to construct an enormous, detailed world within the PCs of the early 1990s.

## History

The tile-map model was introduced to video games by Namco's arcade game *Galaxian* (1979), which ran on the Namco Galaxian arcade system board, capable of displaying multiple colors per tile as well as scrolling. It used a tile size of 8×8 pixels, which since became the most common tile size used in video games. A tilemap consisting of 8×8 tiles required 64 times less memory and processing time than a non-tiled framebuffer, which allowed *Galaxian*'s tile-map system to display more sophisticated graphics, and with better performance, than the more intensive framebuffer system previously used by *Space Invaders* (1978). Some video game consoles such as the Intellivision, released in 1979, were designed to use tile-based graphics, since their games had to fit into video game cartridges as small as 4K in size.

Home computers had hardware tile support in the form of ASCII characters arranged in a grid, usually for the purposes of displaying text, but games could be written using letters and punctuation as game elements. The Atari 400/800 home computers, released in 1979, allow the standard character set to be replaced by a custom one. The new characters don't have to be glyphs, but the walls of a maze or ladders or any game graphics that fit in an 8x8 pixel square. The video coprocessor provides different modes for displaying character grids. In most modes, individual monochrome characters can be displayed in one of four colors; others allow characters to be constructed of 2-bit pixels instead, which allowed up to 5 colors to be displayed by swapping between 2 colors via an extra bit in the tile index byte. Atari used the term *redefined characters* and not *tiles*.

The tile model became widely used in specific game genres such as platform games and role-playing video games, and reached its peak during the 8-bit and 16-bit eras of consoles, with games such as Mega Man (NES), *The Legend of Zelda: A Link to the Past* (SNES) and *Shining Force* (Mega Drive) being prime examples of tile-based games, producing a highly recognizable look and feel.

Most early tile-based games used a top-down perspective. The top-down perspective evolved to a simulated 45-degree angle, seen in 1994's *Final Fantasy VI*, allowing the player to see both the top and one side of objects, to give more sense of depth; this style dominated 8-bit and 16-bit console role-playing games. Ultimate Play the Game developed a series of video games in the 1980s that employed a tile-based isometric perspective. As computers advanced, isometric and dimetric perspectives began to predominate in tile-based games, using parallelogram-shaped tiles instead of square tiles. Notable titles include:

- *Ultima Online*, which mixed elements of 3D (the ground, which is a tile-based height map) and 2D (objects) tiles
- *Civilization II*, which updated Civilization's top-down perspective to a dimetric perspective
- The *Avernum* series, which remade the top-down role-playing series *Exile* with an isometric engine.

Hexagonal tile-based games have been limited for the most part to the strategy and wargaming genres. Notable examples include the Sega Genesis game *Master of Monsters*, SSI's *Five Star* series of wargames starting with *Panzer General*, the *Age of Wonders* series and *Battle for Wesnoth*.
