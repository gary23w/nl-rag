---
title: "Lodash Documentation (part 1/5)"
source: https://lodash.com/docs/
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
part: 1/5
---

# Lodash Documentation

Lodash


## `“Array” Methods`

### `_.chunk(array, [size=1])`

source npm package

Creates an array of elements split into groups the length of `size`. If `array` can't be split evenly, the final chunk will be the remaining elements.Since

3.0.0Arguments`array` *(Array)*: The array to process.`[size=1]` *(number)*: The length of each chunkReturns

*(Array)*: Returns the new array of chunks.Example_.chunk(['a', 'b', 'c', 'd'], 2); _.chunk(['a', 'b', 'c', 'd'], 3);

### `_.compact(array)`

source npm package

Creates an array with all falsey values removed. The values `false`, `null`, `0`, `-0`, `0n`, `""`, `undefined`, and `NaN` are falsy.Since

0.1.0Arguments`array` *(Array)*: The array to compact.Returns

*(Array)*: Returns the new array of filtered values.Example_.compact([0, 1, false, 2, '', 3]);

### `_.concat(array, [values])`

source npm package

Creates a new array concatenating `array` with any additional arrays and/or values.Since

4.0.0Arguments`array` *(Array)*: The array to concatenate.`[values]` *(...*)*: The values to concatenate.Returns

*(Array)*: Returns the new concatenated array.Examplevar array = [1];var other = _.concat(array, 2, [3], [[4]]); console.log(other); console.log(array);

### `_.difference(array, [values])`

source npm package

Creates an array of `array` values not included in the other given arrays using `SameValueZero` for equality comparisons. The order and references of result values are determined by the first array. **Note:** Unlike `_.pullAll`, this method returns a new array.Since

0.1.0Arguments`array` *(Array)*: The array to inspect.`[values]` *(...Array)*: The values to exclude.Returns

*(Array)*: Returns the new array of filtered values.Example_.difference([2, 1], [2, 3]);

### `_.differenceBy(array, [values], [iteratee=_.identity])`

source npm package

This method is like `_.difference` except that it accepts `iteratee` which is invoked for each element of `array` and `values` to generate the criterion by which they're compared. The order and references of result values are determined by the first array. The iteratee is invoked with one argument: *(value)*. **Note:** Unlike `_.pullAllBy`, this method returns a new array.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`[values]` *(...Array)*: The values to exclude.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns the new array of filtered values.Example_.differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); _.differenceBy([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], 'x');

### `_.differenceWith(array, [values], [comparator])`

source npm package

This method is like `_.difference` except that it accepts `comparator` which is invoked to compare elements of `array` to `values`. The order and references of result values are determined by the first array. The comparator is invoked with two arguments: *(arrVal, othVal)*. **Note:** Unlike `_.pullAllWith`, this method returns a new array.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`[values]` *(...Array)*: The values to exclude.`[comparator]` *(Function)*: The comparator invoked per element.Returns

*(Array)*: Returns the new array of filtered values.Examplevar objects = [{ 'x': 1, 'y': 2 }, { 'x': 2, 'y': 1 }]; _.differenceWith(objects, [{ 'x': 1, 'y': 2 }], _.isEqual);

### `_.drop(array, [n=1])`

source npm package

Creates a slice of `array` with `n` elements dropped from the beginning.Since

0.5.0Arguments`array` *(Array)*: The array to query.`[n=1]` *(number)*: The number of elements to drop.Returns

*(Array)*: Returns the slice of `array`.Example_.drop([1, 2, 3]); _.drop([1, 2, 3], 2); _.drop([1, 2, 3], 5); _.drop([1, 2, 3], 0);

### `_.dropRight(array, [n=1])`

source npm package

Creates a slice of `array` with `n` elements dropped from the end.Since

3.0.0Arguments`array` *(Array)*: The array to query.`[n=1]` *(number)*: The number of elements to drop.Returns

*(Array)*: Returns the slice of `array`.Example_.dropRight([1, 2, 3]); _.dropRight([1, 2, 3], 2); _.dropRight([1, 2, 3], 5); _.dropRight([1, 2, 3], 0);

### `_.dropRightWhile(array, [predicate=_.identity])`

source npm package

Creates a slice of `array` excluding elements dropped from the end. Elements are dropped until `predicate` returns falsey. The predicate is invoked with three arguments: *(value, index, array)*.Since

3.0.0Arguments`array` *(Array)*: The array to query.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the slice of `array`.Examplevar users = [  { 'user': 'barney',  'active': true },  { 'user': 'fred',    'active': false },  { 'user': 'pebbles', 'active': false }]; _.dropRightWhile(users, function(o) { return !o.active; }); _.dropRightWhile(users, { 'user': 'pebbles', 'active': false }); _.dropRightWhile(users, ['active', false]); _.dropRightWhile(users, 'active');

### `_.dropWhile(array, [predicate=_.identity])`

source npm package

Creates a slice of `array` excluding elements dropped from the beginning. Elements are dropped until `predicate` returns falsey. The predicate is invoked with three arguments: *(value, index, array)*.Since

3.0.0Arguments`array` *(Array)*: The array to query.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the slice of `array`.Examplevar users = [  { 'user': 'barney',  'active': false },  { 'user': 'fred',    'active': false },  { 'user': 'pebbles', 'active': true }]; _.dropWhile(users, function(o) { return !o.active; }); _.dropWhile(users, { 'user': 'barney', 'active': false }); _.dropWhile(users, ['active', false]); _.dropWhile(users, 'active');

### `_.fill(array, value, [start=0], [end=array.length])`

source npm package

Fills elements of `array` with `value` from `start` up to, but not including, `end`. **Note:** This method mutates `array`.Since

3.2.0Arguments`array` *(Array)*: The array to fill.`value` *(*)*: The value to fill `array` with.`[start=0]` *(number)*: The start position.`[end=array.length]` *(number)*: The end position.Returns

*(Array)*: Returns `array`.Examplevar array = [1, 2, 3]; _.fill(array, 'a');console.log(array); _.fill(Array(3), 2); _.fill([4, 6, 8, 10], '*', 1, 3);

### `_.findIndex(array, [predicate=_.identity], [fromIndex=0])`

source npm package

This method is like `_.find` except that it returns the index of the first element `predicate` returns truthy for instead of the element itself.Since

1.1.0Arguments`array` *(Array)*: The array to inspect.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.`[fromIndex=0]` *(number)*: The index to search from.Returns

*(number)*: Returns the index of the found element, else `-1`.Examplevar users = [  { 'user': 'barney',  'active': false },  { 'user': 'fred',    'active': false },  { 'user': 'pebbles', 'active': true }]; _.findIndex(users, function(o) { return o.user == 'barney'; }); _.findIndex(users, { 'user': 'fred', 'active': false }); _.findIndex(users, ['active', false]); _.findIndex(users, 'active');

### `_.findLastIndex(array, [predicate=_.identity], [fromIndex=array.length-1])`

source npm package

This method is like `_.findIndex` except that it iterates over elements of `collection` from right to left.Since

2.0.0Arguments`array` *(Array)*: The array to inspect.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.`[fromIndex=array.length-1]` *(number)*: The index to search from.Returns

*(number)*: Returns the index of the found element, else `-1`.Examplevar users = [  { 'user': 'barney',  'active': true },  { 'user': 'fred',    'active': false },  { 'user': 'pebbles', 'active': false }]; _.findLastIndex(users, function(o) { return o.user == 'pebbles'; }); _.findLastIndex(users, { 'user': 'barney', 'active': true }); _.findLastIndex(users, ['active', false]); _.findLastIndex(users, 'active');

### `_.flatten(array)`

source npm package

Flattens `array` a single level deep.Since

0.1.0Arguments`array` *(Array)*: The array to flatten.Returns

*(Array)*: Returns the new flattened array.Example_.flatten([1, [2, [3, [4]], 5]]);

### `_.flattenDeep(array)`

source npm package

Recursively flattens `array`.Since

3.0.0Arguments`array` *(Array)*: The array to flatten.Returns

*(Array)*: Returns the new flattened array.Example_.flattenDeep([1, [2, [3, [4]], 5]]);

### `_.flattenDepth(array, [depth=1])`

source npm package

Recursively flatten `array` up to `depth` times.Since

4.4.0Arguments`array` *(Array)*: The array to flatten.`[depth=1]` *(number)*: The maximum recursion depth.Returns

*(Array)*: Returns the new flattened array.Examplevar array = [1, [2, [3, [4]], 5]]; _.flattenDepth(array, 1); _.flattenDepth(array, 2);

### `_.fromPairs(pairs)`

source npm package

The inverse of `_.toPairs`; this method returns an object composed from key-value `pairs`.Since

4.0.0Arguments`pairs` *(Array)*: The key-value pairs.Returns

*(Object)*: Returns the new object.Example_.fromPairs([['a', 1], ['b', 2]]);

### `_.head(array)`

source npm package

Gets the first element of `array`.Since

0.1.0Aliases

*_.first*Arguments`array` *(Array)*: The array to query.Returns

*(*)*: Returns the first element of `array`.Example_.head([1, 2, 3]); _.head([]);

### `_.indexOf(array, value, [fromIndex=0])`

source npm package

Gets the index at which the first occurrence of `value` is found in `array` using `SameValueZero` for equality comparisons. If `fromIndex` is negative, it's used as the offset from the end of `array`.Since

0.1.0Arguments`array` *(Array)*: The array to inspect.`value` *(*)*: The value to search for.`[fromIndex=0]` *(number)*: The index to search from.Returns

*(number)*: Returns the index of the matched value, else `-1`.Example_.indexOf([1, 2, 1, 2], 2); _.indexOf([1, 2, 1, 2], 2, 2);

### `_.initial(array)`

source npm package

Gets all but the last element of `array`.Since

0.1.0Arguments`array` *(Array)*: The array to query.Returns

*(Array)*: Returns the slice of `array`.Example_.initial([1, 2, 3]);

### `_.intersection([arrays])`

source npm package

Creates an array of unique values that are included in all given arrays using `SameValueZero` for equality comparisons. The order and references of result values are determined by the first array.Since

0.1.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.Returns

*(Array)*: Returns the new array of intersecting values.Example_.intersection([2, 1], [2, 3]);

### `_.intersectionBy([arrays], [iteratee=_.identity])`

source npm package

This method is like `_.intersection` except that it accepts `iteratee` which is invoked for each element of each `arrays` to generate the criterion by which they're compared. The order and references of result values are determined by the first array. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns the new array of intersecting values.Example_.intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); _.intersectionBy([{ 'x': 1 }], [{ 'x': 2 }, { 'x': 1 }], 'x');

### `_.intersectionWith([arrays], [comparator])`

source npm package

This method is like `_.intersection` except that it accepts `comparator` which is invoked to compare elements of `arrays`. The order and references of result values are determined by the first array. The comparator is invoked with two arguments: *(arrVal, othVal)*.Since

4.0.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.`[comparator]` *(Function)*: The comparator invoked per element.Returns

*(Array)*: Returns the new array of intersecting values.Examplevar objects = [{ 'x': 1, 'y': 2 }, { 'x': 2, 'y': 1 }];var others = [{ 'x': 1, 'y': 1 }, { 'x': 1, 'y': 2 }]; _.intersectionWith(objects, others, _.isEqual);

### `_.join(array, [separator=','])`

source npm package

Converts all elements in `array` into a string separated by `separator`.Since

4.0.0Arguments`array` *(Array)*: The array to convert.`[separator=',']` *(string)*: The element separator.Returns

*(string)*: Returns the joined string.Example_.join(['a', 'b', 'c'], '~');

### `_.last(array)`

source npm package

Gets the last element of `array`.Since

0.1.0Arguments`array` *(Array)*: The array to query.Returns

*(*)*: Returns the last element of `array`.Example_.last([1, 2, 3]);

### `_.lastIndexOf(array, value, [fromIndex=array.length-1])`

source npm package

This method is like `_.indexOf` except that it iterates over elements of `array` from right to left.Since

0.1.0Arguments`array` *(Array)*: The array to inspect.`value` *(*)*: The value to search for.`[fromIndex=array.length-1]` *(number)*: The index to search from.Returns

*(number)*: Returns the index of the matched value, else `-1`.Example_.lastIndexOf([1, 2, 1, 2], 2); _.lastIndexOf([1, 2, 1, 2], 2, 2);

### `_.nth(array, [n=0])`

source npm package

Gets the element at index `n` of `array`. If `n` is negative, the nth element from the end is returned.Since

4.11.0Arguments`array` *(Array)*: The array to query.`[n=0]` *(number)*: The index of the element to return.Returns

*(*)*: Returns the nth element of `array`.Examplevar array = ['a', 'b', 'c', 'd']; _.nth(array, 1); _.nth(array, -2);

### `_.pull(array, [values])`

source npm package

Removes all given values from `array` using `SameValueZero` for equality comparisons. **Note:** Unlike `_.without`, this method mutates `array`. Use `_.remove` to remove elements from an array by predicate.Since

2.0.0Arguments`array` *(Array)*: The array to modify.`[values]` *(...*)*: The values to remove.Returns

*(Array)*: Returns `array`.Examplevar array = ['a', 'b', 'c', 'a', 'b', 'c']; _.pull(array, 'a', 'c');console.log(array);

### `_.pullAll(array, values)`

source npm package

This method is like `_.pull` except that it accepts an array of values to remove. **Note:** Unlike `_.difference`, this method mutates `array`.Since

4.0.0Arguments`array` *(Array)*: The array to modify.`values` *(Array)*: The values to remove.Returns

*(Array)*: Returns `array`.Examplevar array = ['a', 'b', 'c', 'a', 'b', 'c']; _.pullAll(array, ['a', 'c']);console.log(array);

### `_.pullAllBy(array, values, [iteratee=_.identity])`

source npm package

This method is like `_.pullAll` except that it accepts `iteratee` which is invoked for each element of `array` and `values` to generate the criterion by which they're compared. The iteratee is invoked with one argument: *(value)*. **Note:** Unlike `_.differenceBy`, this method mutates `array`.Since

4.0.0Arguments`array` *(Array)*: The array to modify.`values` *(Array)*: The values to remove.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns `array`.Examplevar array = [{ 'x': 1 }, { 'x': 2 }, { 'x': 3 }, { 'x': 1 }]; _.pullAllBy(array, [{ 'x': 1 }, { 'x': 3 }], 'x');console.log(array);

### `_.pullAllWith(array, values, [comparator])`

source npm package

This method is like `_.pullAll` except that it accepts `comparator` which is invoked to compare elements of `array` to `values`. The comparator is invoked with two arguments: *(arrVal, othVal)*. **Note:** Unlike `_.differenceWith`, this method mutates `array`.Since

4.6.0Arguments`array` *(Array)*: The array to modify.`values` *(Array)*: The values to remove.`[comparator]` *(Function)*: The comparator invoked per element.Returns

*(Array)*: Returns `array`.Examplevar array = [{ 'x': 1, 'y': 2 }, { 'x': 3, 'y': 4 }, { 'x': 5, 'y': 6 }]; _.pullAllWith(array, [{ 'x': 3, 'y': 4 }], _.isEqual);console.log(array);

### `_.pullAt(array, [indexes])`

source npm package

Removes elements from `array` corresponding to `indexes` and returns an array of removed elements. **Note:** Unlike `_.at`, this method mutates `array`.Since

3.0.0Arguments`array` *(Array)*: The array to modify.`[indexes]` *(...(number|number[]))*: The indexes of elements to remove.Returns

*(Array)*: Returns the new array of removed elements.Examplevar array = ['a', 'b', 'c', 'd'];var pulled = _.pullAt(array, [1, 3]); console.log(array); console.log(pulled);

### `_.remove(array, [predicate=_.identity])`

source npm package

Removes all elements from `array` that `predicate` returns truthy for and returns an array of the removed elements. The predicate is invoked with three arguments: *(value, index, array)*. **Note:** Unlike `_.filter`, this method mutates `array`. Use `_.pull` to pull elements from an array by value.Since

2.0.0Arguments`array` *(Array)*: The array to modify.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the new array of removed elements.Examplevar array = [1, 2, 3, 4];var evens = _.remove(array, function(n) {  return n % 2 == 0;}); console.log(array); console.log(evens);

### `_.reverse(array)`

source npm package

Reverses `array` so that the first element becomes the last, the second element becomes the second to last, and so on. **Note:** This method mutates `array` and is based on `Array#reverse`.Since

4.0.0Arguments`array` *(Array)*: The array to modify.Returns

*(Array)*: Returns `array`.Examplevar array = [1, 2, 3]; _.reverse(array); console.log(array);

### `_.slice(array, [start=0], [end=array.length])`

source npm package

Creates a slice of `array` from `start` up to, but not including, `end`. **Note:** This method is used instead of `Array#slice` to ensure dense arrays are returned.Since

3.0.0Arguments`array` *(Array)*: The array to slice.`[start=0]` *(number)*: The start position.`[end=array.length]` *(number)*: The end position.Returns

*(Array)*: Returns the slice of `array`.

### `_.sortedIndex(array, value)`

source npm package

Uses a binary search to determine the lowest index at which `value` should be inserted into `array` in order to maintain its sort order.Since

0.1.0Arguments`array` *(Array)*: The sorted array to inspect.`value` *(*)*: The value to evaluate.Returns

*(number)*: Returns the index at which `value` should be inserted into `array`.Example_.sortedIndex([30, 50], 40);

### `_.sortedIndexBy(array, value, [iteratee=_.identity])`

source npm package

This method is like `_.sortedIndex` except that it accepts `iteratee` which is invoked for `value` and each element of `array` to compute their sort ranking. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`array` *(Array)*: The sorted array to inspect.`value` *(*)*: The value to evaluate.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(number)*: Returns the index at which `value` should be inserted into `array`.Examplevar objects = [{ 'x': 4 }, { 'x': 5 }]; _.sortedIndexBy(objects, { 'x': 4 }, function(o) { return o.x; }); _.sortedIndexBy(objects, { 'x': 4 }, 'x');

### `_.sortedIndexOf(array, value)`

source npm package

This method is like `_.indexOf` except that it performs a binary search on a sorted `array`.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`value` *(*)*: The value to search for.Returns

*(number)*: Returns the index of the matched value, else `-1`.Example_.sortedIndexOf([4, 5, 5, 5, 6], 5);

### `_.sortedLastIndex(array, value)`

source npm package

This method is like `_.sortedIndex` except that it returns the highest index at which `value` should be inserted into `array` in order to maintain its sort order.Since

3.0.0Arguments`array` *(Array)*: The sorted array to inspect.`value` *(*)*: The value to evaluate.Returns

*(number)*: Returns the index at which `value` should be inserted into `array`.Example_.sortedLastIndex([4, 5, 5, 5, 6], 5);

### `_.sortedLastIndexBy(array, value, [iteratee=_.identity])`

source npm package

This method is like `_.sortedLastIndex` except that it accepts `iteratee` which is invoked for `value` and each element of `array` to compute their sort ranking. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`array` *(Array)*: The sorted array to inspect.`value` *(*)*: The value to evaluate.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(number)*: Returns the index at which `value` should be inserted into `array`.Examplevar objects = [{ 'x': 4 }, { 'x': 5 }]; _.sortedLastIndexBy(objects, { 'x': 4 }, function(o) { return o.x; }); _.sortedLastIndexBy(objects, { 'x': 4 }, 'x');

### `_.sortedLastIndexOf(array, value)`

source npm package

This method is like `_.lastIndexOf` except that it performs a binary search on a sorted `array`.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`value` *(*)*: The value to search for.Returns

*(number)*: Returns the index of the matched value, else `-1`.Example_.sortedLastIndexOf([4, 5, 5, 5, 6], 5);

### `_.sortedUniq(array)`

source npm package

This method is like `_.uniq` except that it's designed and optimized for sorted arrays.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.Returns

*(Array)*: Returns the new duplicate free array.Example_.sortedUniq([1, 1, 2]);

### `_.sortedUniqBy(array, [iteratee])`

source npm package

This method is like `_.uniqBy` except that it's designed and optimized for sorted arrays.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`[iteratee]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns the new duplicate free array.Example_.sortedUniqBy([1.1, 1.2, 2.3, 2.4], Math.floor);

### `_.tail(array)`

source npm package

Gets all but the first element of `array`.Since

4.0.0Arguments`array` *(Array)*: The array to query.Returns

*(Array)*: Returns the slice of `array`.Example_.tail([1, 2, 3]);

### `_.take(array, [n=1])`

source npm package

Creates a slice of `array` with `n` elements taken from the beginning.Since

0.1.0Arguments`array` *(Array)*: The array to query.`[n=1]` *(number)*: The number of elements to take.Returns

*(Array)*: Returns the slice of `array`.Example_.take([1, 2, 3]); _.take([1, 2, 3], 2); _.take([1, 2, 3], 5); _.take([1, 2, 3], 0);

### `_.takeRight(array, [n=1])`

source npm package

Creates a slice of `array` with `n` elements taken from the end.Since

3.0.0Arguments`array` *(Array)*: The array to query.`[n=1]` *(number)*: The number of elements to take.Returns

*(Array)*: Returns the slice of `array`.Example_.takeRight([1, 2, 3]); _.takeRight([1, 2, 3], 2); _.takeRight([1, 2, 3], 5); _.takeRight([1, 2, 3], 0);

### `_.takeRightWhile(array, [predicate=_.identity])`

source npm package

Creates a slice of `array` with elements taken from the end. Elements are taken until `predicate` returns falsey. The predicate is invoked with three arguments: *(value, index, array)*.Since

3.0.0Arguments`array` *(Array)*: The array to query.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the slice of `array`.Examplevar users = [  { 'user': 'barney',  'active': true },  { 'user': 'fred',    'active': false },  { 'user': 'pebbles', 'active': false }]; _.takeRightWhile(users, function(o) { return !o.active; }); _.takeRightWhile(users, { 'user': 'pebbles', 'active': false }); _.takeRightWhile(users, ['active', false]); _.takeRightWhile(users, 'active');

### `_.takeWhile(array, [predicate=_.identity])`

source npm package

Creates a slice of `array` with elements taken from the beginning. Elements are taken until `predicate` returns falsey. The predicate is invoked with three arguments: *(value, index, array)*.Since

3.0.0Arguments`array` *(Array)*: The array to query.`[predicate=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the slice of `array`.Examplevar users = [  { 'user': 'barney',  'active': false },  { 'user': 'fred',    'active': false },  { 'user': 'pebbles', 'active': true }]; _.takeWhile(users, function(o) { return !o.active; }); _.takeWhile(users, { 'user': 'barney', 'active': false }); _.takeWhile(users, ['active', false]); _.takeWhile(users, 'active');

### `_.union([arrays])`

source npm package

Creates an array of unique values, in order, from all given arrays using `SameValueZero` for equality comparisons.Since

0.1.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.Returns

*(Array)*: Returns the new array of combined values.Example_.union([2], [1, 2]);

### `_.unionBy([arrays], [iteratee=_.identity])`

source npm package

This method is like `_.union` except that it accepts `iteratee` which is invoked for each element of each `arrays` to generate the criterion by which uniqueness is computed. Result values are chosen from the first array in which the value occurs. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns the new array of combined values.Example_.unionBy([2.1], [1.2, 2.3], Math.floor); _.unionBy([{ 'x': 1 }], [{ 'x': 2 }, { 'x': 1 }], 'x');

### `_.unionWith([arrays], [comparator])`

source npm package

This method is like `_.union` except that it accepts `comparator` which is invoked to compare elements of `arrays`. Result values are chosen from the first array in which the value occurs. The comparator is invoked with two arguments: *(arrVal, othVal)*.Since

4.0.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.`[comparator]` *(Function)*: The comparator invoked per element.Returns

*(Array)*: Returns the new array of combined values.Examplevar objects = [{ 'x': 1, 'y': 2 }, { 'x': 2, 'y': 1 }];var others = [{ 'x': 1, 'y': 1 }, { 'x': 1, 'y': 2 }]; _.unionWith(objects, others, _.isEqual);

### `_.uniq(array)`

source npm package

Creates a duplicate-free version of an array, using `SameValueZero` for equality comparisons, in which only the first occurrence of each element is kept. The order of result values is determined by the order they occur in the array.Since

0.1.0Arguments`array` *(Array)*: The array to inspect.Returns

*(Array)*: Returns the new duplicate free array.Example_.uniq([2, 1, 2]);

### `_.uniqBy(array, [iteratee=_.identity])`

source npm package

This method is like `_.uniq` except that it accepts `iteratee` which is invoked for each element in `array` to generate the criterion by which uniqueness is computed. The order of result values is determined by the order they occur in the array. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns the new duplicate free array.Example_.uniqBy([2.1, 1.2, 2.3], Math.floor); _.uniqBy([{ 'x': 1 }, { 'x': 2 }, { 'x': 1 }], 'x');

### `_.uniqWith(array, [comparator])`

source npm package

This method is like `_.uniq` except that it accepts `comparator` which is invoked to compare elements of `array`. The order of result values is determined by the order they occur in the array.The comparator is invoked with two arguments: *(arrVal, othVal)*.Since

4.0.0Arguments`array` *(Array)*: The array to inspect.`[comparator]` *(Function)*: The comparator invoked per element.Returns

*(Array)*: Returns the new duplicate free array.Examplevar objects = [{ 'x': 1, 'y': 2 }, { 'x': 2, 'y': 1 }, { 'x': 1, 'y': 2 }]; _.uniqWith(objects, _.isEqual);

### `_.unzip(array)`

source npm package

This method is like `_.zip` except that it accepts an array of grouped elements and creates an array regrouping the elements to their pre-zip configuration.Since

1.2.0Arguments`array` *(Array)*: The array of grouped elements to process.Returns

*(Array)*: Returns the new array of regrouped elements.Examplevar zipped = _.zip(['a', 'b'], [1, 2], [true, false]); _.unzip(zipped);

### `_.unzipWith(array, [iteratee=_.identity])`

source npm package

This method is like `_.unzip` except that it accepts `iteratee` to specify how regrouped values should be combined. The iteratee is invoked with the elements of each group: *(...group)*.Since

3.8.0Arguments`array` *(Array)*: The array of grouped elements to process.`[iteratee=_.identity]` *(Function)*: The function to combine regrouped values.Returns

*(Array)*: Returns the new array of regrouped elements.Examplevar zipped = _.zip([1, 2], [10, 20], [100, 200]); _.unzipWith(zipped, _.add);

### `_.without(array, [values])`

source npm package

Creates an array excluding all given values using `SameValueZero` for equality comparisons. **Note:** Unlike `_.pull`, this method returns a new array.Since

0.1.0Arguments`array` *(Array)*: The array to inspect.`[values]` *(...*)*: The values to exclude.Returns

*(Array)*: Returns the new array of filtered values.Example_.without([2, 1, 2, 3], 1, 2);

### `_.xor([arrays])`

source npm package

Creates an array of unique values that is the symmetric difference of the given arrays. The order of result values is determined by the order they occur in the arrays.Since

2.4.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.Returns

*(Array)*: Returns the new array of filtered values.Example_.xor([2, 1], [2, 3]);

### `_.xorBy([arrays], [iteratee=_.identity])`

source npm package

This method is like `_.xor` except that it accepts `iteratee` which is invoked for each element of each `arrays` to generate the criterion by which by which they're compared. The order of result values is determined by the order they occur in the arrays. The iteratee is invoked with one argument: *(value)*.Since

4.0.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.`[iteratee=_.identity]` *(Function)*: The iteratee invoked per element.Returns

*(Array)*: Returns the new array of filtered values.Example_.xorBy([2.1, 1.2], [2.3, 3.4], Math.floor); _.xorBy([{ 'x': 1 }], [{ 'x': 2 }, { 'x': 1 }], 'x');

### `_.xorWith([arrays], [comparator])`

source npm package

This method is like `_.xor` except that it accepts `comparator` which is invoked to compare elements of `arrays`. The order of result values is determined by the order they occur in the arrays. The comparator is invoked with two arguments: *(arrVal, othVal)*.Since

4.0.0Arguments`[arrays]` *(...Array)*: The arrays to inspect.`[comparator]` *(Function)*: The comparator invoked per element.Returns

*(Array)*: Returns the new array of filtered values.Examplevar objects = [{ 'x': 1, 'y': 2 }, { 'x': 2, 'y': 1 }];var others = [{ 'x': 1, 'y': 1 }, { 'x': 1, 'y': 2 }]; _.xorWith(objects, others, _.isEqual);

### `_.zip([arrays])`

source npm package

Creates an array of grouped elements, the first of which contains the first elements of the given arrays, the second of which contains the second elements of the given arrays, and so on.Since

0.1.0Arguments`[arrays]` *(...Array)*: The arrays to process.Returns

*(Array)*: Returns the new array of grouped elements.Example_.zip(['a', 'b'], [1, 2], [true, false]);

### `_.zipObject([props=[]], [values=[]])`

source npm package

This method is like `_.fromPairs` except that it accepts two arrays, one of property identifiers and one of corresponding values.Since

0.4.0Arguments`[props=[]]` *(Array)*: The property identifiers.`[values=[]]` *(Array)*: The property values.Returns

*(Object)*: Returns the new object.Example_.zipObject(['a', 'b'], [1, 2]);

### `_.zipObjectDeep([props=[]], [values=[]])`

source npm package

This method is like `_.zipObject` except that it supports property paths.Since

4.1.0Arguments`[props=[]]` *(Array)*: The property identifiers.`[values=[]]` *(Array)*: The property values.Returns

*(Object)*: Returns the new object.Example_.zipObjectDeep(['a.b[0].c', 'a.b[1].d'], [1, 2]);

### `_.zipWith([arrays], [iteratee=_.identity])`

source npm package

This method is like `_.zip` except that it accepts `iteratee` to specify how grouped values should be combined. The iteratee is invoked with the elements of each group: *(...group)*.Since

3.8.0Arguments`[arrays]` *(...Array)*: The arrays to process.`[iteratee=_.identity]` *(Function)*: The function to combine grouped values.Returns

*(Array)*: Returns the new array of grouped elements.Example_.zipWith([1, 2], [10, 20], [100, 200], function(a, b, c) {  return a + b + c;});
