---
title: "Template Designer Documentation (part 2/2)"
source: https://jinja.palletsprojects.com/en/stable/templates/
domain: jinja2-templating
license: CC-BY-SA-4.0
tags: python jinja2, jinja2 template engine, template rendering python
fetched: 2026-07-02
part: 2/2
---

## List of Builtin Filters

| `abs()` | `forceescape()` | `map()` | `select()` | `unique()` |
|---|---|---|---|---|
| `attr()` | `format()` | `max()` | `selectattr()` | `upper()` |
| `batch()` | `groupby()` | `min()` | `slice()` | `urlencode()` |
| `capitalize()` | `indent()` | `pprint()` | `sort()` | `urlize()` |
| `center()` | `int()` | `random()` | `string()` | `wordcount()` |
| `default()` | `items()` | `reject()` | `striptags()` | `wordwrap()` |
| `dictsort()` | `join()` | `rejectattr()` | `sum()` | `xmlattr()` |
| `escape()` | `last()` | `replace()` | `title()` |   |
| `filesizeformat()` | `length()` | `reverse()` | `tojson()` |   |
| `first()` | `list()` | `round()` | `trim()` |   |
| `float()` | `lower()` | `safe()` | `truncate()` |   |

**jinja-filters.abs(*x*, */*)**

Return the absolute value of the argument.

**jinja-filters.attr(*obj: Any*, *name: str*) → jinja2.runtime.Undefined | Any**

Get an attribute of an object. `foo|attr("bar")` works like `foo.bar`, but returns undefined instead of falling back to `foo["bar"]` if the attribute doesn’t exist.

See Notes on subscriptions for more details.

**jinja-filters.batch(*value: 't.Iterable[V]'*, *linecount: int*, *fill_with: 't.Optional[V]' = None*) → 't.Iterator[t.List[V]]'**

A filter that batches items. It works pretty much like `slice` just the other way round. It returns a list of lists with the given number of items. If you provide a second parameter this is used to fill up missing items. See this example:

```html+jinja
<table>
{%- for row in items|batch(3, '&nbsp;') %}
  <tr>
  {%- for column in row %}
    <td>{{ column }}</td>
  {%- endfor %}
  </tr>
{%- endfor %}
</table>
```

**jinja-filters.capitalize(*s: str*) → str**

Capitalize a value. The first character will be uppercase, all others lowercase.

**jinja-filters.center(*value: str*, *width: int = 80*) → str**

Centers the value in a field of a given width.

**jinja-filters.default(*value: V*, *default_value: V = ''*, *boolean: bool = False*) → V**

If the value is undefined it will return the passed default value, otherwise the value of the variable:

```jinja
{{ my_variable|default('my_variable is not defined') }}
```

This will output the value of `my_variable` if the variable was defined, otherwise `'my_variable is not defined'`. If you want to use default with variables that evaluate to false you have to set the second parameter to `true`:

```jinja
{{ ''|default('the string was empty', true) }}
```

Changelog

Changed in version 2.11: It’s now possible to configure the `Environment` with `ChainableUndefined` to make the `default` filter work on nested elements and attributes that may contain undefined values in the chain without getting an `UndefinedError`.

**Aliases:**

`d`

**jinja-filters.dictsort(*value: Mapping[K, V]*, *case_sensitive: bool = False*, *by: 'te.Literal["key", "value"]' = 'key'*, *reverse: bool = False*) → List[Tuple[K, V]]**

Sort a dict and yield (key, value) pairs. Python dicts may not be in the order you want to display them in, so sort them first.

```jinja
{% for key, value in mydict|dictsort %}
    sort the dict by key, case insensitive

{% for key, value in mydict|dictsort(reverse=true) %}
    sort the dict by key, case insensitive, reverse order

{% for key, value in mydict|dictsort(true) %}
    sort the dict by key, case sensitive

{% for key, value in mydict|dictsort(false, 'value') %}
    sort the dict by value, case insensitive
```

**jinja-filters.escape(*s: 't.Any'*, */*) → 'Markup'**

Replace the characters `&`, `<`, `>`, `'`, and `"` in the string with HTML-safe sequences. Use this if you need to display text that might contain such characters in HTML.

If the object has an `__html__` method, it is called and the return value is assumed to already be safe for HTML.

**Parameters:**

**s** – An object to be converted to a string and escaped.

**Returns:**

A `Markup` string with the escaped text.

**Aliases:**

`e`

**jinja-filters.filesizeformat(*value: str | float | int*, *binary: bool = False*) → str**

Format the value like a ‘human-readable’ file size (i.e. 13 kB, 4.1 MB, 102 Bytes, etc). Per default decimal prefixes are used (Mega, Giga, etc.), if the second parameter is set to `True` the binary prefixes are used (Mebi, Gibi).

**jinja-filters.first(*seq: 't.Iterable[V]'*) → 't.Union[V, Undefined]'**

Return the first item of a sequence.

**jinja-filters.float(*value: Any*, *default: float = 0.0*) → float**

Convert the value into a floating point number. If the conversion doesn’t work it will return `0.0`. You can override this default using the first parameter.

**jinja-filters.forceescape(*value: 't.Union[str, HasHTML]'*) → markupsafe.Markup**

Enforce HTML escaping. This will probably double escape variables.

**jinja-filters.format(*value: str*, **args: Any*, ***kwargs: Any*) → str**

Apply the given values to a printf-style format string, like `string % values`.

```jinja
{{ "%s, %s!"|format(greeting, name) }}
Hello, World!
```

In most cases it should be more convenient and efficient to use the `%` operator or `str.format()`.

```
{{ "%s, %s!" % (greeting, name) }}
{{ "{}, {}!".format(greeting, name) }}
```

**jinja-filters.groupby(*value: 't.Iterable[V]'*, *attribute: str | int*, *default: Any | None = None*, *case_sensitive: bool = False*) → 't.List[_GroupTuple]'**

Group a sequence of objects by an attribute using Python’s `itertools.groupby()`. The attribute can use dot notation for nested access, like `"address.city"`. Unlike Python’s `groupby`, the values are sorted first so only one group is returned for each unique value.

For example, a list of `User` objects with a `city` attribute can be rendered in groups. In this example, `grouper` refers to the `city` value of the group.

```html+jinja
<ul>{% for city, items in users|groupby("city") %}
  <li>{{ city }}
    <ul>{% for user in items %}
      <li>{{ user.name }}
    {% endfor %}</ul>
  </li>
{% endfor %}</ul>
```

`groupby` yields namedtuples of `(grouper, list)`, which can be used instead of the tuple unpacking above. `grouper` is the value of the attribute, and `list` is the items with that value.

```html+jinja
<ul>{% for group in users|groupby("city") %}
  <li>{{ group.grouper }}: {{ group.list|join(", ") }}
{% endfor %}</ul>
```

You can specify a `default` value to use if an object in the list does not have the given attribute.

```jinja
<ul>{% for city, items in users|groupby("city", default="NY") %}
  <li>{{ city }}: {{ items|map(attribute="name")|join(", ") }}</li>
{% endfor %}</ul>
```

Like the `sort()` filter, sorting and grouping is case-insensitive by default. The `key` for each group will have the case of the first item in that group of values. For example, if a list of users has cities `["CA", "NY", "ca"]`, the “CA” group will have two values. This can be disabled by passing `case_sensitive=True`.

Changed in version 3.1: Added the `case_sensitive` parameter. Sorting and grouping is case-insensitive by default, matching other filters that do comparisons.

Changelog

Changed in version 3.0: Added the `default` parameter.

Changed in version 2.6: The attribute supports dot notation for nested access.

**jinja-filters.indent(*s: str*, *width: int | str = 4*, *first: bool = False*, *blank: bool = False*) → str**

Return a copy of the string with each line indented by 4 spaces. The first line and blank lines are not indented by default.

**Parameters:**

- **width** – Number of spaces, or a string, to indent by.
- **first** – Don’t skip indenting the first line.
- **blank** – Don’t skip indenting empty lines.

Changelog

Changed in version 3.0: `width` can be a string.

Changed in version 2.10: Blank lines are not indented by default.

Rename the `indentfirst` argument to `first`.

**jinja-filters.int(*value: Any*, *default: int = 0*, *base: int = 10*) → int**

Convert the value into an integer. If the conversion doesn’t work it will return `0`. You can override this default using the first parameter. You can also override the default base (10) in the second parameter, which handles input with prefixes such as 0b, 0o and 0x for bases 2, 8 and 16 respectively. The base is ignored for decimal numbers and non-string values.

**jinja-filters.items(*value: Mapping[K, V] | jinja2.runtime.Undefined*) → Iterator[Tuple[K, V]]**

Return an iterator over the `(key, value)` items of a mapping.

`x|items` is the same as `x.items()`, except if `x` is undefined an empty iterator is returned.

This filter is useful if you expect the template to be rendered with an implementation of Jinja in another programming language that does not have a `.items()` method on its mapping type.

```html+jinja
<dl>
{% for key, value in my_dict|items %}
    <dt>{{ key }}
    <dd>{{ value }}
{% endfor %}
</dl>
```

Added in version 3.1.

**jinja-filters.join(*value: Iterable[Any]*, *d: str = ''*, *attribute: str | int | NoneType = None*) → str**

Return a string which is the concatenation of the strings in the sequence. The separator between elements is an empty string per default, you can define it with the optional parameter:

```jinja
{{ [1, 2, 3]|join('|') }}
    -> 1|2|3

{{ [1, 2, 3]|join }}
    -> 123
```

It is also possible to join certain attributes of an object:

```jinja
{{ users|join(', ', attribute='username') }}
```

Changelog

Added in version 2.6: The `attribute` parameter was added.

**jinja-filters.last(*seq: 't.Reversible[V]'*) → 't.Union[V, Undefined]'**

Return the last item of a sequence.

Note: Does not work with generators. You may want to explicitly convert it to a list:

```jinja
{{ data | selectattr('name', '==', 'Jinja') | list | last }}
```

**jinja-filters.length(*obj*, */*)**

Return the number of items in a container.

**Aliases:**

`count`

**jinja-filters.list(*value: 't.Iterable[V]'*) → 't.List[V]'**

Convert the value into a list. If it was a string the returned list will be a list of characters.

**jinja-filters.lower(*s: str*) → str**

Convert a value to lowercase.

**jinja-filters.map(*value: Iterable[Any]*, **args: Any*, ***kwargs: Any*) → Iterable[Any]**

Applies a filter on a sequence of objects or looks up an attribute. This is useful when dealing with lists of objects but you are really only interested in a certain value of it.

The basic usage is mapping on an attribute. Imagine you have a list of users but you are only interested in a list of usernames:

```jinja
Users on this page: {{ users|map(attribute='username')|join(', ') }}
```

You can specify a `default` value to use if an object in the list does not have the given attribute.

```jinja
{{ users|map(attribute="username", default="Anonymous")|join(", ") }}
```

Alternatively you can let it invoke a filter by passing the name of the filter and the arguments afterwards. A good example would be applying a text conversion filter on a sequence:

```jinja
Users on this page: {{ titles|map('lower')|join(', ') }}
```

Similar to a generator comprehension such as:

```python
(u.username for u in users)
(getattr(u, "username", "Anonymous") for u in users)
(do_lower(x) for x in titles)
```

Changelog

Changed in version 2.11.0: Added the `default` parameter.

Added in version 2.7.

**jinja-filters.max(*value: 't.Iterable[V]'*, *case_sensitive: bool = False*, *attribute: str | int | NoneType = None*) → 't.Union[V, Undefined]'**

Return the largest item from the sequence.

```jinja
{{ [1, 2, 3]|max }}
    -> 3
```

**Parameters:**

- **case_sensitive** – Treat upper and lower case strings as distinct.
- **attribute** – Get the object with the max value of this attribute.

**jinja-filters.min(*value: 't.Iterable[V]'*, *case_sensitive: bool = False*, *attribute: str | int | NoneType = None*) → 't.Union[V, Undefined]'**

Return the smallest item from the sequence.

```jinja
{{ [1, 2, 3]|min }}
    -> 1
```

**Parameters:**

- **case_sensitive** – Treat upper and lower case strings as distinct.
- **attribute** – Get the object with the min value of this attribute.

**jinja-filters.pprint(*value: Any*) → str**

Pretty print a variable. Useful for debugging.

**jinja-filters.random(*seq: 't.Sequence[V]'*) → 't.Union[V, Undefined]'**

Return a random item from the sequence.

**jinja-filters.reject(*value: 't.Iterable[V]'*, **args: Any*, ***kwargs: Any*) → 't.Iterator[V]'**

Filters a sequence of objects by applying a test to each object, and rejecting the objects with the test succeeding.

If no test is specified, each object will be evaluated as a boolean.

Example usage:

```jinja
{{ numbers|reject("odd") }}
```

Similar to a generator comprehension such as:

```python
(n for n in numbers if not test_odd(n))
```

Changelog

Added in version 2.7.

**jinja-filters.rejectattr(*value: 't.Iterable[V]'*, **args: Any*, ***kwargs: Any*) → 't.Iterator[V]'**

Filters a sequence of objects by applying a test to the specified attribute of each object, and rejecting the objects with the test succeeding.

If no test is specified, the attribute’s value will be evaluated as a boolean.

```jinja
{{ users|rejectattr("is_active") }}
{{ users|rejectattr("email", "none") }}
```

Similar to a generator comprehension such as:

```python
(user for user in users if not user.is_active)
(user for user in users if not test_none(user.email))
```

Changelog

Added in version 2.7.

**jinja-filters.replace(*s: str*, *old: str*, *new: str*, *count: int | None = None*) → str**

Return a copy of the value with all occurrences of a substring replaced with a new one. The first argument is the substring that should be replaced, the second is the replacement string. If the optional third argument `count` is given, only the first `count` occurrences are replaced:

```jinja
{{ "Hello World"|replace("Hello", "Goodbye") }}
    -> Goodbye World

{{ "aaaaargh"|replace("a", "d'oh, ", 2) }}
    -> d'oh, d'oh, aaargh
```

**jinja-filters.reverse(*value: str | Iterable[V]*) → str | Iterable[V]**

Reverse the object or return an iterator that iterates over it the other way round.

**jinja-filters.round(*value: float*, *precision: int = 0*, *method: 'te.Literal["common", "ceil", "floor"]' = 'common'*) → float**

Round the number to a given precision. The first parameter specifies the precision (default is `0`), the second the rounding method:

- `'common'` rounds either up or down
- `'ceil'` always rounds up
- `'floor'` always rounds down

If you don’t specify a method `'common'` is used.

```jinja
{{ 42.55|round }}
    -> 43.0
{{ 42.55|round(1, 'floor') }}
    -> 42.5
```

Note that even if rounded to 0 precision, a float is returned. If you need a real integer, pipe it through `int`:

```jinja
{{ 42.55|round|int }}
    -> 43
```

**jinja-filters.safe(*value: str*) → markupsafe.Markup**

Mark the value as safe which means that in an environment with automatic escaping enabled this variable will not be escaped.

**jinja-filters.select(*value: 't.Iterable[V]'*, **args: Any*, ***kwargs: Any*) → 't.Iterator[V]'**

Filters a sequence of objects by applying a test to each object, and only selecting the objects with the test succeeding.

If no test is specified, each object will be evaluated as a boolean.

Example usage:

```jinja
{{ numbers|select("odd") }}
{{ numbers|select("odd") }}
{{ numbers|select("divisibleby", 3) }}
{{ numbers|select("lessthan", 42) }}
{{ strings|select("equalto", "mystring") }}
```

Similar to a generator comprehension such as:

```python
(n for n in numbers if test_odd(n))
(n for n in numbers if test_divisibleby(n, 3))
```

Changelog

Added in version 2.7.

**jinja-filters.selectattr(*value: 't.Iterable[V]'*, **args: Any*, ***kwargs: Any*) → 't.Iterator[V]'**

Filters a sequence of objects by applying a test to the specified attribute of each object, and only selecting the objects with the test succeeding.

If no test is specified, the attribute’s value will be evaluated as a boolean.

Example usage:

```jinja
{{ users|selectattr("is_active") }}
{{ users|selectattr("email", "none") }}
```

Similar to a generator comprehension such as:

```python
(user for user in users if user.is_active)
(user for user in users if test_none(user.email))
```

Changelog

Added in version 2.7.

**jinja-filters.slice(*value: 't.Collection[V]'*, *slices: int*, *fill_with: 't.Optional[V]' = None*) → 't.Iterator[t.List[V]]'**

Slice an iterator and return a list of lists containing those items. Useful if you want to create a div containing three ul tags that represent columns:

```html+jinja
<div class="columnwrapper">
  {%- for column in items|slice(3) %}
    <ul class="column-{{ loop.index }}">
    {%- for item in column %}
      <li>{{ item }}</li>
    {%- endfor %}
    </ul>
  {%- endfor %}
</div>
```

If you pass it a second argument it’s used to fill missing values on the last iteration.

**jinja-filters.sort(*value: 't.Iterable[V]'*, *reverse: bool = False*, *case_sensitive: bool = False*, *attribute: str | int | NoneType = None*) → 't.List[V]'**

Sort an iterable using Python’s `sorted()`.

```jinja
{% for city in cities|sort %}
    ...
{% endfor %}
```

**Parameters:**

- **reverse** – Sort descending instead of ascending.
- **case_sensitive** – When sorting strings, sort upper and lower case separately.
- **attribute** – When sorting objects or dicts, an attribute or key to sort by. Can use dot notation like `"address.city"`. Can be a list of attributes like `"age,name"`.

The sort is stable, it does not change the relative order of elements that compare equal. This makes it is possible to chain sorts on different attributes and ordering.

```jinja
{% for user in users|sort(attribute="name")
    |sort(reverse=true, attribute="age") %}
    ...
{% endfor %}
```

As a shortcut to chaining when the direction is the same for all attributes, pass a comma separate list of attributes.

```jinja
{% for user in users|sort(attribute="age,name") %}
    ...
{% endfor %}
```

Changelog

Changed in version 2.11.0: The `attribute` parameter can be a comma separated list of attributes, e.g. `"age,name"`.

Changed in version 2.6: The `attribute` parameter was added.

**jinja-filters.string(*s: 't.Any'*, */*) → 'str'**

Convert an object to a string if it isn’t already. This preserves a `Markup` string rather than converting it back to a basic string, so it will still be marked as safe and won’t be escaped again.

```
>>> value = escape("<User 1>")
>>> value
Markup('&lt;User 1&gt;')
>>> escape(str(value))
Markup('&amp;lt;User 1&amp;gt;')
>>> escape(soft_str(value))
Markup('&lt;User 1&gt;')
```

**jinja-filters.striptags(*value: 't.Union[str, HasHTML]'*) → str**

Strip SGML/XML tags and replace adjacent whitespace by one space.

**jinja-filters.sum(*iterable: 't.Iterable[V]'*, *attribute: str | int | NoneType = None*, *start: V = 0*) → V**

Returns the sum of a sequence of numbers plus the value of parameter ‘start’ (which defaults to 0). When the sequence is empty it returns start.

It is also possible to sum up only certain attributes:

```jinja
Total: {{ items|sum(attribute='price') }}
```

Changelog

Changed in version 2.6: The `attribute` parameter was added to allow summing up over attributes. Also the `start` parameter was moved on to the right.

**jinja-filters.title(*s: str*) → str**

Return a titlecased version of the value. I.e. words will start with uppercase letters, all remaining characters are lowercase.

**jinja-filters.tojson(*value: Any*, *indent: int | None = None*) → markupsafe.Markup**

Serialize an object to a string of JSON, and mark it safe to render in HTML. This filter is only for use in HTML documents.

The returned string is safe to render in HTML documents and `<script>` tags. The exception is in HTML attributes that are double quoted; either use single quotes or the `|forceescape` filter.

**Parameters:**

- **value** – The object to serialize to JSON.
- **indent** – The `indent` parameter passed to `dumps`, for pretty-printing the value.

Changelog

Added in version 2.9.

**jinja-filters.trim(*value: str*, *chars: str | None = None*) → str**

Strip leading and trailing characters, by default whitespace.

**jinja-filters.truncate(*s: str*, *length: int = 255*, *killwords: bool = False*, *end: str = '...'*, *leeway: int | None = None*) → str**

Return a truncated copy of the string. The length is specified with the first parameter which defaults to `255`. If the second parameter is `true` the filter will cut the text at length. Otherwise it will discard the last word. If the text was in fact truncated it will append an ellipsis sign (`"..."`). If you want a different ellipsis sign than `"..."` you can specify it using the third parameter. Strings that only exceed the length by the tolerance margin given in the fourth parameter will not be truncated.

```jinja
{{ "foo bar baz qux"|truncate(9) }}
    -> "foo..."
{{ "foo bar baz qux"|truncate(9, True) }}
    -> "foo ba..."
{{ "foo bar baz qux"|truncate(11) }}
    -> "foo bar baz qux"
{{ "foo bar baz qux"|truncate(11, False, '...', 0) }}
    -> "foo bar..."
```

The default leeway on newer Jinja versions is 5 and was 0 before but can be reconfigured globally.

**jinja-filters.unique(*value: 't.Iterable[V]'*, *case_sensitive: bool = False*, *attribute: str | int | NoneType = None*) → 't.Iterator[V]'**

Returns a list of unique items from the given iterable.

```jinja
{{ ['foo', 'bar', 'foobar', 'FooBar']|unique|list }}
    -> ['foo', 'bar', 'foobar']
```

The unique items are yielded in the same order as their first occurrence in the iterable passed to the filter.

**Parameters:**

- **case_sensitive** – Treat upper and lower case strings as distinct.
- **attribute** – Filter objects with unique values for this attribute.

**jinja-filters.upper(*s: str*) → str**

Convert a value to uppercase.

**jinja-filters.urlencode(*value: str | Mapping[str, Any] | Iterable[Tuple[str, Any]]*) → str**

Quote data for use in a URL path or query using UTF-8.

Basic wrapper around `urllib.parse.quote()` when given a string, or `urllib.parse.urlencode()` for a dict or iterable.

**Parameters:**

**value** – Data to quote. A string will be quoted directly. A dict or iterable of `(key, value)` pairs will be joined as a query string.

When given a string, “/” is not quoted. HTTP servers treat “/” and “%2F” equivalently in paths. If you need quoted slashes, use the `|replace("/", "%2F")` filter.

Changelog

Added in version 2.7.

**jinja-filters.urlize(*value: str*, *trim_url_limit: int | None = None*, *nofollow: bool = False*, *target: str | None = None*, *rel: str | None = None*, *extra_schemes: Iterable[str] | None = None*) → str**

Convert URLs in text into clickable links.

This may not recognize links in some situations. Usually, a more comprehensive formatter, such as a Markdown library, is a better choice.

Works on `http://`, `https://`, `www.`, `mailto:`, and email addresses. Links with trailing punctuation (periods, commas, closing parentheses) and leading punctuation (opening parentheses) are recognized excluding the punctuation. Email addresses that include header fields are not recognized (for example, `mailto:address@example.com?cc=copy@example.com`).

**Parameters:**

- **value** – Original text containing URLs to link.
- **trim_url_limit** – Shorten displayed URL values to this length.
- **nofollow** – Add the `rel=nofollow` attribute to links.
- **target** – Add the `target` attribute to links.
- **rel** – Add the `rel` attribute to links.
- **extra_schemes** – Recognize URLs that start with these schemes in addition to the default behavior. Defaults to `env.policies["urlize.extra_schemes"]`, which defaults to no extra schemes.

Changelog

Changed in version 3.0: The `extra_schemes` parameter was added.

Changed in version 3.0: Generate `https://` links for URLs without a scheme.

Changed in version 3.0: The parsing rules were updated. Recognize email addresses with or without the `mailto:` scheme. Validate IP addresses. Ignore parentheses and brackets in more cases.

Changed in version 2.8: The `target` parameter was added.

**jinja-filters.wordcount(*s: str*) → int**

Count the words in that string.

**jinja-filters.wordwrap(*s: str*, *width: int = 79*, *break_long_words: bool = True*, *wrapstring: str | None = None*, *break_on_hyphens: bool = True*) → str**

Wrap a string to the given width. Existing newlines are treated as paragraphs to be wrapped separately.

**Parameters:**

- **s** – Original text to wrap.
- **width** – Maximum length of wrapped lines.
- **break_long_words** – If a word is longer than `width`, break it across lines.
- **break_on_hyphens** – If a word contains hyphens, it may be split across lines.
- **wrapstring** – String to join each wrapped line. Defaults to `Environment.newline_sequence`.

Changelog

Changed in version 2.11: Existing newlines are treated as paragraphs wrapped separately.

Changed in version 2.11: Added the `break_on_hyphens` parameter.

Changed in version 2.7: Added the `wrapstring` parameter.

**jinja-filters.xmlattr(*d: Mapping[str, Any]*, *autospace: bool = True*) → str**

Create an SGML/XML attribute string based on the items in a dict.

**Values** that are neither `none` nor `undefined` are automatically escaped, safely allowing untrusted user input.

User input should not be used as **keys** to this filter. If any key contains a space, `/` solidus, `>` greater-than sign, or `=` equals sign, this fails with a `ValueError`. Regardless of this, user input should never be used as keys to this filter, or must be separately validated first.

```html+jinja
<ul{{ {'class': 'my_list', 'missing': none,
        'id': 'list-%d'|format(variable)}|xmlattr }}>
...
</ul>
```

Results in something like this:

```html
<ul class="my_list" id="list-42">
...
</ul>
```

As you can see it automatically prepends a space in front of the item if the filter returned something unless the second parameter is false.

Changed in version 3.1.4: Keys with `/` solidus, `>` greater-than sign, or `=` equals sign are not allowed.

Changed in version 3.1.3: Keys with spaces are not allowed.


## List of Builtin Tests

| `boolean()` | `even()` | `in()` | `mapping()` | `sequence()` |
|---|---|---|---|---|
| `callable()` | `false()` | `integer()` | `ne()` | `string()` |
| `defined()` | `filter()` | `iterable()` | `none()` | `test()` |
| `divisibleby()` | `float()` | `le()` | `number()` | `true()` |
| `eq()` | `ge()` | `lower()` | `odd()` | `undefined()` |
| `escaped()` | `gt()` | `lt()` | `sameas()` | `upper()` |

**jinja-tests.boolean(*value: Any*) → bool**

Return true if the object is a boolean value.

Changelog

Added in version 2.11.

**jinja-tests.callable(*obj*, */*)**

Return whether the object is callable (i.e., some kind of function).

Note that classes are callable, as are instances of classes with a __call__() method.

**jinja-tests.defined(*value: Any*) → bool**

Return true if the variable is defined:

```jinja
{% if variable is defined %}
    value of variable: {{ variable }}
{% else %}
    variable is not defined
{% endif %}
```

See the `default()` filter for a simple way to set undefined variables.

**jinja-tests.divisibleby(*value: int*, *num: int*) → bool**

Check if a variable is divisible by a number.

**jinja-tests.eq(*a*, *b*, */*)**

Same as a == b.

**Aliases:**

`==`, `equalto`

**jinja-tests.escaped(*value: Any*) → bool**

Check if the value is escaped.

**jinja-tests.even(*value: int*) → bool**

Return true if the variable is even.

**jinja-tests.false(*value: Any*) → bool**

Return true if the object is False.

Changelog

Added in version 2.11.

**jinja-tests.filter(*value: str*) → bool**

Check if a filter exists by name. Useful if a filter may be optionally available.

```jinja
{% if 'markdown' is filter %}
    {{ value | markdown }}
{% else %}
    {{ value }}
{% endif %}
```

Changelog

Added in version 3.0.

**jinja-tests.float(*value: Any*) → bool**

Return true if the object is a float.

Changelog

Added in version 2.11.

**jinja-tests.ge(*a*, *b*, */*)**

Same as a >= b.

**Aliases:**

`>=`

**jinja-tests.gt(*a*, *b*, */*)**

Same as a > b.

**Aliases:**

`>`, `greaterthan`

**jinja-tests.in(*value: Any*, *seq: Container[Any]*) → bool**

Check if value is in seq.

Changelog

Added in version 2.10.

**jinja-tests.integer(*value: Any*) → bool**

Return true if the object is an integer.

Changelog

Added in version 2.11.

**jinja-tests.iterable(*value: Any*) → bool**

Check if it’s possible to iterate over an object.

**jinja-tests.le(*a*, *b*, */*)**

Same as a <= b.

**Aliases:**

`<=`

**jinja-tests.lower(*value: str*) → bool**

Return true if the variable is lowercased.

**jinja-tests.lt(*a*, *b*, */*)**

Same as a < b.

**Aliases:**

`<`, `lessthan`

**jinja-tests.mapping(*value: Any*) → bool**

Return true if the object is a mapping (dict etc.).

Changelog

Added in version 2.6.

**jinja-tests.ne(*a*, *b*, */*)**

Same as a != b.

**Aliases:**

`!=`

**jinja-tests.none(*value: Any*) → bool**

Return true if the variable is none.

**jinja-tests.number(*value: Any*) → bool**

Return true if the variable is a number.

**jinja-tests.odd(*value: int*) → bool**

Return true if the variable is odd.

**jinja-tests.sameas(*value: Any*, *other: Any*) → bool**

Check if an object points to the same memory address than another object:

```jinja
{% if foo.attribute is sameas false %}
    the foo attribute really is the `False` singleton
{% endif %}
```

**jinja-tests.sequence(*value: Any*) → bool**

Return true if the variable is a sequence. Sequences are variables that are iterable.

**jinja-tests.string(*value: Any*) → bool**

Return true if the object is a string.

**jinja-tests.test(*value: str*) → bool**

Check if a test exists by name. Useful if a test may be optionally available.

```jinja
{% if 'loud' is test %}
    {% if value is loud %}
        {{ value|upper }}
    {% else %}
        {{ value|lower }}
    {% endif %}
{% else %}
    {{ value }}
{% endif %}
```

Changelog

Added in version 3.0.

**jinja-tests.true(*value: Any*) → bool**

Return true if the object is True.

Changelog

Added in version 2.11.

**jinja-tests.undefined(*value: Any*) → bool**

Like `defined()` but the other way round.

**jinja-tests.upper(*value: str*) → bool**

Return true if the variable is uppercased.


## List of Global Functions

The following functions are available in the global scope by default:

**jinja-globals.range([*start*, ]*stop*[, *step*])**

Return a list containing an arithmetic progression of integers. `range(i, j)` returns `[i, i+1, i+2, ..., j-1]`; start (!) defaults to `0`. When step is given, it specifies the increment (or decrement). For example, `range(4)` and `range(0, 4, 1)` return `[0, 1, 2, 3]`. The end point is omitted! These are exactly the valid indices for a list of 4 elements.

This is useful to repeat a template block multiple times, e.g. to fill a list. Imagine you have 7 users in the list but you want to render three empty items to enforce a height with CSS:

```html+jinja
<ul>
{% for user in users %}
    <li>{{ user.username }}</li>
{% endfor %}
{% for number in range(10 - users|count) %}
    <li class="empty"><span>...</span></li>
{% endfor %}
</ul>
```

**jinja-globals.lipsum(*n=5*, *html=True*, *min=20*, *max=100*)**

Generates some lorem ipsum for the template. By default, five paragraphs of HTML are generated with each paragraph between 20 and 100 words. If html is False, regular text is returned. This is useful to generate simple contents for layout testing.

**jinja-globals.dict(*\**items*)**

A convenient alternative to dict literals. `{'foo': 'bar'}` is the same as `dict(foo='bar')`.

***class*jinja-globals.cycler(*\*items*)**

Cycle through values by yielding them one at a time, then restarting once the end is reached.

Similar to `loop.cycle`, but can be used outside loops or across multiple loops. For example, render a list of folders and files in a list, alternating giving them “odd” and “even” classes.

```html+jinja
{% set row_class = cycler("odd", "even") %}
<ul class="browser">
{% for folder in folders %}
  <li class="folder {{ row_class.next() }}">{{ folder }}
{% endfor %}
{% for file in files %}
  <li class="file {{ row_class.next() }}">{{ file }}
{% endfor %}
</ul>
```

**Parameters:**

**items** – Each positional argument will be yielded in the order given for each cycle.

Changelog

Added in version 2.1.

***property*current**

Return the current item. Equivalent to the item that will be returned next time `next()` is called.

**next()**

Return the current item, then advance `current` to the next item.

**reset()**

Resets the current item to the first item.

***class*jinja-globals.joiner(*sep=', '*)**

A tiny helper that can be used to “join” multiple sections. A joiner is passed a string and will return that string every time it’s called, except the first time (in which case it returns an empty string). You can use this to join things:

```html+jinja
{% set pipe = joiner("|") %}
{% if categories %} {{ pipe() }}
    Categories: {{ categories|join(", ") }}
{% endif %}
{% if author %} {{ pipe() }}
    Author: {{ author() }}
{% endif %}
{% if can_edit %} {{ pipe() }}
    <a href="?action=edit">Edit</a>
{% endif %}
```

Changelog

Added in version 2.1.

***class*jinja-globals.namespace(*...*)**

Creates a new container that allows attribute assignment using the `{% set %}` tag:

```html+jinja
{% set ns = namespace() %}
{% set ns.foo = 'bar' %}
```

The main purpose of this is to allow carrying a value from within a loop body to an outer scope. Initial values can be provided as a dict, as keyword arguments, or both (same behavior as Python’s `dict` constructor):

```html+jinja
{% set ns = namespace(found=false) %}
{% for item in items %}
    {% if item.check_something() %}
        {% set ns.found = true %}
    {% endif %}
    * {{ item.title }}
{% endfor %}
Found item having something: {{ ns.found }}
```

Changed in version 3.2: Namespace attributes can be assigned to in multiple assignment.

Changelog

Added in version 2.10.


## Extensions

The following sections cover the built-in Jinja extensions that may be enabled by an application. An application could also provide further extensions not covered by this documentation; in which case there should be a separate document explaining said extensions.

### i18n

If the i18n Extension is enabled, it’s possible to mark text in the template as translatable. To mark a section as translatable, use a `trans` block:

```jinja
{% trans %}Hello, {{ user }}!{% endtrans %}
```

Inside the block, no statements are allowed, only text and simple variable tags.

Variable tags can only be a name, not attribute access, filters, or other expressions. To use an expression, bind it to a name in the `trans` tag for use in the block.

```jinja
{% trans user=user.username %}Hello, {{ user }}!{% endtrans %}
```

To bind more than one expression, separate each with a comma (`,`).

```jinja
{% trans book_title=book.title, author=author.name %}
This is {{ book_title }} by {{ author }}
{% endtrans %}
```

To pluralize, specify both the singular and plural forms separated by the `pluralize` tag.

```jinja
{% trans count=list|length %}
There is {{ count }} {{ name }} object.
{% pluralize %}
There are {{ count }} {{ name }} objects.
{% endtrans %}
```

By default, the first variable in a block is used to determine whether to use singular or plural form. If that isn’t correct, specify the variable used for pluralizing as a parameter to `pluralize`.

```jinja
{% trans ..., user_count=users|length %}...
{% pluralize user_count %}...{% endtrans %}
```

When translating blocks of text, whitespace and linebreaks result in hard to read and error-prone translation strings. To avoid this, a trans block can be marked as trimmed, which will replace all linebreaks and the whitespace surrounding them with a single space and remove leading and trailing whitespace.

```jinja
{% trans trimmed book_title=book.title %}
    This is {{ book_title }}.
    You should read it!
{% endtrans %}
```

This results in `This is %(book_title)s. You should read it!` in the translation file.

If trimming is enabled globally, the `notrimmed` modifier can be used to disable it for a block.

Changelog

Added in version 2.10: The `trimmed` and `notrimmed` modifiers have been added.

If the translation depends on the context that the message appears in, the `pgettext` and `npgettext` functions take a `context` string as the first argument, which is used to select the appropriate translation. To specify a context with the `{% trans %}` tag, provide a string as the first token after `trans`.

```jinja
{% trans "fruit" %}apple{% endtrans %}
{% trans "fruit" trimmed count -%}
    1 apple
{%- pluralize -%}
    {{ count }} apples
{%- endtrans %}
```

Added in version 3.1: A context can be passed to the `trans` tag to use `pgettext` and `npgettext`.

It’s possible to translate strings in expressions with these functions:

- `_(message)`: Alias for `gettext`.
- `gettext(message)`: Translate a message.
- `ngettext(singular, plural, n)`: Translate a singular or plural message based on a count variable.
- `pgettext(context, message)`: Like `gettext()`, but picks the translation based on the context string.
- `npgettext(context, singular, plural, n)`: Like `npgettext()`, but picks the translation based on the context string.

You can print a translated string like this:

```jinja
{{ _("Hello, World!") }}
```

To use placeholders, use the `format` filter.

```jinja
{{ _("Hello, %(user)s!")|format(user=user.username) }}
```

Always use keyword arguments to `format`, as other languages may not use the words in the same order.

If New Style Gettext calls are activated, using placeholders is easier. Formatting is part of the `gettext` call instead of using the `format` filter.

```jinja
{{ gettext('Hello World!') }}
{{ gettext('Hello %(name)s!', name='World') }}
{{ ngettext('%(num)d apple', '%(num)d apples', apples|count) }}
```

The `ngettext` function’s format string automatically receives the count as a `num` parameter in addition to the given parameters.

### Expression Statement

If the expression-statement extension is loaded, a tag called `do` is available that works exactly like the regular variable expression (`{{ ... }}`); except it doesn’t print anything. This can be used to modify lists:

```html+jinja
{% do navigation.append('a string') %}
```

### Loop Controls

If the application enables the Loop Controls, it’s possible to use `break` and `continue` in loops. When `break` is reached, the loop is terminated; if `continue` is reached, the processing is stopped and continues with the next iteration.

Here’s a loop that skips every second item:

```html+jinja
{% for user in users %}
    {%- if loop.index is even %}{% continue %}{% endif %}
    ...
{% endfor %}
```

Likewise, a loop that stops processing after the 10th iteration:

```html+jinja
{% for user in users %}
    {%- if loop.index >= 10 %}{% break %}{% endif %}
{%- endfor %}
```

Note that `loop.index` starts with 1, and `loop.index0` starts with 0 (See: For).

### Debug Statement

If the Debug Extension is enabled, a `{% debug %}` tag will be available to dump the current context as well as the available filters and tests. This is useful to see what’s available to use in the template without setting up a debugger.

```html+jinja
<pre>{% debug %}</pre>
```

```
{'context': {'cycler': <class 'jinja2.utils.Cycler'>,
             ...,
             'namespace': <class 'jinja2.utils.Namespace'>},
 'filters': ['abs', 'attr', 'batch', 'capitalize', 'center', 'count', 'd',
             ..., 'urlencode', 'urlize', 'wordcount', 'wordwrap', 'xmlattr'],
 'tests': ['!=', '<', '<=', '==', '>', '>=', 'callable', 'defined',
           ..., 'odd', 'sameas', 'sequence', 'string', 'undefined', 'upper']}
```

### With Statement

Changelog

Added in version 2.3.

The with statement makes it possible to create a new inner scope. Variables set within this scope are not visible outside of the scope.

With in a nutshell:

```html+jinja
{% with %}
    {% set foo = 42 %}
    {{ foo }}           foo is 42 here
{% endwith %}
foo is not visible here any longer
```

Because it is common to set variables at the beginning of the scope, you can do that within the `with` statement. The following two examples are equivalent:

```html+jinja
{% with foo = 42 %}
    {{ foo }}
{% endwith %}

{% with %}
    {% set foo = 42 %}
    {{ foo }}
{% endwith %}
```

An important note on scoping here. In Jinja versions before 2.9 the behavior of referencing one variable to another had some unintended consequences. In particular one variable could refer to another defined in the same with block’s opening statement. This caused issues with the cleaned up scoping behavior and has since been improved. In particular in newer Jinja versions the following code always refers to the variable `a` from outside the `with` block:

```html+jinja
{% with a={}, b=a.attribute %}...{% endwith %}
```

In earlier Jinja versions the `b` attribute would refer to the results of the first attribute. If you depend on this behavior you can rewrite it to use the `set` tag:

```html+jinja
{% with a={} %}
    {% set b = a.attribute %}
{% endwith %}
```

Extension

In older versions of Jinja (before 2.9) it was required to enable this feature with an extension. It’s now enabled by default.


## Autoescape Overrides

Changelog

Added in version 2.4.

If you want you can activate and deactivate the autoescaping from within the templates.

Example:

```html+jinja
{% autoescape true %}
    Autoescaping is active within this block
{% endautoescape %}

{% autoescape false %}
    Autoescaping is inactive within this block
{% endautoescape %}
```

After an `endautoescape` the behavior is reverted to what it was before.

Extension

In older versions of Jinja (before 2.9) it was required to enable this feature with an extension. It’s now enabled by default.
