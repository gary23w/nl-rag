---
title: "Reflective programming"
source: https://en.wikipedia.org/wiki/Reflection_(computer_programming)
domain: newtonsoft-json-dotnet
license: CC-BY-SA-4.0
tags: newtonsoft json, dotnet json library, json.net serialization, json.net converter
fetched: 2026-07-02
---

# Reflective programming

(Redirected from

Reflection (computer programming)

)

In computer science, **reflective programming** or **reflection** is the ability of a process to examine, introspect, and modify its own structure and behavior.

## Historical background

The earliest computers were programmed in their native assembly languages, which were inherently reflective, as these original architectures could be programmed by defining instructions as data and using self-modifying code. As the bulk of programming moved to higher-level compiled languages such as ALGOL, COBOL, Fortran, Pascal, and C, this reflective ability largely disappeared until new programming languages with reflection built into their type systems appeared.

Brian Cantwell Smith's 1982 doctoral dissertation introduced the notion of computational reflection in procedural programming languages and the notion of the meta-circular interpreter as a component of 3-Lisp.

## Uses

Reflection helps programmers make generic software libraries to display data, process different formats of data, perform serialization and deserialization of data for communication, or do bundling and unbundling of data for containers or bursts of communication. Reflective systems may provide a mirror type, used as a decoupled reflection of an object or identifier.

Effective use of reflection almost always requires a plan: A design framework, encoding description, object library, a map of a database or entity relations.

Reflection makes a language more suited to network-oriented code. For example, it assists languages such as Java to operate well in networks by enabling libraries for serialization, bundling and varying data formats. Languages without reflection such as C are required to use auxiliary compilers for tasks like Abstract Syntax Notation to produce code for serialization and bundling.

Reflection can be used for observing and modifying program execution at runtime. A reflection-oriented program component can monitor the execution of an enclosure of code and can modify itself according to a desired goal of that enclosure. This is typically accomplished by dynamically assigning program code at runtime.

In object-oriented programming languages such as Java, reflection allows *inspection* of classes, interfaces, fields and methods at runtime without knowing the names of the interfaces, fields, methods at compile time. It also allows *instantiation* of new objects and *invocation* of methods.

Reflection is often used as part of software testing, such as for the runtime creation/instantiation of mock objects.

Reflection is also a key strategy for metaprogramming.

In some object-oriented programming languages such as C# and Java, reflection can be used to bypass member accessibility rules. For C#-properties this can be achieved by writing directly onto the (usually invisible) backing field of a non-public property. It is also possible to find non-public methods of classes and types and manually invoke them. This works for project-internal files as well as external libraries such as .NET's assemblies and Java's archives.

## Implementation

A language that supports reflection provides a number of features available at runtime that would otherwise be difficult to accomplish in a lower-level language. Some of these features are the abilities to:

- Discover and modify source-code constructions (such as code blocks, classes, methods, protocols, etc.) as first-class objects at runtime. Readable object metadata is provided as a mirror.
- Convert a string matching the symbolic name of a class or function into a reference to or invocation of that class or function.
- Evaluate a string as if it were a source-code statement at runtime.
- Create a new interpreter for the language's bytecode to give a new meaning or purpose for a programming construct.

These features can be implemented in different ways. In MOO, reflection forms a natural part of everyday programming idiom. When verbs (methods) are called, various variables such as `verb` (the name of the verb being called) and `this` (the object on which the verb is called) are populated to give the context of the call. Security is typically managed by accessing the caller stack programmatically: Since `callers()` is a list of the methods by which the current verb was eventually called, performing tests on `callers()[0]` (the command invoked by the original user) allows the verb to protect itself against unauthorised use.

Compiled languages rely on their runtime system to provide information about the source code. A compiled Objective-C executable, for example, records the names of all methods in a block of the executable, providing a table to correspond these with the underlying methods (or selectors for these methods) compiled into the program. In a compiled language that supports runtime creation of functions, such as Common Lisp, the runtime environment must include a compiler or an interpreter.

Reflection can be implemented for languages without built-in reflection by using a program transformation system to define automated source-code changes.

## Security considerations

Reflection may allow a user to create unexpected control flow paths through an application, potentially bypassing security measures. This may be exploited by attackers. Historical vulnerabilities in Java caused by unsafe reflection allowed code retrieved from potentially untrusted remote machines to break out of the Java sandbox security mechanism. A large scale study of 120 Java vulnerabilities in 2013 concluded that unsafe reflection is the most common vulnerability in Java, though not the most exploited.

## Runtime performance

Runtime reflection systems introduce a non-negligible runtime performance overhead. For instance, in Java, because reflective operations are resolved dynamically at execution time, many compiler and JVM optimizations—such as method inlining, static binding, and aggressive just-in-time specialization—cannot be fully applied. As a consequence, reflective calls are typically slower than their statically resolved counterparts. Microbenchmark and application-level studies on Java have shown that reflective operations can incur substantial runtime overhead, especially for method invocation and dynamic object creation, with slowdowns ranging from around 20–40% in moderate cases to more than 300× in heavily reflective dispatch scenarios. In sequential applications, reflection can significantly increase execution time and memory consumption when used in performance-critical code paths. In multithreaded applications, reflective implementations generally preserve scalability, but still exhibit noticeably higher absolute execution times—commonly between 1.5x and 10× slower—than equivalent non-reflective code.

In languages like C++ and Rust, reflection is performed at compile time. Compile-time reflection systems are weaker than runtime reflection systems like those of Java and C#, but incur no runtime overhead due to being performed during compilation.

## Examples

The following code snippets create an instance `foo` of class `Foo` and invoke its method `PrintHello`. For each programming language, normal and reflection-based call sequences are shown.

### Common Lisp

The following is an example in Common Lisp using the Common Lisp Object System:

```mw
(defclass foo () ())
(defmethod print-hello ((f foo)) (format T "Hello from ~S~%" f))

;; Normal, without reflection
(let ((foo (make-instance 'foo)))
  (print-hello foo))

;; With reflection to look up the class named "foo" and the method
;; named "print-hello" that specializes on "foo".
(let* ((foo-class (find-class (read-from-string "foo")))
       (print-hello-method (find-method (symbol-function (read-from-string "print-hello"))
                                        nil (list foo-class))))
  (funcall (sb-mop:method-generic-function print-hello-method)
           (make-instance foo-class)))
```

### C

Reflection is not possible in C, though parts of reflection can be emulated.

```mw
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    // ...
} Foo;

typedef void (*Method)(void*);

// The method: Foo::printHello
void Foo_printHello(void* _) {
    printf("Hello, world!\n");
}

// Simulated method table
typedef struct {
    const char* name;
    Method fn;
} MethodEntry;

const MethodEntry FOO_METHODS[] = {
    { "printHello", Foo_printHello },
    { NULL, NULL } // Sentinel to mark end
};

// Simulate reflective method lookup
Method findMethodByName(const char* name) {
    for (size_t i = 0; FOO_METHODS[i].name; i++) {
        if (strcmp(FOO_METHODS[i].name, name) == 0) {
            return FOO_METHODS[i].fn;
        }
    }
    return NULL;
}

int main() {
    // Without reflection
    Foo foo;
    Foo_printHello(&foo);

    // With emulated reflection
    Foo* reflected = (Foo*)malloc(sizeof(Foo));
    if (!reflected) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }

    const char* name = "printHello";
    Method m = findMethodByName(name);

    if (m) {
        m(reflected);
    } else {
        fprintf(stderr, "Method '%s' not found\n", name);
        free(reflected);
        return EXIT_FAILURE;
    }

    free(reflected);
    return EXIT_SUCCESS;
}
```

### C++

The following is an example in C++ (using reflection added in C++26).

```mw
import std;

using std::string_view;
using std::views::filter;
using std::meta::access_context;
using std::meta::exception;
using std::meta::info;

namespace meta = std::meta;

consteval bool isNonstaticMethod(info mem) noexcept {
    return meta::is_class_member(mem) &&
        !meta::is_static_member(mem) &&
        meta::is_function(mem);
}

consteval info findMethod(info type, string_view name) {
    for (info member : meta::members_of(type, access_context::current())
        | filter(isNonstaticMethod)) {
        if (meta::has_identifier(member) && meta::identifier_of(member) == name) {
            return member;
        }
    }
    // Note: this is std::meta::exception, not std::exception
    throw exception(std::format("Failed to retrieve method {} from type {}", name, meta::identifier_of(type)), ^^findMethod);
}

template <info T, const char* Name>
constexpr auto createInvokerImpl = []() -> auto {
    static constexpr info M = findMethod(T, Name);
    contract_assert(
        meta::parameters_of(M).size() == 0 &&
        meta::return_type_of(M) == ^^void
    );
    return []([:T:]& instance) -> void { instance.[:M:](); };
}();

consteval info createInvoker(info type, string_view name) {
    return meta::substitute(
        ^^createInvokerImpl,
        { meta::reflect_constant(type), meta::reflect_constant_string(name) }
    );
}

class Foo {
private:
    // ...
public:
    Foo() = default;

    void printHello() const {
        std::println("Hello, world!");
    }
};

int main(int argc, char* argv[]) {
    Foo foo;

    // Without reflection
    foo.printHello();

    // With reflection
    auto invokePrint = [:createInvoker(^^Foo, "printHello"):];
    invokePrint(foo);

    return 0;
}
```

### C

The following is an example in C#:

```mw
namespace Wikipedia.Examples;

using System;
using System.Reflection;

class Foo
{
    // ...

    public void PrintHello()
    {
        Console.WriteLine("Hello, world!");
    }
}

public class InvokeFooExample
{
    static void Main(string[] args)
    {
        // Without reflection
        Foo foo = new();
        foo.PrintHello();

        // With reflection
        Object reflectedFoo = Activator.CreateInstance(typeof(Foo));
        MethodInfo method = reflectedFoo.GetType()
            .GetMethod("PrintHello");
        method.Invoke(foo, null);
    }
}
```

### Delphi, Object Pascal

This Delphi and Object Pascal example assumes that a TFoo class has been declared in a unit called Unit1:

```mw
uses RTTI, Unit1;

procedure WithoutReflection;
var
  Foo: TFoo;
begin
  Foo := TFoo.Create;
  try
    Foo.Hello;
  finally
    Foo.Free;
  end;
end;

procedure WithReflection;
var
  RttiContext: TRttiContext;
  RttiType: TRttiInstanceType;
  Foo: TObject;
begin
  RttiType := RttiContext.FindType('Unit1.TFoo') as TRttiInstanceType;
  Foo := RttiType.GetMethod('Create').Invoke(RttiType.MetaclassType, []).AsObject;
  try
    RttiType.GetMethod('Hello').Invoke(Foo, []);
  finally
    Foo.Free;
  end;
end;
```

### eC

The following is an example in eC:

```mw
// Without reflection
Foo foo{};
foo.hello();

// With reflection
Class fooClass = eSystem_FindClass(__thisModule, "Foo");
Instance foo = eInstance_New(fooClass);
Method m = eClass_FindMethod(fooClass, "hello", fooClass.module);
((void(*)())(void*)m.function)(foo);
```

### Go

The following is an example in Go:

```mw
import (
    "fmt"
    "reflect"
)

type Foo struct{}

func (f Foo) Hello() {
    fmt.Println("Hello, world!")
}

func main() {
    // Without reflection
    var f Foo
    f.Hello()

    // With reflection
    var fT reflect.Type = reflect.TypeOf(Foo{})
    var fV reflect.Value = reflect.New(fT)

    var m reflect.Value = fV.MethodByName("Hello")

    if m.IsValid() {
        m.Call(nil)
    } else {
        fmt.Println("Method not found")
    }
}
```

### Java

The following is an example in Java:

```mw
package org.wikipedia.examples;

import java.lang.reflect.Method;

class Foo {
    // ...

    public void printHello() {
       System.out.println("Hello, world!");
    }
}

public class InvokeFooExample {
    public static void main(String[] args) {
        // Without reflection
        Foo foo = new Foo();
        foo.printHello();

        // With reflection
        try {
            Foo reflectedFoo = Foo.class
                .getDeclaredConstructor()
                .newInstance();

            Method m = reflectedFoo.getClass()
                .getDeclaredMethod("printHello", new Class<?>[0]);
            m.invoke(reflectedFoo);
        } catch (ReflectiveOperationException e) {
            System.err.printf("An error occurred: %s%n", e.getMessage());
        }
    }
}
```

Java also provides an internal class (not officially in the Java Class Library) in module `jdk.unsupported`, `sun.reflect.Reflection` which is used by `sun.misc.Unsafe`. It contains one method, `static Class<?> getCallerClass(int depth)` for obtaining the class making a call at a specified depth. This is now superseded by using the class `java.lang.StackWalker.StackFrame` and its method `Class<?> getDeclaringClass()` .

### JavaScript/TypeScript

The following is an example in JavaScript:

```mw
import 'reflect-metadata';

// Without reflection
const foo = new Foo();
foo.hello();

// With reflection
const foo = Reflect.construct(Foo);
const hello = Reflect.get(foo, 'hello');
Reflect.apply(hello, foo, []);

// With eval
eval('new Foo().hello()');
```

The following is the same example in TypeScript:

```mw
import 'reflect-metadata';

// Without reflection
const foo: Foo = new Foo();
foo.hello();

// With reflection
const foo: Foo = Reflect.construct(Foo);
const hello: (this: Foo) => void = Reflect.get(foo, 'hello') as (this: Foo) => void;
Reflect.apply(hello, foo, []);

// With eval
eval('new Foo().hello()');
```

### Julia

The following is an example in Julia:

```mw
julia> struct Point
           x::Int
           y
       end

# Inspection with reflection
julia> fieldnames(Point)
(:x, :y)

julia> fieldtypes(Point)
(Int64, Any)

julia> p = Point(3,4)

# Access with reflection
julia> getfield(p, :x)
3
```

### Kotlin

Using Java reflection:

```mw
package org.wikipedia.examples

import java.lang.reflect.Method

class Foo {
    // ...
    constructor()

    fun printHello() {
        println("Hello, world!")
    }
}

fun main(args: Array<String>) {
    // Without reflection
    val foo = Foo()
    foo.printHello()

    // With reflection
    try {
        // Foo::class.java retrieves a java.lang.Class<Foo>
        val reflectedFoo = Foo::class.java
            .getDeclaredConstructor()
            .newInstance()

        val m: Method = reflectedFoo.javaClass
            .getDeclaredMethod("printHello")

        m.invoke(reflectedFoo)
    } catch (e: ReflectiveOperationException) {
        System.err.printf("An error occurred: %s%n", e.message)
    }
}
```

Using pure Kotlin:

```mw
package org.wikipedia.examples

import kotlin.reflect.full.createInstance
import kotlin.reflect.full.functions

class Foo {
    // ...
    fun printHello() {
        println("Hello, world!")
    }
}

fun main(args: Array<String>) {
    // Without reflection
    val foo = Foo()
    foo.printHello()

    // With reflection
    try {
        val kClass = Foo::class
        val reflectedFoo = kClass.createInstance()
        val function = kClass.functions.first { it.name == "printHello" }
        function.call(reflectedFoo)
    } catch (e: Exception) {
        System.err.printf("An error occurred: %s%n", e.message)
    }
}
```

### Objective-C

The following is an example in Objective-C, implying either the OpenStep or Foundation Kit framework is used:

```mw
// Foo class.
@interface Foo : NSObject
- (void)hello;
@end

// Sending "hello" to a Foo instance without reflection.
Foo* obj = [[Foo alloc] init];
[obj hello];

// Sending "hello" to a Foo instance with reflection.
id obj = [[NSClassFromString(@"Foo") alloc] init];
[obj performSelector: @selector(hello)];
```

### Perl

The following is an example in Perl:

```mw
# Without reflection
my $foo = Foo->new;
$foo->hello;

# or
Foo->new->hello;

# With reflection
my $class = "Foo"
my $constructor = "new";
my $method = "hello";

my $f = $class->$constructor;
$f->$method;

# or
$class->$constructor->$method;

# with eval
eval "new Foo->hello;";
```

### PHP

The following is an example in PHP:

```mw
// Without reflection
$foo = new Foo();
$foo->hello();

// With reflection, using Reflections API
$reflector = new ReflectionClass("Foo");
$foo = $reflector->newInstance();
$hello = $reflector->getMethod("hello");
$hello->invoke($foo);
```

### Python

The following is an example in Python:

```mw
from typing import Any

class Foo:
    # ...
    def print_hello(self) -> None:
        print("Hello, world!")

if __name__ == "__main__":
    # Without reflection
    obj: Foo = Foo()
    obj.print_hello()

    # With reflection
    obj: Foo = globals()["Foo"]()
    _: Any = getattr(obj, "print_hello")()

    # With eval
    eval("Foo().print_hello()")
```

### R

The following is an example in R:

```mw
# Without reflection, assuming foo() returns an S3-type object that has method "hello"
obj <- foo()
hello(obj)

# With reflection
class_name <- "foo"
generic_having_foo_method <- "hello"
obj <- do.call(class_name, list())
do.call(generic_having_foo_method, alist(obj))
```

### Ruby

The following is an example in Ruby:

```mw
# Without reflection
obj = Foo.new
obj.hello

# With reflection
obj = Object.const_get("Foo").new
obj.send :hello

# With eval
eval "Foo.new.hello"
```

### Rust

The following is an example in Rust (using procedural macros).

```mw
// A basic macro that registers a method name string to an actual method call
macro_rules! invoke_method {
    ($instance:expr, $method_name:expr) => {
        match $method_name {
            "print_hello" => $instance.print_hello(),
            _ => eprintln!("An error occurred: Method not found."),
        }
    };
}

struct Foo;

impl Foo {
    fn print_hello(&self) {
        println!("Hello, world!");
    }
}

fn main() {
    let foo = Foo;

    // Normal call sequence
    foo.print_hello();

    // Reflection-style sequence via compile-time mapping
    let method_to_call = "print_hello";
    invoke_method!(foo, method_to_call);
}
```

### Swift

Swift reflection is read-only, and thus dynamic invocation is only possible through Objective-C.

```mw
import Foundation

class Foo: NSObject {
    @objc func printHello() {
        print("Hello, world!")
    }
}

class InvokeFooExample {
    static func main() {
        // Without reflection
        let foo = Foo()
        foo.printHello()

        // With "reflection" (Objective-C runtime)
        let reflectedFoo = Foo()

        let selector = #selector(Foo.printHello)

        if reflectedFoo.responds(to: selector) {
            reflectedFoo.perform(selector)
        }
    }
}
```

Swift's reflection system, with `Swift.Mirror`, is much more limited in scope:

```mw
import Foundation

class Foo {
    func printHello() {
        print("Hello, world!")
    }
}

let foo = Foo()

let mirror = Mirror(reflecting: foo)

print(type(of: foo)) // Foo
print(mirror.children.count) // Properties only
```

### Xojo

The following is an example using Xojo:

```mw
' Without reflection
Dim fooInstance As New Foo
fooInstance.PrintHello

' With reflection
Dim classInfo As Introspection.Typeinfo = GetTypeInfo(Foo)
Dim constructors() As Introspection.ConstructorInfo = classInfo.GetConstructors
Dim fooInstance As Foo = constructors(0).Invoke
Dim methods() As Introspection.MethodInfo = classInfo.GetMethods
For Each m As Introspection.MethodInfo In methods
  If m.Name = "PrintHello" Then
    m.Invoke(fooInstance)
  End If
Next
```
