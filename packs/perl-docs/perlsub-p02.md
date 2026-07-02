---
title: "perlsub (part 2/2)"
source: https://perldoc.perl.org/perlsub
domain: perl-docs
license: GPL-1.0-or-later OR Artistic-1.0
tags: perl, perldoc, perl script, perl module, cpan
fetched: 2026-07-02
part: 2/2
---

## #When to Still Use local()

Despite the existence of `my`, there are still three places where the `local` operator still shines. In fact, in these three places, you *must* use `local` instead of `my`.

1. You need to give a global variable a temporary value, especially $_. The global variables, like `@ARGV` or the punctuation variables, must be `local`ized with `local()`. This block reads in */etc/motd*, and splits it up into chunks separated by lines of equal signs, which are placed in `@Fields`. In particular, it's important to `local`ize $_ in any routine that assigns to it. Look out for implicit assignments in `while` conditionals.
  ```
{
    local @ARGV = ("/etc/motd");
    local $/ = undef;
    local $_ = <>;
    @Fields = split /^\s*=+\s*$/;
}
  ```
2. You need to create a local file or directory handle or a local function. A function that needs a filehandle of its own must use `local()` on a complete typeglob. This can be used to create new symbol table entries: See the Symbol module for a way to create anonymous symbol table entries. Because assignment of a reference to a typeglob creates an alias, this can be used to create what is effectively a local function, or at least, a local alias. See "Function Templates" in perlref for more about manipulating functions by name in this way.
  ```
sub ioqueue {
    local  (*READER, *WRITER);    # not my!
    pipe    (READER,  WRITER)     or die "pipe: $!";
    return (*READER, *WRITER);
}
($head, $tail) = ioqueue();
  ```
  ```
{
    local *grow = \&shrink; # only until this block exits
    grow();                # really calls shrink()
    move();                # if move() grow()s, it shrink()s too
}
grow();                    # get the real grow() again
  ```
3. You want to temporarily change just one element of an array or hash. You can `local`ize just one element of an aggregate. Usually this is done on dynamics: But it also works on lexically declared aggregates.
  ```
{
    local $SIG{INT} = 'IGNORE';
    funct();                            # uninterruptible
}
# interruptibility automatically restored here
  ```


## #Pass by Reference

If you want to pass more than one array or hash into a function--or return them from it--and have them maintain their integrity, then you're going to have to use an explicit pass-by-reference. Before you do that, you need to understand references as detailed in perlref. This section may not make much sense to you otherwise.

Here are a few simple examples. First, let's pass in several arrays to a function and have it `pop` all of them, returning a new list of all their former last elements:

```
@tailings = popmany ( \@w, \@x, \@y, \@z );

sub popmany {
    my $aref;
    my @retlist;
    foreach $aref ( @_ ) {
        push @retlist, pop @$aref;
    }
    return @retlist;
}
```

Here's how you might write a function that returns a list of keys occurring in all the hashes passed to it:

```
@common = inter( \%foo, \%bar, \%joe );
sub inter {
    my ($k, $href, %seen); # locals
    foreach $href (@_) {
        while ( $k = each %$href ) {
            $seen{$k}++;
        }
    }
    return grep { $seen{$_} == @_ } keys %seen;
}
```

So far, we're using just the normal list return mechanism. What happens if you want to pass or return a hash? Well, if you're using only one of them, or you don't mind them concatenating, then the normal calling convention is ok, although a little expensive.

Where people get into trouble is here:

```
(@w, @x) = func(@y, @z);
or
(%w, %x) = func(%y, %z);
```

That syntax simply won't work. It sets just `@w` or `%w` and clears the `@x` or `%x`. Plus the function didn't get passed into two separate arrays or hashes: it got one long list in `@_`, as always.

If you can arrange for everyone to deal with this through references, it's cleaner code, although not so nice to look at. Here's a function that takes two array references as arguments, returning the two array elements in order of how many elements they have in them:

```
($wref, $xref) = func(\@y, \@z);
print "@$wref has more than @$xref\n";
sub func {
    my ($yref, $zref) = @_;
    if (@$yref > @$zref) {
        return ($yref, $zref);
    } else {
        return ($zref, $yref);
    }
}
```

It turns out that you can actually do this also:

```
(*w, *x) = func(\@y, \@z);
print "@w has more than @x\n";
sub func {
    local (*y, *z) = @_;
    if (@y > @z) {
        return (\@y, \@z);
    } else {
        return (\@z, \@y);
    }
}
```

Here we're using the typeglobs to do symbol table aliasing. It's a tad subtle, though, and also won't work if you're using `my` variables, because only globals (even in disguise as `local`s) are in the symbol table.

If you're passing around filehandles, you could usually just use the bare typeglob, like `*STDOUT`, but typeglobs references work, too. For example:

```
splutter(\*STDOUT);
sub splutter {
    my $fh = shift;
    print $fh "her um well a hmmm\n";
}

$rec = get_rec(\*STDIN);
sub get_rec {
    my $fh = shift;
    return scalar <$fh>;
}
```

If you're planning on generating new filehandles, you could do this. Notice to pass back just the bare *FH, not its reference.

```
sub openit {
    my $path = shift;
    local *FH;
    return open (FH, $path) ? *FH : undef;
}
```


## #Prototypes

Perl supports a very limited kind of compile-time argument checking using function prototyping. This can be declared in either the PROTO section or with a prototype attribute. If you declare either of

```
sub mypush (\@@)
sub mypush :prototype(\@@)
```

then `mypush()` takes arguments exactly like `push()` does.

If subroutine signatures are enabled (see "Signatures"), then the shorter PROTO syntax is unavailable, because it would clash with signatures. In that case, a prototype can only be declared in the form of an attribute.

The function declaration must be visible at compile time. The prototype affects only interpretation of regular calls to the function, where regular is defined as not using the `&` sigil. In other words, if you call it like a built-in function, then it behaves like a built-in function. If you call it like an old-fashioned (perl4) subroutine, then it behaves like an old-fashioned subroutine. It naturally falls out from this rule that prototypes have no influence on subroutine references like `\&foo` or on indirect subroutine calls like `&{$subref}()` or `$subref->()`.

Method calls are not influenced by prototypes either, because the function to be called is indeterminate at compile time, since the exact code called depends on inheritance.

Because the intent of this feature is primarily to let you define subroutines that work like built-in functions, here are prototypes for some other functions that parse almost exactly like the corresponding built-in.

```
Declared as             Called as

sub mylink ($$)         mylink $old, $new
sub myvec ($$$)         myvec $var, $offset, 1
sub myindex ($$;$)      myindex getstring(), "substr"
sub mysyswrite ($$$;$)  mysyswrite $buf, 0, length($buf) - $off, $off
sub myreverse (@)       myreverse $x, $y, $z
sub myjoin ($@)         myjoin ":", $x, $y, $z
sub mypop (\@)          mypop @array
sub mysplice (\@$$@)    mysplice @array, 0, 2, @pushme
sub mykeys (\[%@])      mykeys $hashref->%*
sub myopen (*;$)        myopen HANDLE, $name
sub mypipe (**)         mypipe READHANDLE, WRITEHANDLE
sub mygrep (&@)         mygrep { /foo/ } $x, $y, $z
sub myrand (;$)         myrand 42
sub mytime ()           mytime
```

Any backslashed prototype character represents an actual argument that must start with that character (optionally preceded by `my`, `our` or `local`), with the exception of `$`, which will accept any scalar lvalue expression, such as `$foo = 7` or `my_function()->[0]`. The value passed as part of `@_` will be a reference to the actual argument given in the subroutine call, obtained by applying `\` to that argument.

You can use the `\[]` backslash group notation to specify more than one allowed argument type. For example:

```
sub myref (\[$@%&*])
```

will allow calling myref() as

```
myref $var
myref @array
myref %hash
myref &sub
myref *glob
```

and the first argument of myref() will be a reference to a scalar, an array, a hash, a subroutine, or a glob.

Unbackslashed prototype characters have special meanings. Any unbackslashed `@` or `%` eats all remaining arguments, and forces list context. An argument represented by `$` forces scalar context. An `&` requires an anonymous subroutine, which, if passed as the first argument, may look like a bare block: It does not require the `sub` keyword or a subsequent comma.

A `*` allows the subroutine to accept a bareword, constant, scalar expression, typeglob, or a reference to a typeglob in that slot. The value will be available to the subroutine either as a simple scalar, or (in the latter two cases) as a reference to the typeglob. If you wish to always convert such arguments to a typeglob reference, use Symbol::qualify_to_ref() as follows:

```
use Symbol 'qualify_to_ref';

sub foo (*) {
    my $fh = qualify_to_ref(shift, caller);
    ...
}
```

The `+` prototype is a special alternative to `$` that will act like `\[@%]` when given a literal array or hash variable, but will otherwise force scalar context on the argument. This is useful for functions which should accept either a literal array or an array reference as the argument:

```
sub mypush (+@) {
    my $aref = shift;
    die "Not an array or arrayref" unless ref $aref eq 'ARRAY';
    push @$aref, @_;
}
```

When using the `+` prototype, your function must check that the argument is of an acceptable type.

A semicolon (`;`) separates mandatory arguments from optional arguments. It is redundant before `@` or `%`, which gobble up everything else.

As the last character of a prototype, or just before a semicolon, a `@` or a `%`, you can use `_` in place of `$`: if this argument is not provided, `$_` will be used instead.

Note how the last three examples in the table above are treated specially by the parser. `mygrep()` is parsed as a true list operator, `myrand()` is parsed as a true unary operator with unary precedence the same as `rand()`, and `mytime()` is truly without arguments, just like `time()`. That is, if you say

```
mytime +2;
```

you'll get `mytime() + 2`, not `mytime(2)`, which is how it would be parsed without a prototype. If you want to force a unary function to have the same precedence as a list operator, add `;` to the end of the prototype:

```
sub mygetprotobynumber($;);
mygetprotobynumber $x > $y; # parsed as mygetprotobynumber($x > $y)
```

The interesting thing about `&` is that you can generate new syntax with it, provided it's in the initial position:

```
sub try (&@) {
    my($try,$catch) = @_;
    eval { &$try };
    if ($@) {
        local $_ = $@;
        &$catch;
    }
}
sub catch (&) { $_[0] }

try {
    die "phooey";
} catch {
    /phooey/ and print "unphooey\n";
};
```

That prints `"unphooey"`. (Yes, there are still unresolved issues having to do with visibility of `@_`. I'm ignoring that question for the moment. (But note that if we make `@_` lexically scoped, those anonymous subroutines can act like closures... (Gee, is this sounding a little Lispish? (Never mind.))))

And here's a reimplementation of the Perl `grep` operator:

```
sub mygrep (&@) {
    my $code = shift;
    my @result;
    foreach $_ (@_) {
        push(@result, $_) if &$code;
    }
    @result;
}
```

Some folks would prefer full alphanumeric prototypes. Alphanumerics have been intentionally left out of prototypes for the express purpose of someday in the future adding named, formal parameters. The current mechanism's main goal is to let module writers provide better diagnostics for module users. Larry feels the notation quite understandable to Perl programmers, and that it will not intrude greatly upon the meat of the module, nor make it harder to read. The line noise is visually encapsulated into a small pill that's easy to swallow.

If you try to use an alphanumeric sequence in a prototype you will generate an optional warning - "Illegal character in prototype...". Unfortunately earlier versions of Perl allowed the prototype to be used as long as its prefix was a valid prototype. The warning may be upgraded to a fatal error in a future version of Perl once the majority of offending code is fixed.

It's probably best to prototype new functions, not retrofit prototyping into older ones. That's because you must be especially careful about silent impositions of differing list versus scalar contexts. For example, if you decide that a function should take just one parameter, like this:

```
sub func ($) {
    my $n = shift;
    print "you gave me $n\n";
}
```

and someone has been calling it with an array or expression returning a list:

```
func(@foo);
func( $text =~ /\w+/g );
```

Then you've just supplied an automatic `scalar` in front of their argument, which can be more than a bit surprising. The old `@foo` which used to hold one thing doesn't get passed in. Instead, `func()` now gets passed in a `1`; that is, the number of elements in `@foo`. And the `m//g` gets called in scalar context so instead of a list of words it returns a boolean result and advances `pos($text)`. Ouch!

If a sub has both a PROTO and a BLOCK, the prototype is not applied until after the BLOCK is completely defined. This means that a recursive function with a prototype has to be predeclared for the prototype to take effect, like so:

```
sub foo($$);
sub foo($$) {
    foo 1, 2;
}
```

This is all very powerful, of course, and should be used only in moderation to make the world a better place.


## #Constant Functions

Functions with a prototype of `()` are potential candidates for inlining. If the result after optimization and constant folding is either a constant or a lexically-scoped scalar which has no other references, then it will be used in place of function calls made without `&`. Calls made using `&` are never inlined. (See constant for an easy way to declare most constants.)

The following functions would all be inlined:

```
sub pi ()           { 3.14159 }             # Not exact, but close.
sub PI ()           { 4 * atan2 1, 1 }      # As good as it gets,
                                            # and it's inlined, too!
sub ST_DEV ()       { 0 }
sub ST_INO ()       { 1 }

sub FLAG_FOO ()     { 1 << 8 }
sub FLAG_BAR ()     { 1 << 9 }
sub FLAG_MASK ()    { FLAG_FOO | FLAG_BAR }

sub OPT_BAZ ()      { not (0x1B58 & FLAG_MASK) }

sub N () { int(OPT_BAZ) / 3 }

sub FOO_SET () { 1 if FLAG_MASK & FLAG_FOO }
sub FOO_SET2 () { if (FLAG_MASK & FLAG_FOO) { 1 } }
```

(Be aware that the last example was not always inlined in Perl 5.20 and earlier, which did not behave consistently with subroutines containing inner scopes.) You can countermand inlining by using an explicit `return`:

```
sub baz_val () {
    if (OPT_BAZ) {
        return 23;
    }
    else {
        return 42;
    }
}
sub bonk_val () { return 12345 }
```

As alluded to earlier you can also declare inlined subs dynamically at BEGIN time if their body consists of a lexically-scoped scalar which has no other references. Only the first example here will be inlined:

```
BEGIN {
    my $var = 1;
    no strict 'refs';
    *INLINED = sub () { $var };
}

BEGIN {
    my $var = 1;
    my $ref = \$var;
    no strict 'refs';
    *NOT_INLINED = sub () { $var };
}
```

A not so obvious caveat with this (see [RT #79908]) is what happens if the variable is potentially modifiable. For example:

```
BEGIN {
    my $x = 10;
    *FOO = sub () { $x };
    $x++;
}
print FOO(); # printed 10 prior to 5.32.0
```

From Perl 5.22 onwards this gave a deprecation warning, and from Perl 5.32 onwards it became a run-time error. Previously the variable was immediately inlined, and stopped behaving like a normal lexical variable; so it printed `10`, not `11`.

If you still want such a subroutine to be inlined (with no warning), make sure the variable is not used in a context where it could be modified aside from where it is declared.

```
# Fine, no warning
BEGIN {
    my $x = 54321;
    *INLINED = sub () { $x };
}
# Error
BEGIN {
    my $x;
    $x = 54321;
    *ALSO_INLINED = sub () { $x };
}
```

Perl 5.22 also introduced the "const" attribute as an alternative. It was initially experimental, but made stable in Perl 5.40. When applied to an anonymous subroutine, it forces the sub to be called when the `sub` expression is evaluated. The return value is captured and turned into a constant subroutine:

```
my $x = 54321;
*INLINED = sub : const { $x };
$x++;
```

The return value of `INLINED` in this example will always be 54321, regardless of later modifications to $x. You can also put any arbitrary code inside the sub, at it will be executed immediately and its return value captured the same way.

If you really want a subroutine with a `()` prototype that returns a lexical variable you can easily force it to not be inlined by adding an explicit `return`:

```
BEGIN {
    my $x = 10;
    *FOO = sub () { return $x };
    $x++;
}
print FOO(); # prints 11
```

The easiest way to tell if a subroutine was inlined is by using B::Deparse. Consider this example of two subroutines returning `1`, one with a `()` prototype causing it to be inlined, and one without (with deparse output truncated for clarity):

```
$ perl -MO=Deparse -e 'sub ONE { 1 } if (ONE) { print ONE if ONE }'
sub ONE {
    1;
}
if (ONE ) {
    print ONE() if ONE ;
}

$ perl -MO=Deparse -e 'sub ONE () { 1 } if (ONE) { print ONE if ONE }'
sub ONE () { 1 }
do {
    print 1
};
```

If you redefine a subroutine that was eligible for inlining, you'll get a warning by default. You can use this warning to tell whether or not a particular subroutine is considered inlinable, since it's different than the warning for overriding non-inlined subroutines:

```
$ perl -e 'sub one () {1} sub one () {2}'
Constant subroutine one redefined at -e line 1.
$ perl -we 'sub one {1} sub one {2}'
Subroutine one redefined at -e line 1.
```

The warning is considered severe enough not to be affected by the **-w** switch (or its absence) because previously compiled invocations of the function will still be using the old value of the function. If you need to be able to redefine the subroutine, you need to ensure that it isn't inlined, either by dropping the `()` prototype (which changes calling semantics, so beware) or by thwarting the inlining mechanism in some other way, e.g. by adding an explicit `return`, as mentioned above:

```
sub not_inlined () { return 23 }
```


## #Overriding Built-in Functions

Many built-in functions may be overridden, though this should be tried only occasionally and for good reason. Typically this might be done by a package attempting to emulate missing built-in functionality on a non-Unix system.

Overriding may be done only by importing the name from a module at compile time--ordinary predeclaration isn't good enough. However, the `use subs` pragma lets you, in effect, predeclare subs via the import syntax, and these names may then override built-in ones:

```
use subs 'chdir', 'chroot', 'chmod', 'chown';
chdir $somewhere;
sub chdir { ... }
```

To unambiguously refer to the built-in form, precede the built-in name with the special package qualifier `CORE::`. For example, saying `CORE::open()` always refers to the built-in `open()`, even if the current package has imported some other subroutine called `&open()` from elsewhere. Even though it looks like a regular function call, it isn't: the `CORE::` prefix in that case is part of Perl's syntax, and works for any keyword, regardless of what is in the `CORE` package. Taking a reference to it, that is, `\&CORE::open`, only works for some keywords. See CORE.

Library modules should not in general export built-in names like `open` or `chdir` as part of their default `@EXPORT` list, because these may sneak into someone else's namespace and change the semantics unexpectedly. Instead, if the module adds that name to `@EXPORT_OK`, then it's possible for a user to import the name explicitly, but not implicitly. That is, they could say

```
use Module 'open';
```

and it would import the `open` override. But if they said

```
use Module;
```

they would get the default imports without overrides.

The foregoing mechanism for overriding built-in is restricted, quite deliberately, to the package that requests the import. There is a second method that is sometimes applicable when you wish to override a built-in everywhere, without regard to namespace boundaries. This is achieved by importing a sub into the special namespace `CORE::GLOBAL::`. Here is an example that quite brazenly replaces the `glob` operator with something that understands regular expressions.

```
package REGlob;
require Exporter;
@ISA = 'Exporter';
@EXPORT_OK = 'glob';

sub import {
    my $pkg = shift;
    return unless @_;
    my $sym = shift;
    my $where = ($sym =~ s/^GLOBAL_// ? 'CORE::GLOBAL' : caller(0));
    $pkg->export($where, $sym, @_);
}

sub glob {
    my $pat = shift;
    my @got;
    if (opendir my $d, '.') {
        @got = grep /$pat/, readdir $d;
        closedir $d;
    }
    return @got;
}
1;
```

And here's how it could be (ab)used:

```
#use REGlob 'GLOBAL_glob';      # override glob() in ALL namespaces
package Foo;
use REGlob 'glob';              # override glob() in Foo:: only
print for <^[a-z_]+\.pm\$>;     # show all pragmatic modules
```

The initial comment shows a contrived, even dangerous example. By overriding `glob` globally, you would be forcing the new (and subversive) behavior for the `glob` operator for *every* namespace, without the complete cognizance or cooperation of the modules that own those namespaces. Naturally, this should be done with extreme caution--if it must be done at all.

The `REGlob` example above does not implement all the support needed to cleanly override Perl's `glob` operator. The built-in `glob` has different behaviors depending on whether it appears in a scalar or list context, but our `REGlob` doesn't. Indeed, many Perl built-ins have such context sensitive behaviors, and these must be adequately supported by a properly written override. For a fully functional example of overriding `glob`, study the implementation of `File::DosGlob` in the standard library.

When you override a built-in, your replacement should be consistent (if possible) with the built-in native syntax. You can achieve this by using a suitable prototype. To get the prototype of an overridable built-in, use the `prototype` function with an argument of `"CORE::builtin_name"` (see "prototype" in perlfunc).

Note however that some built-ins can't have their syntax expressed by a prototype (such as `system` or `chomp`). If you override them you won't be able to fully mimic their original syntax.

The built-ins `do`, `require` and `glob` can also be overridden, but due to special magic, their original syntax is preserved, and you don't have to define a prototype for their replacements. (You can't override the `do BLOCK` syntax, though).

`require` has special additional dark magic: if you invoke your `require` replacement as `require Foo::Bar`, it will actually receive the argument `"Foo/Bar.pm"` in @_. See "require" in perlfunc.

And, as you'll have noticed from the previous example, if you override `glob`, the `<*>` glob operator is overridden as well.

In a similar fashion, overriding the `readline` function also overrides the equivalent I/O operator `<FILEHANDLE>`. Also, overriding `readpipe` also overrides the operators `` and `qx//`.

Finally, some built-ins (e.g. `exists` or `grep`) can't be overridden.


## #Autoloading

If you call a subroutine that is undefined, you would ordinarily get an immediate, fatal error complaining that the subroutine doesn't exist. (Likewise for subroutines being used as methods, when the method doesn't exist in any base class of the class's package.) However, if an `AUTOLOAD` subroutine is defined in the package or packages used to locate the original subroutine, then that `AUTOLOAD` subroutine is called with the arguments that would have been passed to the original subroutine. The fully qualified name of the original subroutine magically appears in the global $AUTOLOAD variable of the same package as the `AUTOLOAD` routine. The name is not passed as an ordinary argument because, er, well, just because, that's why. (As an exception, a method call to a nonexistent `import` or `unimport` method is just skipped instead. Also, if the AUTOLOAD subroutine is an XSUB, there are other ways to retrieve the subroutine name. See "Autoloading with XSUBs" in perlguts for details.)

Many `AUTOLOAD` routines load in a definition for the requested subroutine using eval(), then execute that subroutine using a special form of goto() that erases the stack frame of the `AUTOLOAD` routine without a trace. (See the source to the standard module documented in AutoLoader, for example.) But an `AUTOLOAD` routine can also just emulate the routine and never define it. For example, let's pretend that a function that wasn't defined should just invoke `system` with those arguments. All you'd do is:

```
sub AUTOLOAD {
    our $AUTOLOAD;              # keep 'use strict' happy
    my $program = $AUTOLOAD;
    $program =~ s/.*:://;
    system($program, @_);
}
date();
who();
ls('-l');
```

In fact, if you predeclare functions you want to call that way, you don't even need parentheses:

```
use subs qw(date who ls);
date;
who;
ls '-l';
```

A more complete example of this is the Shell module on CPAN, which can treat undefined subroutine calls as calls to external programs.

Mechanisms are available to help modules writers split their modules into autoloadable files. See the standard AutoLoader module described in AutoLoader and in AutoSplit, the standard SelfLoader modules in SelfLoader, and the document on adding C functions to Perl code in perlxs.


## #Subroutine Attributes

A subroutine declaration or definition may have a list of attributes associated with it. If such an attribute list is present, it is broken up at space or colon boundaries and treated as though a `use attributes` had been seen. See attributes for details about what attributes are currently supported. Unlike the limitation with the obsolescent `use attrs`, the `sub : ATTRLIST` syntax works to associate the attributes with a pre-declaration, and not just with a subroutine definition.

The attributes must be valid as simple identifier names (without any punctuation other than the '_' character). They may have a parameter list appended, which is only checked for whether its parentheses ('(',')') nest properly.

Examples of valid syntax (even though the attributes are unknown):

```
sub fnord (&\%) : switch(10,foo(7,3))  :  expensive;
sub plugh () : Ugly('\(") :Bad;
sub xyzzy : _5x5 { ... }
```

Examples of invalid syntax:

```
sub fnord : switch(10,foo();    # ()-string not balanced
sub snoid : Ugly('(');          # ()-string not balanced
sub xyzzy : 5x5;                # "5x5" not a valid identifier
sub plugh : Y2::north;          # "Y2::north" not a simple identifier
sub snurt : foo + bar;          # "+" not a colon or space
```

The attribute list is passed as a list of constant strings to the code which associates them with the subroutine. In particular, the second example of valid syntax above currently looks like this in terms of how it's parsed and invoked:

```
use attributes __PACKAGE__, \&plugh, q[Ugly('\(")], 'Bad';
```

For further details on attribute lists and their manipulation, see attributes and Attribute::Handlers.

# #SEE ALSO

See "Function Templates" in perlref for more about references and closures. See perlxs if you'd like to learn about calling C subroutines from Perl. See perlembed if you'd like to learn about calling Perl subroutines from C. See perlmod to learn about bundling up your functions in separate files. See perlmodlib to learn what library modules come standard on your system. See perlootut to learn how to make object method calls.
