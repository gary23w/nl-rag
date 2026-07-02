---
title: "Ramda Documentation (part 4/4)"
source: https://ramdajs.com/docs/
domain: ramda-functional
license: CC-BY-SA-4.0
tags: ramda functional, point-free style, javascript currying, immutable pipeline
fetched: 2026-07-02
part: 4/4
---

## trim String

String → String

Parameters

- str The string to trim.

Returns

String

Trimmed version of `str`.

Added in v0.6.0

Removes (strips) whitespace from both ends of the string.

```
R.trim('   xyz  '); 
R.map(R.trim, R.split(',', 'x, y, z')); 
```


## tryCatch Function

(…x → a) → ((e, …x) → a) → (…x → a)

Parameters

- tryer The function that may throw.
- catcher The function that will be evaluated if `tryer` throws.

Returns

function

A new function that will catch exceptions and send them to the catcher.

Added in v0.20.0

`tryCatch` takes two functions, a `tryer` and a `catcher`. The returned function evaluates the `tryer`; if it does not throw, it simply returns the result. If the `tryer` *does* throw, the returned function evaluates the `catcher` function and returns its result. Note that for effective composition with this function, both the `tryer` and `catcher` functions must return the same type of results.

```
R.tryCatch(R.prop('x'), R.F)({x: true}); 
R.tryCatch(() => { throw 'foo'}, R.always('caught'))('bar') 
'caught'
R.tryCatch(R.times(R.identity), R.always([]))('s') 
R.tryCatch(() => { throw 'this is not a valid value'}, (err, value)=>({error : err,  value }))('bar') 
```


## type Type

* → String

Parameters

- val The value to test

Returns

String

Added in v0.8.0

Gives a single-word string description of the (native) type of a value, returning such answers as 'Object', 'Number', 'Array', or 'Null'. Does not attempt to distinguish user Object types any further, reporting them all as 'Object'.

```
R.type({}); 
R.type(new Map); 
R.type(new Set); 
R.type(1); 
R.type(false); 
R.type('s'); 
R.type(null); 
R.type([]); 
R.type(/[A-z]/); 
R.type(() => {}); 
R.type(async () => {}); 
R.type(undefined); 
R.type(BigInt(123)); 
```


## unapply Function

([*…] → a) → (*… → a)

Parameters

- fn

Returns

function

Added in v0.8.0

Takes a function `fn`, which takes a single array argument, and returns a function which:

- takes any number of positional arguments;
- passes these arguments to `fn` as an array; and
- returns the result.

In other words, `R.unapply` derives a variadic function from a function which takes an array. `R.unapply` is the inverse of `R.apply`.

See also

apply

.

```
R.unapply(JSON.stringify)(1, 2, 3); 
```


## unary Function

(a → b → c → … → z) → (a → z)

Parameters

- fn The function to wrap.

Returns

function

A new function wrapping `fn`. The new function is guaranteed to be of arity 1.

Added in v0.2.0

Wraps a function of any arity (including nullary) in a function that accepts exactly 1 parameter. Any extraneous parameters will not be passed to the supplied function.

See also

binary

,

nAry

.

```
const takesTwoArgs = function(a, b) {
  return [a, b];
};
takesTwoArgs.length; 
takesTwoArgs(1, 2); 

const takesOneArg = R.unary(takesTwoArgs);
takesOneArg.length; 

takesOneArg(1, 2); 
```


## uncurryN Function

Number → (a → b → c … → z) → ((a → b → c …) → z)

Parameters

- length The arity for the returned function.
- fn The function to uncurry.

Returns

function

A new function.

Added in v0.14.0

Returns a function of arity `n` from a (manually) curried function. Note that, the returned function is actually a ramda style curryied function, which can accept one or more arguments in each function calling.

See also

curry

,

curryN

.

```
const addFour = a => b => c => d => a + b + c + d;

const uncurriedAddFour = R.uncurryN(4, addFour);
uncurriedAddFour(1, 2, 3, 4); 
```


## unfold List

(a → [b]) → * → [b]

Parameters

- fn The iterator function. receives one argument, `seed`, and returns either false to quit iteration or an array of length two to proceed. The element at index 0 of this array will be added to the resulting array, and the element at index 1 will be passed to the next call to `fn`.
- seed The seed value.

Returns

Array

The final list.

Added in v0.10.0

Builds a list from a seed value. Accepts an iterator function, which returns either false to stop iteration or an array of length 2 containing the value to add to the resulting list and the seed to be used in the next call to the iterator function.

The iterator function receives one argument: *(seed)*.

```
const f = n => n > 50 ? false : [-n, n + 10];
R.unfold(f, 10); 
```


## union Relation

[*] → [*] → [*]

Parameters

- as The first list.
- bs The second list.

Returns

Array

The first and second lists concatenated, with duplicates removed.

Added in v0.1.0

Combines two lists into a set (i.e. no duplicates) composed of the elements of each list.

```
R.union([1, 2, 3], [2, 3, 4]); 
```


## unionWith Relation

((a, a) → Boolean) → [*] → [*] → [*]

Parameters

- pred A predicate used to test whether two items are equal.
- list1 The first list.
- list2 The second list.

Returns

Array

The first and second lists concatenated, with duplicates removed.

Added in v0.1.0

Combines two lists into a set (i.e. no duplicates) composed of the elements of each list. Duplication is determined according to the value returned by applying the supplied predicate to two list elements. If an element exists in both lists, the first element from the first list will be used.

See also

union

.

```
const l1 = [{a: 1}, {a: 2}];
const l2 = [{a: 1}, {a: 4}];
R.unionWith(R.eqBy(R.prop('a')), l1, l2); 
```


## uniq List

[a] → [a]

Parameters

- list The array to consider.

Returns

Array

The list of unique items.

Added in v0.1.0

Returns a new list containing only one copy of each element in the original list. `R.equals` is used to determine equality.

```
R.uniq([1, 1, 2, 1]); 
R.uniq([1, '1']);     
R.uniq([[42], [42]]); 
```


## uniqBy List

(a → b) → [a] → [a]

Parameters

- fn A function used to produce a value to use during comparisons.
- list The array to consider.

Returns

Array

The list of unique items.

Added in v0.16.0

Returns a new list containing only one copy of each element in the original list, based upon the value returned by applying the supplied function to each list element. Prefers the first item if the supplied function produces the same value on two items. `R.equals` is used for comparison.

Acts as a transducer if a transformer is given in list position.

```
R.uniqBy(Math.abs, [-1, -5, 2, 10, 1, 2]); 
```


## uniqWith List

((a, a) → Boolean) → [a] → [a]

Parameters

- pred A predicate used to test whether two items are equal.
- list The array to consider.

Returns

Array

The list of unique items.

Added in v0.2.0

Returns a new list containing only one copy of each element in the original list, based upon the value returned by applying the supplied predicate to two list elements. Prefers the first item if two items compare equal based on the predicate.

Acts as a transducer if a transformer is given in list position.

```
const strEq = R.eqBy(String);
R.uniqWith(strEq)([1, '1', 2, 1]); 
R.uniqWith(strEq)([{}, {}]);       
R.uniqWith(strEq)([1, '1', 1]);    
R.uniqWith(strEq)(['1', 1, 1]);    
```


## unless Logic

(a → Boolean) → (a → b) → a → a | b

Parameters

- pred A predicate function
- whenFalseFn A function to invoke when the `pred` evaluates to a falsy value.
- x An object to test with the `pred` function and pass to `whenFalseFn` if necessary.

Returns

*

Either `x` or the result of applying `x` to `whenFalseFn`.

Added in v0.18.0

Tests the final argument by passing it to the given predicate function. If the predicate is not satisfied, the function will return the result of calling the `whenFalseFn` function with the same argument. If the predicate is satisfied, the argument is returned as is.

See also

ifElse

,

when

,

cond

.

```
let safeInc = R.unless(R.isNil, R.inc);
safeInc(null); 
safeInc(1); 
```


## unnest List

Chain c => c (c a) → c a

Parameters

- list

Returns

*

Added in v0.3.0

Shorthand for `R.chain(R.identity)`, which removes one level of nesting from any Chain.

See also

flatten

,

chain

.

```
R.unnest([1, [2], [[3]]]); 
R.unnest([[1, 2], [3, 4], [5, 6]]); 
```


## until Logic

(a → Boolean) → (a → a) → a → a

Parameters

- pred A predicate function
- fn The iterator function
- init Initial value

Returns

*

Final value that satisfies predicate

Added in v0.20.0

Takes a predicate, a transformation function, and an initial value, and returns a value of the same type as the initial value. It does so by applying the transformation until the predicate is satisfied, at which point it returns the satisfactory value.

```
R.until(R.gt(R.__, 100), R.multiply(2))(1) 
```


## unwind Object

String → {k: [v]} → [{k: v}]

Parameters

- key The key to determine which property of the object should be unwound.
- object The object containing the list to unwind at the property named by the key.

Returns

List

A list of new objects, each having the given key associated to an item from the unwound list.

Added in v0.28.0

Deconstructs an array field from the input documents to output a document for each element. Each output document is the input document with the value of the array field replaced by the element.

```
R.unwind('hobbies', {
  name: 'alice',
  hobbies: ['Golf', 'Hacking'],
  colors: ['red', 'green'],
});
```


## update List

Number → a → [a] → [a]

Parameters

- idx The index to update.
- x The value to exist at the given index of the returned array.
- list The source array-like object to be updated.

Returns

Array

A copy of `list` with the value at index `idx` replaced with `x`.

Added in v0.14.0

Returns a new copy of the array with the element at the provided index replaced with the given value.

When `idx < -list.length || idx >= list.length`, the original list is returned.

See also

adjust

.

```
R.update(1, '_', ['a', 'b', 'c']);      
R.update(-1, '_', ['a', 'b', 'c']);     

R.update(3, '_', ['a', 'b', 'c']);      
R.update(-4, '_', ['a', 'b', 'c']);     
```


## useWith Function

((x1, x2, …) → z) → [(a → x1), (b → x2), …] → (a → b → … → z)

Parameters

- fn The function to wrap.
- transformers A list of transformer functions

Returns

function

The wrapped function.

Added in v0.1.0

Accepts a function `fn` and a list of transformer functions and returns a new curried function. When the new function is invoked, it calls the function `fn` with parameters consisting of the result of calling each supplied handler on successive arguments to the new function.

If more arguments are passed to the returned function than transformer functions, those arguments are passed directly to `fn` as additional parameters. If you expect additional arguments that don't need to be transformed, although you can ignore them, it's best to pass an identity function so that the new function reports the correct arity.

See also

converge

.

```
R.useWith(Math.pow, [R.identity, R.identity])(3, 4); 
R.useWith(Math.pow, [R.identity, R.identity])(3)(4); 
R.useWith(Math.pow, [R.dec, R.inc])(3, 4); 
R.useWith(Math.pow, [R.dec, R.inc])(3)(4); 
```


## values Object

{k: v} → [v]

Parameters

- obj The object to extract values from

Returns

Array

An array of the values of the object's own properties.

Added in v0.1.0

Returns a list of all the enumerable own properties of the supplied object. Note that the order of the output array is not guaranteed across different JS platforms.

See also

valuesIn

,

keys

,

toPairs

.

```
R.values({a: 1, b: 2, c: 3}); 
```


## valuesIn Object

{k: v} → [v]

Parameters

- obj The object to extract values from

Returns

Array

An array of the values of the object's own and prototype properties.

Added in v0.2.0

Returns a list of all the properties, including prototype properties, of the supplied object. Note that the order of the output array is not guaranteed to be consistent across different JS platforms.

See also

values

,

keysIn

.

```
const F = function() { this.x = 'X'; };
F.prototype.y = 'Y';
const f = new F();
R.valuesIn(f); 
```


## view Object

Lens s a → s → a

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- lens
- x

Returns

*

Added in v0.16.0

Returns a "view" of the given data structure, determined by the given lens. The lens's focus determines which portion of the data structure is visible.

See also

set

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

R.view(xLens, {x: 1, y: 2});  
R.view(xLens, {x: 4, y: 2});  
```


## when Logic

(a → Boolean) → (a → b) → a → a | b

Parameters

- pred A predicate function
- whenTrueFn A function to invoke when the `condition` evaluates to a truthy value.
- x An object to test with the `pred` function and pass to `whenTrueFn` if necessary.

Returns

*

Either `x` or the result of applying `x` to `whenTrueFn`.

Added in v0.18.0

Tests the final argument by passing it to the given predicate function. If the predicate is satisfied, the function will return the result of calling the `whenTrueFn` function with the same argument. If the predicate is not satisfied, the argument is returned as is.

See also

ifElse

,

unless

,

cond

.

```
const truncate = R.when(
  R.propSatisfies(R.gt(R.__, 10), 'length'),
  R.pipe(R.take(10), R.append('…'), R.join(''))
);
truncate('12345');         
truncate('0123456789ABC'); 
```


## where Object

{String: (* → Boolean)} → {String: *} → Boolean

Parameters

- spec
- testObj

Returns

Boolean

Added in v0.1.1

Takes a spec object and a test object; returns true if the test satisfies the spec. Each of the spec's own properties must be a predicate function. Each predicate is applied to the value of the corresponding property of the test object. `where` returns true if all the predicates return true, false otherwise.

`where` is well suited to declaratively expressing constraints for other functions such as `filter` and `find`.

See also

propSatisfies

,

whereEq

.

```
const pred = R.where({
  a: R.equals('foo'),
  b: R.complement(R.equals('bar')),
  x: R.gt(R.__, 10),
  y: R.lt(R.__, 20)
});

pred({a: 'foo', b: 'xxx', x: 11, y: 19}); 
pred({a: 'xxx', b: 'xxx', x: 11, y: 19}); 
pred({a: 'foo', b: 'bar', x: 11, y: 19}); 
pred({a: 'foo', b: 'xxx', x: 10, y: 19}); 
pred({a: 'foo', b: 'xxx', x: 11, y: 20}); 
```


## whereAny Object

{String: (* → Boolean)} → {String: *} → Boolean

Parameters

- spec
- testObj

Returns

Boolean

Added in v0.28.0

Takes a spec object and a test object; each of the spec's own properties must be a predicate function. Each predicate is applied to the value of the corresponding property of the test object. `whereAny` returns true if at least one of the predicates return true, false otherwise.

`whereAny` is well suited to declaratively expressing constraints for other functions such as `filter` and `find`.

See also

propSatisfies

,

where

.

```
const pred = R.whereAny({
  a: R.equals('foo'),
  b: R.complement(R.equals('xxx')),
  x: R.gt(R.__, 10),
  y: R.lt(R.__, 20)
});

pred({a: 'foo', b: 'xxx', x: 8, y: 34}); 
pred({a: 'xxx', b: 'xxx', x: 9, y: 21}); 
pred({a: 'bar', b: 'xxx', x: 10, y: 20}); 
pred({a: 'foo', b: 'bar', x: 10, y: 20}); 
pred({a: 'foo', b: 'xxx', x: 11, y: 20}); 
```


## whereEq Object

{String: *} → {String: *} → Boolean

Parameters

- spec
- testObj

Returns

Boolean

Added in v0.14.0

Takes a spec object and a test object; returns true if the test satisfies the spec, false otherwise. An object satisfies the spec if, for each of the spec's own properties, accessing that property of the object gives the same value (in `R.equals` terms) as accessing that property of the spec.

`whereEq` is a specialization of `where`.

See also

propEq

,

where

.

```
const pred = R.whereEq({a: 1, b: 2});

pred({a: 1});              
pred({a: 1, b: 2});        
pred({a: 1, b: 2, c: 3});  
pred({a: 1, b: 1});        
```


## without List

[a] → [a] → [a]

Parameters

- list1 The values to be removed from `list2`.
- list2 The array to remove values from.

Returns

Array

The new array without values in `list1`.

Added in v0.19.0

Returns a new list without values in the first argument. `R.equals` is used to determine equality.

Acts as a transducer if a transformer is given in list position.

See also

transduce

,

difference

,

remove

.

```
R.without([1, 2], [1, 2, 1, 3, 4]); 
```


## xor Logic

a → b → Boolean

Parameters

- a
- b

Returns

Boolean

true if one of the arguments is truthy and the other is falsy

Added in v0.27.1

Exclusive disjunction logical operation. Returns `true` if one of the arguments is truthy and the other is falsy. Otherwise, it returns `false`.

See also

or

,

and

.

```
R.xor(true, true); 
R.xor(true, false); 
R.xor(false, true); 
R.xor(false, false); 
```


## xprod List

[a] → [b] → [[a,b]]

Parameters

- as The first list.
- bs The second list.

Returns

Array

The list made by combining each possible pair from `as` and `bs` into pairs (`[a, b]`).

Added in v0.1.0

Creates a new list out of the two supplied by creating each possible pair from the lists.

```
R.xprod([1, 2], ['a', 'b']); 
```


## zip List

[a] → [b] → [[a,b]]

Parameters

- list1 The first array to consider.
- list2 The second array to consider.

Returns

Array

The list made by pairing up same-indexed elements of `list1` and `list2`.

Added in v0.1.0

Creates a new list out of the two supplied by pairing up equally-positioned items from both lists. The returned list is truncated to the length of the shorter of the two input lists. Note: `zip` is equivalent to `zipWith(function(a, b) { return [a, b] })`.

```
R.zip([1, 2, 3], ['a', 'b', 'c']); 
```


## zipObj List

[String] → [*] → {String: *}

Parameters

- keys The array that will be properties on the output object.
- values The list of values on the output object.

Returns

Object

The object made by pairing up same-indexed elements of `keys` and `values`.

Added in v0.3.0

Creates a new object out of a list of keys and a list of values. Key/value pairing is truncated to the length of the shorter of the two lists. Note: `zipObj` is equivalent to `pipe(zip, fromPairs)`.

```
R.zipObj(['a', 'b', 'c'], [1, 2, 3]); 
```


## zipWith List

((a, b) → c) → [a] → [b] → [c]

Parameters

- fn The function used to combine the two elements into one value.
- list1 The first array to consider.
- list2 The second array to consider.

Returns

Array

The list made by combining same-indexed elements of `list1` and `list2` using `fn`.

Added in v0.1.0

Creates a new list out of the two supplied by applying the function to each equally-positioned pair in the lists. The returned list is truncated to the length of the shorter of the two input lists.

```
const f = (x, y) => {
  
};
R.zipWith(f, [1, 2, 3], ['a', 'b', 'c']);
```
