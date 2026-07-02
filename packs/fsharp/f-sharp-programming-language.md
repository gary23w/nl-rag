---
title: "F Sharp (programming language)"
source: https://en.wikipedia.org/wiki/F_Sharp_(programming_language)
domain: fsharp
license: CC-BY-SA-4.0
tags: f sharp, fsharp language, dotnet fsharp, fsharp lang
fetched: 2026-07-02
---

# F Sharp (programming language)

**F#** (pronounced **F sharp**) is a general-purpose, high-level, strongly typed, multi-paradigm programming language that encompasses functional, imperative, and object-oriented programming methods. It is most often used as a cross-platform Common Language Infrastructure (CLI) language on .NET, but can also generate JavaScript and graphics processing unit (GPU) code.

F# is developed by the F# Software Foundation, Microsoft and open contributors. An open source, cross-platform compiler for F# is available from the F# Software Foundation. F# is a fully supported language in Visual Studio and JetBrains Rider. Plug-ins supporting F# exist for many widely used editors including Visual Studio Code, Vim, and Emacs.

F# is a member of the ML language family and originated as a .NET Framework implementation of a core of the programming language OCaml. It has also been influenced by C#, Python, Haskell, Scala and Erlang.

## History

### Versions

| F# version | Language specification | Date | Platforms | Runtime |
|---|---|---|---|---|
| 1.x |   | May 2005 | Windows | .NET 1.0 - 3.5 |
| 2.0 | August 2010 | April 2010 | Linux, macOS, Windows | .NET 2.0 - 4.0, Mono |
| 3.0 | November 2012 | August 2012 | Linux, macOS, Windows; JavaScript, GPU | .NET 2.0 - 4.5, Mono |
| 3.1 | November 2013 | October 2013 | Linux, macOS, Windows; JavaScript, GPU | .NET 2.0 - 4.5, Mono |
| 4.0 | January 2016 | July 2015 |   |   |
| 4.1 | May 2018 | March 2017 | Linux, macOS, Windows, JavaScript, GPU | .NET 3.5 - 4.6.2, .NET, Mono |
| 4.5 |   | August 2018 | Linux, macOS, Windows, JavaScript, GPU | .NET 4.5 - 4.7.2, .NET Core SDK 2.1.400 |
| 4.6 |   | March 2019 | Linux, macOS, Windows, JavaScript, GPU | .NET 4.5 - 4.7.2, .NET Core SDK 2.2.300 |
| 4.7 |   | September 2019 | Linux, macOS, Windows, JavaScript, GPU | .NET 4.5 - 4.8, .NET Core SDK 3.0.100 |
| 5.0 |   | November 2020 | Linux, macOS, Windows, JavaScript, GPU | .NET SDK 5.0.100 |
| 6.0 |   | November 2021 | Linux, macOS, Windows, JavaScript, GPU | .NET SDK 6.0.100 |
| 7.0 |   | November 2022 | Linux, macOS, Windows, JavaScript, GPU | .NET SDK 7.0.100 |
| 8.0 |   | November 2023 | Linux, macOS, Windows, JavaScript, GPU | .NET SDK 8.0.100 |
| 9.0 |   | November 2024 | Linux, macOS, Windows, JavaScript, GPU | .NET SDK 9.0.0 |
| 10.0 |   | November 2025 | Linux, macOS, Windows, JavaScript, GPU | .NET SDK 10.0.0 |

### Language evolution

F# uses an open development and engineering process. The language evolution process is managed by Don Syme from Microsoft Research as the benevolent dictator for life (BDFL) for the language design, together with the F# Software Foundation. Earlier versions of the F# language were designed by Microsoft and Microsoft Research using a closed development process.

F# was first included in Visual Studio in the 2010 edition, at the same level as Visual Basic (.NET) and C# (albeit as an option), and remains in all later editions, thus making the language widely available and well-supported.

F# originates from Microsoft Research, Cambridge, UK. The language was originally designed and implemented by Don Syme, according to whom in the fsharp team, they say the F is for "Fun". Andrew Kennedy contributed to the design of units of measure. The Visual F# Tools for Visual Studio are developed by Microsoft. The F# Software Foundation developed the F# open-source compiler and tools, incorporating the open-source compiler implementation provided by the Microsoft Visual F# Tools team.

| F# version | Features added |
|---|---|
| 1.0 | Functional programming Discriminated unions Records Tuples Pattern matching Type abbreviations Object-oriented programming Structs Signature files Scripting files Imperative programming Modules (no functors) Nested modules .NET interoperability |
| 2.0 | Active patterns Units of measure Sequence expressions Asynchronous programming Agent programming Extension members Named arguments Optional arguments Array slicing Quotations Native interoperability Computation expressions |
| 3.0 | Type providers LINQ query expressions CLIMutable attribute Triple-quoted strings Auto-properties Provided units-of-measure |
| 3.1 | Named union type fields Extensions to array slicing Type inference enhancements |
| 4.0 | Printf on unitized values Extension property initializers Non-null provided types Primary constructors as functions Static parameters for provided methods Printf interpolation Extended #if grammar Tailcall attribute Multiple interface instantiations Optional type args Params dictionaries |
| 4.1 | Struct tuples which inter-operate with C# tuples Struct annotations for Records Struct annotations for Single-case Discriminated Unions Underscores in numeric literals Caller info argument attributes Result type and some basic Result functions Mutually referential types and modules within the same file Implicit "Module" syntax on modules with shared name as type Byref returns, supporting consuming C# ref-returning methods Error message improvements Support for 'fixed' |
| 4.5 | Versioning alignment of binary, package, and language Support for 'Span<T>' and related types Ability to produce 'byref' returns The 'voidptr' type The 'inref<'T>' and 'outref<'T>' types to represent readonly and write-only 'byref's 'IsByRefLike' structs 'IsReadOnly' structs Extension method support for 'byref<'T>'/'inref<'T>'/'outref<'T>' 'match!' keyword in computation expressions Relaxed upcast with 'yield' in F# seq/list/array expressions Relaxed indentation with list and array expressions Enumeration cases emitted as public |
| 4.6 | Anonymous record types |
| 4.7 | Implicit yields No more required double underscore Indentation relaxations for parameters passed to constructors and static methods 'nameof' function Open static classes |
| 5.0 | FSharp.Core now targets netstandard2.0 only Package references in F# scripts Support for Jupyter, nteract, and VSCode Notebooks String Interpolation Support for nameof Open Type declarations Enhanced Slicing F# quotations improvements Applicative Computation Expressions Improved stack traces in F# async and other computation expressions Improved .NET interop Improved Map and Set performance in FSharp.Core Improved compiler performance Improved compiler analysis for library authors |
| 6.0 | Tasks Simpler indexing Augments to "active patterns" Overloaded custom operations in computation expressions “as” patterns Indentation syntax revisions More implicit conversions More implicit upcast conversions Implicit integer conversions First-class support for .NET-style implicit conversions Optional warnings for implicit conversions Formatting for binary numbers Discards on use bindings InlineIfLambda optimizer directive Resumable code More collection functions Map has Keys and Values More intrinsics for NativePtr More numeric types with unit annotations Informational warnings for rarely used symbolic operators |
| 7.0 | Static abstract members support in interfaces Making working with SRTPs (statically resolved type parameters) easier Required properties checking Init scope and init-only properties Reference assemblies support F# self-contained deployments & Native AOT Added support for N-d arrays up to rank 32. Result module functions parity with Option. Fixes in resumable state machines codegen for the tasks builds. Better codegen for compiler-generated side-effect-free property getters ARM64 platform-specific compiler and ARM64 target support in F# compiler. Dependency manager #r caching support Parallel type-checking and project-checking support (experimental, can be enabled via VS setting, or by tooling authors) Miscellaneous bugfixes and improvements. |
| 8.0 | _.Property shorthand for (fun x -> x.Property) Nested record field copy and update while! (while bang) feature Extended string interpolation syntax Use and compose string literals for printf and related functions Arithmetic operators in literals Type constraint intersection syntax Extended fixed binding Easier [<Extension>] method definition Static members in interfaces Static let in discriminated unions, records, structs, and types without primary constructors try-with within seq{}, [], and [\|\|] collection expressions Recursive calls and yield! within exception handler Tail call attribute [<Struct>] unions can now have > 49 cases Strict indentation rules New diagnostics from the compiler Switches for compiler parallelization |
| 9.0 | Nullable reference types Discriminated union .Is* properties Partial active patterns can return bool instead of unit option Prefer extension methods to intrinsic properties when arguments are provided Empty-bodied computation expressions Hash directives are allowed to take non-string arguments Extended #help directive in fsi to show documentation in the REPL Allow #nowarn to support the FS prefix on error codes to disable warnings Warning about TailCall attribute on non-recursive functions or let-bound values Enforce attribute targets Updates to the standard library (FSharp.Core) Developer productivity improvements Performance improvements Improvements in tooling |
| 10.0 | Scoped warning suppression Access modifiers on auto property accessors ValueOption optional parameters Tail-call support in computation expressions Typed bindings in computation expressions without parentheses Allow _ in use! bindings Rejecting pseudo-nested modules in types Deprecation warning for omitted `seq` Attribute target enforcement Support for `and!` in task expressions Better trimming by default Parallel compilation in preview Type subsumption cache |

## Language overview

### Functional programming

F# is a strongly typed functional-first language with a large number of capabilities that are normally found only in functional programming languages, while supporting object-oriented features available in C#. Together, these features allow F# programs to be written in a completely functional style and also allow functional and object-oriented styles to be mixed.

Examples of functional features are:

- Everything is an expression
- Type inference (using Hindley–Milner type inference)
- Functions as first-class citizens
- Anonymous functions with capturing semantics (i.e., closures)
- Immutable variables and objects
- Lazy evaluation support
- Higher-order functions
- Nested functions
- Currying
- Pattern matching
- Algebraic data types
- Tuples
- List comprehension
- Monad pattern support (called *computation expressions*)
- Tail call optimisation

F# is an expression-based language using eager evaluation and also in some instances lazy evaluation. Every statement in F#, including `if` expressions, `try` expressions and loops, is a composable expression with a static type. Functions and expressions that do not return any value have a return type of `unit`. F# uses the `let` keyword for binding values to a name. For example:

```mw
let x = 3 + 4
```

binds the value `7` to the name `x`.

New types are defined using the `type` keyword. For functional programming, F# provides *tuple*, *record*, *discriminated union*, *list*, *option*, and *result* types. A *tuple* represents a set of *n* values, where *n* ≥ 0. The value *n* is called the arity of the tuple. A 3-tuple would be represented as `(A, B, C)`, where A, B, and C are values of possibly different types. A tuple can be used to store values only when the number of values is known at design-time and stays constant during execution.

A *record* is a type where the data members are named. Here is an example of record definition:

```mw
 type R = 
        { Name : string 
         Age : int }
```

Records can be created as `let r = { Name="AB"; Age=42 }`. The `with` keyword is used to create a copy of a record, as in `{ r with Name="CD" }`, which creates a new record by copying `r` and changing the value of the `Name` field (assuming the record created in the last example was named `r`).

A discriminated union type is a type-safe version of C unions. For example,

```mw
 type A = 
    | UnionCaseX of string
    | UnionCaseY of int
```

Values of the union type can correspond to either union case. The types of the values carried by each union case is included in the definition of each case.

The *list* type is an immutable linked list represented either using a `head::tail` notation (`::` is the cons operator) or a shorthand as `[item1; item2; item3]`. An empty list is written `[]`. The *option* type is a discriminated union type with choices `Some(x)` or `None`. F# types may be generic, implemented as generic .NET types.

F# supports lambda functions and closures. All functions in F# are first class values and are immutable. Functions can be curried. Being first-class values, functions can be passed as arguments to other functions. Like other functional programming languages, F# allows function composition using the `>>` and `<<` operators.

F# provides *sequence expressions* that define a sequence `seq { ... }`, list `[ ... ]` or array `[| ... |]` through code that generates values. For example,

```mw
 seq { for b in 0 .. 25 do
           if b < 15 then
               yield b*b }
```

forms a sequence of squares of numbers from 0 to 14 by filtering out numbers from the range of numbers from 0 to 25. Sequences are generators – values are generated on-demand (i.e., are lazily evaluated) – while lists and arrays are evaluated eagerly.

F# uses pattern matching to bind values to names. Pattern matching is also used when accessing discriminated unions – the union is value matched against pattern rules and a rule is selected when a match succeeds. F# also supports *active patterns* as a form of extensible pattern matching. It is used, for example, when multiple ways of matching on a type exist.

F# supports a general syntax for defining compositional computations called *computation expressions*. Sequence expressions, asynchronous computations and queries are particular kinds of computation expressions. Computation expressions are an implementation of the monad pattern.

### Imperative programming

F# support for imperative programming includes

- `for` loops
- `while` loops
- arrays, created with the `[| ... |]` syntax
- hash table, created with the `dict [ ... ]` syntax or `System.Collections.Generic.Dictionary<_,_>` type.

Values and record fields can also be labelled as `mutable`. For example:

```mw
// Define 'x' with initial value '1'
let mutable x = 1
// Change the value of 'x' to '3'
x <- 3
```

Also, F# supports access to all CLI types and objects such as those defined in the `System.Collections.Generic` namespace defining imperative data structures.

### Object-oriented programming

Like other Common Language Infrastructure (CLI) languages, F# can use CLI types through object-oriented programming. F# support for object-oriented programming in expressions includes:

- Dot-notation, e.g., `x.Name`
- Object expressions, e.g., `{ new obj() with member x.ToString() = "hello" }`
- Object construction, e.g., `new Form()`
- Type tests, e.g., `x :? string`
- Type coercions, e.g., `x :?> string`
- Named arguments, e.g., `x.Method(someArgument=1)`
- Named setters, e.g., `new Form(Text="Hello")`
- Optional arguments, e.g., `x.Method(OptionalArgument=1)`

Support for object-oriented programming in patterns includes

- Type tests, e.g., `:? string as s`
- Active patterns, which can be defined over object types

F# object type definitions can be class, struct, interface, enum, or delegate type definitions, corresponding to the definition forms found in C#. For example, here is a class with a constructor taking a name and age, and declaring two properties.

```mw
/// A simple object type definition
type Person(name : string, age : int) =
    member x.Name = name
    member x.Age = age
```

### Asynchronous programming

F# supports asynchronous programming through *asynchronous workflows*. An asynchronous workflow is defined as a sequence of commands inside an `async{ ... }`, as in

```mw
let asynctask = 
    async { let req = WebRequest.Create(url)
            let! response = req.GetResponseAsync()
            use stream = response.GetResponseStream()
            use streamreader = new System.IO.StreamReader(stream)
            return streamreader.ReadToEnd() }
```

The `let!` indicates that the expression on the right (getting the response) should be done asynchronously but the flow should only continue when the result is available. In other words, from the point of view of the code block, it is as if getting the response is a blocking call, whereas from the point of view of the system, the thread will not be blocked and may be used to process other flows until the result needed for this one becomes available.

The async block may be invoked using the `Async.RunSynchronously` function. Multiple async blocks can be executed in parallel using the `Async.Parallel` function that takes a list of `async` objects (in the example, `asynctask` is an async object) and creates another async object to run the tasks in the lists in parallel. The resultant object is invoked using `Async.RunSynchronously`.

Inversion of control in F# follows this pattern.

Since version 6.0, F# supports creating, consuming and returning .NET tasks directly.

```mw
    open System.Net.Http
    let fetchUrlAsync (url:string) = // string -> Task<string>
        task {
            use client = new HttpClient()
            let! response = client.GetAsync(url) 
            let! content = response.Content.ReadAsStringAsync()
            do! Task.Delay 500
            return content
        }

    // Usage
    let fetchPrint() =
        let task = task {
            let! data = fetchUrlAsync "https://example.com"
            printfn $"{data}"
        } 
        task.Wait()
```

### Parallel programming

Parallel programming is supported partly through the `Async.Parallel`, `Async.Start` and other operations that run asynchronous blocks in parallel.

Parallel programming is also supported through the `Array.Parallel` functional programming operators in the F# standard library, direct use of the `System.Threading.Tasks` task programming model, the direct use of .NET thread pool and .NET threads and through dynamic translation of F# code to alternative parallel execution engines such as GPU code.

### Units of measure

The F# type system supports units of measure checking for numbers: units of measure, such as meters or kilograms, can be assigned to floating point, unsigned integer and signed integer values. This allows the compiler to check that arithmetic involving these values is dimensionally consistent, helping to prevent common programming mistakes by ensuring that, for instance, lengths are not mistakenly added to times.

The units of measure feature integrates with F# type inference to require minimal type annotations in user code.

```mw
[<Measure>] type m                  // meter
[<Measure>] type s                  // second

let distance = 100.0<m>     // float<m>
let time = 5.0<s>           // float<s>
let speed = distance/time   // float<m/s>

[<Measure>] type kg                 // kilogram
[<Measure>] type N = (kg * m)/(s^2) // Newtons
[<Measure>] type Pa = N/(m^2)       // Pascals 

[<Measure>] type days 
let better_age = 3u<days>          // uint<days>
```

The F# static type checker provides this functionality at compile time, but units are erased from the compiled code. Consequently, it is not possible to determine a value's unit at runtime.

### Metaprogramming

F# allows some forms of syntax customizing via metaprogramming to support embedding custom domain-specific languages within the F# language, particularly through computation expressions.

F# includes a feature for run-time meta-programming called quotations. A quotation expression evaluates to an abstract syntax tree representation of the F# expressions. Similarly, definitions labelled with the `[<ReflectedDefinition>]` attribute can also be accessed in their quotation form. F# quotations are used for various purposes including to compile F# code into JavaScript and GPU code. Quotations represent their F# code expressions as data for use by other parts of the program while requiring it to be syntactically correct F# code.

### Information-rich programming

F# 3.0 introduced a form of compile-time meta-programming through statically extensible type generation called F# type providers. F# type providers allow the F# compiler and tools to be extended with components that provide type information to the compiler on-demand at compile time. F# type providers have been used to give strongly typed access to connected information sources in a scalable way, including to the Freebase knowledge graph.

In F# 3.0 the F# quotation and computation expression features are combined to implement LINQ queries. For example:

```mw
// Use the OData type provider to create types that can be used to access the Northwind database.
open Microsoft.FSharp.Data.TypeProviders

type Northwind = ODataService<"http://services.odata.org/Northwind/Northwind.svc">
let db = Northwind.GetDataContext()

// A query expression.
let query1 = query { for customer in db.Customers do
                     select customer }
```

The combination of type providers, queries and strongly typed functional programming is known as *information rich programming*.

### Agent programming

F# supports a variation of the actor programming model through the in-memory implementation of lightweight asynchronous agents. For example, the following code defines an agent and posts 2 messages:

```mw
    type Message =
        | Enqueue of string
        | Dequeue of AsyncReplyChannel<Option<string>>

    // Provides concurrent access to a list of strings
    let listManager = MailboxProcessor.Start(fun inbox ->
        let rec messageLoop list = async {
            let! msg = inbox.Receive()
            match msg with
                | Enqueue item ->
                    return! messageLoop (item :: list)

                | Dequeue replyChannel ->
                    match list with
                    | [] -> 
                        replyChannel.Reply None
                        return! messageLoop list
                    | head :: tail ->
                        replyChannel.Reply (Some head)
                        return! messageLoop tail
        }

        // Start the loop with an empty list
        messageLoop []
    )

    // Usage 
    async {
        // Enqueue some strings
        listManager.Post(Enqueue "Hello")
        listManager.Post(Enqueue "World")

        // Dequeue and process the strings
        let! str = listManager.PostAndAsyncReply(Dequeue)
        str |> Option.iter (printfn "Dequeued: %s")

    }
    |> Async.Start
```

## Development tools

- Visual Studio, with the Visual F# tools from Microsoft installed, can be used to create, run and debug F# projects. The Visual F# tools include a Visual Studio-hosted read–eval–print loop (REPL) interactive console that can execute F# code as it is written. Visual Studio for Mac also fully supports F# projects.
- Visual Studio Code contains full support for F# via the Ionide extension.
- F# can be developed with any text editor. Specific support exists in editors such as Emacs.
- JetBrains Rider is optimized for the development of F# Code starting with release 2019.1.
- LINQPad has supported F# since version 2.x.

### Comparison of integrated development environments

| IDE | License | Windows | Linux | macOS | Developer |
|---|---|---|---|---|---|
| Microsoft Visual Studio | Proprietary (standard) Freeware (community edition) | Yes | No | Yes | Microsoft |
| Visual Studio Code | Proprietary (binary code) MIT License (source code) | Yes | Yes | Yes | Microsoft |
| Rider | Proprietary | Yes | Yes | Yes | JetBrains |

## Application areas

F# is a general-purpose programming language.

### Web programming

The SAFE Stack is an end-to-end F# stack to develop web applications. It uses ASP.NET Core on the server side and Fable on the client side.

Alternative end-to-end F# options include the WebSharper framework and the Oxpecker framework.

### Cross-platform app development

F# can be used together with the Visual Studio Tools for Xamarin to develop apps for iOS and Android. The Fabulous library provides a more comfortable functional interface.

### Analytical programming

Among others, F# is used for quantitative finance programming, energy trading and portfolio optimization, machine learning, business intelligence and social gaming on Facebook.

In the 2010s, F# has been positioned as an optimized alternative to C#. F#'s scripting ability and inter-language compatibility with all Microsoft products have made it popular among developers.

### Scripting

F# can be used as a scripting language, mainly for desktop read–eval–print loop (REPL) scripting.

## Open-source community

The F# open-source community includes the F# Software Foundation and the F# Open Source Group at GitHub. Popular open-source F# projects include:

- Fable, an F# to Javascript transpiler based on Babel.
- Paket, an alternative package manager for .NET that can still use NuGet repositories, but has centralised version-management.
- FAKE, an F# friendly build-system.
- Giraffe, a functionally oriented middleware for ASP.NET Core.
- Suave, a lightweight web-server and web-development library.

## Compatibility

F# features a legacy "ML compatibility mode" that can directly compile programs written in a large subset of OCaml roughly, with no functors, objects, polymorphic variants, or other additions.

## Examples

A few small samples follow:

```mw
// This is a comment for a sample hello world program.
printfn "Hello World!"
```

A record type definition. Records are immutable by default and are compared by structural equality.

```mw
type Person = {
    FirstName: string
    LastName: string
    Age: int
}

// Creating an instance of the record
let person = { FirstName = "John"; LastName = "Doe"; Age = 30 }
```

A Person class with a constructor taking a name and age and two immutable properties.

```mw
/// This is a documentation comment for a type definition.
type Person(name : string, age : int) =
    member x.Name = name
    member x.Age = age
    
/// class instantiation
let mrSmith = Person("Smith", 42)
```

A simple example that is often used to demonstrate the syntax of functional languages is the factorial function for non-negative 32-bit integers, here shown in F#:

```mw
/// Using pattern matching expression
let rec factorial n =
    match n with
    | 0 -> 1
    | _ -> n * factorial (n - 1)

/// For a single-argument functions there is syntactic sugar (pattern matching function):
let rec factorial = function 
    | 0 -> 1 
    | n -> n * factorial (n - 1)
    
/// Using fold and range operator
let factorial n = [1..n] |> Seq.fold (*) 1
```

Iteration examples:

```mw
/// Iteration using a 'for' loop
let printList lst = 
    for x in lst do
        printfn $"{x}" 

/// Iteration using a higher-order function
let printList2 lst = 
    List.iter (printfn "%d") lst

/// Iteration using a recursive function and pattern matching
let rec printList3 lst =
    match lst with
    | [] -> ()
    | h :: t ->
        printfn "%d" h
        printList3 t
```

Fibonacci examples:

```mw
/// Fibonacci Number formula
[<TailCall>]
let fib n =
    let rec g n f0 f1 =
        match n with
        | 0 -> f0
        | 1 -> f1
        | _ -> g (n - 1) f1 (f0 + f1)
    g n 0 1

/// Another approach - a lazy infinite sequence of Fibonacci numbers
let fibSeq = Seq.unfold (fun (a,b) -> Some(a+b, (b, a+b))) (0,1)

// Print even fibs
[1 .. 10]
|> List.map     fib
|> List.filter  (fun n -> (n % 2) = 0)
|> printList

// Same thing, using a list expression
[ for i in 1..10 do
    let r = fib i
    if r % 2 = 0 then yield r ]
|> printList
```

A sample Windows Forms program:

```mw
// Open the Windows Forms library
open System.Windows.Forms

// Create a window and set a few properties
let form = new Form(Visible=true, TopMost=true, Text="Welcome to F#")

// Create a label to show some text in the form
let label =
    let x = 3 + (4 * 5)
    new Label(Text = $"{x}")

// Add the label to the form
form.Controls.Add(label)

// Finally, run the form
[<System.STAThread>]
Application.Run(form)
```

Asynchronous parallel programming sample (parallel CPU and I/O tasks):

```mw
/// A simple prime number detector
let isPrime (n:int) =
   let bound = int (sqrt (float n))
   seq {2 .. bound} |> Seq.forall (fun x -> n % x <> 0)

// We are using async workflows
let primeAsync n =
    async { return (n, isPrime n) }

/// Return primes between m and n using multiple threads
let primes m n =
    seq {m .. n}
        |> Seq.map primeAsync
        |> Async.Parallel
        |> Async.RunSynchronously
        |> Array.filter snd
        |> Array.map fst

// Run a test
primes 1000000 1002000
    |> Array.iter (printfn "%d")
```
