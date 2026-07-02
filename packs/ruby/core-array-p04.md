---
title: "class Array (part 4/4)"
source: https://ruby-doc.org/core/Array.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 4/4
---

# class Array

```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.sample(random: Random.new(1))     
a.sample(4, random: Random.new(1))  
```

Related: see Methods for Fetching.

```
def sample(n = (ary = false), random: Random)
  if Primitive.mandatory_only?
    
    Primitive.ary_sample0
  else
    
    Primitive.ary_sample(random, n, ary)
  end
end
```

select {|element| ... } → new_array

click to toggle source

select → new_enumerator

With a block given, calls the block with each element of `self`; returns a new array containing those elements of `self` for which the block returns a truthy value:

```
a = [:foo, 'bar', 2, :bam]
a.select {|element| element.to_s.start_with?('b') }
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Fetching.

```
static VALUE
rb_ary_select(VALUE ary)
{
    VALUE result;
    long i;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    result = rb_ary_new2(RARRAY_LEN(ary));
    for (i = 0; i < RARRAY_LEN(ary); i++) {
        if (RTEST(rb_yield(RARRAY_AREF(ary, i)))) {
            rb_ary_push(result, rb_ary_elt(ary, i));
        }
    }
    return result;
}
```

Also aliased as:

filter

, filter

select! {|element| ... } → self or nil

click to toggle source

select! → new_enumerator

With a block given, calls the block with each element of `self`; removes from `self` those elements for which the block returns `false` or `nil`.

Returns `self` if any elements were removed:

```
a = [:foo, 'bar', 2, :bam]
a.select! {|element| element.to_s.start_with?('b') } 
```

Returns `nil` if no elements were removed.

With no block given, returns a new `Enumerator`.

Related: see Methods for Deleting.

```
static VALUE
rb_ary_select_bang(VALUE ary)
{
    struct select_bang_arg args;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    rb_ary_modify(ary);

    args.ary = ary;
    args.len[0] = args.len[1] = 0;
    return rb_ensure(select_bang_i, (VALUE)&args, select_bang_ensure, (VALUE)&args);
}
```

Also aliased as:

filter!

shift → object or nil

click to toggle source

shift(count) → new_array or nil

Removes and returns leading elements from `self`.

With no argument, removes and returns one element, if available, or `nil` otherwise:

```
a = [0, 1, 2, 3]
a.shift  
a        
[].shift 
```

With non-negative numeric argument `count` given, removes and returns the first `count` elements:

```
a = [0, 1, 2, 3]
a.shift(2)   
a            
a.shift(1.1) 
a            
a.shift(0)   
a            
```

If `count` is large, removes and returns all elements:

```
a = [0, 1, 2, 3]
a.shift(50) 
a           
```

If `self` is empty, returns a new empty array.

Related: see Methods for Deleting.

```
static VALUE
rb_ary_shift_m(int argc, VALUE *argv, VALUE ary)
{
    VALUE result;
    long n;

    if (argc == 0) {
        return rb_ary_shift(ary);
    }

    rb_ary_modify_check(ary);
    result = ary_take_first_or_last(argc, argv, ary, ARY_TAKE_FIRST);
    n = RARRAY_LEN(result);
    rb_ary_behead(ary,n);

    return result;
}
```

shuffle(random: Random) → new_array

click to toggle source

Returns a new array containing all elements from `self` in a random order, as selected by the object given by the keyword argument `random`:

```
a =            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.shuffle 
a.shuffle 
```

Duplicate elements are included:

```
a =            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
a.shuffle 
a.shuffle 
```

The object given with the keyword argument `random` is used as the random number generator.

Related: see Methods for Fetching.

```
def shuffle(random: Random)
  Primitive.rb_ary_shuffle(random)
end
```

shuffle!(random: Random) → self

click to toggle source

Shuffles all elements in `self` into a random order, as selected by the object given by the keyword argument `random`. Returns `self`:

```
a =             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.shuffle! 
a.shuffle! 
```

Duplicate elements are included:

```
a =             [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
a.shuffle! 
a.shuffle! 
```

The object given with the keyword argument `random` is used as the random number generator.

Related: see Methods for Assigning.

```
def shuffle!(random: Random)
  Primitive.rb_ary_shuffle_bang(random)
end
```

size → integer

Returns the count of elements in `self`:

```
[0, 1, 2].length 
[].length        
```

Related: see Methods for Querying.

Alias for:

length

slice(index) → object or nil

slice(start, length) → object or nil

slice(range) → object or nil

slice(aseq) → object or nil

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

Alias for:

[]

slice!(index) → object or nil

click to toggle source

slice!(start, length) → new_array or nil

slice!(range) → new_array or nil

Removes and returns elements from `self`.

With numeric argument `index` given, removes and returns the element at offset `index`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(2)   
a             
a.slice!(2.1) 
a             
```

If `index` is negative, counts backwards from the end of `self`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(-2) 
a            
```

If `index` is out of range, returns `nil`.

With numeric arguments `start` and `length` given, removes `length` elements from `self` beginning at zero-based offset `start`; returns the removed objects in a new array:

```
a = ['a', 'b', 'c', 'd']
a.slice!(1, 2)     
a                  
a.slice!(0.1, 1.1) 
a                  
```

If `start` is negative, counts backwards from the end of `self`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(-2, 1) 
a               
```

If `start` is out-of-range, returns `nil`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(5, 1)  
a.slice!(-5, 1) 
```

If `start + length` exceeds the array size, removes and returns all elements from offset `start` to the end:

```
a = ['a', 'b', 'c', 'd']
a.slice!(2, 50) 
a               
```

If `start == a.size` and `length` is non-negative, returns a new empty array.

If `length` is negative, returns `nil`.

With `Range` argument `range` given, treats `range.min` as `start` (as above) and `range.size` as `length` (as above):

```
a = ['a', 'b', 'c', 'd']
a.slice!(1..2) 
a              
```

If `range.start == a.size`, returns a new empty array:

```
a = ['a', 'b', 'c', 'd']
a.slice!(4..5) 
```

If `range.start` is larger than the array size, returns `nil`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(5..6) 
```

If `range.start` is negative, calculates the start index by counting backwards from the end of `self`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(-2..2) 
```

If `range.end` is negative, calculates the end index by counting backwards from the end of `self`:

```
a = ['a', 'b', 'c', 'd']
a.slice!(0..-2) 
```

Related: see Methods for Deleting.

```
static VALUE
rb_ary_slice_bang(int argc, VALUE *argv, VALUE ary)
{
    VALUE arg1;
    long pos, len;

    rb_ary_modify_check(ary);
    rb_check_arity(argc, 1, 2);
    arg1 = argv[0];

    if (argc == 2) {
        pos = NUM2LONG(argv[0]);
        len = NUM2LONG(argv[1]);
        return ary_slice_bang_by_rb_ary_splice(ary, pos, len);
    }

    if (!FIXNUM_P(arg1)) {
        switch (rb_range_beg_len(arg1, &pos, &len, RARRAY_LEN(ary), 0)) {
          case Qtrue:
            /* valid range */
            return ary_slice_bang_by_rb_ary_splice(ary, pos, len);
          case Qnil:
            /* invalid range */
            return Qnil;
          default:
            /* not a range */
            break;
        }
    }

    return rb_ary_delete_at(ary, NUM2LONG(arg1));
}
```

sort → new_array

click to toggle source

sort {|a, b| ... } → new_array

Returns a new array containing the elements of `self`, sorted.

With no block given, compares elements using operator `#<=>` (see Object#<=>):

```
[0, 2, 3, 1].sort 
```

With a block given, calls the block with each combination of pairs of elements from `self`; for each pair `a` and `b`, the block should return a numeric:

- Negative when `b` is to follow `a`.
- Zero when `a` and `b` are equivalent.
- Positive when `a` is to follow `b`.

Example:

```
a = [3, 2, 0, 1]
a.sort {|a, b| a <=> b } 
a.sort {|a, b| b <=> a } 
```

When the block returns zero, the order for `a` and `b` is indeterminate, and may be unstable.

Related: see Methods for Fetching.

```
VALUE
rb_ary_sort(VALUE ary)
{
    ary = rb_ary_dup(ary);
    rb_ary_sort_bang(ary);
    return ary;
}
```

sort! → self

click to toggle source

sort! {|a, b| ... } → self

Like `Array#sort`, but returns `self` with its elements sorted in place.

Related: see Methods for Assigning.

```
VALUE
rb_ary_sort_bang(VALUE ary)
{
    rb_ary_modify(ary);
    RUBY_ASSERT(!ARY_SHARED_P(ary));
    if (RARRAY_LEN(ary) > 1) {
        VALUE tmp = ary_make_substitution(ary); /* only ary refers tmp */
        struct ary_sort_data data;
        long len = RARRAY_LEN(ary);
        RBASIC_CLEAR_CLASS(tmp);
        data.ary = tmp;
        data.receiver = ary;
        RARRAY_PTR_USE(tmp, ptr, {
            ruby_qsort(ptr, len, sizeof(VALUE),
                       rb_block_given_p()?sort_1:sort_2, &data);
        }); /* WB: no new reference */
        rb_ary_modify(ary);
        if (ARY_EMBED_P(tmp)) {
            if (ARY_SHARED_P(ary)) { /* ary might be destructively operated in the given block */
                rb_ary_unshare(ary);
                FL_SET_EMBED(ary);
            }
            if (ARY_EMBED_LEN(tmp) > ARY_CAPA(ary)) {
                ary_resize_capa(ary, ARY_EMBED_LEN(tmp));
            }
            ary_memcpy(ary, 0, ARY_EMBED_LEN(tmp), ARY_EMBED_PTR(tmp));
            ARY_SET_LEN(ary, ARY_EMBED_LEN(tmp));
        }
        else {
            if (!ARY_EMBED_P(ary) && ARY_HEAP_PTR(ary) == ARY_HEAP_PTR(tmp)) {
                FL_UNSET_SHARED(ary);
                ARY_SET_CAPA(ary, RARRAY_LEN(tmp));
            }
            else {
                RUBY_ASSERT(!ARY_SHARED_P(tmp));
                if (ARY_EMBED_P(ary)) {
                    FL_UNSET_EMBED(ary);
                }
                else if (ARY_SHARED_P(ary)) {
                    /* ary might be destructively operated in the given block */
                    rb_ary_unshare(ary);
                }
                else {
                    ary_heap_free(ary);
                }
                ARY_SET_PTR(ary, ARY_HEAP_PTR(tmp));
                ARY_SET_HEAP_LEN(ary, len);
                ARY_SET_CAPA(ary, ARY_HEAP_LEN(tmp));
            }
            /* tmp was lost ownership for the ptr */
            FL_UNSET(tmp, FL_FREEZE);
            FL_SET_EMBED(tmp);
            ARY_SET_EMBED_LEN(tmp, 0);
            FL_SET(tmp, FL_FREEZE);
        }
        /* tmp will be GC'ed. */
        RBASIC_SET_CLASS_RAW(tmp, rb_cArray); /* rb_cArray must be marked */
    }
    ary_verify(ary);
    return ary;
}
```

sort_by! {|element| ... } → self

click to toggle source

sort_by! → new_enumerator

With a block given, sorts the elements of `self` in place; returns self.

Calls the block with each successive element; sorts elements based on the values returned from the block:

```
a = ['aaaa', 'bbb', 'cc', 'd']
a.sort_by! {|element| element.size }
a 
```

For duplicate values returned by the block, the ordering is indeterminate, and may be unstable.

With no block given, returns a new `Enumerator`.

Related: see Methods for Assigning.

```
static VALUE
rb_ary_sort_by_bang(VALUE ary)
{
    VALUE sorted;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    rb_ary_modify(ary);
    sorted = rb_block_call(ary, rb_intern("sort_by"), 0, 0, sort_by_i, 0);
    rb_ary_replace(ary, sorted);
    return ary;
}
```

sum(init = 0) → object

click to toggle source

sum(init = 0) {|element| ... } → object

With no block given, returns the sum of `init` and all elements of `self`; for array `array` and value `init`, equivalent to:

```
sum = init
array.each {|element| sum += element }
sum
```

For example, `[e0, e1, e2].sum` returns `init + e0 + e1 + e2`.

Examples:

```
[0, 1, 2, 3].sum                 
[0, 1, 2, 3].sum(100)            
['abc', 'def', 'ghi'].sum('jkl') 
[[:foo, :bar], ['foo', 'bar']].sum([2, 3])
```

The `init` value and elements need not be numeric, but must all be `+`-compatible:

```
[[:foo, :bar], ['foo', 'bar']].sum(2)
```

With a block given, calls the block with each element of `self`; the block’s return value (instead of the element itself) is used as the addend:

```
['zero', 1, :two].sum('Coerced and concatenated: ') {|element| element.to_s }
```

Notes:

- `Array#join` and `Array#flatten` may be faster than `Array#sum` for an array of strings or an array of arrays.
- `Array#sum` method may not respect method redefinition of “+” methods such as `Integer#+`.

```
static VALUE
rb_ary_sum(int argc, VALUE *argv, VALUE ary)
{
    VALUE e, v, r;
    long i, n;
    int block_given;

    v = (rb_check_arity(argc, 0, 1) ? argv[0] : LONG2FIX(0));

    block_given = rb_block_given_p();

    if (RARRAY_LEN(ary) == 0)
        return v;

    n = 0;
    r = Qundef;

    if (!FIXNUM_P(v) && !RB_BIGNUM_TYPE_P(v) && !RB_TYPE_P(v, T_RATIONAL)) {
        i = 0;
        goto init_is_a_value;
    }

    for (i = 0; i < RARRAY_LEN(ary); i++) {
        e = RARRAY_AREF(ary, i);
        if (block_given)
            e = rb_yield(e);
        if (FIXNUM_P(e)) {
            n += FIX2LONG(e); /* should not overflow long type */
            if (!FIXABLE(n)) {
                v = rb_big_plus(LONG2NUM(n), v);
                n = 0;
            }
        }
        else if (RB_BIGNUM_TYPE_P(e))
            v = rb_big_plus(e, v);
        else if (RB_TYPE_P(e, T_RATIONAL)) {
            if (UNDEF_P(r))
                r = e;
            else
                r = rb_rational_plus(r, e);
        }
        else
            goto not_exact;
    }
    v = finish_exact_sum(n, r, v, argc!=0);
    return v;

  not_exact:
    v = finish_exact_sum(n, r, v, i!=0);

    if (RB_FLOAT_TYPE_P(e)) {
        /*
         * Kahan-Babuska balancing compensated summation algorithm
         * See https://link.springer.com/article/10.1007/s00607-005-0139-x
         */
        double f, c;
        double x, t;

        f = NUM2DBL(v);
        c = 0.0;
        goto has_float_value;
        for (; i < RARRAY_LEN(ary); i++) {
            e = RARRAY_AREF(ary, i);
            if (block_given)
                e = rb_yield(e);
            if (RB_FLOAT_TYPE_P(e))
              has_float_value:
                x = RFLOAT_VALUE(e);
            else if (FIXNUM_P(e))
                x = FIX2LONG(e);
            else if (RB_BIGNUM_TYPE_P(e))
                x = rb_big2dbl(e);
            else if (RB_TYPE_P(e, T_RATIONAL))
                x = rb_num2dbl(e);
            else
                goto not_float;

            if (isnan(f)) continue;
            if (isnan(x)) {
                f = x;
                continue;
            }
            if (isinf(x)) {
                if (isinf(f) && signbit(x) != signbit(f))
                    f = NAN;
                else
                    f = x;
                continue;
            }
            if (isinf(f)) continue;

            t = f + x;
            if (fabs(f) >= fabs(x))
                c += ((f - t) + x);
            else
                c += ((x - t) + f);
            f = t;
        }
        f += c;
        return DBL2NUM(f);

      not_float:
        v = DBL2NUM(f);
    }

    goto has_some_value;
    init_is_a_value:
    for (; i < RARRAY_LEN(ary); i++) {
        e = RARRAY_AREF(ary, i);
        if (block_given)
            e = rb_yield(e);
      has_some_value:
        v = rb_funcall(v, idPLUS, 1, e);
    }
    return v;
}
```

take(count) → new_array

click to toggle source

Returns a new array containing the first `count` element of `self` (as available); `count` must be a non-negative numeric; does not modify `self`:

```
a = ['a', 'b', 'c', 'd']
a.take(2)   
a.take(2.1) 
a.take(50)  
a.take(0)   
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_take(VALUE obj, VALUE n)
{
    long len = NUM2LONG(n);
    if (len < 0) {
        rb_raise(rb_eArgError, "attempt to take negative size");
    }
    return rb_ary_subseq(obj, 0, len);
}
```

take_while {|element| ... } → new_array

click to toggle source

take_while → new_enumerator

With a block given, calls the block with each successive element of `self`; stops iterating if the block returns `false` or `nil`; returns a new array containing those elements for which the block returned a truthy value:

```
a = [0, 1, 2, 3, 4, 5]
a.take_while {|element| element < 3 } 
a.take_while {|element| true }        
a.take_while {|element| false }       
```

With no block given, returns a new `Enumerator`.

Does not modify `self`.

Related: see Methods for Fetching.

```
static VALUE
rb_ary_take_while(VALUE ary)
{
    long i;

    RETURN_ENUMERATOR(ary, 0, 0);
    for (i = 0; i < RARRAY_LEN(ary); i++) {
        if (!RTEST(rb_yield(RARRAY_AREF(ary, i)))) break;
    }
    return rb_ary_take(ary, LONG2FIX(i));
}
```

to_a → self or new_array

click to toggle source

When `self` is an instance of `Array`, returns `self`.

Otherwise, returns a new array containing the elements of `self`:

```
class MyArray < Array; end
my_a = MyArray.new(['foo', 'bar', 'two'])
a = my_a.to_a
a 
a.class 
```

Related: see Methods for Converting.

```
static VALUE
rb_ary_to_a(VALUE ary)
{
    if (rb_obj_class(ary) != rb_cArray) {
        VALUE dup = rb_ary_new2(RARRAY_LEN(ary));
        rb_ary_replace(dup, ary);
        return dup;
    }
    return ary;
}
```

to_ary → self

click to toggle source

Returns `self`.

```
static VALUE
rb_ary_to_ary_m(VALUE ary)
{
    return ary;
}
```

to_h → new_hash

click to toggle source

to_h {|element| ... } → new_hash

Returns a new hash formed from `self`.

With no block given, each element of `self` must be a 2-element sub-array; forms each sub-array into a key-value pair in the new hash:

```
a = [['foo', 'zero'], ['bar', 'one'], ['baz', 'two']]
a.to_h 
[].to_h 
```

With a block given, the block must return a 2-element array; calls the block with each element of `self`; forms each returned array into a key-value pair in the returned hash:

```
a = ['foo', :bar, 1, [2, 3], {baz: 4}]
a.to_h {|element| [element, element.class] }
```

Related: see Methods for Converting.

```
static VALUE
rb_ary_to_h(VALUE ary)
{
    long i;
    VALUE hash = rb_hash_new_with_size(RARRAY_LEN(ary));
    int block_given = rb_block_given_p();

    for (i=0; i<RARRAY_LEN(ary); i++) {
        const VALUE e = rb_ary_elt(ary, i);
        const VALUE elt = block_given ? rb_yield_force_blockarg(e) : e;
        const VALUE key_value_pair = rb_check_array_type(elt);
        if (NIL_P(key_value_pair)) {
            rb_raise(rb_eTypeError, "wrong element type %"PRIsVALUE" at %ld (expected array)",
                     rb_obj_class(elt), i);
        }
        if (RARRAY_LEN(key_value_pair) != 2) {
            rb_raise(rb_eArgError, "wrong array length at %ld (expected 2, was %ld)",
                i, RARRAY_LEN(key_value_pair));
        }
        rb_hash_aset(hash, RARRAY_AREF(key_value_pair, 0), RARRAY_AREF(key_value_pair, 1));
    }
    return hash;
}
```

to_s → new_string

Returns the new string formed by calling method `#inspect` on each array element:

```
a = [:foo, 'bar', 2]
a.inspect 
```

Related: see Methods for Converting.

Alias for:

inspect

transpose → new_array

click to toggle source

Returns a new array that is `self` as a transposed matrix:

```
a = [[:a0, :a1], [:b0, :b1], [:c0, :c1]]
a.transpose 
```

The elements of `self` must all be the same size.

Related: see Methods for Converting.

```
static VALUE
rb_ary_transpose(VALUE ary)
{
    long elen = -1, alen, i, j;
    VALUE tmp, result = 0;

    alen = RARRAY_LEN(ary);
    if (alen == 0) return rb_ary_dup(ary);
    for (i=0; i<alen; i++) {
        tmp = to_ary(rb_ary_elt(ary, i));
        if (elen < 0) {         /* first element */
            elen = RARRAY_LEN(tmp);
            result = rb_ary_new2(elen);
            for (j=0; j<elen; j++) {
                rb_ary_store(result, j, rb_ary_new2(alen));
            }
        }
        else if (elen != RARRAY_LEN(tmp)) {
            rb_raise(rb_eIndexError, "element size differs (%ld should be %ld)",
                     RARRAY_LEN(tmp), elen);
        }
        for (j=0; j<elen; j++) {
            rb_ary_store(rb_ary_elt(result, j), i, rb_ary_elt(tmp, j));
        }
    }
    return result;
}
```

union(*other_arrays) → new_array

click to toggle source

Returns a new array that is the union of the elements of `self` and all given arrays `other_arrays`; items are compared using `eql?`:

```
[0, 1, 2, 3].union([4, 5], [6, 7]) 
```

Removes duplicates (preserving the first found):

```
[0, 1, 1].union([2, 1], [3, 1]) 
```

Preserves order (preserving the position of the first found):

```
[3, 2, 1, 0].union([5, 3], [4, 2]) 
```

With no arguments given, returns a copy of `self`.

Related: see Methods for Combining.

```
static VALUE
rb_ary_union_multi(int argc, VALUE *argv, VALUE ary)
{
    int i;
    long sum;
    VALUE hash;

    sum = RARRAY_LEN(ary);
    for (i = 0; i < argc; i++) {
        argv[i] = to_ary(argv[i]);
        sum += RARRAY_LEN(argv[i]);
    }

    if (sum <= SMALL_ARRAY_LEN) {
        VALUE ary_union = rb_ary_new();

        rb_ary_union(ary_union, ary);
        for (i = 0; i < argc; i++) rb_ary_union(ary_union, argv[i]);

        return ary_union;
    }

    hash = ary_make_hash(ary);
    for (i = 0; i < argc; i++) rb_ary_union_hash(hash, argv[i]);

    return rb_hash_values(hash);
}
```

uniq → new_array

click to toggle source

uniq {|element| ... } → new_array

Returns a new array containing those elements from `self` that are not duplicates, the first occurrence always being retained.

With no block given, identifies and omits duplicate elements using method `eql?` to compare elements:

```
a = [0, 0, 1, 1, 2, 2]
a.uniq 
```

With a block given, calls the block for each element; identifies and omits “duplicate” elements using method `eql?` to compare *block return values*; that is, an element is a duplicate if its block return value is the same as that of a previous element:

```
a = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
a.uniq {|element| element.size } 
```

Related: Methods for Fetching.

```
static VALUE
rb_ary_uniq(VALUE ary)
{
    VALUE hash, uniq;

    if (RARRAY_LEN(ary) <= 1) {
        hash = 0;
        uniq = rb_ary_dup(ary);
    }
    else if (rb_block_given_p()) {
        hash = ary_make_hash_by(ary);
        uniq = rb_hash_values(hash);
    }
    else {
        hash = ary_make_hash(ary);
        uniq = rb_hash_values(hash);
    }

    return uniq;
}
```

uniq! → self or nil

click to toggle source

uniq! {|element| ... } → self or nil

Removes duplicate elements from `self`, the first occurrence always being retained; returns `self` if any elements removed, `nil` otherwise.

With no block given, identifies and removes elements using method `eql?` to compare elements:

```
a = [0, 0, 1, 1, 2, 2]
a.uniq! 
a.uniq! 
```

With a block given, calls the block for each element; identifies and omits “duplicate” elements using method `eql?` to compare *block return values*; that is, an element is a duplicate if its block return value is the same as that of a previous element:

```
a = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
a.uniq! {|element| element.size } 
a.uniq! {|element| element.size } 
```

Related: see Methods for Deleting.

```
static VALUE
rb_ary_uniq_bang(VALUE ary)
{
    VALUE hash;
    long hash_size;

    rb_ary_modify_check(ary);
    if (RARRAY_LEN(ary) <= 1)
        return Qnil;
    if (rb_block_given_p())
        hash = ary_make_hash_by(ary);
    else
        hash = ary_make_hash(ary);

    hash_size = RHASH_SIZE(hash);
    if (RARRAY_LEN(ary) == hash_size) {
        return Qnil;
    }
    rb_ary_modify_check(ary);
    ARY_SET_LEN(ary, 0);
    if (ARY_SHARED_P(ary)) {
        rb_ary_unshare(ary);
        FL_SET_EMBED(ary);
    }
    ary_resize_capa(ary, hash_size);
    rb_hash_foreach(hash, push_value, ary);

    return ary;
}
```

unshift(*objects) → self

click to toggle source

Prepends the given `objects` to `self`:

```
a = [:foo, 'bar', 2]
a.unshift(:bam, :bat) 
```

Related: `Array#shift`; see also Methods for Assigning.

```
VALUE
rb_ary_unshift_m(int argc, VALUE *argv, VALUE ary)
{
    long len = RARRAY_LEN(ary);
    VALUE target_ary;

    if (argc == 0) {
        rb_ary_modify_check(ary);
        return ary;
    }

    target_ary = ary_ensure_room_for_unshift(ary, argc);
    ary_memcpy0(ary, 0, argc, argv, target_ary);
    ARY_SET_LEN(ary, len + argc);
    return ary;
}
```

Also aliased as:

prepend

values_at(*specifiers) → new_array

click to toggle source

Returns elements from `self` in a new array; does not modify `self`.

The objects included in the returned array are the elements of `self` selected by the given `specifiers`, each of which must be a numeric index or a `Range`.

In brief:

```
a = ['a', 'b', 'c', 'd']

a.values_at(2, 0, 2, 0)     
a.values_at(-4, -3, -2, -1) 
a.values_at(-50, 50)        

a.values_at(1..3)       
a.values_at(1...3)      
a.values_at(3..1)       

a.values_at(-3..3)  
a.values_at(-50..3)                          

a.values_at(1..-2)  
a.values_at(1..-50) 

a.values_at(2..3, 3, 0..1, 0) 
```

With no `specifiers` given, returns a new empty array:

```
a = ['a', 'b', 'c', 'd']
a.values_at 
```

For each numeric specifier `index`, includes an element:

- For each non-negative numeric specifier `index` that is in-range (less than `self.size`), includes the element at offset `index`:
  ```
a.values_at(0, 2)     
a.values_at(0.1, 2.9) 
  ```
- For each negative numeric `index` that is in-range (greater than or equal to `- self.size`), counts backwards from the end of `self`:
  ```
a.values_at(-1, -4) 
  ```

The given indexes may be in any order, and may repeat:

```
a.values_at(2, 0, 1, 0, 2) 
```

For each `index` that is out-of-range, includes `nil`:

```
a.values_at(4, -5) 
```

For each `Range` specifier `range`, includes elements according to `range.begin` and `range.end`:

- If both `range.begin` and `range.end` are non-negative and in-range (less than `self.size`), includes elements from index `range.begin` through `range.end - 1` (if `range.exclude_end?`), or through `range.end` (otherwise):
  ```
a.values_at(1..2)  
a.values_at(1...2) 
  ```
- If `range.begin` is negative and in-range (greater than or equal to `- self.size`), counts backwards from the end of `self`:
  ```
a.values_at(-2..3) 
  ```
- If `range.begin` is negative and out-of-range, raises an exception:
  ```
a.values_at(-5..3) 
  ```
- If `range.end` is positive and out-of-range, extends the returned array with `nil` elements:
  ```
a.values_at(1..5) 
  ```
- If `range.end` is negative and in-range, counts backwards from the end of `self`:
  ```
a.values_at(1..-2) 
  ```
- If `range.end` is negative and out-of-range, returns an empty array:
  ```
a.values_at(1..-5) 
  ```

The given ranges may be in any order and may repeat:

```
a.values_at(2..3, 0..1, 2..3) 
```

The given specifiers may be any mixture of indexes and ranges:

```
a.values_at(3, 1..2, 0, 2..3) 
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_values_at(int argc, VALUE *argv, VALUE ary)
{
    long i, olen = RARRAY_LEN(ary);
    VALUE result = rb_ary_new_capa(argc);
    for (i = 0; i < argc; ++i) {
        append_values_at_single(result, ary, olen, argv[i]);
    }
    RB_GC_GUARD(ary);
    return result;
}
```

zip(*other_arrays) → new_array

click to toggle source

zip(*other_arrays) {|sub_array| ... } → nil

With no block given, combines `self` with the collection of `other_arrays`; returns a new array of sub-arrays:

```
[0, 1].zip(['zero', 'one'], [:zero, :one])
```

Returned:

- The outer array is of size `self.size`.
- Each sub-array is of size `other_arrays.size + 1`.
- The *nth* sub-array contains (in order):
  - The *nth* element of `self`.
  - The *nth* element of each of the other arrays, as available.

Example:

```
a = [0, 1]
zipped = a.zip(['zero', 'one'], [:zero, :one])

zipped.size       
zipped.first.size 
```

When the other arrays are all the same size as `self`, the returned sub-arrays are a rearrangement containing exactly elements of all the arrays (including `self`), with no omissions or additions:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3]
c = [:c0, :c1, :c2, :c3]
d = a.zip(b, c)
pp d

[[:a0, :b0, :c0],
 [:a1, :b1, :c1],
 [:a2, :b2, :c2],
 [:a3, :b3, :c3]]
```

When one of the other arrays is smaller than `self`, pads the corresponding sub-array with `nil` elements:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2]
c = [:c0, :c1]
d = a.zip(b, c)
pp d

[[:a0, :b0, :c0],
 [:a1, :b1, :c1],
 [:a2, :b2, nil],
 [:a3, nil, nil]]
```

When one of the other arrays is larger than `self`, *ignores* its trailing elements:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3, :b4]
c = [:c0, :c1, :c2, :c3, :c4, :c5]
d = a.zip(b, c)
pp d

[[:a0, :b0, :c0],
 [:a1, :b1, :c1],
 [:a2, :b2, :c2],
 [:a3, :b3, :c3]]
```

With a block given, calls the block with each of the other arrays; returns `nil`:

```
d = []
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3]
c = [:c0, :c1, :c2, :c3]
a.zip(b, c) {|sub_array| d.push(sub_array.reverse) } 
pp d

[[:c0, :b0, :a0],
 [:c1, :b1, :a1],
 [:c2, :b2, :a2],
 [:c3, :b3, :a3]]
```

For an **object** in **other_arrays** that is not actually an array, forms the the “other array” as `object.to_ary`, if defined, or as `object.each.to_a` otherwise.

Related: see Methods for Converting.

```
static VALUE
rb_ary_zip(int argc, VALUE *argv, VALUE ary)
{
    int i, j;
    long len = RARRAY_LEN(ary);
    VALUE result = Qnil;

    for (i=0; i<argc; i++) {
        argv[i] = take_items(argv[i], len);
    }

    if (rb_block_given_p()) {
        int arity = rb_block_arity();

        if (arity > 1) {
            VALUE work, *tmp;

            tmp = ALLOCV_N(VALUE, work, argc+1);

            for (i=0; i<RARRAY_LEN(ary); i++) {
                tmp[0] = RARRAY_AREF(ary, i);
                for (j=0; j<argc; j++) {
                    tmp[j+1] = rb_ary_elt(argv[j], i);
                }
                rb_yield_values2(argc+1, tmp);
            }

            if (work) ALLOCV_END(work);
        }
        else {
            for (i=0; i<RARRAY_LEN(ary); i++) {
                VALUE tmp = rb_ary_new2(argc+1);

                rb_ary_push(tmp, RARRAY_AREF(ary, i));
                for (j=0; j<argc; j++) {
                    rb_ary_push(tmp, rb_ary_elt(argv[j], i));
                }
                rb_yield(tmp);
            }
        }
    }
    else {
        result = rb_ary_new_capa(len);

        for (i=0; i<len; i++) {
            VALUE tmp = rb_ary_new_capa(argc+1);

            rb_ary_push(tmp, RARRAY_AREF(ary, i));
            for (j=0; j<argc; j++) {
                rb_ary_push(tmp, rb_ary_elt(argv[j], i));
            }
            rb_ary_push(result, tmp);
        }
    }

    return result;
}
```

self | other_array → new_array

click to toggle source

Returns the union of `self` and `other_array`; duplicates are removed; order is preserved; items are compared using `eql?`:

```
[0, 1] | [2, 3] 
[0, 1, 1] | [2, 2, 3] 
[0, 1, 2] | [3, 2, 1, 0] 
```

Related: see Methods for Combining.

```
static VALUE
rb_ary_or(VALUE ary1, VALUE ary2)
{
    VALUE hash;

    ary2 = to_ary(ary2);
    if (RARRAY_LEN(ary1) + RARRAY_LEN(ary2) <= SMALL_ARRAY_LEN) {
        VALUE ary3 = rb_ary_new();
        rb_ary_union(ary3, ary1);
        rb_ary_union(ary3, ary2);
        return ary3;
    }

    hash = ary_make_hash(ary1);
    rb_ary_union_hash(hash, ary2);

    return rb_hash_values(hash);
}
```
