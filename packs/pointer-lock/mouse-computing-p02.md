---
title: "Computer mouse (part 2/2)"
source: https://en.wikipedia.org/wiki/Mouse_(computing)
domain: pointer-lock
license: CC-BY-SA-4.0
tags: pointer lock api, mouse capture relative motion, raw mouse movement, pointer lock change event
fetched: 2026-07-02
part: 2/2
---

## Buttons

Mouse buttons are microswitches which can be pressed to select or interact with an element of a graphical user interface, producing a distinctive clicking sound.

Since around the late 1990s, the three-button scrollmouse has become the de facto standard. Users most commonly employ the second button to invoke a contextual menu in the computer's software user interface, which contains options specifically tailored to the interface element over which the mouse cursor currently sits. By default, the primary mouse button sits located on the left-hand side of the mouse, for the benefit of right-handed users; left-handed users can usually reverse this configuration via software.


## Scrolling

Nearly all mice now have an integrated input primarily intended for scrolling on top, usually a single-axis digital wheel or rocker switch which can also be depressed to act as a third button. Though less common, many mice instead have two-axis inputs such as a tiltable wheel, trackball, or touchpad. Those with a trackball may be designed to stay stationary, using the trackball instead of moving the mouse.


## Speed

Mickeys per second is a unit of measurement for the speed and movement direction of a computer mouse, where direction is often expressed as "horizontal" versus "vertical" mickey count. However, speed can also refer to the ratio between how many pixels the cursor moves on the screen and how far the mouse moves on the mouse pad, which may be expressed as pixels per mickey, pixels per inch, or pixels per centimeter.

The computer industry often measures mouse sensitivity in terms of counts per inch (CPI), commonly expressed as dots per inch (DPI) – the number of steps the mouse will report when it moves one inch. In early mice, this specification was called pulses per inch (ppi). The mickey originally referred to one of these counts, or one resolvable step of motion. If the default mouse-tracking condition involves moving the cursor by one screen-pixel or dot on-screen per reported step, then the CPI does equate to DPI: dots of cursor motion per inch of mouse motion. The CPI or DPI as reported by manufacturers depends on how they make the mouse; the higher the CPI, the faster the cursor moves with mouse movement. However, operating system and application software can adjust the mouse sensitivity, making the cursor move faster or slower than its CPI. As of 2007, software can change the speed of the cursor dynamically, taking into account the mouse's absolute speed and the movement from the last stop-point.

For simple software, when the mouse starts to move, the software will count the number of "counts" or "mickeys" received from the mouse and will move the cursor across the screen by that number of pixels (or multiplied by a rate factor, typically less than 1). The cursor will move slowly on the screen, with good precision. When the movement of the mouse passes the value set for some threshold, the software will start to move the cursor faster, with a greater rate factor. Usually, the user can set the value of the second rate factor by changing the "acceleration" setting.

Operating systems sometimes apply acceleration, referred to as "ballistics", to the motion reported by the mouse. For example, versions of Windows prior to Windows XP doubled reported values above a configurable threshold, and then optionally doubled them again above a second configurable threshold. These doublings applied separately in the X and Y directions, resulting in very nonlinear response.


## Mousepads

Engelbart's original mouse did not require a mousepad; the mouse had two large wheels which could roll on virtually any surface. However, most subsequent mechanical mice starting with the steel roller ball mouse have required a mousepad for optimal performance.

The mousepad, the most common mouse accessory, appears most commonly in conjunction with mechanical mice, because to roll smoothly the ball requires more friction than common desk surfaces usually provide. So-called "hard mousepads" for gamers or optical/laser mice also exist.

Most optical and laser mice do not require a pad, the notable exception being early optical mice which relied on a grid on the pad to detect movement (e.g. Mouse Systems). Whether to use a hard or soft mousepad with an optical mouse is largely a matter of personal preference. One exception occurs when the desk surface creates problems for the optical or laser tracking, for example, a transparent or reflective surface, such as glass.

Some mice also come with small "pads" attached to the bottom surface, also called mouse feet or mouse skates, that help the user slide the mouse smoothly across surfaces.


## In the marketplace

Around 1981, Xerox included mice with its Xerox Star, based on the mouse used in the 1970s on the Alto computer at Xerox PARC. Sun Microsystems, Symbolics, Lisp Machines Inc., and Tektronix also shipped workstations with mice, starting in about 1981. Later, inspired by the Star, Apple Computer released the Apple Lisa, which also used a mouse. However, none of these products achieved large-scale success. Only with the release of the Apple Macintosh in 1984 did the mouse see widespread use.

The Macintosh design, commercially successful and technically influential, led many other vendors to begin producing mice or including them with their other computer products (by 1986, Atari ST, Amiga, Windows 1.0, GEOS for the Commodore 64, and the Apple IIGS).

The widespread adoption of graphical user interfaces in the software of the 1980s and 1990s made mice all but indispensable for controlling computers. In November 2008, Logitech built their billionth mouse.


## Use in games

The device often functions as an interface for PC-based computer games and sometimes for video game consoles. The Classic Mac OS Desk Accessory *Puzzle* in 1984 was the first game designed specifically for a mouse.

### First-person shooters

FPSs naturally lend themselves to separate and simultaneous control of the player's movement and aim, and on computers this has traditionally been achieved with a combination of keyboard and mouse. Players use the X-axis of the mouse for looking (or turning) left and right, and the Y-axis for looking up and down; the keyboard is used for movement and supplemental inputs.

Many shooting genre players prefer a mouse over a gamepad analog stick because the wide range of motion offered by a mouse allows for faster and more varied control. Although an analog stick allows the player more granular control, it is poor for certain movements, as the player's input is relayed based on a vector of both the stick's direction and magnitude. Thus, a small but fast movement (known as "flick-shotting") using a gamepad requires the player to quickly move the stick from its rest position to the edge and back again in quick succession, a difficult maneuver. In addition the stick also has a finite magnitude; if the player is currently using the stick to move at a non-zero velocity their ability to increase the rate of movement of the camera is further limited based on the position their displaced stick was already at before executing the maneuver. The effect of this is that a mouse is well suited not only to small, precise movements but also to large, quick movements and immediate, responsive movements; all of which are important in shooter gaming. This advantage also extends in varying degrees to similar game styles such as third-person shooters.

Some incorrectly ported games or game engines have acceleration and interpolation curves which unintentionally produce excessive, irregular, or even negative acceleration when used with a mouse instead of their native platform's non-mouse default input device. Depending on how deeply hardcoded this misbehavior is, internal user patches or external 3rd-party software may be able to fix it. Individual game engines will also have their own sensitivities. This often restricts one from taking a game's existing sensitivity, transferring it to another, and acquiring the same 360 rotational measurements. A sensitivity converter is the preferred tool that FPS gamers use to translate correctly the rotational movements between different mice and between different games. Calculating the conversion values manually is also possible but it is more time-consuming and requires performing complex mathematical calculations, while using a sensitivity converter is a lot faster and easier for gamers.

Due to their similarity to the WIMP desktop metaphor interface for which mice were originally designed, and to their own tabletop game origins, computer strategy games are most commonly played with mice. In particular, real-time strategy and MOBA games usually require the use of a mouse.

The left button usually controls primary fire. If the game supports multiple fire modes, the right button often provides secondary fire from the selected weapon. Games with only a single fire mode will generally map secondary fire to *aim down the weapon sights*. In some games, the right button may also invoke accessories for a particular weapon, such as allowing access to the scope of a sniper rifle or allowing the mounting of a bayonet or silencer.

Players can use a scroll wheel for changing weapons (or for controlling scope-zoom magnification, in older games). On most first person shooter games, programming may also assign more functions to additional buttons on mice with more than three controls. A keyboard usually controls movement (for example, WASD for moving forward, left, backward, and right, respectively) and other functions such as changing posture. Since the mouse serves for aiming, a mouse that tracks movement accurately and with less lag (latency) will give a player an advantage over players with less accurate or slower mice. In some cases the right mouse button may be used to move the player forward, either in lieu of, or in conjunction with the typical WASD configuration.

Many games provide players with the option of mapping their own choice of a key or button to a certain control. An early technique of players, circle strafing, saw a player continuously strafing while aiming and shooting at an opponent by walking in circle around the opponent with the opponent at the center of the circle. Players could achieve this by holding down a key for strafing while continuously aiming the mouse toward the opponent.

Games using mice for input are so popular that many manufacturers make mice specifically for gaming. Such mice may feature adjustable weights, high-resolution optical or laser components, additional buttons, ergonomic shape, and other features such as adjustable CPI. Mouse Bungees are typically used with gaming mice because it eliminates the annoyance of the cable.

Many games, such as first- or third-person shooters, have a setting named "invert mouse" or similar (not to be confused with "button inversion", sometimes performed by left-handed users) which allows the user to look downward by moving the mouse forward and upward by moving the mouse backward (the opposite of non-inverted movement). This control system resembles that of aircraft control sticks, where pulling back causes pitch up and pushing forward causes pitch down; computer joysticks also typically emulate this control-configuration.

After id Software's commercial hit of *Doom*, which did not support vertical aiming, competitor Bungie's *Marathon* became the first first-person shooter to support using the mouse to aim up and down. Games using the Build engine had an option to invert the Y-axis. The "invert" feature actually made the mouse behave in a manner that users now regard as non-inverted (by default, moving mouse forward resulted in looking down). Soon after, id Software released *Quake*, which introduced the invert feature as users now know it.

### Home consoles

In 1988, the VTech Socrates educational video game console featured a wireless mouse with an attached mouse pad as an optional controller used for some games. In the early 1990s, the Super Nintendo Entertainment System video game system featured a mouse in addition to its controllers. A mouse was also released for the Nintendo 64, although it was only released in Japan. The 1992 game *Mario Paint* in particular used the mouse's capabilities, as did its Japanese-only successor *Mario Artist* on the N64 for its 64DD disk drive peripheral in 1999. Sega released official mice for their Genesis/Mega Drive, Saturn and Dreamcast consoles. NEC sold official mice for its PC Engine and PC-FX consoles. Sony released an official mouse product for the PlayStation console, included one along with the Linux for PlayStation 2 kit, as well as allowing owners to use virtually any USB mouse with the PS2, PS3, and PS4. Nintendo's Wii also had this feature implemented in a later software update, and this support was retained on its successor, the Wii U. Microsoft's Xbox line of game consoles (which used operaring systems based on modified versions of Windows NT) also had universal-wide mouse support using USB.

On June 5, 2025, Nintendo released the Joy-Con 2 controller, a gaming controller with mouse control for the Nintendo Switch 2.
