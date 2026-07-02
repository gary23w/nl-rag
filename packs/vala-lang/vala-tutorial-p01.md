---
title: "Projects/Vala/Tutorial (part 1/3)"
source: https://wiki.gnome.org/Projects/Vala/Tutorial
domain: vala-lang
license: CC-BY-SA-4.0
tags: vala language, vala lang, gobject vala, gnome vala
fetched: 2026-07-02
part: 1/3
---

# Projects/Vala/Tutorial

Vala Tutorial

**Tutorial Location Change** GNOME Wiki is being retired. This tutorial is now available at docs.vala.dev: Vala Documentation - Main Tutorial

Introduction

Disclaimer: Vala is an ongoing project, and its features may change. I will try to keep this tutorial as up to date as I can, but I'm not perfect. Also, I can't promise that the techniques which I suggest are necessarily the best in practice, but again I will try to keep up with that sort of thing.

What is Vala?

Vala is a new programming language that allows modern programming techniques to be used to write applications that run on the GNOME runtime libraries, particularly GLib and GObject. This platform has long provided a very complete programming environment, with such features as a dynamic type system and assisted memory management. Before Vala, the only ways to program for the platform were with the machine native C API, which exposes a lot of often unwanted detail, with a high level language that has an attendant virtual machine, such as Python or the Mono C# language, or alternatively, with C++ through a wrapper library.

Vala is different from all these other techniques, as it outputs C code which can be compiled to run with no extra library support beyond the GNOME platform. This has several consequences, but most importantly: Programs written in Vala should have broadly similar performance to those written directly in C, whilst being easier and faster to write and maintain. A Vala application can do nothing that a C equivalent cannot. Whilst Vala introduces a lot of language features that are not available in C, these are all mapped to C constructs, although they are often ones that are difficult or too time consuming to write directly.

As such, whilst Vala is a modern language with all of the features you would expect, it gains its power from an existing platform, and must in some ways comply with the rules set down by it.

Who is this tutorial for?

This tutorial will not go into depth about basic programming practices. It will only briefly explain the principles of object-oriented programming, instead focusing on how Vala applies the concepts. As such it will be helpful if you have experience of a variety of programming languages already, although in-depth knowledge of any particular one is not required.

Vala shares a lot of syntax with C#, but I will try to avoid describing features in terms of their similarity or differences with either C# or Java, with the aim of making the tutorial more accessible.

What will be useful is a reasonable understanding of C. Whilst this isn't needed for understanding Vala per se, it is important to realise that Vala programs are executed as C, and will often interact with C libraries. Knowledge of C will certainly make a deeper understanding of Vala far easier to come by.

Conventions

Code will be in monospaced text, commands will all be prefaced with a $ prompt. Other than that, everything should be obvious. I tend to code very explicitly, including some information that is actually implied. I will try to explain where some things can be omitted, but that doesn't mean that I encourage you do to this.

At some point I will add in references to the Vala documentation, but that isn't really possible yet.

A First Program

Sadly predictable, but still:

class Demo.HelloWorld : GLib.Object { public static int main(string[] args) { stdout.printf("Hello, World\n"); return 0; } }

Of course, that is a Vala *Hello World* program. I expect you can recognise some parts of it well enough, but just to be thorough I shall go through it step by step.

class Demo.HelloWorld : GLib.Object {

This line identifies the beginning of a class definition. Classes in Vala are very similar in concept to other languages. A class is basically a type of object, of which instances can be created, all having the same properties. The implementation of classed types is taken care of by the *gobject* library, but details of this are not important for general usage.

What is important to note is that this class is specifically described as being a subclass of *GLib.Object*. This is because Vala allows other types of class, but in most cases, this is the sort that you want. In fact, some language features of Vala are only allowed if your class is descended from GLib's *Object*.

Other parts of this line show namespacing and fully qualified names, although these will be explained later.

public static int main(string[] args) {

This is the start of a method definition. A method is a function related to a type of object that can be executed on an object of that type. The static method means that the method can be called without possessing a particular instance of the type. The fact that this method is called *main* and has the signature it does means that Vala will recognise it as the entry point for the program.

The *main* method doesn't have to be defined inside a class. However, if it is defined inside a class it must be static. It doesn't matter if it's public or private. The return type may be either int or void. With a void return type the program will implicitly terminate with exit code 0. The string array parameter holding the command line arguments is optional.

stdout.printf("Hello, World\n");

*stdout* is an object in the *GLib* namespace that Vala ensures you have access to whenever required. This line instructs Vala to execute the method called *printf* of the *stdout* object, with the hello string as an argument. In Vala, this is always the syntax you use to call a method on an object, or to access an object's data. \n is the escape sequence for a new line.

return 0;

return is to return a value to the caller and terminate the execution of the *main* method which also terminates the execution of the program. The returned value of the *main* method is then taken as the exit code of the program.

The last lines simply end the definitions of the method and class.

Compile and Run

Assuming you have Vala installed, then all it takes to compile and execute this program is:

$ valac hello.vala $ ./hello

*valac* is the Vala compiler, which will compile your Vala code into a binary. The resulting binary will have the same name as the source file and can then be directly executed on the machine. You can probably guess the output.

If you get some warnings from a C language compiler, please jump to Valac for the reason and solution.

Basics

Source Files and Compilation

Vala code is written in files with *.vala* extensions. Vala does not enforce as much structure as a language like Java - there are no concepts of packages or class files in the same way. Instead structure is defined by text inside each file, describing the logical location of the code with constructs such as namespaces. When you want to compile Vala code, you give the compiler a list of the files required, and Vala will work out how they fit together.

The upshot of all this is that you can put as many classes or functions into a file as you want, even combining parts of different namespaces in together. This is not necessarily a good idea. There are certain conventions you probably want to follow. A good example of how to structure a project in Vala is the Vala project itself.

All source files for the same package are supplied as command line parameters to the Vala compiler valac, along with compiler flags. This works similarly to how Java source code is compiled. For example:

$ valac compiler.vala --pkg libvala

will produce a binary with the name *compiler* that links with the package *libvala*. In fact, this is how the *valac* compiler is produced!

If you want the binary to have a different name or if you have passed multiple source files to the compiler you can specify the binary name explicitly with the -o switch:

$ valac source1.vala source2.vala -o myprogram $ ./myprogram

If you give *valac* the -C switch, it won't compile your program into a binary file. Instead it will output the intermediate C code for each of your Vala source files into a corresponding C source file, in this case *source1.c* and *source2.c*. If you look at the content of these files you can see that programming a class in Vala is equivalent to the same task in C, but a whole lot more succinct. You will also notice that this class is registered dynamically in the running system. This is a good example of the power of the GNOME platform, but as I've said before, you do not need to know much about this to use Vala.

If you want to have a C header file for your project you can use the -H switch:

$ valac hello.vala -C -H hello.h

Syntax Overview

Vala's syntax is an amalgam heavily based on C#'s. As a result, most of this will be familiar to programmers who know any C-like language, and in light of this I have kept things brief.

Scope is defined using braces. An object or reference is only valid between { and }. These are also the delimiters used to define classes, methods, code blocks etc, so they automatically have their own scope. Vala is not strict about where variables are declared.

An identifier is defined by its type and a name, e.g. int c meaning an integer called *c*. In the case of value types this also creates an object of the given type. For reference types these just define a new reference that doesn't initially point to anything.

Identifier names may be any combination of letters ([a-z], [A-Z]), underscores and digits. However, to define or refer to an identifier with a name that either starts with a digit or is a keyword, you must prefix it with the '@' character. This character is not considered a part of the name. For example, you can name a method *foreach* by writing @foreach, even though this is a reserved Vala keyword. You can omit the '@' character when it can be unambiguously interpreted as an identifier name, such as in "foo.foreach()".

Reference types are instantiated using the new operator and the name of a construction method, which is usually just the name of the type, e.g. Object o = new Object() creates a new Object and makes *o* a reference to it.

Vala allows comments in code in different ways.

These are handled in the same way as in most other languages and so need little explanation. Documentation comments are actually not special to Vala, but a documentation generation tool like Valadoc will recognise them.

Data Types

Broadly speaking there are two types of data in Vala: *reference types* and *value types*. These names describe how instances of the types are passed around the system - a value type is copied whenever it is assigned to a new identifier, a reference type is not copied, instead the new identifier is simply a new reference to the same object.

A constant is defined by putting const before the type. The naming convention for constants is ALL_UPPER_CASE.

Value Types

Vala supports a set of the simple types as most other languages do. Byte, char, uchar; their names are *char* for historical reasons. Character, unichar; a 32-bit Unicode character Integer, int, uint Long Integer, long, ulong Short Integer, short, ushort Guaranteed-size Integer, int8, int16, int32, int64 as well as their unsigned siblings uint8, uint16, uint32, uint64. The numbers indicate the lengths in bits. Float number, float, double Boolean, bool; possible values are true and false Compound, struct Enumeration, enum; represented by integer values, not as classes like Java's enums

Here are some examples. unichar c = 'u'; float percentile = 0.75f; const double MU_BOHR = 927.400915E-26; bool the_box_has_crashed = false; struct Vector { public double x; public double y; public double z; } enum WindowType { TOPLEVEL, POPUP }

Most of these types may have different sizes on different platforms, except for the guaranteed-size integer types. The sizeof operator returns the size that a variable of a given type occupies in bytes:

ulong nbytes = sizeof(int32);

You can determine the minimum and maximum values of a numerical type with *.MIN* and *.MAX*, e.g. int.MIN and int.MAX.

Strings

The data type for strings is string. Vala strings are UTF-8 encoded and immutable.

string text = "A string literal";

Vala offers a feature called *verbatim strings*. These are strings in which escape sequences (such as \n) won't be interpreted, line breaks will be preserved and quotation marks don't have to be masked. They are enclosed with triple double quotation marks. Possible indentations after a line break are part of the string as well.

string verbatim = """This is a so-called "verbatim string". Verbatim strings don't process escape sequences, such as \n, \t, \\, etc. They may contain quotes and may span multiple lines.""";

Strings prefixed with '@' are string templates. They can evaluate embedded variables and expressions prefixed with '$':

int a = 6, b = 7; string s = @"$a * $b = $(a * b)";

The equality operators == and != compare the content of two strings, contrary to Java's behaviour which in this case would check for referential equality.

You can slice a string with [start:end]. Negative values represent positions relative to the end of the string:

string greeting = "hello, world"; string s1 = greeting[7:12]; string s2 = greeting[-4:-2];

Note that indices in Vala start with 0 as in most other programming languages. Starting with Vala 0.11 you can access a single byte of a string with [index]:

uint8 b = greeting[7];

However, you cannot assign a new byte value to this position, since Vala strings are immutable.

Many of the basic types have reasonable methods for parsing from and converting to strings, for example:

bool b = bool.parse("false"); int i = int.parse("-52"); double d = double.parse("6.67428E-11"); string s1 = true.to_string(); string s2 = 21.to_string();

Two useful methods for writing and reading strings to/from the console (and for your first explorations with Vala) are *stdout.printf()* and *stdin.read_line()*:

stdout.printf("Hello, world\n"); stdout.printf("%d %g %s\n", 42, 3.1415, "Vala"); string input = stdin.read_line(); int number = int.parse(stdin.read_line());

You already know *stdout.printf()* from the *Hello World* example. Actually, it can take an arbitrary number of arguments of different types, whereas the first argument is a *format string*, following the same rules as C format strings. If you must output an error message you can use *stderr.printf()* instead of *stdout.printf()*.

In addition the *in* operation can be used to determine whether one string contains another, e.g.

if ("ere" in "Able was I ere I saw Elba.") ...

For more information, please report to the complete overview of the string class.

A sample program demonstrating string usage is also available. Arrays

An array is declared by giving a type name followed by [] and created by using the new operator e.g. int[] a = new int[10] to create an array of integers. The length of such an array can be obtained by the *length* member variable e.g. int count = a.length. Note that if you write Object[] a = new Object[10] no objects will be created, just the array to store them in.

int[] a = new int[10]; int[] b = { 2, 4, 6, 8 };

You can slice an array with [start:end]:

int[] c = b[1:3];

Slicing an array will result in a reference to the requested data, not a copy. However, assigning the slice to an owned variable (as is done above) will result in a copy. If you would like to avoid a copy, you must either assign the slice to an unowned array or pass it directly to an argument (arguments are, by default, unowned):

unowned int[] c = b[1:3];

Multi-dimensional arrays are defined with [,] or [,,] etc.

int[,] c = new int[3,4]; int[,] d = {{2, 4, 6, 8}, {3, 5, 7, 9}, {1, 3, 5, 7}}; d[2,3] = 42;

This sort of array is represented by a single contiguous memory block. Jagged multi-dimensional arrays ([][], also known as "stacked arrays" or "arrays of arrays"), where each row may have a different length, are not yet supported.

To find the length of each dimension in a multi-dimensional array, the *length* member becomes an array, storing the length of each respective dimension.

int[,] arr = new int[4,5]; int r = arr.length[0]; int c = arr.length[1];

Please note that you can't get a mono-dimensional array from a multidimensional array, or even slice a multidimensional array:

int[,] arr = {{1,2}, {3,4}}; int[] b = arr[0]; int[] c = arr[0,]; int[] d = arr[:,0]; int[] e = arr[0:1,0]; int[,] f = arr[0:1,0:1];

You can append array elements dynamically with the += operator. However, this works only for locally defined or private arrays. The array is automatically reallocated if needed. Internally this reallocation happens with sizes growing in powers of 2 for run-time efficiency reasons. However, .length holds the actual number of elements, not the internal size.

int[] e = {}; e += 12; e += 5; e += 37;

You can resize an array by calling *resize()* on it. It will keep the original content (as much as fits).

int[] a = new int[5]; a.resize(12);

You can move elements within an array by calling *move(src, dest, length)* on it. The original positions will be filled with 0.

uint8[] chars = "hello world".data; chars.move (6, 0, 5); print ((string) chars);

If you put the square brackets *after* the identifier together with an indication of size you will get a fixed-size array. Fixed-size arrays are allocated on the stack (if used as local variables) or in-line allocated (if used as fields) and you can't reallocate them later.

int f[10];

Vala does not do any bounds checking for array access at runtime. If you need more safety you should use a more sophisticated data structure like an *ArrayList*. You will learn more about that later in the section about *collections*.

Reference Types

The reference types are all types declared as a class, regardless of whether they are descended from GLib's *Object* or not. Vala will ensure that when you pass an object by reference the system will keep track of the number of references currently alive in order to manage the memory for you. The value of a reference that does not point anywhere is null. More on classes and their features in the section about object oriented programming.

class Track : GLib.Object { public double mass; public double name { get; set; } private bool terminated = false; public void terminate() { terminated = true; } }

Static Type Casting

In Vala, you can cast a variable from one type to another. For a static type cast, a variable is casted by the desired type name with parenthesis. A static cast doesn't impose any runtime type safety checking. It works for all Vala types. For example,

int i = 10; float j = (float) i;

Vala supports another casting mechanism called *dynamic cast* which performs runtime type checking and is described in the section about object oriented programming.

Type Inference

Vala has a mechanism called *type inference*, whereby a local variable may be defined using var instead of giving a type, so long as it is unambiguous what type is meant. The type is inferred from the right hand side of the assignment. It helps reduce unnecessary redundancy in your code without sacrificing static typing:

var p = new Person(); var s = "hello"; var l = new List<int>(); var i = 10;

This only works for local variables. Type inference is especially useful for types with generic type arguments (more on these later). Compare

MyFoo<string, MyBar<string, int>> foo = new MyFoo<string, MyBar<string, int>>();

vs.

var foo = new MyFoo<string, MyBar<string, int>>();

Defining new Type from other

Defining a new type is a matter of derive it from the one you need. Here is an example:

public class ValueList : GLib.List<GLib.Value> { [CCode (has_construct_function = false)] protected ValueList (); public static GLib.Type get_type (); }

Operators

=

assignment. The left operand must be an identifier, and the right must result in a value or reference as appropriate.

+, -, /, *, %

basic arithmetic, applied to left and right operands. The + operator can also concatenate strings.

+=, -=, /=, *=, %=

arithmetic operation between left and right operands, where the left must be an identifier, to which the result is assigned.

++, --

increment and decrement operations with implicit assignment. These take just one argument, which must be an identifier of a simple data type. The value will be changed and assigned back to the identifier. These operators may be placed in either prefix or postfix positions - with the former the evaluated value of the statement will be the newly calculated value, with the latter the original value is returned.

|, ^, &, ~, |=, &=, ^=

bitwise operations: or, exclusive or, and, not. The second set include assignment and are analogous to the arithmetic versions. These can be applied to any of the simple value types. (There is of no assignment operator associated with ~ because this is a unary operator. The equivalent operation is just a = ~a).

<<, >>

bit shift operations, shifting the left operand a number of bits according the right operand.

<<=, >>=

bit shift operations, shifting the left operand a number of bits according the right operand. The left operand must be an identifier, to which the result is assigned.

==

equality test. Evaluates to a bool value dependent on whether the left and right operands are equal. In the case of value types this means their values are equal, in the case of reference types that the objects are the same instance. An exception to this rule is the string type, which is tested for equality by value.

<, >, >=, <=, !=

inequality tests. Evaluate to a bool value dependent on whether the left and right operands are different in the manner described. These are valid for simple value data types, and the string type. For strings these operators compare the lexicographical order.

!, &&, ||

logic operations: not, and, or. These operations can be applied to Boolean values - the first taking just one value the others two.

? :

ternary conditional operator. Evaluates a condition and returns either the value of the left or the right sub-expression based on whether the condition is true or false: *condition* ? *value if true* : *value if false*

??

null coalescing operator: a ?? b is equivalent to a != null ? a : b. This operator is useful for example to provide a default value in case a reference is *null*:

stdout.printf("Hello, %s!\n", name ?? "unknown person");

in

checks if the right operand contains the left operand. This operator works on arrays, strings, collections or any other type that has an appropriate *contains()* method. For strings it performs a substring search.

Operators cannot be overloaded in Vala. There are extra operators that are valid in the context of lambda declarations and other specific tasks - these are explained in the context they are applicable.

Control Structures

while (a > b) { a--; }

will decrement *a* repeatedly, checking before each iteration that *a* is greater than *b*.

do { a--; } while (a > b);

will decrement *a* repeatedly, checking after each iteration that *a* is greater than *b*.

for (int a = 0; a < 10; a++) { stdout.printf("%d\n", a); }

will initialize *a* to 0, then print *a* repeatedly until *a* is no longer less than 10, incrementing *a* after each iteration.

foreach (int a in int_array) { stdout.printf("%d\n", a); }

will print out each integer in an array, or another iterable collection. The meaning of "iterable" will be described later.

All of the four preceding types of loop may be controlled with the keywords break and continue. A break instruction will cause the loop to immediately terminate, while continue will jump straight to the test part of the iteration.

if (a > 0) { stdout.printf("a is greater than 0\n"); } else if (a < 0) { stdout.printf("a is less than 0\n"); } else { stdout.printf("a is equal to 0\n"); }

executes a particular piece of code based on a set of conditions. The first condition to match decides which code will execute, if *a* is greater than 0 it will not be tested whether it is less than 0. Any number of else if blocks is allowed, and zero or one else blocks.

switch (a) { case 1: stdout.printf("one\n"); break; case 2: case 3: stdout.printf("two or three\n"); break; default: stdout.printf("unknown\n"); break; }

A switch statement runs exactly one or zero sections of code based on the value passed to it. In Vala there is no fall through between cases, except for empty cases. In order to ensure this, each non-empty case must end with a break, return or throw statement. It is possible to use switch statements with strings.

A note for C programmers: conditions must always evaluate to a Boolean value. This means that if you want to check a variable for null or 0 you must do this explicitly: if (object != null) { } or if (number != 0) { }.

Language Elements

Methods

Functions are called *methods* in Vala, regardless of whether they are defined inside a class or not. From now on we will stick to the term *method*.

int method_name(int arg1, Object arg2) { return 1; }

This code defines a method, having the name *method_name*, taking two arguments, one an integer and the other an *Object* (the first passed by value, the second as a reference as described). The method will return an integer, which in this case is 1.

All Vala methods are C functions, and therefore take an arbitrary number of arguments and return one value (or none if the method is declared *void*). They may approximate more return values by placing data in locations known to the calling code. Details of how to do this are in the "Parameter Directions" section in the advanced part of this tutorial.

The naming convention for methods in Vala is *all_lower_case* with underscores as word separators. This may be a little bit unfamiliar to C# or Java programmers who are accustomed to *CamelCase* or *mixedCamelCase* method names. But with this style you will be consistent with other Vala and C/GObject libraries.

It is not possible to have multiple methods with the same name but different signature within the same scope ("method overloading"):

void draw(string text) { } void draw(Shape shape) { }

This is due to the fact that libraries produced with Vala are intended to be usable for C programmers as well. In Vala you would do something like this instead:

void draw_text(string text) { } void draw_shape(Shape shape) { }

By choosing slightly different names you can avoid a name clash. In languages that support method overloading it is often used for providing convenience methods with less parameters that chain up to the most general method:

void f(int x, string s, double z) { } void f(int x, string s) { f(x, s, 0.5); } void f(int x) { f(x, "hello"); }

In this case you can use Vala's default argument feature for method parameters in order to achieve a similar behaviour with just one method. You can define default values for the last parameters of a method, so that you don't have to pass them explicitly to a method call:

void f(int x, string s = "hello", double z = 0.5) { }

Some possible calls of this method might be:

f(2); f(2, "hi"); f(2, "hi", 0.75);

It's even possible to define methods with real variable-length argument lists (*varargs*) like *stdout.printf()*, although not necessarily recommended. You will learn how to do that later.

Vala performs a basic nullability check on the method parameters and return values. If it is allowable for a method parameter or a return value to be null, the type symbol should be postfixed with a ? modifier. This extra information helps the Vala compiler to perform static checks and to add runtime assertions on the preconditions of the methods, which may help in avoiding related errors such as dereferencing a null reference.

string? method_name(string? text, Foo? foo, Bar bar) { }

In this example text, foo and the return value may be null, however, bar must not be null.

Delegates

delegate void DelegateType(int a);

Delegates represent methods, allowing chunks of code to be passed around like objects. The example above defines a new type named *DelegateType* which represents methods taking an *int* and not returning a value. Any method that matches this signature may be assigned to a variable of this type or passed as a method argument of this type.

delegate void DelegateType(int a); void f1(int a) { stdout.printf("%d\n", a); } void f2(DelegateType d, int a) { d(a); } void main() { f2(f1, 5); }

This code will execute the method *f2*, passing in a reference to method *f1* and the number 5. *f2* will then execute the method *f1*, passing it the number.

Delegates may also be created locally. A member method can also be assigned to a delegate, e.g,

class Foo { public void f1(int a) { stdout.printf("a = %d\n", a); } delegate void DelegateType(int a); public static int main(string[] args) { Foo foo = new Foo(); DelegateType d1 = foo.f1; d1(10); return 0; } }

More samples in Delegates-Manual

Anonymous Methods / Closures

(a) => { stdout.printf("%d\n", a); }

An *anonymous method*, also known as *lambda expression*, *function literal* or *closure*, can be defined in Vala with the => operator. The parameter list is on the left hand side of the operator, the method body on the right hand side.

An anonymous method standing by itself like the one above does not make much sense. It is only useful if you assign it directly to a variable of a delegate type or pass it as a method argument to another method.

Notice that neither parameter nor return types are explicitly given. Instead the types are inferred from the signature of the delegate it is used with.

Assigning an anonymous method to a delegate variable:

delegate void PrintIntFunc(int a); void main() { PrintIntFunc p1 = (a) => { stdout.printf("%d\n", a); }; p1(10); PrintIntFunc p2 = (a) => stdout.printf("%d\n", a); p2(20); }

Passing an anonymous method to another method:

delegate int Comparator(int a, int b); void my_sorting_algorithm(int[] data, Comparator compare) { } void main() { int[] data = { 3, 9, 2, 7, 5 }; my_sorting_algorithm(data, (a, b) => { if (a < b) return -1; if (a > b) return 1; return 0; }); }

Anonymous methods are real closures. This means you can access the local variables of the outer method within the lambda expression:

delegate int IntOperation(int i); IntOperation curried_add(int a) { return (b) => a + b; } void main() { stdout.printf("2 + 4 = %d\n", curried_add(2)(4)); }

In this example *curried_add* (see Currying) returns a newly created method that preserves the value of *a*. This returned method is directly called afterwards with 4 as argument resulting in the sum of the two numbers.

Namespaces

namespace NameSpaceName { }

Everything between the braces in this statement is in the namespace *NameSpaceName* and must be referenced as such. Any code outside this namespace must either use qualified names for anything within the name of the namespace, or be in a file with an appropriate using declaration in order to import this namespace:

using NameSpaceName;

For example, if the namespace *Gtk* is imported with using Gtk; you can simply write *Window* instead of *Gtk.Window*. A fully qualified name would only be necessary in case of ambiguity, for example between *GLib.Object* and *Gtk.Object*.

The namespace *GLib* is imported by default. Imagine an invisible using GLib; line at the beginning of every Vala file.

Everything that you don't put into a separate namespace will land in the anonymous global namespace. If you have to reference the global namespace explicitly due to ambiguity you can do that with the global:: prefix.

Namespaces can be nested, either by nesting one declaration inside another, or by giving a name of the form *NameSpace1.NameSpace2*.

Several other types of definition can declare themselves to be inside a namespace by following the same naming convention, e.g. class NameSpace1.Test { ... }. Note that when doing this, the final namespace of the definition will be the one the declaration is nested in plus the namespaces declared in the definition.

Structs

struct StructName { public int a; }

defines a struct type, i.e. a compound value type. A Vala struct may have methods in a limited way and also may have private members, meaning the explicit public access modifier is required.

struct Color { public double red; public double green; public double blue; }

This is how you can initialise a struct:

Color c1 = Color(); Color c2 = { 0.5, 0.5, 1.0 }; Color c3 = Color() { red = 0.5, green = 0.5, blue = 1.0 }; var c4 = Color(); var c5 = Color() { red = 0.5, green = 0.5, blue = 1.0 };

Structs are stack/inline allocated and copied on assignment.

To define an array of structs, please see the FAQ.

Classes

class ClassName : SuperClassName, InterfaceName { }

defines a class, i.e. a reference type. In contrast to structs, instances of classes are heap allocated. There is much more syntax related to classes, which is discussed more fully in the section about object oriented programming.

Interfaces

interface InterfaceName : SuperInterfaceName { }

defines an interface, i.e. a non instantiable type. In order to create an instance of an interface you must first implement its abstract methods in a non-abstract class. Vala interfaces are more powerful than Java or C# interfaces. In fact, they can be used as mixins. The details of interfaces are described in the section about object oriented programming.

Code Attributes

Code attributes instruct the Vala compiler details about how the code is supposed to work on the target platform. Their syntax is [AttributeName] or [AttributeName(param1 = value1, param2 = value2, ...)].

They are mostly used for bindings in *vapi* files, [CCode(...)] being the most prominent attribute here. Another example is the [DBus(...)] attribute for exporting remote interfaces via D-Bus.

Object Oriented Programming

Although Vala doesn't force you to work with objects, some features are not available any other way. As such, you will certainly want to program in an object-oriented style most of the time. As with most current languages, in order to define your own object types, you write a class definition.

A class definition states what data each object of its type has, what other object types it can hold references to, and what methods can be executed on it. The definition can include a name of another class which the new one should be a subclass of. An instance of a class is also an instance of all it's class's super classes, as it inherits from them all their methods and data, although it may not be able to access all of this itself. A class may also implement any number of interfaces, which are sets of method definitions that must be implemented by the class - an instance of a class is also an instance of each interface implemented by its class or super classes.

Classes in Vala may also have "static" members. This modifier allows either data or methods to be defined as belonging to the class as a whole, rather than to a specific instance of it. Such members can be accessed without possessing an instance of the class.

Basics

A simple class may be defined as follows:

public class TestClass : GLib.Object { public int first_data = 0; private int second_data; public TestClass() { this.second_data = 5; } public int method_1() { stdout.printf("private data: %d", this.second_data); return this.second_data; } }

This code will define a new type (which is registered automatically with the *gobject* library's type system) that contains three members. There are two data members, the integers defined at the top, and one method called *method_1*, which returns an integer. The class declaration states that this class is a subclass of *GLib.Object*, and therefore instances of it are also *Objects*, and contain all the members of that type also. The fact that this class is descended from *Object* also means that there are special features of Vala that can be used to easily access some of *Object's* features.

This class is described as public (by default, classes are internal). The implication of this is that it can referenced directly by code outside of this file - if you are a C programmer of glib/gobject, you will recognise this as being equivalent to defining the class interfaces in a header file that other code can include.

The members are also all described as either public or private. The member *first_data* is public, so it is visible directly to any user of the class, and can be modified without the containing instance being aware of it. The second data member is private, and so can only be referenced by code belonging to this class. Vala supports four different access modifiers: public No restrictions to access private Access is limited to within the class/struct definition. This is the default if no access modifier is specified protected Access is limited to within the class definition and any class that inherits from the class internal Access is limited exclusively to classes defined within the same package

The constructor initialises new instances of a class. It has the same name as the class, may take zero or more arguments and is defined without return type.

The final part of this class is a method definition. This method is to be called *method_1*, and it will return an integer. As this method is not static, it can only be executed on an instance of this class, and may therefore access members of that instance. It can do this through the this reference, which always points to the instance the method is being called on. Unless there is an ambiguity, the this identifier can be omitted if wished.

You can use this new class as follows:

TestClass t = new TestClass(); t.first_data = 5; t.method_1();

Construction

Vala supports two slightly different construction schemes: the Java/C#-style construction scheme which we will focus on for now, and the GObject-style construction scheme which will be described in a section at the end of the chapter.

Vala does not support constructor overloading for the same reasons that method overloading is not allowed, which means a class may not have multiple constructors with the same name. However, this is no problem because Vala supports *named constructors*. If you want to offer multiple constructors you may give them different name additions:

public class Button : Object { public Button() { } public Button.with_label(string label) { } public Button.from_stock(string stock_id) { } }

Instantiation is analogous:

new Button(); new Button.with_label("Click me"); new Button.from_stock(Gtk.STOCK_OK);

You may chain constructors via this() or this.*name_extension*():

public class Point : Object { public double x; public double y; public Point(double x, double y) { this.x = x; this.y = y; } public Point.rectangular(double x, double y) { this(x, y); } public Point.polar(double radius, double angle) { this.rectangular(radius * Math.cos(angle), radius * Math.sin(angle)); } } void main() { var p1 = new Point.rectangular(5.7, 1.2); var p2 = new Point.polar(5.7, 1.2); }

Destruction

Although Vala manages the memory for you, you might need to add your own destructor if you choose to do manual memory management with pointers (more on that later) or if you have to release other resources. The syntax is the same as in C# and C++:

class Demo : Object { ~Demo() { stdout.printf("in destructor"); } }

Since Vala's memory management is based on *reference counting* instead of *tracing garbage collection*, destructors are deterministic and can be used to implement the RAII pattern for resource management (closing streams, database connections, ...).

Signals

Signals are a system provided by the Object class in GLib, and made easily accessible by Vala to all descendants of Object. A signal is recognisable to C# programmers as an event, or to Java programmers as an alternative way of implementing event listeners. In short, a signal is simply a way of executing an arbitrary number of externally identical methods (i.e. ones with the same signature) at approximately the same time. The actual methods of execution are internal to *gobject*, and not important to Vala programs.

A signal is defined as a member of a class, and appears similar to a method with no body. Signal handlers can then be added to the signal using the connect() method. In order to dive right in at the deep end, the following example also introduces lambda expressions, a very useful way to write signal handling code in Vala:

public class Test : GLib.Object { public signal void sig_1(int a); public static int main(string[] args) { Test t1 = new Test(); t1.sig_1.connect((t, a) => { stdout.printf("%d\n", a); }); t1.sig_1(5); return 0; } }

This code introduces a new class called "Test", using familiar syntax. The first member of this class is a signal, called "sig_1", which is defined as passing an integer. In the main method of this program, we first create a Test instance - a requirement since signals always belong to instances of classes. Next, we assign to our instance's "sig_1" signal a handler, which we define inline as a lambda expression. The definition states that the method will receive two arguments which we call "t" and "a", but do not provide types for. We can be this terse because Vala already knows the definition of the signal and can therefore understand what types are required.

The reason there are two parameters to the handler is that whenever a signal is emitted, the object on which it is emitted is passed as the first argument to the handler. The second argument is that one that the signal says it will provide.

Finally, we get impatient and decide to emit a signal. We do this by calling the signal as though it was a method of our class, and allow gobject to take care of forwarding the message to all attached handlers. Understanding the mechanism used for this is not required to use signals from Vala.

NB: Currently the public access modifier is the only possible option - all signals can be both connected to and emitted by any piece of code.

Signals can be annotated with any combination of flags: [Signal (action=true, detailed=true, run=true, no_recurse=true, no_hooks=true)] public signal void sig_1 ();

More samples in Signal Sampls

Properties

It is good object oriented programming practice to hide implementation details from the users of your classes (information hiding principle), so you can later change the internals without breaking the public API. One practice is to make fields private and provide accessor methods for getting and setting their values (getters and setters).

If you're a Java programmer you will probably think of something like this:

class Person : Object { private int age = 32; public int get_age() { return this.age; } public void set_age(int age) { this.age = age; } }

This works, but Vala can do better. The problem is that these methods are cumbersome to work with. Let's suppose that you want to increase the age of a person by one year:

var alice = new Person(); alice.set_age(alice.get_age() + 1);

This is where properties come into play:

class Person : Object { private int _age = 32; public int age { get { return _age; } set { _age = value; } } }

This syntax should be familiar to C# programmers. A property has a get and a set block for getting and setting its value. value is a keyword that represents the new value that should be assigned to the property.

Now you can access the property as if it was a public field. But behind the scenes the code in the get and set blocks is executed.

var alice = new Person(); alice.age = alice.age + 1; alice.age++;

If you only do the standard implementation as shown above then you can write the property even shorter:

class Person : Object { public int age { get; set; default = 32; } }

With properties you can change the internal working of classes without changing the public API. For example:

static int current_year = 2525; class Person : Object { private int year_of_birth = 2493; public int age { get { return current_year - year_of_birth; } set { year_of_birth = current_year - value; } } }

This time the age is calculated on the fly from the year of birth. Note that you can do more than just simple variable access or assignment within the get and set blocks. You could do a database access, logging, cache updates, etc.

If you want to make a property read-only for the users of the class you should make the setter private:

public int age { get; private set; default = 32; }

Or, alternatively, you can leave out the set block:

class Person : Object { private int _age = 32; public int age { get { return _age; } } }

Properties may not only have a name but also a short description (called *nick*) and a long description (called *blurb*). You can annotate these with a special attribute:

[Description(nick = "age in years", blurb = "This is the person's age in years")] public int age { get; set; default = 32; }

Properties and their additional descriptions can be queried at runtime. Some programs such as the Glade graphical user interface designer make use of this information. In this way Glade can present human readable descriptions for properties of GTK+ widgets.

Every instance of a class derived from GLib.Object has a signal called notify. This signal gets emitted every time a property of its object changes. So you can connect to this signal if you're interested in change notifications in general:

obj.notify.connect((s, p) => { stdout.printf("Property '%s' has changed!\n", p.name); });

s is the source of the signal (obj in this example), p is the property information of type *ParamSpec* for the changed property. If you're only interested in change notifications of a single property you can use this syntax:

alice.notify["age"].connect((s, p) => { stdout.printf("age has changed\n"); });

Note that in this case you must use the string representation of the property name where underscores are replaced by dashes: my_property_name becomes "my-property-name" in this representation, which is the GObject property naming convention.

Change notifications can be disabled with a CCode attribute tag immediately before the declaration of the property:

public class MyObject : Object { [CCode(notify = false)] public int without_notification { get; set; } public int with_notification { get; set; } }

There's another type of properties called *construct properties* that are described later in the section about gobject-style construction.

Note: in case your property is type of struct, to get the property value with Object.get(), you have to declare your variable as example below struct Color { public uint32 argb; public Color() { argb = 0x12345678; } } class Shape: GLib.Object { public Color c { get; set; default = Color(); } } int main() { Color? c = null; Shape s = new Shape(); s.get("c", out c); }

This way, c is an reference instead of an instance of Color on stack. What you passed into s.get() is "Color **" instead of "Color *".

Inheritance

In Vala, a class may derive from one or zero other classes. In practice this is always likely to be one, although there is no implicit inheritance as there is in languages like Java.

When defining a class that inherits from another, you create a relationship between the classes where instances of the subclass are also instances of the superclass. This means that operations on instances of the superclass are also applicable on instances of the subclass. As such, wherever an instance of the superclass is required, an instance of the subclass can be substituted.

When writing the definition of a class it is possible to exercise precise control over who can access what methods and data in the object. The following example demonstrates a range of these options:
