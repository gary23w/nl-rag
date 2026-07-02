---
title: "Built-in Types (part 4/5)"
source: https://docs.python.org/3/library/stdtypes.html
domain: python
license: PSF-2.0
tags: python, pytest, cpython, pip
fetched: 2026-07-02
part: 4/5
---

# Built-in Types

Split the binary sequence into subsequences of the same type, using *sep* as the delimiter string. If *maxsplit* is given, at most *maxsplit* splits are done, the *rightmost* ones. If *sep* is not specified or `None`, any subsequence consisting solely of ASCII whitespace is a separator. Except for splitting from the right, `rsplit()` behaves like `split()` which is described in detail below.

**bytes.rstrip(*bytes=None*, */*)**

**bytearray.rstrip(*bytes=None*, */*)**

Return a copy of the sequence with specified trailing bytes removed. The *bytes* argument is a binary sequence specifying the set of byte values to be removed. If omitted or `None`, the *bytes* argument defaults to removing ASCII whitespace. The *bytes* argument is not a suffix; rather, all combinations of its values are stripped:

```python3
>>> b'   spacious   '.rstrip()
b'   spacious'
>>> b'mississippi'.rstrip(b'ipz')
b'mississ'
```

The binary sequence of byte values to remove may be any bytes-like object. See `removesuffix()` for a method that will remove a single suffix string rather than all of a set of characters. For example:

```python3
>>> b'Monty Python'.rstrip(b' Python')
b'M'
>>> b'Monty Python'.removesuffix(b' Python')
b'Monty'
```

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.split(*sep=None*, *maxsplit=-1*)**

**bytearray.split(*sep=None*, *maxsplit=-1*)**

Split the binary sequence into subsequences of the same type, using *sep* as the delimiter string. If *maxsplit* is given and non-negative, at most *maxsplit* splits are done (thus, the list will have at most `maxsplit+1` elements). If *maxsplit* is not specified or is `-1`, then there is no limit on the number of splits (all possible splits are made).

If *sep* is given, consecutive delimiters are not grouped together and are deemed to delimit empty subsequences (for example, `b'1,,2'.split(b',')` returns `[b'1', b'', b'2']`). The *sep* argument may consist of a multibyte sequence as a single delimiter. Splitting an empty sequence with a specified separator returns `[b'']` or `[bytearray(b'')]` depending on the type of object being split. The *sep* argument may be any bytes-like object.

For example:

```python3
>>> b'1,2,3'.split(b',')
[b'1', b'2', b'3']
>>> b'1,2,3'.split(b',', maxsplit=1)
[b'1', b'2,3']
>>> b'1,2,,3,'.split(b',')
[b'1', b'2', b'', b'3', b'']
>>> b'1<>2<>3<4'.split(b'<>')
[b'1', b'2', b'3<4']
```

If *sep* is not specified or is `None`, a different splitting algorithm is applied: runs of consecutive ASCII whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the sequence has leading or trailing whitespace. Consequently, splitting an empty sequence or a sequence consisting solely of ASCII whitespace without a specified separator returns `[]`.

For example:

```python3
>>> b'1 2 3'.split()
[b'1', b'2', b'3']
>>> b'1 2 3'.split(maxsplit=1)
[b'1', b'2 3']
>>> b'   1   2   3   '.split()
[b'1', b'2', b'3']
```

**bytes.strip(*bytes=None*, */*)**

**bytearray.strip(*bytes=None*, */*)**

Return a copy of the sequence with specified leading and trailing bytes removed. The *bytes* argument is a binary sequence specifying the set of byte values to be removed. If omitted or `None`, the *bytes* argument defaults to removing ASCII whitespace. The *bytes* argument is not a prefix or suffix; rather, all combinations of its values are stripped:

```python3
>>> b'   spacious   '.strip()
b'spacious'
>>> b'www.example.com'.strip(b'cmowz.')
b'example'
```

The binary sequence of byte values to remove may be any bytes-like object.

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

The following methods on bytes and bytearray objects assume the use of ASCII compatible binary formats and should not be applied to arbitrary binary data. Note that all of the bytearray methods in this section do *not* operate in place, and instead produce new objects.

**bytes.capitalize()**

**bytearray.capitalize()**

Return a copy of the sequence with each byte interpreted as an ASCII character, and the first byte capitalized and the rest lowercased. Non-ASCII byte values are passed through unchanged.

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.expandtabs(*tabsize=8*)**

**bytearray.expandtabs(*tabsize=8*)**

Return a copy of the sequence where all ASCII tab characters are replaced by one or more ASCII spaces, depending on the current column and the given tab size. Tab positions occur every *tabsize* bytes (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the sequence, the current column is set to zero and the sequence is examined byte by byte. If the byte is an ASCII tab character (`b'\t'`), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the current byte is an ASCII newline (`b'\n'`) or carriage return (`b'\r'`), it is copied and the current column is reset to zero. Any other byte value is copied unchanged and the current column is incremented by one regardless of how the byte value is represented when printed:

```python3
>>> b'01\t012\t0123\t01234'.expandtabs()
b'01      012     0123    01234'
>>> b'01\t012\t0123\t01234'.expandtabs(4)
b'01  012 0123    01234'
```

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.isalnum()**

**bytearray.isalnum()**

Return `True` if all bytes in the sequence are alphabetical ASCII characters or ASCII decimal digits and the sequence is not empty, `False` otherwise. Alphabetic ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`. ASCII decimal digits are those byte values in the sequence `b'0123456789'`.

For example:

```python3
>>> b'ABCabc1'.isalnum()
True
>>> b'ABC abc1'.isalnum()
False
```

**bytes.isalpha()**

**bytearray.isalpha()**

Return `True` if all bytes in the sequence are alphabetic ASCII characters and the sequence is not empty, `False` otherwise. Alphabetic ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

For example:

```python3
>>> b'ABCabc'.isalpha()
True
>>> b'ABCabc1'.isalpha()
False
```

**bytes.isascii()**

**bytearray.isascii()**

Return `True` if the sequence is empty or all bytes in the sequence are ASCII, `False` otherwise. ASCII bytes are in the range 0-0x7F.

Added in version 3.7.

**bytes.isdigit()**

**bytearray.isdigit()**

Return `True` if all bytes in the sequence are ASCII decimal digits and the sequence is not empty, `False` otherwise. ASCII decimal digits are those byte values in the sequence `b'0123456789'`.

For example:

```python3
>>> b'1234'.isdigit()
True
>>> b'1.23'.isdigit()
False
```

**bytes.islower()**

**bytearray.islower()**

Return `True` if there is at least one lowercase ASCII character in the sequence and no uppercase ASCII characters, `False` otherwise.

For example:

```python3
>>> b'hello world'.islower()
True
>>> b'Hello world'.islower()
False
```

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

**bytes.isspace()**

**bytearray.isspace()**

Return `True` if all bytes in the sequence are ASCII whitespace and the sequence is not empty, `False` otherwise. ASCII whitespace characters are those byte values in the sequence `b' \t\n\r\x0b\f'` (space, tab, newline, carriage return, vertical tab, form feed).

**bytes.istitle()**

**bytearray.istitle()**

Return `True` if the sequence is ASCII titlecase and the sequence is not empty, `False` otherwise. See `bytes.title()` for more details on the definition of “titlecase”.

For example:

```python3
>>> b'Hello World'.istitle()
True
>>> b'Hello world'.istitle()
False
```

**bytes.isupper()**

**bytearray.isupper()**

Return `True` if there is at least one uppercase alphabetic ASCII character in the sequence and no lowercase ASCII characters, `False` otherwise.

For example:

```python3
>>> b'HELLO WORLD'.isupper()
True
>>> b'Hello world'.isupper()
False
```

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

**bytes.lower()**

**bytearray.lower()**

Return a copy of the sequence with all the uppercase ASCII characters converted to their corresponding lowercase counterpart.

For example:

```python3
>>> b'Hello World'.lower()
b'hello world'
```

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.splitlines(*keepends=False*)**

**bytearray.splitlines(*keepends=False*)**

Return a list of the lines in the binary sequence, breaking at ASCII line boundaries. This method uses the universal newlines approach to splitting lines. Line breaks are not included in the resulting list unless *keepends* is given and true.

For example:

```python3
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
[b'ab c', b'', b'de fg', b'kl']
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
[b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']
```

Unlike `split()` when a delimiter string *sep* is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line:

```python3
>>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
([b''], [b'Two lines', b''])
>>> b"".splitlines(), b"One line\n".splitlines()
([], [b'One line'])
```

**bytes.swapcase()**

**bytearray.swapcase()**

Return a copy of the sequence with all the lowercase ASCII characters converted to their corresponding uppercase counterpart and vice-versa.

For example:

```python3
>>> b'Hello World'.swapcase()
b'hELLO wORLD'
```

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Unlike `str.swapcase()`, it is always the case that `bin.swapcase().swapcase() == bin` for the binary versions. Case conversions are symmetrical in ASCII, even though that is not generally true for arbitrary Unicode code points.

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.title()**

**bytearray.title()**

Return a titlecased version of the binary sequence where words start with an uppercase ASCII character and the remaining characters are lowercase. Uncased byte values are left unmodified.

For example:

```python3
>>> b'Hello world'.title()
b'Hello World'
```

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. All other byte values are uncased.

The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions and possessives form word boundaries, which may not be the desired result:

```python3
>>> b"they're bill's friends from the UK".title()
b"They'Re Bill'S Friends From The Uk"
```

A workaround for apostrophes can be constructed using regular expressions:

```python3
>>> import re
>>> def titlecase(s):
...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0:1].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase(b"they're bill's friends.")
b"They're Bill's Friends."
```

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.upper()**

**bytearray.upper()**

Return a copy of the sequence with all the lowercase ASCII characters converted to their corresponding uppercase counterpart.

For example:

```python3
>>> b'Hello World'.upper()
b'HELLO WORLD'
```

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

**bytes.zfill(*width*, */*)**

**bytearray.zfill(*width*, */*)**

Return a copy of the sequence left filled with ASCII `b'0'` digits to make a sequence of length *width*. A leading sign prefix (`b'+'`/ `b'-'`) is handled by inserting the padding *after* the sign character rather than before. For `bytes` objects, the original sequence is returned if *width* is less than or equal to `len(seq)`.

For example:

```python3
>>> b"42".zfill(5)
b'00042'
>>> b"-42".zfill(5)
b'-0042'
```

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

### `printf`-style Bytes Formatting

Note

The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly). If the value being printed may be a tuple or dictionary, wrap it in a tuple.

Bytes objects (`bytes`/`bytearray`) have one unique built-in operation: the `%` operator (modulo). This is also known as the bytes *formatting* or *interpolation* operator. Given `format % values` (where *format* is a bytes object), `%` conversion specifications in *format* are replaced with zero or more elements of *values*. The effect is similar to using the `sprintf()` in the C language.

If *format* requires a single argument, *values* may be a single non-tuple object. [5] Otherwise, *values* must be a tuple with exactly the number of items specified by the format bytes object, or a single mapping object (for example, a dictionary).

A conversion specifier contains two or more characters and has the following components, which must occur in this order:

1. The `'%'` character, which marks the start of the specifier.
2. Mapping key (optional), consisting of a parenthesised sequence of characters (for example, `(somename)`).
3. Conversion flags (optional), which affect the result of some conversion types.
4. Minimum field width (optional). If specified as an `'*'` (asterisk), the actual width is read from the next element of the tuple in *values*, and the object to convert comes after the minimum field width and optional precision.
5. Precision (optional), given as a `'.'` (dot) followed by the precision. If specified as `'*'` (an asterisk), the actual precision is read from the next element of the tuple in *values*, and the value to convert comes after the precision.
6. Length modifier (optional).
7. Conversion type.

When the right argument is a dictionary (or other mapping type), then the formats in the bytes object *must* include a parenthesised mapping key into that dictionary inserted immediately after the `'%'` character. The mapping key selects the value to be formatted from the mapping. For example:

```
>>> print(b'%(language)s has %(number)03d quote types.' %
...       {b'language': b"Python", b"number": 2})
b'Python has 002 quote types.'
```

In this case no `*` specifiers may occur in a format (since they require a sequential parameter list).

The conversion flag characters are:

| Flag | Meaning |
|---|---|
| `'#'` | The value conversion will use the “alternate form” (where defined below). |
| `'0'` | The conversion will be zero padded for numeric values. |
| `'-'` | The converted value is left adjusted (overrides the `'0'` conversion if both are given). |
| `' '` | (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion. |
| `'+'` | A sign character (`'+'` or `'-'`) will precede the conversion (overrides a “space” flag). |

A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it is not necessary for Python – so e.g. `%ld` is identical to `%d`.

The conversion types are:

| Conversion | Meaning | Notes |
|---|---|---|
| `'d'` | Signed integer decimal. |   |
| `'i'` | Signed integer decimal. |   |
| `'o'` | Signed octal value. | (1) |
| `'u'` | Obsolete type – it is identical to `'d'`. | (8) |
| `'x'` | Signed hexadecimal (lowercase). | (2) |
| `'X'` | Signed hexadecimal (uppercase). | (2) |
| `'e'` | Floating-point exponential format (lowercase). | (3) |
| `'E'` | Floating-point exponential format (uppercase). | (3) |
| `'f'` | Floating-point decimal format. | (3) |
| `'F'` | Floating-point decimal format. | (3) |
| `'g'` | Floating-point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4) |
| `'G'` | Floating-point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4) |
| `'c'` | Single byte (accepts integer or single byte objects). |   |
| `'b'` | Bytes (any object that follows the buffer protocol or has `__bytes__()`). | (5) |
| `'s'` | `'s'` is an alias for `'b'` and should only be used for Python2/3 code bases. | (6) |
| `'a'` | Bytes (converts any Python object using `repr(obj).encode('ascii', 'backslashreplace')`). | (5) |
| `'r'` | `'r'` is an alias for `'a'` and should only be used for Python2/3 code bases. | (7) |
| `'%'` | No argument is converted, results in a `'%'` character in the result. |   |

Notes:

1. The alternate form causes a leading octal specifier (`'0o'`) to be inserted before the first digit.
2. The alternate form causes a leading `'0x'` or `'0X'` (depending on whether the `'x'` or `'X'` format was used) to be inserted before the first digit.
3. The alternate form causes the result to always contain a decimal point, even if no digits follow it. The precision determines the number of digits after the decimal point and defaults to 6.
4. The alternate form causes the result to always contain a decimal point, and trailing zeroes are not removed as they would otherwise be. The precision determines the number of significant digits before and after the decimal point and defaults to 6.
5. If precision is `N`, the output is truncated to `N` characters.
6. `b'%s'` is deprecated, but will not be removed during the 3.x series.
7. `b'%r'` is deprecated, but will not be removed during the 3.x series.
8. See **PEP 237**.

Note

The bytearray version of this method does *not* operate in place - it always produces a new object, even if no changes were made.

See also

**PEP 461** - Adding % formatting to bytes and bytearray

Added in version 3.5.

### Memory Views

`memoryview` objects allow Python code to access the internal data of an object that supports the buffer protocol without copying.

***class*memoryview(*object*)**

> Create a `memoryview` that references *object*. *object* must support the buffer protocol. Built-in objects that support the buffer protocol include `bytes` and `bytearray`.
> 
> A `memoryview` has the notion of an *element*, which is the atomic memory unit handled by the originating *object*. For many simple types such as `bytes` and `bytearray`, an element is a single byte, but other types such as `array.array` may have bigger elements.
> 
> `memoryview`s are generic over the type of their underlying data.
> 
> `len(view)` is equal to the length of `tolist`, which is the nested list representation of the view. If `view.ndim = 1`, this is equal to the number of elements in the view.
> 
> Changed in version 3.12: If `view.ndim == 0`, `len(view)` now raises `TypeError` instead of returning 1.
> 
> The `itemsize` attribute will give you the number of bytes in a single element.
> 
> A `memoryview` supports slicing and indexing to expose its data. One-dimensional slicing will result in a subview:
> 
> ```python3
> >>> v = memoryview(b'abcefg')
> >>> v[1]
> 98
> >>> v[-1]
> 103
> >>> v[1:4]
> <memory at 0x7f3ddc9f4350>
> >>> bytes(v[1:4])
> b'bce'
> ```
> 
> If `format` is one of the native format specifiers from the `struct` module, indexing with an integer or a tuple of integers is also supported and returns a single *element* with the correct type. One-dimensional memoryviews can be indexed with an integer or a one-integer tuple. Multi-dimensional memoryviews can be indexed with tuples of exactly *ndim* integers where *ndim* is the number of dimensions. Zero-dimensional memoryviews can be indexed with the empty tuple.
> 
> Here is an example with a non-byte format:
> 
> ```python3
> >>> import array
> >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
> >>> m = memoryview(a)
> >>> m[0]
> -11111111
> >>> m[-1]
> 44444444
> >>> m[::2].tolist()
> [-11111111, -33333333]
> ```
> 
> If the underlying object is writable, the memoryview supports one-dimensional slice assignment. Resizing is not allowed:
> 
> ```python3
> >>> data = bytearray(b'abcefg')
> >>> v = memoryview(data)
> >>> v.readonly
> False
> >>> v[0] = ord(b'z')
> >>> data
> bytearray(b'zbcefg')
> >>> v[1:4] = b'123'
> >>> data
> bytearray(b'z123fg')
> >>> v[2:3] = b'spam'
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ValueError: memoryview assignment: lvalue and rvalue have different structures
> >>> v[2:6] = b'spam'
> >>> data
> bytearray(b'z1spam')
> ```
> 
> One-dimensional memoryviews of hashable (read-only) types with formats ‘B’, ‘b’ or ‘c’ are also hashable. The hash is defined as `hash(m) == hash(m.tobytes())`:
> 
> ```python3
> >>> v = memoryview(b'abcefg')
> >>> hash(v) == hash(b'abcefg')
> True
> >>> hash(v[2:4]) == hash(b'ce')
> True
> >>> hash(v[::-2]) == hash(b'abcefg'[::-2])
> True
> ```
> 
> Changed in version 3.3: One-dimensional memoryviews can now be sliced. One-dimensional memoryviews with formats ‘B’, ‘b’ or ‘c’ are now hashable.
> 
> Changed in version 3.4: memoryview is now registered automatically with `collections.abc.Sequence`
> 
> Changed in version 3.5: memoryviews can now be indexed with tuple of integers.
> 
> Changed in version 3.14: memoryview is now a generic type.
> 
> `memoryview` has several methods:
> 
> **__eq__(*exporter*)**
> 
> A memoryview and a **PEP 3118** exporter are equal if their shapes are equivalent and if all corresponding values are equal when the operands’ respective format codes are interpreted using `struct` syntax.
> 
> For the subset of `struct` format strings currently supported by `tolist()`, `v` and `w` are equal if `v.tolist() == w.tolist()`:
> 
> ```python3
> >>> import array
> >>> a = array.array('I', [1, 2, 3, 4, 5])
> >>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
> >>> c = array.array('b', [5, 3, 1])
> >>> x = memoryview(a)
> >>> y = memoryview(b)
> >>> x == a == y == b
> True
> >>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
> True
> >>> z = y[::-2]
> >>> z == c
> True
> >>> z.tolist() == c.tolist()
> True
> ```
> 
> If either format string is not supported by the `struct` module, then the objects will always compare as unequal (even if the format strings and buffer contents are identical):
> 
> ```python3
> >>> from ctypes import BigEndianStructure, c_long
> >>> class BEPoint(BigEndianStructure):
> ...     _fields_ = [("x", c_long), ("y", c_long)]
> ...
> >>> point = BEPoint(100, 200)
> >>> a = memoryview(point)
> >>> b = memoryview(point)
> >>> a == point
> False
> >>> a == b
> False
> ```
> 
> Note that, as with floating-point numbers, `v is w` does *not* imply `v == w` for memoryview objects.
> 
> Changed in version 3.3: Previous versions compared the raw memory disregarding the item format and the logical array structure.
> 
> **tobytes(*order='C'*)**
> 
> Return the data in the buffer as a bytestring. This is equivalent to calling the `bytes` constructor on the memoryview.
> 
> ```python3
> >>> m = memoryview(b"abc")
> >>> m.tobytes()
> b'abc'
> >>> bytes(m)
> b'abc'
> ```
> 
> For non-contiguous arrays the result is equal to the flattened list representation with all elements converted to bytes. `tobytes()` supports all format strings, including those that are not in `struct` module syntax.
> 
> Added in version 3.8: *order* can be {‘C’, ‘F’, ‘A’}. When *order* is ‘C’ or ‘F’, the data of the original array is converted to C or Fortran order. For contiguous views, ‘A’ returns an exact copy of the physical memory. In particular, in-memory Fortran order is preserved. For non-contiguous views, the data is converted to C first. *order=None* is the same as *order=’C’*.
> 
> **hex(***, *bytes_per_sep=1*)**
> 
> **hex(*sep*, *bytes_per_sep=1*)**
> 
> Return a string object containing two hexadecimal digits for each byte in the buffer.
> 
> ```python3
> >>> m = memoryview(b"abc")
> >>> m.hex()
> '616263'
> ```
> 
> Added in version 3.5.
> 
> Changed in version 3.8: Similar to `bytes.hex()`, `memoryview.hex()` now supports optional *sep* and *bytes_per_sep* parameters to insert separators between bytes in the hex output.
> 
> **tolist()**
> 
> Return the data in the buffer as a list of elements.
> 
> ```python3
> >>> memoryview(b'abc').tolist()
> [97, 98, 99]
> >>> import array
> >>> a = array.array('d', [1.1, 2.2, 3.3])
> >>> m = memoryview(a)
> >>> m.tolist()
> [1.1, 2.2, 3.3]
> ```
> 
> Changed in version 3.3: `tolist()` now supports all single character native formats in `struct` module syntax as well as multi-dimensional representations.
> 
> **toreadonly()**
> 
> Return a readonly version of the memoryview object. The original memoryview object is unchanged.
> 
> ```python3
> >>> m = memoryview(bytearray(b'abc'))
> >>> mm = m.toreadonly()
> >>> mm.tolist()
> [97, 98, 99]
> >>> mm[0] = 42
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: cannot modify read-only memory
> >>> m[0] = 43
> >>> mm.tolist()
> [43, 98, 99]
> ```
> 
> Added in version 3.8.
> 
> **release()**
> 
> Release the underlying buffer exposed by the memoryview object. Many objects take special actions when a view is held on them (for example, a `bytearray` would temporarily forbid resizing); therefore, calling release() is handy to remove these restrictions (and free any dangling resources) as soon as possible.
> 
> After this method has been called, any further operation on the view raises a `ValueError` (except `release()` itself which can be called multiple times):
> 
> ```python3
> >>> m = memoryview(b'abc')
> >>> m.release()
> >>> m[0]
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ValueError: operation forbidden on released memoryview object
> ```
> 
> The context management protocol can be used for a similar effect, using the `with` statement:
> 
> ```python3
> >>> with memoryview(b'abc') as m:
> ...     m[0]
> ...
> 97
> >>> m[0]
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ValueError: operation forbidden on released memoryview object
> ```
> 
> Added in version 3.2.
> 
> **cast(*format*, */*)**
> 
> **cast(*format*, *shape*, */*)**
> 
> Cast a memoryview to a new format or shape. *shape* defaults to `[byte_length//new_itemsize]`, which means that the result view will be one-dimensional. The return value is a new memoryview, but the buffer itself is not copied. Supported casts are 1D -> C-contiguous and C-contiguous -> 1D.
> 
> The destination format is restricted to a single element native format in `struct` syntax. One of the formats must be a byte format (‘B’, ‘b’ or ‘c’). The byte length of the result must be the same as the original length. Note that all byte lengths may depend on the operating system.
> 
> Cast 1D/long to 1D/unsigned bytes:
> 
> ```python3
> >>> import array
> >>> a = array.array('l', [1,2,3])
> >>> x = memoryview(a)
> >>> x.format
> 'l'
> >>> x.itemsize
> 8
> >>> len(x)
> 3
> >>> x.nbytes
> 24
> >>> y = x.cast('B')
> >>> y.format
> 'B'
> >>> y.itemsize
> 1
> >>> len(y)
> 24
> >>> y.nbytes
> 24
> ```
> 
> Cast 1D/unsigned bytes to 1D/char:
> 
> ```python3
> >>> b = bytearray(b'zyz')
> >>> x = memoryview(b)
> >>> x[0] = b'a'
> Traceback (most recent call last):
>   ...
> TypeError: memoryview: invalid type for format 'B'
> >>> y = x.cast('c')
> >>> y[0] = b'a'
> >>> b
> bytearray(b'ayz')
> ```
> 
> Cast 1D/bytes to 3D/ints to 1D/signed char:
> 
> ```python3
> >>> import struct
> >>> buf = struct.pack("i"*12, *list(range(12)))
> >>> x = memoryview(buf)
> >>> y = x.cast('i', shape=[2,2,3])
> >>> y.tolist()
> [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
> >>> y.format
> 'i'
> >>> y.itemsize
> 4
> >>> len(y)
> 2
> >>> y.nbytes
> 48
> >>> z = y.cast('b')
> >>> z.format
> 'b'
> >>> z.itemsize
> 1
> >>> len(z)
> 48
> >>> z.nbytes
> 48
> ```
> 
> Cast 1D/unsigned long to 2D/unsigned long:
> 
> ```python3
> >>> buf = struct.pack("L"*6, *list(range(6)))
> >>> x = memoryview(buf)
> >>> y = x.cast('L', shape=[2,3])
> >>> len(y)
> 2
> >>> y.nbytes
> 48
> >>> y.tolist()
> [[0, 1, 2], [3, 4, 5]]
> ```
> 
> Added in version 3.3.
> 
> Changed in version 3.5: The source format is no longer restricted when casting to a byte view.
> 
> **count(*value*, */*)**
> 
> Count the number of occurrences of *value*.
> 
> Added in version 3.14.

**index(*value*, *start=0*, *stop=sys.maxsize*, */*)**

> Return the index of the first occurrence of *value* (at or after index *start* and before index *stop*).
> 
> Raises a `ValueError` if *value* cannot be found.
> 
> Added in version 3.14.

There are also several readonly attributes available:

**obj**

The underlying object of the memoryview:

```python3
>>> b  = bytearray(b'xyz')
>>> m = memoryview(b)
>>> m.obj is b
True
```

Added in version 3.3.

**nbytes**

`nbytes == product(shape) * itemsize == len(m.tobytes())`. This is the amount of space in bytes that the array would use in a contiguous representation. It is not necessarily equal to `len(m)`:

```python3
>>> import array
>>> a = array.array('i', [1,2,3,4,5])
>>> m = memoryview(a)
>>> len(m)
5
>>> m.nbytes
20
>>> y = m[::2]
>>> len(y)
3
>>> y.nbytes
12
>>> len(y.tobytes())
12
```

Multi-dimensional arrays:

```python3
>>> import struct
>>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
>>> x = memoryview(buf)
>>> y = x.cast('d', shape=[3,4])
>>> y.tolist()
[[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
>>> len(y)
3
>>> y.nbytes
96
```

Added in version 3.3.

**readonly**

A bool indicating whether the memory is read only.

**format**

A string containing the format (in `struct` module style) for each element in the view. A memoryview can be created from exporters with arbitrary format strings, but some methods (e.g. `tolist()`) are restricted to native single element formats.

Changed in version 3.3: format `'B'` is now handled according to the struct module syntax. This means that `memoryview(b'abc')[0] == b'abc'[0] == 97`.

**itemsize**

The size in bytes of each element of the memoryview:

```python3
>>> import array, struct
>>> m = memoryview(array.array('H', [32000, 32001, 32002]))
>>> m.itemsize
2
>>> m[0]
32000
>>> struct.calcsize('H') == m.itemsize
True
```

**ndim**

An integer indicating how many dimensions of a multi-dimensional array the memory represents.

**shape**

A tuple of integers the length of `ndim` giving the shape of the memory as an N-dimensional array.

Changed in version 3.3: An empty tuple instead of `None` when ndim = 0.

**strides**

A tuple of integers the length of `ndim` giving the size in bytes to access each element for each dimension of the array.

Changed in version 3.3: An empty tuple instead of `None` when ndim = 0.

**suboffsets**

Used internally for PIL-style arrays. The value is informational only.

**c_contiguous**

A bool indicating whether the memory is C-contiguous.

Added in version 3.3.

**f_contiguous**

A bool indicating whether the memory is Fortran contiguous.

Added in version 3.3.

**contiguous**

A bool indicating whether the memory is contiguous.

Added in version 3.3.

For information on the thread safety of `memoryview` objects in the free-threaded build, see Thread safety for memoryview objects.


## Set Types — `set`, `frozenset`

A *set* object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built-in `dict`, `list`, and `tuple` classes, and the `collections` module.)

Like other collections, sets support `x in set`, `len(set)`, and `for x in set`. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

There are currently two built-in set types, `set` and `frozenset`. The `set` type is mutable — the contents can be changed using methods like `add()` and `remove()`. Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. The `frozenset` type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.

Non-empty sets (not frozensets) can be created by placing a comma-separated list of elements within braces, for example: `{'jack', 'sjoerd'}`, in addition to the `set` constructor.

The constructors for both classes work the same:

***class*set(*iterable=()*, */*)**

***class*frozenset(*iterable=()*, */*)**

Return a new set or frozenset object whose elements are taken from *iterable*. The elements of a set must be hashable. To represent sets of sets, the inner sets must be `frozenset` objects. If *iterable* is not specified, a new empty set is returned.

Sets can be created by several means:

- Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`
- Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`
- Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`

Instances of `set` and `frozenset` provide the following operations:

**len(s)**

Return the number of elements in set *s* (cardinality of *s*).

**x in s**

Test *x* for membership in *s*.

**x not in s**

Test *x* for non-membership in *s*.

**frozenset.isdisjoint(*other*, */*)**

**set.isdisjoint(*other*, */*)**

Return `True` if the set has no elements in common with *other*. Sets are disjoint if and only if their intersection is the empty set.

**frozenset.issubset(*other*, */*)**

**set.issubset(*other*, */*)**

**set <= other**

Test whether every element in the set is in *other*.

**set < other**

Test whether the set is a proper subset of *other*, that is, `set <= other and set != other`.

**frozenset.issuperset(*other*, */*)**

**set.issuperset(*other*, */*)**

**set >= other**

Test whether every element in *other* is in the set.

**set > other**

Test whether the set is a proper superset of *other*, that is, `set >= other and set != other`.

**frozenset.union(**others*)**

**set.union(**others*)**

**set | other | ...**

Return a new set with elements from the set and all others.

**frozenset.intersection(**others*)**

**set.intersection(**others*)**

**set & other & ...**

Return a new set with elements common to the set and all others.

**frozenset.difference(**others*)**

**set.difference(**others*)**

**set - other - ...**

Return a new set with elements in the set that are not in the others.

**frozenset.symmetric_difference(*other*, */*)**

**set.symmetric_difference(*other*, */*)**

**set ^ other**

Return a new set with elements in either the set or *other* but not both.

**frozenset.copy()**

**set.copy()**

Return a shallow copy of the set.

Note, the non-operator versions of `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, and `issuperset()` methods will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like `set('abc') & 'cbs'` in favor of the more readable `set('abc').intersection('cbs')`.

Both `set` and `frozenset` support set to set comparisons. Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other). A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal). A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).

Instances of `set` are compared to instances of `frozenset` based on their members. For example, `set('abc') == frozenset('abc')` returns `True` and so does `set('abc') in set([frozenset('abc')])`.

The subset and equality comparisons do not generalize to a total ordering function. For example, any two nonempty disjoint sets are not equal and are not subsets of each other, so *all* of the following return `False`: `a<b`, `a==b`, or `a>b`.

Since sets only define partial ordering (subset relationships), the output of the `list.sort()` method is undefined for lists of sets.

Set elements, like dictionary keys, must be hashable.

Binary operations that mix `set` instances with `frozenset` return the type of the first operand. For example: `frozenset('ab') | set('bc')` returns an instance of `frozenset`.

The following table lists operations available for `set` that do not apply to immutable instances of `frozenset`:

**set.update(**others*)**

**set |= other | ...**

Update the set, adding elements from all others.

**set.intersection_update(**others*)**

**set &= other & ...**

Update the set, keeping only elements found in it and all others.

**set.difference_update(**others*)**

**set -= other | ...**

Update the set, removing elements found in others.

**set.symmetric_difference_update(*other*, */*)**

**set ^= other**

Update the set, keeping only elements found in either set, but not in both.

**set.add(*elem*, */*)**

Add element *elem* to the set.

**set.remove(*elem*, */*)**

Remove element *elem* from the set. Raises `KeyError` if *elem* is not contained in the set.

**set.discard(*elem*, */*)**

Remove element *elem* from the set if it is present.

**set.pop()**

Remove and return an arbitrary element from the set. Raises `KeyError` if the set is empty.

**set.clear()**

Remove all elements from the set.

Note, the non-operator versions of the `update()`, `intersection_update()`, `difference_update()`, and `symmetric_difference_update()` methods will accept any iterable as an argument.

Note, the *elem* argument to the `__contains__()`, `remove()`, and `discard()` methods may be a set. To support searching for an equivalent frozenset, a temporary one is created from *elem*.

See also

For detailed information on thread-safety guarantees for `set` objects, see Thread safety for set objects.

Sets and frozensets are generic over the type of their elements.
