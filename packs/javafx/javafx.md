---
title: "JavaFX"
source: https://en.wikipedia.org/wiki/JavaFX
domain: javafx
license: CC-BY-SA-4.0
tags: javafx toolkit, fxml markup, scene graph ui, java rich client
fetched: 2026-07-02
---

# JavaFX

**JavaFX** is a software platform for creating and delivering desktop applications, as well as rich web applications that can run across a wide variety of devices. JavaFX has support for desktop computers and web browsers on Microsoft Windows, Linux (including Raspberry Pi), and macOS, as well as mobile devices running iOS and Android, through Gluon Mobile.

With the release of JDK 11 in 2018, Oracle made JavaFX part of the OpenJDK under the *OpenJFX* project, in order to increase the pace of its development.

Open-source JavaFXPorts works for Android and iOS (iPhone and iPad). The related commercial software created under the name "Gluon" supports the same mobile platforms with additional features plus desktop. This allows a single source code base to create applications for the desktop, Android, and iOS devices.

## Features

JavaFX 1.1 was based on the concept of a "common profile" that is intended to span across all devices supported by JavaFX. This approach makes it possible for developers to use a common programming model while building an application targeted for both desktop and mobile devices and to share much of the code, graphics assets and content between desktop and mobile versions. To address the need for tuning applications on a specific class of devices, the JavaFX 1.1 platform includes APIs that are desktop or mobile-specific. For example, the JavaFX Desktop profile includes Swing and advanced visual effects. JavaFX places all its symbols in the namespace `javafx`.

For the end user, the "Drag-to-Install" feature enables them to drag a JavaFX widget - an application residing in a website - and drop it onto their desktop. The application will not lose its state or context even after the browser is closed. An application can also be re-launched by clicking on a shortcut that gets created automatically on the user's desktop. This behavior is enabled out-of-the-box by the Java applet mechanism since the Java 6u10 update, and is leveraged by JavaFX from the underlying Java layer. Sun touts "Drag-to-Install" as opening up of a new distribution model and allowing developers to "break away from the browser".

JavaFX 1.x included a set of plug-ins for Adobe Photoshop and Illustrator that enable advanced graphics to be integrated directly into JavaFX applications. The plug-ins generate JavaFX Script code that preserves the layers and structure of the graphics. Developers can then add animation or effects to the static graphics imported. There is also an SVG graphics converter tool (also known as Media Factory) that allows for importing graphics and previewing assets after the conversion to JavaFX format.

Before version 2.0 of JavaFX, developers used a statically typed, declarative language called JavaFX Script to build JavaFX applications. Because JavaFX Script was compiled to Java bytecode, programmers could also use Java code instead. JavaFX applications before 2.0 could run on any desktop that could run Java SE, just like it is with the current versions.

JavaFX 2.0 and later is implemented as a Java library, and applications using JavaFX are written in normal Java code. The scripting language was discontinued by Oracle, however the development of it continued for a few years in the Visage project, finally ending in 2013.

Sun Microsystems licensed a custom typeface called Amble for use on JavaFX-powered devices. The font family was designed by mobile user interface design specialist Punchcut and is available as part of the JavaFX SDK 1.3 Release.

### WebView

WebView, the embedded web browser component, uses the WebKit browser engine. It supports the usual HTML5 features such as canvas, media, meter, progress, details and summary tags as well as MathML, SVG, JavaScript and CSS. WebAssembly support is not enabled.

### 3D

Since JavaFX 8, JavaFX has had 3D capablilities, such as dynamic lights, basic shapes, meshes, texture mapping, et cetera. these components can be integrated into scenes and subscenes.

### JavaFX Mobile

JavaFX Mobile was the implementation of the JavaFX platform for rich web applications aimed at mobile devices. JavaFX Mobile 1.x applications can be developed in the same language, JavaFX Script, as JavaFX 1.x applications for browser or desktop, and using the same tools: JavaFX SDK and the JavaFX Production Suite. This concept makes it possible to share code-base and graphics assets for desktop and mobile applications. Through integration with Java ME, the JavaFX applications have access to capabilities of the underlying handset, such as the filesystem, camera, GPS, bluetooth or accelerometer.

An independent application platform built on Java, JavaFX Mobile is capable of running on multiple mobile operating systems, including Android, Windows Mobile, and proprietary real-time operating systems.

JavaFX Mobile was publicly available as part of the JavaFX 1.1 release announced by Sun Microsystems on February 12, 2009.

Sun planned to enable out-of-the-box support of JavaFX on the devices by working with handset manufacturers and mobile operators to preload the JavaFX Mobile runtime on the handsets. JavaFX Mobile running on an Android was demonstrated at JavaOne 2008 and selected partnerships (incl. LG Electronics, Sony Ericsson) were announced at the JavaFX Mobile launch in February, 2009.

### Example

To launch a JavaFX application, the main class extends `javafx.application.Application` and `main()` calls `Application::launch` which internally calls `Application::start`, which is overridden by the main class and acts as the entry point of the application itself.

```mw
package org.wikipedia.examples;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class JavaFXExample extends Application {
    @Override
    public void start(Stage primaryStage) {
        Button button = new Button("Click Me!");
        button.setOnAction(e -> System.out.println("Hello from JavaFX!"));

        StackPane root = new StackPane(button);
        Scene scene = new Scene(root, 300, 200);

        primaryStage.setTitle("JavaFX Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

## Components

The JavaFX platform includes the following components:

- The JavaFX SDK: Including among other things graphics, media services, rich text libraries, and the web view.
- NetBeans IDE for JavaFX: NetBeans with drag-and-drop palette to add objects with transformations, effects and animations plus a set of samples and best practices. For Eclipse users there is a community-supported plugin hosted on e(fx)clipse.
- JavaFX Scene Builder: This was introduced for JavaFX 2.1 and later. A user interface (UI) is created by dragging and dropping controls from a palette. The layout is saved as an FXML file, which is a special XML format.

### Modules

JavaFX is split into the following modules.

| Name | Description |
|---|---|
| `javafx.base` | Defines core APIs for the JavaFX UI toolkit (such as APIs for bindings, properties, collections, and events). |
| `javafx.controls` | Defines the APIs for UI controls, charts, skins in the JavaFX UI toolkit. |
| `javafx.fxml` | Defines the FXML APIs in the JavaFX UI toolkit. |
| `javafx.graphics` | Defines scenegraph, animation, geometry, and other related APIs for the JavaFX UI toolkit. |
| `javafx.media` | Defines media playback and audio content APIs for the JavaFX UI toolkit. |
| `javafx.swing` | Defines JavaFX/Swing interop support APIs for the JavaFX UI toolkit. |
| `javafx.web` | Defines WebView APIs for the JavaFX UI toolkit. |
| `jdk.jsobject` | Defines APIs for JavaScript objects. |
| `jfx.incubator.input` | Incubates mechanism for customising JavaFX controls. |
| `jfx.incubator.richtext` | Incubates RichTextArea control for JavaFX. |

## History

### Releases after version bump

JavaFX is now part of the JRE/JDK for Java 8 (released on March 18, 2014) and has the same numbering, i.e., JavaFX 8.

JavaFX 8 adds several new features, including:

- Support for 3D graphics
- Sensor support
- MathML support, with JavaFX 8 Update 192
- Printing and rich text support
- Generic dialog templates to replace JOptionPane (as of JavaFX 8u40)

JavaFX 9 features were centered on extracting some useful private APIs from the JavaFX code to make these APIs public:

- JEP 253: Prepare JavaFX UI Controls and CSS APIs for Modularization

Oracle announced their intention to stop bundling JavaFX in their build of JDK 11 and later. It is no longer bundled with the latest version.

JavaFX 11 was first shipped in September 2018.

- JavaFX 11.0.2 is the latest public release of JavaFX 11.
- JavaFX 11.0.16 is the latest release of JavaFX 11 for those with a long-term support contract.
- MathML support
- FX Robot API

JavaFX 12 was first shipped in March 2019.

- JavaFX 12.0.1.
- Support for mouse forward/back buttons
- New protected VirtualFlow methods for subclassing

JavaFX 13 shipped in September 2019.

- Support for e-paper displays
- Support for native media rendering, through WritableImages backed by NIO ByteBuffers

JavaFX 14 was released in March 2020.

- Tab size property for Text and TextFlow
- Support for HTTP/2 in WebView

JavaFX 15 was released in September 2020.

- Support for e-paper displays on i.MX6 devices

JavaFX 16 was released in March 2021.

JavaFX 17 was released in September 2021. Highlights:

- 3D SpotLight type
- Load images and stylesheets from inline data-URIs
- Print to files
- Query states of CAPS LOCK and NUM LOCK keys
- Support for multiple screens in the window toolkit for embedded platforms

JavaFX 18 was released in March 2022. Highlights:

- Support for the H.265/HEVC media codec in the video player
- 3D DirectionalLight type
- Transparent backgrounds in WebView
- Set the "managed" property of nodes from CSS
- Factory methods for Border and Background

JavaFX 19 was released in September 2022. Highlights:

- Support for the H.265/HEVC HTTP Live Streaming in the video player
- Fluent bindings with lambdas: map, flatMap and orElse
- :focus-visibile and :focus-within CSS pseudo-classes

JavaFX 20 was released in March 2023. Highlights:

- Constrained resize policies for TableView and TreeTableView
- Improved lifecycle of UI controls skins (Skin::install)
- A simplified and deterministic way to manage listeners (ObservableValue::when)

### Early releases

JavaFX Script, the scripting component of JavaFX, began life as a project by Chris Oliver called F3.

Sun Microsystems first announced JavaFX at the JavaOne Worldwide Java Developer conference in May 2007.

In May 2008 Sun Microsystems announced plans to deliver JavaFX for the browser and desktop by the third quarter of 2008, and JavaFX for mobile devices in the second quarter of 2009. Sun also announced a multi-year agreement with On2 Technologies to bring comprehensive video capabilities to the JavaFX product family using the company's TrueMotion Video codec. Since end of July 2008, developers could download a preview of the JavaFX SDK for Windows and Macintosh, as well as the JavaFX plugin for NetBeans 6.1.

Major releases since JavaFX 1.1 have a release name based on a street or neighborhood in San Francisco. Update releases typically do not have a release name.

On December 4, 2008, Sun released JavaFX 1.0.2.

JavaFX for mobile development was finally made available as part of the JavaFX 1.1 release (named Franca) announced officially on February 12, 2009.

JavaFX 1.2 (named Marina) was released at JavaOne on June 2, 2009. This release introduced:

- Beta support for Linux and Solaris
- Built-in controls and layouts
- Skinnable CSS controls
- Built-in chart widgets
- JavaFX I/O management, masking differences between desktop and mobile devices
- Speed improvements
- Windows Mobile Runtime with Sun Java Wireless Client

JavaFX 1.3 (named Soma) was released on April 22, 2010. This release introduced:

- Performance improvements
- Support of additional platforms
- Improved support for user interface controls

JavaFX 1.3.1 was released on August 21, 2010. This release introduced:

- Quick startup time of JavaFX application
- Custom progress bar for application startup

JavaFX 2.0 (named Presidio) was released on October 10, 2011. This release introduced:

- A new set of Java APIs opening JavaFX capabilities to all Java developers, without the need for them to learn a new scripting language. JavaFX Script support was dropped permanently.
- Support for high performance lazy binding, binding expressions, bound sequence expressions, and partial bind re-evaluation.
- Dropping support for JavaFX Mobile.
- Oracle announcing its intent to open-source JavaFX.
- JavaFX runtime turning to be platform-specific, utilizing system capabilities, as video codec available on the system; instead of implementing only one cross-platform runtime as with JavaFX 1.x.

Various improvements have been made within the JavaFX libraries for multithreading. The Task APIs have been updated to support much more concise threading capabilities (i.e. the JavaTaskBase class is no longer necessary since all the APIs are in Java, and the requirement to have a callback interface and Java implementation class are no longer necessary). In addition, the scene graph has been designed to allow scenes to be constructed on background threads and then attached to "live" scenes in a threadsafe manner.

On May 26, 2011, Oracle released the JavaFX 2.0 Beta. The beta release was only made available for 32 and 64 bit versions of Microsoft Windows XP, Windows Vista and Windows 7. An Early Access version for Mac OS X was also available for members of the JavaFX Partner Program at the time, while Linux support was planned for a future release of JavaFX. JavaFX 2.0 was released with only Windows support. Mac OS X support was added with JavaFX 2.1. Linux support was added with JavaFX 2.2.

JavaFX 2.0 makes use of a new declarative XML language called FXML.

On April 27, 2012, Oracle released version 2.1 of JavaFX, which includes the following main features:

- First official version for OS X (desktop only)
- H.264/MPEG-4 AVC and Advanced Audio Coding support
- CoolType text
- UI enhancements including combo box controls, charts (stacked chart), and menu bars
- Webview component now allows JavaScript to make calls to Java methods

On August 14, 2012, Oracle released version 2.2 of JavaFX, which includes the following main features:

- Linux support (including plugin and webstart)
- Canvas
- New controls: Color Picker, Pagination
- HTTP Live Streaming support
- Touch events and gestures
- Image manipulation API
- Native Packaging

JavaFX 2.2 adds new packaging option called Native Packaging, allowing packaging of an application as a "native bundle". This gives users a way to install and run an application without any external dependencies on a system JRE or FX SDK.

As of Oracle Java SE 7 update 6 and JavaFX 2.2, JavaFX is bundled to be installed with Oracle Java SE platform.

### Future work

Oracle also announced in November 2012 the open sourcing of Decora, a DSL Shader language for JavaFX allowing to generate Shaders for OpenGL and Direct3D.

Oracle wrote in its Client Support Roadmap that JavaFX new fixes will continue to be supported on Java SE 8 through March 2025. Previously, Oracle announced that they are "working with interested third parties to make it easier to build and maintain JavaFX as a separately distributable open-source module." JavaFX will continue to be supported in the future by the company Gluon as a downloadable module in addition to the JDK.

## Availability

As of March 2014 JavaFX is deployed on Microsoft Windows, OS X, and Linux. Oracle has an internal port of JavaFX on iOS and Android. Support for ARM is available starting with JavaFX 8 On February 11, 2013, Richard Bair, chief architect of the Client Java Platform at Oracle, announced that Oracle would open-source the iOS and Android implementations of its JavaFX platform in the next two months.

Starting with version 8u33 of JDK for ARM, support for JavaFX Embedded has been removed.

Support will continue for x86-based architectures.

A commercial port of JavaFX for Android and iOS has been created under the name "Gluon".

## License

There are various licenses for the previous modules that used to compose the JavaFX runtime:

- The JavaFX compiler and an older version of the 2D Scene graph are released under a GPL v2 license,
- The NetBeans plugin for JavaFX is dual licensed under GPL v2 and CDDL.

During development, Sun explained they will roll out their strategy for the JavaFX licensing model for JavaFX first release. After the release in 2008, Jeet Kaul, Sun's Vice president for Client Software, explained that they will soon publish a specification for JavaFX and its associated file formats, and will continue to open-source the JavaFX runtime, and decouple this core from the proprietary parts licensed by external parties.

At JavaOne 2011, Oracle Corporation announced that JavaFX 2.0 would become open-source. Since December 2011, Oracle began to open-source the JavaFX code under the GPL+linking exception.

In December 2012, new portions of the JavaFX source code were open-sourced by Oracle:

- the animations and timelines classes
- the event delivery mechanism and other various core classes
- the render tree interface, and the implementation of this interface
- the geometry and shapes implementation
- the Java part of the rendering engine used in the rendering pipeline
- the logging support
