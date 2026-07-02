---
title: "Types · The Julia Language (part 2/2)"
source: https://docs.julialang.org/en/v1/manual/types/
domain: julia
license: MIT
tags: julia language, julialang
fetched: 2026-07-02
part: 2/2
---

## `Type{T}` type selectors

For each type `T`, `Type{T}` is an abstract parametric type whose only instance is the object `T`. Until we discuss Parametric Methods and conversions, it is difficult to explain the utility of this construct, but in short, it allows one to specialize function behavior on specific types as *values*. This is useful for writing methods (especially parametric ones) whose behavior depends on a type that is given as an explicit argument rather than implied by the type of one of its arguments.

Since the definition is a little difficult to parse, let's look at some examples:

```julia
julia> isa(Float64, Type{Float64})
true

julia> isa(Real, Type{Float64})
false

julia> isa(Real, Type{Real})
true

julia> isa(Float64, Type{Real})
false
```

In other words, `isa(A, Type{B})` is true if and only if `A` and `B` are the same object and that object is a type.

In particular, since parametric types are invariant, we have

```julia
julia> struct TypeParamExample{T}
           x::T
       end

julia> TypeParamExample isa Type{TypeParamExample}
true

julia> TypeParamExample{Int} isa Type{TypeParamExample}
false

julia> TypeParamExample{Int} isa Type{TypeParamExample{Int}}
true
```

Without the parameter, `Type` is simply an abstract type which has all type objects as its instances:

```julia
julia> isa(Type{Float64}, Type)
true

julia> isa(Float64, Type)
true

julia> isa(Real, Type)
true
```

Any object that is not a type is not an instance of `Type`:

```julia
julia> isa(1, Type)
false

julia> isa("foo", Type)
false
```

While `Type` is part of Julia's type hierarchy like any other abstract parametric type, it is not commonly used outside method signatures except in some special cases. Another important use case for `Type` is sharpening field types which would otherwise be captured less precisely, e.g. as `DataType` in the example below where the default constructor could lead to performance problems in code relying on the precise wrapped type (similarly to abstract type parameters).

```julia
julia> struct WrapType{T}
       value::T
       end

julia> WrapType(Float64) # default constructor, note DataType
WrapType{DataType}(Float64)

julia> WrapType(::Type{T}) where T = WrapType{Type{T}}(T)
WrapType

julia> WrapType(Float64) # sharpened constructor, note more precise Type{Float64}
WrapType{Type{Float64}}(Float64)
```


## Type Aliases

Sometimes it is convenient to introduce a new name for an already expressible type. This can be done with a simple assignment statement. For example, `UInt` is aliased to either `UInt32` or `UInt64` as is appropriate for the size of pointers on the system:

```julia
# 32-bit system:
julia> UInt
UInt32

# 64-bit system:
julia> UInt
UInt64
```

This is accomplished via the following code in `base/boot.jl`:

```julia
if Int === Int64
    const UInt = UInt64
else
    const UInt = UInt32
end
```

Of course, this depends on what `Int` is aliased to – but that is predefined to be the correct type – either `Int32` or `Int64`.

(Note that unlike `Int`, `Float` does not exist as a type alias for a specific sized `AbstractFloat`. Unlike with integer registers, where the size of `Int` reflects the size of a native pointer on that machine, the floating point register sizes are specified by the IEEE-754 standard.)

Type aliases may be parametrized:

```julia
julia> const Family{T} = Set{T}
Set

julia> Family{Char} === Set{Char}
true
```


## Operations on Types

Since types in Julia are themselves objects, ordinary functions can operate on them. Some functions that are particularly useful for working with or exploring types have already been introduced, such as the `<:` operator, which indicates whether its left hand operand is a subtype of its right hand operand.

The `isa` function tests if an object is of a given type and returns true or false:

```julia
julia> isa(1, Int)
true

julia> isa(1, AbstractFloat)
false
```

The `typeof` function, already used throughout the manual in examples, returns the type of its argument. Since, as noted above, types are objects, they also have types, and we can ask what their types are:

```julia
julia> typeof(Rational{Int})
DataType

julia> typeof(Union{Real,String})
Union
```

What if we repeat the process? What is the type of a type of a type? As it happens, types are all composite values and thus all have a type of `DataType`:

```julia
julia> typeof(DataType)
DataType

julia> typeof(Union)
DataType
```

`DataType` is its own type.

Another operation that applies to some types is `supertype`, which reveals a type's supertype. Only declared types (`DataType`) have unambiguous supertypes:

```julia
julia> supertype(Float64)
AbstractFloat

julia> supertype(Number)
Any

julia> supertype(AbstractString)
Any

julia> supertype(Any)
Any
```

If you apply `supertype` to other type objects (or non-type objects), a `MethodError` is raised:

```julia
julia> supertype(Union{Float64,Int64})
ERROR: MethodError: no method matching supertype(::Type{Union{Float64, Int64}})
The function `supertype` exists, but no method is defined for this combination of argument types.

Closest candidates are:
[...]
```


## Custom pretty-printing

Often, one wants to customize how instances of a type are displayed. This is accomplished by overloading the `show` function. For example, suppose we define a type to represent complex numbers in polar form:

```julia
julia> struct Polar{T<:Real} <: Number
           r::T
           Θ::T
       end

julia> Polar(r::Real,Θ::Real) = Polar(promote(r,Θ)...)
Polar
```

Here, we've added a custom constructor function so that it can take arguments of different `Real` types and promote them to a common type (see Constructors and Conversion and Promotion). (Of course, we would have to define lots of other methods, too, to make it act like a `Number`, e.g. `+`, `*`, `one`, `zero`, promotion rules and so on.) By default, instances of this type display rather simply, with information about the type name and the field values, as e.g. `Polar{Float64}(3.0,4.0)`.

If we want it to display instead as `3.0 * exp(4.0im)`, we would define the following method to print the object to a given output object `io` (representing a file, terminal, buffer, etcetera; see Networking and Streams):

```julia
julia> Base.show(io::IO, z::Polar) = print(io, z.r, " * exp(", z.Θ, "im)")
```

More fine-grained control over display of `Polar` objects is possible. In particular, sometimes one wants both a verbose multi-line printing format, used for displaying a single object in the REPL and other interactive environments, and also a more compact single-line format used for `print` or for displaying the object as part of another object (e.g. in an array). Although by default the `show(io, z)` function is called in both cases, you can define a *different* multi-line format for displaying an object by overloading a three-argument form of `show` that takes the `text/plain` MIME type as its second argument (see Multimedia I/O), for example:

```julia
julia> Base.show(io::IO, ::MIME"text/plain", z::Polar{T}) where{T} =
           print(io, "Polar{$T} complex number:\n   ", z)
```

(Note that `print(..., z)` here will call the 2-argument `show(io, z)` method.) This results in:

```julia
julia> Polar(3, 4.0)
Polar{Float64} complex number:
   3.0 * exp(4.0im)

julia> [Polar(3, 4.0), Polar(4.0,5.3)]
2-element Vector{Polar{Float64}}:
 3.0 * exp(4.0im)
 4.0 * exp(5.3im)
```

where the single-line `show(io, z)` form is still used for an array of `Polar` values. Technically, the REPL calls `display(z)` to display the result `z` of executing a line, which defaults to `show(io, MIME("text/plain"), z)` (where `io` is an `IOContext` wrapper around `stdout`), which in turn defaults to `show(io, z)`, but you should *not* define new `display` methods unless you are defining a new multimedia display handler (see Multimedia I/O).

Moreover, you can also define `show` methods for other MIME types in order to enable richer display (HTML, images, etcetera) of objects in environments that support this (e.g. IJulia). For example, we can define formatted HTML display of `Polar` objects, with superscripts and italics, via:

```julia
julia> Base.show(io::IO, ::MIME"text/html", z::Polar{T}) where {T} =
           println(io, "<code>Polar{$T}</code> complex number: ",
                   z.r, " <i>e</i><sup>", z.Θ, " <i>i</i></sup>")
```

A `Polar` object will then display automatically using HTML in an environment that supports HTML display, but you can call `show` manually to get HTML output if you want:

```julia
julia> show(stdout, "text/html", Polar(3.0,4.0))
<code>Polar{Float64}</code> complex number: 3.0 <i>e</i><sup>4.0 <i>i</i></sup>
```

An HTML renderer would display this as: `Polar{Float64}` complex number: 3.0 *e*4.0 *i*

As a rule of thumb, the single-line `show` method should print a valid Julia expression for creating the shown object. When this `show` method contains infix operators, such as the multiplication operator (`*`) in our single-line `show` method for `Polar` above, it may not parse correctly when printed as part of another object. To see this, consider the expression object (see Program representation) which takes the square of a specific instance of our `Polar` type:

```julia
julia> a = Polar(3, 4.0)
Polar{Float64} complex number:
   3.0 * exp(4.0im)

julia> print(:($a^2))
3.0 * exp(4.0im) ^ 2
```

Because the operator `^` has higher precedence than `*` (see Operator Precedence and Associativity), this output does not faithfully represent the expression `a ^ 2` which should be equal to `(3.0 * exp(4.0im)) ^ 2`. To solve this issue, we must make a custom method for `Base.show_unquoted(io::IO, z::Polar, indent::Int, precedence::Int)`, which is called internally by the expression object when printing:

```julia
julia> function Base.show_unquoted(io::IO, z::Polar, ::Int, precedence::Int)
           if Base.operator_precedence(:*) <= precedence
               print(io, "(")
               show(io, z)
               print(io, ")")
           else
               show(io, z)
           end
       end

julia> :($a^2)
:((3.0 * exp(4.0im)) ^ 2)
```

The method defined above adds parentheses around the call to `show` when the precedence of the calling operator is higher than or equal to the precedence of multiplication. This check allows expressions which parse correctly without the parentheses (such as `:($a + 2)` and `:($a == 2)`) to omit them when printing:

```julia
julia> :($a + 2)
:(3.0 * exp(4.0im) + 2)

julia> :($a == 2)
:(3.0 * exp(4.0im) == 2)
```

In some cases, it is useful to adjust the behavior of `show` methods depending on the context. This can be achieved via the `IOContext` type, which allows passing contextual properties together with a wrapped IO stream. For example, we can build a shorter representation in our `show` method when the `:compact` property is set to `true`, falling back to the long representation if the property is `false` or absent:

```julia
julia> function Base.show(io::IO, z::Polar)
           if get(io, :compact, false)::Bool
               print(io, z.r, "ℯ", z.Θ, "im")
           else
               print(io, z.r, " * exp(", z.Θ, "im)")
           end
       end
```

This new compact representation will be used when the passed IO stream is an `IOContext` object with the `:compact` property set. In particular, this is the case when printing arrays with multiple columns (where horizontal space is limited):

```julia
julia> show(IOContext(stdout, :compact=>true), Polar(3, 4.0))
3.0ℯ4.0im

julia> [Polar(3, 4.0) Polar(4.0,5.3)]
1×2 Matrix{Polar{Float64}}:
 3.0ℯ4.0im  4.0ℯ5.3im
```

See the `IOContext` documentation for a list of common properties which can be used to adjust printing.

### Output-function summary

Here is a brief summary of the different output functions in Julia and how they are related. Most new types should only need to define `show` methods, if anything.

- `display(x)` tells the current environment to display `x` in whatever way it thinks best. (This might even be a graphical display in something like a Jupyter or Pluto notebook.) By default (e.g. in scripts or in the text REPL), it calls `show(io, "text/plain", x)`, or equivalently `show(io, MIME"text/plain"(), x)`, for an appropriate `io` stream. (In the REPL, `io` is an `IOContext` wrapper around `stdout`.) The REPL uses `display` to output the result of an evaluated expression.
- The 3-argument `show(io, ::MIME"text/plain", x)` method performs verbose pretty-printing of `x`. By default (if no 3-argument method is defined for `typeof(x)`), it calls the 2-argument `show(io, x)`. It is called by the 2-argument `repr("text/plain", x)`. Other 3-argument `show` methods can be defined for additional MIME types as discussed above, to enable richer display of `x` in some interactive environments.
- The 2-argument `show(io, x)` is the default simple text representation of `x`. It is called by the 1-argument `repr(x)`, and is typically the format you might employ to input `x` into Julia. The 1-argument `show(x)` calls `show(stdout, x)`.
- `print(io, x)` by default calls `show(io, x)`, but a few types have a distinct `print` format — most notably, when `x` is a string, `print` outputs the raw text whereas `show` outputs an escaped string enclosed in quotation marks. The 1-argument `print(x)` calls `print(stdout, x)`. `print` is also called by `string(x)`. See also `println` (to append a newline) and `printstyled` (to add colors etc.), both of which call `print`.
- `write(io, x)`, if it is defined (it generally has *no* default definition for new types), writes a "raw" binary representation of `x` to `io`, e.g. an `x::Int32` will be written as 4 bytes.

It is also helpful to be familiar with the metadata that can be attached to an `io` stream by an `IOContext` wrapper. For example, the REPL sets the `:limit => true` flag from `display` for an evaluated expression, in order to limit the output to fit in the terminal; you can query this flag with `get(io, :limit, false)`. And when displaying an object contained within, for example, a multi-column matrix, the `:compact => true` flag could be set, which you can query with `get(io, :compact, false)`.


## "Value types"

In Julia, you can't dispatch on a *value* such as `true` or `false`. However, you can dispatch on parametric types, and Julia allows you to include "plain bits" values (Types, Symbols, Integers, floating-point numbers, tuples, etc.) as type parameters. A common example is the dimensionality parameter in `Array{T,N}`, where `T` is a type (e.g., `Float64`) but `N` is just an `Int`.

You can create your own custom types that take values as parameters, and use them to control dispatch of custom types. By way of illustration of this idea, let's introduce the parametric type `Val{x}`, and its constructor `Val(x) = Val{x}()`, which serves as a customary way to exploit this technique for cases where you don't need a more elaborate hierarchy.

`Val` is defined as:

```julia
julia> struct Val{x}
       end

julia> Val(x) = Val{x}()
Val
```

There is no more to the implementation of `Val` than this. Some functions in Julia's standard library accept `Val` instances as arguments, and you can also use it to write your own functions. For example:

```julia
julia> firstlast(::Val{true}) = "First"
firstlast (generic function with 1 method)

julia> firstlast(::Val{false}) = "Last"
firstlast (generic function with 2 methods)

julia> firstlast(Val(true))
"First"

julia> firstlast(Val(false))
"Last"
```

For consistency across Julia, the call site should always pass a `Val` *instance* rather than using a *type*, i.e., use `foo(Val(:bar))` rather than `foo(Val{:bar})`.

It's worth noting that it's extremely easy to mis-use parametric "value" types, including `Val`; in unfavorable cases, you can easily end up making the performance of your code much *worse*. In particular, you would never want to write actual code as illustrated above. For more information about the proper (and improper) uses of `Val`, please read the more extensive discussion in the performance tips.

- 1"Small" is defined by the `max_union_splitting` configuration, which currently defaults to 4.
- 2A few popular languages have singleton types, including Haskell, Scala and Ruby.
