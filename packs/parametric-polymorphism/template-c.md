---
title: "Template (C++)"
source: https://en.wikipedia.org/wiki/Template_(C%2B%2B)
domain: parametric-polymorphism
license: CC-BY-SA-4.0
tags: parametric polymorphism, type parameter, generic programming, type constructor
fetched: 2026-07-02
---

# Template (C++)

**Templates** are a feature of the C++ programming language that allow functions and classes to operate with generic types. This allows a function or class declaration to reference via a generic variable another different class (built-in or newly declared data type) without creating a full declaration for each of these different classes.

In plain terms, a templated class or function would be the equivalent of (before "compiling") copying and pasting the templated block of code where it is used, and then replacing the template parameter with the actual one. For this reason, classes employing templated methods place the implementation in the headers (*.h files) as no symbol could be compiled without knowing the type beforehand.

The C++ Standard Library provides many useful functions within a framework of connected templates.

Major inspirations for C++ templates were the parameterized modules provided by the language CLU and the generics provided by Ada.

## Technical overview

There are three kinds of templates: *function templates*, *class templates* and, since C++14, *variable templates*. Since C++11, templates may be either variadic or non-variadic; in earlier versions of C++ they are always non-variadic.

C++ Templates are Turing complete.

### Function templates

A *function template* behaves like a function except that the template can accept arguments of various types, enabling type-generic behavior (see example). In other words, a function template represents a family of functions. The format for declaring function templates with type parameters is:

```mw
template <class Identifier> Declaration;
template <typename Identifier> Declaration;
```

Both expressions have the same meaning and behave in exactly the same way. The latter form was introduced to avoid confusion, since a type parameter need not be a class until C++20. (It can be a basic type such as `int` or `double`.)

For example, the C++ Standard Library contains the function template `max(x, y)` which returns the larger of `x` and `y`. That function template could be defined like this:

```mw
template <typename T>
[[nodiscard]]
constexpr T& max(const T& a, const T& b) noexcept {
    return a < b ? b : a;
}
```

This single function definition works with many data types. Specifically, it works with all data types for which **<** (the less-than operator) is defined and returns a value with a type convertible to `bool`. The usage of a function template saves space in the source code file in addition to limiting changes to one function description and making the code easier to read.

An instantiated function template usually produces the same object code, though, compared to writing separate functions for all the different data types used in a specific program. For example, if a program uses both an `int` and a `double` version of the `max()` function template above, the compiler will create an object code version of `max()` that operates on `int` arguments and another object code version that operates on `double` arguments. The compiler output will be identical to what would have been produced if the source code had contained two separate non-templated versions of `max()`, one written to handle `int` and one written to handle `double`.

Here is how the function template could be used:

```mw
import std;

int main() {
    // This will call max<int> by implicit argument deduction.
    std::println("{}", std::max(3, 7));

    // This will call max<double> by implicit argument deduction.
    std::println("{}", std::max(3.0, 7.0));

    // We need to explicitly specify the type of the arguments; 
    // although std::type_identity could solve this problem...
    std::println("{}", max<double>(3, 7.0));
}
```

In the first two cases, the template argument `T` is automatically deduced by the compiler to be `int` and `double`, respectively. In the third case automatic deduction of `max(3, 7.0)` would fail because the type of the parameters must in general match the template arguments exactly. Therefore, we explicitly instantiate the `double` version with `max<double>()`.

This function template can be instantiated with any copy-constructible type for which the expression `y < x` is valid. For user-defined types, this implies that the less-than operator (`<`) must be overloaded in the type.

#### Abbreviated function templates

Since C++20, using `auto` or `concept auto` in any of the parameters of a function declaration, that declaration becomes an *abbreviated function template* declaration. Such a declaration declares a function template and one invented template parameter for each placeholder is appended to the template parameter list:

```mw
// equivalent to:
// template <typename T>
// void f1(T x);
void f1(auto x);

// equivalent to (if Concept1 is a concept):
// <Concept1 T>
// void f2(T x);
void f2(Concept1 auto x);

// equivalent to (if Concept2 is a concept):
// template <Concept2... Ts>
// void f3(Ts... xs)
void f3(Concept2 auto... xs);

// equivalent to (if Concept2 is a concept):
// template <Concept2 T>
// void f4(T... xs);
void f4(Concept2 auto xs, ...);

// equivalent to (if Concept3 and Concept4 are concepts):
// template <Concept3 T, Concept4 U>
// f5(const T* t, U& u);
void f5(const Concept3 auto* t, Concept4 auto& u);
```

Constraining the `max()` using concepts could look something like this:

```mw
using std::totally_ordered;

// in typename declaration:
template <totally_ordered T>
[[nodiscard]]
constexpr T max(T x, T y) noexcept {
    return x < y ? y : x;
}

// in requires clause:
template <typename T>
    requires totally_ordered<T>
[[nodiscard]]
constexpr T max(T x, T y) noexcept {
    return x < y ? y : x;
}
```

### Class templates

A class template provides a specification for generating classes based on parameters. Class templates are generally used to implement containers. A class template is instantiated by passing a given set of types to it as template arguments. The C++ Standard Library contains many class templates, in particular the containers adapted from the Standard Template Library, such as `vector`.

### Variable templates

In C++14, templates can be also used for variables, as in the following example:

```mw
template <typename T> 
constexpr T PI = T{3.141592653589793238462643383L}; // (Almost) from std::numbers::pi
```

### Non-type template parameters

Although templating on types, as in the examples above, is the most common form of templating in C++, it is also possible to template on values. Thus, for example, a class declared with

```mw
template <int K>
class MyClass;
```

can be instantiated with a specific `int`.

As a real-world example, the standard library fixed-size array type `std::array` is templated on both a type (representing the type of object that the array holds) and a number which is of type `std::size_t` (representing the number of elements the array holds). To create a class `Array` equivalent to `std::array`, it can be declared as follows:

```mw
template <class T, size_t N> 
struct Array;
```

and an array of six `char`s might be declared:

```mw
Array<char, 6> myArray;
```

### Template specialization

When a function or class is instantiated from a template, a specialization of that template is created by the compiler for the set of arguments used, and the specialization is referred to as being a generated specialization.

### Explicit template specialization

Sometimes, the programmer may decide to implement a special version of a function (or class) for a given set of template type arguments which is called an explicit specialization. In this way certain template types can have a specialized implementation that is optimized for the type or a more meaningful implementation than the generic implementation.

- If a class template is specialized by a subset of its parameters it is called partial template specialization (function templates cannot be partially specialized).
- If all of the parameters are specialized it is a *full specialization*.

Explicit specialization is used when the behavior of a function or class for particular choices of the template parameters must deviate from the generic behavior: that is, from the code generated by the main template, or templates. For example, the template definition below defines a specific implementation of `max()` for arguments of type `const char*`:

```mw
import std;

template <> 
[[nodiscard]]
constexpr const char* max(const char* a, const char* b) noexcept {
    // Normally, the result of a direct comparison
    // between two C strings is undefined behaviour;
    // using std::strcmp makes defined.
    return std::strcmp(a, b) > 0 ? a : b;
}
```

### Variadic templates

C++11 introduced variadic templates, which can take a variable number of arguments in a manner somewhat similar to variadic functions such as `std::printf`.

```mw
using std::format_string;
using std::ofstream;

enum class Level { ... };

ofstream logFile{"logfile.txt"};

template <typename... Args>
void log(const format_string<Args...>& fmt, Args&&... args) {
    std::println(logFile, fmt, args...);
}
```

Because only C-style variadic parameters are supported in C++, the only way to get type-safe variadic functions (like in Java) is through variadic templates.

### Template aliases

C++11 introduced template aliases, which act like parameterized typedefs.

The following code shows renaming `std::map` to `TreeMap` and `std::unordered_map` to `HashMap`, as well as creating an alias `StringHashMap` for `std::unordered_map<K, std::string>`. This allows, for example, `StringHashMap<int>` to be used as shorthand for `std::unordered_map<int, std::string>`.

```mw
using String = std::string;

// allowing optional specialization of hash functions, allocators, etc.
template <
    typename K, 
    typename V, 
    typename Compare = std::less<K>, 
    typename Alloc = std::allocator<std::pair<const K, T>>
>
using TreeMap = std::map<K, V, Compare, Alloc>;

template <
    typename K, 
    typename V, 
    typename HashFn = std::hash<K>, 
    typename KeyEq = std::equal_to<K>, 
    typename Alloc = std::allocator<std::pair<const K, T>>
> 
using HashMap = std::unordered_map<K, V, HashFn, KeyEq, Alloc>;

// or, only allowing K and V to be specialized:
template <typename K, typename V>
using TreeMap = std::map<K, V>;

template <typename K, typename V> 
using HashMap = std::unordered_map<K, V>;

// Defining StringHashMap<K> = HashMap<K, String>
template <typename K>
using StringHashMap = HashMap<K, String>;

StringHashMap<int> myMap = /* something here... */;
```

### Constrained templates

Since C++20, templates can be constrained similarly to generics wildcards in Java or C# and Rust `where` clauses. This is done using concepts, which represent a set of boolean predicates evaluated at compile time.

For example, this code uses `std::derived_from<Derived, Based>` as an upper inheritance bound. A class satisfies this concept if it inherits from `Player`, and classes that do not cannot be used as the template parameter in `processListOfPlayers()`.

```mw
import std;

using std::derived_from;
using std::vector;

class Player {
    // ...
};

// T is required to be a type whose inheritance upper bound is Player,
// blocking any type that does not inherit from Player
template <derived_from<Player> T>
void processListOfPlayers(const vector<T>& players) {
    // ...
}
```

Concepts can be used to implement a form of type-safe variadic parameters. For example, the Java signature `<T> void fn(T... args);`

```mw
using std::same_as;

template <typename T>
void fn(same_as<T> auto... args) {
    // ...
}
```

Furthermore, to constrain these to any specific type, the `std::same_as<T, U>` and `std::convertible_to<T, U>` concepts may be used. For instance, the Java signatures `void foo(int... args);` and `void bar(String... args);` could be written as `void foo(same_as<int> auto... args);` and `void bar(convertible_to<string> auto... args);` respectively.

### Exported templates

In C++03, "exported templates" were added to C++. These were later removed in C++11, due to very few compilers actually supporting the feature. The only compiler known to support exported templates was Comeau C/C++. Among the cited reasons for removal were:

- Expensive or complex to implement
- Little benefit to most users as well as little interest
- Difficult to use
- Changes to meanings of existing language features
- Restricting the future development of C++

An "exported template" is essentially a class template whose static data members and non-inline methods are exported. It must be marked by the keyword `export`. What distinguishes an "exported template" is the fact that it does not need to be defined in a translation unit that uses the template. For example (in C++03):

File1.cpp:

```mw
#include <iostream>

static void trace() {
    std::cout << "File 1" << std::endl;
}

export template <typename T>
T min(const T& x, const T& y);

int main() {
    trace();
    std::cout << min(2, 3) << std::endl;
}
```

File2.cpp:

```mw
#include <iostream>

static void trace() {
    std::cout << "File 2" << std::endl;
}

export template <typename T>
T min(const T& x, const T& y) {
    trace();
    return a < b ? a : b;
}
```

With the introduction of modules in C++20, the keyword `export` was re-added to C++. This re-allowed declarations like this:

```mw
import std;

using std::is_base_of_v;

export class Atom {
    // ...
};

export template <typename T>
concept ExtendsAtom = is_base_of_v<Atom, T>;

export template <ExtendsAtom Instance, typename... Bases>
class Cluster: public Bases... {
private:
    Instance x;
public:
    explicit Cluster(Instance x, Bases&&... bases):
        Bases(bases)..., x{x} {}

    // ...
};
```

The compilation speed benefits intended to be offered by exported templates are offered by modules anyway, making the feature essentially obsolete and superseded by modules.

## Generic programming features in other languages

Initially, the concept of templates was not included in some languages, such as Java and C# 1.0. Java's adoption of generics mimics the behavior of templates, but is technically different. C# added generics (parameterized types) in .NET 2.0. The generics in Ada predate C++ templates.

Although C++ templates, Java generics, and .NET generics are often considered similar, generics only mimic the basic behavior of C++ templates. Some of the advanced template features utilized by libraries such as Boost and STLSoft, and implementations of the STL, for template metaprogramming (explicit or partial specialization, default template arguments, template non-type arguments, template template arguments, ...) are unavailable with generics.

In C++ templates, compile-time cases were historically performed by pattern matching over the template arguments. For example, the template base class in the Factorial example below is implemented by matching 0 rather than with an inequality test, which was previously unavailable. However, the arrival in C++11 of standard library features such as `std::conditional` has provided another, more flexible way to handle conditional template instantiation.

```mw
// Induction
template <unsigned int N> 
struct Factorial {
    static constexpr unsigned int value = N * Factorial<N - 1>::value;
};

// Base case via template specialization:
template <> 
struct Factorial<0> {
    static constexpr unsigned int value = 1;
};
```

With these definitions, one can compute, say 6! at compile time using the expression `Factorial<6>::value`.

Alternatively, `constexpr` in C++11 / `if constexpr` in C++17 can be used to calculate such values directly using a function at compile-time:

```mw
template <unsigned int N>
[[nodiscard]]
constexpr unsigned int factorial() noexcept {
    if constexpr (N <= 1) {
        return 1;
    } else {
        return N * factorial<N - 1>();
    }
}
```

Because of this, template meta-programming is now mostly used to do operations on types.
