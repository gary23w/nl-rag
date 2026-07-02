---
title: "Extensible Application Markup Language"
source: https://en.wikipedia.org/wiki/Extensible_Application_Markup_Language
domain: avalonia-ui
license: CC-BY-SA-4.0
tags: avalonia toolkit, cross-platform xaml, skia rendering ui, dotnet desktop framework
fetched: 2026-07-02
---

# Extensible Application Markup Language

**Extensible Application Markup Language** (**XAML** /ˈzæməl/ ⓘ) is a declarative XML-based language developed by Microsoft for initializing structured values and objects. It is available under Microsoft's Open Specification Promise.

XAML is used extensively in Windows Presentation Foundation (WPF), Silverlight, Workflow Foundation (WF), Windows UI Library (WinUI), Universal Windows Platform (UWP), and .NET Multi-platform App UI (.NET MAUI). In WPF and UWP, XAML is a user interface markup language to define UI elements, data binding, and events. In WF, however, XAML defines workflows.

XAML elements map directly to Common Language Runtime (CLR) object instances, while XAML attributes map to CLR properties and events on those objects.

Anything that is created or implemented in XAML can be expressed using a more traditional .NET language, such as C# or Visual Basic .NET. However, a key aspect of the technology is the reduced complexity needed for tools to process XAML, because it is based on XML.

## Technology

XAML originally stood for Extensible Avalon Markup Language, *Avalon* being the code-name for Windows Presentation Foundation (WPF). Before the end of .NET Framework 3.0 development, however, Microsoft adopted XAML for Workflow Foundation (WF).

In WPF, XAML describes visual user interfaces. WPF allows for the definition of both 2D and 3D objects, rotations, animations, and a variety of other effects and features. A XAML file can be compiled into a Binary Application Markup Language (BAML) file, which may be inserted as a resource into a .NET Framework assembly. At run-time, the framework engine extracts the BAML file from assembly resources, parses it, and creates a corresponding WPF visual tree or workflow.

In WF contexts, XAML describes potentially long-running declarative logic, such as those created by process modeling tools and rules systems. The serialization format for workflows was previously called XOML, to differentiate it from UI markup use of XAML, but now they are no longer distinguished. However, the file extension for files containing the workflow markup is still ".xoml".

XAML uses a specific way to define look and feel called *Template*s; differing from Cascading Style Sheet syntax, it is closer to XBL.

To create XAML files, one could use Microsoft Expression Blend, Microsoft Visual Studio, the hostable WF visual designer, or XAMLPad.

## Examples

This Windows Presentation Foundation example shows the text "Hello, world!" in the top-level XAML container called Canvas.

```mw
<Canvas xmlns="http://schemas.microsoft.com/client/2010"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <TextBlock>Hello, world!</TextBlock>
</Canvas>
```

The schema (the `xmlns="http://schemas.microsoft.com/..."` part) may have to be changed to work on some computers. Using a schema that Microsoft recommends, the example can also be

```mw
<Canvas xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation">
  <TextBlock>Hello, world!</TextBlock>
</Canvas>
```

A crucial part of utilizing XAML to its full potential is making appropriate usage of binding, as well as creating custom user elements as required. Binding can be done as follows:

```mw
<TextBox x:Name="txtInput" />
<TextBlock Text="{Binding ElementName=txtInput,Path=Text}" />
```

## Differences between versions of XAML

There are three main Microsoft implementations of XAML:

- Windows Presentation Foundation (WPF), first available with .NET Framework 3.0
- Silverlight 3 and 4, first available for Internet Explorer 6 and now deprecated
- Windows UI Library (formerly UWP XAML and WinRT XAML), first shipped with Windows 8 and Windows Server 2012, but now available as a part of the Windows App SDK

These versions have some differences in the parsing behavior. Additionally, the Silverlight 4 XAML parser is not 100% backward-compatible with Silverlight 3 files. Silverlight 3 XAML files may be rejected or parsed differently by the Silverlight 4 parser.

Besides Microsoft implementations, there is also OpenSilver (formerly known as CSHTML5), a contemporary web technology implementation.

## XAML applications in web browsers

Historically, XAML based applications could be run in some web browsers, such as Internet Explorer and Firefox. This could be achieved through XBAP files created from WPF applications, or via the Silverlight browser plugin. However, both these methods are now unsupported on all major browsers due to their reliance on the discontinued NPAPI browser plugin interface.

## Lock-in concerns

In 2007, European Committee for Interoperable Systems (ECIS) – a coalition of mostly American software companies – accused Microsoft of attempting to hijack HTML and replace it with XAML, thus creating a vendor lock-in. Jeremy Reimer, writing for *Ars Technica* described this comment as "the most egregious error" and added that XAML is unlikely to ever replace HTML.
