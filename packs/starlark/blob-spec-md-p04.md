---
title: "starlark/spec.md at master · bazelbuild/starlark · GitHub (part 4/4)"
source: https://github.com/bazelbuild/starlark/blob/master/spec.md
domain: starlark
license: Apache-2.0
tags: starlark language, bazel build language, python-like config dialect, starlark scripting
fetched: 2026-07-02
part: 4/4
---

## Built-in methods

This section lists the methods of built-in types. Methods are selected using dot expressions. For example, strings have a `count` method that counts occurrences of a substring; `"banana".count("a")` yields `3`.

### bytes·elems

`b.elems()` returns an opaque iterable value containing successive int elements of b. Its type is `"bytes.elems"`, and its string representation is of the form `b"...".elems()`.

```highlight
type(b"ABC".elems())	# "bytes.elems"
b"ABC".elems()	        # b"ABC".elems()
list(b"ABC".elems())  	# [65, 66, 67]
```

### dict·clear

`D.clear()` removes all the entries of dictionary D and returns `None`. It fails if the dictionary is frozen or if there are active iterators.

```highlight
x = {"one": 1, "two": 2}
x.clear()                               # None
print(x)                                # {}
```

### dict·get

`D.get(key[, default])` returns the dictionary value corresponding to the given key. If the dictionary contains no such value, `get` returns `None`, or the value of the optional `default` parameter if present.

`get` fails if `key` is unhashable, or the dictionary is frozen or has active iterators.

```highlight
x = {"one": 1, "two": 2}
x.get("one")                            # 1
x.get("three")                          # None
x.get("three", 0)                       # 0
```

### dict·items

`D.items()` returns a new list of key/value pairs, one per element in dictionary D, in the same order as they would be returned by a `for` loop.

```highlight
x = {"one": 1, "two": 2}
x.items()                               # [("one", 1), ("two", 2)]
```

### dict·keys

`D.keys()` returns a new list containing the keys of dictionary D, in the same order as they would be returned by a `for` loop.

```highlight
x = {"one": 1, "two": 2}
x.keys()                               # ["one", "two"]
```

### dict·pop

`D.pop(key[, default])` returns the value corresponding to the specified key, and removes it from the dictionary. If the dictionary contains no such value, and the optional `default` parameter is present, `pop` returns that value; otherwise, it fails.

`pop` fails if `key` is unhashable, or the dictionary is frozen or has active iterators.

```highlight
x = {"one": 1, "two": 2}
x.pop("one")                            # 1
x                                       # {"two": 2}
x.pop("three", 0)                       # 0
x.pop("four")                           # error: missing key
```

### dict·popitem

`D.popitem()` returns the first key/value pair, removing it from the dictionary.

`popitem` fails if the dictionary is empty, frozen, or has active iterators.

```highlight
x = {"one": 1, "two": 2}
x.popitem()                             # ("one", 1)
x.popitem()                             # ("two", 2)
x.popitem()                             # error: empty dict
```

### dict·setdefault

`D.setdefault(key[, default])` returns the dictionary value corresponding to the given key. If the dictionary contains no such value, `setdefault`, like `get`, returns `None` or the value of the optional `default` parameter if present; `setdefault` additionally inserts the new key/value entry into the dictionary.

`setdefault` fails if the key is unhashable, or if the dictionary is frozen or has active iterators.

```highlight
x = {"one": 1, "two": 2}
x.setdefault("one")                     # 1
x.setdefault("three", 3)                # 3
x                                       # {"one": 1, "two": 2, "three": 3}
x.setdefault("three", 33)               # 3
x                                       # {"one": 1, "two": 2, "three": 3}
x.setdefault("four")                    # None
x                                       # {"one": 1, "two": 2, "three": 3, "four": None}
```

### dict·update

`D.update([pairs][, name=value[, ...])` makes a series of key/value insertions into dictionary D, then returns `None.`

If the positional argument `pairs` is present, it must be `None`, another `dict`, or some other iterable. If it is another `dict`, then its key/value pairs are inserted into D. If it is an iterable, it must provide a sequence of pairs (or other iterables of length 2), each of which is treated as a key/value pair to be inserted into D.

Then, for each `name=value` argument present, an entry with key `name` and value `value` is inserted into D.

All insertions overwrite any previous entries having the same key.

It is permissible to update the dict with itself given as pairs. The operation is no-op.

`update` fails if the dictionary is frozen or has active iterators.

```highlight
x = {}
x.update([("a", 1), ("b", 2)], c=3)
x.update({"d": 4})
x.update(e=5)
x                                       # {"a": 1, "b": "2", "c": 3, "d": 4, "e": 5}
```

### dict·values

`D.values()` returns a new list containing the dictionary's values, in the same order as they would be returned by a `for` loop over the dictionary.

```highlight
x = {"one": 1, "two": 2}
x.values()                              # [1, 2]
```

### list·append

`L.append(x)` appends `x` to the list L, and returns `None`.

`append` fails if the list is frozen or has active iterators.

```highlight
x = []
x.append(1)                             # None
x.append(2)                             # None
x.append(3)                             # None
x                                       # [1, 2, 3]
```

### list·clear

`L.clear()` removes all the elements of the list L and returns `None`. It fails if the list is frozen or if there are active iterators.

```highlight
x = [1, 2, 3]
x.clear()                               # None
x                                       # []
```

### list·extend

`L.extend(x)` appends the elements of `x`, which must be iterable, to the list L, and returns `None`.

It is permissible to extend the list with itself. The operation doubles the list.

`extend` fails if `x` is not iterable, or if the list L is frozen or has active iterators.

```highlight
x = []
x.extend([1, 2, 3])                     # None
x.extend(["foo"])                       # None
x                                       # [1, 2, 3, "foo"]

y = [1, 2]
y.extend(y)
y                                       # [1, 2, 1, 2]
```

### list·index

`L.index(x[, start[, end]])` finds `x` within the list L and returns its index.

The optional `start` and `end` parameters restrict the portion of list L that is inspected. If provided and not `None`, they must be list indices of type `int`. If an index is negative, `len(L)` is effectively added to it, then if the index is outside the range `[0:len(L)]`, the nearest value within that range is used; see Indexing.

`index` fails if `x` is not found in L, or if `start` or `end` is not a valid index (`int` or `None`). To avoid this error, test `x in list` before calling `list.index(x)`.

```highlight
x = ["b", "a", "n", "a", "n", "a"]
x.index("a")                            # 1 (bAnana)
x.index("a", 2)                         # 3 (banAna)
x.index("a", -2)                        # 5 (bananA)
```

### list·insert

`L.insert(i, x)` inserts the value `x` in the list L at index `i`, moving higher-numbered elements along by one. It returns `None`.

As usual, the index `i` must be an `int`. If its value is negative, the length of the list is added, then its value is clamped to the nearest value in the range `[0:len(L)]` to yield the effective index.

`insert` fails if the list is frozen or has active iterators.

```highlight
x = ["b", "c", "e"]
x.insert(0, "a")                        # None
x.insert(-1, "d")                       # None
x                                       # ["a", "b", "c", "d", "e"]
```

### list·pop

`L.pop([index])` removes and returns the last element of the list L, or, if the optional index is provided, at that index.

`pop` fails if the index is negative or not less than the length of the list, of if the list is frozen or has active iterators.

```highlight
x = [1, 2, 3]
x.pop()                                 # 3
x.pop()                                 # 2
x                                       # [1]
```

### list·remove

`L.remove(x)` removes the first occurrence of the value `x` from the list L, and returns `None`.

`remove` fails if the list does not contain `x`, is frozen, or has active iterators.

```highlight
x = [1, 2, 3, 2]
x.remove(2)                             # None (x == [1, 3, 2])
x.remove(2)                             # None (x == [1, 3])
x.remove(2)                             # error: element not found
```

### set·add

`S.add(x)` adds the value `x` to the set `S`. It returns `None`.

It is permissible to `add` a value already present in the set; this leaves the set `S` unchanged.

`add` fails if the set `S` is frozen or has active iterators, or if `x` is unhashable.

If you need to add multiple elements to a set, see `update` or the `|=` augmented assignment operation.

### set·clear

`S.clear()` removes all elements from the set `S`. It returns `None`.

`clear` fails if the set `S` is frozen or has active iterators.

### set·difference

`S.difference(*others)` returns a new set containing elements found in the set `S` but not found in any of the collections `*others`.

If `s` and `t` are sets, `s.difference(t)` is equivalent to `s - t`; however, note that the `-` operation requires both sides to be sets, while the `difference` method accepts arbitrary collections.

It is permissible to call `difference` without any arguments; this returns a copy of the set `S`.

`difference` fails if any element of any of the `*others` is unhashable.

```highlight
set([1, 2, 3]).difference([2])             # set([1, 3])
set([1, 2, 3]).difference([0, 1], [3, 4])  # set([2])
```

### set·difference_update

`S.difference_update(*others)` removes from the set `S` any elements found in any of the collections `*others`. It returns `None`.

If `s` and `t` are sets, `s.difference_update(t)` is equivalent to `s -= t`; however, note that the `-=` augmented assignment requires both sides to be sets, while the `difference_update` method accepts arbitrary collections.

It is permissible to call `difference_update` without any arguments; this leaves the set `S` unchanged.

`difference_update` fails if the set `S` is frozen or has active iterators, or if any element of any of the `*others` is unhashable.

```highlight
s = set([1, 2, 3, 4])
s.difference_update([2])             # None; s is set([1, 3, 4])
s.difference_update([0, 1], [4, 5])  # None; s is set([3])
```

### set·discard

`S.discard(x)` removes the value `x` from the set `S` if present. It returns `None`.

It is permissible to `discard` a value not present in the set; this leaves the set `S` unchanged. If you want to fail on an attempt to remove a non-present element, use `remove` instead. If you need to remove multiple elements from a set, see `difference_update` or the `-=` augmented assignment operation.

`discard` fails if the set `S` is frozen or has active iterators, or if `x` is unhashable. This applies even if `x` is not a member of the set.

```highlight
s = set(["x", "y"])
s.discard("y")  # None; s == set(["x"])
s.discard("y")  # None; s == set(["x"])
```

### set·intersection

`S.intersection(*others)` returns a new set containing those elements that the set `S` and all of the collections `*others` have in common.

If `s` and `t` are sets, `s.intersection(t)` is equivalent to `s & t`; however, note that the `&` operation requires both sides to be sets, while the `intersection` method accepts arbitrary collections.

It is permissible to call `intersection` without any arguments; this returns a copy of the set `S`.

`intersection` fails if any element of any of the `*others` is unhashable.

```highlight
set([1, 2]).intersection([2, 3])             # set([2])
set([1, 2, 3]).intersection([0, 1], [1, 2])  # set([1])
```

### set·intersection_update

`S.intersection_update(*others)` removes from the set `S` any elements not found in at least one of the collections `*others`. It returns `None`.

If `s` and `t` are sets, `s.intersection_update(t)` is equivalent to `s &= t`; however, note that the `&=` augmented assignment requires both sides to be sets, while the `intersection_update` method accepts arbitrary collections.

It is permissible to call `intersection_update` without any arguments; this leaves the set `S` unchanged.

`intersection_update` fails if the set `S` is frozen or has active iterators, or if any element of any of the `*others` is unhashable.

```highlight
s = set([1, 2, 3, 4])
s.intersection_update([0, 1, 2])       # None; s is set([1, 2])
s.intersection_update([0, 1], [1, 2])  # None; s is set([1])
```

### set·isdisjoint

`S.isdisjoint(x)` returns `True` if the set `S` and the collection `x` do not have any values in common, and `False` otherwise.

This is equivalent to `not S.intersection(x)`.

`isdisjoint` fails if any element of `x` is unhashable.

### set·issubset

`S.issubset(x)` returns `True` if every element of the set `S` is present in the collection `x`, and `False` otherwise.

This is equivalent to `not S.difference(x)`.

`issubset` fails if any element of `x` is unhashable.

### set·issuperset

`S.issuperset(x)` returns `True` if every element of the collection `x` is present in the set `S`, and `False` otherwise.

This is equivalent to `S == S.union(x)`.

`issuperset` fails if any element of `x` is unhashable.

### set·pop

`S.pop()` removes and returns the first element (in iteration order, which is the order in which elements were first added to the set) from the set `S`.

`pop` fails if the set is empty, is frozen, or has active iterators.

```highlight
s = set([3, 1, 2])
s.pop()  # 3; s == set([1, 2])
s.pop()  # 1; s == set([2])
s.pop()  # 2; s == set()
s.pop()  # error: empty set
```

### set·remove

`S.remove(x)` removes the value `x` from the set `S`. It returns `None`.

`remove` fails if the set doesn't contain `x` (which, in particular, implies that `remove` fails if `x` is unhashable), or if the set is frozen or has active iterators. If you don't want to fail on an attempt to remove a non-present element, use `discard` instead. If you need to remove multiple elements from a set, see `difference_update` or the `-=` augmented assignment operation.

```highlight
s = set([1, 2])
s.remove(2)  # None; s == set([1])
s.remove(2)  # error: element not found
```

### set·symmetric_difference

`S.symmetric_difference(x)` returns a new set containing elements found only in the set `S` or in the collection `x` but not those found in both `S` and `x`.

If `s` and `t` are sets, `s.symmetric_difference(t)` is equivalent to `s ^ t`; however, note that the `^` operation requires both sides to be sets, while the `symmetric_difference` method accepts an arbitrary collection.

`symmetric_difference` fails if any element of `x` is unhashable.

```highlight
set([1, 2]).symmetric_difference([2, 3])  # set([1, 3])
```

### set·symmetric_difference_update

`S.symmetric_difference_update(x)` removes from the set `S` any elements found in both `S` and the collection `x`, and adds to `S` any elements found in `x` but not in `S`. It returns `None`.

If `s` and `t` are sets, `s.symmetric_difference_update(t)` is equivalent to `s ^= t`; however, note that the `^=` augmented assignment requires both sides to be sets, while the `symmetric_difference_update` method accepts an arbitrary collection.

`symmetric_difference_update` fails if the set `S` is frozen or has active iterators, or if any element of `x` is unhashable.

```highlight
s = set([1, 2])
s.symmetric_difference_update([2, 3])  # None; s == set([1, 3])
```

### set·union

`S.union(*others)` returns a new set containing elements found in the set `S` or in any of the collections `*others`.

If `s` and `t` are sets, `s.union(t)` is equivalent to `s | t`; however, note that the `|` operation requires both sides to be sets, while the `union` method accepts arbitrary collections.

It is permissible to call `union` without any arguments; this returns a copy of the set `S`.

`union` fails if any element of any of the `*others` is unhashable.

```highlight
set([1, 2]).union([2, 3])                    # set([1, 2, 3])
set([1, 2]).union([2, 3], {3: "a", 4: "b"})  # set([1, 2, 3, 4])
```

### set·update

`S.update(*others)` adds to the set `S` any elements found in any of the collections `*others`. It returns `None`.

If `s` and `t` are sets, `s.update(t)` is equivalent to `s |= t`; however, note that the `|=` augmented assignment requires both sides to be sets, while the `update` method accepts arbitrary collections.

It is permissible to call `update` without any arguments; this leaves the set `S` unchanged.

`update` fails if the set `S` is frozen or has active iterators, or if any element of any of the `*others` is unhashable.

```highlight
s = set()
s.update([1, 2])          # None; s is set([1, 2])
s.update([2, 3], [3, 4])  # None; s is set([1, 2, 3, 4])
```

### string·capitalize

`S.capitalize()` returns a copy of string S, where the first character (if any) is converted to uppercase; all other characters are converted to lowercase.

```highlight
"hello, world!".capitalize()		# "Hello, world!"
```

### string·count

`S.count(sub[, start[, end]])` returns the number of occurrences of `sub` within the string S, or, if the optional substring indices `start` and `end` are provided, within the designated substring of S. They are interpreted according to Starlark's indexing conventions.

```highlight
"hello, world!".count("o")              # 2
"hello, world!".count("o", 7, 12)       # 1  (in "world")
```

### string·elems

`S.elems()` returns an opaque iterable value containing successive 1-element substrings of S. Its type is `"string.elems"`, and its string representation is of the form `"...".elems()`.

```highlight
"Hello, 123".elems()	        # "Hello, 123".elems()
type("Hello, 123".elems())	# "string.elems"
list("Hello, 123".elems())	# ["H", "e", "l", "l", "o", ",", " ", "1", "2", "3"]
```

### string·endswith

`S.endswith(suffix[, start[, end]])` reports whether the string `S[start:end]` has the specified suffix.

```highlight
"filename.sky".endswith(".sky")         # True
"filename.sky".endswith(".sky", 9, 12)  # False
"filename.sky".endswith("name", 0, 8)   # True
```

The `suffix` argument may be a tuple of strings, in which case the function reports whether any one of them is a suffix.

```highlight
'foo.cc'.endswith(('.cc', '.h'))         # True
```

### string·find

`S.find(sub[, start[, end]])` returns the index of the first occurrence of the substring `sub` within S.

If either or both of `start` or `end` are specified, they specify a subrange of S to which the search should be restricted. They are interpreted according to Starlark's indexing conventions.

If no occurrence is found, `found` returns -1.

```highlight
"bonbon".find("on")             # 1
"bonbon".find("on", 2)          # 4
"bonbon".find("on", 2, 5)       # -1
```

### string·format

`S.format(*args, **kwargs)` returns a version of the format string S in which bracketed portions `{...}` are replaced by arguments from `args` and `kwargs`.

Within the format string, a pair of braces `{{` or `}}` is treated as a literal open or close brace. Each unpaired open brace must be matched by a close brace `}`. The optional text between corresponding open and close braces specifies which argument to use.

```
{}
{field}
```

The *field name* may be either a decimal number or a keyword. A number is interpreted as the index of a positional argument; a keyword specifies the value of a keyword argument. If all the numeric field names form the sequence 0, 1, 2, and so on, they may be omitted and those values will be implied; however, the explicit and implicit forms may not be mixed.

```highlight
"a{x}b{y}c{}".format(1, x=2, y=3)               # "a2b3c1"
"a{}b{}c".format(1, 2)                          # "a1b2c"
"({1}, {0})".format("zero", "one")              # "(one, zero)"
```

### string·index

`S.index(sub[, start[, end]])` returns the index of the first occurrence of the substring `sub` within S, like `S.find`, except that if the substring is not found, the operation fails.

```highlight
"bonbon".index("on")             # 1
"bonbon".index("on", 2)          # 4
"bonbon".index("on", 2, 5)       # error: substring not found  (in "nbo")
```

### string·isalnum

`S.isalnum()` reports whether the string S is non-empty and consists only Unicode letters and digits.

```highlight
"base64".isalnum()              # True
"Catch-22".isalnum()            # False
```

### string·isalpha

`S.isalpha()` reports whether the string S is non-empty and consists only of Unicode letters.

```highlight
"ABC".isalpha()                 # True
"Catch-22".isalpha()            # False
"".isalpha()                    # False
```

### string·isdigit

`S.isdigit()` reports whether the string S is non-empty and consists only of Unicode digits.

```highlight
"123".isdigit()                 # True
"Catch-22".isdigit()            # False
"".isdigit()                    # False
```

### string·islower

`S.islower()` reports whether the string S contains at least one cased Unicode letter, and all such letters are lowercase.

```highlight
"hello, world".islower()        # True
"Catch-22".islower()            # False
"123".islower()                 # False
```

### string·isspace

`S.isspace()` reports whether the string S is non-empty and consists only of Unicode spaces.

```highlight
"    ".isspace()                # True
"\r\t\n".isspace()              # True
"".isspace()                    # False
```

### string·istitle

`S.istitle()` reports whether the string S contains at least one cased Unicode letter, and all such letters that begin a word are in title case.

```highlight
"Hello, World!".istitle()       # True
"Catch-22".istitle()            # True
"HAL-9000".istitle()            # False
"123".istitle()                 # False
```

### string·isupper

`S.isupper()` reports whether the string S contains at least one cased Unicode letter, and all such letters are uppercase.

```highlight
"HAL-9000".isupper()            # True
"Catch-22".isupper()            # False
"123".isupper()                 # False
```

### string·join

`S.join(iterable)` returns the string formed by concatenating each element of its argument, with a copy of the string S between successive elements. The argument must be an iterable whose elements are strings.

```highlight
", ".join(["one", "two", "three"])      # "one, two, three"
"a".join("ctmrn".elems())               # "catamaran"
```

### string·lower

`S.lower()` returns a copy of the string S with letters converted to lowercase.

```highlight
"Hello, World!".lower()                 # "hello, world!"
```

### string·lstrip

`S.lstrip([cutset])` returns a copy of the string S with leading whitespace removed.

Like `strip`, it accepts an optional string parameter that specifies an alternative set of Unicode code points to remove.

```highlight
"\n hello  ".lstrip()                   # "hello  "
"   hello  ".lstrip("h o")              # "ello  "
```

### string·partition

`S.partition(x)` splits string S into three parts and returns them as a tuple: the portion before the first occurrence of string `x`, `x` itself, and the portion following it. If S does not contain `x`, `partition` returns `(S, "", "")`.

`partition` fails if `x` is not a string, or is the empty string.

```highlight
"one/two/three".partition("/")		# ("one", "/", "two/three")
```

### string·removeprefix

`S.removeprefix(x)` removes the prefix `x` from the string S at most once, and returns the rest of the string. If the prefix string is not found then it returns the original string.

`removeprefix` fails if `x` is not a string.

```highlight
"banana".removeprefix("ban")		# "ana"
"banana".removeprefix("ana")		# "banana"
"bbaa".removeprefix("b")		# "baa"
```

### string·removesuffix

`S.removesuffix(x)` removes the suffix `x` from the string S at most once, and returns the rest of the string. If the suffix string is not found then it returns the original string.

`removesuffix` fails if `x` is not a string.

```highlight
"banana".removesuffix("ana")		# "ban"
"banana".removesuffix("ban")		# "banana"
"bbaa".removesuffix("a")		# "bba"
```

### string·replace

`S.replace(old, new[, count])` returns a copy of string S with all occurrences of substring `old` replaced by `new`. If the optional argument `count`, which must be an `int`, is non-negative, it specifies a maximum number of occurrences to replace.

```highlight
"banana".replace("a", "o")		# "bonono"
"banana".replace("a", "o", 2)		# "bonona"
```

### string·rfind

`S.rfind(sub[, start[, end]])` returns the index of the substring `sub` within S, like `S.find`, except that `rfind` returns the index of the substring's *last* occurrence.

```highlight
"bonbon".rfind("on")             # 4
"bonbon".rfind("on", None, 5)    # 1
"bonbon".rfind("on", 2, 5)       # -1
```

### string·rindex

`S.rindex(sub[, start[, end]])` returns the index of the substring `sub` within S, like `S.index`, except that `rindex` returns the index of the substring's *last* occurrence.

```highlight
"bonbon".rindex("on")             # 4
"bonbon".rindex("on", None, 5)    # 1                           (in "bonbo")
"bonbon".rindex("on", 2, 5)       # error: substring not found  (in "nbo")
```

### string·rpartition

`S.rpartition(x)` is like `partition`, but splits `S` at the last occurrence of `x`.

```highlight
"one/two/three".rpartition("/")         # ("one/two", "/", "three")
```

### string·rsplit

`S.rsplit([sep[, maxsplit]])` splits a string into substrings like `S.split`, except that when a maximum number of splits is specified, `rsplit` chooses the rightmost splits.

```highlight
"banana".rsplit("n")                         # ["ba", "a", "a"]
"banana".rsplit("n", 1)                      # ["bana", "a"]
"one two  three".rsplit(None, 1)             # ["one two", "three"]
```

### string·rstrip

`S.rstrip([cutset])` returns a copy of the string S with trailing whitespace removed.

Like `strip`, it accepts an optional string parameter that specifies an alternative set of Unicode code points to remove.

```highlight
"  hello\r ".rstrip()                   # "  hello"
"  hello   ".rstrip("h o")              # "  hell"
```

### string·split

`S.split([sep [, maxsplit]])` returns the list of substrings of S, splitting at occurrences of the delimiter string `sep`.

Consecutive occurrences of `sep` are considered to delimit empty strings, so `'food'.split('o')` returns `['f', '', 'd']`. Splitting an empty string with a specified separator returns `['']`. If `sep` is the empty string, `split` fails.

If `sep` is not specified or is `None`, `split` uses a different algorithm: it removes all leading spaces from S (or trailing spaces in the case of `rsplit`), then splits the string around each consecutive non-empty sequence of Unicode white space characters.

If S consists only of white space, `split` returns the empty list.

If `maxsplit` is given and non-negative, it specifies a maximum number of splits.

```highlight
"one two  three".split()                    # ["one", "two", "three"]
"one two  three".split(" ")                 # ["one", "two", "", "three"]
"one two  three".split(None, 1)             # ["one", "two  three"]
"banana".split("n")                         # ["ba", "a", "a"]
"banana".split("n", 1)                      # ["ba", "ana"]
```

### string·splitlines

`S.splitlines([keepends])` returns a list whose elements are the successive lines of S, that is, the strings formed by splitting S at line terminators (currently assumed to be `\n`, `\r` and `\r\n`, regardless of platform).

The optional argument, `keepends`, is interpreted as a Boolean. If true, line terminators are preserved in the result, though the final element does not necessarily end with a line terminator.

```highlight
"A\nB\rC\r\nD".splitlines()     # ["A", "B", "C", "D"]
"one\n\ntwo".splitlines()       # ["one", "", "two"]
"one\n\ntwo".splitlines(True)   # ["one\n", "\n", "two"]
```

### string·startswith

`S.startswith(prefix[, start[, end]])` reports whether the string `S[start:end]` has the specified prefix.

```highlight
"filename.sky".startswith("filename")         # True
"filename.star".startswith("name", 4)         # True
"filename.star".startswith("name", 4, 7)      # False
```

The `prefix` argument may be a tuple of strings, in which case the function reports whether any one of them is a prefix.

```highlight
'abc'.startswith(('a', 'A'))                  # True
'ABC'.startswith(('a', 'A'))                  # True
'def'.startswith(('a', 'A'))                  # False
```

### string·strip

`S.strip([cutset])` returns a copy of the string S with leading and trailing whitespace removed.

It accepts an optional string argument, `cutset`, which instead removes all leading and trailing Unicode code points contained in `cutset`.

```highlight
"\rhello\t ".strip()                    # "hello"
"  hello   ".strip("h o")               # "ell"
```

### string·title

`S.title()` returns a copy of the string S with letters converted to titlecase.

Letters are converted to uppercase at the start of words, lowercase elsewhere.

```highlight
"hElLo, WoRlD!".title()                 # "Hello, World!"
```

### string·upper

`S.upper()` returns a copy of the string S with letters converted to uppercase.

```highlight
"Hello, World!".upper()                 # "HELLO, WORLD!"
```


## Grammar reference

```
File = {Statement | newline} eof .

Statement = DefStmt | IfStmt | ForStmt | SimpleStmt .

DefStmt = 'def' identifier '(' [Parameters [',']] ')' ':' Suite .

Parameters = Parameter {',' Parameter}.

Parameter  = identifier
           | identifier '=' Expression
           | '*'
           | '*' identifier
           | '**' identifier
           .

IfStmt = 'if' Expression ':' Suite {'elif' Expression ':' Suite} ['else' ':' Suite] .

ForStmt = 'for' LoopVariables 'in' Expressions ':' Suite .

Suite = [newline indent {Statement} outdent] | SimpleStmt .

SimpleStmt = SmallStmt {';' SmallStmt} [';'] '\n' .
# NOTE: '\n' optional at EOF

SmallStmt = ReturnStmt
          | BreakStmt | ContinueStmt | PassStmt
          | AssignStmt
          | ExprStmt
          | LoadStmt
          .

ReturnStmt   = 'return' [Expressions] .
BreakStmt    = 'break' .
ContinueStmt = 'continue' .
PassStmt     = 'pass' .
AssignStmt   = Expressions ('=' | '+=' | '-=' | '*=' | '/=' | '//=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=') Expressions .
ExprStmt     = Expressions .

LoadStmt = 'load' '(' string {',' [identifier '='] string} [','] ')' .

Expression = IfExpr | PrimaryExpr | UnaryExpr | BinaryExpr | LambdaExpr .

IfExpr = Expression 'if' Expression 'else' Expression .

PrimaryExpr = Operand
            | PrimaryExpr DotSuffix
            | PrimaryExpr CallSuffix
            | PrimaryExpr SubscriptSuffix
            .

Operand = identifier
        | int | float | string | bytes
        | ListExpr | ListComp
        | DictExpr | DictComp
        | '(' [Expressions [',']] ')'
        .

DotSuffix   = '.' identifier .
SubscriptSuffix = '[' [Expressions] [':' Expression [':' Expression]] ']'
                | '[' Expressions ']'
                .
CallSuffix  = '(' [Arguments [',']] ')' .

Arguments = Argument {',' Argument} .
Argument  = Expression | identifier '=' Expression | '*' Expression | '**' Expression .

ListExpr = '[' [Expressions [',']] ']' .
ListComp = '[' Expression {CompClause} ']'.

DictExpr = '{' [Entries [',']] '}' .
DictComp = '{' Entry {CompClause} '}' .
Entries  = Entry {',' Entry} .
Entry    = Expression ':' Expression .

CompClause = 'for' LoopVariables 'in' Expression | 'if' Expression .

UnaryExpr = '+' Expression
          | '-' Expression
          | '~' Expression
          | 'not' Expression
          .

BinaryExpr = Expression {Binop Expression} .

Binop = 'or'
      | 'and'
      | '==' | '!=' | '<' | '>' | '<=' | '>=' | 'in' | 'not' 'in'
      | '|'
      | '^'
      | '&'
      | '<<' | '>>'
      | '-' | '+'
      | '*' | '%' | '/' | '//'
      .

LambdaExpr = 'lambda' [Parameters] ':' Expression .

Expressions = Expression {',' Expression} .
# NOTE: trailing comma permitted only when within [...] or (...).

LoopVariables = PrimaryExpr {',' PrimaryExpr} .
```

Tokens:

- spaces: newline, eof, indent, outdent.
- identifier.
- literals: string, bytes, int, float.
- plus all quoted tokens such as '+=', 'return'.

Notes:

- Ambiguity is resolved using operator precedence.
- The grammar does not enforce the legal order of params and args, nor that the first CompClause must be a 'for'.
