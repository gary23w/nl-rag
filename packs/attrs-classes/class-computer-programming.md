---
title: "Class (programming)"
source: https://en.wikipedia.org/wiki/Class_(computer_programming)
domain: attrs-classes
license: CC-BY-SA-4.0
tags: python attrs, attrs classes library, boilerplate class python
fetched: 2026-07-02
---

# Class (programming)

(Redirected from

Class (computer programming)

)

In programming, a **class** is a syntactic entity structure used to create objects. The capabilities of a class differ between programming languages, but generally the shared aspects consist of state (variables) and behavior (methods) that are each either associated with a particular object or with all objects of that class.

Object state can differ between each instance of the class whereas the class state is shared by all of them. The object methods include access to the object state (via an implicit or explicit parameter that references the object) whereas class methods do not.

If the language supports inheritance, a class can be defined based on another class with all of its state and behavior plus additional state and behavior that further specializes the class. The specialized class is a *sub-class*, and the class it is based on is its *superclass*.

In purely object-oriented programming languages, such as Java and C#, all classes might be part of an inheritance tree such that the root class is `Object`, meaning all objects instances are of `Object` or implicitly extend `Object`, which is called a top type.

## History

The concept was introduced mostly in object-oriented programming by the Simula language in the 1960's and has been in continuous use in many programming languages since. Its creation was based in similar concept as block used in prior-based ALGOL 68 programming language.

## Attributes

### Object lifecycle

As an instance of a class, an object is constructed from a class via *instantiation*. Memory is allocated and initialized for the object state and a reference to the object is provided to consuming code. The object is usable until it is destroyed – its state memory is de-allocated.

Most languages allow for custom logic at lifecycle events via a constructor and a destructor.

### Type

An object expresses data type as an interface – the type of each member variable and the signature of each member function (method). A class defines an implementation of an interface, and instantiating the class results in an object that exposes the implementation via the interface. In the terms of type theory, a class is an implementation‍—‌a *concrete* data structure and collection of subroutines‍—‌while a type is an interface. Different (concrete) classes can produce objects of the same (abstract) type (depending on type system). For example, the type (interface) Stack might be implemented by SmallStack that is fast for small stacks but scales poorly and ScalableStack that scales well but has high overhead for small stacks.

### Structure

A class contains data field syntactically described (or *properties*, *fields*, *data members*, or *attributes*). These are usually field types and names that will be associated with state variables at program run time; these state variables either belong to the class or specific instances of the class. In most languages, the structure defined by the class determines the layout of the memory used by its instances. Other implementations are possible: for example, objects in Python use associative key-value containers.

Some programming languages such as Eiffel support specification of invariants as part of the definition of the class, and enforce them through the type system. Encapsulation of state is necessary for being able to enforce the invariants of the class.

### Behavior

The behavior (or action) of a class or its instances is defined using methods. Methods are subroutines with the ability to operate on objects or classes. These operations may alter the state of an object or simply provide ways of accessing it. Many kinds of methods exist, but support for them varies across languages. Some types of methods are created and called by programmer code, while other special methods—such as constructors, destructors, and conversion operators—are created and called by compiler-generated code. A language may also allow the programmer to define and call these special methods.

### Interface

Every class *implements* (or *realizes*) an interface by providing structure and behavior. Structure consists of data and state, and behavior consists of code that specifies how methods are implemented. There is a distinction between the definition of an interface and the implementation of that interface; however, this line is blurred in many programming languages because class declarations both define and implement an interface. Some languages, however, provide features that separate interface and implementation. For example, an abstract class can define an interface without providing an implementation.

Languages that support class inheritance also allow classes to inherit interfaces from the classes that they are derived from.

For example, if "`class Z`" inherits from "`class Y`" and if "`class Y`" implements the interface "`interface X`" then "`class Z`" also implements the functionality(constants and methods declaration) provided by "`interface X`".

In languages that support access specifiers, the interface of a class is considered to be the set of public members of the class, including both methods and attributes (via implicit getter and setter methods); any private members or internal data structures are not intended to be depended on by external code and thus are not part of the interface.

Object-oriented programming methodology dictates that the operations of any interface of a class are to be independent of each other. It results in a layered design where clients of an interface use the methods declared in the interface. An interface places no requirements for clients to invoke the operations of one interface in any particular order. This approach has the benefit that client code can assume that the operations of an interface are available for use whenever the client has access to the object.

#### Interface example

The buttons on the front of your television set are the interface between you and the electrical wiring on the other side of its plastic casing. You press the "power" button to toggle the television on and off. In this example, your particular television is the instance, each method is represented by a button, and all the buttons together compose the interface (other television sets that are the same model as yours would have the same interface). In its most common form, an interface is a specification of a group of related methods without any associated implementation of the methods.

A television set also has a myriad of *attributes*, such as size and whether it supports color, which together comprise its structure. A class represents the full description of a television, including its attributes (structure) and buttons (interface).

Getting the total number of televisions manufactured could be a *static method* of the television class. This method is associated with the class, yet is outside the domain of each instance of the class. A static method that finds a particular instance out of the set of all television objects is another example.

### Member accessibility

The following is a common set of access specifiers:

- *Private* (or *class-private*) restricts access to the class itself. Only methods that are part of the same class can access private members.
- *Protected* (or *class-protected*) allows the class itself and all its subclasses to access the member.
- *Public* means that any code can access the member by its name.

Although many object-oriented languages support the above access specifiers, their semantics may differ.

Object-oriented design uses the access specifiers in conjunction with careful design of public method implementations to enforce class invariants—constraints on the state of the objects. A common usage of access specifiers is to separate the internal data of a class from its interface: the internal structure is made private, while public accessor methods can be used to inspect or alter such private data.

Access specifiers do not necessarily control *visibility*, in that even private members may be visible to client external code. In some languages, an inaccessible but visible member may be referred to at runtime (for example, by a pointer returned from a member function), but an attempt to use it by referring to the name of the member from the client code will be prevented by the type checker.

The various object-oriented programming languages enforce member accessibility and visibility to various degrees, and depending on the language's type system and compilation policies, enforced at either compile time or runtime. For example, the Java language does not allow client code that accesses the private data of a class to compile. In the C++ language, private methods are visible, but not accessible in the interface; however, they may be made invisible by explicitly declaring fully abstract classes that represent the interfaces of the class.

Some languages feature other accessibility schemes:

- *Instance vs. class accessibility*: Ruby supports *instance-private* and *instance-protected* access specifiers in lieu of class-private and class-protected, respectively. They differ in that they restrict access based on the instance itself, rather than the instance's class.
- *Friend*: C++ supports a mechanism where a function explicitly declared as a friend function of the class may access the members designated as private or protected.
- *Path-based*: Java supports restricting access to a member within a Java package, which is the logical path of the file. However, it is a common practice when extending a Java framework to implement classes in the same package as a framework class to access protected members. The source file may exist in a completely different location, and may be deployed to a different .jar file, yet still be in the same logical path as far as the JVM is concerned.

#### Inheritance

Conceptually, a superclass is a superset of its subclasses. For example, `GraphicObject` could be a superclass of `Rectangle` and `Ellipse`, while `Square` would be a subclass of `Rectangle`. These are all subset relations in set theory as well, i.e., all squares are rectangles but not all rectangles are squares.

A common conceptual error is to mistake a *part of* relation with a subclass. For example, a car and truck are both kinds of vehicles and it would be appropriate to model them as subclasses of a vehicle class. However, it would be an error to model the parts of the car as subclass relations. For example, a car is composed of an engine and body, but it would not be appropriate to model an engine or body as a subclass of a car.

In object-oriented modeling these kinds of relations are typically modeled as object properties. In this example, the `Car` class would have a property called `parts`. `parts` would be typed to hold a collection of objects, such as instances of `Body`, `Engine`, `Tires`, etc. Object modeling languages such as UML include capabilities to model various aspects of "part of" and other kinds of relations – data such as the cardinality of the objects, constraints on input and output values, etc. This information can be utilized by developer tools to generate additional code besides the basic data definitions for the objects, such as error checking on get and set methods.

One important question when modeling and implementing a system of object classes is whether a class can have one or more superclasses. In the real world with actual sets, it would be rare to find sets that did not intersect with more than one other set. However, while some systems such as Flavors and CLOS provide a capability for more than one parent to do so at run time introduces complexity that many in the object-oriented community consider antithetical to the goals of using object classes in the first place. Understanding which class will be responsible for handling a message can get complex when dealing with more than one superclass. If used carelessly this feature can introduce some of the same system complexity and ambiguity classes were designed to avoid.

Most modern object-oriented languages such as Smalltalk and Java require single inheritance at run time. For these languages, multiple inheritance may be useful for modeling but not for an implementation.

However, semantic web application objects do have multiple superclasses. The volatility of the Internet requires this level of flexibility and the technology standards such as the Web Ontology Language (OWL) are designed to support it.

A similar issue is whether or not the class hierarchy can be modified at run time. Languages such as Flavors, CLOS, and Smalltalk all support this feature as part of their meta-object protocols. Since classes are themselves first-class objects, it is possible to have them dynamically alter their structure by sending them the appropriate messages. Other languages that focus more on strong typing such as Java and C++ do not allow the class hierarchy to be modified at run time. Semantic web objects have the capability for run time changes to classes. The rationale is similar to the justification for allowing multiple superclasses, that the Internet is so dynamic and flexible that dynamic changes to the hierarchy are required to manage this volatility.

Although many class-based languages support inheritance, inheritance is not an intrinsic aspect of classes. An object-based language (i.e. Classic Visual Basic) supports classes yet does not support inheritance.

## Inter-class relationships

A programming language may support various class relationship features.

### Compositional

Classes can be composed of other classes, thereby establishing a compositional relationship between the enclosing class and its embedded classes. Compositional relationship between classes is also commonly known as a *has-a* relationship. For example, a class `Car` could be composed of and contain a class `Engine`. Therefore, a `Car` *has an* `Engine`. One aspect of composition is containment, which is the enclosure of component instances by the instance that has them. If an enclosing object contains component instances by value, the components and their enclosing object have a similar lifetime. If the components are contained by reference, they may not have a similar lifetime. For example, in Objective-C 2.0:

```mw
@interface Car : NSObject

@property NSString *name;
@property Engine *engine
@property NSArray *tires;

@end
```

This Car class *has* an instance of NSString (a string object), Engine, and NSArray (an array object).

### Hierarchical

Classes can be *derived* from one or more existing classes, thereby establishing a hierarchical relationship between the derived-from classes (*base classes*, *parent classes* or *superclasses*) and the derived class (*child class* or *subclass*) . The relationship of the derived class to the derived-from classes is commonly known as an *is-a* relationship. For example, a class 'Button' could be derived from a class 'Control'. Therefore, a Button *is a* Control. Structural and behavioral members of the parent classes are *inherited* by the child class. Derived classes can define additional structural members (data fields) and behavioral members (methods) in addition to those that they *inherit* and are therefore *specializations* of their superclasses. Also, derived classes can override inherited methods if the language allows.

Not all languages support multiple inheritance. For example, Java allows a class to implement multiple interfaces, but only inherit from one class. If multiple inheritance is allowed, the hierarchy is a directed acyclic graph (or DAG for short), otherwise it is a tree. The hierarchy has classes as nodes and inheritance relationships as links. Classes in the same level are more likely to be associated than classes in different levels. The levels of this hierarchy are called layers or levels of abstraction.

Example (Simplified Objective-C 2.0 code, from iPhone SDK):

```mw
@interface UIResponder : NSObject //...
@interface UIView : UIResponder //...
@interface UIScrollView : UIView //...
@interface UITableView : UIScrollView //...
```

In this example, a UITableView *is a* UIScrollView *is a* UIView *is a* UIResponder *is an* NSObject.

### Modeling

In object-oriented analysis and in Unified Modelling Language (UML), an association between two classes represents a collaboration between the classes or their corresponding instances. Associations have direction; for example, a bi-directional association between two classes indicates that both of the classes are aware of their relationship. Associations may be labeled according to their name or purpose.

An association role is given end of an association and describes the role of the corresponding class. For example, a "subscriber" role describes the way instances of the class "Person" participate in a "subscribes-to" association with the class "Magazine". Also, a "Magazine" has the "subscribed magazine" role in the same association. Association role multiplicity describes how many instances correspond to each instance of the other class of the association. Common multiplicities are "0..1", "1..1", "1..*" and "0..*", where the "*" specifies any number of instances.

## Taxonomy

There are many categories of classes, some of which overlap.

### Abstract and concrete

In a language that supports inheritance, an **abstract class**, or **abstract base class** (**ABC**), is a class that cannot be directly instantiated. By contrast, a **concrete class** is a class that *can* be directly instantiated. Instantiation of an abstract class can occur only indirectly, via a concrete *sub*class.

An abstract class is either labeled as such explicitly or it may simply specify *abstract methods* (or *virtual methods*). An abstract class may provide implementations of some methods, and may also specify virtual methods via signatures that are to be implemented by direct or indirect descendants of the abstract class. Before a class derived from an abstract class can be instantiated, all abstract methods of its parent classes must be implemented by some class in the derivation chain.

Most object-oriented programming languages allow the programmer to specify which classes are considered abstract and will not allow these to be instantiated. For example, in Java, C# and PHP, the reserved word (keyword) `abstract` is used. In C++, an abstract class is a class having at least one abstract method given by the appropriate syntax in that language (a pure virtual function in C++ parlance).

A class consisting of only pure virtual methods is called a *pure abstract base class* (or *pure ABC*) in C++ and is also known as an *interface* by users of the language. Other languages, notably Java and C#, support a variant of abstract classes called an interface via a keyword in the language. In these languages, multiple inheritance is not allowed, but a class can implement multiple interfaces. Such a class can only contain abstract publicly accessible methods.

### Local and inner

In some languages, classes can be declared in scopes other than the global scope. There are various types of such classes.

An *inner class* is a class defined within another class. The relationship between an inner class and its containing class can also be treated as another type of class association. An inner class is typically neither associated with instances of the enclosing class nor instantiated along with its enclosing class. Depending on the language, it may or may not be possible to refer to the class from outside the enclosing class. A related concept is *inner types*, also known as *inner data type* or *nested type*, which is a generalization of the concept of inner classes. C++ is an example of a language that supports both inner classes and inner types (via *typedef* declarations).

A *local class* is a class defined within a procedure or function. Such structure limits references to the class name to within the scope where the class is declared. Depending on the semantic rules of the language, there may be additional restrictions on local classes compared to non-local ones. One common restriction is to disallow local class methods to access local variables of the enclosing function. For example, in C++, a local class may refer to static variables declared within its enclosing function, but may not access the function's automatic variables.

### Metaclass

A metaclass is a class where instances are classes. A metaclass describes a common structure of a collection of classes and can implement a design pattern or describe particular kinds of classes. Metaclasses are often used to describe frameworks.

In some languages, such as Python, Ruby or Smalltalk, a class is also an object; thus each class is an instance of a unique metaclass that is built into the language. The Common Lisp Object System (CLOS) provides metaobject protocols (MOPs) to implement those classes and metaclasses.

### Final

A **final class** cannot be subclassed. It is basically the opposite of an abstract class, which must be subclassed to be used and cannot be instantiated directly. A final class is implicitly a concrete class, *can* be instantiated directly.

A class is declared as final via the keyword `final` in Java, C++ or PHP, or `sealed` in C#. However, this concept should not be confused with classes in Java qualified with the keyword `sealed`, that only allow inheritance from selected subclasses. In languages like Kotlin, all classes are final by default, while to allow a class to be inherited from, it must instead be marked `open`.

For example, Java's `String` class is marked as `final`.

Final classes may allow a compiler to perform optimizations that are not available for classes that can be subclassed.

### Sealed

A "sealed class" is a class that restricts inheritance to a selected list of classes. It should not be confused with the `sealed` keyword in C#, which denotes a final class. The list of permitted classes the sealed class may inherit is specified using a `permits` clause.

```mw
public sealed class Quadrilateral 
    extends Shape 
    implements Renderable, Transformable, Comparable<Quadrilateral>, Measurable
    permits Parallelogram, Trapezoid, Kite {
    // ...
}
```

`non-sealed` is another keyword used to declare that a class or interface which extends a sealed class can be extended by unknown classes.

```mw
sealed class Parallelogram extends Quadrilateral { /* ... */ }
sealed class Rectangle extends Parallelogram { /* ... */ }

non-sealed class Square extends Rectangle { /* ... */ }

// Because Square is non-sealed, any class can inherit from it
class RedSquare extends Square { /* ... */ }
```

### Open

An open class can be changed. Typically, an executable program cannot be changed by customers. Developers can often change some classes, but typically cannot change standard or built-in ones. In Ruby, all classes are open. In Python, classes can be created at runtime, and all can be modified afterward. Objective-C categories permit the programmer to add methods to an existing class without the need to recompile that class or even have access to its source code.

### Mixin

Some languages have special support for mixins, though, in any language with multiple inheritance, a mixin is simply a class that does not represent an is-a-type-of relationship. Mixins are typically used to add the same methods to multiple classes; for example, a class `UnicodeConversionMixin` might provide a method called `unicodeToAscii()` when included in classes `FileReader` and `WebPageScraper` that do not share a common parent.

### Partial

In languages supporting the feature, a *partial class* is a class whose definition may be split into multiple pieces, within a single source-code file or across multiple files. The pieces are merged at compile time, making compiler output the same as for a non-partial class.

The primary motivation for the introduction of partial classes is to facilitate the implementation of code generators, such as visual designers. It is otherwise a challenge or compromise to develop code generators that can manage the generated code when it is interleaved within developer-written code. Using partial classes, a code generator can process a separate file or coarse-grained partial class within a file, and is thus alleviated from intricately interjecting generated code via extensive parsing, increasing compiler efficiency and eliminating the potential risk of corrupting developer code. In a simple implementation of partial classes, the compiler can perform a phase of precompilation where it "unifies" all the parts of a partial class. Then, compilation can proceed as usual.

Other benefits and effects of the partial class feature include:

- Enables separation of a class's interface and implementation code in a unique way.
- Eases navigation through large classes within an editor.
- Enables separation of concerns, in a way similar to aspect-oriented programming but without using any extra tools.
- Enables multiple developers to work on a single class concurrently without the need to merge individual code into one file at a later time.

Partial classes have existed in Smalltalk under the name of *Class Extensions* for considerable time. With the arrival of the .NET framework 2, Microsoft introduced partial classes, supported in both C# 2.0 and Visual Basic 2005. WinRT also supports partial classes.

### Uninstantiable

*Uninstantiable classes* allow programmers to group together per-class fields and methods that are accessible at runtime without an instance of the class. Indeed, instantiation is prohibited for this kind of class.

For example, in C#, a class marked `static` can not be instantiated, can only have static members (fields, methods, other), may not have *instance constructors*, and is `sealed` (is final).

### Unnamed

An *unnamed class* or *anonymous class* is not bound to a name or identifier upon definition. This is analogous to named versus unnamed functions.

```mw
interface Greeting {
    void sayHello();
}

// Anonymous class that implements Greeting
Greeting myGreeting = new Greeting() {
    @Override
    public void sayHello() {
        System.out.println("Hello from an anonymous class!");
    }
};

myGreeting.sayHello();
```

## Benefits

The benefits of organizing software into object classes fall into three categories:

- Rapid development
- Ease of maintenance
- Reuse of code and designs

Object classes facilitate rapid development because they lessen the semantic gap between the code and the users. System analysts can talk to both developers and users using essentially the same vocabulary, talking about accounts, customers, bills, etc. Object classes often facilitate rapid development because most object-oriented environments come with powerful debugging and testing tools. Instances of classes can be inspected at run time to verify that the system is performing as expected. Also, rather than get dumps of core memory, most object-oriented environments have interpreted debugging capabilities so that the developer can analyze exactly where in the program the error occurred and can see which methods were called to which arguments and with what arguments.

Object classes facilitate ease of maintenance via encapsulation. When developers need to change the behavior of an object they can localize the change to just that object and its component parts. This reduces the potential for unwanted side effects from maintenance enhancements.

Software reuse is also a major benefit of using Object classes. Classes facilitate re-use via inheritance and interfaces. When a new behavior is required it can often be achieved by creating a new class and having that class inherit the default behaviors and data of its superclass and then tailoring some aspect of the behavior or data accordingly. Re-use via interfaces (also known as methods) occurs when another object wants to invoke (rather than create a new kind of) some object class. This method for re-use removes many of the common errors that can make their way into software when one program re-uses code from another.

## Runtime representation

As a data type, a class is usually considered as a compile time construct. A language or library may also support prototype or factory metaobjects that represent runtime information about classes, or even represent metadata that provides access to reflective programming (reflection) facilities and ability to manipulate data structure formats at runtime. Many languages distinguish this kind of run-time type information about classes from a class on the basis that the information is not needed at runtime. Some dynamic languages do not make strict distinctions between runtime and compile time constructs, and therefore may not distinguish between metaobjects and classes.

For example, if Human is a metaobject representing the class Person, then instances of class Person can be created by using the facilities of the Human metaobject.

## Class-based programming

**Class-based programming**, or more commonly **class-orientated**, is a style of object-oriented programming which all objects are created by a class and without inheritance between them.

The most popular and developed model of OOP is a class-based model, instead of an object-based model. In this model, objects are entities that combine *state* (i.e., data), *behavior* (i.e., procedures, or *methods*) and *identity* (unique existence among all other objects). The structure and behavior of an object are defined by a class, which is a syntactic structure, or blueprint, of all objects of a specific type. An object must be explicitly created based on a class and an object thus created is considered to be an instance of that class. An object is similar to a structure, with the addition of method pointers, member access control, and an implicit data member which locates instances of the class (i.e., objects of the class) in the class hierarchy (essential for runtime inheritance features).

### Encapsulation

Encapsulation prevents users from breaking the invariants of the class, which is useful because it allows the implementation of a class of objects to be changed for aspects not exposed in the interface without impact to user code. The definitions of encapsulation focus on the grouping and packaging of related information (cohesion) rather than security issues.

### Critique

Class-based languages, or, to be more precise, typed languages, where subclassing is the only way of subtyping, have been criticized for mixing up implementations and interfaces—the essential principle in object-oriented programming. The critics say one might create a bag class that stores a collection of objects, then extend it to make a new class called a set class where the duplication of objects is eliminated. Now, a function that takes an object of the bag class may expect that adding two objects increases the size of a bag by two, yet if one passes an object of a set class, then adding two objects may or may not increase the size of a bag by two. The problem arises precisely because subclassing implies subtyping even in the instances where the principle of subtyping, known as the Liskov substitution principle, does not hold. Barbara Liskov and Jeannette Wing formulated the principle succinctly in a 1994 paper as follows:

> *Subtype Requirement*: Let ⁠ $\phi (x)$ ⁠ be a property provable about objects ⁠ x ⁠ of type ⁠ T ⁠. Then ⁠ $\phi (y)$ ⁠ should be true for objects ⁠ y ⁠ of type ⁠ S ⁠ where ⁠ S ⁠ is a subtype of ⁠ T ⁠.

Thus, normally one must distinguish subtyping and subclassing. Most current object-oriented languages distinguish subtyping and subclassing, however some approaches to design do not.

Also, another common example is that a person object created from a child class cannot become an object of parent class because a child class and a parent class inherit a person class but class-based languages mostly do not allow to change the kind of class of the object at runtime. For class-based languages, this restriction is essential in order to preserve unified view of the class to its users. The users should not need to care whether one of the implementations of a method happens to cause changes that break the invariants of the class. Such changes can be made by destroying the object and constructing another in its place. Polymorphism can be used to preserve the relevant interfaces even when such changes are done, because the objects are viewed as black box abstractions and accessed via object identity. However, usually the value of object references referring to the object is changed, which causes effects to client code.

### Example languages

Although Simula introduced the class abstraction, the canonical example of a class-based language is Smalltalk. Others include PHP, C++, Java, C#, and Objective-C.

## Prototype-based programming

In contrast to creating an object from a class, some programming contexts support object creation by copying (cloning) a prototype object.
