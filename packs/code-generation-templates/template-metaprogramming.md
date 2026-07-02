---
title: "Template metaprogramming"
source: https://en.wikipedia.org/wiki/Template_metaprogramming
domain: code-generation-templates
license: CC-BY-SA-4.0
tags: code generation, template metaprogramming, automatic programming, compiler code generation
fetched: 2026-07-02
---

# Template metaprogramming

**Template metaprogramming** (**TMP**) is a metaprogramming technique in which templates are used by a compiler to generate temporary source code, which is merged by the compiler with the rest of the source code and then compiled. The output of these templates can include compile-time constants, data structures, and complete functions. The use of templates can be thought of as compile-time polymorphism. The technique is used by a number of languages, the best-known being C++, but also Curl, D, Nim, and XL.

Template metaprogramming was, in a sense, discovered accidentally.

Some other languages support similar, if not more powerful, compile-time facilities (such as Lisp's macros).

## Components of template metaprogramming

The use of templates as a metaprogramming technique requires two distinct operations: a template must be defined, and a defined template must be instantiated. The generic form of the generated source code is described in the template definition, and when the template is instantiated, the generic form in the template is used to generate a specific set of source code.

Template metaprogramming is Turing-complete, meaning that any computation expressible by a computer program can be computed, in some form, by a template metaprogram.

Templates are different from *macros*. A macro is a piece of code that executes at compile time and either performs textual manipulation of code to-be compiled (e.g. C++ macros) or manipulates the abstract syntax tree being produced by the compiler (e.g. Rust or Lisp macros). Textual macros are notably more independent of the syntax of the language being manipulated, as they merely change the in-memory text of the source code right before compilation.

Template metaprograms have no mutable variables— that is, no variable can change value once it has been initialized, therefore template metaprogramming can be seen as a form of functional programming. In fact many template implementations implement flow control only through recursion, as seen in the example below.

### Using template metaprogramming

Though the syntax of template metaprogramming is usually very different from the programming language it is used with, it has practical uses. Some common reasons to use templates are to implement generic programming (avoiding sections of code which are similar except for some minor variations) or to perform automatic compile-time optimization such as doing something once at compile time rather than every time the program is run — for instance, by having the compiler unroll loops to eliminate jumps and loop count decrements whenever the program is executed.

## Compile-time class generation

What exactly "programming at compile-time" means can be illustrated with an example of a factorial function, which in non-template C++ can be written using recursion as follows:

```mw
uint32_t factorial(uint32_t n) {
	return n == 0 ? 1 : n * factorial(n - 1); 
}

// Usage examples:
// factorial(0) would yield 1;
// factorial(4) would yield 24.
```

The code above will execute at run time to determine the factorial value of the literals `0` and `4`. By using template metaprogramming and template specialization to provide the ending condition for the recursion, the factorials used in the program—ignoring any factorial not used—can be calculated at compile time by this code:

```mw
template <uint32_t N>
struct Factorial {
	static constexpr uint32_t VALUE = N * Factorial<N - 1>::VALUE;
};

template <>
struct Factorial<0> {
	static constexpr uint32_t VALUE = 1;
};

// Usage examples:
// Factorial<0>::value would yield 1;
// Factorial<4>::value would yield 24.
```

The code above calculates the factorial value of the literals `0` and `4` at compile time and uses the results as if they were precalculated constants. To be able to use templates in this manner, the compiler must know the value of its parameters at compile time, which has the natural precondition that `Factorial<X>::value` can only be used if `X` is known at compile time. In other words, `X` must be a constant literal or a constant expression.

In C++11 and C++20, constexpr and consteval were introduced to let the compiler execute code. Using `constexpr` and `consteval`, one can use the usual recursive factorial definition with the non-templated syntax.

## Compile-time code optimization

The factorial example above is one example of compile-time code optimization in that all factorials used by the program are pre-compiled and injected as numeric constants at compilation, saving both run-time overhead and memory footprint. It is, however, a relatively minor optimization.

As another, more significant, example of compile-time loop unrolling, template metaprogramming can be used to create length-*n* vector classes (where *n* is known at compile time). The benefit over a more traditional length-*n* vector is that the loops can be unrolled, resulting in very optimized code. As an example, consider the addition operator. A length-*n* vector addition might be written as

```mw
template <int Length>
ColumnVector<Length>& ColumnVector<Length>::operator+=(const Vector<Length>& rhs)  {
    for (int i = 0; i < Length; ++i) {
        value[i] += rhs.value[i];
    }
    return *this;
}
```

When the compiler instantiates the function template defined above, the following code may be produced:

```mw
template <>
ColumnVector<2>& ColumnVector<2>::operator+=(const ColumnVector<2>& rhs)  {
    value[0] += rhs.value[0];
    value[1] += rhs.value[1];
    return *this;
}
```

The compiler's optimizer should be able to unroll the `for` loop because the template parameter `Length` is a constant at compile time.

However, care must be taken as this may cause code bloat, since separate unrolled code will be generated for each 'N'(vector size) the template is instantiated with.

## Static polymorphism

Polymorphism is a common standard programming facility where derived objects can be used as instances of their base object but where the derived objects' methods will be invoked, as in this code

```mw
class Base {
public:
    virtual void method() { 
        std::println("Base"); 
    }

    virtual ~Base() {}
};

class Derived : public Base {
public:
    virtual void method() { 
        std::println("Derived");
    }
};

int main() {
    Base* b = new Derived;
    b->method(); // outputs "Derived"
    delete b;
    return 0;
}
```

where all invocations of `virtual` methods will be those of the most-derived class. This *dynamically polymorphic* behaviour is (typically) obtained by the creation of virtual look-up tables for classes with virtual methods, tables that are traversed at run time to identify the method to be invoked. Thus, *run-time polymorphism* necessarily entails execution overhead (though on modern architectures the overhead is small).

However, in many cases the polymorphic behaviour needed is invariant and can be determined at compile time. Then the Curiously Recurring Template Pattern (CRTP) can be used to achieve **static polymorphism**, which is an imitation of polymorphism in programming code but which is resolved at compile time and thus does away with run-time virtual-table lookups. For example:

```mw
template <typename Child>
struct Base {
    void myMethod() {
         // ...
         static_cast<Child*>(this)->myImplementation();
         // ...
    }
};

struct Derived : Base<Derived> {
     void myImplementation() {
         // ...
     }
};
```

Here the base class template will take advantage of the fact that member function bodies are not instantiated until after their declarations, and it will use members of the derived class within its own member functions, via the use of a `static_cast`, thus at compilation generating an object composition with polymorphic characteristics. As an example of real-world usage, the CRTP is used in the Boost iterator library.

Another similar use is the "Barton–Nackman trick", sometimes referred to as "restricted template expansion", where common functionality can be placed in a base class that is used not as a contract but as a necessary component to enforce conformant behaviour while minimising code redundancy.

## Static Table Generation

The benefit of static tables is the replacement of "expensive" calculations with a simple array indexing operation (for examples, see lookup table). In C++, there exists more than one way to generate a static table at compile time. The following listing shows an example of creating a very simple table by using recursive structs and variadic templates. The table has a size of ten. Each value is the square of the index.

```mw
import std;

using std::array;

constexpr int TABLE_SIZE = 10;

/**
 * Variadic template for a recursive helper struct.
 */
template <int Index = 0, int... D>
struct Helper : Helper<Index + 1, D..., Index * Index> { };

/**
 * Specialization of the template to end the recursion when the table size reaches TABLE_SIZE.
 */
template <int... D>
struct Helper<TABLE_SIZE, D...> {
    static constexpr array<int, TABLE_SIZE> TABLE = { D... };
};

constexpr array<int, TABLE_SIZE> TABLE = Helper<>::TABLE;

enum class Numbers {
    FOUR = TABLE[2] // compile time use
};

int main() {
    for (int i: TABLE) {
        std::println("{}", i); // run time use
    }
    std::println("FOUR: {}", Numbers::FOUR);
}
```

The idea behind this is that the struct Helper recursively inherits from a struct with one more template argument (in this example calculated as Index * Index) until the specialization of the template ends the recursion at a size of 10 elements. The specialization simply uses the variable argument list as elements for the array. The compiler will produce code similar to the following (taken from clang called with -Xclang -ast-print -fsyntax-only).

```mw
import std;

using std::array;

template <int Index = 0, int... D> 
struct Helper : Helper<Index + 1, D..., Index * Index> {};
template <> 
struct Helper<0, <>> : Helper<0 + 1, 0 * 0> {};
template <> 
struct Helper<1, <0>> : Helper<1 + 1, 0, 1 * 1> {};
template <> 
struct Helper<2, <0, 1>> : Helper<2 + 1, 0, 1, 2 * 2> {};
template <> 
struct Helper<3, <0, 1, 4>> : Helper<3 + 1, 0, 1, 4, 3 * 3> {};
template <> 
struct Helper<4, <0, 1, 4, 9>> : Helper<4 + 1, 0, 1, 4, 9, 4 * 4> {};
template <> 
struct Helper<5, <0, 1, 4, 9, 16>> : Helper<5 + 1, 0, 1, 4, 9, 16, 5 * 5> {};
template <> 
struct Helper<6, <0, 1, 4, 9, 16, 25>> : Helper<6 + 1, 0, 1, 4, 9, 16, 25, 6 * 6> {};
template <> 
struct Helper<7, <0, 1, 4, 9, 16, 25, 36>> : Helper<7 + 1, 0, 1, 4, 9, 16, 25, 36, 7 * 7> {};
template <> 
struct Helper<8, <0, 1, 4, 9, 16, 25, 36, 49>> : Helper<8 + 1, 0, 1, 4, 9, 16, 25, 36, 49, 8 * 8> {};
template <> 
struct Helper<9, <0, 1, 4, 9, 16, 25, 36, 49, 64>> : Helper<9 + 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 9 * 9> {};
template <> 
struct Helper<10, <0, 1, 4, 9, 16, 25, 36, 49, 64, 81>> {
    static constexpr array<int, TABLE_SIZE> TABLE = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81};
};
```

Since C++17 this can be more readably written as:

```mw
 
import std;

using std::array;

constexpr int TABLE_SIZE = 10;

constexpr array<int, TABLE_SIZE> TABLE = []() -> array<int, TABLE_SIZE> {
    array<int, TABLE_SIZE> a = {};
    for (size_t i = 0; i < TABLE_SIZE; i++) {
        a[i] = i * i;
    }
    return a;
}();

enum class Numbers {
    FOUR = TABLE[2] // compile time use
};

int main() {
    for (int i: TABLE) {
        std::println("{}", i); // run time use
    }
    std::println("FOUR: {}", Numbers::FOUR);
}
```

To show a more sophisticated example the code in the following listing has been extended to have a helper for value calculation (in preparation for more complicated computations), a table specific offset and a template argument for the type of the table values (e.g. `uint8_t`, `uint16_t`, ...).

```mw
                                                                
import std;

using std::array;

constexpr int TABLE_SIZE = 20;
constexpr int OFFSET = 12;

/**
 * Template to calculate a single table entry
 */
template <typename ValueType , ValueType Offset, ValuType Index>
struct ValueHelper {
    static constexpr ValueType VALUE = Offset + Index * Index;
};

/**
 * Variadic template for a recursive helper struct.
 */
template <typename ValueType, ValueType Offset, int N = 0, ValueType... D>
struct Helper : Helper<ValueType, Offset, N + 1, D..., ValueHelper<ValueType, Offset, N>::VALUE> { };

/**
 * Specialization of the template to end the recursion when the table size reaches TABLE_SIZE.
 */
template <typename ValueType, ValueType Offset, ValueType... D>
struct Helper<ValueType, Offset, TABLE_SIZE, D...> {
    static constexpr array<ValueType, TABLE_SIZE> TABLE = { D... };
};

constexpr array<uint16_t, TABLE_SIZE> TABLE = Helper<uint16_t, OFFSET>::TABLE;

int main() {
    for (int i: TABLE) {
        std::println("{}", i);
    }
}
```

Which could be written as follows using C++17:

```mw
import std;

using std::array;

constexpr int TABLE_SIZE = 20;
constexpr int OFFSET = 12;

template <typename ValueType, int Offset>
constexpr array<ValueType, TABLE_SIZE> TABLE = []() -> array<ValueType, TABLE_SIZE> {
    array<ValueType, TABLE_SIZE> A = {};
    for (size_t i = 0; i < TABLE_SIZE; i++) {
        a[i] = Offset + i * i;
    }
    return A;
}();

int main() {
    for (int i: TABLE<uint16_t, OFFSET>) {
        std::pritnln("{}", i);
    }
}
```

## Concepts

The C++20 standard brought C++ programmers a new tool for meta template programming, concepts.

Concepts allow programmers to specify requirements for the type, to make instantiation of template possible. The compiler looks for a template with the concept that has the highest requirements.

Here is an example of the famous Fizz buzz problem solved with Template Meta Programming.

```mw
import std;
import boost.type_index; // for pretty printing of types

using std::tuple;
using boost::typeindex::type_id;

/**
 * Type representation of words to print
 */
struct Fizz {};
struct Buzz {};
struct FizzBuzz {};
template <size_t M> 
struct Number {
    constexpr static size_t N = M; 
};

/**
 * Concepts used to define condition for specializations
 */
template <typename A> 
concept HasN = requires { 
    requires A::N - A::N == 0; 
};

template <typename A> 
concept FizzConc = HasN<A> && requires { 
    requires A::N % 3 == 0; 
};

template <typename A> 
concept BuzzConc = HasN<A> && requires { 
    requires A::N % 5 == 0;
};

template <typename A> 
concept FizzBuzzC = FizzConc<A> && BuzzConc<A>;

/**
 * By specializing `res` structure, with concepts requirements, proper instantiation is performed
 */
template <typename X> 
struct Res;

template <FizzBuzzConc X> 
struct Res<X> { 
    using Result = FizzBuzz; 
};

template <FizzConc X> 
struct Res<X> { 
    using Result = Fizz; 
};

template <BuzzConc X> 
struct Res<X> { 
    using Result = Buzz; 
};

template <HasN X> 
struct Res<X> { 
    using Result = X; 
};

/**
 * Predeclaration of concatenator
 */
template <size_t Concat, typename... Args> 
struct Concatenator;

/**
 * Recursive way of concatenating next types
 */
template <size_t Concat, typename... Args>
struct Concatenator<Concat, tuple<Args...>> { 
    using Type = typename Concatenator<Concat - 1, tuple<typename Res<Number<Concat>>::Result, Args...>>::Type;
};

/**
 * Base case
 */
template <typename... Args> 
struct Concatenator<0, tuple<Args...>> { 
    using Type = tuple<Args...>;
};

/**
 * Final result getter
 */
template <size_t Amount>
using FizzBuzzFull = typename Concatenator<Amount - 1, tuple<typename Res<Number<Amount>>::Result>>::Type;

int main(int argc, char* argv[]) {
	// printing result using boost.type_index, so it's clear
    std::println("{}", type_id<fizz_buzz_full_template<100>>().pretty_name());
}
/*
Result:
	std::tuple<Number<1ul>, Number<2ul>, Fizz, Number<4ul>, Buzz, Fizz, Number<7ul>, Number<8ul>, Fizz, Buzz, Number<11ul>, Fizz, Number<13ul>, Number<14ul>, FizzBuzz, Number<16ul>, Number<17ul>, Fizz, Number<19ul>, Buzz, Fizz, Number<22ul>, Number<23ul>, Fizz, Buzz, Number<26ul>, Fizz, Number<28ul>, Number<29ul>, FizzBuzz, Number<31ul>, Number<32ul>, Fizz, Number<34ul>, Buzz, Fizz, Number<37ul>, Number<38ul>, Fizz, Buzz, Number<41ul>, Fizz, Number<43ul>, Number<44ul>, FizzBuzz, Number<46ul>, Number<47ul>, Fizz, Number<49ul>, Buzz, Fizz, Number<52ul>, Number<53ul>, Fizz, Buzz, Number<56ul>, Fizz, Number<58ul>, Number<59ul>, FizzBuzz, Number<61ul>, Number<62ul>, Fizz, Number<64ul>, Buzz, Fizz, Number<67ul>, Number<68ul>, Fizz, Buzz, Number<71ul>, Fizz, Number<73ul>, Number<74ul>, FizzBuzz, Number<76ul>, Number<77ul>, Fizz, Number<79ul>, Buzz, Fizz, Number<82ul>, Number<83ul>, Fizz, Buzz, Number<86ul>, Fizz, Number<88ul>, Number<89ul>, FizzBuzz, Number<91ul>, Number<92ul>, Fizz, Number<94ul>, Buzz, Fizz, Number<97ul>, Number<98ul>, Fizz, Buzz>
*/
```

## Benefits and drawbacks of template metaprogramming

Compile-time versus execution-time tradeoffs get visible if a great deal of template metaprogramming is used.

- Template metaprogramming allows the programmer to focus on architecture and delegate to the compiler the generation of any implementation required by client code. Thus, template metaprogramming can accomplish truly generic code, facilitating code minimization and better maintainability.
- With respect to C++ prior to version *C++11*, the syntax and idioms of template metaprogramming were esoteric compared to conventional C++ programming, and template metaprograms could be very difficult to understand. But from C++11 onward the syntax for value computation metaprogramming becomes more and more akin to "normal" C++, with less and less readability penalty.
