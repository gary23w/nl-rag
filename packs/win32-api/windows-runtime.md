---
title: "Windows Runtime"
source: https://en.wikipedia.org/wiki/Windows_Runtime
domain: win32-api
license: CC-BY-SA-4.0
tags: win32 api, windows api, windows programming, dynamic-link library
fetched: 2026-07-02
---

# Windows Runtime

**Windows Runtime** (**WinRT**) is a platform-agnostic component and application architecture first introduced in Windows 8 and Windows Server 2012 in 2012. It is implemented in C++ and officially supports development in C++ (via C++/WinRT, C++/CX or WRL), Rust/WinRT, Python/WinRT, JavaScript-TypeScript, and the managed code languages C# and Visual Basic (.NET) (VB.NET).

WinRT is not a runtime in a traditional sense but rather a language-independent application binary interface based on COM to allow object-oriented APIs to be consumed from multiple languages, with services usually provided by a full-blown runtime, such as type activation. That is, WinRT is an "API delivery system". Apps using the Windows Runtime may run inside a sandboxed environment to allow greater security and stability and can natively support both x86 and ARM. WinRT components are designed with interoperability among multiple languages and APIs in mind, including native, managed and scripting languages. Built-in APIs provided by Windows which use the WinRT ABI are commonly known as WinRT APIs; however, anyone can use the WinRT ABI for their own APIs.

## Technology

WinRT is implemented in the programming language C++ and is object-oriented by design. Its underlying technology, the Windows API (Win32 API), is written mostly in the language C. It is an unmanaged application binary interface based on Component Object Model (COM) that allows interfacing from multiple languages, as does COM. However, the API definitions are stored in `.winmd` files, which are encoded in ECMA 335 metadata format, which .NET Framework also uses with a few modifications. For WinRT components implemented in native code, the metadata file only contains the definition of methods, classes, interfaces and enumerations and the implementation is provided in a separate DLL. This common metadata format makes it easier to consume WinRT APIs from .NET apps with simpler syntax than P/Invoke. Windows provides a set of built-in APIs which are built on the WinRT ABI which provide everything from the XAML-based WinUI library and device access such as camera, microphone, etc.

The previous C++/CX (Component Extensions) language, which borrows some C++/CLI syntax, was introduced for writing and consuming WinRT components with less glue code visible to the programmer, relative to classic COM programming in C++, and imposes fewer restrictions relative to C++/CLI on mixing types. The Component Extensions of C++/CX are recommended for use at the API-boundary only, not for other purposes. Regular C++ (with COM-specific discipline) can also be used to program with WinRT components, with the help of the Windows Runtime C++ Template Library (WRL), which is similar in purpose to what Active Template Library provides for COM. In 2019, Microsoft deprecated C++/CX in favor of the C++/WinRT header library.

Most WinRT applications run within a sandbox and need explicit user approval to access critical OS features and underlying hardware. By default, file access is restricted to several predetermined locations, such as the directories Documents or Pictures.

WinRT applications are packaged in the .appx and later the .msix file format; based upon Open Packaging Conventions, it uses a ZIP format with added XML files. WinRT applications are distributed mostly through an application store named Microsoft Store, where Windows apps (termed *Windows Store apps*) can be purchased and downloaded by users. Initially, WinRT apps could only be sideloaded from outside Windows Store on Windows 8 or RT systems that are part of a Windows domain, or equipped with a special activation key obtained from Microsoft. However these restrictions were lifted in the Windows 10 November Update, where users can freely sideload any app signed with a trusted certificate by enabling a setting.

In a major departure from Win32 and similarly to .NET Framework 4.5, most APIs which are expected to take significant time to complete are implemented as asynchronous. When calling a Windows Runtime asynchronous function, the task is started on another thread or process and the function returns immediately, freeing the app to perform other tasks while waiting for results. The asynchronous model requires new programming language constructs. Each language provides their own way to consume asynchronous APIs. Parts of the built-in API needing asynchronous access include on-screen messages and dialogs, file access, Internet connectivity, sockets, streams, devices and services, and calendar, contacts and appointments.

## Services

The metadata describes the APIs written using the WinRT ABI. It defines a programming model that makes it possible to write object-oriented code that can be shared across programming languages, and enables services like reflective programming (reflection).

Herb Sutter, C++ expert at Microsoft, explained during his session on C++ at the 2011 Build conference that the WinRT metadata is in the same format as CLI metadata. Native code (i.e., processor-specific machine code) cannot contain metadata, so it is stored in a separate metadata file that can be reflected like ordinary CLI assemblies. Since it is the same format as CLI metadata, WinRT APIs can be used from managed CLI languages as if it was just a .NET API.

### Type system

WinRT has a rich object-oriented class-based type system that is built on the metadata. It supports constructs with corresponding constructs in the .NET framework: classes, methods, properties, delegates, and events.

One of the major additions to WinRT relative to COM is the cross-application binary interface (ABI), .NET-style generics. Only interfaces and delegates can be generic, runtime classes and methods in them can't. Generic interfaces are also known as parameterized interfaces. In C++/CX, they are declared using the keyword `generic` with a syntax very similar to that of keyword `template`. WinRT classes (ref classes) can also be genericized using C++ templates, but only template instantiations can be exported to .winmd metadata (with some name mangling), unlike WinRT generics which preserve their genericity in the metadata. WinRT also provides a set of interfaces for generic containers that parallel those in the C++ Standard Library, and languages provide some reciprocal (back-and-forth) conversion functions. The consumption of WinRT collections in .NET languages (e.g., C# and VB) and in JavaScript is more transparent than in C++, with automated mappings into their natural equivalents occurring behind the scenes. When authoring a WinRT component in a managed language, some extra, COM-style rules must be followed, e.g. .NET framework collection types cannot be declared as return types, but only the WinRT interfaces that they implement can be used at the component boundary.

#### WinRT components

Classes that are compiled to target the WinRT are called *WinRT components*. They are classes that can be written in any supported language and for any supported platform. The key is the metadata. This metadata makes it possible to interface with the component from any other WinRT language. The runtime requires WinRT components that are built with .NET Framework to use the defined interface types or .NET type interfaces, which automatically map to the first named. Inheritance is as yet not supported in managed WinRT components, except for XAML classes.

### Programming interfaces

Programs and libraries targeted for the WinRT runtime can be created and consumed from several platforms and programming languages. Notably C/C++ (either with language extensions offering first-class support for WinRT concepts, or with a lower-level template library allowing to write code in standard C++), .NET (C# and Visual Basic (.NET) (VB.NET)) and JavaScript. This is made possible by the metadata. In WinRT terminology, a language binding is termed a *language projection.*

#### C++ (C++/WinRT, Component Extensions, WRL)

Standard C++ is a *first-class citizen* of the WinRT platform. As of Windows 10, version 1803, the Windows SDK contains C++/WinRT. C++/WinRT is an entirely standard modern C++17 language projection for Windows Runtime (WinRT) APIs, implemented as a header-file-based library, and designed to provide first-class access to the modern Windows API. With C++/WinRT, Windows Runtime APIs can be authored and consumed using any standards-compliant C++17 compiler. WinRT is a native platform and supports any native (and standard) C++ code, so that a C++ developer can reuse existing native C/C++ libraries. With C++/WinRT, there are no language extensions.

There are two other legacy options for using WinRT from C++: Windows Runtime C++ Template Library (WRL), an ATL-style template library (similar to Windows Template Library or WTL), and C++/CX (C++ with Component Extensions) which resembles C++/CLI. Because of the internal consumption requirements at Microsoft, WRL is exception-free, meaning its return-value discipline is HRESULT-based just like that of COM. C++/CX on the other hand wraps-up calls to WinRT with code that does error checking and throws exceptions as appropriate.

C++/CX has several extensions that enable integration with the platform and its type system. The syntax resembles the one of C++/CLI although it produces native (although not standard) code and metadata that integrates with the runtime. For example, WinRT objects may be allocated with `ref new`, which is the counterpart of `gcnew` from C++/CLI. The hat operator `^` retains its meaning, however in the case where both the caller and callee are written in C++ and living in the same process, a hat reference is simply a pointer to a vptr to a virtual method table (vtable, VMT).

Along with C++/CX, relative to traditional C++ COM programming, are partial classes, again inspired by .NET. These allow instance WinRT XAML code to be translated into C++ code by tools, and then combined with human-written code to produce the complete class while allowing clean separation of the machine-generated and human-edited parts of a class implementation into different files.

#### .NET

The .NET Framework and the Common Language Runtime (CLR) are integrated into the WinRT as a subplatform. It has influenced and set the standards for the ecosystem through the metadata format and libraries. The CLR provides services like JIT-compilation code and garbage collection. WinRT applications using .NET languages use the XAML-based WinUI, and are primarily written in C#, VB.NET, and for the first time for XAML, with native code using C++/CX. Although not yet officially supported, programs can also be written in other .NET languages. With .NET 5, Microsoft removed the built-in WinRT support and instead created CsWinRT, a tool that generates interop code for accessing Windows Runtime APIs similar to how C++/WinRT works.

##### Limitations

Classes defined in WinRT components that are built in managed .NET languages must be declared as `sealed`, so they cannot be derived from. However, non-sealed WinRT classes defined elsewhere can be inherited from in .NET, their virtual methods overridden, and so on; but the inherited managed class must still be sealed.

Members that interface with another language must have a signature with WinRT types or a managed type that is convertible to these.

#### JavaScript

WinRT applications can also be coded using HTML with JavaScript in code-behind, which are run using the Trident rendering engine and Chakra JavaScript engine, both of which are also used by Internet Explorer. When coding a WinRT app in JavaScript, its features are adapted to follow JavaScript naming conventions, and namespaces are also mapped to JavaScript objects.

#### Other languages

Microsoft is in the process of projecting WinRT APIs to languages other than C++. One example is Rust/WinRT, an interface for programs written in Rust to consume and author WinRT APIs. Rust/WinRT is part of Windows App SDK (formerly Project Reunion), a Microsoft effort to reconcile traditional Windows desktop and the UWP app model.

#### Bridges

With the introduction of the Universal Windows Platform (UWP), the platform has received many API bridges that allow programs originally developed for other platforms to be ported easily while taking advantage of UWP features. Microsoft has provided bridges for Android (defunct since 2016), iOS (Cocoa Touch), Progressive Web Apps, Silverlight, as well as traditional Windows desktop apps (using MSIX packaging from the Windows App SDK).

### API

WinRT comes with an application programming interface (API) in the form of a class library that exposes the features of Windows 8 for the developer, like its immersive interface API. It is accessible and consumable from any supported language.

#### Runtime classes

The Windows Runtime classes is a set SDKs that provide access to all functionality from the XAML parser to the camera function. The SDKs are implemented as native C/C++ libraries (unmanaged).

#### Naming conventions

The naming conventions for the components (classes and other members) in the API are heavily influenced by the .NET naming conventions which uses camel case (specifically PascalCase). Microsoft recommends users to follow these rules in case where no others are given.

These conventions are projected differently in some languages, like JavaScript, which converts it to its conventions and the other way around. This is to give a native and consistent experience regardless of the programming language.

#### Restrictions and rules

Since Windows Runtime is projected to various languages, some restrictions on fundamental data types exist so as to host all such languages. Programmers must be careful with the behavior of those types when used with public access (for method parameters, method return values, properties, etc.).

**Basic types**

In .NET languages and C++, a rich set of data types exists, representing various numerals.

In JavaScript, a

Number

can only represent up to 53 bits of precision.

In WinRT, the only lacking numeral data type is 8-bit signed integer relative to .NET and C++. JavaScript developers must be careful when dealing with big numbers while coding for WinRT.

**Strings**

Strings are immutable in .NET and JavaScript, but mutable in C++.

A null pointer passed as a string to WinRT by C++ is converted to an empty string

In .Net, null being passed as a string to WinRT is converted to an empty string

In JavaScript, null being passed as a string to WinRT is converted to a string with the word

null

. This is due to JavaScript's keyword

null

being represented as a null object. Similar results occur when passing

undefined

to WinRT from JavaScript.

**Structs**

In .NET and C++, structs are value types, and such a struct can contain any type in it.

JavaScript does not directly support structs.

In WinRT, use of structs is allowed only for containing types that have value semantics, including numerals, strings, and other structs. Pointers or interface references are disallowed.

**References**

In .NET, objects are passed by reference, whereas numerals and structs are passed by value.

In C++, all types can be passed by reference or value.

In WinRT, interfaces are passed by reference; all other types can be passed either by value or by reference.

**Arrays**

In .NET, C++, and JavaScript arrays are reference types.

In WinRT, arrays are value types and quite restricted.

**Events**

In .NET and C++, clients subscribe to events using

+=

operator.

In JavaScript,

addEventListener

function or setting

on<EventName>

property is used to subscribe to events.

In WinRT, all languages can use their own way to subscribe to events.

**Collections**

Some .NET collections map directly to WinRT collections.

WinRT

Vector

type resembles arrays and the array syntax is used to consume them.

WinRT

Map

type is a key/value pair collection, and is projected as Dictionary in .NET languages.

**Method overloading**

All WinRT languages (.NET, C++, JavaScript) support overloading on parameters

.NET and C++ also support overloading on type.

In WinRT, only parameter number is used for overloading.

**Asynchrony**

All WinRT methods are designed such that any method taking longer than 50 milliseconds is an async method.

The established naming pattern to distinguish asynchronous methods is

<Verb>[<Noun>]Async

. For the full runtime library, all methods that have a chance to last longer than 50 ms are implemented as asynchronous methods only.

## Windows Phone Runtime

Windows Phone 8.1 uses a version of the Windows Runtime named the *Windows Phone Runtime*. It enables developing applications in C# and VB.NET, and Windows Runtime components in C++/CX. Although WP8 brought limited support, the platform did eventually converge with Windows 8.1 in Windows Phone 8.1.

### Windows Phone 8

Windows Phone 8 has limited support for developing and consuming Windows Runtime components through *Windows Phone Runtime*. Many of the Windows Runtime APIs in Windows 8 that handle core operating system functions have been ported to Windows Phone 8. Support for developing native games using C++/CX and DirectX has been added, by request from the game development industry.

However, the Windows Phone XAML Framework is still based on the same Microsoft Silverlight framework, as in Windows Phone 7, for backward compatibility. Thus, as of 2016, XAML development is impossible in C++/CX. Development using either HTML5 or WinJS is unsupported on Windows Phone 8.

### Windows Phone 8.1

Windows Runtime support on Windows Phone 8.1 converges with Windows 8.1. The release brings a full Windows Runtime API to the platform, including support for WinRT XAML, and language bindings for C++/CX, and HTML5-JavaScript. There is also a project type called *Universal apps* to enable apps to share code across 8.1 versions of Windows Phone and Windows.

The Windows Phone 8 Silverlight Framework has been updated. It can exploit some of the new features in the Windows Runtime.

Windows Phone Runtime uses the AppX package format from Windows 8, after formerly using Silverlight XAP.
