---
title: "class Array (part 2/4)"
source: https://ruby-doc.org/core/Array.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/4
---

## What’s Here¶ ↑

First, what’s elsewhere. Class `Array`:

- Inherits from class Object.
- Includes module Enumerable, which provides dozens of additional methods.

Here, class `Array` provides methods that are useful for:

- Creating an Array
- Querying
- Comparing
- Fetching
- Assigning
- Deleting
- Combining
- Iterating
- Converting
- And more.…

### Methods for Creating an `Array`¶ ↑

- `::[]`: Returns a new array populated with given objects.
- `::new`: Returns a new array.
- `::try_convert`: Returns a new array created from a given object.

See also Creating Arrays.

### Methods for Querying¶ ↑

- `all?`: Returns whether all elements meet a given criterion.
- `any?`: Returns whether any element meets a given criterion.
- `count`: Returns the count of elements that meet a given criterion.
- `empty?`: Returns whether there are no elements.
- `find_index` (aliased as `index`): Returns the index of the first element that meets a given criterion.
- `hash`: Returns the integer hash code.
- `include?`: Returns whether any element `==` a given object.
- `length` (aliased as `size`): Returns the count of elements.
- `none?`: Returns whether no element `==` a given object.
- `one?`: Returns whether exactly one element `==` a given object.
- `rindex`: Returns the index of the last element that meets a given criterion.

### Methods for Comparing¶ ↑

- #<=>: Returns -1, 0, or 1, as `self` is less than, equal to, or greater than a given object.
- `==`: Returns whether each element in `self` is `==` to the corresponding element in a given object.
- `eql?`: Returns whether each element in `self` is `eql?` to the corresponding element in a given object.

### Methods for Fetching¶ ↑

These methods do not modify `self`.

- `[]` (aliased as `slice`): Returns consecutive elements as determined by a given argument.
- `assoc`: Returns the first element that is an array whose first element `==` a given object.
- `at`: Returns the element at a given offset.
- `bsearch`: Returns an element selected via a binary search as determined by a given block.
- `bsearch_index`: Returns the index of an element selected via a binary search as determined by a given block.
- `compact`: Returns an array containing all non-`nil` elements.
- `dig`: Returns the object in nested objects that is specified by a given index and additional arguments.
- `drop`: Returns trailing elements as determined by a given index.
- `drop_while`: Returns trailing elements as determined by a given block.
- `fetch`: Returns the element at a given offset.
- `fetch_values`: Returns elements at given offsets.
- `first`: Returns one or more leading elements.
- `last`: Returns one or more trailing elements.
- `max`: Returns one or more maximum-valued elements, as determined by `#<=>` or a given block.
- `min`: Returns one or more minimum-valued elements, as determined by `#<=>` or a given block.
- `minmax`: Returns the minimum-valued and maximum-valued elements, as determined by `#<=>` or a given block.
- `rassoc`: Returns the first element that is an array whose second element `==` a given object.
- `reject`: Returns an array containing elements not rejected by a given block.
- `reverse`: Returns all elements in reverse order.
- `rotate`: Returns all elements with some rotated from one end to the other.
- `sample`: Returns one or more random elements.
- `select` (aliased as `filter`): Returns an array containing elements selected by a given block.
- `shuffle`: Returns elements in a random order.
- `sort`: Returns all elements in an order determined by `#<=>` or a given block.
- `take`: Returns leading elements as determined by a given index.
- `take_while`: Returns leading elements as determined by a given block.
- `uniq`: Returns an array containing non-duplicate elements.
- `values_at`: Returns the elements at given offsets.

### Methods for Assigning¶ ↑

These methods add, replace, or reorder elements in `self`.

- `<<`: Appends an element.
- `[]=`: Assigns specified elements with a given object.
- `concat`: Appends all elements from given arrays.
- `fill`: Replaces specified elements with specified objects.
- `flatten!`: Replaces each nested array in `self` with the elements from that array.
- `initialize_copy` (aliased as `replace`): Replaces the content of `self` with the content of a given array.
- `insert`: Inserts given objects at a given offset; does not replace elements.
- `push` (aliased as `append`): Appends elements.
- `reverse!`: Replaces `self` with its elements reversed.
- `rotate!`: Replaces `self` with its elements rotated.
- `shuffle!`: Replaces `self` with its elements in random order.
- `sort!`: Replaces `self` with its elements sorted, as determined by `#<=>` or a given block.
- `sort_by!`: Replaces `self` with its elements sorted, as determined by a given block.
- `unshift` (aliased as `prepend`): Prepends leading elements.

### Methods for Deleting¶ ↑

Each of these methods removes elements from `self`:

- `clear`: Removes all elements.
- `compact!`: Removes all `nil` elements.
- `delete`: Removes elements equal to a given object.
- `delete_at`: Removes the element at a given offset.
- `delete_if`: Removes elements specified by a given block.
- `keep_if`: Removes elements not specified by a given block.
- `pop`: Removes and returns the last element.
- `reject!`: Removes elements specified by a given block.
- `select!` (aliased as `filter!`): Removes elements not specified by a given block.
- `shift`: Removes and returns the first element.
- `slice!`: Removes and returns a sequence of elements.
- `uniq!`: Removes duplicates.

### Methods for Combining¶ ↑

- #&: Returns an array containing elements found both in `self` and a given array.
- `+`: Returns an array containing all elements of `self` followed by all elements of a given array.
- `-`: Returns an array containing all elements of `self` that are not found in a given array.
- #|: Returns an array containing all element of `self` and all elements of a given array, duplicates removed.
- `difference`: Returns an array containing all elements of `self` that are not found in any of the given arrays..
- `intersection`: Returns an array containing elements found both in `self` and in each given array.
- `product`: Returns or yields all combinations of elements from `self` and given arrays.
- `reverse`: Returns an array containing all elements of `self` in reverse order.
- `union`: Returns an array containing all elements of `self` and all elements of given arrays, duplicates removed.

### Methods for Iterating¶ ↑

- `combination`: Calls a given block with combinations of elements of `self`; a combination does not use the same element more than once.
- `cycle`: Calls a given block with each element, then does so again, for a specified number of times, or forever.
- `each`: Passes each element to a given block.
- `each_index`: Passes each element index to a given block.
- `permutation`: Calls a given block with permutations of elements of `self`; a permutation does not use the same element more than once.
- `repeated_combination`: Calls a given block with combinations of elements of `self`; a combination may use the same element more than once.
- `repeated_permutation`: Calls a given block with permutations of elements of `self`; a permutation may use the same element more than once.
- `reverse_each`: Passes each element, in reverse order, to a given block.

### Methods for Converting¶ ↑

- `collect` (aliased as `map`): Returns an array containing the block return-value for each element.
- `collect!` (aliased as `map!`): Replaces each element with a block return-value.
- `flatten`: Returns an array that is a recursive flattening of `self`.
- `inspect` (aliased as `to_s`): Returns a new `String` containing the elements.
- `join`: Returns a newsString containing the elements joined by the field separator.
- `to_a`: Returns `self` or a new array containing all elements.
- `to_ary`: Returns `self`.
- `to_h`: Returns a new hash formed from the elements.
- `transpose`: Transposes `self`, which must be an array of arrays.
- `zip`: Returns a new array of arrays containing `self` and given arrays.

### Other Methods¶ ↑

- `*`: Returns one of the following:
  - With integer argument `n`, a new array that is the concatenation of `n` copies of `self`.
  - With string argument `field_separator`, a new string that is equivalent to `join(field_separator)`.
- `pack`: Packs the elements into a binary sequence.
- `sum`: Returns a sum of elements according to either `+` or a given block.

### Public Class Methods

[]

(*args)

click to toggle source

Returns a new array, populated with the given objects:

```
Array[1, 'a', /^A/]    
Array[]                
Array.[](1, 'a', /^A/) 
```

Related: see Methods for Creating an Array.

```
static VALUE
rb_ary_s_create(int argc, VALUE *argv, VALUE klass)
{
    VALUE ary = ary_new(klass, argc);
    if (argc > 0 && argv) {
        ary_memcpy(ary, 0, argc, argv);
        ARY_SET_LEN(ary, argc);
    }

    return ary;
}
```

new → new_empty_array

click to toggle source

new(array) → new_array

new(size, default_value = nil) → new_array

new(size = 0) {|index| ... } → new_array

Returns a new array.

With no block and no argument given, returns a new empty array:

```
Array.new 
```

With no block and array argument given, returns a new array with the same elements:

```
Array.new([:foo, 'bar', 2]) 
```

With no block and integer argument given, returns a new array containing that many instances of the given `default_value`:

```
Array.new(0)    
Array.new(3)    
Array.new(2, 3) 
```

With a block given, returns an array of the given `size`; calls the block with each `index` in the range `(0...size)`; the element at that `index` in the returned array is the blocks return value:

```
Array.new(3)  {|index| "Element #{index}" } 
```

A common pitfall for new Rubyists is providing an expression as `default_value`:

```
array = Array.new(2, {})
array 
array[0][:a] = 1
array 
```

If you want the elements of the array to be distinct, you should pass a block:

```
array = Array.new(2) { {} }
array 
array[0][:a] = 1
array 
```

Raises `TypeError` if the first argument is not either an array or an integer-convertible object). Raises `ArgumentError` if the first argument is a negative integer.

Related: see Methods for Creating an Array.

```
static VALUE
rb_ary_initialize(int argc, VALUE *argv, VALUE ary)
{
    long len;
    VALUE size, val;

    rb_ary_modify(ary);
    if (argc == 0) {
        rb_ary_reset(ary);
        RUBY_ASSERT(ARY_EMBED_P(ary));
        RUBY_ASSERT(ARY_EMBED_LEN(ary) == 0);
        if (rb_block_given_p()) {
            rb_warning("given block not used");
        }
        return ary;
    }
    rb_scan_args(argc, argv, "02", &size, &val);
    if (argc == 1 && !FIXNUM_P(size)) {
        val = rb_check_array_type(size);
        if (!NIL_P(val)) {
            rb_ary_replace(ary, val);
            return ary;
        }
    }

    len = NUM2LONG(size);
    /* NUM2LONG() may call size.to_int, ary can be frozen, modified, etc */
    if (len < 0) {
        rb_raise(rb_eArgError, "negative array size");
    }
    if (len > ARY_MAX_SIZE) {
        rb_raise(rb_eArgError, "array size too big");
    }
    /* recheck after argument conversion */
    rb_ary_modify(ary);
    ary_resize_capa(ary, len);
    if (rb_block_given_p()) {
        long i;

        if (argc == 2) {
            rb_warn("block supersedes default value argument");
        }
        for (i=0; i<len; i++) {
            rb_ary_store(ary, i, rb_yield(LONG2NUM(i)));
            ARY_SET_LEN(ary, i + 1);
        }
    }
    else {
        ary_memfill(ary, 0, len, val);
        ARY_SET_LEN(ary, len);
    }
    return ary;
}
```

try_convert(object) → object, new_array, or nil

click to toggle source

Attempts to return an array, based on the given `object`.

If `object` is an array, returns `object`.

Otherwise if `object` responds to `:to_ary`. calls `object.to_ary`: if the return value is an array or `nil`, returns that value; if not, raises `TypeError`.

Otherwise returns `nil`.

Related: see Methods for Creating an Array.

```
static VALUE
rb_ary_s_try_convert(VALUE dummy, VALUE ary)
{
    return rb_check_array_type(ary);
}
```

### Public Instance Methods

self & other_array → new_array

click to toggle source

Returns a new array containing the *intersection* of `self` and `other_array`; that is, containing those elements found in both `self` and `other_array`:

```
[0, 1, 2, 3] & [1, 2] 
```

Omits duplicates:

```
[0, 1, 1, 0] & [0, 1] 
```

Preserves order from `self`:

```
[0, 1, 2] & [3, 2, 1, 0] 
```

Identifies common elements using method `#eql?` (as defined in each element of `self`).

Related: see Methods for Combining.

```
static VALUE
rb_ary_and(VALUE ary1, VALUE ary2)
{
    VALUE hash, ary3, v;
    st_data_t vv;
    long i;

    ary2 = to_ary(ary2);
    ary3 = rb_ary_new();
    if (RARRAY_LEN(ary1) == 0 || RARRAY_LEN(ary2) == 0) return ary3;

    if (RARRAY_LEN(ary1) <= SMALL_ARRAY_LEN && RARRAY_LEN(ary2) <= SMALL_ARRAY_LEN) {
        for (i=0; i<RARRAY_LEN(ary1); i++) {
            v = RARRAY_AREF(ary1, i);
            if (!rb_ary_includes_by_eql(ary2, v)) continue;
            if (rb_ary_includes_by_eql(ary3, v)) continue;
            rb_ary_push(ary3, v);
        }
        return ary3;
    }

    hash = ary_make_hash(ary2);

    for (i=0; i<RARRAY_LEN(ary1); i++) {
        v = RARRAY_AREF(ary1, i);
        vv = (st_data_t)v;
        if (rb_hash_stlike_delete(hash, &vv, 0)) {
            rb_ary_push(ary3, v);
        }
    }

    return ary3;
}
```

self * n → new_array

click to toggle source

self * string_separator → new_string

When non-negative integer argument `n` is given, returns a new array built by concatenating `n` copies of `self`:

```
a = ['x', 'y']
a * 3 
```

When string argument `string_separator` is given, equivalent to `self.join(string_separator)`:

```
[0, [0, 1], {foo: 0}] * ', ' 
```

```
static VALUE
rb_ary_times(VALUE ary, VALUE times)
{
    VALUE ary2, tmp;
    const VALUE *ptr;
    long t, len;

    tmp = rb_check_string_type(times);
    if (!NIL_P(tmp)) {
        return rb_ary_join(ary, tmp);
    }

    len = NUM2LONG(times);
    if (len == 0) {
        ary2 = ary_new(rb_cArray, 0);
        goto out;
    }
    if (len < 0) {
        rb_raise(rb_eArgError, "negative argument");
    }
    if (ARY_MAX_SIZE/len < RARRAY_LEN(ary)) {
        rb_raise(rb_eArgError, "argument too big");
    }
    len *= RARRAY_LEN(ary);

    ary2 = ary_new(rb_cArray, len);
    ARY_SET_LEN(ary2, len);

    ptr = RARRAY_CONST_PTR(ary);
    t = RARRAY_LEN(ary);
    if (0 < t) {
        ary_memcpy(ary2, 0, t, ptr);
        while (t <= len/2) {
            ary_memcpy(ary2, t, t, RARRAY_CONST_PTR(ary2));
            t *= 2;
        }
        if (t < len) {
            ary_memcpy(ary2, t, len-t, RARRAY_CONST_PTR(ary2));
        }
    }
  out:
    return ary2;
}
```

self + other_array → new_array

click to toggle source

Returns a new array containing all elements of `self` followed by all elements of `other_array`:

```
a = [0, 1] + [2, 3]
a 
```

Related: see Methods for Combining.

```
VALUE
rb_ary_plus(VALUE x, VALUE y)
{
    VALUE z;
    long len, xlen, ylen;

    y = to_ary(y);
    xlen = RARRAY_LEN(x);
    ylen = RARRAY_LEN(y);
    len = xlen + ylen;
    z = rb_ary_new2(len);

    ary_memcpy(z, 0, xlen, RARRAY_CONST_PTR(x));
    ary_memcpy(z, xlen, ylen, RARRAY_CONST_PTR(y));
    ARY_SET_LEN(z, len);
    return z;
}
```

self - other_array → new_array

click to toggle source

Returns a new array containing only those elements of `self` that are not found in `other_array`; the order from `self` is preserved:

```
[0, 1, 1, 2, 1, 1, 3, 1, 1] - [1]             
[0, 1, 1, 2, 1, 1, 3, 1, 1] - [3, 2, 0, :foo] 
[0, 1, 2] - [:foo]                            
```

Element are compared using method `#eql?` (as defined in each element of `self`).

Related: see Methods for Combining.

```
VALUE
rb_ary_diff(VALUE ary1, VALUE ary2)
{
    VALUE ary3;
    VALUE hash;
    long i;

    ary2 = to_ary(ary2);
    if (RARRAY_LEN(ary2) == 0) { return ary_make_shared_copy(ary1); }
    ary3 = rb_ary_new();

    if (RARRAY_LEN(ary1) <= SMALL_ARRAY_LEN || RARRAY_LEN(ary2) <= SMALL_ARRAY_LEN) {
        for (i=0; i<RARRAY_LEN(ary1); i++) {
            VALUE elt = rb_ary_elt(ary1, i);
            if (rb_ary_includes_by_eql(ary2, elt)) continue;
            rb_ary_push(ary3, elt);
        }
        return ary3;
    }

    hash = ary_make_hash(ary2);
    for (i=0; i<RARRAY_LEN(ary1); i++) {
        if (rb_hash_stlike_lookup(hash, RARRAY_AREF(ary1, i), NULL)) continue;
        rb_ary_push(ary3, rb_ary_elt(ary1, i));
    }

    return ary3;
}
```

self << object → self

click to toggle source

Appends `object` as the last element in `self`; returns `self`:

```
[:foo, 'bar', 2] << :baz 
```

Appends `object` as a single element, even if it is another array:

```
[:foo, 'bar', 2] << [3, 4] 
```

Related: see Methods for Assigning.

```
VALUE
rb_ary_push(VALUE ary, VALUE item)
{
    long idx = RARRAY_LEN((ary_verify(ary), ary));
    VALUE target_ary = ary_ensure_room_for_push(ary, 1);
    RARRAY_PTR_USE(ary, ptr, {
        RB_OBJ_WRITE(target_ary, &ptr[idx], item);
    });
    ARY_SET_LEN(ary, idx + 1);
    ary_verify(ary);
    return ary;
}
```

self <=> other_array → -1, 0, or 1

click to toggle source

Returns -1, 0, or 1 as `self` is determined to be less than, equal to, or greater than `other_array`.

Iterates over each index `i` in `(0...self.size)`:

- Computes `result[i]` as `self[i] <=> other_array[i]`.
- Immediately returns 1 if `result[i]` is 1:
  ```
[0, 1, 2] <=> [0, 0, 2] 
  ```
- Immediately returns -1 if `result[i]` is -1:
  ```
[0, 1, 2] <=> [0, 2, 2] 
  ```
- Continues if `result[i]` is 0.

When every `result` is 0, returns `self.size <=> other_array.size` (see Integer#<=>):

```
[0, 1, 2] <=> [0, 1]        
[0, 1, 2] <=> [0, 1, 2]     
[0, 1, 2] <=> [0, 1, 2, 3]  
```

Note that when `other_array` is larger than `self`, its trailing elements do not affect the result:

```
[0, 1, 2] <=> [0, 1, 2, -3] 
[0, 1, 2] <=> [0, 1, 2, 0]  
[0, 1, 2] <=> [0, 1, 2, 3]  
```

Related: see Methods for Comparing.

```
VALUE
rb_ary_cmp(VALUE ary1, VALUE ary2)
{
    long len;
    VALUE v;

    ary2 = rb_check_array_type(ary2);
    if (NIL_P(ary2)) return Qnil;
    if (ary1 == ary2) return INT2FIX(0);
    v = rb_exec_recursive_paired(recursive_cmp, ary1, ary2, ary2);
    if (!UNDEF_P(v)) return v;
    len = RARRAY_LEN(ary1) - RARRAY_LEN(ary2);
    if (len == 0) return INT2FIX(0);
    if (len > 0) return INT2FIX(1);
    return INT2FIX(-1);
}
```

self == other_array → true or false

click to toggle source

Returns whether both:

- `self` and `other_array` are the same size.
- Their corresponding elements are the same; that is, for each index `i` in `(0...self.size)`, `self[i] == other_array[i]`.

Examples:

```
[:foo, 'bar', 2] == [:foo, 'bar', 2]   
[:foo, 'bar', 2] == [:foo, 'bar', 2.0] 
[:foo, 'bar', 2] == [:foo, 'bar']      
[:foo, 'bar', 2] == [:foo, 'bar', 3]   
```

This method is different from method `Array#eql?`, which compares elements using `Object#eql?`.

Related: see Methods for Comparing.

```
static VALUE
rb_ary_equal(VALUE ary1, VALUE ary2)
{
    if (ary1 == ary2) return Qtrue;
    if (!RB_TYPE_P(ary2, T_ARRAY)) {
        if (!rb_respond_to(ary2, idTo_ary)) {
            return Qfalse;
        }
        return rb_equal(ary2, ary1);
    }
    if (RARRAY_LEN(ary1) != RARRAY_LEN(ary2)) return Qfalse;
    if (RARRAY_CONST_PTR(ary1) == RARRAY_CONST_PTR(ary2)) return Qtrue;
    return rb_exec_recursive_paired(recursive_equal, ary1, ary2, ary2);
}
```

self[index] → object or nil

click to toggle source

self[start, length] → object or nil

self[range] → object or nil

self[aseq] → object or nil

Returns elements from `self`; does not modify `self`.

In brief:

```
a = [:foo, 'bar', 2]

a[0]     
a[-1]    

a[1, 2]  
a[-2, 2] 

a[0..1]  
a[0..-2] 
a[-2..2] 
```

When a single integer argument `index` is given, returns the element at offset `index`:

```
a = [:foo, 'bar', 2]
a[0] 
a[2] 
a 
```

If `index` is negative, counts backwards from the end of `self`:

```
a = [:foo, 'bar', 2]
a[-1] 
a[-2] 
```

If `index` is out of range, returns `nil`.

When two `Integer` arguments `start` and `length` are given, returns a new `Array` of size `length` containing successive elements beginning at offset `start`:

```
a = [:foo, 'bar', 2]
a[0, 2] 
a[1, 2] 
```

If `start + length` is greater than `self.length`, returns all elements from offset `start` to the end:

```
a = [:foo, 'bar', 2]
a[0, 4] 
a[1, 3] 
a[2, 2] 
```

If `start == self.size` and `length >= 0`, returns a new empty `Array`.

If `length` is negative, returns `nil`.

When a single `Range` argument `range` is given, treats `range.min` as `start` above and `range.size` as `length` above:

```
a = [:foo, 'bar', 2]
a[0..1] 
a[1..2] 
```

Special case: If `range.start == a.size`, returns a new empty `Array`.

If `range.end` is negative, calculates the end index from the end:

```
a = [:foo, 'bar', 2]
a[0..-1] 
a[0..-2] 
a[0..-3] 
```

If `range.start` is negative, calculates the start index from the end:

```
a = [:foo, 'bar', 2]
a[-1..2] 
a[-2..2] 
a[-3..2] 
```

If `range.start` is larger than the array size, returns `nil`.

```
a = [:foo, 'bar', 2]
a[4..1] 
a[4..0] 
a[4..-1] 
```

When a single `Enumerator::ArithmeticSequence` argument `aseq` is given, returns an `Array` of elements corresponding to the indexes produced by the sequence.

```
a = ['--', 'data1', '--', 'data2', '--', 'data3']
a[(1..).step(2)] 
```

Unlike slicing with range, if the start or the end of the arithmetic sequence is larger than array size, throws `RangeError`.

```
a = ['--', 'data1', '--', 'data2', '--', 'data3']
a[(1..11).step(2)]

a[(7..).step(2)]
```

If given a single argument, and its type is not one of the listed, tries to convert it to `Integer`, and raises if it is impossible:

```
a = [:foo, 'bar', 2]

a[:foo]
```

Related: see Methods for Fetching.

```
VALUE
rb_ary_aref(int argc, const VALUE *argv, VALUE ary)
{
    rb_check_arity(argc, 1, 2);
    if (argc == 2) {
        return rb_ary_aref2(ary, argv[0], argv[1]);
    }
    return rb_ary_aref1(ary, argv[0]);
}
```

Also aliased as:

slice

self[index] = object → object

click to toggle source

self[start, length] = object → object

self[range] = object → object

Assigns elements in `self`, based on the given `object`; returns `object`.

In brief:

```
a_orig = [:foo, 'bar', 2]

a = a_orig.dup
a[0] = 'foo' 
a 
a = a_orig.dup
a[7] = 'foo' 
a 

a = a_orig.dup
a[0, 2] = 'foo' 
a 
a = a_orig.dup
a[6, 50] = 'foo' 
a 

a = a_orig.dup
a[0..1] = 'foo' 
a 
a = a_orig.dup
a[6..50] = 'foo' 
a 
```

When `Integer` argument `index` is given, assigns `object` to an element in `self`.

If `index` is non-negative, assigns `object` the element at offset `index`:

```
a = [:foo, 'bar', 2]
a[0] = 'foo' 
a 
```

If `index` is greater than `self.length`, extends the array:

```
a = [:foo, 'bar', 2]
a[7] = 'foo' 
a 
```

If `index` is negative, counts backwards from the end of the array:

```
a = [:foo, 'bar', 2]
a[-1] = 'two' 
a 
```

When `Integer` arguments `start` and `length` are given and `object` is not an `Array`, removes `length - 1` elements beginning at offset `start`, and assigns `object` at offset `start`:

```
a = [:foo, 'bar', 2]
a[0, 2] = 'foo' 
a 
```

If `start` is negative, counts backwards from the end of the array:

```
a = [:foo, 'bar', 2]
a[-2, 2] = 'foo' 
a 
```

If `start` is non-negative and outside the array (`>= self.size`), extends the array with `nil`, assigns `object` at offset `start`, and ignores `length`:

```
a = [:foo, 'bar', 2]
a[6, 50] = 'foo' 
a 
```

If `length` is zero, shifts elements at and following offset `start` and assigns `object` at offset `start`:

```
a = [:foo, 'bar', 2]
a[1, 0] = 'foo' 
a 
```

If `length` is too large for the existing array, does not extend the array:

```
a = [:foo, 'bar', 2]
a[1, 5] = 'foo' 
a 
```

When `Range` argument `range` is given and `object` is not an `Array`, removes `length - 1` elements beginning at offset `start`, and assigns `object` at offset `start`:

```
a = [:foo, 'bar', 2]
a[0..1] = 'foo' 
a 
```

if `range.begin` is negative, counts backwards from the end of the array:

```
a = [:foo, 'bar', 2]
a[-2..2] = 'foo' 
a 
```

If the array length is less than `range.begin`, extends the array with `nil`, assigns `object` at offset `range.begin`, and ignores `length`:

```
a = [:foo, 'bar', 2]
a[6..50] = 'foo' 
a 
```

If `range.end` is zero, shifts elements at and following offset `start` and assigns `object` at offset `start`:

```
a = [:foo, 'bar', 2]
a[1..0] = 'foo' 
a 
```

If `range.end` is negative, assigns `object` at offset `start`, retains `range.end.abs -1` elements past that, and removes those beyond:

```
a = [:foo, 'bar', 2]
a[1..-1] = 'foo' 
a 
a = [:foo, 'bar', 2]
a[1..-2] = 'foo' 
a 
a = [:foo, 'bar', 2]
a[1..-3] = 'foo' 
a 
a = [:foo, 'bar', 2]
```

If `range.end` is too large for the existing array, replaces array elements, but does not extend the array with `nil` values:

```
a = [:foo, 'bar', 2]
a[1..5] = 'foo' 
a 
```

Related: see Methods for Assigning.

```
static VALUE
rb_ary_aset(int argc, VALUE *argv, VALUE ary)
{
    long offset, beg, len;

    rb_check_arity(argc, 2, 3);
    rb_ary_modify_check(ary);
    if (argc == 3) {
        beg = NUM2LONG(argv[0]);
        len = NUM2LONG(argv[1]);
        return ary_aset_by_rb_ary_splice(ary, beg, len, argv[2]);
    }
    if (FIXNUM_P(argv[0])) {
        offset = FIX2LONG(argv[0]);
        return ary_aset_by_rb_ary_store(ary, offset, argv[1]);
    }
    if (rb_range_beg_len(argv[0], &beg, &len, RARRAY_LEN(ary), 1)) {
        /* check if idx is Range */
        return ary_aset_by_rb_ary_splice(ary, beg, len, argv[1]);
    }

    offset = NUM2LONG(argv[0]);
    return ary_aset_by_rb_ary_store(ary, offset, argv[1]);
}
```

all? → true or false

click to toggle source

all?(object) → true or false

all? {|element| ... } → true or false

Returns whether for every element of `self`, a given criterion is satisfied.

With no block and no argument, returns whether every element of `self` is truthy:

```
[[], {}, '', 0, 0.0, Object.new].all? 
[[], {}, '', 0, 0.0, nil].all?        
[[], {}, '', 0, 0.0, false].all?      
```

With argument `object` given, returns whether `object === ele` for every element `ele` in `self`:

```
[0, 0, 0].all?(0)                    
[0, 1, 2].all?(1)                    
['food', 'fool', 'foot'].all?(/foo/) 
['food', 'drink'].all?(/foo/)        
```

With a block given, calls the block with each element in `self`; returns whether the block returns only truthy values:

```
[0, 1, 2].all? { |ele| ele < 3 } 
[0, 1, 2].all? { |ele| ele < 2 } 
```

With both a block and argument `object` given, ignores the block and uses `object` as above.

**Special case**: returns `true` if `self` is empty (regardless of any given argument or block).

Related: see Methods for Querying.

```
static VALUE
rb_ary_all_p(int argc, VALUE *argv, VALUE ary)
{
    long i, len = RARRAY_LEN(ary);

    rb_check_arity(argc, 0, 1);
    if (!len) return Qtrue;
    if (argc) {
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (!RTEST(rb_funcall(argv[0], idEqq, 1, RARRAY_AREF(ary, i)))) return Qfalse;
        }
    }
    else if (!rb_block_given_p()) {
        for (i = 0; i < len; ++i) {
            if (!RTEST(RARRAY_AREF(ary, i))) return Qfalse;
        }
    }
    else {
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (!RTEST(rb_yield(RARRAY_AREF(ary, i)))) return Qfalse;
        }
    }
    return Qtrue;
}
```

any? → true or false

click to toggle source

any?(object) → true or false

any? {|element| ... } → true or false

Returns whether for any element of `self`, a given criterion is satisfied.

With no block and no argument, returns whether any element of `self` is truthy:

```
[nil, false, []].any? 
[nil, false, {}].any? 
[nil, false, ''].any? 
[nil, false].any?     
```

With argument `object` given, returns whether `object === ele` for any element `ele` in `self`:

```
[nil, false, 0].any?(0)          
[nil, false, 1].any?(0)          
[nil, false, 'food'].any?(/foo/) 
[nil, false, 'food'].any?(/bar/) 
```

With a block given, calls the block with each element in `self`; returns whether the block returns any truthy value:

```
[0, 1, 2].any? {|ele| ele < 1 } 
[0, 1, 2].any? {|ele| ele < 0 } 
```

With both a block and argument `object` given, ignores the block and uses `object` as above.

**Special case**: returns `false` if `self` is empty (regardless of any given argument or block).

Related: see Methods for Querying.

```
static VALUE
rb_ary_any_p(int argc, VALUE *argv, VALUE ary)
{
    long i, len = RARRAY_LEN(ary);

    rb_check_arity(argc, 0, 1);
    if (!len) return Qfalse;
    if (argc) {
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (RTEST(rb_funcall(argv[0], idEqq, 1, RARRAY_AREF(ary, i)))) return Qtrue;
        }
    }
    else if (!rb_block_given_p()) {
        for (i = 0; i < len; ++i) {
            if (RTEST(RARRAY_AREF(ary, i))) return Qtrue;
        }
    }
    else {
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (RTEST(rb_yield(RARRAY_AREF(ary, i)))) return Qtrue;
        }
    }
    return Qfalse;
}
```

append(*objects) → self

Appends each argument in `objects` to `self`; returns `self`:

```
a = [:foo, 'bar', 2] 
a.push(:baz, :bat)   
```

Appends each argument as a single element, even if it is another array:

```
a = [:foo, 'bar', 2]               
a.push([:baz, :bat], [:bam, :bad]) 
```

Related: see Methods for Assigning.

Alias for:

push

assoc(object) → found_array or nil

click to toggle source

Returns the first element `ele` in `self` such that `ele` is an array and `ele[0] == object`:

```
a = [{foo: 0}, [2, 4], [4, 5, 6], [4, 5]]
a.assoc(4) 
```

Returns `nil` if no such element is found.

Related: `Array#rassoc`; see also Methods for Fetching.

```
VALUE
rb_ary_assoc(VALUE ary, VALUE key)
{
    long i;
    VALUE v;

    for (i = 0; i < RARRAY_LEN(ary); ++i) {
        v = rb_check_array_type(RARRAY_AREF(ary, i));
        if (!NIL_P(v) && RARRAY_LEN(v) > 0 &&
            rb_equal(RARRAY_AREF(v, 0), key))
            return v;
    }
    return Qnil;
}
```

at(index) → object or nil

click to toggle source

Returns the element of `self` specified by the given `index` or `nil` if there is no such element; `index` must be an integer-convertible object.

For non-negative `index`, returns the element of `self` at offset `index`:

```
a = [:foo, 'bar', 2]
a.at(0)   
a.at(2)   
a.at(2.0) 
```

For negative `index`, counts backwards from the end of `self`:

```
a.at(-2) 
```

Related: `Array#[]`; see also Methods for Fetching.

```
VALUE
rb_ary_at(VALUE ary, VALUE pos)
{
    return rb_ary_entry(ary, NUM2LONG(pos));
}
```

bsearch {|element| ... } → found_element or nil

click to toggle source

bsearch → new_enumerator

Returns the element from `self` found by a binary search, or `nil` if the search found no suitable element.

See Binary Searching.

Related: see Methods for Fetching.

```
static VALUE
rb_ary_bsearch(VALUE ary)
{
    VALUE index_result = rb_ary_bsearch_index(ary);

    if (FIXNUM_P(index_result)) {
        return rb_ary_entry(ary, FIX2LONG(index_result));
    }
    return index_result;
}
```

bsearch_index {|element| ... } → integer or nil

click to toggle source

bsearch_index → new_enumerator

Returns the integer index of the element from `self` found by a binary search, or `nil` if the search found no suitable element.

See Binary Searching.

Related: see Methods for Fetching.

```
static VALUE
rb_ary_bsearch_index(VALUE ary)
{
    long low = 0, high = RARRAY_LEN(ary), mid;
    int smaller = 0, satisfied = 0;
    VALUE v, val;

    RETURN_ENUMERATOR(ary, 0, 0);
    while (low < high) {
        mid = low + ((high - low) / 2);
        val = rb_ary_entry(ary, mid);
        v = rb_yield(val);
        if (FIXNUM_P(v)) {
            if (v == INT2FIX(0)) return INT2FIX(mid);
            smaller = (SIGNED_VALUE)v < 0; /* Fixnum preserves its sign-bit */
        }
        else if (v == Qtrue) {
            satisfied = 1;
            smaller = 1;
        }
        else if (!RTEST(v)) {
            smaller = 0;
        }
        else if (rb_obj_is_kind_of(v, rb_cNumeric)) {
            const VALUE zero = INT2FIX(0);
            switch (rb_cmpint(rb_funcallv(v, id_cmp, 1, &zero), v, zero)) {
              case 0: return INT2FIX(mid);
              case 1: smaller = 0; break;
              case -1: smaller = 1;
            }
        }
        else {
            rb_raise(rb_eTypeError, "wrong argument type %"PRIsVALUE
                     " (must be numeric, true, false or nil)",
                     rb_obj_class(v));
        }
        if (smaller) {
            high = mid;
        }
        else {
            low = mid + 1;
        }
    }
    if (!satisfied) return Qnil;
    return INT2FIX(low);
}
```

clear → self

click to toggle source

Removes all elements from `self`; returns `self`:

```
a = [:foo, 'bar', 2]
a.clear 
```

Related: see Methods for Deleting.

```
VALUE
rb_ary_clear(VALUE ary)
{
    rb_ary_modify_check(ary);
    if (ARY_SHARED_P(ary)) {
        rb_ary_unshare(ary);
        FL_SET_EMBED(ary);
        ARY_SET_EMBED_LEN(ary, 0);
    }
    else {
        ARY_SET_LEN(ary, 0);
        if (ARY_DEFAULT_SIZE * 2 < ARY_CAPA(ary)) {
            ary_resize_capa(ary, ARY_DEFAULT_SIZE * 2);
        }
    }
    ary_verify(ary);
    return ary;
}
```

collect {|element| ... } → new_array

click to toggle source

collect → new_enumerator

With a block given, calls the block with each element of `self`; returns a new array whose elements are the return values from the block:

```
a = [:foo, 'bar', 2]
a1 = a.map {|element| element.class }
a1 
```

With no block given, returns a new `Enumerator`.

Related: `collect!`; see also Methods for Converting.

```
static VALUE
rb_ary_collect(VALUE ary)
{
    long i;
    VALUE collect;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    collect = rb_ary_new2(RARRAY_LEN(ary));
    for (i = 0; i < RARRAY_LEN(ary); i++) {
        rb_ary_push(collect, rb_yield(RARRAY_AREF(ary, i)));
    }
    return collect;
}
```

Also aliased as:

map

collect! {|element| ... } → new_array

click to toggle source

collect! → new_enumerator

With a block given, calls the block with each element of `self` and replaces the element with the block’s return value; returns `self`:

```
a = [:foo, 'bar', 2]
a.map! { |element| element.class } 
```

With no block given, returns a new `Enumerator`.

Related: `collect`; see also Methods for Converting.

```
static VALUE
rb_ary_collect_bang(VALUE ary)
{
    long i;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    rb_ary_modify(ary);
    for (i = 0; i < RARRAY_LEN(ary); i++) {
        rb_ary_store(ary, i, rb_yield(RARRAY_AREF(ary, i)));
    }
    return ary;
}
```

Also aliased as:

map!

combination(count) {|element| ... } → self

click to toggle source

combination(count) → new_enumerator

When a block and a positive integer-convertible object argument `count` (`0 < count <= self.size`) are given, calls the block with each combination of `self` of size `count`; returns `self`:

```
a = %w[a b c]                                   
a.combination(2) {|combination| p combination } 
```

Output:

```
["a", "b"]
["a", "c"]
["b", "c"]
```

The order of the yielded combinations is not guaranteed.

When `count` is zero, calls the block once with a new empty array:

```
a.combination(0) {|combination| p combination }
[].combination(0) {|combination| p combination }
```

Output:

```
[]
[]
```

When `count` is negative or larger than `self.size` and `self` is non-empty, does not call the block:

```
a.combination(-1) {|combination| fail 'Cannot happen' } 
a.combination(4)  {|combination| fail 'Cannot happen' } 
```

With no block given, returns a new `Enumerator`.

Related: `Array#permutation`; see also Methods for Iterating.

```
static VALUE
rb_ary_combination(VALUE ary, VALUE num)
{
    long i, n, len;

    n = NUM2LONG(num);
    RETURN_SIZED_ENUMERATOR(ary, 1, &num, rb_ary_combination_size);
    len = RARRAY_LEN(ary);
    if (n < 0 || len < n) {
        /* yield nothing */
    }
    else if (n == 0) {
        rb_yield(rb_ary_new2(0));
    }
    else if (n == 1) {
        for (i = 0; i < RARRAY_LEN(ary); i++) {
            rb_yield(rb_ary_new3(1, RARRAY_AREF(ary, i)));
        }
    }
    else {
        VALUE ary0 = ary_make_shared_copy(ary); /* private defensive copy of ary */
        volatile VALUE t0;
        long *stack = ALLOCV_N(long, t0, n+1);

        RBASIC_CLEAR_CLASS(ary0);
        combinate0(len, n, stack, ary0);
        ALLOCV_END(t0);
        RBASIC_SET_CLASS_RAW(ary0, rb_cArray);
    }
    return ary;
}
```

compact → new_array

click to toggle source

Returns a new array containing only the non-`nil` elements from `self`; element order is preserved:

```
a = [nil, 0, nil, false, nil, '', nil, [], nil, {}]
a.compact 
```

Related: `Array#compact!`; see also Methods for Deleting.

```
static VALUE
rb_ary_compact(VALUE ary)
{
    ary = rb_ary_dup(ary);
    rb_ary_compact_bang(ary);
    return ary;
}
```

compact! → self or nil

click to toggle source

Removes all `nil` elements from `self`; Returns `self` if any elements are removed, `nil` otherwise:

```
a = [nil, 0, nil, false, nil, '', nil, [], nil, {}]
a.compact! 
a          
a.compact! 
```

Related: `Array#compact`; see also Methods for Deleting.

```
static VALUE
rb_ary_compact_bang(VALUE ary)
{
    VALUE *p, *t, *end;
    long n;

    rb_ary_modify(ary);
    p = t = (VALUE *)RARRAY_CONST_PTR(ary); /* WB: no new reference */
    end = p + RARRAY_LEN(ary);

    while (t < end) {
        if (NIL_P(*t)) t++;
        else *p++ = *t++;
    }
    n = p - RARRAY_CONST_PTR(ary);
    if (RARRAY_LEN(ary) == n) {
        return Qnil;
    }
    ary_resize_smaller(ary, n);

    return ary;
}
```

concat(*other_arrays) → self

click to toggle source

Adds to `self` all elements from each array in `other_arrays`; returns `self`:

```
a = [0, 1]
a.concat(['two', 'three'], [:four, :five], a)
```

Related: see Methods for Assigning.

```
static VALUE
rb_ary_concat_multi(int argc, VALUE *argv, VALUE ary)
{
    rb_ary_modify_check(ary);

    if (argc == 1) {
        rb_ary_concat(ary, argv[0]);
    }
    else if (argc > 1) {
        int i;
        VALUE args = rb_ary_hidden_new(argc);
        for (i = 0; i < argc; i++) {
            rb_ary_concat(args, argv[i]);
        }
        ary_append(ary, args);
    }

    ary_verify(ary);
    return ary;
}
```

count → integer

click to toggle source

count(object) → integer

count {|element| ... } → integer

Returns a count of specified elements.

With no argument and no block, returns the count of all elements:

```
[0, :one, 'two', 3, 3.0].count 
```

With argument `object` given, returns the count of elements `==` to `object`:

```
[0, :one, 'two', 3, 3.0].count(3) 
```

With no argument and a block given, calls the block with each element; returns the count of elements for which the block returns a truthy value:

```
[0, 1, 2, 3].count {|element| element > 1 } 
```

With argument `object` and a block given, issues a warning, ignores the block, and returns the count of elements `==` to `object`.

Related: see Methods for Querying.

```
static VALUE
rb_ary_count(int argc, VALUE *argv, VALUE ary)
{
    long i, n = 0;

    if (rb_check_arity(argc, 0, 1) == 0) {
        VALUE v;

        if (!rb_block_given_p())
            return LONG2NUM(RARRAY_LEN(ary));

        for (i = 0; i < RARRAY_LEN(ary); i++) {
            v = RARRAY_AREF(ary, i);
            if (RTEST(rb_yield(v))) n++;
        }
    }
    else {
        VALUE obj = argv[0];

        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        for (i = 0; i < RARRAY_LEN(ary); i++) {
            if (rb_equal(RARRAY_AREF(ary, i), obj)) n++;
        }
    }

    return LONG2NUM(n);
}
```

cycle(count = nil) {|element| ... } → nil

click to toggle source

cycle(count = nil) → new_enumerator

With a block given, may call the block, depending on the value of argument `count`; `count` must be an integer-convertible object, or `nil`.

When `count` is positive, calls the block with each element, then does so repeatedly, until it has done so `count` times; returns `nil`:

```
output = []
[0, 1].cycle(2) {|element| output.push(element) } 
output 
```

When `count` is zero or negative, does not call the block:

```
[0, 1].cycle(0) {|element| fail 'Cannot happen' }  
[0, 1].cycle(-1) {|element| fail 'Cannot happen' } 
```

When `count` is `nil`, cycles forever:

```
[0, 1].cycle {|element| puts element }
[0, 1].cycle(nil) {|element| puts element }
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Iterating.

```
static VALUE
rb_ary_cycle(int argc, VALUE *argv, VALUE ary)
{
    long n, i;

    rb_check_arity(argc, 0, 1);

    RETURN_SIZED_ENUMERATOR(ary, argc, argv, rb_ary_cycle_size);
    if (argc == 0 || NIL_P(argv[0])) {
        n = -1;
    }
    else {
        n = NUM2LONG(argv[0]);
        if (n <= 0) return Qnil;
    }

    while (RARRAY_LEN(ary) > 0 && (n < 0 || 0 < n--)) {
        for (i=0; i<RARRAY_LEN(ary); i++) {
            rb_yield(RARRAY_AREF(ary, i));
        }
    }
    return Qnil;
}
```

delete(object) → last_removed_object

click to toggle source

delete(object) {|element| ... } → last_removed_object or block_return

Removes zero or more elements from `self`.

With no block given, removes from `self` each element `ele` such that `ele == object`; returns the last removed element:

```
a = [0, 1, 2, 2.0]
a.delete(2) 
a           
```

Returns `nil` if no elements removed:

```
a.delete(2) 
```

With a block given, removes from `self` each element `ele` such that `ele == object`.

If any such elements are found, ignores the block and returns the last removed element:

```
a = [0, 1, 2, 2.0]
a.delete(2) {|element| fail 'Cannot happen' } 
a                                             
```

If no such element is found, returns the block’s return value:

```
a.delete(2) {|element| "Element #{element} not found." }
```

Related: see Methods for Deleting.

```
VALUE
rb_ary_delete(VALUE ary, VALUE item)
{
    VALUE v = item;
    long i1, i2;

    for (i1 = i2 = 0; i1 < RARRAY_LEN(ary); i1++) {
        VALUE e = RARRAY_AREF(ary, i1);

        if (rb_equal(e, item)) {
            v = e;
            continue;
        }
        if (i1 != i2) {
            rb_ary_store(ary, i2, e);
        }
        i2++;
    }
    if (RARRAY_LEN(ary) == i2) {
        if (rb_block_given_p()) {
            return rb_yield(item);
        }
        return Qnil;
    }

    ary_resize_smaller(ary, i2);

    ary_verify(ary);
    return v;
}
```

delete_at(index) → removed_object or nil

click to toggle source

Removes the element of `self` at the given `index`, which must be an integer-convertible object.

When `index` is non-negative, deletes the element at offset `index`:

```
a = [:foo, 'bar', 2]
a.delete_at(1) 
a 
```

When `index` is negative, counts backward from the end of the array:

```
a = [:foo, 'bar', 2]
a.delete_at(-2) 
a 
```

When `index` is out of range, returns `nil`.

```
a = [:foo, 'bar', 2]
a.delete_at(3)  
a.delete_at(-4) 
```

Related: see Methods for Deleting.

```
static VALUE
rb_ary_delete_at_m(VALUE ary, VALUE pos)
{
    return rb_ary_delete_at(ary, NUM2LONG(pos));
}
```

delete_if {|element| ... } → self

click to toggle source

delete_if → new_numerator

With a block given, calls the block with each element of `self`; removes the element if the block returns a truthy value; returns `self`:

```
a = [:foo, 'bar', 2, 'bat']
a.delete_if {|element| element.to_s.start_with?('b') } 
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Deleting.

```
static VALUE
rb_ary_delete_if(VALUE ary)
{
    ary_verify(ary);
    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    ary_reject_bang(ary);
    return ary;
}
```

difference(*other_arrays = []) → new_array

click to toggle source

Returns a new array containing only those elements from `self` that are not found in any of the given `other_arrays`; items are compared using `eql?`; order from `self` is preserved:

```
[0, 1, 1, 2, 1, 1, 3, 1, 1].difference([1]) 
[0, 1, 2, 3].difference([3, 0], [1, 3])     
[0, 1, 2].difference([4])                   
[0, 1, 2].difference                        
```

Returns a copy of `self` if no arguments are given.

Related: `Array#-`; see also Methods for Combining.

```
static VALUE
rb_ary_difference_multi(int argc, VALUE *argv, VALUE ary)
{
    VALUE ary_diff;
    long i, length;
    volatile VALUE t0;
    bool *is_hash = ALLOCV_N(bool, t0, argc);
    ary_diff = rb_ary_new();
    length = RARRAY_LEN(ary);

    for (i = 0; i < argc; i++) {
        argv[i] = to_ary(argv[i]);
        is_hash[i] = (length > SMALL_ARRAY_LEN && RARRAY_LEN(argv[i]) > SMALL_ARRAY_LEN);
        if (is_hash[i]) argv[i] = ary_make_hash(argv[i]);
    }

    for (i = 0; i < RARRAY_LEN(ary); i++) {
        int j;
        VALUE elt = rb_ary_elt(ary, i);
        for (j = 0; j < argc; j++) {
            if (is_hash[j]) {
                if (rb_hash_stlike_lookup(argv[j], RARRAY_AREF(ary, i), NULL))
                    break;
            }
            else {
                if (rb_ary_includes_by_eql(argv[j], elt)) break;
            }
        }
        if (j == argc) rb_ary_push(ary_diff, elt);
    }

    ALLOCV_END(t0);

    return ary_diff;
}
```

dig(index, *identifiers) → object

click to toggle source

Finds and returns the object in nested object specified by `index` and `identifiers`; the nested objects may be instances of various classes. See Dig Methods.

Examples:

```
a = [:foo, [:bar, :baz, [:bat, :bam]]]
a.dig(1) 
a.dig(1, 2) 
a.dig(1, 2, 0) 
a.dig(1, 2, 3) 
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_dig(int argc, VALUE *argv, VALUE self)
{
    rb_check_arity(argc, 1, UNLIMITED_ARGUMENTS);
    self = rb_ary_at(self, *argv);
    if (!--argc) return self;
    ++argv;
    return rb_obj_dig(argc, argv, self, Qnil);
}
```

drop(count) → new_array

click to toggle source

Returns a new array containing all but the first `count` element of `self`, where `count` is a non-negative integer; does not modify `self`.

Examples:

```
a = [0, 1, 2, 3, 4, 5]
a.drop(0) 
a.drop(1) 
a.drop(2) 
a.drop(9) 
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_drop(VALUE ary, VALUE n)
{
    VALUE result;
    long pos = NUM2LONG(n);
    if (pos < 0) {
        rb_raise(rb_eArgError, "attempt to drop negative size");
    }

    result = rb_ary_subseq(ary, pos, RARRAY_LEN(ary));
    if (NIL_P(result)) result = rb_ary_new();
    return result;
}
```

drop_while {|element| ... } → new_array

click to toggle source

drop_while → new_enumerator

With a block given, calls the block with each successive element of `self`; stops if the block returns `false` or `nil`; returns a new array *omitting* those elements for which the block returned a truthy value; does not modify `self`:

```
a = [0, 1, 2, 3, 4, 5]
a.drop_while {|element| element < 3 } 
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Fetching.

```
static VALUE
rb_ary_drop_while(VALUE ary)
{
    long i;

    RETURN_ENUMERATOR(ary, 0, 0);
    for (i = 0; i < RARRAY_LEN(ary); i++) {
        if (!RTEST(rb_yield(RARRAY_AREF(ary, i)))) break;
    }
    return rb_ary_drop(ary, LONG2FIX(i));
}
```

each {|element| ... } → self

click to toggle source

each → new_enumerator

With a block given, iterates over the elements of `self`, passing each element to the block; returns `self`:

```
a = [:foo, 'bar', 2]
a.each {|element|  puts "#{element.class} #{element}" }
```

Output:

```
Symbol foo
String bar
Integer 2
```

Allows the array to be modified during iteration:

```
a = [:foo, 'bar', 2]
a.each {|element| puts element; a.clear if element.to_s.start_with?('b') }
```

Output:

```
foo
bar
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Iterating.

```
VALUE
rb_ary_each(VALUE ary)
{
    long i;
    ary_verify(ary);
    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    for (i=0; i<RARRAY_LEN(ary); i++) {
        rb_yield(RARRAY_AREF(ary, i));
    }
    return ary;
}
```

each_index {|index| ... } → self

click to toggle source

each_index → new_enumerator

With a block given, iterates over the elements of `self`, passing each *array index* to the block; returns `self`:

```
a = [:foo, 'bar', 2]
a.each_index {|index|  puts "#{index} #{a[index]}" }
```

Output:

```
0 foo
1 bar
2 2
```

Allows the array to be modified during iteration:

```
a = [:foo, 'bar', 2]
a.each_index {|index| puts index; a.clear if index > 0 }
a 
```

Output:

```
0
1
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Iterating.

```
static VALUE
rb_ary_each_index(VALUE ary)
{
    long i;
    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);

    for (i=0; i<RARRAY_LEN(ary); i++) {
        rb_yield(LONG2NUM(i));
    }
    return ary;
}
```

empty? → true or false

click to toggle source

Returns `true` if the count of elements in `self` is zero, `false` otherwise.

Related: see Methods for Querying.

```
static VALUE
rb_ary_empty_p(VALUE ary)
{
    return RBOOL(RARRAY_LEN(ary) == 0);
}
```

eql?(other_array) → true or false

click to toggle source

Returns `true` if `self` and `other_array` are the same size, and if, for each index `i` in `self`, `self[i].eql?(other_array[i])`:

```
a0 = [:foo, 'bar', 2]
a1 = [:foo, 'bar', 2]
a1.eql?(a0) 
```

Otherwise, returns `false`.

This method is different from method `Array#==`, which compares using method `Object#==`.

Related: see Methods for Querying.

```
static VALUE
rb_ary_eql(VALUE ary1, VALUE ary2)
{
    if (ary1 == ary2) return Qtrue;
    if (!RB_TYPE_P(ary2, T_ARRAY)) return Qfalse;
    if (RARRAY_LEN(ary1) != RARRAY_LEN(ary2)) return Qfalse;
    if (RARRAY_CONST_PTR(ary1) == RARRAY_CONST_PTR(ary2)) return Qtrue;
    return rb_exec_recursive_paired(recursive_eql, ary1, ary2, ary2);
}
```

fetch(index) → element

click to toggle source

fetch(index, default_value) → element or default_value

fetch(index) {|index| ... } → element or block_return_value

Returns the element of `self` at offset `index` if `index` is in range; `index` must be an integer-convertible object.

With the single argument `index` and no block, returns the element at offset `index`:

```
a = [:foo, 'bar', 2]
a.fetch(1)   
a.fetch(1.1) 
```

If `index` is negative, counts from the end of the array:

```
a = [:foo, 'bar', 2]
a.fetch(-1) 
a.fetch(-2) 
```

With arguments `index` and `default_value` (which may be any object) and no block, returns `default_value` if `index` is out-of-range:

```
a = [:foo, 'bar', 2]
a.fetch(1, nil)  
a.fetch(3, :foo) 
```

With argument `index` and a block, returns the element at offset `index` if index is in range (and the block is not called); otherwise calls the block with index and returns its return value:

```
a = [:foo, 'bar', 2]
a.fetch(1) {|index| raise 'Cannot happen' } 
a.fetch(50) {|index| "Value for #{index}" } 
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_fetch(int argc, VALUE *argv, VALUE ary)
{
    VALUE pos, ifnone;
    long block_given;
    long idx;

    rb_scan_args(argc, argv, "11", &pos, &ifnone);
    block_given = rb_block_given_p();
    if (block_given && argc == 2) {
        rb_warn("block supersedes default value argument");
    }
    idx = NUM2LONG(pos);

    if (idx < 0) {
        idx +=  RARRAY_LEN(ary);
    }
    if (idx < 0 || RARRAY_LEN(ary) <= idx) {
        if (block_given) return rb_yield(pos);
        if (argc == 1) {
            rb_raise(rb_eIndexError, "index %ld outside of array bounds: %ld...%ld",
                        idx - (idx < 0 ? RARRAY_LEN(ary) : 0), -RARRAY_LEN(ary), RARRAY_LEN(ary));
        }
        return ifnone;
    }
    return RARRAY_AREF(ary, idx);
}
```

fetch_values(*indexes) → new_array

click to toggle source

fetch_values(*indexes) { |index| ... } → new_array

With no block given, returns a new array containing the elements of `self` at the offsets specified by `indexes`. Each of the `indexes` must be an integer-convertible object:

```
a = [:foo, :bar, :baz]
a.fetch_values(2, 0)   
a.fetch_values(2.1, 0) 
a.fetch_values         
```

For a negative index, counts backwards from the end of the array:

```
a.fetch_values(-2, -1) 
```

When no block is given, raises an exception if any index is out of range.

With a block given, for each index:

- If the index is in range, uses an element of `self` (as above).
- Otherwise, calls the block with the index and uses the block’s return value.

Example:

```
a = [:foo, :bar, :baz]
a.fetch_values(1, 0, 42, 777) { |index| index.to_s }
```

Related: see Methods for Fetching.

```
def fetch_values(*indexes, &block)
  indexes.map! { |i| fetch(i, &block) }
  indexes
end
```

fill(object, start = nil, count = nil) → new_array

click to toggle source

fill(object, range) → new_array

fill(start = nil, count = nil) {|element| ... } → new_array

fill(range) {|element| ... } → new_array

Replaces selected elements in `self`; may add elements to `self`; always returns `self` (never a new array).

In brief:

```
['a', 'b', 'c', 'd'].fill('-', 1, 2)          
['a', 'b', 'c', 'd'].fill(1, 2) {|e| e.to_s } 

['a', 'b', 'c', 'd'].fill('-', 3, 2)          
['a', 'b', 'c', 'd'].fill(3, 2) {|e| e.to_s } 

['a', 'b', 'c', 'd'].fill('-', 6, 2)          
['a', 'b', 'c', 'd'].fill(6, 2) {|e| e.to_s } 

['a', 'b', 'c', 'd'].fill('-', -3, 3)          
['a', 'b', 'c', 'd'].fill(-3, 3) {|e| e.to_s } 

['a', 'b', 'c', 'd'].fill('-', 1..2)          
['a', 'b', 'c', 'd'].fill(1..2) {|e| e.to_s } 
```

When arguments `start` and `count` are given, they select the elements of `self` to be replaced; each must be an integer-convertible object (or `nil`):

- `start` specifies the zero-based offset of the first element to be replaced; `nil` means zero.
- `count` is the number of consecutive elements to be replaced; `nil` means “all the rest.”

With argument `object` given, that one object is used for all replacements:

```
o = Object.new           
a = ['a', 'b', 'c', 'd'] 
a.fill(o, 1, 2)
```

With a block given, the block is called once for each element to be replaced; the value passed to the block is the *index* of the element to be replaced (not the element itself); the block’s return value replaces the element:

```
a = ['a', 'b', 'c', 'd']               
a.fill(1, 2) {|element| element.to_s } 
```

For arguments `start` and `count`:

- If `start` is non-negative, replaces `count` elements beginning at offset `start`: Extends `self` if necessary: Fills with `nil` if necessary: Does nothing if `count` is non-positive:
  ```
['a', 'b', 'c', 'd'].fill('-', 0, 2) 
['a', 'b', 'c', 'd'].fill('-', 1, 2) 
['a', 'b', 'c', 'd'].fill('-', 2, 2) 

['a', 'b', 'c', 'd'].fill(0, 2) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(1, 2) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(2, 2) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', 3, 2) 
['a', 'b', 'c', 'd'].fill('-', 4, 2) 

['a', 'b', 'c', 'd'].fill(3, 2) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(4, 2) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', 5, 2) 
['a', 'b', 'c', 'd'].fill('-', 6, 2) 

['a', 'b', 'c', 'd'].fill(5, 2) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(6, 2) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', 2, 0)    
['a', 'b', 'c', 'd'].fill('-', 2, -100) 
['a', 'b', 'c', 'd'].fill('-', 6, -100) 

['a', 'b', 'c', 'd'].fill(2, 0) {|e| fail 'Cannot happen' }    
['a', 'b', 'c', 'd'].fill(2, -100) {|e| fail 'Cannot happen' } 
['a', 'b', 'c', 'd'].fill(6, -100) {|e| fail 'Cannot happen' } 
  ```
- If `start` is negative, counts backwards from the end of `self`: Extends `self` if necessary: Starts at the beginning of `self` if `start` is negative and out-of-range: Does nothing if `count` is non-positive:
  ```
['a', 'b', 'c', 'd'].fill('-', -4, 3) 
['a', 'b', 'c', 'd'].fill('-', -3, 3) 

['a', 'b', 'c', 'd'].fill(-4, 3) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(-3, 3) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', -2, 3) 
['a', 'b', 'c', 'd'].fill('-', -1, 3) 

['a', 'b', 'c', 'd'].fill(-2, 3) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(-1, 3) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', -5, 2) 
['a', 'b', 'c', 'd'].fill('-', -6, 2) 

['a', 'b', 'c', 'd'].fill(-5, 2) {|e| e.to_s } 
['a', 'b', 'c', 'd'].fill(-6, 2) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', -2, 0)  
['a', 'b', 'c', 'd'].fill('-', -2, -1) 

['a', 'b', 'c', 'd'].fill(-2, 0) {|e| fail 'Cannot happen' }  
['a', 'b', 'c', 'd'].fill(-2, -1) {|e| fail 'Cannot happen' } 
  ```

When argument `range` is given, it must be a `Range` object whose members are numeric; its `begin` and `end` values determine the elements of `self` to be replaced:

- If both `begin` and `end` are positive, they specify the first and last elements to be replaced: If `end` is smaller than `begin`, replaces no elements:
  ```
['a', 'b', 'c', 'd'].fill('-', 1..2)          
['a', 'b', 'c', 'd'].fill(1..2) {|e| e.to_s } 
  ```
  ```
['a', 'b', 'c', 'd'].fill('-', 2..1)          
['a', 'b', 'c', 'd'].fill(2..1) {|e| e.to_s } 
  ```
- If either is negative (or both are negative), counts backwards from the end of `self`:
  ```
['a', 'b', 'c', 'd'].fill('-', -3..2)  
['a', 'b', 'c', 'd'].fill('-', 1..-2)  
['a', 'b', 'c', 'd'].fill('-', -3..-2) 

['a', 'b', 'c', 'd'].fill(-3..2) {|e| e.to_s }  
['a', 'b', 'c', 'd'].fill(1..-2) {|e| e.to_s }  
['a', 'b', 'c', 'd'].fill(-3..-2) {|e| e.to_s } 
  ```
- If the `end` value is excluded (see `Range#exclude_end?`), omits the last replacement:
  ```
['a', 'b', 'c', 'd'].fill('-', 1...2)  
['a', 'b', 'c', 'd'].fill('-', 1...-2) 

['a', 'b', 'c', 'd'].fill(1...2) {|e| e.to_s }  
['a', 'b', 'c', 'd'].fill(1...-2) {|e| e.to_s } 
  ```
- If the range is endless (see Endless Ranges), replaces elements to the end of `self`:
  ```
['a', 'b', 'c', 'd'].fill('-', 1..)          
['a', 'b', 'c', 'd'].fill(1..) {|e| e.to_s } 
  ```
- If the range is beginless (see Beginless Ranges), replaces elements from the beginning of `self`:
  ```
['a', 'b', 'c', 'd'].fill('-', ..2)          
['a', 'b', 'c', 'd'].fill(..2) {|e| e.to_s } 
  ```

Related: see Methods for Assigning.

```
static VALUE
rb_ary_fill(int argc, VALUE *argv, VALUE ary)
{
    VALUE item = Qundef, arg1, arg2;
    long beg = 0, end = 0, len = 0;

    if (rb_block_given_p()) {
        rb_scan_args(argc, argv, "02", &arg1, &arg2);
        argc += 1;              /* hackish */
    }
    else {
        rb_scan_args(argc, argv, "12", &item, &arg1, &arg2);
    }
    switch (argc) {
      case 1:
        beg = 0;
        len = RARRAY_LEN(ary);
        break;
      case 2:
        if (rb_range_beg_len(arg1, &beg, &len, RARRAY_LEN(ary), 1)) {
            break;
        }
        /* fall through */
      case 3:
        beg = NIL_P(arg1) ? 0 : NUM2LONG(arg1);
        if (beg < 0) {
            beg = RARRAY_LEN(ary) + beg;
            if (beg < 0) beg = 0;
        }
        len = NIL_P(arg2) ? RARRAY_LEN(ary) - beg : NUM2LONG(arg2);
        break;
    }
    rb_ary_modify(ary);
    if (len < 0) {
        return ary;
    }
    if (beg >= ARY_MAX_SIZE || len > ARY_MAX_SIZE - beg) {
        rb_raise(rb_eArgError, "argument too big");
    }
    end = beg + len;
    if (RARRAY_LEN(ary) < end) {
        if (end >= ARY_CAPA(ary)) {
            ary_resize_capa(ary, end);
        }
        ary_mem_clear(ary, RARRAY_LEN(ary), end - RARRAY_LEN(ary));
        ARY_SET_LEN(ary, end);
    }

    if (UNDEF_P(item)) {
        VALUE v;
        long i;

        for (i=beg; i<end; i++) {
            v = rb_yield(LONG2NUM(i));
            if (i>=RARRAY_LEN(ary)) break;
            ARY_SET(ary, i, v);
        }
    }
    else {
        ary_memfill(ary, beg, len, item);
    }
    return ary;
}
```

filter {|element| ... } → new_array

filter → new_enumerator

With a block given, calls the block with each element of `self`; returns a new array containing those elements of `self` for which the block returns a truthy value:

```
a = [:foo, 'bar', 2, :bam]
a.select {|element| element.to_s.start_with?('b') }
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Fetching.

Alias for:

select

filter! {|element| ... } → self or nil

filter! → new_enumerator

With a block given, calls the block with each element of `self`; removes from `self` those elements for which the block returns `false` or `nil`.

Returns `self` if any elements were removed:

```
a = [:foo, 'bar', 2, :bam]
a.select! {|element| element.to_s.start_with?('b') } 
```

Returns `nil` if no elements were removed.

With no block given, returns a new `Enumerator`.

Related: see Methods for Deleting.

Alias for:

select!

find_index

-> new_enumerator

click to toggle source

Returns the zero-based integer index of a specified element, or `nil`.

With only argument `object` given, returns the index of the first element `element` for which `object == element`:

```
a = [:foo, 'bar', 2, 'bar']
a.index('bar') 
```

Returns `nil` if no such element found.

With only a block given, calls the block with each successive element; returns the index of the first element for which the block returns a truthy value:

```
a = [:foo, 'bar', 2, 'bar']
a.index {|element| element == 'bar' } 
```

Returns `nil` if the block never returns a truthy value.

With neither an argument nor a block given, returns a new `Enumerator`.

Related: see Methods for Querying.

```
static VALUE
rb_ary_index(int argc, VALUE *argv, VALUE ary)
{
    VALUE val;
    long i;

    if (argc == 0) {
        RETURN_ENUMERATOR(ary, 0, 0);
        for (i=0; i<RARRAY_LEN(ary); i++) {
            if (RTEST(rb_yield(RARRAY_AREF(ary, i)))) {
                return LONG2NUM(i);
            }
        }
        return Qnil;
    }
    rb_check_arity(argc, 0, 1);
    val = argv[0];
    if (rb_block_given_p())
        rb_warn("given block not used");
    for (i=0; i<RARRAY_LEN(ary); i++) {
        VALUE e = RARRAY_AREF(ary, i);
        if (rb_equal(e, val)) {
            return LONG2NUM(i);
        }
    }
    return Qnil;
}
```

Also aliased as:

index

first → object or nil

click to toggle source

first(count) → new_array

Returns elements from `self`, or `nil`; does not modify `self`.

With no argument given, returns the first element (if available):

```
a = [:foo, 'bar', 2]
a.first 
a 
```

If `self` is empty, returns `nil`.

```
[].first 
```

With a non-negative integer argument `count` given, returns the first `count` elements (as available) in a new array:

```
a.first(0)  
a.first(2)  
a.first(50) 
```

Related: see Methods for Querying.

```
def first n = unspecified = true
  if Primitive.mandatory_only?
    Primitive.attr! :leaf
    Primitive.cexpr! %q{ ary_first(self) }
  else
    if unspecified
      Primitive.cexpr! %q{ ary_first(self) }
    else
      Primitive.cexpr! %q{  ary_take_first_or_last_n(self, NUM2LONG(n), ARY_TAKE_FIRST) }
    end
  end
end
```

flatten(depth = nil) → new_array

click to toggle source

Returns a new array that is a recursive flattening of `self` to `depth` levels of recursion; `depth` must be an integer-convertible object or `nil`. At each level of recursion:

- Each element that is an array is “flattened” (that is, replaced by its individual array elements).
- Each element that is not an array is unchanged (even if the element is an object that has instance method `flatten`).

With non-negative integer argument `depth`, flattens recursively through `depth` levels:

```
a = [ 0, [ 1, [2, 3], 4 ], 5, {foo: 0}, Set.new([6, 7]) ]
a              
a.flatten(0)   
a.flatten(1  ) 
a.flatten(1.1) 
a.flatten(2)   
a.flatten(3)   
```

With `nil` or negative `depth`, flattens all levels.

```
a.flatten     
a.flatten(-1) 
```

Related: `Array#flatten!`; see also Methods for Converting.

```
static VALUE
rb_ary_flatten(int argc, VALUE *argv, VALUE ary)
{
    int level = -1;
    VALUE result;

    if (rb_check_arity(argc, 0, 1) && !NIL_P(argv[0])) {
        level = NUM2INT(argv[0]);
        if (level == 0) return ary_make_shared_copy(ary);
    }

    result = flatten(ary, level);
    if (result == ary) {
        result = ary_make_shared_copy(ary);
    }

    return result;
}
```

flatten!(depth = nil) → self or nil

click to toggle source

Returns `self` as a recursively flattening of `self` to `depth` levels of recursion; `depth` must be an integer-convertible object, or `nil`. At each level of recursion:

- Each element that is an array is “flattened” (that is, replaced by its individual array elements).
- Each element that is not an array is unchanged (even if the element is an object that has instance method `flatten`).

Returns `nil` if no elements were flattened.

With non-negative integer argument `depth`, flattens recursively through `depth` levels:

```
a = [ 0, [ 1, [2, 3], 4 ], 5, {foo: 0}, Set.new([6, 7]) ]
a                   
a.dup.flatten!(1)   
a.dup.flatten!(1.1) 
a.dup.flatten!(2)   
a.dup.flatten!(3)   
```

With `nil` or negative argument `depth`, flattens all levels:

```
a.dup.flatten!     
a.dup.flatten!(-1) 
```

Related: `Array#flatten`; see also Methods for Assigning.

```
static VALUE
rb_ary_flatten_bang(int argc, VALUE *argv, VALUE ary)
{
    int mod = 0, level = -1;
    VALUE result, lv;

    lv = (rb_check_arity(argc, 0, 1) ? argv[0] : Qnil);
    rb_ary_modify_check(ary);
    if (!NIL_P(lv)) level = NUM2INT(lv);
    if (level == 0) return Qnil;

    result = flatten(ary, level);
    if (result == ary) {
        return Qnil;
    }
    if (!(mod = ARY_EMBED_P(result))) rb_ary_freeze(result);
    rb_ary_replace(ary, result);
    if (mod) ARY_SET_EMBED_LEN(result, 0);

    return ary;
}
```

freeze → self

click to toggle source

Freezes `self` (if not already frozen); returns `self`:

```
a = []
a.frozen? 
a.freeze
a.frozen? 
```

No further changes may be made to `self`; raises `FrozenError` if a change is attempted.

Related: `Kernel#frozen?`.

```
VALUE
rb_ary_freeze(VALUE ary)
{
    RUBY_ASSERT(RB_TYPE_P(ary, T_ARRAY));

    if (OBJ_FROZEN(ary)) return ary;

    if (!ARY_EMBED_P(ary) && !ARY_SHARED_P(ary) && !ARY_SHARED_ROOT_P(ary)) {
        ary_shrink_capa(ary);
    }

    return rb_obj_freeze(ary);
}
```

hash → integer

click to toggle source

Returns the integer hash value for `self`.

Two arrays with the same content will have the same hash value (and will compare using eql?):

```
['a', 'b'].hash == ['a', 'b'].hash 
['a', 'b'].hash == ['a', 'c'].hash 
['a', 'b'].hash == ['a'].hash      
```

```
static VALUE
rb_ary_hash(VALUE ary)
{
    return rb_ary_hash_values(RARRAY_LEN(ary), RARRAY_CONST_PTR(ary));
}
```

include?(object) → true or false

click to toggle source

Returns whether for some element `element` in `self`, `object == element`:

```
[0, 1, 2].include?(2)   
[0, 1, 2].include?(2.0) 
[0, 1, 2].include?(2.1) 
```

Related: see Methods for Querying.

```
VALUE
rb_ary_includes(VALUE ary, VALUE item)
{
    long i;
    VALUE e;

    for (i=0; i<RARRAY_LEN(ary); i++) {
        e = RARRAY_AREF(ary, i);
        if (rb_equal(e, item)) {
            return Qtrue;
        }
    }
    return Qfalse;
}
```

index(object) → integer or nil

index {|element| ... } → integer or nil

index → new_enumerator

Returns the zero-based integer index of a specified element, or `nil`.

With only argument `object` given, returns the index of the first element `element` for which `object == element`:

```
a = [:foo, 'bar', 2, 'bar']
a.index('bar') 
```

Returns `nil` if no such element found.

With only a block given, calls the block with each successive element; returns the index of the first element for which the block returns a truthy value:

```
a = [:foo, 'bar', 2, 'bar']
a.index {|element| element == 'bar' } 
```

Returns `nil` if the block never returns a truthy value.

With neither an argument nor a block given, returns a new `Enumerator`.

Related: see Methods for Querying.

Alias for:

find_index

initialize_copy(other_array) → self

click to toggle source

Replaces the elements of `self` with the elements of `other_array`, which must be an array-convertible object; returns `self`:

```
a = ['a', 'b', 'c']   
a.replace(['d', 'e']) 
```

Related: see Methods for Assigning.

```
VALUE
rb_ary_replace(VALUE copy, VALUE orig)
{
    rb_ary_modify_check(copy);
    orig = to_ary(orig);
    if (copy == orig) return copy;

    rb_ary_reset(copy);

    /* orig has enough space to embed the contents of orig. */
    if (RARRAY_LEN(orig) <= ary_embed_capa(copy)) {
        RUBY_ASSERT(ARY_EMBED_P(copy));
        ary_memcpy(copy, 0, RARRAY_LEN(orig), RARRAY_CONST_PTR(orig));
        ARY_SET_EMBED_LEN(copy, RARRAY_LEN(orig));
    }
    /* orig is embedded but copy does not have enough space to embed the
     * contents of orig. */
    else if (ARY_EMBED_P(orig)) {
        long len = ARY_EMBED_LEN(orig);
        VALUE *ptr = ary_heap_alloc_buffer(len);

        FL_UNSET_EMBED(copy);
        ARY_SET_PTR(copy, ptr);
        ARY_SET_LEN(copy, len);
        ARY_SET_CAPA(copy, len);

        // No allocation and exception expected that could leave `copy` in a
        // bad state from the edits above.
        ary_memcpy(copy, 0, len, RARRAY_CONST_PTR(orig));
    }
    /* Otherwise, orig is on heap and copy does not have enough space to embed
     * the contents of orig. */
    else {
        VALUE shared_root = ary_make_shared(orig);
        FL_UNSET_EMBED(copy);
        ARY_SET_PTR(copy, ARY_HEAP_PTR(orig));
        ARY_SET_LEN(copy, ARY_HEAP_LEN(orig));
        rb_ary_set_shared(copy, shared_root);
    }
    ary_verify(copy);
    return copy;
}
```

Also aliased as:

replace

insert(index, *objects) → self

click to toggle source

Inserts the given `objects` as elements of `self`; returns `self`.

When `index` is non-negative, inserts `objects` *before* the element at offset `index`:

```
a = ['a', 'b', 'c']     
a.insert(1, :x, :y, :z) 
```

Extends the array if `index` is beyond the array (`index >= self.size`):

```
a = ['a', 'b', 'c']     
a.insert(5, :x, :y, :z) 
```

When `index` is negative, inserts `objects` *after* the element at offset `index + self.size`:

```
a = ['a', 'b', 'c']      
a.insert(-2, :x, :y, :z) 
```

With no `objects` given, does nothing:

```
a = ['a', 'b', 'c'] 
a.insert(1)         
a.insert(50)        
a.insert(-50)       
```

Raises `IndexError` if `objects` are given and `index` is negative and out of range.

Related: see Methods for Assigning.

```
static VALUE
rb_ary_insert(int argc, VALUE *argv, VALUE ary)
{
    long pos;

    rb_check_arity(argc, 1, UNLIMITED_ARGUMENTS);
    rb_ary_modify_check(ary);
    pos = NUM2LONG(argv[0]);
    if (argc == 1) return ary;
    if (pos == -1) {
        pos = RARRAY_LEN(ary);
    }
    else if (pos < 0) {
        long minpos = -RARRAY_LEN(ary) - 1;
        if (pos < minpos) {
            rb_raise(rb_eIndexError, "index %ld too small for array; minimum: %ld",
                     pos, minpos);
        }
        pos++;
    }
    rb_ary_splice(ary, pos, 0, argv + 1, argc - 1);
    return ary;
}
```

inspect → new_string

click to toggle source

Returns the new string formed by calling method `#inspect` on each array element:

```
a = [:foo, 'bar', 2]
a.inspect 
```

Related: see Methods for Converting.

```
static VALUE
rb_ary_inspect(VALUE ary)
{
    if (RARRAY_LEN(ary) == 0) return rb_usascii_str_new2("[]");
    return rb_exec_recursive(inspect_ary, ary, 0);
}
```

Also aliased as:

to_s

intersect?(other_array) → true or false

click to toggle source

Returns whether `other_array` has at least one element that is `#eql?` to some element of `self`:

```
[1, 2, 3].intersect?([3, 4, 5]) 
[1, 2, 3].intersect?([4, 5, 6]) 
```

Each element must correctly implement method `#hash`.

Related: see Methods for Querying.

```
static VALUE
rb_ary_intersect_p(VALUE ary1, VALUE ary2)
{
    VALUE hash, v, result, shorter, longer;
    st_data_t vv;
    long i;

    ary2 = to_ary(ary2);
    if (RARRAY_LEN(ary1) == 0 || RARRAY_LEN(ary2) == 0) return Qfalse;

    if (RARRAY_LEN(ary1) <= SMALL_ARRAY_LEN && RARRAY_LEN(ary2) <= SMALL_ARRAY_LEN) {
        for (i=0; i<RARRAY_LEN(ary1); i++) {
            v = RARRAY_AREF(ary1, i);
            if (rb_ary_includes_by_eql(ary2, v)) return Qtrue;
        }
        return Qfalse;
    }

    shorter = ary1;
    longer = ary2;
    if (RARRAY_LEN(ary1) > RARRAY_LEN(ary2)) {
        longer = ary1;
        shorter = ary2;
    }

    hash = ary_make_hash(shorter);
    result = Qfalse;

    for (i=0; i<RARRAY_LEN(longer); i++) {
        v = RARRAY_AREF(longer, i);
        vv = (st_data_t)v;
        if (rb_hash_stlike_lookup(hash, vv, 0)) {
            result = Qtrue;
            break;
        }
    }

    return result;
}
```

intersection(*other_arrays) → new_array

click to toggle source

Returns a new array containing each element in `self` that is `#eql?` to at least one element in each of the given `other_arrays`; duplicates are omitted:

```
[0, 0, 1, 1, 2, 3].intersection([0, 1, 2], [0, 1, 3]) 
```

Each element must correctly implement method `#hash`.

Order from `self` is preserved:
