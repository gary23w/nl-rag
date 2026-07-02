---
title: "Delphi (software)"
source: https://en.wikipedia.org/wiki/Delphi_(software)
domain: object-pascal
license: CC-BY-SA-4.0
tags: object pascal, delphi language, free pascal, lazarus ide
fetched: 2026-07-02
---

# Delphi (software)

**Delphi** is a general-purpose programming language and a software product that uses the Delphi dialect of the Object Pascal programming language and provides an integrated development environment (IDE) for rapid application development of desktop, mobile, web, and console software, currently developed and maintained by Embarcadero Technologies.

Delphi's compilers generate native code for Microsoft Windows, macOS, iOS, Android and Linux (x64).

Delphi includes a code editor, a visual designer, an integrated debugger, a source code control component, and support for third-party plugins. The code editor features Code Insight (code completion), Error Insight (real-time error-checking), and refactoring. The visual forms designer has the option of using either the Visual Component Library (VCL) for pure Windows development or the FireMonkey (FMX) framework for cross-platform development. Database support is a key feature and is provided by FireDAC (Database Access Components). Delphi is known for its fast compilation speed, native code, and developer productivity.

Delphi was originally developed by Borland as a rapid application development tool for Windows as the successor of Turbo Pascal. Delphi added full object-oriented programming to the existing language, and the language has grown to support generics, anonymous methods, closures, and native Component Object Model (COM) support.

Delphi and its C++ counterpart, C++Builder, are interoperable and jointly sold under the name RAD Studio. There are Professional, Enterprise, and Architect editions, with the higher editions having more features at a higher price. There is also a free-of-charge Community edition, with most of the features of Professional, but restricted to users and companies with low revenue.

## Features

Delphi supports rapid application development (RAD). Prominent features are a visual designer and two application frameworks, Visual Component Library (VCL) for Windows and FireMonkey (FMX) for cross-platform development.

Delphi uses the Pascal-based programming language Object Pascal created by Anders Hejlsberg for Borland (now IDERA) as the successor to Turbo Pascal. It supports native cross-compilation to many platforms including Windows, Linux, iOS, and Android.

To better support development for Microsoft Windows and interoperate with code developed with other software development tools, Delphi supports independent interfaces of Component Object Model (COM) with reference counting class implementations, and support for many third-party components. Interface implementations can be delegated to fields or properties of classes. Message handlers are implemented by tagging a method of a class with the integer constant of the message to handle.

Database connectivity is extensively supported through VCL database-aware and database access components.

Later versions have included upgraded and enhanced runtime library routines, some provided by the community group FastCode.

### Characteristics

Delphi uses a strongly typed high-level programming language, intended to be easy to use and originally based on the earlier Object Pascal language. Pascal was originally developed as a general-purpose language "suitable for expressing the fundamental constructs known at the time in a concise and logical way", and "its implementation was to be efficient and competitive with existing FORTRAN compilers" but without low-level programming facilities or access to hardware. Turbo Pascal and its descendants, including Delphi, support access to hardware and low-level programming, with the facility to incorporate code written in assembly language and other languages. Delphi's object-orientation features only class- and interface-based polymorphism. Metaclasses are first class objects. Objects are references to the objects (as in Java), which Delphi implicitly de-references, so there is usually no need to manually allocate memory for pointers to objects or use similar techniques that some other languages need. There are dedicated reference-counted string types, and also null-terminated strings.

Strings can be concatenated by using the '+' operator, rather than using functions. For dedicated string types, Delphi handles memory management without programmer intervention. Since Borland Developer Studio 2006, there are functions to locate memory leaks.

Delphi includes an integrated IDE. The Delphi products all ship with a run-time library (RTL) and a Visual Component Library (VCL), including most of its source code. Third-party components (sometimes with full source code) and tools to enhance the IDE or for other Delphi related development tasks are available, some free of charge. The IDE includes a GUI for localization and translation of created programs that may be deployed to a translator; there are also third-party tools with more features for this purpose. The VCL framework maintains a high level of source compatibility between versions, which simplifies updating existing source code to a newer Delphi version. Third-party libraries typically need updates from the vendor but, if source code is supplied, recompilation with the newer version may be sufficient. The VCL was an early adopter of dependency injection or inversion of control; it uses a reusable component model, extensible by the developer. With class helpers, new functionality can be introduced to core RTL and VCL classes without changing the original source code of the RTL or VCL.

Delphi supports a wide range of third-party database access components that provide native connectivity to major database systems. These include specialized libraries for Oracle, SQL Server, MySQL/MariaDB, PostgreSQL, SQLite, and InterBase/Firebird. Some components, like DAC, offer universal data access solutions supporting multiple databases and cloud services such as Salesforce and FreshBooks. These libraries are regularly updated to remain compatible with the latest IDE versions (e.g., RAD Studio 12), operating systems (e.g., macOS Sonoma, iOS 17, Android 13), and database engines (e.g., Oracle 23, SQL Server 2022, PostgreSQL 16).

The compiler is optimizing and is a single-pass compiler. It can optionally compile to a single executable which does not require DLLs. Delphi can also generate standard DLLs, ActiveX DLLs, COM automation servers and Windows services.

The Delphi IDEs since Delphi 2005 increasingly support refactoring features such as method extraction and the possibility to create UML models from the source code or to modify the source through changes made in the model.

Delphi has communities on the web, where also its employees actively participate. And Delphi is using in collaboration with FireDAC components.

### Backward compatibility

Delphi is one of the languages where backward compatibility is close to 100%. Although each new release of Delphi attempts to keep as much backward compatibility as possible to allow existing code reuse, new features, new libraries, and improvements sometimes make newer releases less than 100% backward compatible.

Since 2016, there have been new releases of Delphi every six months, with new platforms being added approximately every second release.

### Frameworks

Delphi offers two frameworks for visual application development, VCL and FireMonkey (FMX):

- Visual Component Library (VCL) is the framework for developing pure Windows applications. VCL is a long-standing framework, included in the first release of Delphi and actively developed ever since then.
- FireMonkey (later abbreviated FMX), was released in 2011, as part of Delphi XE2, together with an additional set of built-in compilers for non-Windows platforms. FireMonkey is a cross-platform framework for Windows, macOS, iOS, Android and Linux (x64). The GUI parts of FireMonkey are largely based on Direct3D and OpenGL. FireMonkey is not compatible with VCL; they are two separate frameworks. FireMonkey applications do, however, allow easy sharing of non-visual code units with VCL applications, enabling a lot of code to be ported or shared easily between the platforms.

### Interoperability

Delphi and its C++ counterpart, C++Builder, are interoperable. They share many core components, notably the IDE, the VCL and FMX frameworks, and much of the runtime library. In addition, they can be used jointly in a project. For example, C++Builder 6 and later can combine source code from Delphi and C++ in one project, while packages compiled with C++Builder can be used from within Delphi. In 2007, the products were released jointly as RAD Studio, a shared host for Delphi and C++Builder, which can be purchased with either or both. Starting with Rio, there is also interoperability with Python.

### Sample "Hello World" program

```mw
program ObjectPascalExample;

type
  THelloWorld = class
    procedure Put;
  end;

procedure THelloWorld.Put;
begin
  Writeln('Hello, World!');
end;

var
  HelloWorld: THelloWorld;               { this is an implicit pointer }

begin
  HelloWorld := THelloWorld.Create;      { constructor returns a pointer to an object of type THelloWorld }
  HelloWorld.Put;
  HelloWorld.Free;                       { this line deallocates the THelloWorld object pointed to by HelloWorld }
end.
```

Note that the object construct is still available in Delphi.

## History

## Uses in schools

In 2016, Delphi was named the language of choice for teaching programming in South African schools as a subject of information technology (IT).

## Roadmaps

Embarcadero used to publish "roadmaps" describing their future development plans. The last one was published in November 2020. Version 10.5 referred to in the November 2020 roadmap was renamed 11.0. Starting with Delphi 11, Embarcadero decided to no longer publish formal roadmaps. Instead, possible new features are now presented in a loose order through blog entries and online webinars. An important role has Marco Cantú (product manager) with his blog.

- Borland Enterprise Studio, a precursor to RAD Studio, is a software development suite that includes support for multiple languages. Borland Enterprise Studio for Windows supports Delphi.
- Borland Kylix: Similar to Delphi, but for Linux, released in 2001. This was the first attempt to add Linux support to the Delphi product family. Kylix used the new CLX cross-platform framework (based on Qt), instead of Delphi's VCL. Kylix was discontinued after version 3. Today Linux support is integrated into the main Delphi product and uses the FireMonkey cross-platform framework.
- InterBase is an embeddable SQL database that integrates natively to Delphi and C++Builder for client/server or embedded development. Its distinguishing features reduced administration requirements, commercial-grade data security, disaster recovery, and change synchronization. It is also accessible by all major languages and platforms in the market with database connection protocols like ODBC, ADO, ADO.NET and even with Java by JDBC/ODBC Bridge or Java type 4 connectors.
- JBuilder was a tool for Java development based on Eclipse since version JBuilder 2007.
- RadPHP (later replaced with HTML5 Builder) was an IDE for PHP that provided true RAD functionality. It has a form designer similar to that of Delphi or Visual Basic, and an integrated debugger based on the Apache web server. It also includes a VCL library ported to PHP. Unlike other IDEs, it supports Web 2.0 features such as Ajax. Delphi for PHP was announced on March 20, 2007, renamed in October 2010 to RadPHP, and is based on Qadram Q studio. Embarcadero acquired Qadram in January 2011.
- Delphi Prism (later renamed Embarcadero Prism) derived from the Oxygene language (formerly named Chrome) from RemObjects. It ran in the Microsoft Visual Studio IDE rather than RAD Studio. It was licensed and rebranded by Embarcadero to replace Delphi.NET when that product was discontinued.
- Free Pascal is an open-source Pascal cross-platform cross-compiler that supports most of Delphi's Object Pascal code. Free Pascal also has its own language extensions, multiple compiler [language syntax] modes, and supports 18+ operating systems and 9+ processor architectures. Lazarus is a cross-platform RAD IDE that uses the Free Pascal compiler.

### Notable third-party libraries

- FastCode – Enhanced runtime libraries and memory manager.
- OpenWire (library) – Data flow, events, and state synchronization component library.
- Teechart – Charting library.
