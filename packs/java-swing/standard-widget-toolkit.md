---
title: "Standard Widget Toolkit"
source: https://en.wikipedia.org/wiki/Standard_Widget_Toolkit
domain: java-swing
license: CC-BY-SA-4.0
tags: java swing, swing components, pluggable look and feel, lightweight java widgets
fetched: 2026-07-02
---

# Standard Widget Toolkit

The **Standard Widget Toolkit** (**SWT**) is a graphical widget toolkit for use with the Java platform. It was originally developed by Stephen Northover at IBM and is now maintained by the Eclipse Foundation in tandem with the Eclipse IDE. It is an alternative to the Abstract Window Toolkit (AWT) and Swing Java graphical user interface (GUI) toolkits provided by Sun Microsystems as part of the Java Platform, Standard Edition (J2SE).

To display GUI elements, the SWT implementation accesses the native GUI libraries of the operating system using Java Native Interface (JNI) in a manner that is similar to those programs written using operating system-specific application programming interfaces (APIs). Programs that call SWT are portable, but the implementation of the toolkit, despite part of it being written in Java, is unique for each platform.

The toolkit is free and open-source software distributed under the Eclipse Public License, which is approved by the Open Source Initiative.

## History

The first Java GUI toolkit was the Abstract Window Toolkit (AWT), introduced with Java Development Kit (JDK) 1.0 as one component of Sun Microsystems' Java platform. The original AWT was a simple Java wrapper library around native (operating system-supplied) widgets such as menus, windows, and buttons.

Swing was the next generation GUI toolkit introduced by Sun in Java Platform, Standard Edition (J2SE) 1.2. Swing was developed to provide a richer set of GUI software components than AWT. Swing GUI elements are all-Java with no native code: instead of wrapping native GUI components, Swing draws its own components by using Java 2D to call low-level operating system drawing routines.

The roots of SWT go back to work that Object Technology International (OTI), did in the 1990s when creating multiplatform, portable, native widget interfaces for Smalltalk, originally for OTI Smalltalk, which became IBM Smalltalk in 1993. IBM Smalltalk's Common Widget layer provided fast, native access to multiple platform widget sets while still providing a common API without suffering the *lowest common denominator* problem typical of other portable graphical user interface (GUI) toolkits. IBM was developing VisualAge, an integrated development environment (IDE) written in Smalltalk. They decided to open-source the project, which led to the development of Eclipse, intended to compete against other IDEs such as Microsoft Visual Studio. Eclipse is written in Java, and IBM developers, deciding that they needed a toolkit that had "native look and feel" and "native performance", created SWT as a Swing replacement.

## Design

SWT is a wrapper around native code objects, such as GTK objects, Motif objects etc. Because of this, SWT widgets are often referred to as "heavyweight", evoking images of a light Java wrapper around a "heavy" native object. In cases where native platform GUI libraries do not support the functionality required for SWT, SWT implements its own GUI code in Java, similar to Swing. In essence, SWT is a compromise between the low-level performance and look and feel of AWT and the high-level ease of use of Swing.

According to the Eclipse Foundation, "SWT and Swing are different tools that were built with different goals in mind. The purpose of SWT is to provide a common API for accessing native widgets across a spectrum of platforms. The primary design goals are high performance, native look and feel, and deep platform integration. Swing, on the other hand, is designed to allow for a highly customizable look and feel that is common across all platforms."

It has been argued that SWT features a clean design, in part inspired by Erich Gamma of Design Patterns fame.

SWT is a simpler toolkit than Swing, with less (possibly) extraneous functionality for the average developer. This has led some people to argue that SWT lacks functionality when compared to Swing.

James Gosling, the creator of the Java language, has argued that SWT is too simple, and is a difficult toolkit to port to new platforms for the same reason that AWT once had porting problems: that it is too simple, too low level, and too tied to the Win32 GUI API, leading to problems adapting the SWT API to other GUI toolkits, such as Motif and OS X Carbon.

Although SWT does not implement the popular model–view–controller (MVC) architecture used in Swing and multiple other high-level GUI toolkits, the JFace library, which is developed as part of the same Eclipse project, does provide a cross-platform, higher-level MVC abstraction atop SWT. Developers may choose to use JFace to provide more flexible and abstract data models for complex SWT controls such as trees, tables, and lists, or access those controls directly as needed.

### Look and feel

SWT widgets have the same *look and feel* as native widgets because they often are the same native widgets. This is in contrast to the Swing toolkit where all widgets are emulations of native widgets. In some cases the difference is distinguishable. For example, the macOS tree widget features a subtle animation when a tree is expanded and default buttons have an animated pulsing glow to focus the user's attention on them. The default Swing version of these widgets does not animate.

Since SWT is simply a wrapper around native GUI code, it does not require large numbers of updates when that native code is changed, providing that operating system vendors are careful not to break clients of their API when the operating systems are updated. The same cannot be said of Swing, which supports the ability to change the look and feel of the running application with "pluggable looks and feels". These enable emulating the native platform user interface using themes, which must be updated to mirror operating system GUI changes, such as theme or other look and feel updates.

SWT aims for "deep platform integration", the Eclipse reference to SWT's use of native widgets. According to Mauro Marinillia of developer.com, "whenever one needs a tight integration with the native platform, SWT can be a plus". This deep integration can be useful in a number of ways, for example enabling SWT to wrap ActiveX objects on Microsoft Windows.

### Programming

The following is a basic "Hello, World!" program using SWT. It shows a window (*Shell*) and a label.

```mw
import org.eclipse.swt.*;
import org.eclipse.swt.widgets.*;

public class HelloWorld
{
   public static void main (String[] args)
   {
      Display display = new Display();
      Shell shell = new Shell(display);
      Label label = new Label(shell, SWT.NONE);
      label.setText("Hello, World!");
      label.pack();
      shell.pack();
      shell.open();
      while (!shell.isDisposed())
      {
         if (!display.readAndDispatch()) display.sleep();
      }
      display.dispose();
   }
}
```

Contrary to Swing, a *Display* class is necessary to access the underlying operating system, and its resources must be explicitly disposed of when they are no longer used.

### Platform support

SWT must be ported to every new GUI library that needs supporting. Unlike Swing and AWT, SWT is not available on every Java-supported platform since SWT is not part of the Java release. There is also some evidence that the performance of SWT on platforms other than Windows is noticeably less efficient. Since SWT uses a different native library for each platform, SWT programs may be exposed to platform-specific bugs.

SWT exposes programs to more low-level details than Swing. This is because SWT is technically just a layer over native library provided GUI functionality, exposing the programmer to native GUI code is part of the design intent of SWT: "Its goal is not to provide a rich user-interface design framework but rather the thinnest possible user-interface API that can be implemented uniformly on the largest possible set of platforms while still providing sufficient functionality to build rich graphical user interface (GUI) applications."

Since the SWT implementation is different for each platform, a platform-specific SWT library (JAR file) must be distributed with each application.

As of 2018, SWT supports these platforms and/or GUI libraries:

- Windows:
  - Win32
  - Windows Presentation Foundation (WPF), under development
- Unix-like: Linux, FreeBSD:
  - GTK
- macOS:
  - Cocoa

As of March 2018, SWT 4.7.3a (and 4.8M6) is officially compatible with the following operating systems (graphic library or similar if explicitly required / processors):

- Microsoft Windows (x86 and x86_64)
- Linux (GTK / PPC64 and PPC64LE)
- macOS (Cocoa / x86_64)

Windows XP has historically been supported, as have Linux on s390, Solaris 11 (SPARCv9), Solaris 10 (x86_64), HP-UX (ia64), and AIX (PPC and PPC64).

### Performance

SWT was designed to be a *high performance* GUI toolkit; faster, more responsive and lighter on system resource usage than Swing.

There has been some attempted benchmarking of SWT and Swing, which concluded that SWT should be more efficient than Swing, although the applications benchmarked in this case were not complex enough to draw solid conclusions for all possible SWT or Swing uses. A fairly thorough set of benchmarks concluded that neither Swing nor SWT outperformed the other in the general case.

### Extensibility and comparison to other Java code

Due to the use of native code, SWT classes do not allow for easy inheritance for all widget classes, which some users consider can hurt extensibility. This can make customizing existing widgets more difficult to achieve with SWT than if one were using Swing. Both toolkits support writing new widgets using only Java code, however in SWT extra work is needed to make the new widget work on every platform.

SWT widgets, unlike almost any other Java toolkit, requires manual object deallocation, in contrast to the standard Java practice of automatic garbage collection. SWT objects must be explicitly deallocated using the `dispose` method, which is analogous to the C language's `free`. If this is not done, memory leaks or other unintended behavior may result. On this matter, some have commented that "explicitly de-allocating the resources could be a step back in development time (and costs) at least for the average Java developer" and that "this is a mixed blessing. It means more control (and more complexity) for the SWT developer instead of more automation (and slowness) when using Swing." The need for manual object deallocation when using SWT is largely due to SWT's use of native objects. These objects are not tracked by the Java JVM, so it cannot track whether or not such objects are in use, and thus cannot garbage collect them at a suitable time.

## Development

There is some development activity to enable combining Swing and SWT. Two different approaches are being attempted:

- *SwingWT* is a project to provide an alternative Swing implementation. It uses an SWT back end to display its widgets, thus providing the native look and feel and performance advantages of SWT along with the same programming model as Swing.
- *SWTSwing* is a project to provide a Swing back end for SWT. In effect, SWT could be run using *Swing native objects* instead of, for example, GTK or Windows native objects. This would enable SWT to work on every platform that Swing supports.

Starting in 2006, there was an SWT-3.2 port to the programming language D called DWT. Since then, the project supports Windows 32-bit, and Linux GTK 32-bit for SWT-3.4. The DWT project also has an addon package that contains a port of JFace and Eclipse Forms.

With JavaFX becoming part of the Java SE platform there has been interest in developing a backend for SWT that relies on JavaFX in a similar way to SWTSwing relies on Swing. A prominent project trying to achieve that was *SWT on JavaFX* which became part of *e(fx)clipse* in 2014.

## Uses

Applications (alphabetically sorted) using SWT include:

- Apache Directory Studio, an LDAP browser–editor
- Eclipse and its plug-ins
- GumTree Platform, scientific workbench
- Haystack, information manager
- IBM Rational Software products: Rational Application Developer, Rational Software Architect, Rational Team Concert and others.
- IBM Lotus Software products: Notes, Sametime, Symphony, and Expeditor
- Studio 3T, GUI client for MongoDB database
- RSSOwl, feed aggregator
- SmartGit, a Git, Mercurial, and Apache Subversion (SVN) client
- TuxGuitar, an open-source tablature editor
- uDig, GIS tool
- Vuze, formerly named Azureus

Recent open-source efforts in the Eclipse community have led to a porting of SWT (and JFace) into a widget toolkit appropriate for the web. The result has been the Eclipse Remote Application Platform (RAP), which combines the qooxdoo Ajax library with the SWT API. Like other Java Ajax projects (such as Echo2, Vaadin and Google Web Toolkit), the usage of the SWT API allows developing applications quickly for the web in much the same way as for the desktop.
