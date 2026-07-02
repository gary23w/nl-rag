---
title: "Lighting control console"
source: https://en.wikipedia.org/wiki/Lighting_control_console
domain: dmx512-lighting
license: CC-BY-SA-4.0
tags: dmx512 protocol, dmx lighting control, stage lighting control, entertainment lighting bus
fetched: 2026-07-02
---

# Lighting control console

A **lighting control console** (also called a **lightboard**, **lighting board**, or **lighting desk**) is an electronic device used in theatrical lighting design to control multiple stage lights at once. They are used throughout the entertainment industry and are normally placed at the front of house (FOH) position or in a control booth.

All lighting control consoles can control dimmers which control the intensity of conventional incandescent lights. Many modern consoles can control Intelligent lighting (lights that can move, change colors and gobo patterns), fog machines and hazers, and other special effects devices. Some consoles can also interface with other electronic performance hardware (i.e. mixing consoles, projectors, media servers, automated winches and motors, etc.) to improve synchronization or unify their control.

Lighting consoles communicate with the dimmers and other devices in the lighting system via an electronic control protocol. The most common protocol used in the entertainment industry today is DMX512, although other protocols (e.g. 0-10 V analog lighting control) may still be found in use, and newer protocols such as ACN and DMX-512-A are evolving to meet the demands of ever increasing device sophistication. Some lighting consoles can communicate over a Local IP network infrastructure to provide control over more scalable systems. A common protocol for this is ESTA E1.31 sACN (pronounced: streaming A.C.N.) or Art-Net.

## Types of control consoles

Consoles vary in size and complexity, from small preset boards to dedicated moving light consoles. The purpose of all lighting consoles, however is the same: to consolidate control of the lights into an organized, easy-to-use system, so that the lighting designer can concentrate on producing a good show. Most consoles accept MIDI Show Control signals and commands to allow show control systems to integrate their capabilities into more complex shows.

### Preset boards

Preset boards are the most basic lighting consoles—and also the most prevalent in smaller installations. They consist of two or more identical fader banks, called **scenes**. The faders (control slides) on these scenes can be manually adjusted. Each scene has the same number of channels which control the same dimmers. So the console operator can build a scene offline or in "blind", a cross-fader or submaster is used to selectively mix or **fade** between the different scenes.

Generally, at least with a preset board, the operator has a cue sheet for each scene, which is a diagram of the board with the faders in their positions, as determined by the lighting designer. The operator sets the faders into their positions based on the cue sheets. Typically during a cue, the operator sets the next scene. Then the operator makes the transition between the scenes using the cross-fader.

Preset boards are not as prevalent since the advent of digital memory consoles, which can store scenes digitally, and are generally much less cumbersome but more expensive than preset boards. However, for small setups such as that of a DJ, they remain the board of choice for their simple to use interface and relative flexibility. Preset boards generally control only conventional lights; though some advanced hybrid consoles can be patched to operate intelligent lights in a round-about way by setting the control channels of the light to channels the preset board can control. However, this is not recommended since it is a cumbersome process.

### Memory consoles

Memory-based consoles have become very popular in almost all larger installations, particularly theatres. This type of controller has almost completely replaced preset consoles as controllers of choice. Memory consoles are preferable in productions where scenes do not change from show to show, such as a theatre production, because scenes are designed and digitally recorded, so there is less room for human error, and less time between lighting cues is required to produce the same result. They also allow for lighting cues to contain larger channel counts due to the same time savings gained from not physically moving individual channel faders.

Many memory consoles have a bank of faders. These faders can be programmed to control a single channel (a channel is a lighting designer's numerical name for a dimmer or group of dimmers) or a group of channels (known as a ""submaster""). The console may also have provision to operate in analog to a manual desk for programming scenes or live control. On more advanced consoles, faders can be used to control effects, chases (sequences of cues), and moving light effects (if the console can control moving lights).

### Moving light controllers

Moving Light Controllers are another step up in sophistication from Memory Consoles. As well as being capable of controlling ordinary luminaires via dimmers, they provide additional controls for intelligent fixtures. On midrange controllers, these are usually provided as a section separate from main Preset and Cue stack controls. These include an array of buttons allowing the operator to select the fixture or fixtures they want to control, and a joystick, or a number of wheels or rotary encoders to control fixture attributes such as the orientation (pan and tilt), focus, colour, gobos etc. found in this type of light. Unlike a fader that shows its value based on the position of a slider, a wheel is continuously variable and provides no visual feedback for the value of a particular control. Some form of display such as LCD or LED is therefore vital for displaying this information. The more advanced desks typically have one or more touchscreens, and present a GUI that integrates all the aspects of lighting control.

As there is no standard way of controlling an intelligent light, an important function for this type of desk is to consolidate the various ways in which the hundreds of types of intelligent lights are controlled into a single *abstract* interface for the user. By integrating knowledge of different fixtures and their attributes into the lighting desk software (often via user-editable DMX profiles corresponding to each operation mode of each lighting fixture), the detail of how an attribute such as pan or tilt is controlled for one device vs. another can be hidden from the operator. This frees the operator to think in terms of what they want to achieve (e.g. pan 30 degrees clockwise) instead of how it is achieved for any given fixture (e.g. send value 137 down channel 23). Furthermore, should a lighting fixture need to be replaced with one from a different vendor that has a different DMX profile, the operator need only change the lighting fixture within the software, and it will adapt the programming from the old fixture to the new one, allowing for the extreme flexibility required by touring shows or venues with multiples operators/consoles. For some further discussion on how intelligent fixtures are controlled, see Digital MultipleX (DMX).

### Personal computer-based controllers

Personal Computer (PC) based controllers are increasing in popularity owing to portability and reduced cost. These lighting console solutions use software with a feature set similar to that found in a hardware-based console. As dimmers, automated fixtures and other standard lighting devices do not generally have current standard computer interfaces, options such as DMX-512 ports and fader/submaster panels connected via USB are commonplace.

This system allows a "build-to-fit" approach: the end user initially provides a PC that fits their budget and any other needs with future options to improve the system, for example, by increasing the number of DMX outputs or additional console style panels.

Many lightboard vendors offer a PC software version of their consoles. Commercial lighting control software often require a specific, and possibly expensive, hardware DMX interface. However, inexpensive (<$150) DMX -> USB PC interfaces such as the ENTTEC and DMXKing DMX USB Pro with public API and other DIY, and free or Open source software hardware combinations are available.

Many console vendors also make a software simulator or "offline editor" for their hardware consoles, and these are often downloadable for free. The simulator can be used to pre-program a show, and the cues then loaded into the actual console. In addition, lighting visualization software is available to simulate and approximate how lighting will appear on stage, and this can be useful for programming effects and spotting obvious programming errors such as incorrect colour changes.

### Remote focus unit

Many memory consoles have an optional Remote Focus Unit (RFU) controller that can be attached to the light board and used to control the board's functions (though usually in some limited capacity). They are usually small enough to be handheld. This is ideal in situations where moving the light board is impractical, but control is needed away from where the board is located. That is, if the light board is in a control room that is located far from the fixtures, such as a catwalk, an RFU can be attached and an electrician or the lighting designer can bring it to a location which is close to the lights. Some of the newer and more advanced boards have RFUs that can be connected through USB or even wirelessly.

Various manufacturers offer software for devices such as Android and iPhones that cause the devices to act as remote controllers for their consoles. Also, independent software developers have released applications that can send Art-Net packets from an iPhone, thus enabling an iPhone to serve as a fully featured console when used in conjunction with an Art-Net to DMX converter or Art-Net compatible luminaries and dimmers. An example of this is ETC's (Electronic Theater Controls) app called iRFR for Apple devices or aRFR for Android devices.

The *Controller Interface Transport Protocol*, or *CITP*, is a network protocol used between visualizers, lighting control consoles and media servers to transport non-show critical information during pre-production. The protocol is used for a number of purposes including SDMX, browsing media and thumbnails, and streaming media among different devices.
