---
title: "class Array (part 3/4)"
source: https://ruby-doc.org/core/Array.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 3/4
---

# class Array

```
[0, 1, 2].intersection([2, 1, 0]) 
```

Returns a copy of `self` if no arguments are given.

Related: see Methods for Combining.

```
static VALUE
rb_ary_intersection_multi(int argc, VALUE *argv, VALUE ary)
{
    VALUE result = rb_ary_dup(ary);
    int i;

    for (i = 0; i < argc; i++) {
        result = rb_ary_and(result, argv[i]);
    }

    return result;
}
```

join(separator = $,) → new_string

click to toggle source

Returns the new string formed by joining the converted elements of `self`; for each element `element`:

- Converts recursively using `element.join(separator)` if `element` is a `kind_of?(Array)`.
- Otherwise, converts using `element.to_s`.

With no argument given, joins using the output field separator, `$,`:

```
a = [:foo, 'bar', 2]
$, 
a.join 
```

With string argument `separator` given, joins using that separator:

```
a = [:foo, 'bar', 2]
a.join("\n") 
```

Joins recursively for nested arrays:

```
a = [:foo, [:bar, [:baz, :bat]]]
a.join 
```

Related: see Methods for Converting.

```
static VALUE
rb_ary_join_m(int argc, VALUE *argv, VALUE ary)
{
    VALUE sep;

    if (rb_check_arity(argc, 0, 1) == 0 || NIL_P(sep = argv[0])) {
        sep = rb_output_fs;
        if (!NIL_P(sep)) {
            rb_category_warn(RB_WARN_CATEGORY_DEPRECATED, "$, is set to non-nil value");
        }
    }

    return rb_ary_join(ary, sep);
}
```

keep_if {|element| ... } → self

click to toggle source

keep_if → new_enumerator

With a block given, calls the block with each element of `self`; removes the element from `self` if the block does not return a truthy value:

```
a = [:foo, 'bar', 2, :bam]
a.keep_if {|element| element.to_s.start_with?('b') } 
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Deleting.

```
static VALUE
rb_ary_keep_if(VALUE ary)
{
    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    rb_ary_select_bang(ary);
    return ary;
}
```

last → last_object or nil

click to toggle source

last(count) → new_array

Returns elements from `self`, or `nil`; `self` is not modified.

With no argument given, returns the last element, or `nil` if `self` is empty:

```
a = [:foo, 'bar', 2]
a.last 
a 
[].last 
```

With non-negative integer argument `count` given, returns a new array containing the trailing `count` elements of `self`, as available:

```
a = [:foo, 'bar', 2]
a.last(2)  
a.last(50) 
a.last(0)  
[].last(3) 
```

Related: see Methods for Fetching.

```
def last n = unspecified = true
  if Primitive.mandatory_only?
    Primitive.attr! :leaf
    Primitive.cexpr! %q{ ary_last(self) }
  else
    if unspecified
      Primitive.cexpr! %q{ ary_last(self) }
    else
      Primitive.cexpr! %q{ ary_take_first_or_last_n(self, NUM2LONG(n), ARY_TAKE_LAST) }
    end
  end
end
```

length → integer

click to toggle source

Returns the count of elements in `self`:

```
[0, 1, 2].length 
[].length        
```

Related: see Methods for Querying.

```
static VALUE
rb_ary_length(VALUE ary)
{
    long len = RARRAY_LEN(ary);
    return LONG2NUM(len);
}
```

Also aliased as:

size

map {|element| ... } → new_array

map → new_enumerator

With a block given, calls the block with each element of `self`; returns a new array whose elements are the return values from the block:

```
a = [:foo, 'bar', 2]
a1 = a.map {|element| element.class }
a1 
```

With no block given, returns a new `Enumerator`.

Related: `collect!`; see also Methods for Converting.

Also aliased as: collect

Alias for:

collect

map! {|element| ... } → new_array

map! → new_enumerator

With a block given, calls the block with each element of `self` and replaces the element with the block’s return value; returns `self`:

```
a = [:foo, 'bar', 2]
a.map! { |element| element.class } 
```

With no block given, returns a new `Enumerator`.

Related: `collect`; see also Methods for Converting.

Alias for:

collect!

max → element

click to toggle source

max(count) → new_array

max {|a, b| ... } → element

max(count) {|a, b| ... } → new_array

Returns one of the following:

- The maximum-valued element from `self`.
- A new array of maximum-valued elements from `self`.

Does not modify `self`.

With no block given, each element in `self` must respond to method `#<=>` with a numeric.

With no argument and no block, returns the element in `self` having the maximum value per method `#<=>`:

```
[1, 0, 3, 2].max 
```

With non-negative numeric argument `count` and no block, returns a new array with at most `count` elements, in descending order, per method `#<=>`:

```
[1, 0, 3, 2].max(3)   
[1, 0, 3, 2].max(3.0) 
[1, 0, 3, 2].max(9)   
[1, 0, 3, 2].max(0)   
```

With a block given, the block must return a numeric.

With a block and no argument, calls the block `self.size - 1` times to compare elements; returns the element having the maximum value per the block:

```
['0', '', '000', '00'].max {|a, b| a.size <=> b.size }
```

With non-negative numeric argument `count` and a block, returns a new array with at most `count` elements, in descending order, per the block:

```
['0', '', '000', '00'].max(2) {|a, b| a.size <=> b.size }
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_max(int argc, VALUE *argv, VALUE ary)
{
    VALUE result = Qundef, v;
    VALUE num;
    long i;

    if (rb_check_arity(argc, 0, 1) && !NIL_P(num = argv[0]))
       return rb_nmin_run(ary, num, 0, 1, 1);

    const long n = RARRAY_LEN(ary);
    if (rb_block_given_p()) {
        for (i = 0; i < RARRAY_LEN(ary); i++) {
           v = RARRAY_AREF(ary, i);
           if (UNDEF_P(result) || rb_cmpint(rb_yield_values(2, v, result), v, result) > 0) {
               result = v;
           }
        }
    }
    else if (n > 0) {
        result = RARRAY_AREF(ary, 0);
        if (n > 1) {
            if (FIXNUM_P(result) && CMP_OPTIMIZABLE(INTEGER)) {
                return ary_max_opt_fixnum(ary, 1, result);
            }
            else if (STRING_P(result) && CMP_OPTIMIZABLE(STRING)) {
                return ary_max_opt_string(ary, 1, result);
            }
            else if (RB_FLOAT_TYPE_P(result) && CMP_OPTIMIZABLE(FLOAT)) {
                return ary_max_opt_float(ary, 1, result);
            }
            else {
                return ary_max_generic(ary, 1, result);
            }
        }
    }
    if (UNDEF_P(result)) return Qnil;
    return result;
}
```

min → element

click to toggle source

min(count) → new_array

min {|a, b| ... } → element

min(count) {|a, b| ... } → new_array

Returns one of the following:

- The minimum-valued element from `self`.
- A new array of minimum-valued elements from `self`.

Does not modify `self`.

With no block given, each element in `self` must respond to method `#<=>` with a numeric.

With no argument and no block, returns the element in `self` having the minimum value per method `#<=>`:

```
[1, 0, 3, 2].min 
```

With non-negative numeric argument `count` and no block, returns a new array with at most `count` elements, in ascending order, per method `#<=>`:

```
[1, 0, 3, 2].min(3)   
[1, 0, 3, 2].min(3.0) 
[1, 0, 3, 2].min(9)   
[1, 0, 3, 2].min(0)   
```

With a block given, the block must return a numeric.

With a block and no argument, calls the block `self.size - 1` times to compare elements; returns the element having the minimum value per the block:

```
['0', '', '000', '00'].min {|a, b| a.size <=> b.size }
```

With non-negative numeric argument `count` and a block, returns a new array with at most `count` elements, in ascending order, per the block:

```
['0', '', '000', '00'].min(2) {|a, b| a.size <=> b.size }
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_min(int argc, VALUE *argv, VALUE ary)
{
    VALUE result = Qundef, v;
    VALUE num;
    long i;

    if (rb_check_arity(argc, 0, 1) && !NIL_P(num = argv[0]))
       return rb_nmin_run(ary, num, 0, 0, 1);

    const long n = RARRAY_LEN(ary);
    if (rb_block_given_p()) {
        for (i = 0; i < RARRAY_LEN(ary); i++) {
           v = RARRAY_AREF(ary, i);
           if (UNDEF_P(result) || rb_cmpint(rb_yield_values(2, v, result), v, result) < 0) {
               result = v;
           }
        }
    }
    else if (n > 0) {
        result = RARRAY_AREF(ary, 0);
        if (n > 1) {
            if (FIXNUM_P(result) && CMP_OPTIMIZABLE(INTEGER)) {
                return ary_min_opt_fixnum(ary, 1, result);
            }
            else if (STRING_P(result) && CMP_OPTIMIZABLE(STRING)) {
                return ary_min_opt_string(ary, 1, result);
            }
            else if (RB_FLOAT_TYPE_P(result) && CMP_OPTIMIZABLE(FLOAT)) {
                return ary_min_opt_float(ary, 1, result);
            }
            else {
                return ary_min_generic(ary, 1, result);
            }
        }
    }
    if (UNDEF_P(result)) return Qnil;
    return result;
}
```

minmax → array

click to toggle source

minmax {|a, b| ... } → array

Returns a 2-element array containing the minimum-valued and maximum-valued elements from `self`; does not modify `self`.

With no block given, the minimum and maximum values are determined using method `#<=>`:

```
[1, 0, 3, 2].minmax 
```

With a block given, the block must return a numeric; the block is called `self.size - 1` times to compare elements; returns the elements having the minimum and maximum values per the block:

```
['0', '', '000', '00'].minmax {|a, b| a.size <=> b.size }
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_minmax(VALUE ary)
{
    if (rb_block_given_p()) {
        return rb_call_super(0, NULL);
    }
    return rb_assoc_new(rb_ary_min(0, 0, ary), rb_ary_max(0, 0, ary));
}
```

none? → true or false

click to toggle source

none?(object) → true or false

none? {|element| ... } → true or false

Returns `true` if no element of `self` meets a given criterion, `false` otherwise.

With no block given and no argument, returns `true` if `self` has no truthy elements, `false` otherwise:

```
[nil, false].none?    
[nil, 0, false].none? 
[].none?              
```

With argument `object` given, returns `false` if for any element `element`, `object === element`; `true` otherwise:

```
['food', 'drink'].none?(/bar/) 
['food', 'drink'].none?(/foo/) 
[].none?(/foo/)                
[0, 1, 2].none?(3)             
[0, 1, 2].none?(1)             
```

With a block given, calls the block with each element in `self`; returns `true` if the block returns no truthy value, `false` otherwise:

```
[0, 1, 2].none? {|element| element > 3 } 
[0, 1, 2].none? {|element| element > 1 } 
```

Related: see Methods for Querying.

```
static VALUE
rb_ary_none_p(int argc, VALUE *argv, VALUE ary)
{
    long i, len = RARRAY_LEN(ary);

    rb_check_arity(argc, 0, 1);
    if (!len) return Qtrue;
    if (argc) {
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (RTEST(rb_funcall(argv[0], idEqq, 1, RARRAY_AREF(ary, i)))) return Qfalse;
        }
    }
    else if (!rb_block_given_p()) {
        for (i = 0; i < len; ++i) {
            if (RTEST(RARRAY_AREF(ary, i))) return Qfalse;
        }
    }
    else {
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (RTEST(rb_yield(RARRAY_AREF(ary, i)))) return Qfalse;
        }
    }
    return Qtrue;
}
```

one? → true or false

click to toggle source

one? {|element| ... } → true or false

one?(object) → true or false

Returns `true` if exactly one element of `self` meets a given criterion.

With no block given and no argument, returns `true` if `self` has exactly one truthy element, `false` otherwise:

```
[nil, 0].one? 
[0, 0].one? 
[nil, nil].one? 
[].one? 
```

With a block given, calls the block with each element in `self`; returns `true` if the block a truthy value for exactly one element, `false` otherwise:

```
[0, 1, 2].one? {|element| element > 0 } 
[0, 1, 2].one? {|element| element > 1 } 
[0, 1, 2].one? {|element| element > 2 } 
```

With argument `object` given, returns `true` if for exactly one element `element`, `object === element`; `false` otherwise:

```
[0, 1, 2].one?(0) 
[0, 0, 1].one?(0) 
[1, 1, 2].one?(0) 
['food', 'drink'].one?(/bar/) 
['food', 'drink'].one?(/foo/) 
[].one?(/foo/) 
```

Related: see Methods for Querying.

```
static VALUE
rb_ary_one_p(int argc, VALUE *argv, VALUE ary)
{
    long i, len = RARRAY_LEN(ary);
    VALUE result = Qfalse;

    rb_check_arity(argc, 0, 1);
    if (!len) return Qfalse;
    if (argc) {
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (RTEST(rb_funcall(argv[0], idEqq, 1, RARRAY_AREF(ary, i)))) {
                if (result) return Qfalse;
                result = Qtrue;
            }
        }
    }
    else if (!rb_block_given_p()) {
        for (i = 0; i < len; ++i) {
            if (RTEST(RARRAY_AREF(ary, i))) {
                if (result) return Qfalse;
                result = Qtrue;
            }
        }
    }
    else {
        for (i = 0; i < RARRAY_LEN(ary); ++i) {
            if (RTEST(rb_yield(RARRAY_AREF(ary, i)))) {
                if (result) return Qfalse;
                result = Qtrue;
            }
        }
    }
    return result;
}
```

pack(template, buffer: nil) → string

click to toggle source

Formats each element in `self` into a binary string; returns that string. See Packed Data.

```
def pack(fmt, buffer: nil)
  Primitive.pack_pack(fmt, buffer)
end
```

permutation(count = self.size) {|permutation| ... } → self

click to toggle source

permutation(count = self.size) → new_enumerator

Iterates over permutations of the elements of `self`; the order of permutations is indeterminate.

With a block and an in-range positive integer argument `count` (`0 < count <= self.size`) given, calls the block with each permutation of `self` of size `count`; returns `self`:

```
a = [0, 1, 2]
perms = []
a.permutation(1) {|perm| perms.push(perm) }
perms 

perms = []
a.permutation(2) {|perm| perms.push(perm) }
perms 

perms = []
a.permutation(3) {|perm| perms.push(perm) }
perms 
```

When `count` is zero, calls the block once with a new empty array:

```
perms = []
a.permutation(0) {|perm| perms.push(perm) }
perms 
```

When `count` is out of range (negative or larger than `self.size`), does not call the block:

```
a.permutation(-1) {|permutation| fail 'Cannot happen' }
a.permutation(4) {|permutation| fail 'Cannot happen' }
```

With no block given, returns a new `Enumerator`.

Related: Methods for Iterating.

```
static VALUE
rb_ary_permutation(int argc, VALUE *argv, VALUE ary)
{
    long r, n, i;

    n = RARRAY_LEN(ary);                  /* Array length */
    RETURN_SIZED_ENUMERATOR(ary, argc, argv, rb_ary_permutation_size);   /* Return enumerator if no block */
    r = n;
    if (rb_check_arity(argc, 0, 1) && !NIL_P(argv[0]))
        r = NUM2LONG(argv[0]);            /* Permutation size from argument */

    if (r < 0 || n < r) {
        /* no permutations: yield nothing */
    }
    else if (r == 0) { /* exactly one permutation: the zero-length array */
        rb_yield(rb_ary_new2(0));
    }
    else if (r == 1) { /* this is a special, easy case */
        for (i = 0; i < RARRAY_LEN(ary); i++) {
            rb_yield(rb_ary_new3(1, RARRAY_AREF(ary, i)));
        }
    }
    else {             /* this is the general case */
        volatile VALUE t0;
        long *p = ALLOCV_N(long, t0, r+roomof(n, sizeof(long)));
        char *used = (char*)(p + r);
        VALUE ary0 = ary_make_shared_copy(ary); /* private defensive copy of ary */
        RBASIC_CLEAR_CLASS(ary0);

        MEMZERO(used, char, n); /* initialize array */

        permute0(n, r, p, used, ary0); /* compute and yield permutations */
        ALLOCV_END(t0);
        RBASIC_SET_CLASS_RAW(ary0, rb_cArray);
    }
    return ary;
}
```

pop → object or nil

click to toggle source

pop(count) → new_array

Removes and returns trailing elements of `self`.

With no argument given, removes and returns the last element, if available; otherwise returns `nil`:

```
a = [:foo, 'bar', 2]
a.pop  
a      
[].pop 
```

With non-negative integer argument `count` given, returns a new array containing the trailing `count` elements of `self`, as available:

```
a = [:foo, 'bar', 2]
a.pop(2) 
a        

a = [:foo, 'bar', 2]
a.pop(50) 
a         
```

Related: `Array#push`; see also Methods for Deleting.

```
static VALUE
rb_ary_pop_m(int argc, VALUE *argv, VALUE ary)
{
    VALUE result;

    if (argc == 0) {
        return rb_ary_pop(ary);
    }

    rb_ary_modify_check(ary);
    result = ary_take_first_or_last(argc, argv, ary, ARY_TAKE_LAST);
    ARY_INCREASE_LEN(ary, -RARRAY_LEN(result));
    ary_verify(ary);
    return result;
}
```

prepend(*objects) → self

Prepends the given `objects` to `self`:

```
a = [:foo, 'bar', 2]
a.unshift(:bam, :bat) 
```

Related: `Array#shift`; see also Methods for Assigning.

Alias for:

unshift

product(*other_arrays) → new_array

click to toggle source

product(*other_arrays) {|combination| ... } → self

Computes all combinations of elements from all the arrays, including both `self` and `other_arrays`:

- The number of combinations is the product of the sizes of all the arrays, including both `self` and `other_arrays`.
- The order of the returned combinations is indeterminate.

With no block given, returns the combinations as an array of arrays:

```
p = [0, 1].product([2, 3])

p.size 
p = [0, 1].product([2, 3], [4, 5])

p.size 
```

If `self` or any argument is empty, returns an empty array:

```
[].product([2, 3], [4, 5]) 
[0, 1].product([2, 3], []) 
```

If no argument is given, returns an array of 1-element arrays, each containing an element of `self`:

```
a.product 
```

With a block given, calls the block with each combination; returns `self`:

```
p = []
[0, 1].product([2, 3]) {|combination| p.push(combination) }
p 
```

If `self` or any argument is empty, does not call the block:

```
[].product([2, 3], [4, 5]) {|combination| fail 'Cannot happen' }

[0, 1].product([2, 3], []) {|combination| fail 'Cannot happen' }
```

If no argument is given, calls the block with each element of `self` as a 1-element array:

```
p = []
[0, 1].product {|combination| p.push(combination) }
p 
```

Related: see Methods for Combining.

```
static VALUE
rb_ary_product(int argc, VALUE *argv, VALUE ary)
{
    int n = argc+1;    /* How many arrays we're operating on */
    volatile VALUE t0 = rb_ary_hidden_new(n);
    volatile VALUE t1 = Qundef;
    VALUE *arrays = RARRAY_PTR(t0); /* The arrays we're computing the product of */
    int *counters = ALLOCV_N(int, t1, n); /* The current position in each one */
    VALUE result = Qnil;      /* The array we'll be returning, when no block given */
    long i,j;
    long resultlen = 1;

    RBASIC_CLEAR_CLASS(t0);

    /* initialize the arrays of arrays */
    ARY_SET_LEN(t0, n);
    arrays[0] = ary;
    for (i = 1; i < n; i++) arrays[i] = Qnil;
    for (i = 1; i < n; i++) arrays[i] = to_ary(argv[i-1]);

    /* initialize the counters for the arrays */
    for (i = 0; i < n; i++) counters[i] = 0;

    /* Otherwise, allocate and fill in an array of results */
    if (rb_block_given_p()) {
        /* Make defensive copies of arrays; exit if any is empty */
        for (i = 0; i < n; i++) {
            if (RARRAY_LEN(arrays[i]) == 0) goto done;
            arrays[i] = ary_make_shared_copy(arrays[i]);
        }
    }
    else {
        /* Compute the length of the result array; return [] if any is empty */
        for (i = 0; i < n; i++) {
            long k = RARRAY_LEN(arrays[i]);
            if (k == 0) {
                result = rb_ary_new2(0);
                goto done;
            }
            if (MUL_OVERFLOW_LONG_P(resultlen, k))
                rb_raise(rb_eRangeError, "too big to product");
            resultlen *= k;
        }
        result = rb_ary_new2(resultlen);
    }
    for (;;) {
        int m;
        /* fill in one subarray */
        VALUE subarray = rb_ary_new2(n);
        for (j = 0; j < n; j++) {
            rb_ary_push(subarray, rb_ary_entry(arrays[j], counters[j]));
        }

        /* put it on the result array */
        if (NIL_P(result)) {
            FL_SET(t0, RARRAY_SHARED_ROOT_FLAG);
            rb_yield(subarray);
            if (!FL_TEST(t0, RARRAY_SHARED_ROOT_FLAG)) {
                rb_raise(rb_eRuntimeError, "product reentered");
            }
            else {
                FL_UNSET(t0, RARRAY_SHARED_ROOT_FLAG);
            }
        }
        else {
            rb_ary_push(result, subarray);
        }

        /*
         * Increment the last counter.  If it overflows, reset to 0
         * and increment the one before it.
         */
        m = n-1;
        counters[m]++;
        while (counters[m] == RARRAY_LEN(arrays[m])) {
            counters[m] = 0;
            /* If the first counter overflows, we are done */
            if (--m < 0) goto done;
            counters[m]++;
        }
    }

done:
    ALLOCV_END(t1);

    return NIL_P(result) ? ary : result;
}
```

push(*objects) → self

click to toggle source

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

```
static VALUE
rb_ary_push_m(int argc, VALUE *argv, VALUE ary)
{
    return rb_ary_cat(ary, argv, argc);
}
```

Also aliased as:

append

rassoc(object) → found_array or nil

click to toggle source

Returns the first element `ele` in `self` such that `ele` is an array and `ele[1] == object`:

```
a = [{foo: 0}, [2, 4], [4, 5, 6], [4, 5]]
a.rassoc(4) 
a.rassoc(5) 
```

Returns `nil` if no such element is found.

Related: `Array#assoc`; see also Methods for Fetching.

```
VALUE
rb_ary_rassoc(VALUE ary, VALUE value)
{
    long i;
    VALUE v;

    for (i = 0; i < RARRAY_LEN(ary); ++i) {
        v = rb_check_array_type(RARRAY_AREF(ary, i));
        if (RB_TYPE_P(v, T_ARRAY) &&
            RARRAY_LEN(v) > 1 &&
            rb_equal(RARRAY_AREF(v, 1), value))
            return v;
    }
    return Qnil;
}
```

reject {|element| ... } → new_array

click to toggle source

reject → new_enumerator

With a block given, returns a new array whose elements are all those from `self` for which the block returns `false` or `nil`:

```
a = [:foo, 'bar', 2, 'bat']
a1 = a.reject {|element| element.to_s.start_with?('b') }
a1 
```

With no block given, returns a new `Enumerator`.

Related: Methods for Fetching.

```
static VALUE
rb_ary_reject(VALUE ary)
{
    VALUE rejected_ary;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    rejected_ary = rb_ary_new();
    ary_reject(ary, rejected_ary);
    return rejected_ary;
}
```

reject! {|element| ... } → self or nil

click to toggle source

reject! → new_enumerator

With a block given, calls the block with each element of `self`; removes each element for which the block returns a truthy value.

Returns `self` if any elements removed:

```
a = [:foo, 'bar', 2, 'bat']
a.reject! {|element| element.to_s.start_with?('b') } 
```

Returns `nil` if no elements removed.

With no block given, returns a new `Enumerator`.

Related: see Methods for Deleting.

```
static VALUE
rb_ary_reject_bang(VALUE ary)
{
    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    rb_ary_modify(ary);
    return ary_reject_bang(ary);
}
```

repeated_combination(size) {|combination| ... } → self

click to toggle source

repeated_combination(size) → new_enumerator

With a block given, calls the block with each repeated combination of length `size` of the elements of `self`; each combination is an array; returns `self`. The order of the combinations is indeterminate.

If a positive integer argument `size` is given, calls the block with each `size`-tuple repeated combination of the elements of `self`. The number of combinations is `(size+1)(size+2)/2`.

Examples:

- `size` is 1:
  ```
c = []
[0, 1, 2].repeated_combination(1) {|combination| c.push(combination) }
c 
  ```
- `size` is 2:
  ```
c = []
[0, 1, 2].repeated_combination(2) {|combination| c.push(combination) }
c 
  ```

If `size` is zero, calls the block once with an empty array.

If `size` is negative, does not call the block:

```
[0, 1, 2].repeated_combination(-1) {|combination| fail 'Cannot happen' }
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Combining.

```
static VALUE
rb_ary_repeated_combination(VALUE ary, VALUE num)
{
    long n, i, len;

    n = NUM2LONG(num);                 /* Combination size from argument */
    RETURN_SIZED_ENUMERATOR(ary, 1, &num, rb_ary_repeated_combination_size);   /* Return enumerator if no block */
    len = RARRAY_LEN(ary);
    if (n < 0) {
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
    else if (len == 0) {
        /* yield nothing */
    }
    else {
        volatile VALUE t0;
        long *p = ALLOCV_N(long, t0, n);
        VALUE ary0 = ary_make_shared_copy(ary); /* private defensive copy of ary */
        RBASIC_CLEAR_CLASS(ary0);

        rcombinate0(len, n, p, n, ary0); /* compute and yield repeated combinations */
        ALLOCV_END(t0);
        RBASIC_SET_CLASS_RAW(ary0, rb_cArray);
    }
    return ary;
}
```

repeated_permutation(size) {|permutation| ... } → self

click to toggle source

repeated_permutation(size) → new_enumerator

With a block given, calls the block with each repeated permutation of length `size` of the elements of `self`; each permutation is an array; returns `self`. The order of the permutations is indeterminate.

If a positive integer argument `size` is given, calls the block with each `size`-tuple repeated permutation of the elements of `self`. The number of permutations is `self.size**size`.

Examples:

- `size` is 1:
  ```
p = []
[0, 1, 2].repeated_permutation(1) {|permutation| p.push(permutation) }
p 
  ```
- `size` is 2:
  ```
p = []
[0, 1, 2].repeated_permutation(2) {|permutation| p.push(permutation) }
p 
  ```

If `size` is zero, calls the block once with an empty array.

If `size` is negative, does not call the block:

```
[0, 1, 2].repeated_permutation(-1) {|permutation| fail 'Cannot happen' }
```

With no block given, returns a new `Enumerator`.

Related: see Methods for Combining.

```
static VALUE
rb_ary_repeated_permutation(VALUE ary, VALUE num)
{
    long r, n, i;

    n = RARRAY_LEN(ary);                  /* Array length */
    RETURN_SIZED_ENUMERATOR(ary, 1, &num, rb_ary_repeated_permutation_size);      /* Return Enumerator if no block */
    r = NUM2LONG(num);                    /* Permutation size from argument */

    if (r < 0) {
        /* no permutations: yield nothing */
    }
    else if (r == 0) { /* exactly one permutation: the zero-length array */
        rb_yield(rb_ary_new2(0));
    }
    else if (r == 1) { /* this is a special, easy case */
        for (i = 0; i < RARRAY_LEN(ary); i++) {
            rb_yield(rb_ary_new3(1, RARRAY_AREF(ary, i)));
        }
    }
    else {             /* this is the general case */
        volatile VALUE t0;
        long *p = ALLOCV_N(long, t0, r);
        VALUE ary0 = ary_make_shared_copy(ary); /* private defensive copy of ary */
        RBASIC_CLEAR_CLASS(ary0);

        rpermute0(n, r, p, ary0); /* compute and yield repeated permutations */
        ALLOCV_END(t0);
        RBASIC_SET_CLASS_RAW(ary0, rb_cArray);
    }
    return ary;
}
```

replace(other_array) → self

Replaces the elements of `self` with the elements of `other_array`, which must be an array-convertible object; returns `self`:

```
a = ['a', 'b', 'c']   
a.replace(['d', 'e']) 
```

Related: see Methods for Assigning.

Alias for:

initialize_copy

reverse → new_array

click to toggle source

Returns a new array containing the elements of `self` in reverse order:

```
[0, 1, 2].reverse 
```

Related: see Methods for Combining.

```
static VALUE
rb_ary_reverse_m(VALUE ary)
{
    long len = RARRAY_LEN(ary);
    VALUE dup = rb_ary_new2(len);

    if (len > 0) {
        const VALUE *p1 = RARRAY_CONST_PTR(ary);
        VALUE *p2 = (VALUE *)RARRAY_CONST_PTR(dup) + len - 1;
        do *p2-- = *p1++; while (--len > 0);
    }
    ARY_SET_LEN(dup, RARRAY_LEN(ary));
    return dup;
}
```

reverse! → self

click to toggle source

Reverses the order of the elements of `self`; returns `self`:

```
a = [0, 1, 2]
a.reverse! 
a          
```

Related: see Methods for Assigning.

```
static VALUE
rb_ary_reverse_bang(VALUE ary)
{
    return rb_ary_reverse(ary);
}
```

reverse_each {|element| ... } → self

click to toggle source

reverse_each → Enumerator

When a block given, iterates backwards over the elements of `self`, passing, in reverse order, each element to the block; returns `self`:

```
a = []
[0, 1, 2].reverse_each {|element| a.push(element) }
a 
```

Allows the array to be modified during iteration:

```
a = ['a', 'b', 'c']
a.reverse_each {|element| a.clear if element.start_with?('b') }
a 
```

When no block given, returns a new `Enumerator`.

Related: see Methods for Iterating.

```
static VALUE
rb_ary_reverse_each(VALUE ary)
{
    long len;

    RETURN_SIZED_ENUMERATOR(ary, 0, 0, ary_enum_length);
    len = RARRAY_LEN(ary);
    while (len--) {
        long nlen;
        rb_yield(RARRAY_AREF(ary, len));
        nlen = RARRAY_LEN(ary);
        if (nlen < len) {
            len = nlen;
        }
    }
    return ary;
}
```

rindex(object) → integer or nil

click to toggle source

rindex {|element| ... } → integer or nil

rindex → new_enumerator

Returns the index of the last element for which `object == element`.

With argument `object` given, returns the index of the last such element found:

```
a = [:foo, 'bar', 2, 'bar']
a.rindex('bar') 
```

Returns `nil` if no such object found.

With a block given, calls the block with each successive element; returns the index of the last element for which the block returns a truthy value:

```
a = [:foo, 'bar', 2, 'bar']
a.rindex {|element| element == 'bar' } 
```

Returns `nil` if the block never returns a truthy value.

When neither an argument nor a block is given, returns a new `Enumerator`.

Related: see Methods for Querying.

```
static VALUE
rb_ary_rindex(int argc, VALUE *argv, VALUE ary)
{
    VALUE val;
    long i = RARRAY_LEN(ary), len;

    if (argc == 0) {
        RETURN_ENUMERATOR(ary, 0, 0);
        while (i--) {
            if (RTEST(rb_yield(RARRAY_AREF(ary, i))))
                return LONG2NUM(i);
            if (i > (len = RARRAY_LEN(ary))) {
                i = len;
            }
        }
        return Qnil;
    }
    rb_check_arity(argc, 0, 1);
    val = argv[0];
    if (rb_block_given_p())
        rb_warn("given block not used");
    while (i--) {
        VALUE e = RARRAY_AREF(ary, i);
        if (rb_equal(e, val)) {
            return LONG2NUM(i);
        }
        if (i > RARRAY_LEN(ary)) {
            break;
        }
    }
    return Qnil;
}
```

rotate(count = 1) → new_array

click to toggle source

Returns a new array formed from `self` with elements rotated from one end to the other.

With non-negative numeric `count`, rotates elements from the beginning to the end:

```
[0, 1, 2, 3].rotate(2)   
[0, 1, 2, 3].rotate(2.1) 
```

If `count` is large, uses `count % array.size` as the count:

```
[0, 1, 2, 3].rotate(22) 
```

With a `count` of zero, rotates no elements:

```
[0, 1, 2, 3].rotate(0) 
```

With negative numeric `count`, rotates in the opposite direction, from the end to the beginning:

```
[0, 1, 2, 3].rotate(-1) 
```

If `count` is small (far from zero), uses `count % array.size` as the count:

```
[0, 1, 2, 3].rotate(-21) 
```

Related: see Methods for Fetching.

```
static VALUE
rb_ary_rotate_m(int argc, VALUE *argv, VALUE ary)
{
    VALUE rotated;
    const VALUE *ptr;
    long len;
    long cnt = (rb_check_arity(argc, 0, 1) ? NUM2LONG(argv[0]) : 1);

    len = RARRAY_LEN(ary);
    rotated = rb_ary_new2(len);
    if (len > 0) {
        cnt = rotate_count(cnt, len);
        ptr = RARRAY_CONST_PTR(ary);
        len -= cnt;
        ary_memcpy(rotated, 0, len, ptr + cnt);
        ary_memcpy(rotated, len, cnt, ptr);
    }
    ARY_SET_LEN(rotated, RARRAY_LEN(ary));
    return rotated;
}
```

rotate!(count = 1) → self

click to toggle source

Rotates `self` in place by moving elements from one end to the other; returns `self`.

With non-negative numeric `count`, rotates `count` elements from the beginning to the end:

```
[0, 1, 2, 3].rotate!(2)   
[0, 1, 2, 3].rotate!(2.1) 
```

If `count` is large, uses `count % array.size` as the count:

```
[0, 1, 2, 3].rotate!(21) 
```

If `count` is zero, rotates no elements:

```
[0, 1, 2, 3].rotate!(0) 
```

With a negative numeric `count`, rotates in the opposite direction, from end to beginning:

```
[0, 1, 2, 3].rotate!(-1) 
```

If `count` is small (far from zero), uses `count % array.size` as the count:

```
[0, 1, 2, 3].rotate!(-21) 
```

Related: see Methods for Assigning.

```
static VALUE
rb_ary_rotate_bang(int argc, VALUE *argv, VALUE ary)
{
    long n = (rb_check_arity(argc, 0, 1) ? NUM2LONG(argv[0]) : 1);
    rb_ary_rotate(ary, n);
    return ary;
}
```

sample(random: Random) → object

click to toggle source

sample(count, random: Random) → new_ary

Returns random elements from `self`, as selected by the object given by the keyword argument `random`.

With no argument `count` given, returns one random element from `self`:

```
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.sample 
a.sample 
```

Returns `nil` if `self` is empty:

```
[].sample 
```

With a non-negative numeric argument `count` given, returns a new array containing `count` random elements from `self`:

```
a.sample(3) 
a.sample(6) 
```

The order of the result array is unrelated to the order of `self`.

Returns a new empty `Array` if `self` is empty:

```
[].sample(4) 
```

May return duplicates in `self`:

```
a = [1, 1, 1, 2, 2, 3]
a.sample(a.size) 
```

Returns no more than `a.size` elements (because no new duplicates are introduced):

```
a.sample(50) 
```

The object given with the keyword argument `random` is used as the random number generator:
