---
title: "class Hash (part 2/2)"
source: https://ruby-doc.org/core/Hash.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/2
---

# class Hash

click to toggle source

Returns a new `Hash` excluding entries for the given `keys`:

```
h = { a: 100, b: 200, c: 300 }
h.except(:a)          
```

Any given `keys` that are not found are ignored.

```
static VALUE
rb_hash_except(int argc, VALUE *argv, VALUE hash)
{
    int i;
    VALUE key, result;

    result = hash_dup_with_compare_by_id(hash);

    for (i = 0; i < argc; i++) {
        key = argv[i];
        rb_hash_delete(result, key);
    }
    compact_after_delete(result);

    return result;
}
```

fetch(key) → object

click to toggle source

fetch(key, default_value) → object

fetch(key) {|key| ... } → object

Returns the value for the given `key`, if found.

```
h = {foo: 0, bar: 1, baz: 2}
h.fetch(:bar) 
```

If `key` is not found and no block was given, returns `default_value`:

```
{}.fetch(:nosuch, :default) 
```

If `key` is not found and a block was given, yields `key` to the block and returns the block’s return value:

```
{}.fetch(:nosuch) {|key| "No key #{key}"} 
```

Raises `KeyError` if neither `default_value` nor a block was given.

Note that this method does not use the values of either `default` or `default_proc`.

```
static VALUE
rb_hash_fetch_m(int argc, VALUE *argv, VALUE hash)
{
    VALUE key;
    st_data_t val;
    long block_given;

    rb_check_arity(argc, 1, 2);
    key = argv[0];

    block_given = rb_block_given_p();
    if (block_given && argc == 2) {
        rb_warn("block supersedes default value argument");
    }

    if (hash_stlike_lookup(hash, key, &val)) {
        return (VALUE)val;
    }
    else {
        if (block_given) {
            return rb_yield(key);
        }
        else if (argc == 1) {
            VALUE desc = rb_protect(rb_inspect, key, 0);
            if (NIL_P(desc)) {
                desc = rb_any_to_s(key);
            }
            desc = rb_str_ellipsize(desc, 65);
            rb_key_err_raise(rb_sprintf("key not found: %"PRIsVALUE, desc), hash, key);
        }
        else {
            return argv[1];
        }
    }
}
```

fetch_values(*keys) → new_array

click to toggle source

fetch_values(*keys) {|key| ... } → new_array

Returns a new `Array` containing the values associated with the given keys *keys:

```
h = {foo: 0, bar: 1, baz: 2}
h.fetch_values(:baz, :foo) 
```

Returns a new empty `Array` if no arguments given.

When a block is given, calls the block with each missing key, treating the block’s return value as the value for that key:

```
h = {foo: 0, bar: 1, baz: 2}
values = h.fetch_values(:bar, :foo, :bad, :bam) {|key| key.to_s}
values 
```

When no block is given, raises an exception if any given key is not found.

```
static VALUE
rb_hash_fetch_values(int argc, VALUE *argv, VALUE hash)
{
    VALUE result = rb_ary_new2(argc);
    long i;

    for (i=0; i<argc; i++) {
        rb_ary_push(result, rb_hash_fetch(hash, argv[i]));
    }
    return result;
}
```

filter

()

Returns a new `Hash` object whose entries are those for which the block returns a truthy value:

```
h = {foo: 0, bar: 1, baz: 2}
h.select {|key, value| value < 2 } 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.select 
e.each {|key, value| value < 2 } 
```

Alias for:

select

filter!

()

Returns `self`, whose entries are those for which the block returns a truthy value:

```
h = {foo: 0, bar: 1, baz: 2}
h.select! {|key, value| value < 2 }  => {:foo=>0, :bar=>1}
```

Returns `nil` if no entries were removed.

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.select!  
e.each { |key, value| value < 2 } 
```

Alias for:

select!

flatten → new_array

click to toggle source

flatten(level) → new_array

Returns a new `Array` object that is a 1-dimensional flattening of `self`.

By default, nested Arrays are not flattened:

```
h = {foo: 0, bar: [:bat, 3], baz: 2}
h.flatten 
```

Takes the depth of recursive flattening from `Integer` argument `level`:

```
h = {foo: 0, bar: [:bat, [:baz, [:bat, ]]]}
h.flatten(1) 
h.flatten(2) 
h.flatten(3) 
h.flatten(4) 
```

When `level` is negative, flattens all nested Arrays:

```
h = {foo: 0, bar: [:bat, [:baz, [:bat, ]]]}
h.flatten(-1) 
h.flatten(-2) 
```

When `level` is zero, returns the equivalent of `to_a` :

```
h = {foo: 0, bar: [:bat, 3], baz: 2}
h.flatten(0) 
h.flatten(0) == h.to_a 
```

```
static VALUE
rb_hash_flatten(int argc, VALUE *argv, VALUE hash)
{
    VALUE ary;

    rb_check_arity(argc, 0, 1);

    if (argc) {
        int level = NUM2INT(argv[0]);

        if (level == 0) return rb_hash_to_a(hash);

        ary = rb_ary_new_capa(RHASH_SIZE(hash) * 2);
        rb_hash_foreach(hash, flatten_i, ary);
        level--;

        if (level > 0) {
            VALUE ary_flatten_level = INT2FIX(level);
            rb_funcallv(ary, id_flatten_bang, 1, &ary_flatten_level);
        }
        else if (level < 0) {
            /* flatten recursively */
            rb_funcallv(ary, id_flatten_bang, 0, 0);
        }
    }
    else {
        ary = rb_ary_new_capa(RHASH_SIZE(hash) * 2);
        rb_hash_foreach(hash, flatten_i, ary);
    }

    return ary;
}
```

has_key?(key) → true or false

Returns `true` if `key` is a key in `self`, otherwise `false`.

Alias for:

include?

has_value?(value) → true or false

click to toggle source

Returns `true` if `value` is a value in `self`, otherwise `false`.

```
static VALUE
rb_hash_has_value(VALUE hash, VALUE val)
{
    VALUE data[2];

    data[0] = Qfalse;
    data[1] = val;
    rb_hash_foreach(hash, rb_hash_search_value, (VALUE)data);
    return data[0];
}
```

Also aliased as:

value?

hash → an_integer

click to toggle source

Returns the `Integer` hash-code for the hash.

Two `Hash` objects have the same hash-code if their content is the same (regardless of order):

```
h1 = {foo: 0, bar: 1, baz: 2}
h2 = {baz: 2, bar: 1, foo: 0}
h2.hash == h1.hash 
h2.eql? h1 
```

```
static VALUE
rb_hash_hash(VALUE hash)
{
    st_index_t size = RHASH_SIZE(hash);
    st_index_t hval = rb_hash_start(size);
    hval = rb_hash_uint(hval, (st_index_t)rb_hash_hash);
    if (size) {
        rb_hash_foreach(hash, hash_i, (VALUE)&hval);
    }
    hval = rb_hash_end(hval);
    return ST2FIX(hval);
}
```

include?(key) → true or false

click to toggle source

Returns `true` if `key` is a key in `self`, otherwise `false`.

```
VALUE
rb_hash_has_key(VALUE hash, VALUE key)
{
    return RBOOL(hash_stlike_lookup(hash, key, NULL));
}
```

Also aliased as:

member?

,

has_key?

,

key?

initialize_copy

(other_hash) -> self

click to toggle source

Replaces the entire contents of `self` with the contents of `other_hash`; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.replace({bat: 3, bam: 4}) 
```

```
static VALUE
rb_hash_replace(VALUE hash, VALUE hash2)
{
    rb_hash_modify_check(hash);
    if (hash == hash2) return hash;
    if (hash_iterating_p(hash)) {
        rb_raise(rb_eRuntimeError, "can't replace hash during iteration");
    }
    hash2 = to_hash(hash2);

    COPY_DEFAULT(hash, hash2);

    if (RHASH_AR_TABLE_P(hash)) {
        hash_ar_free_and_clear_table(hash);
    }
    else {
        hash_st_free_and_clear_table(hash);
    }

    hash_copy(hash, hash2);

    return hash;
}
```

Also aliased as:

replace

inspect → new_string

click to toggle source

Returns a new `String` containing the hash entries:

```
h = {foo: 0, bar: 1, baz: 2}
h.inspect 
```

```
static VALUE
rb_hash_inspect(VALUE hash)
{
    if (RHASH_EMPTY_P(hash))
        return rb_usascii_str_new2("{}");
    return rb_exec_recursive(inspect_hash, hash, 0);
}
```

Also aliased as:

to_s

invert → new_hash

click to toggle source

Returns a new `Hash` object with the each key-value pair inverted:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = h.invert
h1 
```

Overwrites any repeated new keys: (see Entry Order):

```
h = {foo: 0, bar: 0, baz: 0}
h.invert 
```

```
static VALUE
rb_hash_invert(VALUE hash)
{
    VALUE h = rb_hash_new_with_size(RHASH_SIZE(hash));

    rb_hash_foreach(hash, rb_hash_invert_i, h);
    return h;
}
```

keep_if {|key, value| ... } → self

click to toggle source

keep_if → new_enumerator

Calls the block for each key-value pair; retains the entry if the block returns a truthy value; otherwise deletes the entry; returns `self`.

```
h = {foo: 0, bar: 1, baz: 2}
h.keep_if { |key, value| key.start_with?('b') } 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.keep_if 
e.each { |key, value| key.start_with?('b') } 
```

```
static VALUE
rb_hash_keep_if(VALUE hash)
{
    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_modify_check(hash);
    if (!RHASH_TABLE_EMPTY_P(hash)) {
        rb_hash_foreach(hash, keep_if_i, hash);
    }
    return hash;
}
```

key(value) → key or nil

click to toggle source

Returns the key for the first-found entry with the given `value` (see Entry Order):

```
h = {foo: 0, bar: 2, baz: 2}
h.key(0) 
h.key(2) 
```

Returns `nil` if no such value is found.

```
static VALUE
rb_hash_key(VALUE hash, VALUE value)
{
    VALUE args[2];

    args[0] = value;
    args[1] = Qnil;

    rb_hash_foreach(hash, key_i, (VALUE)args);

    return args[1];
}
```

key?(key) → true or false

Returns `true` if `key` is a key in `self`, otherwise `false`.

Alias for:

include?

keys → new_array

click to toggle source

Returns a new `Array` containing all keys in `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.keys 
```

```
VALUE
rb_hash_keys(VALUE hash)
{
    st_index_t size = RHASH_SIZE(hash);
    VALUE keys =  rb_ary_new_capa(size);

    if (size == 0) return keys;

    if (ST_DATA_COMPATIBLE_P(VALUE)) {
        RARRAY_PTR_USE(keys, ptr, {
            if (RHASH_AR_TABLE_P(hash)) {
                size = ar_keys(hash, ptr, size);
            }
            else {
                st_table *table = RHASH_ST_TABLE(hash);
                size = st_keys(table, ptr, size);
            }
        });
        rb_gc_writebarrier_remember(keys);
        rb_ary_set_len(keys, size);
    }
    else {
        rb_hash_foreach(hash, keys_i, keys);
    }

    return keys;
}
```

length → integer

Returns the count of entries in `self`:

```
{foo: 0, bar: 1, baz: 2}.length 
```

Alias for:

size

member?(key) → true or false

Returns `true` if `key` is a key in `self`, otherwise `false`.

Alias for:

include?

merge → copy_of_self

click to toggle source

merge(*other_hashes) → new_hash

merge(*other_hashes) { |key, old_value, new_value| ... } → new_hash

Returns the new `Hash` formed by merging each of `other_hashes` into a copy of `self`.

Each argument in `other_hashes` must be a `Hash`.

With arguments and no block:

- Returns the new `Hash` object formed by merging each successive `Hash` in `other_hashes` into `self`.
- Each new-key entry is added at the end.
- Each duplicate-key entry’s value overwrites the previous value.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h.merge(h1, h2) 
```

With arguments and a block:

- Returns a new `Hash` object that is the merge of `self` and each given hash.
- The given hashes are merged left to right.
- Each new-key entry is added at the end.
- For each duplicate key:
  - Calls the block with the key and the old and new values.
  - The block’s return value becomes the new value for the entry.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h3 = h.merge(h1, h2) { |key, old_value, new_value| old_value + new_value }
h3 
```

With no arguments:

- Returns a copy of `self`.
- The block, if given, is ignored.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h.merge 
h1 = h.merge { |key, old_value, new_value| raise 'Cannot happen' }
h1 
```

```
static VALUE
rb_hash_merge(int argc, VALUE *argv, VALUE self)
{
    return rb_hash_update(argc, argv, copy_compare_by_id(rb_hash_dup(self), self));
}
```

merge! → self

merge!(*other_hashes) → self

merge!(*other_hashes) { |key, old_value, new_value| ... } → self

Merges each of `other_hashes` into `self`; returns `self`.

Each argument in `other_hashes` must be a `Hash`.

With arguments and no block:

- Returns `self`, after the given hashes are merged into it.
- The given hashes are merged left to right.
- Each new entry is added at the end.
- Each duplicate-key entry’s value overwrites the previous value.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h.merge!(h1, h2) 
```

With arguments and a block:

- Returns `self`, after the given hashes are merged.
- The given hashes are merged left to right.
- Each new-key entry is added at the end.
- For each duplicate key:
  - Calls the block with the key and the old and new values.
  - The block’s return value becomes the new value for the entry.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h3 = h.merge!(h1, h2) { |key, old_value, new_value| old_value + new_value }
h3 
```

With no arguments:

- Returns `self`, unmodified.
- The block, if given, is ignored.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h.merge 
h1 = h.merge! { |key, old_value, new_value| raise 'Cannot happen' }
h1 
```

Alias for:

update

rassoc(value) → new_array or nil

click to toggle source

Returns a new 2-element `Array` consisting of the key and value of the first-found entry whose value is `==` to value (see Entry Order):

```
h = {foo: 0, bar: 1, baz: 1}
h.rassoc(1) 
```

Returns `nil` if no such value found.

```
static VALUE
rb_hash_rassoc(VALUE hash, VALUE obj)
{
    VALUE args[2];

    args[0] = obj;
    args[1] = Qnil;
    rb_hash_foreach(hash, rassoc_i, (VALUE)args);
    return args[1];
}
```

rehash → self

click to toggle source

Rebuilds the hash table by recomputing the hash index for each key; returns `self`.

The hash table becomes invalid if the hash value of a key has changed after the entry was created. See Modifying an Active Hash Key.

```
VALUE
rb_hash_rehash(VALUE hash)
{
    VALUE tmp;
    st_table *tbl;

    if (hash_iterating_p(hash)) {
        rb_raise(rb_eRuntimeError, "rehash during iteration");
    }
    rb_hash_modify_check(hash);
    if (RHASH_AR_TABLE_P(hash)) {
        tmp = hash_alloc(0);
        rb_hash_foreach(hash, rb_hash_rehash_i, (VALUE)tmp);

        hash_ar_free_and_clear_table(hash);
        ar_copy(hash, tmp);
    }
    else if (RHASH_ST_TABLE_P(hash)) {
        st_table *old_tab = RHASH_ST_TABLE(hash);
        tmp = hash_alloc(0);

        hash_st_table_init(tmp, old_tab->type, old_tab->num_entries);
        tbl = RHASH_ST_TABLE(tmp);

        rb_hash_foreach(hash, rb_hash_rehash_i, (VALUE)tmp);

        hash_st_free(hash);
        RHASH_ST_TABLE_SET(hash, tbl);
        RHASH_ST_CLEAR(tmp);
    }
    hash_verify(hash);
    return hash;
}
```

reject {|key, value| ... } → new_hash

click to toggle source

reject → new_enumerator

Returns a new `Hash` object whose entries are all those from `self` for which the block returns `false` or `nil`:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = h.reject {|key, value| key.start_with?('b') }
h1 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.reject 
h1 = e.each {|key, value| key.start_with?('b') }
h1 
```

```
static VALUE
rb_hash_reject(VALUE hash)
{
    VALUE result;

    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    result = hash_dup_with_compare_by_id(hash);
    if (!RHASH_EMPTY_P(hash)) {
        rb_hash_foreach(result, delete_if_i, result);
        compact_after_delete(result);
    }
    return result;
}
```

reject! {|key, value| ... } → self or nil

click to toggle source

reject! → new_enumerator

Returns `self`, whose remaining entries are those for which the block returns `false` or `nil`:

```
h = {foo: 0, bar: 1, baz: 2}
h.reject! {|key, value| value < 2 } 
```

Returns `nil` if no entries are removed.

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.reject! 
e.each {|key, value| key.start_with?('b') } 
```

```
static VALUE
rb_hash_reject_bang(VALUE hash)
{
    st_index_t n;

    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_modify(hash);
    n = RHASH_SIZE(hash);
    if (!n) return Qnil;
    rb_hash_foreach(hash, delete_if_i, hash);
    if (n == RHASH_SIZE(hash)) return Qnil;
    return hash;
}
```

replace(other_hash) → self

Replaces the entire contents of `self` with the contents of `other_hash`; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.replace({bat: 3, bam: 4}) 
```

Alias for:

initialize_copy

select {|key, value| ... } → new_hash

click to toggle source

select → new_enumerator

Returns a new `Hash` object whose entries are those for which the block returns a truthy value:

```
h = {foo: 0, bar: 1, baz: 2}
h.select {|key, value| value < 2 } 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.select 
e.each {|key, value| value < 2 } 
```

```
static VALUE
rb_hash_select(VALUE hash)
{
    VALUE result;

    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    result = hash_dup_with_compare_by_id(hash);
    if (!RHASH_EMPTY_P(hash)) {
        rb_hash_foreach(result, keep_if_i, result);
        compact_after_delete(result);
    }
    return result;
}
```

Also aliased as:

filter

select! {|key, value| ... } → self or nil

click to toggle source

select! → new_enumerator

Returns `self`, whose entries are those for which the block returns a truthy value:

```
h = {foo: 0, bar: 1, baz: 2}
h.select! {|key, value| value < 2 }  => {:foo=>0, :bar=>1}
```

Returns `nil` if no entries were removed.

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.select!  
e.each { |key, value| value < 2 } 
```

```
static VALUE
rb_hash_select_bang(VALUE hash)
{
    st_index_t n;

    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_modify_check(hash);
    n = RHASH_SIZE(hash);
    if (!n) return Qnil;
    rb_hash_foreach(hash, keep_if_i, hash);
    if (n == RHASH_SIZE(hash)) return Qnil;
    return hash;
}
```

Also aliased as:

filter!

shift → [key, value] or nil

click to toggle source

Removes the first hash entry (see Entry Order); returns a 2-element `Array` containing the removed key and value:

```
h = {foo: 0, bar: 1, baz: 2}
h.shift 
h 
```

Returns nil if the hash is empty.

```
static VALUE
rb_hash_shift(VALUE hash)
{
    struct shift_var var;

    rb_hash_modify_check(hash);
    if (RHASH_AR_TABLE_P(hash)) {
        var.key = Qundef;
        if (!hash_iterating_p(hash)) {
            if (ar_shift(hash, &var.key, &var.val)) {
                return rb_assoc_new(var.key, var.val);
            }
        }
        else {
            rb_hash_foreach(hash, shift_i_safe, (VALUE)&var);
            if (!UNDEF_P(var.key)) {
                rb_hash_delete_entry(hash, var.key);
                return rb_assoc_new(var.key, var.val);
            }
        }
    }
    if (RHASH_ST_TABLE_P(hash)) {
        var.key = Qundef;
        if (!hash_iterating_p(hash)) {
            if (st_shift(RHASH_ST_TABLE(hash), &var.key, &var.val)) {
                return rb_assoc_new(var.key, var.val);
            }
        }
        else {
            rb_hash_foreach(hash, shift_i_safe, (VALUE)&var);
            if (!UNDEF_P(var.key)) {
                rb_hash_delete_entry(hash, var.key);
                return rb_assoc_new(var.key, var.val);
            }
        }
    }
    return Qnil;
}
```

size → integer

click to toggle source

Returns the count of entries in `self`:

```
{foo: 0, bar: 1, baz: 2}.length 
```

```
VALUE
rb_hash_size(VALUE hash)
{
    return INT2FIX(RHASH_SIZE(hash));
}
```

Also aliased as:

length

slice(*keys) → new_hash

click to toggle source

Returns a new `Hash` object containing the entries for the given `keys`:

```
h = {foo: 0, bar: 1, baz: 2}
h.slice(:baz, :foo) 
```

Any given `keys` that are not found are ignored.

```
static VALUE
rb_hash_slice(int argc, VALUE *argv, VALUE hash)
{
    int i;
    VALUE key, value, result;

    if (argc == 0 || RHASH_EMPTY_P(hash)) {
        return copy_compare_by_id(rb_hash_new(), hash);
    }
    result = copy_compare_by_id(rb_hash_new_with_size(argc), hash);

    for (i = 0; i < argc; i++) {
        key = argv[i];
        value = rb_hash_lookup2(hash, key, Qundef);
        if (!UNDEF_P(value))
            rb_hash_aset(result, key, value);
    }

    return result;
}
```

store(key, value)

Associates the given `value` with the given `key`; returns `value`.

If the given `key` exists, replaces its value with the given `value`; the ordering is not affected (see Entry Order):

```
h = {foo: 0, bar: 1}
h[:foo] = 2 
h.store(:bar, 3) 
h 
```

If `key` does not exist, adds the `key` and `value`; the new entry is last in the order (see Entry Order):

```
h = {foo: 0, bar: 1}
h[:baz] = 2 
h.store(:bat, 3) 
h 
```

Alias for:

[]=

to_a → new_array

click to toggle source

Returns a new `Array` of 2-element `Array` objects; each nested `Array` contains a key-value pair from `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.to_a 
```

```
static VALUE
rb_hash_to_a(VALUE hash)
{
    VALUE ary;

    ary = rb_ary_new_capa(RHASH_SIZE(hash));
    rb_hash_foreach(hash, to_a_i, ary);

    return ary;
}
```

to_h → self or new_hash

click to toggle source

to_h {|key, value| ... } → new_hash

For an instance of `Hash`, returns `self`.

For a subclass of `Hash`, returns a new `Hash` containing the content of `self`.

When a block is given, returns a new `Hash` object whose content is based on the block; the block should return a 2-element `Array` object specifying the key-value pair to be included in the returned Array:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = h.to_h {|key, value| [value, key] }
h1 
```

```
static VALUE
rb_hash_to_h(VALUE hash)
{
    if (rb_block_given_p()) {
        return rb_hash_to_h_block(hash);
    }
    if (rb_obj_class(hash) != rb_cHash) {
        const VALUE flags = RBASIC(hash)->flags;
        hash = hash_dup(hash, rb_cHash, flags & RHASH_PROC_DEFAULT);
    }
    return hash;
}
```

to_hash → self

click to toggle source

Returns `self`.

```
static VALUE
rb_hash_to_hash(VALUE hash)
{
    return hash;
}
```

to_proc → proc

click to toggle source

Returns a `Proc` object that maps a key to its value:

```
h = {foo: 0, bar: 1, baz: 2}
proc = h.to_proc
proc.class 
proc.call(:foo) 
proc.call(:bar) 
proc.call(:nosuch) 
```

```
static VALUE
rb_hash_to_proc(VALUE hash)
{
    return rb_func_lambda_new(hash_proc_call, hash, 1, 1);
}
```

to_s

()

Returns a new `String` containing the hash entries:

```
h = {foo: 0, bar: 1, baz: 2}
h.inspect 
```

Alias for:

inspect

transform_keys {|key| ... } → new_hash

click to toggle source

transform_keys(hash2) → new_hash

transform_keys(hash2) {|other_key| ...} → new_hash

transform_keys → new_enumerator

Returns a new `Hash` object; each entry has:

- A key provided by the block.
- The value from `self`.

An optional hash argument can be provided to map keys to new keys. Any key not given will be mapped using the provided block, or remain the same if no block is given.

Transform keys:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = h.transform_keys {|key| key.to_s }
h1 

h.transform_keys(foo: :bar, bar: :foo)

h.transform_keys(foo: :hello, &:to_s)
```

Overwrites values for duplicate keys:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = h.transform_keys {|key| :bat }
h1 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.transform_keys 
h1 = e.each { |key| key.to_s }
h1 
```

```
static VALUE
rb_hash_transform_keys(int argc, VALUE *argv, VALUE hash)
{
    VALUE result;
    struct transform_keys_args transarg = {0};

    argc = rb_check_arity(argc, 0, 1);
    if (argc > 0) {
        transarg.trans = to_hash(argv[0]);
        transarg.block_given = rb_block_given_p();
    }
    else {
        RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    }
    result = rb_hash_new();
    if (!RHASH_EMPTY_P(hash)) {
        if (transarg.trans) {
            transarg.result = result;
            rb_hash_foreach(hash, transform_keys_hash_i, (VALUE)&transarg);
        }
        else {
            rb_hash_foreach(hash, transform_keys_i, result);
        }
    }

    return result;
}
```

transform_keys! {|key| ... } → self

click to toggle source

transform_keys!(hash2) → self

transform_keys!(hash2) {|other_key| ...} → self

transform_keys! → new_enumerator

Same as `Hash#transform_keys` but modifies the receiver in place instead of returning a new hash.

```
static VALUE
rb_hash_transform_keys_bang(int argc, VALUE *argv, VALUE hash)
{
    VALUE trans = 0;
    int block_given = 0;

    argc = rb_check_arity(argc, 0, 1);
    if (argc > 0) {
        trans = to_hash(argv[0]);
        block_given = rb_block_given_p();
    }
    else {
        RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    }
    rb_hash_modify_check(hash);
    if (!RHASH_TABLE_EMPTY_P(hash)) {
        long i;
        VALUE new_keys = hash_alloc(0);
        VALUE pairs = rb_ary_hidden_new(RHASH_SIZE(hash) * 2);
        rb_hash_foreach(hash, flatten_i, pairs);
        for (i = 0; i < RARRAY_LEN(pairs); i += 2) {
            VALUE key = RARRAY_AREF(pairs, i), new_key, val;

            if (!trans) {
                new_key = rb_yield(key);
            }
            else if (!UNDEF_P(new_key = rb_hash_lookup2(trans, key, Qundef))) {
                /* use the transformed key */
            }
            else if (block_given) {
                new_key = rb_yield(key);
            }
            else {
                new_key = key;
            }
            val = RARRAY_AREF(pairs, i+1);
            if (!hash_stlike_lookup(new_keys, key, NULL)) {
                rb_hash_stlike_delete(hash, &key, NULL);
            }
            rb_hash_aset(hash, new_key, val);
            rb_hash_aset(new_keys, new_key, Qnil);
        }
        rb_ary_clear(pairs);
        rb_hash_clear(new_keys);
    }
    compact_after_delete(hash);
    return hash;
}
```

transform_values {|value| ... } → new_hash

click to toggle source

transform_values → new_enumerator

Returns a new `Hash` object; each entry has:

- A key from `self`.
- A value provided by the block.

Transform values:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = h.transform_values {|value| value * 100}
h1 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.transform_values 
h1 = e.each { |value| value * 100}
h1 
```

```
static VALUE
rb_hash_transform_values(VALUE hash)
{
    VALUE result;

    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    result = hash_dup_with_compare_by_id(hash);
    SET_DEFAULT(result, Qnil);

    if (!RHASH_EMPTY_P(hash)) {
        rb_hash_stlike_foreach_with_replace(result, transform_values_foreach_func, transform_values_foreach_replace, result);
        compact_after_delete(result);
    }

    return result;
}
```

transform_values! {|value| ... } → self

click to toggle source

transform_values! → new_enumerator

Returns `self`, whose keys are unchanged, and whose values are determined by the given block.

```
h = {foo: 0, bar: 1, baz: 2}
h.transform_values! {|value| value * 100} 
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.transform_values! 
h1 = e.each {|value| value * 100}
h1 
```

```
static VALUE
rb_hash_transform_values_bang(VALUE hash)
{
    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_modify_check(hash);

    if (!RHASH_TABLE_EMPTY_P(hash)) {
        rb_hash_stlike_foreach_with_replace(hash, transform_values_foreach_func, transform_values_foreach_replace, hash);
    }

    return hash;
}
```

update

(*other_hashes) { |key, old_value, new_value| } -> self

click to toggle source

Merges each of `other_hashes` into `self`; returns `self`.

Each argument in `other_hashes` must be a `Hash`.

With arguments and no block:

- Returns `self`, after the given hashes are merged into it.
- The given hashes are merged left to right.
- Each new entry is added at the end.
- Each duplicate-key entry’s value overwrites the previous value.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h.merge!(h1, h2) 
```

With arguments and a block:

- Returns `self`, after the given hashes are merged.
- The given hashes are merged left to right.
- Each new-key entry is added at the end.
- For each duplicate key:
  - Calls the block with the key and the old and new values.
  - The block’s return value becomes the new value for the entry.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h3 = h.merge!(h1, h2) { |key, old_value, new_value| old_value + new_value }
h3 
```

With no arguments:

- Returns `self`, unmodified.
- The block, if given, is ignored.

Example:

```
h = {foo: 0, bar: 1, baz: 2}
h.merge 
h1 = h.merge! { |key, old_value, new_value| raise 'Cannot happen' }
h1 
```

```
static VALUE
rb_hash_update(int argc, VALUE *argv, VALUE self)
{
    int i;
    bool block_given = rb_block_given_p();

    rb_hash_modify(self);
    for (i = 0; i < argc; i++){
        VALUE hash = to_hash(argv[i]);
        if (block_given) {
            rb_hash_foreach(hash, rb_hash_update_block_i, self);
        }
        else {
            rb_hash_foreach(hash, rb_hash_update_i, self);
        }
    }
    return self;
}
```

Also aliased as:

merge!

value?(value) → true or false

Returns `true` if `value` is a value in `self`, otherwise `false`.

Alias for:

has_value?

values → new_array

click to toggle source

Returns a new `Array` containing all values in `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.values 
```

```
VALUE
rb_hash_values(VALUE hash)
{
    VALUE values;
    st_index_t size = RHASH_SIZE(hash);

    values = rb_ary_new_capa(size);
    if (size == 0) return values;

    if (ST_DATA_COMPATIBLE_P(VALUE)) {
        if (RHASH_AR_TABLE_P(hash)) {
            rb_gc_writebarrier_remember(values);
            RARRAY_PTR_USE(values, ptr, {
                size = ar_values(hash, ptr, size);
            });
        }
        else if (RHASH_ST_TABLE_P(hash)) {
            st_table *table = RHASH_ST_TABLE(hash);
            rb_gc_writebarrier_remember(values);
            RARRAY_PTR_USE(values, ptr, {
                size = st_values(table, ptr, size);
            });
        }
        rb_ary_set_len(values, size);
    }

    else {
        rb_hash_foreach(hash, values_i, values);
    }

    return values;
}
```

values_at(*keys) → new_array

click to toggle source

Returns a new `Array` containing values for the given `keys`:

```
h = {foo: 0, bar: 1, baz: 2}
h.values_at(:baz, :foo) 
```

The default values are returned for any keys that are not found:

```
h.values_at(:hello, :foo) 
```

```
static VALUE
rb_hash_values_at(int argc, VALUE *argv, VALUE hash)
{
    VALUE result = rb_ary_new2(argc);
    long i;

    for (i=0; i<argc; i++) {
        rb_ary_push(result, rb_hash_aref(hash, argv[i]));
    }
    return result;
}
```
