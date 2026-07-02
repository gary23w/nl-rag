---
title: "class String (part 2/4)"
source: https://ruby-doc.org/core/String.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/4
---

## What’s Here¶ ↑

First, what’s elsewhere. Class `String`:

- Inherits from the Object class.
- Includes the Comparable module.

Here, class `String` provides methods that are useful for:

- Creating a String
- Frozen/Unfrozen Strings
- Querying
- Comparing
- Modifying a String
- Converting to New String
- Converting to Non-String
- Iterating

### Methods for Creating a `String`¶ ↑

- `::new`: Returns a new string.
- `::try_convert`: Returns a new string created from a given object.

### Methods for a Frozen/Unfrozen `String`¶ ↑

- `+@`: Returns a string that is not frozen: `self` if not frozen; `self.dup` otherwise.
- `-@` (aliased as `dedup`): Returns a string that is frozen: `self` if already frozen; `self.freeze` otherwise.
- `freeze`: Freezes `self` if not already frozen; returns `self`.

### Methods for Querying¶ ↑

*Counts*

- `length` (aliased as `size`): Returns the count of characters (not bytes).
- `empty?`: Returns `true` if `self.length` is zero; `false` otherwise.
- `bytesize`: Returns the count of bytes.
- `count`: Returns the count of substrings matching given strings.

*Substrings*

- #=~: Returns the index of the first substring that matches a given `Regexp` or other object; returns `nil` if no match is found.
- `index`: Returns the index of the *first* occurrence of a given substring; returns `nil` if none found.
- `rindex`: Returns the index of the *last* occurrence of a given substring; returns `nil` if none found.
- `include?`: Returns `true` if the string contains a given substring; `false` otherwise.
- `match`: Returns a `MatchData` object if the string matches a given `Regexp`; `nil` otherwise.
- `match?`: Returns `true` if the string matches a given `Regexp`; `false` otherwise.
- `start_with?`: Returns `true` if the string begins with any of the given substrings.
- `end_with?`: Returns `true` if the string ends with any of the given substrings.

*Encodings*

- `encoding`: Returns the `Encoding` object that represents the encoding of the string.
- `unicode_normalized?`: Returns `true` if the string is in Unicode normalized form; `false` otherwise.
- `valid_encoding?`: Returns `true` if the string contains only characters that are valid for its encoding.
- `ascii_only?`: Returns `true` if the string has only ASCII characters; `false` otherwise.

*Other*

- `sum`: Returns a basic checksum for the string: the sum of each byte.
- `hash`: Returns the integer hash code.

### Methods for Comparing¶ ↑

- `==` (aliased as `===`): Returns `true` if a given other string has the same content as `self`.
- `eql?`: Returns `true` if the content is the same as the given other string.
- #<=>: Returns -1, 0, or 1 as a given other string is smaller than, equal to, or larger than `self`.
- `casecmp`: Ignoring case, returns -1, 0, or 1 as a given other string is smaller than, equal to, or larger than `self`.
- `casecmp?`: Returns `true` if the string is equal to a given string after Unicode case folding; `false` otherwise.

### Methods for Modifying a `String`¶ ↑

Each of these methods modifies `self`.

*Insertion*

- `insert`: Returns `self` with a given string inserted at a specified offset.
- `<<`: Returns `self` concatenated with a given string or integer.
- `append_as_bytes`: Returns `self` concatenated with strings without performing any encoding validation or conversion.

*Substitution*

- `sub!`: Replaces the first substring that matches a given pattern with a given replacement string; returns `self` if any changes, `nil` otherwise.
- `gsub!`: Replaces each substring that matches a given pattern with a given replacement string; returns `self` if any changes, `nil` otherwise.
- `succ!` (aliased as `next!`): Returns `self` modified to become its own successor.
- `initialize_copy` (aliased as `replace`): Returns `self` with its entire content replaced by a given string.
- `reverse!`: Returns `self` with its characters in reverse order.
- `setbyte`: Sets the byte at a given integer offset to a given value; returns the argument.
- `tr!`: Replaces specified characters in `self` with specified replacement characters; returns `self` if any changes, `nil` otherwise.
- `tr_s!`: Replaces specified characters in `self` with specified replacement characters, removing duplicates from the substrings that were modified; returns `self` if any changes, `nil` otherwise.

*Casing*

- `capitalize!`: Upcases the initial character and downcases all others; returns `self` if any changes, `nil` otherwise.
- `downcase!`: Downcases all characters; returns `self` if any changes, `nil` otherwise.
- `upcase!`: Upcases all characters; returns `self` if any changes, `nil` otherwise.
- `swapcase!`: Upcases each downcase character and downcases each upcase character; returns `self` if any changes, `nil` otherwise.

*Encoding*

- `encode!`: Returns `self` with all characters transcoded from one encoding to another.
- `unicode_normalize!`: Unicode-normalizes `self`; returns `self`.
- `scrub!`: Replaces each invalid byte with a given character; returns `self`.
- `force_encoding`: Changes the encoding to a given encoding; returns `self`.

*Deletion*

- `clear`: Removes all content, so that `self` is empty; returns `self`.
- `slice!`, `[]=`: Removes a substring determined by a given index, start/length, range, regexp, or substring.
- `squeeze!`: Removes contiguous duplicate characters; returns `self`.
- `delete!`: Removes characters as determined by the intersection of substring arguments.
- `lstrip!`: Removes leading whitespace; returns `self` if any changes, `nil` otherwise.
- `rstrip!`: Removes trailing whitespace; returns `self` if any changes, `nil` otherwise.
- `strip!`: Removes leading and trailing whitespace; returns `self` if any changes, `nil` otherwise.
- `chomp!`: Removes the trailing record separator, if found; returns `self` if any changes, `nil` otherwise.
- `chop!`: Removes trailing newline characters if found; otherwise removes the last character; returns `self` if any changes, `nil` otherwise.

### Methods for Converting to New `String`¶ ↑

Each of these methods returns a new `String` based on `self`, often just a modified copy of `self`.

*Extension*

- `*`: Returns the concatenation of multiple copies of `self`.
- `+`: Returns the concatenation of `self` and a given other string.
- `center`: Returns a copy of `self` centered between pad substrings.
- `concat`: Returns the concatenation of `self` with given other strings.
- `prepend`: Returns the concatenation of a given other string with `self`.
- `ljust`: Returns a copy of `self` of a given length, right-padded with a given other string.
- `rjust`: Returns a copy of `self` of a given length, left-padded with a given other string.

*Encoding*

- `b`: Returns a copy of `self` with ASCII-8BIT encoding.
- `scrub`: Returns a copy of `self` with each invalid byte replaced with a given character.
- `unicode_normalize`: Returns a copy of `self` with each character Unicode-normalized.
- `encode`: Returns a copy of `self` with all characters transcoded from one encoding to another.

*Substitution*

- `dump`: Returns a copy of `self` with all non-printing characters replaced by xHH notation and all special characters escaped.
- `undump`: Returns a copy of `self` with all `\xNN` notations replaced by `\uNNNN` notations and all escaped characters unescaped.
- `sub`: Returns a copy of `self` with the first substring matching a given pattern replaced with a given replacement string.
- `gsub`: Returns a copy of `self` with each substring that matches a given pattern replaced with a given replacement string.
- `succ` (aliased as `next`): Returns the string that is the successor to `self`.
- `reverse`: Returns a copy of `self` with its characters in reverse order.
- `tr`: Returns a copy of `self` with specified characters replaced with specified replacement characters.
- `tr_s`: Returns a copy of `self` with specified characters replaced with specified replacement characters, removing duplicates from the substrings that were modified.
- `%`: Returns the string resulting from formatting a given object into `self`.

*Casing*

- `capitalize`: Returns a copy of `self` with the first character upcased and all other characters downcased.
- `downcase`: Returns a copy of `self` with all characters downcased.
- `upcase`: Returns a copy of `self` with all characters upcased.
- `swapcase`: Returns a copy of `self` with all upcase characters downcased and all downcase characters upcased.

*Deletion*

- `delete`: Returns a copy of `self` with characters removed.
- `delete_prefix`: Returns a copy of `self` with a given prefix removed.
- `delete_suffix`: Returns a copy of `self` with a given suffix removed.
- `lstrip`: Returns a copy of `self` with leading whitespace removed.
- `rstrip`: Returns a copy of `self` with trailing whitespace removed.
- `strip`: Returns a copy of `self` with leading and trailing whitespace removed.
- `chomp`: Returns a copy of `self` with a trailing record separator removed, if found.
- `chop`: Returns a copy of `self` with trailing newline characters or the last character removed.
- `squeeze`: Returns a copy of `self` with contiguous duplicate characters removed.
- `[]` (aliased as `slice`): Returns a substring determined by a given index, start/length, range, regexp, or string.
- `byteslice`: Returns a substring determined by a given index, start/length, or range.
- `chr`: Returns the first character.

*Duplication*

- `to_s` (aliased as `to_str`): If `self` is a subclass of `String`, returns `self` copied into a `String`; otherwise, returns `self`.

### Methods for Converting to Non-`String`¶ ↑

Each of these methods converts the contents of `self` to a non-`String`.

*Characters, Bytes, and Clusters*

- `bytes`: Returns an array of the bytes in `self`.
- `chars`: Returns an array of the characters in `self`.
- `codepoints`: Returns an array of the integer ordinals in `self`.
- `getbyte`: Returns the integer byte at the given index in `self`.
- `grapheme_clusters`: Returns an array of the grapheme clusters in `self`.

*Splitting*

- `lines`: Returns an array of the lines in `self`, as determined by a given record separator.
- `partition`: Returns a 3-element array determined by the first substring that matches a given substring or regexp.
- `rpartition`: Returns a 3-element array determined by the last substring that matches a given substring or regexp.
- `split`: Returns an array of substrings determined by a given delimiter – regexp or string – or, if a block is given, passes those substrings to the block.

*Matching*

- `scan`: Returns an array of substrings matching a given regexp or string, or, if a block is given, passes each matching substring to the block.
- `unpack`: Returns an array of substrings extracted from `self` according to a given format.
- `unpack1`: Returns the first substring extracted from `self` according to a given format.

*Numerics*

- `hex`: Returns the integer value of the leading characters, interpreted as hexadecimal digits.
- `oct`: Returns the integer value of the leading characters, interpreted as octal digits.
- `ord`: Returns the integer ordinal of the first character in `self`.
- `to_i`: Returns the integer value of leading characters, interpreted as an integer.
- `to_f`: Returns the floating-point value of leading characters, interpreted as a floating-point number.

*Strings and Symbols*

- `inspect`: Returns a copy of `self`, enclosed in double quotes, with special characters escaped.
- `intern` (aliased as `to_sym`): Returns the symbol corresponding to `self`.

### Methods for Iterating¶ ↑

- `each_byte`: Calls the given block with each successive byte in `self`.
- `each_char`: Calls the given block with each successive character in `self`.
- `each_codepoint`: Calls the given block with each successive integer codepoint in `self`.
- `each_grapheme_cluster`: Calls the given block with each successive grapheme cluster in `self`.
- `each_line`: Calls the given block with each successive line in `self`, as determined by a given record separator.
- `upto`: Calls the given block with each string value returned by successive calls to `succ`.

### Public Class Methods

new(string = '', **opts) → new_string

click to toggle source

Returns a new String that is a copy of `string`.

With no arguments, returns the empty string with the `Encoding` `ASCII-8BIT`:

```
s = String.new
s 
s.encoding 
```

With optional argument `string` and no keyword arguments, returns a copy of `string` with the same encoding:

```
String.new('foo')               
String.new('тест')              
String.new('こんにちは')          
```

(Unlike String.new, a string literal like `''` or a here document literal always has script encoding.)

With optional keyword argument `encoding`, returns a copy of `string` with the specified encoding; the `encoding` may be an `Encoding` object, an encoding name, or an encoding name alias:

```
String.new('foo', encoding: Encoding::US_ASCII).encoding 
String.new('foo', encoding: 'US-ASCII').encoding         
String.new('foo', encoding: 'ASCII').encoding            
```

The given encoding need not be valid for the string’s content, and that validity is not checked:

```
s = String.new('こんにちは', encoding: 'ascii')
s.valid_encoding? 
```

But the given `encoding` itself is checked:

```
String.new('foo', encoding: 'bar') 
```

With optional keyword argument `capacity`, returns a copy of `string` (or an empty string, if `string` is not given); the given `capacity` is advisory only, and may or may not set the size of the internal buffer, which may in turn affect performance:

```
String.new(capacity: 1)
String.new('foo', capacity: 4096)
```

Note that Ruby strings are null-terminated internally, so the internal buffer size will be one or more bytes larger than the requested capacity depending on the encoding.

The `string`, `encoding`, and `capacity` arguments may all be used together:

```
String.new('hello', encoding: 'UTF-8', capacity: 25)
```

```
static VALUE
rb_str_init(int argc, VALUE *argv, VALUE str)
{
    static ID keyword_ids[2];
    VALUE orig, opt, venc, vcapa;
    VALUE kwargs[2];
    rb_encoding *enc = 0;
    int n;

    if (!keyword_ids[0]) {
        keyword_ids[0] = rb_id_encoding();
        CONST_ID(keyword_ids[1], "capacity");
    }

    n = rb_scan_args(argc, argv, "01:", &orig, &opt);
    if (!NIL_P(opt)) {
        rb_get_kwargs(opt, keyword_ids, 0, 2, kwargs);
        venc = kwargs[0];
        vcapa = kwargs[1];
        if (!UNDEF_P(venc) && !NIL_P(venc)) {
            enc = rb_to_encoding(venc);
        }
        if (!UNDEF_P(vcapa) && !NIL_P(vcapa)) {
            long capa = NUM2LONG(vcapa);
            long len = 0;
            int termlen = enc ? rb_enc_mbminlen(enc) : 1;

            if (capa < STR_BUF_MIN_SIZE) {
                capa = STR_BUF_MIN_SIZE;
            }
            if (n == 1) {
                StringValue(orig);
                len = RSTRING_LEN(orig);
                if (capa < len) {
                    capa = len;
                }
                if (orig == str) n = 0;
            }
            str_modifiable(str);
            if (STR_EMBED_P(str) || FL_TEST(str, STR_SHARED|STR_NOFREE)) {
                /* make noembed always */
                const size_t size = (size_t)capa + termlen;
                const char *const old_ptr = RSTRING_PTR(str);
                const size_t osize = RSTRING_LEN(str) + TERM_LEN(str);
                char *new_ptr = ALLOC_N(char, size);
                if (STR_EMBED_P(str)) RUBY_ASSERT((long)osize <= str_embed_capa(str));
                memcpy(new_ptr, old_ptr, osize < size ? osize : size);
                FL_UNSET_RAW(str, STR_SHARED|STR_NOFREE);
                RSTRING(str)->as.heap.ptr = new_ptr;
            }
            else if (STR_HEAP_SIZE(str) != (size_t)capa + termlen) {
                SIZED_REALLOC_N(RSTRING(str)->as.heap.ptr, char,
                        (size_t)capa + termlen, STR_HEAP_SIZE(str));
            }
            STR_SET_LEN(str, len);
            TERM_FILL(&RSTRING(str)->as.heap.ptr[len], termlen);
            if (n == 1) {
                memcpy(RSTRING(str)->as.heap.ptr, RSTRING_PTR(orig), len);
                rb_enc_cr_str_exact_copy(str, orig);
            }
            FL_SET(str, STR_NOEMBED);
            RSTRING(str)->as.heap.aux.capa = capa;
        }
        else if (n == 1) {
            rb_str_replace(str, orig);
        }
        if (enc) {
            rb_enc_associate(str, enc);
            ENC_CODERANGE_CLEAR(str);
        }
    }
    else if (n == 1) {
        rb_str_replace(str, orig);
    }
    return str;
}
```

try_convert(object) → object, new_string, or nil

click to toggle source

If `object` is a `String` object, returns `object`.

Otherwise if `object` responds to `:to_str`, calls `object.to_str` and returns the result.

Returns `nil` if `object` does not respond to `:to_str`.

Raises an exception unless `object.to_str` returns a `String` object.

```
static VALUE
rb_str_s_try_convert(VALUE dummy, VALUE str)
{
    return rb_check_string_type(str);
}
```

### Public Instance Methods

string % object → new_string

click to toggle source

Returns the result of formatting `object` into the format specification `self` (see `Kernel#sprintf` for formatting details):

```
"%05d" % 123 
```

If `self` contains multiple substitutions, `object` must be an `Array` or `Hash` containing the values to be substituted:

```
"%-5s: %016x" % [ "ID", self.object_id ] 
"foo = %{foo}" % {foo: 'bar'} 
"foo = %{foo}, baz = %{baz}" % {foo: 'bar', baz: 'bat'} 
```

```
static VALUE
rb_str_format_m(VALUE str, VALUE arg)
{
    VALUE tmp = rb_check_array_type(arg);

    if (!NIL_P(tmp)) {
        return rb_str_format(RARRAY_LENINT(tmp), RARRAY_CONST_PTR(tmp), str);
    }
    return rb_str_format(1, &arg, str);
}
```

string * integer → new_string

click to toggle source

Returns a new `String` containing `integer` copies of `self`:

```
"Ho! " * 3 
"Ho! " * 0 
```

```
VALUE
rb_str_times(VALUE str, VALUE times)
{
    VALUE str2;
    long n, len;
    char *ptr2;
    int termlen;

    if (times == INT2FIX(1)) {
        return str_duplicate(rb_cString, str);
    }
    if (times == INT2FIX(0)) {
        str2 = str_alloc_embed(rb_cString, 0);
        rb_enc_copy(str2, str);
        return str2;
    }
    len = NUM2LONG(times);
    if (len < 0) {
        rb_raise(rb_eArgError, "negative argument");
    }
    if (RSTRING_LEN(str) == 1 && RSTRING_PTR(str)[0] == 0) {
        if (STR_EMBEDDABLE_P(len, 1)) {
            str2 = str_alloc_embed(rb_cString, len + 1);
            memset(RSTRING_PTR(str2), 0, len + 1);
        }
        else {
            str2 = str_alloc_heap(rb_cString);
            RSTRING(str2)->as.heap.aux.capa = len;
            RSTRING(str2)->as.heap.ptr = ZALLOC_N(char, (size_t)len + 1);
        }
        STR_SET_LEN(str2, len);
        rb_enc_copy(str2, str);
        return str2;
    }
    if (len && LONG_MAX/len <  RSTRING_LEN(str)) {
        rb_raise(rb_eArgError, "argument too big");
    }

    len *= RSTRING_LEN(str);
    termlen = TERM_LEN(str);
    str2 = str_enc_new(rb_cString, 0, len, STR_ENC_GET(str));
    ptr2 = RSTRING_PTR(str2);
    if (len) {
        n = RSTRING_LEN(str);
        memcpy(ptr2, RSTRING_PTR(str), n);
        while (n <= len/2) {
            memcpy(ptr2 + n, ptr2, n);
            n *= 2;
        }
        memcpy(ptr2 + n, ptr2, len-n);
    }
    STR_SET_LEN(str2, len);
    TERM_FILL(&ptr2[len], termlen);
    rb_enc_cr_str_copy_for_substr(str2, str);

    return str2;
}
```

string + other_string → new_string

click to toggle source

Returns a new `String` containing `other_string` concatenated to `self`:

```
"Hello from " + self.to_s 
```

```
VALUE
rb_str_plus(VALUE str1, VALUE str2)
{
    VALUE str3;
    rb_encoding *enc;
    char *ptr1, *ptr2, *ptr3;
    long len1, len2;
    int termlen;

    StringValue(str2);
    enc = rb_enc_check_str(str1, str2);
    RSTRING_GETMEM(str1, ptr1, len1);
    RSTRING_GETMEM(str2, ptr2, len2);
    termlen = rb_enc_mbminlen(enc);
    if (len1 > LONG_MAX - len2) {
        rb_raise(rb_eArgError, "string size too big");
    }
    str3 = str_enc_new(rb_cString, 0, len1+len2, enc);
    ptr3 = RSTRING_PTR(str3);
    memcpy(ptr3, ptr1, len1);
    memcpy(ptr3+len1, ptr2, len2);
    TERM_FILL(&ptr3[len1+len2], termlen);

    ENCODING_CODERANGE_SET(str3, rb_enc_to_index(enc),
                           ENC_CODERANGE_AND(ENC_CODERANGE(str1), ENC_CODERANGE(str2)));
    RB_GC_GUARD(str1);
    RB_GC_GUARD(str2);
    return str3;
}
```

+string → new_string or self

click to toggle source

Returns `self` if `self` is not frozen and can be mutated without warning issuance.

Otherwise returns `self.dup`, which is not frozen.

```
static VALUE
str_uplus(VALUE str)
{
    if (OBJ_FROZEN(str) || CHILLED_STRING_P(str)) {
        return rb_str_dup(str);
    }
    else {
        return str;
    }
}
```

-string → frozen_string

click to toggle source

Returns a frozen, possibly pre-existing copy of the string.

The returned `String` will be deduplicated as long as it does not have any instance variables set on it and is not a `String` subclass.

Note that `-string` variant is more convenient for defining constants:

```
FILENAME = -'config/database.yml'
```

while `dedup` is better suitable for using the method in chains of calculations:

```
@url_list.concat(urls.map(&:dedup))
```

```
static VALUE
str_uminus(VALUE str)
{
    if (!BARE_STRING_P(str) && !rb_obj_frozen_p(str)) {
        str = rb_str_dup(str);
    }
    return rb_fstring(str);
}
```

Also aliased as:

dedup

string << object → string

click to toggle source

Concatenates `object` to `self` and returns `self`:

```
s = 'foo'
s << 'bar' 
s          
```

If `object` is an `Integer`, the value is considered a codepoint and converted to a character before concatenation:

```
s = 'foo'
s << 33 
```

If that codepoint is not representable in the encoding of *string*, `RangeError` is raised.

```
s = 'foo'
s.encoding              
s << 0x00110000         
s = 'foo'.encode('EUC-JP')
s << 0x00800080         
```

If the encoding is US-ASCII and the codepoint is 0..0xff, *string* is automatically promoted to ASCII-8BIT.

```
s = 'foo'.encode('US-ASCII')
s << 0xff
s.encoding              
```

Related: `String#concat`, which takes multiple arguments.

```
VALUE
rb_str_concat(VALUE str1, VALUE str2)
{
    unsigned int code;
    rb_encoding *enc = STR_ENC_GET(str1);
    int encidx;

    if (RB_INTEGER_TYPE_P(str2)) {
        if (rb_num_to_uint(str2, &code) == 0) {
        }
        else if (FIXNUM_P(str2)) {
            rb_raise(rb_eRangeError, "%ld out of char range", FIX2LONG(str2));
        }
        else {
            rb_raise(rb_eRangeError, "bignum out of char range");
        }
    }
    else {
        return rb_str_append(str1, str2);
    }

    encidx = rb_ascii8bit_appendable_encoding_index(enc, code);

    if (encidx >= 0) {
        rb_str_buf_cat_byte(str1, (unsigned char)code);
    }
    else {
        long pos = RSTRING_LEN(str1);
        int cr = ENC_CODERANGE(str1);
        int len;
        char *buf;

        switch (len = rb_enc_codelen(code, enc)) {
          case ONIGERR_INVALID_CODE_POINT_VALUE:
            rb_raise(rb_eRangeError, "invalid codepoint 0x%X in %s", code, rb_enc_name(enc));
            break;
          case ONIGERR_TOO_BIG_WIDE_CHAR_VALUE:
          case 0:
            rb_raise(rb_eRangeError, "%u out of char range", code);
            break;
        }
        buf = ALLOCA_N(char, len + 1);
        rb_enc_mbcput(code, buf, enc);
        if (rb_enc_precise_mbclen(buf, buf + len + 1, enc) != len) {
            rb_raise(rb_eRangeError, "invalid codepoint 0x%X in %s", code, rb_enc_name(enc));
        }
        rb_str_resize(str1, pos+len);
        memcpy(RSTRING_PTR(str1) + pos, buf, len);
        if (cr == ENC_CODERANGE_7BIT && code > 127) {
            cr = ENC_CODERANGE_VALID;
        }
        else if (cr == ENC_CODERANGE_BROKEN) {
            cr = ENC_CODERANGE_UNKNOWN;
        }
        ENC_CODERANGE_SET(str1, cr);
    }
    return str1;
}
```

string <=> other_string → -1, 0, 1, or nil

click to toggle source

Compares `self` and `other_string`, returning:

- -1 if `other_string` is larger.
- 0 if the two are equal.
- 1 if `other_string` is smaller.
- `nil` if the two are incomparable.

Examples:

```
'foo' <=> 'foo' 
'foo' <=> 'food' 
'food' <=> 'foo' 
'FOO' <=> 'foo' 
'foo' <=> 'FOO' 
'foo' <=> 1 
```

```
static VALUE
rb_str_cmp_m(VALUE str1, VALUE str2)
{
    int result;
    VALUE s = rb_check_string_type(str2);
    if (NIL_P(s)) {
        return rb_invcmp(str1, str2);
    }
    result = rb_str_cmp(str1, s);
    return INT2FIX(result);
}
```

string == object → true or false

click to toggle source

Returns `true` if `object` has the same length and content; as `self`; `false` otherwise:

```
s = 'foo'
s == 'foo' 
s == 'food' 
s == 'FOO' 
```

Returns `false` if the two strings’ encodings are not compatible:

```
"\u{e4 f6 fc}".encode("ISO-8859-1") == ("\u{c4 d6 dc}") 
```

If `object` is not an instance of `String` but responds to `to_str`, then the two strings are compared using `object.==`.

```
VALUE
rb_str_equal(VALUE str1, VALUE str2)
{
    if (str1 == str2) return Qtrue;
    if (!RB_TYPE_P(str2, T_STRING)) {
        if (!rb_respond_to(str2, idTo_str)) {
            return Qfalse;
        }
        return rb_equal(str2, str1);
    }
    return rb_str_eql_internal(str1, str2);
}
```

Also aliased as:

===

string === object → true or false

Returns `true` if `object` has the same length and content; as `self`; `false` otherwise:

```
s = 'foo'
s == 'foo' 
s == 'food' 
s == 'FOO' 
```

Returns `false` if the two strings’ encodings are not compatible:

```
"\u{e4 f6 fc}".encode("ISO-8859-1") == ("\u{c4 d6 dc}") 
```

If `object` is not an instance of `String` but responds to `to_str`, then the two strings are compared using `object.==`.

Alias for:

==

string =~ regexp → integer or nil

click to toggle source

string =~ object → integer or nil

Returns the `Integer` index of the first substring that matches the given `regexp`, or `nil` if no match found:

```
'foo' =~ /f/ 
'foo' =~ /o/ 
'foo' =~ /x/ 
```

Note: also updates Global Variables at `Regexp`.

If the given `object` is not a `Regexp`, returns the value returned by `object =~ self`.

Note that `string =~ regexp` is different from `regexp =~ string` (see Regexp#=~):

```
number= nil
"no. 9" =~ /(?<number>\d+)/
number 
/(?<number>\d+)/ =~ "no. 9"
number 
```

```
static VALUE
rb_str_match(VALUE x, VALUE y)
{
    switch (OBJ_BUILTIN_TYPE(y)) {
      case T_STRING:
        rb_raise(rb_eTypeError, "type mismatch: String given");

      case T_REGEXP:
        return rb_reg_match(y, x);

      default:
        return rb_funcall(y, idEqTilde, 1, x);
    }
}
```

string[index] → new_string or nil

click to toggle source

string[start, length] → new_string or nil

string[range] → new_string or nil

string[regexp, capture = 0] → new_string or nil

string[substring] → new_string or nil

Returns the substring of `self` specified by the arguments. See examples at String Slices.

```
static VALUE
rb_str_aref_m(int argc, VALUE *argv, VALUE str)
{
    if (argc == 2) {
        if (RB_TYPE_P(argv[0], T_REGEXP)) {
            return rb_str_subpat(str, argv[0], argv[1]);
        }
        else {
            return rb_str_substr_two_fixnums(str, argv[0], argv[1], TRUE);
        }
    }
    rb_check_arity(argc, 1, 2);
    return rb_str_aref(str, argv[0]);
}
```

Also aliased as:

slice

string[index] = new_string

click to toggle source

string[start, length] = new_string

string[range] = new_string

string[regexp, capture = 0] = new_string

string[substring] = new_string

Replaces all, some, or none of the contents of `self`; returns `new_string`. See String Slices.

A few examples:

```
s = 'foo'
s[2] = 'rtune'     
s                  
s[1, 5] = 'init'   
s                  
s[3..4] = 'al'     
s                  
s[/e$/] = 'ly'     
s                  
s['lly'] = 'ncial' 
s                  
```

```
static VALUE
rb_str_aset_m(int argc, VALUE *argv, VALUE str)
{
    if (argc == 3) {
        if (RB_TYPE_P(argv[0], T_REGEXP)) {
            rb_str_subpat_set(str, argv[0], argv[1], argv[2]);
        }
        else {
            rb_str_update(str, NUM2LONG(argv[0]), NUM2LONG(argv[1]), argv[2]);
        }
        return argv[2];
    }
    rb_check_arity(argc, 2, 3);
    return rb_str_aset(str, argv[0], argv[1]);
}
```

append_as_bytes(*objects) → string

click to toggle source

Concatenates each object in `objects` into `self` without any encoding validation or conversion and returns `self`:

```
s = 'foo'
s.append_as_bytes(" \xE2\x82")  
s.valid_encoding?               
s.append_as_bytes("\xAC 12")
s.valid_encoding?               
```

For each given object `object` that is an `Integer`, the value is considered a Byte. If the `Integer` is bigger than one byte, only the lower byte is considered, similar to `String#setbyte`:

```
s = ""
s.append_as_bytes(0, 257)             
```

Related: `String#<<`, `String#concat`, which do an encoding aware concatenation.

```
VALUE
rb_str_append_as_bytes(int argc, VALUE *argv, VALUE str)
{
    long needed_capacity = 0;
    volatile VALUE t0;
    enum ruby_value_type *types = ALLOCV_N(enum ruby_value_type, t0, argc);

    for (int index = 0; index < argc; index++) {
        VALUE obj = argv[index];
        enum ruby_value_type type = types[index] = rb_type(obj);
        switch (type) {
          case T_FIXNUM:
          case T_BIGNUM:
            needed_capacity++;
            break;
          case T_STRING:
            needed_capacity += RSTRING_LEN(obj);
            break;
          default:
            rb_raise(
                rb_eTypeError,
                "wrong argument type %"PRIsVALUE" (expected String or Integer)",
                rb_obj_class(obj)
            );
            break;
        }
    }

    str_ensure_available_capa(str, needed_capacity);
    char *sptr = RSTRING_END(str);

    for (int index = 0; index < argc; index++) {
        VALUE obj = argv[index];
        enum ruby_value_type type = types[index];
        switch (type) {
          case T_FIXNUM:
          case T_BIGNUM: {
            argv[index] = obj = rb_int_and(obj, INT2FIX(0xff));
            char byte = (char)(NUM2INT(obj) & 0xFF);
            *sptr = byte;
            sptr++;
            break;
          }
          case T_STRING: {
            const char *ptr;
            long len;
            RSTRING_GETMEM(obj, ptr, len);
            memcpy(sptr, ptr, len);
            sptr += len;
            break;
          }
          default:
            rb_bug("append_as_bytes arguments should have been validated");
        }
    }

    STR_SET_LEN(str, RSTRING_LEN(str) + needed_capacity);
    TERM_FILL(sptr, TERM_LEN(str)); /* sentinel */

    int cr = ENC_CODERANGE(str);
    switch (cr) {
      case ENC_CODERANGE_7BIT: {
        for (int index = 0; index < argc; index++) {
            VALUE obj = argv[index];
            enum ruby_value_type type = types[index];
            switch (type) {
              case T_FIXNUM:
              case T_BIGNUM: {
                if (!ISASCII(NUM2INT(obj))) {
                    goto clear_cr;
                }
                break;
              }
              case T_STRING: {
                if (ENC_CODERANGE(obj) != ENC_CODERANGE_7BIT) {
                    goto clear_cr;
                }
                break;
              }
              default:
                rb_bug("append_as_bytes arguments should have been validated");
            }
        }
        break;
      }
      case ENC_CODERANGE_VALID:
        if (ENCODING_GET_INLINED(str) == ENCINDEX_ASCII_8BIT) {
            goto keep_cr;
        }
        else {
            goto clear_cr;
        }
        break;
      default:
        goto clear_cr;
        break;
    }

    RB_GC_GUARD(t0);

  clear_cr:
    // If no fast path was hit, we clear the coderange.
    // append_as_bytes is predominently meant to be used in
    // buffering situation, hence it's likely the coderange
    // will never be scanned, so it's not worth spending time
    // precomputing the coderange except for simple and common
    // situations.
    ENC_CODERANGE_CLEAR(str);
  keep_cr:
    return str;
}
```

ascii_only? → true or false

click to toggle source

Returns `true` if `self` contains only ASCII characters, `false` otherwise:

```
'abc'.ascii_only?         
"abc\u{6666}".ascii_only? 
```

```
static VALUE
rb_str_is_ascii_only_p(VALUE str)
{
    int cr = rb_enc_str_coderange(str);

    return RBOOL(cr == ENC_CODERANGE_7BIT);
}
```

b → string

click to toggle source

Returns a copy of `self` that has ASCII-8BIT encoding; the underlying bytes are not modified:

```
s = "\x99"
s.encoding   
t = s.b      
t.encoding   

s = "\u4095" 
s.encoding   
s.bytes      
t = s.b      
t.encoding   
t.bytes      
```

```
static VALUE
rb_str_b(VALUE str)
{
    VALUE str2;
    if (STR_EMBED_P(str)) {
        str2 = str_alloc_embed(rb_cString, RSTRING_LEN(str) + TERM_LEN(str));
    }
    else {
        str2 = str_alloc_heap(rb_cString);
    }
    str_replace_shared_without_enc(str2, str);

    if (rb_enc_asciicompat(STR_ENC_GET(str))) {
        // BINARY strings can never be broken; they're either 7-bit ASCII or VALID.
        // If we know the receiver's code range then we know the result's code range.
        int cr = ENC_CODERANGE(str);
        switch (cr) {
          case ENC_CODERANGE_7BIT:
            ENC_CODERANGE_SET(str2, ENC_CODERANGE_7BIT);
            break;
          case ENC_CODERANGE_BROKEN:
          case ENC_CODERANGE_VALID:
            ENC_CODERANGE_SET(str2, ENC_CODERANGE_VALID);
            break;
          default:
            ENC_CODERANGE_CLEAR(str2);
            break;
        }
    }

    return str2;
}
```

byteindex(substring, offset = 0) → integer or nil

click to toggle source

byteindex(regexp, offset = 0) → integer or nil

Returns the `Integer` byte-based index of the first occurrence of the given `substring`, or `nil` if none found:

```
'foo'.byteindex('f') 
'foo'.byteindex('o') 
'foo'.byteindex('oo') 
'foo'.byteindex('ooo') 
```

Returns the `Integer` byte-based index of the first match for the given `Regexp` `regexp`, or `nil` if none found:

```
'foo'.byteindex(/f/) 
'foo'.byteindex(/o/) 
'foo'.byteindex(/oo/) 
'foo'.byteindex(/ooo/) 
```

`Integer` argument `offset`, if given, specifies the byte-based position in the string to begin the search:

```
'foo'.byteindex('o', 1) 
'foo'.byteindex('o', 2) 
'foo'.byteindex('o', 3) 
```

If `offset` is negative, counts backward from the end of `self`:

```
'foo'.byteindex('o', -1) 
'foo'.byteindex('o', -2) 
'foo'.byteindex('o', -3) 
'foo'.byteindex('o', -4) 
```

If `offset` does not land on character (codepoint) boundary, `IndexError` is raised.

Related: `String#index`, `String#byterindex`.

```
static VALUE
rb_str_byteindex_m(int argc, VALUE *argv, VALUE str)
{
    VALUE sub;
    VALUE initpos;
    long pos;

    if (rb_scan_args(argc, argv, "11", &sub, &initpos) == 2) {
        long slen = RSTRING_LEN(str);
        pos = NUM2LONG(initpos);
        if (pos < 0 ? (pos += slen) < 0 : pos > slen) {
            if (RB_TYPE_P(sub, T_REGEXP)) {
                rb_backref_set(Qnil);
            }
            return Qnil;
        }
    }
    else {
        pos = 0;
    }

    str_ensure_byte_pos(str, pos);

    if (RB_TYPE_P(sub, T_REGEXP)) {
        if (rb_reg_search(sub, str, pos, 0) >= 0) {
            VALUE match = rb_backref_get();
            struct re_registers *regs = RMATCH_REGS(match);
            pos = BEG(0);
            return LONG2NUM(pos);
        }
    }
    else {
        StringValue(sub);
        pos = rb_str_byteindex(str, sub, pos);
        if (pos >= 0) return LONG2NUM(pos);
    }
    return Qnil;
}
```

byterindex(substring, offset = self.bytesize) → integer or nil

click to toggle source

byterindex(regexp, offset = self.bytesize) → integer or nil

Returns the `Integer` byte-based index of the *last* occurrence of the given `substring`, or `nil` if none found:

```
'foo'.byterindex('f') 
'foo'.byterindex('o') 
'foo'.byterindex('oo') 
'foo'.byterindex('ooo') 
```

Returns the `Integer` byte-based index of the *last* match for the given `Regexp` `regexp`, or `nil` if none found:

```
'foo'.byterindex(/f/) 
'foo'.byterindex(/o/) 
'foo'.byterindex(/oo/) 
'foo'.byterindex(/ooo/) 
```

The *last* match means starting at the possible last position, not the last of longest matches.

```
'foo'.byterindex(/o+/) 
$~ 
```

To get the last longest match, needs to combine with negative lookbehind.

```
'foo'.byterindex(/(?<!o)o+/) 
$~ 
```

Or `String#byteindex` with negative lookforward.

```
'foo'.byteindex(/o+(?!.*o)/) 
$~ 
```

`Integer` argument `offset`, if given and non-negative, specifies the maximum starting byte-based position in the string to *end* the search:

```
'foo'.byterindex('o', 0) 
'foo'.byterindex('o', 1) 
'foo'.byterindex('o', 2) 
'foo'.byterindex('o', 3) 
```

If `offset` is a negative `Integer`, the maximum starting position in the string to *end* the search is the sum of the string’s length and `offset`:

```
'foo'.byterindex('o', -1) 
'foo'.byterindex('o', -2) 
'foo'.byterindex('o', -3) 
'foo'.byterindex('o', -4) 
```

If `offset` does not land on character (codepoint) boundary, `IndexError` is raised.

Related: `String#byteindex`.

```
static VALUE
rb_str_byterindex_m(int argc, VALUE *argv, VALUE str)
{
    VALUE sub;
    VALUE initpos;
    long pos, len = RSTRING_LEN(str);

    if (rb_scan_args(argc, argv, "11", &sub, &initpos) == 2) {
        pos = NUM2LONG(initpos);
        if (pos < 0 && (pos += len) < 0) {
            if (RB_TYPE_P(sub, T_REGEXP)) {
                rb_backref_set(Qnil);
            }
            return Qnil;
        }
        if (pos > len) pos = len;
    }
    else {
        pos = len;
    }

    str_ensure_byte_pos(str, pos);

    if (RB_TYPE_P(sub, T_REGEXP)) {
        if (rb_reg_search(sub, str, pos, 1) >= 0) {
            VALUE match = rb_backref_get();
            struct re_registers *regs = RMATCH_REGS(match);
            pos = BEG(0);
            return LONG2NUM(pos);
        }
    }
    else {
        StringValue(sub);
        pos = rb_str_byterindex(str, sub, pos);
        if (pos >= 0) return LONG2NUM(pos);
    }
    return Qnil;
}
```

bytes → array_of_bytes

click to toggle source

Returns an array of the bytes in `self`:

```
'hello'.bytes 
'тест'.bytes  
'こんにちは'.bytes
```

```
static VALUE
rb_str_bytes(VALUE str)
{
    VALUE ary = WANTARRAY("bytes", RSTRING_LEN(str));
    return rb_str_enumerate_bytes(str, ary);
}
```

bytesize → integer

click to toggle source

Returns the count of bytes (not characters) in `self`:

```
'foo'.bytesize        
'тест'.bytesize       
'こんにちは'.bytesize   
```

Contrast with `String#length`:

```
'foo'.length       
'тест'.length      
'こんにちは'.length  
```

```
VALUE
rb_str_bytesize(VALUE str)
{
    return LONG2NUM(RSTRING_LEN(str));
}
```

byteslice(index, length = 1) → string or nil

click to toggle source

byteslice(range) → string or nil

Returns a substring of `self`, or `nil` if the substring cannot be constructed.

With integer arguments `index` and `length` given, returns the substring beginning at the given `index` of the given `length` (if possible), or `nil` if `length` is negative or `index` falls outside of `self`:

```
s = '0123456789' 
s.byteslice(2)   
s.byteslice(200) 
s.byteslice(4, 3)  
s.byteslice(4, 30) 
s.byteslice(4, -1) 
s.byteslice(40, 2) 
```

In either case above, counts backwards from the end of `self` if `index` is negative:

```
s = '0123456789'   
s.byteslice(-4)    
s.byteslice(-4, 3) 
```

With `Range` argument `range` given, returns `byteslice(range.begin, range.size)`:

```
s = '0123456789'    
s.byteslice(4..6)   
s.byteslice(-6..-4) 
s.byteslice(5..2)   
s.byteslice(40..42) 
```

In all cases, a returned string has the same encoding as `self`:

```
s.encoding              
s.byteslice(4).encoding 
```

```
static VALUE
rb_str_byteslice(int argc, VALUE *argv, VALUE str)
{
    if (argc == 2) {
        long beg = NUM2LONG(argv[0]);
        long len = NUM2LONG(argv[1]);
        return str_byte_substr(str, beg, len, TRUE);
    }
    rb_check_arity(argc, 1, 2);
    return str_byte_aref(str, argv[0]);
}
```

bytesplice(index, length, str) → string

click to toggle source

bytesplice(index, length, str, str_index, str_length) → string

bytesplice(range, str) → string

bytesplice(range, str, str_range) → string

Replaces some or all of the content of `self` with `str`, and returns `self`. The portion of the string affected is determined using the same criteria as `String#byteslice`, except that `length` cannot be omitted. If the replacement string is not the same length as the text it is replacing, the string will be adjusted accordingly.

If `str_index` and `str_length`, or `str_range` are given, the content of `self` is replaced by str.byteslice(str_index, str_length) or str.byteslice(str_range); however the substring of `str` is not allocated as a new string.

The form that take an `Integer` will raise an `IndexError` if the value is out of range; the `Range` form will raise a `RangeError`. If the beginning or ending offset does not land on character (codepoint) boundary, an `IndexError` will be raised.

```
static VALUE
rb_str_bytesplice(int argc, VALUE *argv, VALUE str)
{
    long beg, len, vbeg, vlen;
    VALUE val;
    int cr;

    rb_check_arity(argc, 2, 5);
    if (!(argc == 2 || argc == 3 || argc == 5)) {
        rb_raise(rb_eArgError, "wrong number of arguments (given %d, expected 2, 3, or 5)", argc);
    }
    if (argc == 2 || (argc == 3 && !RB_INTEGER_TYPE_P(argv[0]))) {
        if (!rb_range_beg_len(argv[0], &beg, &len, RSTRING_LEN(str), 2)) {
            rb_raise(rb_eTypeError, "wrong argument type %s (expected Range)",
                     rb_builtin_class_name(argv[0]));
        }
        val = argv[1];
        StringValue(val);
        if (argc == 2) {
            /* bytesplice(range, str) */
            vbeg = 0;
            vlen = RSTRING_LEN(val);
        }
        else {
            /* bytesplice(range, str, str_range) */
            if (!rb_range_beg_len(argv[2], &vbeg, &vlen, RSTRING_LEN(val), 2)) {
                rb_raise(rb_eTypeError, "wrong argument type %s (expected Range)",
                         rb_builtin_class_name(argv[2]));
            }
        }
    }
    else {
        beg = NUM2LONG(argv[0]);
        len = NUM2LONG(argv[1]);
        val = argv[2];
        StringValue(val);
        if (argc == 3) {
            /* bytesplice(index, length, str) */
            vbeg = 0;
            vlen = RSTRING_LEN(val);
        }
        else {
            /* bytesplice(index, length, str, str_index, str_length) */
            vbeg = NUM2LONG(argv[3]);
            vlen = NUM2LONG(argv[4]);
        }
    }
    str_check_beg_len(str, &beg, &len);
    str_check_beg_len(val, &vbeg, &vlen);
    str_modify_keep_cr(str);

    if (RB_UNLIKELY(ENCODING_GET_INLINED(str) != ENCODING_GET_INLINED(val))) {
        rb_enc_associate(str, rb_enc_check(str, val));
    }

    rb_str_update_1(str, beg, len, val, vbeg, vlen);
    cr = ENC_CODERANGE_AND(ENC_CODERANGE(str), ENC_CODERANGE(val));
    if (cr != ENC_CODERANGE_BROKEN)
        ENC_CODERANGE_SET(str, cr);
    return str;
}
```

capitalize(*options) → string

click to toggle source

Returns a string containing the characters in `self`; the first character is upcased; the remaining characters are downcased:

```
s = 'hello World!' 
s.capitalize       
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#capitalize!`.

```
static VALUE
rb_str_capitalize(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_UPCASE | ONIGENC_CASE_TITLECASE;
    VALUE ret;

    flags = check_case_options(argc, argv, flags);
    enc = str_true_enc(str);
    if (RSTRING_LEN(str) == 0 || !RSTRING_PTR(str)) return str;
    if (flags&ONIGENC_CASE_ASCII_ONLY) {
        ret = rb_str_new(0, RSTRING_LEN(str));
        rb_str_ascii_casemap(str, ret, &flags, enc);
    }
    else {
        ret = rb_str_casemap(str, &flags, enc);
    }
    return ret;
}
```

capitalize!(*options) → self or nil

click to toggle source

Upcases the first character in `self`; downcases the remaining characters; returns `self` if any changes were made, `nil` otherwise:

```
s = 'hello World!' 
s.capitalize!      
s                  
s.capitalize!      
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#capitalize`.

```
static VALUE
rb_str_capitalize_bang(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_UPCASE | ONIGENC_CASE_TITLECASE;

    flags = check_case_options(argc, argv, flags);
    str_modify_keep_cr(str);
    enc = str_true_enc(str);
    if (RSTRING_LEN(str) == 0 || !RSTRING_PTR(str)) return Qnil;
    if (flags&ONIGENC_CASE_ASCII_ONLY)
        rb_str_ascii_casemap(str, str, &flags, enc);
    else
        str_shared_replace(str, rb_str_casemap(str, &flags, enc));

    if (ONIGENC_CASE_MODIFIED&flags) return str;
    return Qnil;
}
```

casecmp(other_string) → -1, 0, 1, or nil

click to toggle source

Compares `self.downcase` and `other_string.downcase`; returns:

- -1 if `other_string.downcase` is larger.
- 0 if the two are equal.
- 1 if `other_string.downcase` is smaller.
- `nil` if the two are incomparable.

Examples:

```
'foo'.casecmp('foo') 
'foo'.casecmp('food') 
'food'.casecmp('foo') 
'FOO'.casecmp('foo') 
'foo'.casecmp('FOO') 
'foo'.casecmp(1) 
```

See Case Mapping.

Related: `String#casecmp?`.

```
static VALUE
rb_str_casecmp(VALUE str1, VALUE str2)
{
    VALUE s = rb_check_string_type(str2);
    if (NIL_P(s)) {
        return Qnil;
    }
    return str_casecmp(str1, s);
}
```

casecmp?(other_string) → true, false, or nil

click to toggle source

Returns `true` if `self` and `other_string` are equal after Unicode case folding, otherwise `false`:

```
'foo'.casecmp?('foo') 
'foo'.casecmp?('food') 
'food'.casecmp?('foo') 
'FOO'.casecmp?('foo') 
'foo'.casecmp?('FOO') 
```

Returns `nil` if the two values are incomparable:

```
'foo'.casecmp?(1) 
```

See Case Mapping.

Related: `String#casecmp`.

```
static VALUE
rb_str_casecmp_p(VALUE str1, VALUE str2)
{
    VALUE s = rb_check_string_type(str2);
    if (NIL_P(s)) {
        return Qnil;
    }
    return str_casecmp_p(str1, s);
}
```

center(size, pad_string = ' ') → new_string

click to toggle source

Returns a centered copy of `self`.

If integer argument `size` is greater than the size (in characters) of `self`, returns a new string of length `size` that is a copy of `self`, centered and padded on both ends with `pad_string`:

```
'hello'.center(10)       
'  hello'.center(10)     
'hello'.center(10, 'ab') 
'тест'.center(10)        
'こんにちは'.center(10)    
```

If `size` is not greater than the size of `self`, returns a copy of `self`:

```
'hello'.center(5)  
'hello'.center(1)  
```

Related: `String#ljust`, `String#rjust`.

```
static VALUE
rb_str_center(int argc, VALUE *argv, VALUE str)
{
    return rb_str_justify(argc, argv, str, 'c');
}
```

chars → array_of_characters

click to toggle source

Returns an array of the characters in `self`:

```
'hello'.chars     
'тест'.chars      
'こんにちは'.chars 
```

```
static VALUE
rb_str_chars(VALUE str)
{
    VALUE ary = WANTARRAY("chars", rb_str_strlen(str));
    return rb_str_enumerate_chars(str, ary);
}
```

chomp(line_sep = $/) → new_string

click to toggle source

Returns a new string copied from `self`, with trailing characters possibly removed:

When `line_sep` is `"\n"`, removes the last one or two characters if they are `"\r"`, `"\n"`, or `"\r\n"` (but not `"\n\r"`):

```
$/                    
"abc\r".chomp         
"abc\n".chomp         
"abc\r\n".chomp       
"abc\n\r".chomp       
"тест\r\n".chomp      
"こんにちは\r\n".chomp  
```

When `line_sep` is `''` (an empty string), removes multiple trailing occurrences of `"\n"` or `"\r\n"` (but not `"\r"` or `"\n\r"`):

```
"abc\n\n\n".chomp('')           
"abc\r\n\r\n\r\n".chomp('')     
"abc\n\n\r\n\r\n\n\n".chomp('') 
"abc\n\r\n\r\n\r".chomp('')     
"abc\r\r\r".chomp('')           
```

When `line_sep` is neither `"\n"` nor `''`, removes a single trailing line separator if there is one:

```
'abcd'.chomp('d')  
'abcdd'.chomp('d') 
```

```
static VALUE
rb_str_chomp(int argc, VALUE *argv, VALUE str)
{
    VALUE rs = chomp_rs(argc, argv);
    if (NIL_P(rs)) return str_duplicate(rb_cString, str);
    return rb_str_subseq(str, 0, chompped_length(str, rs));
}
```

chomp!(line_sep = $/) → self or nil

click to toggle source

Like `String#chomp`, but modifies `self` in place; returns `nil` if no modification made, `self` otherwise.

```
static VALUE
rb_str_chomp_bang(int argc, VALUE *argv, VALUE str)
{
    VALUE rs;
    str_modifiable(str);
    if (RSTRING_LEN(str) == 0 && argc < 2) return Qnil;
    rs = chomp_rs(argc, argv);
    if (NIL_P(rs)) return Qnil;
    return rb_str_chomp_string(str, rs);
}
```

chop → new_string

click to toggle source

Returns a new string copied from `self`, with trailing characters possibly removed.

Removes `"\r\n"` if those are the last two characters.

```
"abc\r\n".chop      
"тест\r\n".chop     
"こんにちは\r\n".chop 
```

Otherwise removes the last character if it exists.

```
'abcd'.chop     
'тест'.chop     
'こんにちは'.chop 
''.chop         
```

If you only need to remove the newline separator at the end of the string, `String#chomp` is a better alternative.

```
static VALUE
rb_str_chop(VALUE str)
{
    return rb_str_subseq(str, 0, chopped_length(str));
}
```

chop! → self or nil

click to toggle source

Like `String#chop`, but modifies `self` in place; returns `nil` if `self` is empty, `self` otherwise.

Related: `String#chomp!`.

```
static VALUE
rb_str_chop_bang(VALUE str)
{
    str_modify_keep_cr(str);
    if (RSTRING_LEN(str) > 0) {
        long len;
        len = chopped_length(str);
        STR_SET_LEN(str, len);
        TERM_FILL(&RSTRING_PTR(str)[len], TERM_LEN(str));
        if (ENC_CODERANGE(str) != ENC_CODERANGE_7BIT) {
            ENC_CODERANGE_CLEAR(str);
        }
        return str;
    }
    return Qnil;
}
```

chr → string

click to toggle source

Returns a string containing the first character of `self`:

```
s = 'foo' 
s.chr     
```

```
static VALUE
rb_str_chr(VALUE str)
{
    return rb_str_substr(str, 0, 1);
}
```

clear → self

click to toggle source

Removes the contents of `self`:

```
s = 'foo' 
s.clear   
```

```
static VALUE
rb_str_clear(VALUE str)
{
    str_discard(str);
    STR_SET_EMBED(str);
    STR_SET_LEN(str, 0);
    RSTRING_PTR(str)[0] = 0;
    if (rb_enc_asciicompat(STR_ENC_GET(str)))
        ENC_CODERANGE_SET(str, ENC_CODERANGE_7BIT);
    else
        ENC_CODERANGE_SET(str, ENC_CODERANGE_VALID);
    return str;
}
```

codepoints → array_of_integers

click to toggle source

Returns an array of the codepoints in `self`; each codepoint is the integer value for a character:

```
'hello'.codepoints     
'тест'.codepoints      
'こんにちは'.codepoints 
```

```
static VALUE
rb_str_codepoints(VALUE str)
{
    VALUE ary = WANTARRAY("codepoints", rb_str_strlen(str));
    return rb_str_enumerate_codepoints(str, ary);
}
```

concat(*objects) → string

click to toggle source

Concatenates each object in `objects` to `self` and returns `self`:

```
s = 'foo'
s.concat('bar', 'baz') 
s                      
```

For each given object `object` that is an `Integer`, the value is considered a codepoint and converted to a character before concatenation:

```
s = 'foo'
s.concat(32, 'bar', 32, 'baz') 
```

Related: `String#<<`, which takes a single argument.

```
static VALUE
rb_str_concat_multi(int argc, VALUE *argv, VALUE str)
{
    str_modifiable(str);

    if (argc == 1) {
        return rb_str_concat(str, argv[0]);
    }
    else if (argc > 1) {
        int i;
        VALUE arg_str = rb_str_tmp_new(0);
        rb_enc_copy(arg_str, str);
        for (i = 0; i < argc; i++) {
            rb_str_concat(arg_str, argv[i]);
        }
        rb_str_buf_append(str, arg_str);
    }

    return str;
}
```

count(*selectors) → integer

click to toggle source

Returns the total number of characters in `self` that are specified by the given `selectors` (see Multiple Character Selectors):

```
a = "hello world"
a.count "lo"                   
a.count "lo", "o"              
a.count "hello", "^l"          
a.count "ej-m"                 

"hello^world".count "\\^aeiou" 
"hello-world".count "a\\-eo"   

c = "hello world\\r\\n"
c.count "\\"                   
c.count "\\A"                  
c.count "X-\\w"                
```

```
static VALUE
rb_str_count(int argc, VALUE *argv, VALUE str)
{
    char table[TR_TABLE_SIZE];
    rb_encoding *enc = 0;
    VALUE del = 0, nodel = 0, tstr;
    char *s, *send;
    int i;
    int ascompat;
    size_t n = 0;

    rb_check_arity(argc, 1, UNLIMITED_ARGUMENTS);

    tstr = argv[0];
    StringValue(tstr);
    enc = rb_enc_check(str, tstr);
    if (argc == 1) {
        const char *ptstr;
        if (RSTRING_LEN(tstr) == 1 && rb_enc_asciicompat(enc) &&
            (ptstr = RSTRING_PTR(tstr),
             ONIGENC_IS_ALLOWED_REVERSE_MATCH(enc, (const unsigned char *)ptstr, (const unsigned char *)ptstr+1)) &&
            !is_broken_string(str)) {
            int clen;
            unsigned char c = rb_enc_codepoint_len(ptstr, ptstr+1, &clen, enc);

            s = RSTRING_PTR(str);
            if (!s || RSTRING_LEN(str) == 0) return INT2FIX(0);
            send = RSTRING_END(str);
            while (s < send) {
                if (*(unsigned char*)s++ == c) n++;
            }
            return SIZET2NUM(n);
        }
    }

    tr_setup_table(tstr, table, TRUE, &del, &nodel, enc);
    for (i=1; i<argc; i++) {
        tstr = argv[i];
        StringValue(tstr);
        enc = rb_enc_check(str, tstr);
        tr_setup_table(tstr, table, FALSE, &del, &nodel, enc);
    }

    s = RSTRING_PTR(str);
    if (!s || RSTRING_LEN(str) == 0) return INT2FIX(0);
    send = RSTRING_END(str);
    ascompat = rb_enc_asciicompat(enc);
    while (s < send) {
        unsigned int c;

        if (ascompat && (c = *(unsigned char*)s) < 0x80) {
            if (table[c]) {
                n++;
            }
            s++;
        }
        else {
            int clen;
            c = rb_enc_codepoint_len(s, send, &clen, enc);
            if (tr_find(c, table, del, nodel)) {
                n++;
            }
            s += clen;
        }
    }

    return SIZET2NUM(n);
}
```

crypt(salt_str) → new_string

click to toggle source

Returns the string generated by calling `crypt(3)` standard library function with `str` and `salt_str`, in this order, as its arguments. Please do not use this method any longer. It is legacy; provided only for backward compatibility with ruby scripts in earlier days. It is bad to use in contemporary programs for several reasons:

- Behaviour of C’s `crypt(3)` depends on the OS it is run. The generated string lacks data portability.
- On some OSes such as Mac OS, `crypt(3)` never fails (i.e. silently ends up in unexpected results).
- On some OSes such as Mac OS, `crypt(3)` is not thread safe.
- So-called “traditional” usage of `crypt(3)` is very very very weak. According to its manpage, Linux’s traditional `crypt(3)` output has only 2**56 variations; too easy to brute force today. And this is the default behaviour.
- In order to make things robust some OSes implement so-called “modular” usage. To go through, you have to do a complex build-up of the `salt_str` parameter, by hand. Failure in generation of a proper salt string tends not to yield any errors; typos in parameters are normally not detectable.
  - For instance, in the following example, the second invocation of `String#crypt` is wrong; it has a typo in “round=” (lacks “s”). However the call does not fail and something unexpected is generated.
    ```
"foo".crypt("$5$rounds=1000$salt$") 
"foo".crypt("$5$round=1000$salt$")  
    ```
- Even in the “modular” mode, some hash functions are considered archaic and no longer recommended at all; for instance module `$1$` is officially abandoned by its author: see phk.freebsd.dk/sagas/md5crypt_eol/ . For another instance module `$3$` is considered completely broken: see the manpage of FreeBSD.
- On some OS such as Mac OS, there is no modular mode. Yet, as written above, `crypt(3)` on Mac OS never fails. This means even if you build up a proper salt string it generates a traditional DES hash anyways, and there is no way for you to be aware of.
  ```
"foo".crypt("$5$rounds=1000$salt$") 
  ```

If for some reason you cannot migrate to other secure contemporary password hashing algorithms, install the string-crypt gem and `require 'string/crypt'` to continue using it.

```
static VALUE
rb_str_crypt(VALUE str, VALUE salt)
{
#ifdef HAVE_CRYPT_R
    VALUE databuf;
    struct crypt_data *data;
#   define CRYPT_END() ALLOCV_END(databuf)
#else
    extern char *crypt(const char *, const char *);
#   define CRYPT_END() rb_nativethread_lock_unlock(&crypt_mutex.lock)
#endif
    VALUE result;
    const char *s, *saltp;
    char *res;
#ifdef BROKEN_CRYPT
    char salt_8bit_clean[3];
#endif

    StringValue(salt);
    mustnot_wchar(str);
    mustnot_wchar(salt);
    s = StringValueCStr(str);
    saltp = RSTRING_PTR(salt);
    if (RSTRING_LEN(salt) < 2 || !saltp[0] || !saltp[1]) {
        rb_raise(rb_eArgError, "salt too short (need >=2 bytes)");
    }

#ifdef BROKEN_CRYPT
    if (!ISASCII((unsigned char)saltp[0]) || !ISASCII((unsigned char)saltp[1])) {
        salt_8bit_clean[0] = saltp[0] & 0x7f;
        salt_8bit_clean[1] = saltp[1] & 0x7f;
        salt_8bit_clean[2] = '\0';
        saltp = salt_8bit_clean;
    }
#endif
#ifdef HAVE_CRYPT_R
    data = ALLOCV(databuf, sizeof(struct crypt_data));
# ifdef HAVE_STRUCT_CRYPT_DATA_INITIALIZED
    data->initialized = 0;
# endif
    res = crypt_r(s, saltp, data);
#else
    crypt_mutex_initialize();
    rb_nativethread_lock_lock(&crypt_mutex.lock);
    res = crypt(s, saltp);
#endif
    if (!res) {
        int err = errno;
        CRYPT_END();
        rb_syserr_fail(err, "crypt");
    }
    result = rb_str_new_cstr(res);
    CRYPT_END();
    return result;
}
```

-string → frozen_string

dedup → frozen_string

Returns a frozen, possibly pre-existing copy of the string.

The returned `String` will be deduplicated as long as it does not have any instance variables set on it and is not a `String` subclass.

Note that `-string` variant is more convenient for defining constants:

```
FILENAME = -'config/database.yml'
```

while `dedup` is better suitable for using the method in chains of calculations:

```
@url_list.concat(urls.map(&:dedup))
```

Alias for:

-@

delete(*selectors) → new_string

click to toggle source

Returns a copy of `self` with characters specified by `selectors` removed (see Multiple Character Selectors):

```
"hello".delete "l","lo"        
"hello".delete "lo"            
"hello".delete "aeiou", "^e"   
"hello".delete "ej-m"          
```

```
static VALUE
rb_str_delete(int argc, VALUE *argv, VALUE str)
{
    str = str_duplicate(rb_cString, str);
    rb_str_delete_bang(argc, argv, str);
    return str;
}
```

delete!(*selectors) → self or nil

click to toggle source

Like `String#delete`, but modifies `self` in place. Returns `self` if any changes were made, `nil` otherwise.

```
static VALUE
rb_str_delete_bang(int argc, VALUE *argv, VALUE str)
{
    char squeez[TR_TABLE_SIZE];
    rb_encoding *enc = 0;
    char *s, *send, *t;
    VALUE del = 0, nodel = 0;
    int modify = 0;
    int i, ascompat, cr;

    if (RSTRING_LEN(str) == 0 || !RSTRING_PTR(str)) return Qnil;
    rb_check_arity(argc, 1, UNLIMITED_ARGUMENTS);
    for (i=0; i<argc; i++) {
        VALUE s = argv[i];

        StringValue(s);
        enc = rb_enc_check(str, s);
        tr_setup_table(s, squeez, i==0, &del, &nodel, enc);
    }

    str_modify_keep_cr(str);
    ascompat = rb_enc_asciicompat(enc);
    s = t = RSTRING_PTR(str);
    send = RSTRING_END(str);
    cr = ascompat ? ENC_CODERANGE_7BIT : ENC_CODERANGE_VALID;
    while (s < send) {
        unsigned int c;
        int clen;

        if (ascompat && (c = *(unsigned char*)s) < 0x80) {
            if (squeez[c]) {
                modify = 1;
            }
            else {
                if (t != s) *t = c;
                t++;
            }
            s++;
        }
        else {
            c = rb_enc_codepoint_len(s, send, &clen, enc);

            if (tr_find(c, squeez, del, nodel)) {
                modify = 1;
            }
            else {
                if (t != s) rb_enc_mbcput(c, t, enc);
                t += clen;
                if (cr == ENC_CODERANGE_7BIT) cr = ENC_CODERANGE_VALID;
            }
            s += clen;
        }
    }
    TERM_FILL(t, TERM_LEN(str));
    STR_SET_LEN(str, t - RSTRING_PTR(str));
    ENC_CODERANGE_SET(str, cr);

    if (modify) return str;
    return Qnil;
}
```

delete_prefix(prefix) → new_string

click to toggle source

Returns a copy of `self` with leading substring `prefix` removed:

```
'hello'.delete_prefix('hel')      
'hello'.delete_prefix('llo')      
'тест'.delete_prefix('те')        
'こんにちは'.delete_prefix('こん')  
```

Related: `String#delete_prefix!`, `String#delete_suffix`.

```
static VALUE
rb_str_delete_prefix(VALUE str, VALUE prefix)
{
    long prefixlen;

    prefixlen = deleted_prefix_length(str, prefix);
    if (prefixlen <= 0) return str_duplicate(rb_cString, str);

    return rb_str_subseq(str, prefixlen, RSTRING_LEN(str) - prefixlen);
}
```

delete_prefix!(prefix) → self or nil

click to toggle source

Like `String#delete_prefix`, except that `self` is modified in place. Returns `self` if the prefix is removed, `nil` otherwise.

```
static VALUE
rb_str_delete_prefix_bang(VALUE str, VALUE prefix)
{
    long prefixlen;
    str_modify_keep_cr(str);

    prefixlen = deleted_prefix_length(str, prefix);
    if (prefixlen <= 0) return Qnil;

    return rb_str_drop_bytes(str, prefixlen);
}
```

delete_suffix(suffix) → new_string

click to toggle source

Returns a copy of `self` with trailing substring `suffix` removed:

```
'hello'.delete_suffix('llo')      
'hello'.delete_suffix('hel')      
'тест'.delete_suffix('ст')        
'こんにちは'.delete_suffix('ちは')  
```

Related: `String#delete_suffix!`, `String#delete_prefix`.

```
static VALUE
rb_str_delete_suffix(VALUE str, VALUE suffix)
{
    long suffixlen;

    suffixlen = deleted_suffix_length(str, suffix);
    if (suffixlen <= 0) return str_duplicate(rb_cString, str);

    return rb_str_subseq(str, 0, RSTRING_LEN(str) - suffixlen);
}
```

delete_suffix!(suffix) → self or nil

click to toggle source

Like `String#delete_suffix`, except that `self` is modified in place. Returns `self` if the suffix is removed, `nil` otherwise.

```
static VALUE
rb_str_delete_suffix_bang(VALUE str, VALUE suffix)
{
    long olen, suffixlen, len;
    str_modifiable(str);

    suffixlen = deleted_suffix_length(str, suffix);
    if (suffixlen <= 0) return Qnil;

    olen = RSTRING_LEN(str);
    str_modify_keep_cr(str);
    len = olen - suffixlen;
    STR_SET_LEN(str, len);
    TERM_FILL(&RSTRING_PTR(str)[len], TERM_LEN(str));
    if (ENC_CODERANGE(str) != ENC_CODERANGE_7BIT) {
        ENC_CODERANGE_CLEAR(str);
    }
    return str;
}
```

downcase(*options) → string

click to toggle source

Returns a string containing the downcased characters in `self`:

```
s = 'Hello World!' 
s.downcase         
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#downcase!`, `String#upcase`, `String#upcase!`.

```
static VALUE
rb_str_downcase(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_DOWNCASE;
    VALUE ret;

    flags = check_case_options(argc, argv, flags);
    enc = str_true_enc(str);
    if (case_option_single_p(flags, enc, str)) {
        ret = rb_str_new(RSTRING_PTR(str), RSTRING_LEN(str));
        str_enc_copy_direct(ret, str);
        downcase_single(ret);
    }
    else if (flags&ONIGENC_CASE_ASCII_ONLY) {
        ret = rb_str_new(0, RSTRING_LEN(str));
        rb_str_ascii_casemap(str, ret, &flags, enc);
    }
    else {
        ret = rb_str_casemap(str, &flags, enc);
    }

    return ret;
}
```

downcase!(*options) → self or nil

click to toggle source

Downcases the characters in `self`; returns `self` if any changes were made, `nil` otherwise:

```
s = 'Hello World!' 
s.downcase!        
s                  
s.downcase!        
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#downcase`, `String#upcase`, `String#upcase!`.

```
static VALUE
rb_str_downcase_bang(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_DOWNCASE;

    flags = check_case_options(argc, argv, flags);
    str_modify_keep_cr(str);
    enc = str_true_enc(str);
    if (case_option_single_p(flags, enc, str)) {
        if (downcase_single(str))
            flags |= ONIGENC_CASE_MODIFIED;
    }
    else if (flags&ONIGENC_CASE_ASCII_ONLY)
        rb_str_ascii_casemap(str, str, &flags, enc);
    else
        str_shared_replace(str, rb_str_casemap(str, &flags, enc));

    if (ONIGENC_CASE_MODIFIED&flags) return str;
    return Qnil;
}
```

dump → string

click to toggle source

Returns a printable version of `self`, enclosed in double-quotes, with special characters escaped, and with non-printing characters replaced by hexadecimal notation:

```
"hello \n ''".dump    
"\f\x00\xff\\\"".dump 
```

Related: `String#undump` (inverse of `String#dump`).

```
VALUE
rb_str_dump(VALUE str)
{
    int encidx = rb_enc_get_index(str);
    rb_encoding *enc = rb_enc_from_index(encidx);
    long len;
    const char *p, *pend;
    char *q, *qend;
    VALUE result;
    int u8 = (encidx == rb_utf8_encindex());
    static const char nonascii_suffix[] = ".dup.force_encoding(\"%s\")";

    len = 2;                    /* "" */
    if (!rb_enc_asciicompat(enc)) {
        len += strlen(nonascii_suffix) - rb_strlen_lit("%s");
        len += strlen(enc->name);
    }

    p = RSTRING_PTR(str); pend = p + RSTRING_LEN(str);
    while (p < pend) {
        int clen;
        unsigned char c = *p++;

        switch (c) {
          case '"':  case '\\':
          case '\n': case '\r':
          case '\t': case '\f':
          case '\013': case '\010': case '\007': case '\033':
            clen = 2;
            break;

          case '#':
            clen = IS_EVSTR(p, pend) ? 2 : 1;
            break;

          default:
            if (ISPRINT(c)) {
                clen = 1;
            }
            else {
                if (u8 && c > 0x7F) {   /* \u notation */
                    int n = rb_enc_precise_mbclen(p-1, pend, enc);
                    if (MBCLEN_CHARFOUND_P(n)) {
                        unsigned int cc = rb_enc_mbc_to_codepoint(p-1, pend, enc);
                        if (cc <= 0xFFFF)
                            clen = 6;  /* \uXXXX */
                        else if (cc <= 0xFFFFF)
                            clen = 9;  /* \u{XXXXX} */
                        else
                            clen = 10; /* \u{XXXXXX} */
                        p += MBCLEN_CHARFOUND_LEN(n)-1;
                        break;
                    }
                }
                clen = 4;       /* \xNN */
            }
            break;
        }

        if (clen > LONG_MAX - len) {
            rb_raise(rb_eRuntimeError, "string size too big");
        }
        len += clen;
    }

    result = rb_str_new(0, len);
    p = RSTRING_PTR(str); pend = p + RSTRING_LEN(str);
    q = RSTRING_PTR(result); qend = q + len + 1;

    *q++ = '"';
    while (p < pend) {
        unsigned char c = *p++;

        if (c == '"' || c == '\\') {
            *q++ = '\\';
            *q++ = c;
        }
        else if (c == '#') {
            if (IS_EVSTR(p, pend)) *q++ = '\\';
            *q++ = '#';
        }
        else if (c == '\n') {
            *q++ = '\\';
            *q++ = 'n';
        }
        else if (c == '\r') {
            *q++ = '\\';
            *q++ = 'r';
        }
        else if (c == '\t') {
            *q++ = '\\';
            *q++ = 't';
        }
        else if (c == '\f') {
            *q++ = '\\';
            *q++ = 'f';
        }
        else if (c == '\013') {
            *q++ = '\\';
            *q++ = 'v';
        }
        else if (c == '\010') {
            *q++ = '\\';
            *q++ = 'b';
        }
        else if (c == '\007') {
            *q++ = '\\';
            *q++ = 'a';
        }
        else if (c == '\033') {
            *q++ = '\\';
            *q++ = 'e';
        }
        else if (ISPRINT(c)) {
            *q++ = c;
        }
        else {
            *q++ = '\\';
            if (u8) {
                int n = rb_enc_precise_mbclen(p-1, pend, enc) - 1;
                if (MBCLEN_CHARFOUND_P(n)) {
                    int cc = rb_enc_mbc_to_codepoint(p-1, pend, enc);
                    p += n;
                    if (cc <= 0xFFFF)
                        snprintf(q, qend-q, "u%04X", cc);    /* \uXXXX */
                    else
                        snprintf(q, qend-q, "u{%X}", cc);  /* \u{XXXXX} or \u{XXXXXX} */
                    q += strlen(q);
                    continue;
                }
            }
            snprintf(q, qend-q, "x%02X", c);
            q += 3;
        }
    }
    *q++ = '"';
    *q = '\0';
    if (!rb_enc_asciicompat(enc)) {
        snprintf(q, qend-q, nonascii_suffix, enc->name);
        encidx = rb_ascii8bit_encindex();
    }
    /* result from dump is ASCII */
    rb_enc_associate_index(result, encidx);
    ENC_CODERANGE_SET(result, ENC_CODERANGE_7BIT);
    return result;
}
```

each_byte {|byte| ... } → self

click to toggle source

each_byte → enumerator

Calls the given block with each successive byte from `self`; returns `self`:

```
'hello'.each_byte {|byte| print byte, ' ' }
print "\n"
'тест'.each_byte {|byte| print byte, ' ' }
print "\n"
'こんにちは'.each_byte {|byte| print byte, ' ' }
print "\n"
```

Output:

```
104 101 108 108 111
209 130 208 181 209 129 209 130
227 129 147 227 130 147 227 129 171 227 129 161 227 129 175
```

Returns an enumerator if no block is given.

```
static VALUE
rb_str_each_byte(VALUE str)
{
    RETURN_SIZED_ENUMERATOR(str, 0, 0, rb_str_each_byte_size);
    return rb_str_enumerate_bytes(str, 0);
}
```

each_char {|c| ... } → self

click to toggle source

each_char → enumerator

Calls the given block with each successive character from `self`; returns `self`:

```
'hello'.each_char {|char| print char, ' ' }
print "\n"
'тест'.each_char {|char| print char, ' ' }
print "\n"
'こんにちは'.each_char {|char| print char, ' ' }
print "\n"
```

Output:

```
h e l l o
т е с т
こ ん に ち は
```

Returns an enumerator if no block is given.

```
static VALUE
rb_str_each_char(VALUE str)
{
    RETURN_SIZED_ENUMERATOR(str, 0, 0, rb_str_each_char_size);
    return rb_str_enumerate_chars(str, 0);
}
```

each_codepoint {|integer| ... } → self

click to toggle source

each_codepoint → enumerator

Calls the given block with each successive codepoint from `self`; each codepoint is the integer value for a character; returns `self`:

```
'hello'.each_codepoint {|codepoint| print codepoint, ' ' }
print "\n"
'тест'.each_codepoint {|codepoint| print codepoint, ' ' }
print "\n"
'こんにちは'.each_codepoint {|codepoint| print codepoint, ' ' }
print "\n"
```

Output:

```
104 101 108 108 111
1090 1077 1089 1090
12371 12435 12395 12385 12399
```

Returns an enumerator if no block is given.

```
static VALUE
rb_str_each_codepoint(VALUE str)
{
    RETURN_SIZED_ENUMERATOR(str, 0, 0, rb_str_each_char_size);
    return rb_str_enumerate_codepoints(str, 0);
}
```

each_grapheme_cluster {|gc| ... } → self

click to toggle source

each_grapheme_cluster → enumerator

Calls the given block with each successive grapheme cluster from `self` (see Unicode Grapheme Cluster Boundaries); returns `self`:

```
s = "\u0061\u0308-pqr-\u0062\u0308-xyz-\u0063\u0308" 
s.each_grapheme_cluster {|gc| print gc, ' ' }
```

Output:

```
ä - p q r - b̈ - x y z - c̈
```

Returns an enumerator if no block is given.

```
static VALUE
rb_str_each_grapheme_cluster(VALUE str)
{
    RETURN_SIZED_ENUMERATOR(str, 0, 0, rb_str_each_grapheme_cluster_size);
    return rb_str_enumerate_grapheme_clusters(str, 0);
}
```

each_line(line_sep = $/, chomp: false) {|substring| ... } → self

click to toggle source

each_line(line_sep = $/, chomp: false) → enumerator

With a block given, forms the substrings (“lines”) that are the result of splitting `self` at each occurrence of the given line separator `line_sep`; passes each line to the block; returns `self`:

```
s = <<~EOT
This is the first line.
This is line two.

This is line four.
This is line five.
EOT

s.each_line {|line| p line }
```

Output:

```
"This is the first line.\n"
"This is line two.\n"
"\n"
"This is line four.\n"
"This is line five.\n"
```

With a different `line_sep`:

```
s.each_line(' is ') {|line| p line }
```

Output:

```
"This is "
"the first line.\nThis is "
"line two.\n\nThis is "
"line four.\nThis is "
"line five.\n"
```

With `chomp` as `true`, removes the trailing `line_sep` from each line:

```
s.each_line(chomp: true) {|line| p line }
```

Output:

```
"This is the first line."
"This is line two."
""
"This is line four."
"This is line five."
```

With an empty string as `line_sep`, forms and passes “paragraphs” by splitting at each occurrence of two or more newlines:

```
s.each_line('') {|line| p line }
```

Output:

```
"This is the first line.\nThis is line two.\n\n"
"This is line four.\nThis is line five.\n"
```

With no block given, returns an enumerator.

```
static VALUE
rb_str_each_line(int argc, VALUE *argv, VALUE str)
{
    RETURN_SIZED_ENUMERATOR(str, argc, argv, 0);
    return rb_str_enumerate_lines(argc, argv, str, 0);
}
```

empty? → true or false

click to toggle source

Returns `true` if the length of `self` is zero, `false` otherwise:

```
"hello".empty? 
" ".empty? 
"".empty? 
```

```
static VALUE
rb_str_empty(VALUE str)
{
    return RBOOL(RSTRING_LEN(str) == 0);
}
```

encode(dst_encoding = Encoding.default_internal, **enc_opts) → string

click to toggle source

encode(dst_encoding, src_encoding, **enc_opts) → string

Returns a copy of `self` transcoded as determined by `dst_encoding`. By default, raises an exception if `self` contains an invalid byte or a character not defined in `dst_encoding`; that behavior may be modified by encoding options; see below.

With no arguments:

- Uses the same encoding if `Encoding.default_internal` is `nil` (the default):
  ```
Encoding.default_internal 
s = "Ruby\x99".force_encoding('Windows-1252')
s.encoding                
s.bytes                   
t = s.encode              
t.encoding                
t.bytes                   
  ```
- Otherwise, uses the encoding `Encoding.default_internal`:
  ```
Encoding.default_internal = 'UTF-8'
t = s.encode              
t.encoding                
  ```

With only argument `dst_encoding` given, uses that encoding:

```
s = "Ruby\x99".force_encoding('Windows-1252')
s.encoding            
t = s.encode('UTF-8') 
t.encoding            
```

With arguments `dst_encoding` and `src_encoding` given, interprets `self` using `src_encoding`, encodes the new string using `dst_encoding`:

```
s = "Ruby\x99"
t = s.encode('UTF-8', 'Windows-1252') 
t.encoding                            
```

Optional keyword arguments `enc_opts` specify encoding options; see Encoding Options.

Please note that, unless `invalid: :replace` option is given, conversion from an encoding `enc` to the same encoding `enc` (independent of whether `enc` is given explicitly or implicitly) is a no-op, i.e. the string is simply copied without any changes, and no exceptions are raised, even if there are invalid bytes.

```
static VALUE
str_encode(int argc, VALUE *argv, VALUE str)
{
    VALUE newstr = str;
    int encidx = str_transcode(argc, argv, &newstr);
    return encoded_dup(newstr, str, encidx);
}
```

encode!(dst_encoding = Encoding.default_internal, **enc_opts) → self

click to toggle source

encode!(dst_encoding, src_encoding, **enc_opts) → self

Like `encode`, but applies encoding changes to `self`; returns `self`.

```
static VALUE
str_encode_bang(int argc, VALUE *argv, VALUE str)
{
    VALUE newstr;
    int encidx;

    rb_check_frozen(str);

    newstr = str;
    encidx = str_transcode(argc, argv, &newstr);

    if (encidx < 0) return str;
    if (newstr == str) {
        rb_enc_associate_index(str, encidx);
        return str;
    }
    rb_str_shared_replace(str, newstr);
    return str_encode_associate(str, encidx);
}
```

encoding → encoding

click to toggle source

Returns the `Encoding` object that represents the encoding of obj.

```
VALUE
rb_obj_encoding(VALUE obj)
{
    int idx = rb_enc_get_index(obj);
    if (idx < 0) {
        rb_raise(rb_eTypeError, "unknown encoding");
    }
    return rb_enc_from_encoding_index(idx & ENC_INDEX_MASK);
}
```

end_with?(*strings) → true or false

click to toggle source

Returns whether `self` ends with any of the given `strings`.

Returns `true` if any given string matches the end, `false` otherwise:

```
'hello'.end_with?('ello')               
'hello'.end_with?('heaven', 'ello')     
'hello'.end_with?('heaven', 'paradise') 
'тест'.end_with?('т')                   
'こんにちは'.end_with?('は')              
```

Related: `String#start_with?`.

```
static VALUE
rb_str_end_with(int argc, VALUE *argv, VALUE str)
{
    int i;

    for (i=0; i<argc; i++) {
        VALUE tmp = argv[i];
        const char *p, *s, *e;
        long slen, tlen;
        rb_encoding *enc;

        StringValue(tmp);
        enc = rb_enc_check(str, tmp);
        if ((tlen = RSTRING_LEN(tmp)) == 0) return Qtrue;
        if ((slen = RSTRING_LEN(str)) < tlen) continue;
        p = RSTRING_PTR(str);
        e = p + slen;
        s = e - tlen;
        if (!at_char_boundary(p, s, e, enc))
            continue;
        if (memcmp(s, RSTRING_PTR(tmp), tlen) == 0)
            return Qtrue;
    }
    return Qfalse;
}
```

eql?(object) → true or false

click to toggle source

Returns `true` if `object` has the same length and content; as `self`; `false` otherwise:

```
s = 'foo'
s.eql?('foo') 
s.eql?('food') 
s.eql?('FOO') 
```

Returns `false` if the two strings’ encodings are not compatible:

```
"\u{e4 f6 fc}".encode("ISO-8859-1").eql?("\u{c4 d6 dc}") 
```

```
VALUE
rb_str_eql(VALUE str1, VALUE str2)
{
    if (str1 == str2) return Qtrue;
    if (!RB_TYPE_P(str2, T_STRING)) return Qfalse;
    return rb_str_eql_internal(str1, str2);
}
```

force_encoding(encoding) → self

click to toggle source

Changes the encoding of `self` to `encoding`, which may be a string encoding name or an `Encoding` object; returns self:

```
s = 'łał'
s.bytes                   
s.encoding                
s.force_encoding('ascii') 
s.encoding                
```

Does not change the underlying bytes:

```
s.bytes                   
```

Makes the change even if the given `encoding` is invalid for `self` (as is the change above):

```
s.valid_encoding?                 
s.force_encoding(Encoding::UTF_8) 
s.valid_encoding?                 
```

```
static VALUE
rb_str_force_encoding(VALUE str, VALUE enc)
{
    str_modifiable(str);

    rb_encoding *encoding = rb_to_encoding(enc);
    int idx = rb_enc_to_index(encoding);

    // If the encoding is unchanged, we do nothing.
    if (ENCODING_GET(str) == idx) {
        return str;
    }

    rb_enc_associate_index(str, idx);

    // If the coderange was 7bit and the new encoding is ASCII-compatible
    // we can keep the coderange.
    if (ENC_CODERANGE(str) == ENC_CODERANGE_7BIT && encoding && rb_enc_asciicompat(encoding)) {
        return str;
    }

    ENC_CODERANGE_CLEAR(str);
    return str;
}
```

getbyte(index) → integer or nil

click to toggle source

Returns the byte at zero-based `index` as an integer, or `nil` if `index` is out of range:

```
s = 'abcde'   
s.getbyte(0)  
s.getbyte(-1) 
s.getbyte(5)  
```

Related: `String#setbyte`.

```
VALUE
rb_str_getbyte(VALUE str, VALUE index)
{
    long pos = NUM2LONG(index);

    if (pos < 0)
        pos += RSTRING_LEN(str);
    if (pos < 0 ||  RSTRING_LEN(str) <= pos)
        return Qnil;

    return INT2FIX((unsigned char)RSTRING_PTR(str)[pos]);
}
```

grapheme_clusters → array_of_grapheme_clusters

click to toggle source

Returns an array of the grapheme clusters in `self` (see Unicode Grapheme Cluster Boundaries):

```
s = "\u0061\u0308-pqr-\u0062\u0308-xyz-\u0063\u0308" 
s.grapheme_clusters
```

```
static VALUE
rb_str_grapheme_clusters(VALUE str)
{
    VALUE ary = WANTARRAY("grapheme_clusters", rb_str_strlen(str));
    return rb_str_enumerate_grapheme_clusters(str, ary);
}
```

gsub(pattern, replacement) → new_string

click to toggle source

gsub(pattern) {|match| ... } → new_string

gsub(pattern) → enumerator

Returns a copy of `self` with all occurrences of the given `pattern` replaced.

See Substitution Methods.

Returns an `Enumerator` if no `replacement` and no block given.

Related: `String#sub`, `String#sub!`, `String#gsub!`.

```
static VALUE
rb_str_gsub(int argc, VALUE *argv, VALUE str)
{
    return str_gsub(argc, argv, str, 0);
}
```

gsub!(pattern, replacement) → self or nil

click to toggle source

gsub!(pattern) {|match| ... } → self or nil

gsub!(pattern) → an_enumerator

Performs the specified substring replacement(s) on `self`; returns `self` if any replacement occurred, `nil` otherwise.

See Substitution Methods.

Returns an `Enumerator` if no `replacement` and no block given.

Related: `String#sub`, `String#gsub`, `String#sub!`.

```
static VALUE
rb_str_gsub_bang(int argc, VALUE *argv, VALUE str)
{
    str_modify_keep_cr(str);
    return str_gsub(argc, argv, str, 1);
}
```

hash → integer

click to toggle source

Returns the integer hash value for `self`. The value is based on the length, content and encoding of `self`.

Related: `Object#hash`.

```
static VALUE
rb_str_hash_m(VALUE str)
{
    st_index_t hval = rb_str_hash(str);
    return ST2FIX(hval);
}
```

hex → integer

click to toggle source
