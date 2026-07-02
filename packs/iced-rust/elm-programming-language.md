---
title: "Elm (programming language)"
source: https://en.wikipedia.org/wiki/Elm_(programming_language)
domain: iced-rust
license: CC-BY-SA-4.0
tags: iced toolkit, elm architecture, rust reactive gui, cross-platform rendering
fetched: 2026-07-02
---

# Elm (programming language)

**Elm** is a domain-specific programming language for declaratively creating web browser-based graphical user interfaces. Elm is purely functional, and is developed with emphasis on usability, performance, and robustness. It advertises "no runtime exceptions in practice", made possible by the Elm compiler's static type checking.

## History

Elm was initially designed by Evan Czaplicki as his thesis in 2012. The first release of Elm came with many examples and an online editor that made it easy to try out in a web browser. Czaplicki joined Prezi in 2013 to work on Elm, and in 2016 moved to NoRedInk as an Open Source Engineer, also starting the Elm Software Foundation.

The initial implementation of the Elm compiler targets HyperText Markup Language (HTML), Cascading Style Sheets (CSS), and JavaScript. The set of core tools has continued to expand, now including a read–eval–print loop (REPL), package manager, time-travelling debugger, and installers for macOS and Windows. Elm also has an ecosystem of community created libraries, and Ellie, an advanced online editor that allows saved work and including community libraries.

## Features

Elm has a small set of language constructs, including traditional if-expressions, let-expressions for storing local values, and case-expressions for pattern matching. As a functional language, it supports anonymous functions, functions as arguments, and functions can return functions, the latter often by partial application of curried functions. Functions are called by value. Its semantics include immutable values, stateless functions, and static typing with type inference. Elm programs render HTML through a virtual DOM, and may interoperate with other code by using "JavaScript as a service".

### Immutability

All values in Elm are immutable, meaning that a value cannot be modified after it is created. Elm uses persistent data structures to implement its arrays, sets, and dictionaries in the standard library.

### Static types

Elm is statically typed. Type annotations are optional (due to type inference) but strongly encouraged. Annotations exist on the line above the definition (unlike C-family languages where types and names are interspersed). Elm uses a single colon to mean "has type".

Types include primitives like integers and strings, and basic data structures such as lists, tuples, and records. Functions have types written with arrows, for example `round : Float -> Int`. Custom types allow the programmer to create custom types to represent data in a way that matches the problem domain.

Types can refer to other types, for example a `List Int`. Types are always capitalized; lowercase names are type variables. For example, a `List a` is a list of values of unknown type. It is the type of the empty list and of the argument to `List.length`, which is agnostic to the list's elements. There are a few special types that programmers create to interact with the Elm runtime. For example, `Html Msg` represents a (virtual) DOM tree whose event handlers all produce messages of type `Msg`.

Rather than allow any value to be implicitly nullable (such as JavaScript's `undefined` or a null pointer), Elm's standard library defines a `Maybe a` type. Code that produces or handles an optional value does so explicitly using this type, and all other code is guaranteed a value of the claimed type is actually present.

Elm provides a limited number of built-in type classes: `number` which includes `Int` and `Float` to facilitate the use of numeric operators such as `(+)` or `(*)`, `comparable` which includes numbers, characters, strings, lists of comparable things, and tuples of comparable things to facilitate the use of comparison operators, and `appendable` which includes strings and lists to facilitate concatenation with `(++)`. Elm does not provide a mechanism to include custom types into these type classes or create new type classes (see Limits).

### Module system

Elm has a module system that allows users to break their code into smaller parts called modules. Modules can hide implementation details such as helper functions, and group related code together. Modules serve as a namespace for imported code, such as `Bitwise.and`. Third party libraries (or packages) consist of one or more modules, and are available from the Elm Public Library. All libraries are versioned according to semver, which is enforced by the compiler and other tools. That is, removing a function or changing its type can only be done in a major release.

### Interoperability with HTML, CSS, and JavaScript

Elm uses an abstraction called ports to communicate with JavaScript. It allows values to flow in and out of Elm programs, making it possible to communicate between Elm and JavaScript.

Elm has a library called elm/html that a programmer can use to write HTML and CSS within Elm. It uses a virtual DOM approach to make updates efficient.

### Backend

Elm does not officially support server-side development. Czaplicki does consider it a primary goal, but public progress on this front has been slow. Nevertheless, there are several independent projects which attempt to explore Elm on the backend.

The primary full-stack Elm platform is Lamdera, an open-core "unfork" of Elm. Czaplicki has also teased Elm Studio, a potential alternative to Lamdera, but it is not yet available to the public. Czaplicki's demos seemingly use a future version of Elm that supports type-safe Postgres table generation. There is also speculation that that future versions of Elm would compile to C and use Emscripten to generate WASM, but this is unconfirmed by Czaplicki.

For full-stack frameworks, as opposed to BaaS products, elm-pages is likely the most popular fully open-source option. It does not extend the Elm language (although it does use open-source components of the aforementioned Lamdera compiler), but rather runs the compiled JavaScript on Node.js. It also supports scripting using the `BackendTask` API. There is also Pine, an Elm to .NET compiler, which allows safe interop with C#, F#, and other CLR languages.

There were also attempts in Elm versions prior to 0.19.0 to use the BEAM (Erlang virtual machine) to run Elm, but they are currently non-functional due to the removal of native code in 0.19.0 and changes to the package manager. One of the projects executed Elm directly on the environment, while another one compiled it to Elixir.

## The Elm Architecture (TEA pattern)

The Elm Architecture is a software design pattern and as a TLA called TEA pattern for building interactive web applications. Elm applications are naturally constructed in that way, but other projects may find the concept useful.

An Elm program is always split into three parts:

- Model - the state of the application
- View - a function that turns the model into HTML
- Update - a function that updates the model based on messages

Those are the core of the Elm Architecture.

For example, imagine an application that displays a number and a button that increments the number when pressed. In this case, all we need to store is one number, so our model can be as simple as `type alias Model = Int`. The `view` function would be defined with the `Html` library and display the number and button. For the number to be updated, we need to be able to send a message to the `update` function, which is done through a custom type such as `type Msg = Increase`. The `Increase` value is attached to the button defined in the `view` function such that when the button is clicked by a user, `Increase` is passed on to the `update` function, which can update the model by increasing the number.

In the Elm Architecture, sending messages to `update` is the only way to change the state. In more sophisticated applications, messages may come from various sources: user interaction, initialization of the model, internal calls from `update`, subscriptions to external events (window resize, system clock, JavaScript interop...) and URL changes and requests.

## Limits

Elm does not support higher-kinded polymorphism, which related languages Haskell, Scala and PureScript offer, nor does Elm support the creation of type classes.

This means that, for example, Elm does not have a generic `map` function which works across multiple data structures such as `List` and `Set`. In Elm, such functions are typically invoked qualified by their module name, for example calling `List.map` and `Set.map`. In Haskell or PureScript, there would be only one function `map`. This is a known feature request that is on Czaplicki's rough roadmap since at least 2015. On the other hand, implementations of TEA pattern in advanced languages like Scala does not suffer from such limitations and can benefit from Scala's type classes, type-level and kind-level programming constructs.

Another outcome is a large amount of boilerplate code in medium to large size projects as illustrated by the author of "Elm in Action," a former Elm core team member, in his single page application example with almost identical fragments being repeated in update, view, subscriptions, route parsing and building functions.

## Example code

```mw
-- This is a single line comment.

{-
This is a multi-line comment.
It is {- nestable. -}
-}

-- Here we define a value named `greeting`. The type is inferred as a `String`.
greeting =
    "Hello World!"

-- It is best to add type annotations to top-level declarations.
hello : String
hello =
    "Hi there."

-- Functions are declared the same way, with arguments following the function name.
add x y =
    x + y

-- Again, it is best to add type annotations.
hypotenuse : Float -> Float -> Float
hypotenuse a b =
    sqrt (a^2 + b^2)

-- We can create lambda functions with the `\[arg] -> [expression]` syntax.
hello : String -> String
hello = \s -> "Hi, " ++ s

-- Function declarations may have the anonymous parameter names denoted by `_`, 
-- which are matched but not used in the body. 
const : a -> b -> a
const k _ = k

-- Functions are also curried; here we've curried the multiplication 
-- infix operator with a `2`
multiplyBy2 : number -> number
multiplyBy2 =
    (*) 2

-- If-expressions are used to branch on `Bool` values
absoluteValue : number -> number
absoluteValue number =
    if number < 0 then negate number else number

-- Records are used to hold values with named fields
book : { title : String, author : String, pages : Int }
book =
    { title = "Steppenwolf"
    , author = "Hesse"
    , pages = 237 
    }

-- Record access is done with `.`
title : String
title =
    book.title

-- Record access `.` can also be used as a function
author : String
author =
    .author book

-- We can create tagged unions with the `type` keyword.
-- The following value represents a binary tree.
type Tree a
    = Empty
    | Node a (Tree a) (Tree a)

-- It is possible to inspect these types with case-expressions.
depth : Tree a -> Int
depth tree =
    case tree of
        Empty -> 0
        Node _ left right ->
            1 + max (depth left) (depth right)
```
