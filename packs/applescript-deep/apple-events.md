---
title: "Apple event"
source: https://en.wikipedia.org/wiki/Apple_events
domain: applescript-deep
license: CC-BY-SA-4.0
tags: applescript language, apple events, hypercard software, scripting language, classic mac
fetched: 2026-07-02
---

# Apple event

(Redirected from

Apple events

)

**Apple events** are the message-based interprocess communication mechanism in Mac OS, first making an appearance in System 7 and supported by every version of the classic Mac OS since then and by macOS. Apple events describe "high-level" events such as "open document" or "print file", whereas earlier OSs had supported much more basic events, namely "click" and "keypress". Apple events form the basis of the Mac OS scripting system, the Open Scripting Architecture (the primary language of such being AppleScript).

The starting point is a dynamically-typed, extensible descriptor format called an **AEDesc**, which is just an OSType code specifying the data type, together with a block of type-dependent data. For instance, the OSType code `inte` indicates that the data was a four-byte signed integer in big-endian format.

Besides predefined type codes for various common simple types, there are two predefined structured descriptor types: an **AERecord**, which has data type `reco` (record), and **AEList** with type `list` (list or array). The internal structure of these contain recursively-nested AEDescs, while the AERecord also associates each element with a unique record field ID, which is an OSType. The Apple Event Manager provides API calls to construct these structures, as well as extract their contents and query the type of contents they hold.

The Apple Event Manager also supports *coercions*, which converts AEDescs from one data type to another. In addition to standard coercions, for instance between integer and real types, applications can install their own coercion handler callbacks, which handle conversions to and from custom data types.

An **Apple event** proper is an AERecord with fields that depended on the purpose of the event. In addition, it has *attributes* (which are distinct from record fields, which are now called the *parameters* of the event) from a set predefined by the Apple Event Manager. These specify what the event is supposed to do (through *event class* and *event ID*), the target address to which the event is to be sent (which could be a process on the local or a remote machine), and various other options for handling it. Remote machines initially had to be connected via AppleTalk, but Mac OS 9 added the option for connections via TCP/IP.

After sending an Apple event to its target process, the sending process can elect to receive a reply to an Apple event. This can contain various bits of information returned from the target about the processing of the original event, including an error code indicating success/failure, any information requested by the original event, and/or other appropriate information.

Apple events are the foundation of the AppleEvent Object Model, which in turn is the foundation of the OSA and AppleScript. As of 2016, the official implementation of the Apple Event Manager API is available in C and its descendants, including C++. Official bindings are also provided for Objective-C and Swift through the Cocoa API. Unofficial bindings also exist for other languages (with varying degrees of limitation), including Perl, UserTalk, Ruby and Python.

## Object Model

The **AppleEvent Object Model** (**AEOM**) was a set of protocols built on top of AppleEvents by which applications running under classic Mac OS and macOS could control each other's functions. Applications that implemented some part of the AEOM were called *scriptable* because they could be controlled via AppleScript. Unfortunately, scriptability support remained patchy and inconsistent throughout the history of classic Mac OS.

The AEOM provided a syntactic layer under which any application could publish its internal objects, allowing those objects to be manipulated in a standardized way. Unlike other similar-sounding concepts such as ToolTalk, there was a clear, orthogonal distinction between *nouns* and *verbs*; thus, instead of providing separate commands for "close document" and "close window", there was a single "close" verb which could take references to "document" or "window" objects, or any other object that the application published.

The objects that an application made available through its AEOM support were arranged in a hierarchy. At the top was the application itself, referenced via a null object descriptor. Other objects were referenced by (recursively) specifying their parent object, together with other information identifying it as a child of that parent, all collected in an AERecord. An *iterator* was provided by parents to enumerate their children, or children of a certain class, allowing applications to address a set of elements. The system was generally similar to the Document Object Model used in XML, although with some differences in access patterns.

Each object could have *elements* and *properties*; elements were other objects, which might be created or deleted, while properties could not be created or deleted but had values which might be interrogated or changed. For instance, the application might have one or more window *elements* representing windows showing the contents of currently-open documents. These windows might have *properties* such as their title, position and size.

An application could define custom verbs for operating on its objects. The AEOM also specified various standard verbs which (it was hoped) applications would implement in a consistent fashion, such as open, close, create element, delete, set data, and get data. Each verb was defined as an AppleEvent of a specific type and class, together with particular parameters of particular types that were expected to be present. For instance, the "get data" event was the standard means for obtaining the value of a property: it took essentially one parameter, which was an object descriptor identifying the property to be queried. The value of that property would be returned in the reply event. The "set data" event took two parameters, the object descriptor for the property to set and the new value for the property; the reply event was only expected to return a success status or failure error code.

The entire AppleEvent architecture identifies things using four-byte OSType codes, studiously avoiding actual words or phrases in English (or any other language). Instead, the correspondence between internal AppleEvent codes and external natural-language descriptions is specified through the **aete** (*AppleEvent Terminology Extension*) resource — the "extension" being to the standard terminology built into AppleScript itself. An application may provide multiple 'aete' resources for multiple languages, in keeping with the original multilingual design of AppleScript itself

For instance, consider the following AppleScript sequence controlling a fictional drawing application:

```mw
 tell application "ScriptableDraw"
   set background color of window "New Drawing" to background color of window "Old Drawing"
 end tell
```

This actually involves the sending of two AppleEvents to the target application (and the receipt of their corresponding replies): first, a get-data event is sent to retrieve the background color property of the window identified by the name "Old Drawing"; then a set-data event is sent to apply the value returned as the background color property of the window named "New Drawing".

Since this sort of access pattern was typical, AppleScript made widespread use of the `tell` statement, which switched the context to the named object in a fashion similar to the `with` statement found in Visual Basic or Pascal. All commands after the `tell` to the corresponding `end tell` would be sent to the object named in the `tell`, instead of the default object, which was the current application.

Object descriptors allowed the identification of objects in various ways. The most interesting one was using a where-clause (which translated into AppleScript terminology as a *filter expression*). For instance, the AppleScript 1.0 SDK shipped with the source code for an example application called the Scriptable Text Editor, which would respond to scripts such as:

```mw
 tell application "Scriptable Text Editor"
   tell window "Example Document"
     set text style of every word whose length > 7 to bold
   end tell
 end tell
```

Even today, it is rare to find this kind of power in general-purpose scripting languages outside of SQL.

Adding support for the AEOM in the classic Mac OS was a difficult process. Application developers had to identify their objects and hand-write code to allow them to be addressed. This typically took the form of code for returning the "next" object of a particular type, allowing AppleScript to iterate over them. But since the OS did not contain an object model, this work was left entirely to the developers, many of whom did not implement it. Oddly, even Apple's own application framework, MacApp, did not offer such a model except for the GUI objects it knew about, once again making the developer do most of the work of scripting the objects representing the data itself. Largely for these reasons, AppleScript support was not very widespread.

Apple did attempt to address this problem with the introduction of various object "suites", which represented standard objects and verbs that were expected to be supported by different types of applications. For instance, all applications were expected to support the "core suite", and any application editing text was expected to support the "text suite". By selecting a suitable set of suites, the developer could at least reduce the workload of planning how to expose their objects. Yet because these objects were generally not part of the system itself (with the exception of the severely limited TextEdit editor), the actual implementation was left to the developer.

Applications developed in Cocoa, the system formerly known as OpenStep, offer a rich object runtime that can be queried from any other application. This makes implementation of the AEOM considerably easier, dramatically reducing the amount of code needed in the average application. Additionally the majority of Cocoa applications are constructed primarily from Cocoa-standard objects, all of which were upgraded to offer fairly extensive scriptability. This extends not only to GUI objects as under MacApp, but also to data objects inside them, including text, tables and various list objects. A text file is used to map the internal "object-like" names onto human-readable versions, and in most cases creating this is all that is needed to add fairly substantial scriptability to most programs.

While Cocoa applications are not AEOM based, and often use subtly different objects than Apple's originally defined standard objects, Cocoa apps are generally much more scriptable than their "classic" counterparts—in fact, it is uncommon to find a Cocoa application that is *not* scriptable to some degree.

## Scripting Bridge

The Scripting Bridge is a macOS framework which allows applications to communicate with each other without the use of an intermediary scripting language such as AppleScript. Like AppleScript, the Scripting Bridge uses Apple events for inter-application communication.

The Scripting Bridge is typically used from Objective-C, but can be used in other programming languages through an Objective-C bridge such as MacRuby and PyObjC.
