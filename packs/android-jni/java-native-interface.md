---
title: "Java Native Interface"
source: https://en.wikipedia.org/wiki/Java_Native_Interface
domain: android-jni
license: CC-BY-SA-4.0
tags: java native interface, android jni, native development kit, foreign function interface
fetched: 2026-07-02
---

# Java Native Interface

The **Java Native Interface** (or Native Method Interface) is a foreign function interface designed for non-Java programming frameworks. The JNI enables Java code to call and be called by native code (i.e. any code using the `JNIEnv` and interfacing through the C application binary interface), native applications (programs specific to a hardware and operating system platform) and libraries written in other languages such as C, C++ and assembly.

Java 22 introduces the Foreign Function and Memory API, which can be seen as the successor to Java Native Interface.

## Objectives

JNI allows native methods to allow for applications to make calls outside of the Java platform, e.g. when the standard Java class library does not support platform-specific features or a certain program library. It is also used to modify an existing application (written in another programming language) to be accessible to Java applications. Many standard library classes depend on JNI to provide functionality to the developer and the user, such as file I/O and audio APIs. Only applications and signed applets may invoke JNI.

The JNI framework allows native code to manipulate and consume Java objects. A native method (marked by the keyword `native` in Java) can create Java objects and inspect and use these objects to perform its tasks. A native method can also inspect and use objects created by Java application code.

An application that relies on JNI loses the platform portability Java offers (a partial workaround is to write a separate implementation of JNI code for each platform and have Java detect the operating system and load the correct one at runtime).

Not only can native code interface with Java, it can also draw on a Java `Canvas`, which is possible with the Java AWT Native Interface, available since J2SE 1.3.

JNI also allows direct access to assembly, without a C bridge. Accessing Java applications from assembly is possible in the same way.

The JNI is the entry point between languages used to begin the JVM startup.

## Mapping types

Java types are the default primitive types available on Java, while JVM type signatures are identifiers used by the JVM to identify the type matching on Java, while native types are types defined by the JNI itself to map to native types. For primitives, the following typedefs are provided:

| Java type | Native typedef | Description | JVM type signature | Closest native type |
|---|---|---|---|---|
| `boolean` | `jboolean` | unsigned 8 bits | Z | `bool` |
| `byte` | `jbyte` | signed 8 bits | B | `char` or `int8_t` |
| `char` | `jchar` | unsigned 16 bits | C | `char16_t` |
| `short` | `jshort` | signed 16 bits | S | `short` or `int16_t` |
| `int` | `jint` | signed 32 bits | I | `int` or `int32_t` |
| `long` | `jlong` | signed 64 bits | J | `long` or `int64_t` |
| `float` | `jfloat` | 32 bits | F | `float` or `float32_t` |
| `double` | `jdouble` | 64 bits | D | `double` or `float64_t` |
| `void` | `void` | not applicable | V | `void` |

In addition, the JVM type signature `L*fully-qualified-class*;` refers the class uniquely specified by that name, for example the signature `Ljava.lang.String;` (`Ljava/lang/String;` in class files) refers to the class `java.lang.String`. Prefixing `[` to the signature denotes an array of that type; for example, `[I` refers to `int[]`, and `[[I` refers to `int[][]`, up to a maximum of 255 dimensions.

These types are interchangeable. One can use `jint` where you normally use an `int`, and vice versa, without any typecasting required. However, mapping between Java strings and arrays to native strings and arrays is different; for instance, `jstring` and `char*` are not interchangeable types, nor are `jintArray` and `int[]`.

JNI additionally contains the following declarations for Java reference types in `<jni.h>`:

```mw
#ifdef __cplusplus
class _jobject {};
class _jclass : public _jobject {};
// ...
typedef _jobject *jobject;
typedef _jclass *jclass;
// ...
#else
struct _jobject;
// ...
typedef struct _jobject *jobject;
typedef jobject jclass;
// ...
#endif
```

Here, all Java reference types are defined as opaque empty types which act as handles to Java objects. These types should not be dereferenced.

| Java type | JNI handle |
|---|---|
| `java.lang.Object` | `jobject` |
| `java.lang.Class` (non-generic) | `jclass` |
| `java.lang.Throwable` | `jthrowable` |
| `java.lang.String` | `jstring` |
| `T[]` (for a type `T`) | `jarray` |
| `boolean[]` | `jbooleanArray` |
| `byte[]` | `jbyteArray` |
| `char[]` | `jcharArray` |
| `short[]` | `jshortArray` |
| `int[]` | `jintArray` |
| `long[]` | `jlongArray` |
| `float[]` | `jfloatArray` |
| `double[]` | `jdoubleArray` |
| `java.lang.Object[]` | `jobjectArray` |

Additionally, the following opaque types are used as handles:

| Java class meta-object | JNI handle |
|---|---|
| Class field | `jfieldID` |
| Class method | `jmethodID` |

Note however that `jfieldID` and `jmethodID` are just opaque handles, and do not correspond to `java.lang.reflect.Field`/`java.lang.reflect.Method`.

## Design

The communication between native code and Java code is intermediated by the JNI, acting as an ABI.

```mw
// jni.h file

struct JNINativeInterface_;
struct JNIEnv_;

#ifdef __cplusplus
typedef JNIEnv_ JNIEnv;
#else
typedef const struct JNINativeInterface_ *JNIEnv;
#endif
```

`JNIEnv` is used to access the structure of functions (array of function pointers), and each function being identifiable by a unique pointer. According to the programming language, C or C++, the implementation can be a little different. For example, in C:

```mw
// jni.h file

struct JNINativeInterface_ {

    jint (JNICALL *GetVersion) // JNICALL declaration of a pointer to identify the specific function;
       (JNIEnv *env); // Parameter env is a pointer to the JNIEnv pointer, the pointer-to-pointer;

    jclass (JNICALL *DefineClass)
      (JNIEnv *env, const char *name);

    jclass (JNICALL *FindClass)
      (JNIEnv *env, const char *name);

    // Others functions pointers...
}
```

### Implementation

In the JNI framework, native functions are implemented in separate .c or .cpp files (C++ provides a slightly simpler interface with JNI). When the JVM invokes the function, it passes a `JNIEnv*`, a `jobject`, and any Java arguments declared by the Java method. For example, the following converts `jstring` to a `const char*`:

```mw
extern "C" {

JNIEXPORT void JNICALL Java_ClassName_MethodName (JNIEnv* env, jobject obj, jstring javaString) {
    const char* nativeString = env->GetStringUTFChars(javaString, 0);

    // Do something with the nativeString

    env->ReleaseStringUTFChars(javaString, nativeString);
}

}
```

The `env` pointer is a structure that contains the interface to the JVM. It includes all of the functions necessary to interact with the JVM and to work with Java objects. Anything that Java code can do can be done using `JNIEnv`. The argument `obj` is a reference to the Java object inside which this native method has been declared.

Native data types can be mapped to/from Java data types. For compound types, such as objects, arrays and strings, the native code must explicitly convert the data by calling methods in the `JNIEnv`.

A JNI environment pointer (`JNIEnv*`) is passed as an argument for each native function mapped to a Java method, allowing for interaction with the JNI environment within the native method. This JNI interface pointer can be stored, but remains valid only in the current thread. Other threads must first call `AttachCurrentThread()` to attach themselves to the VM and obtain a JNI interface pointer. Once attached, a native thread works like a regular Java thread running within a native method. The native thread remains attached to the VM until it calls `DetachCurrentThread()` to detach itself.

The JNI framework does not provide any automatic garbage collection for non-JVM memory resources allocated by code executing on the native side. Consequently, native code is responsible explicitly releasing all acquired resources.

On Linux and Solaris platforms, if the native code registers itself as a signal handler, it can intercept signals intended for the JVM. A chain of responsibility can be used to allow native code to interoperate with the JVM. On Windows platforms, Structured Exception Handling (SEH) may be employed to wrap native code in SEH `try`/`catch` blocks so as to capture machine (CPU/FPU) generated software interrupts (such as null pointer dereferences and divide-by-zero operations), and to handle these situations before the interrupt is propagated back up into the JVM (i.e. Java side code).

The encoding used for the `NewStringUTF()`, `GetStringUTFLength()`, `GetStringUTFChars()`, `ReleaseStringUTFChars()` and `GetStringUTFRegion()` functions is "modified UTF-8", which is not valid UTF-8 for all inputs, but a different encoding. The null character (U+0000) and codepoints not on the Basic Multilingual Plane (greater than or equal to U+10000, i.e. those represented as surrogate pairs in UTF-16) are encoded differently in modified UTF-8. Many programs actually use these functions incorrectly and treat the UTF-8 strings returned or passed into the functions as standard UTF-8 strings instead of modified UTF-8 strings. Programs should use the `NewString()`, `GetStringLength()`, `GetStringChars()`, `ReleaseStringChars()`, `GetStringRegion()`, `GetStringCritical()` and `ReleaseStringCritical()` functions, which use UTF-16LE encoding on little-endian architectures and UTF-16BE on big-endian architectures, and then use a UTF-16 to UTF-8 conversion routine.

For example, the following demonstrates a native implementation of a Java method `HelloJNI::sayHello()`:

```mw
#include <stdio.h>
#include <jni.h>

JNIEXPORT void JNICALL Java_HelloJNI_sayHello(JNIEnv* env, jobject obj) {
    printf("Hello from C!\n");
}
```

Then, in Java, the function is called like so:

```mw
public class HelloJNI {
    static {
        // "hello" refers to libhello.so on Linux
        System.loadLibrary("hello"); // System.load() is other way to load a library.
    }

    public native void sayHello();

    public static void main(String[] args) {
        new HelloJNI().sayHello();
    }
}
```

## Performance

JNI incurs considerable overhead and performance loss under certain circumstances:

- Function calls to JNI methods are expensive, especially when repeatedly calling a method.
- Native methods are not inlined by the JVM, nor can the method be JIT compiled, as the method is already compiled.
- A Java array may be copied for access in native code, and later copied back. The cost is linear in the size of the array.
- If the method is passed an object, or needs to make a callback, then the native method will likely be making its own calls to the JVM. Accessing Java fields, methods and types from native code invokes Java reflection. Signatures are specified in strings and queried from the JVM. This is both slow and error-prone.
- Java strings are objects and have length and are encoded. Accessing or creating a string may require an $O(n)$ copy.

## Foreign Function and Memory API

Java 22 introduced the Foreign Function and Memory API, located in `java.lang.foreign` which can be seen as a sort of successor to the Java Native Interface. It has a simpler interface and generally requires less boilerplate than JNI, due to no longer requiring the inclusion of `<jni.h>` in the foreign library to invoke, and Foreign Function and Memory API abstracts away the usage of the `native` keyword completely. It supports region-based memory management. The class `java.lang.foreign.MemorySegment` models a contiguous segment of memory which can lie inside or outside the JVM heap, and a `java.lang.foreign.MemorySegment` is allocated using a `java.lang.foreign.Arena` which controls the lifetime of the region of memory backing its allocated segment of memory.

The `java.lang.foreign.Arena` offers the following arena kinds:

| Arena kind | Factory method | Bounded lifetime | Explicitly closeable | Accessible from multiple threads |
|---|---|---|---|---|
| Global | `Arena.global()` | No | No | Yes |
| Automatic | `Arena.ofAuto()` | Yes | No | Yes |
| Confined | `Arena.ofConfined()` | Yes | Yes | No |
| Shared | `Arena.ofShared()` | Yes | Yes | Yes |

```mw
package org.wikipedia.examples;

import java.lang.foreign.Arena;
import java.lang.foreign.MemorySegment;
import java.lang.foreign.ValueLayout;

public class ForeignMemoryExample {
    public static void main(String[] args) {
        try (Arena arena = Arena.ofConfined()) {
            MemorySegment segment = arena.allocate(5 * Double.BYTES);
            
            for (int i = 0; i < 5; ++i) {
                segment.setAtIndex(ValueLayout.JAVA_DOUBLE, i, i * 1.1);
            }

            for (int i = 0; i < 5; ++i) {
                double value = segment.getAtIndex(ValueLayout.JAVA_DOUBLE, i);
                System.out.printf("Value at index %d: %d%n", i, value);
            }
        }
    }
}
```

In a sense, Java Foreign Function and Memory API allows for direct memory allocation outside the JVM heap (i.e. the operating system heap), through `Arena.allocate()` and `MemorySegment.allocateNative()` which allocate raw memory directly, while `Arena.close()` and `MemorySegment.close()` are used to deallocate/release the memory segment.

As a foreign function interface, the classes `java.lang.foreign.Linker` is offered for accessing between foreign functions from Java (to and from), `java.lang.foreign.SymbolLookup` for retrieving the address of a symbol in a library, and `java.lang.foreign.FunctionDescriptor` for modelling a foreign function signature.

```mw
package org.wikipedia.examples;

import java.lang.foreign.Arena;
import java.lang.foreign.FunctionDescriptor;
import java.lang.foreign.Linker;
import java.lang.foreign.MemorySegment;
import java.lang.foreign.SymbolLookup;
import java.lang.foreign.ValueLayout;
import java.lang.invoke.MethodHandle;

public class ForeignFunctionExample {
    public static void main(String[] args) throws Throwable {
        Linker linker = Linker.nativeLinker();
        
        SymbolLookup stdlib = linker.defaultLookup();
        
        MethodHandle printf = linker.downcallHandle(
            stdlib.findOrThrow("printf"),
            FunctionDescriptor.of(ValueLayout.JAVA_INT, ValueLayout.ADDRESS)
        );

        MethodHandle strlen = linker.downcallHandle(
            stdlib.findOrThrow("strlen"),
            FunctionDescriptor.of(ValueLayout.JAVA_LONG, ValueLayout.ADDRESS)
        );

        try (Arena arena = Arena.ofConfined()) {
            MemorySegment formatString = arena.allocateUtf8String("Hello, %s!\n");
            MemorySegment argString = arena.allocateUtf8String("World");
            printf.invokeExact(formatString, argString); // prints "Hello, World!"
            long len = (long)strlen.invokeExact(formatString); // len = 5
        }
    }
}
```

Layouts are modelled by `java.lang.foreign.ValueLayout`, which consists of:

| Type | Name | Description |
|---|---|---|
| `java.lang.foreign.AddressLayout` | `ADDRESS` | An address layout with the same size as `size_t` |
| `java.lang.foreign.AddressLayout` | `ADDRESS_UNALIGED` | An unaligned address layout with the same size as `size_t` |
| `java.lang.foreign.ValueLayout.OfBoolean` | `JAVA_BOOLEAN` | A value layout constant with the same size as a Java `boolean` |
| `java.lang.foreign.ValueLayout.OfByte` | `JAVA_BYTE` | A value layout constant with the same size as a Java `byte` |
| `java.lang.foreign.ValueLayout.OfChar` | `JAVA_CHAR` | A value layout constant with the same size as a Java `char` |
| `java.lang.foreign.ValueLayout.OfChar` | `JAVA_CHAR_UNALIGNED` | An unaligned value layout with the same size as a Java `char` |
| `java.lang.foreign.ValueLayout.OfShort` | `JAVA_SHORT` | A value layout constant with the same size as a Java `short` |
| `java.lang.foreign.ValueLayout.OfShort` | `JAVA_SHORT_UNALIGNED` | An unaligned value layout with the same size as a Java `short` |
| `java.lang.foreign.ValueLayout.OfInt` | `JAVA_INT` | A value layout constant with the same size as a Java `int` |
| `java.lang.foreign.ValueLayout.OfInt` | `JAVA_INT_UNALIGNED` | An unaligned value layout with the same size as a Java `int` |
| `java.lang.foreign.ValueLayout.OfLong` | `JAVA_LONG` | A value layout constant with the same size as a Java `long` |
| `java.lang.foreign.ValueLayout.OfLong` | `JAVA_LONG_UNALIGNED` | An unaligned value layout with the same size as a Java `long` |
| `java.lang.foreign.ValueLayout.OfFloat` | `JAVA_FLOAT` | A value layout constant with the same size as a Java `float` |
| `java.lang.foreign.ValueLayout.OfFloat` | `JAVA_FLOAT_UNALIGNED` | An unaligned value layout with the same size as a Java `float` |
| `java.lang.foreign.ValueLayout.OfDouble` | `JAVA_DOUBLE` | A value layout constant with the same size as a Java `double` |
| `java.lang.foreign.ValueLayout.OfDouble` | `JAVA_DOUBLE_UNALIGNED` | An unaligned value layout with the same size as a Java `double` |

Primitives receive `ValueLayout.JAVA_*` layouts when mapped to their native types, while pointer types use `ValueLayout.ADDRESS` (for instance `char*`, `int**` or `struct Point*`).

Additionally, the constant `MemorySegment.NULL` (of type `java.lang.foreign.MemorySegment`) is a zero-length native segment representing a null address (`nullptr`), equivalent to `MemorySegment.ofAddress(0)`.

Java offers additional methods to express more complicated native types. For instance, the following native types

```mw
struct Point {
    int x;
    long y;
};

union Choice {
    float a;
    int b;
};
```

receive the following layouts:

```mw
import java.lang.foreign.MemoryLayout;
import java.lang.foreign.StructLayout;
import java.lang.foreign.UnionLayout;

StructLayout pointLayout = MemoryLayout.structLayout(
    ValueLayout.JAVA_INT.withName("x"),
    MemoryLayout.paddingLayout(4),
    ValueLayout.JAVA_LONG.withName("y")
};

UnionLayout choiceLayout = MemoryLayout.unionLayout(
    ValueLayout.JAVA_FLOAT.withName("a"),
    ValueLayout.JAVA_INT.withName("b")
);
```

## Alternatives

The Java Runtime Interface was created by Netscape as a precursor.

Microsoft's proprietary implementation of a Java Virtual Machine (Visual J++) had a similar mechanism for calling native code from Java, called the Raw Native Interface (RNI). In addition, it offered a simple way to call existing native code that was not itself aware of Java, such as (but not limited to) the Windows API, (J/Direct). However, following the Sun–Microsoft litigation about this implementation, Visual J++ ceased to be maintained. RNI was simpler to use than JNI, because no management of the Java environment pointer was needed; instead, all Java objects were accessed directly. To facilitate this, a tool was used to generate header files from Java classes. Similarly, J/Direct was easier to use than using the necessary intermediate native library and JNI.

Java Native Access (JNA) is a community-developed library that provides Java programmers easy access to native shared libraries without using JNI. However, this requires the redistribution of the dependent jar library. The tradeoff is between JNI being more complex and JNA being slower, and not built-in like JNI.

Historically, GCC (until GCC 7) offered the GNU Compiler for Java. This compiler offered the Compiled Native Interface (CNI), which allowed direct interoperability between C++ and Java. It provided an API that was heavily based off of JNI itself. It claimed several advantages over JNI, as it represented Java classes directly as C++ classes.

Since Java 22, the Foreign Function and Memory API supersedes the JNI, due to its reduced boilerplate and simplified interface.
