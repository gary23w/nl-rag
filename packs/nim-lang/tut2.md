---
title: "Nim Tutorial (Part II)"
source: https://nim-lang.org/docs/tut2.html
domain: nim-lang
license: CC-BY-SA-4.0
tags: nim language, nim lang, nimble, nim compiler
fetched: 2026-07-02
---

# Nim Tutorial (Part II)

Source

Edit

Author:Andreas Rumpf Version:2.2.10 "Repetition renders the ridiculous reasonable." -- Norman Wildberger

This document is a tutorial for the advanced constructs of the *Nim* programming language. **Note that this document is somewhat obsolete as the** manual **contains many more examples of the advanced language features.**

Pragmas are Nim's method to give the compiler additional information/ commands without introducing a massive number of new keywords. Pragmas are enclosed in the special {. and .} curly dot brackets. This tutorial does not cover pragmas. See the manual or user guide for a description of the available pragmas.

While Nim's support for object oriented programming (OOP) is minimalistic, powerful OOP techniques can be used. OOP is seen as *one* way to design a program, not *the only* way. Often a procedural approach leads to simpler and more efficient code. In particular, preferring composition over inheritance is often the better design.

Inheritance in Nim is entirely optional. To enable inheritance with runtime type information the object needs to inherit from RootObj. This can be done directly, or indirectly by inheriting from an object that inherits from RootObj. Usually types with inheritance are also marked as ref types even though this isn't strictly enforced. To check at runtime if an object is of a certain type, the of operator can be used.

type Person = ref object of RootObj name*: string age: int Student = ref object of Person id: int var student: Student person: Person assert(student of Student) student = Student(name: "Anton", age: 5, id: 2) echo student[]

Inheritance is done with the object of syntax. Multiple inheritance is currently not supported. If an object type has no suitable ancestor, RootObj can be used as its ancestor, but this is only a convention. Objects that have no ancestor are implicitly final. You can use the inheritable pragma to introduce new object roots apart from system.RootObj. (This is used in the GTK wrapper for instance.)

Ref objects should be used whenever inheritance is used. It isn't strictly necessary, but with non-ref objects, assignments such as let person: Person = Student(id: 123) will truncate subclass fields.

**Note**: Composition (*has-a* relation) is often preferable to inheritance (*is-a* relation) for simple code reuse. Since objects are value types in Nim, composition is as efficient as inheritance.

Concepts like abstract classes, protocols, traits, and interfaces can be simulated as objects of closures:

type IntFieldInterface = object getter: proc (): int setter: proc (x: int) proc outer: IntFieldInterface = var captureMe = 0 proc getter(): int = result = captureMe proc setter(x: int) = captureMe = x result = IntFieldInterface(getter: getter, setter: setter)

Objects, tuples and references can model quite complex data structures which depend on each other; they are *mutually recursive*. In Nim these types can only be declared within a single type section. (Anything else would require arbitrary symbol lookahead which slows down compilation.)

Example:

type Node = ref object le, ri: Node sym: ref Sym Sym = object name: string line: int code: Node

Nim distinguishes between type casts and type conversions. Casts are done with the cast operator and force the compiler to interpret a bit pattern to be of another type.

Type conversions are a much more polite way to convert a type into another: They preserve the abstract *value*, not necessarily the *bit-pattern*. If a type conversion is not possible, the compiler complains or an exception is raised.

The syntax for type conversions is destination_type(expression_to_convert) (like an ordinary call):

proc getID(x: Person): int = Student(x).id

The InvalidObjectConversionDefect exception is raised if x is not a Student.

Often an object hierarchy is overkill in certain situations where simple variant types are needed.

An example:

type NodeKind = enum nkInt, nkFloat, nkString, nkAdd, nkSub, nkIf Node = ref object case kind: NodeKind of nkInt: intVal: int of nkFloat: floatVal: float of nkString: strVal: string of nkAdd, nkSub: leftOp, rightOp: Node of nkIf: condition, thenPart, elsePart: Node var n = Node(kind: nkFloat, floatVal: 1.0) n.strVal = ""

As can be seen from the example, an advantage to an object hierarchy is that no conversion between different object types is needed. Yet, access to invalid object fields raises an exception.

There is a syntactic sugar for calling routines: The syntax obj.methodName(args) can be used instead of methodName(obj, args). If there are no remaining arguments, the parentheses can be omitted: obj.len (instead of len(obj)).

This method call syntax is not restricted to objects, it can be used for any type:

import std/strutils echo "abc".len echo "abc".toUpperAscii() echo({'a', 'b', 'c'}.card) stdout.writeLine("Hallo")

(Another way to look at the method call syntax is that it provides the missing postfix notation.)

So "pure object oriented" code is easy to write:

import std/[strutils, sequtils] stdout.writeLine("Give a list of numbers (separated by spaces): ") stdout.write(stdin.readLine.splitWhitespace.map(parseInt).max.`$`) stdout.writeLine(" is the maximum!")

As the above example shows, Nim has no need for *get-properties*: Ordinary get-procedures that are called with the *method call syntax* achieve the same. But setting a value is different; for this a special setter syntax is needed:

type Socket* = ref object of RootObj h: int proc `host=`*(s: var Socket, value: int) {.inline.} = s.h = value proc host*(s: Socket): int {.inline.} = s.h var s: Socket new s s.host = 34

(The example also shows inline procedures.)

The [] array access operator can be overloaded to provide array properties:

type Vector* = object x, y, z: float proc `[]=`* (v: var Vector, i: int, value: float) = case i of 0: v.x = value of 1: v.y = value of 2: v.z = value else: assert(false) proc `[]`* (v: Vector, i: int): float = case i of 0: result = v.x of 1: result = v.y of 2: result = v.z else: assert(false)

The example is silly, since a vector is better modelled by a tuple which already provides v[] access.

Procedures always use static dispatch. For dynamic dispatch replace the proc keyword by method:

type Expression = ref object of RootObj Literal = ref object of Expression x: int PlusExpr = ref object of Expression a, b: Expression method eval(e: Expression): int {.base.} = quit "to override!" method eval(e: Literal): int = e.x method eval(e: PlusExpr): int = eval(e.a) + eval(e.b) proc newLit(x: int): Literal = Literal(x: x) proc newPlus(a, b: Expression): PlusExpr = PlusExpr(a: a, b: b) echo eval(newPlus(newPlus(newLit(1), newLit(2)), newLit(4)))

Note that in the example the constructors newLit and newPlus are procs because it makes more sense for them to use static binding, but eval is a method because it requires dynamic binding.

**Note:** Starting from Nim 0.20, to use multi-methods one must explicitly pass --multimethods:on when compiling.

In a multi-method all parameters that have an object type are used for the dispatching:

type Thing = ref object of RootObj Unit = ref object of Thing x: int method collide(a, b: Thing) {.inline.} = quit "to override!" method collide(a: Thing, b: Unit) {.inline.} = echo "1" method collide(a: Unit, b: Thing) {.inline.} = echo "2" var a, b: Unit new a new b collide(a, b)

As the example demonstrates, invocation of a multi-method cannot be ambiguous: Collide 2 is preferred over collide 1 because the resolution works from left to right. Thus Unit, Thing is preferred over Thing, Unit.

**Performance note**: Nim generates dispatch trees for methods by default. With --experimental:vtables, it also provides an option to generate a virtual method table for methods, which tends to produce better performance in general, especially for deep object hierarchies. However, other optimizations like compile time evaluation or dead code elimination do not work with methods.

In Nim exceptions are objects. By convention, exception types are suffixed with 'Error'. The system module defines an exception hierarchy that you might want to stick to. Exceptions derive from system.Exception, which provides the common interface.

Exceptions have to be allocated on the heap because their lifetime is unknown. The compiler will prevent you from raising an exception created on the stack. All raised exceptions should at least specify the reason for being raised in the msg field.

A convention is that exceptions should be raised in *exceptional* cases, they should not be used as an alternative method of control flow.

Raising an exception is done with the raise statement:

var e: ref OSError new(e) e.msg = "the request to the OS failed" raise e

If the raise keyword is not followed by an expression, the last exception is *re-raised*. For the purpose of avoiding repeating this common code pattern, the template newException in the system module can be used:

raise newException(OSError, "the request to the OS failed")

The try statement handles exceptions:

from std/strutils import parseInt var f: File if open(f, "numbers.txt"): try: let a = readLine(f) let b = readLine(f) echo "sum: ", parseInt(a) + parseInt(b) except OverflowDefect: echo "overflow!" except ValueError: echo "could not convert string to integer" except IOError: echo "IO error!" except CatchableError: echo "Unknown exception!" raise finally: close(f)

The statements after the try are executed unless an exception is raised. Then the appropriate except part is executed.

The empty except part is executed if there is an exception that is not explicitly listed. It is similar to an else part in if statements.

If there is a finally part, it is always executed after the exception handlers.

The exception is *consumed* in an except part. If an exception is not handled, it is propagated through the call stack. This means that often the rest of the procedure - that is not within a finally clause - is not executed (if an exception occurs).

If you need to *access* the actual exception object or message inside an except branch you can use the getCurrentException() and getCurrentExceptionMsg() procs from the system module. Example:

try: doSomethingHere() except CatchableError: let e = getCurrentException() msg = getCurrentExceptionMsg() echo "Got exception ", repr(e), " with message ", msg

Through the use of the optional {.raises.} pragma you can specify that a proc is meant to raise a specific set of exceptions, or none at all. If the {.raises.} pragma is used, the compiler will verify that this is true. For instance, if you specify that a proc raises IOError, and at some point it (or one of the procs it calls) starts raising a new exception the compiler will prevent that proc from compiling. Usage example:

proc complexProc() {.raises: [IOError, ArithmeticDefect].} = ... proc simpleProc() {.raises: [].} = ...

Once you have code like this in place, if the list of raised exception changes the compiler will stop with an error specifying the line of the proc which stopped validating the pragma and the raised exception not being caught, along with the file and line where the uncaught exception is being raised, which may help you locate the offending code which has changed.

If you want to add the {.raises.} pragma to existing code, the compiler can also help you. You can add the {.effects.} pragma statement to your proc and the compiler will output all inferred effects up to that point (exception tracking is part of Nim's effect system). Another more roundabout way to find out the list of exceptions raised by a proc is to use the Nim doc command which generates documentation for a whole module and decorates all procs with the list of raised exceptions. You can read more about Nim's effect system and related pragmas in the manual.

Generics are Nim's means to parametrize procs, iterators or types with type parameters. Generic parameters are written within square brackets, for example Foo[T]. They are most useful for efficient type safe containers:

type BinaryTree*[T] = ref object le, ri: BinaryTree[T] data: T proc newNode*[T](data: T): BinaryTree[T] = new(result) result.data = data proc add*[T](root: var BinaryTree[T], n: BinaryTree[T]) = if root == nil: root = n else: var it = root while it != nil: var c = cmp(it.data, n.data) if c < 0: if it.le == nil: it.le = n return it = it.le else: if it.ri == nil: it.ri = n return it = it.ri proc add*[T](root: var BinaryTree[T], data: T) = add(root, newNode(data)) iterator preorder*[T](root: BinaryTree[T]): T = var stack: seq[BinaryTree[T]] = @[root] while stack.len > 0: var n = stack.pop() while n != nil: yield n.data add(stack, n.ri) n = n.le var root: BinaryTree[string] add(root, newNode("hello")) add(root, "world") for str in preorder(root): stdout.writeLine(str)

The example shows a generic binary tree. Depending on context, the brackets are used either to introduce type parameters or to instantiate a generic proc, iterator or type. As the example shows, generics work with overloading: the best match of add is used. The built-in add procedure for sequences is not hidden and is used in the preorder iterator.

There is a special [:T] syntax when using generics with the method call syntax:

proc foo[T](i: T) = discard var i: int i.foo[:int]()

Templates are a simple substitution mechanism that operates on Nim's abstract syntax trees. Templates are processed in the semantic pass of the compiler. They integrate well with the rest of the language and share none of C's preprocessor macros flaws.

To *invoke* a template, call it like a procedure.

Example:

template `!=` (a, b: untyped): untyped = not (a == b) assert(5 != 6)

The !=, >, >=, in, notin, isnot operators are in fact templates: this has the benefit that if you overload the == operator, the != operator is available automatically and does the right thing. (Except for IEEE floating point numbers - NaN breaks basic boolean logic.)

a > b is transformed into b < a. a in b is transformed into contains(b, a). notin and isnot have the obvious meanings.

Templates are especially useful for lazy evaluation purposes. Consider a simple proc for logging:

const debug = true proc log(msg: string) {.inline.} = if debug: stdout.writeLine(msg) var x = 4 log("x has the value: " & $x)

This code has a shortcoming: if debug is set to false someday, the quite expensive $ and & operations are still performed! (The argument evaluation for procedures is *eager*).

Turning the log proc into a template solves this problem:

const debug = true template log(msg: string) = if debug: stdout.writeLine(msg) var x = 4 log("x has the value: " & $x)

The parameters' types can be ordinary types or the meta types untyped, typed, or type. type suggests that only a type symbol may be given as an argument, and untyped means symbol lookups and type resolution is not performed before the expression is passed to the template.

If the template has no explicit return type, void is used for consistency with procs and methods.

To pass a block of statements to a template, use untyped for the last parameter:

template withFile(f: untyped, filename: string, mode: FileMode, body: untyped) = let fn = filename var f: File if open(f, fn, mode): try: body finally: close(f) else: quit("cannot open: " & fn) withFile(txt, "ttempl3.txt", fmWrite): txt.writeLine("line 1") txt.writeLine("line 2")

In the example the two writeLine statements are bound to the body parameter. The withFile template contains boilerplate code and helps to avoid a common bug: to forget to close the file. Note how the let fn = filename statement ensures that filename is evaluated only once.

import std/math template liftScalarProc(fname) = proc fname[T](x: openarray[T]): auto = var temp: T type outType = typeof(fname(temp)) result = newSeq[outType](x.len) for i in 0..<x.len: result[i] = fname(x[i]) liftScalarProc(sqrt) echo sqrt(@[4.0, 16.0, 25.0, 36.0])

Nim code can be compiled to JavaScript. However in order to write JavaScript-compatible code you should remember the following:

- addr and ptr have slightly different semantic meaning in JavaScript. It is recommended to avoid those if you're not sure how they are translated to JavaScript.
- cast[T](x) in JavaScript is translated to (x), except for casting between signed/unsigned ints, in which case it behaves as static cast in C language.
- cstring in JavaScript means JavaScript string. It is a good practice to use cstring only when it is semantically appropriate. E.g. don't use cstring as a binary data buffer.

The next part is entirely about metaprogramming via macros: Part III.
