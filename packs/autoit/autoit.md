---
title: "AutoIt"
source: https://en.wikipedia.org/wiki/AutoIt
domain: autoit
license: CC-BY-SA-4.0
tags: autoit language, gui testing, windows automation, scripting language, task automation
fetched: 2026-07-02
---

# AutoIt

**AutoIt** /ɔːtoʊ ɪt/ is a freeware programming language for Microsoft Windows. In its earliest release, it was primarily intended to create automation scripts (sometimes called macros) for Microsoft Windows programs but has since grown to include enhancements in both programming language design and overall functionality.

The scripting language in AutoIt 1 and 2 was statement-driven and designed primarily for simulating user interaction. From version 3 onward, the AutoIt syntax is similar to that found in the BASIC family of languages. In this form, AutoIt is a general-purpose, third-generation programming language with a classical data model and a variant data type that can store several types of data, including arrays.

An AutoIt automation script can be converted into a compressed, stand-alone executable which can be run on computers even if they do not have the AutoIt interpreter installed. A wide range of function libraries (known as UDFs, or "User Defined Functions") are also included as standard or are available from the website to add specialized functionality. AutoIt is also distributed with an IDE based on the free SciTE editor. The compiler and help text are fully integrated and provide a *de facto* standard environment for developers using AutoIt.

## History

| 1999 | January: First AutoIt Version (1.0) |
|---|---|
| August: AutoIt v2 |   |
| September: First AutoIt version with Compiler |   |
| 2000 |   |
| 2001 |   |
| 2002 | December: AutoIt v3 (Public Beta) |
| 2003 |   |
| 2004 | February: AutoIt v3 (Stable) |
| 2005 | February: AutoIt v3.1.0.15 released, first release with support for GUI scripts |
| 2006 | September: Auto3Lib started |
| 2007 | November: AutoIt v3.2.10.0 released, Auto3Lib incorporated into AutoIt v3 |
| 2008 | May: AutoIt v3.2.12.0 released, incorporating further GUI functionality |
| June: AutoIt v3.2.12.1 released, last version to support Windows 95 and Windows NT 4.0 |   |
| December: AutoIt v3.3.0.0 released |   |
| 2009 | December: AutoIt v3.3.2.0 released |
| 2010 | January: AutoIt v3.3.4.0 released |
| March: AutoIt v3.3.6.0 released |   |
| April: AutoIt v3.3.6.1 released |   |
| 2011 | December: AutoIt v3.3.8.0 released |
| 2012 | January: AutoIt v3.3.8.1 released, last version to support Windows 2000 |
| 2013 | December: AutoIt v3.3.10.0 released |
| 2014 | June: AutoIt v3.3.12.0 released |
| 2015 | July: AutoIt v3.3.14.0 and v3.3.14.1 released |
| September: AutoIt v3.3.14.2 released |   |
| 2016 |   |
| 2017 |   |
| 2018 | February: AutoIt v3.3.14.3 released |
| March: AutoIt v3.3.14.5 released |   |
| 2019 |   |
| 2020 |   |
| 2021 |   |
| 2022 | March: AutoIt v3.3.16.0 released |
| September: AutoIt v3.3.16.1 released, last version to support Windows XP and Windows Server 2003 |   |
| 2023 |   |
| 2024 |   |
| 2025 | September: AutoIt v3.3.18.0 released |

### License

AutoIt1 and AutoIt2 were closed-source projects, and had a very different syntax than AutoIt3, whose syntax is more like VBScript and BASIC.

AutoIt3 was initially free and open-source, licensed under the terms of the GNU General Public License, with its initial public release 3.0.100 in February 2004, and had open-source releases in March 2004 and August 2004. Version 3.0.102, released in August 2004, was initially open-source, but by January 2005 was distributed as closed-source. Subsequent releases, starting from the February 2005 release of version 3.1.0, were all closed-source.

The free and open-source AutoHotkey project derived 29 of its functions from the AutoIt 3.1 source code. The AutoHotkey syntax is quite different from AutoIt3 syntax, and rather resembles AutoIt2 syntax.

## Features

AutoIt is typically used to produce utility software for Microsoft Windows and to automate routine tasks, such as systems management, monitoring, maintenance, or software installation. It is also used to simulate user interaction, whereby an application is "driven" (via automated form entry, keypresses, mouse clicks, and so on) to do things by an AutoIt script.

AutoIt can also be used in low-cost laboratory automation. Applications include instrument synchronization, alarm monitoring and results gathering. Devices such as CNC routers and 3D-printers can also be controlled.

- 64-bit code support from version 3.2.10.0
- Add-on libraries and modules for specific apps
- Automate sending user input and keystrokes to apps, as well as to individual controls within an app
- Call functions in DLL files
- Compatible with User Account Control
- Compiling into standalone executables
- Create graphical user interfaces, including message and input boxes
- Include data files in the compiled file to be extracted when running
- Manipulate windows and processes
- Object-oriented design through a library
- Play sounds, pause, resume, stop, seek, get the current position of the sound and get the length of the sound
- Run console apps and access the standard streams
- Scripting language with BASIC-like structure for Windows
- Simulate mouse movements
- Supports the component object model (COM)
- Supports regular expressions
- Supports TCP and UDP protocols
- Unicode support from version 3.2.4.0

## Examples

### Automating the Windows Calculator

```mw
; Make available a library of constant values.
#include <MsgBoxConstants.au3>

; Display a message box with a timeout of 6 seconds.
MsgBox($MB_OK, "Attention", "Avoid touching the keyboard or mouse during automation.", 6)

; Run the Windows Calculator.
Run("calc.exe")

; Wait for the calculator to become active with a timeout of 10 seconds.
WinWaitActive("[CLASS:CalcFrame]", "", 10)

; If the calculator did not appear after 10 seconds then exit the script.
If WinExists("[CLASS:CalcFrame]") = 0 Then Exit

; Automatically type the current year into the calculator.
Send(@YEAR)

; Let's slow the script down a bit so we can see what's going on.
Sleep(600)

; Automatically type in 'divide by 4', and then sleep 600 ms.
Send("/4")
Sleep(600)

; Hit the return key to display the result, and sleep 600 ms.
Send("{ENTER}")
Sleep(600)

; Copy the result to the clipboard using the Windows shortcut Ctrl+C.
Send("^c")

; Declare, and assign the contents of the clipboard to, a variable.
Local $fResult = ClipGet()

; Check to see if the variable contains a decimal point or not.
If StringInStr($fResult, ".") Then
    ; Display a message box with a timeout of 5 seconds.
    MsgBox($MB_OK, "Leap Year", @YEAR & " is not a leap year.", 5)
Else
    ; This message will only display if the current year is a leap year.
    MsgBox($MB_OK, "Leap Year", @YEAR & " is a leap year.", 5)
EndIf

; Close the Windows calculator - always tidy up afterwards.
WinClose("[CLASS:CalcFrame]")
```

### Find average

```mw
; Find Average by JohnOne, modified by czardas
#include <MsgBoxConstants.au3>

_Example() ; Run the example.

Func _Example()
    ; Display an input box and ask the user to enter some numbers separated by commas.
    Local $sInput = InputBox("Find Average", "Enter some numbers separated by commas: 1,2,42,100,3")

	; If an error occurred then exit the script.
	If @error Then Exit

    ; Populate an array with the user's input.
    Local $aSplit = StringSplit($sInput, ",")

    ; Pass the array to the function _Find_Average() and then check for errors.
    Local $fAverage = _Find_Average($aSplit)
    If @error Then Exit

    ; Display the result in a message box.
    MsgBox($MB_OK, "Find Average", "Result: " & $fAverage)
EndFunc   ;==>_Example

Func _Find_Average($aArray)
    ; If the input is not of the correct type (an array), then return an error along with the details.
    If Not IsArray($aArray) Then Return SetError(1, 0, VarGetType($aArray))
	; More detailed checks are possible, but for brevity just one is performed here.

    ; Declare a variable to store the sum of the numbers.
    Local $iArraySum = 0

    ; Loop through the array.
    For $i = 1 To $aArray[0]
        ; Increment the sum by the number in each array element.
        $iArraySum += Number($aArray[$i])
    Next

    ; Return the average rounded to 2 decimal places.
    Return Round($iArraySum / $aArray[0], 2)
EndFunc   ;==>_Find_Average
```
