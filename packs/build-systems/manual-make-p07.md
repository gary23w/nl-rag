---
title: "GNU make (part 7/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 7/17
---

## 6 How to Use Variables

A *variable* is a name defined in a makefile to represent a string of text, called the variable’s *value*. These values are substituted by explicit request into targets, prerequisites, recipes, and other parts of the makefile. (In some other versions of `make`, variables are called *macros*.)

Variables and functions in all parts of a makefile are expanded when read, except for in recipes, the right-hand sides of variable definitions using ‘=’, and the bodies of variable definitions using the `define` directive. The value a variable expands to is that of its most recent definition at the time of expansion. In other words, variables are dynamically scoped.

Variables can represent lists of file names, options to pass to compilers, programs to run, directories to look in for source files, directories to write output in, or anything else you can imagine.

A variable name may be any sequence of characters not containing ‘:’, ‘#’, ‘=’, or whitespace. However, variable names containing characters other than letters, numbers, and underscores should be considered carefully, as in some shells they cannot be passed through the environment to a sub-`make` (see Communicating Variables to a Sub-`make`). Variable names beginning with ‘.’ and an uppercase letter may be given special meaning in future versions of `make`.

Variable names are case-sensitive. The names ‘foo’, ‘FOO’, and ‘Foo’ all refer to different variables.

It is traditional to use upper case letters in variable names, but we recommend using lower case letters for variable names that serve internal purposes in the makefile, and reserving upper case for parameters that control implicit rules or for parameters that the user should override with command options (see Overriding Variables).

A few variables have names that are a single punctuation character or just a few characters. These are the *automatic variables*, and they have particular specialized uses. See Automatic Variables.

Next: The Two Flavors of Variables, Previous: How to Use Variables, Up: How to Use Variables   [Contents][Index]

### 6.1 Basics of Variable References

To substitute a variable’s value, write a dollar sign followed by the name of the variable in parentheses or braces: either ‘$(foo)’ or ‘${foo}’ is a valid reference to the variable `foo`. This special significance of ‘$’ is why you must write ‘$$’ to have the effect of a single dollar sign in a file name or recipe.

Variable references can be used in any context: targets, prerequisites, recipes, most directives, and new variable values. Here is an example of a common case, where a variable holds the names of all the object files in a program:

```
objects = program.o foo.o utils.o
program : $(objects)
        cc -o program $(objects)

$(objects) : defs.h
```

Variable references work by strict textual substitution. Thus, the rule

```
foo = c
prog.o : prog.$(foo)
        $(foo)$(foo) -$(foo) prog.$(foo)
```

could be used to compile a C program prog.c. Since spaces before the variable value are ignored in variable assignments, the value of `foo` is precisely ‘c’. (Don’t actually write your makefiles this way!)

A dollar sign followed by a character other than a dollar sign, open-parenthesis or open-brace treats that single character as the variable name. Thus, you could reference the variable `x` with ‘$x’. However, this practice can lead to confusion (e.g., ‘$foo’ refers to the variable `f` followed by the string `oo`) so we recommend using parentheses or braces around all variables, even single-letter variables, unless omitting them gives significant readability improvements. One place where readability is often improved is automatic variables (see Automatic Variables).

Next: Advanced Features for Reference to Variables, Previous: Basics of Variable References, Up: How to Use Variables   [Contents][Index]

### 6.2 The Two Flavors of Variables

There are different ways that a variable in GNU `make` can get a value; we call them the *flavors* of variables. The flavors are distinguished in how they handle the values they are assigned in the makefile, and in how those values are managed when the variable is later used and expanded.

Next: Simply Expanded Variable Assignment, Previous: The Two Flavors of Variables, Up: The Two Flavors of Variables   [Contents][Index]

#### 6.2.1 Recursively Expanded Variable Assignment

The first flavor of variable is a *recursively expanded* variable. Variables of this sort are defined by lines using ‘=’ (see Setting Variables) or by the `define` directive (see Defining Multi-Line Variables). The value you specify is installed verbatim; if it contains references to other variables, these references are expanded whenever this variable is substituted (in the course of expanding some other string). When this happens, it is called *recursive expansion*.

For example,

```
foo = $(bar)
bar = $(ugh)
ugh = Huh?

all:;echo $(foo)
```

will echo ‘Huh?’: ‘$(foo)’ expands to ‘$(bar)’ which expands to ‘$(ugh)’ which finally expands to ‘Huh?’.

This flavor of variable is the only sort supported by most other versions of `make`. It has its advantages and its disadvantages. An advantage (most would say) is that:

```
CFLAGS = $(include_dirs) -O
include_dirs = -Ifoo -Ibar
```

will do what was intended: when ‘CFLAGS’ is expanded in a recipe, it will expand to ‘-Ifoo -Ibar -O’. A major disadvantage is that you cannot append something on the end of a variable, as in

```
CFLAGS = $(CFLAGS) -O
```

because it will cause an infinite loop in the variable expansion. (Actually `make` detects the infinite loop and reports an error.)

Another disadvantage is that any functions (see Functions for Transforming Text) referenced in the definition will be executed every time the variable is expanded. This makes `make` run slower; worse, it causes the `wildcard` and `shell` functions to give unpredictable results because you cannot easily control when they are called, or even how many times.

Next: Immediately Expanded Variable Assignment, Previous: Recursively Expanded Variable Assignment, Up: The Two Flavors of Variables   [Contents][Index]

#### 6.2.2 Simply Expanded Variable Assignment

To avoid the problems and inconveniences of recursively expanded variables, there is another flavor: simply expanded variables.

*Simply expanded variables* are defined by lines using ‘:=’ or ‘::=’ (see Setting Variables). Both forms are equivalent in GNU `make`; however only the ‘::=’ form is described by the POSIX standard (support for ‘::=’ is added to the POSIX standard for POSIX Issue 8).

The value of a simply expanded variable is scanned once, expanding any references to other variables and functions, when the variable is defined. Once that expansion is complete the value of the variable is never expanded again: when the variable is used the value is copied verbatim as the expansion. If the value contained variable references the result of the expansion will contain their values *as of the time this variable was defined*. Therefore,

```
x := foo
y := $(x) bar
x := later
```

is equivalent to

```
y := foo bar
x := later
```

Here is a somewhat more complicated example, illustrating the use of ‘:=’ in conjunction with the `shell` function. (See The `shell` Function.) This example also shows use of the variable `MAKELEVEL`, which is changed when it is passed down from level to level. (See Communicating Variables to a Sub-`make`, for information about `MAKELEVEL`.)

```
ifeq (0,${MAKELEVEL})
whoami    := $(shell whoami)
host-type := $(shell arch)
MAKE := ${MAKE} host-type=${host-type} whoami=${whoami}
endif
```

An advantage of this use of ‘:=’ is that a typical ‘descend into a directory’ recipe then looks like this:

```
${subdirs}:
        ${MAKE} -C $@ all
```

Simply expanded variables generally make complicated makefile programming more predictable because they work like variables in most programming languages. They allow you to redefine a variable using its own value (or its value processed in some way by one of the expansion functions) and to use the expansion functions much more efficiently (see Functions for Transforming Text).

You can also use them to introduce controlled leading whitespace into variable values. Leading whitespace characters are discarded from your input before substitution of variable references and function calls; this means you can include leading spaces in a variable value by protecting them with variable references, like this:

```
nullstring :=
space := $(nullstring) # end of the line
```

Here the value of the variable `space` is precisely one space. The comment ‘# end of the line’ is included here just for clarity. Since trailing space characters are *not* stripped from variable values, just a space at the end of the line would have the same effect (but be rather hard to read). If you put whitespace at the end of a variable value, it is a good idea to put a comment like that at the end of the line to make your intent clear. Conversely, if you do *not* want any whitespace characters at the end of your variable value, you must remember not to put a random comment on the end of the line after some whitespace, such as this:

```
dir := /foo/bar    # directory to put the frobs in
```

Here the value of the variable `dir` is ‘/foo/bar    ’ (with four trailing spaces), which was probably not the intention. (Imagine something like ‘$(dir)/file’ with this definition!)

Next: Conditional Variable Assignment, Previous: Simply Expanded Variable Assignment, Up: The Two Flavors of Variables   [Contents][Index]

#### 6.2.3 Immediately Expanded Variable Assignment

Another form of assignment allows for immediate expansion, but unlike simple assignment the resulting variable is recursive: it will be re-expanded again on every use. In order to avoid unexpected results, after the value is immediately expanded it will automatically be quoted: all instances of `$` in the value after expansion will be converted into `$$`. This type of assignment uses the ‘:::=’ operator. For example,

```
var = first
OUT :::= $(var)
var = second
```

results in the `OUT` variable containing the text ‘first’, while here:

```
var = one$$two
OUT :::= $(var)
var = three$$four
```

results in the `OUT` variable containing the text ‘one$$two’. The value is expanded when the variable is assigned, so the result is the expansion of the first value of `var`, ‘one$two’; then the value is re-escaped before the assignment is complete giving the final result of ‘one$$two’.

The variable `OUT` is thereafter considered a recursive variable, so it will be re-expanded when it is used.

This seems functionally equivalent to the ‘:=’ / ‘::=’ operators, but there are a few differences:

First, after assignment the variable is a normal recursive variable; when you append to it with ‘+=’ the value on the right-hand side is not expanded immediately. If you prefer the ‘+=’ operator to expand the right-hand side immediately you should use the ‘:=’ / ‘::=’ assignment instead.

Second, these variables are slightly less efficient than simply expanded variables since they do need to be re-expanded when they are used, rather than merely copied. However since all variable references are escaped this expansion simply un-escapes the value, it won’t expand any variables or run any functions.

Here is another example:

```
var = one$$two
OUT :::= $(var)
OUT += $(var)
var = three$$four
```

After this, the value of `OUT` is the text ‘one$$two $(var)’. When this variable is used it will be expanded and the result will be ‘one$two three$four’.

This style of assignment is equivalent to the traditional BSD `make` ‘:=’ operator; as you can see it works slightly differently than the GNU `make` ‘:=’ operator. The `:::=` operator is added to the POSIX specification in Issue 8 to provide portability.

Previous: Immediately Expanded Variable Assignment, Up: The Two Flavors of Variables   [Contents][Index]

#### 6.2.4 Conditional Variable Assignment

There is another assignment operator for variables, ‘?=’. This is called a conditional variable assignment operator, because it only has an effect if the variable is not yet defined. This statement:

```
FOO ?= bar
```

is exactly equivalent to this (see The `origin` Function):

```
ifeq ($(origin FOO), undefined)
  FOO = bar
endif
```

Note that a variable set to an empty value is still defined, so ‘?=’ will not set that variable.

Next: How Variables Get Their Values, Previous: The Two Flavors of Variables, Up: How to Use Variables   [Contents][Index]

### 6.3 Advanced Features for Reference to Variables

This section describes some advanced features you can use to reference variables in more flexible ways.

Next: Computed Variable Names, Previous: Advanced Features for Reference to Variables, Up: Advanced Features for Reference to Variables   [Contents][Index]

#### 6.3.1 Substitution References

A *substitution reference* substitutes the value of a variable with alterations that you specify. It has the form ‘$(*var*:*a*=*b*)’ (or ‘${*var*:*a*=*b*}’) and its meaning is to take the value of the variable *var*, replace every *a* at the end of a word with *b* in that value, and substitute the resulting string.

When we say “at the end of a word”, we mean that *a* must appear either followed by whitespace or at the end of the value in order to be replaced; other occurrences of *a* in the value are unaltered. For example:

```
foo := a.o b.o l.a c.o
bar := $(foo:.o=.c)
```

sets ‘bar’ to ‘a.c b.c l.a c.c’. See Setting Variables.

A substitution reference is shorthand for the `patsubst` expansion function (see Functions for String Substitution and Analysis): ‘$(*var*:*a*=*b*)’ is equivalent to ‘$(patsubst %*a*,%*b*,*var*)’. We provide substitution references as well as `patsubst` for compatibility with other implementations of `make`.

Another type of substitution reference lets you use the full power of the `patsubst` function. It has the same form ‘$(*var*:*a*=*b*)’ described above, except that now *a* must contain a single ‘%’ character. This case is equivalent to ‘$(patsubst *a*,*b*,$(*var*))’. See Functions for String Substitution and Analysis, for a description of the `patsubst` function. For example:

```
foo := a.o b.o l.a c.o
bar := $(foo:%.o=%.c)
```

sets ‘bar’ to ‘a.c b.c l.a c.c’.

Previous: Substitution References, Up: Advanced Features for Reference to Variables   [Contents][Index]

#### 6.3.2 Computed Variable Names

Computed variable names are an advanced concept, very useful in more sophisticated makefile programming. In simple situations you need not consider them, but they can be extremely useful.

Variables may be referenced inside the name of a variable. This is called a *computed variable name* or a *nested variable reference*. For example,

```
x = y
y = z
a := $($(x))
```

defines `a` as ‘z’: the ‘$(x)’ inside ‘$($(x))’ expands to ‘y’, so ‘$($(x))’ expands to ‘$(y)’ which in turn expands to ‘z’. Here the name of the variable to reference is not stated explicitly; it is computed by expansion of ‘$(x)’. The reference ‘$(x)’ here is nested within the outer variable reference.

The previous example shows two levels of nesting, but any number of levels is possible. For example, here are three levels:

```
x = y
y = z
z = u
a := $($($(x)))
```

Here the innermost ‘$(x)’ expands to ‘y’, so ‘$($(x))’ expands to ‘$(y)’ which in turn expands to ‘z’; now we have ‘$(z)’, which becomes ‘u’.

References to recursively-expanded variables within a variable name are re-expanded in the usual fashion. For example:

```
x = $(y)
y = z
z = Hello
a := $($(x))
```

defines `a` as ‘Hello’: ‘$($(x))’ becomes ‘$($(y))’ which becomes ‘$(z)’ which becomes ‘Hello’.

Nested variable references can also contain modified references and function invocations (see Functions for Transforming Text), just like any other reference. For example, using the `subst` function (see Functions for String Substitution and Analysis):

```
x = variable1
variable2 := Hello
y = $(subst 1,2,$(x))
z = y
a := $($($(z)))
```

eventually defines `a` as ‘Hello’. It is doubtful that anyone would ever want to write a nested reference as convoluted as this one, but it works: ‘$($($(z)))’ expands to ‘$($(y))’ which becomes ‘$($(subst 1,2,$(x)))’. This gets the value ‘variable1’ from `x` and changes it by substitution to ‘variable2’, so that the entire string becomes ‘$(variable2)’, a simple variable reference whose value is ‘Hello’.

A computed variable name need not consist entirely of a single variable reference. It can contain several variable references, as well as some invariant text. For example,

```
a_dirs := dira dirb
1_dirs := dir1 dir2
```

```
a_files := filea fileb
1_files := file1 file2
```

```
ifeq "$(use_a)" "yes"
a1 := a
else
a1 := 1
endif
```

```
ifeq "$(use_dirs)" "yes"
df := dirs
else
df := files
endif

dirs := $($(a1)_$(df))
```

will give `dirs` the same value as `a_dirs`, `1_dirs`, `a_files` or `1_files` depending on the settings of `use_a` and `use_dirs`.

Computed variable names can also be used in substitution references:

```
a_objects := a.o b.o c.o
1_objects := 1.o 2.o 3.o

sources := $($(a1)_objects:.o=.c)
```

defines `sources` as either ‘a.c b.c c.c’ or ‘1.c 2.c 3.c’, depending on the value of `a1`.

The only restriction on this sort of use of nested variable references is that they cannot specify part of the name of a function to be called. This is because the test for a recognized function name is done before the expansion of nested references. For example,

```
ifdef do_sort
func := sort
else
func := strip
endif
```

```
bar := a d b g q c
```

```
foo := $($(func) $(bar))
```

attempts to give ‘foo’ the value of the variable ‘sort a d b g q c’ or ‘strip a d b g q c’, rather than giving ‘a d b g q c’ as the argument to either the `sort` or the `strip` function. This restriction could be removed in the future if that change is shown to be a good idea.

You can also use computed variable names in the left-hand side of a variable assignment, or in a `define` directive, as in:

```
dir = foo
$(dir)_sources := $(wildcard $(dir)/*.c)
define $(dir)_print =
lpr $($(dir)_sources)
endef
```

This example defines the variables ‘dir’, ‘foo_sources’, and ‘foo_print’.

Note that *nested variable references* are quite different from *recursively expanded variables* (see The Two Flavors of Variables), though both are used together in complex ways when doing makefile programming.

Next: Setting Variables, Previous: Advanced Features for Reference to Variables, Up: How to Use Variables   [Contents][Index]

### 6.4 How Variables Get Their Values

Variables can get values in several different ways:

- You can specify an overriding value when you run `make`. See Overriding Variables.
- You can specify a value in the makefile, either with an assignment (see Setting Variables) or with a verbatim definition (see Defining Multi-Line Variables).
- You can specify a short-lived value with the `let` function (see The `let` Function) or with the `foreach` function (see The `foreach` Function).
- Variables in the environment become `make` variables. See Variables from the Environment.
- Several *automatic* variables are given new values for each rule. Each of these has a single conventional use. See Automatic Variables.
- Several variables have constant initial values. See Variables Used by Implicit Rules.

Next: Appending More Text to Variables, Previous: How Variables Get Their Values, Up: How to Use Variables   [Contents][Index]

### 6.5 Setting Variables

To set a variable from the makefile, write a line starting with the variable name followed by one of the assignment operators ‘=’, ‘:=’, ‘::=’, or ‘:::=’. Whatever follows the operator and any initial whitespace on the line becomes the value. For example,

```
objects = main.o foo.o bar.o utils.o
```

defines a variable named `objects` to contain the value ‘main.o foo.o bar.o utils.o’. Whitespace around the variable name and immediately after the ‘=’ is ignored.

Variables defined with ‘=’ are *recursively expanded* variables. Variables defined with ‘:=’ or ‘::=’ are *simply expanded* variables; these definitions can contain variable references which will be expanded before the definition is made. Variables defined with ‘:::=’ are *immediately expanded* variables. The different assignment operators are described in See The Two Flavors of Variables.

The variable name may contain function and variable references, which are expanded when the line is read to find the actual variable name to use.

There is no limit on the length of the value of a variable except the amount of memory on the computer. You can split the value of a variable into multiple physical lines for readability (see Splitting Long Lines).

Most variable names are considered to have the empty string as a value if you have never set them. Several variables have built-in initial values that are not empty, but you can set them in the usual ways (see Variables Used by Implicit Rules). Several special variables are set automatically to a new value for each rule; these are called the *automatic* variables (see Automatic Variables).

If you’d like a variable to be set to a value only if it’s not already set, then you can use the shorthand operator ‘?=’ instead of ‘=’. These two settings of the variable ‘FOO’ are identical (see The `origin` Function):

```
FOO ?= bar
```

and

```
ifeq ($(origin FOO), undefined)
FOO = bar
endif
```

The shell assignment operator ‘!=’ can be used to execute a shell script and set a variable to its output. This operator first evaluates the right-hand side, then passes that result to the shell for execution. If the result of the execution ends in a newline, that one newline is removed; all other newlines are replaced by spaces. The resulting string is then placed into the named recursively-expanded variable. For example:

```
hash != printf '\043'
file_list != find . -name '*.c'
```

If the result of the execution could produce a `$`, and you don’t intend what follows that to be interpreted as a make variable or function reference, then you must replace every `$` with `$$` as part of the execution. Alternatively, you can set a simply expanded variable to the result of running a program using the `shell` function call. See The `shell` Function. For example:

```
hash := $(shell printf '\043')
var := $(shell find . -name "*.c")
```

As with the `shell` function, the exit status of the just-invoked shell script is stored in the `.SHELLSTATUS` variable.

Next: The `override` Directive, Previous: Setting Variables, Up: How to Use Variables   [Contents][Index]

### 6.6 Appending More Text to Variables

Often it is useful to add more text to the value of a variable already defined. You do this with a line containing ‘+=’, like this:

```
objects += another.o
```

This takes the value of the variable `objects`, and adds the text ‘another.o’ to it (preceded by a single space, if it has a value already). Thus:

```
objects = main.o foo.o bar.o utils.o
objects += another.o
```

sets `objects` to ‘main.o foo.o bar.o utils.o another.o’.

Using ‘+=’ is similar to:

```
objects = main.o foo.o bar.o utils.o
objects := $(objects) another.o
```

but differs in ways that become important when you use more complex values.

When the variable in question has not been defined before, ‘+=’ acts just like normal ‘=’: it defines a recursively-expanded variable. However, when there *is* a previous definition, exactly what ‘+=’ does depends on what flavor of variable you defined originally. See The Two Flavors of Variables, for an explanation of the two flavors of variables.

When you add to a variable’s value with ‘+=’, `make` acts essentially as if you had included the extra text in the initial definition of the variable. If you defined it first with ‘:=’ or ‘::=’, making it a simply-expanded variable, ‘+=’ adds to that simply-expanded definition, and expands the new text before appending it to the old value just as ‘:=’ does (see Setting Variables, for a full explanation of ‘:=’ or ‘::=’). In fact,

```
variable := value
variable += more
```

is exactly equivalent to:

```
variable := value
variable := $(variable) more
```

On the other hand, when you use ‘+=’ with a variable that you defined first to be recursively-expanded using plain ‘=’ or ‘:::=’, `make` appends the un-expanded text to the existing value, whatever it is. This means that

```
variable = value
variable += more
```

is roughly equivalent to:

```
temp = value
variable = $(temp) more
```

except that of course it never defines a variable called `temp`. The importance of this comes when the variable’s old value contains variable references. Take this common example:

```
CFLAGS = $(includes) -O
…
CFLAGS += -pg # enable profiling
```

The first line defines the `CFLAGS` variable with a reference to another variable, `includes`. (`CFLAGS` is used by the rules for C compilation; see Catalogue of Built-In Rules.) Using ‘=’ for the definition makes `CFLAGS` a recursively-expanded variable, meaning ‘$(includes) -O’ is *not* expanded when `make` processes the definition of `CFLAGS`. Thus, `includes` need not be defined yet for its value to take effect. It only has to be defined before any reference to `CFLAGS`. If we tried to append to the value of `CFLAGS` without using ‘+=’, we might do it like this:

```
CFLAGS := $(CFLAGS) -pg # enable profiling
```

This is pretty close, but not quite what we want. Using ‘:=’ redefines `CFLAGS` as a simply-expanded variable; this means `make` expands the text ‘$(CFLAGS) -pg’ before setting the variable. If `includes` is not yet defined, we get ‘ -O -pg’, and a later definition of `includes` will have no effect. Conversely, by using ‘+=’ we set `CFLAGS` to the *unexpanded* value ‘$(includes) -O -pg’. Thus we preserve the reference to `includes`, so if that variable gets defined at any later point, a reference like ‘$(CFLAGS)’ still uses its value.

Next: Defining Multi-Line Variables, Previous: Appending More Text to Variables, Up: How to Use Variables   [Contents][Index]

### 6.7 The `override` Directive

If a variable has been set with a command argument (see Overriding Variables), then ordinary assignments in the makefile are ignored. If you want to set the variable in the makefile even though it was set with a command argument, you can use an `override` directive, which is a line that looks like this:

```
override variable = value
```
