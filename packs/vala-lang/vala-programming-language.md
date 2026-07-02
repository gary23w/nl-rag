---
title: "Vala (programming language)"
source: https://en.wikipedia.org/wiki/Vala_(programming_language)
domain: vala-lang
license: CC-BY-SA-4.0
tags: vala language, vala lang, gobject vala, gnome vala
fetched: 2026-07-02
---

# Vala (programming language)

**Vala** is an object-oriented programming language with a self-hosting compiler that generates an intermediate representation in C source code and uses the GObject system. It is free and open-source software released with a GNU Lesser General Public License (LGPL) version 2.1+.

Vala is syntactically similar to C# and includes notable features such as anonymous functions, signals, properties, generics, assisted memory management, exception handling, type inference, and foreach statements. Its developers, Jürg Billeter and Raffaele Sandrini, wanted to bring these features to the plain C runtime with little overhead and no special runtime support by targeting the GObject object system. Rather than compiling directly to machine code or assembly language, it compiles to a lower-level intermediate language. It transpiles to C, which is then compiled with a C compiler for a given platform, such as GNU Compiler Collection (GCC) or Clang.

Using functions from native code libraries requires writing vapi files, defining the library interfaces. Writing these interface definitions is well-documented for C libraries. Bindings are already available for many libraries, including some not based on GObject such as the multimedia library Simple DirectMedia Layer (SDL) and OpenGL.

## Description

Vala is a programming language that combines the high-level build-time performance of scripting languages with the run-time performance of low-level programming languages. It aims to bring modern programming language features to GNOME without imposing added runtime requirements and without using a different application binary interface (ABI), compared to applications and libraries written in C. The syntax of Vala is similar to C#, modified to better fit the GObject type system.

## History

Vala was conceived by Jürg Billeter and was implemented by him and Raffaele Sandrini, who wished for a higher-level alternative for developing GNOME applications instead of C. They liked the syntax and semantics of C# but did not want to use Mono, so they finished a compiler in May 2006. Initially, it was bootstrapped using C, and one year later (with release of version 0.1.0 in July 2007), the Vala compiler became self-hosted. In 2008, the Genie language was created to expose a Python-like syntax to the Vala compiler. As of 2021, the current stable release branch with long-term support is 0.48, and the language is under active development with the goal of releasing a stable version 1.0.

| Version | Release date | Remarks |
|---|---|---|
| Unsupported: 0.0.1 | 2006-07-15 |   |
| Unsupported: 0.1.0 | 2007-07-09 |   |
| Unsupported: 0.10.0 | 2010-09-18 |   |
| Unsupported: 0.20.0 | 2013-05-27 |   |
| Unsupported: 0.30.0 | 2015-09-18 |   |
| Unsupported: 0.40.0 | 2018-05-12 | Stable Long-term Support |
| Unsupported: 0.42.0 | 2018-09-01 |   |
| Unsupported: 0.44.0 | 2019-05-09 |   |
| Unsupported: 0.46.0 | 2019-09-05 |   |
| Unsupported: 0.48.0 | 2020-03-03 | Stable Long-term Support |
| Unsupported: 0.50.0 | 2020-09-10 |   |
| Unsupported: 0.52.0 | 2021-05-17 |   |
| Unsupported: 0.54.0 | 2021-09-16 |   |
| Supported: 0.40.25 | 2021-01-11 | Stable Long-term Support |
| Unsupported: 0.56.0 | 2022-03-17 | Stable Long-term Support |
| Supported: 0.48.25 | 2022-09-16 | Stable Long-term Support |
| Latest version: 0.56.17 | 2024-04-19 | Stable Long-term Support |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |
| For old versions, only first point releases are listed |   |   |

## Language design

### Features

Vala uses GLib and its submodules (GObject, GModule, GThread, GIO) as the core library, which is available for most operating systems and offers things like platform independent threading, input/output, file management, network sockets, plugins, regular expressions, etc. The syntax of Vala currently supports modern language features as follows:

- Interfaces
- Properties
- Signals
- Foreach
- Lambda expressions
- Type inference for local variables
- Generics
- Non-null types
- Assisted memory management
- Exception handling

Graphical user interfaces can be developed with the GTK GUI toolkit and the Glade GUI builder.

### Memory management

For memory management, the GType or GObject system provides reference counting. In C, a programmer must manually manage adding and removing references, but in Vala, managing such reference counts is automated if a programmer uses the language's built-in reference types rather than plain pointers. The only detail one needs to worry about is to avoid generating reference cycles, because in that case this memory management system will not work correctly.

Vala also allows manual memory management with pointers as an option.

### Bindings

Vala is intended to provide runtime access to existing C libraries, especially GObject-based libraries, without the need for runtime bindings. To use a library with Vala, all that is needed is an API file (.vapi) containing the class and method declarations in Vala syntax. However, C++ libraries are not supported. At present, vapi files for a large part of the GNU project and GNOME platform are included with each release of Vala, including GTK. There is also a library named Gee, written in Vala, that provides GObject-based interfaces and classes for commonly used data structures.

It should also be easily possible to write a bindings generator for access to Vala libraries from applications written in other languages, e.g., C#, as the Vala parser is written as a library, so that all compile-time information is available when generating a binding.

## Tools

### Editors

Tooling for Vala development has seen significant improvement over the recent years. The following is a list of some popular IDEs and text editors with plug-ins that add support for programming in Vala:

- GNOME Builder
- Visual Studio Code, with Vala plugin
- Vim, with arrufat/vala.vim plugin
- Emacs, with vala-mode
- Atom
- Geany

### Code intelligence

Currently, there are two actively developing language servers which offer code intelligence for Vala as follows:

- vala-lang/vala-language-server, designed for any editor that supports LSP, including VSCode, vim, and GNOME Builder
- esodan/gvls, currently the default language server for Vala in GNOME Builder and provides support to any editor with support for LSP

### Build systems

Currently, there are a number of build systems supporting Vala, including Automake, CMake, Meson, and others.

### Debugging

Debugging for Vala programs can be done with either GDB or LLDB. For debugging in IDEs,

- GNOME Builder has built-in debugging support for Vala with GDB.
- Visual Studio Code has extensions for GDB and LLDB, such as cpptools and CodeLLDB.

## Examples

### Hello world

Simple "Hello, World!" program in Vala:

```mw
void main() {
	print("Hello World\n");
}
```

As can be noted, unlike C or C++, there are no header files in Vala. The linking to libraries is done by specifying `--pkg` parameters during compiling. Moreover, the GLib library is always linked and its namespace can be omitted (`print` is in fact `GLib.print`).

### Object-oriented programming

Below is a more complex version which defines a subclass `HelloWorld` inheriting from the base class `GLib.Object`, aka the GObject class. It shows some of Vala's object-oriented features:

```mw
class HelloWorld: Object {
	private uint year = 0;
	
	public HelloWorld() {
	}
	
	public HelloWorld.with_year(int year) {
		if (year > 0)
			this.year = year;
	}

	public void greeting() {
		if (year == 0)
			print("Hello World\n");
		else
			/* Strings prefixed with '@' are string templates. */
			print(@"Hello World, $(this.year)\n"); 
	}
}

void main (string[] args) {
	var helloworld = new HelloWorld.with_year(2021);
	helloworld.greeting();
}
```

As in the case of GObject library, Vala does not support multiple inheritance, but a class in Vala can implement any number of interfaces, which may contain default implementations for their methods. Here is a piece of sample code to demonstrate a Vala interface with default implementation (sometimes referred to as a mixin)

```mw
using GLib;

interface Printable {
	public abstract string print();

	public virtual string pretty_print() {
		return "Please " + print();
	}
}

class NormalPrint: Object, Printable {
	string print() {
		return "don't forget about me";
	}
}

class OverridePrint: Object, Printable {
	string print() {
		return "Mind the gap";
	}

	public override string pretty_print() {
		return "Override";
	}
}

void main(string[] args) {
	var normal = new NormalPrint();
	var overridden = new OverridePrint();

	print (normal.pretty_print());
	print (overridden.pretty_print());
}
```

### Signals and callbacks

Below is a basic example to show a signal defined in a class that is not compact, which has a signal system built in by Vala through GLib. Then callback functions are registered to the signal of an instance of the class. The instance can emit the signal and each callback function (also referred to as handler) connected to the signal for the instance will get invoked in the order they were connected in:

```mw
class Foo {
    public signal void some_event();   // definition of the signal

    public void method() {
        some_event();                  // emitting the signal (callbacks get invoked)
    }
}

void callback_a() {
    stdout.printf("Callback A\n");
}

void callback_b() {
    stdout.printf("Callback B\n");
}

void main() {
    var foo = new Foo();
    foo.some_event.connect(callback_a);      // connecting the callback functions
    foo.some_event.connect(callback_b);
    foo.method();
}
```

### Threading

A new thread in Vala is a portion of code such as a function that is requested to be executed concurrently at runtime. The creation and synchronization of new threads are done by using the `Thread` class in GLib, which takes the function as a parameter when creating new threads, as shown in the following (very simplified) example:

```mw
int question(){
    // Some print operations 
    for(var i = 0; i < 3; i++){
        print(".");
        Thread.usleep(800000);
        stdout.flush();
    }

    return 42;
}

void main() {
    if (!Thread.supported()) {
        stderr.printf("Cannot run without thread support.\n");
        return;
    }
    print("The Ultimate Question of Life, the Universe, and Everything");
    // Generic parameter is the type of return value
    var thread = new Thread<int>("question", question);

    print(@" $(thread.join())\n");
}
```

### Graphical user interface

Below is an example using GTK to create a GUI "Hello, World!" program (see also GTK hello world) in Vala:

```mw
using Gtk;

int main(string[] args) {
	Gtk.init(ref args);

	var window = new Window();
	window.title = "Hello, World!";
	window.border_width = 10;
	window.window_position = WindowPosition.CENTER;
	window.set_default_size(350, 70);
	window.destroy.connect(Gtk.main_quit);

	var label = new Label("Hello, World!");

	window.add(label);
	window.show_all();

	Gtk.main();
	return 0;
}
```

The statement `Gtk.main()` creates and starts a main loop listening for events, which are passed along via signals to the callback functions. As this example uses the GTK package, it needs an extra `--pkg` parameter (which invokes pkg-config in the C backend) to compile:

```mw
valac --pkg gtk+-3.0 hellogtk.vala
```
