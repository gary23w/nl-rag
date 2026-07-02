---
title: "Sprite (computer graphics)"
source: https://en.wikipedia.org/wiki/Sprite_(computer_graphics)
domain: game-dev
license: CC-BY-SA-4.0
tags: game development, game engine, entity component system, collision detection, pathfinding, game physics
fetched: 2026-07-02
---

# Sprite (computer graphics)

In computer graphics, a **sprite** is a two-dimensional bitmap that is integrated into a larger scene, most often in a 2D video game. Originally, the term *sprite* referred to fixed-sized objects composited together, by hardware, with a background. Use of the term has since become more general.

Systems with hardware sprites include arcade video games of the 1970s and 1980s; game consoles including as the Atari VCS (1977), ColecoVision (1982), Famicom (1983), Genesis/Mega Drive (1988); and home computers such as the TI-99/4 (1979), Atari 8-bit computers (1979), Commodore 64 (1982), MSX (1983), Amiga (1985), and X68000 (1987). Hardware varies in the number of sprites supported, the size and colors of each sprite, and special effects such as scaling or reporting pixel-precise overlap.

Hardware composition of sprites occurs as each scan line is prepared for the video output device, such as a cathode-ray tube, without involvement of the main CPU and without the need for a full-screen frame buffer. Sprites can be positioned or altered by setting attributes used during the hardware composition process. The number of sprites which can be displayed per scan line is often lower than the total number of sprites a system supports. For example, the Texas Instruments TMS9918 chip supports 32 sprites, but only four can appear on the same scan line.

The CPUs in modern computers, video game consoles, and mobile devices are fast enough that bitmaps can be drawn into a frame buffer without special hardware assistance. Beyond that, GPUs can render vast numbers of scaled, rotated, anti-aliased, partially translucent, very high resolution images in parallel with the CPU.

## Etymology

According to Karl Guttag, one of two engineers for the 1979 Texas Instruments TMS9918 video display processor, this use of the word *sprite* came from David Ackley, a manager at TI. It was also used by Danny Hillis at Texas Instruments in the late 1970s. The term was derived from the fact that sprites "float" on top of the background image without overwriting it, much like a ghost or mythological sprite.

Some hardware manufacturers used different terms, especially before *sprite* became common:

**Player/Missile Graphics** was a term used by Atari, Inc. for hardware sprites in the Atari 8-bit computers (1979) and Atari 5200 console (1982). The term reflects the use for both characters ("players") and smaller associated objects ("missiles") that share the same color. The earlier Atari Video Computer System and some Atari arcade games used *player*, *missile*, and *ball*.

**Stamp** was used in some arcade hardware in the early 1980s, including *Ms. Pac-Man*.

**Movable Object Block**, or **MOB**, was used in MOS Technology's graphics chip literature. Commodore, the main user of MOS chips and the owner of MOS for most of the chip maker's lifetime, instead used the term *sprite* for the Commodore 64.

**OBJ**s (short for *objects*) is used in the developer manuals for the NES, Super NES, and Game Boy. The region of video RAM used to store sprite attributes and coordinates is called **OAM** (Object Attribute Memory). This also applies to the Game Boy Advance and Nintendo DS.

## History

### Arcade video games

The use of sprites originated with arcade video games. Nolan Bushnell came up with the original concept when he developed the first arcade video game, *Computer Space* (1971). Technical limitations made it difficult to adapt the early mainframe game *Spacewar!* (1962), which performed an entire screen refresh for every little movement, so he came up with a solution to the problem: controlling each individual game element with a dedicated transistor. The rockets were essentially hardwired bitmaps that moved around the screen independently of the background, an important innovation for producing screen images more efficiently and providing the basis for sprite graphics.

The earliest video games to represent player characters as human player sprites were arcade sports video games, beginning with Taito's *TV Basketball*, released in April 1974 and licensed to Midway Manufacturing for release in North America. Designed by Tomohiro Nishikado, he wanted to move beyond simple *Pong*-style rectangles to character graphics, by rearranging the rectangle shapes into objects that look like basketball players and basketball hoops. Ramtek released another sports video game in October 1974, *Baseball*, which similarly displayed human-like characters.

The Namco Galaxian arcade system board, for the 1979 arcade game *Galaxian*, displays animated, multi-colored sprites over a scrolling background. It became the basis for Nintendo's *Radar Scope* and *Donkey Kong* arcade hardware and home consoles such as the Nintendo Entertainment System. According to Steve Golson from General Computer Corporation, the term "stamp" was used instead of "sprite" at the time.

### Home systems

Signetics devised the first chips capable of generating sprite graphics (referred to as *objects* by Signetics) for home systems. The Signetics 2636 video processors were first used in the 1978 1292 Advanced Programmable Video System and later in the 1979 Elektor TV Games Computer.

The Atari VCS, released in 1977, has a hardware sprite implementation where five graphical objects can be moved independently of the game playfield. The term *sprite* was not in use at the time. The VCS's sprites are called *movable objects* in the programming manual, further identified as two *players*, two *missiles*, and one *ball*. These each consist of a single row of pixels that are displayed on a scan line. To produce a two-dimensional shape, the sprite's single-row bitmap is altered by software from one scan line to the next.

The 1979 Atari 400 and 800 home computers have similar, but more elaborate, circuitry capable of moving eight single-color objects per scan line: four 8-bit wide *players* and four 2-bit wide *missiles*. Each is the full height of the display—a long, thin strip. DMA from a table in memory automatically sets the graphics pattern registers for each scan line. Hardware registers control the horizontal position of each player and missile. Vertical motion is achieved by moving the bitmap data within a player or missile's strip. The feature was called *player/missile graphics* by Atari.

Texas Instruments developed the TMS9918 chip with sprite support for its 1979 TI-99/4 home computer. An updated version is used in the 1981 TI-99/4A.

### In 2.5D and 3D games

Sprites remained popular with the rise of 2.5D games (those which recreate a 3D game space from a 2D map) in the late 1980s and early 1990s. A technique called billboarding allows 2.5D games to keep onscreen sprites rotated toward the player view at all times. Some 2.5D games, such as 1993's *Doom*, allow the same entity to be represented by different sprites depending on its rotation relative to the viewer, furthering the illusion of 3D.

Fully 3D games usually present world objects as 3D models, but sprites are supported in some 3D game engines, such as GoldSrc and Unreal, and may be billboarded or locked to fixed orientations. Sprites remain useful for small details, particle effects, and other applications where the lack of a third dimension is not a major detriment.

## Systems with hardware sprites

These are base hardware specs and do not include additional programming techniques, such as using raster interrupts to repurpose sprites mid-frame.

System

Sprite hardware

Introduced

Sprites on screen

Sprites per scan line

Max.

texels

on line

Texture

width

Texture height

Colors

Zoom

Rotation

Collision detection

Transparency

Ref.

Amstrad Plus

ASIC

1990

16

16

?

16

16

15

2, 4× vertical, 2, 4× horizontal

No

No

Color key

Atari 2600

TIA

1977

5

5

19

1, 8

262

1

2, 4, 8× horizontal

Horizontal mirroring

Yes

Color key

Atari 8-bit computers

GTIA

/

ANTIC

1979

8

8

40

2, 8

128, 256

1

2× vertical, 2, 4× horizontal

No

Yes

Color key

Commodore 64

VIC-II

1982

8

8

96, 192

12, 24

21

1, 3

2× integer

No

Yes

Color key

Amiga (OCS)

Denise

1985

8, can be reused horizontally per 4 pixel increments

Arbitrary, 8 unique

Arbitrary

16

Arbitrary

3, 15

Vertical by display list

No

Yes

Color key

Amiga (AGA)

Lisa

1992

8, can be reused horizontally per 2 pixel increments

Arbitrary, 8 unique

Arbitrary

16, 32, 64

Arbitrary

3, 15

Vertical by display list

No

Yes

Color key

ColecoVision

TMS9918A

1983

32

4

64

8, 16

8, 16

1

2× integer

No

Partial

Color key

TI-99/4 & 4A

TMS9918

1979

32

4

64

8, 16

8, 16

1

2× integer

No

Partial

Color key

Gameduino

2011

256

96

1,536

16

16

255

No

Yes

Yes

Color key

Intellivision

STIC AY-3-8900

1979

8

8

64

8

8,16

1

2, 4, 8× vertical, 2× horizontal

Horizontal and vertical mirroring

Yes

Color key

MSX

TMS9918A

1983

32

4

64

8, 16

8, 16

1

2× integer

No

Partial

Color key

MSX2

Yamaha V9938

1986

32

8

128

8, 16

8,16

1, 3, 7, 15 per line

2× integer

No

Partial

Color key

MSX2+

/

MSX turbo R

Yamaha V9958

1988

32

8

128

8,16

8,16

1, 3, 7, 15 per line

2× integer

No

Partial

Color key

Namco Pac-Man

(arcade)

TTL

1980

6

6

96

16

16

3

No

Horizontal and vertical mirroring

No

Color key

TurboGrafx-16

HuC6270A

1987

64

16

256

16, 32

16, 32, 64

15

No

Horizontal and vertical mirroring

Yes

Color key

Namco Galaxian

(arcade)

TTL

1979

7

7

112

16

16

3

No

Horizontal and vertical mirroring

No

Color key

Nintendo

Donkey Kong

,

Radar Scope

(arcade)

1979

128

16

256

16

16

3

Integer

No

Yes

Color key

Nintendo DS

Integrated PPU

2004

128

128

1,210

8, 16, 32, 64

8, 16, 32, 64

65,536

Affine

Affine

No

Color key, blending

NES/Famicom

Ricoh

RP2C0x PPU

1983

64

8

64

8

8, 16

3

No

Horizontal and vertical mirroring

Partial

Color key

Game Boy

Integrated PPU

1989

40

10

80

8

8, 16

3

No

Horizontal and vertical mirroring

No

Color key

Game Boy Advance

Integrated PPU

2001

128

128

1210

8, 16, 32, 64

8, 16, 32, 64

15, 255

Affine

Affine

No

Color key, blending

Master System

,

Game Gear

YM2602B VDP

(TMS9918-derived)

1985

64

8

128

8, 16

8, 16

15

2× integer, 2× vertical

Background tile mirroring

Yes

Color key

Genesis / Mega Drive

YM7101 VDP

(SMS VDP-derived)

1988

80

20

320

8, 16, 24, 32

8, 16, 24, 32

15

No

Horizontal and vertical mirroring

Yes

Color key

Sega OutRun

(arcade)

1986

128

128

1600

8 to 512

8 to 256

15

Anisotropic

Horizontal and vertical mirroring

Yes

Alpha

X68000

Cynthia jr. (original), Cynthia (later models)

1987

128

32

512

16

16

15

2× integer

Horizontal and vertical mirroring

Partial

Color key

Neo Geo

LSPC2-A2

1990

384

96

1536

16

16 to 512

15

Sprite shrinking

Horizontal and vertical mirroring

Partial

Color key

Super NES / Super Famicom

S-PPU1, S-PPU2

1990

128

34

256

8, 16, 32, 64

8, 16, 32, 64

15

No

Horizontal and vertical mirroring

No

Color key, averaging

System

Sprite hardware

Introduced

Sprites on screen

Sprites on line

Max.

texels

on line

Texture

width

Texture height

Colors

Hardware zoom

Rotation

Collision detection

Transparency

Source
