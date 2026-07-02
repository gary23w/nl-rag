---
title: "DirectInput"
source: https://en.wikipedia.org/wiki/DirectInput
domain: game-input-handling
license: CC-BY-SA-4.0
tags: game input handling, game controller input, gamepad mapping, input device event
fetched: 2026-07-02
---

# DirectInput

**DirectInput** is a legacy application programming interface developed by American company Microsoft that collects user input via devices such as the mouse, keyboard, and gamepads. It also provides a system for *action mapping*, which allows the user to assign specific actions within a game to the buttons and axes of the input devices. Additionally it handles *haptic feedback/force feedback* (input/output) devices. Microsoft also introduced a input library called *XInput* specifically for the Xbox 360 controller.

DirectInput supports up to 128 buttons, 8 axes, and 4 point of view hats.

DirectInput and XInput provide benefits over normal Win32 input events:

- they enable an application to retrieve data from input devices even when the application is in the background
- they provide full support for any type of input device, as well as for *haptic feedback*
- through *action mapping*, applications can retrieve input data without needing to know what kind of device generated that input

While DirectInput forms a part of the DirectX library, it has not been significantly revised since DirectX 8 (2001–2002). Microsoft recommends that new applications make use of the Windows message loop for keyboard and mouse input instead of DirectInput (as indicated in the Meltdown 2005 slideshow), and to use GameInput instead of legacy APIs such as DirectInput or XInput.

## History

DirectX included DirectInput from version 1.0 (1995). It initially offered true support only for joysticks, as the mouse and keyboard modules simply provided wrappers to the standard Win32 API. DirectX version 3.0 (1996) added support for keyboards and mice; it also improved joystick support. DirectX 5.0 (1997) included greatly improved joystick support, including adding haptic feedback, increasing the number of buttons, changing the underlying device-driver model and incorporating a COM-based API. Mouse support also increased the number of buttons seen from four to eight. In DirectX 7.0 (1999- ), DirectInput added a long-promised feature of seeing individual mice much like individual joysticks, but the feature didn't work with the later released Windows XP, even though as of 2010 it works with Windows 98/Me and DirectX 9. DirectX 8.0 (2000), the last version with major changes, included action mapping and broader support for different types of devices.

While Microsoft initially intended that DirectInput would handle all inputs, this didn't work out. As of 2011 Microsoft no longer recommends using DirectInput for keyboards or mice, and has started pushing the newer XInput for Xbox 360 controllers. In Windows Vista, Windows 7 and later Windows versions, the in-built action mapping UI has been removed. DirectInput is not available for Windows Store apps.

## XInput

XInput, a more recent but now legacy API for "next generation" controllers, was introduced in December 2005 alongside the launch of the Xbox 360. This specification provided support for Xbox 360 controllers in Windows XP SP1 and subsequent operating systems, and is described by Microsoft as being easier to program for and requiring less setup than DirectInput. XInput is compatible with DirectX version 9 and later.

## Xbox 360 Controller support

An *Xbox 360 Controller*, with the default Microsoft driver, has the following limitations with DirectInput, compared to XInput:

- The buttons are not accurate. This may cause issues with games that don't support controller remapping.
- The left and right triggers will act as a single axis representing the signed difference between the triggers, not as independent analog axis or button.
- Vibration effects will not operate.
- Querying for headset devices will not operate, XInput 1.4 as part of Windows 8 introduced Xbox headset support.

According to MSDN, "the combination of the left and right triggers in DirectInput is by design. Games have always assumed that DirectInput device axes are centered when there is no user interaction with the device. However, the Xbox 360 controller was designed to register minimum value, not center, when the triggers are not being held." MSDN proffered the "solution" of combining the triggers, setting one trigger to a positive direction and the other to a negative direction, so no user interaction is indicative to DirectInput of the "control" being at center.

The above, however, ignores the fact that many DirectInput controllers, such as gamepads with dual analog sticks and racing-wheel controller sets, already map triggers and pedals independently. In addition, many DirectInput devices also have vibration effects. At least one 3rd-party driver, XBCD, gives the Xbox 360 controllers the vibration support, dead zones and (optionally) independent analog/digital triggers through DirectInput its XInput driver possesses. This suggests that Microsoft's Xbox 360 controller driver was given *intentionally* weaker DirectInput support, rather than due to any differences between DirectInput and XInput APIs. On the other hand, Xbox 360 controllers using XInput support only very basic control of vibration motors in contrast with greater palette of effects supported via DirectInput.
