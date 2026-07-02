---
title: "Nim Manual (part 5/5)"
source: https://nim-lang.org/docs/manual.html
domain: nim-lang
license: CC-BY-SA-4.0
tags: nim language, nim lang, nimble, nim compiler
fetched: 2026-07-02
part: 5/5
---

# Nim Manual

{.link: "/usr/lib/libIrrlicht.so".} {.emit: """ using namespace irr; using namespace core; using namespace scene; using namespace video; using namespace io; using namespace gui; """.} const irr = "<irrlicht/irrlicht.h>" type IrrlichtDeviceObj {.header: irr, importcpp: "IrrlichtDevice".} = object IrrlichtDevice = ptr IrrlichtDeviceObj proc createDevice(): IrrlichtDevice {. header: irr, importcpp: "createDevice(@)".} proc run(device: IrrlichtDevice): bool {. header: irr, importcpp: "#.run(@)".}

The compiler needs to be told to generate C++ (command cpp) for this to work. The conditional symbol cpp is defined when the compiler emits C++ code.

The *sloppy interfacing* example uses .emit to produce using namespace declarations. It is usually much better to instead refer to the imported name via the namespace::identifier notation:

type IrrlichtDeviceObj {.header: irr, importcpp: "irr::IrrlichtDevice".} = object

When importcpp is applied to an enum type the numerical enum values are annotated with the C++ enum type, like in this example: ((TheCppEnum)(3)). (This turned out to be the simplest way to implement it.)

Note that the importcpp variant for procs uses a somewhat cryptic pattern language for maximum flexibility:

- A hash # symbol is replaced by the first or next argument.
- A dot following the hash #. indicates that the call should use C++'s dot or arrow notation.
- An at symbol @ is replaced by the remaining arguments, separated by commas.

For example:

proc cppMethod(this: CppObj, a, b, c: cint) {.importcpp: "#.CppMethod(@)".} var x: ptr CppObj cppMethod(x[], 1, 2, 3)

Produces:

x->CppMethod(1, 2, 3)

As a special rule to keep backward compatibility with older versions of the importcpp pragma, if there is no special pattern character (any of # ' @) at all, C++'s dot or arrow notation is assumed, so the above example can also be written as:

proc cppMethod(this: CppObj, a, b, c: cint) {.importcpp: "CppMethod".}

Note that the pattern language naturally also covers C++'s operator overloading capabilities:

proc vectorAddition(a, b: Vec3): Vec3 {.importcpp: "# + #".} proc dictLookup(a: Dict, k: Key): Value {.importcpp: "#[#]".}

- An apostrophe ' followed by an integer i in the range 0..9 is replaced by the i'th parameter *type*. The 0th position is the result type. This can be used to pass types to C++ function templates. Between the ' and the digit, an asterisk can be used to get to the base type of the type. (So it "takes away a star" from the type; T* becomes T.) Two stars can be used to get to the element type of the element type etc.

For example:

type Input {.importcpp: "System::Input".} = object proc getSubsystem*[T](): ptr T {.importcpp: "SystemManager::getSubsystem<'*0>()", nodecl.} let x: ptr Input = getSubsystem[Input]()

Produces:

x = SystemManager::getSubsystem<System::Input>()

- #@ is a special case to support a cnew operation. It is required so that the call expression is inlined directly, without going through a temporary location. This is only required to circumvent a limitation of the current code generator.

For example C++'s new operator can be "imported" like this:

proc cnew*[T](x: T): ptr T {.importcpp: "(new '*0#@)", nodecl.} proc constructFoo(a, b: cint): Foo {.importcpp: "Foo(@)".} let x = cnew constructFoo(3, 4)

Produces:

x = new Foo(3, 4)

However, depending on the use case new Foo can also be wrapped like this instead:

proc newFoo(a, b: cint): ptr Foo {.importcpp: "new Foo(@)".} let x = newFoo(3, 4)

Sometimes a C++ class has a private copy constructor and so code like Class c = Class(1,2); must not be generated but instead Class c(1,2);. For this purpose the Nim proc that wraps a C++ constructor needs to be annotated with the constructor pragma. This pragma also helps to generate faster C++ code since construction then doesn't invoke the copy constructor:

proc constructFoo(a, b: cint): Foo {.importcpp: "Foo(@)", constructor.}

Since Nim generates C++ directly, any destructor is called implicitly by the C++ compiler at the scope exits. This means that often one can get away with not wrapping the destructor at all! However, when it needs to be invoked explicitly, it needs to be wrapped. The pattern language provides everything that is required:

proc destroyFoo(this: var Foo) {.importcpp: "#.~Foo()".}

Generic importcpp'ed objects are mapped to C++ templates. This means that one can import C++'s templates rather easily without the need for a pattern language for object types:

type StdMap[K, V] {.importcpp: "std::map", header: "<map>".} = object proc `[]=`[K, V](this: var StdMap[K, V]; key: K; val: V) {. importcpp: "#[#] = #", header: "<map>".} var x: StdMap[cint, cdouble] x[6] = 91.4

Produces:

std::map<int, double> x; x[6] = 91.4;

- If more precise control is needed, the apostrophe ' can be used in the supplied pattern to denote the concrete type parameters of the generic type. See the usage of the apostrophe operator in proc patterns for more details. type VectorIterator[T] {.importcpp: "std::vector<'0>::iterator".} = object var x: VectorIterator[cint] Produces: std::vector<int>::iterator x;

Similar to the importcpp pragma for C++, the importjs pragma can be used to import Javascript methods or symbols in general. The generated code then uses the Javascript method calling syntax: obj.method(arg).

Similar to the importc pragma for C, the importobjc pragma can be used to import Objective C methods. The generated code then uses the Objective C method calling syntax: [obj method param1: arg]. In addition with the header and emit pragmas this allows *sloppy* interfacing with libraries written in Objective C:

{.passl: "-lobjc".} {.emit: """ #include <objc/Object.h> @interface Greeter:Object { } - (void)greet:(long)x y:(long)dummy; @end #include <stdio.h> @implementation Greeter - (void)greet:(long)x y:(long)dummy { printf("Hello, World!\n"); } @end #include <stdlib.h> """.} type Id {.importc: "id", header: "<objc/Object.h>", final.} = distinct int proc newGreeter: Id {.importobjc: "Greeter new", nodecl.} proc greet(self: Id, x, y: int) {.importobjc: "greet", nodecl.} proc free(self: Id) {.importobjc: "free", nodecl.} var g = newGreeter() g.greet(12, 34) g.free()

The compiler needs to be told to generate Objective C (command objc) for this to work. The conditional symbol objc is defined when the compiler emits Objective C code.

The codegenDecl pragma can be used to directly influence Nim's code generator. It receives a format string that determines how the variable, proc or object type is declared in the generated code.

For variables, $1 in the format string represents the type of the variable, $2 is the name of the variable, and each appearance of $# represents $1/$2 respectively according to its position.

The following Nim code:

var a {.codegenDecl: "$# progmem $#".}: int

will generate this C code:

int progmem a

For procedures, $1 is the return type of the procedure, $2 is the name of the procedure, $3 is the parameter list, and each appearance of $# represents $1/$2/$3 respectively according to its position.

The following nim code:

proc myinterrupt() {.codegenDecl: "__interrupt $# $#$#".} = echo "realistic interrupt handler"

will generate this code:

__interrupt void myinterrupt()

For object types, the $1 represents the name of the object type, $2 is the list of fields and $3 is the base type.

const strTemplate = """ struct $1 { $2 }; """ type Foo {.codegenDecl:strTemplate.} = object a, b: int

will generate this code:

struct Foo { NI a; NI b; };

The cppNonPod pragma should be used for non-POD importcpp types so that they work properly (in particular regarding constructor and destructor) for threadvar variables. This requires --tlsEmulation:off.

type Foo {.cppNonPod, importcpp, header: "funs.h".} = object x: cint proc main()= var a {.threadvar.}: Foo

The pragmas listed here can be used to optionally accept values from the -d/--define option at compile time.

The implementation currently provides the following possible options (various others may be added later).

| pragma | description |
|---|---|
| intdefine | Reads in a build-time define as an integer |
| strdefine | Reads in a build-time define as a string |
| booldefine | Reads in a build-time define as a bool |

const FooBar {.intdefine.}: int = 5 echo FooBar

nim c -d:FooBar=42 foobar.nim

In the above example, providing the -d flag causes the symbol FooBar to be overwritten at compile-time, printing out 42. If the -d:FooBar=42 were to be omitted, the default value of 5 would be used. To see if a value was provided, defined(FooBar) can be used.

The syntax -d:flag is actually just a shortcut for -d:flag=true.

These pragmas also accept an optional string argument for qualified define names.

const FooBar {.intdefine: "package.FooBar".}: int = 5 echo FooBar

nim c -d:package.FooBar=42 foobar.nim

This helps disambiguate define names in different packages.

See also the generic `define` pragma for a version of these pragmas that detects the type of the define based on the constant value.

The pragma pragma can be used to declare user-defined pragmas. This is useful because Nim's templates and macros do not affect pragmas. User-defined pragmas are in a different module-wide scope than all other symbols. They cannot be imported from a module.

Example:

when appType == "lib": {.pragma: rtl, exportc, dynlib, cdecl.} else: {.pragma: rtl, importc, dynlib: "client.dll", cdecl.} proc p*(a, b: int): int {.rtl.} = result = a + b

In the example, a new pragma named rtl is introduced that either imports a symbol from a dynamic library or exports the symbol for dynamic library generation.

It is possible to define custom typed pragmas. Custom pragmas do not affect code generation directly, but their presence can be detected by macros. Custom pragmas are defined using templates annotated with pragma pragma:

template dbTable(name: string, table_space: string = "") {.pragma.} template dbKey(name: string = "", primary_key: bool = false) {.pragma.} template dbForeignKey(t: typedesc) {.pragma.} template dbIgnore {.pragma.}

Consider this stylized example of a possible Object Relation Mapping (ORM) implementation:

const tblspace {.strdefine.} = "dev" type User {.dbTable("users", tblspace).} = object id {.dbKey(primary_key = true).}: int name {.dbKey"full_name".}: string is_cached {.dbIgnore.}: bool age: int UserProfile {.dbTable("profiles", tblspace).} = object id {.dbKey(primary_key = true).}: int user_id {.dbForeignKey: User.}: int read_access: bool write_access: bool admin_access: bool

In this example, custom pragmas are used to describe how Nim objects are mapped to the schema of the relational database. Custom pragmas can have zero or more arguments. In order to pass multiple arguments use one of template call syntaxes. All arguments are typed and follow standard overload resolution rules for templates. Therefore, it is possible to have default values for arguments, pass by name, varargs, etc.

Custom pragmas can be used in all locations where ordinary pragmas can be specified. It is possible to annotate procs, templates, type and variable definitions, statements, etc.

The macros module includes helpers which can be used to simplify custom pragma access hasCustomPragma, getCustomPragmaVal. Please consult the macros module documentation for details. These macros are not magic, everything they do can also be achieved by walking the AST of the object representation.

More examples with custom pragmas:

- Better serialization/deserialization control: type MyObj = object a {.dontSerialize.}: int b {.defaultDeserialize: 5.}: int c {.serializationKey: "_c".}: string
- Adopting type for gui inspector in a game engine: type MyComponent = object position {.editable, animatable.}: Vector3 alpha {.editRange: [0.0..1.0], animatable.}: float32

Macros and templates can sometimes be called with the pragma syntax. Cases where this is possible include when attached to routine (procs, iterators, etc.) declarations or routine type expressions. The compiler will perform the following simple syntactic transformations:

template command(name: string, def: untyped) = discard proc p() {.command("print").} = discard

This is translated to:

command("print"): proc p() = discard

type AsyncEventHandler = proc (x: Event) {.async.}

This is translated to:

type AsyncEventHandler = async(proc (x: Event))

When multiple macro pragmas are applied to the same definition, the first one from left to right will be evaluated. This macro can then choose to keep the remaining macro pragmas in its output, and those will be evaluated in the same way.

There are a few more applications of macro pragmas, such as in type, variable and constant declarations, but this behavior is considered to be experimental and is documented in the experimental manual instead.

Nim's FFI (foreign function interface) is extensive and only the parts that scale to other future backends (like the LLVM/JavaScript backends) are documented here.

The importc pragma provides a means to import a proc or a variable from C. The optional argument is a string containing the C identifier. If the argument is missing, the C name is the Nim identifier *exactly as spelled*:

proc printf(formatstr: cstring) {.header: "<stdio.h>", importc: "printf", varargs.}

When importc is applied to a let statement it can omit its value which will then be expected to come from C. This can be used to import a C const:

{.emit: "const int cconst = 42;".} let cconst {.importc, nodecl.}: cint assert cconst == 42

Note that this pragma has been abused in the past to also work in the JS backend for JS objects and functions. Other backends do provide the same feature under the same name. Also, when the target language is not set to C, other pragmas are available:

- importcpp
- importobjc
- importjs

The string literal passed to importc can be a format string:

proc p(s: cstring) {.importc: "prefix$1".}

In the example, the external name of p is set to prefixp. Only $1 is available and a literal dollar sign must be written as $$.

The exportc pragma provides a means to export a type, a variable, or a procedure to C. Enums and constants can't be exported. The optional argument is a string containing the C identifier. If the argument is missing, the C name is the Nim identifier *exactly as spelled*:

proc callme(formatstr: cstring) {.exportc: "callMe", varargs.}

Note that this pragma is somewhat of a misnomer: Other backends do provide the same feature under the same name.

The string literal passed to exportc can be a format string:

proc p(s: string) {.exportc: "prefix$1".} = echo s

In the example, the external name of p is set to prefixp. Only $1 is available and a literal dollar sign must be written as $$.

If the symbol should also be exported to a dynamic library, the dynlib pragma should be used in addition to the exportc pragma. See Dynlib pragma for export.

The exportcpp pragma works like the exportc pragma but it requires the cpp backend. When compiled with the cpp backend, the exportc pragma adds export "C" to the declaration in the generated code so that it can be called from both C and C++ code. exportcpp pragma doesn't add export "C".

Like exportc or importc, the extern pragma affects name mangling. The string literal passed to extern can be a format string:

proc p(s: string) {.extern: "prefix$1".} = echo s

In the example, the external name of p is set to prefixp. Only $1 is available and a literal dollar sign must be written as $$.

The bycopy pragma can be applied to an object or tuple type or a proc param. It instructs the compiler to pass the type by value to procs:

type Vector {.bycopy.} = object x, y, z: float

The Nim compiler automatically determines whether a parameter is passed by value or by reference based on the parameter type's size. If a parameter must be passed by value or by reference, (such as when interfacing with a C library) use the bycopy or byref pragmas. Notice params marked as byref takes precedence over types marked as bycopy.

The byref pragma can be applied to an object or tuple type or a proc param. When applied to a type it instructs the compiler to pass the type by reference (hidden pointer) to procs. When applied to a param it will take precedence, even if the the type was marked as bycopy. When an importc type has a byref pragma or parameters are marked as byref in an importc proc, these params translate to pointers. When an importcpp type has a byref pragma, these params translate to C++ references &.

{.emit: """/*TYPESECTION*/ typedef struct { int x; } CStruct; """.} {.emit: """ #ifdef __cplusplus extern "C" #endif int takesCStruct(CStruct* x) { return x->x; } """.} type CStruct {.importc, byref.} = object x: cint proc takesCStruct(x: CStruct): cint {.importc.}

or

type CStruct {.importc.} = object x: cint proc takesCStruct(x {.byref.}: CStruct): cint {.importc.}

{.emit: """/*TYPESECTION*/ struct CppStruct { int x; int takesCppStruct(CppStruct& y) { return x + y.x; } }; """.} type CppStruct {.importcpp, byref.} = object x: cint proc takesCppStruct(x, y: CppStruct): cint {.importcpp.}

The varargs pragma can be applied to procedures only (and procedure types). It tells Nim that the proc can take a variable number of parameters after the last specified parameter. Nim string values will be converted to C strings automatically:

proc printf(formatstr: cstring) {.header: "<stdio.h>", varargs.} printf("hallo %s", "world")

The union pragma can be applied to any object type. It means all of an object's fields are overlaid in memory. This produces a union instead of a struct in the generated C/C++ code. The object declaration then must not use inheritance or any GC'ed memory but this is currently not checked.

**Future directions**: GC'ed memory should be allowed in unions and the GC should scan unions conservatively.

The packed pragma can be applied to any object type. It ensures that the fields of an object are packed back-to-back in memory. It is useful to store packets or messages from/to network or hardware drivers, and for interoperability with C. Combining packed pragma with inheritance is not defined, and it should not be used with GC'ed memory (ref's).

**Future directions**: Using GC'ed memory in packed pragma will result in a static error. Usage with inheritance should be defined and documented.

With the dynlib pragma, a procedure or a variable can be imported from a dynamic library (.dll files for Windows, lib*.so files for UNIX). The non-optional argument has to be the name of the dynamic library:

proc gtk_image_new(): PGtkWidget {.cdecl, dynlib: "libgtk-x11-2.0.so", importc.}

In general, importing a dynamic library does not require any special linker options or linking with import libraries. This also implies that no *devel* packages need to be installed.

The dynlib import mechanism supports a versioning scheme:

proc Tcl_Eval(interp: pTcl_Interp, script: cstring): int {.cdecl, importc, dynlib: "libtcl(|8.5|8.4|8.3).so.(1|0)".}

At runtime, the dynamic library is searched for (in this order):

```
libtcl.so.1
libtcl.so.0
libtcl8.5.so.1
libtcl8.5.so.0
libtcl8.4.so.1
libtcl8.4.so.0
libtcl8.3.so.1
libtcl8.3.so.0
```

The dynlib pragma supports not only constant strings as an argument but also string expressions in general:

import std/os proc getDllName: string = result = "mylib.dll" if fileExists(result): return result = "mylib2.dll" if fileExists(result): return quit("could not load dynamic library") proc myImport(s: cstring) {.cdecl, importc, dynlib: getDllName().}

**Note**: Patterns like libtcl(|8.5|8.4).so are only supported in constant strings, because they are precompiled.

**Note**: Passing variables to the dynlib pragma will fail at runtime because of order of initialization problems.

**Note**: A dynlib import can be overridden with the --dynlibOverride:name command-line option. The Compiler User Guide contains further information.

With the dynlib pragma, a procedure can also be exported to a dynamic library. The pragma then has no argument and has to be used in conjunction with the exportc pragma:

proc exportme(): int {.cdecl, exportc, dynlib.}

This is only useful if the program is compiled as a dynamic library via the --app:lib command-line option.

The --threads:on command-line switch is enabled by default. The typedthreads module module then contains several threading primitives. See spawn for further details.

The only ways to create a thread is via spawn or createThread.

A proc that is executed as a new thread of execution should be marked by the thread pragma for reasons of readability. The compiler checks for violations of the no heap sharing restriction: This restriction implies that it is invalid to construct a data structure that consists of memory allocated from different (thread-local) heaps.

A thread proc can be passed to createThread or spawn.

A variable can be marked with the threadvar pragma, which makes it a thread-local variable; Additionally, this implies all the effects of the global pragma.

var checkpoints* {.threadvar.}: seq[string]

Due to implementation restrictions, thread-local variables cannot be initialized within the var section. (Every thread-local variable needs to be replicated at thread creation.)

The interaction between threads and exceptions is simple: A *handled* exception in one thread cannot affect any other thread. However, an *unhandled* exception in one thread terminates the whole *process*.

Nim provides common low level concurrency mechanisms like locks, atomic intrinsics or condition variables.

Nim significantly improves on the safety of these features via additional pragmas:

1. A guard annotation is introduced to prevent data races.
2. Every access of a guarded memory location needs to happen in an appropriate locks statement.

Object fields and global variables can be annotated via a guard pragma:

import std/locks var glock: Lock var gdata {.guard: glock.}: int

The compiler then ensures that every access of gdata is within a locks section:

proc invalid = echo gdata proc valid = {.locks: [glock].}: echo gdata

Top level accesses to gdata are always allowed so that it can be initialized conveniently. It is *assumed* (but not enforced) that every top level statement is executed before any concurrent action happens.

The locks section deliberately looks ugly because it has no runtime semantics and should not be used directly! It should only be used in templates that also implement some form of locking at runtime:

template lock(a: Lock; body: untyped) = pthread_mutex_lock(a) {.locks: [a].}: try: body finally: pthread_mutex_unlock(a)

The guard does not need to be of any particular type. It is flexible enough to model low level lockfree mechanisms:

var dummyLock {.compileTime.}: int var atomicCounter {.guard: dummyLock.}: int template atomicRead(x): untyped = {.locks: [dummyLock].}: memoryReadBarrier() x echo atomicRead(atomicCounter)

The locks pragma takes a list of lock expressions locks: [a, b, ...] in order to support *multi lock* statements.

The guard annotation can also be used to protect fields within an object. The guard then needs to be another field within the same object or a global variable.

Since objects can reside on the heap or on the stack, this greatly enhances the expressiveness of the language:

import std/locks type ProtectedCounter = object v {.guard: L.}: int L: Lock proc incCounters(counters: var openArray[ProtectedCounter]) = for i in 0..counters.high: lock counters[i].L: inc counters[i].v

The access to field x.v is allowed since its guard x.L is active. After template expansion, this amounts to:

proc incCounters(counters: var openArray[ProtectedCounter]) = for i in 0..counters.high: pthread_mutex_lock(counters[i].L) {.locks: [counters[i].L].}: try: inc counters[i].v finally: pthread_mutex_unlock(counters[i].L)

There is an analysis that checks that counters[i].L is the lock that corresponds to the protected location counters[i].v. This analysis is called path analysis because it deals with paths to locations like obj.field[i].fieldB[j].

The path analysis is **currently unsound**, but that doesn't make it useless. Two paths are considered equivalent if they are syntactically the same.

This means the following compiles (for now) even though it really should not:

{.locks: [a[i].L].}: inc i access a[i].v
