---
title: "class Regexp (part 2/2)"
source: https://ruby-doc.org/core/Regexp.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/2
---

## References¶ ↑

Read (online PDF books):

- Mastering Regular Expressions by Jeffrey E.F. Friedl.
- Regular Expressions Cookbook by Jan Goyvaerts & Steven Levithan.

Explore, test (interactive online editor):

- Rubular.

### Constants

**EXTENDED see `Regexp.options` and `Regexp.new` FIXEDENCODING see `Regexp.options` and `Regexp.new` IGNORECASE see `Regexp.options` and `Regexp.new` MULTILINE see `Regexp.options` and `Regexp.new` NOENCODING see `Regexp.options` and `Regexp.new`**

### Public Class Methods

compile

(*args)

Alias for `Regexp.new`

escape(string) → new_string

click to toggle source

Returns a new string that escapes any characters that have special meaning in a regular expression:

```
s = Regexp.escape('\*?{}.')      
```

For any string `s`, this call returns a `MatchData` object:

```
r = Regexp.new(Regexp.escape(s)) 
r.match(s)                       
```

```
static VALUE
rb_reg_s_quote(VALUE c, VALUE str)
{
    return rb_reg_quote(reg_operand(str, TRUE));
}
```

last_match → matchdata or nil

click to toggle source

last_match(n) → string or nil

last_match(name) → string or nil

With no argument, returns the value of `$~`, which is the result of the most recent pattern match (see Regexp global variables):

```
/c(.)t/ =~ 'cat'  
Regexp.last_match 
/a/ =~ 'foo'      
Regexp.last_match 
```

With non-negative integer argument `n`, returns the _n_th field in the matchdata, if any, or nil if none:

```
/c(.)t/ =~ 'cat'     
Regexp.last_match(0) 
Regexp.last_match(1) 
Regexp.last_match(2) 
```

With negative integer argument `n`, counts backwards from the last field:

```
Regexp.last_match(-1)       
```

With string or symbol argument `name`, returns the string value for the named capture, if any:

```
/(?<lhs>\w+)\s*=\s*(?<rhs>\w+)/ =~ 'var = val'
Regexp.last_match        
Regexp.last_match(:lhs)  
Regexp.last_match('rhs') 
Regexp.last_match('foo') 
```

```
static VALUE
rb_reg_s_last_match(int argc, VALUE *argv, VALUE _)
{
    if (rb_check_arity(argc, 0, 1) == 1) {
        VALUE match = rb_backref_get();
        int n;
        if (NIL_P(match)) return Qnil;
        n = match_backref_number(match, argv[0]);
        return rb_reg_nth_match(n, match);
    }
    return match_getter();
}
```

linear_time?(re)

click to toggle source

linear_time?(string, options = 0)

Returns `true` if matching against `re` can be done in linear time to the input string.

```
Regexp.linear_time?(/re/) 
```

Note that this is a property of the ruby interpreter, not of the argument regular expression. Identical regexp can or cannot run in linear time depending on your ruby binary. Neither forward nor backward compatibility is guaranteed about the return value of this method. Our current algorithm is (*1) but this is subject to change in the future. Alternative implementations can also behave differently. They might always return false for everything.

(*1): doi.org/10.1109/SP40001.2021.00032

```
static VALUE
rb_reg_s_linear_time_p(int argc, VALUE *argv, VALUE self)
{
    struct reg_init_args args;
    VALUE re = reg_extract_args(argc, argv, &args);

    if (NIL_P(re)) {
        re = reg_init_args(rb_reg_alloc(), args.str, args.enc, args.flags);
    }

    return RBOOL(onig_check_linear_time(RREGEXP_PTR(re)));
}
```

new(string, options = 0, timeout: nil) → regexp

click to toggle source

new(regexp, timeout: nil) → regexp

With argument `string` given, returns a new regexp with the given string and options:

```
r = Regexp.new('foo') 
r.source              
r.options             
```

Optional argument `options` is one of the following:

- A `String` of options:
  ```
Regexp.new('foo', 'i')  
Regexp.new('foo', 'im') 
  ```
- The bit-wise OR of one or more of the constants `Regexp::EXTENDED`, `Regexp::IGNORECASE`, `Regexp::MULTILINE`, and `Regexp::NOENCODING`:
  ```
Regexp.new('foo', Regexp::IGNORECASE) 
Regexp.new('foo', Regexp::EXTENDED)   
Regexp.new('foo', Regexp::MULTILINE)  
Regexp.new('foo', Regexp::NOENCODING)  
flags = Regexp::IGNORECASE | Regexp::EXTENDED |  Regexp::MULTILINE
Regexp.new('foo', flags)              
  ```
- `nil` or `false`, which is ignored.
- Any other truthy value, in which case the regexp will be case-insensitive.

If optional keyword argument `timeout` is given, its float value overrides the timeout interval for the class, `Regexp.timeout`. If `nil` is passed as +timeout, it uses the timeout interval for the class, `Regexp.timeout`.

With argument `regexp` given, returns a new regexp. The source, options, timeout are the same as `regexp`. `options` and `n_flag` arguments are ineffective. The timeout can be overridden by `timeout` keyword.

```
options = Regexp::MULTILINE
r = Regexp.new('foo', options, timeout: 1.1) 
r2 = Regexp.new(r)                           
r2.timeout                                   
r3 = Regexp.new(r, timeout: 3.14)            
r3.timeout                                   
```

```
static VALUE
rb_reg_initialize_m(int argc, VALUE *argv, VALUE self)
{
    struct reg_init_args args;
    VALUE re = reg_extract_args(argc, argv, &args);

    if (NIL_P(re)) {
        reg_init_args(self, args.str, args.enc, args.flags);
    }
    else {
        reg_copy(self, re);
    }

    set_timeout(&RREGEXP_PTR(self)->timelimit, args.timeout);

    return self;
}
```

escape(string) → new_string

click to toggle source

Returns a new string that escapes any characters that have special meaning in a regular expression:

```
s = Regexp.escape('\*?{}.')      
```

For any string `s`, this call returns a `MatchData` object:

```
r = Regexp.new(Regexp.escape(s)) 
r.match(s)                       
```

```
static VALUE
rb_reg_s_quote(VALUE c, VALUE str)
{
    return rb_reg_quote(reg_operand(str, TRUE));
}
```

timeout → float or nil

click to toggle source

It returns the current default timeout interval for `Regexp` matching in second. `nil` means no default timeout configuration.

```
static VALUE
rb_reg_s_timeout_get(VALUE dummy)
{
    double d = hrtime2double(rb_reg_match_time_limit);
    if (d == 0.0) return Qnil;
    return DBL2NUM(d);
}
```

timeout = float or nil

click to toggle source

It sets the default timeout interval for `Regexp` matching in second. `nil` means no default timeout configuration. This configuration is process-global. If you want to set timeout for each `Regexp`, use `timeout` keyword for `Regexp.new`.

```
Regexp.timeout = 1
/^a*b?a*$/ =~ "a" * 100000 + "x" 
```

```
static VALUE
rb_reg_s_timeout_set(VALUE dummy, VALUE timeout)
{
    rb_ractor_ensure_main_ractor("can not access Regexp.timeout from non-main Ractors");

    set_timeout(&rb_reg_match_time_limit, timeout);

    return timeout;
}
```

try_convert(object) → regexp or nil

click to toggle source

Returns `object` if it is a regexp:

```
Regexp.try_convert(/re/) 
```

Otherwise if `object` responds to `:to_regexp`, calls `object.to_regexp` and returns the result.

Returns `nil` if `object` does not respond to `:to_regexp`.

```
Regexp.try_convert('re') 
```

Raises an exception unless `object.to_regexp` returns a regexp.

```
static VALUE
rb_reg_s_try_convert(VALUE dummy, VALUE re)
{
    return rb_check_regexp_type(re);
}
```

union(*patterns) → regexp

click to toggle source

union(array_of_patterns) → regexp

Returns a new regexp that is the union of the given patterns:

```
r = Regexp.union(%w[cat dog])      
r.match('cat')      
r.match('dog')      
r.match('cog')      
```

For each pattern that is a string, `Regexp.new(pattern)` is used:

```
Regexp.union('penzance')             
Regexp.union('a+b*c')                
Regexp.union('skiing', 'sledding')   
Regexp.union(['skiing', 'sledding']) 
```

For each pattern that is a regexp, it is used as is, including its flags:

```
Regexp.union(/foo/i, /bar/m, /baz/x)

Regexp.union([/foo/i, /bar/m, /baz/x])
```

With no arguments, returns `/(?!)/`:

```
Regexp.union 
```

If any regexp pattern contains captures, the behavior is unspecified.

```
static VALUE
rb_reg_s_union_m(VALUE self, VALUE args)
{
    VALUE v;
    if (RARRAY_LEN(args) == 1 &&
        !NIL_P(v = rb_check_array_type(rb_ary_entry(args, 0)))) {
        return rb_reg_s_union(self, v);
    }
    return rb_reg_s_union(self, args);
}
```

### Public Instance Methods

regexp == object → true or false

Returns `true` if `object` is another Regexp whose pattern, flags, and encoding are the same as `self`, `false` otherwise:

```
/foo/ == Regexp.new('foo')                          
/foo/ == /foo/i                                     
/foo/ == Regexp.new('food')                         
/foo/ == Regexp.new("abc".force_encoding("euc-jp")) 
```

Alias for:

eql?

regexp === string → true or false

click to toggle source

Returns `true` if `self` finds a match in `string`:

```
/^[a-z]*$/ === 'HELLO' 
/^[A-Z]*$/ === 'HELLO' 
```

This method is called in case statements:

```
s = 'HELLO'
case s
when /\A[a-z]*\z/; print "Lower case\n"
when /\A[A-Z]*\z/; print "Upper case\n"
else               print "Mixed case\n"
end 
```

```
static VALUE
rb_reg_eqq(VALUE re, VALUE str)
{
    long start;

    str = reg_operand(str, FALSE);
    if (NIL_P(str)) {
        rb_backref_set(Qnil);
        return Qfalse;
    }
    start = rb_reg_search(re, str, 0, 0);
    return RBOOL(start >= 0);
}
```

regexp =~ string → integer or nil

click to toggle source

Returns the integer index (in characters) of the first match for `self` and `string`, or `nil` if none; also sets the rdoc-ref:Regexp global variables:

```
/at/ =~ 'input data' 
$~                   
/ax/ =~ 'input data' 
$~                   
```

Assigns named captures to local variables of the same names if and only if `self`:

- Is a regexp literal; see Regexp Literals.
- Does not contain interpolations; see Regexp interpolation.
- Is at the left of the expression.

Example:

```
/(?<lhs>\w+)\s*=\s*(?<rhs>\w+)/ =~ '  x = y  '
p lhs 
p rhs 
```

Assigns `nil` if not matched:

```
/(?<lhs>\w+)\s*=\s*(?<rhs>\w+)/ =~ '  x = '
p lhs 
p rhs 
```

Does not make local variable assignments if `self` is not a regexp literal:

```
r = /(?<foo>\w+)\s*=\s*(?<foo>\w+)/
r =~ '  x = y  '
p foo 
p bar 
```

The assignment does not occur if the regexp is not at the left:

```
'  x = y  ' =~ /(?<foo>\w+)\s*=\s*(?<foo>\w+)/
p foo, foo 
```

A regexp interpolation, `#{}`, also disables the assignment:

```
r = /(?<foo>\w+)/
/(?<foo>\w+)\s*=\s*#{r}/ =~ 'x = y'
p foo 
```

```
VALUE
rb_reg_match(VALUE re, VALUE str)
{
    long pos = reg_match_pos(re, &str, 0, NULL);
    if (pos < 0) return Qnil;
    pos = rb_str_sublen(str, pos);
    return LONG2FIX(pos);
}
```

casefold?→ true or false

click to toggle source

Returns `true` if the case-insensitivity flag in `self` is set, `false` otherwise:

```
/a/.casefold?           
/a/i.casefold?          
/(?i:a)/.casefold?      
```

```
static VALUE
rb_reg_casefold_p(VALUE re)
{
    rb_reg_check(re);
    return RBOOL(RREGEXP_PTR(re)->options & ONIG_OPTION_IGNORECASE);
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

eql?

== object -> true or false

click to toggle source

Returns `true` if `object` is another Regexp whose pattern, flags, and encoding are the same as `self`, `false` otherwise:

```
/foo/ == Regexp.new('foo')                          
/foo/ == /foo/i                                     
/foo/ == Regexp.new('food')                         
/foo/ == Regexp.new("abc".force_encoding("euc-jp")) 
```

```
VALUE
rb_reg_equal(VALUE re1, VALUE re2)
{
    if (re1 == re2) return Qtrue;
    if (!RB_TYPE_P(re2, T_REGEXP)) return Qfalse;
    rb_reg_check(re1); rb_reg_check(re2);
    if (FL_TEST(re1, KCODE_FIXED) != FL_TEST(re2, KCODE_FIXED)) return Qfalse;
    if (RREGEXP_PTR(re1)->options != RREGEXP_PTR(re2)->options) return Qfalse;
    if (RREGEXP_SRC_LEN(re1) != RREGEXP_SRC_LEN(re2)) return Qfalse;
    if (ENCODING_GET(re1) != ENCODING_GET(re2)) return Qfalse;
    return RBOOL(memcmp(RREGEXP_SRC_PTR(re1), RREGEXP_SRC_PTR(re2), RREGEXP_SRC_LEN(re1)) == 0);
}
```

Also aliased as:

==

fixed_encoding? → true or false

click to toggle source

Returns `false` if `self` is applicable to a string with any ASCII-compatible encoding; otherwise returns `true`:

```
r = /a/                                          
r.fixed_encoding?                               
r.match?("\u{6666} a")                          
r.match?("\xa1\xa2 a".force_encoding("euc-jp")) 
r.match?("abc".force_encoding("euc-jp"))        

r = /a/u                                        
r.fixed_encoding?                               
r.match?("\u{6666} a")                          
r.match?("\xa1\xa2".force_encoding("euc-jp"))   
r.match?("abc".force_encoding("euc-jp"))        

r = /\u{6666}/                                  
r.fixed_encoding?                               
r.encoding                                      
r.match?("\u{6666} a")                          
r.match?("\xa1\xa2".force_encoding("euc-jp"))   
r.match?("abc".force_encoding("euc-jp"))        
```

```
static VALUE
rb_reg_fixed_encoding_p(VALUE re)
{
    return RBOOL(FL_TEST(re, KCODE_FIXED));
}
```

hash → integer

click to toggle source

Returns the integer hash value for `self`.

Related: `Object#hash`.

```
VALUE
rb_reg_hash(VALUE re)
{
    st_index_t hashval = reg_hash(re);
    return ST2FIX(hashval);
}
```

inspect → string

click to toggle source

Returns a nicely-formatted string representation of `self`:

```
/ab+c/ix.inspect 
```

Related: `Regexp#to_s`.

```
static VALUE
rb_reg_inspect(VALUE re)
{
    if (!RREGEXP_PTR(re) || !RREGEXP_SRC(re) || !RREGEXP_SRC_PTR(re)) {
        return rb_any_to_s(re);
    }
    return rb_reg_desc(re);
}
```

match(string, offset = 0) → matchdata or nil

click to toggle source

match(string, offset = 0) {|matchdata| ... } → object

With no block given, returns the `MatchData` object that describes the match, if any, or `nil` if none; the search begins at the given character `offset` in `string`:

```
/abra/.match('abracadabra')      
/abra/.match('abracadabra', 4)   
/abra/.match('abracadabra', 8)   
/abra/.match('abracadabra', 800) 

string = "\u{5d0 5d1 5e8 5d0}cadabra"
/abra/.match(string, 7)          
/abra/.match(string, 8)          
/abra/.match(string.b, 8)        
```

With a block given, calls the block if and only if a match is found; returns the block’s value:

```
/abra/.match('abracadabra') {|matchdata| p matchdata }

/abra/.match('abracadabra', 4) {|matchdata| p matchdata }

/abra/.match('abracadabra', 8) {|matchdata| p matchdata }

/abra/.match('abracadabra', 8) {|marchdata| fail 'Cannot happen' }
```

Output (from the first two blocks above):

```
 /(.)(.)(.)/.match("abc")[2] 
 /(.)(.)/.match("abc", 1)[2] 
```

```
static VALUE
rb_reg_match_m(int argc, VALUE *argv, VALUE re)
{
    VALUE result = Qnil, str, initpos;
    long pos;

    if (rb_scan_args(argc, argv, "11", &str, &initpos) == 2) {
        pos = NUM2LONG(initpos);
    }
    else {
        pos = 0;
    }

    pos = reg_match_pos(re, &str, pos, &result);
    if (pos < 0) {
        rb_backref_set(Qnil);
        return Qnil;
    }
    rb_match_busy(result);
    if (!NIL_P(result) && rb_block_given_p()) {
        return rb_yield(result);
    }
    return result;
}
```

match?(string) → true or false

click to toggle source

match?(string, offset = 0) → true or false

Returns `true` or `false` to indicate whether the regexp is matched or not without updating $~ and other related variables. If the second parameter is present, it specifies the position in the string to begin the search.

```
/R.../.match?("Ruby")    
/R.../.match?("Ruby", 1) 
/P.../.match?("Ruby")    
$&                       
```

```
static VALUE
rb_reg_match_m_p(int argc, VALUE *argv, VALUE re)
{
    long pos = rb_check_arity(argc, 1, 2) > 1 ? NUM2LONG(argv[1]) : 0;
    return rb_reg_match_p(re, argv[0], pos);
}
```

named_captures → hash

click to toggle source

Returns a hash representing named captures of `self` (see Named Captures):

- Each key is the name of a named capture.
- Each value is an array of integer indexes for that named capture.

Examples:

```
/(?<foo>.)(?<bar>.)/.named_captures 
/(?<foo>.)(?<foo>.)/.named_captures 
/(.)(.)/.named_captures             
```

```
static VALUE
rb_reg_named_captures(VALUE re)
{
    regex_t *reg = (rb_reg_check(re), RREGEXP_PTR(re));
    VALUE hash = rb_hash_new_with_size(onig_number_of_names(reg));
    onig_foreach_name(reg, reg_named_captures_iter, (void*)hash);
    return hash;
}
```

names → array_of_names

click to toggle source

Returns an array of names of captures (see Named Captures):

```
/(?<foo>.)(?<bar>.)(?<baz>.)/.names 
/(?<foo>.)(?<foo>.)/.names          
/(.)(.)/.names                      
```

```
static VALUE
rb_reg_names(VALUE re)
{
    VALUE ary;
    rb_reg_check(re);
    ary = rb_ary_new_capa(onig_number_of_names(RREGEXP_PTR(re)));
    onig_foreach_name(RREGEXP_PTR(re), reg_names_iter, (void*)ary);
    return ary;
}
```

options → integer

click to toggle source

Returns an integer whose bits show the options set in `self`.

The option bits are:

```
Regexp::IGNORECASE 
Regexp::EXTENDED   
Regexp::MULTILINE  
```

Examples:

```
/foo/.options    
/foo/i.options   
/foo/x.options   
/foo/m.options   
/foo/mix.options 
```

Note that additional bits may be set in the returned integer; these are maintained internally in `self`, are ignored if passed to `Regexp.new`, and may be ignored by the caller:

Returns the set of bits corresponding to the options used when creating this regexp (see `Regexp::new` for details). Note that additional bits may be set in the returned options: these are used internally by the regular expression code. These extra bits are ignored if the options are passed to `Regexp::new`:

```
r = /\xa1\xa2/e                 
r.source                        
r.options                       
Regexp.new(r.source, r.options) 
```

```
static VALUE
rb_reg_options_m(VALUE re)
{
    int options = rb_reg_options(re);
    return INT2NUM(options);
}
```

source → string

click to toggle source

Returns the original string of `self`:

```
/ab+c/ix.source 
```

`Regexp` escape sequences are retained:

```
/\x20\+/.source  
```

Lexer escape characters are not retained:

```
/\//.source  
```

```
static VALUE
rb_reg_source(VALUE re)
{
    VALUE str;

    rb_reg_check(re);
    str = rb_str_dup(RREGEXP_SRC(re));
    return str;
}
```

timeout → float or nil

click to toggle source

It returns the timeout interval for `Regexp` matching in second. `nil` means no default timeout configuration.

This configuration is per-object. The global configuration set by `Regexp.timeout=` is ignored if per-object configuration is set.

```
re = Regexp.new("^a*b?a*$", timeout: 1)
re.timeout               
re =~ "a" * 100000 + "x" 
```

```
static VALUE
rb_reg_timeout_get(VALUE re)
{
    rb_reg_check(re);
    double d = hrtime2double(RREGEXP_PTR(re)->timelimit);
    if (d == 0.0) return Qnil;
    return DBL2NUM(d);
}
```

to_s → string

click to toggle source

Returns a string showing the options and string of `self`:

```
r0 = /ab+c/ix
s0 = r0.to_s 
```

The returned string may be used as an argument to `Regexp.new`, or as interpolated text for a Regexp interpolation:

```
r1 = Regexp.new(s0) 
r2 = /#{s0}/        
```

Note that `r1` and `r2` are not equal to `r0` because their original strings are different:

```
r0 == r1  
r0.source 
r1.source 
```

Related: `Regexp#inspect`.

```
static VALUE
rb_reg_to_s(VALUE re)
{
    return rb_reg_str_with_term(re, '/');
}
```

~ rxp → integer or nil

click to toggle source

Equivalent to `*rxp* =~ $_`:

```
$_ = "input data"
~ /at/ 
```

```
VALUE
rb_reg_match2(VALUE re)
{
    long start;
    VALUE line = rb_lastline_get();

    if (!RB_TYPE_P(line, T_STRING)) {
        rb_backref_set(Qnil);
        return Qnil;
    }

    start = rb_reg_search(re, line, 0, 0);
    if (start < 0) {
        return Qnil;
    }
    start = rb_str_sublen(line, start);
    return LONG2FIX(start);
}
```
