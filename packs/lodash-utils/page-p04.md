---
title: "Lodash Documentation (part 4/5)"
source: https://lodash.com/docs/
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
part: 4/5
---

## `“Object” Methods`

### `_.assign(object, [sources])`

source npm package

Assigns own enumerable string keyed properties of source objects to the destination object. Source objects are applied from left to right. Subsequent sources overwrite property assignments of previous sources. **Note:** This method mutates `object` and is loosely based on `Object.assign`.Since

0.10.0Arguments`object` *(Object)*: The destination object.`[sources]` *(...Object)*: The source objects.Returns

*(Object)*: Returns `object`.Examplefunction Foo() {  this.a = 1;} function Bar() {  this.c = 3;} Foo.prototype.b = 2;Bar.prototype.d = 4; _.assign({ 'a': 0 }, new Foo, new Bar);

### `_.assignIn(object, [sources])`

source npm package

This method is like `_.assign` except that it iterates over own and inherited source properties. **Note:** This method mutates `object`.Since

4.0.0Aliases

*_.extend*Arguments`object` *(Object)*: The destination object.`[sources]` *(...Object)*: The source objects.Returns

*(Object)*: Returns `object`.Examplefunction Foo() {  this.a = 1;} function Bar() {  this.c = 3;} Foo.prototype.b = 2;Bar.prototype.d = 4; _.assignIn({ 'a': 0 }, new Foo, new Bar);

### `_.assignInWith(object, sources, [customizer])`

source npm package

This method is like `_.assignIn` except that it accepts `customizer` which is invoked to produce the assigned values. If `customizer` returns `undefined`, assignment is handled by the method instead. The `customizer` is invoked with five arguments: *(objValue, srcValue, key, object, source)*. **Note:** This method mutates `object`.Since

4.0.0Aliases

*_.extendWith*Arguments`object` *(Object)*: The destination object.`sources` *(...Object)*: The source objects.`[customizer]` *(Function)*: The function to customize assigned values.Returns

*(Object)*: Returns `object`.Examplefunction customizer(objValue, srcValue) {  return _.isUndefined(objValue) ? srcValue : objValue;} var defaults = _.partialRight(_.assignInWith, customizer); defaults({ 'a': 1 }, { 'b': 2 }, { 'a': 3 });

### `_.assignWith(object, sources, [customizer])`

source npm package

This method is like `_.assign` except that it accepts `customizer` which is invoked to produce the assigned values. If `customizer` returns `undefined`, assignment is handled by the method instead. The `customizer` is invoked with five arguments: *(objValue, srcValue, key, object, source)*. **Note:** This method mutates `object`.Since

4.0.0Arguments`object` *(Object)*: The destination object.`sources` *(...Object)*: The source objects.`[customizer]` *(Function)*: The function to customize assigned values.Returns

*(Object)*: Returns `object`.Examplefunction customizer(objValue, srcValue) {  return _.isUndefined(objValue) ? srcValue : objValue;} var defaults = _.partialRight(_.assignWith, customizer); defaults({ 'a': 1 }, { 'b': 2 }, { 'a': 3 });

### `_.at(object, [paths])`

source npm package

Creates an array of values corresponding to `paths` of `object`.Since

1.0.0Arguments`object` *(Object)*: The object to iterate over.`[paths]` *(...(string|string[]))*: The property paths to pick.Returns

*(Array)*: Returns the picked values.Examplevar object = { 'a': [{ 'b': { 'c': 3 } }, 4] }; _.at(object, ['a[0].b.c', 'a[1]']);

### `_.create(prototype, [properties])`

source npm package

Creates an object that inherits from the `prototype` object. If a `properties` object is given, its own enumerable string keyed properties are assigned to the created object.Since

2.3.0Arguments`prototype` *(Object)*: The object to inherit from.`[properties]` *(Object)*: The properties to assign to the object.Returns

*(Object)*: Returns the new object.Examplefunction Shape() {  this.x = 0;  this.y = 0;} function Circle() {  Shape.call(this);} Circle.prototype = _.create(Shape.prototype, {  'constructor': Circle}); var circle = new Circle;circle instanceof Circle; circle instanceof Shape;

### `_.defaults(object, [sources])`

source npm package

Assigns own and inherited enumerable string keyed properties of source objects to the destination object for all destination properties that resolve to `undefined`. Source objects are applied from left to right. Once a property is set, additional values of the same property are ignored. **Note:** This method mutates `object`.Since

0.1.0Arguments`object` *(Object)*: The destination object.`[sources]` *(...Object)*: The source objects.Returns

*(Object)*: Returns `object`.Example_.defaults({ 'a': 1 }, { 'b': 2 }, { 'a': 3 });

### `_.defaultsDeep(object, [sources])`

source npm package

This method is like `_.defaults` except that it recursively assigns default properties. **Note:** This method mutates `object`.Since

3.10.0Arguments`object` *(Object)*: The destination object.`[sources]` *(...Object)*: The source objects.Returns

*(Object)*: Returns `object`.Example_.defaultsDeep({ 'a': { 'b': 2 } }, { 'a': { 'b': 1, 'c': 3 } });

### `_.findKey(object, [predicate=_.identity])`

source npm package

This method is like `_.find` except that it returns the key of the first element `predicate` returns truthy for instead of the element itself.Since

1.1.0Arguments`object` *(Object)*: The object to inspect.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(*)*: Returns the key of the matched element, else `undefined`.Examplevar users = {  'barney':  { 'age': 36, 'active': true },  'fred':    { 'age': 40, 'active': false },  'pebbles': { 'age': 1,  'active': true }}; _.findKey(users, function(o) { return o.age < 40; }); _.findKey(users, { 'age': 1, 'active': true }); _.findKey(users, ['active', false]); _.findKey(users, 'active');

### `_.findLastKey(object, [predicate=_.identity])`

source npm package

This method is like `_.findKey` except that it iterates over elements of a collection in the opposite order.Since

2.0.0Arguments`object` *(Object)*: The object to inspect.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(*)*: Returns the key of the matched element, else `undefined`.Examplevar users = {  'barney':  { 'age': 36, 'active': true },  'fred':    { 'age': 40, 'active': false },  'pebbles': { 'age': 1,  'active': true }}; _.findLastKey(users, function(o) { return o.age < 40; }); _.findLastKey(users, { 'age': 36, 'active': true }); _.findLastKey(users, ['active', false]); _.findLastKey(users, 'active');

### `_.forIn(object, [iteratee=_.identity])`

source npm package

Iterates over own and inherited enumerable string keyed properties of an object and invokes `iteratee` for each property. The iteratee is invoked with three arguments: *(value, key, object)*. Iteratee functions may exit iteration early by explicitly returning `false`.Since

0.3.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Object)*: Returns `object`.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.forIn(new Foo, function(value, key) {  console.log(key);});

### `_.forInRight(object, [iteratee=_.identity])`

source npm package

This method is like `_.forIn` except that it iterates over properties of `object` in the opposite order.Since

2.0.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Object)*: Returns `object`.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.forInRight(new Foo, function(value, key) {  console.log(key);});

### `_.forOwn(object, [iteratee=_.identity])`

source npm package

Iterates over own enumerable string keyed properties of an object and invokes `iteratee` for each property. The iteratee is invoked with three arguments: *(value, key, object)*. Iteratee functions may exit iteration early by explicitly returning `false`.Since

0.3.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Object)*: Returns `object`.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.forOwn(new Foo, function(value, key) {  console.log(key);});

### `_.forOwnRight(object, [iteratee=_.identity])`

source npm package

This method is like `_.forOwn` except that it iterates over properties of `object` in the opposite order.Since

2.0.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Object)*: Returns `object`.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.forOwnRight(new Foo, function(value, key) {  console.log(key);});

### `_.functions(object)`

source npm package

Creates an array of function property names from own enumerable properties of `object`.Since

0.1.0Arguments`object` *(Object)*: The object to inspect.Returns

*(Array)*: Returns the function names.Examplefunction Foo() {  this.a = _.constant('a');  this.b = _.constant('b');} Foo.prototype.c = _.constant('c'); _.functions(new Foo);

### `_.functionsIn(object)`

source npm package

Creates an array of function property names from own and inherited enumerable properties of `object`.Since

4.0.0Arguments`object` *(Object)*: The object to inspect.Returns

*(Array)*: Returns the function names.Examplefunction Foo() {  this.a = _.constant('a');  this.b = _.constant('b');} Foo.prototype.c = _.constant('c'); _.functionsIn(new Foo);

### `_.get(object, path, [defaultValue])`

source npm package

Gets the value at `path` of `object`. If the resolved value is `undefined`, the `defaultValue` is returned in its place.Since

3.7.0Arguments`object` *(Object)*: The object to query.`path` *(Array|string)*: The path of the property to get.`[defaultValue]` *(*)*: The value returned for `undefined` resolved values.Returns

*(*)*: Returns the resolved value.Examplevar object = { 'a': [{ 'b': { 'c': 3 } }] }; _.get(object, 'a[0].b.c'); _.get(object, ['a', '0', 'b', 'c']); _.get(object, 'a.b.c', 'default');

### `_.has(object, path)`

source npm package

Checks if `path` is a direct property of `object`.Since

0.1.0Arguments`object` *(Object)*: The object to query.`path` *(Array|string)*: The path to check.Returns

*(boolean)*: Returns `true` if `path` exists, else `false`.Examplevar object = { 'a': { 'b': 2 } };var other = _.create({ 'a': _.create({ 'b': 2 }) }); _.has(object, 'a'); _.has(object, 'a.b'); _.has(object, ['a', 'b']); _.has(other, 'a');

### `_.hasIn(object, path)`

source npm package

Checks if `path` is a direct or inherited property of `object`.Since

4.0.0Arguments`object` *(Object)*: The object to query.`path` *(Array|string)*: The path to check.Returns

*(boolean)*: Returns `true` if `path` exists, else `false`.Examplevar object = _.create({ 'a': _.create({ 'b': 2 }) }); _.hasIn(object, 'a'); _.hasIn(object, 'a.b'); _.hasIn(object, ['a', 'b']); _.hasIn(object, 'b');

### `_.invert(object)`

source npm package

Creates an object composed of the inverted keys and values of `object`. If `object` contains duplicate values, subsequent values overwrite property assignments of previous values.Since

0.7.0Arguments`object` *(Object)*: The object to invert.Returns

*(Object)*: Returns the new inverted object.Examplevar object = { 'a': 1, 'b': 2, 'c': 1 }; _.invert(object);

### `_.invertBy(object, [iteratee=_.identity])`

source npm package

This method is like `_.invert` except that the inverted object is generated from the results of running each element of `object` thru `iteratee`. The corresponding inverted value of each inverted key is an array of keys responsible for generating the inverted value. The iteratee is invoked with one argument: *(value)*.Since

4.1.0Arguments`object` *(Object)*: The object to invert.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Object)*: Returns the new inverted object.Examplevar object = { 'a': 1, 'b': 2, 'c': 1 }; _.invertBy(object); _.invertBy(object, function(value) {  return 'group' + value;});

### `_.invoke(object, path, [args])`

source npm package

Invokes the method at `path` of `object`.Since

4.0.0Arguments`object` *(Object)*: The object to query.`path` *(Array|string)*: The path of the method to invoke.`[args]` *(...*)*: The arguments to invoke the method with.Returns

*(*)*: Returns the result of the invoked method.Examplevar object = { 'a': [{ 'b': { 'c': [1, 2, 3, 4] } }] }; _.invoke(object, 'a[0].b.c.slice', 1, 3);

### `_.keys(object)`

source npm package

Creates an array of the own enumerable property names of `object`. **Note:** Non-object values are coerced to objects. See the ES spec for more details.Since

0.1.0Arguments`object` *(Object)*: The object to query.Returns

*(Array)*: Returns the array of property names.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.keys(new Foo); _.keys('hi');

### `_.keysIn(object)`

source npm package

Creates an array of the own and inherited enumerable property names of `object`. **Note:** Non-object values are coerced to objects.Since

3.0.0Arguments`object` *(Object)*: The object to query.Returns

*(Array)*: Returns the array of property names.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.keysIn(new Foo);

### `_.mapKeys(object, [iteratee=_.identity])`

source npm package

The opposite of `_.mapValues`; this method creates an object with the same values as `object` and keys generated by running each own enumerable string keyed property of `object` thru `iteratee`. The iteratee is invoked with three arguments: *(value, key, object)*.Since

3.8.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Object)*: Returns the new mapped object.Example_.mapKeys({ 'a': 1, 'b': 2 }, function(value, key) {  return key + value;});

### `_.mapValues(object, [iteratee=_.identity])`

source npm package

Creates an object with the same keys as `object` and values generated by running each own enumerable string keyed property of `object` thru `iteratee`. The iteratee is invoked with three arguments: *(value, key, object)*.Since

2.4.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Object)*: Returns the new mapped object.Examplevar users = {  'fred':    { 'user': 'fred',    'age': 40 },  'pebbles': { 'user': 'pebbles', 'age': 1 }}; _.mapValues(users, function(o) { return o.age; }); _.mapValues(users, 'age');

### `_.merge(object, [sources])`

source npm package

This method is like `_.assign` except that it recursively merges own and inherited enumerable string keyed properties of source objects into the destination object. Source properties that resolve to `undefined` are skipped if a destination value exists. Array and plain object properties are merged recursively. Other objects and value types are overridden by assignment. Source objects are applied from left to right. Subsequent sources overwrite property assignments of previous sources. **Note:** This method mutates `object`.Since

0.5.0Arguments`object` *(Object)*: The destination object.`[sources]` *(...Object)*: The source objects.Returns

*(Object)*: Returns `object`.Examplevar object = {  'a': [{ 'b': 2 }, { 'd': 4 }]}; var other = {  'a': [{ 'c': 3 }, { 'e': 5 }]}; _.merge(object, other);

### `_.mergeWith(object, sources, customizer)`

source npm package

This method is like `_.merge` except that it accepts `customizer` which is invoked to produce the merged values of the destination and source properties. If `customizer` returns `undefined`, merging is handled by the method instead. The `customizer` is invoked with six arguments: *(objValue, srcValue, key, object, source, stack)*. **Note:** This method mutates `object`.Since

4.0.0Arguments`object` *(Object)*: The destination object.`sources` *(...Object)*: The source objects.`customizer` *(Function)*: The function to customize assigned values.Returns

*(Object)*: Returns `object`.Examplefunction customizer(objValue, srcValue) {  if (_.isArray(objValue)) {    return objValue.concat(srcValue);  }} var object = { 'a': [1], 'b': [2] };var other = { 'a': [3], 'b': [4] }; _.mergeWith(object, other, customizer);

### `_.omit(object, [paths])`

source npm package

The opposite of `_.pick`; this method creates an object composed of the own and inherited enumerable property paths of `object` that are not omitted. **Note:** This method is considerably slower than `_.pick`.Since

0.1.0Arguments`object` *(Object)*: The source object.`[paths]` *(...(string|string[]))*: The property paths to omit.Returns

*(Object)*: Returns the new object.Examplevar object = { 'a': 1, 'b': '2', 'c': 3 }; _.omit(object, ['a', 'c']);

### `_.omitBy(object, [predicate=_.identity])`

source npm package

The opposite of `_.pickBy`; this method creates an object composed of the own and inherited enumerable string keyed properties of `object` that `predicate` doesn't return truthy for. The predicate is invoked with two arguments: *(value, key)*.Since

4.0.0Arguments`object` *(Object)*: The source object.`[predicate=_.identity]` *(Function)*: The function invoked per property.Returns

*(Object)*: Returns the new object.Examplevar object = { 'a': 1, 'b': '2', 'c': 3 }; _.omitBy(object, _.isNumber);

### `_.pick(object, [paths])`

source npm package

Creates an object composed of the picked `object` properties.Since

0.1.0Arguments`object` *(Object)*: The source object.`[paths]` *(...(string|string[]))*: The property paths to pick.Returns

*(Object)*: Returns the new object.Examplevar object = { 'a': 1, 'b': '2', 'c': 3 }; _.pick(object, ['a', 'c']);

### `_.pickBy(object, [predicate=_.identity])`

source npm package

Creates an object composed of the `object` properties `predicate` returns truthy for. The predicate is invoked with two arguments: *(value, key)*.Since

4.0.0Arguments`object` *(Object)*: The source object.`[predicate=_.identity]` *(Function)*: The function invoked per property.Returns

*(Object)*: Returns the new object.Examplevar object = { 'a': 1, 'b': '2', 'c': 3 }; _.pickBy(object, _.isNumber);

### `_.result(object, path, [defaultValue])`

source npm package

This method is like `_.get` except that if the resolved value is a function it's invoked with the `this` binding of its parent object and its result is returned.Since

0.1.0Arguments`object` *(Object)*: The object to query.`path` *(Array|string)*: The path of the property to resolve.`[defaultValue]` *(*)*: The value returned for `undefined` resolved values.Returns

*(*)*: Returns the resolved value.Examplevar object = { 'a': [{ 'b': { 'c1': 3, 'c2': _.constant(4) } }] }; _.result(object, 'a[0].b.c1'); _.result(object, 'a[0].b.c2'); _.result(object, 'a[0].b.c3', 'default'); _.result(object, 'a[0].b.c3', _.constant('default'));

### `_.set(object, path, value)`

source npm package

Sets the value at `path` of `object`. If a portion of `path` doesn't exist, it's created. Arrays are created for missing index properties while objects are created for all other missing properties. Use `_.setWith` to customize `path` creation. **Note:** This method mutates `object`.Since

3.7.0Arguments`object` *(Object)*: The object to modify.`path` *(Array|string)*: The path of the property to set.`value` *(*)*: The value to set.Returns

*(Object)*: Returns `object`.Examplevar object = { 'a': [{ 'b': { 'c': 3 } }] }; _.set(object, 'a[0].b.c', 4);console.log(object.a[0].b.c); _.set(object, ['x', '0', 'y', 'z'], 5);console.log(object.x[0].y.z);

### `_.setWith(object, path, value, [customizer])`

source npm package

This method is like `_.set` except that it accepts `customizer` which is invoked to produce the objects of `path`. If `customizer` returns `undefined` path creation is handled by the method instead. The `customizer` is invoked with three arguments: *(nsValue, key, nsObject)*. **Note:** This method mutates `object`.Since

4.0.0Arguments`object` *(Object)*: The object to modify.`path` *(Array|string)*: The path of the property to set.`value` *(*)*: The value to set.`[customizer]` *(Function)*: The function to customize assigned values.Returns

*(Object)*: Returns `object`.Examplevar object = {}; _.setWith(object, '[0][1]', 'a', Object);

### `_.toPairs(object)`

source npm package

Creates an array of own enumerable string keyed-value pairs for `object` which can be consumed by `_.fromPairs`. If `object` is a map or set, its entries are returned.Since

4.0.0Aliases

*_.entries*Arguments`object` *(Object)*: The object to query.Returns

*(Array)*: Returns the key-value pairs.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.toPairs(new Foo);

### `_.toPairsIn(object)`

source npm package

Creates an array of own and inherited enumerable string keyed-value pairs for `object` which can be consumed by `_.fromPairs`. If `object` is a map or set, its entries are returned.Since

4.0.0Aliases

*_.entriesIn*Arguments`object` *(Object)*: The object to query.Returns

*(Array)*: Returns the key-value pairs.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.toPairsIn(new Foo);

### `_.transform(object, [iteratee=_.identity], [accumulator])`

source npm package

An alternative to `_.reduce`; this method transforms `object` to a new `accumulator` object which is the result of running each of its own enumerable string keyed properties thru `iteratee`, with each invocation potentially mutating the `accumulator` object. If `accumulator` is not provided, a new object with the same `[[Prototype]]` will be used. The iteratee is invoked with four arguments: *(accumulator, value, key, object)*. Iteratee functions may exit iteration early by explicitly returning `false`.Since

1.3.0Arguments`object` *(Object)*: The object to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.`[accumulator]` *(*)*: The custom accumulator value.Returns

*(*)*: Returns the accumulated value.Example_.transform([2, 3, 4], function(result, n) {  result.push(n *= n);  return n % 2 == 0;}, []); _.transform({ 'a': 1, 'b': 2, 'c': 1 }, function(result, value, key) {  (result[value] || (result[value] = [])).push(key);}, {});

### `_.unset(object, path)`

source npm package

Removes the property at `path` of `object`. **Note:** This method mutates `object`.Since

4.0.0Arguments`object` *(Object)*: The object to modify.`path` *(Array|string)*: The path of the property to unset.Returns

*(boolean)*: Returns `true` if the property is deleted, else `false`.Examplevar object = { 'a': [{ 'b': { 'c': 7 } }] };_.unset(object, 'a[0].b.c'); console.log(object); _.unset(object, ['a', '0', 'b', 'c']); console.log(object);

### `_.update(object, path, updater)`

source npm package

This method is like `_.set` except that accepts `updater` to produce the value to set. Use `_.updateWith` to customize `path` creation. The `updater` is invoked with one argument: *(value)*. **Note:** This method mutates `object`.Since

4.6.0Arguments`object` *(Object)*: The object to modify.`path` *(Array|string)*: The path of the property to set.`updater` *(Function)*: The function to produce the updated value.Returns

*(Object)*: Returns `object`.Examplevar object = { 'a': [{ 'b': { 'c': 3 } }] }; _.update(object, 'a[0].b.c', function(n) { return n * n; });console.log(object.a[0].b.c); _.update(object, 'x[0].y.z', function(n) { return n ? n + 1 : 0; });console.log(object.x[0].y.z);

### `_.updateWith(object, path, updater, [customizer])`

source npm package

This method is like `_.update` except that it accepts `customizer` which is invoked to produce the objects of `path`. If `customizer` returns `undefined` path creation is handled by the method instead. The `customizer` is invoked with three arguments: *(nsValue, key, nsObject)*. **Note:** This method mutates `object`.Since

4.6.0Arguments`object` *(Object)*: The object to modify.`path` *(Array|string)*: The path of the property to set.`updater` *(Function)*: The function to produce the updated value.`[customizer]` *(Function)*: The function to customize assigned values.Returns

*(Object)*: Returns `object`.Examplevar object = {}; _.updateWith(object, '[0][1]', _.constant('a'), Object);

### `_.values(object)`

source npm package

Creates an array of the own enumerable string keyed property values of `object`. **Note:** Non-object values are coerced to objects.Since

0.1.0Arguments`object` *(Object)*: The object to query.Returns

*(Array)*: Returns the array of property values.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.values(new Foo); _.values('hi');

### `_.valuesIn(object)`

source npm package

Creates an array of the own and inherited enumerable string keyed property values of `object`. **Note:** Non-object values are coerced to objects.Since

3.0.0Arguments`object` *(Object)*: The object to query.Returns

*(Array)*: Returns the array of property values.Examplefunction Foo() {  this.a = 1;  this.b = 2;} Foo.prototype.c = 3; _.valuesIn(new Foo);


## `“Seq” Methods`

### `_(value)`

source

Creates a `lodash` object which wraps `value` to enable implicit method chain sequences. Methods that operate on and return arrays, collections, and functions can be chained together. Methods that retrieve a single value or may return a primitive value will automatically end the chain sequence and return the unwrapped value. Otherwise, the value must be unwrapped with `_#value`. Explicit chain sequences, which must be unwrapped with `_#value`, may be enabled using `_.chain`. The execution of chained methods is lazy, that is, it's deferred until `_#value` is implicitly or explicitly called. Lazy evaluation allows several methods to support shortcut fusion. Shortcut fusion is an optimization to merge iteratee calls; this avoids the creation of intermediate arrays and can greatly reduce the number of iteratee executions. Sections of a chain sequence qualify for shortcut fusion if the section is applied to an array and iteratees accept only one argument. The heuristic for whether a section qualifies for shortcut fusion is subject to change. Chaining is supported in custom builds as long as the `_#value` method is directly or indirectly included in the build. In addition to lodash methods, wrappers have `Array` and `String` methods. The wrapper `Array` methods are: `concat`, `join`, `pop`, `push`, `shift`, `sort`, `splice`, and `unshift` The wrapper `String` methods are: `replace` and `split` The wrapper methods that support shortcut fusion are: `at`, `compact`, `drop`, `dropRight`, `dropWhile`, `filter`, `find`, `findLast`, `head`, `initial`, `last`, `map`, `reject`, `reverse`, `slice`, `tail`, `take`, `takeRight`, `takeRightWhile`, `takeWhile`, and `toArray` The chainable wrapper methods are: `after`, `ary`, `assign`, `assignIn`, `assignInWith`, `assignWith`, `at`, `before`, `bind`, `bindAll`, `bindKey`, `castArray`, `chain`, `chunk`, `commit`, `compact`, `concat`, `conforms`, `constant`, `countBy`, `create`, `curry`, `debounce`, `defaults`, `defaultsDeep`, `defer`, `delay`, `difference`, `differenceBy`, `differenceWith`, `drop`, `dropRight`, `dropRightWhile`, `dropWhile`, `extend`, `extendWith`, `fill`, `filter`, `flatMap`, `flatMapDeep`, `flatMapDepth`, `flatten`, `flattenDeep`, `flattenDepth`, `flip`, `flow`, `flowRight`, `fromPairs`, `functions`, `functionsIn`, `groupBy`, `initial`, `intersection`, `intersectionBy`, `intersectionWith`, `invert`, `invertBy`, `invokeMap`, `iteratee`, `keyBy`, `keys`, `keysIn`, `map`, `mapKeys`, `mapValues`, `matches`, `matchesProperty`, `memoize`, `merge`, `mergeWith`, `method`, `methodOf`, `mixin`, `negate`, `nthArg`, `omit`, `omitBy`, `once`, `orderBy`, `over`, `overArgs`, `overEvery`, `overSome`, `partial`, `partialRight`, `partition`, `pick`, `pickBy`, `plant`, `property`, `propertyOf`, `pull`, `pullAll`, `pullAllBy`, `pullAllWith`, `pullAt`, `push`, `range`, `rangeRight`, `rearg`, `reject`, `remove`, `rest`, `reverse`, `sampleSize`, `set`, `setWith`, `shuffle`, `slice`, `sort`, `sortBy`, `splice`, `spread`, `tail`, `take`, `takeRight`, `takeRightWhile`, `takeWhile`, `tap`, `throttle`, `thru`, `toArray`, `toPairs`, `toPairsIn`, `toPath`, `toPlainObject`, `transform`, `unary`, `union`, `unionBy`, `unionWith`, `uniq`, `uniqBy`, `uniqWith`, `unset`, `unshift`, `unzip`, `unzipWith`, `update`, `updateWith`, `values`, `valuesIn`, `without`, `wrap`, `xor`, `xorBy`, `xorWith`, `zip`, `zipObject`, `zipObjectDeep`, and `zipWith` The wrapper methods that are **not** chainable by default are: `add`, `attempt`, `camelCase`, `capitalize`, `ceil`, `clamp`, `clone`, `cloneDeep`, `cloneDeepWith`, `cloneWith`, `conformsTo`, `deburr`, `defaultTo`, `divide`, `each`, `eachRight`, `endsWith`, `eq`, `escape`, `escapeRegExp`, `every`, `find`, `findIndex`, `findKey`, `findLast`, `findLastIndex`, `findLastKey`, `first`, `floor`, `forEach`, `forEachRight`, `forIn`, `forInRight`, `forOwn`, `forOwnRight`, `get`, `gt`, `gte`, `has`, `hasIn`, `head`, `identity`, `includes`, `indexOf`, `inRange`, `invoke`, `isArguments`, `isArray`, `isArrayBuffer`, `isArrayLike`, `isArrayLikeObject`, `isBoolean`, `isBuffer`, `isDate`, `isElement`, `isEmpty`, `isEqual`, `isEqualWith`, `isError`, `isFinite`, `isFunction`, `isInteger`, `isLength`, `isMap`, `isMatch`, `isMatchWith`, `isNaN`, `isNative`, `isNil`, `isNull`, `isNumber`, `isObject`, `isObjectLike`, `isPlainObject`, `isRegExp`, `isSafeInteger`, `isSet`, `isString`, `isUndefined`, `isTypedArray`, `isWeakMap`, `isWeakSet`, `join`, `kebabCase`, `last`, `lastIndexOf`, `lowerCase`, `lowerFirst`, `lt`, `lte`, `max`, `maxBy`, `mean`, `meanBy`, `min`, `minBy`, `multiply`, `noConflict`, `noop`, `now`, `nth`, `pad`, `padEnd`, `padStart`, `parseInt`, `pop`, `random`, `reduce`, `reduceRight`, `repeat`, `result`, `round`, `runInContext`, `sample`, `shift`, `size`, `snakeCase`, `some`, `sortedIndex`, `sortedIndexBy`, `sortedLastIndex`, `sortedLastIndexBy`, `startCase`, `startsWith`, `stubArray`, `stubFalse`, `stubObject`, `stubString`, `stubTrue`, `subtract`, `sum`, `sumBy`, `template`, `times`, `toFinite`, `toInteger`, `toJSON`, `toLength`, `toLower`, `toNumber`, `toSafeInteger`, `toString`, `toUpper`, `trim`, `trimEnd`, `trimStart`, `truncate`, `unescape`, `uniqueId`, `upperCase`, `upperFirst`, `value`, and `words`Arguments`value` *(*)*: The value to wrap in a `lodash` instance.Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplefunction square(n) {  return n * n;} var wrapped = _([1, 2, 3]); wrapped.reduce(_.add); var squares = wrapped.map(square); _.isArray(squares); _.isArray(squares.value());

### `_.chain(value)`

source

Creates a `lodash` wrapper instance that wraps `value` with explicit method chain sequences enabled. The result of such sequences must be unwrapped with `_#value`.Since

1.3.0Arguments`value` *(*)*: The value to wrap.Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplevar users = [  { 'user': 'barney',  'age': 36 },  { 'user': 'fred',    'age': 40 },  { 'user': 'pebbles', 'age': 1 }]; var youngest = _  .chain(users)  .sortBy('age')  .map(function(o) {    return o.user + ' is ' + o.age;  })  .head()  .value();

### `_.tap(value, interceptor)`

source

This method invokes `interceptor` and returns `value`. The interceptor is invoked with one argument; *(value)*. The purpose of this method is to "tap into" a method chain sequence in order to modify intermediate results.Since

0.1.0Arguments`value` *(*)*: The value to provide to `interceptor`.`interceptor` *(Function)*: The function to invoke.Returns

*(*)*: Returns `value`.Example_([1, 2, 3]) .tap(function(array) {   array.pop(); }) .reverse() .value();

### `_.thru(value, interceptor)`

source

This method is like `_.tap` except that it returns the result of `interceptor`. The purpose of this method is to "pass thru" values replacing intermediate results in a method chain sequence.Since

3.0.0Arguments`value` *(*)*: The value to provide to `interceptor`.`interceptor` *(Function)*: The function to invoke.Returns

*(*)*: Returns the result of `interceptor`.Example_('  abc  ') .chain() .trim() .thru(function(value) {   return [value]; }) .value();

### `_.prototype[Symbol.iterator]()`

source

Enables the wrapper to be iterable.Since

4.0.0Returns

*(Object)*: Returns the wrapper object.Examplevar wrapped = _([1, 2]); wrapped[Symbol.iterator]() === wrapped; Array.from(wrapped);

### `_.prototype.at([paths])`

source

This method is the wrapper version of `_.at`.Since

1.0.0Arguments`[paths]` *(...(string|string[]))*: The property paths to pick.Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplevar object = { 'a': [{ 'b': { 'c': 3 } }, 4] }; _(object).at(['a[0].b.c', 'a[1]']).value();

### `_.prototype.chain()`

source

Creates a `lodash` wrapper instance with explicit method chain sequences enabled.Since

0.1.0Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplevar users = [  { 'user': 'barney', 'age': 36 },  { 'user': 'fred',   'age': 40 }]; _(users).head(); _(users)  .chain()  .head()  .pick('user')  .value();

### `_.prototype.commit()`

source

Executes the chain sequence and returns the wrapped result.Since

3.2.0Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplevar array = [1, 2];var wrapped = _(array).push(3); console.log(array); wrapped = wrapped.commit();console.log(array); wrapped.last(); console.log(array);

### `_.prototype.next()`

source

Gets the next value on a wrapped object following the iterator protocol.Since

4.0.0Returns

*(Object)*: Returns the next iterator value.Examplevar wrapped = _([1, 2]); wrapped.next(); wrapped.next(); wrapped.next();

### `_.prototype.plant(value)`

source

Creates a clone of the chain sequence planting `value` as the wrapped value.Since

3.2.0Arguments`value` *(*)*: The value to plant.Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplefunction square(n) {  return n * n;} var wrapped = _([1, 2]).map(square);var other = wrapped.plant([3, 4]); other.value(); wrapped.value();

### `_.prototype.reverse()`

source

This method is the wrapper version of `_.reverse`. **Note:** This method mutates the wrapped array.Since

0.1.0Returns

*(Object)*: Returns the new `lodash` wrapper instance.Examplevar array = [1, 2, 3]; _(array).reverse().value() console.log(array);

### `_.prototype.value()`

source

Executes the chain sequence to resolve the unwrapped value.Since

0.1.0Aliases

*_.prototype.toJSON, _.prototype.valueOf*Returns

*(*)*: Returns the resolved unwrapped value.Example_([1, 2, 3]).value();
