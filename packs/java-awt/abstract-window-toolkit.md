---
title: "Abstract Window Toolkit"
source: https://en.wikipedia.org/wiki/Abstract_Window_Toolkit
domain: java-awt
license: CC-BY-SA-4.0
tags: abstract window toolkit, java awt, native peer widgets, heavyweight components
fetched: 2026-07-02
---

# Abstract Window Toolkit

The **Abstract Window Toolkit** (**AWT**) is Java's original platform-dependent windowing, graphics, and user-interface widget toolkit, preceding Swing. The AWT is part of the Java Foundation Classes (JFC) — the standard API for providing a graphical user interface (GUI) for a Java program. AWT is also the GUI toolkit for a number of Java ME profiles. For example, Connected Device Configuration profiles require Java runtimes on mobile telephones to support the Abstract Window Toolkit.

## History

When Sun Microsystems first released Java in 1995, AWT widgets provided a thin level of abstraction over the underlying native user-interface. For example, creating an AWT check box would cause AWT directly to call the underlying native subroutine that created a check box. However, the check box on Windows is not the same as the check box on macOS or on the various types of Unix. Some application developers prefer this model because it provides a high degree of fidelity to the underlying native windowing toolkit and seamless integration with native applications. In other words, a GUI program written using AWT looks like a native Microsoft Windows application when run on Windows, but the same program looks like a native Apple Macintosh application when run on a Mac, etc. However, some application developers dislike this model because they prefer their applications to look exactly the same on every platform.

In J2SE 1.2, the Swing toolkit largely superseded the AWT's widgets. In addition to providing a richer set of UI widgets, Swing draws its own widgets (by using Java 2D to call into low-level subroutines in the local graphics subsystem) instead of relying on the operating system's high-level user interface module. Swing provides the option of using either the native platform's "look and feel" or a cross-platform look and feel (the "Java Look and Feel") that looks the same on all windowing systems.

## Architecture

The AWT provides two levels of APIs:

- A general interface between Java and the native system, used for windowing, events, and layout managers. This API is at the core of Java GUI programming and is also used by Swing and Java 2D. It contains:
  - The interface between the native windowing system and the Java application;
  - The core of the GUI event subsystem;
  - Several layout managers;
  - The interface to input devices such as mouse and keyboard; and
  - A `java.awt.datatransfer` package for use with the Clipboard and Drag and Drop.
- A basic set of GUI widgets such as buttons, text boxes, and menus. It also provides the AWT Native Interface, which enables rendering libraries compiled to native code to draw directly to an AWT `Canvas` object drawing surface.

AWT also makes some higher level functionality available to applications, such as:

- Access to the system tray on supporting systems; and
- The ability to launch some desktop applications such as web browsers and email clients from a Java application.

Neither AWT nor Swing is inherently thread safe. Therefore, code that updates the GUI or processes events should execute on the Event dispatching thread. Failure to do so may result in a deadlock or race condition. To address this problem, a utility class called SwingWorker allows applications to perform time-consuming tasks following user-interaction events in the event dispatching thread.

## Mixing AWT and Swing components

Where there is a Swing version of an AWT component it will begin with J- and should be used exclusively, replacing the AWT version. For example, in Swing, only use JButton, never Button class. As mentioned above, the AWT core classes, such as Color and Font, are still used as-is in Swing.

When drawing in Swing, use JPanel and override paintComponent(Graphics g) instead of using the AWT paint() methods.

Before Java 6 Update 12, mixing Swing components and basic AWT widgets often resulted in undesired side effects, with AWT widgets appearing on top of the Swing widgets regardless of their defined z-order. This problem was because the rendering architecture of the two widget toolkits was very different, despite Swing borrowing heavyweight top containers from AWT.

Starting in Java 6 Update 12, it is possible to mix Swing and AWT widgets without having z-order problems.

## Example

```mw
package org.wikipedia.examples;

import java.awt.Frame;
import java.awt.Label;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MyApp {

    public static void main(String[] args) {
        Frame frame = new Frame("Application");
        
        frame.add(new Label("Hello!"));
        frame.setSize(500, 500);
        frame.setLocationRelativeTo(null); // Centers the window
        
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                frame.dispose(); // Releases native screen resources
            }
        });
        
        frame.setVisible(true);
    }
}
```

## Implementation

As the AWT is a bridge to the underlying native user-interface, its implementation on a new operating system may involve a lot of work, especially if it involves any of the AWT GUI widgets, because each of them requires that its native peers be developed from scratch.

A new project, Caciocavallo, has been created, that provides an OpenJDK-based Java API to ease AWT implementation on new systems. The project has successfully implemented AWT widgets using Java2D. All the necessary core-JDK modifications have since been pushed to OpenJDK 7, which means that Java can now be used on a graphics stack other than one of those provided by the official JDK (X Window System, OpenGL or DirectX), by including an external library and setting some system properties. A DirectFB backend for Caciocavallo is under development, as is an HTML5 backend; the aim is to deploy existing Swing applications—without Java support—as ordinary web applications running on a web server.
