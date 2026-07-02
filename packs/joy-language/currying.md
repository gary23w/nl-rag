---
title: "Currying"
source: https://en.wikipedia.org/wiki/Currying
domain: joy-language
license: CC-BY-SA-4.0
tags: joy language, function level programming, manfred von thun, concatenative programming, higher order function
fetched: 2026-07-02
---

# Currying

In mathematics and computer science, **currying** is the technique of translating a function that takes multiple arguments into a sequence of families of functions, each taking a single argument.

In the prototypical example, one begins with a function $f:(X\times Y)\to Z$ that takes two arguments, one from X and one from $Y,$ and produces objects in $Z.$ The curried form of this function treats the first argument as a parameter, so as to create a family of functions $f_{x}:Y\to Z.$ The family is arranged so that for each object x in $X,$ there is exactly one function $f_{x}$ , such that for any y in Y , $f_{x}(y)=f(x,y)$ .

In this example, ${\mbox{curry}}$ itself becomes a function that takes f as an argument, and returns a function that maps each x to $f_{x}.$ The proper notation for expressing this is verbose. The function f belongs to the set of functions $(X\times Y)\to Z.$ Meanwhile, $f_{x}$ belongs to the set of functions $Y\to Z.$ Thus, something that maps x to $f_{x}$ will be of the type $X\to [Y\to Z].$ With this notation, ${\mbox{curry}}$ is a function that takes objects from the first set, and returns objects in the second set, and so one writes ${\mbox{curry}}:[(X\times Y)\to Z]\to (X\to [Y\to Z]).$ This is a somewhat informal example; more precise definitions of what is meant by "object" and "function" are given below. These definitions vary from context to context, and take different forms, depending on the theory that one is working in.

Currying is related to, but not the same as, partial application. The example above can be used to illustrate partial application; it is quite similar. Partial application is the function ${\mbox{apply}}$ that takes the pair f and x together as arguments, and returns $f_{x}.$ Using the same notation as above, partial application has the signature ${\mbox{apply}}:([(X\times Y)\to Z]\times X)\to [Y\to Z].$ Written this way, application can be seen to be adjoint to currying.

The currying of a function with more than two arguments can be defined by induction.

Currying is useful in both practical and theoretical settings. In functional programming languages, and many others, it provides a way of automatically managing how arguments are passed to functions and exceptions. In theoretical computer science, it provides a way to study functions with multiple arguments in simpler theoretical models which provide only one argument. The most general setting for the strict notion of currying and uncurrying is in the closed monoidal categories, which underpins a vast generalization of the Curry–Howard correspondence of proofs and programs to a correspondence with many other structures, including quantum mechanics, cobordisms, and string theory.

The concept of currying was introduced by Gottlob Frege, developed by Moses Schönfinkel, and further developed by Haskell Curry.

**Uncurrying** is the dual transformation to currying, and can be seen as a form of defunctionalization. It takes a function f whose return value is another function g , and yields a new function $f'$ that takes as parameters the arguments for both f and g , and returns, as a result, the application of f and subsequently, g , to those arguments. The process can be iterated.

## Motivation

Currying provides a way for working with functions that take multiple arguments, and using them in frameworks where functions might take only one argument. For example, some analytical techniques can only be applied to functions with a single argument. Practical functions frequently take more arguments than this. Frege showed that it was sufficient to provide solutions for the single argument case, as it was possible to transform a function with multiple arguments into a chain of single-argument functions instead. This transformation is the process now known as currying. All "ordinary" functions that might typically be encountered in mathematical analysis or in computer programming can be curried. However, there are categories in which currying is not possible; the most general categories which allow currying are the closed monoidal categories.

Some programming languages almost always use curried functions to achieve multiple arguments; notable examples are ML and Haskell, where in both cases all functions have exactly one argument. This property is inherited from lambda calculus, where multi-argument functions are usually represented in curried form.

Currying is related to, but not the same as partial application. In practice, the programming technique of closures can be used to perform partial application and a kind of currying, by hiding arguments in an environment that travels with the curried function.

## History

The "Curry" in "Currying" is a reference to logician Haskell Curry, who used the concept extensively, but Moses Schönfinkel had the idea six years before Curry. The alternative name "Schönfinkelisation" has been proposed. In the mathematical context, the principle can be traced back to work in 1893 by Frege.

The originator of the word "currying" is not clear. David Turner says the word was coined by Christopher Strachey in his 1967 lecture notes Fundamental Concepts in Programming Languages, but that source introduces the concept as "a device originated by Schönfinkel", and the term "currying" is not used, while Curry is mentioned later in the context of higher-order functions. John C. Reynolds defined "currying" in a 1972 paper, but did not claim to have coined the term.

## Definition

Currying is most easily understood by starting with an informal definition, which can then be molded to fit many different domains. First, there is some notation to be established. The notation $X\to Y$ denotes all functions from X to Y . If f is such a function, we write $f\colon X\to Y$ . Let $X\times Y$ denote the ordered pairs of the elements of X and Y respectively, that is, the Cartesian product of X and Y . Here, X and Y may be sets, or they may be types, or they may be other kinds of objects, as explored below.

Given a function

$f\colon (X\times Y)\to Z$

,

**currying** constructs a new function

$g\colon X\to (Y\to Z)$

.

That is, g takes an argument of type X and returns a function of type $Y\to Z$ . It is defined by

$g(x)(y)=f(x,y)$

for x of type X and y of type Y . We then also write

${\text{curry}}(f)=g.$

**Uncurrying** is the reverse transformation, and is most easily understood in terms of its right adjoint, the function $\operatorname {apply} .$

### Set theory

In set theory, the notation $Y^{X}$ is used to denote the set of functions from the set X to the set Y . Currying is the natural bijection between the set $A^{B\times C}$ of functions from $B\times C$ to A , and the set $(A^{C})^{B}$ of functions from B to the set of functions from C to A . In symbols:

$A^{B\times C}\cong (A^{C})^{B}$

Indeed, it is this natural bijection that justifies the exponential notation for the set of functions. As is the case in all instances of currying, the formula above describes an adjoint pair of functors: for every fixed set C , the functor $B\mapsto B\times C$ is left adjoint to the functor $A\mapsto A^{C}$ .

In the category of sets, the object $Y^{X}$ is called the exponential object.

### Function spaces

In the theory of function spaces, such as in functional analysis or homotopy theory, one is commonly interested in continuous functions between topological spaces. One writes ${\text{Hom}}(X,Y)$ (the Hom functor) for the set of *all* functions from X to Y , and uses the notation $Y^{X}$ to denote the subset of continuous functions. Here, ${\text{curry}}$ is the bijection

${\text{curry}}:{\text{Hom}}(X\times Y,Z)\to {\text{Hom}}(X,{\text{Hom}}(Y,Z)),$

while uncurrying is the inverse map. If the set $Y^{X}$ of continuous functions from X to Y is given the compact-open topology, and if the space Y is locally compact Hausdorff, then

${\text{curry}}:Z^{X\times Y}\to (Z^{Y})^{X}$

is a homeomorphism. This is also the case when X , Y and $Y^{X}$ are compactly generated, although there are more cases.

One useful corollary is that a function is continuous if and only if its curried form is continuous. Another important result is that the application map, usually called "evaluation" in this context, is continuous (note that eval is a strictly different concept in computer science.) That is,

${\begin{aligned}&&{\text{eval}}:Y^{X}\times X\to Y\\&&(f,x)\mapsto f(x)\end{aligned}}$

is continuous when $Y^{X}$ is compact-open and Y locally compact Hausdorff. These two results are central for establishing the continuity of homotopy, i.e. when X is the unit interval I , so that $Z^{I\times Y}\cong (Z^{Y})^{I}$ can be thought of as either a homotopy of two functions from Y to Z , or, equivalently, a single (continuous) path in $Z^{Y}$ .

### Algebraic topology

In algebraic topology, currying serves as an example of Eckmann–Hilton duality, and, as such, plays an important role in a variety of different settings. For example, loop space is adjoint to reduced suspensions; this is commonly written as

$[\Sigma X,Z]\approxeq [X,\Omega Z]$

where $[A,B]$ is the set of homotopy classes of maps $A\rightarrow B$ , and $\Sigma A$ is the suspension of *A*, and $\Omega A$ is the loop space of *A*. In essence, the suspension $\Sigma X$ can be seen as the cartesian product of X with the unit interval, modulo an equivalence relation to turn the interval into a loop. The curried form then maps the space X to the space of functions from loops into Z , that is, from X into $\Omega Z$ . Then ${\text{curry}}$ is the adjoint functor that maps suspensions to loop spaces, and uncurrying is the dual.

The duality between the mapping cone and the mapping fiber (cofibration and fibration) can be understood as a form of currying, which in turn leads to the duality of the long exact and coexact Puppe sequences.

In homological algebra, the relationship between currying and uncurrying is known as tensor-hom adjunction. Here, an interesting twist arises: the Hom functor and the tensor product functor might not lift to an exact sequence; this leads to the definition of the Ext functor and the Tor functor.

### Domain theory

In order theory, the theory of lattices of partially ordered sets, ${\text{curry}}$ is a continuous function when the lattice is given the Scott topology. Scott-continuous functions were first investigated in the attempt to provide a semantics for lambda calculus (as ordinary set theory is inadequate to do this). More generally, Scott-continuous functions are now studied in domain theory, which encompasses the study of denotational semantics of computer algorithms. Note that the Scott topology is quite different than many common topologies one might encounter in the category of topological spaces; the Scott topology is typically finer, and is not sober.

The notion of continuity makes its appearance in homotopy type theory, where, roughly speaking, two computer programs can be considered to be homotopic, i.e. compute the same results, if they can be "continuously" refactored from one to the other.

### Lambda calculi

In theoretical computer science, currying provides a way to study functions with multiple arguments in very simple theoretical models, such as the lambda calculus, in which functions only take a single argument. Consider a function $f(x,y)$ taking two arguments, and having the type $(X\times Y)\to Z$ , which should be understood to mean that *x* must have the type X , *y* must have the type Y , and the function itself returns the type Z . The curried form of *f* is defined as

${\text{curry}}(f)=\lambda x.(\lambda y.(f(x,y)))$

where $\lambda$ is the abstractor of lambda calculus. Since curry takes, as input, functions with the type $(X\times Y)\to Z$ , one concludes that the type of curry itself is

${\text{curry}}:((X\times Y)\to Z)\to (X\to (Y\to Z))$

The → operator is often considered right-associative, so the curried function type $X\to (Y\to Z)$ is often written as $X\to Y\to Z$ . Conversely, function application is considered to be left-associative, so that $f(x,y)$ is equivalent to

$(({\text{curry}}(f)\;x)\;y)={\text{curry}}(f)\;x\;y$

.

That is, the parenthesis are not required to disambiguate the order of the application.

Curried functions may be used in any programming language that supports closures; however, uncurried functions are generally preferred for efficiency reasons, since the overhead of partial application and closure creation can then be avoided for most function calls.

### Type theory

In type theory, the general idea of a type system in computer science is formalized into a specific algebra of types. For example, when writing $f\colon X\to Y$ , the intent is that X and Y are types, while the arrow $\to$ is a type constructor, specifically, the function type or arrow type. Similarly, the Cartesian product $X\times Y$ of types is constructed by the product type constructor $\times$ .

The type-theoretical approach is expressed in programming languages such as ML and the languages derived from and inspired by it: Caml, Haskell, and F#.

The type-theoretical approach provides a natural complement to the language of category theory, as discussed below. This is because categories, and specifically, monoidal categories, have an internal language, with simply typed lambda calculus being the most prominent example of such a language. It is important in this context, because it can be built from a single type constructor, the arrow type. Currying then endows the language with a natural product type. The correspondence between objects in categories and types then allows programming languages to be re-interpreted as logics (via Curry–Howard correspondence), and as other types of mathematical systems, as explored further, below.

### Logic

Under the Curry–Howard correspondence, the existence of currying and uncurrying is equivalent to the logical theorem $((A\land B)\to C)\Leftrightarrow (A\to (B\to C))$ (also known as exportation), as tuples (product type) corresponds to conjunction in logic, and function type corresponds to implication.

The exponential object $Q^{P}$ in the category of Heyting algebras is normally written as material implication $P\to Q$ . Distributive Heyting algebras are Boolean algebras, and the exponential object has the explicit form $\neg P\lor Q$ , thus making it clear that the exponential object really is material implication.

### Category theory

The above notions of currying and uncurrying find their most general, abstract statement in category theory. Currying is a universal property of an exponential object, and gives rise to an adjunction in cartesian closed categories. That is, there is a natural isomorphism between the morphisms from a binary product $f\colon (X\times Y)\to Z$ and the morphisms to an exponential object $g\colon X\to Z^{Y}$ .

This generalizes to a broader result in closed monoidal categories: Currying is the statement that the tensor product and the internal Hom are adjoint functors; that is, for every object B there is a natural isomorphism:

$\mathrm {Hom} (A\otimes B,C)\cong \mathrm {Hom} (A,B\Rightarrow C).$

Here, *Hom* denotes the (external) Hom-functor of all morphisms in the category, while $B\Rightarrow C$ denotes the internal hom functor in the closed monoidal category. For the category of sets, the two are the same. When the product is the cartesian product, then the internal hom $B\Rightarrow C$ becomes the exponential object $C^{B}$ .

Currying can break down in one of two ways. One is if a category is not closed, and thus lacks an internal hom functor (possibly because there is more than one choice for such a functor). Another way is if it is not monoidal, and thus lacks a product (that is, lacks a way of writing down pairs of objects). Categories that do have both products and internal homs are exactly the closed monoidal categories.

The setting of cartesian closed categories is sufficient for the discussion of classical logic; the more general setting of closed monoidal categories is suitable for quantum computation.

The difference between these two is that the product for cartesian categories (such as the category of sets, complete partial orders or Heyting algebras) is just the Cartesian product; it is interpreted as an ordered pair of items (or a list). Simply typed lambda calculus is the internal language of cartesian closed categories; and it is for this reason that pairs and lists are the primary types in the type theory of LISP, Scheme and many functional programming languages.

By contrast, the product for monoidal categories (such as Hilbert space and the vector spaces of functional analysis) is the tensor product. The internal language of such categories is linear logic, a form of quantum logic; the corresponding type system is the linear type system. Such categories are suitable for describing entangled quantum states, and, more generally, allow a vast generalization of the Curry–Howard correspondence to quantum mechanics, to cobordisms in algebraic topology, and to string theory. The linear type system, and linear logic are useful for describing synchronization primitives, such as mutual exclusion locks, and the operation of vending machines.

## Contrast with partial function application

Currying and partial function application are often conflated. One of the significant differences between the two is that a call to a partially applied function returns the result right away, not another function down the currying chain; this distinction can be illustrated clearly for functions whose arity is greater than two.

Given a function of type $f\colon (X\times Y\times Z)\to N$ , currying produces ${\text{curry}}(f)\colon X\to (Y\to (Z\to N))$ . That is, while an evaluation of the first function might be represented as $f(1,2,3)$ , evaluation of the curried function would be represented as $f_{\text{curried}}(1)(2)(3)$ , applying each argument in turn to a single-argument function returned by the previous invocation. Note that after calling $f_{\text{curried}}(1)$ , we are left with a function that takes a single argument and returns another function, not a function that takes two arguments.

In contrast, **partial function application** refers to the process of fixing a number of arguments to a function, producing another function of smaller arity. Given the definition of f above, we might fix (or 'bind') the first argument, producing a function of type ${\text{partial}}(f)\colon (Y\times Z)\to N$ . Evaluation of this function might be represented as $f_{\text{partial}}(2,3)$ . Note that the result of partial function application in this case is a function that takes two arguments.

Intuitively, partial function application says "if you fix the first argument of the function, you get a function of the remaining arguments". For example, if function *div* stands for the division operation *x*/*y*, then *div* with the parameter *x* fixed at 1 (i.e., *div* 1) is another function: the same as the function *inv* that returns the multiplicative inverse of its argument, defined by *inv*(*y*) = 1/*y*.

The practical motivation for partial application is that very often the functions obtained by supplying some but not all of the arguments to a function are useful; for example, many languages have a function or operator similar to `plus_one`. Partial application makes it easy to define these functions, for example by creating a function that represents the addition operator with 1 bound as its first argument.

Partial application can be seen as evaluating a curried function at a fixed point, e.g. given $f\colon (X\times Y\times Z)\to N$ and $a\in X$ then ${\text{curry}}({\text{partial}}(f)_{a})(y)(z)={\text{curry}}(f)(a)(y)(z)$ or simply ${\text{partial}}(f)_{a}={\text{curry}}_{1}(f)(a)$ where ${\text{curry}}_{1}$ curries f's first parameter.

Thus, partial application is reduced to a curried function at a fixed point. Further, a curried function at a fixed point is (trivially), a partial application. For further evidence, note that, given any function $f(x,y)$ , a function $g(y,x)$ may be defined such that $g(y,x)=f(x,y)$ . Thus, any partial application may be reduced to a single curry operation. As such, curry is more suitably defined as an operation which, in many theoretical cases, is often applied recursively, but which is theoretically indistinguishable (when considered as an operation) from a partial application.

So, a partial application can be defined as the objective result of a single application of the curry operator on some ordering of the inputs of some function.
