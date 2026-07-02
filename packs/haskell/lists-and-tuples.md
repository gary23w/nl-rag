---
title: "Haskell/Lists and tuples"
source: https://en.wikibooks.org/wiki/Haskell/Lists_and_tuples
domain: haskell
license: CC-BY-SA-4.0 (Wikibooks)
tags: haskell, ghc, hackage, cabal
fetched: 2026-07-02
---

# Haskell/Lists and tuples

<

Haskell

Haskell uses two fundamental structures for managing several values: lists and tuples. They both work by grouping multiple values into a single combined value.

## Lists

Let's build some lists in GHCi:

```
Prelude> let numbers = [1,2,3,4]
Prelude> let truths  = [True, False, False]
Prelude> let strings = ["here", "are", "some", "strings"]
```

The square brackets delimit the list, and individual elements are separated by commas. The only important restriction is that all elements in a list must be of the same type. Trying to define a list with mixed-type elements results in a typical type error:

```
Prelude> let mixed = [True, "bonjour"]

<interactive>:1:19:
    Couldn't match `Bool' against `[Char]'
      Expected type: Bool
      Inferred type: [Char]
    In the list element: "bonjour"
    In the definition of `mixed': mixed = [True, "bonjour"]
```

### Building lists

In addition to specifying the whole list at once using square brackets and commas, you can build them up piece by piece using the `(:)` operator pronounced "cons". The process of building up a list this way is often referred to as **consing**. This terminology comes from LISP programmers who invented the verb "to cons" (a mnemonic for "constructor") to refer to this specific task of prepending an element to a list.

**Example:** Consing something on to a list

```
Prelude> let numbers = [1,2,3,4]
Prelude> numbers
[1,2,3,4]
Prelude> 0:numbers
[0,1,2,3,4]
```

When you cons something on to a list (`something:someList`), you get back another list. Thus, you can keep on consing for as long as you wish. Note that the cons operator evaluates from right to left. Another (more general) way to think of it is that it takes the first value to its left and the whole expression to its right.

**Example:** Consing lots of things to a list

```
Prelude> 1:0:numbers
[1,0,1,2,3,4]
Prelude> 2:1:0:numbers
[2,1,0,1,2,3,4]
Prelude> 5:4:3:2:1:0:numbers
[5,4,3,2,1,0,1,2,3,4]
```

In fact, Haskell builds all lists this way by consing all elements to the *empty list*, `[]`. The commas-and-brackets notation are just *syntactic sugar*. So `[1,2,3,4,5]` is exactly equivalent to `1:2:3:4:5:[]`

You will, however, want to watch out for a potential pitfall in list construction. Whereas `True:False:[]` is perfectly good Haskell, `True:False` is *not*:

**Example:** Whoops!

```
Prelude> True:False

<interactive>:1:5:
    Couldn't match `[Bool]' against `Bool'
      Expected type: [Bool]
      Inferred type: Bool
    In the second argument of `(:)', namely `False'
    In the definition of `it': it = True : False
```

`True:False` produces a familiar-looking type error message. It tells us that the cons operator `(:)` (which is really just a function) expected a list as its second argument, but we gave it another `Bool` instead. `(:)` only knows how to stick things onto lists.

So, when using cons, remember:

- The elements of the list must have the same type.
- You can only cons `(:)` something onto a list, not the other way around (you cannot cons a list onto an element). So, the final item on the right must be a list, and the items on the left must be independent elements, not lists.

| Exercises |
|---|
| Would the following piece of Haskell work: `3:[True,False]`? Why or why not? Write a function `cons8` that takes a list as an argument and conses `8` (at the beginning) on to it. Test it out on the following lists by doing: `cons8 []` `cons8 [1,2,3]` `cons8 [True,False]` `let foo = cons8 [1,2,3]` `cons8 foo` Adapt the above function in a way that `8` is at the end of the list. (Hint: recall the concatenation operator `++` from the previous chapter.) Write a function that takes two arguments, a list and a thing, and conses the thing onto the list. You can start out with: `let myCons list thing =` |

### Strings are just lists

As we briefly mentioned in the Type Basics module, strings in Haskell are just lists of characters. That means values of type String can be manipulated just like any other list. For instance, instead of entering strings directly as a sequence of characters enclosed in double quotation marks, they may also be constructed through a sequence of Char values, either linked with `(:)` and terminated by an empty list or using the commas-and-brackets notation.

```
Prelude> "hey" == ['h','e','y']
True
Prelude> "hey" == 'h':'e':'y':[]
True
```

Using double-quoted strings is just more syntactic sugar.

### Lists of lists

Lists can contain *anything* — as long as they are all of the same type. Because lists are things too, lists can contain other lists! Try the following in the interpreter:

**Example:** Lists can contain lists

```
Prelude> let listOfLists = [[1,2],[3,4],[5,6]]
Prelude> listOfLists
[[1,2],[3,4],[5,6]]
```

Lists of lists can be tricky sometimes because a list of things does not have the same type as a thing all by itself. The type `Int` is different from `[Int]`. Let's sort through these implications with a few exercises:

| Exercises |
|---|
| Which of these are valid Haskell and which are not? Rewrite in cons notation. `[1,2,3,[]]` `[1,[2,3],4]` `[[1,2,3],[]]` Which of these are valid Haskell, and which are not? Rewrite in comma and bracket notation. `[]:[[1,2,3],[4,5,6]]` `[]:[]` `[]:[]:[]` `[1]:[]:[]` `["hi"]:[1]:[]` Can Haskell have lists of lists of lists? Why or why not? Why is the following list invalid in Haskell? `[[1,2],3,[4,5]]` |

Lists of different types of things cannot be consed, but the empty list can be consed with lists of anything. For example, `[]:[[1, 2], [1, 2, 3]]` is valid and will produce `[[], [1, 2], [1, 2, 3]]`, and `[1]:[[1, 2], [1, 2, 3]]` is valid and will produce `[[1], [1, 2], [1, 2, 3]]`, but `['a']:[[1, 2], [1, 2, 3]]` will produce an error message.

Lists of lists allow us to express some kinds of complicated, structured data (two-dimensional matrices, for example). They are also one of the places where the Haskell type system truly shines. Human programmers (including this wikibook co-author) get confused *all* the time when working with lists of lists, and having restrictions on types often helps in wading through the potential mess.

## Tuples

### A different notion of many

**Tuples** offer another way of storing multiple values in a single value. Tuples and lists have two key differences:

- Tuples have a *fixed* number of elements (*immutable*); you can't cons to a tuple. Therefore, it makes sense to use tuples when you *know* in advance how many values are to be stored. For example, we might want a type for storing 2D coordinates of a point. We know exactly how many values we need for each point (two – the *x* and *y* coordinates), so tuples are applicable.

- The elements of a tuple do not need to be all of the same type. For instance, in a phonebook application we might want to handle the entries by crunching three values into one: the name, phone number, and the number of times we made calls. In such a case the three values won't have the same type, since the name and the phone number are strings, but contact counter will be a number, so lists wouldn't work.

Tuples are marked by parentheses with elements delimited by commas. Let's look at some sample tuples:

**Example:** Some tuples

```mw
(True, 1)
("Hello world", False)
(4, 5, "Six", True, 'b')
```

The first example is a tuple containing two elements: True and 1. The next example again has two elements: "Hello world" and False. The third example is a tuple consisting of *five* elements: 4 (a number), 5 (another number), "Six" (a string), True (a boolean value), and 'b' (a character).

A quick note on nomenclature: In general you use *n-tuple* to denote a tuple of size *n*. Commonly, we call 2-tuples (that is, tuples with 2 elements) *pairs* and 3-tuples *triples*. Tuples of greater sizes aren't actually all that common, but we can logically extend the naming system to *quadruples*, *quintuples*, and so on.

| Exercises |
|---|
| Write down the 3-tuple whose first element is 4, second element is "hello" and third element is True. Which of the following are valid tuples? `(4, 4)` `(4, "hello")` `(True, "Blah", "foo")` `()` Lists can be built by consing new elements onto them. Cons a number onto a list of numbers, you will get back a list of numbers. There is no such way to build up tuples. Why do you think that is? For the sake of argument, say that there was such a function. What would you get if you "consed" something on a tuple? |

Tuples are handy when you want to return more than one value from a function. In many languages, returning two or more things at once often requires wrapping them up in a single-purpose data structure, maybe one that only gets used in that function. In Haskell, we would return such results as a tuple.

### Tuples within tuples (and other combinations)

We can apply the same reasoning to tuples about storing lists within lists. Tuples are things too, so you can store tuples within tuples (within tuples up to any arbitrary level of complexity). Likewise, you could also have lists of tuples, tuples of lists, and all sorts of related combinations.

**Example:** Nesting tuples and lists

```mw
((2,3), True)
((2,3), [2,3])
[(1,2), (3,4), (5,6)]
```

The type of a tuple is defined not only by its size, but, like lists, by the types of objects it contains. For example, the tuples `("Hello",32)` and `(47,"World")` are fundamentally different. One is of type `(String,Int)`, whereas the other is `(Int,String)`. This has implications for building up lists of tuples. We could very well have lists like `[("a",1),("b",9),("c",9)]`, but Haskell cannot have a list like `[("a",1),(2,"b"),(9,"c")]`.

| Exercises |
|---|
| Which of these are valid Haskell, and why? `1:(2,3)` `(2,4):(2,3)` `(2,4):[]` `[(2,4),(5,5),('a','b')]` `([2,4],[2,2])` |

## Retrieving values

For lists and tuples to be useful, we will need to access the internal values they contain.

Let's begin with pairs (i.e. 2-tuples) representing the (*x*, *y*) coordinates of a point. Imagine you want to specify a specific square on a chess board. You could label the ranks and files from 1 to 8. Then, a pair `(2, 5)` could represent the square in rank 2 and file 5. Say we want a function for finding all the pieces in a given rank. We could start with the coordinates of all the pieces and then look at the rank part and see whether it equals whatever row we want to examine. Given a coordinate pair `(x, y)` of a piece, our function would need to extract the `x` (the rank coordinate). For this sort of goal, there are two standard functions, `fst` and `snd`, that retrieve the first and second elements out of a pair, respectively. Let's see some examples:

**Example:** Using `fst` and `snd`

```
Prelude> fst (2, 5)
2
Prelude> fst (True, "boo")
True
Prelude> snd (5, "Hello")
"Hello"
```

Note that these functions, by definition, *only* work on pairs.

For lists, the functions `head` and `tail` are *roughly* analogous to `fst` and `snd`. They disassemble a list by taking apart what `(:)` joined. `head` evaluates to the first element of the list, while `tail` gives the rest of the list.

**Example:** Using `head` and `tail`

```
Prelude> 2:[7,5,0]
[2,7,5,0]
Prelude> head [2,7,5,0]
2
Prelude> tail [2,7,5,0]
[7,5,0]
```

*Note*

Unfortunately, we have a serious problem with `head` and `tail`. If we apply either of them to an empty list...

```
Prelude> head []
*** Exception: Prelude.head: empty list
```

... it blows up, as an empty list has no first element, nor any other elements at all. Outside of GHCi, attempting to run `head` or `tail` on the empty list will crash a program.

We will play with `head` and `tail` for the moment, but we want to avoid any risk of such malfunctions in our real code, so we will learn later about better options. One might ask "What is the problem? Using `head` and `tail` works fine if we are careful and never pass them an empty list, or if we somehow test whether a list is empty before calling them." But that way lies madness.

As programs get bigger and more complicated, the number of places in which an empty list could end up being passed to `head` and `tail` grows quickly as does the number of places in which we might make a mistake. As a rule of thumb, you should avoid functions that might fail without warning. As we advance through the book, we will learn better ways to avoid these risks.

### Pending questions

The four functions introduced here do not appear to fully solve the problem we started this section with. While `fst` and `snd` provide a satisfactory solution for pairs, what about tuples with three or more elements? And with lists, can we do any better than just breaking them after the first element? For the moment, we will have to leave these questions pending. Once we do some necessary groundwork, we will return to this subject in future chapters on list manipulation. For now, know that separating head and tail of a list will allow us to do anything we want.

| Exercises |
|---|
| Use a combination of `fst` and `snd` to extract the 4 from the tuple `(("Hello", 4), True)`. Normal chess notation is somewhat different to ours: it numbers the rows from 1-8 and the columns a-h; and the column label is customarily given first. Could we label a specific point with a character and a number, like `('a', 4)`? What important difference with lists does this illustrate? Write a function which returns the head and the tail of a list as the first and second elements of a tuple. Use `head` and `tail` to write a function which gives the fifth element of a list. Then, make a critique of it, pointing out any annoyances and pitfalls you notice. |

## Polymorphic types

Recall that the type of a list depends on the types of its elements and is denoted by enclosing it in square brackets:

```
Prelude> :t [True, False]
[True, False] :: [Bool]
Prelude> :t ["hey", "my"]
["hey", "my"] :: [[Char]]
```

Lists of `Bool` are a different type than lists of `[Char]` (which is the same as a list of `String` because `[Char]` and `String` are synonyms). Since functions only accept arguments of the types specified in the type of the function, that might lead to some complications. For example, consider the case of `head`. Given that `[Int]`, `[Bool]` and `[String]` are different types, it seems we would need separate functions for every case – `headInt :: [Int] -> Int`, `headBool :: [Bool] -> Bool`, `headString :: [String] -> String`, and so on… That, however, would be not only very annoying but also rather senseless. After all, lists are assembled in the same way regardless of the types of the values they contain, and so we would expect the procedure to get the first element of the list would remain the same in all cases.

Fortunately, we do have a single function `head`, which works on all lists:

```
Prelude> head [True, False]
True
Prelude> head ["hey", "my"]
"hey"
```

How can that possibly work? As usual, checking the type of `head` provides a good hint:

**Example:** Our first polymorphic type

```
Prelude> :t head
head :: [a] -> a
```

The `a` in the signature is *not* a type – remember that type names always start with uppercase letters. Instead, it is a **type variable**. When Haskell sees a type variable, it allows any type to take its place. In type theory (a branch of mathematics), this is called *polymorphism*: functions or values with only a single type are called *monomorphic*, and things that use type variables to admit more than one type are *polymorphic*. The type of `head`, for instance, tells us that it takes a list (`[a]`) of values of an arbitrary type (`a`) and gives back a value of that same type (`a`).

Note that within a single type signature, all cases of the same type variable must be of the same type. For example,

```mw
f :: a -> a
```

means that `f` takes an argument of *any* type and gives something of the *same* type as the result, as opposed to

```mw
f :: a -> b
```

which means that `f` takes an argument of *any* type and gives a result of *any* type which *may or may not* match the type of whatever we have for `a`. The different type variables do not specify that the types must be different, it only says that they can be different.

### Example: `fst` and `snd`

As we saw, you can use the `fst` and `snd` functions to extract parts of pairs. By now, you should already be building the habit of wondering "what type is this?" for every function you come across. Let's consider the cases of `fst` and `snd`. These two functions take a pair as their argument and return one element of this pair. As with lists, the type of a pair depends on the type of its elements, so the functions need to be polymorphic. Also remember that pairs (and tuples in general) don't have to be homogeneous with respect to internal types. So if we were to say:

```mw
fst :: (a, a) -> a
```

That would mean `fst` would only work if the first and second part of the pair given as input had the same type. So the correct type is:

**Example:** The types of `fst` and `snd`

```mw
fst :: (a, b) -> a
snd :: (a, b) -> b
```

If you knew nothing about `fst` and `snd` other than the type signatures, you might still guess that they return the first and second parts of a pair, respectively. Although that is correct, other functions may have this same type signature. All the signatures say is that they just have to return something *with the same type* as the first and second parts of the pair, respectively.

| Exercises |
|---|
| Give type signatures for the following functions: The solution to the third exercise of the previous section ("... a function which returns the head and the tail of a list as the first and second elements of a tuple"). The solution to the fourth exercise of the previous section ("... a function which gives the fifth element of a list"). `h x y z = chr (x - 2)` (remember we discussed chr in the previous chapter). |

## Summary

This chapter introduced lists and tuples. The key similarities and differences between them are:

1. Lists are defined by square brackets and commas : `[1,2,3]`.
  - Lists can contain *anything* as long as all the elements of the list are of the same type.
  - Lists can also be built by the cons operator, `(:)`, but you can only cons things onto lists.
2. Tuples are defined by parentheses and commas : `("Bob",32)`
  - Tuples can contain *anything*, even things of different types.
  - The length of a tuple is encoded in its type; tuples with different lengths will have different types.
3. Lists and tuples can be combined in any number of ways: lists within lists, tuples within lists, etc, but their criteria must still be fulfilled for the combinations to be valid.
