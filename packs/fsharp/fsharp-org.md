---
title: "fsharp.org"
source: https://fsharp.org/
domain: fsharp
license: CC-BY-SA-4.0
tags: f sharp, fsharp language, dotnet fsharp, fsharp lang
fetched: 2026-07-02
---

# fsharp.org

F#

empowers everyone to write

succinct

,

robust

and

performant

code

F# gives you **simplicity** like Python with **correctness**, **robustness** and **performance** beyond C# or Java.

F# is **open source**, **cross-platform** and **free** to use with **professional** tooling.

F# is a **JavaScript** and **.NET** language for **web**, **cloud**, **data-science**, **apps** and more.

HelloWorld.fs

```fsharp
let hello name =
    printfn $"Hello, {name}!"

let greets = [
    "World"
    "Solar System"
    "Galaxy"
    "Universe"
    "Omniverse"
]

greets |> List.iter hello
```

## Concise like Python

F#’s elegant syntax and strong typing give you the tools to solve problems succinctly, robustly and happily.

## Concise like Python

F#’s elegant syntax and strong typing give you the tools to solve problems succinctly, robustly and happily.

- **Concise syntax** defines reusable functions with minimal boilerplate
- **Simple lists** uses indentation-based syntax without requiring commas
- **String interpolation** provides readable string formatting with the `$` prefix
- **Pipeline operator** creates a readable left-to-right flow of data

In just a few lines of code, F# provides a clean, readable implementation that would require significantly more boilerplate in many other languages. This expressive style becomes even more valuable as your programs grow in complexity.

OOP.fs

```fsharp
// Interface definition
type ICalculator =
    abstract Add: x: int -> y: int -> int
    abstract Multiply: x: int -> y: int -> int

// Class implementation with interface
type Calculator(precision: int) =
    
    // Interface implementation
    interface ICalculator with
        member _.Add x y = x + y
        member _.Multiply x y = x * y
    
    // Public methods
    member _.Subtract(x, y) = x - y
    
    // Method using property
    member _.RoundToPrecision(value: float) =
        System.Math.Round(value, precision)
        
    // Method with default parameter
    member _.Power(x: float, ?exponent: float) =
        let exp = defaultArg exponent 2.0
        System.Math.Pow(x, exp)

// Object expression (anonymous implementation)
let quickCalc = 
    { new ICalculator with 
        member _.Add x y = x + y
        member _.Multiply x y = x * y }

// Type extension - add method to existing type
type System.Int32 with
    member x.IsEven = x % 2 = 0
```

## Objects Made Simple

F# is **functional first** and **immutable by default**, but it also provides pragmatic support for object programming.

## Objects Made Simple

F# is **functional first** and **immutable by default**, but it also provides pragmatic support for object programming.

- **Seamless .NET integration** lets you work with existing .NET libraries and frameworks
- **Rich interface system** allows you to define clear contracts for your components
- **Object expressions** provide lightweight implementation of interfaces without defining full classes
- **Concise member syntax** keeps methods and properties clean and readable
- **Automatic property generation** reduces boilerplate code for data-carrying types
- **Type extensions** let you add methods to existing types without inheritance

PaymentSystem.fs

```fsharp
type CardInfo = { Number: string; Expiry: string; Cvv: string }

type BankInfo = { AccountNumber: string; RoutingNumber: string }

type PayPalInfo = { Email: string; Token: string }

type PaymentMethod =
    | CreditCard of CardInfo
    | BankTransfer of BankInfo
    | PayPal of PayPalInfo

type Payment = {
    Amount: decimal
    Method: PaymentMethod
}

let processPayment payment =
    match payment.Method with
    | CreditCard card -> 
        printfn
            "Processing $%.2f via card %s"
            payment.Amount
            card.Number
    | BankTransfer bank ->
        printfn
            "Processing $%.2f via bank account %s"
            payment.Amount
            bank.AccountNumber
    | PayPal pp ->
        printfn
            "Processing $%.2f via PayPal account %s"
            payment.Amount
            pp.Email
```

## Domain Models made Simple and Safe

## Domain Models made Simple and Safe

F# gives you superb capabilities to create precise domain models that prevent errors at compile time.

- **Discriminated unions** model each payment method with exactly the fields it needs
- **No “impossible” states** can exist - a credit card payment can’t have a routing number
- **Exhaustive pattern matching** ensures every payment type is handled properly
- **Type safety** catches errors at compile time that would be runtime bugs in other languages

By modeling your domain using F#’s algebraic data types, you create self-documenting code where the type system itself enforces business rules. This powerful technique shifts many bugs from runtime to compile time, dramatically improving software reliability.

WebApps.fs

```fsharp
open Browser.Dom
open Feliz

// DOM manipulation
let button = document.createElement("button")
button.textContent <- "Click me!"
button.addEventListener("click", fun _ -> 
    window.alert("Hello from F#!")
)
document.body.appendChild(button) |> ignore

// React component (Feliz)
let counter = React.functionComponent(fun () ->
    let (count, setCount) = React.useState(0)
    Html.div [
        Html.button [
            prop.text "-"
            prop.onClick (fun _ -> setCount(count - 1) )
        ]
        Html.span [prop.text count]
        Html.button [
            prop.text "+"
            prop.onClick (fun _ -> setCount(count + 1) )
        ]
    ]
)
```

## F# for JavaScript and the Full Stack

F# is for both client and server. With F# web technologies, you can target JavaScript environments directly. This means you can use F# to build web applications, mobile apps, and even serverless functions that run in the cloud.

## F# for JavaScript and the Full Stack

F# is for both client and server. With F# web technologies, you can target JavaScript environments directly. This means you can use F# to build web applications, mobile apps, and even serverless functions that run in the cloud.

- **Type-safe DOM manipulation** catches errors at compile time, not runtime
- **Seamless React integration** with hooks and modern patterns
- **Full npm ecosystem access** with clean TypeScript-like interop
- **Simplified async programming** with F#’s computation expressions for promises

F# brings its powerful type system and immutability to frontend development, eliminating common JavaScript bugs while maintaining full access to the JavaScript ecosystem.

TypeProviders.fs

```fsharp
open FSharp.Data

type PeopleDB = CsvProvider<"people.csv">

let printPeople () =
    let people = PeopleDB.Load("people.csv")

    for person in people.Rows do
        // Access the CSV fields with intellisense and type safety!
        printfn $"Name: %s{person.Name}, Id: %i{person.Id}"
```

## Type-Safe, Integrated Data

F# Type Providers create a seamless bridge between your code and data sources.

## Type-Safe, Integrated Data

F# Type Providers create a seamless bridge between your code and data sources.

- **Zero-friction data access** connects to CSV, JSON, XML, SQL, and more without manual mapping
- **Static typing at compile time** prevents runtime errors when accessing external data
- **Automatic schema discovery** creates F# types directly from sample data or schemas
- **Full IDE integration** provides intellisense for external data sources
- **Design-time capabilities** validate your code against live data sources before execution

SequenceExpressions.fs

```fsharp
let rec fizzBuzzSeq n = seq {
    match n with
    | x when x % 15 = 0 -> "fizzbuzz"
    | x when x % 3 = 0 -> "fizz"
    | x when x % 5 = 0 -> "buzz"
    | _ -> n.ToString()
    
    // Tail recursion makes this as efficient as a "while" loop
    yield! fizzBuzzSeq (n + 1)
}

// Process the sequence using a pipeline
fizzBuzzSeq 1
|> Seq.take 100
|> Seq.iter (printfn "%s")
```

## Data Pipelines with Sequence Expressions

F# sequence expressions provide compositional, functional stream processing capabilities that integrate seamlessly with every part of the language.

## Data Pipelines with Sequence Expressions

F# sequence expressions provide compositional, functional stream processing capabilities that integrate seamlessly with every part of the language.

- **Simplified data generation** through sequence expressions
- **Compositional data processing** through library routines
- **On-demand evaluation** of data streams
- **Fluent, maintainable code** that is easy to read and understand

AsyncExpressions.fs

```fsharp
// An async function
let fetchDataAsync url = async {
    printfn "Fetching data from %s..." url
    do! Async.Sleep 1000 // Simulate network delay
    return sprintf "Data from %s" url
}

// Using pattern matching in async code
let processPersonAsync person = async {
    let result = validatePerson person.Age person.Name
    match result with
    | Ok validated ->
        return! fetchDataAsync $"profile/{validated.Name}"
    | Error msg ->
        return $"Validation error: {msg}"
}

processPersonAsync { Name = "Snowdrop"; Age = 13}
|> Async.RunSynchronously
```

## Async Programming made Easy

F# async expressions provide a powerful way to handle asynchronous programming, making it more readable and maintainable. They allow you to write non-blocking code that looks like synchronous code, which is particularly useful for I/O-bound operations.

## Async Programming made Easy

F# async expressions provide a powerful way to handle asynchronous programming, making it more readable and maintainable. They allow you to write non-blocking code that looks like synchronous code, which is particularly useful for I/O-bound operations.

- **Async expressions** provide a clean syntax for defining asynchronous workflows
- **Integration with existing libraries** makes it easy to use async expressions with other F# features
- **Error handling** is simplified with the use of discriminated unions and pattern matching
- **Seamless integration** with F#’s type system ensures type safety and reduces runtime errors
- **Support for cancellation** and timeouts allows you to manage long-running operations effectively

ComputationExpressions.fs

```fsharp
// Define a custom computation expression for validation
type ValidationBuilder() =
    member _.Bind(x, f) = // Defines "let!"
        match x with
        | Ok value -> f value
        | Error e -> Error e
    member _.Return(x) = Ok x // Defines "return"
    member _.ReturnFrom(x) = x // Defines "return!"
let validate = ValidationBuilder()

type Person = { Name: string; Age: int }

// Use the custom computation expression
let validatePerson age name = validate {
    let! validAge = 
        if age >= 0 && age < 150 then Ok age
        else Error "Age must be between 0 and 150"
        
    let! nonEmptyName = 
        if String.length name > 0 then Ok name
        else Error "Name cannot be empty"
        
    if String.length name > 100 then
        return! Error "Name is too long!"
    else
        return { Name = nonEmptyName; Age = validAge }
}
```

## Clean Code with Computation Expressions

F# computation expressions give you an elegant syntax for compositional control flows with a clean, readable notation that some say is F#’s superpower.

## Clean Code with Computation Expressions

F# computation expressions give you an elegant syntax for compositional control flows with a clean, readable notation that some say is F#’s superpower.

- **Computation expressions** factor out how code is composed together
- **Custom control flow abstractions** create domain-specific mini-languages
- **Seamless error handling** with railway-oriented programming patterns
- **Elegant data transformations** by hiding boilerplate and focusing on business logic
- **Composable workflows** that can be combined and nested for complex operations

UnitsOfMeasure.fs

```fsharp
open FSharp.Data.UnitSystems.SI

// Acceleration due to gravity
let g = 9.81<m/s^2> 

// The return type is inferred as float<m>
let distance ( t: float<s> ) =
    0.5 * g * t * t  

let fallDuration = 2.0<s>
let fallDistance = distance fallDuration
printfn $"Distance fallen in {fallDuration}s is {fallDistance}m"
```

## Safe Numbers through Units of Measure

F# offers world-class compile-time unit safety without runtime overhead, giving you the power to express your domain in a type-safe way. This is particularly useful in scientific, engineering and financial applications where unit errors can lead to catastrophic results.

## Safe Numbers through Units of Measure

F# offers world-class compile-time unit safety without runtime overhead, giving you the power to express your domain in a type-safe way. This is particularly useful in scientific, engineering and financial applications where unit errors can lead to catastrophic results.

- **Compile-time dimensional safety** catches errors before running, preventing scientific and engineering mistakes
- **Domain-specific units** express quantities that directly reflect your problem space
- **Automatic unit conversions** maintain type safety while handling complex calculations
- **Seamless interoperability** works with normal numeric types when needed
- **Custom unit definitions** let you create your own units and conversions with simple syntax

### Learn

- F# Hello World in 5min
- F# for Beginners
- F# for JavaScript

### Community

- Join the conversation on Bluesky or Discord
- Participate in Amplifying F#
- Contribute to F# projects

We would recommend F# as an additional tool in the kit of any company building software on the .NET stack.

**Michael Newton**, Senior Developer

F# makes it easy to spend your time answering interesting questions about the domain and less time answering questions about the language.

**Jamie Dixon**

Around 95% of the code in these projects has been developed in F#

Anton Schwaighofer, **Microsoft**

Many languages are evolving to be ready for the future ... F# is already there.

Alex Hardwicke

F# will continue to be our language of choice for scientific computing.

**Dr. Andrew Phillips**

It's like 'Python with type inference' — but even better!

An anonymous game developer

I evaluated F# and found that for certain tasks it was better than C# in terms of performance while maintaining suitable readability

**Atalasoft**

Large insurance company developed an entire pension quote calculator entirely in F# in under 100 days with no prior F# experience at all...

**Large insurance company**

The benefits of functional programming in F# have given us a great advantage over our slow moving competitors.

Bayard Rock

Bohdan ... shows F#'s use for performing aggregations over large datasets, taking advantage of CPU and IO parallelism

**Bohdan Szymanik**

F# encourages Reason Driven Development that leads to virtually bug-free code

**Boston-based Financial Services Firm, Fixed Income**

F# is the night vision goggles I need when I go into the dark and attempt to solve previously unsolved problems.

**Professor Byron Cook**

F# allow us to keep the code simple even in complicated business cases.

Urs Enzler

Just use F#. Your future self will thank you from saving them hundreds of headaches.

**Cameron Murdoch**

F# is a powerful language and it is great to do cross platform development with it.

**Can Erten**

At ClearTax, We have built a whole product from the ground-up in F#. It's been running in production for a couple of years — this has been a great experience for us.

**Ankit Solanki, ClearTax**

The efficient use of functional programming throughout the R&D cycle helped make the cycle faster and more efficient.

Moody Hadi (CME Group)

On a release of a complex rules engine and data transformation system to one of our customers, we were delighted to hear that across 90+ markets, not one of them found any issues with any of the calculations in the datasets. F# just works.

**Isaac Abraham, Compositional IT**

At Credit Suisse, we've been using F# to develop quantitative models for financial products

**Howard Mansell**

...your code is less error-prone...

**Dario**

F# rocks... building out various algorithms for DNA processing here and it's like a drug

**Darren Platt**

Overall, F# made our development work faster and more reliable.

**David Gillard**

F#...made it trivial...

**Prof David Walker**

F# brought correct defaults, simplicity and safety back to our coding

**Deyan Petrov, 5G Pay**

There is a noticeable interest in the developer community in Russia towards F#.

**Dmitry Soshnikov**

I could not recommend F# highly enough – I insist that you try it!

**Ben Lynch**

F#'s powerful type inference means less typing, more thinking

**Don Syme**

My team chose F# for its functional paradigm, maturity, and ease of interoperation with the .NET framework

**Dylan Hutchison**

At a major Investment Bank, we used F# to build an Early Warning Indicator System for Liquidity Risk

**Stephen Channell**

...we have decided to use F# as our functional language to have automatic integration with rest of the system...

EMEA-based Security Solutions Company

With its new tools, the bank can speed development by 50 percent or more, improve quality, and reduce costs.

**Large Financial Services Firm, Europe**

I can tell you, F# really saved us a ton of effort.

**Giuseppe Maggiore**

We see great potential for F# to be used as a scripting language in CAD; it fits very well for computational design challenges in the construction industry.

**Goswin Rothenthal**

Grange Insurance parallelized its rating engine to take better advantage of multicore server hardware

**Grange Insurance**

F# terse syntax made the final code look really similar to the algorithm we wrote at first

**Green Eagle Solutions**

The performance is phenomenal. We can now re-calculate the entire bank portfolio from scratch in less than a second and the response-time for single deal verification calculation is far below 100 milliseconds.

**Jan Erik Ekelof**, M.Sc.

Solving a number of programming problems using the language convinced me of the supreme qualities of F#

**Hans Rischel**

When F# is combined with Visual Studio... productivity goes through the roof!

**Prof Nigel Horspool**

The compiler and the use of exhaustive pattern matching have saved us from what could’ve been many mistakes in production.

**Kristian Lundström & Simon Lydell**

Using F# for cross-platform mobile development (Android, iOS) saves development time

James Moore

...I have to say I love the language...

**Jared Parsons**

Each feature is designed to be there, rather than has to be there from feature creep.

**Jimmy Byrd**

A type system that gets out of your way, instead of burdening you with keywords and repeated chants.

**Jimmy Byrd**

Type providers made working with external data sources simple and intuitive.

**Jon Canning**

F# allowed us to mix Domain-Driven Design, Functional Programming and Azure to deliver a high quality web application.

**Jorge Fioranelli**

F# is more flexible than C#, yet gives stronger type safety. It allows for fearless refactoring, which is also easier because of naturally less coupled code while at the same time codebase being 40%-size of equivalent c# one.

**Jozef Rudy, PhD**

The F# code is consistently shorter, easier to read, easier to refactor and contains far fewer bugs. As our data analysis tools have developed ... we've become more productive.

**Kaggle**

The results speak for themselves.

**Matt Ball**

I keep being surprised by how compact and readable F# is...

**London-Based Asset Management Company**

The sensible defaults (immutability, non-nullability, algebraic data types, etc.) along with the power of the F# compiler enables our team to quickly and concisely develop systems.

**Matt McCarty**

Using a full F# stack to provide Server, Browser client and Mobile apps.

**Maxime Mangel**

Programming in F# feels like writing out ideas rather than code

**Maria Gorinova**

Everyone gets really amazed when they try F# and experience its immense expressive power

**Mário Pereira**

With F# I can develop libraries in a fraction of the time.

**Mauricio Scheffer**

In our engineering group at Microsoft we use F# for several projects

Microsoft Engineering Team

The simple, well-designed and powerful core of the language was perfect for introducing the fundamental concepts of functional programming.

**Michael R. Hansen**

...We use F# in oceanographic research to connect multiple visualizations together in time and space...

**Rob Fatland**, Microsoft Research

F# is central to Microsoft’s quantum algorithm research

**Dave Wecker**

it is fun language to code in

**namigop** (Erik Araojo)

F# was so easy to pick up we went from complete novices to having our code in production in less than a week.

Jack Mott

...The AI is implemented in F#...

**Microsoft**, **Path of Go**

...That's the reason we have chosen F# for our undergraduate functional programming class...

**Prof. Peter Sestoft**

Anyone who has developed software can appreciate that while a working program is an asset the source code is a liability, especially when working in a regulated industry. F# lets us keep the codebase small and agile while delivering feature-rich and proven to work solutions.

**Eugene Tolmachev, Prolucid**

The power and flexibility of the language lets us ship features faster, with fewer bugs.

**Marty Dill**

Many attributes of the F# programming language make it an ideal choice for ...the exponentially growing volumes of molecular analysis data

**Dr. Robert Boissy**

F# is very popular among my students for the programming projects

**Simão Sousa**

For a machine learning scientist, speed of experimentation is the critical factor to optimize.

**Patrice Simard**

The use of F# demonstrates a sweet spot for the language within enterprise software

**Simon Cousins**

I have now delivered three business critical projects written in F#. I am still waiting for the first bug to come in.

**UK-based Power Company**

By using F# and its strong type system, we were able to keep the code base consistent and easily adaptable to this ever-evolving and growing project.

Joh Dokler

F#'s language features not only made it a no-brainer for our project, but allowed us to produce composable, deterministic, and concise code.

**Stephen Kennedy**

F#...levels the playing field between beginners and experienced programmers.

**Prof. Susan Eisenbach**

"Speed. I am speed." works for F# like a charm.

**Sync.Today**

...the core logic is written in F# wherever possible...

**Andrea D’Intino**

We recommend teaching F# because it is an extraordinary and flexible tool for teaching different areas of Computer Science

**Antonio Cisternino**

I am using F# to develop an API for data encryption using fully homomorphic encryption.

**Vitor Pereira**

F# proved ideal for the complex data machinations required to build the models from raw Excel input.

A Fortune 100 Manufacturer

The F# solution offers us an order of magnitude increase in productivty...

**GameSys**

Read More Testimonials

## Sponsors Past & Present
