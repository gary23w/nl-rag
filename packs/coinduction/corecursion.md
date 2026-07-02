---
title: "Corecursion"
source: https://en.wikipedia.org/wiki/Corecursion
domain: coinduction
license: CC-BY-SA-4.0
tags: coinduction principle, corecursion scheme, coinductive definition, infinite data structure
fetched: 2026-07-02
---

# Corecursion

In computer science, **corecursion** is a type of operation that is dual to (structural) recursion. Whereas recursion consumes a data structure by first handling the topmost layer before descending into its inner parts, corecursion produces a data structure by first defining the topmost layer before defining its inner parts. Corecursion is a particularly important in total languages, as it allows encoding potentially non-terminating computations in a context where every function must terminate. It is supported by theorem provers Agda and Rocq.

Both corecursion and recursion can be thought of as operating on trees, which include data structures like lists and streams as special cases. Since recursion must terminate, it only works on trees that are well-founded, i.e. not infinitely deep, which are called *data* or *initial data types*; on the other hand, corecursion produces *codata* or *final data types*, which includes infinitely deep trees. Codata cannot be represented in memory directly, so is often implemented using self-referential data structures or lazy evaluation.

## Data and codata

In total programming languages, the natural numbers may be defined as follows (using Haskell syntax):

```mw
data Nat = Zero | Succ Nat
```

This states that every natural number is either zero or the successor of an existing natural number. For example, the number one is represented as `Succ Zero`, two as `Succ (Succ Zero)`, three as `Succ (Succ (Succ Zero))` and so on.

If we interpret the above declaration in an *inductive* way, then all natural numbers are generated like this, and we get our familiar set of natural numbers. Importantly, we can do recursion on this set: for example, we can use it to make a list that repeats a value `n` times:

```mw
repeat :: a -> Nat -> [a]
repeat x Zero = []                  -- Base case
repeat x (Succ n) = x : repeat x n  -- Inductive step
```

Note that the use of `repeat x n` is crucial—we could not have written `repeat x (Succ n)`, because that is the function we are trying to define, and therefore it would loop forever. More specifically, the input must get smaller—or rather deeper, if seen as a data structure—each time we recurse.

The declaration may also be interpreted in a *coinductive* way, which may be denoted as:

```mw
codata CoNat = Zero | Succ CoNat
```

`CoNat` has all the natural numbers that `Nat` has automatically. But because codata can be infinitely deep, it has an extra term `Succ (Succ (Succ (Succ …)))` that continues on indefinitely—often denoted ∞. This is unique to the conatural numbers, so it can only be constructed using corecursion:

```mw
infinity :: CoNat
infinity = Succ infinity
```

While recursion requires that the input of the recursive call must get smaller each time, corecursion requires that the output of the recursive call must get larger each time. This is why we must write `Succ infinity`; just `infinity = infinity` would be disallowed as it loops forever.

To illustrate the duality between recursion and corecursion, we can encapsulate them in two functions, `rec` and `corec`. These functions' existence, together with the regular two constructors of `Nat` and `CoNat`, uniquely identify their respective types, and therefore allow rewriting all forms of recursion and corecursion in terms of them.

```mw
rec :: Nat -> (Maybe c -> c) -> c
rec Zero f = f Nothing
rec (Succ n) f = f (Just (rec n f))

corec :: (c -> Maybe c) -> c -> CoNat
corec f base =
  case f base of
    Nothing -> Zero
    Just x -> Succ (corec f x)
```

Conceptually, `CoNat` can be thought of as a state machine, where `c` is a type encapsulating the "current state". The function `c -> Maybe c` is a state transition function that either results in termination with `Zero` or continuation with `Succ`. We can rewrite the examples above using the functions:

```mw
repeat x n = rec n (\ s ->
  case s of
    Nothing -> []
    Just a -> x : a)
    
infinity = corec (\ () -> Just ()) ()
```

A more complex example of codata is that of binary trees, where each node is either a leaf node, holding some data, or is a branch node that has exactly two children:

```mw
codata BinaryTree a = Leaf a | Branch (BinaryTree a) (BinaryTree a)
```

This example has many more infinitely deep terms that can only be constructed by corecursion. For example, it can be infinitely deep only on the left-hand side, or on both sides, or alternating left and right:

```mw
infiniteLeft :: a -> BinaryTree a
infiniteLeft x = Branch (infiniteLeft x) (Leaf x)

infiniteBoth :: BinaryTree a
infiniteBoth = Branch infiniteBoth infiniteBoth

infiniteAlternating :: a -> Bool -> BinaryTree a
infiniteAlternating x False = Branch (infiniteAlternating x True) (Leaf x)
infiniteAlternating x True = Branch (Leaf x) (infiniteAlternating x False)
```

Again, corecursion on binary trees has a more general form based on a "state machine"-like constructor:

```mw
corec :: (c -> Either a (c, c)) -> c -> BinaryTree a
corec f base =
  case f base of
    Left x -> Leaf x
    Right (x, y) -> Branch (corec f x) (corec f y)
```

### M-types

In a dependently-typed setting, codata can be encoded using M-types, which are dual to W-types. Given a type *A* and an *A*-indexed family of types *B*, one can form the M-type ${\mathsf {M}}_{a:A}B(a)$ , representing the type of trees whose nodes are labelled with elements of *A* and who child nodes are indexed by the set *B*(*a*). In pseudocode, M-types (and their corecursion principle) may be defined as:

```mw
codata M a (b :: a -> *) = M
  { root :: a
  , branch :: b root -> M a b } 
  
corec :: (c -> (root :: a, b root -> c)) -> c -> M a b
corec f base =
  let (root, branch) = f base
  in M { root = root, branch = \ i -> corec f (branch i) }
```

As an example, the natural and conatural numbers may be constructed as W- and M-types of the same function:

```mw
f :: Bool -> *
f False = Void -- Zero case (no branches)
f True = ()    -- Succ case (one branch)

Nat = W Bool f
CoNat = M Bool f
```

M-types can be proven to exist in many elementary topoi, and their existence follows from the existence of W-types.

## Mathematical description

The above section showed that there is an intimate link between natural and conatural numbers and `Maybe c`, and similarly between binary trees and `Either a (c, c)`. This link is made precise by showing that `Nat` is in bijection with `Maybe Nat`, and `CoNat` with `Maybe CoNat`; explicitly, this bjiection associates `Zero` with `Nothing` and `Succ n` with `Just n`. In other words, `Nat` and `CoNat` are fixed points (up to isomorphism) of the map $X\mapsto X+1$ .

The difference between data and codata is that data is the least such fixed point, while codata is the greatest. In this way, recursion can be summarized as the statement that "every element of the type was generated only by the given constructors (`Zero` and `Succ` in the case of `Nat`/`CoNat`)", while corecursion states that "every value that can be analysed using the constructors as cases exists".

From a category-theoretic perspective, `CoNat` can be precisely defined as the final coalgebra of the endofunctor $X\mapsto X+1$ . Unfolding this definition, we have that:

- There is a function `pred :: CoNat -> Maybe CoNat`. "Pred" stands for "predecessor", and the intuition is that it subtracts one from the conatural number or gives `Nothing` otherwise. In other words, `pred Zero = Nothing` and `pred (Succ n) = Just n`. This shows that `CoNat` is a coalgebra of the functor, but not necessarily the final one.
- For every type `c` and function `f :: c -> Maybe c`, there is a function `corec f :: c -> CoNat` such that `pred (corec f x) = fmap (corec f) (f x)`. Breaking this down further, if `f x = Just y` then `corec f x = Succ (corec f y)`, while if `f x = Nothing` then `corec f x = Zero`—this matches the definition of `corec` we are familiar with.
- `corec` is *unique* in the following sense: for any other function `g :: c -> CoNat` that also satisfies `pred (g x) = fmap g (f x)`, `g x = corec f x`. This ensures that `CoNat` is a *final* coalgebra.

`Maybe c` can be replaced with any other functor in the above description to obtain the definition of any other coinductive type.

Not all functors have final coalgebras. For example, Cantor's theorem tells us that no set can be in bijection with its powerset, and therefore the powerset functor `a -> Bool` has no final coalgebra. However, in the case of polynomial functors or quotient polynomial functors, final coalgebras always exist; polynomial functors are functors that can be expressed in the form $\textstyle X\mapsto \sum _{a:\alpha }X^{\beta (a)}$ for a type *α* and *α*-indexed type family *β*(*a*). The M-type is exactly the construction of this final coalgebra.

## Coinduction

While one can reason about coinductive data types using the uniqueness of `corec` directly, it is often more convenient to use **coinduction**, which can prove equalities of codata. Given a final coalgebra *A* of a polynomial functor *F*—i.e. *$\textstyle F(X)=\sum _{a:\alpha }X^{\beta (a)}$*— we say that a relation $R\subseteq A\times A$ is a bisimulation if, for all $(a,b)\in R$ , ${\text{root}}(a)={\text{root}}(b)$ and ${\text{branch}}(a,i)R{\text{branch}}(b,i)$ for all $i:B({\text{root}}(a))$ . Here, ${\text{root}}$ and ${\text{branch}}$ refer to the maps:

${\begin{aligned}{\text{root}}&:A\rightarrow \alpha \\{\text{branch}}&:\prod _{a:A}\beta ({\text{root}}(a))\rightarrow A\end{aligned}}$

The principle of coinduction states that for all bisimulations *R* on *A* and $(a,b)\in R$ , $a=b$ .

More generally, for a coalgebra map ${\text{get}}:A\rightarrow F(A)$ , a relation *R* on *A* is a bisimulation if there exists a function $f:R\rightarrow F(R)$ satisfying, for all $(a,b)\in R$ ,

- ${\text{get}}(a)=F(\pi _{1})(f(a,b))$ and
- ${\text{get}}(b)=F(\pi _{2})(f(a,b))$ ,

where *π*₁ and *π*₂ are the first and second projection maps $R\rightarrow A$ . It can be seen this equivalent to the polynomial case by setting $f(a,b)=({\text{root}}(a),i\mapsto ({\text{branch}}(a,i),{\text{branch}}(b,i)))$ . The required equalities can also be expressed as a commutative diagram:

Coinduction is easy to prove from the uniqueness of `corec`: *π*₁ and *π*₂ both satisfy the required property to be equal to `corec f`, and are therefore equal to each other, thus showing that $a=\pi _{1}(a,b)=\pi _{2}(a,b)=b$ .

### Example: Conatural number addition

To demonstrate the usage of coinduction, we will prove some basic properties about addition on conatural numbers. Addition can be defined identically to how it is defined for natural numbers:

```mw
add :: CoNat -> CoNat -> CoNat
add a Zero = a
add a (Succ b) = Succ (add a b)
```

This definition, while valid, hides some amount of complexity. We may alternatively write:

```mw
add Zero Zero = Zero
add (Succ a) Zero = Succ (add a Zero)
add a (Succ b) = Succ (add a b)
```

This definition makes the translation to `corec` straightforward:

```mw
iterate :: (CoNat, CoNat) -> Maybe (CoNat, CoNat)
iterate Zero Zero = Nothing
iterate (Succ a) Zero = Just (a, Zero)
iterate a (Succ b) = Just (a, b)

add a b = corec iterate (a, b)
```

We can prove that $a+0=a$ by coinduction on the relation $\{(a+0,a)|a\in \mathbb {N} ^{\infty }\}$ (where $\mathbb {N} ^{\infty }$ is the set of conatural numbers). First, it follows from the definition of addition that $a+0=0\iff a=0$ ; second, if we assume that $(x+1,y+1)$ is of the form $(a+0,a)$ for some *a*, we must show that $(x,y)$ is also of this form. We have: $x+1=a+0=(y+1)+0=(y+0)+1$ Thus $x=y+0$ , and therefore $(x,y)=(y+0,y)$ as required.

The identity $(a+1)+b=(a+b)+1$ may be similarly proven by coinduction on $\{(((a+1)+b)-1,a+b)|a,b\in \mathbb {N} ^{\infty }\}$ (remember the relation must necessarily include $(0,0)$ ); finally, commutativity— $a+b=b+a$ —results from similar straightforward coinduction on $\{(a+b,b+a)|a,b\in \mathbb {N} ^{\infty }\}$ .

## In programming languages

If the domain of discourse is the category of sets and total functions (such as in theorem provers like Agda and Rocq), then final types (codata) may contain infinite, non-wellfounded values, whereas initial types (data) do not. On the other hand, if the domain of discourse is the category of complete partial orders and continuous functions, which corresponds roughly to the Haskell programming language, then final types coincide with initial types, and the corresponding final coalgebra and initial algebra form an isomorphism.

## History

Corecursion, referred to as *circular programming,* dates at least to (Bird 1984), who credits John Hughes and Philip Wadler; more general forms were developed in (Allison 1989). The original motivations included producing more efficient algorithms (allowing a single pass over data in some cases, instead of requiring multiple passes) and implementing classical data structures, such as doubly linked lists and queues, in functional languages.
