---
title: "class String (part 3/4)"
source: https://ruby-doc.org/core/String.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 3/4
---

# class String

Interprets the leading substring of `self` as a string of hexadecimal digits (with an optional sign and an optional `0x`) and returns the corresponding number; returns zero if there is no such leading substring:

```
'0x0a'.hex        
'-1234'.hex       
'0'.hex           
'non-numeric'.hex 
```

Related: `String#oct`.

```
static VALUE
rb_str_hex(VALUE str)
{
    return rb_str_to_inum(str, 16, FALSE);
}
```

include?(other_string) → true or false

click to toggle source

Returns `true` if `self` contains `other_string`, `false` otherwise:

```
s = 'foo'
s.include?('f')    
s.include?('fo')   
s.include?('food') 
```

```
VALUE
rb_str_include(VALUE str, VALUE arg)
{
    long i;

    StringValue(arg);
    i = rb_str_index(str, arg, 0);

    return RBOOL(i != -1);
}
```

index(substring, offset = 0) → integer or nil

click to toggle source

index(regexp, offset = 0) → integer or nil

Returns the integer index of the first match for the given argument, or `nil` if none found; the search of `self` is forward, and begins at position `offset` (in characters).

With string argument `substring`, returns the index of the first matching substring in `self`:

```
'foo'.index('f')         
'foo'.index('o')         
'foo'.index('oo')        
'foo'.index('ooo')       
'тест'.index('с')        
'こんにちは'.index('ち')   
```

With `Regexp` argument `regexp`, returns the index of the first match in `self`:

```
'foo'.index(/o./) 
'foo'.index(/.o/) 
```

With positive integer `offset`, begins the search at position `offset`:

```
'foo'.index('o', 1)        
'foo'.index('o', 2)        
'foo'.index('o', 3)        
'тест'.index('с', 1)       
'こんにちは'.index('ち', 2)  
```

With negative integer `offset`, selects the search position by counting backward from the end of `self`:

```
'foo'.index('o', -1)  
'foo'.index('o', -2)  
'foo'.index('o', -3)  
'foo'.index('o', -4)  
'foo'.index(/o./, -2) 
'foo'.index(/.o/, -2) 
```

Related: `String#rindex`.

```
static VALUE
rb_str_index_m(int argc, VALUE *argv, VALUE str)
{
    VALUE sub;
    VALUE initpos;
    rb_encoding *enc = STR_ENC_GET(str);
    long pos;

    if (rb_scan_args(argc, argv, "11", &sub, &initpos) == 2) {
        long slen = str_strlen(str, enc); /* str's enc */
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

    if (RB_TYPE_P(sub, T_REGEXP)) {
        pos = str_offset(RSTRING_PTR(str), RSTRING_END(str), pos,
                         enc, single_byte_optimizable(str));

        if (rb_reg_search(sub, str, pos, 0) >= 0) {
            VALUE match = rb_backref_get();
            struct re_registers *regs = RMATCH_REGS(match);
            pos = rb_str_sublen(str, BEG(0));
            return LONG2NUM(pos);
        }
    }
    else {
        StringValue(sub);
        pos = rb_str_index(str, sub, pos);
        if (pos >= 0) {
            pos = rb_str_sublen(str, pos);
            return LONG2NUM(pos);
        }
    }
    return Qnil;
}
```

initialize_copy

(other_string) -> self

click to toggle source

Replaces the contents of `self` with the contents of `other_string`:

```
s = 'foo'        
s.replace('bar') 
```

```
VALUE
rb_str_replace(VALUE str, VALUE str2)
{
    str_modifiable(str);
    if (str == str2) return str;

    StringValue(str2);
    str_discard(str);
    return str_replace(str, str2);
}
```

Also aliased as:

replace

insert(index, other_string) → self

click to toggle source

Inserts the given `other_string` into `self`; returns `self`.

If the `Integer` `index` is positive, inserts `other_string` at offset `index`:

```
'foo'.insert(1, 'bar') 
```

If the `Integer` `index` is negative, counts backward from the end of `self` and inserts `other_string` at offset `index+1` (that is, *after* `self[index]`):

```
'foo'.insert(-2, 'bar') 
```

```
static VALUE
rb_str_insert(VALUE str, VALUE idx, VALUE str2)
{
    long pos = NUM2LONG(idx);

    if (pos == -1) {
        return rb_str_append(str, str2);
    }
    else if (pos < 0) {
        pos++;
    }
    rb_str_update(str, pos, 0, str2);
    return str;
}
```

inspect → string

click to toggle source

Returns a printable version of `self`, enclosed in double-quotes, and with special characters escaped:

```
s = "foo\tbar\tbaz\n"
s.inspect
```

```
VALUE
rb_str_inspect(VALUE str)
{
    int encidx = ENCODING_GET(str);
    rb_encoding *enc = rb_enc_from_index(encidx);
    const char *p, *pend, *prev;
    char buf[CHAR_ESC_LEN + 1];
    VALUE result = rb_str_buf_new(0);
    rb_encoding *resenc = rb_default_internal_encoding();
    int unicode_p = rb_enc_unicode_p(enc);
    int asciicompat = rb_enc_asciicompat(enc);

    if (resenc == NULL) resenc = rb_default_external_encoding();
    if (!rb_enc_asciicompat(resenc)) resenc = rb_usascii_encoding();
    rb_enc_associate(result, resenc);
    str_buf_cat2(result, "\"");

    p = RSTRING_PTR(str); pend = RSTRING_END(str);
    prev = p;
    while (p < pend) {
        unsigned int c, cc;
        int n;

        n = rb_enc_precise_mbclen(p, pend, enc);
        if (!MBCLEN_CHARFOUND_P(n)) {
            if (p > prev) str_buf_cat(result, prev, p - prev);
            n = rb_enc_mbminlen(enc);
            if (pend < p + n)
                n = (int)(pend - p);
            while (n--) {
                snprintf(buf, CHAR_ESC_LEN, "\\x%02X", *p & 0377);
                str_buf_cat(result, buf, strlen(buf));
                prev = ++p;
            }
            continue;
        }
        n = MBCLEN_CHARFOUND_LEN(n);
        c = rb_enc_mbc_to_codepoint(p, pend, enc);
        p += n;
        if ((asciicompat || unicode_p) &&
          (c == '"'|| c == '\\' ||
            (c == '#' &&
             p < pend &&
             MBCLEN_CHARFOUND_P(rb_enc_precise_mbclen(p,pend,enc)) &&
             (cc = rb_enc_codepoint(p,pend,enc),
              (cc == '$' || cc == '@' || cc == '{'))))) {
            if (p - n > prev) str_buf_cat(result, prev, p - n - prev);
            str_buf_cat2(result, "\\");
            if (asciicompat || enc == resenc) {
                prev = p - n;
                continue;
            }
        }
        switch (c) {
          case '\n': cc = 'n'; break;
          case '\r': cc = 'r'; break;
          case '\t': cc = 't'; break;
          case '\f': cc = 'f'; break;
          case '\013': cc = 'v'; break;
          case '\010': cc = 'b'; break;
          case '\007': cc = 'a'; break;
          case 033: cc = 'e'; break;
          default: cc = 0; break;
        }
        if (cc) {
            if (p - n > prev) str_buf_cat(result, prev, p - n - prev);
            buf[0] = '\\';
            buf[1] = (char)cc;
            str_buf_cat(result, buf, 2);
            prev = p;
            continue;
        }
        /* The special casing of 0x85 (NEXT_LINE) here is because
         * Oniguruma historically treats it as printable, but it
         * doesn't match the print POSIX bracket class or character
         * property in regexps.
         *
         * See Ruby Bug #16842 for details:
         * https://bugs.ruby-lang.org/issues/16842
         */
        if ((enc == resenc && rb_enc_isprint(c, enc) && c != 0x85) ||
            (asciicompat && rb_enc_isascii(c, enc) && ISPRINT(c))) {
            continue;
        }
        else {
            if (p - n > prev) str_buf_cat(result, prev, p - n - prev);
            rb_str_buf_cat_escaped_char(result, c, unicode_p);
            prev = p;
            continue;
        }
    }
    if (p > prev) str_buf_cat(result, prev, p - prev);
    str_buf_cat2(result, "\"");

    return result;
}
```

intern → symbol

click to toggle source

Returns the `Symbol` corresponding to *str*, creating the symbol if it did not previously exist. See `Symbol#id2name`.

```
"Koala".intern         
s = 'cat'.to_sym       
s == :cat              
s = '@cat'.to_sym      
s == :@cat             
```

This can also be used to create symbols that cannot be represented using the `:xxx` notation.

```
'cat and dog'.to_sym   
```

```
VALUE
rb_str_intern(VALUE str)
{
    VALUE sym;

    GLOBAL_SYMBOLS_ENTER(symbols);
    {
        sym = lookup_str_sym_with_lock(symbols, str);

        if (sym) {
            // ok
        }
        else if (USE_SYMBOL_GC) {
            rb_encoding *enc = rb_enc_get(str);
            rb_encoding *ascii = rb_usascii_encoding();
            if (enc != ascii && sym_check_asciionly(str, false)) {
                str = rb_str_dup(str);
                rb_enc_associate(str, ascii);
                OBJ_FREEZE(str);
                enc = ascii;
            }
            else {
                str = rb_str_dup(str);
                OBJ_FREEZE(str);
            }
            str = rb_fstring(str);
            int type = rb_str_symname_type(str, IDSET_ATTRSET_FOR_INTERN);
            if (type < 0) type = ID_JUNK;
            sym = dsymbol_alloc(symbols, rb_cSymbol, str, enc, type);
        }
        else {
            ID id = intern_str(str, 0);
            sym = ID2SYM(id);
        }
    }
    GLOBAL_SYMBOLS_LEAVE();
    return sym;
}
```

Also aliased as:

to_sym

length → integer

click to toggle source

Returns the count of characters (not bytes) in `self`:

```
'foo'.length        
'тест'.length       
'こんにちは'.length   
```

Contrast with `String#bytesize`:

```
'foo'.bytesize        
'тест'.bytesize       
'こんにちは'.bytesize   
```

```
VALUE
rb_str_length(VALUE str)
{
    return LONG2NUM(str_strlen(str, NULL));
}
```

Also aliased as:

size

lines(Line_sep = $/, chomp: false) → array_of_strings

click to toggle source

Forms substrings (“lines”) of `self` according to the given arguments (see `String#each_line` for details); returns the lines in an array.

```
static VALUE
rb_str_lines(int argc, VALUE *argv, VALUE str)
{
    VALUE ary = WANTARRAY("lines", 0);
    return rb_str_enumerate_lines(argc, argv, str, ary);
}
```

ljust(size, pad_string = ' ') → new_string

click to toggle source

Returns a left-justified copy of `self`.

If integer argument `size` is greater than the size (in characters) of `self`, returns a new string of length `size` that is a copy of `self`, left justified and padded on the right with `pad_string`:

```
'hello'.ljust(10)       
'  hello'.ljust(10)     
'hello'.ljust(10, 'ab') 
'тест'.ljust(10)        
'こんにちは'.ljust(10)    
```

If `size` is not greater than the size of `self`, returns a copy of `self`:

```
'hello'.ljust(5)  
'hello'.ljust(1)  
```

Related: `String#rjust`, `String#center`.

```
static VALUE
rb_str_ljust(int argc, VALUE *argv, VALUE str)
{
    return rb_str_justify(argc, argv, str, 'l');
}
```

lstrip → new_string

click to toggle source

Returns a copy of `self` with leading whitespace removed; see Whitespace in Strings:

```
whitespace = "\x00\t\n\v\f\r "
s = whitespace + 'abc' + whitespace
s        
s.lstrip 
```

Related: `String#rstrip`, `String#strip`.

```
static VALUE
rb_str_lstrip(VALUE str)
{
    char *start;
    long len, loffset;
    RSTRING_GETMEM(str, start, len);
    loffset = lstrip_offset(str, start, start+len, STR_ENC_GET(str));
    if (loffset <= 0) return str_duplicate(rb_cString, str);
    return rb_str_subseq(str, loffset, len - loffset);
}
```

lstrip! → self or nil

click to toggle source

Like `String#lstrip`, except that any modifications are made in `self`; returns `self` if any modification are made, `nil` otherwise.

Related: `String#rstrip!`, `String#strip!`.

```
static VALUE
rb_str_lstrip_bang(VALUE str)
{
    rb_encoding *enc;
    char *start, *s;
    long olen, loffset;

    str_modify_keep_cr(str);
    enc = STR_ENC_GET(str);
    RSTRING_GETMEM(str, start, olen);
    loffset = lstrip_offset(str, start, start+olen, enc);
    if (loffset > 0) {
        long len = olen-loffset;
        s = start + loffset;
        memmove(start, s, len);
        STR_SET_LEN(str, len);
        TERM_FILL(start+len, rb_enc_mbminlen(enc));
        return str;
    }
    return Qnil;
}
```

match(pattern, offset = 0) → matchdata or nil

click to toggle source

match(pattern, offset = 0) {|matchdata| ... } → object

Returns a `MatchData` object (or `nil`) based on `self` and the given `pattern`.

Note: also updates Global Variables at `Regexp`.

- Computes `regexp` by converting `pattern` (if not already a `Regexp`).
  ```
regexp = Regexp.new(pattern)
  ```
- Computes `matchdata`, which will be either a `MatchData` object or `nil` (see `Regexp#match`):
  ```
matchdata = <tt>regexp.match(self)
  ```

With no block given, returns the computed `matchdata`:

```
'foo'.match('f') 
'foo'.match('o') 
'foo'.match('x') 
```

If `Integer` argument `offset` is given, the search begins at index `offset`:

```
'foo'.match('f', 1) 
'foo'.match('o', 1) 
```

With a block given, calls the block with the computed `matchdata` and returns the block’s return value:

```
'foo'.match(/o/) {|matchdata| matchdata } 
'foo'.match(/x/) {|matchdata| matchdata } 
'foo'.match(/f/, 1) {|matchdata| matchdata } 
```

```
static VALUE
rb_str_match_m(int argc, VALUE *argv, VALUE str)
{
    VALUE re, result;
    if (argc < 1)
        rb_check_arity(argc, 1, 2);
    re = argv[0];
    argv[0] = str;
    result = rb_funcallv(get_pat(re), rb_intern("match"), argc, argv);
    if (!NIL_P(result) && rb_block_given_p()) {
        return rb_yield(result);
    }
    return result;
}
```

match?(pattern, offset = 0) → true or false

click to toggle source

Returns `true` or `false` based on whether a match is found for `self` and `pattern`.

Note: does not update Global Variables at `Regexp`.

Computes `regexp` by converting `pattern` (if not already a `Regexp`).

```
regexp = Regexp.new(pattern)
```

Returns `true` if `self+.match(regexp)` returns a `MatchData` object, `false` otherwise:

```
'foo'.match?(/o/) 
'foo'.match?('o') 
'foo'.match?(/x/) 
```

If `Integer` argument `offset` is given, the search begins at index `offset`:

```
'foo'.match?('f', 1) 
'foo'.match?('o', 1) 
```

```
static VALUE
rb_str_match_m_p(int argc, VALUE *argv, VALUE str)
{
    VALUE re;
    rb_check_arity(argc, 1, 2);
    re = get_pat(argv[0]);
    return rb_reg_match_p(re, str, argc > 1 ? NUM2LONG(argv[1]) : 0);
}
```

next

()

Returns the successor to `self`. The successor is calculated by incrementing characters.

The first character to be incremented is the rightmost alphanumeric: or, if no alphanumerics, the rightmost character:

```
'THX1138'.succ 
'<<koala>>'.succ 
'***'.succ 
```

The successor to a digit is another digit, “carrying” to the next-left character for a “rollover” from 9 to 0, and prepending another digit if necessary:

```
'00'.succ 
'09'.succ 
'99'.succ 
```

The successor to a letter is another letter of the same case, carrying to the next-left character for a rollover, and prepending another same-case letter if necessary:

```
'aa'.succ 
'az'.succ 
'zz'.succ 
'AA'.succ 
'AZ'.succ 
'ZZ'.succ 
```

The successor to a non-alphanumeric character is the next character in the underlying character set’s collating sequence, carrying to the next-left character for a rollover, and prepending another character if necessary:

```
s = 0.chr * 3
s 
s.succ 
s = 255.chr * 3
s 
s.succ 
```

Carrying can occur between and among mixtures of alphanumeric characters:

```
s = 'zz99zz99'
s.succ 
s = '99zz99zz'
s.succ 
```

The successor to an empty `String` is a new empty `String`:

```
''.succ 
```

Alias for:

succ

next!

()

Equivalent to `String#succ`, but modifies `self` in place; returns `self`.

Alias for:

succ!

oct → integer

click to toggle source

Interprets the leading substring of `self` as a string of octal digits (with an optional sign) and returns the corresponding number; returns zero if there is no such leading substring:

```
'123'.oct             
'-377'.oct            
'0377non-numeric'.oct 
'non-numeric'.oct     
```

If `self` starts with `0`, radix indicators are honored; see `Kernel#Integer`.

Related: `String#hex`.

```
static VALUE
rb_str_oct(VALUE str)
{
    return rb_str_to_inum(str, -8, FALSE);
}
```

ord → integer

click to toggle source

Returns the integer ordinal of the first character of `self`:

```
'h'.ord         
'hello'.ord     
'тест'.ord      
'こんにちは'.ord  
```

```
static VALUE
rb_str_ord(VALUE s)
{
    unsigned int c;

    c = rb_enc_codepoint(RSTRING_PTR(s), RSTRING_END(s), STR_ENC_GET(s));
    return UINT2NUM(c);
}
```

partition(string_or_regexp) → [head, match, tail]

click to toggle source

Returns a 3-element array of substrings of `self`.

Matches a pattern against `self`, scanning from the beginning. The pattern is:

- `string_or_regexp` itself, if it is a `Regexp`.
- `Regexp.quote(string_or_regexp)`, if `string_or_regexp` is a string.

If the pattern is matched, returns pre-match, first-match, post-match:

```
'hello'.partition('l')      
'hello'.partition('ll')     
'hello'.partition('h')      
'hello'.partition('o')      
'hello'.partition(/l+/)     
'hello'.partition('')       
'тест'.partition('т')       
'こんにちは'.partition('に')  
```

If the pattern is not matched, returns a copy of `self` and two empty strings:

```
'hello'.partition('x') 
```

Related: `String#rpartition`, `String#split`.

```
static VALUE
rb_str_partition(VALUE str, VALUE sep)
{
    long pos;

    sep = get_pat_quoted(sep, 0);
    if (RB_TYPE_P(sep, T_REGEXP)) {
        if (rb_reg_search(sep, str, 0, 0) < 0) {
            goto failed;
        }
        VALUE match = rb_backref_get();
        struct re_registers *regs = RMATCH_REGS(match);

        pos = BEG(0);
        sep = rb_str_subseq(str, pos, END(0) - pos);
    }
    else {
        pos = rb_str_index(str, sep, 0);
        if (pos < 0) goto failed;
    }
    return rb_ary_new3(3, rb_str_subseq(str, 0, pos),
                          sep,
                          rb_str_subseq(str, pos+RSTRING_LEN(sep),
                                             RSTRING_LEN(str)-pos-RSTRING_LEN(sep)));

  failed:
    return rb_ary_new3(3, str_duplicate(rb_cString, str), str_new_empty_String(str), str_new_empty_String(str));
}
```

prepend(*other_strings) → string

click to toggle source

Prepends each string in `other_strings` to `self` and returns `self`:

```
s = 'foo'
s.prepend('bar', 'baz') 
s                       
```

Related: `String#concat`.

```
static VALUE
rb_str_prepend_multi(int argc, VALUE *argv, VALUE str)
{
    str_modifiable(str);

    if (argc == 1) {
        rb_str_update(str, 0L, 0L, argv[0]);
    }
    else if (argc > 1) {
        int i;
        VALUE arg_str = rb_str_tmp_new(0);
        rb_enc_copy(arg_str, str);
        for (i = 0; i < argc; i++) {
            rb_str_append(arg_str, argv[i]);
        }
        rb_str_update(str, 0L, 0L, arg_str);
    }

    return str;
}
```

replace(other_string) → self

Replaces the contents of `self` with the contents of `other_string`:

```
s = 'foo'        
s.replace('bar') 
```

Alias for:

initialize_copy

reverse → string

click to toggle source

Returns a new string with the characters from `self` in reverse order.

```
'stressed'.reverse 
```

```
static VALUE
rb_str_reverse(VALUE str)
{
    rb_encoding *enc;
    VALUE rev;
    char *s, *e, *p;
    int cr;

    if (RSTRING_LEN(str) <= 1) return str_duplicate(rb_cString, str);
    enc = STR_ENC_GET(str);
    rev = rb_str_new(0, RSTRING_LEN(str));
    s = RSTRING_PTR(str); e = RSTRING_END(str);
    p = RSTRING_END(rev);
    cr = ENC_CODERANGE(str);

    if (RSTRING_LEN(str) > 1) {
        if (single_byte_optimizable(str)) {
            while (s < e) {
                *--p = *s++;
            }
        }
        else if (cr == ENC_CODERANGE_VALID) {
            while (s < e) {
                int clen = rb_enc_fast_mbclen(s, e, enc);

                p -= clen;
                memcpy(p, s, clen);
                s += clen;
            }
        }
        else {
            cr = rb_enc_asciicompat(enc) ?
                ENC_CODERANGE_7BIT : ENC_CODERANGE_VALID;
            while (s < e) {
                int clen = rb_enc_mbclen(s, e, enc);

                if (clen > 1 || (*s & 0x80)) cr = ENC_CODERANGE_UNKNOWN;
                p -= clen;
                memcpy(p, s, clen);
                s += clen;
            }
        }
    }
    STR_SET_LEN(rev, RSTRING_LEN(str));
    str_enc_copy_direct(rev, str);
    ENC_CODERANGE_SET(rev, cr);

    return rev;
}
```

reverse! → self

click to toggle source

Returns `self` with its characters reversed:

```
s = 'stressed'
s.reverse! 
s          
```

```
static VALUE
rb_str_reverse_bang(VALUE str)
{
    if (RSTRING_LEN(str) > 1) {
        if (single_byte_optimizable(str)) {
            char *s, *e, c;

            str_modify_keep_cr(str);
            s = RSTRING_PTR(str);
            e = RSTRING_END(str) - 1;
            while (s < e) {
                c = *s;
                *s++ = *e;
                *e-- = c;
            }
        }
        else {
            str_shared_replace(str, rb_str_reverse(str));
        }
    }
    else {
        str_modify_keep_cr(str);
    }
    return str;
}
```

rindex(substring, offset = self.length) → integer or nil

click to toggle source

rindex(regexp, offset = self.length) → integer or nil

Returns the `Integer` index of the *last* occurrence of the given `substring`, or `nil` if none found:

```
'foo'.rindex('f') 
'foo'.rindex('o') 
'foo'.rindex('oo') 
'foo'.rindex('ooo') 
```

Returns the `Integer` index of the *last* match for the given `Regexp` `regexp`, or `nil` if none found:

```
'foo'.rindex(/f/) 
'foo'.rindex(/o/) 
'foo'.rindex(/oo/) 
'foo'.rindex(/ooo/) 
```

The *last* match means starting at the possible last position, not the last of longest matches.

```
'foo'.rindex(/o+/) 
$~ 
```

To get the last longest match, needs to combine with negative lookbehind.

```
'foo'.rindex(/(?<!o)o+/) 
$~ 
```

Or `String#index` with negative lookforward.

```
'foo'.index(/o+(?!.*o)/) 
$~ 
```

`Integer` argument `offset`, if given and non-negative, specifies the maximum starting position in the string to *end* the search:

```
'foo'.rindex('o', 0) 
'foo'.rindex('o', 1) 
'foo'.rindex('o', 2) 
'foo'.rindex('o', 3) 
```

If `offset` is a negative `Integer`, the maximum starting position in the string to *end* the search is the sum of the string’s length and `offset`:

```
'foo'.rindex('o', -1) 
'foo'.rindex('o', -2) 
'foo'.rindex('o', -3) 
'foo'.rindex('o', -4) 
```

Related: `String#index`.

```
static VALUE
rb_str_rindex_m(int argc, VALUE *argv, VALUE str)
{
    VALUE sub;
    VALUE initpos;
    rb_encoding *enc = STR_ENC_GET(str);
    long pos, len = str_strlen(str, enc); /* str's enc */

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

    if (RB_TYPE_P(sub, T_REGEXP)) {
        /* enc = rb_enc_check(str, sub); */
        pos = str_offset(RSTRING_PTR(str), RSTRING_END(str), pos,
                         enc, single_byte_optimizable(str));

        if (rb_reg_search(sub, str, pos, 1) >= 0) {
            VALUE match = rb_backref_get();
            struct re_registers *regs = RMATCH_REGS(match);
            pos = rb_str_sublen(str, BEG(0));
            return LONG2NUM(pos);
        }
    }
    else {
        StringValue(sub);
        pos = rb_str_rindex(str, sub, pos);
        if (pos >= 0) {
            pos = rb_str_sublen(str, pos);
            return LONG2NUM(pos);
        }
    }
    return Qnil;
}
```

rjust(size, pad_string = ' ') → new_string

click to toggle source

Returns a right-justified copy of `self`.

If integer argument `size` is greater than the size (in characters) of `self`, returns a new string of length `size` that is a copy of `self`, right justified and padded on the left with `pad_string`:

```
'hello'.rjust(10)       
'hello  '.rjust(10)     
'hello'.rjust(10, 'ab') 
'тест'.rjust(10)        
'こんにちは'.rjust(10)    
```

If `size` is not greater than the size of `self`, returns a copy of `self`:

```
'hello'.rjust(5, 'ab')  
'hello'.rjust(1, 'ab')  
```

Related: `String#ljust`, `String#center`.

```
static VALUE
rb_str_rjust(int argc, VALUE *argv, VALUE str)
{
    return rb_str_justify(argc, argv, str, 'r');
}
```

rpartition(sep) → [head, match, tail]

click to toggle source

Returns a 3-element array of substrings of `self`.

Matches a pattern against `self`, scanning backwards from the end. The pattern is:

- `string_or_regexp` itself, if it is a `Regexp`.
- `Regexp.quote(string_or_regexp)`, if `string_or_regexp` is a string.

If the pattern is matched, returns pre-match, last-match, post-match:

```
'hello'.rpartition('l')      
'hello'.rpartition('ll')     
'hello'.rpartition('h')      
'hello'.rpartition('o')      
'hello'.rpartition(/l+/)     
'hello'.rpartition('')       
'тест'.rpartition('т')       
'こんにちは'.rpartition('に')  
```

If the pattern is not matched, returns two empty strings and a copy of `self`:

```
'hello'.rpartition('x') 
```

Related: `String#partition`, `String#split`.

```
static VALUE
rb_str_rpartition(VALUE str, VALUE sep)
{
    long pos = RSTRING_LEN(str);

    sep = get_pat_quoted(sep, 0);
    if (RB_TYPE_P(sep, T_REGEXP)) {
        if (rb_reg_search(sep, str, pos, 1) < 0) {
            goto failed;
        }
        VALUE match = rb_backref_get();
        struct re_registers *regs = RMATCH_REGS(match);

        pos = BEG(0);
        sep = rb_str_subseq(str, pos, END(0) - pos);
    }
    else {
        pos = rb_str_sublen(str, pos);
        pos = rb_str_rindex(str, sep, pos);
        if (pos < 0) {
            goto failed;
        }
    }

    return rb_ary_new3(3, rb_str_subseq(str, 0, pos),
                          sep,
                          rb_str_subseq(str, pos+RSTRING_LEN(sep),
                                        RSTRING_LEN(str)-pos-RSTRING_LEN(sep)));
  failed:
    return rb_ary_new3(3, str_new_empty_String(str), str_new_empty_String(str), str_duplicate(rb_cString, str));
}
```

rstrip → new_string

click to toggle source

Returns a copy of the receiver with trailing whitespace removed; see Whitespace in Strings:

```
whitespace = "\x00\t\n\v\f\r "
s = whitespace + 'abc' + whitespace
s        
s.rstrip 
```

Related: `String#lstrip`, `String#strip`.

```
static VALUE
rb_str_rstrip(VALUE str)
{
    rb_encoding *enc;
    char *start;
    long olen, roffset;

    enc = STR_ENC_GET(str);
    RSTRING_GETMEM(str, start, olen);
    roffset = rstrip_offset(str, start, start+olen, enc);

    if (roffset <= 0) return str_duplicate(rb_cString, str);
    return rb_str_subseq(str, 0, olen-roffset);
}
```

rstrip! → self or nil

click to toggle source

Like `String#rstrip`, except that any modifications are made in `self`; returns `self` if any modification are made, `nil` otherwise.

Related: `String#lstrip!`, `String#strip!`.

```
static VALUE
rb_str_rstrip_bang(VALUE str)
{
    rb_encoding *enc;
    char *start;
    long olen, roffset;

    str_modify_keep_cr(str);
    enc = STR_ENC_GET(str);
    RSTRING_GETMEM(str, start, olen);
    roffset = rstrip_offset(str, start, start+olen, enc);
    if (roffset > 0) {
        long len = olen - roffset;

        STR_SET_LEN(str, len);
        TERM_FILL(start+len, rb_enc_mbminlen(enc));
        return str;
    }
    return Qnil;
}
```

scan(string_or_regexp) → array

click to toggle source

scan(string_or_regexp) {|matches| ... } → self

Matches a pattern against `self`; the pattern is:

- `string_or_regexp` itself, if it is a `Regexp`.
- `Regexp.quote(string_or_regexp)`, if `string_or_regexp` is a string.

Iterates through `self`, generating a collection of matching results:

- If the pattern contains no groups, each result is the matched string, `$&`.
- If the pattern contains groups, each result is an array containing one entry per group.

With no block given, returns an array of the results:

```
s = 'cruel world'
s.scan(/\w+/)      
s.scan(/.../)      
s.scan(/(...)/)    
s.scan(/(..)(..)/) 
```

With a block given, calls the block with each result; returns `self`:

```
s.scan(/\w+/) {|w| print "<<#{w}>> " }
print "\n"
s.scan(/(.)(.)/) {|x,y| print y, x }
print "\n"
```

Output:

```
<<cruel>> <<world>>
rceu lowlr
```

```
static VALUE
rb_str_scan(VALUE str, VALUE pat)
{
    VALUE result;
    long start = 0;
    long last = -1, prev = 0;
    char *p = RSTRING_PTR(str); long len = RSTRING_LEN(str);

    pat = get_pat_quoted(pat, 1);
    mustnot_broken(str);
    if (!rb_block_given_p()) {
        VALUE ary = rb_ary_new();

        while (!NIL_P(result = scan_once(str, pat, &start, 0))) {
            last = prev;
            prev = start;
            rb_ary_push(ary, result);
        }
        if (last >= 0) rb_pat_search(pat, str, last, 1);
        else rb_backref_set(Qnil);
        return ary;
    }

    while (!NIL_P(result = scan_once(str, pat, &start, 1))) {
        last = prev;
        prev = start;
        rb_yield(result);
        str_mod_check(str, p, len);
    }
    if (last >= 0) rb_pat_search(pat, str, last, 1);
    return str;
}
```

scrub(replacement_string = default_replacement) → new_string

click to toggle source

scrub{|bytes| ... } → new_string

Returns a copy of `self` with each invalid byte sequence replaced by the given `replacement_string`.

With no block given and no argument, replaces each invalid sequence with the default replacement string (`"�"` for a Unicode encoding, `'?'` otherwise):

```
s = "foo\x81\x81bar"
s.scrub 
```

With no block given and argument `replacement_string` given, replaces each invalid sequence with that string:

```
"foo\x81\x81bar".scrub('xyzzy') 
```

With a block given, replaces each invalid sequence with the value of the block:

```
"foo\x81\x81bar".scrub {|bytes| p bytes; 'XYZZY' }
```

Output:

```
"\x81"
"\x81"
```

```
static VALUE
str_scrub(int argc, VALUE *argv, VALUE str)
{
    VALUE repl = argc ? (rb_check_arity(argc, 0, 1), argv[0]) : Qnil;
    VALUE new = rb_str_scrub(str, repl);
    return NIL_P(new) ? str_duplicate(rb_cString, str): new;
}
```

scrub! → self

click to toggle source

scrub!(replacement_string = default_replacement) → self

scrub!{|bytes| ... } → self

Like `String#scrub`, except that any replacements are made in `self`.

```
static VALUE
str_scrub_bang(int argc, VALUE *argv, VALUE str)
{
    VALUE repl = argc ? (rb_check_arity(argc, 0, 1), argv[0]) : Qnil;
    VALUE new = rb_str_scrub(str, repl);
    if (!NIL_P(new)) rb_str_replace(str, new);
    return str;
}
```

setbyte(index, integer) → integer

click to toggle source

Sets the byte at zero-based `index` to `integer`; returns `integer`:

```
s = 'abcde'      
s.setbyte(0, 98) 
s                
```

Related: `String#getbyte`.

```
VALUE
rb_str_setbyte(VALUE str, VALUE index, VALUE value)
{
    long pos = NUM2LONG(index);
    long len = RSTRING_LEN(str);
    char *ptr, *head, *left = 0;
    rb_encoding *enc;
    int cr = ENC_CODERANGE_UNKNOWN, width, nlen;

    if (pos < -len || len <= pos)
        rb_raise(rb_eIndexError, "index %ld out of string", pos);
    if (pos < 0)
        pos += len;

    VALUE v = rb_to_int(value);
    VALUE w = rb_int_and(v, INT2FIX(0xff));
    char byte = (char)(NUM2INT(w) & 0xFF);

    if (!str_independent(str))
        str_make_independent(str);
    enc = STR_ENC_GET(str);
    head = RSTRING_PTR(str);
    ptr = &head[pos];
    if (!STR_EMBED_P(str)) {
        cr = ENC_CODERANGE(str);
        switch (cr) {
          case ENC_CODERANGE_7BIT:
            left = ptr;
            *ptr = byte;
            if (ISASCII(byte)) goto end;
            nlen = rb_enc_precise_mbclen(left, head+len, enc);
            if (!MBCLEN_CHARFOUND_P(nlen))
                ENC_CODERANGE_SET(str, ENC_CODERANGE_BROKEN);
            else
                ENC_CODERANGE_SET(str, ENC_CODERANGE_VALID);
            goto end;
          case ENC_CODERANGE_VALID:
            left = rb_enc_left_char_head(head, ptr, head+len, enc);
            width = rb_enc_precise_mbclen(left, head+len, enc);
            *ptr = byte;
            nlen = rb_enc_precise_mbclen(left, head+len, enc);
            if (!MBCLEN_CHARFOUND_P(nlen))
                ENC_CODERANGE_SET(str, ENC_CODERANGE_BROKEN);
            else if (MBCLEN_CHARFOUND_LEN(nlen) != width || ISASCII(byte))
                ENC_CODERANGE_CLEAR(str);
            goto end;
        }
    }
    ENC_CODERANGE_CLEAR(str);
    *ptr = byte;

  end:
    return value;
}
```

size

()

Returns the count of characters (not bytes) in `self`:

```
'foo'.length        
'тест'.length       
'こんにちは'.length   
```

Contrast with `String#bytesize`:

```
'foo'.bytesize        
'тест'.bytesize       
'こんにちは'.bytesize   
```

Alias for:

length

slice

(*args)

Returns the substring of `self` specified by the arguments. See examples at String Slices.

Alias for:

[]

slice!(index) → new_string or nil

click to toggle source

slice!(start, length) → new_string or nil

slice!(range) → new_string or nil

slice!(regexp, capture = 0) → new_string or nil

slice!(substring) → new_string or nil

Removes and returns the substring of `self` specified by the arguments. See String Slices.

A few examples:

```
string = "This is a string"
string.slice!(2)        
string.slice!(3..6)     
string.slice!(/s.*t/)   
string.slice!("r")      
string                  
```

```
static VALUE
rb_str_slice_bang(int argc, VALUE *argv, VALUE str)
{
    VALUE result = Qnil;
    VALUE indx;
    long beg, len = 1;
    char *p;

    rb_check_arity(argc, 1, 2);
    str_modify_keep_cr(str);
    indx = argv[0];
    if (RB_TYPE_P(indx, T_REGEXP)) {
        if (rb_reg_search(indx, str, 0, 0) < 0) return Qnil;
        VALUE match = rb_backref_get();
        struct re_registers *regs = RMATCH_REGS(match);
        int nth = 0;
        if (argc > 1 && (nth = rb_reg_backref_number(match, argv[1])) < 0) {
            if ((nth += regs->num_regs) <= 0) return Qnil;
        }
        else if (nth >= regs->num_regs) return Qnil;
        beg = BEG(nth);
        len = END(nth) - beg;
        goto subseq;
    }
    else if (argc == 2) {
        beg = NUM2LONG(indx);
        len = NUM2LONG(argv[1]);
        goto num_index;
    }
    else if (FIXNUM_P(indx)) {
        beg = FIX2LONG(indx);
        if (!(p = rb_str_subpos(str, beg, &len))) return Qnil;
        if (!len) return Qnil;
        beg = p - RSTRING_PTR(str);
        goto subseq;
    }
    else if (RB_TYPE_P(indx, T_STRING)) {
        beg = rb_str_index(str, indx, 0);
        if (beg == -1) return Qnil;
        len = RSTRING_LEN(indx);
        result = str_duplicate(rb_cString, indx);
        goto squash;
    }
    else {
        switch (rb_range_beg_len(indx, &beg, &len, str_strlen(str, NULL), 0)) {
          case Qnil:
            return Qnil;
          case Qfalse:
            beg = NUM2LONG(indx);
            if (!(p = rb_str_subpos(str, beg, &len))) return Qnil;
            if (!len) return Qnil;
            beg = p - RSTRING_PTR(str);
            goto subseq;
          default:
            goto num_index;
        }
    }

  num_index:
    if (!(p = rb_str_subpos(str, beg, &len))) return Qnil;
    beg = p - RSTRING_PTR(str);

  subseq:
    result = rb_str_new(RSTRING_PTR(str)+beg, len);
    rb_enc_cr_str_copy_for_substr(result, str);

  squash:
    if (len > 0) {
        if (beg == 0) {
            rb_str_drop_bytes(str, len);
        }
        else {
            char *sptr = RSTRING_PTR(str);
            long slen = RSTRING_LEN(str);
            if (beg + len > slen) /* pathological check */
                len = slen - beg;
            memmove(sptr + beg,
                    sptr + beg + len,
                    slen - (beg + len));
            slen -= len;
            STR_SET_LEN(str, slen);
            TERM_FILL(&sptr[slen], TERM_LEN(str));
        }
    }
    return result;
}
```

split(field_sep = $;, limit = 0) → array

click to toggle source

split(field_sep = $;, limit = 0) {|substring| ... } → self
