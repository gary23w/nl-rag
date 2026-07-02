---
title: "module Enumerable (part 2/3)"
source: https://ruby-doc.org/core/Enumerable.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/3
---

## About the Examples¶ ↑

The example code snippets for the Enumerable methods:

- Always show the use of one or more Array-like classes (often `Array` itself).
- Sometimes show the use of a Hash-like class. For some methods, though, the usage would not make sense, and so it is not shown. Example: `tally` would find exactly one of each `Hash` entry.

### Public Instance Methods

all? → true or false

click to toggle source

all?(pattern) → true or false

all? {|element| ... } → true or false

Returns whether every element meets a given criterion.

If `self` has no element, returns `true` and argument or block are not used.

With no argument and no block, returns whether every element is truthy:

```
(1..4).all?           
%w[a b c d].all?      
[1, 2, nil].all?      
['a','b', false].all? 
[].all?               
```

With argument `pattern` and no block, returns whether for each element `element`, `pattern === element`:

```
(1..4).all?(Integer)                 
(1..4).all?(Numeric)                 
(1..4).all?(Float)                   
%w[bar baz bat bam].all?(/ba/)       
%w[bar baz bat bam].all?(/bar/)      
%w[bar baz bat bam].all?('ba')       
{foo: 0, bar: 1, baz: 2}.all?(Array) 
{foo: 0, bar: 1, baz: 2}.all?(Hash)  
[].all?(Integer)                     
```

With a block given, returns whether the block returns a truthy value for every element:

```
(1..4).all? {|element| element < 5 }                    
(1..4).all? {|element| element < 4 }                    
{foo: 0, bar: 1, baz: 2}.all? {|key, value| value < 3 } 
{foo: 0, bar: 1, baz: 2}.all? {|key, value| value < 2 } 
```

Related: `any?`, `none?` `one?`.

```
static VALUE
enum_all(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo = MEMO_ENUM_NEW(Qtrue);
    WARN_UNUSED_BLOCK(argc);
    ENUM_BLOCK_CALL(all);
    return memo->v1;
}
```

any? → true or false

click to toggle source

any?(pattern) → true or false

any? {|element| ... } → true or false

Returns whether any element meets a given criterion.

If `self` has no element, returns `false` and argument or block are not used.

With no argument and no block, returns whether any element is truthy:

```
(1..4).any?          
%w[a b c d].any?     
[1, false, nil].any? 
[].any?              
```

With argument `pattern` and no block, returns whether for any element `element`, `pattern === element`:

```
[nil, false, 0].any?(Integer)        
[nil, false, 0].any?(Numeric)        
[nil, false, 0].any?(Float)          
%w[bar baz bat bam].any?(/m/)        
%w[bar baz bat bam].any?(/foo/)      
%w[bar baz bat bam].any?('ba')       
{foo: 0, bar: 1, baz: 2}.any?(Array) 
{foo: 0, bar: 1, baz: 2}.any?(Hash)  
[].any?(Integer)                     
```

With a block given, returns whether the block returns a truthy value for any element:

```
(1..4).any? {|element| element < 2 }                    
(1..4).any? {|element| element < 1 }                    
{foo: 0, bar: 1, baz: 2}.any? {|key, value| value < 1 } 
{foo: 0, bar: 1, baz: 2}.any? {|key, value| value < 0 } 
```

Related: `all?`, `none?`, `one?`.

```
static VALUE
enum_any(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo = MEMO_ENUM_NEW(Qfalse);
    WARN_UNUSED_BLOCK(argc);
    ENUM_BLOCK_CALL(any);
    return memo->v1;
}
```

chain(*enums) → enumerator

click to toggle source

Returns an enumerator object generated from this enumerator and given enumerables.

```
e = (1..3).chain([4, 5])
e.to_a 
```

```
static VALUE
enum_chain(int argc, VALUE *argv, VALUE obj)
{
    VALUE enums = rb_ary_new_from_values(1, &obj);
    rb_ary_cat(enums, argv, argc);
    return new_enum_chain(enums);
}
```

chunk {|array| ... } → enumerator

click to toggle source

Each element in the returned enumerator is a 2-element array consisting of:

- A value returned by the block.
- An array (“chunk”) containing the element for which that value was returned, and all following elements for which the block returned the same value:

So that:

- Each block return value that is different from its predecessor begins a new chunk.
- Each block return value that is the same as its predecessor continues the same chunk.

Example:

```
e = (0..10).chunk {|i| (i / 3).floor } 

e.next 
e.next 
e.next 
e.next 
```

Method `chunk` is especially useful for an enumerable that is already sorted. This example counts words for each initial letter in a large array of words:

```
url = 'https://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt'
words = URI::open(url).readlines

e = words.chunk {|word| word.upcase[0] } 

e.each {|c, words| p [c, words.length]; break if c == 'F' }
```

Output:

```
["A", 17096]
["B", 11070]
["C", 19901]
["D", 10896]
["E", 8736]
["F", 6860]
```

You can use the special symbol `:_alone` to force an element into its own separate chuck:

```
a = [0, 0, 1, 1]
e = a.chunk{|i| i.even? ? :_alone : true }
e.to_a 
```

For example, you can put each line that contains a URL into its own chunk:

```
pattern = /http/
open(filename) { |f|
  f.chunk { |line| line =~ pattern ? :_alone : true }.each { |key, lines|
    pp lines
  }
}
```

You can use the special symbol `:_separator` or `nil` to force an element to be ignored (not included in any chunk):

```
a = [0, 0, -1, 1, 1]
e = a.chunk{|i| i < 0 ? :_separator : true }
e.to_a 
```

Note that the separator does end the chunk:

```
a = [0, 0, -1, 1, -1, 1]
e = a.chunk{|i| i < 0 ? :_separator : true }
e.to_a 
```

For example, the sequence of hyphens in svn log can be eliminated as follows:

```
sep = "-"*72 + "\n"
IO.popen("svn log README") { |f|
  f.chunk { |line|
    line != sep || nil
  }.each { |_, lines|
    pp lines
  }
}
```

Paragraphs separated by empty lines can be parsed as follows:

```
File.foreach("README").chunk { |line|
  /\A\s*\z/ !~ line || nil
}.each { |_, lines|
  pp lines
}
```

```
static VALUE
enum_chunk(VALUE enumerable)
{
    VALUE enumerator;

    RETURN_SIZED_ENUMERATOR(enumerable, 0, 0, enum_size);

    enumerator = rb_obj_alloc(rb_cEnumerator);
    rb_ivar_set(enumerator, id_chunk_enumerable, enumerable);
    rb_ivar_set(enumerator, id_chunk_categorize, rb_block_proc());
    rb_block_call(enumerator, idInitialize, 0, 0, chunk_i, enumerator);
    return enumerator;
}
```

chunk_while {|elt_before, elt_after| bool } → an_enumerator

click to toggle source

Creates an enumerator for each chunked elements. The beginnings of chunks are defined by the block.

This method splits each chunk using adjacent elements, *elt_before* and *elt_after*, in the receiver enumerator. This method split chunks between *elt_before* and *elt_after* where the block returns `false`.

The block is called the length of the receiver enumerator minus one.

The result enumerator yields the chunked elements as an array. So `each` method can be called as follows:

```
enum.chunk_while { |elt_before, elt_after| bool }.each { |ary| ... }
```

Other methods of the `Enumerator` class and `Enumerable` module, such as `to_a`, `map`, etc., are also usable.

For example, one-by-one increasing subsequence can be chunked as follows:

```
a = [1,2,4,9,10,11,12,15,16,19,20,21]
b = a.chunk_while {|i, j| i+1 == j }
p b.to_a 
c = b.map {|a| a.length < 3 ? a : "#{a.first}-#{a.last}" }
p c 
d = c.join(",")
p d 
```

Increasing (non-decreasing) subsequence can be chunked as follows:

```
a = [0, 9, 2, 2, 3, 2, 7, 5, 9, 5]
p a.chunk_while {|i, j| i <= j }.to_a
```

Adjacent evens and odds can be chunked as follows: (`Enumerable#chunk` is another way to do it.)

```
a = [7, 5, 9, 2, 0, 7, 9, 4, 2, 0]
p a.chunk_while {|i, j| i.even? == j.even? }.to_a
```

`Enumerable#slice_when` does the same, except splitting when the block returns `true` instead of `false`.

```
static VALUE
enum_chunk_while(VALUE enumerable)
{
    VALUE enumerator;
    VALUE pred;

    pred = rb_block_proc();

    enumerator = rb_obj_alloc(rb_cEnumerator);
    rb_ivar_set(enumerator, id_slicewhen_enum, enumerable);
    rb_ivar_set(enumerator, id_slicewhen_pred, pred);
    rb_ivar_set(enumerator, id_slicewhen_inverted, Qtrue);

    rb_block_call(enumerator, idInitialize, 0, 0, slicewhen_i, enumerator);
    return enumerator;
}
```

collect

-> enumerator

click to toggle source

Returns an array of objects returned by the block.

With a block given, calls the block with successive elements; returns an array of the objects returned by the block:

```
(0..4).map {|i| i*i }                               
{foo: 0, bar: 1, baz: 2}.map {|key, value| value*2} 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_collect(VALUE obj)
{
    VALUE ary;
    int min_argc, max_argc;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    ary = rb_ary_new();
    min_argc = rb_block_min_max_arity(&max_argc);
    rb_lambda_call(obj, id_each, 0, 0, collect_i, min_argc, max_argc, ary);

    return ary;
}
```

Also aliased as:

map

collect_concat

()

Returns an array of flattened objects returned by the block.

With a block given, calls the block with successive elements; returns a flattened array of objects returned by the block:

```
[0, 1, 2, 3].flat_map {|element| -element }                    
[0, 1, 2, 3].flat_map {|element| [element, -element] }         
[[0, 1], [2, 3]].flat_map {|e| e + [100] }                     
{foo: 0, bar: 1, baz: 2}.flat_map {|key, value| [key, value] } 
```

With no block given, returns an `Enumerator`.

Alias: `collect_concat`.

Alias for:

flat_map

compact → array

click to toggle source

Returns an array of all non-`nil` elements:

```
a = [nil, 0, nil, 'a', false, nil, false, nil, 'a', nil, 0, nil]
a.compact 
```

```
static VALUE
enum_compact(VALUE obj)
{
    VALUE ary;

    ary = rb_ary_new();
    rb_block_call(obj, id_each, 0, 0, compact_i, ary);

    return ary;
}
```

count → integer

click to toggle source

count(object) → integer

count {|element| ... } → integer

Returns the count of elements, based on an argument or block criterion, if given.

With no argument and no block given, returns the number of elements:

```
[0, 1, 2].count                
{foo: 0, bar: 1, baz: 2}.count 
```

With argument `object` given, returns the number of elements that are `==` to `object`:

```
[0, 1, 2, 1].count(1)           
```

With a block given, calls the block with each element and returns the number of elements for which the block returns a truthy value:

```
[0, 1, 2, 3].count {|element| element < 2}              
{foo: 0, bar: 1, baz: 2}.count {|key, value| value < 2} 
```

```
static VALUE
enum_count(int argc, VALUE *argv, VALUE obj)
{
    VALUE item = Qnil;
    struct MEMO *memo;
    rb_block_call_func *func;

    if (argc == 0) {
        if (rb_block_given_p()) {
            func = count_iter_i;
        }
        else {
            func = count_all_i;
        }
    }
    else {
        rb_scan_args(argc, argv, "1", &item);
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        func = count_i;
    }

    memo = MEMO_NEW(item, 0, 0);
    rb_block_call(obj, id_each, 0, 0, func, (VALUE)memo);
    return imemo_count_value(memo);
}
```

cycle(n = nil) {|element| ...} → nil

click to toggle source

cycle(n = nil) → enumerator

When called with positive integer argument `n` and a block, calls the block with each element, then does so again, until it has done so `n` times; returns `nil`:

```
a = []
(1..4).cycle(3) {|element| a.push(element) } 
a 
a = []
('a'..'d').cycle(2) {|element| a.push(element) }
a 
a = []
{foo: 0, bar: 1, baz: 2}.cycle(2) {|element| a.push(element) }
a 
```

If count is zero or negative, does not call the block.

When called with a block and `n` is `nil`, cycles forever.

When no block is given, returns an `Enumerator`.

```
static VALUE
enum_cycle(int argc, VALUE *argv, VALUE obj)
{
    VALUE ary;
    VALUE nv = Qnil;
    long n, i, len;

    rb_check_arity(argc, 0, 1);

    RETURN_SIZED_ENUMERATOR(obj, argc, argv, enum_cycle_size);
    if (!argc || NIL_P(nv = argv[0])) {
        n = -1;
    }
    else {
        n = NUM2LONG(nv);
        if (n <= 0) return Qnil;
    }
    ary = rb_ary_new();
    RBASIC_CLEAR_CLASS(ary);
    rb_block_call(obj, id_each, 0, 0, cycle_i, ary);
    len = RARRAY_LEN(ary);
    if (len == 0) return Qnil;
    while (n < 0 || 0 < --n) {
        for (i=0; i<len; i++) {
            enum_yield_array(RARRAY_AREF(ary, i));
        }
    }
    return Qnil;
}
```

detect

(*args)

Returns the first element for which the block returns a truthy value.

With a block given, calls the block with successive elements of the collection; returns the first element for which the block returns a truthy value:

```
(0..9).find {|element| element > 2}                
```

If no such element is found, calls `if_none_proc` and returns its return value.

```
(0..9).find(proc {false}) {|element| element > 12} 
{foo: 0, bar: 1, baz: 2}.find {|key, value| key.start_with?('b') }            
{foo: 0, bar: 1, baz: 2}.find(proc {[]}) {|key, value| key.start_with?('c') } 
```

With no block given, returns an `Enumerator`.

Alias for:

find

drop(n) → array

click to toggle source

For positive integer `n`, returns an array containing all but the first `n` elements:

```
r = (1..4)
r.drop(3)  
r.drop(2)  
r.drop(1)  
r.drop(0)  
r.drop(50) 

h = {foo: 0, bar: 1, baz: 2, bat: 3}
h.drop(2) 
```

```
static VALUE
enum_drop(VALUE obj, VALUE n)
{
    VALUE result;
    struct MEMO *memo;
    long len = NUM2LONG(n);

    if (len < 0) {
        rb_raise(rb_eArgError, "attempt to drop negative size");
    }

    result = rb_ary_new();
    memo = MEMO_NEW(result, 0, len);
    rb_block_call(obj, id_each, 0, 0, drop_i, (VALUE)memo);
    return result;
}
```

drop_while {|element| ... } → array

click to toggle source

drop_while → enumerator

Calls the block with successive elements as long as the block returns a truthy value; returns an array of all elements after that point:

```
(1..4).drop_while{|i| i < 3 } 
h = {foo: 0, bar: 1, baz: 2}
a = h.drop_while{|element| key, value = *element; value < 2 }
a 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_drop_while(VALUE obj)
{
    VALUE result;
    struct MEMO *memo;

    RETURN_ENUMERATOR(obj, 0, 0);
    result = rb_ary_new();
    memo = MEMO_NEW(result, 0, FALSE);
    rb_block_call(obj, id_each, 0, 0, drop_while_i, (VALUE)memo);
    return result;
}
```

each_cons(n) { ... } → self

click to toggle source

each_cons(n) → enumerator

Calls the block with each successive overlapped `n`-tuple of elements; returns `self`:

```
a = []
(1..5).each_cons(3) {|element| a.push(element) }
a 

a = []
h = {foo: 0,  bar: 1, baz: 2, bam: 3}
h.each_cons(2) {|element| a.push(element) }
a 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_each_cons(VALUE obj, VALUE n)
{
    long size = NUM2LONG(n);
    struct MEMO *memo;
    int arity;

    if (size <= 0) rb_raise(rb_eArgError, "invalid size");
    RETURN_SIZED_ENUMERATOR(obj, 1, &n, enum_each_cons_size);
    arity = rb_block_arity();
    if (enum_size_over_p(obj, size)) return obj;
    memo = MEMO_NEW(rb_ary_new2(size), dont_recycle_block_arg(arity), size);
    rb_block_call(obj, id_each, 0, 0, each_cons_i, (VALUE)memo);

    return obj;
}
```

each_entry(*args) {|element| ... } → self

click to toggle source

each_entry(*args) → enumerator

Calls the given block with each element, converting multiple values from yield to an array; returns `self`:

```
a = []
(1..4).each_entry {|element| a.push(element) } 
a 

a = []
h = {foo: 0, bar: 1, baz:2}
h.each_entry {|element| a.push(element) }

a 

class Foo
  include Enumerable
  def each
    yield 1
    yield 1, 2
    yield
  end
end
Foo.new.each_entry {|yielded| p yielded }
```

Output:

```
1
[1, 2]
nil
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_each_entry(int argc, VALUE *argv, VALUE obj)
{
    RETURN_SIZED_ENUMERATOR(obj, argc, argv, enum_size);
    rb_block_call(obj, id_each, argc, argv, each_val_i, 0);
    return obj;
}
```

each_slice(n) { ... } → self

click to toggle source

each_slice(n) → enumerator

Calls the block with each successive disjoint `n`-tuple of elements; returns `self`:

```
a = []
(1..10).each_slice(3) {|tuple| a.push(tuple) }
a 

a = []
h = {foo: 0, bar: 1, baz: 2, bat: 3, bam: 4}
h.each_slice(2) {|tuple| a.push(tuple) }
a 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_each_slice(VALUE obj, VALUE n)
{
    long size = NUM2LONG(n);
    VALUE ary;
    struct MEMO *memo;
    int arity;

    if (size <= 0) rb_raise(rb_eArgError, "invalid slice size");
    RETURN_SIZED_ENUMERATOR(obj, 1, &n, enum_each_slice_size);
    size = limit_by_enum_size(obj, size);
    ary = rb_ary_new2(size);
    arity = rb_block_arity();
    memo = MEMO_NEW(ary, dont_recycle_block_arg(arity), size);
    rb_block_call(obj, id_each, 0, 0, each_slice_i, (VALUE)memo);
    ary = memo->v1;
    if (RARRAY_LEN(ary) > 0) rb_yield(ary);

    return obj;
}
```

each_with_index(*args) {|element, i| ..... } → self

click to toggle source

each_with_index(*args) → enumerator

Invoke `self.each` with `*args`. With a block given, the block receives each element and its index; returns `self`:

```
h = {}
(1..4).each_with_index {|element, i| h[element] = i } 
h 

h = {}
%w[a b c d].each_with_index {|element, i| h[element] = i }

h 

a = []
h = {foo: 0, bar: 1, baz: 2}
h.each_with_index {|element, i| a.push([i, element]) }

a 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_each_with_index(int argc, VALUE *argv, VALUE obj)
{
    RETURN_SIZED_ENUMERATOR(obj, argc, argv, enum_size);

    rb_block_call(obj, id_each, argc, argv, each_with_index_i, INT2FIX(0));
    return obj;
}
```

each_with_object(object) { |(*args), memo_object| ... } → object

click to toggle source

each_with_object(object) → enumerator

Calls the block once for each element, passing both the element and the given object:

```
(1..4).each_with_object([]) {|i, a| a.push(i**2) }

{foo: 0, bar: 1, baz: 2}.each_with_object({}) {|(k, v), h| h[v] = k }
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_each_with_object(VALUE obj, VALUE memo)
{
    RETURN_SIZED_ENUMERATOR(obj, 1, &memo, enum_size);

    rb_block_call(obj, id_each, 0, 0, each_with_object_i, memo);

    return memo;
}
```

entries

(*args)

Returns an array containing the items in `self`:

```
(0..4).to_a 
```

Alias for:

to_a

filter

()

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

filter_map {|element| ... } → array

click to toggle source

filter_map → enumerator

Returns an array containing truthy elements returned by the block.

With a block given, calls the block with successive elements; returns an array containing each truthy value returned by the block:

```
(0..9).filter_map {|i| i * 2 if i.even? }                              
{foo: 0, bar: 1, baz: 2}.filter_map {|key, value| key if value.even? } 
```

When no block given, returns an `Enumerator`.

```
static VALUE
enum_filter_map(VALUE obj)
{
    VALUE ary;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    ary = rb_ary_new();
    rb_block_call(obj, id_each, 0, 0, filter_map_i, ary);

    return ary;
}
```

find(if_none_proc = nil) {|element| ... } → object or nil

click to toggle source

find(if_none_proc = nil) → enumerator

Returns the first element for which the block returns a truthy value.

With a block given, calls the block with successive elements of the collection; returns the first element for which the block returns a truthy value:

```
(0..9).find {|element| element > 2}                
```

If no such element is found, calls `if_none_proc` and returns its return value.

```
(0..9).find(proc {false}) {|element| element > 12} 
{foo: 0, bar: 1, baz: 2}.find {|key, value| key.start_with?('b') }            
{foo: 0, bar: 1, baz: 2}.find(proc {[]}) {|key, value| key.start_with?('c') } 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_find(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo;
    VALUE if_none;

    if_none = rb_check_arity(argc, 0, 1) ? argv[0] : Qnil;
    RETURN_ENUMERATOR(obj, argc, argv);
    memo = MEMO_NEW(Qundef, 0, 0);
    if (rb_block_pair_yield_optimizable())
        rb_block_call2(obj, id_each, 0, 0, find_i_fast, (VALUE)memo, RB_BLOCK_NO_USE_PACKED_ARGS);
    else
        rb_block_call2(obj, id_each, 0, 0, find_i, (VALUE)memo, RB_BLOCK_NO_USE_PACKED_ARGS);
    if (memo->u3.cnt) {
        return memo->v1;
    }
    if (!NIL_P(if_none)) {
        return rb_funcallv(if_none, id_call, 0, 0);
    }
    return Qnil;
}
```

Also aliased as:

detect

find_all

-> enumerator

click to toggle source

Returns an array containing elements selected by the block.

With a block given, calls the block with successive elements; returns an array of those elements for which the block returns a truthy value:

```
(0..9).select {|element| element % 3 == 0 } 
a = {foo: 0, bar: 1, baz: 2}.select {|key, value| key.start_with?('b') }
a 
```

With no block given, returns an `Enumerator`.

Related: `reject`.

```
static VALUE
enum_find_all(VALUE obj)
{
    VALUE ary;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    ary = rb_ary_new();
    rb_block_call(obj, id_each, 0, 0, find_all_i, ary);

    return ary;
}
```

Also aliased as:

select

,

filter

find_index(object) → integer or nil

click to toggle source

find_index {|element| ... } → integer or nil

find_index → enumerator

Returns the index of the first element that meets a specified criterion, or `nil` if no such element is found.

With argument `object` given, returns the index of the first element that is `==` `object`:

```
['a', 'b', 'c', 'b'].find_index('b') 
```

With a block given, calls the block with successive elements; returns the first element for which the block returns a truthy value:

```
['a', 'b', 'c', 'b'].find_index {|element| element.start_with?('b') } 
{foo: 0, bar: 1, baz: 2}.find_index {|key, value| value > 1 }         
```

With no argument and no block given, returns an `Enumerator`.

```
static VALUE
enum_find_index(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo;  /* [return value, current index, ] */
    VALUE condition_value = Qnil;
    rb_block_call_func *func;

    if (argc == 0) {
        RETURN_ENUMERATOR(obj, 0, 0);
        func = find_index_iter_i;
    }
    else {
        rb_scan_args(argc, argv, "1", &condition_value);
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        func = find_index_i;
    }

    memo = MEMO_NEW(Qnil, condition_value, 0);
    rb_block_call(obj, id_each, 0, 0, func, (VALUE)memo);
    return memo->v1;
}
```

first → element or nil

click to toggle source

first(n) → array

Returns the first element or elements.

With no argument, returns the first element, or `nil` if there is none:

```
(1..4).first                   
%w[a b c].first                
{foo: 1, bar: 1, baz: 2}.first 
[].first                       
```

With integer argument `n`, returns an array containing the first `n` elements that exist:

```
(1..4).first(2)                   
%w[a b c d].first(3)              
%w[a b c d].first(50)             
{foo: 1, bar: 1, baz: 2}.first(2) 
[].first(2)                       
```

```
static VALUE
enum_first(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo;
    rb_check_arity(argc, 0, 1);
    if (argc > 0) {
        return enum_take(obj, argv[0]);
    }
    else {
        memo = MEMO_NEW(Qnil, 0, 0);
        rb_block_call(obj, id_each, 0, 0, first_i, (VALUE)memo);
        return memo->v1;
    }
}
```

flat_map {|element| ... } → array

click to toggle source

flat_map → enumerator

Returns an array of flattened objects returned by the block.

With a block given, calls the block with successive elements; returns a flattened array of objects returned by the block:

```
[0, 1, 2, 3].flat_map {|element| -element }                    
[0, 1, 2, 3].flat_map {|element| [element, -element] }         
[[0, 1], [2, 3]].flat_map {|e| e + [100] }                     
{foo: 0, bar: 1, baz: 2}.flat_map {|key, value| [key, value] } 
```

With no block given, returns an `Enumerator`.

Alias: `collect_concat`.

```
static VALUE
enum_flat_map(VALUE obj)
{
    VALUE ary;

    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    ary = rb_ary_new();
    rb_block_call(obj, id_each, 0, 0, flat_map_i, ary);

    return ary;
}
```

Also aliased as:

collect_concat

grep(pattern) → array

click to toggle source

grep(pattern) {|element| ... } → array

Returns an array of objects based elements of `self` that match the given pattern.

With no block given, returns an array containing each element for which `pattern === element` is `true`:

```
a = ['foo', 'bar', 'car', 'moo']
a.grep(/ar/)                   
(1..10).grep(3..8)             
['a', 'b', 0, 1].grep(Integer) 
```

With a block given, calls the block with each matching element and returns an array containing each object returned by the block:

```
a = ['foo', 'bar', 'car', 'moo']
a.grep(/ar/) {|element| element.upcase } 
```

Related: `grep_v`.

```
static VALUE
enum_grep(VALUE obj, VALUE pat)
{
    return enum_grep0(obj, pat, Qtrue);
}
```

grep_v(pattern) → array

click to toggle source

grep_v(pattern) {|element| ... } → array

Returns an array of objects based on elements of `self` that *don’t* match the given pattern.

With no block given, returns an array containing each element for which `pattern === element` is `false`:

```
a = ['foo', 'bar', 'car', 'moo']
a.grep_v(/ar/)                   
(1..10).grep_v(3..8)             
['a', 'b', 0, 1].grep_v(Integer) 
```

With a block given, calls the block with each non-matching element and returns an array containing each object returned by the block:

```
a = ['foo', 'bar', 'car', 'moo']
a.grep_v(/ar/) {|element| element.upcase } 
```

Related: `grep`.

```
static VALUE
enum_grep_v(VALUE obj, VALUE pat)
{
    return enum_grep0(obj, pat, Qfalse);
}
```

group_by {|element| ... } → hash

click to toggle source

group_by → enumerator

With a block given returns a hash:

- Each key is a return value from the block.
- Each value is an array of those elements for which the block returned that key.

Examples:

```
g = (1..6).group_by {|i| i%3 }
g 
h = {foo: 0, bar: 1, baz: 0, bat: 1}
g = h.group_by {|key, value| value }
g 
```

With no block given, returns an `Enumerator`.

```
static VALUE
enum_group_by(VALUE obj)
{
    RETURN_SIZED_ENUMERATOR(obj, 0, 0, enum_size);

    return enum_hashify(obj, 0, 0, group_by_i);
}
```

include?(object) → true or false

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

Alias for:

member?

inject(symbol) → object

click to toggle source

inject(initial_value, symbol) → object

inject {|memo, value| ... } → object

inject(initial_value) {|memo, value| ... } → object

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

```
static VALUE
enum_inject(int argc, VALUE *argv, VALUE obj)
{
    struct MEMO *memo;
    VALUE init, op;
    rb_block_call_func *iter = inject_i;
    ID id;
    int num_args;

    if (rb_block_given_p()) {
        num_args = rb_scan_args(argc, argv, "02", &init, &op);
    }
    else {
        num_args = rb_scan_args(argc, argv, "11", &init, &op);
    }

    switch (num_args) {
      case 0:
        init = Qundef;
        break;
      case 1:
        if (rb_block_given_p()) {
            break;
        }
        id = rb_check_id(&init);
        op = id ? ID2SYM(id) : init;
        init = Qundef;
        iter = inject_op_i;
        break;
      case 2:
        if (rb_block_given_p()) {
            rb_warning("given block not used");
        }
        id = rb_check_id(&op);
        if (id) op = ID2SYM(id);
        iter = inject_op_i;
        break;
    }

    if (iter == inject_op_i &&
        SYMBOL_P(op) &&
        RB_TYPE_P(obj, T_ARRAY) &&
        rb_method_basic_definition_p(CLASS_OF(obj), id_each)) {
        return ary_inject_op(obj, init, op);
    }

    memo = MEMO_NEW(init, Qnil, op);
    rb_block_call(obj, id_each, 0, 0, iter, (VALUE)memo);
    if (UNDEF_P(memo->v1)) return Qnil;
    return memo->v1;
}
```

Also aliased as:

reduce

lazy → lazy_enumerator

click to toggle source

Returns an `Enumerator::Lazy`, which redefines most `Enumerable` methods to postpone enumeration and enumerate values only on an as-needed basis.

### Example¶ ↑

The following program finds pythagorean triples:

```
def pythagorean_triples
  (1..Float::INFINITY).lazy.flat_map {|z|
    (1..z).flat_map {|x|
      (x..z).select {|y|
        x**2 + y**2 == z**2
      }.map {|y|
        [x, y, z]
      }
    }
  }
end

p pythagorean_triples.take(10).force 
p pythagorean_triples.first(10)      

p pythagorean_triples.take_while { |*, z| z < 100 }.force
```

```
static VALUE
enumerable_lazy(VALUE obj)
{
    VALUE result = lazy_to_enum_i(obj, sym_each, 0, 0, lazyenum_size, rb_keyword_given_p());
    /* Qfalse indicates that the Enumerator::Lazy has no method name */
    rb_ivar_set(result, id_method, Qfalse);
    return result;
}
```

map {|element| ... } → array

map → enumerator

Returns an array of objects returned by the block.

With a block given, calls the block with successive elements; returns an array of the objects returned by the block:

```
(0..4).map {|i| i*i }                               
{foo: 0, bar: 1, baz: 2}.map {|key, value| value*2} 
```

With no block given, returns an `Enumerator`.

Alias for:

collect

max → element

click to toggle source

max(n) → array

max {|a, b| ... } → element

max(n) {|a, b| ... } → array

Returns the element with the maximum element according to a given criterion. The ordering of equal elements is indeterminate and may be unstable.

With no argument and no block, returns the maximum element, using the elements’ own method `#<=>` for comparison:

```
(1..4).max                   
(-4..-1).max                 
%w[d c b a].max              
{foo: 0, bar: 1, baz: 2}.max 
[].max                       
```

With positive integer argument `n` given, and no block, returns an array containing the first `n` maximum elements that exist:

```
(1..4).max(2)                   
(-4..-1).max(2)                
%w[d c b a].max(2)              
{foo: 0, bar: 1, baz: 2}.max(2) 
[].max(2)                       
```

With a block given, the block determines the maximum elements. The block is called with two elements `a` and `b`, and must return:
