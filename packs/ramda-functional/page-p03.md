---
title: "Ramda Documentation (part 3/4)"
source: https://ramdajs.com/docs/
domain: ramda-functional
license: CC-BY-SA-4.0
tags: ramda functional, point-free style, javascript currying, immutable pipeline
fetched: 2026-07-02
part: 3/4
---

## once Function

(a… → b) → (a… → b)

Parameters

- fn The function to wrap in a call-only-once wrapper.

Returns

function

The wrapped function.

Added in v0.1.0

Accepts a function `fn` and returns a function that guards invocation of `fn` such that `fn` can only ever be called once, no matter how many times the returned function is invoked. The first value calculated is returned in subsequent invocations.

```
const addOneOnce = R.once(x => x + 1);
addOneOnce(10); 
addOneOnce(addOneOnce(50)); 
```


## or Logic

a → b → a | b

Parameters

- a
- b

Returns

Any

Added in v0.1.0

Returns the first argument if it is truthy, otherwise the second argument. Acts as the boolean `or` statement if both inputs are `Boolean`s.

See also

either

,

and

.

```
R.or(true, true); 
R.or(true, false); 
R.or(false, true); 
R.or(false, false); 
```


## otherwise Function

(e → b) → (Promise e a) → (Promise e b)

(e → (Promise f b)) → (Promise e a) → (Promise f b)

Parameters

- onFailure The function to apply. Can return a value or a promise of a value.
- p

Returns

Promise

The result of calling `p.then(null, onFailure)`

Added in v0.26.0

Returns the result of applying the onFailure function to the value inside a failed promise. This is useful for handling rejected promises inside function compositions.

See also

andThen

.

```
const failedFetch = id => Promise.reject('bad ID');
const useDefault = () => ({ firstName: 'Bob', lastName: 'Loblaw' });

const recoverFromFailure = R.pipe(
  failedFetch,
  R.otherwise(useDefault),
  R.andThen(R.pick(['firstName', 'lastName'])),
);
recoverFromFailure(12345).then(console.log);
```


## over Object

Lens s a → (a → a) → s → s

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- lens
- v
- x

Returns

*

Added in v0.16.0

Returns the result of "setting" the portion of the given data structure focused by the given lens to the result of applying the given function to the focused value.

See also

view

,

set

,

lens

,

lensIndex

,

lensProp

,

lensPath

.

```
const headLens = R.lensIndex(0);

R.over(headLens, R.toUpper, ['foo', 'bar', 'baz']); 
```


## pair List

a → b → (a,b)

Parameters

- fst
- snd

Returns

Array

Added in v0.18.0

Takes two arguments, `fst` and `snd`, and returns `[fst, snd]`.

See also

objOf

,

of

.

```
R.pair('foo', 'bar'); 
```


## partial Function

((a, b, c, …, n) → x) → [a, b, c, …] → ((d, e, f, …, n) → x)

Parameters

- f
- args

Returns

function

Added in v0.10.0

Takes a function `f` and a list of arguments, and returns a function `g`. When applied, `g` returns the result of applying `f` to the arguments provided initially followed by the arguments provided to `g`.

See also

partialRight

,

curry

.

```
const multiply2 = (a, b) => a * b;
const double = R.partial(multiply2, [2]);
double(3); 

const greet = (salutation, title, firstName, lastName) =>
  salutation + ', ' + title + ' ' + firstName + ' ' + lastName + '!';

const sayHello = R.partial(greet, ['Hello']);
const sayHelloToMs = R.partial(sayHello, ['Ms.']);
sayHelloToMs('Jane', 'Jones'); 
```


## partialObject Function

(({ a, b, c, …, n }) → x) → { a, b, c, …} → ({ d, e, f, …, n } → x)

Parameters

- f
- props

Returns

function

Added in v0.28.0

Takes a function `f` and an object, and returns a function `g`. When applied, `g` returns the result of applying `f` to the object provided initially merged deeply (right) with the object provided as an argument to `g`.

See also

partial

,

partialRight

,

curry

,

mergeDeepRight

.

```
const multiply2 = ({ a, b }) => a * b;
const double = R.partialObject(multiply2, { a: 2 });
double({ b: 2 }); 

const greet = ({ salutation, title, firstName, lastName }) =>
  salutation + ', ' + title + ' ' + firstName + ' ' + lastName + '!';

const sayHello = R.partialObject(greet, { salutation: 'Hello' });
const sayHelloToMs = R.partialObject(sayHello, { title: 'Ms.' });
sayHelloToMs({ firstName: 'Jane', lastName: 'Jones' }); 
```


## partialRight Function

((a, b, c, …, n) → x) → [d, e, f, …, n] → ((a, b, c, …) → x)

Parameters

- f
- args

Returns

function

Added in v0.10.0

Takes a function `f` and a list of arguments, and returns a function `g`. When applied, `g` returns the result of applying `f` to the arguments provided to `g` followed by the arguments provided initially.

See also

partial

.

```
const greet = (salutation, title, firstName, lastName) =>
  salutation + ', ' + title + ' ' + firstName + ' ' + lastName + '!';

const greetMsJaneJones = R.partialRight(greet, ['Ms.', 'Jane', 'Jones']);

greetMsJaneJones('Hello'); 
```


## partition List

Filterable f => (a → Boolean) → f a → [f a, f a]

Parameters

- pred A predicate to determine which side the element belongs to.
- filterable the list (or other filterable) to partition.

Returns

Array

An array, containing first the subset of elements that satisfy the predicate, and second the subset of elements that do not satisfy.

Added in v0.1.4

Takes a predicate and a list or other `Filterable` object and returns the pair of filterable objects of the same type of elements which do and do not satisfy, the predicate, respectively. Filterable objects include plain objects or any object that has a filter method such as `Array`.

See also

filter

,

reject

.

```
R.partition(R.includes('s'), ['sss', 'ttt', 'foo', 'bars']);

R.partition(R.includes('s'), { a: 'sss', b: 'ttt', foo: 'bars' });
```


## path Object

[Idx] → {a} → a | Undefined

Idx = String | NonNegativeInt

Idx = String | Int | Symbol

Parameters

- path The path to use.
- obj The object or array to retrieve the nested property from.

Returns

*

The data at `path`.

Added in v0.2.0

Retrieves the value at a given path. The nodes of the path can be arbitrary strings or non-negative integers. For anything else, the value is unspecified. Integer paths are meant to index arrays, strings are meant for objects.

See also

prop

,

nth

,

assocPath

,

dissocPath

.

```
R.path(['a', 'b'], {a: {b: 2}}); 
R.path(['a', 'b'], {c: {b: 2}}); 
R.path(['a', 'b', 0], {a: {b: [1, 2, 3]}}); 
R.path(['a', 'b', -2], {a: {b: [1, 2, 3]}}); 
R.path([2], {'2': 2}); 
R.path([-2], {'-2': 'a'}); 
```


## pathEq Relation

a → [Idx] → {a} → Boolean

Idx = String | Int | Symbol

Parameters

- val The value to compare the nested property with
- path The path of the nested property to use
- obj The object to check the nested property in

Returns

Boolean

`true` if the value equals the nested object property, `false` otherwise.

Added in v0.7.0

Determines whether a nested path on an object has a specific value, in `R.equals` terms. Most likely used to filter a list.

See also

whereEq

,

propEq

,

pathSatisfies

,

equals

.

```
const user1 = { address: { zipCode: 90210 } };
const user2 = { address: { zipCode: 55555 } };
const user3 = { name: 'Bob' };
const users = [ user1, user2, user3 ];
const isFamous = R.pathEq(90210, ['address', 'zipCode']);
R.filter(isFamous, users); 
```


## pathOr Object

a → [Idx] → {a} → a

Idx = String | Int | Symbol

Parameters

- d The default value.
- p The path to use.
- obj The object to retrieve the nested property from.

Returns

*

The data at `path` of the supplied object or the default value.

Added in v0.18.0

If the given, non-null object has a value at the given path, returns the value at that path. Otherwise returns the provided default value.

```
R.pathOr('N/A', ['a', 'b'], {a: {b: 2}}); 
R.pathOr('N/A', ['a', 'b'], {c: {b: 2}}); 
```


## paths Object

[Idx] → {a} → [a | Undefined]

Idx = [String | Int | Symbol]

Parameters

- pathsArray The array of paths to be fetched.
- obj The object to retrieve the nested properties from.

Returns

Array

A list consisting of values at paths specified by "pathsArray".

Added in v0.27.1

Retrieves the values at given paths of an object.

See also

path

.

```
R.paths([['a', 'b'], ['p', 0, 'q']], {a: {b: 2}, p: [{q: 3}]}); 
R.paths([['a', 'b'], ['p', 'r']], {a: {b: 2}, p: [{q: 3}]}); 
```


## pathSatisfies Logic

(a → Boolean) → [Idx] → {a} → Boolean

Idx = String | Int | Symbol

Parameters

- pred
- propPath
- obj

Returns

Boolean

Added in v0.19.0

Returns `true` if the specified object property at given path satisfies the given predicate; `false` otherwise.

See also

propSatisfies

,

path

.

```
R.pathSatisfies(y => y > 0, ['x', 'y'], {x: {y: 2}}); 
R.pathSatisfies(R.is(Object), [], {x: {y: 2}}); 
```


## pick Object

[k] → {k: v} → {k: v}

Parameters

- names an array of String property names to copy onto a new object
- obj The object to copy from

Returns

Object

A new object with only properties from `names` on it.

Added in v0.1.0

Returns a partial copy of an object containing only the keys specified. If the key does not exist, the property is ignored.

See also

omit

,

props

.

```
R.pick(['a', 'd'], {a: 1, b: 2, c: 3, d: 4}); 
R.pick(['a', 'e', 'f'], {a: 1, b: 2, c: 3, d: 4}); 
```


## pickAll Object

[k] → {k: v} → {k: v}

Parameters

- names an array of String property names to copy onto a new object
- obj The object to copy from

Returns

Object

A new object with only properties from `names` on it.

Added in v0.1.0

Similar to `pick` except that this one includes a `key: undefined` pair for properties that don't exist.

See also

pick

.

```
R.pickAll(['a', 'd'], {a: 1, b: 2, c: 3, d: 4}); 
R.pickAll(['a', 'e', 'f'], {a: 1, b: 2, c: 3, d: 4}); 
```


## pickBy Object

((v, k) → Boolean) → {k: v} → {k: v}

Parameters

- pred A predicate to determine whether or not a key should be included on the output object.
- obj The object to copy from

Returns

Object

A new object with only properties that satisfy `pred` on it.

Added in v0.8.0

Returns a partial copy of an object containing only the keys that satisfy the supplied predicate.

See also

pick

,

filter

.

```
const isUpperCase = (val, key) => key.toUpperCase() === key;
R.pickBy(isUpperCase, {a: 1, b: 2, A: 3, B: 4}); 
```


## pipe Function

(((a, b, …, n) → o), (o → p), …, (x → y), (y → z)) → ((a, b, …, n) → z)

Parameters

- functions

Returns

function

Added in v0.1.0

Performs left-to-right function composition. The first argument may have any arity; the remaining arguments must be unary.

In some libraries this function is named `sequence`.

**Note:** The result of pipe is not automatically curried.

See also

compose

.

```
const f = R.pipe(Math.pow, R.negate, R.inc);

f(3, 4); 
```


## pipeWith Function

((* → *), [((a, b, …, n) → o), (o → p), …, (x → y), (y → z)]) → ((a, b, …, n) → z)

Parameters

- transformer The transforming function
- functions The functions to pipe

Returns

function

Added in v0.26.0

Performs left-to-right function composition using transforming function. The first function may have any arity; the remaining functions must be unary.

**Note:** The result of pipeWith is not automatically curried. Transforming function is not used on the first argument.

See also

andThen

,

composeWith

,

pipe

.


## pluck List

Functor f => k → f {k: v} → f v

Parameters

- key The key name to pluck off of each object.
- f The array or functor to consider.

Returns

Array

The list of values for the given key.

Added in v0.1.0

Returns a new list by plucking the same named property off all objects in the list supplied.

`pluck` will work on any functor in addition to arrays, as it is equivalent to `R.map(R.prop(k), f)`.

See also

project

,

prop

,

props

.

```
var getAges = R.pluck('age');
getAges([{name: 'fred', age: 29}, {name: 'wilma', age: 27}]); 

R.pluck(0, [[1, 2], [3, 4]]);               
R.pluck('val', {a: {val: 3}, b: {val: 5}}); 
```


## prepend List

a → [a] → [a]

Parameters

- el The item to add to the head of the output list.
- list The array to add to the tail of the output list.

Returns

Array

A new array.

Added in v0.1.0

Returns a new list with the given element at the front, followed by the contents of the list.

See also

append

.

```
R.prepend('fee', ['fi', 'fo', 'fum']); 
```


## product Math

[Number] → Number

Parameters

- list An array of numbers

Returns

Number

The product of all the numbers in the list.

Added in v0.1.0

Multiplies together all the elements of a list.

See also

reduce

.

```
R.product([2,4,6,8,100,1]); 
```


## project Object

[k] → [{k: v}] → [{k: v}]

Parameters

- props The property names to project
- objs The objects to query

Returns

Array

An array of objects with just the `props` properties.

Added in v0.1.0

Reasonable analog to SQL `select` statement.

See also

pluck

,

props

,

prop

.

```
const abby = {name: 'Abby', age: 7, hair: 'blond', grade: 2};
const fred = {name: 'Fred', age: 12, hair: 'brown', grade: 7};
const kids = [abby, fred];
R.project(['name', 'grade'], kids); 
```


## promap Function

(a → b) → (c → d) → (b → c) → (a → d)

Profunctor p => (a → b) → (c → d) → p b c → p a d

Parameters

- f The preprocessor function, a -> b
- g The postprocessor function, c -> d
- profunctor The profunctor instance to be promapped, e.g. b -> c

Returns

Profunctor

The new profunctor instance, e.g. a -> d

Added in v0.28.0

Takes two functions as pre- and post- processors respectively for a third function, i.e. `promap(f, g, h)(x) === g(h(f(x)))`.

Dispatches to the `promap` method of the third argument, if present, according to the FantasyLand Profunctor spec.

Acts as a transducer if a transformer is given in profunctor position.

See also

transduce

.

```
const decodeChar = R.promap(s => s.charCodeAt(), String.fromCharCode, R.add(-8))
const decodeString = R.promap(R.split(''), R.join(''), R.map(decodeChar))
decodeString("ziuli") 
```


## prop Object

Idx → {s: a} → a | Undefined

Idx = String | Int | Symbol

Parameters

- p The property name or array index
- obj The object to query

Returns

*

The value at `obj.p`.

Added in v0.1.0

Returns a function that when supplied an object returns the indicated property of that object, if it exists.

See also

path

,

props

,

pluck

,

project

,

nth

.

```
R.prop('x', {x: 100}); 
R.prop('x', {}); 
R.prop(0, [100]); 
R.compose(R.inc, R.prop('x'))({ x: 3 }) 
```


## propEq Relation

a → String → Object → Boolean

Parameters

- val The value to compare the property with
- name the specified object property's key
- obj The object to check the property in

Returns

Boolean

`true` if the value equals the specified object property, `false` otherwise.

Added in v0.1.0

Returns `true` if the specified object property is equal, in `R.equals` terms, to the given value; `false` otherwise. You can test multiple properties with `R.whereEq`, and test nested path property with `R.pathEq`.

See also

whereEq

,

pathEq

,

propSatisfies

,

equals

.

```
const abby = {name: 'Abby', age: 7, hair: 'blond'};
const fred = {name: 'Fred', age: 12, hair: 'brown'};
const rusty = {name: 'Rusty', age: 10, hair: 'brown'};
const alois = {name: 'Alois', age: 15, disposition: 'surly'};
const kids = [abby, fred, rusty, alois];
const hasBrownHair = R.propEq('brown', 'hair');
R.filter(hasBrownHair, kids); 
```


## propIs Type

Type → String → Object → Boolean

Parameters

- type
- name
- obj

Returns

Boolean

Added in v0.16.0

Returns `true` if the specified object property is of the given type; `false` otherwise.

See also

is

,

propSatisfies

.

```
R.propIs(Number, 'x', {x: 1, y: 2});  
R.propIs(Number, 'x', {x: 'foo'});    
R.propIs(Number, 'x', {});            
```


## propOr Object

a → String → Object → a

Parameters

- val The default value.
- p The name of the property to return.
- obj The object to query.

Returns

*

The value of given property of the supplied object or the default value.

Added in v0.6.0

Return the specified property of the given non-null object if the property is present and it's value is not `null`, `undefined` or `NaN`.

Otherwise the first argument is returned.

```
const alice = {
  name: 'ALICE',
  age: 101
};
const favorite = R.prop('favoriteLibrary');
const favoriteWithDefault = R.propOr('Ramda', 'favoriteLibrary');

favorite(alice);  
favoriteWithDefault(alice);  
```


## props Object

[k] → {k: v} → [v]

Parameters

- ps The property names to fetch
- obj The object to query

Returns

Array

The corresponding values or partially applied function.

Added in v0.1.0

Acts as multiple `prop`: array of keys in, array of values out. Preserves order.

See also

prop

,

pluck

,

project

.

```
R.props(['x', 'y'], {x: 1, y: 2}); 
R.props(['c', 'a', 'b'], {b: 2, a: 1}); 

const fullName = R.compose(R.join(' '), R.props(['first', 'last']));
fullName({last: 'Bullet-Tooth', age: 33, first: 'Tony'}); 
```


## propSatisfies Logic

(a → Boolean) → String → {String: a} → Boolean

Parameters

- pred
- name
- obj

Returns

Boolean

Added in v0.16.0

Returns `true` if the specified object property satisfies the given predicate; `false` otherwise. You can test multiple properties with `R.where`.

See also

where

,

propEq

,

propIs

.

```
R.propSatisfies(x => x > 0, 'x', {x: 1, y: 2}); 
```


## range List

Number → Number → [Number]

Parameters

- from The first number in the list.
- to One more than the last number in the list.

Returns

Array

The list of numbers in the set `[a, b)`.

Added in v0.1.0

Returns a list of numbers from `from` (inclusive) to `to` (exclusive).

```
R.range(1, 5);    
R.range(1, 5.5);  
R.range(1.5, 5.5);  
```


## rebuild List

([String, a] → [[String, b]]) → {k: a} → {k: b}

Parameters

- convert A function that converts a key and a value to an array of key-value arrays.
- obj The structure to convert

Returns

Array

A new object whose key-value pairs are the result of applying the `convert` function to every key-value pair in `obj`.

Added in v0.31.0

Transforms an object into a new one, applying to every key-value pair a function creating zero, one, or many new key-value pairs, and combining the results into a single object.

See also

map

,

mapKeys

,

renameKeys

.

```
R.rebuild((k, v) => [[k.toUpperCase(), v * v]], {a: 1, b: 2, c: 3}) 
```


## reduce List

((a, b) → a) → a → [b] → a

Parameters

- fn The iterator function. Receives two values, the accumulator and the current element from the array.
- acc The accumulator value.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.1.0

Returns a single item by iterating through the list, successively calling the iterator function and passing it an accumulator value and the current value from the array, and then passing the result to the next call.

The iterator function receives two values: *(acc, value)*. It may use `R.reduced` to shortcut the iteration.

The arguments' order of `reduceRight`'s iterator function is *(value, acc)*.

Note: `R.reduce` does not skip deleted or unassigned indices (sparse arrays), unlike the native `Array.prototype.reduce` method. For more details on this behavior, see: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#Description

Be cautious of mutating and returning the accumulator. If you reuse it across invocations, it will continue to accumulate onto the same value. The general recommendation is to always return a new value. If you can't do so for performance reasons, then be sure to reinitialize the accumulator on each invocation.

Dispatches to the `reduce` method of the third argument, if present. When doing so, it is up to the user to handle the `R.reduced` shortcuting, as this is not implemented by `reduce`.

See also

reduced

,

addIndex

,

reduceRight

.

```
R.reduce(R.subtract, 0, [1, 2, 3, 4]) 
```


## reduceBy List

((a, b) → a) → a → (b → String) → [b] → {String: a}

Parameters

- valueFn The function that reduces the elements of each group to a single value. Receives two values, accumulator for a particular group and the current element.
- acc The (initial) accumulator value for each group.
- keyFn The function that maps the list's element into a key.
- list The array to group.

Returns

Object

An object with the output of `keyFn` for keys, mapped to the output of `valueFn` for elements which produced that key when passed to `keyFn`.

Added in v0.20.0

Groups the elements of the list according to the result of calling the String-returning function `keyFn` on each element and reduces the elements of each group to a single value via the reducer function `valueFn`.

The value function receives two values: *(acc, value)*. It may use `R.reduced` to short circuit the iteration.

This function is basically a more general `groupBy` function.

Acts as a transducer if a transformer is given in list position.

See also

groupBy

,

reduce

,

reduced

.

```
const groupNames = (acc, {name}) => acc.concat(name)
const toGrade = ({score}) =>
  score < 65 ? 'F' :
  score < 70 ? 'D' :
  score < 80 ? 'C' :
  score < 90 ? 'B' : 'A'

var students = [
  {name: 'Abby', score: 83},
  {name: 'Bart', score: 62},
  {name: 'Curt', score: 88},
  {name: 'Dora', score: 92},
]

reduceBy(groupNames, [], toGrade, students)
```


## reduced List

a → *

Parameters

- x The final value of the reduce.

Returns

*

The wrapped value.

Added in v0.15.0

Returns a value wrapped to indicate that it is the final value of the reduce and transduce functions. The returned value should be considered a black box: the internal structure is not guaranteed to be stable.

This optimization is available to the below functions:

- `reduce`
- `reduceWhile`
- `reduceBy`
- `reduceRight`
- `transduce`

See also

reduce

,

reduceWhile

,

reduceBy

,

reduceRight

,

transduce

.

```
R.reduce(
 (acc, item) => item > 3 ? R.reduced(acc) : acc.concat(item),
 [],
 [1, 2, 3, 4, 5]) 
```


## reduceRight List

((a, b) → b) → b → [a] → b

Parameters

- fn The iterator function. Receives two values, the current element from the array and the accumulator.
- acc The accumulator value.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.1.0

Returns a single item by iterating through the list, successively calling the iterator function and passing it an accumulator value and the current value from the array, and then passing the result to the next call.

Similar to `reduce`, except moves through the input list from the right to the left.

The iterator function receives two values: *(value, acc)*, while the arguments' order of `reduce`'s iterator function is *(acc, value)*. `reduceRight` may use `reduced` to short circuit the iteration.

Note: `R.reduceRight` does not skip deleted or unassigned indices (sparse arrays), unlike the native `Array.prototype.reduceRight` method. For more details on this behavior, see: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#Description

Be cautious of mutating and returning the accumulator. If you reuse it across invocations, it will continue to accumulate onto the same value. The general recommendation is to always return a new value. If you can't do so for performance reasons, then be sure to reinitialize the accumulator on each invocation.

See also

reduce

,

addIndex

,

reduced

.

```
R.reduceRight(R.subtract, 0, [1, 2, 3, 4]) 
```


## reduceWhile List

((a, b) → Boolean) → ((a, b) → a) → a → [b] → a

Parameters

- pred The predicate. It is passed the accumulator and the current element.
- fn The iterator function. Receives two values, the accumulator and the current element.
- a The accumulator value.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.22.0

Like `reduce`, `reduceWhile` returns a single item by iterating through the list, successively calling the iterator function. `reduceWhile` also takes a predicate that is evaluated before each step. If the predicate returns `false`, it "short-circuits" the iteration and returns the current value of the accumulator. `reduceWhile` may alternatively be short-circuited via `reduced`.

See also

reduce

,

reduced

.

```
const isOdd = (acc, x) => x % 2 !== 0;
const xs = [1, 3, 5, 60, 777, 800];
R.reduceWhile(isOdd, R.add, 0, xs); 

const ys = [2, 4, 6]
R.reduceWhile(isOdd, R.add, 111, ys); 
```


## reject List

Filterable f => (a → Boolean) → f a → f a

Parameters

- pred
- filterable

Returns

Array

Added in v0.1.0

The complement of `filter`.

Acts as a transducer if a transformer is given in list position. Filterable objects include plain objects or any object that has a filter method such as `Array`.

See also

filter

,

transduce

,

addIndex

.

```
const isOdd = (n) => n % 2 !== 0;

R.reject(isOdd, [1, 2, 3, 4]); 

R.reject(isOdd, {a: 1, b: 2, c: 3, d: 4}); 
```


## remove List

Number → Number → [a] → [a]

Parameters

- start The position to start removing elements
- count The number of elements to remove
- list The list to remove from

Returns

Array

A new Array with `count` elements from `start` removed.

Added in v0.2.2

Removes the sub-list of `list` starting at index `start` and containing `count` elements. *Note that this is not destructive*: it returns a copy of the list with the changes. No lists have been harmed in the application of this function.

See also

without

.

```
R.remove(2, 3, [1,2,3,4,5,6,7,8]); 
```


## renameKeys Object

Object → Object → Object

Parameters

- mapping An object pairing existing keys with new ones
- obj A target object to convert

Returns

Object

The result of replacing existing keys with their mapping counterparts when such exist

Added in v0.31.0

Converts an object to a new one by changing all keys that are also found as keys in a mapping object to their corresponding values from that object.

See also

mapKeys

,

rebuild

.

```
var mapping = { name: 'firstName', address: 'street' };
var obj = { name: 'John', city: 'Paris' };

R.renameKeys(mapping, obj) 
```


## repeat List

a → n → [a]

Parameters

- value The value to repeat.
- n The desired size of the output list.

Returns

Array

A new array containing `n` `value`s.

Added in v0.1.1

Returns a fixed list of size `n` containing a specified identical value.

See also

times

.

```
R.repeat('hi', 5); 

const obj = {};
const repeatedObjs = R.repeat(obj, 5); 
repeatedObjs[0] === repeatedObjs[1]; 
```


## replace String

RegExp|String → String → String → String

Parameters

- pattern A regular expression or a substring to match.
- replacement The string to replace the matches with.
- str The String to do the search and replacement in.

Returns

String

The result.

Added in v0.7.0

Replace a substring or regex match in a string with a replacement.

The first two parameters correspond to the parameters of the `String.prototype.replace()` function, so the second parameter can also be a function.

```
R.replace('foo', 'bar', 'foo foo foo'); 
R.replace(/foo/, 'bar', 'foo foo foo'); 

R.replace(/foo/g, 'bar', 'foo foo foo'); 
```


## reverse List

[a] → [a]

String → String

Parameters

- list

Returns

Array

Added in v0.1.0

Returns a new list or string with the elements or characters in reverse order.

```
R.reverse([1, 2, 3]);  
R.reverse([1, 2]);     
R.reverse([1]);        
R.reverse([]);         

R.reverse('abc');      
R.reverse('ab');       
R.reverse('a');        
R.reverse('');         
```


## scan List

((a, b) → a) → a → [b] → [a]

Parameters

- fn The iterator function. Receives two values, the accumulator and the current element from the array
- acc The accumulator value.
- list The list to iterate over.

Returns

Array

A list of all intermediately reduced values.

Added in v0.10.0

Scan is similar to `reduce`, but returns a list of successively reduced values from the left.

Acts as a transducer if a transformer is given in list position.

See also

reduce

,

mapAccum

.

```
const numbers = [1, 2, 3, 4];
const factorials = R.scan(R.multiply, 1, numbers); 
```


## sequence List

fantasy-land/of :: TypeRep f => f ~> a → f a

(Applicative f, Traversable t) => TypeRep f → t (f a) → f (t a)

(Applicative f, Traversable t) => (a → f a) → t (f a) → f (t a)

Parameters

- TypeRepresentative with an `of` or `fantasy-land/of` method
- traversable

Returns

*

Added in v0.19.0

Transforms a Traversable of Applicative into an Applicative of Traversable.

Dispatches to the `"fantasy-land/traverse"` or the `traverse` method of the second argument, if present.

See also

traverse

.

```
R.sequence(Maybe.of, [Just(1), Just(2), Just(3)]);   
R.sequence(Maybe.of, [Just(1), Just(2), Nothing()]); 

R.sequence(R.of(Array), Just([1, 2, 3])); 
R.sequence(R.of(Array), Nothing());       
```


## set Object

Lens s a → a → s → s

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- lens
- v
- x

Returns

*

Added in v0.16.0

Returns the result of "setting" the portion of the given data structure focused by the given lens to the given value.

See also

view

,

over

,

lens

,

lensIndex

,

lensProp

,

lensPath

.

```
const xLens = R.lensProp('x');

R.set(xLens, 4, {x: 1, y: 2});  
R.set(xLens, 8, {x: 1, y: 2});  
```


## slice List

Number → Number → [a] → [a]

Number → Number → String → String

Parameters

- fromIndex The start index (inclusive).
- toIndex The end index (exclusive).
- list

Returns

*

Added in v0.1.4

Returns the elements of the given list or string (or object with a `slice` method) from `fromIndex` (inclusive) to `toIndex` (exclusive).

Dispatches to the `slice` method of the third argument, if present.

```
R.slice(1, 3, ['a', 'b', 'c', 'd']);        
R.slice(1, Infinity, ['a', 'b', 'c', 'd']); 
R.slice(0, -1, ['a', 'b', 'c', 'd']);       
R.slice(-3, -1, ['a', 'b', 'c', 'd']);      
R.slice(0, 3, 'ramda');                     
```


## sort List

((a, a) → Number) → [a] → [a]

Parameters

- comparator A sorting function :: a -> b -> Int
- list The list to sort

Returns

Array

a new array with its elements sorted by the comparator function.

Added in v0.1.0

Returns a copy of the list, sorted according to the comparator function, which should accept two values at a time and return a negative number if the first value is smaller, a positive number if it's larger, and zero if they are equal. Please note that this is a **copy** of the list. It does not modify the original.

See also

ascend

,

descend

.

```
const diff = function(a, b) { return a - b; };
R.sort(diff, [4,2,7,5]); 
```


## sortBy Relation

Ord b => (a → b) → [a] → [a]

Parameters

- fn
- list The list to sort.

Returns

Array

A new list sorted by the keys generated by `fn`.

Added in v0.1.0

Sorts the list according to the supplied function.

```
const sortByFirstItem = R.sortBy(R.prop(0));
const pairs = [[-1, 1], [-2, 2], [-3, 3]];
sortByFirstItem(pairs); 

const sortByNameCaseInsensitive = R.sortBy(R.compose(R.toLower, R.prop('name')));
const alice = {
  name: 'ALICE',
  age: 101
};
const bob = {
  name: 'Bob',
  age: -10
};
const clara = {
  name: 'clara',
  age: 314.159
};
const people = [clara, bob, alice];
sortByNameCaseInsensitive(people); 
```


## sortWith Relation

[(a, a) → Number] → [a] → [a]

Parameters

- functions A list of comparator functions.
- list The list to sort.

Returns

Array

A new list sorted according to the comarator functions.

Added in v0.23.0

Sorts a list according to a list of comparators.

See also

ascend

,

descend

.

```
const alice = {
  name: 'alice',
  age: 40
};
const bob = {
  name: 'bob',
  age: 30
};
const clara = {
  name: 'clara',
  age: 40
};
const people = [clara, bob, alice];
const ageNameSort = R.sortWith([
  R.descend(R.prop('age')),
  R.ascend(R.prop('name'))
]);
ageNameSort(people); 
```


## split String

(String | RegExp) → String → [String]

Parameters

- sep The pattern.
- str The string to separate into an array.

Returns

Array

The array of strings from `str` separated by `sep`.

Added in v0.1.0

Splits a string into an array of strings based on the given separator.

See also

join

.

```
const pathComponents = R.split('/');
R.tail(pathComponents('/usr/local/bin/node')); 

R.split('.', 'a.b.c.xyz.d'); 
```


## splitAt List

Number → [a] → [[a], [a]]

Number → String → [String, String]

Parameters

- index The index where the array/string is split.
- array The array/string to be split.

Returns

Array

Added in v0.19.0

Splits a given list or string at a given index.

```
R.splitAt(1, [1, 2, 3]);          
R.splitAt(5, 'hello world');      
R.splitAt(-1, 'foobar');          
```


## splitEvery List

Number → [a] → [[a]]

Number → String → [String]

Parameters

- n
- list

Returns

Array

Added in v0.16.0

Splits a collection into slices of the specified length.

```
R.splitEvery(3, [1, 2, 3, 4, 5, 6, 7]); 
R.splitEvery(3, 'foobarbaz'); 
```


## splitWhen List

(a → Boolean) → [a] → [[a], [a]]

Parameters

- pred The predicate that determines where the array is split.
- list The array to be split.

Returns

Array

Added in v0.19.0

Takes a list and a predicate and returns a pair of lists with the following properties:

- the result of concatenating the two output lists is equivalent to the input list;
- none of the elements of the first output list satisfies the predicate; and
- if the second output list is non-empty, its first element satisfies the predicate.

```
R.splitWhen(R.equals(2), [1, 2, 3, 1, 2, 3]);   
```


## splitWhenever List

(a → Boolean) → [a] → [[a]]

Parameters

- pred The predicate that determines where the array is split.
- list The array to be split.

Returns

Array

Added in v0.28.0

Splits an array into slices on every occurrence of a value.

```
R.splitWhenever(R.equals(2), [1, 2, 3, 2, 4, 5, 2, 6, 7]); 
```


## startsWith List

[a] → [a] → Boolean

String → String → Boolean

Parameters

- prefix
- list

Returns

Boolean

Added in v0.24.0

Checks if a list starts with the provided sublist.

Similarly, checks if a string starts with the provided substring.

See also

endsWith

.

```
R.startsWith('a', 'abc')                
R.startsWith('b', 'abc')                
R.startsWith(['a'], ['a', 'b', 'c'])    
R.startsWith(['b'], ['a', 'b', 'c'])    
```


## subtract Math

Number → Number → Number

Parameters

- a The first value.
- b The second value.

Returns

Number

The result of `a - b`.

Added in v0.1.0

Subtracts its second argument from its first argument.

See also

add

.

```
R.subtract(10, 8); 

const minus5 = R.subtract(R.__, 5);
minus5(17); 

const complementaryAngle = R.subtract(90);
complementaryAngle(30); 
complementaryAngle(72); 
```


## sum Math

[Number] → Number

Parameters

- list An array of numbers

Returns

Number

The sum of all the numbers in the list.

Added in v0.1.0

Adds together all the elements of a list.

See also

reduce

.

```
R.sum([2,4,6,8,100,1]); 
```


## swap List

Number → Number → [a] → [a]

Parameters

- indexA The first index
- indexB The second index
- o Either the object or list which will serve to realise the swap

Returns

Array

The new object or list reordered

Added in v0.29.0

Swap an item, at index `indexA` with another item, at index `indexB`, in an object or a list of elements. A new result will be created containing the new elements order.

```
R.swap(0, 2, ['a', 'b', 'c', 'd', 'e', 'f']); 
R.swap(-1, 0, ['a', 'b', 'c', 'd', 'e', 'f']); 
R.swap('a', 'b', {a: 1, b: 2}); 
R.swap(0, 2, 'foo'); 
```


## symmetricDifference Relation

[*] → [*] → [*]

Parameters

- list1 The first list.
- list2 The second list.

Returns

Array

The elements in `list1` or `list2`, but not both.

Added in v0.19.0

Finds the set (i.e. no duplicates) of all elements contained in the first or second list, but not both.

See also

symmetricDifferenceWith

,

difference

,

differenceWith

.

```
R.symmetricDifference([1,2,3,4], [7,6,5,4,3]); 
R.symmetricDifference([7,6,5,4,3], [1,2,3,4]); 
```


## symmetricDifferenceWith Relation

((a, a) → Boolean) → [a] → [a] → [a]

Parameters

- pred A predicate used to test whether two items are equal.
- list1 The first list.
- list2 The second list.

Returns

Array

The elements in `list1` or `list2`, but not both.

Added in v0.19.0

Finds the set (i.e. no duplicates) of all elements contained in the first or second list, but not both. Duplication is determined according to the value returned by applying the supplied predicate to two list elements.

See also

symmetricDifference

,

difference

,

differenceWith

.

```
const eqA = R.eqBy(R.prop('a'));
const l1 = [{a: 1}, {a: 2}, {a: 3}, {a: 4}];
const l2 = [{a: 3}, {a: 4}, {a: 5}, {a: 6}];
R.symmetricDifferenceWith(eqA, l1, l2); 
```


## T Function

* → Boolean

Parameters

Returns

Boolean

Added in v0.9.0

A function that always returns `true`. Any passed in parameters are ignored.

See also

F

.

```
R.T(); 
```


## tail List

[a] → [a]

String → String

Parameters

- list

Returns

*

Added in v0.1.0

Returns all but the first element of the given list or string (or object with a `tail` method).

Dispatches to the `slice` method of the first argument, if present.

See also

head

,

init

,

last

.

```
R.tail([1, 2, 3]);  
R.tail([1, 2]);     
R.tail([1]);        
R.tail([]);         

R.tail('abc');  
R.tail('ab');   
R.tail('a');    
R.tail('');     
```


## take List

Number → [a] → [a]

Number → String → String

Parameters

- n
- list

Returns

*

Added in v0.1.0

Returns the first `n` elements of the given list, string, or transducer/transformer (or object with a `take` method).

Dispatches to the `take` method of the second argument, if present.

See also

drop

.

```
R.take(1, ['foo', 'bar', 'baz']); 
R.take(2, ['foo', 'bar', 'baz']); 
R.take(3, ['foo', 'bar', 'baz']); 
R.take(4, ['foo', 'bar', 'baz']); 
R.take(3, 'ramda');               

const personnel = [
  'Dave Brubeck',
  'Paul Desmond',
  'Eugene Wright',
  'Joe Morello',
  'Gerry Mulligan',
  'Bob Bates',
  'Joe Dodge',
  'Ron Crotty'
];

const takeFive = R.take(5);
takeFive(personnel);
```


## takeLast List

Number → [a] → [a]

Number → String → String

Parameters

- n The number of elements to return.
- xs The collection to consider.

Returns

Array

Added in v0.16.0

Returns a new list containing the last `n` elements of the given list. If `n > list.length`, returns a list of `list.length` elements.

See also

dropLast

.

```
R.takeLast(1, ['foo', 'bar', 'baz']); 
R.takeLast(2, ['foo', 'bar', 'baz']); 
R.takeLast(3, ['foo', 'bar', 'baz']); 
R.takeLast(4, ['foo', 'bar', 'baz']); 
R.takeLast(3, 'ramda');               
```


## takeLastWhile List

(a → Boolean) → [a] → [a]

(a → Boolean) → String → String

Parameters

- fn The function called per iteration.
- xs The collection to iterate over.

Returns

Array

A new array.

Added in v0.16.0

Returns a new list containing the last `n` elements of a given list, passing each value to the supplied predicate function, and terminating when the predicate function returns `false`. Excludes the element that caused the predicate function to fail. The predicate function is passed one argument: *(value)*.

See also

dropLastWhile

,

addIndex

.

```
const isNotOne = x => x !== 1;

R.takeLastWhile(isNotOne, [1, 2, 3, 4]); 

R.takeLastWhile(x => x !== 'R' , 'Ramda'); 
```


## takeWhile List

(a → Boolean) → [a] → [a]

(a → Boolean) → String → String

Parameters

- fn The function called per iteration.
- xs The collection to iterate over.

Returns

Array

A new array.

Added in v0.1.0

Returns a new list containing the first `n` elements of a given list, passing each value to the supplied predicate function, and terminating when the predicate function returns `false`. Excludes the element that caused the predicate function to fail. The predicate function is passed one argument: *(value)*.

Dispatches to the `takeWhile` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

dropWhile

,

transduce

,

addIndex

.

```
const isNotFour = x => x !== 4;

R.takeWhile(isNotFour, [1, 2, 3, 4, 3, 2, 1]); 

R.takeWhile(x => x !== 'd' , 'Ramda'); 
```


## tap Function

(a → *) → a → a

Parameters

- fn The function to call with `x`. The return value of `fn` will be thrown away.
- x

Returns

*

`x`.

Added in v0.1.0

Runs the given function with the supplied object, then returns the object.

Acts as a transducer if a transformer is given as second parameter.

```
const sayX = x => console.log('x is ' + x);
R.tap(sayX, 100); 
```


## test String

RegExp → String → Boolean

Parameters

- pattern
- str

Returns

Boolean

Added in v0.12.0

Determines whether a given string matches a given regular expression.

See also

match

.

```
R.test(/^x/, 'xyz'); 
R.test(/^y/, 'xyz'); 
```


## thunkify Function

((a, b, …, j) → k) → (a, b, …, j) → (() → k)

Parameters

- fn A function to wrap in a thunk

Returns

function

Expects arguments for `fn` and returns a new function that, when called, applies those arguments to `fn`.

Added in v0.26.0

Creates a thunk out of a function. A thunk delays a calculation until its result is needed, providing lazy evaluation of arguments.

See also

partial

,

partialRight

.

```
R.thunkify(R.identity)(42)(); 
R.thunkify((a, b) => a + b)(25, 17)(); 
```


## times List

(Number → a) → Number → [a]

Parameters

- fn The function to invoke. Passed one argument, the current value of `n`.
- n A value between `0` and `n - 1`. Increments after each function call.

Returns

Array

An array containing the return values of all calls to `fn`.

Added in v0.2.3

Calls an input function `n` times, returning an array containing the results of those function calls.

`fn` is passed one argument: The current value of `n`, which begins at `0` and is gradually incremented to `n - 1`.

See also

repeat

.

```
R.times(R.identity, 5); 
```


## toLower String

String → String

Parameters

- str The string to lower case.

Returns

String

The lower case version of `str`.

Added in v0.9.0

The lower case version of a string.

See also

toUpper

.

```
R.toLower('XYZ'); 
```


## toPairs Object

{String: *} → [[String,*]]

Parameters

- obj The object to extract from

Returns

Array

An array of key, value arrays from the object's own properties.

Added in v0.4.0

Converts an object into an array of key, value arrays. Only the object's own properties are used. Note that the order of the output array is not guaranteed to be consistent across different JS platforms.

See also

fromPairs

,

keys

,

values

.

```
R.toPairs({a: 1, b: 2, c: 3}); 
```


## toPairsIn Object

{String: *} → [[String,*]]

Parameters

- obj The object to extract from

Returns

Array

An array of key, value arrays from the object's own and prototype properties.

Added in v0.4.0

Converts an object into an array of key, value arrays. The object's own properties and prototype properties are used. Note that the order of the output array is not guaranteed to be consistent across different JS platforms.

```
const F = function() { this.x = 'X'; };
F.prototype.y = 'Y';
const f = new F();
R.toPairsIn(f); 
```


## toString String

* → String

Parameters

- val

Returns

String

Added in v0.14.0

Returns the string representation of the given value. `eval`'ing the output should result in a value equivalent to the input value. Many of the built-in `toString` methods do not satisfy this requirement.

If the given value is an `[object Object]` with a `toString` method other than `Object.prototype.toString`, this method is invoked with no arguments to produce the return value. This means user-defined constructor functions can provide a suitable `toString` method. For example:

```
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function() {
  return 'new Point(' + this.x + ', ' + this.y + ')';
};

R.toString(new Point(1, 2)); //=> 'new Point(1, 2)'
```

```
R.toString(42); 
R.toString('abc'); 
R.toString([1, 2, 3]); 
R.toString({foo: 1, bar: 2, baz: 3}); 
R.toString(new Date('2001-02-03T04:05:06Z')); 
```


## toUpper String

String → String

Parameters

- str The string to upper case.

Returns

String

The upper case version of `str`.

Added in v0.9.0

The upper case version of a string.

See also

toLower

.

```
R.toUpper('abc'); 
```


## transduce List

(c → c) → ((a, b) → a) → a → [b] → a

Parameters

- xf The transducer function. Receives a transformer and returns a transformer.
- fn The iterator function. Receives two values, the accumulator and the current element from the array. Wrapped as transformer, if necessary, and used to initialize the transducer
- acc The initial accumulator value.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.12.0

Initializes a transducer using supplied iterator function. Returns a single item by iterating through the list, successively calling the transformed iterator function and passing it an accumulator value and the current value from the array, and then passing the result to the next call.

The iterator function receives two values: *(acc, value)*. It will be wrapped as a transformer to initialize the transducer. A transformer can be passed directly in place of an iterator function. In both cases, iteration may be stopped early with the `R.reduced` function.

A transducer is a function that accepts a transformer and returns a transformer and can be composed directly.

A transformer is an object that provides a 2-arity reducing iterator function, step, 0-arity initial value function, init, and 1-arity result extraction function, result. The step function is used as the iterator function in reduce. The result function is used to convert the final accumulator into the return type and in most cases is `R.identity`. The init function can be used to provide an initial accumulator, but is ignored by transduce.

The iteration is performed with `R.reduce` after initializing the transducer.

See also

reduce

,

reduced

,

into

.

```
const numbers = [1, 2, 3, 4];
const transducer = R.compose(R.map(R.add(1)), R.take(2));
R.transduce(transducer, R.flip(R.append), [], numbers); 

const isOdd = (x) => x % 2 !== 0;
const firstOddTransducer = R.compose(R.filter(isOdd), R.take(1));
R.transduce(firstOddTransducer, R.flip(R.append), [], R.range(0, 100)); 
```


## transpose List

[[a]] → [[a]]

Parameters

- list A 2D list

Returns

Array

A 2D list

Added in v0.19.0

Transposes the rows and columns of a 2D list. When passed a list of `n` lists of length `x`, returns a list of `x` lists of length `n`.

```
R.transpose([[1, 'a'], [2, 'b'], [3, 'c']]) 
R.transpose([[1, 2, 3], ['a', 'b', 'c']]) 

R.transpose([[10, 11], [20], [], [30, 31, 32]]) 
```


## traverse List

fantasy-land/of :: TypeRep f => f ~> a → f a

(Applicative f, Traversable t) => TypeRep f → (a → f b) → t a → f (t b)

(Applicative f, Traversable t) => (b → f b) → (a → f b) → t a → f (t b)

Parameters

- TypeRepresentative with an `of` or `fantasy-land/of` method
- f
- traversable

Returns

*

Added in v0.19.0

Maps an Applicative-returning function over a Traversable, then uses `sequence` to transform the resulting Traversable of Applicative into an Applicative of Traversable.

Dispatches to the `traverse` method of the third argument, if present.

See also

sequence

.

```
const safeDiv = n => d => d === 0 ? Maybe.Nothing() : Maybe.Just(n / d)

R.traverse(Maybe.of, safeDiv(10), [2, 4, 5]); 
R.traverse(Maybe.of, safeDiv(10), [2, 0, 5]); 

R.traverse(Maybe, safeDiv(10), Right(4)); 
R.traverse(Maybe, safeDiv(10), Right(0)); 
R.traverse(Maybe, safeDiv(10), Left("X")); 
```
