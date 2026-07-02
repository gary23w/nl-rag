---
title: "module Enumerable (part 3/3)"
source: https://ruby-doc.org/core/Enumerable.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 3/3
---

# module Enumerable

- A negative integer if `a < b`.
- Zero if `a == b`.
- A positive integer if `a > b`.

With a block given and no argument, returns the maximum element as determined by the block:

```
%w[xxx x xxxx xx].max {|a, b| a.size <=> b.size } 
h = {foo: 0, bar: 1, baz: 2}
h.max {|pair1, pair2| pair1[1] <=> pair2[1] }     
[].max {|a, b| a <=> b }                          
```

With a block given and positive integer argument `n` given, returns an array containing the first `n` maximum elements that exist, as determined by the block.

```
%w[xxx x xxxx xx].max(2) {|a, b| a.size <=> b.size } 
h = {foo: 0, bar: 1, baz: 2}
h.max(2) {|pair1, pair2| pair1[1] <=> pair2[1] }

[].max(2) {|a, b| a <=> b }                          
```

Related: `min`, `minmax`, `max_by`.

```
static VALUE
enum_max(int argc, VALUE *argv, VALUE obj)
{
    VALUE memo;
    struct max_t *m = NEW_MEMO_FOR(struct max_t, memo);
    VALUE result;
    VALUE num;

    if (rb_check_arity(argc, 0, 1) && !NIL_P(num = argv[0]))
       return rb_nmin_run(obj, num, 0, 1, 0);

    m->max = Qundef;
    if (rb_block_given_p()) {
        rb_block_call(obj, id_each, 0, 0, max_ii, (VALUE)memo);
    }
    else {
        rb_block_call(obj, id_each, 0, 0, max_i, (VALUE)memo);
    }
    result = m->max;
    if (UNDEF_P(result)) return Qnil;
    return result;
}
```

max_by {|element| ... } → element

click to toggle source

max_by(n) {|element| ... } → array

max_by → enumerator

max_by(n) → enumerator

Returns the elements for which the block returns the maximum values.

With a block given and no argument, returns the element for which the block returns the maximum value:

```
(1..4).max_by {|element| -element }                    
%w[a b c d].max_by {|element| -element.ord }           
{foo: 0, bar: 1, baz: 2}.max_by {|key, value| -value } 
[].max_by {|element| -element }                        
```

With a block given and positive integer argument `n` given, returns an array containing the `n` elements for which the block returns maximum values:

```
(1..4).max_by(2) {|element| -element }

%w[a b c d].max_by(2) {|element| -element.ord }

{foo: 0, bar: 1, baz: 2}.max_by(2) {|key, value| -value }

[].max_by(2) {|element| -element }
```

Returns an `Enumerator` if no block is given.

Related: `max`, `minmax`, `min_by`.

```
static VALUE
enum_max_by(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo;
    VALUE num;

    rb_check_arity(argc, 0, 1);

    RETURN_SIZED_ENUMERATOR(obj, argc, argv, enum_size);

    if (argc && !NIL_P(num = argv[0]))
        return rb_nmin_run(obj, num, 1, 1, 0);

    memo = MEMO_NEW(Qundef, Qnil, 0);
    rb_block_call(obj, id_each, 0, 0, max_by_i, (VALUE)memo);
    return memo->v2;
}
```

member?

(object) -> true or false

click to toggle source

Returns whether for any element `object == element`:

```
(1..4).include?(2)                       
(1..4).include?(5)                       
(1..4).include?('2')                     
%w[a b c d].include?('b')                
%w[a b c d].include?('2')                
{foo: 0, bar: 1, baz: 2}.include?(:foo)  
{foo: 0, bar: 1, baz: 2}.include?('foo') 
{foo: 0, bar: 1, baz: 2}.include?(0)     
```

```
static VALUE
enum_member(VALUE obj, VALUE val)
{
    struct MEMO *memo = MEMO_NEW(val, Qfalse, 0);

    rb_block_call(obj, id_each, 0, 0, member_i, (VALUE)memo);
    return memo->v2;
}
```

Also aliased as:

include?

min → element

click to toggle source

min(n) → array

min {|a, b| ... } → element

min(n) {|a, b| ... } → array

Returns the element with the minimum element according to a given criterion. The ordering of equal elements is indeterminate and may be unstable.

With no argument and no block, returns the minimum element, using the elements’ own method `#<=>` for comparison:

```
(1..4).min                   
(-4..-1).min                 
%w[d c b a].min              
{foo: 0, bar: 1, baz: 2}.min 
[].min                       
```

With positive integer argument `n` given, and no block, returns an array containing the first `n` minimum elements that exist:

```
(1..4).min(2)                   
(-4..-1).min(2)                 
%w[d c b a].min(2)              
{foo: 0, bar: 1, baz: 2}.min(2) 
[].min(2)                       
```

With a block given, the block determines the minimum elements. The block is called with two elements `a` and `b`, and must return:

- A negative integer if `a < b`.
- Zero if `a == b`.
- A positive integer if `a > b`.

With a block given and no argument, returns the minimum element as determined by the block:

```
%w[xxx x xxxx xx].min {|a, b| a.size <=> b.size } 
h = {foo: 0, bar: 1, baz: 2}
h.min {|pair1, pair2| pair1[1] <=> pair2[1] } 
[].min {|a, b| a <=> b }                          
```

With a block given and positive integer argument `n` given, returns an array containing the first `n` minimum elements that exist, as determined by the block.

```
%w[xxx x xxxx xx].min(2) {|a, b| a.size <=> b.size } 
h = {foo: 0, bar: 1, baz: 2}
h.min(2) {|pair1, pair2| pair1[1] <=> pair2[1] }

[].min(2) {|a, b| a <=> b }                          
```

Related: `min_by`, `minmax`, `max`.

```
static VALUE
enum_min(int argc, VALUE *argv, VALUE obj)
{
    VALUE memo;
    struct min_t *m = NEW_MEMO_FOR(struct min_t, memo);
    VALUE result;
    VALUE num;

    if (rb_check_arity(argc, 0, 1) && !NIL_P(num = argv[0]))
       return rb_nmin_run(obj, num, 0, 0, 0);

    m->min = Qundef;
    if (rb_block_given_p()) {
        rb_block_call(obj, id_each, 0, 0, min_ii, memo);
    }
    else {
        rb_block_call(obj, id_each, 0, 0, min_i, memo);
    }
    result = m->min;
    if (UNDEF_P(result)) return Qnil;
    return result;
}
```

min_by {|element| ... } → element

click to toggle source

min_by(n) {|element| ... } → array

min_by → enumerator

min_by(n) → enumerator

Returns the elements for which the block returns the minimum values.

With a block given and no argument, returns the element for which the block returns the minimum value:

```
(1..4).min_by {|element| -element }                    
%w[a b c d].min_by {|element| -element.ord }           
{foo: 0, bar: 1, baz: 2}.min_by {|key, value| -value } 
[].min_by {|element| -element }                        
```

With a block given and positive integer argument `n` given, returns an array containing the `n` elements for which the block returns minimum values:

```
(1..4).min_by(2) {|element| -element }

%w[a b c d].min_by(2) {|element| -element.ord }

{foo: 0, bar: 1, baz: 2}.min_by(2) {|key, value| -value }

[].min_by(2) {|element| -element }
```

Returns an `Enumerator` if no block is given.

Related: `min`, `minmax`, `max_by`.

```
static VALUE
enum_min_by(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo;
    VALUE num;

    rb_check_arity(argc, 0, 1);

    RETURN_SIZED_ENUMERATOR(obj, argc, argv, enum_size);

    if (argc && !NIL_P(num = argv[0]))
        return rb_nmin_run(obj, num, 1, 0, 0);

    memo = MEMO_NEW(Qundef, Qnil, 0);
    rb_block_call(obj, id_each, 0, 0, min_by_i, (VALUE)memo);
    return memo->v2;
}
```

minmax → [minimum, maximum]

click to toggle source

minmax {|a, b| ... } → [minimum, maximum]

Returns a 2-element array containing the minimum and maximum elements according to a given criterion. The ordering of equal elements is indeterminate and may be unstable.

With no argument and no block, returns the minimum and maximum elements, using the elements’ own method `#<=>` for comparison:

```
(1..4).minmax                   
(-4..-1).minmax                 
%w[d c b a].minmax              
{foo: 0, bar: 1, baz: 2}.minmax 
[].minmax                       
```

With a block given, returns the minimum and maximum elements as determined by the block:

```
%w[xxx x xxxx xx].minmax {|a, b| a.size <=> b.size } 
h = {foo: 0, bar: 1, baz: 2}
h.minmax {|pair1, pair2| pair1[1] <=> pair2[1] }

[].minmax {|a, b| a <=> b }                          
```

Related: `min`, `max`, `minmax_by`.

```
static VALUE
enum_minmax(VALUE obj)
{
    VALUE memo;
    struct minmax_t *m = NEW_MEMO_FOR(struct minmax_t, memo);

    m->min = Qundef;
    m->last = Qundef;
    if (rb_block_given_p()) {
        rb_block_call(obj, id_each, 0, 0, minmax_ii, memo);
        if (!UNDEF_P(m->last))
            minmax_ii_update(m->last, m->last, m);
    }
    else {
        rb_block_call(obj, id_each, 0, 0, minmax_i, memo);
        if (!UNDEF_P(m->last))
            minmax_i_update(m->last, m->last, m);
    }
    if (!UNDEF_P(m->min)) {
        return rb_assoc_new(m->min, m->max);
    }
    return rb_assoc_new(Qnil, Qnil);
}
```

minmax_by {|element| ... } → [minimum, maximum]

click to toggle source

minmax_by → enumerator

Returns a 2-element array containing the elements for which the block returns minimum and maximum values:

```
(1..4).minmax_by {|element| -element }

%w[a b c d].minmax_by {|element| -element.ord }

{foo: 0, bar: 1, baz: 2}.minmax_by {|key, value| -value }

[].minmax_by {|element| -element }
```

Returns an `Enumerator` if no block is given.

Related: `max_by`, `minmax`, `min_by`.

```
static VALUE
enum_minmax_by(VALUE obj)
{
    VALUE memo;
    struct minmax_by_t *m = NEW_MEMO_FOR(struct minmax_by_t, memo);

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    m->min_bv = Qundef;
    m->max_bv = Qundef;
    m->min = Qnil;
    m->max = Qnil;
    m->last_bv = Qundef;
    m->last = Qundef;
    rb_block_call(obj, id_each, 0, 0, minmax_by_i, memo);
    if (!UNDEF_P(m->last_bv))
        minmax_by_i_update(m->last_bv, m->last_bv, m->last, m->last, m);
    m = MEMO_FOR(struct minmax_by_t, memo);
    return rb_assoc_new(m->min, m->max);
}
```

none? → true or false

click to toggle source

none?(pattern) → true or false

none? {|element| ... } → true or false

Returns whether no element meets a given criterion.

With no argument and no block, returns whether no element is truthy:

```
(1..4).none?           
[nil, false].none?     
{foo: 0}.none?         
{foo: 0, bar: 1}.none? 
[].none?               
```

With argument `pattern` and no block, returns whether for no element `element`, `pattern === element`:

```
[nil, false, 1.1].none?(Integer)      
%w[bar baz bat bam].none?(/m/)        
%w[bar baz bat bam].none?(/foo/)      
%w[bar baz bat bam].none?('ba')       
{foo: 0, bar: 1, baz: 2}.none?(Hash)  
{foo: 0}.none?(Array)                 
[].none?(Integer)                     
```

With a block given, returns whether the block returns a truthy value for no element:

```
(1..4).none? {|element| element < 1 }                     
(1..4).none? {|element| element < 2 }                     
{foo: 0, bar: 1, baz: 2}.none? {|key, value| value < 0 }  
{foo: 0, bar: 1, baz: 2}.none? {|key, value| value < 1 } 
```

Related: `one?`, `all?`, `any?`.

```
static VALUE
enum_none(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo = MEMO_ENUM_NEW(Qtrue);

    WARN_UNUSED_BLOCK(argc);
    ENUM_BLOCK_CALL(none);
    return memo->v1;
}
```

one? → true or false

click to toggle source

one?(pattern) → true or false

one? {|element| ... } → true or false

Returns whether exactly one element meets a given criterion.

With no argument and no block, returns whether exactly one element is truthy:

```
(1..1).one?           
[1, nil, false].one?  
(1..4).one?           
{foo: 0}.one?         
{foo: 0, bar: 1}.one? 
[].one?               
```

With argument `pattern` and no block, returns whether for exactly one element `element`, `pattern === element`:

```
[nil, false, 0].one?(Integer)        
[nil, false, 0].one?(Numeric)        
[nil, false, 0].one?(Float)          
%w[bar baz bat bam].one?(/m/)        
%w[bar baz bat bam].one?(/foo/)      
%w[bar baz bat bam].one?('ba')       
{foo: 0, bar: 1, baz: 2}.one?(Array) 
{foo: 0}.one?(Array)                 
[].one?(Integer)                     
```

With a block given, returns whether the block returns a truthy value for exactly one element:

```
(1..4).one? {|element| element < 2 }                     
(1..4).one? {|element| element < 1 }                     
{foo: 0, bar: 1, baz: 2}.one? {|key, value| value < 1 }  
{foo: 0, bar: 1, baz: 2}.one? {|key, value| value < 2 } 
```

Related: `none?`, `all?`, `any?`.

```
static VALUE
enum_one(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo = MEMO_ENUM_NEW(Qundef);
    VALUE result;

    WARN_UNUSED_BLOCK(argc);
    ENUM_BLOCK_CALL(one);
    result = memo->v1;
    if (UNDEF_P(result)) return Qfalse;
    return result;
}
```

partition {|element| ... } → [true_array, false_array]

click to toggle source

partition → enumerator

With a block given, returns an array of two arrays:

- The first having those elements for which the block returns a truthy value.
- The other having all other elements.

Examples:

```
p = (1..4).partition {|i| i.even? }
p 
p = ('a'..'d').partition {|c| c < 'c' }
p 
h = {foo: 0, bar: 1, baz: 2, bat: 3}
p = h.partition {|key, value| key.start_with?('b') }
p 
p = h.partition {|key, value| value < 2 }
p 
```

With no block given, returns an `Enumerator`.

Related: `Enumerable#group_by`.

```
static VALUE
enum_partition(VALUE obj)
{
    struct MEMO *memo;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    memo = MEMO_NEW(rb_ary_new(), rb_ary_new(), 0);
    rb_block_call(obj, id_each, 0, 0, partition_i, (VALUE)memo);

    return rb_assoc_new(memo->v1, memo->v2);
}
```

reduce

(p1 = v1, p2 = v2)

Returns the result of applying a reducer to an initial value and the first element of the `Enumerable`. It then takes the result and applies the function to it and the second element of the collection, and so on. The return value is the result returned by the final call to the function.

You can think of

```
[ a, b, c, d ].inject(i) { |r, v| fn(r, v) }
```

as being

```
fn(fn(fn(fn(i, a), b), c), d)
```

In a way the `inject` function *injects* the function between the elements of the enumerable.

`inject` is aliased as `reduce`. You use it when you want to *reduce* a collection to a single value.

**The Calling Sequences**

Let’s start with the most verbose:

```
enum.inject(initial_value) do |result, next_value|
  
  
  
  
end
```

For example:

```
product = [ 2, 3, 4 ].inject(1) do |result, next_value|
  result * next_value
end
product 
```

When this runs, the block is first called with `1` (the initial value) and `2` (the first element of the array). The block returns `1*2`, so on the next iteration the block is called with `2` (the previous result) and `3`. The block returns `6`, and is called one last time with `6` and `4`. The result of the block, `24` becomes the value returned by `inject`. This code returns the product of the elements in the enumerable.

**First Shortcut: Default Initial value**

In the case of the previous example, the initial value, `1`, wasn’t really necessary: the calculation of the product of a list of numbers is self-contained.

In these circumstances, you can omit the `initial_value` parameter. `inject` will then initially call the block with the first element of the collection as the `result` parameter and the second element as the `next_value`.

```
[ 2, 3, 4 ].inject do |result, next_value|
  result * next_value
end
```

This shortcut is convenient, but can only be used when the block produces a result which can be passed back to it as a first parameter.

Here’s an example where that’s not the case: it returns a hash where the keys are words and the values are the number of occurrences of that word in the enumerable.

```
freqs = File.read("README.md")
  .scan(/\w{2,}/)
  .reduce(Hash.new(0)) do |counts, word|
    counts[word] += 1
    counts
  end
freqs #=> {"Actions"=>4,
           "Status"=>5,
           "MinGW"=>3,
           "https"=>27,
           "github"=>10,
           "com"=>15, ...
```

Note that the last line of the block is just the word `counts`. This ensures the return value of the block is the result that’s being calculated.

**Second Shortcut: a Reducer function**

A *reducer function* is a function that takes a partial result and the next value, returning the next partial result. The block that is given to `inject` is a reducer.

You can also write a reducer as a function and pass the name of that function (as a symbol) to `inject`. However, for this to work, the function

1. Must be defined on the type of the result value
2. Must accept a single parameter, the next value in the collection, and
3. Must return an updated result which will also implement the function.

Here’s an example that adds elements to a string. The two calls invoke the functions `String#concat` and `String#+` on the result so far, passing it the next value.

```
s = [ "cat", " ", "dog" ].inject("", :concat)
s 
s = [ "cat", " ", "dog" ].inject("The result is:", :+)
s 
```

Here’s a more complex example when the result object maintains state of a different type to the enumerable elements.

```
class Turtle

  def initialize
    @x = @y = 0
  end

  def move(dir)
    case dir
    when "n" then @y += 1
    when "s" then @y -= 1
    when "e" then @x += 1
    when "w" then @x -= 1
    end
    self
  end
end

position = "nnneesw".chars.reduce(Turtle.new, :move)
position  
```

**Third Shortcut: Reducer With no Initial Value**

If your reducer returns a value that it can accept as a parameter, then you don’t have to pass in an initial value. Here `:*` is the name of the *times* function:

```
product = [ 2, 3, 4 ].inject(:*)
product 
```

`String` concatenation again:

```
s = [ "cat", " ", "dog" ].inject(:+)
s 
```

And an example that converts a hash to an array of two-element subarrays.

```
nested = {foo: 0, bar: 1}.inject([], :push)
nested 
```

Alias for:

inject

reject {|element| ... } → array

click to toggle source

reject → enumerator

Returns an array of objects rejected by the block.

With a block given, calls the block with successive elements; returns an array of those elements for which the block returns `nil` or `false`:

```
(0..9).reject {|i| i * 2 if i.even? }                             
{foo: 0, bar: 1, baz: 2}.reject {|key, value| key if value.odd? } 
```

When no block given, returns an `Enumerator`.

Related: `select`.

```
static VALUE
enum_reject(VALUE obj)
{
    VALUE ary;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    ary = rb_ary_new();
    rb_block_call(obj, id_each, 0, 0, reject_i, ary);

    return ary;
}
```

reverse_each(*args) {|element| ... } → self

click to toggle source

reverse_each(*args) → enumerator

With a block given, calls the block with each element, but in reverse order; returns `self`:

```
a = []
(1..4).reverse_each {|element| a.push(-element) } 
a 

a = []
%w[a b c d].reverse_each {|element| a.push(element) }

a 

a = []
h.reverse_each {|element| a.push(element) }

a 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_reverse_each(int argc, VALUE *argv, VALUE obj)
{
    VALUE ary;
    long len;

    RETURN_SIZED_ENUMERATOR(obj, argc, argv, enum_size);

    ary = enum_to_a(argc, argv, obj);

    len = RARRAY_LEN(ary);
    while (len--) {
        long nlen;
        rb_yield(RARRAY_AREF(ary, len));
        nlen = RARRAY_LEN(ary);
        if (nlen < len) {
            len = nlen;
        }
    }

    return obj;
}
```

select {|element| ... } → array

select → enumerator

Returns an array containing elements selected by the block.

With a block given, calls the block with successive elements; returns an array of those elements for which the block returns a truthy value:

```
(0..9).select {|element| element % 3 == 0 } 
a = {foo: 0, bar: 1, baz: 2}.select {|key, value| key.start_with?('b') }
a 
```

With no block given, returns an `Enumerator`.

Related: `reject`.

Alias for:

find_all

slice_after(pattern) → an_enumerator

click to toggle source

slice_after { |elt| bool } → an_enumerator

Creates an enumerator for each chunked elements. The ends of chunks are defined by *pattern* and the block.

If `*pattern* === *elt*` returns `true` or the block returns `true` for the element, the element is end of a chunk.

The `===` and *block* is called from the first element to the last element of *enum*.

The result enumerator yields the chunked elements as an array. So `each` method can be called as follows:

```
enum.slice_after(pattern).each { |ary| ... }
enum.slice_after { |elt| bool }.each { |ary| ... }
```

Other methods of the `Enumerator` class and `Enumerable` module, such as `map`, etc., are also usable.

For example, continuation lines (lines end with backslash) can be concatenated as follows:

```
lines = ["foo\n", "bar\\\n", "baz\n", "\n", "qux\n"]
e = lines.slice_after(/(?<!\\)\n\z/)
p e.to_a

p e.map {|ll| ll[0...-1].map {|l| l.sub(/\\\n\z/, "") }.join + ll.last }
```

```
static VALUE
enum_slice_after(int argc, VALUE *argv, VALUE enumerable)
{
    VALUE enumerator;
    VALUE pat = Qnil, pred = Qnil;

    if (rb_block_given_p()) {
        if (0 < argc)
            rb_raise(rb_eArgError, "both pattern and block are given");
        pred = rb_block_proc();
    }
    else {
        rb_scan_args(argc, argv, "1", &pat);
    }

    enumerator = rb_obj_alloc(rb_cEnumerator);
    rb_ivar_set(enumerator, id_sliceafter_enum, enumerable);
    rb_ivar_set(enumerator, id_sliceafter_pat, pat);
    rb_ivar_set(enumerator, id_sliceafter_pred, pred);

    rb_block_call(enumerator, idInitialize, 0, 0, sliceafter_i, enumerator);
    return enumerator;
}
```

slice_before(pattern) → enumerator

click to toggle source

slice_before {|elt| ... } → enumerator

With argument `pattern`, returns an enumerator that uses the pattern to partition elements into arrays (“slices”). An element begins a new slice if `element === pattern` (or if it is the first element).

```
a = %w[foo bar fop for baz fob fog bam foy]
e = a.slice_before(/ba/) 
e.each {|array| p array }
```

Output:

```
["foo"]
["bar", "fop", "for"]
["baz", "fob", "fog"]
["bam", "foy"]
```

With a block, returns an enumerator that uses the block to partition elements into arrays. An element begins a new slice if its block return is a truthy value (or if it is the first element):

```
e = (1..20).slice_before {|i| i % 4 == 2 } 
e.each {|array| p array }
```

Output:

```
[1]
[2, 3, 4, 5]
[6, 7, 8, 9]
[10, 11, 12, 13]
[14, 15, 16, 17]
[18, 19, 20]
```

Other methods of the `Enumerator` class and `Enumerable` module, such as `to_a`, `map`, etc., are also usable.

For example, iteration over ChangeLog entries can be implemented as follows:

```
open("ChangeLog") { |f|
  f.slice_before(/\A\S/).each { |e| pp e }
}

open("ChangeLog") { |f|
  f.slice_before { |line| /\A\S/ === line }.each { |e| pp e }
}
```

“svn proplist -R” produces multiline output for each file. They can be chunked as follows:

```
IO.popen([{"LC_ALL"=>"C"}, "svn", "proplist", "-R"]) { |f|
  f.lines.slice_before(/\AProp/).each { |lines| p lines }
}
```

If the block needs to maintain state over multiple elements, local variables can be used. For example, three or more consecutive increasing numbers can be squashed as follows (see `chunk_while` for a better way):

```
a = [0, 2, 3, 4, 6, 7, 9]
prev = a[0]
p a.slice_before { |e|
  prev, prev2 = e, prev
  prev2 + 1 != e
}.map { |es|
  es.length <= 2 ? es.join(",") : "#{es.first}-#{es.last}"
}.join(",")
```

However local variables should be used carefully if the result enumerator is enumerated twice or more. The local variables should be initialized for each enumeration. `Enumerator.new` can be used to do it.

```
def wordwrap(words, maxwidth)
  Enumerator.new {|y|
    
    cols = 0
    words.slice_before { |w|
      cols += 1 if cols != 0
      cols += w.length
      if maxwidth < cols
        cols = w.length
        true
      else
        false
      end
    }.each {|ws| y.yield ws }
  }
end
text = (1..20).to_a.join(" ")
enum = wordwrap(text.split(/\s+/), 10)
puts "-"*10
enum.each { |ws| puts ws.join(" ") } 
puts "-"*10
enum.each { |ws| puts ws.join(" ") } 
puts "-"*10
```

mbox contains series of mails which start with Unix From line. So each mail can be extracted by slice before Unix From line.

```
open("mbox") { |f|
  f.slice_before { |line|
    line.start_with? "From "
  }.each { |mail|
    unix_from = mail.shift
    i = mail.index("\n")
    header = mail[0...i]
    body = mail[(i+1)..-1]
    body.pop if body.last == "\n"
    fields = header.slice_before { |line| !" \t".include?(line[0]) }.to_a
    p unix_from
    pp fields
    pp body
  }
}

open("mbox") { |f|
  emp = true
  f.slice_before { |line|
    prevemp = emp
    emp = line == "\n"
    prevemp && line.start_with?("From ")
  }.each { |mail|
    mail.pop if mail.last == "\n"
    pp mail
  }
}
```

```
static VALUE
enum_slice_before(int argc, VALUE *argv, VALUE enumerable)
{
    VALUE enumerator;

    if (rb_block_given_p()) {
        if (argc != 0)
            rb_error_arity(argc, 0, 0);
        enumerator = rb_obj_alloc(rb_cEnumerator);
        rb_ivar_set(enumerator, id_slicebefore_sep_pred, rb_block_proc());
    }
    else {
        VALUE sep_pat;
        rb_scan_args(argc, argv, "1", &sep_pat);
        enumerator = rb_obj_alloc(rb_cEnumerator);
        rb_ivar_set(enumerator, id_slicebefore_sep_pat, sep_pat);
    }
    rb_ivar_set(enumerator, id_slicebefore_enumerable, enumerable);
    rb_block_call(enumerator, idInitialize, 0, 0, slicebefore_i, enumerator);
    return enumerator;
}
```

slice_when {|elt_before, elt_after| bool } → an_enumerator

click to toggle source

Creates an enumerator for each chunked elements. The beginnings of chunks are defined by the block.

This method splits each chunk using adjacent elements, *elt_before* and *elt_after*, in the receiver enumerator. This method split chunks between *elt_before* and *elt_after* where the block returns `true`.

The block is called the length of the receiver enumerator minus one.

The result enumerator yields the chunked elements as an array. So `each` method can be called as follows:

```
enum.slice_when { |elt_before, elt_after| bool }.each { |ary| ... }
```

Other methods of the `Enumerator` class and `Enumerable` module, such as `to_a`, `map`, etc., are also usable.

For example, one-by-one increasing subsequence can be chunked as follows:

```
a = [1,2,4,9,10,11,12,15,16,19,20,21]
b = a.slice_when {|i, j| i+1 != j }
p b.to_a 
c = b.map {|a| a.length < 3 ? a : "#{a.first}-#{a.last}" }
p c 
d = c.join(",")
p d 
```

Near elements (threshold: 6) in sorted array can be chunked as follows:

```
a = [3, 11, 14, 25, 28, 29, 29, 41, 55, 57]
p a.slice_when {|i, j| 6 < j - i }.to_a
```

Increasing (non-decreasing) subsequence can be chunked as follows:

```
a = [0, 9, 2, 2, 3, 2, 7, 5, 9, 5]
p a.slice_when {|i, j| i > j }.to_a
```

Adjacent evens and odds can be chunked as follows: (`Enumerable#chunk` is another way to do it.)

```
a = [7, 5, 9, 2, 0, 7, 9, 4, 2, 0]
p a.slice_when {|i, j| i.even? != j.even? }.to_a
```

Paragraphs (non-empty lines with trailing empty lines) can be chunked as follows: (See `Enumerable#chunk` to ignore empty lines.)

```
lines = ["foo\n", "bar\n", "\n", "baz\n", "qux\n"]
p lines.slice_when {|l1, l2| /\A\s*\z/ =~ l1 && /\S/ =~ l2 }.to_a
```

`Enumerable#chunk_while` does the same, except splitting when the block returns `false` instead of `true`.

```
static VALUE
enum_slice_when(VALUE enumerable)
{
    VALUE enumerator;
    VALUE pred;

    pred = rb_block_proc();

    enumerator = rb_obj_alloc(rb_cEnumerator);
    rb_ivar_set(enumerator, id_slicewhen_enum, enumerable);
    rb_ivar_set(enumerator, id_slicewhen_pred, pred);
    rb_ivar_set(enumerator, id_slicewhen_inverted, Qfalse);

    rb_block_call(enumerator, idInitialize, 0, 0, slicewhen_i, enumerator);
    return enumerator;
}
```

sort → array

click to toggle source

sort {|a, b| ... } → array

Returns an array containing the sorted elements of `self`. The ordering of equal elements is indeterminate and may be unstable.

With no block given, the sort compares using the elements’ own method `#<=>`:

```
%w[b c a d].sort              
{foo: 0, bar: 1, baz: 2}.sort 
```

With a block given, comparisons in the block determine the ordering. The block is called with two elements `a` and `b`, and must return:

- A negative integer if `a < b`.
- Zero if `a == b`.
- A positive integer if `a > b`.

Examples:

```
a = %w[b c a d]
a.sort {|a, b| b <=> a } 
h = {foo: 0, bar: 1, baz: 2}
h.sort {|a, b| b <=> a } 
```

See also `sort_by`. It implements a Schwartzian transform which is useful when key computation or comparison is expensive.

```
static VALUE
enum_sort(VALUE obj)
{
    return rb_ary_sort_bang(enum_to_a(0, 0, obj));
}
```

sort_by {|element| ... } → array

click to toggle source

sort_by → enumerator

With a block given, returns an array of elements of `self`, sorted according to the value returned by the block for each element. The ordering of equal elements is indeterminate and may be unstable.

Examples:

```
a = %w[xx xxx x xxxx]
a.sort_by {|s| s.size }        
a.sort_by {|s| -s.size }       
h = {foo: 2, bar: 1, baz: 0}
h.sort_by{|key, value| value } 
h.sort_by{|key, value| key }   
```

With no block given, returns an `Enumerator`.

The current implementation of `sort_by` generates an array of tuples containing the original collection element and the mapped value. This makes `sort_by` fairly expensive when the keysets are simple.

```
require 'benchmark'

a = (1..100000).map { rand(100000) }

Benchmark.bm(10) do |b|
  b.report("Sort")    { a.sort }
  b.report("Sort by") { a.sort_by { |a| a } }
end
```

*produces:*

```
user     system      total        real
Sort        0.180000   0.000000   0.180000 (  0.175469)
Sort by     1.980000   0.040000   2.020000 (  2.013586)
```

However, consider the case where comparing the keys is a non-trivial operation. The following code sorts some files on modification time using the basic `sort` method.

```
files = Dir["*"]
sorted = files.sort { |a, b| File.new(a).mtime <=> File.new(b).mtime }
sorted   
```

This sort is inefficient: it generates two new `File` objects during every comparison. A slightly better technique is to use the `Kernel#test` method to generate the modification times directly.

```
files = Dir["*"]
sorted = files.sort { |a, b|
  test(?M, a) <=> test(?M, b)
}
sorted   
```

This still generates many unnecessary `Time` objects. A more efficient technique is to cache the sort keys (modification times in this case) before the sort. Perl users often call this approach a Schwartzian transform, after Randal Schwartz. We construct a temporary array, where each element is an array containing our sort key along with the filename. We sort this array, and then extract the filename from the result.

```
sorted = Dir["*"].collect { |f|
   [test(?M, f), f]
}.sort.collect { |f| f[1] }
sorted   
```

This is exactly what `sort_by` does internally.

```
sorted = Dir["*"].sort_by { |f| test(?M, f) }
sorted   
```

To produce the reverse of a specific order, the following can be used:

```
ary.sort_by { ... }.reverse!
```

```
static VALUE
enum_sort_by(VALUE obj)
{
    VALUE ary, buf;
    struct MEMO *memo;
    long i;
    struct sort_by_data *data;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    if (RB_TYPE_P(obj, T_ARRAY) && RARRAY_LEN(obj) <= LONG_MAX/2) {
        ary = rb_ary_new2(RARRAY_LEN(obj)*2);
    }
    else {
        ary = rb_ary_new();
    }
    RBASIC_CLEAR_CLASS(ary);
    buf = rb_ary_hidden_new(SORT_BY_BUFSIZE*2);
    rb_ary_store(buf, SORT_BY_BUFSIZE*2-1, Qnil);
    memo = MEMO_NEW(0, 0, 0);
    data = (struct sort_by_data *)&memo->v1;
    RB_OBJ_WRITE(memo, &data->ary, ary);
    RB_OBJ_WRITE(memo, &data->buf, buf);
    data->n = 0;
    data->primitive_uniformed = SORT_BY_UNIFORMED((CMP_OPTIMIZABLE(FLOAT) && CMP_OPTIMIZABLE(INTEGER)),
                                                  CMP_OPTIMIZABLE(FLOAT),
                                                  CMP_OPTIMIZABLE(INTEGER));
    rb_block_call(obj, id_each, 0, 0, sort_by_i, (VALUE)memo);
    ary = data->ary;
    buf = data->buf;
    if (data->n) {
        rb_ary_resize(buf, data->n*2);
        rb_ary_concat(ary, buf);
    }
    if (RARRAY_LEN(ary) > 2) {
        if (data->primitive_uniformed) {
            RARRAY_PTR_USE(ary, ptr,
                           rb_uniform_intro_sort_2((struct rb_uniform_sort_data*)ptr,
                                                   (struct rb_uniform_sort_data*)(ptr + RARRAY_LEN(ary))));
        }
        else {
            RARRAY_PTR_USE(ary, ptr,
                           ruby_qsort(ptr, RARRAY_LEN(ary)/2, 2*sizeof(VALUE),
                                      sort_by_cmp, (void *)ary));
        }
    }
    if (RBASIC(ary)->klass) {
        rb_raise(rb_eRuntimeError, "sort_by reentered");
    }
    for (i=1; i<RARRAY_LEN(ary); i+=2) {
        RARRAY_ASET(ary, i/2, RARRAY_AREF(ary, i));
    }
    rb_ary_resize(ary, RARRAY_LEN(ary)/2);
    RBASIC_SET_CLASS_RAW(ary, rb_cArray);

    return ary;
}
```

sum(initial_value = 0) → number

click to toggle source

sum(initial_value = 0) {|element| ... } → object

With no block given, returns the sum of `initial_value` and the elements:

```
(1..100).sum          
(1..100).sum(1)       
('a'..'d').sum('foo') 
```

Generally, the sum is computed using methods `+` and `each`; for performance optimizations, those methods may not be used, and so any redefinition of those methods may not have effect here.

One such optimization: When possible, computes using Gauss’s summation formula *n(n+1)/2*:

```
100 * (100 + 1) / 2 
```

With a block given, calls the block with each element; returns the sum of `initial_value` and the block return values:

```
(1..4).sum {|i| i*i }                        
(1..4).sum(100) {|i| i*i }                   
h = {a: 0, b: 1, c: 2, d: 3, e: 4, f: 5}
h.sum {|key, value| value.odd? ? value : 0 } 
('a'..'f').sum('x') {|c| c < 'd' ? c : '' }  
```

```
static VALUE
enum_sum(int argc, VALUE* argv, VALUE obj)
{
    struct enum_sum_memo memo;
    VALUE beg, end;
    int excl;

    memo.v = (rb_check_arity(argc, 0, 1) == 0) ? LONG2FIX(0) : argv[0];
    memo.block_given = rb_block_given_p();
    memo.n = 0;
    memo.r = Qundef;

    if ((memo.float_value = RB_FLOAT_TYPE_P(memo.v))) {
        memo.f = RFLOAT_VALUE(memo.v);
        memo.c = 0.0;
    }
    else {
        memo.f = 0.0;
        memo.c = 0.0;
    }

    if (RTEST(rb_range_values(obj, &beg, &end, &excl))) {
        if (!memo.block_given && !memo.float_value &&
                (FIXNUM_P(beg) || RB_BIGNUM_TYPE_P(beg)) &&
                (FIXNUM_P(end) || RB_BIGNUM_TYPE_P(end))) {
            return int_range_sum(beg, end, excl, memo.v);
        }
    }

    if (RB_TYPE_P(obj, T_HASH) &&
            rb_method_basic_definition_p(CLASS_OF(obj), id_each))
        hash_sum(obj, &memo);
    else
        rb_block_call(obj, id_each, 0, 0, enum_sum_i, (VALUE)&memo);

    if (memo.float_value) {
        return DBL2NUM(memo.f + memo.c);
    }
    else {
        if (memo.n != 0)
            memo.v = rb_fix_plus(LONG2FIX(memo.n), memo.v);
        if (!UNDEF_P(memo.r)) {
            memo.v = rb_rational_plus(memo.r, memo.v);
        }
        return memo.v;
    }
}
```

take(n) → array

click to toggle source

For non-negative integer `n`, returns the first `n` elements:

```
r = (1..4)
r.take(2) 
r.take(0) 

h = {foo: 0, bar: 1, baz: 2, bat: 3}
h.take(2) 
```

```
static VALUE
enum_take(VALUE obj, VALUE n)
{
    struct MEMO *memo;
    VALUE result;
    long len = NUM2LONG(n);

    if (len < 0) {
        rb_raise(rb_eArgError, "attempt to take negative size");
    }

    if (len == 0) return rb_ary_new2(0);
    result = rb_ary_new2(len);
    memo = MEMO_NEW(result, 0, len);
    rb_block_call(obj, id_each, 0, 0, take_i, (VALUE)memo);
    return result;
}
```

take_while {|element| ... } → array

click to toggle source

take_while → enumerator

Calls the block with successive elements as long as the block returns a truthy value; returns an array of all elements up to that point:

```
(1..4).take_while{|i| i < 3 } 
h = {foo: 0, bar: 1, baz: 2}
h.take_while{|element| key, value = *element; value < 2 }
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_take_while(VALUE obj)
{
    VALUE ary;

    RETURN_ENUMERATOR(obj, 0, 0);
    ary = rb_ary_new();
    rb_block_call(obj, id_each, 0, 0, take_while_i, ary);
    return ary;
}
```

tally(hash = {}) → hash

click to toggle source

When argument `hash` is not given, returns a new hash whose keys are the distinct elements in `self`; each integer value is the count of occurrences of each element:

```
%w[a b c b c a c b].tally 
```

When argument `hash` is given, returns `hash`, possibly augmented; for each element `ele` in `self`:

- Adds it as a key with a zero value if that key does not already exist:
  ```
hash[ele] = 0 unless hash.include?(ele)
  ```
- Increments the value of key `ele`:
  ```
hash[ele] += 1
  ```

This is useful for accumulating tallies across multiple enumerables:

```
h = {}                   
%w[a c d b c a].tally(h) 
%w[b a z].tally(h)       
%w[b a m].tally(h)       
```

The key to be added or found for an element depends on the class of `self`; see Enumerable in Ruby Classes.

Examples:

- `Array` (and certain array-like classes): the key is the element (as above).
- `Hash` (and certain hash-like classes): the key is the 2-element array formed from the key-value pair:
  ```
h = {}                        
{foo: 'a', bar: 'b'}.tally(h) 
{foo: 'c', bar: 'd'}.tally(h) 
{foo: 'a', bar: 'b'}.tally(h) 
{foo: 'c', bar: 'd'}.tally(h) 
  ```

```
static VALUE
enum_tally(int argc, VALUE *argv, VALUE obj)
{
    VALUE hash;
    if (rb_check_arity(argc, 0, 1)) {
        hash = rb_to_hash_type(argv[0]);
        rb_check_frozen(hash);
    }
    else {
        hash = rb_hash_new();
    }

    return enum_hashify_into(obj, 0, 0, tally_i, hash);
}
```

to_a(*args) → array

click to toggle source

Returns an array containing the items in `self`:

```
(0..4).to_a 
```

```
static VALUE
enum_to_a(int argc, VALUE *argv, VALUE obj)
{
    VALUE ary = rb_ary_new();

    rb_block_call_kw(obj, id_each, argc, argv, collect_all, ary, RB_PASS_CALLED_KEYWORDS);

    return ary;
}
```

Also aliased as:

entries

to_h(*args) → hash

click to toggle source

to_h(*args) {|element| ... } → hash

When `self` consists of 2-element arrays, returns a hash each of whose entries is the key-value pair formed from one of those arrays:

```
[[:foo, 0], [:bar, 1], [:baz, 2]].to_h 
```

When a block is given, the block is called with each element of `self`; the block should return a 2-element array which becomes a key-value pair in the returned hash:

```
(0..3).to_h {|i| [i, i ** 2]} 
```

Raises an exception if an element of `self` is not a 2-element array, and a block is not passed.

```
static VALUE
enum_to_h(int argc, VALUE *argv, VALUE obj)
{
    rb_block_call_func *iter = rb_block_given_p() ? enum_to_h_ii : enum_to_h_i;
    return enum_hashify(obj, argc, argv, iter);
}
```

to_set

(klass = Set, *args, &block)

click to toggle source

Makes a set from the enumerable object with given arguments.

```
def to_set(klass = Set, *args, &block)
  klass.new(self, *args, &block)
end
```

uniq → array

click to toggle source

uniq {|element| ... } → array

With no block, returns a new array containing only unique elements; the array has no two elements `e0` and `e1` such that `e0.eql?(e1)`:

```
%w[a b c c b a a b c].uniq       
[0, 1, 2, 2, 1, 0, 0, 1, 2].uniq 
```

With a block, returns a new array containing elements only for which the block returns a unique value:

```
a = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
a.uniq {|i| i.even? ? i : 0 } 
a = %w[a b c d e e d c b a a b c d e]
a.uniq {|c| c < 'c' }         
```

```
static VALUE
enum_uniq(VALUE obj)
{
    VALUE hash, ret;
    rb_block_call_func *const func =
        rb_block_given_p() ? uniq_iter : uniq_func;

    hash = rb_obj_hide(rb_hash_new());
    rb_block_call(obj, id_each, 0, 0, func, hash);
    ret = rb_hash_values(hash);
    rb_hash_clear(hash);
    return ret;
}
```

zip(*other_enums) → array

click to toggle source

zip(*other_enums) {|array| ... } → nil

With no block given, returns a new array `new_array` of size self.size whose elements are arrays. Each nested array `new_array[n]` is of size `other_enums.size+1`, and contains:

- The `n`-th element of self.
- The `n`-th element of each of the `other_enums`.

If all `other_enums` and self are the same size, all elements are included in the result, and there is no `nil`-filling:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3]
c = [:c0, :c1, :c2, :c3]
d = a.zip(b, c)
d 

f = {foo: 0, bar: 1, baz: 2}
g = {goo: 3, gar: 4, gaz: 5}
h = {hoo: 6, har: 7, haz: 8}
d = f.zip(g, h)
d 
  
  
  
  
```

If any enumerable in other_enums is smaller than self, fills to `self.size` with `nil`:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2]
c = [:c0, :c1]
d = a.zip(b, c)
d 
```

If any enumerable in other_enums is larger than self, its trailing elements are ignored:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3, :b4]
c = [:c0, :c1, :c2, :c3, :c4, :c5]
d = a.zip(b, c)
d 
```

When a block is given, calls the block with each of the sub-arrays (formed as above); returns nil:

```
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3]
c = [:c0, :c1, :c2, :c3]
a.zip(b, c) {|sub_array| p sub_array} 
```

Output:

```
[:a0, :b0, :c0]
[:a1, :b1, :c1]
[:a2, :b2, :c2]
[:a3, :b3, :c3]
```

```
static VALUE
enum_zip(int argc, VALUE *argv, VALUE obj)
{
    int i;
    ID conv;
    struct MEMO *memo;
    VALUE result = Qnil;
    VALUE args = rb_ary_new4(argc, argv);
    int allary = TRUE;

    argv = RARRAY_PTR(args);
    for (i=0; i<argc; i++) {
        VALUE ary = rb_check_array_type(argv[i]);
        if (NIL_P(ary)) {
            allary = FALSE;
            break;
        }
        argv[i] = ary;
    }
    if (!allary) {
        static const VALUE sym_each = STATIC_ID2SYM(id_each);
        CONST_ID(conv, "to_enum");
        for (i=0; i<argc; i++) {
            if (!rb_respond_to(argv[i], id_each)) {
                rb_raise(rb_eTypeError, "wrong argument type %"PRIsVALUE" (must respond to :each)",
                         rb_obj_class(argv[i]));
            }
            argv[i] = rb_funcallv(argv[i], conv, 1, &sym_each);
        }
    }
    if (!rb_block_given_p()) {
        result = rb_ary_new();
    }

    /* TODO: use NODE_DOT2 as memo(v, v, -) */
    memo = MEMO_NEW(result, args, 0);
    rb_block_call(obj, id_each, 0, 0, allary ? zip_ary : zip_i, (VALUE)memo);

    return result;
}
```
