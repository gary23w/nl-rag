---
title: "Projects/Vala/Tutorial (part 3/3)"
source: https://wiki.gnome.org/Projects/Vala/Tutorial
domain: vala-lang
license: CC-BY-SA-4.0
tags: vala language, vala lang, gobject vala, gnome vala
fetched: 2026-07-02
part: 3/3
---

# Projects/Vala/Tutorial

If the direct call above is used, then the resumed asynchronous method takes control of the CPU immediately and runs until its next yield before returning to the code that executed callback(). The Idle.add() method is useful if the callback must be made from a background thread, e.g. to resume the async method after completion of some background processing. (The (owned) cast is necessary to avoid a warning about copying delegates.)

The third common way of using yield is when calling another asynchronous method, for example:

yield display_jpeg(fnam);

or

var status = yield fetch_webpage(url, out text);

In both cases, the calling method gives up control of the CPU and does not resume until the called method completes. The yield statement automatically registers a callback with the called method to make sure that the caller resumes correctly. The automatic callback also collects the return value from the called method.

When this yield statement executes, control of the CPU first passes to the called method which runs until its first yield and then drops back to the calling method, which completes the yield statement itself, and then gives back control to its own caller.

Examples

See Async Method Samples for examples of different ways that async may be used.

Weak References

Vala's memory management is based on automatic reference counting. Each time an object is assigned to a variable its internal reference count is increased by 1, each time a variable referencing an object goes out of scope its internal reference count is decreased by 1. If the reference count reaches 0 the object will be freed.

However, it is possible to form a reference cycle with your data structures. For example, with a tree data structure where a child node holds a reference to its parent and vice versa, or a doubly-linked list where each element holds a reference to its predecessor and the predecessor holds a reference to its successor.

In these cases objects could keep themselves alive simply by referencing to each other, even though they should be freed. To break such a reference cycle you can use the weak modifier for one of the references:

class Node { public weak Node prev; public Node next; }

This topic is explained in detail on this page: Vala's Memory Management Explained.

Ownership

Unowned References

Normally when creating an object in Vala you are returned a reference to it. Specifically this means that as well as being passed a pointer to the object in memory, it is also recorded in the object itself that this pointer exists. Similarly, whenever another reference to the object is created, this is also recorded. As an object knows how many references there are to it, it can automatically be removed when needed. This is the basis of Vala's memory management.

Methods ownership

*Unowned references* conversely are not recorded in the object they reference. This allows the object to be removed when it logically should be, regardless of the fact that there might be still references to it. The usual way to achieve this is with a method defined to return an unowned reference, e.g.:

class Test { private Object o; public unowned Object get_unowned_ref() { this.o = new Object(); return this.o; } }

When calling this method, in order to collect a reference to the returned object, you must expect to receive a weak reference:

unowned Object o = get_unowned_ref();

The reason for this seemingly over complicated example because of the concept of ownership. If the Object "o" was not stored in the class, then when the method "get_unowned_ref" returned, "o" would become unowned (i.e. there would be no references to it). If this were the case, the object would be deleted and the method would never return a valid reference. If the return value was not defined as unowned, the ownership would pass to the calling code. The calling code is, however, expecting an unowned reference, which cannot receive the ownership.

If the calling code is written as Object o = get_unowned_ref();

Vala will try to either obtain a reference of or a duplicate of the instance the unowned reference pointing to.

Properties ownership

In contrast to normal methods, properties always have unowned return value. That means you can't return a new object created within the get method. That also means, you can't use an owned return value from a method call. The somewhat irritating fact is because of that a property value is owned by the object that HAS this property. A call to obtain this property value should not steal or reproduce (by duplicating, or increasing the reference count of) the value from the object side.

As such, the following example will result in a compilation error

public Object property { get { return new Object(); } }

nor can you do this

public string property { get { return getter_method(); } } public string getter_method() { return "some text"; }

on the other hand, this is perfectly fine

public string property { get { return getter_method(); } } public unowned string getter_method() { return "some text"; }

The unowned modifier can be used to make automatic property's storage unowned. That means

public unowned Object property { get; private set; }

is identical to

private unowned Object _property; public Object property { get { return _property; } }

The keyword owned can be used to specifically ask a property to return a owned reference of the value, therefore causing the property value be reproduced in the object side. Think twice before adding the owned keyword. Is it a property or simply a get_xxx method? There may also be problems in your design. Anyways, the following code is a correct segment,

public owned Object property { owned get { return new Object(); } }

Unowned references play a similar role to pointers which are described later. They are however much simpler to use than pointers, as they can be easily converted to normal references. However, in general they should not be widely used in the programs unless you know what you are doing.

Ownership Transfer

The keyword owned is used to transfer ownership. As a prefix of a parameter type, it means that ownership of the object is transferred into this code context. As an type conversion operator, it can be used to avoid duplicating non-reference counting classes, which is usually impossible in Vala. For example,

Foo foo = (owned) bar;

This means that *bar* will be set to *null* and *foo* inherits the reference/ownership of the object *bar* references.

Variable-Length Argument Lists

Vala supports C-style variable-length argument lists ("varargs") for methods. They are declared with an ellipsis ("...") in the method signature. A method with varargs requires at least one fixed argument:

void method_with_varargs(int x, ...) { var l = va_list(); string s = l.arg(); int i = l.arg(); stdout.printf("%s: %d\n", s, i); }

In this example x is a fixed argument to meet the requirements. You obtain the varargs list with va_list(). Then you can retrieve the arguments one after another by calling the generic method arg<T>() sequently on this list, with T being the type that the argument should be interpreted as. If the type is evident from the context (as in our example) the type is inferred automatically and you can just call arg() without the generic type argument.

This example parses an arbitrary number of *string - double* argument pairs:

void method_with_varargs(int fixed, ...) { var l = va_list(); while (true) { string? key = l.arg(); if (key == null) { break; } double val = l.arg(); stdout.printf("%s: %g\n", key, val); } } void main() { method_with_varargs(42, "foo", 0.75, "bar", 0.25, "baz", 0.32); }

It checks for *null* as a sentinel to recognize the end of the varargs list. Vala always implicitly passes *null* as the last argument of a varargs method call.

Varargs have a serious drawback that you should be aware of: they are not type-safe. The compiler can't tell you whether you are passing arguments of the right type to the method or not. That's why you should consider using varargs only if you have a good reason, for example: providing a convenience function for C programmers using your Vala library, binding a C function. Often an array argument is a better choice.

A common pattern with varargs is to expect alternating *string - value* pairs as arguments, usually meaning *gobject property - value*. In this case you can write *property: value* instead, e.g.:

actor.animate (AnimationMode.EASE_OUT_BOUNCE, 3000, x: 100.0, y: 200.0, rotation_angle_z: 500.0, opacity: 0);

is equivalent to:

actor.animate (AnimationMode.EASE_OUT_BOUNCE, 3000, "x", 100.0, "y", 200.0, "rotation-angle-z", 500.0, "opacity", 0);

Pointers

Pointers are Vala's way of allowing manual memory management. Normally when you create an instance of a type you receive a reference to it, and Vala will take care of destroying the instance when there are no more references left to it. By requesting instead a pointer to an instance, you take responsibility for destroying the instance when it is no longer wanted, and therefore get greater control over how much memory is used.

This functionality is not necessarily needed most of the time, as modern computers are usually fast enough to handle reference counting and have enough memory that small inefficiencies are not important. The times when you might resort to manual memory management are: When you specifically want to optimise part of a program and unowned references are insufficient. When you are dealing with an external library that does not implement reference counting for memory management (probably meaning one not based on gobject.)

In order to create an instance of a type, and receive a pointer to it:

Object* o = new Object();

In order to access members of that instance:

o->method_1(); o->data_1;

In order to free the memory pointed to:

delete o;

Vala also supports the *address-of* (&) and *indirection* (*) operators known from C:

int i = 42; int* i_ptr = &i; int j = *i_ptr;

The behavior is a bit different with reference types, you can omit the address-of and indirection operator on assignment:

Foo f = new Foo(); Foo* f_ptr = f; Foo g = f_ptr; unowned Foo f_weak = f;

The usage of reference-type pointers is equivalent to the use of unowned references.

Non-Object classes

Classes defined as not being descended from *GLib.Object* are treated as a special case. They are derived directly from GLib's type system and therefore much lighter in weight. In a more recent Vala compiler, one can also implement interfaces, signals and properties with these classes.

One obvious case of using these non-*Object* classes stays in the GLib bindings. Because GLib is at a lower level than GObject, most classes defined in the binding are of this kind. Also, as mentioned before, the lighter weight of non-object classes make them useful in many practical situations (e.g. the Vala compiler itself). However the detailed usage of non-*Object* classes are outside the scope of this tutorial. Be aware that these classes are fundamentally different from structs.

D-Bus Integration

D-Bus is tightly integrated into the language and has never been easier than with Vala.

To export a custom class as a D-Bus service you just need to annotate it with the *DBus* code attribute and register an instance of this class with your local D-Bus session.

[DBus(name = "org.example.DemoService")] public class DemoService : Object { int counter; public int status; public int something { get; set; } public signal void sig1(); public void some_method() { counter++; stdout.printf("heureka! counter = %d\n", counter); sig1(); } public void some_method_sender(string message, GLib.BusName sender) { counter++; stdout.printf("heureka! counter = %d, '%s' message from sender %s\n", counter, message, sender); } }

Register an instance of the service and start a main loop:

void on_bus_aquired (DBusConnection conn) { try { var service = new DemoService(); conn.register_object ("/org/example/demo", service); } catch (IOError e) { stderr.printf ("Could not register service: %s\n", e.message); } } void main () { Bus.own_name (BusType.SESSION, "org.example.DemoService", BusNameOwnerFlags.NONE, on_bus_aquired, () => {}, () => stderr.printf ("Could not acquire name\n")); new MainLoop ().run (); }

You must compile this example with the *gio-2.0* package:

$ valac --pkg gio-2.0 dbus-demo-service.vala $ ./dbus-demo-service

All member names are automatically mangled from Vala's *lower_case_with_underscores* naming convention to D-Bus *CamelCase* names. The exported D-Bus interface of this example will have a property *Something*, a signal *Sig1* and a method *SomeMethod*. You can open a new terminal window and call the method from command line with:

$ dbus-send --type=method_call \ --dest=org.example.DemoService \ /org/example/demo \ org.example.DemoService.SomeMethod

or

$ dbus-send --type=method_call \ --dest=org.example.DemoService \ /org/example/demo \ org.example.DemoService.SomeMethodSender \ string:'hello world'

You can also use a graphical D-Bus debugger like D-Feet to browse your D-Bus interfaces and call methods.

Some comprehensive examples: DBus Client Samples and DBus Server Sample

Profiles

The generated C code can target a different minimum runtime by using valac's --profile option. Vala supports two different profiles: gobject (default) libc

A profile determines which Vala language features are available to match the minimum runtime environment. The gobject profile enables code generation that requires GLib's GType runtime type system and so the runtime environment will usually require libgobject and its small number of dependencies.

The libc profile removes the dependency on GLib and disables the runtime type system. The profile either generates alternative code or errors at compile time if a Vala language feature is used that requires the runtime type system. This is useful for writing code that targets microcontrollers or for generating binaries for system utilities or extremely small container images. The runtime environment will usually require a small subset of the ISO C standard library. The posix profile is currently an alias for libc because a POSIX compatible operating system includes the C standard library, but code generated from the profile can target non-POSIX platforms where a minimal C standard library is available for dynamic linking at runtime or statically linked in to the binary.

To select a different profile use valac's --profile switch: valac --profile=libc somecode.vala

Of course, the binary will still require the runtime dependencies needed for the libraries targeted with valac's --pkg option.

Experimental Features

Some features of Vala are experimental. This means they are not fully tested and might be subject to changes in future versions.

Chained Relational Expressions

This feature allows you to write complex relational expressions like

if (1 < a && a < 5) {} if (0 < a && a < b && b < c && c < d && d < 255) { }

in a more natural way:

if (1 < a < 5) {} if (0 < a < b < c < d < 255) { }

Regular Expression Literals

Regular expressions are a powerful technique for pattern matching in strings. Vala has experimental support for regular expression literals (/regex/). Example:

string email = "tux@kernel.org"; if (/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.match(email)) { stdout.printf("Valid email address\n"); }

The trailing *i* makes the expression case insensitive. You can store a regular expression in a variable of type *Regex*:

Regex regex = /foo/;

A example of regular expression replacement:

var r = /(foo|bar|cow)/; var o = r.replace ("this foo is great", -1, 0, "thing"); print ("%s\n", o);

The following trailing characters can be used: *i*, letters in the pattern match both upper- and lowercase letters *m*, the "start of line" and "end of line" constructs match immediately following or immediately before any newline in the string, respectively, as well as at the very start and end. *s*, a dot metacharater *.* in the pattern matches all characters, including newlines. Without it, newlines are excluded. *x*, whitespace data characters in the pattern are totally ignored except when escaped or inside a character class.

Strict Non-Null Mode

If you compile your code with --enable-experimental-non-null the Vala compiler will run in strict non-null type checking mode and consider *every* type to be not nullable by default unless it is explicitly declared nullable by marking it with a question mark:

Object o1 = new Object(); Object? o2 = new Object();

The compiler will perform a static compile-time analysis to ensure that no nullable reference is assigned to a non-nullable reference, e.g. this won't be possible:

o1 = o2;

*o2* could be *null* and *o1* was declared non-nullable, so this assignment is forbidden. However, you can override this behaviour with an explicit non-null cast if you're sure that *o2* is not *null*:

o1 = (!) o2;

The strict non-null mode helps in avoiding unwanted *null* dereferencing errors. This feature would come to full potential if the nullability of all return types in bindings was marked correctly, which is currently not always the case.

Libraries

At the system level, a Vala library is exactly a C library, and so the same tools are used. In order to make the process simpler, and so that the Vala compiler can understand the process there is then an extra level of Vala specific information.

A "Vala library" is therefore, the system part: A system library (e.g. *libgee.so*) A *pkg-config* entry (e.g. *gee-1.0.pc*)

Both of which are installed in the standard locations. And the Vala specific files: A VAPI file (e.g. *gee-1.0.vapi*) An optional dependency file (e.g. *gee-1.0.deps*)

These files are explained later in this section. It should be noted that the library names are the same in the Vala specific files as in the *pkg-config* files.

Using Libraries

Using a library in Vala is largely automated if you use the *valac* compiler. The Vala specific library files make up what is known as a package. You tell the compiler that a package is needed by your program as follows:

$ valac --pkg gee-1.0 test.vala

This command means your program can use any of the definitions in the *gee-1.0.vapi* file, and also any in any of the packages that *gee-1.0* depends on. These dependencies would be be listed in *gee-1.0.deps* if there were any. In this example *valac* is set to build all the way to binary, and will therefore incorporate information from *pkg-config* to link the correct libraries. This is why the *pkg-config* names are also used for Vala package names.

Packages are generally used with namespaces, but they are not technically related. This means that even though your application is built with reference to the package, you must still include the required using statements in each file as appropriate, or else use the fully qualified names of all symbols.

It is also possible to treat a local library (one that is not installed) as a package. For comparison, Vala itself uses an internal version of Gee. When *valac* is built it creates a VAPI file of this internal library and uses it roughly as follows:

$ valac --vapidir ../gee --pkg gee ...

For details on how to generate this library, see the next section or the example.

Creating a Library

Using Autotools

It is possible to use Autotools to create a library written in Vala. A library is created by using C code generated by Vala compiler, linked and installed as any other library. Then you need tell which C files must be used to create the library and which of them must be distributable, allowing others to compile a tarball without Vala using standard Autotools commands: **configure**, **make** and **make install**.

Example

This example was taken from GXml recent additions. GXmlDom is a library aimed to have a GObject based libxml2 replacement; is written in Vala and originally used to use WAF to build.

**valac** can be used to generate C code and headers from Vala sources. At this time is possible to generate a GObjectIntrospection and the VAPI file from the vala sources too.

**gxml.vala.stamp** is used as the code sources for our library.

Is important to add --pkg switches in order to valac to success and set all CFLAGS and LIBS required by the C library to compile and link against.

NULL = AM_CPPFLAGS = \ -DPACKAGE_LOCALE_DIR=\""$(prefix)/$(DATADIRNAME)/locale"\" \ -DPACKAGE_SRC_DIR=\""$(srcdir)"\" \ -DPACKAGE_DATA_DIR=\""$(datadir)"\" BUILT_SOURCES = gxml.vala.stamp CLEANFILES = gxml.vala.stamp AM_CFLAGS =\ -Wall\ -g \ $(GLIB_CFLAGS) \ $(LIBXML_CFLAGS) \ $(GIO_CFLAGS) \ $(GEE_CFLAGS) \ $(VALA_CFLAGS) \ $(NULL) lib_LTLIBRARIES = libgxml.la VALAFLAGS = \ $(top_srcdir)/vapi/config.vapi \ --vapidir=$(top_srcdir)/vapi \ --pkg libxml-2.0 \ --pkg gee-1.0 \ --pkg gobject-2.0 \ --pkg gio-2.0 \ $(NULL) libgxml_la_VALASOURCES = \ Attr.vala \ BackedNode.vala \ CDATASection.vala \ CharacterData.vala \ Comment.vala \ Document.vala \ DocumentFragment.vala \ DocumentType.vala \ DomError.vala \ Element.vala \ Entity.vala \ EntityReference.vala \ Implementation.vala \ NamespaceAttr.vala \ NodeList.vala \ NodeType.vala \ Notation.vala \ ProcessingInstruction.vala \ Text.vala \ XNode.vala \ $(NULL) libgxml_la_SOURCES = \ gxml.vala.stamp \ $(libgxml_la_VALASOURCES:.vala=.c) \ $(NULL) # Generate C code and headers, including GObject Introspection GIR files and VAPI file gxml-1.0.vapi gxml.vala.stamp GXml-1.0.gir: $(libgxml_la_VALASOURCES) $(VALA_COMPILER) $(VALAFLAGS) -C -H $(top_builddir)/gxml/gxml-dom.h --gir=GXmlDom-1.0.gir --library gxmldom-1.0 $^ @touch $@ # Library configuration libgxml_la_LDFLAGS = libgxml_la_LIBADD = \ $(GLIB_LIBS) \ $(LIBXML_LIBS) \ $(GIO_LIBS) \ $(GEE_LIBS) \ $(VALA_LIBS) \ $(NULL) include_HEADERS = \ gxml.h \ $(NULL) pkgconfigdir = $(libdir)/pkgconfig pkgconfig_DATA = libgxml-1.0.pc gxmlincludedir=$(includedir)/libgxml-1.0/gxml gxmlinclude_HEADERS= gxml-dom.h # GObject Introspection if ENABLE_GI_SYSTEM_INSTALL girdir = $(INTROSPECTION_GIRDIR) typelibsdir = $(INTROSPECTION_TYPELIBDIR) else girdir = $(datadir)/gir-1.0 typelibsdir = $(libdir)/girepository-1.0 endif # GIR files are generated automatically by Valac so is not necessary to scan source code to generate it INTROSPECTION_GIRS = INTROSPECTION_GIRS += GXmlDom-1.0.gir INTROSPECTION_COMPILER_ARGS = \ --includedir=. \ --includedir=$(top_builddir)/gxml GXmlDom-1.0.typelib: $(INTROSPECTION_GIRS) $(INTROSPECTION_COMPILER) $(INTROSPECTION_COMPILER_ARGS) $< -o $@ gir_DATA = $(INTROSPECTION_GIRS) typelibs_DATA = GXmlDom-1.0.typelib vapidir = $(VALA_VAPIDIR) vapi_DATA=gxmldom-1.0.vapi CLEANFILES += $(INTROSPECTION_GIRS) $(typelibs_DATA) gxml-1.0.vapi EXTRA_DIST = \ libgxml-1.0.pc.in \ $(libgxml_la_VALASOURCES) \ $(typelibs_DATA) \ $(INTROSPECTION_GIRS) \ gxml.vala.stamp

Compilation and linking using Command Line

Vala is not yet capable of directly creating dynamic or static libraries. To create a library, proceed with the -c (compile only) switch and link the object files with your favourite linker, i.e. libtool or ar.

$ valac -c ...(source files) $ ar cx ...(object files)

or by compiling the intermediate C code with *gcc*

$ valac -C ...(source files) $ gcc -o my-best-library.so --shared -fPIC ...(compiled C code files)...

Example

The following is an example of how to write a simple library in Vala, and also to compile and test it locally without having to install it first.

Save the following code to a file *test.vala*. This is the actual library code, containing the functions we want to call from our main program.

public class MyLib : Object { public void hello() { stdout.printf("Hello World, MyLib\n"); } public int sum(int x, int y) { return x + y; } }

Use the next command to generate *test.c*, *test.h* and *test.vapi* files. These are the C versions of the library to be compiled, and the VAPI file representing the library's public interface.

$ valac -C -H test.h --library test test.vala --basedir ./

Now compile the library:

$ gcc --shared -fPIC -o libtest.so $(pkg-config --cflags --libs gobject-2.0) test.c

Save the following code to a file called *hello.vala*. This is the code that will use the library we have created.

void main() { var test = new MyLib(); test.hello(); int x = 4, y = 5; stdout.printf("The sum of %d and %d is %d\n", x, y, test.sum(x, y)); }

Now compile the application code, telling the compiler that we want to link against the library we just created.

$ valac -X -I. -X -L. -X -ltest -o hello hello.vala test.vapi --basedir ./

We can now run the program. This command states that any required libraries will be found in the current directory.

$ LD_LIBRARY_PATH=$PWD ./hello

The output of the program should be:

Hello World, MyLib The sum of 4 and 5 is 9

You can also create a GObjectIntrospection GIR file for your library with the --gir option:

valac -C test.vala --library test --gir Test-1.0.gir

GIR files are XML descriptions of the API.

Binding Libraries with VAPI Files

VAPI files are descriptions of the public interface of external Vala libraries. When a library is written in Vala, this file is created by the Vala compiler, and basically an amalgamation of all public definitions from all Vala source files. For a library written in C, the VAPI file gets more complicated, particular if the naming conventions of the library do not follow the GLib convention. The VAPI file will in this case contain many annotations describing how the standardised Vala interface mangles onto the C version.

This process of creating this generally amounts to three steps, Running *vala-gen-introspect* to extract metadata from the C library. Adding extra metadata to standardise the interface or make various other changes. Generating a VAPI file from the above sources using *vapigen*.

Specific instructions on how to generate bindings are in the Vala Bindings Tutorial

Tools

The Vala distribution includes several programs to help you build and work with Vala applications. For more details of each tool, see the man pages.

valac

valac is the Vala compiler. It's primary function is to transform Vala code into compilable C code.

You can generally ignore warnings from the C compiler when using Vala and just need to notice the warnings from valac Vala has better information than the C compiler, so it knows certain things are valid when the C compiler has no way of knowing that.

Unfortunately we can't just add casts everywhere since there are situations where we can't generate a valid cast (and, what's more, no way to know what those situations are).

For example, compiling the Hello World will give us some warnings because valac by default generates code which is compatible with older versions of the GLib.Some methods may have been deprecated in your new version of GLib so that C language compiler will warn you.

Imagine a machine with older glib version want to run your vala program!

valac could generate C code with target GLib version:

$ valac --target-glib auto hello.vala # It will use the latest version of GLib which may not be compatible

The recommended approach is to just disable those warnings by passing options to the C compiler: $ valac -X -w hello.vala # Generated code is compatible, `-X` will pass `-w` to C compiler to disable all warnings.

You could set a alias in your bash/zsh/fish shell.

valac can also automate the entire build and link project in simple cases:

$ valac -o appname --pkg gee-1.0 file_name_1.vala file_name_2.vala

The -o switch requests that an object file is created, rather than just outputting C source files. The --pkg option says that this build needs information from the *gee-1.0* package. You do not need to specify details about what libraries to link in, the package has this information internally. Finally, a list of source files is given. If you need a more complicated build process, use the -C switch to generate C files instead of a binary, and continue the process manually, or through a script.

vapigen

vapigen is a tool to make bindings. It creates a VAPI files from a library's metadata and any extra information required. See also Vala Bindings Tutorial.

vala-gen-introspect

vala-gen-introspect is a tool for extracting metainformation about GObject based libraries. Nowadays, the preferred method is to use GObjectIntrospection instead, as vapigen can use GIR files directly. See also Vala Bindings Tutorial.

Techniques

Debugging

For demonstration purposes we will create a buggy program by intentionally dereferencing a null reference, which will result in a segmentation fault:

class Foo : Object { public int field; } void main() { Foo? foo = null; stdout.printf("%d\n", foo.field); }

$ valac debug-demo.vala $ ./debug-demo Segmentation fault

So how do we debug this program? The -g command line option tells the Vala compiler to include Vala source code line information in the compiled binary, --save-temps keeps the temporary C source files:

$ valac -g --save-temps debug-demo.vala

Vala programs can be debugged with the GNU Debugger gdb or one of its graphical front-ends, e.g. Nemiver.

$ nemiver debug-demo

A sample gdb session:

$ gdb debug-demo (gdb) run Starting program: /home/valacoder/debug-demo Program received signal SIGSEGV, Segmentation fault. 0x0804881f in _main () at debug-demo.vala:7 7 stdout.printf("%d\n", foo.field); (gdb)

Using GLib

GLib includes a large set of utilities, including wrappers for most of the standard libc functions and more. These tools are available on all Vala platforms, even those which are not POSIX compliant. For a complete description of all that GLib provides, see the GLib Reference Manual. That reference is related to the C API for GLib, but it is mainly very simple to work out how to translate into Vala.

The GLib functions are available in Vala through the following naming convention: C API Vala Example g_topic_foobar() GLib.Topic.foobar() GLib.Path.get_basename()

The GLib types can be used similarly: Instantiate with Call an object member with GLib.Foo foo = new GLib.Foo(); foo.bar();

The APIs are not identical between C and Vala, but these naming rules should mean you can find the functions you need in the GLib VAPI files shipped with Vala, and from there find the parameters. This will hopefully suffice until more Vala documentation can be generated.

File Handling

For flexible file I/O and file handling see GIO Samples.

You can also use FileUtils.get_contents to load a file into a string.

string content; FileUtils.get_contents("file.vala", out content);
