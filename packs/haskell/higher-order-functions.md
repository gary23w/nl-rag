---
title: "Haskell/Higher-order functions"
source: https://en.wikibooks.org/wiki/Haskell/Higher-order_functions
domain: haskell
license: CC-BY-SA-4.0 (Wikibooks)
tags: haskell, ghc, hackage, cabal
fetched: 2026-07-02
---

# Haskell/Higher-order functions

<

Haskell

At the heart of functional programming is the idea that functions are *just like any other value*. The power of functional style comes from handling functions themselves as regular values, i.e. by passing functions to other functions and returning them from functions. A function that takes another function (or several functions) as an argument is called a *higher-order function*. They can be found pretty much anywhere in a Haskell program, and indeed we have already met some of them, such as `map` and the various folds. We saw commonplace examples of higher-order functions when discussing `map` in Lists II. Now, we are going to explore some common ways of writing code that manipulates functions.

## A sorting algorithm

For a concrete example, we will consider the task of sorting a list. *Quicksort* is a well-known recursive sorting algorithm. To apply its sorting strategy to a list, we first choose one element and then divide the rest of the list into (A) those elements that should go before the chosen element, (B) those elements equal to the chosen one, and (C) those that should go after. Then, we apply the same algorithm to the unsorted (A) and (C) lists. After enough recursive sorting, we concatenate everything back together and have a final sorted list. That strategy can be translated into a Haskell implementation in a very simple way.

```mw
-- Type signature: any list with elements in the Ord class can be sorted.
quickSort :: (Ord a) => [a] -> [a]
-- Base case:
-- If the list is empty, there is nothing to do.
quickSort [] = []

-- The recursive case:
-- We pick the first element as our "pivot", the rest is to be sorted.
-- Note how the pivot itself ends up included in the middle part.
quickSort (x : xs) = (quickSort less) ++ (x : equal) ++ (quickSort more)
    where
        less = filter (< x) xs
        equal = filter (== x) xs
        more = filter (> x) xs
```

It should be pointed out that our `quickSort` is rather naïve. A more efficient implementation would avoid the three passes through `filter` at each recursive step and not use `(++)` to build the sorted list. Furthermore, unlike our implementation, the *original* quicksort algorithm does the sorting in-place using mutability. We will ignore such concerns for now, as we are more interested in the usage patterns of sorting functions, rather than in exact implementation.

### The `Ord` class

Almost all the basic data types in Haskell are members of the `Ord` class, which is for ordering tests what `Eq` is for equality tests. The `Ord` class defines which ordering is the "natural" one for a given type. It provides a function called `compare`, with type:

```mw
compare :: (Ord a) => a -> a -> Ordering
```

`compare` takes two values and compares them, returning an `Ordering` value, which is `LT` if the first value is *less than* the second, `EQ` if it is *equal* and `GT` if it is *greater than*. For an `Ord` type, `(<)`, `(==)` from `Eq` and `(>)` can be seen as shortcuts to `compare` that check for one of the three possibilities and return a `Bool` to indicate whether the specified ordering is true according to the `Ord` specification for that type. Note that each of the tests we use with `filter` in the definition of `quickSort` corresponds to one of the possible results of `compare`, and so we might have written, for instance, `less` as less = filter (\y -> y `compare` x == LT) xs.

## Choosing how to compare

With `quickSort`, sorting any list with elements in the `Ord` class is easy. Suppose we have a list of `String` and we want to sort them; we just apply `quickSort` to the list. For the rest of this chapter, we will use a pseudo-dictionary of just a few words (but dictionaries with thousands of words would work just as well):

```mw
dictionary = ["I", "have", "a", "thing", "for", "Linux"]
```

`quickSort dictionary` returns:

```mw
["I", "Linux", "a", "for", "have", "thing"]
```

As you can see, capitalization is considered for sorting by default. Haskell `String`s are lists of Unicode characters. Unicode (and almost all other encodings of characters) specifies that the character code for capital letters are less than the lower case letters. So "Z" is less than "a".

To get a proper dictionary-like sorting, we need a case insensitive `quickSort`. To achieve that, we can take a hint from the discussion of `compare` just above. The recursive case of `quickSort` can be rewritten as:

```mw
quickSort compare (x : xs) = (quickSort compare less) ++ (x : equal) ++ (quickSort compare more)
    where
        less  = filter (\y -> y `compare` x == LT) xs
        equal = filter (\y -> y `compare` x == EQ) xs
        more  = filter (\y -> y `compare` x == GT) xs
```

While this version is less tidy than the original one, it makes it obvious that the ordering of the elements hinges entirely on the `compare` function. That means we only need to replace `compare` with an `(Ord a) => a -> a -> Ordering` function of our choice. Therefore, our updated `quickSort'` is a higher-order function which takes a comparison function along with the list to sort.

```mw
quickSort' :: (Ord a) => (a -> a -> Ordering) -> [a] -> [a]
-- No matter how we compare two things the base case doesn't change,
-- so we use the _ "wildcard" to ignore the comparison function.
quickSort' _ [] = []

-- c is our comparison function
quickSort' c (x : xs) = (quickSort' c less) ++ (x : equal) ++ (quickSort' c more)
    where
        less  = filter (\y -> y `c` x == LT) xs
        equal = filter (\y -> y `c` x == EQ) xs
        more  = filter (\y -> y `c` x == GT) xs
```

We can reuse our `quickSort'` function to serve many different purposes.

If we wanted a *descending* order, we could just reverse our original sorted list with `reverse (quickSort dictionary)`. Yet to actually do the initial sort descending, we could supply `quickSort'` with a comparison function that returns the opposite of the usual `Ordering`.

```mw
-- the usual ordering uses the compare function from the Ord class
usual = compare

-- the descending ordering, note we flip the order of the arguments to compare
descending x y = compare y x

-- the case-insensitive version is left as an exercise!
insensitive = ... 
-- How can we do case-insensitive comparisons without making a big list of all possible cases?
```

*Note*

`Data.List` offers a `sort` function for sorting lists. It does not use quicksort; rather, it uses an efficient implementation of an algorithm called *mergesort*. `Data.List` also includes `sortBy`, which takes a custom comparison function just like our `quickSort'`

| Exercises |
|---|
| Write `insensitive`, such that `quickSort' insensitive dictionary` gives `["a", "for", "have", "I", "Linux", "thing"]`. |

## Higher-Order Functions and Types

The concept of *currying* (the generating of intermediate functions on the way toward a final result) was first introduced in the earlier chapter "Lists II". This is a good place to revisit how currying works.

Our `quickSort'` has type `(a -> a -> Ordering) -> [a] -> [a]`.

Most of the time, the type of a higher-order function provides a guideline about how to use it. A straightforward way of reading the type signature would be "`quickSort'` takes, as its first argument, a function that gives an ordering of two `a`s. Its second argument is a list of `a`s. Finally, it returns a new list of `a`s". This is enough to correctly guess that it uses the given ordering function to sort the list.

Note that the parentheses surrounding `a -> a -> Ordering` are mandatory. They specify that `a -> a -> Ordering` forms a single argument that happens to be a function.

Without the parentheses, we would get `a -> a -> Ordering -> [a] -> [a]` which accepts four arguments (none of which are themselves functions) instead of the desired two, and that wouldn't work as desired.

Remember that the `->` operator is right-associative. Thus, our erroneous type signature `a -> a -> Ordering -> [a] -> [a]` means the same thing as `a -> (a -> (Ordering -> ([a] -> [a])))`.

Given that `->` is right-associative, the explicitly grouped version of the correct `quickSort'` signature is actually `(a -> a -> Ordering) -> ([a] -> [a])`. This makes perfect sense. Our original `quickSort` lacking the adjustable comparison function argument was of type `[a] -> [a]`. It took a list and sorted it. Our new `quickSort'` is simply a function that generates `quickSort` style functions! If we plug in `compare` for the `(a -> a -> Ordering)` part, then we just return our original simple `quickSort` function. If we use a different comparison function for the argument, we generate a *different* variety of a `quickSort` function.

Of course, if we not only give a comparison function as an argument but also feed in an actual list to sort, then the final result is not the new `quickSort`-style function; instead, it continues on and passes the list to the new function and returns the sorted list as our final result.

| Exercises |
|---|
| *(Challenging)* The following exercise combines what you have learned about higher order functions, recursion and I/O. We are going to recreate what is known in imperative languages as a *for loop*. Implement a function for :: a -> (a -> Bool) -> (a -> a) -> (a -> IO ()) -> IO () for i p f job = -- ??? An example of how this function would be used might be for 1 (<10) (+1) print which prints the numbers 1 to 9 on the screen. The desired behaviour of `for` is: starting from an initial value `i`, `for` first checks `p i`, if it evaluates to true it then executes `job i`, else it stops and does nothing. If `job i` was executed, it then uses `f` to modify this value and checks to see if the modified value `f i` satisfies some condition `p`. If it doesn't, it stops; otherwise, the for loop continues, using the modified `f i` in place of `i`. Implement the for loop in Haskell. The paragraph just above gives an imperative description of the for loop. Describe your implementation in more functional terms. Some more challenging exercises you could try Consider a task like "print the list of numbers from 1 to 10". Given that `print` is a function, and we want to apply it to a list of numbers, using `map` sounds like the natural thing to do. But would it actually work? Implement a function `sequenceIO :: [IO a] -> IO [a]`. Given a list of actions, this function runs each of the actions in order and returns all their results as a list. Implement a function `mapIO :: (a -> IO b) -> [a] -> IO [b]` which given a function of type `a -> IO b` and a list of type `[a]`, runs that action on each item in the list, and returns the results. This exercise was inspired from a blog post by osfameron. No peeking! |

## Function manipulation

We will close the chapter by discussing a few examples of common and useful general-purpose higher-order functions. Familiarity with these will greatly enhance your skill at both writing and reading Haskell code.

### Flipping arguments

`flip` is a handy little Prelude function. It takes a function of two arguments and returns a version of the same function with the arguments swapped.

```mw
flip :: (a -> b -> c) -> b -> a -> c
```

`flip` in use:

```
Prelude> (flip (/)) 3 1
0.3333333333333333
Prelude> (flip map) [1,2,3] (*2)
[2,4,6]
```

We could have used flip to write a point-free version of the `descending` comparing function from the quickSort example:

```mw
descending = flip compare
```

`flip` is particularly useful when we want to pass a function with two arguments of different types to another function and the arguments are in the wrong order with respect to the signature of the higher-order function.

### Composition

The `(.)` composition operator is another higher-order function. It has the signature:

```mw
(.) :: (b -> c) -> (a -> b) -> a -> c
```

`(.)` takes two functions as arguments and returns a new function which applies the second function to the argument and then the first. (Writing the type of `(.)` as `(b -> c) -> (a -> b) -> (a -> c)` can make that easier to see.)

Composition and higher-order functions provide a range of powerful tricks. For a tiny sample, first consider the `inits` function, defined in the module `Data.List`. Quoting the documentation, it "returns all initial segments of the argument, shortest first", so that:

```
Prelude Data.List> inits [1,2,3]
[[],[1],[1,2],[1,2,3]]
```

We can provide a one-line implementation for `inits` (written point-free for extra dramatic effect) using only the following higher-order functions from Prelude: `flip`, `scanl`, `(.)` and `map`:

```mw
myInits :: [a] -> [[a]]
myInits = map reverse . scanl (flip (:)) []
```

Swallowing a definition so condensed may look daunting at first, so analyze it slowly, bit by bit, recalling what each function does and using the type signatures as a guide.

The definition of `myInits` is super concise and clean with use of parentheses kept to a bare minimum. Naturally, if one goes overboard with composition by writing mile-long `(.)` chains, things will get confusing; but, when deployed reasonably, these point-free styles shine. Furthermore, the implementation is quite "high level": we do not deal explicitly with details like pattern matching or recursion; the functions we deployed — both the higher-order ones and their functional arguments — take care of such plumbing.

### Application

`($)` is a curious higher-order operator. Its type is:

```mw
($) :: (a -> b) -> a -> b
```

It takes a function as its first argument, and *all* it does is to apply the function to the second argument, so that, for instance, `(head $ "abc") == (head "abc")`.

You might think that `($)` is completely useless! However, there are two interesting points about it. First, `($)` has very low precedence, unlike regular function application which has the highest precedence. In effect, that means we can avoid confusing nesting of parentheses by breaking precedence with `$`. We write a non-point-free version of `myInits` without adding new parentheses:

```mw
myInits :: [a] -> [[a]]
myInits xs = map reverse . scanl (flip (:)) [] $ xs
```

Furthermore, as `($)` is just a function which happens to apply functions, and functions are just values, we can write intriguing expressions such as:

```mw
map ($ 2) [(2*), (4*), (8*)]
```

(Yes, that is a list of functions, and it is perfectly legal.)

### `uncurry` and `curry`

As the name suggests, `uncurry` is a function that undoes currying; that is, it converts a function of two arguments into a function that takes a pair as its only argument.

```mw
uncurry :: (a -> b -> c) -> (a, b) -> c
```

```
Prelude> let addPair = uncurry (+)
Prelude> addPair (2, 3)
5
```

One interesting use of `uncurry` occasionally seen in the wild is in combination with `($)`, so that the first element of a pair is applied to the second.

```
Prelude> uncurry ($) (reverse, "stressed")
"desserts"
```

There is also `curry`, which is the opposite of `uncurry`.

```mw
curry :: ((a, b) -> c) -> a -> b -> c
```

```
Prelude> curry addPair 2 3 -- addPair as in the earlier example.
5
```

Because most Haskell functions are already curried, `curry` is nowhere near as common as `uncurry`.

### `id` and `const`

Finally, we should mention two functions which, while not higher-order functions themselves, are most often used as arguments to higher-order functions. `id`, the *identity* function, is a function with type `a -> a` that returns its argument unchanged.

```
Prelude> id "Hello"
"Hello"
```

Similar in spirit to `id`, `const` is an `a -> b -> a` function that works like this:

```
Prelude> const "Hello" "world"
"Hello"
```

`const` takes two arguments, discards the second and returns the first. Seen as a function of one argument, `a -> (b -> a)`, it returns a constant function, which always returns the same value no matter what argument it is given.

`id` and `const` might appear worthless at first. However, when dealing with higher-order functions it is sometimes necessary to pass a dummy function, be it one that does nothing with its argument or one that always returns the same value. `id` and `const` give us convenient dummy functions for such cases.

| Exercises |
|---|
| Write implementations for `curry`, `uncurry` and `const`. Describe what the following functions do without testing them: `uncurry const` `curry fst` `curry swap`, where `swap :: (a, b) -> (b, a)` swaps the elements of a pair. (`swap` can be found in `Data.Tuple`.) *(Very hard)* Use `foldr` to implement `foldl`. Hint: begin by reviewing the sections about `foldr` and `foldl` in Lists III. There are two solutions; one is easier but relatively boring and the other is truly interesting. For the interesting one, think carefully about how you would go about composing all functions in a list. |
