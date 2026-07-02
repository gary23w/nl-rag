---
title: "Haskell/Pattern matching"
source: https://en.wikibooks.org/wiki/Haskell/Pattern_matching
domain: haskell
license: CC-BY-SA-4.0 (Wikibooks)
tags: haskell, ghc, hackage, cabal
fetched: 2026-07-02
---

# Haskell/Pattern matching

<

Haskell

In the previous modules, we introduced and made occasional reference to pattern matching. Now that we have developed some familiarity with the language, it is time to take a proper, deeper look. We will kick-start the discussion with a condensed description, which we will expand upon throughout the chapter:

*In pattern matching, we attempt to **match** values against **patterns** and, if so desired, **bind** variables to successful matches*.

## Analysing pattern matching

Pattern matching is virtually everywhere. For example, consider this definition of `map`:

```mw
map _ []     = []
map f (x:xs) = f x : map f xs
```

At surface level, there are four different patterns involved, two per equation.

- `f` is a pattern which matches *anything at all*, and binds the `f` variable to whatever is matched.
- `(x:xs)` is a pattern that matches a *non-empty list* which is formed by something (which gets bound to the `x` variable) which was cons'd (by the `(:)` function) onto something else (which gets bound to `xs`).
- `[]` is a pattern that matches *the empty list*. It doesn't bind any variables.
- `_` is the pattern which matches anything without binding (wildcard, "don't care" pattern).

In the `(x:xs)` pattern, `x` and `xs` can be seen as sub-patterns used to match the parts of the list. Just like `f`, they match anything - though it is evident that if there is a successful match and `x` has type `a`, `xs` will have type `[a]`. Finally, these considerations imply that `xs` will also match an empty list, and so a one-element list matches `(x:xs)`.

From the above dissection, we can say pattern matching gives us a way to:

- *recognize values*. For instance, when `map` is called and the second argument matches `[]` the first equation for `map` is used instead of the second one.
- *bind variables* to the recognized values. In this case, the variables `f`, `x`, and `xs` are assigned to the values passed as arguments to `map` when the second equation is used, and so we can use these values through the variables in the right-hand side of `=`. As `_` and `[]` show, binding is not an essential part of pattern matching, but just a side effect of using variable names as patterns.
- *break down values into parts*, as the `(x:xs)` pattern does by binding two variables to parts (head and tail) of a matched argument (the non-empty list).

## The connection with constructors

Despite the detailed analysis above, it may seem a little too magical how we break down a list as if we were undoing the effects of the `(:)` operator. Be careful: this process will not work with any arbitrary operator. For example, one might think of defining a function which uses `(++)` to chop off the first three elements of a list:

```mw
dropThree ([x,y,z] ++ xs) = xs
```

But that *will not work*. The function `(++)` is not allowed in patterns. In fact, most other functions that act on lists are similarly prohibited from pattern matching. Which functions, then, *are* allowed?

In one word, *constructors* – the functions used to build values of algebraic data types. Let us consider a random example:

```mw
data Foo = Bar | Baz Int
```

Here `Bar` and `Baz` are constructors for the type `Foo`. You *can* use them for pattern matching `Foo` values and bind variables to the `Int` value contained in a `Foo` constructed with `Baz`:

```mw
f :: Foo -> Int
f Bar     = 1
f (Baz x) = x - 1
```

This is exactly like `showAnniversary` and `showDate` in the Type declarations module. For instance:

```mw
data Date = Date Int Int Int   -- Year, Month, Day
showDate :: Date -> String
showDate (Date y m d) = show y ++ "-" ++ show m ++ "-" ++ show d
```

The `(Date y m d)` pattern in the left-hand side of the `showDate` definition matches a `Date` (built with the `Date` constructor) and binds the variables `y`, `m` and `d` to the contents of the `Date` value.

### Why does it work with lists?

As for lists, they are no different from `data`-defined algebraic data types as far as pattern matching is concerned. It works as if lists were defined with this `data` declaration (note that the following isn't actually valid syntax: lists are actually too deeply ingrained into Haskell to be defined like this):

```mw
data [a] = [] | a : [a]
```

So the empty list, `[]` and the `(:)` function are constructors of the list datatype, and so you can pattern match with them. `[]` takes no arguments, and therefore no variables can be bound when it is used for pattern matching. `(:)` takes two arguments, the list head and tail, which may then have variables bound to them when the pattern is recognized. (This might seem odd if you slipped into thinking that : adds to a list. It doesn’t- it constructs a new list and the old one remains unchanged.)

```
Prelude> :t []
[] :: [a]
Prelude> :t (:)
(:) :: a -> [a] -> [a]
```

Furthermore, since `[x, y, z]` is just syntactic sugar for `x:y:z:[]`, we can achieve something like `dropThree` using pattern matching alone:

```mw
dropThree :: [a] -> [a]
dropThree (_:_:_:xs) = xs
dropThree _          = []
```

The first pattern will match any list with at least three elements. The catch-all second definition provides a reasonable default when lists fail to match the main pattern, and thus prevents runtime crashes due to pattern match failure.

*Note*

From the fact that we *could* write a `dropThree` function with bare pattern matching it doesn't follow that we *should* do so! Even though the solution is simple, it is still a waste of effort to code something this specific when we could just use Prelude and settle it with `drop 3 xs` instead. Mirroring what was said before about baking bare recursive functions, we might say: *don't get too excited about pattern matching either...*

### Tuple constructors

Analogous considerations are valid for tuples. Our access to their components via pattern matching...

```mw
fstPlusSnd :: (Num a) => (a, a) -> a
fstPlusSnd (x, y) = x + y

norm3D :: (Floating a) => (a, a, a) -> a
norm3D (x, y, z) = sqrt (x^2 + y^2 + z^2)
```

... is granted by the existence of tuple constructors. For pairs, the constructor is the comma operator, `(,)`; for larger tuples there are `(,,)`; `(,,,)` and so on. These operators are slightly unusual in that we can't use them infix in the regular way; so `5 , 3` is not a valid way to write `(5, 3)`. All of them, however, can be used prefix, which is occasionally useful.

```
Prelude> (,) 5 3
(5,3)
Prelude> (,,,) "George" "John" "Paul" "Ringo"
("George","John","Paul","Ringo")
```

## Matching literal values

As discussed earlier in the book, a simple piece-wise function definition like this one

```mw
f :: Int -> Int
f 0 = 1
f 1 = 5
f 2 = 2
f _ = -1
```

is performing pattern matching as well, matching the argument of `f` with the `Int` literals 0, 1 and 2, and finally with `_` . In general, numeric and character literals can be used in pattern matching on their own as well as together with constructor patterns. For instance, this function

```mw
g :: [Int] -> Bool
g (0:[]) = False
g (0:xs) = True
g _ = False
```

will evaluate to False for the [0] list, to True if the list has 0 as first element and a non-empty tail and to False in all other cases. Also, lists with literal elements like [1,2,3], or even "abc" (which is equivalent to ['a','b','c']) can be used for pattern matching as well, since these forms are only syntactic sugar for the (:) constructor.

The above considerations are only valid for literal values, so the following will **not** work:

```mw
k = 1
--again, this won't work as expected
h :: Int -> Bool
h k = True
h _ = False
```

| Exercises |
|---|
| Test the flawed `h` function above in GHCi, with arguments equal to and different from 1. Then, explain what goes wrong. In this section about pattern matching with literal values, we made no mention of the boolean values `True` and `False`, but we can do pattern matching with them as well, as demonstrated in the Next steps chapter. Can you guess why we omitted them? (Hint: is there anything distinctive about the way we write boolean values?) |

## Syntax tricks

### As-patterns

Sometimes, when matching a sub-pattern within a value, it may be useful to bind a name to the whole value being matched. As-patterns allow exactly this: they are of the form *`var@pattern`* and have the additional effect to bind the name `var` to the whole value being matched by `pattern`. For instance, here is a toy variation on the map theme:

```mw
contrivedMap :: ([a] -> a -> b) -> [a] -> [b]
contrivedMap f [] = []
contrivedMap f list@(x:xs) = f list x : contrivedMap f xs
```

`contrivedMap` passes to the parameter function `f` not only `x` but also the undivided list used as argument of each recursive call. Writing it without as-patterns would have been a bit clunky because we would have to either use `head` or needlessly *reconstruct* the original value of `list`, i.e. actually evaluate `x:xs` on the right side:

```mw
contrivedMap :: ([a] -> a -> b) -> [a] -> [b]
contrivedMap f [] = []
contrivedMap f (x:xs) = f (x:xs) x : contrivedMap f xs
```

| Exercises |
|---|
| Implement `scanr`, as in the exercise in Lists III, but this time using an as-pattern. |

### Introduction to records

For constructors with many elements, *records* provide a way of naming values in a datatype using the following syntax:

```mw
data Foo2 = Bar2 | Baz2 {bazNumber::Int, bazName::String}
```

Using records allows doing matching and binding only for the variables relevant to the function we're writing, making code much clearer:

```mw
h :: Foo2 -> Int
h Baz2 {bazName=name} = length name
h Bar2 {} = 0

x = Baz2 1 "Haskell"     -- construct by declaration order, try ":t Baz2" in GHCi
y = Baz2 {bazName = "Curry", bazNumber = 2} -- construct by name

h x -- 7
h y -- 5
```

Also, the `{}` pattern can be used for matching a constructor regardless of the datatype elements even if you don't use records in the `data` declaration:

```mw
data Foo = Bar | Baz Int
g :: Foo -> Bool
g Bar {} = True
g Baz {} = False
```

The function `g` does not have to be changed if we modify the number or the type of elements of the constructors `Bar` or `Baz`.

There are further advantages to using record syntax which we will cover in more details in the Named fields section of the More on datatypes chapter.

## Where we can use pattern matching

The short answer is that *wherever you can bind variables, you can pattern match*. Let us have a glance at such places we have seen before; a few more will be introduced in the following chapters.

### Equations

The most obvious use case is the left-hand side of function definition equations, which were the subject of our examples so far.

```mw
map _ []     = []
map f (x:xs) = f x : map f xs
```

In the `map` definition we're doing pattern matching on the left hand side of both equations, and also binding variables on the second one.

#### `let` expressions and `where` clauses

Both `let` and `where` are ways of doing local variable bindings. As such, you can also use pattern matching in them. A simple example:

```mw
y = let (x:_) = map (*2) [1,2,3]
    in x + 5
```

Or, equivalently,

```mw
y = x + 5
    where 
    (x:_) = map (*2) [1,2,3]
```

Here, `x` will be bound to the first element of `map ((*) 2) [1,2,3]`. `y`, therefore, will evaluate to $2+5=7$ .

### Lambda abstractions

Pattern matching can be used directly in lambda abstractions:

```mw
swap = \(x,y) -> (y,x)
```

It is clear, however, that this syntax permits only one pattern (or one for each argument in the case of a multi-argument lambda abstraction).

### List comprehensions

After the `|` in list comprehensions you can pattern match. This is actually extremely useful, and adds a lot to the expressiveness of comprehensions. Let's see how that works with a slightly more sophisticated example. Prelude provides a `Maybe` type which has the following constructors:

```mw
data Maybe a = Nothing | Just a
```

It is typically used to hold values resulting from an operation which may or may not succeed; if the operation succeeds, the `Just` constructor is used and the value is passed to it; otherwise `Nothing` is used. The utility function `catMaybes` (which is available from Data.Maybe library module) takes a list of Maybes (which may contain both "Just" and "Nothing" Maybes), and retrieves the contained values by filtering out the `Nothing` values and getting rid of the `Just` wrappers of the `Just x`. Writing it with list comprehensions is very straightforward:

```mw
catMaybes :: [Maybe a] -> [a]
catMaybes ms = [ x | Just x <- ms ]
```

Another nice thing about using a list comprehension for this task is that if the pattern match fails (that is, it meets a Nothing) it just moves on to the next element in `ms`, thus avoiding the need of explicitly handling constructors we are not interested in with alternate function definitions.

### `do` blocks

Within a `do` block like the ones we used in the Simple input and output chapter, we can pattern match with the left-hand side of the left arrow variable bindings:

```mw
putFirstChar = do
    (c:_) <- getLine
    putStrLn [c]
```

Furthermore, the `let` bindings in `do` blocks are, as far as pattern matching is concerned, just the same as the "real" let expressions.
