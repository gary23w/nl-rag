---
title: "Objective-C"
source: https://en.wikipedia.org/wiki/Objective-C
domain: objective-c
license: CC-BY-SA-4.0
tags: objective-c, objective c, cocoa framework, nsobject
fetched: 2026-07-02
---

# Objective-C

**Objective-C** is a high-level general-purpose, object-oriented programming language that adds Smalltalk-style message passing (messaging) to the C programming language. Originally developed by Brad Cox and Tom Love in the early 1980s, it was selected by NeXT for its NeXTSTEP operating system. Due to Apple macOS’s direct lineage from NeXTSTEP, Objective-C was the standard language used, supported, and promoted by Apple for developing macOS and iOS applications (via their respective application programming interfaces (APIs), Cocoa and Cocoa Touch) from 1997, when Apple purchased NeXT, until the introduction of the Swift language in 2014.

Objective-C programs developed for non-Apple operating systems or that are not dependent on Apple's APIs may also be compiled for any platform supported by GNU, GNU Compiler Collection (GCC) or LLVM/Clang.

Objective-C source code "messaging/implementation" program files usually have `.m` filename extensions, while Objective-C "header/interface" files have `.h` extensions, the same as C header files. Objective-C++ files are denoted with a `.mm` filename extension.

## History

Objective-C was created mainly by Brad Cox and Tom Love in the early 1980s at their company Productivity Products International (PPI).

Leading up to the creation of their company, both had been introduced to Smalltalk while at ITT Corporation's Programming Technology Center in 1981. The earliest work on Objective-C traces back to around then. Cox was intrigued by problems of true reusability in software design and programming. He realized that a language like Smalltalk would be invaluable in building development environments for system developers at ITT. However, he and Tom Love also recognized that backward compatibility with C was critically important in ITT's telecom engineering milieu.

Cox began writing a pre-processor for C to add some of the abilities of Smalltalk. He soon had a working implementation of an object-oriented extension to the C language, which he named Object-Oriented Pre-Compiler (OOPC). Love was hired by Schlumberger Research in 1982 and had the opportunity to acquire the first commercial copy of Smalltalk-80, which further influenced the development of their brainchild. To demonstrate that real progress could be made, Cox showed that making interchangeable software components really needed only a few practical changes to existing tools. Specifically, they needed to support objects in a flexible manner, come supplied with a usable set of libraries, and allow for the code (and any resources needed by the code) to be bundled into one cross-platform format.

Love and Cox eventually formed PPI to commercialize their product. To avoid legal disputes with his previous employers, Cox reimplemented his compiler for the language, which was renamed "Objective-C". The company's main product line consisted of this compiler, along with class libraries intended to be used with it. In 1986, Cox published the main description of Objective-C in its original form in the book *Object-Oriented Programming: An Evolutionary Approach*. Although he was careful to explain that there is more to the problem of reusability than just what Objective-C provides, the language was often compared feature for feature with other languages.

### Popularization through NeXT

In 1988, NeXT licensed Objective-C from StepStone (the new name of PPI, the owner of the Objective-C trademark) and extended the GCC compiler to support Objective-C. NeXT developed the Application Kit (AppKit) and Foundation Kit libraries on which the NeXTSTEP user interface and Interface Builder were based. While the NeXT workstations failed to make a great impact in the marketplace, the tools were widely lauded in the industry. NeXT dropped hardware production and focused on software tools, selling NeXTSTEP (and OPENSTEP) as a platform for custom programming.

To circumvent the terms of the GPL, NeXT had originally intended to ship the Objective-C frontend separately, allowing the user to link it with GCC to produce the compiler executable. Though initially accepted by Richard M. Stallman, this plan was rejected after Stallman consulted with GNU's lawyers and NeXT agreed to make Objective-C part of GCC.

The work to extend GNU Compiler Collection (GCC) was led by Steve Naroff, who joined NeXT from StepStone. The compiler changes were made available as per GNU General Public License (GPL) terms, but the runtime libraries were not, rendering the open source contribution unusable to the general public. This led to other parties developing such runtime libraries under open source licenses. Later, Steve Naroff was also principal contributor to work at Apple to build the Objective-C frontend to Clang.

The GNU project started work on its free software implementation of Cocoa, named GNUstep, based on the OpenStep standard. Dennis Glatting wrote the first GNU Objective-C runtime in 1992. The current GNU Objective-C runtime, in use since 1993, is the one developed by Kresten Krab Thorup while he was a university student in Denmark. Thorup also worked at NeXT from 1993 to 1996.

### Apple development and Swift

After acquiring NeXT in 1996, Apple Computer used OpenStep in its then-new operating system, Mac OS X. This included Objective-C, NeXT's Objective-C-based developer tool, Project Builder, and its interface design tool, Interface Builder. Both were later merged into one application, Xcode. Most of Apple's current Cocoa API is based on OpenStep interface objects and is the most significant Objective-C environment being used for active development.

At Worldwide Developers Conference (WWDC) 2014, Apple introduced a new language, Swift, which was characterized as "Objective-C without the C".

## Syntax

Objective-C is a thin layer atop C and is a "strict superset" of C, meaning that it is possible to compile any C program with an Objective-C compiler and to freely include C language code within an Objective-C class.

Objective-C derives its object syntax from Smalltalk. All of the syntax for non-object-oriented operations (including primitive variables, pre-processing, expressions, function declarations, and function calls) are identical to those of C, while the syntax for object-oriented features is an implementation of Smalltalk-style messaging.

### Messages

The Objective-C model of object-oriented programming is based on message passing to object instances. In Objective-C, one does not *call a method*; one *sends a message*. This is unlike the Simula-style programming model used by C++. The difference between these two concepts is in how the code referenced by the method or message name is executed. In a Simula-style language, the method name is—in most cases—bound to a section of code in the target class by the compiler. In Smalltalk and Objective-C, the target of a message is resolved at runtime, with the receiving object itself interpreting the message. A method is identified by a *selector* or `SEL` — a unique identifier for each message name, often just a `NUL`-terminated string representing its name—and resolved to a C method pointer implementing it: an `IMP`. A consequence of this is that the message-passing system has no type checking. The object to which the message is directed—the *receiver*—is not guaranteed to respond to a message, and if it does not, it raises an exception.

Sending the message `method` to the object pointed to by the pointer `obj` would require the following code in C++:

```mw
obj->method(argument);
```

In Objective-C, this is written as follows:

```mw
[obj method:argument];
```

The "method" call is translated by the compiler to the `objc_msgSend(id self, SEL op, ...)` family of runtime functions. Different implementations handle modern additions like `super`. In GNU families, this function is named `objc_msg_sendv`, but it has been deprecated in favor of a modern lookup system under `objc_msg_lookup`.

Both styles of programming have multiple strengths and weaknesses. Object-oriented programming in the Simula (C++) style allows multiple inheritance and faster execution by using compile-time binding whenever possible, but it does not support dynamic binding by default. It also forces all methods to have a corresponding implementation unless they are abstract. The Smalltalk-style programming as used in Objective-C allows messages to go unimplemented, with the method resolved to its implementation at runtime. For example, a message may be sent to a collection of objects, to which only some will be expected to respond, without fear of producing runtime errors. Message passing also does not require that an object be defined at compile time. An implementation is still required for the method to be called in the derived object. (See the dynamic typing section below for more advantages of dynamic (late) binding.)

### Interfaces and implementations

Objective-C requires that the interface and implementation of a class be in separately declared code blocks. By convention, developers place the interface in a header file and the implementation in a code file. The header files, normally suffixed .h, are similar to C header files while the implementation (method) files, normally suffixed .m, can be very similar to C code files.

#### Interface

This is analogous to class declarations as used in other object-oriented languages, such as C++ or Python.

The interface of a class is usually defined in a header file. A common convention is to name the header file after the name of the class, e.g. `Ball.h` would contain the interface for the class `Ball`.

An interface declaration takes the form:

```mw
@interface ClassName : SuperclassName {
  // instance variables
}
+ classMethod1;
+ (return_type)classMethod2;
+ (return_type)classMethod3:(param1_type)param1_varName;

- (return_type)instanceMethod1With1Parameter:(param1_type)param1_varName;
- (return_type)instanceMethod2With2Parameters:(param1_type)param1_varName
                              param2_callName:(param2_type)param2_varName;
@end
```

In the above, plus signs denote class methods, or methods that can be called on the class itself (not on an instance), and minus signs denote instance methods, which can only be called on a particular instance of the class. Class methods also have no access to instance variables.

The code above is roughly equivalent to the following C++ interface:

```mw
class ClassName : public SuperclassName {
protected:
  // instance variables

public:
  // Class (static) functions
  static void *classMethod1();
  static return_type classMethod2();
  static return_type classMethod3(param1_type param1_varName);

  // Instance (member) functions
  return_type instanceMethod1With1Parameter(param1_type param1_varName);
  return_type
  instanceMethod2With2Parameters(param1_type param1_varName,
                                 param2_type param2_varName = default);
};
```

Note that `instanceMethod2With2Parameters:param2_callName:` demonstrates the interleaving of selector segments with argument expressions, for which there is no direct equivalent in C/C++.

Return types can be any standard C type, a pointer to a generic Objective-C object, a pointer to a specific type of object such as NSArray *, NSImage *, or NSString *, or a pointer to the class to which the method belongs (instancetype). The default return type is the generic Objective-C type `id`.

Method arguments begin with a name labeling the argument that is part of the method name, followed by a colon followed by the expected argument type in parentheses and the argument name. The label can be omitted.

```mw
- (void)setRangeStart:(int)start end:(int)end;
- (void)importDocumentWithName:(NSString *)name
      withSpecifiedPreferences:(Preferences *)prefs
                    beforePage:(int)insertPage;
```

A derivative of the interface definition is the *category*, which allows one to add methods to existing classes.

#### Implementation

The interface only declares the class interface and not the methods themselves: the actual code is written in the implementation file. Implementation (method) files normally have the file extension `.m`, which originally signified "messages".

```mw
@implementation classname
+ (return_type)classMethod {
  // implementation
}
- (return_type)instanceMethod {
  // implementation
}
@end
```

Methods are written using their interface declarations. Comparing Objective-C and C:

```mw
- (int)method:(int)i {
  return [self square_root:i];
}
```

```mw
int function(int i) {
  return square_root(i);
}
```

The syntax allows pseudo-naming of arguments.

```mw
- (void)changeColorToRed:(float)red green:(float)green blue:(float)blue {
  //... Implementation ...
}

// Called like so:
[myColor changeColorToRed:5.0 green:2.0 blue:6.0];
```

Internal representations of a method vary between different implementations of Objective-C. If myColor is of the class `Color`, instance method `-changeColorToRed:green:blue:` might be internally labeled `_i_Color_changeColorToRed_green_blue`. The `i` is to refer to an instance method, with the class and then method names appended and colons changed to underscores. As the order of parameters is part of the method name, it cannot be changed to suit coding style or expression as with true named parameters.

However, internal names of the function are rarely used directly. Generally, messages are converted to function calls defined in the Objective-C runtime library. It is not necessarily known at link time which method will be called because the class of the receiver (the object being sent the message) need not be known until runtime.

#### Instantiation

Once an Objective-C class is written, it can be instantiated. This is done by first allocating an uninitialized instance of the class (an object) and then by initializing it. An object is not fully functional until both steps have been completed. These steps should be accomplished with one line of code so that there is never an allocated object that hasn't undergone initialization (and because it is unwise to keep the intermediate result since `-init` can return a different object than that on which it is called).

Instantiation with the default, no-parameter initializer:

```mw
MyObject *foo = [[MyObject alloc] init];
```

Instantiation with a custom initializer:

```mw
MyObject *foo = [[MyObject alloc] initWithString:myString];
```

In the case where no custom initialization is being performed, the "new" method can often be used in place of the alloc-init messages:

```mw
MyObject *foo = [MyObject new];
```

Also, some classes implement class method initializers. Like `+new`, they combine `+alloc` and `-init`, but unlike `+new`, they return an autoreleased instance. Some class method initializers take parameters:

```mw
MyObject *foo = [MyObject object];
MyObject *bar = [MyObject objectWithString:@"Wikipedia :)"];
```

The *alloc* message allocates enough memory to hold all the instance variables for an object, sets all the instance variables to zero values, and turns the memory into an instance of the class; at no point during the initialization is the memory an instance of the superclass.

The *init* message performs the set-up of the instance upon creation. The *init* method is often written as follows:

```mw
- (id)init {
    self = [super init];
    if (self) {
        // perform initialization of object here
    }
    return self;
}
```

In the above example, notice the `id` return type. This type stands for *pointer to any object* in Objective-C (See the Dynamic typing section).

The initializer pattern is used to assure that the object is properly initialized by its superclass before the init method performs its initialization. It performs the following actions:

- Line 2 Sends the superclass instance an `init` message and assigns the result to `self` (pointer to the current object).
- Line 3 Checks if the returned object pointer is valid before performing any initialization.
- Line 6 Returns the value of self to the caller.

A non-valid object pointer has the value `nil`; conditional statements like `if` treat nil like a null pointer, so the initialization code will not be executed if `[super init]` returned nil. If there is an error in initialization, the init method should perform any necessary cleanup, including sending a `release` message to self, and return `nil` to indicate that initialization failed. Any checking for such errors must only be performed after having called the superclass initialization to ensure that destroying the object will be done correctly.

If a class has more than one initialization method, only one of them (the *designated initializer*) needs to follow this pattern; others should call the designated initializer instead of the superclass initializer.

### Protocols

In other programming languages, these are called *interfaces*.

Objective-C was extended at NeXT to introduce the concept of multiple inheritance of specification, but not implementation, through the introduction of protocols. This is a pattern achievable either as an abstract multiple inherited base class in C++, or as an *interface* (as in Java and C#). Objective-C makes use of ad hoc protocols called *informal protocols* and compiler-enforced protocols called *formal protocols*.

An informal protocol is a list of methods that a class can opt to implement. It is specified in the documentation, since it has no presence in the language. Informal protocols are implemented as a category (see below) on NSObject and often include optional methods, which, if implemented, can change the behavior of a class. For example, a text field class might have a delegate that implements an informal protocol with an optional method for performing auto-completion of user-typed text. The text field discovers whether the delegate implements that method (via reflective programming (reflection)) and, if so, calls the delegate's method to support the auto-complete feature.

A formal protocol is similar to an interface in Java, C#, and Ada 2005. It is a list of methods that any class can declare itself to implement. Objective-C versions before 2.0 required that a class must implement all methods in a protocol it declares itself as adopting; the compiler will emit an error if the class does not implement every method from its declared protocols. Objective-C 2.0 added support for marking certain methods in a protocol optional, and the compiler will not enforce implementation of optional methods.

A class must be declared to implement that protocol to be said to conform to it. This is detectable at runtime. Formal protocols cannot provide any implementations; they simply assure callers that classes that conform to the protocol will provide implementations. In the NeXT/Apple library, protocols are frequently used by the Distributed Objects system to represent the abilities of an object executing on a remote system.

The syntax

```mw
@protocol NSLocking
- (void)lock;
- (void)unlock;
@end
```

denotes that there is the abstract idea of locking. By stating in the class definition that the protocol is implemented,

```mw
@interface NSLock : NSObject <NSLocking>
// ...
@end
```

instances of NSLock claim that they will provide an implementation for the two instance methods.

### Dynamic typing

Objective-C, like Smalltalk, can use dynamic typing: an object can be sent a message that is not specified in its interface. This can allow for increased flexibility, as it allows an object to "capture" a message and send the message to a different object that can respond to the message appropriately, or likewise send the message on to another object. This behavior is known as *message forwarding* or *delegation* (see below). Alternatively, an error handler can be used in case the message cannot be forwarded. If an object does not forward a message, respond to it, or handle an error, then the system will generate a runtime exception. If messages are sent to *nil* (the null object pointer), they will be silently ignored or raise a generic exception, depending on compiler options.

Static typing information may also optionally be added to variables. This information is then checked at compile time. In the following four statements, increasingly specific type information is provided. The statements are equivalent at runtime, but the extra information allows the compiler to warn the programmer if the passed argument does not match the type specified.

```mw
- (void)setMyValue:(id)foo;
```

In the above statement, *foo* may be of any class.

```mw
- (void)setMyValue:(id<NSCopying>)foo;
```

In the above statement, *foo* may be an instance of any class that conforms to the *`NSCopying`* protocol.

```mw
- (void)setMyValue:(NSNumber *)foo;
```

In the above statement, *foo* must be an instance of the *NSNumber* class.

```mw
- (void)setMyValue:(NSNumber<NSCopying> *)foo;
```

In the above statement, *foo* must be an instance of the *NSNumber* class, and it must conform to the *`NSCopying`* protocol.

In Objective-C, all objects are represented as pointers, and static initialization is not allowed. The simplest object is the type that id (objc_obj *) points to, which only has an *isa* pointer describing its class. Other types from C, like values and structs, are unchanged because they are not part of the object system. This decision differs from the C++ object model, where structs and classes are united.

### Forwarding

Objective-C permits the sending of a message to an object that may not respond. Rather than responding or simply dropping the message, an object can forward the message to an object that can respond. Forwarding can be used to simplify implementation of certain design patterns, such as the observer pattern or the proxy pattern.

The Objective-C runtime specifies a pair of methods in `Object`

- forwarding methods:- (retval_t)forward:(SEL)sel args:(arglist_t)args; // with GCC - (id)forward:(SEL)sel args:(marg_list)args; // with NeXT/Apple systems
- action methods:- (retval_t)performv:(SEL)sel args:(arglist_t)args; // with GCC - (id)performv:(SEL)sel args:(marg_list)args; // with NeXT/Apple systems

An object wishing to implement forwarding needs only to override the forwarding method with a new method to define the forwarding behavior. The action method `performv::` need not be overridden, as this method merely performs an action based on the selector and arguments. Notice the `SEL` type, which is the type of messages in Objective-C.

Note: in OpenStep, Cocoa, and GNUstep, the commonly used frameworks of Objective-C, one does not use the `Object` class. The `- (void)forwardInvocation:(NSInvocation *)anInvocation` method of the `NSObject` class is used to do forwarding.

#### Example

Here is an example of a program that demonstrates the basics of forwarding.

***Forwarder.h***

```mw
#import <objc/Object.h>

@interface Forwarder : Object {
  id recipient; // The object we want to forward the message to.
}

// Accessor methods.
- (id)recipient;
- (id)setRecipient:(id)_recipient;
@end
```

***Forwarder.m***

```mw
#import "Forwarder.h"

@implementation Forwarder
- (retval_t)forward:(SEL)sel args:(arglist_t)args {
  /*
  * Check whether the recipient actually responds to the message.
  * This may or may not be desirable, for example, if a recipient
  * in turn does not respond to the message, it might do forwarding
  * itself.
  */
  if ([recipient respondsToSelector:sel]) {
    return [recipient performv:sel args:args];
  } else {
    return [self error:"Recipient does not respond"];
  }
}

- (id)setRecipient:(id)_recipient {
  [recipient autorelease];
  recipient = [_recipient retain];
  return self;
}

- (id)recipient {
  return recipient;
}
@end
```

***Recipient.h***

```mw
#import <objc/Object.h>

// A simple Recipient object.
@interface Recipient : Object
- (id)hello;
@end
```

***Recipient.m***

```mw
#import "Recipient.h"

@implementation Recipient

- (id)hello {
  printf("Recipient says hello!\n");

  return self;
}

@end
```

***main.m***

```mw
#import "Forwarder.h"
#import "Recipient.h"

int main(void) {
  Forwarder *forwarder = [Forwarder new];
  Recipient *recipient = [Recipient new];

  [forwarder setRecipient:recipient]; // Set the recipient.
  /*
  * Observe forwarder does not respond to a hello message! It will
  * be forwarded. All unrecognized methods will be forwarded to
  * the recipient
  * (if the recipient responds to them, as written in the Forwarder)
  */
  [forwarder hello];

  [recipient release];
  [forwarder release];

  return 0;
}
```
