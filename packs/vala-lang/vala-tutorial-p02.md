---
title: "Projects/Vala/Tutorial (part 2/3)"
source: https://wiki.gnome.org/Projects/Vala/Tutorial
domain: vala-lang
license: CC-BY-SA-4.0
tags: vala language, vala lang, gobject vala, gnome vala
fetched: 2026-07-02
part: 2/3
---

# Projects/Vala/Tutorial

class SuperClass : GLib.Object { private int data; public SuperClass(int data) { this.data = data; } protected void protected_method() { } public static void public_static_method() { } } class SubClass : SuperClass { public SubClass() { base(10); } }

*data* is an instance data member of *SuperClass*. There will be a member of this type in every instance of *SuperClass*, and it is declared private so will only be accessible by code that is a part of *SuperClass*.

*protected_method* is an instance method of *SuperClass*. You will be able to execute this method only an instance of *SuperClass* or of one of its subclasses, and only from code that belongs to *SuperClass* or one of its subclasses - this latter rule being the result of the protected modifier.

*public_static_method* has two modifiers. The static modifier means that this method may be called without owning an instance of *SuperClass* or of one of its subclasses. As a result, this method will not have access to a this reference when it is executed. The public modifier means that this method can be called from any code, no matter its relationship with *SuperClass* or its subclasses.

Given these definitions, an instance of *SubClass* will contain all three members of *SuperClass*, but will only be able to access the non-private members. External code will only be able to access the public method.

With base a constructor of a subclass can chain up to a constructor of its base class.

Abstract Classes

There is another modifier for methods, called abstract. This modifier allows you to describe a method that is not actually implemented in the class. Instead, it must be implemented by subclasses before it can be called. This allows you to define operations that can be called on all instances of a type, whilst ensuring that all more specific types provide their own version of the functionality.

A class containing abstract methods must be declared abstract as well. The result of this is to prevent any instantiation of the type.

public abstract class Animal : Object { public void eat() { stdout.printf("*chomp chomp*\n"); } public abstract void say_hello(); } public class Tiger : Animal { public override void say_hello() { stdout.printf("*roar*\n"); } } public class Duck : Animal { public override void say_hello() { stdout.printf("*quack*\n"); } }

The implementation of an abstract method must be marked with override. Properties may be abstract as well.

Virtual Methods

A virtual method allows to define default implementations to abstract classes and allows to derived classes to override its behavior, this is different than hiding methods.

public abstract class Caller : GLib.Object { public abstract string name { get; protected set; } public abstract void update (string new_name); public virtual bool reset () { name = "No Name"; return true; } } public class ContactCV : Caller { public override string name { get; protected set; } public override void update (string new_name) { name = "ContactCV - " + new_name; } public override bool reset () { name = "ContactCV-Name"; stdout.printf ("CotactCV.reset () implementation!\n"); return true; } } public class Contact : Caller { public override string name { get; protected set; } public override void update (string new_name) { name = "Contact - " + new_name; } public static void main () { var c = new Contact (); c.update ("John Strauss"); stdout.printf(@"Name: $(c.name)\n"); c.reset (); stdout.printf(@"Reset Name: $(c.name)\n"); var cv = new ContactCV (); cv.update ("Xochitl Calva"); stdout.printf(@"Name: $(cv.name)\n"); cv.reset (); stdout.printf(@"Reset Name: $(cv.name)\n"); stdout.printf("END\n"); } }

As you can see in the above example, Caller is an abstract class defining both an abstract property and a method, but adds a virtual method which can be overridden by derived classes. Contact class implements abstract methods and properties of Caller, while using the default implementation for reset() by avoiding to define a new one. ContactCV class implements all abstract definitions on Caller, but overrides reset() so as to define its own implementation.

Interfaces

A class in Vala may implement any number of interfaces. Each interface is a type, much like a class, but one that cannot be instantiated. By "implementing" one or more interfaces, a class may declare that its instances are also instances of the interface, and therefore may be used in any situation where an instance of that interface is expected.

The procedure for implementing an interface is the same as for inheriting from classes with abstract methods in - if the class is to be useful it must provide implementations for all methods that are described but not yet implemented.

A simple interface definition looks like:

public interface ITest : GLib.Object { public abstract int data_1 { get; set; } public abstract void method_1(); }

This code describes an interface "ITest" which requires GLib.Object as parent of the implementor class and contains two members. "data_1" is a property, as described above, except that it is declared abstract. Vala will therefore not implement this property, but instead require that classes implementing this interface have a property called "data_1" that has both get and set accessors - it is required that this be abstract as an interface may not have any data members. The second member "method_1" is a method. Here it is declared that this method must be implemented by classes that implement this interface.

The simplest possible full implementation of this interface is:

public class Test1 : GLib.Object, ITest { public int data_1 { get; set; } public void method_1() { } }

And may be used as follows:

var t = new Test1(); t.method_1(); ITest i = t; i.method_1();

Defining Prerequisites

Interfaces in Vala may not inherit from other interfaces, but they may declare other interfaces to be prerequisites, which works in roughly the same way. For example, it may be desirable to say that any class that implements a List interface must also implement a Collection and Traversable interfaces. The syntax for this is exactly the same as for describing interface implementation in classes:

public interface List : Collection, Traversable { }

This definition of "List" may not be implemented in a class without "Collection" also being implemented, and so Vala enforces the following style of declaration for a class wishing to implement "List", where all implemented interfaces must be described:

public class ListClass : GLib.Object, Collection, List { }

Vala interfaces may also have a class as a prerequisite. If a class name is given in the list of prerequisites, the interface may only be implemented in classes that derive from that prerequisite class. This is often used to ensure that an instance of an interface is also a GLib.Object subclass, and so the interface can be used, for example, as the type of a property.

The fact that interfaces can not inherit from other interfaces is mostly only a technical distinction - in practice Vala's system works the same as other languages in this area, but with the extra feature of prerequisite classes.

Defining default implementation in methods

There's another important difference between Vala interfaces and Java/C# interfaces: Vala interfaces may have non-abstract methods.

Vala actually allows method implementations in interfaces, then a method with a default implementation must be declared as virtual. Due to this fact Vala interfaces can act as mixins. This is a restricted form of multiple inheritance.

public interface Callable : GLib.Object { public abstract bool answering { get; protected set; } public abstract void answer (); public virtual bool hang () { answering = false; return true; } }

Interface Callable defines an abstract property called answering, where any class implementing this interface can monitor the state of a call, details about answer a call is a mautter of the implementator, but hang defines a default implementation to set answering to false when hanging a call.

public class Phone : GLib.Object, Callable { public bool answering { get; protected set; } public void answer () { } public static void main () { var f = new Phone (); if (f.hang ()) stdout.printf("Hand done.\n"); else stdout.printf("Hand Error!\n"); stdout.printf("END\n"); } }

When compiling and running, you will find that Phone class actually no implements Callable.hang() method, but it is able to use it, then the result is a message Hang done.

public class TechPhone : GLib.Object, Callable { public bool answering { get; protected set; } public void answer () { } public bool hang () { answering = false; stdout.printf ("TechPhone.hang () implementation!"); return false; } }

In this case TechPhone is another implementation to Callable, then when hang() method is called on an instance of TechPhone it will always return false and print the message TechPhone.hang () implementation!, hidding completelly Callable.hang() default implementation.

Properties

An interface can define properties that must be implemented for classes. Implementator class must define a property with the same signature and access permissions to the property's get and set.

As any GObject property, you can define a body to property's set and get in the implementator class, when no body is used values are set and get by default. If given, you must define a private field to store the properties values to be used outside or inside the class.

Callable interface definition, defines an answering property. In this case this interface defines a answering with a protected set, allowing a read only property for any object using an instance of Callable, but allows class implementors to write values to it, like TechPhone class does when implements hang() method.

Mixins and Multiple Inheritance

As described above, Vala while it is backed by C and GObject, can provide a limited multiple inheritance mechanism, by adding virtual methods to Interfaces. Is possible to add some ways to define default method implementations in interface implementor class and allow derived classes to override that methods.

If you define a virtual method in an interface and implement it in a class, you can't override interface's method without leaving derived classes unable to access to interface default one. Consider following code:

public interface Callable : GLib.Object { public abstract bool answering { get; protected set; } public abstract void answer (); public abstract bool hang (); public static bool default_hang (Callable call) { stdout.printf ("At Callable.hang()\n"); call.answering = false; return true; } } public abstract class Caller : GLib.Object, Callable { public bool answering { get; protected set; } public void answer () { stdout.printf ("At Caller.answer()\n"); answering = true; hang (); } public virtual bool hang () { return Callable.default_hang (this); } } public class TechPhone : Caller { public string number { get; set; } } public class Phone : Caller { public override bool hang () { stdout.printf ("At Phone.hang()\n"); return false; } public static void main () { var f = (Callable) new Phone (); f.answer (); if (f.hang ()) stdout.printf("Hand done.\n"); else stdout.printf("Hand Error!\n"); var t = (Callable) new TechPhone (); t.answer (); if (t.hang ()) stdout.printf("Tech Hand done.\n"); else stdout.printf("Tech Hand Error!\n"); stdout.printf("END\n"); } }

In this case, we have defined a Callable interface with a default implementation for abstract bool hang () called default_hang, it could be a static or virtual method. Then Caller is a base class implementing Callable for the TechPhone and Phone classes, while Caller's hang () method simple call Callable default implementation. TechPhone doesn't do anything and just takes Caller as base class, using the default method implementations; but Phone overrides Caller.hang () and this makes to use its own implementation, allowing to always call it even if it is cast to Callable object.

Explicit method implementation

The explicit interface method implementation allows to implement two interfaces that have methods (not properties) with the same name. Example: interface Foo { public abstract int m(); } interface Bar { public abstract string m(); } class Cls: Foo, Bar { public int Foo.m() { return 10; } public string Bar.m() { return "bar"; } } void main () { var cls = new Cls (); message ("%d %s", ((Foo) cls).m(), ((Bar) cls).m()); }

Will output 10 bar.

Polymorphism

*Polymorphism* describes the way in which the same object can be used as though it were more than one distinct type of thing. Several of the techniques already described here suggest how this is possible in Vala: An instance of a class may be used as in instance of a superclass, or of any implemented interfaces, without any knowledge of its actual type.

A logical extension of this power is to allow a subtype to behave differently to its parent type when addressed in exactly the same way. This is not a very easy concept to explain, so I'll begin with an example of what will happen if you do not directly aim for this goal:

class SuperClass : GLib.Object { public void method_1() { stdout.printf("SuperClass.method_1()\n"); } } class SubClass : SuperClass { public void method_1() { stdout.printf("SubClass.method_1()\n"); } }

These two classes both implement a method called "method_1", and "SubClass" therefore contains two methods called "method_1", as it inherits one from "SuperClass". Each of these may be called as the following code shows:

SubClass o1 = new SubClass(); o1.method_1(); SuperClass o2 = o1; o2.method_1();

This will actually result in two different methods being called. The second line believes "o1" to be a "SubClass" and will call that class's version of the method. The fourth line believes "o2" to be a "SuperClass" and will call that class's version of the method.

The problem this example exposes, is that any code holding a reference to "SuperClass" will call the methods actually described in that class, even in the actual object is of a subclass. The way to change this behaviour is using virtual methods. Consider the following rewritten version of the last example:

class SuperClass : GLib.Object { public virtual void method_1() { stdout.printf("SuperClass.method_1()\n"); } } class SubClass : SuperClass { public override void method_1() { stdout.printf("SubClass.method_1()\n"); } }

When this code is used in the same way as before, "SubClass"'s "method_1" will be called twice. This is because we have told the system that "method_1" is a virtual method, meaning that if it is overridden in a subclass, that new version will always be executed on instances of that subclass, regardless of the knowledge of the caller.

This distinction is probably familiar to programmers of some languages, such as C++, but it is in fact the opposite of Java style languages, in which steps must be taken to prevent a method being virtual.

You will probably now also have recognised that when method is declared as abstract it must also be virtual. Otherwise, it would not be possible to execute that method given an apparent instance of the type it was declared in. When implementing an abstract method in a subclass, you may therefore choose to declare the implementation as override, thus passing on the virtual nature of the method, and allowing subtypes to do the same if they desire.

It's also possible to implement interface methods in such a way that subclasses can change the implementation. The process in this case is for the initial implementation to declare the method implementation to be virtual, and then subclasses can override as required.

When writing a class, it is common to want to use functionality defined in a class you have inherited from. This is complicated where the method name is used more than one in the inheritance tree for your class. For this Vala provides the base keyword. The most common case is where you have overridden a virtual method to provide extra functionality, but still need the parent class' method to be called. The following example shows this case:

public override void method_name() { base.method_name(); extra_task(); }

Vala also allows properties to be virtual:

class SuperClass : GLib.Object { public virtual string prop_1 { get { return "SuperClass.prop_1"; } } } class SubClass : SuperClass { public override string prop_1 { get { return "SubClass.prop_1"; } }

Method Hiding

By using the new modifier you can hide an inherited method with a new method of the same name. The new method may have a different signature. Method hiding is not to be confused with method overriding, because method hiding does not exhibit polymorphic behaviour.

class Foo : Object { public void my_method() { } } class Bar : Foo { public new void my_method() { } }

You can still call the original method by casting to the base class or interface:

void main() { var bar = new Bar(); bar.my_method(); (bar as Foo).my_method(); }

Run-Time Type Information

Since Vala classes are registered at runtime and each instance carries its type information you can dynamically check the type of an object with the is operator:

bool b = object is SomeTypeName;

You can get the type information of Object instances with the get_type() method:

Type type = object.get_type(); stdout.printf("%s\n", type.name());

With the typeof() operator you can get the type information of a type directly. From this type information you can later create new instances with Object.new():

Type type = typeof(Foo); Foo foo = (Foo) Object.new(type);

Which constructor will be called? It's the construct {} block that will be described in the section about gobject-style construction.

Dynamic Type Casting

For the dynamic cast, a variable is casted by a postfix expression as DesiredTypeName. Vala will include a runtime type checking to ensure this casting is reasonable - if it is an illegal casting, null will be returned. However, this requires both the source type and the target type to be referenced class types.

For example, Button b = widget as Button;

If for some reason the class of the widget instance is not the Button class or one of its subclasses or does not implement the Button interface, b will be null. This cast is equivalent to:

Button b = (widget is Button) ? (Button) widget : null;

Generics

Vala includes a runtime generics system, by which a particular instance of a class can be restricted with a particular type or set of types chosen at construction time. This restriction is generally used to require that data stored in the object must be of a particular type, for example in order to implement a list of objects of a certain type. In that example, Vala would make sure that only objects of the requested type could be added to the list, and that on retrieval all objects would be cast to that type.

In Vala, generics are handled while the program is running. When you define a class that can be restricted by a type, there still exists only one class, with each instance customised individually. This is in contrast to C++ which creates a new class for each type restriction required - Vala's is similar to the system used by Java. This has various consequences, most importantly: that static members are shared by the type as a whole, regardless of the restrictions placed on each instance; and that given a class and a subclass, a generic refined by the subclass can be used as a generic refined by the class.

The following code demonstrates how to use the generics system to define a minimal wrapper class:

public class Wrapper<G>: GLib.Object { public G data { get; set; } }

This "Wrapper" class must be restricted with a type in order to instantiate it - in this case the type will be identified as "G", and so instances of this class will store one object of "G" type.

In order to instantiate this class, a type must be chosen, for example the built in string type (in Vala there is no restriction on what type may be used in a generic). To create an briefly use this class:

void main () { var w = new Wrapper<string>(); w.data = "test"; stdout.printf(w.data); }

As you can see, when the data is retrieved from the wrapper, it is assigned to an identifier with no explicit type. This is possible because Vala knows what sort of objects are in each wrapper instance, and therefore can do this work for you.

The fact that Vala does not create multiple classes out of your generic definition means that you can code as follows: (This is called Type Erasure which is same in Java to avoid massive expansion in generated C code.)

class TestClass : GLib.Object { } void accept_object_wrapper(Wrapper<Glib.Object> w) { } ... var test_wrapper = new Wrapper<TestClass>(); accept_object_wrapper(test_wrapper); ...

Since all Test Class instances are also Objects, the "accept_object_wrapper" method will happily accept the object it is passed, and treat its wrapped object as though it was a GLib.Object instance.

GObject-Style Construction

As pointed out before, Vala supports an alternative construction scheme that is slightly different to the one described before, but closer to the way GObject construction works. Which one you prefer depends on whether you come from the GObject side or from the Java or C# side. The gobject-style construction scheme introduces some new syntax elements: *construct properties*, a special Object(...) call and a construct block. Let's take a look at how this works:

public class Person : Object { public string name { get; construct; } public int age { get; construct set; } public Person(string name) { Object(name: name); } public Person.with_age(string name, int years) { Object(name: name, age: years); } construct { stdout.printf("Welcome %s\n", this.name); } }

With the gobject-style construction scheme each construction method only contains an Object(...) call for setting so-called *construct properties*. The Object(...) call takes a variable number of named arguments in the form of property: value. These properties must be declared as construct or set properties. They will be set to the given values and afterwards all construct {} blocks in the hierarchy from *GLib.Object* down to our class will be called.

The construct block is guaranteed to be called when an instance of this class is created, even if it is created as a subtype. It does neither have any parameters, nor a return value. Within this block you can call other methods and set member variables as needed.

Construct properties are defined just as get and set properties, and therefore can run arbitrary code on assignment. If you need to do initialisation based on a single construct property, it is possible to write a custom construct block for the property, which will be executed immediately on assignment, and before any other construction code.

If a construct property is declared without set it is a so-called *construct only* property, which means it can only be assigned on construction, but no longer afterwards. In the example above *name* is such a construct only property.

Here's a summary of the various types of properties together with the nomenclature usually found in the documentation of gobject-based libraries:

public int a { get; private set; } public int b { private get; set; } public int c { get; set; } public int d { get; set construct; } public int e { get; construct; }

In some cases you may also want to perform some action - not when instances of a class is created - but when the class itself is created by the GObject runtime. In GObject terminology we are talking about a snippet of code run inside the class_init function for the class in question. In Java this is known as *static initializer blocks*. In Vala this looks like:

static construct { ... }

Advanced Features

Assertions and Contract Programming

With *assertions* a programmer can check assumptions at runtime. The syntax is assert(*condition*). If an assertion fails the program will terminate with an appropriate error message. There are a few more assertion methods within the GLib standard namespace, e.g.: assert_not_reached() return_if_fail(bool expr) return_if_reached() warn_if_fail(bool expr) warn_if_reached()

You might be tempted to use assertions in order to check method arguments for null. However, this is not necessary, since Vala does that implicitly for all parameters that are not marked with ? as being *nullable*.

void method_name(Foo foo, Bar bar) { }

Vala supports basic contract programming features. A method may have preconditions (requires) and postconditions (ensures) that must be fulfilled at the beginning or the end of a method respectively:

double method_name(int x, double d) requires (x > 0 && x < 10) requires (d >= 0.0 && d <= 1.0) ensures (result >= 0.0 && result <= 10.0) { return d * x; }

result is a special variable representing the return value.

Error Handling

GLib has a system for managing runtime exceptions called GError. Vala translates this into a form familiar to modern programming languages, but its implementation means it is not quite the same as in Java or C#. It is important to consider when to use this type of error handling - GError is very specifically designed to deal with recoverable runtime errors, i.e. factors that are not known until the program is run on a live system, and that are not fatal to the execution. You should not use GError for problems that can be foreseen, such as reporting that an invalid value has been passed to a method. If a method, for example, requires a number greater than 0 as a parameter, it should fail on negative values using contract programming techniques such as preconditions or assertions described in the previous section.

Vala errors are so-called *checked exceptions*, which means that errors must get handled at some point. However, if you don't catch an error the Vala compiler will only issue a warning without stopping the compilation process.

Using exceptions (or *errors* in Vala terminology) is a matter of:

1) Declaring that a method may raise an error:

void my_method() throws IOError { }

2) Throwing the error when appropriate:

if (something_went_wrong) { throw new IOError.FILE_NOT_FOUND("Requested file could not be found."); }

3) Catching the error from the calling code:

try { my_method(); } catch (IOError e) { stdout.printf("Error: %s\n", e.message); }

4) Comparing error code by "is" operator IOChannel channel; try { channel = new IOChannel.file("/tmp/my_lock", "w"); } catch (FileError e) { if(e is FileError.EXIST) { throw e; } GLib.error("", e.message); }

All this appears more or less as in other languages, but defining the types of errors allowed is fairly unique. Errors have three components, known as "domain", "code" and message. Messages we have already seen, it is simply a piece of text provided when the error is created. Error domains describe the type of problem, and equates to a subclass of "Exception" in Java or similar. In the above examples we imagined an error domain called "IOError". The third part, the error code is a refinement describing the exact variety of problem encountered. Each error domain has one or more error codes - in the example there is a code called "FILE_NOT_FOUND".

The way to define this information about error types is related to the implementation in glib. In order for the examples here to work, a definition is needed such as:

errordomain IOError { FILE_NOT_FOUND }

When catching an error, you give the error domain you wish to catch errors in, and if an error in that domain is thrown, the code in the handler is run with the error assigned to the supplied name. From that error object you can extract the error code and message as needed. If you want to catch errors from more than one domain, simply provide extra catch blocks. There is also an optional block that can be placed after a try and any catch blocks, called finally. This code is to be run always at the end of the section, regardless of whether an error was thrown or any catch blocks were executed, even if the error was in fact no handled and will be thrown again. This allows, for example, any resources reserved in the try block be freed regardless of any errors raised. A complete example of these features:

public errordomain ErrorType1 { CODE_1A } public errordomain ErrorType2 { CODE_2A, CODE_2B } public class Test : GLib.Object { public static void thrower() throws ErrorType1, ErrorType2 { throw new ErrorType1.CODE_1A("Error"); } public static void catcher() throws ErrorType2 { try { thrower(); } catch (ErrorType1 e) { } finally { } } public static int main(string[] args) { try { catcher(); } catch (ErrorType2 e) { if (e is ErrorType2.CODE_2B) { } } return 0; } }

This example has two error domains, both of which can be thrown by the "thrower" method. Catcher can only throw the second type of error, and so must handle the first type if "thrower" throws it. Finally the "main" method will handle any errors from "catcher".

Parameter Directions

A method in Vala is passed zero or more arguments. The default behaviour when a method is called is as follows: Any value type parameters are copied to a location local to the method as it executes. Any reference type parameters are not copied, instead just a reference to them is passed to the method.

This behaviour can be changed with the modifiers 'ref' and 'out'. 'out' from the caller sideyou may pass an uninitialised variable to the method and you may expect it to be initialised after the method returns 'out' from callee sidethe parameter is considered uninitialised and you have to initialise it 'ref' from caller sidethe variable you're passing to the method has to be initialised and it may be changed or not by the method 'ref' from callee sidethe parameter is considered initialised and you may change it or not

void method_1(int a, out int b, ref int c) { ... } void method_2(Object o, out Object p, ref Object q) { ... }

These methods can be called as follows:

int a = 1; int b; int c = 3; method_1(a, out b, ref c); Object o = new Object(); Object p; Object q = new Object(); method_2(o, out p, ref q);

The treatment of each variable will be: "a" is of a value type. The value will be copied into a new memory location local to the method, and so changes to it will not be visible to the caller. "b" is also of a value type, but passed as an out parameter. In this case, the value is not copied, instead a pointer to the data is passed to the method, and so any change to the method parameter will be visible to the calling code. "c" is treated in the same way as "b", the only change is in the signalled intent of the method. "o" is of a reference type. The method is passed a reference to the same object as the caller has. The method can therefore change that object, but if it reassigns to the parameter, that change will not be visible to the caller. "p" is of the same type, but passed as an out parameter. This means that the method will receive a pointer to the reference to the object. It may therefore replace the reference with a reference to another object, and when the method returns the caller will instead own a reference to that other object. When you use this type of parameter, if you do not assign a new reference to the parameter, it will be set to null. "q" is again of the same type. This case is treated like "p" with the important differences that the method may choose not to change the reference, and may access the object referred to. Vala will ensure that in this instance "q" actually refers to any object, and is not set to null.

Here is an example of how to implement method_1():

void method_1(int a, out int b, ref int c) { b = a + c; c = 3; }

When setting the value to the out argument "b", Vala will ensure that "b" is not null. So you can safely pass null as the second argument of method_1() if you are not interested by this value.

Collections

Gee is a library of collection classes, written in Vala. The classes should all be familiar to users of libraries such as Java's Foundation Classes. Gee consists of a set of interfaces and various types that implement these in different ways.

If you want to use Gee in your own application, install the library separately on your system. Gee can be obtained from http://live.gnome.org/Projects/Libgee. In order to use the library you must compile your programs with --pkg gee-0.8.

The fundamental types of collection are: Lists: Ordered collections of items, accessible by numeric index. Sets: Unordered collections of distinct. Maps: Unordered collection of items, accessible by index of arbitrary type.

All the lists and sets in the library implement the *Collection* interface, and all maps the *Map* interface. Lists also implement *List* and sets *Set*. These common interfaces means not only that all collections of a similar type can be used interchangeably, but also that new collections can be written using the same interfaces, and therefore used with existing code.

Also common to every *Collection* type is the *Iterable* interface. This means that any object in this category can be iterated through using a standard set of methods, or directly in Vala using the foreach syntax.

All classes and interfaces use the generics system. This means that they must be instantiated with a particular type or set of types that they will contain. The system will ensure that only the intended types can be put into the collections, and that when objects are retrieved they are returned as the correct type.

Full Gee API documentation, Gee Examples

Some important Gee classes are:

ArrayList<G>

Implementing: Iterable<G>, Collection<G>, List<G>

An ordered list of items of type G backed by a dynamically resizing array. This type is very fast for accessing data, but potentially slow at inserting items anywhere other than at the end, or at inserting items when the internal array is full.

HashMap<K,V>

Implementing: Iterable<Entry<K,V>>, Map<K,V>

A 1:1 map from elements of type K to elements of type V. The mapping is made by computing a hash value for each key - this can be customised by providing pointers to functions for hashing and testing equality of keys in specific ways.

You can optionally pass custom hash and equal functions to the constructor, for example:

var map = new Gee.HashMap<Foo, Object>(foo_hash, foo_equal);

For strings and integers the hash and equal functions are detected automatically, objects are distinguished by their references by default. You have to provide custom hash and equal functions only if you want to override the default behaviour.

HashSet<G>

Implementing: Iterable<G>, Collection<G>, Set<G>

A set of elements of type G. Duplicates are detected by computing a hash value for each key - this can be customised by providing pointers to functions for hashing and testing equality of keys in specific ways.

Read-Only Views

You can get a read-only view of a collection via the *read_only_view* property, e.g. my_map.read_only_view. This will return a wrapper that has the same interface as its contained collection, but will not allow any form of modification, or any access to the contained collection.

Methods With Syntax Support

Vala recognizes some methods with certain names and signatures and provides syntax support for them. For example, if a type has a *contains()* method objects of this type can be used with the in operator. The following table lists these special methods. *T* and *Tn* are only type placeholders in this table and meant to be replaced with real types. **Indexers** T2 get(T1 index) index access: obj[index] void set(T1 index, T2 item) index assignment: obj[index] = item **Indexers with multiple indices** T3 get(T1 index1, T2 index2) index access: obj[index1, index2] void set(T1 index1, T2 index2, T3 item) index assignment: obj[index1, index2] = item (... and so on for more indices) **Others** T slice(long start, long end) slicing: obj[start:end] bool contains(T needle) in operator: bool b = needle in obj string to_string() support within string templates: @"$obj" Iterator iterator() iterable via foreach T2 get(T1 index) T1 size { get; } iterable via foreach

The *Iterator* type can have any name and must implement one of these two protocols: bool next() T get() standard iterator protocol: iterating until *.next()* returns false. The current element is retrieved via *.get()*. T? next_value() alternative iterator protocol: If the iterator object has a *.next_value()* function that returns a nullable type then we iterate by calling this function until it returns null.

This example implements some of these methods:

public class EvenNumbers { public int get(int index) { return index * 2; } public bool contains(int i) { return i % 2 == 0; } public string to_string() { return "[This object enumerates even numbers]"; } public Iterator iterator() { return new Iterator(this); } public class Iterator { private int index; private EvenNumbers even; public Iterator(EvenNumbers even) { this.even = even; } public bool next() { return true; } public int get() { this.index++; return this.even[this.index - 1]; } } } void main() { var even = new EvenNumbers(); stdout.printf("%d\n", even[5]); if (4 in even) { stdout.printf(@"$even\n"); } foreach (int i in even) { stdout.printf("%d\n", i); if (i == 20) break; } }

Multi-Threading

Threads in Vala

A program written in Vala may have more than one thread of execution, allowing it it do more than one thing at a time. Exactly how this is managed is outside of Vala's scope - threads may be sharing a single processor core or not, depending on the environment.

A very simplified example:

void thread_func() { stdout.printf("child_thread is running.\n"); } void main() { if (!Thread.supported()) { error("Cannot run without thread support.\n"); } var thread = new Thread<void> ("child_thread", thread_func); stdout.printf("main_thread is running"); }

Note the test at the start of the main method. Originally, UNIX did not have threads, which means some traditional UNIX APIs are problematic in threaded programs. Using this test could check whether the currnt environment supports threads. In most cases, it can be omitted.

Now look at the following statement:

var thread = new Thread<void> ("new_thread", thread_func);

We create a new thread and it will start immediately. The first argument is its name,the second one is the content of the new thread. The generic parameter is the type of value which a thread returns.

The program will still not act as we expected, because we just Without any sort of event loop, a Vala program will terminate when its primary/root/parent thread (the one created to run "main") ends. In order to control this behaviour, you can allow threads to cooperate. This can be done powerfully using event loops and asynchronous queues, but in this introduction to threading we will just show the basic capabilities of threads.

The child thread will be killed if its primary/parent thread has finished According to this fact, we should tell the primary thread to wait for child threads to finish, by invoking a method join in module Thread.

var thread = new Thread<void> ("child_thread", thread_func); stdout.printf("main_thread is running"); thread.join();

Because of the method join, the primary thread has to wait for child thread to finish.

What's more, it is possible for a thread to tell the system that it currently has no need to execute, and thereby suggest that another thread should be run instead, this is done using the static method *Thread.yield()*. If this statement was placed at the end of the above *main* method, the runtime system will pause the main thread for an instant and check if there are other threads that can be run - on finding the newly created thread in a runnable state, it will run that instead until it is finished - and the program will act is it appears it should. However, there is no guarantee that this will happen still. The system is able to decide when threads run, and as such might not allow the new thread to finish before the primary thread is restarted and the program ends.

All these examples have a potential problem, in that the newly created thread doesn't know the context in which it should run. In C you would supply the thread creation method with some data, in Vala instead you would normally pass an instance method, instead of a static method.

More samples in Thread Samples

Resource Control

Whenever more than one thread of execution is running simultaneously, there is a chance that data are accessed simultaneously. This can lead to race conditions, where the outcome depends on when the system decides to switch between threads.

In order to control this situation, you can use the lock keyword to ensure that certain blocks of code will not be interrupted by other threads that need to access the same data. The best way to show this is probably with an example:

public class Test : GLib.Object { private int a { get; set; } public void action_1() { lock (a) { int tmp = a; tmp++; a = tmp; } } public void action_2() { lock (a) { int tmp = a; tmp--; a = tmp; } } }

This class defines two methods, where both need to change the value of "a". If there were no lock statements here, it would be possible for the instructions in these methods to be interweaved, and the resulting change to "a" would be effectively random. As there are the lock statements here, Vala will guarantee that if one thread has locked "a", another thread that needs the same lock will have to wait its turn.

In Vala it is only possible to lock members of the object that is executing the code. This might appear to be a major restriction, but in fact the standard use for this technique should involve classes that are individually responsible for controlling a resource, and so all locking will indeed be internal to the class. Likewise, in above example all accesses to "a" are encapsulated in the class.

The Main Loop

GLib includes a system for running an event loop, in the classes around MainLoop. The purpose of this system is to allow you to write a program that waits for events and responds to them, instead of having to constantly check conditions. This is the model that GTK+ uses, so that a program can wait for user interaction without having to have any currently running code.

The following program creates and starts a MainLoop, and then attaches a source of events to it. In this case the source is a simple timer, that will execute the given method after 2000ms. The method will in fact just stop the main loop, which will in this case exit the program.

void main() { var loop = new MainLoop(); var time = new TimeoutSource(2000); time.set_callback(() => { stdout.printf("Time!\n"); loop.quit(); return false; }); time.attach(loop.get_context()); loop.run(); }

When using GTK+, a main loop will be created automatically, and will be started when you call the `Gtk.main()' method. This marks the point where the program is ready to run and start accepting events from the user or elsewhere. The code in GTK+ is equivalent to the short example above, and so you may add event sources in much the same way, although of course you need to use the GTK+ methods to control the main loop.

void main(string[] args) { Gtk.init(ref args); var time = new TimeoutSource(2000); time.set_callback(() => { stdout.printf("Time!\n"); Gtk.main_quit(); return false; }); time.attach(null); Gtk.main(); }

A common requirement in GUI programs is to execute some code as soon as possible, but only when it will not disturb the user. For this, you use IdleSource instances. These send events to the programs main loop, but request they only be dealt with when there is nothing more important to do.

For more information about event loops, see the GLib and GTK+ documentation.

Asynchronous Methods

Asynchronous methods are methods whose execution can be paused and resumed under the control of the programmer. They are often used in the main thread of an application where a method needs to wait for an external slow task to complete, but must not stop other processing from happening. (For example, one slow operation must not freeze the whole GUI). When the method has to wait, it gives control of the CPU back to its caller (i.e. it *yields*), but it arranges to be called back to resume execution when data becomes ready. External slow tasks that async methods might wait for include: waiting for data from a remote server, or waiting for calculations in another thread to complete, or waiting for data to load from a disk drive.

Asynchronous methods are normally used with a GLib main loop running, because idle callbacks are used to handle some of the internal callbacks. However under certain conditions async may be used without the GLib main loop, for example if the async methods always yield and Idle.add() is never used. (FIXME: Check what are the exact conditions.)

Asynchronous methods are designed for interleaving the processing of many different long-lived operations within a single thread. They do not by themselves spread the load out over different threads. However, an async method may be used to control a background thread and to wait for it to complete, or to queue operations for a background thread to process.

Async methods in Vala use the GIO library to handle the callbacks, so must be built with the --pkg=gio-2.0 option.

An asynchronous method is defined with the async keyword. For example:

async void display_jpeg(string fnam) { [...] }

or:

async int fetch_webpage(string url, out string text) throws IOError { [...] text = result; return status; }

The method may take arguments and return a value like any other method. It may use a yield statement at any time to give control of the CPU back to its caller.

An async method may be called with either of these two forms:

display_jpeg.begin("test.jpg"); display_jpeg.begin("test.jpg", (obj, res) => { display_jpeg.end(res); });

Both forms starts the async method running with the given arguments. The second form in addition registers an AsyncReadyCallback which is executed when the method finishes. The callback takes a source object, obj, and an instance of GAyncResult, res, as arguments. In the callback the .end() method should be called to receive the return value of the asynchronous method if it has one. If the async method can throw an exception, the .end() call is where the exception arrives and must be caught. If the method has out arguments, then these should be omitted from the .begin() call and added to the .end() call instead.

For example:

fetch_webpage.begin("http://www.example.com/", (obj, res) => { try { string text; var status = fetch_webpage.end(res, out text); } catch (IOError e) { } });

When an asynchronous method starts running, it takes control of the CPU until it reaches its first yield statement, at which point it returns to the caller. When the method is resumed, it continues execution immediately after that yield statement. There are several common ways to use yield:

This form gives up control, but arranges for the GLib main loop to resume the method when there are no more events to process:

Idle.add(fetch_webpage.callback); yield;

This form gives up control, and stores the callback details for some other code to use to resume the method's execution:

SourceFunc callback = fetch_webpage.callback; [... store 'callback' somewhere ...] yield;

Some code elsewhere must now call the stored SourceFunc in order for the method to be resumed. This could be done by scheduling the GLib main loop to run it:

Idle.add((owned) callback);

or alternatively a direct call may be made if the caller is running in the main thread:

callback();
