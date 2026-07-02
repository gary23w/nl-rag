---
title: "Lodash Documentation (part 3/5)"
source: https://lodash.com/docs/
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
part: 3/5
---

## `“Lang” Methods`

### `_.castArray(value)`

source npm package

Casts `value` as an array if it's not one.Since

4.4.0Arguments`value` *(*)*: The value to inspect.Returns

*(Array)*: Returns the cast array.Example_.castArray(1); _.castArray({ 'a': 1 }); _.castArray('abc'); _.castArray(null); _.castArray(undefined); _.castArray(); var array = [1, 2, 3];console.log(_.castArray(array) === array);

### `_.clone(value)`

source npm package

Creates a shallow clone of `value`. **Note:** This method is loosely based on the structured clone algorithm and supports cloning arrays, array buffers, booleans, date objects, maps, numbers, `Object` objects, regexes, sets, strings, symbols, and typed arrays. The own enumerable properties of `arguments` objects are cloned as plain objects. An empty object is returned for uncloneable values such as error objects, functions, DOM nodes, and WeakMaps.Since

0.1.0Arguments`value` *(*)*: The value to clone.Returns

*(*)*: Returns the cloned value.Examplevar objects = [{ 'a': 1 }, { 'b': 2 }]; var shallow = _.clone(objects);console.log(shallow[0] === objects[0]);

### `_.cloneDeep(value)`

source npm package

This method is like `_.clone` except that it recursively clones `value`.Since

1.0.0Arguments`value` *(*)*: The value to recursively clone.Returns

*(*)*: Returns the deep cloned value.Examplevar objects = [{ 'a': 1 }, { 'b': 2 }]; var deep = _.cloneDeep(objects);console.log(deep[0] === objects[0]);

### `_.cloneDeepWith(value, [customizer])`

source npm package

This method is like `_.cloneWith` except that it recursively clones `value`.Since

4.0.0Arguments`value` *(*)*: The value to recursively clone.`[customizer]` *(Function)*: The function to customize cloning.Returns

*(*)*: Returns the deep cloned value.Examplefunction customizer(value) {  if (_.isElement(value)) {    return value.cloneNode(true);  }} var el = _.cloneDeepWith(document.body, customizer); console.log(el === document.body);console.log(el.nodeName);console.log(el.childNodes.length);

### `_.cloneWith(value, [customizer])`

source npm package

This method is like `_.clone` except that it accepts `customizer` which is invoked to produce the cloned value. If `customizer` returns `undefined`, cloning is handled by the method instead. The `customizer` is invoked with up to four arguments; *(value [, index|key, object, stack])*.Since

4.0.0Arguments`value` *(*)*: The value to clone.`[customizer]` *(Function)*: The function to customize cloning.Returns

*(*)*: Returns the cloned value.Examplefunction customizer(value) {  if (_.isElement(value)) {    return value.cloneNode(false);  }} var el = _.cloneWith(document.body, customizer); console.log(el === document.body);console.log(el.nodeName);console.log(el.childNodes.length);

### `_.conformsTo(object, source)`

source npm package

Checks if `object` conforms to `source` by invoking the predicate properties of `source` with the corresponding property values of `object`. **Note:** This method is equivalent to `_.conforms` when `source` is partially applied.Since

4.14.0Arguments`object` *(Object)*: The object to inspect.`source` *(Object)*: The object of property predicates to conform to.Returns

*(boolean)*: Returns `true` if `object` conforms, else `false`.Examplevar object = { 'a': 1, 'b': 2 }; _.conformsTo(object, { 'b': function(n) { return n > 1; } }); _.conformsTo(object, { 'b': function(n) { return n > 2; } });

### `_.eq(value, other)`

source npm package

Performs a `SameValueZero` comparison between two values to determine if they are equivalent.Since

4.0.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.Returns

*(boolean)*: Returns `true` if the values are equivalent, else `false`.Examplevar object = { 'a': 1 };var other = { 'a': 1 }; _.eq(object, object); _.eq(object, other); _.eq('a', 'a'); _.eq('a', Object('a')); _.eq(NaN, NaN);

### `_.gt(value, other)`

source npm package

Checks if `value` is greater than `other`.Since

3.9.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.Returns

*(boolean)*: Returns `true` if `value` is greater than `other`, else `false`.Example_.gt(3, 1); _.gt(3, 3); _.gt(1, 3);

### `_.gte(value, other)`

source npm package

Checks if `value` is greater than or equal to `other`.Since

3.9.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.Returns

*(boolean)*: Returns `true` if `value` is greater than or equal to `other`, else `false`.Example_.gte(3, 1); _.gte(3, 3); _.gte(1, 3);

### `_.isArguments(value)`

source npm package

Checks if `value` is likely an `arguments` object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an `arguments` object, else `false`.Example_.isArguments(function() { return arguments; }()); _.isArguments([1, 2, 3]);

### `_.isArray(value)`

source npm package

Checks if `value` is classified as an `Array` object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an array, else `false`.Example_.isArray([1, 2, 3]); _.isArray(document.body.children); _.isArray('abc'); _.isArray(_.noop);

### `_.isArrayBuffer(value)`

source npm package

Checks if `value` is classified as an `ArrayBuffer` object.Since

4.3.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an array buffer, else `false`.Example_.isArrayBuffer(new ArrayBuffer(2)); _.isArrayBuffer(new Array(2));

### `_.isArrayLike(value)`

source npm package

Checks if `value` is array-like. A value is considered array-like if it's not a function and has a `value.length` that's an integer greater than or equal to `0` and less than or equal to `Number.MAX_SAFE_INTEGER`.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is array-like, else `false`.Example_.isArrayLike([1, 2, 3]); _.isArrayLike(document.body.children); _.isArrayLike('abc'); _.isArrayLike(_.noop);

### `_.isArrayLikeObject(value)`

source npm package

This method is like `_.isArrayLike` except that it also checks if `value` is an object.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an array-like object, else `false`.Example_.isArrayLikeObject([1, 2, 3]); _.isArrayLikeObject(document.body.children); _.isArrayLikeObject('abc'); _.isArrayLikeObject(_.noop);

### `_.isBoolean(value)`

source npm package

Checks if `value` is classified as a boolean primitive or object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a boolean, else `false`.Example_.isBoolean(false); _.isBoolean(null);

### `_.isBuffer(value)`

source npm package

Checks if `value` is a buffer.Since

4.3.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a buffer, else `false`.Example_.isBuffer(new Buffer(2)); _.isBuffer(new Uint8Array(2));

### `_.isDate(value)`

source npm package

Checks if `value` is classified as a `Date` object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a date object, else `false`.Example_.isDate(new Date); _.isDate('Mon April 23 2012');

### `_.isElement(value)`

source npm package

Checks if `value` is likely a DOM element.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a DOM element, else `false`.Example_.isElement(document.body); _.isElement('<body>');

### `_.isEmpty(value)`

source npm package

Checks if `value` is an empty object, collection, map, or set. Objects are considered empty if they have no own enumerable string keyed properties. Array-like values such as `arguments` objects, arrays, buffers, strings, or jQuery-like collections are considered empty if they have a `length` of `0`. Similarly, maps and sets are considered empty if they have a `size` of `0`.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is empty, else `false`.Example_.isEmpty(null); _.isEmpty(true); _.isEmpty(1); _.isEmpty([1, 2, 3]); _.isEmpty({ 'a': 1 });

### `_.isEqual(value, other)`

source npm package

Performs a deep comparison between two values to determine if they are equivalent. **Note:** This method supports comparing arrays, array buffers, booleans, date objects, error objects, maps, numbers, `Object` objects, regexes, sets, strings, symbols, and typed arrays. `Object` objects are compared by their own, not inherited, enumerable properties. Functions and DOM nodes are compared by strict equality, i.e. `===`.Since

0.1.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.Returns

*(boolean)*: Returns `true` if the values are equivalent, else `false`.Examplevar object = { 'a': 1 };var other = { 'a': 1 }; _.isEqual(object, other); object === other;

### `_.isEqualWith(value, other, [customizer])`

source npm package

This method is like `_.isEqual` except that it accepts `customizer` which is invoked to compare values. If `customizer` returns `undefined`, comparisons are handled by the method instead. The `customizer` is invoked with up to six arguments: *(objValue, othValue [, index|key, object, other, stack])*.Since

4.0.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.`[customizer]` *(Function)*: The function to customize comparisons.Returns

*(boolean)*: Returns `true` if the values are equivalent, else `false`.Examplefunction isGreeting(value) {  return /^h(?:i|ello)$/.test(value);} function customizer(objValue, othValue) {  if (isGreeting(objValue) && isGreeting(othValue)) {    return true;  }} var array = ['hello', 'goodbye'];var other = ['hi', 'goodbye']; _.isEqualWith(array, other, customizer);

### `_.isError(value)`

source npm package

Checks if `value` is an `Error`, `EvalError`, `RangeError`, `ReferenceError`, `SyntaxError`, `TypeError`, or `URIError` object.Since

3.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an error object, else `false`.Example_.isError(new Error); _.isError(Error);

### `_.isFinite(value)`

source npm package

Checks if `value` is a finite primitive number. **Note:** This method is based on `Number.isFinite`.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a finite number, else `false`.Example_.isFinite(3); _.isFinite(Number.MIN_VALUE); _.isFinite(Infinity); _.isFinite('3');

### `_.isFunction(value)`

source npm package

Checks if `value` is classified as a `Function` object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a function, else `false`.Example_.isFunction(_); _.isFunction(/abc/);

### `_.isInteger(value)`

source npm package

Checks if `value` is an integer. **Note:** This method is based on `Number.isInteger`.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an integer, else `false`.Example_.isInteger(3); _.isInteger(Number.MIN_VALUE); _.isInteger(Infinity); _.isInteger('3');

### `_.isLength(value)`

source npm package

Checks if `value` is a valid array-like length. **Note:** This method is loosely based on `ToLength`.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a valid length, else `false`.Example_.isLength(3); _.isLength(Number.MIN_VALUE); _.isLength(Infinity); _.isLength('3');

### `_.isMap(value)`

source npm package

Checks if `value` is classified as a `Map` object.Since

4.3.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a map, else `false`.Example_.isMap(new Map); _.isMap(new WeakMap);

### `_.isMatch(object, source)`

source npm package

Performs a partial deep comparison between `object` and `source` to determine if `object` contains equivalent property values. **Note:** This method is equivalent to `_.matches` when `source` is partially applied. Partial comparisons will match empty array and empty object `source` values against any array or object value, respectively. See `_.isEqual` for a list of supported value comparisons.Since

3.0.0Arguments`object` *(Object)*: The object to inspect.`source` *(Object)*: The object of property values to match.Returns

*(boolean)*: Returns `true` if `object` is a match, else `false`.Examplevar object = { 'a': 1, 'b': 2 }; _.isMatch(object, { 'b': 2 }); _.isMatch(object, { 'b': 1 });

### `_.isMatchWith(object, source, [customizer])`

source npm package

This method is like `_.isMatch` except that it accepts `customizer` which is invoked to compare values. If `customizer` returns `undefined`, comparisons are handled by the method instead. The `customizer` is invoked with five arguments: *(objValue, srcValue, index|key, object, source)*.Since

4.0.0Arguments`object` *(Object)*: The object to inspect.`source` *(Object)*: The object of property values to match.`[customizer]` *(Function)*: The function to customize comparisons.Returns

*(boolean)*: Returns `true` if `object` is a match, else `false`.Examplefunction isGreeting(value) {  return /^h(?:i|ello)$/.test(value);} function customizer(objValue, srcValue) {  if (isGreeting(objValue) && isGreeting(srcValue)) {    return true;  }} var object = { 'greeting': 'hello' };var source = { 'greeting': 'hi' }; _.isMatchWith(object, source, customizer);

### `_.isNaN(value)`

source npm package

Checks if `value` is `NaN`. **Note:** This method is based on `Number.isNaN` and is not the same as global `isNaN` which returns `true` for `undefined` and other non-number values.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is `NaN`, else `false`.Example_.isNaN(NaN); _.isNaN(new Number(NaN)); isNaN(undefined); _.isNaN(undefined);

### `_.isNative(value)`

source npm package

Checks if `value` is a pristine native function. **Note:** This method can't reliably detect native functions in the presence of the core-js package because core-js circumvents this kind of detection. Despite multiple requests, the core-js maintainer has made it clear: any attempt to fix the detection will be obstructed. As a result, we're left with little choice but to throw an error. Unfortunately, this also affects packages, like babel-polyfill, which rely on core-js.Since

3.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a native function, else `false`.Example_.isNative(Array.prototype.push); _.isNative(_);

### `_.isNil(value)`

source npm package

Checks if `value` is `null` or `undefined`.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is nullish, else `false`.Example_.isNil(null); _.isNil(void 0); _.isNil(NaN);

### `_.isNull(value)`

source npm package

Checks if `value` is `null`.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is `null`, else `false`.Example_.isNull(null); _.isNull(void 0);

### `_.isNumber(value)`

source npm package

Checks if `value` is classified as a `Number` primitive or object. **Note:** To exclude `Infinity`, `-Infinity`, and `NaN`, which are classified as numbers, use the `_.isFinite` method.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a number, else `false`.Example_.isNumber(3); _.isNumber(Number.MIN_VALUE); _.isNumber(Infinity); _.isNumber('3');

### `_.isObject(value)`

source npm package

Checks if `value` is the language type of `Object`. *(e.g. arrays, functions, objects, regexes, `new Number(0)`, and `new String('')`)*Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is an object, else `false`.Example_.isObject({}); _.isObject([1, 2, 3]); _.isObject(_.noop); _.isObject(null);

### `_.isObjectLike(value)`

source npm package

Checks if `value` is object-like. A value is object-like if it's not `null` and has a `typeof` result of "object".Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is object-like, else `false`.Example_.isObjectLike({}); _.isObjectLike([1, 2, 3]); _.isObjectLike(_.noop); _.isObjectLike(null);

### `_.isPlainObject(value)`

source npm package

Checks if `value` is a plain object, that is, an object created by the `Object` constructor or one with a `[[Prototype]]` of `null`.Since

0.8.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a plain object, else `false`.Examplefunction Foo() {  this.a = 1;} _.isPlainObject(new Foo); _.isPlainObject([1, 2, 3]); _.isPlainObject({ 'x': 0, 'y': 0 }); _.isPlainObject(Object.create(null));

### `_.isRegExp(value)`

source npm package

Checks if `value` is classified as a `RegExp` object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a regexp, else `false`.Example_.isRegExp(/abc/); _.isRegExp('/abc/');

### `_.isSafeInteger(value)`

source npm package

Checks if `value` is a safe integer. An integer is safe if it's an IEEE-754 double precision number which isn't the result of a rounded unsafe integer. **Note:** This method is based on `Number.isSafeInteger`.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a safe integer, else `false`.Example_.isSafeInteger(3); _.isSafeInteger(Number.MIN_VALUE); _.isSafeInteger(Infinity); _.isSafeInteger('3');

### `_.isSet(value)`

source npm package

Checks if `value` is classified as a `Set` object.Since

4.3.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a set, else `false`.Example_.isSet(new Set); _.isSet(new WeakSet);

### `_.isString(value)`

source npm package

Checks if `value` is classified as a `String` primitive or object.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a string, else `false`.Example_.isString('abc'); _.isString(1);

### `_.isSymbol(value)`

source npm package

Checks if `value` is classified as a `Symbol` primitive or object.Since

4.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a symbol, else `false`.Example_.isSymbol(Symbol.iterator); _.isSymbol('abc');

### `_.isTypedArray(value)`

source npm package

Checks if `value` is classified as a typed array.Since

3.0.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a typed array, else `false`.Example_.isTypedArray(new Uint8Array); _.isTypedArray([]);

### `_.isUndefined(value)`

source npm package

Checks if `value` is `undefined`.Since

0.1.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is `undefined`, else `false`.Example_.isUndefined(void 0); _.isUndefined(null);

### `_.isWeakMap(value)`

source npm package

Checks if `value` is classified as a `WeakMap` object.Since

4.3.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a weak map, else `false`.Example_.isWeakMap(new WeakMap); _.isWeakMap(new Map);

### `_.isWeakSet(value)`

source npm package

Checks if `value` is classified as a `WeakSet` object.Since

4.3.0Arguments`value` *(*)*: The value to check.Returns

*(boolean)*: Returns `true` if `value` is a weak set, else `false`.Example_.isWeakSet(new WeakSet); _.isWeakSet(new Set);

### `_.lt(value, other)`

source npm package

Checks if `value` is less than `other`.Since

3.9.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.Returns

*(boolean)*: Returns `true` if `value` is less than `other`, else `false`.Example_.lt(1, 3); _.lt(3, 3); _.lt(3, 1);

### `_.lte(value, other)`

source npm package

Checks if `value` is less than or equal to `other`.Since

3.9.0Arguments`value` *(*)*: The value to compare.`other` *(*)*: The other value to compare.Returns

*(boolean)*: Returns `true` if `value` is less than or equal to `other`, else `false`.Example_.lte(1, 3); _.lte(3, 3); _.lte(3, 1);

### `_.toArray(value)`

source npm package

Converts `value` to an array.Since

0.1.0Arguments`value` *(*)*: The value to convert.Returns

*(Array)*: Returns the converted array.Example_.toArray({ 'a': 1, 'b': 2 }); _.toArray('abc'); _.toArray(1); _.toArray(null);

### `_.toFinite(value)`

source npm package

Converts `value` to a finite number.Since

4.12.0Arguments`value` *(*)*: The value to convert.Returns

*(number)*: Returns the converted number.Example_.toFinite(3.2); _.toFinite(Number.MIN_VALUE); _.toFinite(Infinity); _.toFinite('3.2');

### `_.toInteger(value)`

source npm package

Converts `value` to an integer. **Note:** This method is loosely based on `ToInteger`.Since

4.0.0Arguments`value` *(*)*: The value to convert.Returns

*(number)*: Returns the converted integer.Example_.toInteger(3.2); _.toInteger(Number.MIN_VALUE); _.toInteger(Infinity); _.toInteger('3.2');

### `_.toLength(value)`

source npm package

Converts `value` to an integer suitable for use as the length of an array-like object. **Note:** This method is based on `ToLength`.Since

4.0.0Arguments`value` *(*)*: The value to convert.Returns

*(number)*: Returns the converted integer.Example_.toLength(3.2); _.toLength(Number.MIN_VALUE); _.toLength(Infinity); _.toLength('3.2');

### `_.toNumber(value)`

source npm package

Converts `value` to a number.Since

4.0.0Arguments`value` *(*)*: The value to process.Returns

*(number)*: Returns the number.Example_.toNumber(3.2); _.toNumber(Number.MIN_VALUE); _.toNumber(Infinity); _.toNumber('3.2');

### `_.toPlainObject(value)`

source npm package

Converts `value` to a plain object flattening inherited enumerable string keyed properties of `value` to own properties of the plain object.Since

3.0.0Arguments`value` *(*)*: The value to convert.Returns

*(Object)*: Returns the converted plain object.Examplefunction Foo() {  this.b = 2;} Foo.prototype.c = 3; _.assign({ 'a': 1 }, new Foo); _.assign({ 'a': 1 }, _.toPlainObject(new Foo));

### `_.toSafeInteger(value)`

source npm package

Converts `value` to a safe integer. A safe integer can be compared and represented correctly.Since

4.0.0Arguments`value` *(*)*: The value to convert.Returns

*(number)*: Returns the converted integer.Example_.toSafeInteger(3.2); _.toSafeInteger(Number.MIN_VALUE); _.toSafeInteger(Infinity); _.toSafeInteger('3.2');

### `_.toString(value)`

source npm package

Converts `value` to a string. An empty string is returned for `null` and `undefined` values. The sign of `-0` is preserved.Since

4.0.0Arguments`value` *(*)*: The value to convert.Returns

*(string)*: Returns the converted string.Example_.toString(null); _.toString(-0); _.toString([1, 2, 3]);


## `“Math” Methods`

### `_.add(augend, addend)`

source npm package

Adds two numbers.Since

3.4.0Arguments`augend` *(number)*: The first number in an addition.`addend` *(number)*: The second number in an addition.Returns

*(number)*: Returns the total.Example_.add(6, 4);

### `_.ceil(number, [precision=0])`

source npm package

Computes `number` rounded up to `precision`.Since

3.10.0Arguments`number` *(number)*: The number to round up.`[precision=0]` *(number)*: The precision to round up to.Returns

*(number)*: Returns the rounded up number.Example_.ceil(4.006); _.ceil(6.004, 2); _.ceil(6040, -2);

### `_.divide(dividend, divisor)`

source npm package

Divide two numbers.Since

4.7.0Arguments`dividend` *(number)*: The first number in a division.`divisor` *(number)*: The second number in a division.Returns

*(number)*: Returns the quotient.Example_.divide(6, 4);

### `_.floor(number, [precision=0])`

source npm package

Computes `number` rounded down to `precision`.Since

3.10.0Arguments`number` *(number)*: The number to round down.`[precision=0]` *(number)*: The precision to round down to.Returns

*(number)*: Returns the rounded down number.Example_.floor(4.006); _.floor(0.046, 2); _.floor(4060, -2);

### `_.max(array)`

source npm package

Computes the maximum value of `array`. If `array` is empty or falsey, `undefined` is returned.Since

0.1.0Arguments`array` *(Array)*: The array to iterate over.Returns

*(*)*: Returns the maximum value.Example_.max([4, 2, 8, 6]); _.max([]);

### `_.maxBy(array, [iteratee=_.identity])`

source npm package

This method is like `_.max` except that it accepts `iteratee` which is invoked for each element in `array` to generate the criterion by which the value is ranked. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`array` *(Array)*: The array to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(*)*: Returns the maximum value.Examplevar objects = [{ 'n': 1 }, { 'n': 2 }]; _.maxBy(objects, function(o) { return o.n; }); _.maxBy(objects, 'n');

### `_.mean(array)`

source npm package

Computes the mean of the values in `array`.Since

4.0.0Arguments`array` *(Array)*: The array to iterate over.Returns

*(number)*: Returns the mean.Example_.mean([4, 2, 8, 6]);

### `_.meanBy(array, [iteratee=_.identity])`

source npm package

This method is like `_.mean` except that it accepts `iteratee` which is invoked for each element in `array` to generate the value to be averaged. The iteratee is invoked with one argument: *(value)*.Since

4.7.0Arguments`array` *(Array)*: The array to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(number)*: Returns the mean.Examplevar objects = [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]; _.meanBy(objects, function(o) { return o.n; }); _.meanBy(objects, 'n');

### `_.min(array)`

source npm package

Computes the minimum value of `array`. If `array` is empty or falsey, `undefined` is returned.Since

0.1.0Arguments`array` *(Array)*: The array to iterate over.Returns

*(*)*: Returns the minimum value.Example_.min([4, 2, 8, 6]); _.min([]);

### `_.minBy(array, [iteratee=_.identity])`

source npm package

This method is like `_.min` except that it accepts `iteratee` which is invoked for each element in `array` to generate the criterion by which the value is ranked. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`array` *(Array)*: The array to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(*)*: Returns the minimum value.Examplevar objects = [{ 'n': 1 }, { 'n': 2 }]; _.minBy(objects, function(o) { return o.n; }); _.minBy(objects, 'n');

### `_.multiply(multiplier, multiplicand)`

source npm package

Multiply two numbers.Since

4.7.0Arguments`multiplier` *(number)*: The first number in a multiplication.`multiplicand` *(number)*: The second number in a multiplication.Returns

*(number)*: Returns the product.Example_.multiply(6, 4);

### `_.round(number, [precision=0])`

source npm package

Computes `number` rounded to `precision`.Since

3.10.0Arguments`number` *(number)*: The number to round.`[precision=0]` *(number)*: The precision to round to.Returns

*(number)*: Returns the rounded number.Example_.round(4.006); _.round(4.006, 2); _.round(4060, -2);

### `_.subtract(minuend, subtrahend)`

source npm package

Subtract two numbers.Since

4.0.0Arguments`minuend` *(number)*: The first number in a subtraction.`subtrahend` *(number)*: The second number in a subtraction.Returns

*(number)*: Returns the difference.Example_.subtract(6, 4);

### `_.sum(array)`

source npm package

Computes the sum of the values in `array`.Since

3.4.0Arguments`array` *(Array)*: The array to iterate over.Returns

*(number)*: Returns the sum.Example_.sum([4, 2, 8, 6]);

### `_.sumBy(array, [iteratee=_.identity])`

source npm package

This method is like `_.sum` except that it accepts `iteratee` which is invoked for each element in `array` to generate the value to be summed. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`array` *(Array)*: The array to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(number)*: Returns the sum.Examplevar objects = [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]; _.sumBy(objects, function(o) { return o.n; }); _.sumBy(objects, 'n');


## `“Number” Methods`

### `_.clamp(number, [lower], upper)`

source npm package

Clamps `number` within the inclusive `lower` and `upper` bounds.Since

4.0.0Arguments`number` *(number)*: The number to clamp.`[lower]` *(number)*: The lower bound.`upper` *(number)*: The upper bound.Returns

*(number)*: Returns the clamped number.Example_.clamp(-10, -5, 5); _.clamp(10, -5, 5);

### `_.inRange(number, [start=0], end)`

source npm package

Checks if `n` is between `start` and up to, but not including, `end`. If `end` is not specified, it's set to `start` with `start` then set to `0`. If `start` is greater than `end` the params are swapped to support negative ranges.Since

3.3.0Arguments`number` *(number)*: The number to check.`[start=0]` *(number)*: The start of the range.`end` *(number)*: The end of the range.Returns

*(boolean)*: Returns `true` if `number` is in the range, else `false`.Example_.inRange(3, 2, 4); _.inRange(4, 8); _.inRange(4, 2); _.inRange(2, 2); _.inRange(1.2, 2); _.inRange(5.2, 4); _.inRange(-3, -2, -6);

### `_.random([lower=0], [upper=1], [floating])`

source npm package

Produces a random number between the inclusive `lower` and `upper` bounds. If only one argument is provided a number between `0` and the given number is returned. If `floating` is `true`, or either `lower` or `upper` are floats, a floating-point number is returned instead of an integer. **Note:** JavaScript follows the IEEE-754 standard for resolving floating-point values which can produce unexpected results. **Note:** If `lower` is greater than `upper`, the values are swapped.Since

0.7.0Arguments`[lower=0]` *(number)*: The lower bound.`[upper=1]` *(number)*: The upper bound.`[floating]` *(boolean)*: Specify returning a floating-point number.Returns

*(number)*: Returns the random number.Example_.random(0, 5); _.random(5, 0); _.random(5); _.random(-5); _.random(5, true); _.random(1.2, 5.2);
