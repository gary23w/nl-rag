---
title: "Underscore.js"
source: https://en.wikipedia.org/wiki/Underscore.js
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
---

# Underscore.js

**Underscore.js** is a JavaScript library which provides utility functions for common programming tasks. It is comparable to features provided by Prototype.js and the Ruby language, but opts for a functional programming design instead of extending object prototypes. The documentation refers to Underscore.js as "the tie to go along with jQuery's tux, and Backbone.js' suspenders." Underscore.js was created by Jeremy Ashkenas, who is also known for Backbone.js and CoffeeScript.

## History

Jeremy Ashkenas created Underscore by the end of 2009 as a spin-off from the DocumentCloud project, together with Backbone.js. It was one of the earliest libraries for JavaScript to provide general functional programming utilities, taking inspiration from Prototype.js, Oliver Steele's Functional JavaScript, and John Resig's Micro-Templating.

In 2012, John-David Dalton created a fork of Underscore, named Lo-Dash (now Lodash). Lo-Dash was initially promoted as a drop-in alternative for Underscore with "consistency, customization, performance, & extras". Nevertheless, Lodash already departed from the original Underscore interface at an early stage and started making more drastic changes with the 3.0.0 release, making it necessary for Lodash users to change their code.

In May 2015, Jeremy Ashkenas announced that John-David Dalton had contacted him about merging the libraries back together. Despite concerns about code style and code size, Ashkenas was not opposed to merging some of Lodash's extensions into Underscore. At the time, there were several developers contributing to Underscore and Lodash in parallel; this group of contributors started making changes to Underscore in order to make it more like Lodash.

In parallel to this effort, however, Dalton made more drastic changes to the Lodash interface. In June 2015, he announced Lodash version 4.0.0, which distanced Lodash even further from the Underscore interface, while making a significant departure from the version 3.x series of Lodash itself as well. This prompted some projects that depended on Lodash to create their own distributions of Lodash 3.

In February 2016, Dalton announced that he considered the merge effort to be complete. He suggested that users switch from Underscore to Lodash, motivating this with usage share statistics. A maintainer of Underscore however made clear that there was no intention to stop developing Underscore as a separate library. Both libraries entered a state of low development activity after 2016.

Over time, newer versions of the ECMAScript standard have added built-in functions to the language that replicate some of the functionality of Underscore, such as `Object.assign` and `Array.prototype.map`. However, the built-in functions are sometimes less powerful than their Underscore equivalents; in particular, built-in array iteration methods such as `map`, `filter` and `forEach` cannot iterate over plain objects and do not support iteratee shorthands.

As of March 2021, Underscore is being actively developed by Julian Gonggrijp, who started making major contributions in March 2020. The library is still widely depended upon and is being downloaded from npm several million times every week.

## Content

In essence, Underscore provides three things:

1. A collection of more than 100 reusable functions, which are meant to be practically useful in everyday applications. The documentation distinguishes several categories:
  - **Collection functions** such as `find`, `map`, `min`/`max`, `groupBy` and `shuffle` process collections of data. These functions can operate on the elements of array-like sequences as well as on the properties of objects.
  - **Array functions** such as `first`/`last`, `flatten`, `chunk` and `zip` operate exclusively on array-like objects.
  - **Function functions** such as `bind`, `memoize`, `partial` and `debounce` take a function as argument and return a new function with altered properties (higher-order functions).
  - **Object functions** is a more foundational category, containing many functions that are also reused internally in Underscore. It can be roughly divided in two subcategories:
    - Type testing functions such as `isNumber`, `isElement` and `isDataView`.
    - Functions such as `keys`, `extend`, `pick`/`omit`, `pairs` and `invert`, which manipulate (plain) objects as data.
  - **Utility functions** is a rest category. Among others, it includes the trivial functions `identity` and `noop` and the string manipulating functions `escape`, `unescape` and `template`. This category also includes the functions `iteratee` and `mixin`, which could be considered special facilities as in point 2.
2. Special facilities, such as `chain` and `iteratee`, which combine with the functions under point 1 in order to enable a shorter, cleaner syntax. The special function `_`, which the library is named after, is central to these facilities.
3. Literate source code that is meant to be read, so that it is easy to follow how the library is implemented. The documentation includes a rendered version of the source code, where the comments are on the left and the logic is on the right. The comments are formatted using Markdown and the logic has syntax highlighting. Since version 1.11, Underscore is modular. For this reason, the documentation now includes both a modular version of the annotated source, in which each function is on a separate page and the `import` references are clickable hyperlinks, and a single read version, where all functions are on a single page by order of dependency.

### Overview and examples of functions

Underscore promotes a functional style, where multiple functions can be combined in a single expression in order to obtain new functionality. For example, the following expression uses two Underscore functions to group words by their first characters:

```mw
import { groupBy, first } from 'underscore';

groupBy(['avocado', 'apricot', 'cherry', 'date', 'durian'], first);

// result:
// { a: ['avocado', 'apricot'],
//   c: ['cherry'],
//   d: ['date', 'durian']
// }
```

Underscore functions are not in any way set apart from user-defined functions. Had the user implemented her own `first` function, the above expression would have worked equally well:

```mw
import { groupBy } from 'underscore';

const first = array => array[0];

groupBy(['avocado', 'apricot', 'cherry', 'date', 'durian'], first);
```

The set of functions provided by Underscore is however specifically chosen to minimize such effort, so that the user can compose functionality out of existing functions rather than writing her own.

Functions that iterate over the contents of an array or object usually take the data as the first parameter and an iterating function or *iteratee* as the second parameter. In the example above, `first` is the iteratee passed to `groupBy`.

Although the iteratee is not required to use them, it receives three arguments in most cases: (1) the value at the current position in the collection, (2) the key or index of this value and (3) the whole collection. In the following example, the second argument is used in an iteratee to `pick` in order to select only the properties of an object of which the key starts with an uppercase letter:

```mw
import { pick } from 'underscore';

const details = {
    Official: 'Wolfgang Amadeus Mozart',
    informal: 'Wolfie'
};
const keyIsUpper = (value, key) => key[0] === key[0].toUpperCase();

pick(details, keyIsUpper);
// {Official: 'Wolfgang Amadeus Mozart'}
```

Many Underscore functions can be used as an iteratee, as previously illustrated with `first`. Apart from that, there are several common cases where the user can avoid writing an iteratee function, by using an iteratee shorthand instead. In the following example, the string `'name'` is used as an iteratee shorthand in order to extract all the `name` properties from an array of objects:

```mw
import { map } from 'underscore';

const people = [
    {name: 'Lily', age: 44, occupation: 'librarian'},
    {name: 'Harold', age: 10, occupation: 'dreamer'},
    {name: 'Sasha', age: 68, occupation: 'library developer'}
];

map(people, 'name');  // ['Lily', 'Harold', 'Sasha']
```

All functions in the "collection" category, including the `groupBy` and `map` functions demonstrated above, can iterate both over the indices of an array and over the keys of an object. This is illustrated below with `reduce`:

```mw
import { reduce } from 'underscore';

const add = (a, b) => a + b;
const sum = numbers => reduce(numbers, add, 0);

sum([11, 12, 13]);                  // 36
sum({Alice: 9, Bob: 9, Clair: 7});  // 25
```

Besides functions that iterate over arrays or objects, Underscore provides a wide range of other reusable functions. For example, `throttle` limits the frequency with which a function is evaluated:

```mw
import { throttle } from 'underscore';

// The scroll event triggers very often, so the following line may
// slow down the browser.
document.body.addEventListener('scroll', expensiveUpdateFunction);

// Limit evaluation to once every 100 milliseconds.
const throttledUpdateFunction = throttle(expensiveUpdateFunction, 100);

// Much smoother user experience!
document.body.addEventListener('scroll', throttledUpdateFunction);
```

Another example is `defaults`, which assigns object properties only if not already set:

```mw
import { defaults } from 'underscore';

const requestData = {
    url: 'wikipedia.org',
    method: 'POST',
    body: 'article text'
};
const defaultFields = {
    method: 'GET',
    headers: {'X-Requested-With': 'XMLHttpRequest'}
};

defaults(requestData, defaultFields);
// {
//     url: 'wikipedia.org',
//     method: 'POST',
//     body: 'article text',
//     headers: {'X-Requested-With': 'XMLHttpRequest'}
// }
```

### The `_` function

Underscore derives its name from the function `_`, which serves multiple purposes.

#### Wrapper function

As a function, `_` returns a wrapped version of any value that is passed as its first argument. This special object has all Underscore functions as methods, thus enabling a different notation that is referred to as "OOP style":

```mw
import _, { last } from 'underscore';

// "Normal" or "functional" style
last([1, 2, 3]); // 3

// "OOP style"
_([1, 2, 3]).last() // 3
```

This feature is used in *chaining* (next section). The value can be unwrapped again with the `.value()` method in order to further process it outside of Underscore. Values also unwrap automatically in some cases.

```mw
// Explicit unwrap
_([1, 2, 3]).value()  // [1, 2, 3]

// Automatic unwrap when coerced to number
1 + _(2)  // 3

// Automatic unwrap when coerced to string
'abc' + _('def')  // 'abcdef'

// Automatic unwrap when formatted as JSON
JSON.stringify({ a: _([1, 2]) })  // '{"a":[1,2]}'
```

#### Partial application placeholder

`_` also acts as a placeholder for the `partial` function. `partial` creates a partially applied version of a function and `_` can be used to leave some parameters "open" so that these can be supplied later. For example, the `groupBy` example from the overview can be extended as follows to turn the expression into a reusable function:

```mw
import _, { partial, groupBy, first } from 'underscore';

const groupByFirstChar = partial(groupBy, _, first);

groupByFirstChar(['avocado', 'apricot', 'cherry', 'date', 'durian']);
// { a: ['avocado', 'apricot'],
//   c: ['cherry'],
//   d: ['date', 'durian']
// }

groupByFirstChar(['chestnut', 'pistache', 'walnut', 'cashew']);
// { c: ['chestnut', 'cashew'],
//   p: ['pistache'],
//   w: ['walnut]
// }
```

#### Customization point

Furthermore, `_` serves as a central customization point where users can adjust the behavior of Underscore functions to their needs. Specifically, users can override `_.iteratee` in order to create new iteratee shorthands, and `_.templateSettings` in order to customize the `template` function.

#### Namespace handle

More generally, *all* Underscore functions are present as properties on `_`, for example also `_.map` and `_.debounce`. This makes it possible to use `_` as a namespace handle. With the arrival of modules in ES6, having such a namespace handle is no longer strictly necessary, but the practice is still commonly found in code using older module systems such as AMD and CommonJS:

```mw
var _ = require('underscore');

_.groupBy(['avocado', 'apricot', 'cherry', 'date', 'durian'], _.first);
```

Given the existing practice, it can also be a convenient notation to clarify that one means a function specifically from the Underscore library and not a function with the same name from another library. For example, both Underscore and Async provide a function named `each`; to distinguish between them, one may write `_.each` and `async.each`, respectively.

### Chaining

The function `chain` can be used to create a modified version of the wrapper produced by the `_` function. When invoked on such a *chained wrapper*, each method returns a new wrapper so that the user can continue to process intermediate results with Underscore functions:

```mw
import { chain } from 'underscore';

const square = x => x * x;
const isOdd = x => x % 2;

chain([1, 2, 3, 4]).filter(isOdd).map(square).last()
// returns a wrapper of 9
```

It is not uncommon for a function implemented with Underscore to consist entirely of a `return` statement with a chain ending in `.value()`:

```mw
const add = (x, y) => x + y;

// Given an array of numbers, return the sum of the squares of
// those numbers. This could be used in a statistics library.
function sumOfSquares(numbers) {
    return chain(numbers)
        .map(square)
        .reduce(add)
        .value();
}
```

Chaining is not exclusive to the functions that ship with Underscore. Users can enable chaining for their own functions as well by passing them to the `mixin` function:

```mw
import { reduce, mixin } from 'underscore';

const sum = numbers => reduce(numbers, add, 0);

mixin({ sum, square });

chain([1, 2, 3]).map(square).sum().value();  // 14
chain([1, 2, 3]).sum().square().value();     // 36
```

In fact, this is exactly how chaining is enabled for Underscore's own functions as well. All Underscore functions are written as regular standalone functions, without any special preparations for chaining, and then "mixed into" the `_` function afterwards.

### Iteratee shorthands

As previously mentioned in the overview, most Underscore functions that iterate over arrays or objects accept a shorthand notation as iteratee instead of a function. Repeating the example from that section here:

```mw
import { map } from 'underscore';

const people = [
    {name: 'Lily', details: {age: 44, occupation: 'fire fighter'}},
    {name: 'Harold', details: {age: 10, occupation: 'dreamer'}},
    {name: 'Sasha', details: {age: 68, occupation: 'library developer'}}
];

map(people, 'name');  // ['Lily', 'Harold', 'Sasha']
```

Under the hood, this notation is enabled by passing the shorthand value through `_.iteratee` in order to obtain a function. `_.iteratee` defaults to the `iteratee` function that ships with Underscore, which, depending on the value, returns a function as follows.

#### Paths

When the value is a string, `iteratee` forwards the value to `property`, which interprets the string as a property key. It returns a function that attempts to extract the property with the given key from its argument. The following expressions are all equivalent:

```mw
import { iteratee, property } from 'underscore';

map(people, 'name');
map(people, iteratee('name'));
map(people, property('name'));
map(people, obj => obj && obj['name']);
// ['Lily', 'Harold', 'Sasha']
```

Arrays and numbers are also passed to `property`. Arrays can be used to retrieve nested properties:

```mw
map(people, ['details', 'occupation']);
// ['fire fighter', 'dreamer', 'library developer']
```

Numbers can be used as array and string indices. Combining all of this, we can use the following expression to count how many times letters of the alphabet occur as the second character of a person's occupation:

```mw
import { countBy } from 'underscore';

countBy(people, ['details', 'occupation', 1]);  // {i: 2, r: 1}
```

#### Attribute hashes

When the value is an object, `iteratee` forwards it to `matcher`, which interprets the object as a set of attributes that must be matched. It returns a function that will return `true` or `false` depending on whether its argument has this same set of attributes.

```mw
import { find } from 'underscore';

find(people, {name: 'Sasha'});
// {name: 'Sasha', details: {age: 68, occupation: 'library developer'}}

find(people, {name: 'Walter'});
// undefined
```

#### `null` and `undefined`

When the value is `null` or `undefined`, `iteratee` returns the identity function that Underscore exports as `identity`. This can be used to filter out the truthy values from a collection:

```mw
import { filter, iteratee, identity } from 'underscore';

const example = [0, 1, '', 'abc', true, false, {}];

// The following expressions are all equivalent.
filter(example);
filter(example, undefined);
filter(example, iteratee(undefined));
filter(example, identity);
// [1, 'abc', true, {}]
```

#### Overriding `_.iteratee`

Users can override _.iteratee in order to create custom shorthands. The following example illustrates how one may use this to implement regular expression filtering:

```mw
import {
    iteratee as originalIteratee,
    isRegExp,
    mixin,
    filter,
} from 'underscore';

function iteratee(value, context) {
    if (isRegExp(value)) {
        return string => value.test(string);
    } else {
        return originalIteratee(value, context);
    }
}

mixin({iteratee});

filter(['absolutely', 'amazing', 'fabulous', 'trousers'], /ab/);
// ['absolutely', 'fabulous']
```
