---
title: "Ramda Documentation (part 1/4)"
source: https://ramdajs.com/docs/
domain: ramda-functional
license: CC-BY-SA-4.0
tags: ramda functional, point-free style, javascript currying, immutable pipeline
fetched: 2026-07-02
part: 1/4
---

## __ Function

Added in v0.6.0

A special placeholder value used to specify "gaps" within curried functions, allowing partial application of any combination of arguments, regardless of their positions.

If `g` is a curried ternary function and `_` is `R.__`, the following are equivalent:

- `g(1, 2, 3)`
- `g(_, 2, 3)(1)`
- `g(_, _, 3)(1)(2)`
- `g(_, _, 3)(1, 2)`
- `g(_, 2, _)(1, 3)`
- `g(_, 2)(1)(3)`
- `g(_, 2)(1, 3)`
- `g(_, 2)(_, 3)(1)`

```
const greet = R.replace('{name}', R.__, 'Hello, {name}!');
greet('Alice'); 
```


## add Math

Number → Number → Number

Parameters

- a
- b

Returns

Number

Added in v0.1.0

Adds two values.

See also

subtract

.

```
R.add(2, 3);       
R.add(7)(10);      
```


## addIndex Function

(((a …) → b) … → [a] → *) → (((a …, Int, [a]) → b) … → [a] → *)

Parameters

- fn A list iteration function that does not pass index or list to its callback

Returns

function

An altered list iteration function that passes (item, index, list) to its callback

Added in v0.15.0

Creates a new list iteration function from an existing one by adding two new parameters to its callback function: the current index, and the entire list.

This would turn, for instance, `R.map` function into one that more closely resembles `Array.prototype.map`. Note that this will only work for functions in which the iteration callback function is the first parameter, and where the list is the last parameter. (This latter might be unimportant if the list parameter is not used.)

```
const mapIndexed = R.addIndex(R.map);
mapIndexed((val, idx) => idx + '-' + val, ['f', 'o', 'o', 'b', 'a', 'r']);
```


## addIndexRight Function

((a … → b) … → [a] → *) → (a …, Int, [a] → b) … → [a] → *)

Parameters

- fn A list iteration function that does not pass index or list to its callback

Returns

function

An altered list iteration function that passes (item, index, list) to its callback

Added in v0.29.0

As with `addIndex`, `addIndexRight` creates a new list iteration function from an existing one by adding two new parameters to its callback function: the current index, and the entire list.

Unlike `addIndex`, `addIndexRight` iterates from the right to the left.

```
const revmap = (fn, ary) => R.map(fn, R.reverse(ary));
const revmapIndexed = R.addIndexRight(revmap);
revmapIndexed((val, idx) => idx + '-' + val, ['f', 'o', 'o', 'b', 'a', 'r']);
```


## adjust List

Number → (a → a) → [a] → [a]

Parameters

- idx The index.
- fn The function to apply.
- list An array-like object whose value at the supplied index will be replaced.

Returns

Array

A copy of the supplied array-like object with the element at index `idx` replaced with the value returned by applying `fn` to the existing element.

Added in v0.14.0

Applies a function to the value at the given index of an array, returning a new copy of the array with the element at the given index replaced with the result of the function application.

When `idx < -list.length || idx >= list.length`, the original list is returned.

See also

update

.

```
R.adjust(1, R.toUpper, ['a', 'b', 'c', 'd']);      
R.adjust(-1, R.toUpper, ['a', 'b', 'c', 'd']);     

R.adjust(4, R.toUpper, ['a', 'b', 'c', 'd']);      
R.adjust(-5, R.toUpper, ['a', 'b', 'c', 'd']);     
```


## all List

(a → Boolean) → [a] → Boolean

Parameters

- fn The predicate function.
- list The array to consider.

Returns

Boolean

`true` if the predicate is satisfied by every element, `false` otherwise.

Added in v0.1.0

Returns `true` if all elements of the list match the predicate, `false` if there are any that don't.

Dispatches to the `all` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

any

,

none

,

transduce

.

```
const equals3 = R.equals(3);
R.all(equals3)([3, 3, 3, 3]); 
R.all(equals3)([3, 3, 1, 3]); 
```


## allPass Logic

[(*… → Boolean)] → (*… → Boolean)

Parameters

- predicates An array of predicates to check

Returns

function

The combined predicate

Added in v0.9.0

Takes a list of predicates and returns a predicate that returns true for a given list of arguments if every one of the provided predicates is satisfied by those arguments.

The function returned is a curried function whose arity matches that of the highest-arity predicate.

See also

anyPass

,

both

.

```
const isQueen = R.propEq('Q', 'rank');
const isSpade = R.propEq('♠︎', 'suit');
const isQueenOfSpades = R.allPass([isQueen, isSpade]);

isQueenOfSpades({rank: 'Q', suit: '♣︎'}); 
isQueenOfSpades({rank: 'Q', suit: '♠︎'}); 
```


## always Function

a → (* → a)

Parameters

- val The value to wrap in a function

Returns

function

A Function :: * -> val.

Added in v0.1.0

Returns a function that always returns the given value. Note that for non-primitives the value returned is a reference to the original value.

This function is known as `const`, `constant`, or `K` (for K combinator) in other languages and libraries.

```
const t = R.always('Tee');
t(); 
```


## and Logic

a → b → a | b

Parameters

- a
- b

Returns

Any

Added in v0.1.0

Returns the first argument if it is falsy, otherwise the second argument. Acts as the boolean `and` statement if both inputs are `Boolean`s.

See also

both

,

or

.

```
R.and(true, true); 
R.and(true, false); 
R.and(false, true); 
R.and(false, false); 
```


## andThen Function

(a → b) → (Promise e a) → (Promise e b)

(a → (Promise e b)) → (Promise e a) → (Promise e b)

Parameters

- onSuccess The function to apply. Can return a value or a promise of a value.
- p

Returns

Promise

The result of calling `p.then(onSuccess)`

Added in v0.27.1

Returns the result of applying the onSuccess function to the value inside a successfully resolved promise. This is useful for working with promises inside function compositions.

See also

otherwise

,

pipeWith

.

```
const makeQuery = email => ({ query: { email }});
const fetchMember = request =>
  Promise.resolve({ firstName: 'Bob', lastName: 'Loblaw', id: 42 });
const pickName = R.pick(['firstName', 'lastName'])

const getMemberName = R.pipe(
  makeQuery,
  fetchMember,
  R.andThen(pickName),
);

const getMemberName = R.pipe(
  makeQuery,
  fetchMember,
)

R.pipeWith(R.andThen, [getMemberName, pickName])('bob@gmail.com').then(console.log)

getMemberName('bob@gmail.com').then(console.log);
```


## any List

(a → Boolean) → [a] → Boolean

Parameters

- fn The predicate function.
- list The array to consider.

Returns

Boolean

`true` if the predicate is satisfied by at least one element, `false` otherwise.

Added in v0.1.0

Returns `true` if at least one of the elements of the list match the predicate, `false` otherwise.

Dispatches to the `any` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

all

,

none

,

transduce

.

```
const lessThan0 = R.flip(R.lt)(0);
const lessThan2 = R.flip(R.lt)(2);
R.any(lessThan0)([1, 2]); 
R.any(lessThan2)([1, 2]); 
```


## anyPass Logic

[(*… → Boolean)] → (*… → Boolean)

Parameters

- predicates An array of predicates to check

Returns

function

The combined predicate

Added in v0.9.0

Takes a list of predicates and returns a predicate that returns true for a given list of arguments if at least one of the provided predicates is satisfied by those arguments.

The function returned is a curried function whose arity matches that of the highest-arity predicate.

See also

allPass

,

either

.

```
const isClub = R.propEq('♣', 'suit');
const isSpade = R.propEq('♠', 'suit');
const isBlackCard = R.anyPass([isClub, isSpade]);

isBlackCard({rank: '10', suit: '♣'}); 
isBlackCard({rank: 'Q', suit: '♠'}); 
isBlackCard({rank: 'Q', suit: '♦'}); 
```


## ap Function

[a → b] → [a] → [b]

Apply f => f (a → b) → f a → f b

(r → a → b) → (r → a) → (r → b)

Parameters

- applyF
- applyX

Returns

*

Added in v0.3.0

ap applies a list of functions to a list of values.

Dispatches to the `ap` method of the first argument, if present. Also treats curried functions as applicatives.

```
R.ap([R.multiply(2), R.add(3)], [1,2,3]); 
R.ap([R.concat('tasty '), R.toUpper], ['pizza', 'salad']); 

R.ap(R.concat, R.toUpper)('Ramda') 
```


## aperture List

Number → [a] → [[a]]

Parameters

- n The size of the tuples to create
- list The list to split into `n`-length tuples

Returns

Array

The resulting list of `n`-length tuples

Added in v0.12.0

Returns a new list, composed of n-tuples of consecutive elements. If `n` is greater than the length of the list, an empty list is returned.

Acts as a transducer if a transformer is given in list position.

See also

transduce

.

```
R.aperture(2, [1, 2, 3, 4, 5]); 
R.aperture(3, [1, 2, 3, 4, 5]); 
R.aperture(7, [1, 2, 3, 4, 5]); 
```


## append List

a → [a] → [a]

Parameters

- el The element to add to the end of the new list.
- list The list of elements to add a new item to. list.

Returns

Array

A new list containing the elements of the old list followed by `el`.

Added in v0.1.0

Returns a new list containing the contents of the given list, followed by the given element.

See also

prepend

.

```
R.append('tests', ['write', 'more']); 
R.append('tests', []); 
R.append(['tests'], ['write', 'more']); 
```


## apply Function

(*… → a) → [*] → a

Parameters

- fn The function which will be called with `args`
- args The arguments to call `fn` with

Returns

*

result The result, equivalent to `fn(...args)`

Added in v0.7.0

Applies function `fn` to the argument list `args`. This is useful for creating a fixed-arity function from a variadic function. `fn` should be a bound function if context is significant.

See also

call

,

unapply

.

```
const nums = [1, 2, 3, -99, 42, 6, 7];
R.apply(Math.max, nums); 
```


## applySpec Function

{k: ((a, b, …, m) → v)} → ((a, b, …, m) → {k: v})

Parameters

- spec an object recursively mapping properties to functions for producing the values for these properties.

Returns

function

A function that returns an object of the same structure as `spec', with each property set to the value returned by calling its associated function with the supplied arguments.

Added in v0.20.0

Given a spec object recursively mapping properties to functions, creates a function producing an object of the same structure, by mapping each property to the result of calling its associated function with the supplied arguments.

See also

converge

,

juxt

.

```
const getMetrics = R.applySpec({
  sum: R.add,
  nested: { mul: R.multiply }
});
getMetrics(2, 4); 
```


## applyTo Function

a → (a → b) → b

Parameters

- x The value
- f The function to apply

Returns

*

The result of applying `f` to `x`

Added in v0.25.0

Takes a value and applies a function to it.

This function is also known as the `thrush` combinator.

```
const t42 = R.applyTo(42);
t42(R.identity); 
t42(R.add(1)); 
```


## ascend Function

Ord b => (a → b) → a → a → Number

Parameters

- fn A function of arity one that returns a value that can be compared
- a The first item to be compared.
- b The second item to be compared.

Returns

Number

`-1` if fn(a)

<

fn(b), `1` if fn(b)

<

fn(a), otherwise `0`

Added in v0.23.0

Makes an ascending comparator function out of a function that returns a value that can be compared with `<` and `>`.

See also

descend

,

ascendNatural

,

descendNatural

.

```
const byAge = R.ascend(R.prop('age'));
const people = [
  { name: 'Emma', age: 70 },
  { name: 'Peter', age: 78 },
  { name: 'Mikhail', age: 62 },
];
const peopleByYoungestFirst = R.sort(byAge, people);
  
```


## ascendNatural Function

s → (a → String) → a → a → Number

Parameters

- locales A string with a BCP 47 language tag, or an array of such strings. Corresponds to the locales parameter of the Intl.Collator() constructor.
- fn A function of arity one that returns a string that can be compared
- a The first item to be compared.
- b The second item to be compared.

Returns

Number

`-1` if a occurs before b, `1` if a occurs after b, otherwise `0`

Added in v0.30.1

Makes an ascending comparator function out of a function that returns a value that can be compared with natural sorting using localeCompare.

See also

ascend

.

```
const unsorted = ['3', '1', '10', 'Ørjan', 'Bob', 'Älva'];

R.sort(R.ascendNatural('en', R.identity), unsorted);

R.sort(R.ascendNatural('sv', R.identity), unsorted);

    R.sort(R.ascend(R.identity), unsorted);
```


## assoc Object

Idx → a → {k: v} → {k: v}

Idx = String | Int

Parameters

- prop The property name to set
- val The new value
- obj The object to clone

Returns

Object

A new object equivalent to the original except for the changed property.

Added in v0.8.0

Makes a shallow clone of an object, setting or overriding the specified property with the given value. Note that this copies and flattens prototype properties onto the new object as well. All non-primitive properties are copied by reference.

See also

dissoc

,

pick

.

```
R.assoc('c', 3, {a: 1, b: 2}); 

R.assoc(4, 3, [1, 2]); 
R.assoc(-1, 3, [1, 2]); 
```


## assocPath Object

[Idx] → a → {a} → {a}

Idx = String | Int | Symbol

Parameters

- path the path to set
- val The new value
- obj The object to clone

Returns

Object

A new object equivalent to the original except along the specified path.

Added in v0.8.0

Makes a shallow clone of an object, setting or overriding the nodes required to create the given path, and placing the specific value at the tail end of that path. Note that this copies and flattens prototype properties onto the new object as well. All non-primitive properties are copied by reference.

See also

dissocPath

.

```
R.assocPath(['a', 'b', 'c'], 42, {a: {b: {c: 0}}}); 

R.assocPath(['a', 'b', 'c'], 42, {a: 5}); 
R.assocPath(['a', 1, 'c'], 42, {a: []}); 
R.assocPath(['a', -1], 42, {a: [1, 2]}); 
```


## binary Function

(a → b → c → … → z) → ((a, b) → z)

Parameters

- fn The function to wrap.

Returns

function

A new function wrapping `fn`. The new function is guaranteed to be of arity 2.

Added in v0.2.0

Wraps a function of any arity (including nullary) in a function that accepts exactly 2 parameters. Any extraneous parameters will not be passed to the supplied function.

See also

nAry

,

unary

.

```
const takesThreeArgs = function(a, b, c) {
  return [a, b, c];
};
takesThreeArgs.length; 
takesThreeArgs(1, 2, 3); 

const takesTwoArgs = R.binary(takesThreeArgs);
takesTwoArgs.length; 

takesTwoArgs(1, 2, 3); 
```


## bind Function

(* → *) → {*} → (* → *)

Parameters

- fn The function to bind to context
- thisObj The context to bind `fn` to

Returns

function

A function that will execute in the context of `thisObj`.

Added in v0.6.0

Creates a function that is bound to a context. Note: `R.bind` does not provide the additional argument-binding capabilities of Function.prototype.bind.

See also

partial

.

```
const log = R.bind(console.log, console);
R.pipe(R.assoc('a', 2), R.tap(log), R.assoc('a', 3))({a: 1}); 
```


## both Logic

(*… → Boolean) → (*… → Boolean) → (*… → Boolean)

Parameters

- f A predicate
- g Another predicate

Returns

function

a function that applies its arguments to `f` and `g` and `&&`s their outputs together.

Added in v0.12.0

A function which calls the two provided functions and returns the `&&` of the results. It returns the result of the first function if it is false-y and the result of the second function otherwise. Note that this is short-circuited, meaning that the second function will not be invoked if the first returns a false-y value.

In addition to functions, `R.both` also accepts any fantasy-land compatible applicative functor.

See also

either

,

allPass

,

and

.

```
const gt10 = R.gt(R.__, 10)
const lt20 = R.lt(R.__, 20)
const f = R.both(gt10, lt20);
f(15); 
f(30); 

R.both(Maybe.Just(false), Maybe.Just(55)); 
R.both([false, false, 'a'], [11]); 
```


## call Function

((*… → a), *…) → a

Parameters

- fn The function to apply to the remaining arguments.
- args Any number of positional arguments.

Returns

*

Added in v0.9.0

Returns the result of calling its first argument with the remaining arguments. This is occasionally useful as a converging function for `R.converge`: the first branch can produce a function while the remaining branches produce values to be passed to that function as its arguments.

See also

apply

.

```
R.call(R.add, 1, 2); 

const indentN = R.pipe(
  R.repeat(' '),
  R.join(''),
  R.replace(/^(?!$)/gm)
);

const format = R.converge(
  R.call,
  [
    R.pipe(R.prop('indent'), indentN),
    R.prop('value')
  ]
);

format({indent: 2, value: 'foo\nbar\nbaz\n'}); 
```


## chain List

Chain m => (a → m b) → m a → m b

Parameters

- fn The function to map with
- list The list to map over

Returns

Array

The result of flat-mapping `list` with `fn`

Added in v0.3.0

`chain` maps a function over a list and concatenates the results. `chain` is also known as `flatMap` in some libraries.

Dispatches to the `chain` method of the second argument, if present, according to the FantasyLand Chain spec.

If second argument is a function, `chain(f, g)(x)` is equivalent to `f(g(x), x)`.

Acts as a transducer if a transformer is given in list position.

```
const duplicate = n => [n, n];
R.chain(duplicate, [1, 2, 3]); 

R.chain(R.append, R.head)([1, 2, 3]); 
```


## clamp Relation

Ord a => a → a → a → a

Parameters

- minimum The lower limit of the clamp (inclusive)
- maximum The upper limit of the clamp (inclusive)
- value Value to be clamped

Returns

Number

Returns `minimum` when `val

<

minimum`, `maximum` when `val > maximum`, returns `val` otherwise

Added in v0.20.0

Restricts a number to be within a range.

Also works for other ordered types such as Strings and Dates.

```
R.clamp(1, 10, -5) 
R.clamp(1, 10, 15) 
R.clamp(1, 10, 4)  
```


## clone Object

{*} → {*}

Parameters

- value The object or array to clone

Returns

*

A deeply cloned copy of `val`

Added in v0.1.0

Creates a deep copy of the source that can be used in place of the source object without retaining any references to it. The source object may contain (nested) `Array`s and `Object`s, `Number`s, `String`s, `Boolean`s and `Date`s. `Function`s are assigned by reference rather than copied.

Dispatches to a `clone` method if present.

Note that if the source object has multiple nodes that share a reference, the returned object will have the same structure, but the references will be pointed to the location within the cloned value.

```
const objects = [{}, {}, {}];
const objectsClone = R.clone(objects);
objects === objectsClone; 
objects[0] === objectsClone[0]; 
```


## collectBy List

Idx a => (b → a) → [b] → [[b]]

Idx = String | Int | Symbol

Parameters

- fn Function :: a -> Idx
- list The array to group

Returns

Array

An array of arrays where each sub-array contains items for which the String-returning function has returned the same value.

Added in v0.28.0

Splits a list into sub-lists, based on the result of calling a key-returning function on each element, and grouping the results according to values returned.

See also

groupBy

,

partition

.

```
R.collectBy(R.prop('type'), [
  {type: 'breakfast', item: '☕️'},
  {type: 'lunch', item: '🌯'},
  {type: 'dinner', item: '🍝'},
  {type: 'breakfast', item: '🥐'},
  {type: 'lunch', item: '🍕'}
]);
```


## comparator Function

((a, b) → Boolean) → ((a, b) → Number)

Parameters

- pred A predicate function of arity two which will return `true` if the first argument is less than the second, `false` otherwise

Returns

function

A Function :: a -> b -> Int that returns `-1` if a

<

b, `1` if b

<

a, otherwise `0`

Added in v0.1.0

Makes a comparator function out of a function that reports whether the first element is less than the second.

```
const byAge = R.comparator((a, b) => a.age < b.age);
const people = [
  { name: 'Emma', age: 70 },
  { name: 'Peter', age: 78 },
  { name: 'Mikhail', age: 62 },
];
const peopleByIncreasingAge = R.sort(byAge, people);
  
```


## complement Logic

(*… → *) → (*… → Boolean)

Parameters

- f

Returns

function

Added in v0.12.0

Takes a function `f` and returns a function `g` such that if called with the same arguments when `f` returns a "truthy" value, `g` returns `false` and when `f` returns a "falsy" value `g` returns `true`.

`R.complement` may be applied to any functor

See also

not

.

```
const isNotNil = R.complement(R.isNil);
R.isNil(null); 
isNotNil(null); 
R.isNil(7); 
isNotNil(7); 
```


## compose Function

((y → z), (x → y), …, (o → p), ((a, b, …, n) → o)) → ((a, b, …, n) → z)

Parameters

- ...functions The functions to compose

Returns

function

Added in v0.1.0

Performs right-to-left function composition. The last argument may have any arity; the remaining arguments must be unary.

**Note:** The result of compose is not automatically curried.

See also

pipe

.

```
const classyGreeting = (firstName, lastName) => "The name's " + lastName + ", " + firstName + " " + lastName
const yellGreeting = R.compose(R.toUpper, classyGreeting);
yellGreeting('James', 'Bond'); 

R.compose(Math.abs, R.add(1), R.multiply(2))(-4) 
```


## composeWith Function

((* → *), [(y → z), (x → y), …, (o → p), ((a, b, …, n) → o)]) → ((a, b, …, n) → z)

Parameters

- transformer The transforming function
- functions The functions to compose

Returns

function

Added in v0.26.0

Performs right-to-left function composition using transforming function. The last function may have any arity; the remaining functions must be unary. Unlike `compose`, functions are passed in an array.

**Note:** The result of composeWith is not automatically curried. Transforming function is not used on the last argument.

See also

compose

,

pipeWith

.

```
const composeWhileNotNil = R.composeWith((f, res) => R.isNil(res) ? res : f(res));

composeWhileNotNil([R.inc, R.prop('age')])({age: 1}) 
composeWhileNotNil([R.inc, R.prop('age')])({}) 
```


## concat List

[a] → [a] → [a]

String → String → String

Parameters

- firstList The first list
- secondList The second list

Returns

Array

A list consisting of the elements of `firstList` followed by the elements of `secondList`.

Added in v0.1.0

Returns the result of concatenating the given lists or strings.

Note: `R.concat` expects both arguments to be of the same type, unlike the native `Array.prototype.concat` method. It will throw an error if you `concat` an Array with a non-Array value.

Dispatches to the `concat` method of the first argument, if present. Can also concatenate two members of a fantasy-land compatible semigroup.

```
R.concat('ABC', 'DEF'); 
R.concat([4, 5, 6], [1, 2, 3]); 
R.concat([], []); 
```


## cond Logic

[[(*… → Boolean),(*… → *)]] → (*… → *)

Parameters

- pairs A list of [predicate, transformer]

Returns

function

Added in v0.6.0

Returns a function, `fn`, which encapsulates `if/else, if/else, ...` logic. `R.cond` takes a list of [predicate, transformer] pairs. All of the arguments to `fn` are applied to each of the predicates in turn until one returns a "truthy" value, at which point `fn` returns the result of applying its arguments to the corresponding transformer. If none of the predicates matches, `fn` returns undefined.

**Please note**: This is not a direct substitute for a `switch` statement. Remember that both elements of every pair passed to `cond` are *functions*, and `cond` returns a function.

See also

ifElse

,

unless

,

when

.

```
const fn = R.cond([
  [R.equals(0),   R.always('water freezes at 0°C')],
  [R.equals(100), R.always('water boils at 100°C')],
  [R.T,           temp => 'nothing special happens at ' + temp + '°C']
]);
fn(0); 
fn(50); 
fn(100); 
```


## construct Function

(* → {*}) → (* → {*})

Parameters

- fn The constructor function to wrap.

Returns

function

A wrapped, curried constructor function.

Added in v0.1.0

Wraps a constructor function inside a curried function that can be called with the same arguments and returns the same type.

See also

invoker

.

```
function Animal(kind) {
  this.kind = kind;
};
Animal.prototype.sighting = function() {
  return "It's a " + this.kind + "!";
}

const AnimalConstructor = R.construct(Animal)

AnimalConstructor('Pig'); 

const animalTypes = ["Lion", "Tiger", "Bear"];
const animalSighting = R.invoker(0, 'sighting');
const sightNewAnimal = R.compose(animalSighting, AnimalConstructor);
R.map(sightNewAnimal, animalTypes); 
```


## constructN Function

Number → (* → {*}) → (* → {*})

Parameters

- n The arity of the constructor function.
- Fn The constructor function to wrap.

Returns

function

A wrapped, curried constructor function.

Added in v0.4.0

Wraps a constructor function inside a curried function that can be called with the same arguments and returns the same type. The arity of the function returned is specified to allow using variadic constructor functions.

```
function Salad() {
  this.ingredients = arguments;
}

Salad.prototype.recipe = function() {
  const instructions = R.map(ingredient => 'Add a dollop of ' + ingredient, this.ingredients);
  return R.join('\n', instructions);
};

const ThreeLayerSalad = R.constructN(3, Salad);

const salad = ThreeLayerSalad('Mayonnaise')('Potato Chips')('Ketchup');

console.log(salad.recipe());
```


## converge Function

((x1, x2, …) → z) → [((a, b, …) → x1), ((a, b, …) → x2), …] → (a → b → … → z)

Parameters

- after A function. `after` will be invoked with the return values of `fn1` and `fn2` as its arguments.
- functions A list of functions.

Returns

function

A new function.

Added in v0.4.2

Accepts a converging function and a list of branching functions and returns a new function. The arity of the new function is the same as the arity of the longest branching function. When invoked, this new function is applied to some arguments, and each branching function is applied to those same arguments. The results of each branching function are passed as arguments to the converging function to produce the return value.

See also

useWith

.

```
const average = R.converge(R.divide, [R.sum, R.length])
average([1, 2, 3, 4, 5, 6, 7]) 

const strangeConcat = R.converge(R.concat, [R.toUpper, R.toLower])
strangeConcat("Yodel") 
```


## count List

(a → Boolean) → [a] → Number

Parameters

- predicate The function to match items against.
- list The list to count elements from.

Returns

Number

The count of items matching the predicate.

Added in v0.28.0

Returns the number of items in a given `list` matching the predicate `f`

```
const even = x => x % 2 == 0;

R.count(even, [1, 2, 3, 4, 5]); 
R.map(R.count(even), [[1, 1, 1], [2, 3, 4, 5], [6]]); 
```


## countBy Relation

(a → String) → [a] → {*}

Parameters

- fn The function used to map values to keys.
- list The list to count elements from.

Returns

Object

An object mapping keys to number of occurrences in the list.

Added in v0.1.0

Counts the elements of a list according to how many match each value of a key generated by the supplied function. Returns an object mapping the keys produced by `fn` to the number of occurrences in the list. Note that all keys are coerced to strings because of how JavaScript objects work.

Acts as a transducer if a transformer is given in list position.

```
const numbers = [1.0, 1.1, 1.2, 2.0, 3.0, 2.2];
R.countBy(Math.floor)(numbers);    

const letters = ['a', 'b', 'A', 'a', 'B', 'c'];
R.countBy(R.toLower)(letters);   
```


## curry Function

(* → a) → (* → a)

Parameters

- fn The function to curry.

Returns

function

A new, curried function.

Added in v0.1.0

Returns a curried equivalent of the provided function. The curried function has two unusual capabilities. First, its arguments needn't be provided one at a time. If `f` is a ternary function and `g` is `R.curry(f)`, the following are equivalent:

- `g(1)(2)(3)`
- `g(1)(2, 3)`
- `g(1, 2)(3)`
- `g(1, 2, 3)`

Secondly, the special placeholder value `R.__` may be used to specify "gaps", allowing partial application of any combination of arguments, regardless of their positions. If `g` is as above and `_` is `R.__`, the following are equivalent:

- `g(1, 2, 3)`
- `g(_, 2, 3)(1)`
- `g(_, _, 3)(1)(2)`
- `g(_, _, 3)(1, 2)`
- `g(_, 2)(1)(3)`
- `g(_, 2)(1, 3)`
- `g(_, 2)(_, 3)(1)`

Please note that default parameters don't count towards a function arity and therefore `curry` won't work well with those.

See also

curryN

,

partial

.

```
const addFourNumbers = (a, b, c, d) => a + b + c + d;
const curriedAddFourNumbers = R.curry(addFourNumbers);
const f = curriedAddFourNumbers(1, 2);
const g = f(3);
g(4); 

const h = R.curry((a, b, c = 2) => a + b + c);
h(1)(2)(7); 
```


## curryN Function

Number → (* → a) → (* → a)

Parameters

- length The arity for the returned function.
- fn The function to curry.

Returns

function

A new, curried function.

Added in v0.5.0

Returns a curried equivalent of the provided function, with the specified arity. The curried function has two unusual capabilities. First, its arguments needn't be provided one at a time. If `g` is `R.curryN(3, f)`, the following are equivalent:

- `g(1)(2)(3)`
- `g(1)(2, 3)`
- `g(1, 2)(3)`
- `g(1, 2, 3)`

Secondly, the special placeholder value `R.__` may be used to specify "gaps", allowing partial application of any combination of arguments, regardless of their positions. If `g` is as above and `_` is `R.__`, the following are equivalent:

- `g(1, 2, 3)`
- `g(_, 2, 3)(1)`
- `g(_, _, 3)(1)(2)`
- `g(_, _, 3)(1, 2)`
- `g(_, 2)(1)(3)`
- `g(_, 2)(1, 3)`
- `g(_, 2)(_, 3)(1)`

See also

curry

.

```
const sumArgs = (...args) => R.sum(args);

const curriedAddFourNumbers = R.curryN(4, sumArgs);
const f = curriedAddFourNumbers(1, 2);
const g = f(3);
g(4); 
```


## dec Math

Number → Number

Parameters

- n

Returns

Number

n - 1

Added in v0.9.0

Decrements its argument.

See also

inc

.

```
R.dec(42); 
```


## defaultTo Logic

a → b → a | b

Parameters

- default The default value.
- val `val` will be returned instead of `default` unless `val` is `null`, `undefined` or `NaN`.

Returns

*

The second value if it is not `null`, `undefined` or `NaN`, otherwise the default value

Added in v0.10.0

Returns the second argument if it is not `null`, `undefined` or `NaN`; otherwise the first argument is returned.

```
const defaultTo42 = R.defaultTo(42);

defaultTo42(null);  
defaultTo42(undefined);  
defaultTo42(false);  
defaultTo42('Ramda');  

defaultTo42(parseInt('string')); 
```


## descend Function

Ord b => (a → b) → a → a → Number

Parameters

- fn A function of arity one that returns a value that can be compared
- a The first item to be compared.
- b The second item to be compared.

Returns

Number

`-1` if fn(a) > fn(b), `1` if fn(b) > fn(a), otherwise `0`

Added in v0.23.0

Makes a descending comparator function out of a function that returns a value that can be compared with `<` and `>`.

See also

ascend

,

descendNatural

,

ascendNatural

.

```
const byAge = R.descend(R.prop('age'));
const people = [
  { name: 'Emma', age: 70 },
  { name: 'Peter', age: 78 },
  { name: 'Mikhail', age: 62 },
];
const peopleByOldestFirst = R.sort(byAge, people);
  
```


## descendNatural Function

s → (a → String) → a → a → Number

Parameters

- locales A string with a BCP 47 language tag, or an array of such strings. Corresponds to the locales parameter of the Intl.Collator() constructor.
- fn A function of arity one that returns a string that can be compared
- a The first item to be compared.
- b The second item to be compared.

Returns

Number

`-1` if a occurs after b, `1` if a occurs before b, otherwise `0`

Added in v0.30.1

Makes a descending comparator function out of a function that returns a value that can be compared with natural sorting using localeCompare.

See also

descend

.

```
const unsorted = ['3', '1', '10', 'Ørjan', 'Bob', 'Älva'];

R.sort(R.descendNatural('en', R.identity), unsorted);

R.sort(R.descendNatural('sv', R.identity), unsorted);

    R.sort(R.descend(R.identity), unsorted);
```


## difference Relation

[*] → [*] → [*]

Parameters

- list1 The first list.
- list2 The second list.

Returns

Array

The elements in `list1` that are not in `list2`.

Added in v0.1.0

Finds the set (i.e. no duplicates) of all elements in the first list not contained in the second list. Objects and Arrays are compared in terms of value equality, not reference equality.

See also

differenceWith

,

symmetricDifference

,

symmetricDifferenceWith

,

without

.

```
R.difference([1,2,3,4], [7,6,5,4,3]); 
R.difference([7,6,5,4,3], [1,2,3,4]); 
R.difference([{a: 1}, {b: 2}], [{a: 1}, {c: 3}]) 
```


## differenceWith Relation

((a, a) → Boolean) → [a] → [a] → [a]

Parameters

- pred A predicate used to test whether two items are equal.
- list1 The first list.
- list2 The second list.

Returns

Array

The elements in `list1` that are not in `list2`.

Added in v0.1.0

Finds the set (i.e. no duplicates) of all elements in the first list not contained in the second list. Duplication is determined according to the value returned by applying the supplied predicate to two list elements.

See also

difference

,

symmetricDifference

,

symmetricDifferenceWith

.

```
const cmp = (x, y) => x.a === y.a;
const l1 = [{a: 1}, {a: 2}, {a: 3}];
const l2 = [{a: 3}, {a: 4}];
R.differenceWith(cmp, l1, l2); 

R.differenceWith(R.equals, [1, 2, 3, 3, 3], []); 
R.differenceWith(R.equals, [1, 2, 3, 3, 3], [1]); 
```


## dissoc Object

String → {k: v} → {k: v}

Parameters

- prop The name of the property to dissociate
- obj The object to clone

Returns

Object

A new object equivalent to the original but without the specified property

Added in v0.10.0

Returns a new object that does not contain a `prop` property.

See also

assoc

,

omit

.

```
R.dissoc('b', {a: 1, b: 2, c: 3}); 
```


## dissocPath Object

[Idx] → {k: v} → {k: v}

Idx = String | Int | Symbol

Parameters

- path The path to the value to omit
- obj The object to clone

Returns

Object

A new object without the property at path

Added in v0.11.0

Makes a shallow clone of an object, omitting the property at the given path. Note that this copies and flattens prototype properties onto the new object as well. All non-primitive properties are copied by reference.

See also

assocPath

.

```
R.dissocPath(['a', 'b', 'c'], {a: {b: {c: 42}}}); 
```


## divide Math

Number → Number → Number

Parameters

- a The first value.
- b The second value.

Returns

Number

The result of `a / b`.

Added in v0.1.0

Divides two numbers. Equivalent to `a / b`.

See also

multiply

.

```
R.divide(71, 100); 

const half = R.divide(R.__, 2);
half(42); 

const reciprocal = R.divide(1);
reciprocal(4);   
```


## drop List

Number → [a] → [a]

Number → String → String

Parameters

- n
- list

Returns

*

A copy of list without the first `n` elements

Added in v0.1.0

Returns all but the first `n` elements of the given list, string, or transducer/transformer (or object with a `drop` method).

Dispatches to the `drop` method of the second argument, if present.

See also

take

,

transduce

,

dropLast

,

dropWhile

.

```
R.drop(1, ['foo', 'bar', 'baz']); 
R.drop(2, ['foo', 'bar', 'baz']); 
R.drop(3, ['foo', 'bar', 'baz']); 
R.drop(4, ['foo', 'bar', 'baz']); 
R.drop(3, 'ramda');               
```


## dropLast List

Number → [a] → [a]

Number → String → String

Parameters

- n The number of elements of `list` to skip.
- list The list of elements to consider.

Returns

Array

A copy of the list with only the first `list.length - n` elements

Added in v0.16.0

Returns a list containing all but the last `n` elements of the given `list`.

Acts as a transducer if a transformer is given in list position.

See also

takeLast

,

drop

,

dropWhile

,

dropLastWhile

.

```
R.dropLast(1, ['foo', 'bar', 'baz']); 
R.dropLast(2, ['foo', 'bar', 'baz']); 
R.dropLast(3, ['foo', 'bar', 'baz']); 
R.dropLast(4, ['foo', 'bar', 'baz']); 
R.dropLast(3, 'ramda');               
```


## dropLastWhile List

(a → Boolean) → [a] → [a]

(a → Boolean) → String → String

Parameters

- predicate The function to be called on each element
- xs The collection to iterate over.

Returns

Array

A new array without any trailing elements that return `falsy` values from the `predicate`.

Added in v0.16.0

Returns a new list excluding all the tailing elements of a given list which satisfy the supplied predicate function. It passes each value from the right to the supplied predicate function, skipping elements until the predicate function returns a `falsy` value. The predicate function is applied to one argument: *(value)*.

Acts as a transducer if a transformer is given in list position.

See also

takeLastWhile

,

addIndex

,

drop

,

dropWhile

.

```
const lteThree = x => x <= 3;

R.dropLastWhile(lteThree, [1, 2, 3, 4, 3, 2, 1]); 

R.dropLastWhile(x => x !== 'd' , 'Ramda'); 
```


## dropRepeats List

[a] → [a]

Parameters

- list The array to consider.

Returns

Array

`list` without repeating elements.

Added in v0.14.0

Returns a new list without any consecutively repeating elements. `R.equals` is used to determine equality.

Acts as a transducer if a transformer is given in list position.

See also

transduce

.

```
R.dropRepeats([1, 1, 1, 2, 3, 4, 4, 2, 2]); 
```


## dropRepeatsBy List

(a → b) → [a] → [a]

Parameters

- fn A function used to produce a value to use during comparisons.
- list The array to consider.

Returns

Array

`list` without repeating elements.

Added in v0.29.0

Returns a new list without any consecutively repeating elements, based upon the value returned by applying the supplied function to each list element. `R.equals` is used to determine equality.

Acts as a transducer if a transformer is given in list position.

See also

transduce

.

```
R.dropRepeatsBy(Math.abs, [1, -1, -1, 2, 3, -4, 4, 2, 2]); 
```


## dropRepeatsWith List

((a, a) → Boolean) → [a] → [a]

Parameters

- pred A predicate used to test whether two items are equal.
- list The array to consider.

Returns

Array

`list` without repeating elements.

Added in v0.14.0

Returns a new list without any consecutively repeating elements. Equality is determined by applying the supplied predicate to each pair of consecutive elements. The first element in a series of equal elements will be preserved.

Acts as a transducer if a transformer is given in list position.

See also

transduce

.

```
const l = [1, -1, 1, 3, 4, -4, -4, -5, 5, 3, 3];
R.dropRepeatsWith(R.eqBy(Math.abs), l); 
```


## dropWhile List

(a → Boolean) → [a] → [a]

(a → Boolean) → String → String

Parameters

- fn The function called per iteration.
- xs The collection to iterate over.

Returns

Array

A new array.

Added in v0.9.0

Returns a new list excluding the leading elements of a given list which satisfy the supplied predicate function. It passes each value to the supplied predicate function, skipping elements while the predicate function returns `true`. The predicate function is applied to one argument: *(value)*.

Dispatches to the `dropWhile` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

takeWhile

,

transduce

,

addIndex

.

```
const lteTwo = x => x <= 2;

R.dropWhile(lteTwo, [1, 2, 3, 4, 3, 2, 1]); 

R.dropWhile(x => x !== 'd' , 'Ramda'); 
```


## either Logic

(*… → Boolean) → (*… → Boolean) → (*… → Boolean)

Parameters

- f a predicate
- g another predicate

Returns

function

a function that applies its arguments to `f` and `g` and `||`s their outputs together.

Added in v0.12.0

A function wrapping calls to the two functions in an `||` operation, returning the result of the first function if it is truth-y and the result of the second function otherwise. Note that this is short-circuited, meaning that the second function will not be invoked if the first returns a truth-y value.

In addition to functions, `R.either` also accepts any fantasy-land compatible applicative functor.

See also

both

,

anyPass

,

or

.

```
const gt10 = x => x > 10;
const even = x => x % 2 === 0;
const f = R.either(gt10, even);
f(101); 
f(8); 

R.either(Maybe.Just(false), Maybe.Just(55)); 
R.either([false, false, 'a'], [11]) 
```


## empty Function

a → a

Parameters

- x

Returns

*

Added in v0.3.0

Returns the empty value of its argument's type. Ramda defines the empty value of Array (`[]`), Object (`{}`), String (`''`), Map (`new Map()`), Set (`new Set()`), TypedArray (`Uint8Array []`, `Float32Array []`, etc), and Arguments. Other types are supported if they define `<Type>.empty`, `<Type>.prototype.empty` or implement the FantasyLand Monoid spec.

Dispatches to the `empty` method of the first argument, if present.

```
R.empty(Just(42));               
R.empty([1, 2, 3]);              
R.empty('unicorns');             
R.empty({x: 1, y: 2});           
R.empty(Uint8Array.from('123')); 
R.empty(Set);                    
```


## endsWith List

[a] → [a] → Boolean

String → String → Boolean

Parameters

- suffix
- list

Returns

Boolean

Added in v0.24.0

Checks if a list ends with the provided sublist.

Similarly, checks if a string ends with the provided substring.

See also

startsWith

.

```
R.endsWith('c', 'abc')                
R.endsWith('b', 'abc')                
R.endsWith(['c'], ['a', 'b', 'c'])    
R.endsWith(['b'], ['a', 'b', 'c'])    
```


## eqBy Relation

(a → b) → a → a → Boolean

Parameters

- f
- x
- y

Returns

Boolean

Added in v0.18.0

Takes a function and two values in its domain and returns `true` if the values map to the same value in the codomain; `false` otherwise.

```
R.eqBy(Math.abs, 5, -5); 
```


## eqProps Object

k → {k: v} → {k: v} → Boolean

Parameters

- prop The name of the property to compare
- obj1
- obj2

Returns

Boolean

Added in v0.1.0

Reports whether two objects have the same value, in `R.equals` terms, for the specified property. Useful as a curried predicate.

```
const o1 = { a: 1, b: 2, c: 3, d: 4 };
const o2 = { a: 10, b: 20, c: 3, d: 40 };
R.eqProps('a', o1, o2); 
R.eqProps('c', o1, o2); 
```


## equals Relation

a → b → Boolean

Parameters

- a
- b

Returns

Boolean

Added in v0.15.0

Returns `true` if its arguments are equivalent, `false` otherwise. Handles cyclical data structures.

Dispatches symmetrically to the `equals` methods of both arguments, if present.

```
R.equals(1, 1); 
R.equals(1, '1'); 
R.equals([1, 2, 3], [1, 2, 3]); 

const a = {}; a.v = a;
const b = {}; b.v = b;
R.equals(a, b); 
```


## evolve Object

{k: (v → v)} → {k: v} → {k: v}

Parameters

- transformations The object specifying transformation functions to apply to the object.
- object The object to be transformed.

Returns

Object

The transformed object.

Added in v0.9.0

Creates a new object by recursively evolving a shallow copy of `object`, according to the `transformation` functions. All non-primitive properties are copied by reference.

A `transformation` function will not be invoked if its corresponding key does not exist in the evolved object.

```
const tomato = {firstName: '  Tomato ', data: {elapsed: 100, remaining: 1400}, id:123};
const transformations = {
  firstName: R.trim,
  lastName: R.trim, 
  data: {elapsed: R.add(1), remaining: R.add(-1)}
};
R.evolve(transformations, tomato); 
```


## F Function

* → Boolean

Parameters

Returns

Boolean

Added in v0.9.0

A function that always returns `false`. Any passed in parameters are ignored.

See also

T

.

```
R.F(); 
```


## filter List

Filterable f => (a → Boolean) → f a → f a

Parameters

- pred
- filterable

Returns

Array

Filterable

Added in v0.1.0

Takes a predicate and a `Filterable`, and returns a new filterable of the same type containing the members of the given filterable which satisfy the given predicate. Filterable objects include plain objects, Maps, or any object that has a filter method such as `Array`.

Dispatches to the `filter` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

reject

,

transduce

,

addIndex

.

```
const isEven = n => n % 2 === 0;

R.filter(isEven, [1, 2, 3, 4]); 

R.filter(isEven, {a: 1, b: 2, c: 3, d: 4}); 
```


## find List

(a → Boolean) → [a] → a | undefined

Parameters

- fn The predicate function used to determine if the element is the desired one.
- list The array to consider.

Returns

Object

The element found, or `undefined`.

Added in v0.1.0

Returns the first element of the list which matches the predicate, or `undefined` if no element matches.

Dispatches to the `find` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

transduce

.

```
const xs = [{a: 1}, {a: 2}, {a: 3}];
R.find(R.propEq(2, 'a'))(xs); 
R.find(R.propEq(4, 'a'))(xs); 
```


## findIndex List

(a → Boolean) → [a] → Number

Parameters

- fn The predicate function used to determine if the element is the desired one.
- list The array to consider.

Returns

Number

The index of the element found, or `-1`.

Added in v0.1.1

Returns the index of the first element of the list which matches the predicate, or `-1` if no element matches.

Acts as a transducer if a transformer is given in list position.

See also

transduce

,

indexOf

.

```
const xs = [{a: 1}, {a: 2}, {a: 3}];
R.findIndex(R.propEq(2, 'a'))(xs); 
R.findIndex(R.propEq(4, 'a'))(xs); 
```


## findLast List

(a → Boolean) → [a] → a | undefined

Parameters

- fn The predicate function used to determine if the element is the desired one.
- list The array to consider.

Returns

Object

The element found, or `undefined`.

Added in v0.1.1

Returns the last element of the list which matches the predicate, or `undefined` if no element matches.

Acts as a transducer if a transformer is given in list position.

See also

transduce

.

```
const xs = [{a: 1, b: 0}, {a:1, b: 1}];
R.findLast(R.propEq(1, 'a'))(xs); 
R.findLast(R.propEq(4, 'a'))(xs); 
```


## findLastIndex List

(a → Boolean) → [a] → Number

Parameters

- fn The predicate function used to determine if the element is the desired one.
- list The array to consider.

Returns

Number

The index of the element found, or `-1`.

Added in v0.1.1

Returns the index of the last element of the list which matches the predicate, or `-1` if no element matches.

Acts as a transducer if a transformer is given in list position.

See also

transduce

,

lastIndexOf

.

```
const xs = [{a: 1, b: 0}, {a:1, b: 1}];
R.findLastIndex(R.propEq(1, 'a'))(xs); 
R.findLastIndex(R.propEq(4, 'a'))(xs); 
```


## flatten List

[a] → [b]

Parameters

- list The array to consider.

Returns

Array

The flattened list.

Added in v0.1.0

Returns a new list by pulling every item out of it (and all its sub-arrays) and putting them in a new array, depth-first.

See also

unnest

.

```
R.flatten([1, 2, [3, 4], 5, [6, [7, 8, [9, [10, 11], 12]]]]);
```


## flip Function

((a, b, c, …) → z) → (b → a → c → … → z)

Parameters

- fn The function to invoke with its first two parameters reversed.

Returns

*

The result of invoking `fn` with its first two parameters' order reversed.

Added in v0.1.0

Returns a new function much like the supplied one, except that the first two arguments' order is reversed.

```
const mergeThree = (a, b, c) => [].concat(a, b, c);

mergeThree(1, 2, 3); 

R.flip(mergeThree)(1, 2, 3); 
```
