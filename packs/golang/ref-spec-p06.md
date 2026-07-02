---
title: "The Go Programming Language Specification (part 6/6)"
source: https://go.dev/ref/spec
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
part: 6/6
---

## Built-in functions

Built-in functions are predeclared. They are called like any other function but some of them accept a type instead of an expression as the first argument.

The built-in functions do not have standard Go types, so they can only appear in call expressions; they cannot be used as function values.

### Appending to and copying slices

The built-in functions `append` and `copy` assist in common slice operations. For both functions, the result is independent of whether the memory referenced by the arguments overlaps.

The variadic function `append` appends zero or more values `x` to a slice `s` of type `S` and returns the resulting slice, also of type `S`. The values `x` are passed to a parameter of type `...E` where `E` is the element type of `S` and the respective parameter passing rules apply. As a special case, `append` also accepts a slice whose type is assignable to type `[]byte` with a second argument of `string` type followed by `...`. This form appends the bytes of the string.

```
append(s S, x ...E) S  // E is the element type of S
```

If `S` is a type parameter, all types in its type set must have the same underlying slice type `[]E`.

If the capacity of `s` is not large enough to fit the additional values, `append` allocates a new, sufficiently large underlying array that fits both the existing slice elements and the additional values. Otherwise, `append` re-uses the underlying array.

```
s0 := []int{0, 0}
s1 := append(s0, 2)                // append a single element     s1 is []int{0, 0, 2}
s2 := append(s1, 3, 5, 7)          // append multiple elements    s2 is []int{0, 0, 2, 3, 5, 7}
s3 := append(s2, s0...)            // append a slice              s3 is []int{0, 0, 2, 3, 5, 7, 0, 0}
s4 := append(s3[3:6], s3[2:]...)   // append overlapping slice    s4 is []int{3, 5, 7, 2, 3, 5, 7, 0, 0}

var t []interface{}
t = append(t, 42, 3.1415, "foo")   //                             t is []interface{}{42, 3.1415, "foo"}

var b []byte
b = append(b, "bar"...)            // append string contents      b is []byte{'b', 'a', 'r' }
```

The function `copy` copies slice elements from a source `src` to a destination `dst` and returns the number of elements copied. Both arguments must have identical element type `E` and must be assignable to a slice of type `[]E`. The number of elements copied is the minimum of `len(src)` and `len(dst)`. As a special case, `copy` also accepts a destination argument assignable to type `[]byte` with a source argument of a `string` type. This form copies the bytes from the string into the byte slice.

```
copy(dst, src []T) int
copy(dst []byte, src string) int
```

If the type of one or both arguments is a type parameter, all types in their respective type sets must have the same underlying slice type `[]E`.

Examples:

```
var a = [...]int{0, 1, 2, 3, 4, 5, 6, 7}
var s = make([]int, 6)
var b = make([]byte, 5)
n1 := copy(s, a[0:])            // n1 == 6, s is []int{0, 1, 2, 3, 4, 5}
n2 := copy(s, s[2:])            // n2 == 4, s is []int{2, 3, 4, 5, 4, 5}
n3 := copy(b, "Hello, World!")  // n3 == 5, b is []byte("Hello")
```

### Clear

The built-in function `clear` takes an argument of map, slice, or type parameter type, and deletes or zeroes out all elements [Go 1.21].

```
Call        Argument type     Result

clear(m)    map[K]T           deletes all entries, resulting in an
                              empty map (len(m) == 0)

clear(s)    []T               sets all elements up to the length of
                              s to the zero value of T

clear(t)    type parameter    see below
```

If the type of the argument to `clear` is a type parameter, all types in its type set must be maps or slices, and `clear` performs the operation corresponding to the actual type argument.

If the map or slice is `nil`, `clear` is a no-op.

### Close

For a channel `ch`, the built-in function `close(ch)` records that no more values will be sent on the channel. It is an error if `ch` is a receive-only channel. Sending to or closing a closed channel causes a run-time panic. Closing the nil channel also causes a run-time panic. After calling `close`, and after any previously sent values have been received, receive operations will return the zero value for the channel's type without blocking. The multi-valued receive operation returns a received value along with an indication of whether the channel is closed.

If the type of the argument to `close` is a type parameter, all types in its type set must be channels. It is an error if any of those channels is a receive-only channel.

### Manipulating complex numbers

Three functions assemble and disassemble complex numbers. The built-in function `complex` constructs a complex value from a floating-point real and imaginary part, while `real` and `imag` extract the real and imaginary parts of a complex value.

```
complex(realPart, imaginaryPart floatT) complexT
real(complexT) floatT
imag(complexT) floatT
```

The type of the arguments and return value correspond. For `complex`, the two arguments must be of the same floating-point type and the return type is the complex type with the corresponding floating-point constituents: `complex64` for `float32` arguments, and `complex128` for `float64` arguments. If one of the arguments evaluates to an untyped constant, it is first implicitly converted to the type of the other argument. If both arguments evaluate to untyped constants, they must be non-complex numbers or their imaginary parts must be zero, and the return value of the function is an untyped complex constant.

For `real` and `imag`, the argument must be of complex type, and the return type is the corresponding floating-point type: `float32` for a `complex64` argument, and `float64` for a `complex128` argument. If the argument evaluates to an untyped constant, it must be a number, and the return value of the function is an untyped floating-point constant.

The `real` and `imag` functions together form the inverse of `complex`, so for a value `z` of a complex type `Z`, `z == Z(complex(real(z), imag(z)))`.

If the operands of these functions are all constants, the return value is a constant.

```
var a = complex(2, -2)             // complex128
const b = complex(1.0, -1.4)       // untyped complex constant 1 - 1.4i
x := float32(math.Cos(math.Pi/2))  // float32
var c64 = complex(5, -x)           // complex64
var s int = complex(1, 0)          // untyped complex constant 1 + 0i can be converted to int
_ = complex(1, 2<<s)               // illegal: 2 assumes floating-point type, cannot shift
var rl = real(c64)                 // float32
var im = imag(a)                   // float64
const c = imag(b)                  // untyped constant -1.4
_ = imag(3 << s)                   // illegal: 3 assumes complex type, cannot shift
```

Arguments of type parameter type are not permitted.

### Deletion of map elements

The built-in function `delete` removes the element with key `k` from a map `m`. The value `k` must be assignable to the key type of `m`.

```
delete(m, k)  // remove element m[k] from map m
```

If the type of `m` is a type parameter, all types in that type set must be maps, and they must all have identical key types.

If the map `m` is `nil` or the element `m[k]` does not exist, `delete` is a no-op.

### Length and capacity

The built-in functions `len` and `cap` take arguments of various types and return a result of type `int`. The implementation guarantees that the result always fits into an `int`.

```
Call      Argument type    Result

len(s)    string type      string length in bytes
          [n]T, *[n]T      array length (== n)
          []T              slice length
          map[K]T          map length (number of defined keys)
          chan T           number of elements queued in channel buffer
          type parameter   see below

cap(s)    [n]T, *[n]T      array length (== n)
          []T              slice capacity
          chan T           channel buffer capacity
          type parameter   see below
```

If the argument type is a type parameter `P`, the call `len(e)` (or `cap(e)` respectively) must be valid for each type in `P`'s type set. The result is the length (or capacity, respectively) of the argument whose type corresponds to the type argument with which `P` was instantiated.

The capacity of a slice is the number of elements for which there is space allocated in the underlying array. At any time the following relationship holds:

```
0 <= len(s) <= cap(s)
```

The length of a `nil` slice, map or channel is 0. The capacity of a `nil` slice or channel is 0.

The expression `len(s)` is constant if `s` is a string constant. The expressions `len(s)` and `cap(s)` are constants if the type of `s` is an array or pointer to an array and the expression `s` does not contain channel receives or (non-constant) function calls; in this case `s` is not evaluated. Otherwise, invocations of `len` and `cap` are not constant and `s` is evaluated.

```
const (
	c1 = imag(2i)                    // imag(2i) = 2.0 is a constant
	c2 = len([10]float64{2})         // [10]float64{2} contains no function calls
	c3 = len([10]float64{c1})        // [10]float64{c1} contains no function calls
	c4 = len([10]float64{imag(2i)})  // imag(2i) is a constant and no function call is issued
	c5 = len([10]float64{imag(z)})   // invalid: imag(z) is a (non-constant) function call
)
var z complex128
```

### Making slices, maps and channels

The built-in function `make` takes a type `T`, which must be a slice, map or channel type, or a type parameter, optionally followed by a type-specific list of expressions. It returns a value of type `T` (not `*T`). The memory is initialized as described in the section on initial values.

```
Call             Type T            Result

make(T, n)       slice             slice of type T with length n and capacity n
make(T, n, m)    slice             slice of type T with length n and capacity m

make(T)          map               map of type T
make(T, n)       map               map of type T with initial space for approximately n elements

make(T)          channel           unbuffered channel of type T
make(T, n)       channel           buffered channel of type T, buffer size n

make(T, n)       type parameter    see below
make(T, n, m)    type parameter    see below
```

If the first argument is a type parameter, all types in its type set must have the same underlying type, which must be a slice or map type, or, if there are channel types, there must only be channel types, they must all have the same element type, and the channel directions must not conflict.

Each of the size arguments `n` and `m` must be of integer type, have a type set containing only integer types, or be an untyped constant. A constant size argument must be non-negative and representable by a value of type `int`; if it is an untyped constant it is given type `int`. If both `n` and `m` are provided and are constant, then `n` must be no larger than `m`. For slices and channels, if `n` is negative or larger than `m` at run time, a run-time panic occurs.

```
s := make([]int, 10, 100)       // slice with len(s) == 10, cap(s) == 100
s := make([]int, 1e3)           // slice with len(s) == cap(s) == 1000
s := make([]int, 1<<63)         // illegal: len(s) is not representable by a value of type int
s := make([]int, 10, 0)         // illegal: len(s) > cap(s)
c := make(chan int, 10)         // channel with a buffer size of 10
m := make(map[string]int, 100)  // map with initial space for approximately 100 elements
```

Calling `make` with a map type and size hint `n` will create a map with initial space to hold `n` map elements. The precise behavior is implementation-dependent.

### Min and max

The built-in functions `min` and `max` compute the smallest—or largest, respectively—value of a fixed number of arguments of ordered types. There must be at least one argument [Go 1.21].

The same type rules as for operators apply: for ordered arguments `x` and `y`, `min(x, y)` is valid if `x + y` is valid, and the type of `min(x, y)` is the type of `x + y` (and similarly for `max`). If all arguments are constant, the result is constant.

```
var x, y int
m := min(x)                 // m == x
m := min(x, y)              // m is the smaller of x and y
m := max(x, y, 10)          // m is the larger of x and y but at least 10
c := max(1, 2.0, 10)        // c == 10.0 (floating-point kind)
f := max(0, float32(x))     // type of f is float32
var s []string
_ = min(s...)               // invalid: slice arguments are not permitted
t := max("", "foo", "bar")  // t == "foo" (string kind)
```

For numeric arguments, assuming all NaNs are equal, `min` and `max` are commutative and associative:

```
min(x, y)    == min(y, x)
min(x, y, z) == min(min(x, y), z) == min(x, min(y, z))
```

For floating-point arguments negative zero, NaN, and infinity the following rules apply:

```
   x        y    min(x, y)    max(x, y)

  -0.0    0.0         -0.0          0.0    // negative zero is smaller than (non-negative) zero
  -Inf      y         -Inf            y    // negative infinity is smaller than any other number
  +Inf      y            y         +Inf    // positive infinity is larger than any other number
   NaN      y          NaN          NaN    // if any argument is a NaN, the result is a NaN
```

For string arguments the result for `min` is the first argument with the smallest (or for `max`, largest) value, compared lexically byte-wise:

```
min(x, y)    == if x <= y then x else y
min(x, y, z) == min(min(x, y), z)
```

### Allocation

The built-in function `new` creates a new, initialized variable and returns a pointer to it. It accepts a single argument, which may be either a type or an expression.

If the argument is a type `T`, then `new(T)` allocates a variable of type `T` initialized to its zero value.

If the argument is an expression `x`, then `new(x)` allocates a variable of the type of `x` initialized to the value of `x`. If that value is an untyped constant, it is first implicitly converted to its default type; if it is an untyped boolean value, it is first implicitly converted to type bool. The predeclared identifier `nil` cannot be used as an argument to `new`.

For example, `new(int)` and `new(123)` each return a pointer to a new variable of type `int`. The value of the first variable is `0`, and the value of the second is `123`. Similarly

```
type S struct { a int; b float64 }
new(S)
```

allocates a variable of type `S`, initializes it (`a=0`, `b=0.0`), and returns a value of type `*S` containing the address of the variable.

### Handling panics

Two built-in functions, `panic` and `recover`, assist in reporting and handling run-time panics and program-defined error conditions.

```
func panic(interface{})
func recover() interface{}
```

While executing a function `F`, an explicit call to `panic` or a run-time panic terminates the execution of `F`. Any functions deferred by `F` are then executed as usual. Next, any deferred functions run by `F`'s caller are run, and so on up to any deferred by the top-level function in the executing goroutine. At that point, the program is terminated and the error condition is reported, including the value of the argument to `panic`. This termination sequence is called *panicking*.

```
panic(42)
panic("unreachable")
panic(Error("cannot parse"))
```

The `recover` function allows a program to manage behavior of a panicking goroutine. Suppose a function `G` defers a function `D` that calls `recover` and a panic occurs in a function on the same goroutine in which `G` is executing. When the running of deferred functions reaches `D`, the return value of `D`'s call to `recover` will be the value passed to the call of `panic`. If `D` returns normally, without starting a new `panic`, the panicking sequence stops. In that case, the state of functions called between `G` and the call to `panic` is discarded, and normal execution resumes. Any functions deferred by `G` before `D` are then run and `G`'s execution terminates by returning to its caller.

The return value of `recover` is `nil` when the goroutine is not panicking or `recover` was not called directly by a deferred function. Conversely, if a goroutine is panicking and `recover` was called directly by a deferred function, the return value of `recover` is guaranteed not to be `nil`. To ensure this, calling `panic` with a `nil` interface value (or an untyped `nil`) causes a run-time panic.

The `protect` function in the example below invokes the function argument `g` and protects callers from run-time panics caused by `g`.

```
func protect(g func()) {
	defer func() {
		log.Println("done")  // Println executes normally even if there is a panic
		if x := recover(); x != nil {
			log.Printf("run time panic: %v", x)
		}
	}()
	log.Println("start")
	g()
}
```

### Bootstrapping

Current implementations provide several built-in functions useful during bootstrapping. These functions are documented for completeness but are not guaranteed to stay in the language. They do not return a result.

```
Function   Behavior

print      prints all arguments; formatting of arguments is implementation-specific
println    like print but prints spaces between arguments and a newline at the end
```

Implementation restriction: `print` and `println` need not accept arbitrary argument types, but printing of boolean, numeric, and string types must be supported.


## Packages

Go programs are constructed by linking together *packages*. A package in turn is constructed from one or more source files that together declare constants, types, variables and functions belonging to the package and which are accessible in all files of the same package. Those elements may be exported and used in another package.

### Source file organization

Each source file consists of a package clause defining the package to which it belongs, followed by a possibly empty set of import declarations that declare packages whose contents it wishes to use, followed by a possibly empty set of declarations of functions, types, variables, and constants.

```
SourceFile = PackageClause ";" { ImportDecl ";" } { TopLevelDecl ";" } .
```

### Package clause

A package clause begins each source file and defines the package to which the file belongs.

```
PackageClause = "package" PackageName .
PackageName   = identifier .
```

The PackageName must not be the blank identifier.

```
package math
```

A set of files sharing the same PackageName form the implementation of a package. An implementation may require that all source files for a package inhabit the same directory.

### Import declarations

An import declaration states that the source file containing the declaration depends on functionality of the *imported* package (§Program initialization and execution) and enables access to exported identifiers of that package. The import names an identifier (PackageName) to be used for access and an ImportPath that specifies the package to be imported.

```
ImportDecl = "import" ( ImportSpec | "(" { ImportSpec ";" } ")" ) .
ImportSpec = [ "." | PackageName ] ImportPath .
ImportPath = string_lit .
```

The PackageName is used in qualified identifiers to access exported identifiers of the package within the importing source file. It is declared in the file block. If the PackageName is omitted, it defaults to the identifier specified in the package clause of the imported package. If an explicit period (`.`) appears instead of a name, all the package's exported identifiers declared in that package's package block will be declared in the importing source file's file block and must be accessed without a qualifier.

The interpretation of the ImportPath is implementation-dependent but it is typically a substring of the full file name of the compiled package and may be relative to a repository of installed packages.

Implementation restriction: A compiler may restrict ImportPaths to non-empty strings using only characters belonging to Unicode's L, M, N, P, and S general categories (the Graphic characters without spaces) and may also exclude the characters !"#$%&'()*,:;<=>?[\]^`{|} and the Unicode replacement character U+FFFD.

Consider a compiled a package containing the package clause `package math`, which exports function `Sin`, and installed the compiled package in the file identified by `"lib/math"`. This table illustrates how `Sin` is accessed in files that import the package after the various types of import declaration.

```
Import declaration          Local name of Sin

import   "lib/math"         math.Sin
import m "lib/math"         m.Sin
import . "lib/math"         Sin
```

An import declaration declares a dependency relation between the importing and imported package. It is illegal for a package to import itself, directly or indirectly, or to directly import a package without referring to any of its exported identifiers. To import a package solely for its side-effects (initialization), use the blank identifier as explicit package name:

```
import _ "lib/math"
```

### An example package

Here is a complete Go package that implements a concurrent prime sieve.

```
package main

import "fmt"

// Send the sequence 2, 3, 4, … to channel 'ch'.
func generate(ch chan<- int) {
	for i := 2; ; i++ {
		ch <- i  // Send 'i' to channel 'ch'.
	}
}

// Copy the values from channel 'src' to channel 'dst',
// removing those divisible by 'prime'.
func filter(src <-chan int, dst chan<- int, prime int) {
	for i := range src {  // Loop over values received from 'src'.
		if i%prime != 0 {
			dst <- i  // Send 'i' to channel 'dst'.
		}
	}
}

// The prime sieve: Daisy-chain filter processes together.
func sieve() {
	ch := make(chan int)  // Create a new channel.
	go generate(ch)       // Start generate() as a subprocess.
	for {
		prime := <-ch
		fmt.Print(prime, "\n")
		ch1 := make(chan int)
		go filter(ch, ch1, prime)
		ch = ch1
	}
}

func main() {
	sieve()
}
```


## Program initialization and execution

### The zero value

When storage is allocated for a variable, either through a declaration or a call of `new`, or when a new value is created, either through a composite literal or a call of `make`, and no explicit initialization is provided, the variable or value is given a default value. Each element of such a variable or value is set to the *zero value* for its type: `false` for booleans, `0` for numeric types, `""` for strings, and `nil` for pointers, functions, interfaces, slices, channels, and maps. This initialization is done recursively, so for instance each element of an array of structs will have its fields zeroed if no value is specified.

These two simple declarations are equivalent:

```
var i int
var i int = 0
```

After

```
type T struct { i int; f float64; next *T }
t := new(T)
```

the following holds:

```
t.i == 0
t.f == 0.0
t.next == nil
```

The same would also be true after

```
var t T
```

### Package initialization

Within a package, package-level variable initialization proceeds stepwise, with each step selecting the variable earliest in *declaration order* which has no dependencies on uninitialized variables.

More precisely, a package-level variable is considered *ready for initialization* if it is not yet initialized and either has no initialization expression or its initialization expression has no *dependencies* on uninitialized variables. Initialization proceeds by repeatedly initializing the next package-level variable that is earliest in declaration order and ready for initialization, until there are no variables ready for initialization.

If any variables are still uninitialized when this process ends, those variables are part of one or more initialization cycles, and the program is not valid.

Multiple variables on the left-hand side of a variable declaration initialized by single (multi-valued) expression on the right-hand side are initialized together: If any of the variables on the left-hand side is initialized, all those variables are initialized in the same step.

```
var x = a
var a, b = f() // a and b are initialized together, before x is initialized
```

For the purpose of package initialization, blank variables are treated like any other variables in declarations.

The declaration order of variables declared in multiple files is determined by the order in which the files are presented to the compiler: Variables declared in the first file are declared before any of the variables declared in the second file, and so on. To ensure reproducible initialization behavior, build systems are encouraged to present multiple files belonging to the same package in lexical file name order to a compiler.

Dependency analysis does not rely on the actual values of the variables, only on lexical *references* to them in the source, analyzed transitively. For instance, if a variable `x`'s initialization expression refers to a function whose body refers to variable `y` then `x` depends on `y`. Specifically:

- A reference to a variable or function is an identifier denoting that variable or function.
- A reference to a method `m` is a method value or method expression of the form `t.m`, where the (static) type of `t` is not an interface type, and the method `m` is in the method set of `t`. It is immaterial whether the resulting function value `t.m` is invoked.
- A variable, function, or method `x` depends on a variable `y` if `x`'s initialization expression or body (for functions and methods) contains a reference to `y` or to a function or method that depends on `y`.

For example, given the declarations

```
var (
	a = c + b  // == 9
	b = f()    // == 4
	c = f()    // == 5
	d = 3      // == 5 after initialization has finished
)

func f() int {
	d++
	return d
}
```

the initialization order is `d`, `b`, `c`, `a`. Note that the order of subexpressions in initialization expressions is irrelevant: `a = c + b` and `a = b + c` result in the same initialization order in this example.

Dependency analysis is performed per package; only references referring to variables, functions, and (non-interface) methods declared in the current package are considered. If other, hidden, data dependencies exists between variables, the initialization order between those variables is unspecified.

For instance, given the declarations

```
var x = I(T{}).ab()   // x has an undetected, hidden dependency on a and b
var _ = sideEffect()  // unrelated to x, a, or b
var a = b
var b = 42

type I interface      { ab() []int }
type T struct{}
func (T) ab() []int   { return []int{a, b} }
```

the variable `a` will be initialized after `b` but whether `x` is initialized before `b`, between `b` and `a`, or after `a`, and thus also the moment at which `sideEffect()` is called (before or after `x` is initialized) is not specified.

Variables may also be initialized using functions named `init` declared in the package block, with no arguments and no result parameters.

```
func init() { … }
```

Multiple such functions may be defined per package, even within a single source file. In the package block, the `init` identifier can be used only to declare `init` functions, yet the identifier itself is not declared. Thus `init` functions cannot be referred to from anywhere in a program.

The entire package is initialized by assigning initial values to all its package-level variables followed by calling all `init` functions in the order they appear in the source, possibly in multiple files, as presented to the compiler.

### Program initialization

The packages of a complete program are initialized stepwise, one package at a time. If a package has imports, the imported packages are initialized before initializing the package itself. If multiple packages import a package, the imported package will be initialized only once. The importing of packages, by construction, guarantees that there can be no cyclic initialization dependencies. More precisely:

Given the list of all packages, sorted by import path, in each step the first uninitialized package in the list for which all imported packages (if any) are already initialized is initialized. This step is repeated until all packages are initialized.

Package initialization—variable initialization and the invocation of `init` functions—happens in a single goroutine, sequentially, one package at a time. An `init` function may launch other goroutines, which can run concurrently with the initialization code. However, initialization always sequences the `init` functions: it will not invoke the next one until the previous one has returned.

### Program execution

A complete program is created by linking a single, unimported package called the *main package* with all the packages it imports, transitively. The main package must have package name `main` and declare a function `main` that takes no arguments and returns no value.

```
func main() { … }
```

Program execution begins by initializing the program and then invoking the function `main` in package `main`. When that function invocation returns, the program exits. It does not wait for other (non-`main`) goroutines to complete.


## Errors

The predeclared type `error` is defined as

```
type error interface {
	Error() string
}
```

It is the conventional interface for representing an error condition, with the nil value representing no error. For instance, a function to read data from a file might be defined:

```
func Read(f *File, b []byte) (n int, err error)
```


## Run-time panics

Execution errors such as attempting to index an array out of bounds trigger a *run-time panic* equivalent to a call of the built-in function `panic` with a value of the implementation-defined interface type `runtime.Error`. That type satisfies the predeclared interface type `error`. The exact error values that represent distinct run-time error conditions are unspecified.

```
package runtime

type Error interface {
	error
	// and perhaps other methods
}
```


## System considerations

### Package `unsafe`

The built-in package `unsafe`, known to the compiler and accessible through the import path `"unsafe"`, provides facilities for low-level programming including operations that violate the type system. A package using `unsafe` must be vetted manually for type safety and may not be portable. The package provides the following interface:

```
package unsafe

type ArbitraryType int  // shorthand for an arbitrary Go type; it is not a real type
type Pointer *ArbitraryType

func Alignof(variable ArbitraryType) uintptr
func Offsetof(selector ArbitraryType) uintptr
func Sizeof(variable ArbitraryType) uintptr

type IntegerType int  // shorthand for an integer type; it is not a real type
func Add(ptr Pointer, len IntegerType) Pointer
func Slice(ptr *ArbitraryType, len IntegerType) []ArbitraryType
func SliceData(slice []ArbitraryType) *ArbitraryType
func String(ptr *byte, len IntegerType) string
func StringData(str string) *byte
```

A `Pointer` is a pointer type but a `Pointer` value may not be dereferenced. Any pointer or value of underlying type `uintptr` can be converted to a type of underlying type `Pointer` and vice versa. If the respective types are type parameters, all types in their respective type sets must have the same underlying type, which must be `uintptr` and `Pointer`, respectively. The effect of converting between `Pointer` and `uintptr` is implementation-defined.

```
var f float64
bits = *(*uint64)(unsafe.Pointer(&f))

type ptr unsafe.Pointer
bits = *(*uint64)(ptr(&f))

func f[P ~*B, B any](p P) uintptr {
	return uintptr(unsafe.Pointer(p))
}

var p ptr = nil
```

The functions `Alignof` and `Sizeof` take an expression `x` of any type and return the alignment or size, respectively, of a hypothetical variable `v` as if `v` were declared via `var v = x`.

The function `Offsetof` takes a (possibly parenthesized) selector `s.f`, denoting a field `f` of the struct denoted by `s` or `*s`, and returns the field offset in bytes relative to the struct's address. If `f` is an embedded field, it must be reachable without pointer indirections through fields of the struct. For a struct `s` with field `f`:

```
uintptr(unsafe.Pointer(&s)) + unsafe.Offsetof(s.f) == uintptr(unsafe.Pointer(&s.f))
```

Computer architectures may require memory addresses to be *aligned*; that is, for addresses of a variable to be a multiple of a factor, the variable's type's *alignment*. The function `Alignof` takes an expression denoting a variable of any type and returns the alignment of the (type of the) variable in bytes. For a variable `x`:

```
uintptr(unsafe.Pointer(&x)) % unsafe.Alignof(x) == 0
```

A (variable of) type `T` has *variable size* if `T` is a type parameter, or if it is an array or struct type containing elements or fields of variable size. Otherwise the size is *constant*. Calls to `Alignof`, `Offsetof`, and `Sizeof` are compile-time constant expressions of type `uintptr` if their arguments (or the struct `s` in the selector expression `s.f` for `Offsetof`) are types of constant size.

The function `Add` adds `len` to `ptr` and returns the updated pointer `unsafe.Pointer(uintptr(ptr) + uintptr(len))` [Go 1.17]. The `len` argument must be of integer type or an untyped constant. A constant `len` argument must be representable by a value of type `int`; if it is an untyped constant it is given type `int`. The rules for valid uses of `Pointer` still apply.

The function `Slice` returns a slice whose underlying array starts at `ptr` and whose length and capacity are `len`. `Slice(ptr, len)` is equivalent to

```
(*[len]ArbitraryType)(unsafe.Pointer(ptr))[:]
```

except that, as a special case, if `ptr` is `nil` and `len` is zero, `Slice` returns `nil` [Go 1.17].

The `len` argument must be of integer type or an untyped constant. A constant `len` argument must be non-negative and representable by a value of type `int`; if it is an untyped constant it is given type `int`. At run time, if `len` is negative, or if `ptr` is `nil` and `len` is not zero, a run-time panic occurs [Go 1.17].

The function `SliceData` returns a pointer to the underlying array of the `slice` argument. If the slice's capacity `cap(slice)` is not zero, that pointer is `&slice[:1][0]`. If `slice` is `nil`, the result is `nil`. Otherwise it is a non-`nil` pointer to an unspecified memory address [Go 1.20].

The function `String` returns a `string` value whose underlying bytes start at `ptr` and whose length is `len`. The same requirements apply to the `ptr` and `len` argument as in the function `Slice`. If `len` is zero, the result is the empty string `""`. Since Go strings are immutable, the bytes passed to `String` must not be modified afterwards. [Go 1.20]

The function `StringData` returns a pointer to the underlying bytes of the `str` argument. For an empty string the return value is unspecified, and may be `nil`. Since Go strings are immutable, the bytes returned by `StringData` must not be modified [Go 1.20].

### Size and alignment guarantees

For the numeric types, the following sizes are guaranteed:

```
type                                 size in bytes

byte, uint8, int8                     1
uint16, int16                         2
uint32, int32, float32                4
uint64, int64, float64, complex64     8
complex128                           16
```

The following minimal alignment properties are guaranteed:

1. For a variable `x` of any type: `unsafe.Alignof(x)` is at least 1.
2. For a variable `x` of struct type: `unsafe.Alignof(x)` is the largest of all the values `unsafe.Alignof(x.f)` for each field `f` of `x`, but at least 1.
3. For a variable `x` of array type: `unsafe.Alignof(x)` is the same as the alignment of a variable of the array's element type.

A struct or array type has size zero if it contains no fields (or elements, respectively) that have a size greater than zero. Two distinct zero-size variables may have the same address in memory.


## Appendix

### Language versions

The Go 1 compatibility guarantee ensures that programs written to the Go 1 specification will continue to compile and run correctly, unchanged, over the lifetime of that specification. More generally, as adjustments are made and features added to the language, the compatibility guarantee ensures that a Go program that works with a specific Go language version will continue to work with any subsequent version.

For instance, the ability to use the prefix `0b` for binary integer literals was introduced with Go 1.13, indicated by [Go 1.13] in the section on integer literals. Source code containing an integer literal such as `0b1011` will be rejected if the implied or required language version used by the compiler is older than Go 1.13.

The following table describes the minimum language version required for features introduced after Go 1.

#### Go 1.9

- An alias declaration may be used to declare an alias name for a type.

#### Go 1.13

- Integer literals may use the prefixes `0b`, `0B`, `0o`, and `0O` for binary, and octal literals, respectively.
- Hexadecimal floating-point literals may be written using the prefixes `0x` and `0X`.
- The imaginary suffix `i` may be used with any (binary, decimal, hexadecimal) integer or floating-point literal, not just decimal literals.
- The digits of any number literal may be separated (grouped) using underscores `_`.
- The shift count in a shift operation may be a signed integer type.

#### Go 1.14

- Emdedding a method more than once through different embedded interfaces is not an error.

#### Go 1.17

- A slice may be converted to an array pointer if the slice and array element types match, and the array is not longer than the slice.
- The built-in package `unsafe` includes the new functions `Add` and `Slice`.

#### Go 1.18

The 1.18 release adds polymorphic functions and types ("generics") to the language. Specifically:

- The set of operators and punctuation includes the new token `~`.
- Function and type declarations may declare type parameters.
- Interface types may embed arbitrary types (not just type names of interfaces) as well as union and `~T` type elements.
- The set of predeclared types includes the new types `any` and `comparable`.

#### Go 1.20

- A slice may be converted to an array if the slice and array element types match and the array is not longer than the slice.
- The built-in package `unsafe` includes the new functions `SliceData`, `String`, and `StringData`.
- Comparable types (such as ordinary interfaces) may satisfy `comparable` constraints, even if the type arguments are not strictly comparable.

#### Go 1.21

- The set of predeclared functions includes the new functions `min`, `max`, and `clear`.
- Type inference uses the types of interface methods for inference. It also infers type arguments for generic functions assigned to variables or passed as arguments to other (possibly generic) functions.

#### Go 1.22

- In a "for" statement, each iteration has its own set of iteration variables rather than sharing the same variables in each iteration.
- A "for" statement with "range" clause may iterate over integer values from zero to an upper limit.

#### Go 1.23

- A "for" statement with "range" clause accepts an iterator function as range expression.

#### Go 1.24

- An alias declaration may declare type parameters.

### Type unification rules

The type unification rules describe if and how two types unify. The precise details are relevant for Go implementations, affect the specifics of error messages (such as whether a compiler reports a type inference or other error), and may explain why type inference fails in unusual code situations. But by and large these rules can be ignored when writing Go code: type inference is designed to mostly "work as expected", and the unification rules are fine-tuned accordingly.

Type unification is controlled by a *matching mode*, which may be *exact* or *loose*. As unification recursively descends a composite type structure, the matching mode used for elements of the type, the *element matching mode*, remains the same as the matching mode except when two types are unified for assignability (`≡A`): in this case, the matching mode is *loose* at the top level but then changes to *exact* for element types, reflecting the fact that types don't have to be identical to be assignable.

Two types that are not bound type parameters unify exactly if any of following conditions is true:

- Both types are identical.
- Both types have identical structure and their element types unify exactly.
- Exactly one type is an unbound type parameter, and all the types in its type set unify with the other type per the unification rules for `≡A` (loose unification at the top level and exact unification for element types).

If both types are bound type parameters, they unify per the given matching modes if:

- Both type parameters are identical.
- At most one of the type parameters has a known type argument. In this case, the type parameters are *joined*: they both stand for the same type argument. If neither type parameter has a known type argument yet, a future type argument inferred for one the type parameters is simultaneously inferred for both of them.
- Both type parameters have a known type argument and the type arguments unify per the given matching modes.

A single bound type parameter `P` and another type `T` unify per the given matching modes if:

- `P` doesn't have a known type argument. In this case, `T` is inferred as the type argument for `P`.
- `P` does have a known type argument `A`, `A` and `T` unify per the given matching modes, and one of the following conditions is true:
  - Both `A` and `T` are interface types: In this case, if both `A` and `T` are also defined types, they must be identical. Otherwise, if neither of them is a defined type, they must have the same number of methods (unification of `A` and `T` already established that the methods match).
  - Neither `A` nor `T` are interface types: In this case, if `T` is a defined type, `T` replaces `A` as the inferred type argument for `P`.

Finally, two types that are not bound type parameters unify loosely (and per the element matching mode) if:

- Both types unify exactly.
- One type is a defined type, the other type is a type literal, but not an interface, and their underlying types unify per the element matching mode.
- Both types are interfaces (but not type parameters) with identical type terms, both or neither embed the predeclared type comparable, corresponding method types unify exactly, and the method set of one of the interfaces is a subset of the method set of the other interface.
- Only one type is an interface (but not a type parameter), corresponding methods of the two types unify per the element matching mode, and the method set of the interface is a subset of the method set of the other type.
- Both types have the same structure and their element types unify per the element matching mode.
