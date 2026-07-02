---
title: "Lodash Documentation (part 5/5)"
source: https://lodash.com/docs/
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
part: 5/5
---

## `“String” Methods`

### `_.camelCase([string=''])`

source npm package

Converts `string` to camel case.Since

3.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the camel cased string.Example_.camelCase('Foo Bar'); _.camelCase('--foo-bar--'); _.camelCase('__FOO_BAR__');

### `_.capitalize([string=''])`

source npm package

Converts the first character of `string` to upper case and the remaining to lower case.Since

3.0.0Arguments`[string='']` *(string)*: The string to capitalize.Returns

*(string)*: Returns the capitalized string.Example_.capitalize('FRED');

### `_.deburr([string=''])`

source npm package

Deburrs `string` by converting Latin-1 Supplement and Latin Extended-A letters to basic Latin letters and removing combining diacritical marks.Since

3.0.0Arguments`[string='']` *(string)*: The string to deburr.Returns

*(string)*: Returns the deburred string.Example_.deburr('déjà vu');

### `_.endsWith([string=''], [target], [position=string.length])`

source npm package

Checks if `string` ends with the given target string.Since

3.0.0Arguments`[string='']` *(string)*: The string to inspect.`[target]` *(string)*: The string to search for.`[position=string.length]` *(number)*: The position to search up to.Returns

*(boolean)*: Returns `true` if `string` ends with `target`, else `false`.Example_.endsWith('abc', 'c'); _.endsWith('abc', 'b'); _.endsWith('abc', 'b', 2);

### `_.escape([string=''])`

source npm package

Converts the characters "&", "<", ">", '"', and "'" in `string` to their corresponding HTML entities. **Note:** No other characters are escaped. To escape additional characters use a third-party library like *he*. Though the ">" character is escaped for symmetry, characters like ">" and "/" don't need escaping in HTML and have no special meaning unless they're part of a tag or unquoted attribute value. See Mathias Bynens's article *(under "semi-related fun fact")* for more details. When working with HTML you should always quote attribute values to reduce XSS vectors.Since

0.1.0Arguments`[string='']` *(string)*: The string to escape.Returns

*(string)*: Returns the escaped string.Example_.escape('fred, barney, & pebbles');

### `_.escapeRegExp([string=''])`

source npm package

Escapes the `RegExp` special characters "^", "$", "", ".", "*", "+", "?", "(", ")", "[", "]", "{", "}", and "|" in `string`.Since

3.0.0Arguments`[string='']` *(string)*: The string to escape.Returns

*(string)*: Returns the escaped string.Example_.escapeRegExp('[lodash](https://lodash.com/)');

### `_.kebabCase([string=''])`

source npm package

Converts `string` to kebab case.Since

3.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the kebab cased string.Example_.kebabCase('Foo Bar'); _.kebabCase('fooBar'); _.kebabCase('__FOO_BAR__');

### `_.lowerCase([string=''])`

source npm package

Converts `string`, as space separated words, to lower case.Since

4.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the lower cased string.Example_.lowerCase('--Foo-Bar--'); _.lowerCase('fooBar'); _.lowerCase('__FOO_BAR__');

### `_.lowerFirst([string=''])`

source npm package

Converts the first character of `string` to lower case.Since

4.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the converted string.Example_.lowerFirst('Fred'); _.lowerFirst('FRED');

### `_.pad([string=''], [length=0], [chars=' '])`

source npm package

Pads `string` on the left and right sides if it's shorter than `length`. Padding characters are truncated if they can't be evenly divided by `length`.Since

3.0.0Arguments`[string='']` *(string)*: The string to pad.`[length=0]` *(number)*: The padding length.`[chars=' ']` *(string)*: The string used as padding.Returns

*(string)*: Returns the padded string.Example_.pad('abc', 8); _.pad('abc', 8, '_-'); _.pad('abc', 3);

### `_.padEnd([string=''], [length=0], [chars=' '])`

source npm package

Pads `string` on the right side if it's shorter than `length`. Padding characters are truncated if they exceed `length`.Since

4.0.0Arguments`[string='']` *(string)*: The string to pad.`[length=0]` *(number)*: The padding length.`[chars=' ']` *(string)*: The string used as padding.Returns

*(string)*: Returns the padded string.Example_.padEnd('abc', 6); _.padEnd('abc', 6, '_-'); _.padEnd('abc', 3);

### `_.padStart([string=''], [length=0], [chars=' '])`

source npm package

Pads `string` on the left side if it's shorter than `length`. Padding characters are truncated if they exceed `length`.Since

4.0.0Arguments`[string='']` *(string)*: The string to pad.`[length=0]` *(number)*: The padding length.`[chars=' ']` *(string)*: The string used as padding.Returns

*(string)*: Returns the padded string.Example_.padStart('abc', 6); _.padStart('abc', 6, '_-'); _.padStart('abc', 3);

### `_.parseInt(string, [radix=10])`

source npm package

Converts `string` to an integer of the specified radix. If `radix` is `undefined` or `0`, a `radix` of `10` is used unless `value` is a hexadecimal, in which case a `radix` of `16` is used. **Note:** This method aligns with the ES5 implementation of `parseInt`.Since

1.1.0Arguments`string` *(string)*: The string to convert.`[radix=10]` *(number)*: The radix to interpret `value` by.Returns

*(number)*: Returns the converted integer.Example_.parseInt('08'); _.map(['6', '08', '10'], _.parseInt);

### `_.repeat([string=''], [n=1])`

source npm package

Repeats the given string `n` times.Since

3.0.0Arguments`[string='']` *(string)*: The string to repeat.`[n=1]` *(number)*: The number of times to repeat the string.Returns

*(string)*: Returns the repeated string.Example_.repeat('*', 3); _.repeat('abc', 2); _.repeat('abc', 0);

### `_.replace([string=''], pattern, replacement)`

source npm package

Replaces matches for `pattern` in `string` with `replacement`. **Note:** This method is based on `String#replace`.Since

4.0.0Arguments`[string='']` *(string)*: The string to modify.`pattern` *(RegExp|string)*: The pattern to replace.`replacement` *(Function|string)*: The match replacement.Returns

*(string)*: Returns the modified string.Example_.replace('Hi Fred', 'Fred', 'Barney');

### `_.snakeCase([string=''])`

source npm package

Converts `string` to snake case.Since

3.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the snake cased string.Example_.snakeCase('Foo Bar'); _.snakeCase('fooBar'); _.snakeCase('--FOO-BAR--');

### `_.split([string=''], separator, [limit])`

source npm package

Splits `string` by `separator`. **Note:** This method is based on `String#split`.Since

4.0.0Arguments`[string='']` *(string)*: The string to split.`separator` *(RegExp|string)*: The separator pattern to split by.`[limit]` *(number)*: The length to truncate results to.Returns

*(Array)*: Returns the string segments.Example_.split('a-b-c', '-', 2);

### `_.startCase([string=''])`

source npm package

Converts `string` to start case.Since

3.1.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the start cased string.Example_.startCase('--foo-bar--'); _.startCase('fooBar'); _.startCase('__FOO_BAR__');

### `_.startsWith([string=''], [target], [position=0])`

source npm package

Checks if `string` starts with the given target string.Since

3.0.0Arguments`[string='']` *(string)*: The string to inspect.`[target]` *(string)*: The string to search for.`[position=0]` *(number)*: The position to search from.Returns

*(boolean)*: Returns `true` if `string` starts with `target`, else `false`.Example_.startsWith('abc', 'a'); _.startsWith('abc', 'b'); _.startsWith('abc', 'b', 1);

### `_.template([string=''], [options={}])`

source npm package

Creates a compiled template function that can interpolate data properties in "interpolate" delimiters, HTML-escape interpolated data properties in "escape" delimiters, and execute JavaScript in "evaluate" delimiters. Data properties may be accessed as free variables in the template. If a setting object is given, it takes precedence over `_.templateSettings` values. **Security:** `_.template` is insecure and should not be used. It will be removed in Lodash v5. Avoid untrusted input. See threat model. **Note:** In the development build `_.template` utilizes sourceURLs for easier debugging. For more information on precompiling templates see lodash's custom builds documentation. For more information on Chrome extension sandboxes see Chrome's extensions documentation.Since

0.1.0Arguments`[string='']` *(string)*: The template string.`[options={}]` *(Object)*: The options object.`[options.escape=_.templateSettings.escape]` *(RegExp)*: The HTML "escape" delimiter.`[options.evaluate=_.templateSettings.evaluate]` *(RegExp)*: The "evaluate" delimiter.`[options.imports=_.templateSettings.imports]` *(Object)*: An object to import into the template as free variables.`[options.interpolate=_.templateSettings.interpolate]` *(RegExp)*: The "interpolate" delimiter.`[options.sourceURL='lodash.templateSources[n]']` *(string)*: The sourceURL of the compiled template.`[options.variable='obj']` *(string)*: The data object variable name.Returns

*(Function)*: Returns the compiled template function.Examplevar compiled = _.template('hello <%= user %>!');compiled({ 'user': 'fred' }); var compiled = _.template('<b><%- value %></b>');compiled({ 'value': '<script>' }); var compiled = _.template('<% _.forEach(users, function(user) { %><li><%- user %></li><% }); %>');compiled({ 'users': ['fred', 'barney'] }); var compiled = _.template('<% print("hello " + user); %>!');compiled({ 'user': 'barney' }); var compiled = _.template('hello ${ user }!');compiled({ 'user': 'pebbles' }); var compiled = _.template('<%= "\\<%- value %\\>" %>');compiled({ 'value': 'ignored' }); var text = '<% jq.each(users, function(user) { %><li><%- user %></li><% }); %>';var compiled = _.template(text, { 'imports': { 'jq': jQuery } });compiled({ 'users': ['fred', 'barney'] }); var compiled = _.template('hello <%= user %>!', { 'sourceURL': '/basic/greeting.jst' });compiled(data); var compiled = _.template('hi <%= data.user %>!', { 'variable': 'data' });compiled.source; _.templateSettings.interpolate = /{{([\s\S]+?)}}/g;var compiled = _.template('hello {{ user }}!');compiled({ 'user': 'mustache' }); fs.writeFileSync(path.join(process.cwd(), 'jst.js'), '\  var JST = {\    "main": ' + _.template(mainText).source + '\  };\');

### `_.toLower([string=''])`

source npm package

Converts `string`, as a whole, to lower case just like String#toLowerCase.Since

4.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the lower cased string.Example_.toLower('--Foo-Bar--'); _.toLower('fooBar'); _.toLower('__FOO_BAR__');

### `_.toUpper([string=''])`

source npm package

Converts `string`, as a whole, to upper case just like String#toUpperCase.Since

4.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the upper cased string.Example_.toUpper('--foo-bar--'); _.toUpper('fooBar'); _.toUpper('__foo_bar__');

### `_.trim([string=''], [chars=whitespace])`

source npm package

Removes leading and trailing whitespace or specified characters from `string`.Since

3.0.0Arguments`[string='']` *(string)*: The string to trim.`[chars=whitespace]` *(string)*: The characters to trim.Returns

*(string)*: Returns the trimmed string.Example_.trim('  abc  '); _.trim('-_-abc-_-', '_-'); _.map(['  foo  ', '  bar  '], _.trim);

### `_.trimEnd([string=''], [chars=whitespace])`

source npm package

Removes trailing whitespace or specified characters from `string`.Since

4.0.0Arguments`[string='']` *(string)*: The string to trim.`[chars=whitespace]` *(string)*: The characters to trim.Returns

*(string)*: Returns the trimmed string.Example_.trimEnd('  abc  '); _.trimEnd('-_-abc-_-', '_-');

### `_.trimStart([string=''], [chars=whitespace])`

source npm package

Removes leading whitespace or specified characters from `string`.Since

4.0.0Arguments`[string='']` *(string)*: The string to trim.`[chars=whitespace]` *(string)*: The characters to trim.Returns

*(string)*: Returns the trimmed string.Example_.trimStart('  abc  '); _.trimStart('-_-abc-_-', '_-');

### `_.truncate([string=''], [options={}])`

source npm package

Truncates `string` if it's longer than the given maximum string length. The last characters of the truncated string are replaced with the omission string which defaults to "...".Since

4.0.0Arguments`[string='']` *(string)*: The string to truncate.`[options={}]` *(Object)*: The options object.`[options.length=30]` *(number)*: The maximum string length.`[options.omission='...']` *(string)*: The string to indicate text is omitted.`[options.separator]` *(RegExp|string)*: The separator pattern to truncate to.Returns

*(string)*: Returns the truncated string.Example_.truncate('hi-diddly-ho there, neighborino'); _.truncate('hi-diddly-ho there, neighborino', {  'length': 24,  'separator': ' '}); _.truncate('hi-diddly-ho there, neighborino', {  'length': 24,  'separator': /,? +/}); _.truncate('hi-diddly-ho there, neighborino', {  'omission': ' [...]'});

### `_.unescape([string=''])`

source npm package

The inverse of `_.escape`; this method converts the HTML entities `&amp;`, `&lt;`, `&gt;`, `&quot;`, and `&#39;` in `string` to their corresponding characters. **Note:** No other HTML entities are unescaped. To unescape additional HTML entities use a third-party library like *he*.Since

0.6.0Arguments`[string='']` *(string)*: The string to unescape.Returns

*(string)*: Returns the unescaped string.Example_.unescape('fred, barney, &amp; pebbles');

### `_.upperCase([string=''])`

source npm package

Converts `string`, as space separated words, to upper case.Since

4.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the upper cased string.Example_.upperCase('--foo-bar'); _.upperCase('fooBar'); _.upperCase('__foo_bar__');

### `_.upperFirst([string=''])`

source npm package

Converts the first character of `string` to upper case.Since

4.0.0Arguments`[string='']` *(string)*: The string to convert.Returns

*(string)*: Returns the converted string.Example_.upperFirst('fred'); _.upperFirst('FRED');

### `_.words([string=''], [pattern])`

source npm package

Splits `string` into an array of its words.Since

3.0.0Arguments`[string='']` *(string)*: The string to inspect.`[pattern]` *(RegExp|string)*: The pattern to match words.Returns

*(Array)*: Returns the words of `string`.Example_.words('fred, barney, & pebbles'); _.words('fred, barney, & pebbles', /[^, ]+/g);


## `“Util” Methods`

### `_.attempt(func, [args])`

source npm package

Attempts to invoke `func`, returning either the result or the caught error object. Any additional arguments are provided to `func` when it's invoked.Since

3.0.0Arguments`func` *(Function)*: The function to attempt.`[args]` *(...*)*: The arguments to invoke `func` with.Returns

*(*)*: Returns the `func` result or error object.Examplevar elements = _.attempt(function(selector) {  return document.querySelectorAll(selector);}, '>_>'); if (_.isError(elements)) {  elements = [];}

### `_.bindAll(object, methodNames)`

source npm package

Binds methods of an object to the object itself, overwriting the existing method. **Note:** This method doesn't set the "length" property of bound functions.Since

0.1.0Arguments`object` *(Object)*: The object to bind and assign the bound methods to.`methodNames` *(...(string|string[]))*: The object method names to bind.Returns

*(Object)*: Returns `object`.Examplevar view = {  'label': 'docs',  'click': function() {    console.log('clicked ' + this.label);  }}; _.bindAll(view, ['click']);jQuery(element).on('click', view.click);

### `_.cond(pairs)`

source npm package

Creates a function that iterates over `pairs` and invokes the corresponding function of the first predicate to return truthy. The predicate-function pairs are invoked with the `this` binding and arguments of the created function.Since

4.0.0Arguments`pairs` *(Array)*: The predicate-function pairs.Returns

*(Function)*: Returns the new composite function.Examplevar func = _.cond([  [_.matches({ 'a': 1 }),           _.constant('matches A')],  [_.conforms({ 'b': _.isNumber }), _.constant('matches B')],  [_.stubTrue,                      _.constant('no match')]]); func({ 'a': 1, 'b': 2 }); func({ 'a': 0, 'b': 1 }); func({ 'a': '1', 'b': '2' });

### `_.conforms(source)`

source npm package

Creates a function that invokes the predicate properties of `source` with the corresponding property values of a given object, returning `true` if all predicates return truthy, else `false`. **Note:** The created function is equivalent to `_.conformsTo` with `source` partially applied.Since

4.0.0Arguments`source` *(Object)*: The object of property predicates to conform to.Returns

*(Function)*: Returns the new spec function.Examplevar objects = [  { 'a': 2, 'b': 1 },  { 'a': 1, 'b': 2 }]; _.filter(objects, _.conforms({ 'b': function(n) { return n > 1; } }));

### `_.constant(value)`

source npm package

Creates a function that returns `value`.Since

2.4.0Arguments`value` *(*)*: The value to return from the new function.Returns

*(Function)*: Returns the new constant function.Examplevar objects = _.times(2, _.constant({ 'a': 1 })); console.log(objects); console.log(objects[0] === objects[1]);

### `_.defaultTo(value, defaultValue)`

source npm package

Checks `value` to determine whether a default value should be returned in its place. The `defaultValue` is returned if `value` is `NaN`, `null`, or `undefined`.Since

4.14.0Arguments`value` *(*)*: The value to check.`defaultValue` *(*)*: The default value.Returns

*(*)*: Returns the resolved value.Example_.defaultTo(1, 10); _.defaultTo(undefined, 10);

### `_.flow([funcs])`

source npm package

Creates a function that returns the result of invoking the given functions with the `this` binding of the created function, where each successive invocation is supplied the return value of the previous.Since

3.0.0Arguments`[funcs]` *(...(Function|Function[]))*: The functions to invoke.Returns

*(Function)*: Returns the new composite function.Examplefunction square(n) {  return n * n;} var addSquare = _.flow([_.add, square]);addSquare(1, 2);

### `_.flowRight([funcs])`

source npm package

This method is like `_.flow` except that it creates a function that invokes the given functions from right to left.Since

3.0.0Arguments`[funcs]` *(...(Function|Function[]))*: The functions to invoke.Returns

*(Function)*: Returns the new composite function.Examplefunction square(n) {  return n * n;} var addSquare = _.flowRight([square, _.add]);addSquare(1, 2);

### `_.identity(value)`

source npm package

This method returns the first argument it receives.Since

0.1.0Arguments`value` *(*)*: Any value.Returns

*(*)*: Returns `value`.Examplevar object = { 'a': 1 }; console.log(_.identity(object) === object);

### `_.iteratee([func=_.identity])`

source npm package

Creates a function that invokes `func` with the arguments of the created function. If `func` is a property name, the created function returns the property value for a given element. If `func` is an array or object, the created function returns `true` for elements that contain the equivalent source properties, otherwise it returns `false`.Since

4.0.0Arguments`[func=_.identity]` *(*)*: The value to convert to a callback.Returns

*(Function)*: Returns the callback.Examplevar users = [  { 'user': 'barney', 'age': 36, 'active': true },  { 'user': 'fred',   'age': 40, 'active': false }]; _.filter(users, _.iteratee({ 'user': 'barney', 'active': true })); _.filter(users, _.iteratee(['user', 'fred'])); _.map(users, _.iteratee('user')); _.iteratee = _.wrap(_.iteratee, function(iteratee, func) {  return !_.isRegExp(func) ? iteratee(func) : function(string) {    return func.test(string);  };}); _.filter(['abc', 'def'], /ef/);

### `_.matches(source)`

source npm package

Creates a function that performs a partial deep comparison between a given object and `source`, returning `true` if the given object has equivalent property values, else `false`. **Note:** The created function is equivalent to `_.isMatch` with `source` partially applied. Partial comparisons will match empty array and empty object `source` values against any array or object value, respectively. See `_.isEqual` for a list of supported value comparisons. **Note:** Multiple values can be checked by combining several matchers using `_.overSome`Since

3.0.0Arguments`source` *(Object)*: The object of property values to match.Returns

*(Function)*: Returns the new spec function.Examplevar objects = [  { 'a': 1, 'b': 2, 'c': 3 },  { 'a': 4, 'b': 5, 'c': 6 }]; _.filter(objects, _.matches({ 'a': 4, 'c': 6 })); _.filter(objects, _.overSome([_.matches({ 'a': 1 }), _.matches({ 'a': 4 })]));

### `_.matchesProperty(path, srcValue)`

source npm package

Creates a function that performs a partial deep comparison between the value at `path` of a given object to `srcValue`, returning `true` if the object value is equivalent, else `false`. **Note:** Partial comparisons will match empty array and empty object `srcValue` values against any array or object value, respectively. See `_.isEqual` for a list of supported value comparisons. **Note:** Multiple values can be checked by combining several matchers using `_.overSome`Since

3.2.0Arguments`path` *(Array|string)*: The path of the property to get.`srcValue` *(*)*: The value to match.Returns

*(Function)*: Returns the new spec function.Examplevar objects = [  { 'a': 1, 'b': 2, 'c': 3 },  { 'a': 4, 'b': 5, 'c': 6 }]; _.find(objects, _.matchesProperty('a', 4)); _.filter(objects, _.overSome([_.matchesProperty('a', 1), _.matchesProperty('a', 4)]));

### `_.method(path, [args])`

source npm package

Creates a function that invokes the method at `path` of a given object. Any additional arguments are provided to the invoked method.Since

3.7.0Arguments`path` *(Array|string)*: The path of the method to invoke.`[args]` *(...*)*: The arguments to invoke the method with.Returns

*(Function)*: Returns the new invoker function.Examplevar objects = [  { 'a': { 'b': _.constant(2) } },  { 'a': { 'b': _.constant(1) } }]; _.map(objects, _.method('a.b')); _.map(objects, _.method(['a', 'b']));

### `_.methodOf(object, [args])`

source npm package

The opposite of `_.method`; this method creates a function that invokes the method at a given path of `object`. Any additional arguments are provided to the invoked method.Since

3.7.0Arguments`object` *(Object)*: The object to query.`[args]` *(...*)*: The arguments to invoke the method with.Returns

*(Function)*: Returns the new invoker function.Examplevar array = _.times(3, _.constant),    object = { 'a': array, 'b': array, 'c': array }; _.map(['a[2]', 'c[0]'], _.methodOf(object)); _.map([['a', '2'], ['c', '0']], _.methodOf(object));

### `_.mixin([object=lodash], source, [options={}])`

source npm package

Adds all own enumerable string keyed function properties of a source object to the destination object. If `object` is a function, then methods are added to its prototype as well. **Note:** Use `_.runInContext` to create a pristine `lodash` function to avoid conflicts caused by modifying the original.Since

0.1.0Arguments`[object=lodash]` *(Function|Object)*: The destination object.`source` *(Object)*: The object of functions to add.`[options={}]` *(Object)*: The options object.`[options.chain=true]` *(boolean)*: Specify whether mixins are chainable.Returns

*(*)*: Returns `object`.Examplefunction vowels(string) {  return _.filter(string, function(v) {    return /[aeiou]/i.test(v);  });} _.mixin({ 'vowels': vowels });_.vowels('fred'); _('fred').vowels().value(); _.mixin({ 'vowels': vowels }, { 'chain': false });_('fred').vowels();

### `_.noConflict()`

source npm package

Reverts the `_` variable to its previous value and returns a reference to the `lodash` function.Since

0.1.0Returns

*(Function)*: Returns the `lodash` function.Examplevar lodash = _.noConflict();

### `_.noop()`

source npm package

This method returns `undefined`.Since

2.3.0Example_.times(2, _.noop);

### `_.nthArg([n=0])`

source npm package

Creates a function that gets the argument at index `n`. If `n` is negative, the nth argument from the end is returned.Since

4.0.0Arguments`[n=0]` *(number)*: The index of the argument to return.Returns

*(Function)*: Returns the new pass-thru function.Examplevar func = _.nthArg(1);func('a', 'b', 'c', 'd'); var func = _.nthArg(-2);func('a', 'b', 'c', 'd');

### `_.over([iteratees=[_.identity]])`

source npm package

Creates a function that invokes `iteratees` with the arguments it receives and returns their results.Since

4.0.0Arguments`[iteratees=[_.identity]]` *(...(Function|Function[]))*: The iteratees to invoke.Returns

*(Function)*: Returns the new function.Examplevar func = _.over([Math.max, Math.min]); func(1, 2, 3, 4);

### `_.overEvery([predicates=[_.identity]])`

source npm package

Creates a function that checks if **all** of the `predicates` return truthy when invoked with the arguments it receives. Following shorthands are possible for providing predicates. Pass an `Object` and it will be used as an parameter for `_.matches` to create the predicate. Pass an `Array` of parameters for `_.matchesProperty` and the predicate will be created using them.Since

4.0.0Arguments`[predicates=[_.identity]]` *(...(Function|Function[]))*: The predicates to check.Returns

*(Function)*: Returns the new function.Examplevar func = _.overEvery([Boolean, isFinite]); func('1'); func(null); func(NaN);

### `_.overSome([predicates=[_.identity]])`

source npm package

Creates a function that checks if **any** of the `predicates` return truthy when invoked with the arguments it receives. Following shorthands are possible for providing predicates. Pass an `Object` and it will be used as an parameter for `_.matches` to create the predicate. Pass an `Array` of parameters for `_.matchesProperty` and the predicate will be created using them.Since

4.0.0Arguments`[predicates=[_.identity]]` *(...(Function|Function[]))*: The predicates to check.Returns

*(Function)*: Returns the new function.Examplevar func = _.overSome([Boolean, isFinite]); func('1'); func(null); func(NaN); var matchesFunc = _.overSome([{ 'a': 1 }, { 'a': 2 }])var matchesPropertyFunc = _.overSome([['a', 1], ['a', 2]])

### `_.property(path)`

source npm package

Creates a function that returns the value at `path` of a given object.Since

2.4.0Arguments`path` *(Array|string)*: The path of the property to get.Returns

*(Function)*: Returns the new accessor function.Examplevar objects = [  { 'a': { 'b': 2 } },  { 'a': { 'b': 1 } }]; _.map(objects, _.property('a.b')); _.map(_.sortBy(objects, _.property(['a', 'b'])), 'a.b');

### `_.propertyOf(object)`

source npm package

The opposite of `_.property`; this method creates a function that returns the value at a given path of `object`.Since

3.0.0Arguments`object` *(Object)*: The object to query.Returns

*(Function)*: Returns the new accessor function.Examplevar array = [0, 1, 2],    object = { 'a': array, 'b': array, 'c': array }; _.map(['a[2]', 'c[0]'], _.propertyOf(object)); _.map([['a', '2'], ['c', '0']], _.propertyOf(object));

### `_.range([start=0], end, [step=1])`

source npm package

Creates an array of numbers *(positive and/or negative)* progressing from `start` up to, but not including, `end`. A step of `-1` is used if a negative `start` is specified without an `end` or `step`. If `end` is not specified, it's set to `start` with `start` then set to `0`. **Note:** JavaScript follows the IEEE-754 standard for resolving floating-point values which can produce unexpected results.Since

0.1.0Arguments`[start=0]` *(number)*: The start of the range.`end` *(number)*: The end of the range.`[step=1]` *(number)*: The value to increment or decrement by.Returns

*(Array)*: Returns the range of numbers.Example_.range(4); _.range(-4); _.range(1, 5); _.range(0, 20, 5); _.range(0, -4, -1); _.range(1, 4, 0); _.range(0);

### `_.rangeRight([start=0], end, [step=1])`

source npm package

This method is like `_.range` except that it populates values in descending order.Since

4.0.0Arguments`[start=0]` *(number)*: The start of the range.`end` *(number)*: The end of the range.`[step=1]` *(number)*: The value to increment or decrement by.Returns

*(Array)*: Returns the range of numbers.Example_.rangeRight(4); _.rangeRight(-4); _.rangeRight(1, 5); _.rangeRight(0, 20, 5); _.rangeRight(0, -4, -1); _.rangeRight(1, 4, 0); _.rangeRight(0);

### `_.runInContext([context=root])`

source npm package

Create a new pristine `lodash` function using the `context` object.Since

1.1.0Arguments`[context=root]` *(Object)*: The context object.Returns

*(Function)*: Returns a new `lodash` function.Example_.mixin({ 'foo': _.constant('foo') }); var lodash = _.runInContext();lodash.mixin({ 'bar': lodash.constant('bar') }); _.isFunction(_.foo);_.isFunction(_.bar); lodash.isFunction(lodash.foo);lodash.isFunction(lodash.bar); var defer = _.runInContext({ 'setTimeout': setImmediate }).defer;

### `_.stubArray()`

source npm package

This method returns a new empty array.Since

4.13.0Returns

*(Array)*: Returns the new empty array.Examplevar arrays = _.times(2, _.stubArray); console.log(arrays); console.log(arrays[0] === arrays[1]);

### `_.stubFalse()`

source npm package

This method returns `false`.Since

4.13.0Returns

*(boolean)*: Returns `false`.Example_.times(2, _.stubFalse);

### `_.stubObject()`

source npm package

This method returns a new empty object.Since

4.13.0Returns

*(Object)*: Returns the new empty object.Examplevar objects = _.times(2, _.stubObject); console.log(objects); console.log(objects[0] === objects[1]);

### `_.stubString()`

source npm package

This method returns an empty string.Since

4.13.0Returns

*(string)*: Returns the empty string.Example_.times(2, _.stubString);

### `_.stubTrue()`

source npm package

This method returns `true`.Since

4.13.0Returns

*(boolean)*: Returns `true`.Example_.times(2, _.stubTrue);

### `_.times(n, [iteratee=_.identity])`

source npm package

Invokes the iteratee `n` times, returning an array of the results of each invocation. The iteratee is invoked with one argument; *(index)*.Since

0.1.0Arguments`n` *(number)*: The number of times to invoke `iteratee`.`[iteratee=_.identity]` *(Function)*: The function invoked per iteration.Returns

*(Array)*: Returns the array of results.Example_.times(3, String);  _.times(4, _.constant(0));

### `_.toPath(value)`

source npm package

Converts `value` to a property path array.Since

4.0.0Arguments`value` *(*)*: The value to convert.Returns

*(Array)*: Returns the new property path array.Example_.toPath('a.b.c'); _.toPath('a[0].b.c');

### `_.uniqueId([prefix=''])`

source npm package

Generates a unique ID. If `prefix` is given, the ID is appended to it.Since

0.1.0Arguments`[prefix='']` *(string)*: The value to prefix the ID with.Returns

*(string)*: Returns the unique ID.Example_.uniqueId('contact_'); _.uniqueId();


## `Properties`

### `_.VERSION`

source

(string): The semantic version number.

### `_.templateSettings`

source npm package

(Object): By default, the template delimiters used by lodash are like those in embedded Ruby *(ERB)* as well as ES2015 template strings. Change the following template settings to use alternative delimiters. **Security:** See threat model — `_.template` is insecure and will be removed in v5.

### `_.templateSettings.escape`

source

(RegExp): Used to detect `data` property values to be HTML-escaped.

### `_.templateSettings.evaluate`

source

(RegExp): Used to detect code to be evaluated.

### `_.templateSettings.imports`

source

(Object): Used to import variables into the compiled template.

### `_.templateSettings.interpolate`

source

(RegExp): Used to detect `data` property values to inject.

### `_.templateSettings.variable`

source

(string): Used to reference the data object in the template text.


## `Methods`

### `_.templateSettings.imports._`

source

A reference to the `lodash` function.
