---
title: "Monad (functional programming) (part 2/2)"
source: https://en.wikipedia.org/wiki/Monad_(functional_programming)
domain: haskell
license: CC-BY-SA-4.0 (Wikibooks)
tags: haskell, ghc, hackage, cabal
fetched: 2026-07-02
part: 2/2
---

## More examples

### Identity monad

The simplest monad is the **Identity monad**, which just annotates plain values and functions to satisfy the monad laws:

```
newtype Id T  =  T

unit(x)    =  x
(x >>= f)  =  f(x)
```

`Identity` does actually have valid uses though, such as providing a base case for recursive monad transformers. It can also be used to perform basic variable assignment within an imperative-style block.

### Collections

Any collection with a proper append is already a monoid, but it turns out that `List` is not the only collection that also has a well-defined join and qualifies as a monad. One can even mutate `List` into these other monadic collections by simply imposing special properties on append:

| Collection | Monoid properties | Combinatoric properties |   |   |   |
|---|---|---|---|---|---|
| Commutative? | Idempotent? | Details | Ordered? | Unique items? |   |
| List | No | No | Free monoid | Yes | No |
| Finite multiset | Yes | No |   | No | No |
| Finite set | Yes | Yes |   | No | Yes |

### IO monad (Haskell)

As already mentioned, pure code should not have unmanaged side effects, but that does not preclude a program from *explicitly* describing and managing effects. This idea is central to Haskell's **IO monad**, where an object of type `IO a` can be seen as describing an action to be performed in the world, optionally providing information about the world of type `a`. An action that provides no information about the world has the type `IO ()`, "providing" the dummy value `()`. When a programmer binds an `IO` value to a function, the function computes the next action to be performed based on the information about the world provided by the previous action (input from users, files, etc.). Most significantly, because the value of the IO monad can only be bound to a function that computes another IO monad, the bind function imposes a discipline of a sequence of actions where the result of an action can only be provided to a function that will compute the next action to perform. This means that actions which do not need to be performed never are, and actions that do need to be performed have a well defined sequence.

For example, Haskell has several functions for acting on the wider file system, including one that checks whether a file exists and another that deletes a file. Their two type signatures are:

```mw
doesFileExist :: FilePath -> IO Bool
removeFile :: FilePath -> IO ()
```

The first is interested in whether a given file really exists, and as a result, outputs a Boolean value within the `IO` monad. The second function, on the other hand, is only concerned with acting on the file system so the `IO` container it outputs is empty.

`IO` is not limited just to file I/O though; it even allows for user I/O, and along with imperative syntax sugar, can mimic a typical "Hello, World!" program:

```mw
main :: IO ()
main = do
  putStrLn "Hello, world!"
  putStrLn "What is your name, user?"
  name <- getLine
  putStrLn ("Nice to meet you, " ++ name ++ "!")
```

Desugared, this translates into the following monadic pipeline (`>>` in Haskell is just a variant of bind for when only monadic effects matter and the underlying result can be discarded):

```mw
main :: IO ()
main =
  putStrLn "Hello, world!" >>
  putStrLn "What is your name, user?" >> 
  getLine >>= (\name ->
    putStrLn ("Nice to meet you, " ++ name ++ "!"))
```

### Writer monad (Java)

Another common situation is keeping a log file or otherwise reporting a program's progress. Sometimes, a programmer may want to log even more specific, technical data for later profiling or debugging. The **Writer monad** can handle these tasks by generating auxiliary output that accumulates step-by-step.

To show how the monad pattern is not restricted to primarily functional languages, this example implements a `Writer` monad in Java, stored in a class representing the `Writer` monad.

```mw
import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

record Writer<T>(T value, List<String> log) {
    // Internals here...
}
```

Defining unit is also very simple:

```mw
record Writer<T>(T value, List<String> log) {
    // ...

    public static <T> Writer<T> unit(T value) {
        return new Writer<>(value, new ArrayList<>());
    }
}
```

Only unit is needed to define simple functions that output `Writer` objects with debugging notes:

```mw
import java.util.List;

class Ops {
    private Ops() {}

    public static Writer<Integer> squared(int x) {
        return new Writer<>(x * x, List.of(String.format("%d was squared.", x)));
    }

    public static Writer<Integer> halved(int x) {
        return new Writer<>(x / 2, List.of(String.format("%d was halved.", x)));
    }
}
```

A true monad still requires bind, but for `Writer`, this operation combines the current log with the log produced by applying a transformation:

```mw
record Writer<T>(T value, List<String> log) {
    // ...

    public <U> Writer<U> bind(Function<T, Writer<U>> transform) {
        Writer<U> result = transform.apply(this.value);
        List<String> newLog = new ArrayList<>(this.log);
        newLog.addAll(result.log());
        return new Writer<>(result.value(), newLog);
    }
}
```

The sample functions can now be chained together using bind, which can be represented using method chaining:

```mw
Writer<Integer> result = Writer.unit(4)
    .bind(Ops::squared)
    .bind(Ops::halved);
```

The final result is a clean separation of concerns between performing computations and accumulating log output for later inspection:

```mw
System.out.println(result.value()); // 8
System.out.println(result.log()); // [4 was squared., 16 was halved.]
```

### Environment monad

An environment monad (also called a *reader monad* and a *function monad*) allows a computation to depend on values from a shared environment. The monad type constructor maps a type T to functions of type *E* → *T*, where E is the type of the shared environment. The monad functions are: return : T → E → T = t ↦ e ↦ t bind : ( E → T ) → ( T → E → T ′ ) → E → T ′ = r ↦ f ↦ e ↦ f ( r e ) e {\displaystyle {\begin{array}{ll}{\text{return}}\colon &T\rightarrow E\rightarrow T=t\mapsto e\mapsto t\\{\text{bind}}\colon &(E\rightarrow T)\rightarrow (T\rightarrow E\rightarrow T')\rightarrow E\rightarrow T'=r\mapsto f\mapsto e\mapsto f\,(r\,e)\,e\end{array}}} ({\displaystyle {\begin{array}{ll}{\text{return}}\colon &T\rightarrow E\rightarrow T=t\mapsto e\mapsto t\\{\text{bind}}\colon &(E\rightarrow T)\rightarrow (T\rightarrow E\rightarrow T')\rightarrow E\rightarrow T'=r\mapsto f\mapsto e\mapsto f\,(r\,e)\,e\end{array}}})

The following monadic operations are useful: ask : E → E = id E local : ( E → E ) → ( E → T ) → E → T = f ↦ c ↦ e ↦ c ( f e ) {\displaystyle {\begin{array}{ll}{\text{ask}}\colon &E\rightarrow E={\text{id}}_{E}\\{\text{local}}\colon &(E\rightarrow E)\rightarrow (E\rightarrow T)\rightarrow E\rightarrow T=f\mapsto c\mapsto e\mapsto c\,(f\,e)\end{array}}} ({\displaystyle {\begin{array}{ll}{\text{ask}}\colon &E\rightarrow E={\text{id}}_{E}\\{\text{local}}\colon &(E\rightarrow E)\rightarrow (E\rightarrow T)\rightarrow E\rightarrow T=f\mapsto c\mapsto e\mapsto c\,(f\,e)\end{array}}})

The ask operation is used to retrieve the current context, while local executes a computation in a modified subcontext. As in a state monad, computations in the environment monad may be invoked by simply providing an environment value and applying it to an instance of the monad.

Formally, a value in an environment monad is equivalent to a function with an additional, anonymous argument; return and bind are equivalent to the K and S combinators, respectively, in the SKI combinator calculus.

### State monads

A state monad allows a programmer to attach state information of any type to a calculation. Given any value type, the corresponding type in the state monad is a function which accepts a state, then outputs a new state (of type `s`) along with a return value (of type `t`). This is similar to an environment monad, except that it also returns a new state, and thus allows modeling a *mutable* environment.

```mw
type State s t = s -> (t, s)
```

Note that this monad takes a type parameter, the type of the state information. The monad operations are defined as follows:

```mw
-- "return" produces the given value without changing the state.
return x = \s -> (x, s)
-- "bind" modifies m so that it applies f to its result.
m >>= f = \r -> let (x, s) = m r in (f x) s
```

Useful state operations include:

```mw
get = \s -> (s, s) -- Examine the state at this point in the computation.
put s = \_ -> ((), s) -- Replace the state.
modify f = \s -> ((), f s) -- Update the state
```

Another operation applies a state monad to a given initial state:

```mw
runState :: State s a -> s -> (a, s)
runState t s = t s
```

do-blocks in a state monad are sequences of operations that can examine and update the state data.

Informally, a state monad of state type S maps the type of return values T into functions of type S → T × S {\displaystyle S\rightarrow T\times S} ({\displaystyle S\rightarrow T\times S}), where S is the underlying state. The return and bind function are:

return

:

T

→

S

→

T

×

S

=

t

↦

s

↦

(

t

,

s

)

bind

:

(

S

→

T

×

S

)

→

(

T

→

S

→

T

′

×

S

)

→

S

→

T

′

×

S

=

m

↦

k

↦

s

↦

(

k

t

s

′

)

where

(

t

,

s

′

)

=

m

s

{\displaystyle {\begin{array}{ll}{\text{return}}\colon &T\rightarrow S\rightarrow T\times S=t\mapsto s\mapsto (t,s)\\{\text{bind}}\colon &(S\rightarrow T\times S)\rightarrow (T\rightarrow S\rightarrow T'\times S)\rightarrow S\rightarrow T'\times S\ =m\mapsto k\mapsto s\mapsto (k\ t\ s')\quad {\text{where}}\;(t,s')=m\,s\end{array}}}

.

From the category theory point of view, a state monad is derived from the adjunction between the product functor and the exponential functor, which exists in any cartesian closed category by definition.

### Continuation monad

A continuation monad with return type R maps type T into functions of type ( T → R ) → R {\displaystyle \left(T\rightarrow R\right)\rightarrow R} ({\displaystyle \left(T\rightarrow R\right)\rightarrow R}). It is used to model continuation-passing style. The return and bind functions are as follows:

return

:

T

→

(

T

→

R

)

→

R

=

t

↦

f

↦

f

t

bind

:

(

(

T

→

R

)

→

R

)

→

(

T

→

(

T

′

→

R

)

→

R

)

→

(

T

′

→

R

)

→

R

=

c

↦

f

↦

k

↦

c

(

t

↦

f

t

k

)

{\displaystyle {\begin{array}{ll}{\text{return}}\colon &T\rightarrow \left(T\rightarrow R\right)\rightarrow R=t\mapsto f\mapsto f\,t\\{\text{bind}}\colon &\left(\left(T\rightarrow R\right)\rightarrow R\right)\rightarrow \left(T\rightarrow \left(T'\rightarrow R\right)\rightarrow R\right)\rightarrow \left(T'\rightarrow R\right)\rightarrow R=c\mapsto f\mapsto k\mapsto c\,\left(t\mapsto f\,t\,k\right)\end{array}}}

The call-with-current-continuation function is defined as follows:

call/cc

:

(

(

T

→

(

T

′

→

R

)

→

R

)

→

(

T

→

R

)

→

R

)

→

(

T

→

R

)

→

R

=

f

↦

k

↦

(

f

(

t

↦

x

↦

k

t

)

k

)

{\displaystyle {\text{call/cc}}\colon \ \left(\left(T\rightarrow \left(T'\rightarrow R\right)\rightarrow R\right)\rightarrow \left(T\rightarrow R\right)\rightarrow R\right)\rightarrow \left(T\rightarrow R\right)\rightarrow R=f\mapsto k\mapsto \left(f\left(t\mapsto x\mapsto k\,t\right)\,k\right)}

### Program logging

The following code is pseudocode. Suppose we have two functions `foo` and `bar`, with types

```mw
foo : int -> int
bar : int -> int
```

That is, both functions take in an integer and return another integer. Then we can apply the functions in succession like so:

```mw
foo (bar x)
```

Where the result is the result of `foo` applied to the result of `bar` applied to `x`.

But suppose we are debugging our program, and we would like to add logging messages to `foo` and `bar`. So we change the types as so:

```mw
foo : int -> int * string
bar : int -> int * string
```

So that both functions return a tuple, with the result of the application as the integer, and a logging message with information about the applied function and all the previously applied functions as the string.

Unfortunately, this means we can no longer compose `foo` and `bar`, as their input type `int` is not compatible with their output type `int * string`. And although we can again gain composability by modifying the types of each function to be `int * string -> int * string`, this would require us to add boilerplate code to each function to extract the integer from the tuple, which would get tedious as the number of such functions increases.

Instead, let us define a helper function to abstract away this boilerplate for us:

```mw
bind : int * string -> (int -> int * string) -> int * string
```

`bind` takes in an integer and string tuple, then takes in a function (like `foo`) that maps from an integer to an integer and string tuple. Its output is an integer and string tuple, which is the result of applying the input function to the integer within the input integer and string tuple. In this way, we only need to write boilerplate code to extract the integer from the tuple once, in `bind`.

Now we have regained some composability. For example:

```mw
bind (bind (x,s) bar) foo
```

Where `(x,s)` is an integer and string tuple.

To make the benefits even clearer, let us define an infix operator as an alias for `bind`:

```mw
(>>=) : int * string -> (int -> int * string) -> int * string
```

So that `t >>= f` is the same as `bind t f`.

Then the above example becomes:

```mw
((x,s) >>= bar) >>= foo
```

Finally, we define a new function to avoid writing `(x, "")` every time we wish to create an empty logging message, where `""` is the empty string.

```mw
return : int -> int * string
```

Which wraps `x` in the tuple described above.

The result is a pipeline for logging messages:

```mw
((return x) >>= bar) >>= foo
```

That allows us to more easily log the effects of `bar` and `foo` on `x`.

`int * string` denotes a pseudo-coded **monadic value**. `bind` and `return` are analogous to the corresponding functions of the same name. In fact, `int * string`, `bind`, and `return` form a monad.

### Additive monads

An **additive monad** is a monad endowed with an additional closed, associative, binary operator **mplus** and an identity element under mplus, called **mzero**. The `Maybe` monad can be considered additive, with `Nothing` as mzero and a variation on the OR operator as mplus. `List` is also an additive monad, with the empty list `[]` acting as mzero and the concatenation operator `++` as mplus.

Intuitively, mzero represents a monadic wrapper with no value from an underlying type, but is also considered a "zero" (rather than a "one") since it acts as an absorber for bind, returning mzero whenever bound to a monadic function. This property is two-sided, and bind will also return mzero when any value is bound to a monadic zero function.

In category-theoretic terms, an additive monad qualifies once as a monoid over monadic functions with bind (as all monads do), and again over monadic values via mplus.

### Free monads

Sometimes, the general outline of a monad may be useful, but no simple pattern recommends one monad or another. This is where a **free monad** comes in; as a free object in the category of monads, it can represent monadic structure without any specific constraints beyond the monad laws themselves. Just as a free monoid concatenates elements without evaluation, a free monad allows chaining computations with markers to satisfy the type system, but otherwise imposes no deeper semantics itself.

For example, by working entirely through the `Just` and `Nothing` markers, the `Maybe` monad is in fact a free monad. The `List` monad, on the other hand, is not a free monad since it brings extra, specific facts about lists (like append) into its definition. One last example is an abstract free monad:

```mw
data Free f a
  = Pure a
  | Free (f (Free f a))

unit :: a -> Free f a
unit x = Pure x

bind :: Functor f => Free f a -> (a -> Free f b) -> Free f b
bind (Pure x) f = f x
bind (Free x) f = Free (fmap (\y -> bind y f) x)
```

Free monads, however, are *not* restricted to a linked-list like in this example, and can be built around other structures like trees.

Using free monads intentionally may seem impractical at first, but their formal nature is particularly well-suited for syntactic problems. A free monad can be used to track syntax and type while leaving semantics for later, and has found use in parsers and interpreters as a result. Others have applied them to more dynamic, operational problems too, such as providing iteratees within a language.

### Comonads

Besides generating monads with extra properties, for any given monad, one can also define a **comonad**. Conceptually, if monads represent computations built up from underlying values, then comonads can be seen as reductions back down to values. Monadic code, in a sense, cannot be fully "unpacked"; once a value is wrapped within a monad, it remains quarantined there along with any side-effects (a good thing in purely functional programming). Sometimes though, a problem is more about consuming contextual data, which comonads can model explicitly.

Technically, a comonad is the categorical dual of a monad, which loosely means that it will have the same required components, only with the direction of the type signatures *reversed*. Starting from the bind-centric monad definition, a comonad consists of:

- A type constructor W that marks the higher-order type W T
- The dual of unit, called **counit** here, extracts the underlying value from the comonad:

```
counit(wa) : W T → T
```

- A reversal of bind (also represented with `=>>`) that **extend**s a chain of reducing functions:

```
(wa =>> f) : (W U, W U → T) → W T
```

extend and counit must also satisfy duals of the monad laws:

```
counit ∘ ( (wa =>> f) → wb )  ↔  f(wa) → b
wa =>> counit  ↔  wa
wa ( (=>> f(wx = wa)) → wb (=>> g(wy = wb)) → wc )  ↔  ( wa (=>> f(wx = wa)) → wb ) (=>> g(wy = wb)) → wc
```

Analogous to monads, comonads can also be derived from functors using a dual of join:

- **duplicate** takes an already comonadic value and wraps it in another layer of comonadic structure:

```
duplicate(wa) : W T → W (W T)
```

While operations like extend are reversed, however, a comonad does *not* reverse functions it acts on, and consequently, comonads are still functors with map, not cofunctors. The alternate definition with duplicate, counit, and map must also respect its own comonad laws:

```
((map duplicate) ∘ duplicate) wa  ↔  (duplicate ∘ duplicate) wa  ↔  wwwa
((map counit) ∘ duplicate)    wa  ↔  (counit ∘ duplicate)    wa  ↔  wa
((map map φ) ∘ duplicate)     wa  ↔  (duplicate ∘ (map φ))   wa  ↔  wwb
```

And as with monads, the two forms can be converted automatically:

```
(map φ) wa    ↔  wa =>> (φ ∘ counit) wx
duplicate wa  ↔  wa =>> wx
```

```
wa =>> f(wx)  ↔  ((map f) ∘ duplicate) wa
```

A simple example is the **Product comonad**, which outputs values based on an input value and shared environment data. In fact, the `Product` comonad is just the dual of the `Writer` monad and effectively the same as the `Reader` monad (both discussed below). `Product` and `Reader` differ only in which function signatures they accept, and how they complement those functions by wrapping or unwrapping values.

A less trivial example is the **Stream comonad**, which can be used to represent data streams and attach filters to the incoming signals with extend. In fact, while not as popular as monads, researchers have found comonads particularly useful for stream processing and modeling dataflow programming.

Due to their strict definitions, however, one cannot simply move objects back and forth between monads and comonads. As an even higher abstraction, arrows can subsume both structures, but finding more granular ways to combine monadic and comonadic code is an active area of research.
