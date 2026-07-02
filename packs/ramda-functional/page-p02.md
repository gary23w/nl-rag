---
title: "Ramda Documentation (part 2/4)"
source: https://ramdajs.com/docs/
domain: ramda-functional
license: CC-BY-SA-4.0
tags: ramda functional, point-free style, javascript currying, immutable pipeline
fetched: 2026-07-02
part: 2/4
---

## flow Function

a → [(a → b), …, (y → z)] → z

Parameters

- a The seed value
- pipeline functions composing the pipeline

Returns

*

z The result of applying the seed value to the function pipeline

Added in v0.30.0

Takes the value of an expression and applies it to a function which is the left-to-right serial composition of the functions given in the second argument.

The functions in the pipeline should be unary functions.

`flow` is helps to avoid introducing an extra function with named arguments for computing the result of a function pipeline which depends on given initial values. Rather than defining a referential transparent function `f = (_x, _y) => R.pipe(g(_x), h(_y), …)` which is only later needed once `z = f(x, y)`, the introduction of `f`, `_x` and `_y` can be avoided: `z = flow(x, [g, h(y),…]`

In some libraries this function is named `pipe`.

See also

pipe

.

```
R.flow(9, [Math.sqrt, R.negate, R.inc]); 

const personObj = { first: 'Jane', last: 'Doe' };
const fullName = R.flow(personObj, [R.values, R.join(' ')]); 
const givenName = R.flow('    ', [R.trim, R.when(R.isEmpty, R.always(fullName))]); 
```


## forEach List

(a → *) → [a] → [a]

Parameters

- fn The function to invoke. Receives one argument, `value`.
- list The list to iterate over.

Returns

Array

The original list.

Added in v0.1.1

Iterate over an input `list`, calling a provided function `fn` for each element in the list.

`fn` receives one argument: *(value)*.

Note: `R.forEach` does not skip deleted or unassigned indices (sparse arrays), unlike the native `Array.prototype.forEach` method. For more details on this behavior, see: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#Description

Also note that, unlike `Array.prototype.forEach`, Ramda's `forEach` returns the original array. In some libraries this function is named `each`.

Dispatches to the `forEach` method of the second argument, if present.

See also

addIndex

.

```
const printXPlusFive = x => console.log(x + 5);
R.forEach(printXPlusFive, [1, 2, 3]); 
```


## forEachObjIndexed Object

((a, String, StrMap a) → Any) → StrMap a → StrMap a

Parameters

- fn The function to invoke. Receives three argument, `value`, `key`, `obj`.
- obj The object to iterate over.

Returns

Object

The original object.

Added in v0.23.0

Iterate over an input `object`, calling a provided function `fn` for each key and value in the object.

`fn` receives three argument: *(value, key, obj)*.

```
const printKeyConcatValue = (value, key) => console.log(key + ':' + value);
R.forEachObjIndexed(printKeyConcatValue, {x: 1, y: 2}); 
```


## fromPairs List

[[k,v]] → {k: v}

Parameters

- pairs An array of two-element arrays that will be the keys and values of the output object.

Returns

Object

The object made by pairing up `keys` and `values`.

Added in v0.3.0

Creates a new object from a list key-value pairs. If a key appears in multiple pairs, the rightmost pair is included in the object.

See also

toPairs

,

pair

.

```
R.fromPairs([['a', 1], ['b', 2], ['c', 3]]); 
```


## groupBy List

Idx a => (b → a) → [b] → {a: [b]}

Idx = String | Int | Symbol

Parameters

- fn Function :: a -> Idx
- list The array to group

Returns

Object

An object with the output of `fn` for keys, mapped to arrays of elements that produced that key when passed to `fn`.

Added in v0.1.0

Splits a list into sub-lists stored in an object, based on the result of calling a key-returning function on each element, and grouping the results according to values returned.

Dispatches to the `groupBy` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

reduceBy

,

transduce

,

indexBy

,

collectBy

.

```
const byGrade = R.groupBy(function(student) {
  const score = student.score;
  return score < 65 ? 'F' :
         score < 70 ? 'D' :
         score < 80 ? 'C' :
         score < 90 ? 'B' : 'A';
});
const students = [{name: 'Abby', score: 84},
                {name: 'Eddy', score: 58},
                
                {name: 'Jack', score: 69}];
byGrade(students);
```


## groupWith List

((a, a) → Boolean) → [a] → [[a]]

Parameters

- fn Function for determining whether two given (adjacent) elements should be in the same group
- list The array to group. Also accepts a string, which will be treated as a list of characters.

Returns

List

A list that contains sublists of elements, whose concatenations are equal to the original list.

Added in v0.21.0

Takes a list and returns a list of lists where each sublist's elements are all satisfied pairwise comparison according to the provided function. Only adjacent elements are passed to the comparison function.

```
R.groupWith(R.equals, [0, 1, 1, 2, 3, 5, 8, 13, 21])

R.groupWith((a, b) => a + 1 === b, [0, 1, 1, 2, 3, 5, 8, 13, 21])

R.groupWith((a, b) => a % 2 === b % 2, [0, 1, 1, 2, 3, 5, 8, 13, 21])

const isVowel = R.test(/^[aeiou]$/i);
R.groupWith(R.eqBy(isVowel), 'aestiou')
```


## gt Relation

Ord a => a → a → Boolean

Parameters

- a
- b

Returns

Boolean

Added in v0.1.0

Returns `true` if the first argument is greater than the second; `false` otherwise.

See also

lt

.

```
R.gt(2, 1); 
R.gt(2, 2); 
R.gt(2, 3); 
R.gt('a', 'z'); 
R.gt('z', 'a'); 
```


## gte Relation

Ord a => a → a → Boolean

Parameters

- a
- b

Returns

Boolean

Added in v0.1.0

Returns `true` if the first argument is greater than or equal to the second; `false` otherwise.

See also

lte

.

```
R.gte(2, 1); 
R.gte(2, 2); 
R.gte(2, 3); 
R.gte('a', 'z'); 
R.gte('z', 'a'); 
```


## has Object

s → {s: x} → Boolean

Parameters

- prop The name of the property to check for.
- obj The object to query.

Returns

Boolean

Whether the property exists.

Added in v0.7.0

Returns whether or not an object has an own property with the specified name

```
const hasName = R.has('name');
hasName({name: 'alice'});   
hasName({name: 'bob'});     
hasName({});                

const point = {x: 0, y: 0};
const pointHas = R.has(R.__, point);
pointHas('x');  
pointHas('y');  
pointHas('z');  
```


## hasIn Object

s → {s: x} → Boolean

Parameters

- prop The name of the property to check for.
- obj The object to query.

Returns

Boolean

Whether the property exists.

Added in v0.7.0

Returns whether or not an object or its prototype chain has a property with the specified name

```
function Rectangle(width, height) {
  this.width = width;
  this.height = height;
}
Rectangle.prototype.area = function() {
  return this.width * this.height;
};

const square = new Rectangle(2, 2);
R.hasIn('width', square);  
R.hasIn('area', square);  
```


## hasPath Object

[Idx] → {a} → Boolean

Idx = String | Int | Symbol

Parameters

- path The path to use.
- obj The object to check the path in.

Returns

Boolean

Whether the path exists.

Added in v0.26.0

Returns whether or not a path exists in an object. Only the object's own properties are checked.

See also

has

.

```
R.hasPath(['a', 'b'], {a: {b: 2}});         
R.hasPath(['a', 'b'], {a: {b: undefined}}); 
R.hasPath(['a', 'b'], {a: {c: 2}});         
R.hasPath(['a', 'b'], {});                  
```


## head List

[a] → a | Undefined

String → String | Undefined

Parameters

- list

Returns

*

Added in v0.1.0

Returns the first element of the given list or string. In some libraries this function is named `first`.

See also

tail

,

init

,

last

.

```
R.head([1, 2, 3]);  
R.head([1]);        
R.head([]);         

R.head('abc');  
R.head('a');    
R.head('');     
```


## identical Relation

a → a → Boolean

Parameters

- a
- b

Returns

Boolean

Added in v0.15.0

Returns true if its arguments are identical, false otherwise. Values are identical if they reference the same memory. `NaN` is identical to `NaN`; `0` and `-0` are not identical.

Note this is merely a curried version of ES6 `Object.is`.

`identical` does not support the `__` placeholder.

```
const o = {};
R.identical(o, o); 
R.identical(1, 1); 
R.identical(1, '1'); 
R.identical([], []); 
R.identical(0, -0); 
R.identical(NaN, NaN); 
```


## identity Function

a → a

Parameters

- x The value to return.

Returns

*

The input value, `x`.

Added in v0.1.0

A function that does nothing but return the parameter supplied to it. Good as a default or placeholder function.

```
R.identity(1); 

const obj = {};
R.identity(obj) === obj; 
```


## ifElse Logic

(*… → Boolean) → (*… → *) → (*… → *) → (*… → *)

Parameters

- condition A predicate function
- onTrue A function to invoke when the `condition` evaluates to a truthy value.
- onFalse A function to invoke when the `condition` evaluates to a falsy value.

Returns

function

A new function that will process either the `onTrue` or the `onFalse` function depending upon the result of the `condition` predicate.

Added in v0.8.0

Creates a function that will process either the `onTrue` or the `onFalse` function depending upon the result of the `condition` predicate.

Note that `ifElse` takes its arity from the longest of the three functions passed to it.

See also

unless

,

when

,

cond

.

```
const incCount = R.ifElse(
  R.has('count'),
  R.over(R.lensProp('count'), R.inc),
  R.assoc('count', 1)
);
incCount({ count: 1 }); 
incCount({});           
```


## inc Math

Number → Number

Parameters

- n

Returns

Number

n + 1

Added in v0.9.0

Increments its argument.

See also

dec

.

```
R.inc(42); 
```


## includes List

a → [a] → Boolean

Parameters

- a The item to compare against.
- list The array to consider.

Returns

Boolean

`true` if an equivalent item is in the list, `false` otherwise.

Added in v0.26.0

Returns `true` if the specified value is equal, in `R.equals` terms, to at least one element of the given list; `false` otherwise. Also works with strings.

See also

any

.

```
R.includes(3, [1, 2, 3]); 
R.includes(4, [1, 2, 3]); 
R.includes({ name: 'Fred' }, [{ name: 'Fred' }]); 
R.includes([42], [[42]]); 
R.includes('ba', 'banana'); 
```


## indexBy List

Idx a => (b → a) → [b] → {a: b}

Idx = String | Int | Symbol

Parameters

- fn Function :: a -> Idx
- array The array of objects to index

Returns

Object

An object indexing each array element by the given property.

Added in v0.19.0

Given a function that generates a key, turns a list of objects into an object indexing the objects by the given key. Note that if multiple objects generate the same value for the indexing key only the last value will be included in the generated object.

Acts as a transducer if a transformer is given in list position.

See also

groupBy

.

```
const list = [{id: 'xyz', title: 'A'}, {id: 'abc', title: 'B'}];
R.indexBy(R.prop('id'), list);
```


## indexOf List

a → [a] → Number

Parameters

- target The item to find.
- xs The array to search in.

Returns

Number

the index of the target, or -1 if the target is not found.

Added in v0.1.0

Returns the position of the first occurrence of an item in an array, or -1 if the item is not included in the array. `R.equals` is used to determine equality.

See also

lastIndexOf

,

findIndex

.

```
R.indexOf(3, [1,2,3,4]); 
R.indexOf(10, [1,2,3,4]); 
```


## init List

[a] → [a]

String → String

Parameters

- list

Returns

*

Added in v0.9.0

Returns all but the last element of the given list or string.

See also

last

,

head

,

tail

.

```
R.init([1, 2, 3]);  
R.init([1, 2]);     
R.init([1]);        
R.init([]);         

R.init('abc');  
R.init('ab');   
R.init('a');    
R.init('');     
```


## innerJoin Relation

((a, b) → Boolean) → [a] → [b] → [a]

Parameters

- pred
- xs
- ys

Returns

Array

Added in v0.24.0

Takes a predicate `pred`, a list `xs`, and a list `ys`, and returns a list `xs'` comprising each of the elements of `xs` which is equal to one or more elements of `ys` according to `pred`.

`pred` must be a binary function expecting an element from each list.

`xs`, `ys`, and `xs'` are treated as sets, semantically, so ordering should not be significant, but since `xs'` is ordered the implementation guarantees that its values are in the same order as they appear in `xs`. Duplicates are not removed, so `xs'` may contain duplicates if `xs` contains duplicates.

See also

intersection

.

```
R.innerJoin(
  (record, id) => record.id === id,
  [{id: 824, name: 'Richie Furay'},
   {id: 956, name: 'Dewey Martin'},
   {id: 313, name: 'Bruce Palmer'},
   {id: 456, name: 'Stephen Stills'},
   {id: 177, name: 'Neil Young'}],
  [177, 456, 999]
);
```


## insert List

Number → a → [a] → [a]

Parameters

- index The position to insert the element
- elt The element to insert into the Array
- list The list to insert into

Returns

Array

A new Array with `elt` inserted at `index`.

Added in v0.2.2

Inserts the supplied element into the list, at the specified `index`. *Note that this is not destructive*: it returns a copy of the list with the changes. No lists have been harmed in the application of this function.

```
R.insert(2, 'x', [1,2,3,4]); 
```


## insertAll List

Number → [a] → [a] → [a]

Parameters

- index The position to insert the sub-list
- elts The sub-list to insert into the Array
- list The list to insert the sub-list into

Returns

Array

A new Array with `elts` inserted starting at `index`.

Added in v0.9.0

Inserts the sub-list into the list, at the specified `index`. *Note that this is not destructive*: it returns a copy of the list with the changes. No lists have been harmed in the application of this function.

```
R.insertAll(2, ['x','y','z'], [1,2,3,4]); 
```


## intersection Relation

[*] → [*] → [*]

Parameters

- list1 The first list.
- list2 The second list.

Returns

Array

The list of elements found in both `list1` and `list2`.

Added in v0.1.0

Combines two lists into a set (i.e. no duplicates) composed of those elements common to both lists.

See also

innerJoin

.

```
R.intersection([1,2,3,4], [7,6,5,4,3]); 
```


## intersperse List

a → [a] → [a]

Parameters

- separator The element to add to the list.
- list The list to be interposed.

Returns

Array

The new list.

Added in v0.14.0

Creates a new list with the separator interposed between elements.

Dispatches to the `intersperse` method of the second argument, if present.

```
R.intersperse('a', ['b', 'n', 'n', 's']); 
```


## into List

a → (b → b) → [c] → a

Parameters

- acc The initial accumulator value.
- xf The transducer function. Receives a transformer and returns a transformer.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.12.0

Transforms the items of the list with the transducer and appends the transformed items to the accumulator using an appropriate iterator function based on the accumulator type.

The accumulator can be an array, string, object or a transformer. Iterated items will be appended to arrays and concatenated to strings. Objects will be merged directly or 2-item arrays will be merged as key, value pairs.

The accumulator can also be a transformer object that provides a 2-arity reducing iterator function, step, 0-arity initial value function, init, and 1-arity result extraction function result. The step function is used as the iterator function in reduce. The result function is used to convert the final accumulator into the return type and in most cases is R.identity. The init function is used to provide the initial accumulator.

The iteration is performed with `R.reduce` after initializing the transducer.

See also

transduce

.

```
const numbers = [1, 2, 3, 4];
const transducer = R.compose(R.map(R.add(1)), R.take(2));

R.into([], transducer, numbers); 

const intoArray = R.into([]);
intoArray(transducer, numbers); 
```


## invert Object

{s: x} → {x: [ s, … ]}

Parameters

- obj The object or array to invert

Returns

Object

out A new object with keys in an array.

Added in v0.9.0

Same as `R.invertObj`, however this accounts for objects with duplicate values by putting the values into an array.

See also

invertObj

.

```
const raceResultsByFirstName = {
  first: 'alice',
  second: 'jake',
  third: 'alice',
};
R.invert(raceResultsByFirstName);
```


## invertObj Object

{s: x} → {x: s}

Parameters

- obj The object or array to invert

Returns

Object

out A new object

Added in v0.9.0

Returns a new object with the keys of the given object as values, and the values of the given object, which are coerced to strings, as keys. Note that the last key found is preferred when handling the same value.

See also

invert

.

```
const raceResults = {
  first: 'alice',
  second: 'jake'
};
R.invertObj(raceResults);

const raceResults = ['alice', 'jake'];
R.invertObj(raceResults);
```


## invoker Function

Number → String → (a → b → … → n → Object → *)

Parameters

- arity Number of arguments the returned function should take before the target object.
- method Name of any of the target object's methods to call.

Returns

function

A new curried function.

Added in v0.1.0

Given an `arity` (Number) and a `name` (String) the `invoker` function returns a curried function that takes `arity` arguments and a `context` object. It will "invoke" the `name`'d function (a method) on the `context` object.

See also

construct

.

```
const asJson = invoker(0, "json")

fetch("http://example.com/index.json").then(asJson)

const sliceFrom = invoker(1, 'slice');
sliceFrom(6, 'abcdefghijklm'); 

const sliceFrom6 = invoker(2, 'slice')(6);
sliceFrom6(8, 'abcdefghijklm'); 

const firstCreditCardSection = invoker(2, "slice", 0, 4)
firstCreditCardSection("4242 4242 4242 4242") 

const firstCreditCardSection = invoker(2, "slice")(0, 4)
firstCreditCardSection("4242 4242 4242 4242") 
```


## is Type

(* → {*}) → a → Boolean

Parameters

- ctor A constructor
- val The value to test

Returns

Boolean

Added in v0.3.0

See if an object (i.e. `val`) is an instance of the supplied constructor. This function will check up the inheritance chain, if any. If `val` was created using `Object.create`, `R.is(Object, val) === true`.

```
R.is(Object, {}); 
R.is(Number, 1); 
R.is(Object, 1); 
R.is(String, 's'); 
R.is(String, new String('')); 
R.is(Object, new String('')); 
R.is(Object, 's'); 
R.is(Number, {}); 
```


## isEmpty Logic

a → Boolean

Parameters

- x

Returns

Boolean

Added in v0.1.0

Returns `true` if the given value is its type's empty value; `false` otherwise.

See also

empty

,

isNotEmpty

.

```
R.isEmpty([1, 2, 3]);           
R.isEmpty([]);                  
R.isEmpty('');                  
R.isEmpty(null);                
R.isEmpty({});                  
R.isEmpty({length: 0});         
R.isEmpty(Uint8Array.from('')); 
R.isEmpty(new Set())            
R.isEmpty(new Map())            
```


## isNil Type

* → Boolean

Parameters

- x The value to test.

Returns

Boolean

`true` if `x` is `undefined` or `null`, otherwise `false`.

Added in v0.9.0

Checks if the input value is `null` or `undefined`.

```
R.isNil(null); 
R.isNil(undefined); 
R.isNil(0); 
R.isNil([]); 
```


## isNotEmpty Logic

a → Boolean

Parameters

- x

Returns

Boolean

Added in v0.29.2

Returns `false` if the given value is its type's empty value; `true` otherwise.

See also

empty

,

isEmpty

.

```
R.isNotEmpty([1, 2, 3]);           
R.isNotEmpty([]);                  
R.isNotEmpty('');                  
R.isNotEmpty(null);                
R.isNotEmpty({});                  
R.isNotEmpty({length: 0});         
R.isNotEmpty(Uint8Array.from('')); 
```


## isNotNil Type

* → Boolean

Parameters

- x The value to test.

Returns

Boolean

`true` if `x` is not `undefined` or not `null`, otherwise `false`.

Added in v0.29.0

Checks if the input value is not `null` and not `undefined`.

```
R.isNotNil(null); 
R.isNotNil(undefined); 
R.isNotNil(0); 
R.isNotNil([]); 
```


## join List

String → [a] → String

Parameters

- separator The string used to separate the elements.
- xs The elements to join into a string.

Returns

String

str The string made by concatenating `xs` with `separator`.

Added in v0.1.0

Returns a string made by inserting the `separator` between each element and concatenating all the elements into a single string.

See also

split

.

```
const spacer = R.join(' ');
spacer(['a', 2, 3.4]);   
R.join('|', [1, 2, 3]);    
```


## juxt Function

[(a, b, …, m) → n] → ((a, b, …, m) → [n])

Parameters

- fns An array of functions

Returns

function

A function that returns a list of values after applying each of the original `fns` to its parameters.

Added in v0.19.0

juxt applies a list of functions to a list of values.

See also

applySpec

.

```
const getRange = R.juxt([Math.min, Math.max]);
getRange(3, 4, 9, -3); 
```


## keys Object

{k: v} → [k]

Parameters

- obj The object to extract properties from

Returns

Array

An array of the object's own properties.

Added in v0.1.0

Returns a list containing the names of all the enumerable own properties of the supplied object. Note that the order of the output array is not guaranteed to be consistent across different JS platforms.

See also

keysIn

,

values

,

toPairs

.

```
R.keys({a: 1, b: 2, c: 3}); 
```


## keysIn Object

{k: v} → [k]

Parameters

- obj The object to extract properties from

Returns

Array

An array of the object's own and prototype properties.

Added in v0.2.0

Returns a list containing the names of all the properties of the supplied object, including prototype properties. Note that the order of the output array is not guaranteed to be consistent across different JS platforms.

See also

keys

,

valuesIn

.

```
const F = function() { this.x = 'X'; };
F.prototype.y = 'Y';
const f = new F();
R.keysIn(f); 
```


## last List

[a] → a | Undefined

String → String | Undefined

Parameters

- list

Returns

*

Added in v0.1.4

Returns the last element of the given list or string.

See also

init

,

head

,

tail

.

```
R.last([1, 2, 3]);  
R.last([1]);        
R.last([]);         

R.last('abc');  
R.last('a');    
R.last('');     
```


## lastIndexOf List

a → [a] → Number

Parameters

- target The item to find.
- xs The array to search in.

Returns

Number

the index of the target, or -1 if the target is not found.

Added in v0.1.0

Returns the position of the last occurrence of an item in an array, or -1 if the item is not included in the array. `R.equals` is used to determine equality.

See also

indexOf

,

findLastIndex

.

```
R.lastIndexOf(3, [-1,3,3,0,1,2,3,4]); 
R.lastIndexOf(10, [1,2,3,4]); 
```


## length List

[a] → Number

Parameters

- list The array to inspect.

Returns

Number

The length of the array.

Added in v0.3.0

Returns the number of elements in the array by returning `list.length`.

```
R.length([]); 
R.length([1, 2, 3]); 
```


## lens Object

(s → a) → ((a, s) → s) → Lens s a

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- getter
- setter

Returns

Lens

Added in v0.8.0

Returns a lens for the given getter and setter functions. The getter "gets" the value of the focus; the setter "sets" the value of the focus. The setter should not mutate the data structure.

See also

view

,

set

,

over

,

lensIndex

,

lensProp

.

```
const xLens = R.lens(R.prop('x'), R.assoc('x'));

R.view(xLens, {x: 1, y: 2});            
R.set(xLens, 4, {x: 1, y: 2});          
R.over(xLens, R.negate, {x: 1, y: 2});  
```


## lensIndex Object

Number → Lens s a

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- n

Returns

Lens

Added in v0.14.0

Returns a lens whose focus is the specified index.

When `idx < -list.length || idx >= list.length`, `R.set` or `R.over`, the original list is returned.

See also

view

,

set

,

over

,

nth

.

```
const headLens = R.lensIndex(0);

R.view(headLens, ['a', 'b', 'c']);            
R.set(headLens, 'x', ['a', 'b', 'c']);        
R.over(headLens, R.toUpper, ['a', 'b', 'c']); 

R.set(R.lensIndex(3), 'x', ['a', 'b', 'c']);         
R.over(R.lensIndex(-4), R.toUpper, ['a', 'b', 'c']); 
```


## lensPath Object

[Idx] → Lens s a

Idx = String | Int | Symbol

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- path The path to use.

Returns

Lens

Added in v0.19.0

Returns a lens whose focus is the specified path.

See also

view

,

set

,

over

.

```
const xHeadYLens = R.lensPath(['x', 0, 'y']);

R.view(xHeadYLens, {x: [{y: 2, z: 3}, {y: 4, z: 5}]});

R.set(xHeadYLens, 1, {x: [{y: 2, z: 3}, {y: 4, z: 5}]});

R.over(xHeadYLens, R.negate, {x: [{y: 2, z: 3}, {y: 4, z: 5}]});
```


## lensProp Object

String → Lens s a

Lens s a = Functor f => (a → f a) → s → f s

Parameters

- k

Returns

Lens

Added in v0.14.0

Returns a lens whose focus is the specified property.

See also

view

,

set

,

over

.

```
const xLens = R.lensProp('x');

R.view(xLens, {x: 1, y: 2});            
R.set(xLens, 4, {x: 1, y: 2});          
R.over(xLens, R.negate, {x: 1, y: 2});  
```


## lift Function

(*… → *) → ([*]… → [*])

Parameters

- fn The function to lift into higher context

Returns

function

The lifted function.

Added in v0.7.0

"lifts" a function of arity >= 1 so that it may "map over" a list, Function or other object that satisfies the FantasyLand Apply spec.

See also

liftN

.

```
const madd3 = R.lift((a, b, c) => a + b + c);

madd3([100, 200], [30, 40], [5, 6, 7]); 

const madd5 = R.lift((a, b, c, d, e) => a + b + c + d + e);

madd5([10, 20], [1], [2, 3], [4], [100, 200]); 
```


## liftN Function

Number → (*… → *) → ([*]… → [*])

Parameters

- fn The function to lift into higher context

Returns

function

The lifted function.

Added in v0.7.0

"lifts" a function to be the specified arity, so that it may "map over" that many lists, Functions or other objects that satisfy the FantasyLand Apply spec.

See also

lift

,

ap

.

```
const madd3 = R.liftN(3, (...args) => R.sum(args));
madd3([1,2,3], [1,2,3], [1]); 
```


## lt Relation

Ord a => a → a → Boolean

Parameters

- a
- b

Returns

Boolean

Added in v0.1.0

Returns `true` if the first argument is less than the second; `false` otherwise.

See also

gt

.

```
R.lt(2, 1); 
R.lt(2, 2); 
R.lt(2, 3); 
R.lt('a', 'z'); 
R.lt('z', 'a'); 
```


## lte Relation

Ord a => a → a → Boolean

Parameters

- a
- b

Returns

Boolean

Added in v0.1.0

Returns `true` if the first argument is less than or equal to the second; `false` otherwise.

See also

gte

.

```
R.lte(2, 1); 
R.lte(2, 2); 
R.lte(2, 3); 
R.lte('a', 'z'); 
R.lte('z', 'a'); 
```


## map List

Functor f => (a → b) → f a → f b

Parameters

- fn The function to be called on every element of the input `list`.
- list The list to be iterated over.

Returns

Array

The new list.

Added in v0.1.0

Takes a function and a functor, applies the function to each of the functor's values, and returns a functor of the same shape.

Ramda provides suitable `map` implementations for `Array` and `Object`, so this function may be applied to `[1, 2, 3]` or `{x: 1, y: 2, z: 3}`.

Dispatches to the `map` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

Also treats functions as functors and will compose them together.

See also

transduce

,

addIndex

,

pluck

,

project

.

```
const double = x => x * 2;

R.map(double, [1, 2, 3]); 

R.map(double, {x: 1, y: 2, z: 3}); 
```


## mapAccum List

((acc, x) → (acc, y)) → acc → [x] → (acc, [y])

Parameters

- fn The function to be called on every element of the input `list`.
- acc The accumulator value.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.10.0

The `mapAccum` function behaves like a combination of map and reduce; it applies a function to each element of a list, passing an accumulating parameter from left to right, and returning a final value of this accumulator together with the new list.

The iterator function receives two arguments, *acc* and *value*, and should return a tuple *[acc, value]*.

See also

scan

,

addIndex

,

mapAccumRight

.

```
const digits = ['1', '2', '3', '4'];
const appender = (a, b) => [a + b, a + b];

R.mapAccum(appender, 0, digits); 
```


## mapAccumRight List

((acc, x) → (acc, y)) → acc → [x] → (acc, [y])

Parameters

- fn The function to be called on every element of the input `list`.
- acc The accumulator value.
- list The list to iterate over.

Returns

*

The final, accumulated value.

Added in v0.10.0

The `mapAccumRight` function behaves like a combination of map and reduce; it applies a function to each element of a list, passing an accumulating parameter from right to left, and returning a final value of this accumulator together with the new list.

Similar to `mapAccum`, except moves through the input list from the right to the left.

The iterator function receives two arguments, *acc* and *value*, and should return a tuple *[acc, value]*.

See also

addIndex

,

mapAccum

.

```
const digits = ['1', '2', '3', '4'];
const appender = (a, b) => [b + a, b + a];

R.mapAccumRight(appender, 5, digits); 
```


## mapKeys Object

(String → String) → Object → Object

Parameters

- fn
- obj

Returns

Object

Added in v0.31.0

Transforms an object by converting the keys to new values.

**Note** that if multiple keys map to the same new key, the last one processed will dominate.

See also

map

,

rebuild

,

renameKeys

.

```
R.mapKeys(toUpper, {foo: 1, bar: 2, baz: 3}) 
```


## mapObjIndexed Object

((*, String, Object) → *) → Object → Object

Parameters

- fn
- obj

Returns

Object

Added in v0.9.0

An Object-specific version of `map`. The function is applied to three arguments: *(value, key, obj)*. If only the value is significant, use `map` instead.

See also

map

.

```
const xyz = { x: 1, y: 2, z: 3 };
const prependKeyAndDouble = (num, key, obj) => key + (num * 2);

R.mapObjIndexed(prependKeyAndDouble, xyz); 
```


## match String

RegExp → String → [String | Undefined]

Parameters

- rx A regular expression.
- str The string to match against

Returns

Array

The list of matches or empty array.

Added in v0.1.0

Tests a regular expression against a String. Note that this function will return an empty array when there are no matches. This differs from `String.prototype.match` which returns `null` when there are no matches.

See also

test

.

```
R.match(/([a-z]a)/g, 'bananas'); 
R.match(/a/, 'b'); 
R.match(/a/, null); 
```


## mathMod Math

Number → Number → Number

Parameters

- m The dividend.
- p the modulus.

Returns

Number

The result of `b mod a`.

Added in v0.3.0

`mathMod` behaves like the modulo operator should mathematically, unlike the `%` operator (and by extension, `R.modulo`). So while `-17 % 5` is `-2`, `mathMod(-17, 5)` is `3`. `mathMod` requires Integer arguments, and returns NaN when the modulus is zero or negative.

See also

modulo

.

```
R.mathMod(-17, 5);  
R.mathMod(17, 5);   
R.mathMod(17, -5);  
R.mathMod(17, 0);   
R.mathMod(17.2, 5); 
R.mathMod(17, 5.3); 

const clock = R.mathMod(R.__, 12);
clock(15); 
clock(24); 

const seventeenMod = R.mathMod(17);
seventeenMod(3);  
seventeenMod(4);  
seventeenMod(10); 
```


## max Relation

Ord a => a → a → a

Parameters

- a
- b

Returns

*

Added in v0.1.0

Returns the larger of its two arguments.

See also

maxBy

,

min

.

```
R.max(789, 123); 
R.max('a', 'b'); 
```


## maxBy Relation

Ord b => (a → b) → a → a → a

Parameters

- f
- a
- b

Returns

*

Added in v0.8.0

Takes a function and two values, and returns whichever value produces the larger result when passed to the provided function.

See also

max

,

minBy

.

```
const square = n => n * n;

R.maxBy(square, -3, 2); 

R.reduce(R.maxBy(square), 0, [3, -5, 4, 1, -2]); 
R.reduce(R.maxBy(square), 0, []); 
```


## mean Math

[Number] → Number

Parameters

- list

Returns

Number

Added in v0.14.0

Returns the mean of the given list of numbers.

See also

median

.

```
R.mean([2, 7, 9]); 
R.mean([]); 
```


## median Math

[Number] → Number

Parameters

- list

Returns

Number

Added in v0.14.0

Returns the median of the given list of numbers.

See also

mean

.

```
R.median([2, 9, 7]); 
R.median([7, 2, 10, 9]); 
R.median([]); 
```


## memoizeWith Function

(*… → String) → (*… → a) → (*… → a)

Parameters

- keyGen The function to generate the cache key.
- fn The function to memoize.

Returns

function

Memoized version of `fn`.

Added in v0.24.0

Takes a string-returning function `keyGen` and a function `fn` and returns a new function that returns cached results for subsequent calls with the same arguments.

When the function is invoked, `keyGen` is applied to the same arguments and its result becomes the cache key. If the cache contains something under that key, the function simply returns it and does not invoke `fn` at all.

Otherwise `fn` is applied to the same arguments and its return value is cached under that key and returned by the function.

Care must be taken when implementing `keyGen` to avoid key collision, or if tracking references, memory leaks and mutating arguments.

```
const withAge = memoizeWith(o => `${o.birth}/${o.death}`, ({birth, death}) => {

  console.log(`computing age for ${birth}/${death}`);
  return ({birth, death, age: death - birth});
});

withAge({birth: 1921, death: 1999});

withAge({birth: 1921, death: 1999});
```


## mergeAll List

[{k: v}] → {k: v}

Parameters

- list An array of objects

Returns

Object

A merged object.

Added in v0.10.0

Creates one new object with the own properties from a list of objects. If a key exists in more than one object, the value from the last object it exists in will be used.

See also

reduce

.

```
R.mergeAll([{foo:1},{bar:2},{baz:3}]); 
R.mergeAll([{foo:1},{foo:2},{bar:2}]); 
```


## mergeDeepLeft Object

{a} → {a} → {a}

Parameters

- lObj
- rObj

Returns

Object

Added in v0.24.0

Creates a new object with the own properties of the first object merged with the own properties of the second object. If a key exists in both objects:

- and both values are objects, the two values will be recursively merged
- otherwise the value from the first object will be used.

See also

mergeDeepRight

,

mergeDeepWith

,

mergeDeepWithKey

.

```
R.mergeDeepLeft({ name: 'fred', age: 10, contact: { email: 'moo@example.com' }},
                { age: 40, contact: { email: 'baa@example.com' }});
```


## mergeDeepRight Object

{a} → {a} → {a}

Parameters

- lObj
- rObj

Returns

Object

Added in v0.24.0

Creates a new object with the own properties of the first object merged with the own properties of the second object. If a key exists in both objects:

- and both values are objects, the two values will be recursively merged
- otherwise the value from the second object will be used.

See also

mergeDeepLeft

,

mergeDeepWith

,

mergeDeepWithKey

.

```
R.mergeDeepRight({ name: 'fred', age: 10, contact: { email: 'moo@example.com' }},
                 { age: 40, contact: { email: 'baa@example.com' }});
```


## mergeDeepWith Object

((a, a) → a) → {a} → {a} → {a}

Parameters

- fn
- lObj
- rObj

Returns

Object

Added in v0.24.0

Creates a new object with the own properties of the two provided objects. If a key exists in both objects:

- and both associated values are also objects then the values will be recursively merged.
- otherwise the provided function is applied to associated values using the resulting value as the new value associated with the key. If a key only exists in one object, the value will be associated with the key of the resulting object.

See also

mergeWith

,

mergeDeepWithKey

.

```
R.mergeDeepWith(R.concat,
                { a: true, c: { values: [10, 20] }},
                { b: true, c: { values: [15, 35] }});
```


## mergeDeepWithKey Object

((String, a, a) → a) → {a} → {a} → {a}

Parameters

- fn
- lObj
- rObj

Returns

Object

Added in v0.24.0

Creates a new object with the own properties of the two provided objects. If a key exists in both objects:

- and both associated values are also objects then the values will be recursively merged.
- otherwise the provided function is applied to the key and associated values using the resulting value as the new value associated with the key. If a key only exists in one object, the value will be associated with the key of the resulting object.

See also

mergeWithKey

,

mergeDeepWith

.

```
let concatValues = (k, l, r) => k == 'values' ? R.concat(l, r) : r
R.mergeDeepWithKey(concatValues,
                   { a: true, c: { thing: 'foo', values: [10, 20] }},
                   { b: true, c: { thing: 'bar', values: [15, 35] }});
```


## mergeLeft Object

{k: v} → {k: v} → {k: v}

Parameters

- l
- r

Returns

Object

Added in v0.26.0

Create a new object with the own properties of the first object merged with the own properties of the second object. If a key exists in both objects, the value from the first object will be used.

See also

mergeRight

,

mergeDeepLeft

,

mergeWith

,

mergeWithKey

.

```
R.mergeLeft({ 'age': 40 }, { 'name': 'fred', 'age': 10 });

const resetToDefault = R.mergeLeft({x: 0});
resetToDefault({x: 5, y: 2}); 
```


## mergeRight Object

{k: v} → {k: v} → {k: v}

Parameters

- l
- r

Returns

Object

Added in v0.26.0

Create a new object with the own properties of the first object merged with the own properties of the second object. If a key exists in both objects, the value from the second object will be used.

See also

mergeLeft

,

mergeDeepRight

,

mergeWith

,

mergeWithKey

.

```
R.mergeRight({ 'name': 'fred', 'age': 10 }, { 'age': 40 });

const withDefaults = R.mergeRight({x: 0, y: 0});
withDefaults({y: 2}); 
```


## mergeWith Object

((a, a) → a) → {a} → {a} → {a}

Parameters

- fn
- l
- r

Returns

Object

Added in v0.19.0

Creates a new object with the own properties of the two provided objects. If a key exists in both objects, the provided function is applied to the values associated with the key in each object, with the result being used as the value associated with the key in the returned object.

See also

mergeDeepWith

,

mergeWithKey

.

```
R.mergeWith(R.concat,
            { a: true, values: [10, 20] },
            { b: true, values: [15, 35] });
```


## mergeWithKey Object

((String, a, a) → a) → {a} → {a} → {a}

Parameters

- fn
- l
- r

Returns

Object

Added in v0.19.0

Creates a new object with the own properties of the two provided objects. If a key exists in both objects, the provided function is applied to the key and the values associated with the key in each object, with the result being used as the value associated with the key in the returned object.

See also

mergeDeepWithKey

,

mergeWith

.

```
let concatValues = (k, l, r) => k == 'values' ? R.concat(l, r) : r
R.mergeWithKey(concatValues,
               { a: true, thing: 'foo', values: [10, 20] },
               { b: true, thing: 'bar', values: [15, 35] });
```


## min Relation

Ord a => a → a → a

Parameters

- a
- b

Returns

*

Added in v0.1.0

Returns the smaller of its two arguments.

See also

minBy

,

max

.

```
R.min(789, 123); 
R.min('a', 'b'); 
```


## minBy Relation

Ord b => (a → b) → a → a → a

Parameters

- f
- a
- b

Returns

*

Added in v0.8.0

Takes a function and two values, and returns whichever value produces the smaller result when passed to the provided function.

See also

min

,

maxBy

.

```
const square = n => n * n;

R.minBy(square, -3, 2); 

R.reduce(R.minBy(square), Infinity, [3, -5, 4, 1, -2]); 
R.reduce(R.minBy(square), Infinity, []); 
```


## modify Object

Idx → (v → v) → {k: v} → {k: v}

Parameters

- prop The property to be modified.
- fn The function to apply to the property.
- object The object to be transformed.

Returns

Object

The transformed object.

Added in v0.28.0

Creates a copy of the passed object by applying an `fn` function to the given `prop` property.

The function will not be invoked, and the object will not change if its corresponding property does not exist in the object. All non-primitive properties are copied to the new object by reference.

```
const person = {name: 'James', age: 20, pets: ['dog', 'cat']};
R.modify('age', R.add(1), person); 
R.modify('pets', R.append('turtle'), person); 
```


## modifyPath Object

[Idx] → (v → v) → {k: v} → {k: v}

Parameters

- path The path to be modified.
- fn The function to apply to the path.
- object The object to be transformed.

Returns

Object

The transformed object.

Added in v0.28.0

Creates a shallow clone of the passed object by applying an `fn` function to the value at the given path.

The function will not be invoked, and the object will not change if its corresponding path does not exist in the object. All non-primitive properties are copied to the new object by reference.

```
const person = {name: 'James', address: { zipCode: '90216' }};
R.modifyPath(['address', 'zipCode'], R.reverse, person); 

const person = {name: 'James', addresses: [{ zipCode: '90216' }]};
R.modifyPath(['addresses', 0, 'zipCode'], R.reverse, person); 
```


## modulo Math

Number → Number → Number

Parameters

- a The value to the divide.
- b The pseudo-modulus

Returns

Number

The result of `b % a`.

Added in v0.1.1

Divides the first parameter by the second and returns the remainder. Note that this function preserves the JavaScript-style behavior for modulo. For mathematical modulo see `mathMod`.

See also

mathMod

.

```
R.modulo(17, 3); 

R.modulo(-17, 3); 
R.modulo(17, -3); 

const isOdd = R.modulo(R.__, 2);
isOdd(42); 
isOdd(21); 
```


## move List

Number → Number → [a] → [a]

Parameters

- from The source index
- to The destination index
- list The list which will serve to realise the move

Returns

Array

The new list reordered

Added in v0.27.1

Move an item, at index `from`, to index `to`, in a list of elements. A new list will be created containing the new elements order.

```
R.move(0, 2, ['a', 'b', 'c', 'd', 'e', 'f']); 
R.move(-1, 0, ['a', 'b', 'c', 'd', 'e', 'f']); 
```


## multiply Math

Number → Number → Number

Parameters

- a The first value.
- b The second value.

Returns

Number

The result of `a * b`.

Added in v0.1.0

Multiplies two numbers. Equivalent to `a * b` but curried.

See also

divide

.

```
const double = R.multiply(2);
const triple = R.multiply(3);
double(3);       
triple(4);       
R.multiply(2, 5);  
```


## nAry Function

Number → (* → a) → (* → a)

Parameters

- n The desired arity of the new function.
- fn The function to wrap.

Returns

function

A new function wrapping `fn`. The new function is guaranteed to be of arity `n`.

Added in v0.1.0

Wraps a function of any arity (including nullary) in a function that accepts exactly `n` parameters. Any extraneous parameters will not be passed to the supplied function.

See also

binary

,

unary

.

```
const takesTwoArgs = (a, b) => [a, b];

takesTwoArgs.length; 
takesTwoArgs(1, 2); 

const takesOneArg = R.nAry(1, takesTwoArgs);
takesOneArg.length; 

takesOneArg(1, 2); 
```


## negate Math

Number → Number

Parameters

- n

Returns

Number

Added in v0.9.0

Negates its argument.

```
R.negate(42); 
```


## none List

(a → Boolean) → [a] → Boolean

Parameters

- fn The predicate function.
- list The array to consider.

Returns

Boolean

`true` if the predicate is not satisfied by every element, `false` otherwise.

Added in v0.12.0

Returns `true` if no elements of the list match the predicate, `false` otherwise.

Dispatches to the `all` method of the second argument, if present.

Acts as a transducer if a transformer is given in list position.

See also

all

,

any

.

```
const isEven = n => n % 2 === 0;
const isOdd = n => n % 2 !== 0;

R.none(isEven, [1, 3, 5, 7, 9, 11]); 
R.none(isOdd, [1, 3, 5, 7, 8, 11]); 
```


## not Logic

* → Boolean

Parameters

- a any value

Returns

Boolean

the logical inverse of passed argument.

Added in v0.1.0

A function that returns the `!` of its argument. It will return `true` when passed false-y value, and `false` when passed a truth-y one.

See also

complement

.

```
R.not(true); 
R.not(false); 
R.not(0); 
R.not(1); 
```


## nth List

Number → [a] → a | Undefined

Number → String → String | Undefined

Parameters

- offset
- list

Returns

*

Added in v0.1.0

Returns the nth element of the given list or string. If n is negative the element at index length + n is returned.

```
const list = ['foo', 'bar', 'baz', 'quux'];
R.nth(1, list); 
R.nth(-1, list); 
R.nth(-99, list); 

R.nth(2, 'abc'); 
R.nth(3, 'abc'); 
```


## nthArg Function

Number → *… → *

Parameters

- n

Returns

function

Added in v0.9.0

Returns a function which returns its nth argument.

```
R.nthArg(1)('a', 'b', 'c'); 
R.nthArg(-1)('a', 'b', 'c'); 
```


## o Function

(b → c) → (a → b) → a → c

Parameters

- f
- g

Returns

function

Added in v0.24.0

`o` is a curried composition function that returns a unary function. Like `compose`, `o` performs right-to-left function composition. Unlike `compose`, the rightmost function passed to `o` will be invoked with only one argument. Also, unlike `compose`, `o` is limited to accepting only 2 unary functions. The name o was chosen because of its similarity to the mathematical composition operator ∘.

See also

compose

,

pipe

.

```
const classyGreeting = name => "The name's " + name.last + ", " + name.first + " " + name.last
const yellGreeting = R.o(R.toUpper, classyGreeting);
yellGreeting({first: 'James', last: 'Bond'}); 

R.o(R.multiply(10), R.add(10))(-4) 
```


## objOf Object

String → a → {String:a}

Parameters

- key
- val

Returns

Object

Added in v0.18.0

Creates an object containing a single key:value pair.

See also

pair

.

```
const matchPhrases = R.compose(
  R.objOf('must'),
  R.map(R.objOf('match_phrase'))
);
matchPhrases(['foo', 'bar', 'baz']); 
```


## of Function

(* → {*}) → a → {a}

Parameters

- Ctor A constructor
- val any value

Returns

*

An instance of the `Ctor` wrapping `val`.

Added in v0.3.0

Given a constructor and a value, returns a new instance of that constructor containing the value.

Dispatches to the `fantasy-land/of` method of the constructor first (if present) or to the `of` method last (if present). When neither are present, wraps the value in an array.

Note this `of` is different from the ES6 `of`; See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of

```
R.of(Array, 42);   
R.of(Array, [42]); 
R.of(Maybe, 42);   
```


## omit Object

[String] → {String: *} → {String: *}

Parameters

- names an array of String property names to omit from the new object
- obj The object to copy from

Returns

Object

A new object with properties from `names` not on it.

Added in v0.1.0

Returns a partial copy of an object omitting the keys specified.

See also

pick

.

```
R.omit(['a', 'd'], {a: 1, b: 2, c: 3, d: 4}); 
```


## on Function

((a, a) → b) → (c → a) → c → c → b

Parameters

- f a binary function
- g a unary function
- a any value
- b any value

Returns

any

The result of `f`

Added in v0.28.0

Takes a binary function `f`, a unary function `g`, and two values. Applies `g` to each value, then applies the result of each to `f`.

Also known as the P combinator.

```
const eqBy = R.on((a, b) => a === b);
eqBy(R.prop('a'), {b:0, a:1}, {a:1}) 

const containsInsensitive = R.on(R.includes, R.toLower);
containsInsensitive('o', 'FOO'); 
```
