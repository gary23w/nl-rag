---
title: "class String (part 4/4)"
source: https://ruby-doc.org/core/String.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 4/4
---

# class String

Returns an array of substrings of `self` that are the result of splitting `self` at each occurrence of the given field separator `field_sep`.

When `field_sep` is `$;`:

- If `$;` is `nil` (its default value), the split occurs just as if `field_sep` were given as a space character (see below).
- If `$;` is a string, the split occurs just as if `field_sep` were given as that string (see below).

When `field_sep` is `' '` and `limit` is `0` (its default value), the split occurs at each sequence of whitespace:

```
'abc def ghi'.split(' ')         => ["abc", "def", "ghi"]
"abc \n\tdef\t\n  ghi".split(' ') 
'abc  def   ghi'.split(' ')      => ["abc", "def", "ghi"]
''.split(' ')                    => []
```

When `field_sep` is a string different from `' '` and `limit` is `0`, the split occurs at each occurrence of `field_sep`; trailing empty substrings are not returned:

```
'abracadabra'.split('ab')  => ["", "racad", "ra"]
'aaabcdaaa'.split('a')     => ["", "", "", "bcd"]
''.split('a')              => []
'3.14159'.split('1')       => ["3.", "4", "59"]
'!@#$%^$&*($)_+'.split('$') 
'тест'.split('т')          => ["", "ес"]
'こんにちは'.split('に')     => ["こん", "ちは"]
```

When `field_sep` is a `Regexp` and `limit` is `0`, the split occurs at each occurrence of a match; trailing empty substrings are not returned:

```
'abracadabra'.split(/ab/) 
'aaabcdaaa'.split(/a/)   => ["", "", "", "bcd"]
'aaabcdaaa'.split(//)    => ["a", "a", "a", "b", "c", "d", "a", "a", "a"]
'1 + 1 == 2'.split(/\W+/) 
```

If the Regexp contains groups, their matches are also included in the returned array:

```
'1:2:3'.split(/(:)()()/, 2) 
```

As seen above, if `limit` is `0`, trailing empty substrings are not returned:

```
'aaabcdaaa'.split('a')   => ["", "", "", "bcd"]
```

If `limit` is positive integer `n`, no more than `n - 1-` splits occur, so that at most `n` substrings are returned, and trailing empty substrings are included:

```
'aaabcdaaa'.split('a', 1) 
'aaabcdaaa'.split('a', 2) 
'aaabcdaaa'.split('a', 5) 
'aaabcdaaa'.split('a', 7) 
'aaabcdaaa'.split('a', 8) 
```

Note that if `field_sep` is a Regexp containing groups, their matches are in the returned array, but do not count toward the limit.

If `limit` is negative, it behaves the same as if `limit` was zero, meaning that there is no limit, and trailing empty substrings are included:

```
'aaabcdaaa'.split('a', -1) 
```

If a block is given, it is called with each substring:

```
'abc def ghi'.split(' ') {|substring| p substring }
```

Output:

```
"abc"
"def"
"ghi"
```

Related: `String#partition`, `String#rpartition`.

```
static VALUE
rb_str_split_m(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    VALUE spat;
    VALUE limit;
    split_type_t split_type;
    long beg, end, i = 0, empty_count = -1;
    int lim = 0;
    VALUE result, tmp;

    result = rb_block_given_p() ? Qfalse : Qnil;
    if (rb_scan_args(argc, argv, "02", &spat, &limit) == 2) {
        lim = NUM2INT(limit);
        if (lim <= 0) limit = Qnil;
        else if (lim == 1) {
            if (RSTRING_LEN(str) == 0)
                return result ? rb_ary_new2(0) : str;
            tmp = str_duplicate(rb_cString, str);
            if (!result) {
                rb_yield(tmp);
                return str;
            }
            return rb_ary_new3(1, tmp);
        }
        i = 1;
    }
    if (NIL_P(limit) && !lim) empty_count = 0;

    enc = STR_ENC_GET(str);
    split_type = SPLIT_TYPE_REGEXP;
    if (!NIL_P(spat)) {
        spat = get_pat_quoted(spat, 0);
    }
    else if (NIL_P(spat = rb_fs)) {
        split_type = SPLIT_TYPE_AWK;
    }
    else if (!(spat = rb_fs_check(spat))) {
        rb_raise(rb_eTypeError, "value of $; must be String or Regexp");
    }
    else {
        rb_category_warn(RB_WARN_CATEGORY_DEPRECATED, "$; is set to non-nil value");
    }
    if (split_type != SPLIT_TYPE_AWK) {
        switch (BUILTIN_TYPE(spat)) {
          case T_REGEXP:
            rb_reg_options(spat); /* check if uninitialized */
            tmp = RREGEXP_SRC(spat);
            split_type = literal_split_pattern(tmp, SPLIT_TYPE_REGEXP);
            if (split_type == SPLIT_TYPE_AWK) {
                spat = tmp;
                split_type = SPLIT_TYPE_STRING;
            }
            break;

          case T_STRING:
            mustnot_broken(spat);
            split_type = literal_split_pattern(spat, SPLIT_TYPE_STRING);
            break;

          default:
            UNREACHABLE_RETURN(Qnil);
        }
    }

#define SPLIT_STR(beg, len) (empty_count = split_string(result, str, beg, len, empty_count))

    beg = 0;
    char *ptr = RSTRING_PTR(str);
    char *eptr = RSTRING_END(str);
    if (split_type == SPLIT_TYPE_AWK) {
        char *bptr = ptr;
        int skip = 1;
        unsigned int c;

        if (result) result = rb_ary_new();
        end = beg;
        if (is_ascii_string(str)) {
            while (ptr < eptr) {
                c = (unsigned char)*ptr++;
                if (skip) {
                    if (ascii_isspace(c)) {
                        beg = ptr - bptr;
                    }
                    else {
                        end = ptr - bptr;
                        skip = 0;
                        if (!NIL_P(limit) && lim <= i) break;
                    }
                }
                else if (ascii_isspace(c)) {
                    SPLIT_STR(beg, end-beg);
                    skip = 1;
                    beg = ptr - bptr;
                    if (!NIL_P(limit)) ++i;
                }
                else {
                    end = ptr - bptr;
                }
            }
        }
        else {
            while (ptr < eptr) {
                int n;

                c = rb_enc_codepoint_len(ptr, eptr, &n, enc);
                ptr += n;
                if (skip) {
                    if (rb_isspace(c)) {
                        beg = ptr - bptr;
                    }
                    else {
                        end = ptr - bptr;
                        skip = 0;
                        if (!NIL_P(limit) && lim <= i) break;
                    }
                }
                else if (rb_isspace(c)) {
                    SPLIT_STR(beg, end-beg);
                    skip = 1;
                    beg = ptr - bptr;
                    if (!NIL_P(limit)) ++i;
                }
                else {
                    end = ptr - bptr;
                }
            }
        }
    }
    else if (split_type == SPLIT_TYPE_STRING) {
        char *str_start = ptr;
        char *substr_start = ptr;
        char *sptr = RSTRING_PTR(spat);
        long slen = RSTRING_LEN(spat);

        if (result) result = rb_ary_new();
        mustnot_broken(str);
        enc = rb_enc_check(str, spat);
        while (ptr < eptr &&
               (end = rb_memsearch(sptr, slen, ptr, eptr - ptr, enc)) >= 0) {
            /* Check we are at the start of a char */
            char *t = rb_enc_right_char_head(ptr, ptr + end, eptr, enc);
            if (t != ptr + end) {
                ptr = t;
                continue;
            }
            SPLIT_STR(substr_start - str_start, (ptr+end) - substr_start);
            ptr += end + slen;
            substr_start = ptr;
            if (!NIL_P(limit) && lim <= ++i) break;
        }
        beg = ptr - str_start;
    }
    else if (split_type == SPLIT_TYPE_CHARS) {
        char *str_start = ptr;
        int n;

        if (result) result = rb_ary_new_capa(RSTRING_LEN(str));
        mustnot_broken(str);
        enc = rb_enc_get(str);
        while (ptr < eptr &&
               (n = rb_enc_precise_mbclen(ptr, eptr, enc)) > 0) {
            SPLIT_STR(ptr - str_start, n);
            ptr += n;
            if (!NIL_P(limit) && lim <= ++i) break;
        }
        beg = ptr - str_start;
    }
    else {
        if (result) result = rb_ary_new();
        long len = RSTRING_LEN(str);
        long start = beg;
        long idx;
        int last_null = 0;
        struct re_registers *regs;
        VALUE match = 0;

        for (; rb_reg_search(spat, str, start, 0) >= 0;
             (match ? (rb_match_unbusy(match), rb_backref_set(match)) : (void)0)) {
            match = rb_backref_get();
            if (!result) rb_match_busy(match);
            regs = RMATCH_REGS(match);
            end = BEG(0);
            if (start == end && BEG(0) == END(0)) {
                if (!ptr) {
                    SPLIT_STR(0, 0);
                    break;
                }
                else if (last_null == 1) {
                    SPLIT_STR(beg, rb_enc_fast_mbclen(ptr+beg, eptr, enc));
                    beg = start;
                }
                else {
                    if (start == len)
                        start++;
                    else
                        start += rb_enc_fast_mbclen(ptr+start,eptr,enc);
                    last_null = 1;
                    continue;
                }
            }
            else {
                SPLIT_STR(beg, end-beg);
                beg = start = END(0);
            }
            last_null = 0;

            for (idx=1; idx < regs->num_regs; idx++) {
                if (BEG(idx) == -1) continue;
                SPLIT_STR(BEG(idx), END(idx)-BEG(idx));
            }
            if (!NIL_P(limit) && lim <= ++i) break;
        }
        if (match) rb_match_unbusy(match);
    }
    if (RSTRING_LEN(str) > 0 && (!NIL_P(limit) || RSTRING_LEN(str) > beg || lim < 0)) {
        SPLIT_STR(beg, RSTRING_LEN(str)-beg);
    }

    return result ? result : str;
}
```

squeeze(*selectors) → new_string

click to toggle source

Returns a copy of `self` with characters specified by `selectors` “squeezed” (see Multiple Character Selectors):

“Squeezed” means that each multiple-character run of a selected character is squeezed down to a single character; with no arguments given, squeezes all characters:

```
"yellow moon".squeeze                  
"  now   is  the".squeeze(" ")         
"putters shoot balls".squeeze("m-z")   
```

```
static VALUE
rb_str_squeeze(int argc, VALUE *argv, VALUE str)
{
    str = str_duplicate(rb_cString, str);
    rb_str_squeeze_bang(argc, argv, str);
    return str;
}
```

squeeze!(*selectors) → self or nil

click to toggle source

Like `String#squeeze`, but modifies `self` in place. Returns `self` if any changes were made, `nil` otherwise.

```
static VALUE
rb_str_squeeze_bang(int argc, VALUE *argv, VALUE str)
{
    char squeez[TR_TABLE_SIZE];
    rb_encoding *enc = 0;
    VALUE del = 0, nodel = 0;
    unsigned char *s, *send, *t;
    int i, modify = 0;
    int ascompat, singlebyte = single_byte_optimizable(str);
    unsigned int save;

    if (argc == 0) {
        enc = STR_ENC_GET(str);
    }
    else {
        for (i=0; i<argc; i++) {
            VALUE s = argv[i];

            StringValue(s);
            enc = rb_enc_check(str, s);
            if (singlebyte && !single_byte_optimizable(s))
                singlebyte = 0;
            tr_setup_table(s, squeez, i==0, &del, &nodel, enc);
        }
    }

    str_modify_keep_cr(str);
    s = t = (unsigned char *)RSTRING_PTR(str);
    if (!s || RSTRING_LEN(str) == 0) return Qnil;
    send = (unsigned char *)RSTRING_END(str);
    save = -1;
    ascompat = rb_enc_asciicompat(enc);

    if (singlebyte) {
        while (s < send) {
            unsigned int c = *s++;
            if (c != save || (argc > 0 && !squeez[c])) {
                *t++ = save = c;
            }
        }
    }
    else {
        while (s < send) {
            unsigned int c;
            int clen;

            if (ascompat && (c = *s) < 0x80) {
                if (c != save || (argc > 0 && !squeez[c])) {
                    *t++ = save = c;
                }
                s++;
            }
            else {
                c = rb_enc_codepoint_len((char *)s, (char *)send, &clen, enc);

                if (c != save || (argc > 0 && !tr_find(c, squeez, del, nodel))) {
                    if (t != s) rb_enc_mbcput(c, t, enc);
                    save = c;
                    t += clen;
                }
                s += clen;
            }
        }
    }

    TERM_FILL((char *)t, TERM_LEN(str));
    if ((char *)t - RSTRING_PTR(str) != RSTRING_LEN(str)) {
        STR_SET_LEN(str, (char *)t - RSTRING_PTR(str));
        modify = 1;
    }

    if (modify) return str;
    return Qnil;
}
```

start_with?(*string_or_regexp) → true or false

click to toggle source

Returns whether `self` starts with any of the given `string_or_regexp`.

Matches patterns against the beginning of `self`. For each given `string_or_regexp`, the pattern is:

- `string_or_regexp` itself, if it is a `Regexp`.
- `Regexp.quote(string_or_regexp)`, if `string_or_regexp` is a string.

Returns `true` if any pattern matches the beginning, `false` otherwise:

```
'hello'.start_with?('hell')               
'hello'.start_with?(/H/i)                 
'hello'.start_with?('heaven', 'hell')     
'hello'.start_with?('heaven', 'paradise') 
'тест'.start_with?('т')                   
'こんにちは'.start_with?('こ')              
```

Related: `String#end_with?`.

```
static VALUE
rb_str_start_with(int argc, VALUE *argv, VALUE str)
{
    int i;

    for (i=0; i<argc; i++) {
        VALUE tmp = argv[i];
        if (RB_TYPE_P(tmp, T_REGEXP)) {
            if (rb_reg_start_with_p(tmp, str))
                return Qtrue;
        }
        else {
            const char *p, *s, *e;
            long slen, tlen;
            rb_encoding *enc;

            StringValue(tmp);
            enc = rb_enc_check(str, tmp);
            if ((tlen = RSTRING_LEN(tmp)) == 0) return Qtrue;
            if ((slen = RSTRING_LEN(str)) < tlen) continue;
            p = RSTRING_PTR(str);
            e = p + slen;
            s = p + tlen;
            if (!at_char_right_boundary(p, s, e, enc))
                continue;
            if (memcmp(p, RSTRING_PTR(tmp), tlen) == 0)
                return Qtrue;
        }
    }
    return Qfalse;
}
```

strip → new_string

click to toggle source

Returns a copy of the receiver with leading and trailing whitespace removed; see Whitespace in Strings:

```
whitespace = "\x00\t\n\v\f\r "
s = whitespace + 'abc' + whitespace
s       
s.strip 
```

Related: `String#lstrip`, `String#rstrip`.

```
static VALUE
rb_str_strip(VALUE str)
{
    char *start;
    long olen, loffset, roffset;
    rb_encoding *enc = STR_ENC_GET(str);

    RSTRING_GETMEM(str, start, olen);
    loffset = lstrip_offset(str, start, start+olen, enc);
    roffset = rstrip_offset(str, start+loffset, start+olen, enc);

    if (loffset <= 0 && roffset <= 0) return str_duplicate(rb_cString, str);
    return rb_str_subseq(str, loffset, olen-loffset-roffset);
}
```

strip! → self or nil

click to toggle source

Like `String#strip`, except that any modifications are made in `self`; returns `self` if any modification are made, `nil` otherwise.

Related: `String#lstrip!`, `String#strip!`.

```
static VALUE
rb_str_strip_bang(VALUE str)
{
    char *start;
    long olen, loffset, roffset;
    rb_encoding *enc;

    str_modify_keep_cr(str);
    enc = STR_ENC_GET(str);
    RSTRING_GETMEM(str, start, olen);
    loffset = lstrip_offset(str, start, start+olen, enc);
    roffset = rstrip_offset(str, start+loffset, start+olen, enc);

    if (loffset > 0 || roffset > 0) {
        long len = olen-roffset;
        if (loffset > 0) {
            len -= loffset;
            memmove(start, start + loffset, len);
        }
        STR_SET_LEN(str, len);
        TERM_FILL(start+len, rb_enc_mbminlen(enc));
        return str;
    }
    return Qnil;
}
```

sub(pattern, replacement) → new_string

click to toggle source

sub(pattern) {|match| ... } → new_string

Returns a copy of `self` with only the first occurrence (not all occurrences) of the given `pattern` replaced.

See Substitution Methods.

Related: `String#sub!`, `String#gsub`, `String#gsub!`.

```
static VALUE
rb_str_sub(int argc, VALUE *argv, VALUE str)
{
    str = str_duplicate(rb_cString, str);
    rb_str_sub_bang(argc, argv, str);
    return str;
}
```

sub!(pattern, replacement) → self or nil

click to toggle source

sub!(pattern) {|match| ... } → self or nil

Replaces the first occurrence (not all occurrences) of the given `pattern` on `self`; returns `self` if a replacement occurred, `nil` otherwise.

See Substitution Methods.

Related: `String#sub`, `String#gsub`, `String#gsub!`.

```
static VALUE
rb_str_sub_bang(int argc, VALUE *argv, VALUE str)
{
    VALUE pat, repl, hash = Qnil;
    int iter = 0;
    long plen;
    int min_arity = rb_block_given_p() ? 1 : 2;
    long beg;

    rb_check_arity(argc, min_arity, 2);
    if (argc == 1) {
        iter = 1;
    }
    else {
        repl = argv[1];
        hash = rb_check_hash_type(argv[1]);
        if (NIL_P(hash)) {
            StringValue(repl);
        }
    }

    pat = get_pat_quoted(argv[0], 1);

    str_modifiable(str);
    beg = rb_pat_search(pat, str, 0, 1);
    if (beg >= 0) {
        rb_encoding *enc;
        int cr = ENC_CODERANGE(str);
        long beg0, end0;
        VALUE match, match0 = Qnil;
        struct re_registers *regs;
        char *p, *rp;
        long len, rlen;

        match = rb_backref_get();
        regs = RMATCH_REGS(match);
        if (RB_TYPE_P(pat, T_STRING)) {
            beg0 = beg;
            end0 = beg0 + RSTRING_LEN(pat);
            match0 = pat;
        }
        else {
            beg0 = BEG(0);
            end0 = END(0);
            if (iter) match0 = rb_reg_nth_match(0, match);
        }

        if (iter || !NIL_P(hash)) {
            p = RSTRING_PTR(str); len = RSTRING_LEN(str);

            if (iter) {
                repl = rb_obj_as_string(rb_yield(match0));
            }
            else {
                repl = rb_hash_aref(hash, rb_str_subseq(str, beg0, end0 - beg0));
                repl = rb_obj_as_string(repl);
            }
            str_mod_check(str, p, len);
            rb_check_frozen(str);
        }
        else {
            repl = rb_reg_regsub(repl, str, regs, RB_TYPE_P(pat, T_STRING) ? Qnil : pat);
        }

        enc = rb_enc_compatible(str, repl);
        if (!enc) {
            rb_encoding *str_enc = STR_ENC_GET(str);
            p = RSTRING_PTR(str); len = RSTRING_LEN(str);
            if (coderange_scan(p, beg0, str_enc) != ENC_CODERANGE_7BIT ||
                coderange_scan(p+end0, len-end0, str_enc) != ENC_CODERANGE_7BIT) {
                rb_raise(rb_eEncCompatError, "incompatible character encodings: %s and %s",
                         rb_enc_inspect_name(str_enc),
                         rb_enc_inspect_name(STR_ENC_GET(repl)));
            }
            enc = STR_ENC_GET(repl);
        }
        rb_str_modify(str);
        rb_enc_associate(str, enc);
        if (ENC_CODERANGE_UNKNOWN < cr && cr < ENC_CODERANGE_BROKEN) {
            int cr2 = ENC_CODERANGE(repl);
            if (cr2 == ENC_CODERANGE_BROKEN ||
                (cr == ENC_CODERANGE_VALID && cr2 == ENC_CODERANGE_7BIT))
                cr = ENC_CODERANGE_UNKNOWN;
            else
                cr = cr2;
        }
        plen = end0 - beg0;
        rlen = RSTRING_LEN(repl);
        len = RSTRING_LEN(str);
        if (rlen > plen) {
            RESIZE_CAPA(str, len + rlen - plen);
        }
        p = RSTRING_PTR(str);
        if (rlen != plen) {
            memmove(p + beg0 + rlen, p + beg0 + plen, len - beg0 - plen);
        }
        rp = RSTRING_PTR(repl);
        memmove(p + beg0, rp, rlen);
        len += rlen - plen;
        STR_SET_LEN(str, len);
        TERM_FILL(&RSTRING_PTR(str)[len], TERM_LEN(str));
        ENC_CODERANGE_SET(str, cr);

        RB_GC_GUARD(match);

        return str;
    }
    return Qnil;
}
```

succ → new_str

click to toggle source

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

```
VALUE
rb_str_succ(VALUE orig)
{
    VALUE str;
    str = rb_str_new(RSTRING_PTR(orig), RSTRING_LEN(orig));
    rb_enc_cr_str_copy_for_substr(str, orig);
    return str_succ(str);
}
```

Also aliased as:

next

succ! → self

click to toggle source

Equivalent to `String#succ`, but modifies `self` in place; returns `self`.

```
static VALUE
rb_str_succ_bang(VALUE str)
{
    rb_str_modify(str);
    str_succ(str);
    return str;
}
```

Also aliased as:

next!

sum(n = 16) → integer

click to toggle source

Returns a basic `n`-bit checksum of the characters in `self`; the checksum is the sum of the binary value of each byte in `self`, modulo `2**n - 1`:

```
'hello'.sum     
'hello'.sum(4)  
'hello'.sum(64) 
'тест'.sum      
'こんにちは'.sum  
```

This is not a particularly strong checksum.

```
static VALUE
rb_str_sum(int argc, VALUE *argv, VALUE str)
{
    int bits = 16;
    char *ptr, *p, *pend;
    long len;
    VALUE sum = INT2FIX(0);
    unsigned long sum0 = 0;

    if (rb_check_arity(argc, 0, 1) && (bits = NUM2INT(argv[0])) < 0) {
        bits = 0;
    }
    ptr = p = RSTRING_PTR(str);
    len = RSTRING_LEN(str);
    pend = p + len;

    while (p < pend) {
        if (FIXNUM_MAX - UCHAR_MAX < sum0) {
            sum = rb_funcall(sum, '+', 1, LONG2FIX(sum0));
            str_mod_check(str, ptr, len);
            sum0 = 0;
        }
        sum0 += (unsigned char)*p;
        p++;
    }

    if (bits == 0) {
        if (sum0) {
            sum = rb_funcall(sum, '+', 1, LONG2FIX(sum0));
        }
    }
    else {
        if (sum == INT2FIX(0)) {
            if (bits < (int)sizeof(long)*CHAR_BIT) {
                sum0 &= (((unsigned long)1)<<bits)-1;
            }
            sum = LONG2FIX(sum0);
        }
        else {
            VALUE mod;

            if (sum0) {
                sum = rb_funcall(sum, '+', 1, LONG2FIX(sum0));
            }

            mod = rb_funcall(INT2FIX(1), idLTLT, 1, INT2FIX(bits));
            mod = rb_funcall(mod, '-', 1, INT2FIX(1));
            sum = rb_funcall(sum, '&', 1, mod);
        }
    }
    return sum;
}
```

swapcase(*options) → string

click to toggle source

Returns a string containing the characters in `self`, with cases reversed; each uppercase character is downcased; each lowercase character is upcased:

```
s = 'Hello World!' 
s.swapcase         
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#swapcase!`.

```
static VALUE
rb_str_swapcase(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_UPCASE | ONIGENC_CASE_DOWNCASE;
    VALUE ret;

    flags = check_case_options(argc, argv, flags);
    enc = str_true_enc(str);
    if (RSTRING_LEN(str) == 0 || !RSTRING_PTR(str)) return str_duplicate(rb_cString, str);
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

swapcase!(*options) → self or nil

click to toggle source

Upcases each lowercase character in `self`; downcases uppercase character; returns `self` if any changes were made, `nil` otherwise:

```
s = 'Hello World!' 
s.swapcase!        
s                  
''.swapcase!       
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#swapcase`.

```
static VALUE
rb_str_swapcase_bang(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_UPCASE | ONIGENC_CASE_DOWNCASE;

    flags = check_case_options(argc, argv, flags);
    str_modify_keep_cr(str);
    enc = str_true_enc(str);
    if (flags&ONIGENC_CASE_ASCII_ONLY)
        rb_str_ascii_casemap(str, str, &flags, enc);
    else
        str_shared_replace(str, rb_str_casemap(str, &flags, enc));

    if (ONIGENC_CASE_MODIFIED&flags) return str;
    return Qnil;
}
```

to_c → complex

click to toggle source

Returns `self` interpreted as a `Complex` object; leading whitespace and trailing garbage are ignored:

```
'9'.to_c                 
'2.5'.to_c               
'2.5/1'.to_c             
'-3/2'.to_c              
'-i'.to_c                
'45i'.to_c               
'3-4i'.to_c              
'-4e2-4e-2i'.to_c        
'-0.0-0.0i'.to_c         
'1/2+3/4i'.to_c          
'1.0@0'.to_c             
"1.0@#{Math::PI/2}".to_c 
"1.0@#{Math::PI}".to_c   
```

Returns Complex zero if the string cannot be converted:

```
'ruby'.to_c        
```

See `Kernel#Complex`.

```
static VALUE
string_to_c(VALUE self)
{
    VALUE num;

    rb_must_asciicompat(self);

    (void)parse_comp(rb_str_fill_terminator(self, 1), FALSE, &num);

    return num;
}
```

to_f → float

click to toggle source

Returns the result of interpreting leading characters in `self` as a Float:

```
'3.14159'.to_f  
'1.234e-2'.to_f 
```

Characters past a leading valid number (in the given `base`) are ignored:

```
'3.14 (pi to two places)'.to_f 
```

Returns zero if there is no leading valid number:

```
'abcdef'.to_f 
```

```
static VALUE
rb_str_to_f(VALUE str)
{
    return DBL2NUM(rb_str_to_dbl(str, FALSE));
}
```

to_i(base = 10) → integer

click to toggle source

Returns the result of interpreting leading characters in `self` as an integer in the given `base` (which must be in (0, 2..36)):

```
'123456'.to_i     
'123def'.to_i(16) 
```

With `base` zero, string `object` may contain leading characters to specify the actual base:

```
'123def'.to_i(0)   
'0123def'.to_i(0)  
'0b123def'.to_i(0) 
'0o123def'.to_i(0) 
'0d123def'.to_i(0) 
'0x123def'.to_i(0) 
```

Characters past a leading valid number (in the given `base`) are ignored:

```
'12.345'.to_i   
'12345'.to_i(2) 
```

Returns zero if there is no leading valid number:

```
'abcdef'.to_i 
'2'.to_i(2)   
```

```
static VALUE
rb_str_to_i(int argc, VALUE *argv, VALUE str)
{
    int base = 10;

    if (rb_check_arity(argc, 0, 1) && (base = NUM2INT(argv[0])) < 0) {
        rb_raise(rb_eArgError, "invalid radix %d", base);
    }
    return rb_str_to_inum(str, base, FALSE);
}
```

to_r → rational

click to toggle source

Returns the result of interpreting leading characters in `str` as a rational. Leading whitespace and extraneous characters past the end of a valid number are ignored. Digit sequences can be separated by an underscore. If there is not a valid number at the start of `str`, zero is returned. This method never raises an exception.

```
'  2  '.to_r       
'300/2'.to_r       
'-9.2'.to_r        
'-9.2e2'.to_r      
'1_234_567'.to_r   
'21 June 09'.to_r  
'21/06/09'.to_r    
'BWV 1079'.to_r    
```

NOTE: “0.3”.to_r isn’t the same as 0.3.to_r. The former is equivalent to “3/10”.to_r, but the latter isn’t so.

```
"0.3".to_r == 3/10r  
0.3.to_r   == 3/10r  
```

See also `Kernel#Rational`.

```
static VALUE
string_to_r(VALUE self)
{
    VALUE num;

    rb_must_asciicompat(self);

    num = parse_rat(RSTRING_PTR(self), RSTRING_END(self), 0, TRUE);

    if (RB_FLOAT_TYPE_P(num) && !FLOAT_ZERO_P(num))
        rb_raise(rb_eFloatDomainError, "Infinity");
    return num;
}
```

to_s → self or string

click to toggle source

Returns `self` if `self` is a `String`, or `self` converted to a `String` if `self` is a subclass of `String`.

```
static VALUE
rb_str_to_s(VALUE str)
{
    if (rb_obj_class(str) != rb_cString) {
        return str_duplicate(rb_cString, str);
    }
    return str;
}
```

Also aliased as:

to_str

to_str

()

Returns `self` if `self` is a `String`, or `self` converted to a `String` if `self` is a subclass of `String`.

Alias for:

to_s

to_sym → symbol

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

Alias for:

intern

tr(selector, replacements) → new_string

click to toggle source

Returns a copy of `self` with each character specified by string `selector` translated to the corresponding character in string `replacements`. The correspondence is *positional*:

- Each occurrence of the first character specified by `selector` is translated to the first character in `replacements`.
- Each occurrence of the second character specified by `selector` is translated to the second character in `replacements`.
- And so on.

Example:

```
'hello'.tr('el', 'ip') 
```

If `replacements` is shorter than `selector`, it is implicitly padded with its own last character:

```
'hello'.tr('aeiou', '-')   
'hello'.tr('aeiou', 'AA-') 
```

Arguments `selector` and `replacements` must be valid character selectors (see Character Selectors), and may use any of its valid forms, including negation, ranges, and escaping:

```
'hello'.tr('^aeiou', '-') 

'ibm'.tr('b-z', 'a-z') 

'hel^lo'.tr('\^aeiou', '-')     
'i-b-m'.tr('b\-z', 'a-z')       
'foo\\bar'.tr('ab\\', 'XYZ')    
```

```
static VALUE
rb_str_tr(VALUE str, VALUE src, VALUE repl)
{
    str = str_duplicate(rb_cString, str);
    tr_trans(str, src, repl, 0);
    return str;
}
```

tr!(selector, replacements) → self or nil

click to toggle source

Like `String#tr`, but modifies `self` in place. Returns `self` if any changes were made, `nil` otherwise.

```
static VALUE
rb_str_tr_bang(VALUE str, VALUE src, VALUE repl)
{
    return tr_trans(str, src, repl, 0);
}
```

tr_s(selector, replacements) → string

click to toggle source

Like `String#tr`, but also squeezes the modified portions of the translated string; returns a new string (translated and squeezed).

```
'hello'.tr_s('l', 'r')   
'hello'.tr_s('el', '-')  
'hello'.tr_s('el', 'hx') 
```

Related: `String#squeeze`.

```
static VALUE
rb_str_tr_s(VALUE str, VALUE src, VALUE repl)
{
    str = str_duplicate(rb_cString, str);
    tr_trans(str, src, repl, 1);
    return str;
}
```

tr_s!(selector, replacements) → self or nil

click to toggle source

Like `String#tr_s`, but modifies `self` in place. Returns `self` if any changes were made, `nil` otherwise.

Related: `String#squeeze!`.

```
static VALUE
rb_str_tr_s_bang(VALUE str, VALUE src, VALUE repl)
{
    return tr_trans(str, src, repl, 1);
}
```

undump → string

click to toggle source

Returns an unescaped version of `self`:

```
s_orig = "\f\x00\xff\\\""    
s_dumped = s_orig.dump       
s_undumped = s_dumped.undump 
s_undumped == s_orig         
```

Related: `String#dump` (inverse of `String#undump`).

```
static VALUE
str_undump(VALUE str)
{
    const char *s = RSTRING_PTR(str);
    const char *s_end = RSTRING_END(str);
    rb_encoding *enc = rb_enc_get(str);
    VALUE undumped = rb_enc_str_new(s, 0L, enc);
    bool utf8 = false;
    bool binary = false;
    int w;

    rb_must_asciicompat(str);
    if (rb_str_is_ascii_only_p(str) == Qfalse) {
        rb_raise(rb_eRuntimeError, "non-ASCII character detected");
    }
    if (!str_null_check(str, &w)) {
        rb_raise(rb_eRuntimeError, "string contains null byte");
    }
    if (RSTRING_LEN(str) < 2) goto invalid_format;
    if (*s != '"') goto invalid_format;

    /* strip '"' at the start */
    s++;

    for (;;) {
        if (s >= s_end) {
            rb_raise(rb_eRuntimeError, "unterminated dumped string");
        }

        if (*s == '"') {
            /* epilogue */
            s++;
            if (s == s_end) {
                /* ascii compatible dumped string */
                break;
            }
            else {
                static const char force_encoding_suffix[] = ".force_encoding(\""; /* "\")" */
                static const char dup_suffix[] = ".dup";
                const char *encname;
                int encidx;
                ptrdiff_t size;

                /* check separately for strings dumped by older versions */
                size = sizeof(dup_suffix) - 1;
                if (s_end - s > size && memcmp(s, dup_suffix, size) == 0) s += size;

                size = sizeof(force_encoding_suffix) - 1;
                if (s_end - s <= size) goto invalid_format;
                if (memcmp(s, force_encoding_suffix, size) != 0) goto invalid_format;
                s += size;

                if (utf8) {
                    rb_raise(rb_eRuntimeError, "dumped string contained Unicode escape but used force_encoding");
                }

                encname = s;
                s = memchr(s, '"', s_end-s);
                size = s - encname;
                if (!s) goto invalid_format;
                if (s_end - s != 2) goto invalid_format;
                if (s[0] != '"' || s[1] != ')') goto invalid_format;

                encidx = rb_enc_find_index2(encname, (long)size);
                if (encidx < 0) {
                    rb_raise(rb_eRuntimeError, "dumped string has unknown encoding name");
                }
                rb_enc_associate_index(undumped, encidx);
            }
            break;
        }

        if (*s == '\\') {
            s++;
            if (s >= s_end) {
                rb_raise(rb_eRuntimeError, "invalid escape");
            }
            undump_after_backslash(undumped, &s, s_end, &enc, &utf8, &binary);
        }
        else {
            rb_str_cat(undumped, s++, 1);
        }
    }

    RB_GC_GUARD(str);

    return undumped;
invalid_format:
    rb_raise(rb_eRuntimeError, "invalid dumped string; not wrapped with '\"' nor '\"...\".force_encoding(\"...\")' form");
}
```

unicode_normalize(form = :nfc) → string

click to toggle source

Returns a copy of `self` with Unicode normalization applied.

Argument `form` must be one of the following symbols (see Unicode normalization forms):

- `:nfc`: Canonical decomposition, followed by canonical composition.
- `:nfd`: Canonical decomposition.
- `:nfkc`: Compatibility decomposition, followed by canonical composition.
- `:nfkd`: Compatibility decomposition.

The encoding of `self` must be one of:

- Encoding::UTF_8
- Encoding::UTF_16BE
- Encoding::UTF_16LE
- Encoding::UTF_32BE
- Encoding::UTF_32LE
- Encoding::GB18030
- Encoding::UCS_2BE
- Encoding::UCS_4BE

Examples:

```
"a\u0300".unicode_normalize      
"\u00E0".unicode_normalize(:nfd) 
```

Related: `String#unicode_normalize!`, `String#unicode_normalized?`.

```
static VALUE
rb_str_unicode_normalize(int argc, VALUE *argv, VALUE str)
{
    return unicode_normalize_common(argc, argv, str, id_normalize);
}
```

unicode_normalize!(form = :nfc) → self

click to toggle source

Like `String#unicode_normalize`, except that the normalization is performed on `self`.

Related `String#unicode_normalized?`.

```
static VALUE
rb_str_unicode_normalize_bang(int argc, VALUE *argv, VALUE str)
{
    return rb_str_replace(str, unicode_normalize_common(argc, argv, str, id_normalize));
}
```

unicode_normalized?(form = :nfc) → true or false

click to toggle source

Returns `true` if `self` is in the given `form` of Unicode normalization, `false` otherwise. The `form` must be one of `:nfc`, `:nfd`, `:nfkc`, or `:nfkd`.

Examples:

```
"a\u0300".unicode_normalized?       
"a\u0300".unicode_normalized?(:nfd) 
"\u00E0".unicode_normalized?        
"\u00E0".unicode_normalized?(:nfd)  
```

Raises an exception if `self` is not in a Unicode encoding:

```
s = "\xE0".force_encoding('ISO-8859-1')
s.unicode_normalized? 
```

Related: `String#unicode_normalize`, `String#unicode_normalize!`.

```
static VALUE
rb_str_unicode_normalized_p(int argc, VALUE *argv, VALUE str)
{
    return unicode_normalize_common(argc, argv, str, id_normalized_p);
}
```

unpack(template, offset: 0, &block) → array

click to toggle source

Extracts data from `self`.

If `block` is not given, forming objects that become the elements of a new array, and returns that array. Otherwise, yields each object.

See Packed Data.

```
def unpack(fmt, offset: 0)
  Primitive.attr! :use_block
  Primitive.pack_unpack(fmt, offset)
end
```

unpack1(template, offset: 0) → object

click to toggle source

Like `String#unpack`, but unpacks and returns only the first extracted object. See Packed Data.

```
def unpack1(fmt, offset: 0)
  Primitive.pack_unpack1(fmt, offset)
end
```

upcase(*options) → string

click to toggle source

Returns a string containing the upcased characters in `self`:

```
s = 'Hello World!' 
s.upcase           
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#upcase!`, `String#downcase`, `String#downcase!`.

```
static VALUE
rb_str_upcase(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_UPCASE;
    VALUE ret;

    flags = check_case_options(argc, argv, flags);
    enc = str_true_enc(str);
    if (case_option_single_p(flags, enc, str)) {
        ret = rb_str_new(RSTRING_PTR(str), RSTRING_LEN(str));
        str_enc_copy_direct(ret, str);
        upcase_single(ret);
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

upcase!(*options) → self or nil

click to toggle source

Upcases the characters in `self`; returns `self` if any changes were made, `nil` otherwise:

```
s = 'Hello World!' 
s.upcase!          
s                  
s.upcase!          
```

The casing may be affected by the given `options`; see Case Mapping.

Related: `String#upcase`, `String#downcase`, `String#downcase!`.

```
static VALUE
rb_str_upcase_bang(int argc, VALUE *argv, VALUE str)
{
    rb_encoding *enc;
    OnigCaseFoldType flags = ONIGENC_CASE_UPCASE;

    flags = check_case_options(argc, argv, flags);
    str_modify_keep_cr(str);
    enc = str_true_enc(str);
    if (case_option_single_p(flags, enc, str)) {
        if (upcase_single(str))
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

upto(other_string, exclusive = false) {|string| ... } → self

click to toggle source

upto(other_string, exclusive = false) → new_enumerator

With a block given, calls the block with each `String` value returned by successive calls to `String#succ`; the first value is `self`, the next is `self.succ`, and so on; the sequence terminates when value `other_string` is reached; returns `self`:

```
'a8'.upto('b6') {|s| print s, ' ' } 
```

Output:

```
a8 a9 b0 b1 b2 b3 b4 b5 b6
```

If argument `exclusive` is given as a truthy object, the last value is omitted:

```
'a8'.upto('b6', true) {|s| print s, ' ' } 
```

Output:

```
a8 a9 b0 b1 b2 b3 b4 b5
```

If `other_string` would not be reached, does not call the block:

```
'25'.upto('5') {|s| fail s }
'aa'.upto('a') {|s| fail s }
```

With no block given, returns a new Enumerator:

```
'a8'.upto('b6') 
```

```
static VALUE
rb_str_upto(int argc, VALUE *argv, VALUE beg)
{
    VALUE end, exclusive;

    rb_scan_args(argc, argv, "11", &end, &exclusive);
    RETURN_ENUMERATOR(beg, argc, argv);
    return rb_str_upto_each(beg, end, RTEST(exclusive), str_upto_i, Qnil);
}
```

valid_encoding? → true or false

click to toggle source

Returns `true` if `self` is encoded correctly, `false` otherwise:

```
"\xc2\xa1".force_encoding("UTF-8").valid_encoding? 
"\xc2".force_encoding("UTF-8").valid_encoding?     
"\x80".force_encoding("UTF-8").valid_encoding?     
```

```
static VALUE
rb_str_valid_encoding_p(VALUE str)
{
    int cr = rb_enc_str_coderange(str);

    return RBOOL(cr != ENC_CODERANGE_BROKEN);
}
```
