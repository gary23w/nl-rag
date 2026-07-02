---
title: "The Go Programming Language Specification (part 2/6)"
source: https://go.dev/ref/spec
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
part: 2/6
---

## Properties of types and values

### Representation of values

Values of predeclared types (see below for the interfaces `any` and `error`), arrays, and structs are self-contained: Each such value contains a complete copy of all its data, and variables of such types store the entire value. For instance, an array variable provides the storage (the variables) for all elements of the array. The respective zero values are specific to the value's types; they are never `nil`.

Non-nil pointer, function, slice, map, and channel values contain references to underlying data which may be shared by multiple values:

- A pointer value is a reference to the variable holding the pointer base type value.
- A function value contains references to the (possibly anonymous) function and enclosed variables.
- A slice value contains the slice length, capacity, and a reference to its underlying array.
- A map or channel value is a reference to the implementation-specific data structure of the map or channel.

An interface value may be self-contained or contain references to underlying data depending on the interface's dynamic type. The predeclared identifier `nil` is the zero value for types whose values can contain references.

When multiple values share underlying data, changing one value may change another. For instance, changing an element of a slice will change that element in the underlying array for all slices that share the array.

### Underlying types

Each type `T` has an *underlying type*: If `T` is one of the predeclared boolean, numeric, or string types, or a type literal, the corresponding underlying type is `T` itself. Otherwise, `T`'s underlying type is the underlying type of the type to which `T` refers in its declaration. For a type parameter that is the underlying type of its type constraint, which is always an interface.

```
type (
	A1 = string
	A2 = A1
)

type (
	B1 string
	B2 B1
	B3 []B1
	B4 B3
)

func f[P any](x P) { … }
```

The underlying type of `string`, `A1`, `A2`, `B1`, and `B2` is `string`. The underlying type of `[]B1`, `B3`, and `B4` is `[]B1`. The underlying type of `P` is `interface{}`.

### Type identity

Two types are either *identical* ("the same") or *different*.

A named type is always different from any other type. Otherwise, two types are identical if their underlying type literals are structurally equivalent; that is, they have the same literal structure and corresponding components have identical types. In detail:

- Two array types are identical if they have identical element types and the same array length.
- Two slice types are identical if they have identical element types.
- Two struct types are identical if they have the same sequence of fields, and if corresponding pairs of fields have the same names, identical types, and identical tags, and are either both embedded or both not embedded. Non-exported field names from different packages are always different.
- Two pointer types are identical if they have identical base types.
- Two function types are identical if they have the same number of parameters and result values, corresponding parameter and result types are identical, and either both functions are variadic or neither is. Parameter and result names are not required to match.
- Two interface types are identical if they define the same type set.
- Two map types are identical if they have identical key and element types.
- Two channel types are identical if they have identical element types and the same direction.
- Two instantiated types are identical if their defined types and all type arguments are identical.

Given the declarations

```
type (
	A0 = []string
	A1 = A0
	A2 = struct{ a, b int }
	A3 = int
	A4 = func(A3, float64) *A0
	A5 = func(x int, _ float64) *[]string

	B0 A0
	B1 []string
	B2 struct{ a, b int }
	B3 struct{ a, c int }
	B4 func(int, float64) *B0
	B5 func(x int, y float64) *A1

	C0 = B0
	D0[P1, P2 any] struct{ x P1; y P2 }
	E0 = D0[int, string]
)
```

these types are identical:

```
A0, A1, and []string
A2 and struct{ a, b int }
A3 and int
A4, func(int, float64) *[]string, and A5

B0 and C0
D0[int, string] and E0
[]int and []int
struct{ a, b *B5 } and struct{ a, b *B5 }
func(x int, y float64) *[]string, func(int, float64) (result *[]string), and A5
```

`B0` and `B1` are different because they are new types created by distinct type definitions; `func(int, float64) *B0` and `func(x int, y float64) *[]string` are different because `B0` is different from `[]string`; and `P1` and `P2` are different because they are different type parameters. `D0[int, string]` and `struct{ x int; y string }` are different because the former is an instantiated defined type while the latter is a type literal (but they are still assignable).

### Assignability

A value `x` of type `V` is *assignable* to a variable of type `T` ("`x` is assignable to `T`") if one of the following conditions applies:

- `V` and `T` are identical.
- `V` and `T` have identical underlying types but are not type parameters and at least one of `V` or `T` is not a named type.
- `V` and `T` are channel types with identical element types, `V` is a bidirectional channel, and at least one of `V` or `T` is not a named type.
- `T` is an interface type, but not a type parameter, and `x` implements `T`.
- `x` is the predeclared identifier `nil` and `T` is a pointer, function, slice, map, channel, or interface type, but not a type parameter.
- `x` is an untyped constant representable by a value of type `T`.

Additionally, if `x`'s type `V` or `T` are type parameters, `x` is assignable to a variable of type `T` if one of the following conditions applies:

- `x` is the predeclared identifier `nil`, `T` is a type parameter, and `x` is assignable to each type in `T`'s type set.
- `V` is not a named type, `T` is a type parameter, and `x` is assignable to each type in `T`'s type set.
- `V` is a type parameter and `T` is not a named type, and values of each type in `V`'s type set are assignable to `T`.

### Representability

A constant `x` is *representable* by a value of type `T`, where `T` is not a type parameter, if one of the following conditions applies:

- `x` is in the set of values determined by `T`.
- `T` is a floating-point type and `x` can be rounded to `T`'s precision without overflow. Rounding uses IEEE 754 round-to-even rules but with an IEEE negative zero further simplified to an unsigned zero. Note that constant values never result in an IEEE negative zero, NaN, or infinity.
- `T` is a complex type, and `x`'s components `real(x)` and `imag(x)` are representable by values of `T`'s component type (`float32` or `float64`).

If `T` is a type parameter, `x` is representable by a value of type `T` if `x` is representable by a value of each type in `T`'s type set.

```
x                   T           x is representable by a value of T because

'a'                 byte        97 is in the set of byte values
97                  rune        rune is an alias for int32, and 97 is in the set of 32-bit integers
"foo"               string      "foo" is in the set of string values
1024                int16       1024 is in the set of 16-bit integers
42.0                byte        42 is in the set of unsigned 8-bit integers
1e10                uint64      10000000000 is in the set of unsigned 64-bit integers
2.718281828459045   float32     2.718281828459045 rounds to 2.7182817 which is in the set of float32 values
-1e-1000            float64     -1e-1000 rounds to IEEE -0.0 which is further simplified to 0.0
0i                  int         0 is an integer value
(42 + 0i)           float32     42.0 (with zero imaginary part) is in the set of float32 values
```

```
x                   T           x is not representable by a value of T because

0                   bool        0 is not in the set of boolean values
'a'                 string      'a' is a rune, it is not in the set of string values
1024                byte        1024 is not in the set of unsigned 8-bit integers
-1                  uint16      -1 is not in the set of unsigned 16-bit integers
1.1                 int         1.1 is not an integer value
42i                 float32     (0 + 42i) is not in the set of float32 values
1e1000              float64     1e1000 overflows to IEEE +Inf after rounding
```

### Method sets

The *method set* of a type determines the methods that can be called on an operand of that type. Every type has a (possibly empty) method set associated with it:

- The method set of a defined type `T` consists of all methods declared with receiver type `T`.
- The method set of a pointer to a defined type `T` (where `T` is neither a pointer nor an interface) is the set of all methods declared with receiver `*T` or `T`.
- The method set of an interface type is the intersection of the method sets of each type in the interface's type set (the resulting method set is usually just the set of declared methods in the interface).

Further rules apply to structs (and pointer to structs) containing embedded fields, as described in the section on struct types. Any other type has an empty method set.

In a method set, each method must have a unique non-blank method name.


## Blocks

A *block* is a possibly empty sequence of declarations and statements within matching brace brackets.

```
Block         = "{" StatementList "}" .
StatementList = { Statement ";" } .
```

In addition to explicit blocks in the source code, there are implicit blocks:

1. The *universe block* encompasses all Go source text.
2. Each package has a *package block* containing all Go source text for that package.
3. Each file has a *file block* containing all Go source text in that file.
4. Each "if", "for", and "switch" statement is considered to be in its own implicit block.
5. Each clause in a "switch" or "select" statement acts as an implicit block.

Blocks nest and influence scoping.


## Declarations and scope

A *declaration* binds a non-blank identifier to a constant, type, type parameter, variable, function, label, or package. Every identifier in a program must be declared. No identifier may be declared twice in the same block, and no identifier may be declared in both the file and package block.

The blank identifier may be used like any other identifier in a declaration, but it does not introduce a binding and thus is not declared. In the package block, the identifier `init` may only be used for `init` function declarations, and like the blank identifier it does not introduce a new binding.

```
Declaration  = ConstDecl | TypeDecl | VarDecl .
TopLevelDecl = Declaration | FunctionDecl | MethodDecl .
```

The *scope* of a declared identifier is the extent of source text in which the identifier denotes the specified constant, type, variable, function, label, or package.

Go is lexically scoped using blocks:

1. The scope of a predeclared identifier is the universe block.
2. The scope of an identifier denoting a constant, type, variable, or function (but not method) declared at top level (outside any function) is the package block.
3. The scope of the package name of an imported package is the file block of the file containing the import declaration.
4. The scope of an identifier denoting a method receiver, function parameter, or result variable is the function body.
5. The scope of an identifier denoting a type parameter of a function or declared by a method receiver begins after the name of the function and ends at the end of the function body.
6. The scope of an identifier denoting a type parameter of a type begins after the name of the type and ends at the end of the TypeSpec.
7. The scope of a constant or variable identifier declared inside a function begins at the end of the ConstSpec or VarSpec (ShortVarDecl for short variable declarations) and ends at the end of the innermost containing block.
8. The scope of a type identifier declared inside a function begins at the identifier in the TypeSpec and ends at the end of the innermost containing block.

An identifier declared in a block may be redeclared in an inner block. While the identifier of the inner declaration is in scope, it denotes the entity declared by the inner declaration.

The package clause is not a declaration; the package name does not appear in any scope. Its purpose is to identify the files belonging to the same package and to specify the default package name for import declarations.

### Label scopes

Labels are declared by labeled statements and are used in the "break", "continue", and "goto" statements. It is illegal to define a label that is never used. In contrast to other identifiers, labels are not block scoped and do not conflict with identifiers that are not labels. The scope of a label is the body of the function in which it is declared and excludes the body of any nested function.

### Blank identifier

The *blank identifier* is represented by the underscore character `_`. It serves as an anonymous placeholder instead of a regular (non-blank) identifier and has special meaning in declarations, as an operand, and in assignment statements.

### Predeclared identifiers

The following identifiers are implicitly declared in the universe block [Go 1.18] [Go 1.21]:

```
Types:
	any bool byte comparable
	complex64 complex128 error float32 float64
	int int8 int16 int32 int64 rune string
	uint uint8 uint16 uint32 uint64 uintptr

Constants:
	true false iota

Zero value:
	nil

Functions:
	append cap clear close complex copy delete imag len
	make max min new panic print println real recover
```

### Exported identifiers

An identifier may be *exported* to permit access to it from another package. An identifier is exported if both:

1. the first character of the identifier's name is a Unicode uppercase letter (Unicode character category Lu); and
2. the identifier is declared in the package block or it is a field name or method name.

All other identifiers are not exported.

### Uniqueness of identifiers

Given a set of identifiers, an identifier is called *unique* if it is *different* from every other in the set. Two identifiers are different if they are spelled differently, or if they appear in different packages and are not exported. Otherwise, they are the same.

### Constant declarations

A constant declaration binds a list of identifiers (the names of the constants) to the values of a list of constant expressions. The number of identifiers must be equal to the number of expressions, and the *n*th identifier on the left is bound to the value of the *n*th expression on the right.

```
ConstDecl      = "const" ( ConstSpec | "(" { ConstSpec ";" } ")" ) .
ConstSpec      = IdentifierList [ [ Type ] "=" ExpressionList ] .

IdentifierList = identifier { "," identifier } .
ExpressionList = Expression { "," Expression } .
```

If the type is present, all constants take the type specified, and the expressions must be assignable to that type, which must not be a type parameter. If the type is omitted, the constants take the individual types of the corresponding expressions. If the expression values are untyped constants, the declared constants remain untyped and the constant identifiers denote the constant values. For instance, if the expression is a floating-point literal, the constant identifier denotes a floating-point constant, even if the literal's fractional part is zero.

```
const Pi float64 = 3.14159265358979323846
const zero = 0.0         // untyped floating-point constant
const (
	size int64 = 1024
	eof        = -1  // untyped integer constant
)
const a, b, c = 3, 4, "foo"  // a = 3, b = 4, c = "foo", untyped integer and string constants
const u, v float32 = 0, 3    // u = 0.0, v = 3.0
```

Within a parenthesized `const` declaration list the expression list may be omitted from any but the first ConstSpec. Such an empty list is equivalent to the textual substitution of the first preceding non-empty expression list and its type if any. Omitting the list of expressions is therefore equivalent to repeating the previous list. The number of identifiers must be equal to the number of expressions in the previous list. Together with the `iota` constant generator this mechanism permits light-weight declaration of sequential values:

```
const (
	Sunday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Partyday
	numberOfDays  // this constant is not exported
)
```

### Iota

Within a constant declaration, the predeclared identifier `iota` represents successive untyped integer constants. Its value is the index of the respective ConstSpec in that constant declaration, starting at zero. It can be used to construct a set of related constants:

```
const (
	c0 = iota  // c0 == 0
	c1 = iota  // c1 == 1
	c2 = iota  // c2 == 2
)

const (
	a = 1 << iota  // a == 1  (iota == 0)
	b = 1 << iota  // b == 2  (iota == 1)
	c = 3          // c == 3  (iota == 2, unused)
	d = 1 << iota  // d == 8  (iota == 3)
)

const (
	u         = iota * 42  // u == 0     (untyped integer constant)
	v float64 = iota * 42  // v == 42.0  (float64 constant)
	w         = iota * 42  // w == 84    (untyped integer constant)
)

const x = iota  // x == 0
const y = iota  // y == 0
```

By definition, multiple uses of `iota` in the same ConstSpec all have the same value:

```
const (
	bit0, mask0 = 1 << iota, 1<<iota - 1  // bit0 == 1, mask0 == 0  (iota == 0)
	bit1, mask1                           // bit1 == 2, mask1 == 1  (iota == 1)
	_, _                                  //                        (iota == 2, unused)
	bit3, mask3                           // bit3 == 8, mask3 == 7  (iota == 3)
)
```

This last example exploits the implicit repetition of the last non-empty expression list.

### Type declarations

A type declaration binds an identifier, the *type name*, to a type. Type declarations come in two forms: alias declarations and type definitions.

```
TypeDecl = "type" ( TypeSpec | "(" { TypeSpec ";" } ")" ) .
TypeSpec = AliasDecl | TypeDef .
```

#### Alias declarations

An alias declaration binds an identifier to the given type [Go 1.9].

```
AliasDecl = identifier [ TypeParameters ] "=" Type .
```

Within the scope of the identifier, it serves as an *alias* for the given type.

```
type (
	nodeList = []*Node  // nodeList and []*Node are identical types
	Polar    = polar    // Polar and polar denote identical types
)
```

If the alias declaration specifies type parameters [Go 1.24], the type name denotes a *generic alias*. Generic aliases must be instantiated when they are used.

```
type set[P comparable] = map[P]bool
```

In an alias declaration the given type cannot be a type parameter declared in the same declaration.

```
type A[P any] = P   // illegal: P is a type parameter declared in the declaration of A

func f[P any]() {
	type A = P  // ok: T is a type parameter declared by the enclosing function
}
```

#### Type definitions

A type definition creates a new, distinct type with the same underlying type and operations as the given type and binds an identifier, the *type name*, to it.

```
TypeDef = identifier [ TypeParameters ] Type .
```

The new type is called a *defined type*. It is different from any other type, including the type it is created from.

```
type (
	Point struct{ x, y float64 }  // Point and struct{ x, y float64 } are different types
	polar Point                   // polar and Point denote different types
)

type TreeNode struct {
	left, right *TreeNode
	value any
}

type Block interface {
	BlockSize() int
	Encrypt(src, dst []byte)
	Decrypt(src, dst []byte)
}
```

A defined type may have methods associated with it. It does not inherit any methods bound to the given type, but the method set of an interface type or of elements of a composite type remains unchanged:

```
// A Mutex is a data type with two methods, Lock and Unlock.
type Mutex struct         { /* Mutex fields */ }
func (m *Mutex) Lock()    { /* Lock implementation */ }
func (m *Mutex) Unlock()  { /* Unlock implementation */ }

// NewMutex has the same composition as Mutex but its method set is empty.
type NewMutex Mutex

// The method set of PtrMutex's underlying type *Mutex remains unchanged,
// but the method set of PtrMutex is empty.
type PtrMutex *Mutex

// The method set of *PrintableMutex contains the methods
// Lock and Unlock bound to its embedded field Mutex.
type PrintableMutex struct {
	Mutex
}

// MyBlock is an interface type that has the same method set as Block.
type MyBlock Block
```

Type definitions may be used to define different boolean, numeric, or string types and associate methods with them:

```
type TimeZone int

const (
	EST TimeZone = -(5 + iota)
	CST
	MST
	PST
)

func (tz TimeZone) String() string {
	return fmt.Sprintf("GMT%+dh", tz)
}
```

If the type definition specifies type parameters, the type name denotes a *generic type*. Generic types must be instantiated when they are used.

```
type List[T any] struct {
	next  *List[T]
	value T
}
```

In a type definition the given type cannot be a type parameter.

```
type T[P any] P    // illegal: P is a type parameter

func f[P any]() {
	type L P   // illegal: P is a type parameter declared by the enclosing function
}
```

A generic type may also have methods associated with it. In this case, the method receivers must declare the same number of type parameters as present in the generic type definition.

```
// The method Len returns the number of elements in the linked list l.
func (l *List[T]) Len() int  { … }
```

### Type parameter declarations

A type parameter list declares the *type parameters* of a generic function or type declaration. The type parameter list looks like an ordinary function parameter list except that the type parameter names must all be present and the list is enclosed in square brackets rather than parentheses [Go 1.18].

```
TypeParameters = "[" TypeParamList [ "," ] "]" .
TypeParamList  = TypeParamDecl { "," TypeParamDecl } .
TypeParamDecl  = IdentifierList TypeConstraint .
```

All non-blank names in the list must be unique. Each name declares a type parameter, which is a new and different named type that acts as a placeholder for an (as of yet) unknown type in the declaration. The type parameter is replaced with a *type argument* upon instantiation of the generic function or type.

```
[P any]
[S interface{ ~[]byte|string }]
[S ~[]E, E any]
[P Constraint[int]]
[_ any]
```

Just as each ordinary function parameter has a parameter type, each type parameter has a corresponding (meta-)type which is called its *type constraint*.

A parsing ambiguity arises when the type parameter list for a generic type declares a single type parameter `P` with a constraint `C` such that the text `P C` forms a valid expression:

```
type T[P *C] …
type T[P (C)] …
type T[P *C|Q] …
…
```

In these rare cases, the type parameter list is indistinguishable from an expression and the type declaration is parsed as an array type declaration. To resolve the ambiguity, embed the constraint in an interface or use a trailing comma:

```
type T[P interface{*C}] …
type T[P *C,] …
```

Type parameters may also be declared by the receiver specification of a method declaration associated with a generic type.

#### Type constraints

A *type constraint* is an interface that defines the set of permissible type arguments for the respective type parameter and controls the operations supported by values of that type parameter [Go 1.18].

```
TypeConstraint = TypeElem .
```

If the constraint is an interface literal of the form `interface{E}` where `E` is an embedded type element (not a method), in a type parameter list the enclosing `interface{ … }` may be omitted for convenience:

```
[T []P]                      // = [T interface{[]P}]
[T ~int]                     // = [T interface{~int}]
[T int|string]               // = [T interface{int|string}]
type Constraint ~int         // illegal: ~int is not in a type parameter list
```

The predeclared interface type `comparable` denotes the set of all non-interface types that are strictly comparable [Go 1.18].

Even though interfaces that are not type parameters are comparable, they are not strictly comparable and therefore they do not implement `comparable`. However, they satisfy `comparable`.

```
int                          // implements comparable (int is strictly comparable)
[]byte                       // does not implement comparable (slices cannot be compared)
interface{}                  // does not implement comparable (see above)
interface{ ~int | ~string }  // type parameter only: implements comparable (int, string types are strictly comparable)
interface{ comparable }      // type parameter only: implements comparable (comparable implements itself)
interface{ ~int | ~[]byte }  // type parameter only: does not implement comparable (slices are not comparable)
interface{ ~struct{ any } }  // type parameter only: does not implement comparable (field any is not strictly comparable)
```

The `comparable` interface and interfaces that (directly or indirectly) embed `comparable` may only be used as type constraints. They cannot be the types of values or variables, or components of other, non-interface types.

#### Satisfying a type constraint

A type argument `T`*satisfies* a type constraint `C` if `T` is an element of the type set defined by `C`; in other words, if `T` implements `C`. As an exception, a strictly comparable type constraint may also be satisfied by a comparable (not necessarily strictly comparable) type argument [Go 1.20]. More precisely:

A type T *satisfies* a constraint `C` if

- `T` implements `C`; or
- `C` can be written in the form `interface{ comparable; E }`, where `E` is a basic interface and `T` is comparable and implements `E`.

```
type argument      type constraint                // constraint satisfaction

int                interface{ ~int }              // satisfied: int implements interface{ ~int }
string             comparable                     // satisfied: string implements comparable (string is strictly comparable)
[]byte             comparable                     // not satisfied: slices are not comparable
any                interface{ comparable; int }   // not satisfied: any does not implement interface{ int }
any                comparable                     // satisfied: any is comparable and implements the basic interface any
struct{f any}      comparable                     // satisfied: struct{f any} is comparable and implements the basic interface any
any                interface{ comparable; m() }   // not satisfied: any does not implement the basic interface interface{ m() }
interface{ m() }   interface{ comparable; m() }   // satisfied: interface{ m() } is comparable and implements the basic interface interface{ m() }
```

Because of the exception in the constraint satisfaction rule, comparing operands of type parameter type may panic at run-time (even though comparable type parameters are always strictly comparable).

### Variable declarations

A variable declaration creates one or more variables, binds corresponding identifiers to them, and gives each a type and an initial value.

```
VarDecl = "var" ( VarSpec | "(" { VarSpec ";" } ")" ) .
VarSpec = IdentifierList ( Type [ "=" ExpressionList ] | "=" ExpressionList ) .
```

```
var i int
var U, V, W float64
var k = 0
var x, y float32 = -1, -2
var (
	i       int
	u, v, s = 2.0, 3.0, "bar"
)
var re, im = complexSqrt(-1)
var _, found = entries[name]  // map lookup; only interested in "found"
```

If a list of expressions is given, the variables are initialized with the expressions following the rules for assignment statements. Otherwise, each variable is initialized to its zero value.

If a type is present, each variable is given that type. Otherwise, each variable is given the type of the corresponding initialization value in the assignment. If that value is an untyped constant, it is first implicitly converted to its default type; if it is an untyped boolean value, it is first implicitly converted to type `bool`. The predeclared identifier `nil` cannot be used to initialize a variable with no explicit type.

```
var d = math.Sin(0.5)  // d is float64
var i = 42             // i is int
var t, ok = x.(T)      // t is T, ok is bool
var n = nil            // illegal
```

Implementation restriction: A compiler may make it illegal to declare a variable inside a function body if the variable is never used.

### Short variable declarations

A *short variable declaration* uses the syntax:

```
ShortVarDecl = IdentifierList ":=" ExpressionList .
```

It is shorthand for a regular variable declaration with initializer expressions but no types:

```
"var" IdentifierList "=" ExpressionList .
```

```
i, j := 0, 10
f := func() int { return 7 }
ch := make(chan int)
r, w, _ := os.Pipe()  // os.Pipe() returns a connected pair of Files and an error, if any
_, y, _ := coord(p)   // coord() returns three values; only interested in y coordinate
```

Unlike regular variable declarations, a short variable declaration may *redeclare* variables provided they were originally declared earlier in the same block (or the parameter lists if the block is the function body) with the same type, and at least one of the non-blank variables is new. As a consequence, redeclaration can only appear in a multi-variable short declaration. Redeclaration does not introduce a new variable; it just assigns a new value to the original. The non-blank variable names on the left side of `:=` must be unique.

```
field1, offset := nextField(str, 0)
field2, offset := nextField(str, offset)  // redeclares offset
x, y, x := 1, 2, 3                        // illegal: x repeated on left side of :=
```

Short variable declarations may appear only inside functions. In some contexts such as the initializers for "if", "for", or "switch" statements, they can be used to declare local temporary variables.

### Function declarations

A function declaration binds an identifier, the *function name*, to a function.

```
FunctionDecl = "func" FunctionName [ TypeParameters ] Signature [ FunctionBody ] .
FunctionName = identifier .
FunctionBody = Block .
```

If the function's signature declares result parameters, the function body's statement list must end in a terminating statement.

```
func IndexRune(s string, r rune) int {
	for i, c := range s {
		if c == r {
			return i
		}
	}
	// invalid: missing return statement
}
```

If the function declaration specifies type parameters, the function name denotes a *generic function*. A generic function must be instantiated before it can be called or used as a value.

```
func min[T ~int|~float64](x, y T) T {
	if x < y {
		return x
	}
	return y
}
```

A function declaration without type parameters may omit the body. Such a declaration provides the signature for a function implemented outside Go, such as an assembly routine.

```
func flushICache(begin, end uintptr)  // implemented externally
```

### Method declarations

A method is a function with a *receiver*. A method declaration binds an identifier, the *method name*, to a method, and associates the method with the receiver's *base type*.

```
MethodDecl = "func" Receiver MethodName Signature [ FunctionBody ] .
Receiver   = Parameters .
```

The receiver is specified via an extra parameter section preceding the method name. That parameter section must declare a single non-variadic parameter, the receiver. Its type must be a defined type `T` or a pointer to a defined type `T`, possibly followed by a list of type parameter names `[P1, P2, …]` enclosed in square brackets. `T` is called the receiver *base type*. A receiver base type cannot be a pointer or interface type and it must be defined in the same package as the method. The method is said to be *bound* to its receiver base type and the method name is visible only within selectors for type `T` or `*T`.

A non-blank receiver identifier must be unique in the method signature. If the receiver's value is not referenced inside the body of the method, its identifier may be omitted in the declaration. The same applies in general to parameters of functions and methods.

For a base type, the non-blank names of methods bound to it must be unique. If the base type is a struct type, the non-blank method and field names must be distinct.

Given defined type `Point` the declarations

```
func (p *Point) Length() float64 {
	return math.Sqrt(p.x * p.x + p.y * p.y)
}

func (p *Point) Scale(factor float64) {
	p.x *= factor
	p.y *= factor
}
```

bind the methods `Length` and `Scale`, with receiver type `*Point`, to the base type `Point`.

If the receiver base type is a generic type, the receiver specification must declare corresponding type parameters for the method to use. This makes the receiver type parameters available to the method. Syntactically, this type parameter declaration looks like an instantiation of the receiver base type: the type arguments must be identifiers denoting the type parameters being declared, one for each type parameter of the receiver base type. The type parameter names do not need to match their corresponding parameter names in the receiver base type definition, and all non-blank parameter names must be unique in the receiver parameter section and the method signature. The receiver type parameter constraints are implied by the receiver base type definition: corresponding type parameters have corresponding constraints.

```
type Pair[A, B any] struct {
	a A
	b B
}

func (p Pair[A, B]) Swap() Pair[B, A]  { … }  // receiver declares A, B
func (p Pair[First, _]) First() First  { … }  // receiver declares First, corresponds to A in Pair
```

If the receiver type is denoted by (a pointer to) an alias, the alias must not be generic and it must not denote an instantiated generic type, neither directly nor indirectly via another alias, and irrespective of pointer indirections.

```
type GPoint[P any] = Point
type HPoint        = *GPoint[int]
type IPair         = Pair[int, int]

func (*GPoint[P]) Draw(P)   { … }  // illegal: alias must not be generic
func (HPoint) Draw(P)       { … }  // illegal: alias must not denote instantiated type GPoint[int]
func (*IPair) Second() int  { … }  // illegal: alias must not denote instantiated type Pair[int, int]
```
