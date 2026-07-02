---
title: "Fixed-point combinator"
source: https://en.wikipedia.org/wiki/Fixed-point_combinator
domain: graph-reduction
license: CC-BY-SA-4.0
tags: graph reduction, combinator graph reduction, spineless tagless G-machine, supercombinator compilation
fetched: 2026-07-02
---

# Fixed-point combinator

In combinatory logic for computer science, a **fixed-point combinator** (or **fixpoint combinator**) is a higher-order function (i.e., a function that takes a function as argument) that returns some *fixed point* (a value that is mapped to itself) of its argument function, if one exists.

Formally, if $\mathrm {fix}$ is a fixed-point combinator and the function f has one or more fixed points, then $\mathrm {fix} \ f$ is one of these fixed points, i.e.,

$\mathrm {fix} \ f\ =f\ (\mathrm {fix} \ f).$

Fixed-point combinators can be defined in the lambda calculus and in functional programming languages, and provide a means to allow for recursive definitions.

## Introduction

Applied to a non-constant function of one variable that treats its argument as a piece of data (such as e.g. the sine function), the Y combinator usually does not terminate. Y really is meant to be used with codata, e.g. a colist constructor that places the first element there and expects "the rest of elements" as an argument, that will be fleshed out later; or a higher-order function that expects to be supplied as its first argument with a function "to compute the rest," which it might or might not call, as needed.

Applied to such "one step functional," Y arranges for the creation of that "rest of computation" function, consisting of that same step it was given and the "rest of computation" again, which really means just the original step repeated as many times as needed, calling "the rest" function as and if needed, but not always. The resulting function behaves like a *while* or a *for* loop. Used in this way, the Y combinator implements general recursion.

The lambda calculus does not have global names, for a function to refer to itself by name inside its own definition, as is possible in many programming languages. But it has local names, i.e. parameters in lambda abstractions. An abstraction term can receive another term as an argument, and refer to that argument by the parameter name inside the function's body.

The Y combinator may also be used in implementing Curry's paradox. The heart of Curry's paradox is that untyped lambda calculus is unsound as a deductive system, and the Y combinator demonstrates this by allowing an anonymous expression to represent zero, or even many values. This is inconsistent in mathematical logic.

### Y combinator in lambda calculus

In the classical untyped lambda calculus, every function has a fixed point. A particular implementation of $\mathrm {fix}$ is Haskell Curry's paradoxical combinator Y, given by

$\mathrm {Y} =\lambda f.\ (\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$

(Here using the standard notations and conventions of lambda calculus: Y is a function that takes one argument *f* and returns the entire expression following the first period; the expression $\lambda x.f\ (x\ x)$ denotes a function that takes one argument *x*, thought of as a function, and returns the expression $f\ (x\ x)$ , where $(x\ x)$ denotes *x* applied to itself. Juxtaposition of expressions denotes function application, is left-associative, and has higher precedence than the period.)

### Verification

The following calculation verifies that $\mathrm {Y} g$ is indeed a fixed point of the function g :

| $\mathrm {Y} \ g\$ | $\triangleq (\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x)))\ g\ \ \$ | by the definition of $\mathrm {Y}$ |
|---|---|---|
|   | $=_{_{\beta }}(\lambda x.g\ (x\ x))\ (\lambda x.g\ (x\ x))\$ | by β-reduction: replacing the formal argument *f* of Y with the actual argument *g* |
|   | $=_{_{\beta }}g\ ((\lambda x.g\ (x\ x))\ (\lambda x.g\ (x\ x)))\$ | by β-reduction: replacing the formal argument *x* of the first function with the actual argument $(\lambda x.g\ (x\ x))$ |
|   | $\equiv g\ (\mathrm {Y} \ g)$ | by second equality, above |

The lambda term $g\ (\mathrm {Y} \ g)$ may not, in general, β-reduce to the term $\mathrm {Y} \ g$ . However, both terms β-reduce to the same term, as shown.

### Example implementations

An example implementation of Y in the language R is presented below:

```mw
Y <- \(f) {
  g <- \(x) f(x(x))
  g(g)
}
```

This can then be used to implement factorial as follows:

```mw
fact <- \(f) \(n)
  if (n == 0) 1 else n * f(n - 1)
  
Y(fact)(5) # yields 5! = 120
```

Y is only needed when function names are absent. Substituting all the definitions into one line so that function names are not required gives:

```mw
(\(f) (\(x) f(x(x)))(\(x) f(x(x)))) (\(f) \(n) if (n == 0) 1 else n * f(n - 1)) (5)
```

This works because R uses lazy evaluation.

Languages that use strict evaluation, such as Python, C++, and other strict programming languages, can often express Y; however, any implementation is useless in practice since it loops indefinitely until terminating via a stack overflow.

## Fixed-point combinator

The Y combinator is an implementation of a fixed-point combinator in lambda calculus. Fixed-point combinators may also be easily defined in other functional and imperative languages. The implementation in lambda calculus is more difficult due to limitations in lambda calculus. The fixed-point combinator may be used in a number of different areas:

- General mathematics
- Untyped lambda calculus
- Typed lambda calculus
- Functional programming
- Imperative programming

Fixed-point combinators may be applied to a range of different functions, but normally will not terminate unless there is an extra parameter. When the function to be fixed refers to its parameter, another call to the function is invoked, so the calculation never gets started. Instead, the extra parameter is used to trigger the start of the calculation.

The type of the fixed point is the return type of the function being fixed. This may be a real or a function or any other type.

In the untyped lambda calculus, the function to apply the fixed-point combinator to may be expressed using an encoding, like Church encoding. In this case particular lambda terms (which define functions) are considered as values. "Running" (beta reducing) the fixed-point combinator on the encoding gives a lambda term for the result, which may then be interpreted as fixed-point value.

Alternately, a function may be considered as a lambda term defined purely in lambda calculus.

These different approaches affect how a mathematician and a programmer may regard a fixed-point combinator. A mathematician may see the Y combinator applied to a function as being an expression satisfying the fixed-point equation, and therefore a solution.

In contrast, a person only wanting to apply a fixed-point combinator to some general programming task may see it only as a means of implementing recursion.

### Values and domains

Many functions do not have any fixed points, for instance $f:\mathbb {N} \to \mathbb {N}$ with $f(n)=n+1$ . Using Church encoding, natural numbers can be represented in lambda calculus, and this function *f* can be defined in lambda calculus. However, its domain will now contain *all* lambda expressions, not just those representing natural numbers. The Y combinator, applied to *f*, will yield a fixed-point for *f*, but this fixed-point won't represent a natural number. If trying to compute Y *f* in an actual programming language, an infinite loop will occur.

### Function versus implementation

The fixed-point combinator may be defined in mathematics and then implemented in other languages. General mathematics defines a function based on its extensional properties. That is, two functions are equal if they perform the same mapping. Lambda calculus and programming languages regard function identity as an intensional property. A function's identity is based on its implementation.

A lambda calculus function (or term) is an implementation of a mathematical function. In the lambda calculus there are a number of combinators (implementations) that satisfy the mathematical definition of a fixed-point combinator.

### Definition of the term "combinator"

Combinatory logic is a higher-order functions theory. A combinator is a *closed* lambda expression, meaning that it has no free variables. The combinators may be combined to direct values to their correct places in the expression without ever naming them as variables.

## Recursive definitions and fixed-point combinators

Fixed-point combinators can be used to implement recursive definition of functions. However, they are rarely used in practical programming. Strongly normalizing type systems such as the simply typed lambda calculus disallow non-termination and hence fixed-point combinators often cannot be assigned a type or require complex type system features. Furthermore, fixed-point combinators are often inefficient compared to other strategies for implementing recursion, as they require more function reductions and construct and take apart a tuple for each group of mutually recursive definitions.

### The factorial function

The factorial function provides a good example of how a fixed-point combinator may be used to define recursive functions. The standard recursive definition of the factorial function in mathematics can be written as

$\operatorname {fact} \ n={\begin{cases}1&{\text{if}}~n=0\\n\times \operatorname {fact} (n-1)&{\text{otherwise.}}\end{cases}}$

where *n* is a non-negative integer.

This poses a problem, though, as $\operatorname {fact}$ inside the definition of $\operatorname {fact}$ cannot possibly signify the inclusion of the definition as a whole inside itself. Instead, as it normally goes almost unnoticed, it is the reference to the definition by its *name*. This presupposes the existence of a global registry of names, so called "environment". And the lambda calculus lacks this entirely.

Still, name references do exist in lambda calculus – local names, names of parameters of a given function. And thus the above can be re-written as

${\begin{aligned}&\operatorname {fact} (n)=\operatorname {f} (\operatorname {f} ,n)\\&\quad {\text{where}}\\&\quad \operatorname {f} (s,n)={\begin{cases}1&{\text{if}}~n=0\\n\times s(s,n-1)&{\text{otherwise}}\end{cases}}\end{aligned}}$

Splitting off a separate copy of $\operatorname {f}$ and passing it as an argument to itself makes it available to itself to be called, as and if needed, inside itself. In such a call it must again be passed along as an argument so it will be available to the next invocation, and so on, as the chain of invocations progresses. The definition of $\operatorname {f}$ is *open recursive*, and calling $\operatorname {f}$ with itself as an argument at the top closes the circle.

Implementing this in lambda calculus is now trivial, and directly leads to the definition of the Y combinator, one instance of a fixed-point combinator, such that $\operatorname {fix} f=f\,(\operatorname {fix} f)$ . Or directly, define a function *F* of two arguments *f* and *n*:

$F\ f\ n=(\operatorname {IsZero} \ n)\ 1\ (\operatorname {multiply} \ n\ (f\ (\operatorname {pred} \ n)))$

(Here $(\operatorname {IsZero} \ n)$ is a function that takes two arguments and returns its first argument if *n*=0, and its second argument otherwise; $\operatorname {pred} \ n$ evaluates to *n*–1.)

Now define $\operatorname {fact} ={\textsf {fix}}\ F=F\ ({\textsf {fix}}\ F)$ . Then $\operatorname {fact}$ is a fixed-point of *F*, which gives

${\begin{aligned}\operatorname {fact} n&=F\ \operatorname {fact} \ n\\&=(\operatorname {IsZero} \ n)\ 1\ (\operatorname {multiply} \ n\ (\operatorname {fact} \ (\operatorname {pred} \ n)))\ \end{aligned}}$

as desired.

## Fixed-point combinators in lambda calculus

The Y combinator, discovered by Haskell Curry, is defined as

$Y=\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$

### Other fixed-point combinators

In untyped lambda calculus fixed-point combinators are not especially rare. In fact there are infinitely many of them. In 2005 Mayer Goldberg showed that the set of fixed-point combinators of untyped lambda calculus is recursively enumerable.

The Y combinator can be expressed in the SKI-calculus as

${\mathsf {Y=S(K(SII))(S(S(KS)K)(K(SII)))=SS(S(S(KS)K))(K(SII))}}$

Additional combinators (B, C, K, W system) allow for much shorter encodings. With ${\mathsf {U=SII}}$ the self-application combinator, since ${\mathsf {S}}({\mathsf {K}}x)yz=x(yz)={\mathsf {B}}xyz$ and ${\mathsf {S}}x({\mathsf {K}}y)z=xzy={\mathsf {C}}xyz$ , the above becomes

${\mathsf {Y=S(KU)(SB(KU))=BU(CBU)}}\ \ \ ;\ \ {\mathsf {Y=SSI(BWB)}}$

The shortest fixed-point combinator in the SK-calculus using S and K combinators only, found by John Tromp, is

${\mathsf {Y'=SSK(S(K(SS(S(SSK))))K)=WC(SB(C(WC)))}}$

although note that it is not in normal form, which is longer. This combinator corresponds to the lambda expression

${\mathsf {Y}}'=(\lambda xy.xyx)(\lambda yx.y(xyx))$

The following fixed-point combinator is simpler than the Y combinator, and β-reduces into the Y combinator; it is sometimes cited as the Y combinator itself:

${\mathsf {X}}=\lambda f.(\lambda x.xx)(\lambda x.f(xx))\ \ \ ;\ \ {\mathsf {Xf=U(BfU)}}$

Another common fixed-point combinator is the Turing fixed-point combinator (named after its discoverer, Alan Turing):

$\Theta =(\lambda xy.y(xxy))\ (\lambda xy.y(xxy))={\mathsf {SII(S(K(SI))(SII))=U(B(SI)U)}}$

Its advantage over ${\mathsf {Y}}$ is that $\Theta \ f$ beta-reduces to $f\ (\Theta f)$ , whereas ${\mathsf {Y}}\ f$ and $f\ ({\mathsf {Y}}f)$ only beta-reduce to a common term.

$\Theta$ also has a simple call-by-value form:

$\Theta _{v}=(\lambda xy.y(\lambda z.xxyz))\ (\lambda xy.y(\lambda z.xxyz))$

The analog for mutual recursion is a *polyvariadic fix-point combinator*, which may be denoted Y*.

### Strict fixed-point combinator

In a strict programming language the Y combinator will expand until stack overflow, or never halt in case of tail call optimization. The Z combinator will work in strict languages (also called eager languages, where applicative evaluation order is applied). The Z combinator has the next argument defined explicitly, preventing the expansion of $Zg$ in the right-hand side of the definition:

$Zgv=g(Zg)v\ .$

and in lambda calculus it is an eta-expansion of the Y combinator:

$Z=\lambda f.(\lambda x.f(\lambda v.xxv))\ (\lambda x.f(\lambda v.xxv))\ .$

### Non-standard fixed-point combinators

If F is a fixed-point combinator in untyped lambda calculus, then there is:

${\mathsf {F}}=\lambda x.Fx=\lambda x.x(Fx)=\lambda x.x(x(Fx))=\cdots$

Terms that have the same Böhm tree as a fixed-point combinator, i.e., have the same infinite extension $\lambda x.x(x(x\cdots ))$ , are called *non-standard fixed-point combinators*. Any fixed-point combinator is also a non-standard one, but not all non-standard fixed-point combinators are fixed-point combinators because some of them fail to satisfy the fixed-point equation that defines the "standard" ones. These combinators are called *strictly non-standard fixed-point combinators*; an example is the following combinator:

${\mathsf {N=BU(B(BU)B)}}$

where

${\mathsf {B}}=\lambda xyz.x(yz)$

${\mathsf {U}}=\lambda x.xx\$

since

${\mathsf {N}}=\lambda x.Nx=\lambda x.x(N_{2}x)=\lambda x.x(x(x(N_{3}x)))=\lambda x.x(x(x(x(x(x(N_{4}x))))))=\cdots$

where ${\mathsf {N}}_{i}$ are modifications of ${\mathsf {N}}$ created on the fly which add i instances of x at once into the chain while being replaced with ${\mathsf {N}}_{i+1}$ .

The set of non-standard fixed-point combinators is not recursively enumerable.

## Implementation in other languages

The Y combinator is a particular implementation of a fixed-point combinator in lambda calculus. Its structure is determined by the limitations of lambda calculus. It is not necessary or helpful to use this structure in implementing the fixed-point combinator in other languages.

Simple examples of fixed-point combinators implemented in some programming paradigms are given below.

### Lazy functional implementation

In a language that supports lazy evaluation, as in Haskell, it is possible to define a fixed-point combinator using the defining equation of the fixed-point combinator which is conventionally named `fix`. Since Haskell has lazy data types, this combinator can also be used to define fixed points of data constructors (and not only to implement recursive functions). The definition is given here, followed by some usage examples. In Hackage, the original sample is:

```mw
fix, fix' :: (a -> a) -> a
fix f = let x = f x in x         -- Lambda dropped. Sharing.
                                 -- Original definition in Data.Function.
-- alternative:
fix' f = f (fix' f)              -- Lambda lifted. Non-sharing.

fix (\x -> 9)                    -- this evaluates to 9

fix (\x -> 3:x)                  -- evaluates to the lazy infinite list [3,3,3,...]

fact = fix fac                   -- evaluates to the factorial function
  where fac f 0 = 1
        fac f x = x * f (x-1)

fact 5                           -- evaluates to 120
```

### Strict functional implementation

In a strict functional language, as illustrated below with OCaml, the argument to *f* is expanded beforehand, yielding an infinite call sequence,

$f\ (f...(f\ ({\mathsf {fix}}\ f))...)\ x$

.

This may be resolved by defining fix with an extra parameter.

```mw
let rec fix f x = f (fix f) x (* note the extra x; hence fix f = \x-> f (fix f) x *)

let factabs fact = function   (* factabs has extra level of lambda abstraction *)
   0 -> 1
 | x -> x * fact (x-1)

let _ = (fix factabs) 5       (* evaluates to "120" *)
```

In a multi-paradigm functional language (one decorated with imperative features), such as Lisp, Peter Landin suggested the use of a variable assignment to create a fixed-point combinator, as in the below example using Scheme:

```mw
(define Y!
  (lambda (f)
    ((lambda (g)                       
       (set! g (f (lambda (x) (g x)))) ;; (set! g expr) assigns g the value of expr,
       g)                              ;; replacing g's initial value of #f, creating 
     #f)))                             ;; thus the truly self-referential value in g
```

Using a lambda calculus with axioms for assignment statements, it can be shown that `Y!` satisfies the same fixed-point law as the call-by-value Y combinator:

$(Y_{!}\ \lambda x.e)e'=(\lambda x.e)\ (Y_{!}\ \lambda x.e)e'$

In more idiomatic modern Scheme usage, this would typically be handled via a `letrec` expression, as lexical scope was introduced to Lisp in the 1970s:

```mw
(define Y*
  (lambda (f)
    (letrec                           ;; (letrec ((g expr)) ...) locally defines g 
         ((g                          ;; as expr recursively: g in expr refers to 
            (f (lambda (x) (g x)))))  ;; that same g being defined, g = f (λx. g x)
	   g)))                           ;; ((Y* f) ...) = (g ...) = ((f (λx. g x)) ...)
```

Or without the internal label:

```mw
(define Y*
  (lambda (f)
    ((lambda (i) (i i))
     (lambda (i)
       (f (lambda x
	        (apply (i i) x)))))))
```

### Imperative language implementation

This example is a slightly interpretive implementation of a fixed-point combinator. A class is used to contain the `fix()` function, called `FixedPointCombinator`. The function to be fixed is contained in a class that inherits from fixer. The `fix()` function accesses the function to be fixed using a concept to call `apply()`. As for the strict functional definition, `fix()` is explicitly given an extra parameter `x`, which means that lazy evaluation is not needed.

```mw
using std::same_as;

template <typename Ret, typename Arg, typename T>
concept FixedPointApplicable = requires (Arg x) {
    { T::apply(x) } -> same_as<Ret>;
};

template <typename Ret, typename Arg, FixedPointApplicable<Ret, Arg> Derived>
class FixedPointCombinator {
public:
    static Ret fix(Arg x) noexcept {
        return Derived::apply(x);
    }
};

class Factorial : public FixedPointCombinator<long, long, Factorial> {
    static long apply(long x) noexcept {
        if (x == 0) {
            return 1;
        }
        return x * fix(x - 1);
    }
};

long result = Factorial::fix(5);
```

Using only lambdas, one can create a fixed-point combinator like so:

```mw
auto fix = [](auto f) {
    return [f](auto&&... args) -> decltype(auto) {
        return f(f, std::forward<decltype(args)>(args)...);
    };
};

auto factorial = fix([](auto self, long n) -> long {
    return n == 0 ? 1 : n * self(self, n - 1);
});

std::println("5! = {}", factorial(5)); // prints 120
```

Another example can be shown to demonstrate SKI combinator calculus (with given bird name from combinatory logic) being used to build up Z combinator to achieve tail call-like behavior through trampolining:

```mw
// Combinators
const K = <A, B>(a: A) => (_b: B) => a; // Kestrel
const S = <A, B, C>(a: (x: C) => (y: B) => A) => (b: (x: C) => B) => (c: C) => a(c)(b(c)); // Starling

// Derived combinators
const I = S(K)(K); // Identity
const B = S(K(S))(K); // Bluebird
const C = S(B(B)(S))(K(K)); // Cardinal
const W = C(S)(I); // Warbler
const T = C(I); // Thrush
const V = B(C)(T); // Vireo
const I1 = C(C(I)); // Identity Bird Once Removed; same as C(B(B)(I))(I)
const C1 = B(C); // Cardinal Once Removed
const R1 = C1(C1); // Robin Once Removed
const V1 = B(R1)(C1); // Vireo Once Removed
const I2 = R1(V); // Identity Bird Twice Removed

// Z combinators
const Z = B(W(I1))(V1(B)(W(I2)));

const Z2 = S(K(S(S(K(S(S(K)(K))(S(K)(K))))(S(K(S(K(S))(K)))(S(K(S(S(K)(K))))(K))))(K(S(S(K))))))(S(S(K(S(S(K(S(K(S))(K)))(S))(K(K))))(S(K(S(S(K(S(K(S))(K)))(S))(K(K))))(S(K(S))(K))))(K(S(S(K(S(S(K)(K))(S(K)(K))))(S(K(S(K(S))(K)))(S(K(S(S(K)(K))))(K))))(K(S(K(S(S(K(S(S(K(S(K(S))(K)))(S))(K(K))))(S(K(S(S(K(S(K(S))(K)))(S))(K(K))))(S(K(S(S(K)(K))))(K))))))(K))))));
	// Alternative fully expanded form.

const Z3 = S(S(K(S(S)(K(S(S(K)(K))(S(K)(K))))))(K))(S(S(K(S))(K))(K(S(S(K(S))(S(K(S(K(S(K(S(K(S(S)(K(K))))(K)))(S)))(S(S(K)(K)))))(K)))(K(K(S(S(K)(K))(S(K)(K))))))));
	// Another shorter version.

const trampoline = <T>(fn: T | (() => T)): T => {
	let ctx = fn;
	while (typeof ctx === "function") {
		ctx = (ctx as () => T)();
    }
	return ctx;
};

const countFn = (self: (n: number) => any) => (n: number): any =>
	n === 0
		? (console.log(n), n)
		: () => self(n - 1); // Return thunk "() => self(n - 1)" instead.

// Examples
trampoline(Z(countFn)(10));
trampoline(Z2(countFn)(10));
trampoline(Z3(countFn)(10));
```

## Typing

In System F (polymorphic lambda calculus) a polymorphic fixed-point combinator has type

∀a.(a → a) → a

where a is a type variable. That is, if the type of $\mathrm {fix} \ f$ fulfilling the equation $\mathrm {fix} \ f\ =\ f\ (\mathrm {fix} \ f)$ is a —the most general type—then the type of f is $a\to a$ . So then, $\mathrm {fix}$ takes a function that maps a to a and uses it to return a value of type a .

In the simply typed lambda calculus extended with recursive data types, fixed-point operators can be written, but the type of a "useful" fixed-point operator (one whose application always returns) may be restricted.

In the simply typed lambda calculus, the fixed-point combinator Y cannot be assigned a type because at some point it would deal with the self-application sub-term $x~x$ by the application rule:

${\Gamma \vdash x\!:\!t_{1}\to t_{2}\quad \Gamma \vdash x\!:\!t_{1}} \over {\Gamma \vdash x~x\!:\!t_{2}}$

where x has the infinite type $t_{1}=t_{1}\to t_{2}$ . No fixed-point combinator can in fact be typed; in those systems, any support for recursion must be explicitly added to the language.

### Type for the Y combinator

In programming languages that support named recursive data types, the unbounded recursion in $t:=t\to a$ , which creates the would-be infinite type t , is broken by naming the type t explicitly, as e.g. type $R\ a$ which is defined so as to be isomorphic to (or just to be a synonym of) the type $R\ a\to a$ . Thus $R\ a:=R\ a\to a$ is recognized as a recursive type. A datum (value) of the type $R\ a$ is created by simply tagging a value that is a function that has the type $R\ a\to a$ , by the data constructor tag for the type $R\ a$ .

For example, in the following Haskell code, let `Rec` be that tag name, and thus `Rec` and `app` be the names of the two directions of the isomorphism, with types:

```mw
Rec :: (R a -> a) -> R a
app :: R a -> (R a -> a)
```

(where $::$ means "has type"). This lets us write:

```mw
newtype R a = Rec { app :: R a -> a }
-- app (Rec g) = g    -- g :: R a -> a
--      Rec g      :: R a
-- app             :: R a -> (R a -> a)

y :: (a -> a) -> a
y f = (\ x -> f (app x x)) (Rec (\ x -> f (app x x)))
--       x :: R a
--   app x :: R a -> a
-- app x x ::        a
```

The usual lambda-calculus definition $\operatorname {Y} f=\operatorname {U} (\lambda x.f\ (\operatorname {U} x))$ (where $\operatorname {U} x=x\ x$ , and thus the term $\operatorname {U} (\lambda x.f\ (\operatorname {U} x))$ witnesses the equivalence $x\ x=f\ (x\ x)$ ) contains at its core the self-application $x\ x$ , which is untypeable in the statically typed programming languages. But the expression `app x x` above *is* typeable. Equivalently, we can redefine the self-application combinator $\operatorname {U}$ and use it as

```mw
U' g = g (Rec g)
y f = U' (\ Rec g -> f (U' g))
--     g (Rec g)  =  f (g (Rec g))

U'' x = app x x
y f = U'' (Rec (\ x -> f (U'' x)))
--        app x x  =  f (app x x)
```

Or in OCaml:

```mw
type 'a recc = In of ('a recc -> 'a)
let out (In x) = x

let y f = (fun x a -> f (out x x) a) (In (fun x a -> f (out x x) a))
```

Alternatively:

```mw
let y f = (fun x -> f (fun z -> out x x z)) (In (fun x -> f (fun z -> out x x z)))
```

Some languages allow for explicitly marking general types as being recursive even without naming them. Doing that also allows for defining the $\operatorname {Y}$ combinator in such languages.

## General information

Because fixed-point combinators can be used to implement recursion, it is possible to use them to describe specific types of recursive computations, such as those in fixed-point iteration, iterative methods, recursive join in relational databases, data-flow analysis, FIRST and FOLLOW sets of non-terminals in a context-free grammar, transitive closure, and other types of closure operations.

A function for which *every* input is a fixed point is called an identity function. Formally:

$\forall x(f\ x=x)$

In contrast to universal quantification over all x , a fixed-point combinator constructs *one* value that is a fixed point of f . The remarkable property of a fixed-point combinator is that it constructs a fixed point for an *arbitrary given* function f .

Other functions have the special property that, after being applied once, further applications don't have any effect. More formally:

$\forall x(f\ (f\ x)=f\ x)$

Such functions are called idempotent (see also Projection (mathematics)). An example of such a function is the function that returns 0 for all even integers, and 1 for all odd integers.

In lambda calculus, from a computational point of view, applying a fixed-point combinator to an identity function or an idempotent function typically results in non-terminating computation. For example, obtaining

$(\mathrm {Y} \ \lambda x.x)=(\lambda x.(\lambda x.x)(x\ x))\ (\lambda x.(\lambda x.x)(x\ x))$

where the resulting term can only reduce to itself and represents an infinite loop.

Fixed-point combinators do not necessarily exist in more restrictive models of computation. For instance, they do not exist in simply typed lambda calculus.

The Y combinator allows recursion to be defined as a set of rewrite rules, without requiring native recursion support in the language.

In programming languages that support anonymous functions, fixed-point combinators allow the definition and use of anonymous recursive functions, i.e., without having to bind such functions to identifiers. In this setting, the use of fixed-point combinators is sometimes called *anonymous recursion*.
