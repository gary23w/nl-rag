---
title: "ActionScript"
source: https://en.wikipedia.org/wiki/ActionScript
domain: haxe-language
license: CC-BY-SA-4.0
tags: haxe language, cross platform software, actionscript language, source to source compiler, neko virtual machine
fetched: 2026-07-02
---

# ActionScript

**ActionScript** is an object-oriented programming language originally developed by Macromedia Inc. (later acquired by Adobe). It is influenced by HyperTalk, the scripting language for HyperCard. It is now an implementation of ECMAScript (meaning it is a superset of the syntax and semantics of the language more widely known as JavaScript), though it originally arose as a sibling, both being influenced by HyperTalk. ActionScript code is usually converted to bytecode format by a compiler.

ActionScript is used primarily for the development of websites and software targeting the Adobe Flash platform, originally finding use on web pages in the form of embedded SWF files.

ActionScript 3 is also used with the Adobe AIR system for the development of desktop and mobile applications. The language itself is open-source in that its specification is offered free of charge and both an open-source compiler (as part of Apache Flex) and open-source virtual machine (Tamarin) are available.

ActionScript was also used with Scaleform GFx for the development of three-dimensional video-game user interfaces and heads up displays.

## Overview

ActionScript was initially designed for controlling simple two-dimensional vector animations made in Adobe Flash (formerly Macromedia Flash). Initially focused on animation, early versions of Flash content offered few interactivity features, thus had very limited scripting ability. Later versions added functionality allowing for the creation of web-based games and rich web applications with streaming media (such as video and audio). Today, ActionScript is suitable for desktop and mobile development through Adobe AIR; it is used in some database applications and in basic robotics as in Make Controller Kit.

Flash MX 2004 introduced ActionScript 2.0, a scripting language more suited to the development of Flash applications. Saving time is often possible by scripting something rather than animating it, which usually also enables a higher level of flexibility when editing.

Since the arrival of the Flash Player 9 alpha (in 2006), a newer version of ActionScript has been released, ActionScript 3.0. This version of the language is intended to be compiled and run on a version of the Tamarin virtual machine, formerly ActionScript Virtual Machine 2, that was also fully rewritten (dubbed AVM2). Because of this, code written in ActionScript 3.0 is generally targeted for Flash Player 9 and higher, and will not work in prior versions. At the same time, ActionScript 3.0 executes up to 10 times faster than legacy ActionScript code due to the just-in-time compiler enhancements.

Flash libraries can be used with the XML abilities of the browser to render rich content in the browser. This technology is known as Asynchronous Flash and XML, much like AJAX. Adobe offers its Flex product line to meet the demand for rich web applications built on the Flash runtime, with behaviors and programming done in ActionScript. ActionScript 3.0 forms the foundation of the Flex 2 application programming interface (API).

## History

ActionScript started as an object-oriented programming language for Macromedia's Flash authoring tool, later developed by Adobe Systems as Adobe Flash. The first three versions of the Flash authoring tool provided limited interactivity features. Early Flash developers could attach a simple command, called an "action", to a button or a frame. The set of actions was basic navigation controls, with commands such as "play", "stop", "getURL", and "gotoAndPlay".

With the release of Flash 4 in 1999, this simple set of actions became a small scripting language. New capabilities introduced for Flash 4 included variables, expressions, operators, if statements, and loops. Although referred to internally as "ActionScript", the Flash 4 user manual and marketing documents continued to use the term "actions" to describe this set of commands.

### Timeline by player version

- **Flash Player 2**: The first version with scripting support, its actions included gotoAndPlay, gotoAndStop, nextFrame and nextScene for timeline control.
- **Flash Player 3**: Expanded basic scripting support, it has the ability to load external SWFs (loadMovie).
- **Flash Player 4**: The first player with a full scripting implementation (called *Actions*), the scripting was a Flash-based syntax and contained support for loops, conditionals, variables, and other basic language constructs.
- **Flash Player 5**: Included in the first version of ActionScript, it used prototype-based programming based on ECMAScript, and allowed full procedural programming and object-oriented programming. Design based development.
- **Flash Player 6** added an event-handling model, accessibility controls, and support for switch. The first version with support for the Action Message Format (AMF) and Real-Time Messaging Protocol (RTMP) allowed for on demand audio/video streaming.
- **Flash Player 7**: Additions to it include Cascading Style Sheets (CSS) styling for text and support for ActionScript 2.0, a programming language based on the ECMAScript 4 Netscape Proposal with class-based inheritance. However, ActionScript 2.0 can cross compile to ActionScript 1.0 bytecode, so that it can run in Flash Player 6.
- **Flash Player 8** further extended ActionScript 1/ActionScript 2 by adding new class libraries with APIs for controlling bitmap data at run-time, file uploads, and live filters for blur and drop shadow.
- **Flash Player 9 (initially called 8.5)** added ActionScript 3.0 with the advent of a new virtual machine, called ActionScript Virtual Machine 2 (AVM2), which coexists with the previous AVM1 needed to support legacy content. Performance increases were a major objective for this release of the player, including a new just-in-time (JIT) compiler. Support for binary sockets, ECMAScript for XML (E4X) XML parsing, full-screen mode, and regular expressions were added. This is the first release of the player to be titled Adobe Flash Player.
- **Flash Player 10 (initially called Astro)**: Added basic 3D manipulation, such as rotating on the X, Y, and Z axis, a 3D drawing API, and texture mapping. Ability to create custom filters using Adobe Pixel Bender. Several visual processing tasks are now offloaded to the GPU which gives a noticeable decrease to rendering time for each frame, resulting in higher frame rates, especially with H.264 video. There is a new sound API which allows for custom creation of audio in flash, something that has never been possible before. Furthermore, Flash Player 10 supports Peer to Peer (P2P) communication with Real Time Media Flow Protocol (RTMFP).
- **Flash Player 11**: The major addition in this version are the Stage3D-based advanced (graphic card accelerated) 3D capabilities for Windows Desktop, Mac Desktop, iOS, Android, and other major platforms. Significant compatibility improvements have been added for the iOS platform, and other non-desktop platforms. Other features include H.264 encoding for cameras, Native JSON support, Cubic Bézier Curves, a secure random number generator, LZMA compression for SWF files, workers to offload some code execution to other processor threads, graphics card accelerated camera feed rendering, memory intrinsics and performance analysis, and the ActionScript Compiler 2.0, as well as some other minor additions.
- **Flash Player 11.2**: released in March 2012, focused on adding features that are key for the gaming and video markets. Some of the features in the release include the following: Mouse-lock support. Right and middle mouse-click support. Context menu disabling. Hardware-accelerated graphics/Stage 3D support for Apple iOS and Android via Adobe AIR. Support for more hardware accelerated video cards (from January 2008) in order to expand availability of hardware-accelerated content. New Throttle event API (dispatches event when Flash Player throttles, pauses, or resumes content). Multithreaded video decoding pipeline on PCs, which improves overall performance of video on all desktop platforms. Notification of use of premium features in the debug players; content runs unrestricted in the release players.
- **Flash Player 11.3**: released in June 2012, focused on enabling features and functionality key for the gaming market, as well as addressing popular feature requests from developers. Some of the features in this release include the following: Keyboard input support in full-screen mode. Improved audio support for working with low-latency audio. Ability to progressively stream textures for Stage 3D content. Protected mode for Flash Player in Firefox. Frame label events. Support for compressing BitmapData to JPEG and PNG formats. Support for Mac OS X App Store application sandboxing requirements. Text streaming support for Stage 3D. Expanded information about GPU driver details. Bitmap draw with quality API (new). Release outside mouse event API. Flash Player silent update support for Mac OS. Stylus support for Android 4.0 devices (Adobe AIR). USB debugging for iOS (Adobe AIR). iOS simulator support (Adobe AIR).
- **Flash Player 11.4**: Released in August 2012, it focused on enabling features and functionality that are key for the gaming market, as well as addressing popular feature requests from developers. Some of the features in this release include ActionScript workers (enables concurrent ActionScript execution on separate threads), support for advanced profiling, LZMA compression support for ByteArray, support for hardware-accelerated video cards for Stage 3D expanded to 2006, improved ActionScript performance when targeting Apple iOS, performance index API to inform about performance capabilities of current environment, support for compressed textures with alpha support, support for StageVideo.attachCamera API, and support for push notifications for iOS (Adobe AIR).
- **Flash Player 11.5**: Released in November 2012, it focused on performance improvement and stability. Some of the features in this release include shared ByteArray support for ActionScript workers, debug stack trace in release builds of Flash Player, and various bug fixes.
- **Flash Player 11.6**: Released in March 2013, it focuses on performance improvements, security enhancements, and stability. Some of the features in this release include ability to query graphics vector data at runtime, full-screen permission dialog user interface improvements, ability to load SWFs at runtime when deploying as an AIR application in AOT mode on iOS, finer-grained control over supported display resolution on iOS devices when deploying as an AIR application, HiDPI support for Flash Professional, and ActionScript 3 access to fast memory operations/intrinsics.
- **Flash Player 11.7**: Released in June 2013, code-named "Geary", this release focuses on premium video, gaming, security, and stability. Some of the features planned for this release include Android captive runtime debugging, support for the OUYA controller, remote hosting of SWF files on iOS, and preventing backup of shared objects on iOS for better iCloud support.
- **Flash Player 11.8**: Adobe was planning to release this version in the early part of the second half of 2013, code-named "Harrison". This release focused on premium video, gaming, security, and stability. Some of the features in this release would have included recursive stop API on MovieClips and GamePad support on desktop browsers and Android.

### Timeline by ActionScript version

#### 2000–2004: ActionScript "1.0"

With the release of Flash 5 in September 2000, the "actions" from Flash 4 were enhanced once more and named "ActionScript" for the first time. This was the first version of ActionScript with influences from JavaScript and the ECMA-262 (Third Edition) standard, supporting the said standard's object model and many of its core data types. Local variables may be declared with the var statement, and user-defined functions with parameter passing and return values can also be created. Notably, ActionScript could now also be typed with a text editor rather than being assembled by choosing actions from drop-down lists and dialog box controls. With the next release of its authoring tool, Flash MX, and its corresponding player, Flash Player 6, the language remained essentially unchanged; there were only minor changes, such as the addition of the switch statement and the "strict equality" (===) operator, which brought it closer to being ECMA-262-compliant. Two important features of ActionScript that distinguish it from later versions are its loose type system and its reliance on prototype-based inheritance. Loose typing refers to the ability of a variable to hold any type of data. This allows for rapid script development and is particularly well-suited for small-scale scripting projects. Prototype-based inheritance is the ActionScript 1.0 mechanism for code reuse and object-oriented programming. Instead of a class keyword that defines common characteristics of a class, ActionScript 1.0 uses a special object that serves as a "prototype" for a class of objects. All common characteristics of a class are defined in the class's prototype object and every instance of that class contains a link to that prototype object.

#### 2003–2006: ActionScript 2.0

The next major revision of the language, ActionScript 2.0, was introduced in September 2003 with the release of Flash MX 2004 and its corresponding player, Flash Player 7. In response to user demand for a language better equipped for larger and more complex applications, ActionScript 2.0 featured compile-time type checking and class-based syntax, such as the keywords class and extends. While this allowed for a more structured object-oriented programming approach, the code would still be compiled to ActionScript 1.0 bytecode, allowing it to be used on the preceding Flash Player 6 as well. In other words, the class-based inheritance syntax was a layer on top of the existing prototype-based system. With ActionScript 2.0, developers could constrain variables to a specific type by adding a type annotation so that type mismatch errors could be found at compile-time. ActionScript 2.0 also introduced class-based inheritance syntax so that developers could create classes and interfaces, much as they would in class-based languages such as Java and C++. This version conformed partially to the ECMAScript Fourth Edition draft specification.

#### 2006–2020: ActionScript 3.0

In June 2006, ActionScript 3.0 debuted with Adobe Flex 2.0 and its corresponding player, Flash Player 9. ActionScript 3.0 was a fundamental restructuring of the language, so much so that it uses an entirely different virtual machine. Flash Player 9 contains two virtual machines, AVM1 for code written in ActionScript 1.0 and 2.0, and AVM2 for content written in ActionScript 3.0. ActionScript 3.0 added limited support for hardware acceleration (DirectX, OpenGL).

The update to the language introduced several new features:

- Compile-time and run-time type checking—type information exists at both compile-time and runtime.
- Improved performance from a class-based inheritance system separate from the prototype-based inheritance system.
- Support for packages, namespaces, and regular expressions.
- Compiles to an entirely new type of bytecode, incompatible with ActionScript 1.0 and 2.0 bytecode.
- Revised Flash Player API, organized into packages.
- Unified event handling system based on the DOM event handling standard.
- Integration of ECMAScript for XML (E4X) for purposes of XML processing.
- Direct access to the Flash runtime display list for complete control of what gets displayed at runtime.
- Completely conforming implementation of the ECMAScript fourth edition draft specification.
- Limited support for dynamic 3D objects. (X, Y, Z rotation, and texture mapping)

### Flash Lite

- **Flash Lite 1.0**: Flash Lite is the Flash technology specifically developed for mobile phones and consumer electronics devices. Supports Flash 4 ActionScript.
- **Flash Lite 1.1**: Flash 4 ActionScript support and additional device APIs added.
- **Flash Lite 2.0 and 2.1**: Added support for Flash 7 ActionScript 2.0 and some additional fscommand2 API.
- **Flash Lite 3**: Added support for Flash 8 ActionScript 2.0 and also FLV video playback.
- **Flash Lite 4**: Added support for Flash 10 ActionScript 3.0 as a browser plugin and also hardware graphics acceleration.

### AIR

Adobe AIR supports ActionScript, in addition to some extended contents, such as the Stage3D engine Adobe has developed. The number of APIs (Application programming interfaces) available to ActionScript 3.0 has also risen dramatically.

## Syntax

ActionScript code is free form and thus may be created with any amount or style of whitespace that an author desires. The basic syntax is derived from ECMAScript.

### ActionScript 2.0

The following code, which works in any compliant player, creates a text field at depth 0, at position (0, 0) on the screen (measured in pixels), that is 100 pixels wide and high. Then the `text` parameter is set to the "Hello, world" string, and it is automatically displayed in the player:

```mw
createTextField("greet", 0, 0, 0, 100, 100);
greet.text = "Hello, world";
```

When writing external ActionScript 2.0 class files the above example could be written in a file named Greeter.as as following.

```mw
package org.wikipedia.example {
    import flash.display.MovieClip;

    class Greeter extends MovieClip {
        public function Greeter() {
            var txtHello: TextField = this.createTextField("txtHello", 0, 0, 0, 100, 100);
            txtHello.text = "Hello, world";
        }
    }
}
```

### ActionScript 3.0

ActionScript 3.0 has a similar syntax to ActionScript 2.0, but a different set of APIs for creating objects. Compare the script below to the previous ActionScript 2.0 version:

```mw
var txtHello: TextField = new TextField();
txtHello.text = "Hello World";
this.addChild(txtHello);
```

Minimal ActionScript 3.0 programs may be somewhat larger and more complicated due to the increased separation of the programming language and the Flash integrated development environment (IDE).

Presume the following file to be Greeter.as:

```mw
package org.wikipedia.example {
    import flash.display.Sprite;
    import flash.text.TextField;

    public class Greeter extends Sprite {
        public function Greeter() {
            var txtHello: TextField = new TextField();
            txtHello.text = "Hello World";
            this.addChild(txtHello);
        }
    }
}
```

ActionScript 3 can also be used in MXML files when using Apache's Flex framework:

```mw
<?xml version="1.0" encoding="utf-8"?>
<s:Application
         xmlns:fx="http://ns.adobe.com/mxml/2009"
	     xmlns:s="library://ns.adobe.com/flex/mx/polysylabi"
	     xmlns:mx="library://ns.adobe.com/flex/mx"
         layout="vertical"
         creationComplete="initApp()">

    <fx:Script>
        <![CDATA[
            public function initApp(): void {
               // Prints our "Hello, world!" message into title
               title.text = "Hello, World!";
            }
        ]]>
    </fx:Script>

    <s:Label id="title" fontSize="54" fontStyle="bold" />
</s:Application>
```

## Data structures

### Data types

ActionScript primarily consists of "fundamental" or "simple" data types that are used to create other data types. These data types are very similar to Java data types. Since ActionScript 3 was a complete rewrite of ActionScript 2, the data types and their inheritances have changed.

**ActionScript 2 top level data types**

- **String**: A list of characters such as "Hello World"
- **Number**: Any Numeric value
- **Boolean**: A simple binary storage that can only be "true" or "false".
- **Object**: Object is the data type all complex data types inherit from. It allows for the grouping of methods, functions, parameters, and other objects.

**ActionScript 2 complex data types**

There are additional "complex" data types. These are more processor and memory intensive and consist of many "simple" data types. For AS2, some of these data types are:

- **MovieClip**: An ActionScript creation that allows easy usage of visible objects.
- **TextField**: A simple dynamic or input text field. Inherits the MovieClip type.
- **Button**: A simple button with 4 frames (states): Up, Over, Down and Hit. Inherits the MovieClip type.
- **Date**: Allows access to information about a specific point in time.
- **Array**: Allows linear storage of data.
- **XML**: An XML object
- **XMLNode**: An XML node
- **LoadVars**: A Load Variables object allows for the storing and send of HTTP POST and HTTP GET variables
- **Sound**
- **NetStream**
- **NetConnection**
- **MovieClipLoader**
- **EventListener**

**ActionScript 3 primitive (prime) data types**

- **Boolean**: The Boolean data type has only two possible values: true and false or 1 and 0. No other values are valid.
- **int**: The int data type is a 32-bit integer between -2,147,483,648 and 2,147,483,647.
- **Null**: The Null data type contains only one value, null. This is the default value for the String data type and all classes that define complex data types, including the Object class.
- **Number**: The Number data type can represent integers, unsigned integers, and floating-point numbers. The Number data type uses the 64-bit double-precision format as specified by the IEEE Standard for Binary Floating-Point Arithmetic (IEEE-754). The Number type can store integers between -9,007,199,254,740,992 (-253) to 9,007,199,254,740,992 (253), and floating-point values between Number.MAX_VALUE (1.79769313486231e+308) and Number.MIN_VALUE (4.940656458412467e-324).
- **String**: The String data type represents a sequence of 16-bit characters. Strings are stored internally as Unicode characters, using the UTF-16 format. Previous versions of Flash used the UTF-8 format.
- **uint**: The uint (unsigned integer) data type is a 32-bit unsigned integer between 0 and 4,294,967,295.
- **void**: The void data type contains only one value, undefined. In previous versions of ActionScript, undefined was the default value for instances of the Object class. In ActionScript 3.0, the default value for Object instances is null.

**ActionScript 3 some complex data types**

- **Array**: Contains a list of data. Though ActionScript 3 is a strongly typed language, the contents of an Array may be of any type and values must be cast back to their original type after retrieval (support for typed Arrays has recently been added with the Vector class).
- **Date**: A date object containing the date/time digital representation.
- **Error**: A generic error object that allows runtime error reporting when thrown as an exception.
- **flash.display:Bitmap**: A non-animated bitmap display object.
- **flash.display:MovieClip**: Animated movie clip display object; Flash timeline is, by default, a MovieClip.
- **flash.display:Shape**: A non-animated vector shape object.
- **flash.display:SimpleButton**: A simple interactive button type supporting "up", "over", and "down" states with an arbitrary hit area.
- **flash.display:Sprite**: A display object container without a timeline.
- **flash.media:Video**: A video playback object supporting direct (progressive download) or streaming (RTMP) transports. As of Flash Player version 9.0.115.0, the H.264/MP4 high-definition video format is also supported alongside standard Flash video (FLV) content.
- **flash.text:TextField**: A dynamic, optionally interactive text field object.
- **flash.utils:ByteArray**: Contains an array of binary byte data.
- **flash.utils:Dictionary**: Dictionaries are a variant of Object that may contain keys of any data type (whereas Object always uses strings for its keys).
- **Function**: The core class for all Flash method definitions.
- **Object**: The Object data type is defined by the Object class. The Object class serves as the base class for all class definitions in ActionScript. Objects in their basic form can be used as associative arrays that contain key-value pairs, where keys are Strings and values may be any type.
- **RegExp**: A regular expression object for strings.
- **Vector**: A variant of array supported when publishing for Flash Player 10 or above. Vectors are typed, dense Arrays (values must be defined or null) which may be fixed-length, and are bounds-checked during retrieval. Vectors are not just more typesafe than Arrays but also perform faster.
- **XML**: A revised XML object based on the E4X (Standard ECMA-357); nodes and attributes are accessed differently from ActionScript 2.0 object (a legacy class named XMLDocument is provided for backwards compatibility).
- **XMLList**: An array-based object for various content lookups in the XML class.

### Using data types

The basic syntax is:

```mw
var variableName: VariableType = new VariableType(param1, param2, ..., paramN);
```

So in order to make an empty Object:

```mw
var myObject: Object = new Object();
```

Or, in an informal way:

```mw
var myObject = {};
```

Some types are automatically put in place:

```mw
var myString: String = "Hello Wikipedia!"; // This would automatically set the variable as a string.
var myNumber: Number = 5; // This would do the same for a number.
var myObject: Object = { param1: "Hi!", param2: 76 }; // This creates an object with two variables.
// param1 is a string with the data of "Hi!",
// and param2 is a number with the data of 76.

// This is the syntax for automatically creating an Array.
var myArray: Array = [5, "Hello!", { a: 5, b: 7 }];
// It creates an Array with 3 variables.
// The first (0) is a number with the value of 5,
// the second (1) is a string with the value of "Hello!",
// and the third (2) is an object with { a: 5, b: 7 }.
```

Unlike some object-oriented languages, ActionScript makes no distinction between primitive types and reference types. In ActionScript, all variables are reference types. However, objects that belong to the primitive data types, which includes Boolean, Number, int, uint, and String, are immutable.

So if a variable of a supposedly primitive type, e.g. an integer is passed to a function, altering that variable inside the function will not alter the original variable, as a new int Object is created when inside the function. If a variable of another (not primitive) datatype, e.g. XML is passed to a function, altering that variable inside the function will alter the original variable as well, as no new XML Object is created.

Some data types can be assigned values with literals:

```mw
var item1: String = "ABC";
var item2: Boolean = true;
var item3: Number = 12;
var item4: Array = ["a", "b", "c"];
var item5: Object = { name: "Actionscript", version: "3.0" };
var item6: XML = <node><child /></node>; // Note that the primitive XML is not quoted
```

A reference in ActionScript is a pointer to an instance of a class. A reference stores the memory address of an object – operations against references will follow the value of the reference to the memory address of the object and carry out the operation on that object. All objects in ActionScript are accessed through references instead of being accessed directly.

```mw
var item1: XML = new XML("<node><child /></node>");
var item2: XML = item1;
item2.firstChild.attributes.value = 13;
// item1 now equals item2 since item2 simply points to what item1 points to.
// Both are now:
// <node><child value="13" /></node>
```

Only references to an object may be removed by using the "delete" keyword. Removal of actual objects and data is done by the Flash Player garbage collector which checks for any existing references in the Flash memory space. If none are found (no other reference is made to the orphaned object), it is removed from memory. For this reason, memory management in ActionScript requires careful application development planning.

```mw
var item1: XML = new XML("<node><child /></node>");
delete item1;
// If no other reference to item1 is present anywhere else in the application,
// it will be removed on the garbage collector's next pass
```

## Code protection

Like most bytecode file formats, Flash SWF files can be decompiled into their source code and assets (similarly to how Microsoft .NET files can be decompiled). Some decompilers are capable of nearly full reconstruction of the original source file, approximate to the actual code that was used during creation (although results vary on a case-by-case basis).

In opposition to the decompilers, ActionScript obfuscators have been introduced, which transform code into a form that breaks decompiler output while preserving the functionality and structure of the program. Higher-quality obfuscators implement lexical transformations such as identifier renaming, control flow transformation, and data abstraction transformation which collectively make it harder for decompilers to generate output likely to be useful to a human. Less robust obfuscators insert traps for decompilers. Such obfuscators either cause the decompiler software to crash unexpectedly or to generate unintelligible source code.
