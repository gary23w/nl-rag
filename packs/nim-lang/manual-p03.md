---
title: "Nim Manual (part 3/5)"
source: https://nim-lang.org/docs/manual.html
domain: nim-lang
license: CC-BY-SA-4.0
tags: nim language, nim lang, nimble, nim compiler
fetched: 2026-07-02
part: 3/5
---

# Nim Manual

As can be seen in the example, base methods have to be annotated with the base pragma. The base pragma also acts as a reminder for the programmer that a base method m is used as the foundation to determine all the effects that a call to m might cause.

**Note**: Compile-time execution is not (yet) supported for methods.

**Note**: Starting from Nim 0.20, generic methods are deprecated.

**Note:** Starting from Nim 0.20, to use multi-methods one must explicitly pass --multimethods:on when compiling.

In a multi-method, all parameters that have an object type are used for the dispatching:

type Thing = ref object of RootObj Unit = ref object of Thing x: int method collide(a, b: Thing) {.base, inline.} = quit "to override!" method collide(a: Thing, b: Unit) {.inline.} = echo "1" method collide(a: Unit, b: Thing) {.inline.} = echo "2" var a, b: Unit new a new b collide(a, b)

Dynamic method resolution can be inhibited via the builtin system.procCall. This is somewhat comparable to the super keyword that traditional OOP languages offer.

type Thing = ref object of RootObj Unit = ref object of Thing x: int method m(a: Thing) {.base.} = echo "base" method m(a: Unit) = procCall m(Thing(a)) echo "1"

The for statement is an abstract mechanism to iterate over the elements of a container. It relies on an iterator to do so. Like while statements, for statements open an implicit block so that they can be left with a break statement.

The for loop declares iteration variables - their scope reaches until the end of the loop body. The iteration variables' types are inferred by the return type of the iterator.

An iterator is similar to a procedure, except that it can be called in the context of a for loop. Iterators provide a way to specify the iteration over an abstract type. The yield statement in the called iterator plays a key role in the execution of a for loop. Whenever a yield statement is reached, the data is bound to the for loop variables and control continues in the body of the for loop. The iterator's local variables and execution state are automatically saved between calls. Example:

iterator items*(a: string): char {.inline.} = var i = 0 while i < len(a): yield a[i] inc(i) for ch in items("hello world"): echo ch

The compiler generates code as if the programmer had written this:

var i = 0 while i < len(a): var ch = a[i] echo ch inc(i)

If the iterator yields a tuple, there can be as many iteration variables as there are components in the tuple. The i'th iteration variable's type is the type of the i'th component. In other words, implicit tuple unpacking in a for loop context is supported.

If the for loop expression e does not denote an iterator and the for loop has exactly 1 variable, the for loop expression is rewritten to items(e); i.e. an items iterator is implicitly invoked:

for x in [1,2,3]: echo x

If the for loop has exactly 2 variables, a pairs iterator is implicitly invoked.

Symbol lookup of the identifiers items/pairs is performed after the rewriting step, so that all overloads of items/pairs are taken into account.

There are 2 kinds of iterators in Nim: *inline* and *closure* iterators. An inline iterator is an iterator that's always inlined by the compiler leading to zero overhead for the abstraction, but may result in a heavy increase in code size.

Caution: the body of a for loop over an inline iterator is inlined into each yield statement appearing in the iterator code, so ideally the code should be refactored to contain a single yield when possible to avoid code bloat.

Inline iterators are second class citizens; They can be passed as parameters only to other inlining code facilities like templates, macros, and other inline iterators.

In contrast to that, a closure iterator can be passed around more freely:

iterator count0(): int {.closure.} = yield 0 iterator count2(): int {.closure.} = var x = 1 yield x inc x yield x proc invoke(iter: iterator(): int {.closure.}) = for x in iter(): echo x invoke(count0) invoke(count2)

Closure iterators and inline iterators have some restrictions:

1. For now, a closure iterator cannot be executed at compile time.
2. return is allowed in a closure iterator but not in an inline iterator (but rarely useful) and ends the iteration.
3. Inline iterators cannot be recursive.
4. Neither inline nor closure iterators have the special result variable.

Iterators that are neither marked {.closure.} nor {.inline.} explicitly default to being inline, but this may change in future versions of the implementation.

The iterator type is always of the calling convention closure implicitly.

Unlike named iterators, anonymous iterator expressions evaluate to the iterator type. In practice, this means a named iterator declaration without {.closure.} defaults to inline, but an expression like let it = iterator(): int = yield 1 produces a callable closure iterator value.

The following example shows how to use iterators to implement a collaborative tasking system:

type Task = iterator (ticker: int) iterator a1(ticker: int) {.closure.} = echo "a1: A" yield echo "a1: B" yield echo "a1: C" yield echo "a1: D" iterator a2(ticker: int) {.closure.} = echo "a2: A" yield echo "a2: B" yield echo "a2: C" proc runTasks(t: varargs[Task]) = var ticker = 0 while true: let x = t[ticker mod t.len] if finished(x): break x(ticker) inc ticker runTasks(a1, a2)

The builtin system.finished can be used to determine if an iterator has finished its operation; no exception is raised on an attempt to invoke an iterator that has already finished its work.

Note that system.finished is error-prone to use because it only returns true one iteration after the iterator has finished:

iterator mycount(a, b: int): int {.closure.} = var x = a while x <= b: yield x inc x var c = mycount while not finished(c): echo c(1, 3) 1 2 3 0

Instead, this code has to be used:

var c = mycount while true: let value = c(1, 3) if finished(c): break echo value

It helps to think that the iterator actually returns a pair (value, done) and finished is used to access the hidden done field.

Closure iterators are *resumable functions* and so one has to provide the arguments to every call. To get around this limitation one can capture parameters of an outer factory proc:

proc mycount(a, b: int): iterator (): int = result = iterator (): int = var x = a while x <= b: yield x inc x let foo = mycount(1, 4) for f in foo(): echo f

The call can be made more like an inline iterator with a for loop macro:

import std/macros macro toItr(x: ForLoopStmt): untyped = let expr = x[0] let call = x[1][1] let body = x[2] result = quote do: block: let itr = `call` for `expr` in itr(): `body` for f in toItr(mycount(1, 4)): echo f

Because of full backend function call apparatus involvement, closure iterator invocation is typically higher cost than inline iterators. Adornment by a macro wrapper at the call site like this is a possibly useful reminder.

The factory proc, as an ordinary procedure, can be recursive. The above macro allows such recursion to look much like a recursive iterator would. For example:

proc recCountDown(n: int): iterator(): int = result = iterator(): int = if n > 0: yield n for e in toItr(recCountDown(n - 1)): yield e for i in toItr(recCountDown(6)): echo i

See also iterable for passing iterators to templates and macros.

A converter is like an ordinary proc except that it enhances the "implicitly convertible" type relation (see Convertible relation):

converter toBool(x: int): bool = x != 0 if 4: echo "compiles"

A converter can also be explicitly invoked for improved readability. Note that implicit converter chaining is not supported: If there is a converter from type A to type B and from type B to type C, the implicit conversion from A to C is not provided.

Example:

type Node = ref object le, ri: Node sym: ref Sym Sym = object name: string line: int code: Node

A type section begins with the type keyword. It contains multiple type definitions. A type definition binds a type to a name. Type definitions can be recursive or even mutually recursive. Mutually recursive types are only possible within a single type section. Nominal types like objects or enums can only be defined in a type section.

Example:

var f: File if open(f, "numbers.txt"): try: var a = readLine(f) var b = readLine(f) echo "sum: " & $(parseInt(a) + parseInt(b)) except OverflowDefect: echo "overflow!" except ValueError, IOError: echo "catch multiple exceptions!" except CatchableError: echo "Catchable exception!" finally: close(f)

The statements after the try are executed in sequential order unless an exception e is raised. If the exception type of e matches any listed in an except clause, the corresponding statements are executed. The statements following the except clauses are called exception handlers.

If there is a finally clause, it is always executed after the exception handlers.

The exception is *consumed* in an exception handler. However, an exception handler may raise another exception. If the exception is not handled, it is propagated through the call stack. This means that often the rest of the procedure - that is not within a finally clause - is not executed (if an exception occurs).

Try can also be used as an expression; the type of the try branch then needs to fit the types of except branches, but the type of the finally branch always has to be void:

from std/strutils import parseInt let x = try: parseInt("133a") except ValueError: -1 finally: echo "hi"

To prevent confusing code there is a parsing limitation; if the try follows a ( it has to be written as a one liner:

from std/strutils import parseInt let x = (try: parseInt("133a") except ValueError: -1)

Within an except clause it is possible to access the current exception using the following syntax:

try: except IOError as e: echo "I/O error: " & e.msg

Alternatively, it is possible to use getCurrentException to retrieve the exception that has been raised:

try: except IOError: let e = getCurrentException()

Note that getCurrentException always returns a ref Exception type. If a variable of the proper type is needed (in the example above, IOError), one must convert it explicitly:

try: except IOError: let e = (ref IOError)(getCurrentException())

However, this is seldom needed. The most common case is to extract an error message from e, and for such situations, it is enough to use getCurrentExceptionMsg:

try: except CatchableError: echo getCurrentExceptionMsg()

It is possible to create custom exceptions. A custom exception is a custom type:

type LoadError* = object of Exception

Ending the custom exception's name with Error is recommended.

Custom exceptions can be raised just like any other exception, e.g.:

raise newException(LoadError, "Failed to load data")

Instead of a try finally statement a defer statement can be used, which avoids lexical nesting and offers more flexibility in terms of scoping as shown below.

Any statements following the defer will be considered to be in an implicit try block in the current block:

proc main = var f = open("numbers.txt", fmWrite) defer: close(f) f.write "abc" f.write "def"

Is rewritten to:

proc main = var f = open("numbers.txt") try: f.write "abc" f.write "def" finally: close(f)

When defer is at the outermost scope of a template/macro, its scope extends to the block where the template/macro is called from:

template safeOpenDefer(f, path) = var f = open(path, fmWrite) defer: close(f) template safeOpenFinally(f, path, body) = var f = open(path, fmWrite) try: body finally: close(f) block: safeOpenDefer(f, "/tmp/z01.txt") f.write "abc" block: safeOpenFinally(f, "/tmp/z01.txt"): f.write "abc" block: var f = open("/tmp/z01.txt", fmWrite) try: f.write "abc" finally: close(f)

Top-level defer statements are not supported since it's unclear what such a statement should refer to.

Example:

raise newException(IOError, "IO failed")

Apart from built-in operations like array indexing, memory allocation, etc. the raise statement is the only way to raise an exception.

If no exception name is given, the current exception is re-raised. The ReraiseDefect exception is raised if there is no exception to re-raise. It follows that the raise statement *always* raises an exception.

The exception tree is defined in the system module. Every exception inherits from system.Exception. Exceptions that indicate programming bugs inherit from system.Defect (which is a subtype of Exception) and are strictly speaking not catchable as they can also be mapped to an operation that terminates the whole process. If panics are turned into exceptions, these exceptions inherit from Defect.

Exceptions that indicate any other runtime error that can be caught inherit from system.CatchableError (which is a subtype of Exception).

Exception |-- CatchableError | |-- IOError | | `-- EOFError | |-- OSError | |-- ResourceExhaustedError | `-- ValueError | `-- KeyError `-- Defect |-- AccessViolationDefect |-- ArithmeticDefect | |-- DivByZeroDefect | `-- OverflowDefect |-- AssertionDefect |-- DeadThreadDefect |-- FieldDefect |-- FloatingPointDefect | |-- FloatDivByZeroDefect | |-- FloatInvalidOpDefect | |-- FloatOverflowDefect | |-- FloatUnderflowDefect | `-- InexactDefect |-- IndexDefect |-- NilAccessDefect |-- ObjectAssignmentDefect |-- ObjectConversionDefect |-- OutOfMemoryDefect |-- RangeDefect |-- ReraiseDefect `-- StackOverflowDefect

It is possible to raise/catch imported C++ exceptions. Types imported using importcpp can be raised or caught. Exceptions are raised by value and caught by reference. Example:

type CStdException {.importcpp: "std::exception", header: "<exception>", inheritable.} = object CRuntimeError {.requiresInit, importcpp: "std::runtime_error", header: "<stdexcept>".} = object of CStdException proc what(s: CStdException): cstring {.importcpp: "((char *)#.what())".} proc initRuntimeError(a: cstring): CRuntimeError {.importcpp: "std::runtime_error(@)", constructor.} proc initStdException(): CStdException {.importcpp: "std::exception()", constructor.} proc fn() = let a = initRuntimeError("foo") doAssert $a.what == "foo" var b = "" try: raise initRuntimeError("foo2") except CStdException as e: doAssert e is CStdException b = $e.what() doAssert b == "foo2" try: raise initStdException() except CStdException: discard try: raise initRuntimeError("foo3") except CRuntimeError as e: b = $e.what() except CStdException: doAssert false doAssert b == "foo3" fn()

**Note:** getCurrentException() and getCurrentExceptionMsg() are not available for imported exceptions from C++. One needs to use the except ImportedException as x: syntax and rely on functionality of the x object to get exception details.

**Note**: The rules for effect tracking changed with the release of version 1.6 of the Nim compiler.

Nim supports exception tracking. The raises pragma can be used to explicitly define which exceptions a proc/iterator/method/converter is allowed to raise. The compiler verifies this:

proc p(what: bool) {.raises: [IOError, OSError].} = if what: raise newException(IOError, "IO") else: raise newException(OSError, "OS")

An empty raises list (raises: []) means that no exception may be raised:

proc p(): bool {.raises: [].} = try: unsafeCall() result = true except CatchableError: result = false

A raises list can also be attached to a proc type. This affects type compatibility:

type Callback = proc (s: string) {.raises: [IOError].} var c: Callback proc p(x: string) = raise newException(OSError, "OS") c = p

For a routine p, the compiler uses inference rules to determine the set of possibly raised exceptions; the algorithm operates on p's call graph:

1. Every indirect call via some proc type T is assumed to raise system.Exception (the base type of the exception hierarchy) and thus any exception unless T has an explicit raises list. However, if the call is of the form f(...) where f is a parameter of the currently analyzed routine that is marked as .effectsOf: f, it is ignored. The call is optimistically assumed to have no effect. Rule 2 compensates for this case.
2. Every expression e of some proc type within a call that is passed to parameter marked as .effectsOf of proc p is assumed to be called indirectly and thus its raises list is added to p's raises list.
3. Every call to a proc q which has an unknown body (due to a forward declaration) is assumed to raise system.Exception unless q has an explicit raises list. Procs that are importc'ed are assumed to have .raises: [], unless explicitly declared otherwise.
4. Every call to a method m is assumed to raise system.Exception unless m has an explicit raises list.
5. For every other call, the analysis can determine an exact raises list.
6. For determining a raises list, the raise and try statements of p are taken into consideration.

Exceptions inheriting from system.Defect are not tracked with the .raises: [] exception tracking mechanism. This is more consistent with the built-in operations. The following code is valid:

proc mydiv(a, b): int {.raises: [].} = a div b

And so is:

proc mydiv(a, b): int {.raises: [].} = if b == 0: raise newException(DivByZeroDefect, "division by zero") else: result = a div b

The reason for this is that DivByZeroDefect inherits from Defect and with --panics:on Defects become unrecoverable errors. (Since version 1.4 of the language.)

Rules 1-2 of the exception tracking inference rules (see the previous section) ensure the following works:

proc weDontRaiseButMaybeTheCallback(callback: proc()) {.raises: [], effectsOf: callback.} = callback() proc doRaise() {.raises: [IOError].} = raise newException(IOError, "IO") proc use() {.raises: [].} = weDontRaiseButMaybeTheCallback(doRaise)

As can be seen from the example, a parameter of type proc (...) can be annotated as .effectsOf. Such a parameter allows for effect polymorphism: The proc weDontRaiseButMaybeTheCallback raises the exceptions that callback raises.

So in many cases a callback does not cause the compiler to be overly conservative in its effect analysis:

{.push warningAsError[Effect]: on.} import std/algorithm type MyInt = distinct int var toSort = @[MyInt 1, MyInt 2, MyInt 3] proc cmpN(a, b: MyInt): int = cmp(a.int, b.int) proc harmless {.raises: [].} = toSort.sort cmpN proc cmpE(a, b: MyInt): int {.raises: [Exception].} = cmp(a.int, b.int) proc harmful {.raises: [].} = toSort.sort cmpE

Exception tracking is part of Nim's effect system. Raising an exception is an *effect*. Other effects can also be defined. A user defined effect is a means to *tag* a routine and to perform checks against this tag:

type IO = object proc readLine(): string {.tags: [IO].} = discard proc no_effects_please() {.tags: [].} = let x = readLine()

A tag has to be a type name. A tags list - like a raises list - can also be attached to a proc type. This affects type compatibility.

The inference for tag tracking is analogous to the inference for exception tracking.

There is also a way which can be used to forbid certain effects:

type IO = object proc readLine(): string {.tags: [IO].} = discard proc echoLine(): void = discard proc no_IO_please() {.forbids: [IO].} = echoLine() let y = readLine()

The forbids pragma defines a list of illegal effects - if any statement invokes any of those effects, the compilation will fail. Procedure types with any disallowed effect are the subtypes of equal procedure types without such lists:

type MyEffect = object type ProcType1 = proc (i: int): void {.forbids: [MyEffect].} type ProcType2 = proc (i: int): void proc caller1(p: ProcType1): void = p(1) proc caller2(p: ProcType2): void = p(1) proc effectful(i: int): void {.tags: [MyEffect].} = echo $i proc effectless(i: int): void {.forbids: [MyEffect].} = echo $i proc toBeCalled1(i: int): void = effectful(i) proc toBeCalled2(i: int): void = effectless(i) caller1(toBeCalled1) caller1(toBeCalled2) caller2(toBeCalled1) caller2(toBeCalled2)

ProcType2 is a subtype of ProcType1. Unlike with the tags pragma, the parent context - the function which calls other functions with forbidden effects - doesn't inherit the forbidden list of effects.

The noSideEffect pragma is used to mark a proc/iterator that can have only side effects through parameters. This means that the proc/iterator only changes locations that are reachable from its parameters and the return value only depends on the parameters. If none of its parameters have the type var, ref, ptr, cstring, or proc, then no locations are modified.

In other words, a routine has no side effects if it does not access a threadlocal or global variable and it does not call any routine that has a side effect.

It is a static error to mark a proc/iterator to have no side effect if the compiler cannot verify this.

As a special semantic rule, the built-in debugEcho pretends to be free of side effects so that it can be used for debugging routines marked as noSideEffect.

func is syntactic sugar for a proc with no side effects:

func `+` (x, y: int): int

To override the compiler's side effect analysis a {.noSideEffect.} cast pragma block can be used:

func f() = {.cast(noSideEffect).}: echo "test"

**Side effects are usually inferred. The inference for side effects is analogous to the inference for exception tracking.**

When the compiler cannot infer side effects, as is the case for imported functions, one can annotate them with the sideEffect pragma.

We call a proc p GC safe when it doesn't access any global variable that contains GC'ed memory (string, seq, ref or a closure) either directly or indirectly through a call to a GC unsafe proc.

**The GC safety property is usually inferred. The inference for GC safety is analogous to the inference for exception tracking.**

The gcsafe annotation can be used to mark a proc to be gcsafe, otherwise this property is inferred by the compiler. Note that noSideEffect implies gcsafe.

Routines that are imported from C are always assumed to be gcsafe.

To override the compiler's gcsafety analysis a {.cast(gcsafe).} pragma block can be used:

var someGlobal: string = "some string here" perThread {.threadvar.}: string proc setPerThread() = {.cast(gcsafe).}: deepCopy(perThread, someGlobal)

See also:

- Shared heap memory management.

The effects pragma has been designed to assist the programmer with the effects analysis. It is a statement that makes the compiler output all inferred effects up to the effects's position:

proc p(what: bool) = if what: raise newException(IOError, "IO") {.effects.} else: raise newException(OSError, "OS")

The compiler produces a hint message that IOError can be raised. OSError is not listed as it cannot be raised in the branch the effects pragma appears in.

Generics are Nim's means to parametrize procs, iterators or types with type parameters. Depending on the context, the brackets are used either to introduce type parameters or to instantiate a generic proc, iterator, or type.

The following example shows how a generic binary tree can be modeled:

type BinaryTree*[T] = ref object le, ri: BinaryTree[T] data: T proc newNode*[T](data: T): BinaryTree[T] = result = BinaryTree[T](le: nil, ri: nil, data: data) proc add*[T](root: var BinaryTree[T], n: BinaryTree[T]) = if root == nil: root = n else: var it = root while it != nil: var c = cmp(it.data, n.data) if c < 0: if it.le == nil: it.le = n return it = it.le else: if it.ri == nil: it.ri = n return it = it.ri proc add*[T](root: var BinaryTree[T], data: T) = add(root, newNode(data)) iterator preorder*[T](root: BinaryTree[T]): T = var stack: seq[BinaryTree[T]] = @[root] while stack.len > 0: var n = stack.pop() while n != nil: yield n.data add(stack, n.ri) n = n.le var root: BinaryTree[string] add(root, newNode("hello")) add(root, "world") for str in preorder(root): stdout.writeLine(str)

The T is called a generic type parameter or a type variable.

Let's consider the anatomy of a generic proc to agree on defined terminology.

p[T: t](arg1: f): y

- p: Callee symbol
- [...]: Generic parameters
- T: t: Generic constraint
- T: Type variable
- [T: t](arg1: f): y: Formal signature
- arg1: f: Formal parameter
- f: Formal parameter type
- y: Formal return type

The use of the word "formal" here is to denote the symbols as they are defined by the programmer, not as they may be at compile time contextually. Since generics may be instantiated and types bound, we have more than one entity to think about when generics are involved.

The usage of a generic will resolve the formally defined expression into an instance of that expression bound to only concrete types. This process is called "instantiation".

Brackets at the site of a generic's formal definition specify the "constraints" as in:

type Foo[T] = object proc p[H;T: Foo[H]](param: T): H

A constraint definition may have more than one symbol defined by separating each definition by a ;. Notice how T is composed of H and the return type of p is defined as H. When this generic proc is instantiated H will be bound to a concrete type, thus making T concrete and the return type of p will be bound to the same concrete type used to define H.

Brackets at the site of usage can be used to supply concrete types to instantiate the generic in the same order that the symbols are defined in the constraint. Alternatively, type bindings may be inferred by the compiler in some situations, allowing for cleaner code.

The is operator is evaluated during semantic analysis to check for type equivalence. It is therefore very useful for type specialization within generic code:

type Table[Key, Value] = object keys: seq[Key] values: seq[Value] when not (Key is string): deletedKeys: seq[bool]

A type class is a special pseudo-type that can be used to match against types in the context of overload resolution or the is operator. Nim supports the following built-in type classes:

| type class | matches |
|---|---|
| object | any object type |
| tuple | any tuple type |
| enum | any enumeration |
| proc | any proc type |
| iterator | any iterator type |
| ref | any ref type |
| ptr | any ptr type |
| var | any var type |
| distinct | any distinct type |
| array | any array type |
| set | any set type |
| seq | any seq type |
| auto | any type |

Furthermore, every generic type automatically creates a type class of the same name that will match any instantiation of the generic type.

Type classes can be combined using the standard boolean operators to form more complex type classes:

type RecordType = (tuple or object) proc printFields[T: RecordType](rec: T) = for key, value in fieldPairs(rec): echo key, " = ", value

Type constraints on generic parameters can be grouped with , and propagation stops with ;, similarly to parameters for macros and templates:

proc fn1[T; U, V: SomeFloat]() = discard template fn2(t; u, v: SomeFloat) = discard

Whilst the syntax of type classes appears to resemble that of ADTs/algebraic data types in ML-like languages, it should be understood that type classes are static constraints to be enforced at type instantiations. Type classes are not really types in themselves but are instead a system of providing generic "checks" that ultimately *resolve* to some singular type. Type classes do not allow for runtime type dynamism, unlike object variants or methods.

As an example, the following would not compile:

type TypeClass = int | string var foo: TypeClass = 2 foo = "this will fail"

Nim allows for type classes and regular types to be specified as type constraints of the generic type parameter:

proc onlyIntOrString[T: int|string](x, y: T) = discard onlyIntOrString(450, 616) onlyIntOrString(5.0, 0.0) onlyIntOrString("xy", 50)

proc and iterator type classes also accept a calling convention pragma to restrict the calling convention of the matching proc or iterator type.

proc onlyClosure[T: proc {.closure.}](x: T) = discard onlyClosure(proc() = echo "hello") proc foo() {.nimcall.} = discard onlyClosure(foo)

A type class can be used directly as the parameter's type.

type RecordType = (tuple or object) proc printFields(rec: RecordType) = for key, value in fieldPairs(rec): echo key, " = ", value

Procedures utilizing type classes in such a manner are considered to be implicitly generic. They will be instantiated once for each unique combination of parameter types used within the program.

By default, during overload resolution, each named type class will bind to exactly one concrete type. We call such type classes bind once types. Here is an example taken directly from the system module to illustrate this:

proc `==`*(x, y: tuple): bool = result = true for a, b in fields(x, y): if a != b: result = false

Alternatively, the distinct type modifier can be applied to the type class to allow each parameter matching the type class to bind to a different type. Such type classes are called bind many types.

Procs written with the implicitly generic style will often need to refer to the type parameters of the matched generic type. They can be easily accessed using the dot syntax:

type Matrix[T, Rows, Columns] = object ... proc `[]`(m: Matrix, row, col: int): Matrix.T = m.data[col * high(Matrix.Columns) + row]

Here are more examples that illustrate implicit generics:

proc p(t: Table; k: Table.Key): Table.Value proc p[Key, Value](t: Table[Key, Value]; k: Key): Value

proc p(a: Table, b: Table) proc p[Key, Value](a, b: Table[Key, Value])

proc p(a: Table, b: distinct Table) proc p[Key, Value, KeyB, ValueB](a: Table[Key, Value], b: Table[KeyB, ValueB])

typedesc used as a parameter type also introduces an implicit generic. typedesc has its own set of rules:

proc p(a: typedesc) proc p[T](a: typedesc[T])

typedesc is a "bind many" type class:

proc p(a, b: typedesc) proc p[T, T2](a: typedesc[T], b: typedesc[T2])

A parameter of type typedesc is itself usable as a type. If it is used as a type, it's the underlying type. In other words, one level of "typedesc"-ness is stripped off:

proc p(a: typedesc; b: a) = discard proc p[T](a: typedesc[T]; b: T) = discard p(int, 4)

The types var T and typedesc[T] cannot be inferred in a generic instantiation. The following is not allowed:

proc g[T](f: proc(x: T); x: T) = f(x) proc c(y: int) = echo y proc v(y: var int) = y += 100 var i: int g(c, 42) g(v, i) g[var int](v, i)

The symbol binding rules in generics are slightly subtle: There are "open" and "closed" symbols. A "closed" symbol cannot be re-bound in the instantiation context, an "open" symbol can. Per default, overloaded symbols are open and every other symbol is closed.

Open symbols are looked up in two different contexts: Both the context at definition and the context at instantiation are considered:

type Index = distinct int proc `==` (a, b: Index): bool {.borrow.} var a = (0, 0.Index) var b = (0, 0.Index) echo a == b

In the example, the generic `==` for tuples (as defined in the system module) uses the == operators of the tuple's components. However, the == for the Index type is defined *after* the == for tuples; yet the example compiles as the instantiation takes the currently defined symbols into account too.

A symbol can be forced to be open by a mixin declaration:

proc create*[T](): ref T = mixin init new result init result

mixin statements only make sense in templates and generics.

The bind statement is the counterpart to the mixin statement. It can be used to explicitly declare identifiers that should be bound early (i.e. the identifiers should be looked up in the scope of the template/generic definition):

var lastId = 0 template genId*: untyped = bind lastId inc(lastId) lastId

import A echo genId()

But a bind is rarely useful because symbol binding from the definition scope is the default.

bind statements only make sense in templates and generics.

The following example outlines a problem that can arise when generic instantiations cross multiple different modules:

proc genericA*[T](x: T) = mixin init init(x)

import C proc genericB*[T](x: T) = bind init genericA(x)

type O = object proc init*(x: var O) = discard

import B, C genericB O()

In module B has an init proc from module C in its scope that is not taken into account when genericB is instantiated which leads to the instantiation of genericA. The solution is to forward these symbols by a bind statement inside genericB.

A template is a simple form of a macro: It is a simple substitution mechanism that operates on Nim's abstract syntax trees. It is processed in the semantic pass of the compiler.

The syntax to *invoke* a template is the same as calling a procedure.

Example:

template `!=` (a, b: untyped): untyped = not (a == b) assert(5 != 6)

The !=, >, >=, in, notin, isnot operators are in fact templates:

a > b is transformed into b < a. a in b is transformed into contains(b, a). notin and isnot have the obvious meanings.

The "types" of templates can be the symbols untyped, typed or typedesc. These are "meta types", they can only be used in certain contexts. Regular types can be used too; this implies that typed expressions are expected.

An untyped parameter means that symbol lookups and type resolution is not performed before the expression is passed to the template. This means that *undeclared* identifiers, for example, can be passed to the template:

template declareInt(x: untyped) = var x: int declareInt(x) x = 3

template declareInt(x: typed) = var x: int declareInt(x)

A template where every parameter is untyped is called an immediate template. For historical reasons, templates can be explicitly annotated with an immediate pragma and then these templates do not take part in overloading resolution and the parameters' types are *ignored* by the compiler. Explicit immediate templates are now deprecated.

**Note**: For historical reasons, stmt was an alias for typed and expr was an alias for untyped, but they are removed.

One can pass a block of statements as the last argument to a template following the special : syntax:

template withFile(f, fn, mode, actions: untyped): untyped = var f: File if open(f, fn, mode): try: actions finally: close(f) else: quit("cannot open: " & fn) withFile(txt, "ttempl3.txt", fmWrite): txt.writeLine("line 1") txt.writeLine("line 2")

In the example, the two writeLine statements are bound to the actions parameter.

Usually, to pass a block of code to a template, the parameter that accepts the block needs to be of type untyped. Because symbol lookups are then delayed until template instantiation time:

template t(body: typed) = proc p = echo "hey" block: body t: p()

The above code fails with the error message that p is not declared. The reason for this is that the p() body is type-checked before getting passed to the body parameter and type checking in Nim implies symbol lookups. The same code works with untyped as the passed body is not required to be type-checked:

template t(body: untyped) = proc p = echo "hey" block: body t: p()

In addition to the untyped meta-type that prevents type checking, there is also varargs[untyped] so that not even the number of parameters is fixed:

template hideIdentifiers(x: varargs[untyped]) = discard hideIdentifiers(undeclared1, undeclared2)

However, since a template cannot iterate over varargs, this feature is generally much more useful for macros.

A template is a hygienic macro and so opens a new scope. Most symbols are bound from the definition scope of the template:

var lastId = 0 template genId*: untyped = inc(lastId) lastId

import A echo genId()

As in generics, symbol binding can be influenced via mixin or bind statements.

In templates, identifiers can be constructed with the backticks notation:

template typedef(name: untyped, typ: typedesc) = type `T name`* {.inject.} = typ `P name`* {.inject.} = ref `T name` typedef(myint, int) var x: PMyInt

In the example, name is instantiated with myint, so `T name` becomes Tmyint.

A parameter p in a template is even substituted in the expression x.p. Thus, template arguments can be used as field names and a global symbol can be shadowed by the same argument name even when fully qualified:

type Lev = enum levA, levB var abclev = levB template tstLev(abclev: Lev) = echo abclev, " ", m.abclev tstLev(levA)

But the global symbol can properly be captured by a bind statement:

type Lev = enum levA, levB var abclev = levB template tstLev(abclev: Lev) = bind m.abclev echo abclev, " ", m.abclev tstLev(levA)

Per default, templates are hygienic: Local identifiers declared in a template cannot be accessed in the instantiation context:

template newException*(exceptn: typedesc, message: string): untyped = var e: ref exceptn new(e) e.msg = message e let e = "message" raise newException(IoError, e)

Whether a symbol that is declared in a template is exposed to the instantiation scope is controlled by the inject and gensym pragmas: gensym'ed symbols are not exposed but inject'ed symbols are.

The default for symbols of entity type, var, let and const is gensym. For proc, iterator, converter, template, macro, the default is inject, but if a gensym symbol with the same name is defined in the same syntax-level scope, it will be gensym by default. This can be overridden by marking the routine as inject.

If the name of the entity is passed as a template parameter, it is an inject'ed symbol:

template withFile(f, fn, mode: untyped, actions: untyped): untyped = block: var f: File ... withFile(txt, "ttempl3.txt", fmWrite): txt.writeLine("line 1") txt.writeLine("line 2")

The inject and gensym pragmas are second class annotations; they have no semantics outside a template definition and cannot be abstracted over:

{.pragma myInject: inject.} template t() = var x {.myInject.}: int

To get rid of hygiene in templates, one can use the dirty pragma for a template. inject and gensym have no effect in dirty templates.

gensym'ed symbols cannot be used as field in the x.field syntax. Nor can they be used in the ObjectConstruction(field: value) and namedParameterCall(field = value) syntactic constructs.

The reason for this is that code like

type T = object f: int template tmp(x: T) = let f = 34 echo x.f, T(f: 4)

should work as expected.

However, this means that the method call syntax is not available for gensym'ed symbols:

template tmp(x) = type T {.gensym.} = int echo x.T tmp(12)

The expression x in x.f needs to be semantically checked (that means symbol lookup and type checking) before it can be decided that it needs to be rewritten to f(x). Therefore, the dot syntax has some limitations when it is used to invoke templates/macros:

template declareVar(name: untyped) = const name {.inject.} = 45 unknownIdentifier.declareVar

It is also not possible to use fully qualified identifiers with module symbol in method call syntax. The order in which the dot operator binds to symbols prohibits this.

import std/sequtils var myItems = @[1,3,3,7] let N1 = count(myItems, 3) let N2 = sequtils.count(myItems, 3) let N3 = myItems.count(3) let N4 = myItems.sequtils.count(3)

This means that when for some reason a procedure needs a disambiguation through the module name, the call needs to be written in function call syntax.

A macro is a special function that is executed at compile time. Normally, the input for a macro is an abstract syntax tree (AST) of the code that is passed to it. The macro can then do transformations on it and return the transformed AST. This can be used to add custom language features and implement domain-specific languages.

Macro invocation is a case where semantic analysis does **not** entirely proceed top to bottom and left to right. Instead, semantic analysis happens at least twice:

- Semantic analysis recognizes and resolves the macro invocation.
- The compiler executes the macro body (which may invoke other procs).
- It replaces the AST of the macro invocation with the AST returned by the macro.
- It repeats semantic analysis of that region of the code.
- If the AST returned by the macro contains other macro invocations, this process iterates.

While macros enable advanced compile-time code transformations, they cannot change Nim's syntax.

**Style note:** For code readability, it is best to use the least powerful programming construct that remains expressive. So the "check list" is:

1. Use an ordinary proc/iterator, if possible.
2. Else: Use a generic proc/iterator, if possible.
3. Else: Use a template, if possible.
4. Else: Use a macro.

The following example implements a powerful debug command that accepts a variable number of arguments:

import std/macros macro debug(args: varargs[untyped]): untyped = result = nnkStmtList.newTree() for n in args: result.add newCall("write", newIdentNode("stdout"), newLit(n.repr)) result.add newCall("write", newIdentNode("stdout"), newLit(": ")) result.add newCall("writeLine", newIdentNode("stdout"), n) var a: array[0..10, int] x = "some string" a[0] = 42 a[1] = 45 debug(a[0], a[1], x)

The macro call expands to:

write(stdout, "a[0]") write(stdout, ": ") writeLine(stdout, a[0]) write(stdout, "a[1]") write(stdout, ": ") writeLine(stdout, a[1]) write(stdout, "x") write(stdout, ": ") writeLine(stdout, x)

Arguments that are passed to a varargs parameter are wrapped in an array constructor expression. This is why debug iterates over all of args's children.

The above debug macro relies on the fact that write, writeLine and stdout are declared in the system module and are thus visible in the instantiating context. There is a way to use bound identifiers (aka symbols) instead of using unbound identifiers. The bindSym builtin can be used for that:

import std/macros macro debug(n: varargs[typed]): untyped = result = newNimNode(nnkStmtList, n) for x in n: add(result, newCall(bindSym"write", bindSym"stdout", toStrLit(x))) add(result, newCall(bindSym"write", bindSym"stdout", newStrLitNode(": "))) add(result, newCall(bindSym"writeLine", bindSym"stdout", x)) var a: array[0..10, int] x = "some string" a[0] = 42 a[1] = 45 debug(a[0], a[1], x)

The macro call expands to:

write(stdout, "a[0]") write(stdout, ": ") writeLine(stdout, a[0]) write(stdout, "a[1]") write(stdout, ": ") writeLine(stdout, a[1]) write(stdout, "x") write(stdout, ": ") writeLine(stdout, x)

In this version of debug, the symbols write, writeLine and stdout are already bound and are not looked up again. As the example shows, bindSym does work with overloaded symbols implicitly.

Note that the symbol names passed to bindSym have to be constant. The experimental feature dynamicBindSym (experimental manual) allows this value to be computed dynamically.

Macros can receive of, elif, else, except, finally and do blocks (including their different forms such as do with routine parameters) as arguments if called in statement form.

macro performWithUndo(task, undo: untyped) = ... performWithUndo do: do: let num = 12 match (num mod 3, num mod 5): of (0, 0): echo "FizzBuzz" of (0, _): echo "Fizz" of (_, 0): echo "Buzz" else: echo num

A macro that takes as its only input parameter an expression of the special type system.ForLoopStmt can rewrite the entirety of a for loop:

import std/macros macro example(loop: ForLoopStmt) = result = newTree(nnkForStmt) result.add loop[^3] result.add loop[^2][^1] result.add newCall(bindSym"echo", loop[0]) for item in example([1, 2, 3]): discard

Expands to:

for item in items([1, 2, 3]): echo item

Another example:

import std/macros macro enumerate(x: ForLoopStmt): untyped = expectKind x, nnkForStmt var countStart = if x[^2].len == 2: newLit(0) else: x[^2][1] result = newStmtList() result.add newVarStmt(x[0], countStart) var body = x[^1] if body.kind != nnkStmtList: body = newTree(nnkStmtList, body) body.add newCall(bindSym"inc", x[0]) var newFor = newTree(nnkForStmt) for i in 1..x.len-3: newFor.add x[i] newFor.add x[^2][^1] newFor.add body result.add newFor result = quote do: block: `result` for a, b in enumerate(items([1, 2, 3])): echo a, " ", b for a, b in enumerate(10, [1, 2, 3, 5]): echo a, " ", b

Macros named `` case `` can provide implementations of case statements for certain types. The following is an example of such an implementation for tuples, leveraging the existing equality operator for tuples (as provided in system.==):

import std/macros macro `case`(n: tuple): untyped = result = newTree(nnkIfStmt) let selector = n[0] for i in 1 ..< n.len: let it = n[i] case it.kind of nnkElse, nnkElifBranch, nnkElifExpr, nnkElseExpr: result.add it of nnkOfBranch: for j in 0..it.len-2: let cond = newCall("==", selector, it[j]) result.add newTree(nnkElifBranch, cond, it[^1]) else: error "custom 'case' for tuple cannot handle this node", it case ("foo", 78) of ("foo", 78): echo "yes" of ("bar", 88): echo "no" else: discard

case macros are subject to overload resolution. The type of the case statement's selector expression is matched against the type of the first argument of the case macro. Then the complete case statement is passed in place of the argument and the macro is evaluated.

In other words, the macro needs to transform the full case statement but only the statement's selector expression is used to determine which macro to call.

As their name suggests, static parameters must be constant expressions:

proc precompiledRegex(pattern: static string): RegEx = var res {.global.} = re(pattern) return res precompiledRegex("/d+") precompiledRegex(paramStr(1))

For the purposes of code generation, all static parameters are treated as generic parameters - the proc will be compiled separately for each unique supplied value (or combination of values).

Static parameters can also appear in the signatures of generic types:

type Matrix[M,N: static int; T: Number] = array[0..(M*N - 1), T] AffineTransform2D[T] = Matrix[3, 3, T] AffineTransform3D[T] = Matrix[4, 4, T] var m1: AffineTransform3D[float] var m2: AffineTransform2D[string]

Please note that static T is just a syntactic convenience for the underlying generic type static[T]. The type parameter can be omitted to obtain the type class of all constant expressions. A more specific type class can be created by instantiating static with another type class.

One can force an expression to be evaluated at compile time as a constant expression by coercing it to a corresponding static type:

import std/math echo static(fac(5)), " ", static[bool](16.isPowerOfTwo)

The compiler will report any failure to evaluate the expression or a possible type mismatch error.

In many contexts, Nim treats the names of types as regular values. These values exist only during the compilation phase, but since all values must have a type, typedesc is considered their special type.

typedesc acts as a generic type. For instance, the type of the symbol int is typedesc[int]. Just like with regular generic types, when the generic parameter is omitted, typedesc denotes the type class of all types. As a syntactic convenience, one can also use typedesc as a modifier.

Procs featuring typedesc parameters are considered implicitly generic. They will be instantiated for each unique combination of supplied types, and within the body of the proc, the name of each parameter will refer to the bound concrete type:

proc new(T: typedesc): ref T = echo "allocating ", T.name new(result) var n = Node.new var tree = new(BinaryTree[int])

When multiple type parameters are present, they will bind freely to different types. To force a bind-once behavior, one can use an explicit generic parameter:

proc acceptOnlyTypePairs[T, U](A, B: typedesc[T]; C, D: typedesc[U])

Once bound, type parameters can appear in the rest of the proc signature:

template declareVariableWithType(T: typedesc, value: T) = var x: T = value declareVariableWithType int, 42

Overload resolution can be further influenced by constraining the set of types that will match the type parameter. This works in practice by attaching attributes to types via templates. The constraint can be a concrete type or a type class.

template maxval(T: typedesc[int]): int = high(int) template maxval(T: typedesc[float]): float = Inf var i = int.maxval var f = float.maxval when false: var s = string.maxval template isNumber(t: typedesc[object]): string = "Don't think so." template isNumber(t: typedesc[SomeInteger]): string = "Yes!" template isNumber(t: typedesc[SomeFloat]): string = "Maybe, could be NaN." echo "is int a number? ", isNumber(int) echo "is float a number? ", isNumber(float) echo "is RootObj a number? ", isNumber(RootObj)

Passing typedesc is almost identical, just with the difference that the macro is not instantiated generically. The type expression is simply passed as a NimNode to the macro, like everything else.

import std/macros macro forwardType(arg: typedesc): typedesc = let tmp: NimNode = arg result = tmp var tmp: forwardType(int)

**Note**: typeof(x) can for historical reasons also be written as type(x) but type(x) is discouraged.

One can obtain the type of a given expression by constructing a typeof value from it (in many other languages this is known as the typeof operator):

var x = 0 var y: typeof(x)

If typeof is used to determine the result type of a proc/iterator/converter call c(X) (where X stands for a possibly empty list of arguments), the interpretation, where c is an iterator, is preferred over the other interpretations, but this behavior can be changed by passing typeOfProc as the second argument to typeof:

iterator split(s: string): string = discard proc split(s: string): seq[string] = discard assert typeof("a b c".split) is string assert typeof("a b c".split, typeOfProc) is seq[string]

Nim supports splitting a program into pieces by a module concept. Each module needs to be in its own file and has its own namespace. Modules enable information hiding and separate compilation. A module may gain access to the symbols of another module by the import statement. Recursive module dependencies are allowed, but are slightly subtle. Only top-level symbols that are marked with an asterisk (*) are exported. A valid module name can only be a valid Nim identifier (and thus its filename is identifier.nim).

The algorithm for compiling modules is:

- Compile the whole module as usual, following import statements recursively.
- If there is a cycle, only import the already parsed symbols (that are exported); if an unknown identifier occurs then abort.

This is best illustrated by an example:

type T1* = int import B proc main() = var i = p(3) main()

import A proc p*(x: A.T1): A.T1 = result = x + 1

After the import keyword, a list of module names can follow or a single module name followed by an except list to prevent some symbols from being imported:

import std/strutils except `%`, toUpperAscii echo "$1" % "abc".toUpperAscii

It is not checked that the except list is really exported from the module. This feature allows us to compile against different versions of the module, even when one version does not export some of these identifiers.

The import statement is only allowed at the top level.

String literals can be used for import/include statements. The compiler performs path substitution when used.

The include statement does something fundamentally different than importing a module: it merely includes the contents of a file. The include statement is useful to split up a large module into several files:

include fileA, fileB, fileC

The include statement can be used outside the top level, as such:

echo "Hello World!"

proc main() = include A main()

A module alias can be introduced via the as keyword, after which the original module name is inaccessible:

import std/strutils as su, std/sequtils as qu echo su.format("$1", "lalelu")

The notations path/to/module or "path/to/module" can be used to refer to a module in subdirectories:

import lib/pure/os, "lib/pure/times"

Note that the module name is still strutils and not lib/pure/strutils, thus one **cannot** do:

import lib/pure/strutils echo lib/pure/strutils.toUpperAscii("abc")

Likewise, the following does not make sense as the name is strutils already:

import lib/pure/strutils as strutils

The syntax import dir / [moduleA, moduleB] can be used to import multiple modules from the same directory.
