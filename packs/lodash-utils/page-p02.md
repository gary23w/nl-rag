---
title: "Lodash Documentation (part 2/5)"
source: https://lodash.com/docs/
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
part: 2/5
---

## `“Collection” Methods`

### `_.countBy(collection, [iteratee=_.identity])`

source npm package

Creates an object composed of keys generated from the results of running each element of `collection` thru `iteratee`. The corresponding value of each key is the number of times the key was returned by `iteratee`. The iteratee is invoked with one argument: *(value)*.Since

0.5.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee to transform keys.Returns

*(Object)*: Returns the composed aggregate object.Example_.countBy([6.1, 4.2, 6.3], Math.floor); _.countBy(['one', 'two', 'three'], 'length');

### `_.every(collection, [predicate=_.identity])`

source npm package

Checks if `predicate` returns truthy for **all** elements of `collection`. Iteration is stopped once `predicate` returns falsey. The predicate is invoked with three arguments: *(value, index|key, collection)*. **Note:** This method returns `true` for empty collections because everything is true of elements of empty collections.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(boolean)*: Returns `true` if all elements pass the predicate check, else `false`.Example_.every([true, 1, null, 'yes'], Boolean); var users = [  { 'user': 'barney', 'age': 36, 'active': false },  { 'user': 'fred',   'age': 40, 'active': false }]; _.every(users, { 'user': 'barney', 'active': false }); _.every(users, ['active', false]); _.every(users, 'active');

### `_.filter(collection, [predicate=_.identity])`

source npm package

Iterates over elements of `collection`, returning an array of all elements `predicate` returns truthy for. The predicate is invoked with three arguments: *(value, index|key, collection)*. **Note:** Unlike `_.remove`, this method returns a new array.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the new filtered array.Examplevar users = [  { 'user': 'barney', 'age': 36, 'active': true },  { 'user': 'fred',   'age': 40, 'active': false }]; _.filter(users, function(o) { return !o.active; }); _.filter(users, { 'age': 36, 'active': true }); _.filter(users, ['active', false]); _.filter(users, 'active'); _.filter(users, _.overSome([{ 'age': 36 }, ['age', 40]]));

### `_.find(collection, [predicate=_.identity], [fromIndex=0])`

source npm package

Iterates over elements of `collection`, returning the first element `predicate` returns truthy for. The predicate is invoked with three arguments: *(value, index|key, collection)*.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to inspect.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.`[fromIndex=0]` *(number)*: The index to search from.Returns

*(*)*: Returns the matched element, else `undefined`.Examplevar users = [  { 'user': 'barney',  'age': 36, 'active': true },  { 'user': 'fred',    'age': 40, 'active': false },  { 'user': 'pebbles', 'age': 1,  'active': true }]; _.find(users, function(o) { return o.age < 40; }); _.find(users, { 'age': 1, 'active': true }); _.find(users, ['active', false]); _.find(users, 'active');

### `_.findLast(collection, [predicate=_.identity], [fromIndex=collection.length-1])`

source npm package

This method is like `_.find` except that it iterates over elements of `collection` from right to left.Since

2.0.0Arguments`collection` *(Array|Object)*: The collection to inspect.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.`[fromIndex=collection.length-1]` *(number)*: The index to search from.Returns

*(*)*: Returns the matched element, else `undefined`.Example_.findLast([1, 2, 3, 4], function(n) {  return n % 2 == 1;});

### `_.flatMap(collection, [iteratee=_.identity])`

source npm package

Creates a flattened array of values by running each element in `collection` thru `iteratee` and flattening the mapped results. The iteratee is invoked with three arguments: *(value, index|key, collection)*.Since

4.0.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the new flattened array.Examplefunction duplicate(n) {  return [n, n];} _.flatMap([1, 2], duplicate);

### `_.flatMapDeep(collection, [iteratee=_.identity])`

source npm package

This method is like `_.flatMap` except that it recursively flattens the mapped results.Since

4.7.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the new flattened array.Examplefunction duplicate(n) {  return [[[n, n]]];} _.flatMapDeep([1, 2], duplicate);

### `_.flatMapDepth(collection, [iteratee=_.identity], [depth=1])`

source npm package

This method is like `_.flatMap` except that it recursively flattens the mapped results up to `depth` times.Since

4.7.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.`[depth=1]` *(number)*: The maximum recursion depth.Returns

*(Array)*: Returns the new flattened array.Examplefunction duplicate(n) {  return [[[n, n]]];} _.flatMapDepth([1, 2], duplicate, 2);

### `_.forEach(collection, [iteratee=_.identity])`

source npm package

Iterates over elements of `collection` and invokes `iteratee` for each element. The iteratee is invoked with three arguments: *(value, index|key, collection)*. Iteratee functions may exit iteration early by explicitly returning `false`. **Note:** As with other "Collections" methods, objects with a "length" property are iterated like arrays. To avoid this behavior use `_.forIn` or `_.forOwn` for object iteration.Since

0.1.0Aliases

*_.each*Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(*)*: Returns `collection`.Example_.forEach([1, 2], function(value) {  console.log(value);}); _.forEach({ 'a': 1, 'b': 2 }, function(value, key) {  console.log(key);});

### `_.forEachRight(collection, [iteratee=_.identity])`

source npm package

This method is like `_.forEach` except that it iterates over elements of `collection` from right to left.Since

2.0.0Aliases

*_.eachRight*Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(*)*: Returns `collection`.Example_.forEachRight([1, 2], function(value) {  console.log(value);});

### `_.groupBy(collection, [iteratee=_.identity])`

source npm package

Creates an object composed of keys generated from the results of running each element of `collection` thru `iteratee`. The order of grouped values is determined by the order they occur in `collection`. The corresponding value of each key is an array of elements responsible for generating the key. The iteratee is invoked with one argument: *(value)*.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee to transform keys.Returns

*(Object)*: Returns the composed aggregate object.Example_.groupBy([6.1, 4.2, 6.3], Math.floor); _.groupBy(['one', 'two', 'three'], 'length');

### `_.includes(collection, value, [fromIndex=0])`

source npm package

Checks if `value` is in `collection`. If `collection` is a string, it's checked for a substring of `value`, otherwise `SameValueZero` is used for equality comparisons. If `fromIndex` is negative, it's used as the offset from the end of `collection`.Since

0.1.0Arguments`collection` *(Array|Object|string)*: The collection to inspect.`value` *(*)*: The value to search for.`[fromIndex=0]` *(number)*: The index to search from.Returns

*(boolean)*: Returns `true` if `value` is found, else `false`.Example_.includes([1, 2, 3], 1); _.includes([1, 2, 3], 1, 2); _.includes({ 'a': 1, 'b': 2 }, 1); _.includes('abcd', 'bc');

### `_.invokeMap(collection, path, [args])`

source npm package

Invokes the method at `path` of each element in `collection`, returning an array of the results of each invoked method. Any additional arguments are provided to each invoked method. If `path` is a function, it's invoked for, and `this` bound to, each element in `collection`.Since

4.0.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`path` *(Array|Function|string)*: The path of the method to invoke or the function invoked per iteration.`[args]` *(...*)*: The arguments to invoke each method with.Returns

*(Array)*: Returns the array of results.Example_.invokeMap([[5, 1, 7], [3, 2, 1]], 'sort'); _.invokeMap([123, 456], String.prototype.split, '');

### `_.keyBy(collection, [iteratee=_.identity])`

source npm package

Creates an object composed of keys generated from the results of running each element of `collection` thru `iteratee`. The corresponding value of each key is the last element responsible for generating the key. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The iteratee to transform keys.Returns

*(Object)*: Returns the composed aggregate object.Examplevar array = [  { 'dir': 'left', 'code': 97 },  { 'dir': 'right', 'code': 100 }]; _.keyBy(array, function(o) {  return String.fromCharCode(o.code);}); _.keyBy(array, 'dir');

### `_.map(collection, [iteratee=_.identity])`

source npm package

Creates an array of values by running each element in `collection` thru `iteratee`. The iteratee is invoked with three arguments: *(value, index|key, collection)*. Many lodash methods are guarded to work as iteratees for methods like `_.every`, `_.filter`, `_.map`, `_.mapValues`, `_.reject`, and `_.some`. The guarded methods are: `ary`, `chunk`, `curry`, `curryRight`, `drop`, `dropRight`, `every`, `fill`, `invert`, `parseInt`, `random`, `range`, `rangeRight`, `repeat`, `sampleSize`, `slice`, `some`, `sortBy`, `split`, `take`, `takeRight`, `template`, `trim`, `trimEnd`, `trimStart`, and `words`Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the new mapped array.Examplefunction square(n) {  return n * n;} _.map([4, 8], square); _.map({ 'a': 4, 'b': 8 }, square); var users = [  { 'user': 'barney' },  { 'user': 'fred' }]; _.map(users, 'user');

### `_.orderBy(collection, [iteratees=[_.identity]], [orders])`

source npm package

This method is like `_.sortBy` except that it allows specifying the sort orders of the iteratees to sort by. If `orders` is unspecified, all values are sorted in ascending order. Otherwise, specify an order of "desc" for descending or "asc" for ascending sort order of corresponding values.Since

4.0.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratees=[_.identity]]` *(Array[]|Function[]|Object[]|string[])*: The iteratees to sort by.`[orders]` *(string[])*: The sort orders of `iteratees`.Returns

*(Array)*: Returns the new sorted array.Examplevar users = [  { 'user': 'fred',   'age': 48 },  { 'user': 'barney', 'age': 34 },  { 'user': 'fred',   'age': 40 },  { 'user': 'barney', 'age': 36 }]; _.orderBy(users, ['user', 'age'], ['asc', 'desc']);

### `_.partition(collection, [predicate=_.identity])`

source npm package

Creates an array of elements split into two groups, the first of which contains elements `predicate` returns truthy for, the second of which contains elements `predicate` returns falsey for. The predicate is invoked with one argument: *(value)*.Since

3.0.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the array of grouped elements.Examplevar users = [  { 'user': 'barney',  'age': 36, 'active': false },  { 'user': 'fred',    'age': 40, 'active': true },  { 'user': 'pebbles', 'age': 1,  'active': false }]; _.partition(users, function(o) { return o.active; }); _.partition(users, { 'age': 1, 'active': false }); _.partition(users, ['active', false]); _.partition(users, 'active');

### `_.reduce(collection, [iteratee=_.identity], [accumulator])`

source npm package

Reduces `collection` to a value which is the accumulated result of running each element in `collection` thru `iteratee`, where each successive invocation is supplied the return value of the previous. If `accumulator` is not given, the first element of `collection` is used as the initial value. The iteratee is invoked with four arguments: *(accumulator, value, index|key, collection)*. Many lodash methods are guarded to work as iteratees for methods like `_.reduce`, `_.reduceRight`, and `_.transform`. The guarded methods are: `assign`, `defaults`, `defaultsDeep`, `includes`, `merge`, `orderBy`, and `sortBy`Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.`[accumulator]` *(*)*: The initial value.Returns

*(*)*: Returns the accumulated value.Example_.reduce([1, 2], function(sum, n) {  return sum + n;}, 0); _.reduce({ 'a': 1, 'b': 2, 'c': 1 }, function(result, value, key) {  (result[value] || (result[value] = [])).push(key);  return result;}, {});

### `_.reduceRight(collection, [iteratee=_.identity], [accumulator])`

source npm package

This method is like `_.reduce` except that it iterates over elements of `collection` from right to left.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.`[accumulator]` *(*)*: The initial value.Returns

*(*)*: Returns the accumulated value.Examplevar array = [[0, 1], [2, 3], [4, 5]]; _.reduceRight(array, function(flattened, other) {  return flattened.concat(other);}, []);

### `_.reject(collection, [predicate=_.identity])`

source npm package

The opposite of `_.filter`; this method returns the elements of `collection` that `predicate` does **not** return truthy for.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the new filtered array.Examplevar users = [  { 'user': 'barney', 'age': 36, 'active': false },  { 'user': 'fred',   'age': 40, 'active': true }]; _.reject(users, function(o) { return !o.active; }); _.reject(users, { 'age': 40, 'active': true }); _.reject(users, ['active', false]); _.reject(users, 'active');

### `_.sample(collection)`

source npm package

Gets a random element from `collection`.Since

2.0.0Arguments`collection` *(Array|Object)*: The collection to sample.Returns

*(*)*: Returns the random element.Example_.sample([1, 2, 3, 4]);

### `_.sampleSize(collection, [n=1])`

source npm package

Gets `n` random elements at unique keys from `collection` up to the size of `collection`.Since

4.0.0Arguments`collection` *(Array|Object)*: The collection to sample.`[n=1]` *(number)*: The number of elements to sample.Returns

*(Array)*: Returns the random elements.Example_.sampleSize([1, 2, 3], 2); _.sampleSize([1, 2, 3], 4);

### `_.shuffle(collection)`

source npm package

Creates an array of shuffled values, using a version of the Fisher-Yates shuffle.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to shuffle.Returns

*(Array)*: Returns the new shuffled array.Example_.shuffle([1, 2, 3, 4]);

### `_.size(collection)`

source npm package

Gets the size of `collection` by returning its length for array-like values or the number of own enumerable string keyed properties for objects.Since

0.1.0Arguments`collection` *(Array|Object|string)*: The collection to inspect.Returns

*(number)*: Returns the collection size.Example_.size([1, 2, 3]); _.size({ 'a': 1, 'b': 2 }); _.size('pebbles');

### `_.some(collection, [predicate=_.identity])`

source npm package

Checks if `predicate` returns truthy for **any** element of `collection`. Iteration is stopped once `predicate` returns truthy. The predicate is invoked with three arguments: *(value, index|key, collection)*.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(boolean)*: Returns `true` if any element passes the predicate check, else `false`.Example_.some([null, 0, 'yes', false], Boolean); var users = [  { 'user': 'barney', 'active': true },  { 'user': 'fred',   'active': false }]; _.some(users, { 'user': 'barney', 'active': false }); _.some(users, ['active', false]); _.some(users, 'active');

### `_.sortBy(collection, [iteratees=[_.identity]])`

source npm package

Creates an array of elements, sorted in ascending order by the results of running each element in a collection thru each iteratee. This method performs a stable sort, that is, it preserves the original sort order of equal elements. The iteratees are invoked with one argument: *(value)*.Since

0.1.0Arguments`collection` *(Array|Object)*: The collection to iterate over.`[iteratees=[_.identity]]` *(...(Function|Function[]))*: The iteratees to sort by.Returns

*(Array)*: Returns the new sorted array.Examplevar users = [  { 'user': 'fred',   'age': 48 },  { 'user': 'barney', 'age': 36 },  { 'user': 'fred',   'age': 30 },  { 'user': 'barney', 'age': 34 }]; _.sortBy(users, [function(o) { return o.user; }]); _.sortBy(users, ['user', 'age']);


## `“Date” Methods`

### `_.now()`

source npm package

Gets the timestamp of the number of milliseconds that have elapsed since the Unix epoch *(1 January `1970 00`:00:00 UTC)*.Since

2.4.0Returns

*(number)*: Returns the timestamp.Example_.defer(function(stamp) {  console.log(_.now() - stamp);}, _.now());


## `“Function” Methods`

### `_.after(n, func)`

source npm package

The opposite of `_.before`; this method creates a function that invokes `func` once it's called `n` or more times.Since

0.1.0Arguments`n` *(number)*: The number of calls before `func` is invoked.`func` *(Function)*: The function to restrict.Returns

*(Function)*: Returns the new restricted function.Examplevar saves = ['profile', 'settings']; var done = _.after(saves.length, function() {  console.log('done saving!');}); _.forEach(saves, function(type) {  asyncSave({ 'type': type, 'complete': done });});

### `_.ary(func, [n=func.length])`

source npm package

Creates a function that invokes `func`, with up to `n` arguments, ignoring any additional arguments.Since

3.0.0Arguments`func` *(Function)*: The function to cap arguments for.`[n=func.length]` *(number)*: The arity cap.Returns

*(Function)*: Returns the new capped function.Example_.map(['6', '8', '10'], _.ary(parseInt, 1));

### `_.before(n, func)`

source npm package

Creates a function that invokes `func`, with the `this` binding and arguments of the created function, while it's called less than `n` times. Subsequent calls to the created function return the result of the last `func` invocation.Since

3.0.0Arguments`n` *(number)*: The number of calls at which `func` is no longer invoked.`func` *(Function)*: The function to restrict.Returns

*(Function)*: Returns the new restricted function.ExamplejQuery(element).on('click', _.before(5, addContactToList));

### `_.bind(func, thisArg, [partials])`

source npm package

Creates a function that invokes `func` with the `this` binding of `thisArg` and `partials` prepended to the arguments it receives. The `_.bind.placeholder` value, which defaults to `_` in monolithic builds, may be used as a placeholder for partially applied arguments. **Note:** Unlike native `Function#bind`, this method doesn't set the "length" property of bound functions.Since

0.1.0Arguments`func` *(Function)*: The function to bind.`thisArg` *(*)*: The `this` binding of `func`.`[partials]` *(...*)*: The arguments to be partially applied.Returns

*(Function)*: Returns the new bound function.Examplefunction greet(greeting, punctuation) {  return greeting + ' ' + this.user + punctuation;} var object = { 'user': 'fred' }; var bound = _.bind(greet, object, 'hi');bound('!'); var bound = _.bind(greet, object, _, '!');bound('hi');

### `_.bindKey(object, key, [partials])`

source npm package

Creates a function that invokes the method at `object[key]` with `partials` prepended to the arguments it receives. This method differs from `_.bind` by allowing bound functions to reference methods that may be redefined or don't yet exist. See Peter Michaux's article for more details. The `_.bindKey.placeholder` value, which defaults to `_` in monolithic builds, may be used as a placeholder for partially applied arguments.Since

0.10.0Arguments`object` *(Object)*: The object to invoke the method on.`key` *(string)*: The key of the method.`[partials]` *(...*)*: The arguments to be partially applied.Returns

*(Function)*: Returns the new bound function.Examplevar object = {  'user': 'fred',  'greet': function(greeting, punctuation) {    return greeting + ' ' + this.user + punctuation;  }}; var bound = _.bindKey(object, 'greet', 'hi');bound('!'); object.greet = function(greeting, punctuation) {  return greeting + 'ya ' + this.user + punctuation;}; bound('!'); var bound = _.bindKey(object, 'greet', _, '!');bound('hi');

### `_.curry(func, [arity=func.length])`

source npm package

Creates a function that accepts arguments of `func` and either invokes `func` returning its result, if at least `arity` number of arguments have been provided, or returns a function that accepts the remaining `func` arguments, and so on. The arity of `func` may be specified if `func.length` is not sufficient. The `_.curry.placeholder` value, which defaults to `_` in monolithic builds, may be used as a placeholder for provided arguments. **Note:** This method doesn't set the "length" property of curried functions.Since

2.0.0Arguments`func` *(Function)*: The function to curry.`[arity=func.length]` *(number)*: The arity of `func`.Returns

*(Function)*: Returns the new curried function.Examplevar abc = function(a, b, c) {  return [a, b, c];}; var curried = _.curry(abc); curried(1)(2)(3); curried(1, 2)(3); curried(1, 2, 3); curried(1)(_, 3)(2);

### `_.curryRight(func, [arity=func.length])`

source npm package

This method is like `_.curry` except that arguments are applied to `func` in the manner of `_.partialRight` instead of `_.partial`. The `_.curryRight.placeholder` value, which defaults to `_` in monolithic builds, may be used as a placeholder for provided arguments. **Note:** This method doesn't set the "length" property of curried functions.Since

3.0.0Arguments`func` *(Function)*: The function to curry.`[arity=func.length]` *(number)*: The arity of `func`.Returns

*(Function)*: Returns the new curried function.Examplevar abc = function(a, b, c) {  return [a, b, c];}; var curried = _.curryRight(abc); curried(3)(2)(1); curried(2, 3)(1); curried(1, 2, 3); curried(3)(1, _)(2);

### `_.debounce(func, [wait=0], [options={}])`

source npm package

Creates a debounced function that delays invoking `func` until after `wait` milliseconds have elapsed since the last time the debounced function was invoked. The debounced function comes with a `cancel` method to cancel delayed `func` invocations and a `flush` method to immediately invoke them. Provide `options` to indicate whether `func` should be invoked on the leading and/or trailing edge of the `wait` timeout. The `func` is invoked with the last arguments provided to the debounced function. Subsequent calls to the debounced function return the result of the last `func` invocation. **Note:** If `leading` and `trailing` options are `true`, `func` is invoked on the trailing edge of the timeout only if the debounced function is invoked more than once during the `wait` timeout. If `wait` is `0` and `leading` is `false`, `func` invocation is deferred until to the next tick, similar to `setTimeout` with a timeout of `0`. See David Corbacho's article for details over the differences between `_.debounce` and `_.throttle`.Since

0.1.0Arguments`func` *(Function)*: The function to debounce.`[wait=0]` *(number)*: The number of milliseconds to delay.`[options={}]` *(Object)*: The options object.`[options.leading=false]` *(boolean)*: Specify invoking on the leading edge of the timeout.`[options.maxWait]` *(number)*: The maximum time `func` is allowed to be delayed before it's invoked.`[options.trailing=true]` *(boolean)*: Specify invoking on the trailing edge of the timeout.Returns

*(Function)*: Returns the new debounced function.ExamplejQuery(window).on('resize', _.debounce(calculateLayout, 150)); jQuery(element).on('click', _.debounce(sendMail, 300, {  'leading': true,  'trailing': false})); var debounced = _.debounce(batchLog, 250, { 'maxWait': 1000 });var source = new EventSource('/stream');jQuery(source).on('message', debounced); jQuery(window).on('popstate', debounced.cancel);

### `_.defer(func, [args])`

source npm package

Defers invoking the `func` until the current call stack has cleared. Any additional arguments are provided to `func` when it's invoked.Since

0.1.0Arguments`func` *(Function)*: The function to defer.`[args]` *(...*)*: The arguments to invoke `func` with.Returns

*(number)*: Returns the timer id.Example_.defer(function(text) {  console.log(text);}, 'deferred');

### `_.delay(func, wait, [args])`

source npm package

Invokes `func` after `wait` milliseconds. Any additional arguments are provided to `func` when it's invoked.Since

0.1.0Arguments`func` *(Function)*: The function to delay.`wait` *(number)*: The number of milliseconds to delay invocation.`[args]` *(...*)*: The arguments to invoke `func` with.Returns

*(number)*: Returns the timer id.Example_.delay(function(text) {  console.log(text);}, 1000, 'later');

### `_.flip(func)`

source npm package

Creates a function that invokes `func` with arguments reversed.Since

4.0.0Arguments`func` *(Function)*: The function to flip arguments for.Returns

*(Function)*: Returns the new flipped function.Examplevar flipped = _.flip(function() {  return _.toArray(arguments);}); flipped('a', 'b', 'c', 'd');

### `_.memoize(func, [resolver])`

source npm package

Creates a function that memoizes the result of `func`. If `resolver` is provided, it determines the cache key for storing the result based on the arguments provided to the memoized function. By default, the first argument provided to the memoized function is used as the map cache key. The `func` is invoked with the `this` binding of the memoized function. **Note:** The cache is exposed as the `cache` property on the memoized function. Its creation may be customized by replacing the `_.memoize.Cache` constructor with one whose instances implement the `Map` method interface of `clear`, `delete`, `get`, `has`, and `set`.Since

0.1.0Arguments`func` *(Function)*: The function to have its output memoized.`[resolver]` *(Function)*: The function to resolve the cache key.Returns

*(Function)*: Returns the new memoized function.Examplevar object = { 'a': 1, 'b': 2 };var other = { 'c': 3, 'd': 4 }; var values = _.memoize(_.values);values(object); values(other); object.a = 2;values(object); values.cache.set(object, ['a', 'b']);values(object); _.memoize.Cache = WeakMap;

### `_.negate(predicate)`

source npm package

Creates a function that negates the result of the predicate `func`. The `func` predicate is invoked with the `this` binding and arguments of the created function.Since

3.0.0Arguments`predicate` *(Function)*: The predicate to negate.Returns

*(Function)*: Returns the new negated function.Examplefunction isEven(n) {  return n % 2 == 0;} _.filter([1, 2, 3, 4, 5, 6], _.negate(isEven));

### `_.once(func)`

source npm package

Creates a function that is restricted to invoking `func` once. Repeat calls to the function return the value of the first invocation. The `func` is invoked with the `this` binding and arguments of the created function.Since

0.1.0Arguments`func` *(Function)*: The function to restrict.Returns

*(Function)*: Returns the new restricted function.Examplevar initialize = _.once(createApplication);initialize();initialize();

### `_.overArgs(func, [transforms=[_.identity]])`

source npm package

Creates a function that invokes `func` with its arguments transformed.Since

4.0.0Arguments`func` *(Function)*: The function to wrap.`[transforms=[_.identity]]` *(...(Function|Function[]))*: The argument transforms.Returns

*(Function)*: Returns the new function.Examplefunction doubled(n) {  return n * 2;} function square(n) {  return n * n;} var func = _.overArgs(function(x, y) {  return [x, y];}, [square, doubled]); func(9, 3); func(10, 5);

### `_.partial(func, [partials])`

source npm package

Creates a function that invokes `func` with `partials` prepended to the arguments it receives. This method is like `_.bind` except it does **not** alter the `this` binding. The `_.partial.placeholder` value, which defaults to `_` in monolithic builds, may be used as a placeholder for partially applied arguments. **Note:** This method doesn't set the "length" property of partially applied functions.Since

0.2.0Arguments`func` *(Function)*: The function to partially apply arguments to.`[partials]` *(...*)*: The arguments to be partially applied.Returns

*(Function)*: Returns the new partially applied function.Examplefunction greet(greeting, name) {  return greeting + ' ' + name;} var sayHelloTo = _.partial(greet, 'hello');sayHelloTo('fred'); var greetFred = _.partial(greet, _, 'fred');greetFred('hi');

### `_.partialRight(func, [partials])`

source npm package

This method is like `_.partial` except that partially applied arguments are appended to the arguments it receives. The `_.partialRight.placeholder` value, which defaults to `_` in monolithic builds, may be used as a placeholder for partially applied arguments. **Note:** This method doesn't set the "length" property of partially applied functions.Since

1.0.0Arguments`func` *(Function)*: The function to partially apply arguments to.`[partials]` *(...*)*: The arguments to be partially applied.Returns

*(Function)*: Returns the new partially applied function.Examplefunction greet(greeting, name) {  return greeting + ' ' + name;} var greetFred = _.partialRight(greet, 'fred');greetFred('hi'); var sayHelloTo = _.partialRight(greet, 'hello', _);sayHelloTo('fred');

### `_.rearg(func, indexes)`

source npm package

Creates a function that invokes `func` with arguments arranged according to the specified `indexes` where the argument value at the first index is provided as the first argument, the argument value at the second index is provided as the second argument, and so on.Since

3.0.0Arguments`func` *(Function)*: The function to rearrange arguments for.`indexes` *(...(number|number[]))*: The arranged argument indexes.Returns

*(Function)*: Returns the new function.Examplevar rearged = _.rearg(function(a, b, c) {  return [a, b, c];}, [2, 0, 1]); rearged('b', 'c', 'a')

### `_.rest(func, [start=func.length-1])`

source npm package

Creates a function that invokes `func` with the `this` binding of the created function and arguments from `start` and beyond provided as an array. **Note:** This method is based on the rest parameter.Since

4.0.0Arguments`func` *(Function)*: The function to apply a rest parameter to.`[start=func.length-1]` *(number)*: The start position of the rest parameter.Returns

*(Function)*: Returns the new function.Examplevar say = _.rest(function(what, names) {  return what + ' ' + _.initial(names).join(', ') +    (_.size(names) > 1 ? ', & ' : '') + _.last(names);}); say('hello', 'fred', 'barney', 'pebbles');

### `_.spread(func, [start=0])`

source npm package

Creates a function that invokes `func` with the `this` binding of the create function and an array of arguments much like `Function#apply`. **Note:** This method is based on the spread operator.Since

3.2.0Arguments`func` *(Function)*: The function to spread arguments over.`[start=0]` *(number)*: The start position of the spread.Returns

*(Function)*: Returns the new function.Examplevar say = _.spread(function(who, what) {  return who + ' says ' + what;}); say(['fred', 'hello']); var numbers = Promise.all([  Promise.resolve(40),  Promise.resolve(36)]); numbers.then(_.spread(function(x, y) {  return x + y;}));

### `_.throttle(func, [wait=0], [options={}])`

source npm package

Creates a throttled function that only invokes `func` at most once per every `wait` milliseconds. The throttled function comes with a `cancel` method to cancel delayed `func` invocations and a `flush` method to immediately invoke them. Provide `options` to indicate whether `func` should be invoked on the leading and/or trailing edge of the `wait` timeout. The `func` is invoked with the last arguments provided to the throttled function. Subsequent calls to the throttled function return the result of the last `func` invocation. **Note:** If `leading` and `trailing` options are `true`, `func` is invoked on the trailing edge of the timeout only if the throttled function is invoked more than once during the `wait` timeout. If `wait` is `0` and `leading` is `false`, `func` invocation is deferred until to the next tick, similar to `setTimeout` with a timeout of `0`. See David Corbacho's article for details over the differences between `_.throttle` and `_.debounce`.Since

0.1.0Arguments`func` *(Function)*: The function to throttle.`[wait=0]` *(number)*: The number of milliseconds to throttle invocations to.`[options={}]` *(Object)*: The options object.`[options.leading=true]` *(boolean)*: Specify invoking on the leading edge of the timeout.`[options.trailing=true]` *(boolean)*: Specify invoking on the trailing edge of the timeout.Returns

*(Function)*: Returns the new throttled function.ExamplejQuery(window).on('scroll', _.throttle(updatePosition, 100)); var throttled = _.throttle(renewToken, 300000, { 'trailing': false });jQuery(element).on('click', throttled); jQuery(window).on('popstate', throttled.cancel);

### `_.unary(func)`

source npm package

Creates a function that accepts up to one argument, ignoring any additional arguments.Since

4.0.0Arguments`func` *(Function)*: The function to cap arguments for.Returns

*(Function)*: Returns the new capped function.Example_.map(['6', '8', '10'], _.unary(parseInt));

### `_.wrap(value, [wrapper=identity])`

source npm package

Creates a function that provides `value` to `wrapper` as its first argument. Any additional arguments provided to the function are appended to those provided to the `wrapper`. The wrapper is invoked with the `this` binding of the created function.Since

0.1.0Arguments`value` *(*)*: The value to wrap.`[wrapper=identity]` *(Function)*: The wrapper function.Returns

*(Function)*: Returns the new function.Examplevar p = _.wrap(_.escape, function(func, text) {  return '<p>' + func(text) + '</p>';}); p('fred, barney, & pebbles');
