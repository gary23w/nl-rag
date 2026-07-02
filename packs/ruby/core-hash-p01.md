---
title: "class Hash (part 1/2)"
source: https://ruby-doc.org/core/Hash.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 1/2
---

# class Hash

A `Hash` maps each of its unique keys to a specific value.

A `Hash` has certain similarities to an `Array`, but:

- An `Array` index is always an `Integer`.
- A `Hash` key can be (almost) any object.

### `Hash` Data Syntax¶ ↑

The older syntax for `Hash` data uses the “hash rocket,” `=>`:

```
h = {:foo => 0, :bar => 1, :baz => 2}
h 
```

Alternatively, but only for a `Hash` key that’s a `Symbol`, you can use a newer JSON-style syntax, where each bareword becomes a Symbol:

```
h = {foo: 0, bar: 1, baz: 2}
h 
```

You can also use a `String` in place of a bareword:

```
h = {'foo': 0, 'bar': 1, 'baz': 2}
h 
```

And you can mix the styles:

```
h = {foo: 0, :bar => 1, 'baz': 2}
h 
```

But it’s an error to try the JSON-style syntax for a key that’s not a bareword or a String:

```

# Raises SyntaxError (syntax error, unexpected ':', expecting =>):
h = {0: 'zero'}
```

`Hash` value can be omitted, meaning that value will be fetched from the context by the name of the key:

```
x = 0
y = 100
h = {x:, y:}
h 
```

### Common Uses¶ ↑

You can use a `Hash` to give names to objects:

```
person = {name: 'Matz', language: 'Ruby'}
person 
```

You can use a `Hash` to give names to method arguments:

```
def some_method(hash)
  p hash
end
some_method({foo: 0, bar: 1, baz: 2}) 
```

Note: when the last argument in a method call is a `Hash`, the curly braces may be omitted:

```
some_method(foo: 0, bar: 1, baz: 2) 
```

You can use a `Hash` to initialize an object:

```
class Dev
  attr_accessor :name, :language
  def initialize(hash)
    self.name = hash[:name]
    self.language = hash[:language]
  end
end
matz = Dev.new(name: 'Matz', language: 'Ruby')
matz 
```

### Creating a `Hash`¶ ↑

You can create a `Hash` object explicitly with:

- A hash literal.

You can convert certain objects to Hashes with:

- Method `Hash`.

You can create a `Hash` by calling method `Hash.new`.

Create an empty `Hash`:

```
h = Hash.new
h 
h.class 
```

You can create a `Hash` by calling method `Hash.[]`.

Create an empty `Hash`:

```
h = Hash[]
h 
```

Create a `Hash` with initial entries:

```
h = Hash[foo: 0, bar: 1, baz: 2]
h 
```

You can create a `Hash` by using its literal form (curly braces).

Create an empty `Hash`:

```
h = {}
h 
```

Create a `Hash` with initial entries:

```
h = {foo: 0, bar: 1, baz: 2}
h 
```

### `Hash` Value Basics¶ ↑

The simplest way to retrieve a `Hash` value (instance method `[]`):

```
h = {foo: 0, bar: 1, baz: 2}
h[:foo] 
```

The simplest way to create or update a `Hash` value (instance method `[]=`):

```
h = {foo: 0, bar: 1, baz: 2}
h[:bat] = 3 
h 
h[:foo] = 4 
h 
```

The simplest way to delete a `Hash` entry (instance method `delete`):

```
h = {foo: 0, bar: 1, baz: 2}
h.delete(:bar) 
h 
```

### Entry Order¶ ↑

A `Hash` object presents its entries in the order of their creation. This is seen in:

- Iterative methods such as `each`, `each_key`, `each_pair`, `each_value`.
- Other order-sensitive methods such as `shift`, `keys`, `values`.
- The `String` returned by method `inspect`.

A new `Hash` has its initial ordering per the given entries:

```
h = Hash[foo: 0, bar: 1]
h 
```

New entries are added at the end:

```
h[:baz] = 2
h 
```

Updating a value does not affect the order:

```
h[:baz] = 3
h 
```

But re-creating a deleted entry can affect the order:

```
h.delete(:foo)
h[:foo] = 5
h 
```

### `Hash` Keys¶ ↑

#### `Hash` Key Equivalence¶ ↑

Two objects are treated as the same hash key when their `hash` value is identical and the two objects are `eql?` to each other.

#### Modifying an Active `Hash` Key¶ ↑

Modifying a `Hash` key while it is in use damages the hash’s index.

This `Hash` has keys that are Arrays:

```
a0 = [ :foo, :bar ]
a1 = [ :baz, :bat ]
h = {a0 => 0, a1 => 1}
h.include?(a0) 
h[a0] 
a0.hash 
```

Modifying array element `a0[0]` changes its hash value:

```
a0[0] = :bam
a0.hash 
```

And damages the `Hash` index:

```
h.include?(a0) 
h[a0] 
```

You can repair the hash index using method `rehash`:

```
h.rehash 
h.include?(a0) 
h[a0] 
```

A `String` key is always safe. That’s because an unfrozen `String` passed as a key will be replaced by a duplicated and frozen String:

```
s = 'foo'
s.frozen? 
h = {s => 0}
first_key = h.keys.first
first_key.frozen? 
```

#### User-Defined `Hash` Keys¶ ↑

To be usable as a `Hash` key, objects must implement the methods `hash` and `eql?`. Note: this requirement does not apply if the `Hash` uses `compare_by_identity` since comparison will then rely on the keys’ object id instead of `hash` and `eql?`.

`Object` defines basic implementation for `hash` and `eq?` that makes each object a distinct key. Typically, user-defined classes will want to override these methods to provide meaningful behavior, or for example inherit `Struct` that has useful definitions for these.

A typical implementation of `hash` is based on the object’s data while `eql?` is usually aliased to the overridden `==` method:

```
class Book
  attr_reader :author, :title

  def initialize(author, title)
    @author = author
    @title = title
  end

  def ==(other)
    self.class === other &&
      other.author == @author &&
      other.title == @title
  end

  alias eql? ==

  def hash
    [self.class, @author, @title].hash
  end
end

book1 = Book.new 'matz', 'Ruby in a Nutshell'
book2 = Book.new 'matz', 'Ruby in a Nutshell'

reviews = {}

reviews[book1] = 'Great reference!'
reviews[book2] = 'Nice and compact!'

reviews.length 
```

### Default Values¶ ↑

The methods `[]`, `values_at` and `dig` need to return the value associated to a certain key. When that key is not found, that value will be determined by its default proc (if any) or else its default (initially ‘nil`).

You can retrieve the default value with method `default`:

```
h = Hash.new
h.default 
```

You can set the default value by passing an argument to method `Hash.new` or with method `default=`

```
h = Hash.new(-1)
h.default 
h.default = 0
h.default 
```

This default value is returned for `[]`, `values_at` and `dig` when a key is not found:

```
counts = {foo: 42}
counts.default 
counts[:foo] = 42
counts[:bar] 
counts.default = 0
counts[:bar] 
counts.values_at(:foo, :bar, :baz) 
counts.dig(:bar) 
```

Note that the default value is used without being duplicated. It is not advised to set the default value to a mutable object:

```
synonyms = Hash.new([])
synonyms[:hello] 
synonyms[:hello] << :hi 
synonyms.default 
synonyms[:world] << :universe
synonyms[:world] 
synonyms.keys 
```

To use a mutable object as default, it is recommended to use a default proc

#### Default `Proc`¶ ↑

When the default proc for a `Hash` is set (i.e., not `nil`), the default value returned by method `[]` is determined by the default proc alone.

You can retrieve the default proc with method `default_proc`:

```
h = Hash.new
h.default_proc 
```

You can set the default proc by calling `Hash.new` with a block or calling the method `default_proc=`

```
h = Hash.new { |hash, key| "Default value for #{key}" }
h.default_proc.class 
h.default_proc = proc { |hash, key| "Default value for #{key.inspect}" }
h.default_proc.class 
```

When the default proc is set (i.e., not `nil`) and method `[]` is called with with a non-existent key, `[]` calls the default proc with both the `Hash` object itself and the missing key, then returns the proc’s return value:

```
h = Hash.new { |hash, key| "Default value for #{key}" }
h[:nosuch] 
```

Note that in the example above no entry for key `:nosuch` is created:

```
h.include?(:nosuch) 
```

However, the proc itself can add a new entry:

```
synonyms = Hash.new { |hash, key| hash[key] = [] }
synonyms.include?(:hello) 
synonyms[:hello] << :hi 
synonyms[:world] << :universe 
synonyms.keys 
```

Note that setting the default proc will clear the default value and vice versa.

Be aware that a default proc that modifies the hash is not thread-safe in the sense that multiple threads can call into the default proc concurrently for the same key.

### What’s Here¶ ↑

First, what’s elsewhere. Class `Hash`:

- Inherits from class Object.
- Includes module Enumerable, which provides dozens of additional methods.

Here, class `Hash` provides methods that are useful for:

- Creating a Hash
- Setting Hash State
- Querying
- Comparing
- Fetching
- Assigning
- Deleting
- Iterating
- Converting
- Transforming Keys and Values
- And more.…

Class `Hash` also includes methods from module `Enumerable`.

#### Methods for Creating a `Hash`¶ ↑

- `::[]`: Returns a new hash populated with given objects.
- `::new`: Returns a new empty hash.
- `::try_convert`: Returns a new hash created from a given object.

#### Methods for Setting `Hash` State¶ ↑

- `compare_by_identity`: Sets `self` to consider only identity in comparing keys.
- `default=`: Sets the default to a given value.
- `default_proc=`: Sets the default proc to a given proc.
- `rehash`: Rebuilds the hash table by recomputing the hash index for each key.

#### Methods for Querying¶ ↑

- `any?`: Returns whether any element satisfies a given criterion.
- `compare_by_identity?`: Returns whether the hash considers only identity when comparing keys.
- `default`: Returns the default value, or the default value for a given key.
- `default_proc`: Returns the default proc.
- `empty?`: Returns whether there are no entries.
- `eql?`: Returns whether a given object is equal to `self`.
- `hash`: Returns the integer hash code.
- `has_value?` (aliased as `value?`): Returns whether a given object is a value in `self`.
- `include?` (aliased as `has_key?`, `member?`, `key?`): Returns whether a given object is a key in `self`.
- `size` (aliased as `length`): Returns the count of entries.

#### Methods for Comparing¶ ↑

- #<: Returns whether `self` is a proper subset of a given object.
- #<=: Returns whether `self` is a subset of a given object.
- `==`: Returns whether a given object is equal to `self`.
- #>: Returns whether `self` is a proper superset of a given object
- #>=: Returns whether `self` is a superset of a given object.

#### Methods for Fetching¶ ↑

- `[]`: Returns the value associated with a given key.
- `assoc`: Returns a 2-element array containing a given key and its value.
- `dig`: Returns the object in nested objects that is specified by a given key and additional arguments.
- `fetch`: Returns the value for a given key.
- `fetch_values`: Returns array containing the values associated with given keys.
- `key`: Returns the key for the first-found entry with a given value.
- `keys`: Returns an array containing all keys in `self`.
- `rassoc`: Returns a 2-element array consisting of the key and value of the first-found entry having a given value.
- `values`: Returns an array containing all values in `self`/
- `values_at`: Returns an array containing values for given keys.

#### Methods for Assigning¶ ↑

- `[]=` (aliased as `store`): Associates a given key with a given value.
- `merge`: Returns the hash formed by merging each given hash into a copy of `self`.
- `update` (aliased as `merge!`): Merges each given hash into `self`.
- `replace` (aliased as `initialize_copy`): Replaces the entire contents of `self` with the contents of a given hash.

#### Methods for Deleting¶ ↑

These methods remove entries from `self`:

- `clear`: Removes all entries from `self`.
- `compact!`: Removes all `nil`-valued entries from `self`.
- `delete`: Removes the entry for a given key.
- `delete_if`: Removes entries selected by a given block.
- `select!` (aliased as `filter!`): Keep only those entries selected by a given block.
- `keep_if`: Keep only those entries selected by a given block.
- `reject!`: Removes entries selected by a given block.
- `shift`: Removes and returns the first entry.

These methods return a copy of `self` with some entries removed:

- `compact`: Returns a copy of `self` with all `nil`-valued entries removed.
- `except`: Returns a copy of `self` with entries removed for specified keys.
- `select` (aliased as `filter`): Returns a copy of `self` with only those entries selected by a given block.
- `reject`: Returns a copy of `self` with entries removed as specified by a given block.
- `slice`: Returns a hash containing the entries for given keys.

#### Methods for Iterating¶ ↑

- `each_pair` (aliased as `each`): Calls a given block with each key-value pair.
- `each_key`: Calls a given block with each key.
- `each_value`: Calls a given block with each value.

#### Methods for Converting¶ ↑

- `inspect` (aliased as `to_s`): Returns a new `String` containing the hash entries.
- `to_a`: Returns a new array of 2-element arrays; each nested array contains a key-value pair from `self`.
- `to_h`: Returns `self` if a `Hash`; if a subclass of `Hash`, returns a `Hash` containing the entries from `self`.
- `to_hash`: Returns `self`.
- `to_proc`: Returns a proc that maps a given key to its value.

#### Methods for Transforming Keys and Values¶ ↑

- `transform_keys`: Returns a copy of `self` with modified keys.
- `transform_keys!`: Modifies keys in `self`
- `transform_values`: Returns a copy of `self` with modified values.
- `transform_values!`: Modifies values in `self`.

#### Other Methods¶ ↑

- `flatten`: Returns an array that is a 1-dimensional flattening of `self`.
- `invert`: Returns a hash with the each key-value pair inverted.

### Public Class Methods

Hash[] → new_empty_hash

click to toggle source

Hash[hash] → new_hash

Hash[ [*2_element_arrays] ] → new_hash

Hash[*objects] → new_hash

Returns a new `Hash` object populated with the given objects, if any. See `Hash::new`.

With no argument, returns a new empty `Hash`.

When the single given argument is a `Hash`, returns a new `Hash` populated with the entries from the given `Hash`, excluding the default value or proc.

```
h = {foo: 0, bar: 1, baz: 2}
Hash[h] 
```

When the single given argument is an `Array` of 2-element Arrays, returns a new `Hash` object wherein each 2-element array forms a key-value entry:

```
Hash[ [ [:foo, 0], [:bar, 1] ] ] 
```

When the argument count is an even number; returns a new `Hash` object wherein each successive pair of arguments has become a key-value entry:

```
Hash[:foo, 0, :bar, 1] 
```

Raises an exception if the argument list does not conform to any of the above.

```
static VALUE
rb_hash_s_create(int argc, VALUE *argv, VALUE klass)
{
    VALUE hash, tmp;

    if (argc == 1) {
        tmp = rb_hash_s_try_convert(Qnil, argv[0]);
        if (!NIL_P(tmp)) {
            if (!RHASH_EMPTY_P(tmp)  && rb_hash_compare_by_id_p(tmp)) {
                /* hash_copy for non-empty hash will copy compare_by_identity
                   flag, but we don't want it copied. Work around by
                   converting hash to flattened array and using that. */
                tmp = rb_hash_to_a(tmp);
            }
            else {
                hash = hash_alloc(klass);
                if (!RHASH_EMPTY_P(tmp))
                    hash_copy(hash, tmp);
                return hash;
            }
        }
        else {
            tmp = rb_check_array_type(argv[0]);
        }

        if (!NIL_P(tmp)) {
            long i;

            hash = hash_alloc(klass);
            for (i = 0; i < RARRAY_LEN(tmp); ++i) {
                VALUE e = RARRAY_AREF(tmp, i);
                VALUE v = rb_check_array_type(e);
                VALUE key, val = Qnil;

                if (NIL_P(v)) {
                    rb_raise(rb_eArgError, "wrong element type %s at %ld (expected array)",
                             rb_builtin_class_name(e), i);
                }
                switch (RARRAY_LEN(v)) {
                  default:
                    rb_raise(rb_eArgError, "invalid number of elements (%ld for 1..2)",
                             RARRAY_LEN(v));
                  case 2:
                    val = RARRAY_AREF(v, 1);
                  case 1:
                    key = RARRAY_AREF(v, 0);
                    rb_hash_aset(hash, key, val);
                }
            }
            return hash;
        }
    }
    if (argc % 2 != 0) {
        rb_raise(rb_eArgError, "odd number of arguments for Hash");
    }

    hash = hash_alloc(klass);
    rb_hash_bulk_insert(argc, argv, hash);
    hash_verify(hash);
    return hash;
}
```

new(default_value = nil) → new_hash

click to toggle source

new(default_value = nil, capacity: size) → new_hash

new {|hash, key| ... } → new_hash

new(capacity: size) {|hash, key| ... } → new_hash

Returns a new empty `Hash` object.

The initial default value and initial default proc for the new hash depend on which form above was used. See Default Values.

If neither an argument nor a block is given, initializes both the default value and the default proc to `nil`:

```
h = Hash.new
h.default 
h.default_proc 
```

If argument `default_value` is given but no block is given, initializes the default value to the given `default_value` and the default proc to `nil`:

```
h = Hash.new(false)
h.default 
h.default_proc 
```

If a block is given but no `default_value`, stores the block as the default proc and sets the default value to `nil`:

```
h = Hash.new {|hash, key| "Default value for #{key}" }
h.default 
h.default_proc.class 
h[:nosuch] 
```

If both a block and a `default_value` are given, raises an `ArgumentError`

If the optional keyword argument `capacity` is given, the hash will be allocated with enough capacity to accommodate this many keys without having to be resized.

```
def initialize(ifnone = (ifnone_unset = true), capacity: 0, &block)
  Primitive.rb_hash_init(capacity, ifnone_unset, ifnone, block)
end
```

ruby2_keywords_hash(hash) → hash

click to toggle source

Duplicates a given hash and adds a ruby2_keywords flag. This method is not for casual use; debugging, researching, and some truly necessary cases like deserialization of arguments.

```
h = {k: 1}
h = Hash.ruby2_keywords_hash(h)
def foo(k: 42)
  k
end
foo(*[h]) 
```

```
static VALUE
rb_hash_s_ruby2_keywords_hash(VALUE dummy, VALUE hash)
{
    Check_Type(hash, T_HASH);
    VALUE tmp = rb_hash_dup(hash);
    if (RHASH_EMPTY_P(hash) && rb_hash_compare_by_id_p(hash)) {
        rb_hash_compare_by_id(tmp);
    }
    RHASH(tmp)->basic.flags |= RHASH_PASS_AS_KEYWORDS;
    return tmp;
}
```

ruby2_keywords_hash?(hash) → true or false

click to toggle source

Checks if a given hash is flagged by `Module#ruby2_keywords` (or `Proc#ruby2_keywords`). This method is not for casual use; debugging, researching, and some truly necessary cases like serialization of arguments.

```
ruby2_keywords def foo(*args)
  Hash.ruby2_keywords_hash?(args.last)
end
foo(k: 1)   
foo({k: 1}) 
```

```
static VALUE
rb_hash_s_ruby2_keywords_hash_p(VALUE dummy, VALUE hash)
{
    Check_Type(hash, T_HASH);
    return RBOOL(RHASH(hash)->basic.flags & RHASH_PASS_AS_KEYWORDS);
}
```

try_convert(obj) → obj, new_hash, or nil

click to toggle source

If `obj` is a `Hash` object, returns `obj`.

Otherwise if `obj` responds to `:to_hash`, calls `obj.to_hash` and returns the result.

Returns `nil` if `obj` does not respond to `:to_hash`

Raises an exception unless `obj.to_hash` returns a `Hash` object.

```
static VALUE
rb_hash_s_try_convert(VALUE dummy, VALUE hash)
{
    return rb_check_hash_type(hash);
}
```

### Public Instance Methods

hash < other_hash → true or false

click to toggle source

Returns `true` if `hash` is a proper subset of `other_hash`, `false` otherwise:

```
h1 = {foo: 0, bar: 1}
h2 = {foo: 0, bar: 1, baz: 2}
h1 < h2 
h2 < h1 
h1 < h1 
```

```
static VALUE
rb_hash_lt(VALUE hash, VALUE other)
{
    other = to_hash(other);
    if (RHASH_SIZE(hash) >= RHASH_SIZE(other)) return Qfalse;
    return hash_le(hash, other);
}
```

hash <= other_hash → true or false

click to toggle source

Returns `true` if `hash` is a subset of `other_hash`, `false` otherwise:

```
h1 = {foo: 0, bar: 1}
h2 = {foo: 0, bar: 1, baz: 2}
h1 <= h2 
h2 <= h1 
h1 <= h1 
```

```
static VALUE
rb_hash_le(VALUE hash, VALUE other)
{
    other = to_hash(other);
    if (RHASH_SIZE(hash) > RHASH_SIZE(other)) return Qfalse;
    return hash_le(hash, other);
}
```

hash == object → true or false

click to toggle source

Returns `true` if all of the following are true:

- `object` is a `Hash` object.
- `hash` and `object` have the same keys (regardless of order).
- For each key `key`, `hash[key] == object[key]`.

Otherwise, returns `false`.

Equal:

```
h1 = {foo: 0, bar: 1, baz: 2}
h2 = {foo: 0, bar: 1, baz: 2}
h1 == h2 
h3 = {baz: 2, bar: 1, foo: 0}
h1 == h3 
```

```
static VALUE
rb_hash_equal(VALUE hash1, VALUE hash2)
{
    return hash_equal(hash1, hash2, FALSE);
}
```

hash > other_hash → true or false

click to toggle source

Returns `true` if `hash` is a proper superset of `other_hash`, `false` otherwise:

```
h1 = {foo: 0, bar: 1, baz: 2}
h2 = {foo: 0, bar: 1}
h1 > h2 
h2 > h1 
h1 > h1 
```

```
static VALUE
rb_hash_gt(VALUE hash, VALUE other)
{
    other = to_hash(other);
    if (RHASH_SIZE(hash) <= RHASH_SIZE(other)) return Qfalse;
    return hash_le(other, hash);
}
```

hash >= other_hash → true or false

click to toggle source

Returns `true` if `hash` is a superset of `other_hash`, `false` otherwise:

```
h1 = {foo: 0, bar: 1, baz: 2}
h2 = {foo: 0, bar: 1}
h1 >= h2 
h2 >= h1 
h1 >= h1 
```

```
static VALUE
rb_hash_ge(VALUE hash, VALUE other)
{
    other = to_hash(other);
    if (RHASH_SIZE(hash) < RHASH_SIZE(other)) return Qfalse;
    return hash_le(other, hash);
}
```

hash[key] → value

click to toggle source

Returns the value associated with the given `key`, if found:

```
h = {foo: 0, bar: 1, baz: 2}
h[:foo] 
```

If `key` is not found, returns a default value (see Default Values):

```
h = {foo: 0, bar: 1, baz: 2}
h[:nosuch] 
```

```
VALUE
rb_hash_aref(VALUE hash, VALUE key)
{
    st_data_t val;

    if (hash_stlike_lookup(hash, key, &val)) {
        return (VALUE)val;
    }
    else {
        return rb_hash_default_value(hash, key);
    }
}
```

hash[key] = value → value

click to toggle source

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

```
VALUE
rb_hash_aset(VALUE hash, VALUE key, VALUE val)
{
    bool iter_p = hash_iterating_p(hash);

    rb_hash_modify(hash);

    if (!RHASH_STRING_KEY_P(hash, key)) {
        RHASH_UPDATE_ITER(hash, iter_p, key, hash_aset, val);
    }
    else {
        RHASH_UPDATE_ITER(hash, iter_p, key, hash_aset_str, val);
    }
    return val;
}
```

Also aliased as:

store

any? → true or false

click to toggle source

any?(object) → true or false

any? {|key, value| ... } → true or false

Returns `true` if any element satisfies a given criterion; `false` otherwise.

If `self` has no element, returns `false` and argument or block are not used.

With no argument and no block, returns `true` if `self` is non-empty; `false` if empty.

With argument `object` and no block, returns `true` if for any key `key` `h.assoc(key) == object`:

```
h = {foo: 0, bar: 1, baz: 2}
h.any?([:bar, 1]) 
h.any?([:bar, 0]) 
h.any?([:baz, 1]) 
```

With no argument and a block, calls the block with each key-value pair; returns `true` if the block returns any truthy value, `false` otherwise:

```
h = {foo: 0, bar: 1, baz: 2}
h.any? {|key, value| value < 3 } 
h.any? {|key, value| value > 3 } 
```

Related: `Enumerable#any?`

```
static VALUE
rb_hash_any_p(int argc, VALUE *argv, VALUE hash)
{
    VALUE args[2];
    args[0] = Qfalse;

    rb_check_arity(argc, 0, 1);
    if (RHASH_EMPTY_P(hash)) return Qfalse;
    if (argc) {
        if (rb_block_given_p()) {
            rb_warn("given block not used");
        }
        args[1] = argv[0];

        rb_hash_foreach(hash, any_p_i_pattern, (VALUE)args);
    }
    else {
        if (!rb_block_given_p()) {
            /* yields pairs, never false */
            return Qtrue;
        }
        if (rb_block_pair_yield_optimizable())
            rb_hash_foreach(hash, any_p_i_fast, (VALUE)args);
        else
            rb_hash_foreach(hash, any_p_i, (VALUE)args);
    }
    return args[0];
}
```

assoc(key) → new_array or nil

click to toggle source

If the given `key` is found, returns a 2-element `Array` containing that key and its value:

```
h = {foo: 0, bar: 1, baz: 2}
h.assoc(:bar) 
```

Returns `nil` if key `key` is not found.

```
static VALUE
rb_hash_assoc(VALUE hash, VALUE key)
{
    VALUE args[2];

    if (RHASH_EMPTY_P(hash)) return Qnil;

    if (RHASH_ST_TABLE_P(hash) && !RHASH_IDENTHASH_P(hash)) {
        VALUE value = Qundef;
        st_table assoctable = *RHASH_ST_TABLE(hash);
        assoctable.type = &(struct st_hash_type){
            .compare = assoc_cmp,
            .hash = assoctable.type->hash,
        };
        VALUE arg = (VALUE)&(struct assoc_arg){
            .tbl = &assoctable,
            .key = (st_data_t)key,
        };

        if (RB_OBJ_FROZEN(hash)) {
            value = assoc_lookup(arg);
        }
        else {
            hash_iter_lev_inc(hash);
            value = rb_ensure(assoc_lookup, arg, hash_foreach_ensure, hash);
        }
        hash_verify(hash);
        if (!UNDEF_P(value)) return rb_assoc_new(key, value);
    }

    args[0] = key;
    args[1] = Qnil;
    rb_hash_foreach(hash, assoc_i, (VALUE)args);
    return args[1];
}
```

clear → self

click to toggle source

Removes all hash entries; returns `self`.

```
VALUE
rb_hash_clear(VALUE hash)
{
    rb_hash_modify_check(hash);

    if (hash_iterating_p(hash)) {
        rb_hash_foreach(hash, clear_i, 0);
    }
    else if (RHASH_AR_TABLE_P(hash)) {
        ar_clear(hash);
    }
    else {
        st_clear(RHASH_ST_TABLE(hash));
        compact_after_delete(hash);
    }

    return hash;
}
```

compact → new_hash

click to toggle source

Returns a copy of `self` with all `nil`-valued entries removed:

```
h = {foo: 0, bar: nil, baz: 2, bat: nil}
h1 = h.compact
h1 
```

```
static VALUE
rb_hash_compact(VALUE hash)
{
    VALUE result = rb_hash_dup(hash);
    if (!RHASH_EMPTY_P(hash)) {
        rb_hash_foreach(result, delete_if_nil, result);
        compact_after_delete(result);
    }
    else if (rb_hash_compare_by_id_p(hash)) {
        result = rb_hash_compare_by_id(result);
    }
    return result;
}
```

compact! → self or nil

click to toggle source

Returns `self` with all its `nil`-valued entries removed (in place):

```
h = {foo: 0, bar: nil, baz: 2, bat: nil}
h.compact! 
```

Returns `nil` if no entries were removed.

```
static VALUE
rb_hash_compact_bang(VALUE hash)
{
    st_index_t n;
    rb_hash_modify_check(hash);
    n = RHASH_SIZE(hash);
    if (n) {
        rb_hash_foreach(hash, delete_if_nil, hash);
        if (n != RHASH_SIZE(hash))
            return hash;
    }
    return Qnil;
}
```

compare_by_identity → self

click to toggle source

Sets `self` to consider only identity in comparing keys; two keys are considered the same only if they are the same object; returns `self`.

By default, these two object are considered to be the same key, so `s1` will overwrite `s0`:

```
s0 = 'x'
s1 = 'x'
h = {}
h.compare_by_identity? 
h[s0] = 0
h[s1] = 1
h 
```

After calling #compare_by_identity, the keys are considered to be different, and therefore do not overwrite each other:

```
h = {}
h.compare_by_identity 
h.compare_by_identity? 
h[s0] = 0
h[s1] = 1
h 
```

```
VALUE
rb_hash_compare_by_id(VALUE hash)
{
    VALUE tmp;
    st_table *identtable;

    if (rb_hash_compare_by_id_p(hash)) return hash;

    rb_hash_modify_check(hash);
    if (hash_iterating_p(hash)) {
        rb_raise(rb_eRuntimeError, "compare_by_identity during iteration");
    }

    if (RHASH_TABLE_EMPTY_P(hash)) {
        // Fast path: There's nothing to rehash, so we don't need a `tmp` table.
        // We're most likely an AR table, so this will need an allocation.
        ar_force_convert_table(hash, __FILE__, __LINE__);
        HASH_ASSERT(RHASH_ST_TABLE_P(hash));

        RHASH_ST_TABLE(hash)->type = &identhash;
    }
    else {
        // Slow path: Need to rehash the members of `self` into a new
        // `tmp` table using the new `identhash` compare/hash functions.
        tmp = hash_alloc(0);
        hash_st_table_init(tmp, &identhash, RHASH_SIZE(hash));
        identtable = RHASH_ST_TABLE(tmp);

        rb_hash_foreach(hash, rb_hash_rehash_i, (VALUE)tmp);
        rb_hash_free(hash);

        // We know for sure `identtable` is an st table,
        // so we can skip `ar_force_convert_table` here.
        RHASH_ST_TABLE_SET(hash, identtable);
        RHASH_ST_CLEAR(tmp);
    }

    return hash;
}
```

compare_by_identity? → true or false

click to toggle source

Returns `true` if `compare_by_identity` has been called, `false` otherwise.

```
VALUE
rb_hash_compare_by_id_p(VALUE hash)
{
    return RBOOL(RHASH_IDENTHASH_P(hash));
}
```

default → object

click to toggle source

default(key) → object

Returns the default value for the given `key`. The returned value will be determined either by the default proc or by the default value. See Default Values.

With no argument, returns the current default value:

```
h = {}
h.default 
```

If `key` is given, returns the default value for `key`, regardless of whether that key exists:

```
h = Hash.new { |hash, key| hash[key] = "No key #{key}"}
h[:foo] = "Hello"
h.default(:foo) 
```

```
static VALUE
rb_hash_default(int argc, VALUE *argv, VALUE hash)
{
    VALUE ifnone;

    rb_check_arity(argc, 0, 1);
    ifnone = RHASH_IFNONE(hash);
    if (FL_TEST(hash, RHASH_PROC_DEFAULT)) {
        if (argc == 0) return Qnil;
        return call_default_proc(ifnone, hash, argv[0]);
    }
    return ifnone;
}
```

default = value → object

click to toggle source

Sets the default value to `value`; returns `value`:

```
h = {}
h.default 
h.default = false 
h.default 
```

See Default Values.

```
static VALUE
rb_hash_set_default(VALUE hash, VALUE ifnone)
{
    rb_hash_modify_check(hash);
    SET_DEFAULT(hash, ifnone);
    return ifnone;
}
```

default_proc → proc or nil

click to toggle source

Returns the default proc for `self` (see Default Values):

```
h = {}
h.default_proc 
h.default_proc = proc {|hash, key| "Default value for #{key}" }
h.default_proc.class 
```

```
static VALUE
rb_hash_default_proc(VALUE hash)
{
    if (FL_TEST(hash, RHASH_PROC_DEFAULT)) {
        return RHASH_IFNONE(hash);
    }
    return Qnil;
}
```

default_proc = proc → proc

click to toggle source

Sets the default proc for `self` to `proc` (see Default Values):

```
h = {}
h.default_proc 
h.default_proc = proc { |hash, key| "Default value for #{key}" }
h.default_proc.class 
h.default_proc = nil
h.default_proc 
```

```
VALUE
rb_hash_set_default_proc(VALUE hash, VALUE proc)
{
    VALUE b;

    rb_hash_modify_check(hash);
    if (NIL_P(proc)) {
        SET_DEFAULT(hash, proc);
        return proc;
    }
    b = rb_check_convert_type_with_id(proc, T_DATA, "Proc", idTo_proc);
    if (NIL_P(b) || !rb_obj_is_proc(b)) {
        rb_raise(rb_eTypeError,
                 "wrong default_proc type %s (expected Proc)",
                 rb_obj_classname(proc));
    }
    proc = b;
    SET_PROC_DEFAULT(hash, proc);
    return proc;
}
```

delete(key) → value or nil

click to toggle source

delete(key) {|key| ... } → object

Deletes the entry for the given `key` and returns its associated value.

If no block is given and `key` is found, deletes the entry and returns the associated value:

```
h = {foo: 0, bar: 1, baz: 2}
h.delete(:bar) 
h 
```

If no block given and `key` is not found, returns `nil`.

If a block is given and `key` is found, ignores the block, deletes the entry, and returns the associated value:

```
h = {foo: 0, bar: 1, baz: 2}
h.delete(:baz) { |key| raise 'Will never happen'} 
h 
```

If a block is given and `key` is not found, calls the block and returns the block’s return value:

```
h = {foo: 0, bar: 1, baz: 2}
h.delete(:nosuch) { |key| "Key #{key} not found" } 
h 
```

```
static VALUE
rb_hash_delete_m(VALUE hash, VALUE key)
{
    VALUE val;

    rb_hash_modify_check(hash);
    val = rb_hash_delete_entry(hash, key);

    if (!UNDEF_P(val)) {
        compact_after_delete(hash);
        return val;
    }
    else {
        if (rb_block_given_p()) {
            return rb_yield(key);
        }
        else {
            return Qnil;
        }
    }
}
```

delete_if {|key, value| ... } → self

click to toggle source

delete_if → new_enumerator

If a block given, calls the block with each key-value pair; deletes each entry for which the block returns a truthy value; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.delete_if {|key, value| value > 0 } 
```

If no block given, returns a new Enumerator:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.delete_if 
e.each { |key, value| value > 0 } 
```

```
VALUE
rb_hash_delete_if(VALUE hash)
{
    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_modify_check(hash);
    if (!RHASH_TABLE_EMPTY_P(hash)) {
        rb_hash_foreach(hash, delete_if_i, hash);
        compact_after_delete(hash);
    }
    return hash;
}
```

dig(key, *identifiers) → object

click to toggle source

Finds and returns the object in nested objects that is specified by `key` and `identifiers`. The nested objects may be instances of various classes. See Dig Methods.

Nested Hashes:

```
h = {foo: {bar: {baz: 2}}}
h.dig(:foo) 
h.dig(:foo, :bar) 
h.dig(:foo, :bar, :baz) 
h.dig(:foo, :bar, :BAZ) 
```

Nested Hashes and Arrays:

```
h = {foo: {bar: [:a, :b, :c]}}
h.dig(:foo, :bar, 2) 
```

This method will use the default values for keys that are not present:

```
h = {foo: {bar: [:a, :b, :c]}}
h.dig(:hello) 
h.default_proc = -> (hash, _key) { hash }
h.dig(:hello, :world) 
h.dig(:hello, :world, :foo, :bar, 2) 
```

```
static VALUE
rb_hash_dig(int argc, VALUE *argv, VALUE self)
{
    rb_check_arity(argc, 1, UNLIMITED_ARGUMENTS);
    self = rb_hash_aref(self, *argv);
    if (!--argc) return self;
    ++argv;
    return rb_obj_dig(argc, argv, self, Qnil);
}
```

each {|key, value| ... } → self

each → new_enumerator

Calls the given block with each key-value pair; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.each_pair {|key, value| puts "#{key}: #{value}"} 
```

Output:

```
foo: 0
bar: 1
baz: 2
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.each_pair 
h1 = e.each {|key, value| puts "#{key}: #{value}"}
h1 
```

Output:

```
foo: 0
bar: 1
baz: 2
```

Alias for:

each_pair

each_key {|key| ... } → self

click to toggle source

each_key → new_enumerator

Calls the given block with each key; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.each_key {|key| puts key }  
```

Output:

```
foo
bar
baz
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.each_key 
h1 = e.each {|key| puts key }
h1 
```

Output:

```
foo
bar
baz
```

```
static VALUE
rb_hash_each_key(VALUE hash)
{
    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_foreach(hash, each_key_i, 0);
    return hash;
}
```

each_pair

-> new_enumerator

click to toggle source

Calls the given block with each key-value pair; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.each_pair {|key, value| puts "#{key}: #{value}"} 
```

Output:

```
foo: 0
bar: 1
baz: 2
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.each_pair 
h1 = e.each {|key, value| puts "#{key}: #{value}"}
h1 
```

Output:

```
foo: 0
bar: 1
baz: 2
```

```
static VALUE
rb_hash_each_pair(VALUE hash)
{
    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    if (rb_block_pair_yield_optimizable())
        rb_hash_foreach(hash, each_pair_i_fast, 0);
    else
        rb_hash_foreach(hash, each_pair_i, 0);
    return hash;
}
```

Also aliased as:

each

each_value {|value| ... } → self

click to toggle source

each_value → new_enumerator

Calls the given block with each value; returns `self`:

```
h = {foo: 0, bar: 1, baz: 2}
h.each_value {|value| puts value } 
```

Output:

```
0
1
2
```

Returns a new `Enumerator` if no block given:

```
h = {foo: 0, bar: 1, baz: 2}
e = h.each_value 
h1 = e.each {|value| puts value }
h1 
```

Output:

```
0
1
2
```

```
static VALUE
rb_hash_each_value(VALUE hash)
{
    RETURN_SIZED_ENUMERATOR(hash, 0, 0, hash_enum_size);
    rb_hash_foreach(hash, each_value_i, 0);
    return hash;
}
```

empty? → true or false

click to toggle source

Returns `true` if there are no hash entries, `false` otherwise:

```
{}.empty? 
{foo: 0, bar: 1, baz: 2}.empty? 
```

```
VALUE
rb_hash_empty_p(VALUE hash)
{
    return RBOOL(RHASH_EMPTY_P(hash));
}
```

eql?(object) → true or false

click to toggle source

Returns `true` if all of the following are true:

- `object` is a `Hash` object.
- `hash` and `object` have the same keys (regardless of order).
- For each key `key`, `h[key].eql?(object[key])`.

Otherwise, returns `false`.

```
h1 = {foo: 0, bar: 1, baz: 2}
h2 = {foo: 0, bar: 1, baz: 2}
h1.eql? h2 
h3 = {baz: 2, bar: 1, foo: 0}
h1.eql? h3 
```

```
static VALUE
rb_hash_eql(VALUE hash1, VALUE hash2)
{
    return hash_equal(hash1, hash2, TRUE);
}
```

except(*keys) → a_hash
