---
title: "GNU make (part 8/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 8/17
---

# GNU make

or

```
override variable := value
```

To append more text to a variable defined on the command line, use:

```
override variable += more text
```

See Appending More Text to Variables.

Variable assignments marked with the `override` flag have a higher priority than all other assignments, except another `override`. Subsequent assignments or appends to this variable which are not marked `override` will be ignored.

The `override` directive was not invented for escalation in the war between makefiles and command arguments. It was invented so you can alter and add to values that the user specifies with command arguments.

For example, suppose you always want the ‘-g’ switch when you run the C compiler, but you would like to allow the user to specify the other switches with a command argument just as usual. You could use this `override` directive:

```
override CFLAGS += -g
```

You can also use `override` directives with `define` directives. This is done as you might expect:

```
override define foo =
bar
endef
```

See Defining Multi-Line Variables.

Next: Undefining Variables, Previous: The `override` Directive, Up: How to Use Variables   [Contents][Index]

### 6.8 Defining Multi-Line Variables

Another way to set the value of a variable is to use the `define` directive. This directive has an unusual syntax which allows newline characters to be included in the value, which is convenient for defining both canned sequences of commands (see Defining Canned Recipes), and also sections of makefile syntax to use with `eval` (see The `eval` Function).

The `define` directive is followed on the same line by the name of the variable being defined and an (optional) assignment operator, and nothing more. The value to give the variable appears on the following lines. The end of the value is marked by a line containing just the word `endef`.

Aside from this difference in syntax, `define` works just like any other variable definition. The variable name may contain function and variable references, which are expanded when the directive is read to find the actual variable name to use.

The final newline before the `endef` is not included in the value; if you want your value to contain a trailing newline you must include a blank line. For example in order to define a variable that contains a newline character you must use *two* empty lines, not one:

```
define newline

endef
```

You may omit the variable assignment operator if you prefer. If omitted, `make` assumes it to be ‘=’ and creates a recursively-expanded variable (see The Two Flavors of Variables). When using a ‘+=’ operator, the value is appended to the previous value as with any other append operation: with a single space separating the old and new values.

You may nest `define` directives: `make` will keep track of nested directives and report an error if they are not all properly closed with `endef`. Note that lines beginning with the recipe prefix character are considered part of a recipe, so any `define` or `endef` strings appearing on such a line will not be considered `make` directives.

```
define two-lines
echo foo
echo $(bar)
endef
```

When used in a recipe, the previous example is functionally equivalent to this:

```
two-lines = echo foo; echo $(bar)
```

since two commands separated by semicolon behave much like two separate shell commands. However, note that using two separate lines means `make` will invoke the shell twice, running an independent sub-shell for each line. See Recipe Execution.

If you want variable definitions made with `define` to take precedence over command-line variable definitions, you can use the `override` directive together with `define`:

```
override define two-lines =
foo
$(bar)
endef
```

See The `override` Directive.

Next: Variables from the Environment, Previous: Defining Multi-Line Variables, Up: How to Use Variables   [Contents][Index]

### 6.9 Undefining Variables

If you want to clear a variable, setting its value to empty is usually sufficient. Expanding such a variable will yield the same result (empty string) regardless of whether it was set or not. However, if you are using the `flavor` (see The `flavor` Function) and `origin` (see The `origin` Function) functions, there is a difference between a variable that was never set and a variable with an empty value. In such situations you may want to use the `undefine` directive to make a variable appear as if it was never set. For example:

```
foo := foo
bar = bar

undefine foo
undefine bar

$(info $(origin foo))
$(info $(flavor bar))
```

This example will print “undefined” for both variables.

If you want to undefine a command-line variable definition, you can use the `override` directive together with `undefine`, similar to how this is done for variable definitions:

```
override undefine CFLAGS
```

Next: Target-specific Variable Values, Previous: Undefining Variables, Up: How to Use Variables   [Contents][Index]

### 6.10 Variables from the Environment

Variables in `make` can come from the environment in which `make` is run. Every environment variable that `make` sees when it starts up is transformed into a `make` variable with the same name and value. However, an explicit assignment in the makefile, or with a command argument, overrides the environment. (If the ‘-e’ flag is specified, then values from the environment override assignments in the makefile. See Summary of Options. But this is not recommended practice.)

Thus, by setting the variable `CFLAGS` in your environment, you can cause all C compilations in most makefiles to use the compiler switches you prefer. This is safe for variables with standard or conventional meanings because you know that no makefile will use them for other things. (Note this is not totally reliable; some makefiles set `CFLAGS` explicitly and therefore are not affected by the value in the environment.)

When `make` runs a recipe, some variables defined in the makefile are placed into the environment of each command `make` invokes. By default, only variables that came from the `make`’s environment or set on its command line are placed into the environment of the commands. You can use the `export` directive to pass other variables. See Communicating Variables to a Sub-`make`, for full details.

Other use of variables from the environment is not recommended. It is not wise for makefiles to depend for their functioning on environment variables set up outside their control, since this would cause different users to get different results from the same makefile. This is against the whole purpose of most makefiles.

Such problems would be especially likely with the variable `SHELL`, which is normally present in the environment to specify the user’s choice of interactive shell. It would be very undesirable for this choice to affect `make`; so, `make` handles the `SHELL` environment variable in a special way; see Choosing the Shell.

Next: Pattern-specific Variable Values, Previous: Variables from the Environment, Up: How to Use Variables   [Contents][Index]

### 6.11 Target-specific Variable Values

Variable values in `make` are usually global; that is, they are the same regardless of where they are evaluated (unless they’re reset, of course). Exceptions to that are variables defined with the `let` function (see The `let` Function) or the `foreach` function (see The `foreach` Function, and automatic variables (see Automatic Variables).

Another exception are *target-specific variable values*. This feature allows you to define different values for the same variable, based on the target that `make` is currently building. As with automatic variables, these values are only available within the context of a target’s recipe (and in other target-specific assignments).

Set a target-specific variable value like this:

```
target … : variable-assignment
```

Target-specific variable assignments can be prefixed with any or all of the special keywords `export`, `unexport`, `override`, or `private`; these apply their normal behavior to this instance of the variable only.

Multiple *target* values create a target-specific variable value for each member of the target list individually.

The *variable-assignment* can be any valid form of assignment; recursive (‘=’), simple (‘:=’ or ‘::=’), immediate (‘::=’), appending (‘+=’), or conditional (‘?=’). All variables that appear within the *variable-assignment* are evaluated within the context of the target: thus, any previously-defined target-specific variable values will be in effect. Note that this variable is actually distinct from any “global” value: the two variables do not have to have the same flavor (recursive vs. simple).

Target-specific variables have the same priority as any other makefile variable. Variables provided on the command line (and in the environment if the ‘-e’ option is in force) will take precedence. Specifying the `override` directive will allow the target-specific variable value to be preferred.

There is one more special feature of target-specific variables: when you define a target-specific variable that variable value is also in effect for all prerequisites of this target, and all their prerequisites, etc. (unless those prerequisites override that variable with their own target-specific variable value). So, for example, a statement like this:

```
prog : CFLAGS = -g
prog : prog.o foo.o bar.o
```

will set `CFLAGS` to ‘-g’ in the recipe for prog, but it will also set `CFLAGS` to ‘-g’ in the recipes that create prog.o, foo.o, and bar.o, and any recipes which create their prerequisites.

Be aware that a given prerequisite will only be built once per invocation of make, at most. If the same file is a prerequisite of multiple targets, and each of those targets has a different value for the same target-specific variable, then the first target to be built will cause that prerequisite to be built and the prerequisite will inherit the target-specific value from the first target. It will ignore the target-specific values from any other targets.

Next: Suppressing Inheritance, Previous: Target-specific Variable Values, Up: How to Use Variables   [Contents][Index]

### 6.12 Pattern-specific Variable Values

In addition to target-specific variable values (see Target-specific Variable Values), GNU `make` supports pattern-specific variable values. In this form, the variable is defined for any target that matches the pattern specified.

Set a pattern-specific variable value like this:

```
pattern … : variable-assignment
```

where *pattern* is a %-pattern. As with target-specific variable values, multiple *pattern* values create a pattern-specific variable value for each pattern individually. The *variable-assignment* can be any valid form of assignment. Any command line variable setting will take precedence, unless `override` is specified.

For example:

```
%.o : CFLAGS = -O
```

will assign `CFLAGS` the value of ‘-O’ for all targets matching the pattern `%.o`.

If a target matches more than one pattern, the matching pattern-specific variables with longer stems are interpreted first. This results in more specific variables taking precedence over the more generic ones, for example:

```
%.o: %.c
        $(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@

lib/%.o: CFLAGS := -fPIC -g
%.o: CFLAGS := -g

all: foo.o lib/bar.o
```

In this example the first definition of the `CFLAGS` variable will be used to update lib/bar.o even though the second one also applies to this target. Pattern-specific variables which result in the same stem length are considered in the order in which they were defined in the makefile.

Pattern-specific variables are searched after any target-specific variables defined explicitly for that target, and before target-specific variables defined for the parent target.

Next: Other Special Variables, Previous: Pattern-specific Variable Values, Up: How to Use Variables   [Contents][Index]

### 6.13 Suppressing Inheritance

As described in previous sections, `make` variables are inherited by prerequisites. This capability allows you to modify the behavior of a prerequisite based on which targets caused it to be rebuilt. For example, you might set a target-specific variable on a `debug` target, then running ‘make debug’ will cause that variable to be inherited by all prerequisites of `debug`, while just running ‘make all’ (for example) would not have that assignment.

Sometimes, however, you may not want a variable to be inherited. For these situations, `make` provides the `private` modifier. Although this modifier can be used with any variable assignment, it makes the most sense with target- and pattern-specific variables. Any variable marked `private` will be visible to its local target but will not be inherited by prerequisites of that target. A global variable marked `private` will be visible in the global scope but will not be inherited by any target, and hence will not be visible in any recipe.

As an example, consider this makefile:

```
EXTRA_CFLAGS =

prog: private EXTRA_CFLAGS = -L/usr/local/lib
prog: a.o b.o
```

Due to the `private` modifier, `a.o` and `b.o` will not inherit the `EXTRA_CFLAGS` variable assignment from the `prog` target.

Previous: Suppressing Inheritance, Up: How to Use Variables   [Contents][Index]

### 6.14 Other Special Variables

GNU `make` supports some variables that have special properties.

**`MAKEFILE_LIST`**

Contains the name of each makefile that is parsed by `make`, in the order in which it was parsed. The name is appended just before `make` begins to parse the makefile. Thus, if the first thing a makefile does is examine the last word in this variable, it will be the name of the current makefile. Once the current makefile has used `include`, however, the last word will be the just-included makefile.

If a makefile named `Makefile` has this content:

```
name1 := $(lastword $(MAKEFILE_LIST))

include inc.mk

name2 := $(lastword $(MAKEFILE_LIST))

all:
        @echo name1 = $(name1)
        @echo name2 = $(name2)
```

then you would expect to see this output:

```
name1 = Makefile
name2 = inc.mk
```

**`.DEFAULT_GOAL`**

Sets the default goal to be used if no targets were specified on the command line (see Arguments to Specify the Goals). The `.DEFAULT_GOAL` variable allows you to discover the current default goal, restart the default goal selection algorithm by clearing its value, or to explicitly set the default goal. The following example illustrates these cases:

```
# Query the default goal.
ifeq ($(.DEFAULT_GOAL),)
  $(warning no default goal is set)
endif

.PHONY: foo
foo: ; @echo $@

$(warning default goal is $(.DEFAULT_GOAL))

# Reset the default goal.
.DEFAULT_GOAL :=

.PHONY: bar
bar: ; @echo $@

$(warning default goal is $(.DEFAULT_GOAL))

# Set our own.
.DEFAULT_GOAL := foo
```

This makefile prints:

```
no default goal is set
default goal is foo
default goal is bar
foo
```

Note that assigning more than one target name to `.DEFAULT_GOAL` is invalid and will result in an error.

**`MAKE_RESTARTS`**

This variable is set only if this instance of `make` has restarted (see How Makefiles Are Remade): it will contain the number of times this instance has restarted. Note this is not the same as recursion (counted by the `MAKELEVEL` variable). You should not set, modify, or export this variable.

**`MAKE_TERMOUT`**

**`MAKE_TERMERR`**

When `make` starts it will check whether stdout and stderr will show their output on a terminal. If so, it will set `MAKE_TERMOUT` and `MAKE_TERMERR`, respectively, to the name of the terminal device (or `true` if this cannot be determined). If set these variables will be marked for export. These variables will not be changed by `make` and they will not be modified if already set.

These values can be used (particularly in combination with output synchronization (see Output During Parallel Execution) to determine whether `make` itself is writing to a terminal; they can be tested to decide whether to force recipe commands to generate colorized output for example.

If you invoke a sub-`make` and redirect its stdout or stderr it is your responsibility to reset or unexport these variables as well, if your makefiles rely on them.

**`.RECIPEPREFIX`**

The first character of the value of this variable is used as the character make assumes is introducing a recipe line. If the variable is empty (as it is by default) that character is the standard tab character. For example, this is a valid makefile:

```
.RECIPEPREFIX = >
all:
> @echo Hello, world
```

The value of `.RECIPEPREFIX` can be changed multiple times; once set it stays in effect for all rules parsed until it is modified.

**`.VARIABLES`**

Expands to a list of the *names* of all global variables defined so far. This includes variables which have empty values, as well as built-in variables (see Variables Used by Implicit Rules), but does not include any variables which are only defined in a target-specific context. Note that any value you assign to this variable will be ignored; it will always return its special value.

**`.FEATURES`**

Expands to a list of special features supported by this version of `make`. Possible values include, but are not limited to:

**‘archives’**

Supports `ar` (archive) files using special file name syntax. See Using `make` to Update Archive Files.

**‘check-symlink’**

Supports the `-L` (`--check-symlink-times`) flag. See Summary of Options.

**‘else-if’**

Supports “else if” non-nested conditionals. See Syntax of Conditionals.

**‘extra-prereqs’**

Supports the `.EXTRA_PREREQS` special target.

**‘grouped-target’**

Supports grouped target syntax for explicit rules. See Multiple Targets in a Rule.

**‘guile’**

Has GNU Guile available as an embedded extension language. See GNU Guile Integration.

**‘jobserver’**

Supports “job server” enhanced parallel builds. See Parallel Execution.

**‘jobserver-fifo’**

Supports “job server” enhanced parallel builds using named pipes. See Integrating GNU `make`.

**‘load’**

Supports dynamically loadable objects for creating custom extensions. See Loading Dynamic Objects.

**‘notintermediate’**

Supports the `.NOTINTERMEDIATE` special target. See Integrating GNU `make`.

**‘oneshell’**

Supports the `.ONESHELL` special target. See Using One Shell.

**‘order-only’**

Supports order-only prerequisites. See Types of Prerequisites.

**‘output-sync’**

Supports the `--output-sync` command line option. See Summary of Options.

**‘second-expansion’**

Supports secondary expansion of prerequisite lists.

**‘shell-export’**

Supports exporting `make` variables to `shell` functions.

**‘shortest-stem’**

Uses the “shortest stem” method of choosing which pattern, of multiple applicable options, will be used. See How Patterns Match.

**‘target-specific’**

Supports target-specific and pattern-specific variable assignments. See Target-specific Variable Values.

**‘undefine’**

Supports the `undefine` directive. See Undefining Variables.

**`.INCLUDE_DIRS`**

Expands to a list of directories that `make` searches for included makefiles (see Including Other Makefiles). Note that modifying this variable’s value does not change the list of directories which are searched.

**`.EXTRA_PREREQS`**

Each word in this variable is a new prerequisite which is added to targets for which it is set. These prerequisites differ from normal prerequisites in that they do not appear in any of the automatic variables (see Automatic Variables). This allows prerequisites to be defined which do not impact the recipe.

Consider a rule to link a program:

```
myprog: myprog.o file1.o file2.o
       $(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LDLIBS)
```

Now suppose you want to enhance this makefile to ensure that updates to the compiler cause the program to be re-linked. You can add the compiler as a prerequisite, but you must ensure that it’s not passed as an argument to link command. You’ll need something like this:

```
myprog: myprog.o file1.o file2.o $(CC)
       $(CC) $(CFLAGS) $(LDFLAGS) -o $@ \
           $(filter-out $(CC),$^) $(LDLIBS)
```

Then consider having multiple extra prerequisites: they would all have to be filtered out. Using `.EXTRA_PREREQS` and target-specific variables provides a simpler solution:

```
myprog: myprog.o file1.o file2.o
       $(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LDLIBS)
myprog: .EXTRA_PREREQS = $(CC)
```

This feature can also be useful if you want to add prerequisites to a makefile you cannot easily modify: you can create a new file such as extra.mk:

```
myprog: .EXTRA_PREREQS = $(CC)
```

then invoke `make -f extra.mk -f Makefile`.

Setting `.EXTRA_PREREQS` globally will cause those prerequisites to be added to all targets (which did not themselves override it with a target-specific value). Note `make` is smart enough not to add a prerequisite listed in `.EXTRA_PREREQS` as a prerequisite to itself.

Next: Functions for Transforming Text, Previous: How to Use Variables, Up: GNU `make`   [Contents][Index]


## 7 Conditional Parts of Makefiles

A *conditional* directive causes part of a makefile to be obeyed or ignored depending on the values of variables. Conditionals can compare the value of one variable to another, or the value of a variable to a constant string. Conditionals control what `make` actually “sees” in the makefile, so they *cannot* be used to control recipes at the time of execution.

Next: Syntax of Conditionals, Previous: Conditional Parts of Makefiles, Up: Conditional Parts of Makefiles   [Contents][Index]

### 7.1 Example of a Conditional

The following example of a conditional tells `make` to use one set of libraries if the `CC` variable is ‘gcc’, and a different set of libraries otherwise. It works by controlling which of two recipe lines will be used for the rule. The result is that ‘CC=gcc’ as an argument to `make` changes not only which compiler is used but also which libraries are linked.

```
libs_for_gcc = -lgnu
normal_libs =

foo: $(objects)
ifeq ($(CC),gcc)
        $(CC) -o foo $(objects) $(libs_for_gcc)
else
        $(CC) -o foo $(objects) $(normal_libs)
endif
```

This conditional uses three directives: one `ifeq`, one `else` and one `endif`.

The `ifeq` directive begins the conditional, and specifies the condition. It contains two arguments, separated by a comma and surrounded by parentheses. Variable substitution is performed on both arguments and then they are compared. The lines of the makefile following the `ifeq` are obeyed if the two arguments match; otherwise they are ignored.

The `else` directive causes the following lines to be obeyed if the previous conditional failed. In the example above, this means that the second alternative linking command is used whenever the first alternative is not used. It is optional to have an `else` in a conditional.

The `endif` directive ends the conditional. Every conditional must end with an `endif`. Unconditional makefile text follows.

As this example illustrates, conditionals work at the textual level: the lines of the conditional are treated as part of the makefile, or ignored, according to the condition. This is why the larger syntactic units of the makefile, such as rules, may cross the beginning or the end of the conditional.

When the variable `CC` has the value ‘gcc’, the above example has this effect:

```
foo: $(objects)
        $(CC) -o foo $(objects) $(libs_for_gcc)
```

When the variable `CC` has any other value, the effect is this:

```
foo: $(objects)
        $(CC) -o foo $(objects) $(normal_libs)
```

Equivalent results can be obtained in another way by conditionalizing a variable assignment and then using the variable unconditionally:

```
libs_for_gcc = -lgnu
normal_libs =

ifeq ($(CC),gcc)
  libs=$(libs_for_gcc)
else
  libs=$(normal_libs)
endif

foo: $(objects)
        $(CC) -o foo $(objects) $(libs)
```

Next: Conditionals that Test Flags, Previous: Example of a Conditional, Up: Conditional Parts of Makefiles   [Contents][Index]

### 7.2 Syntax of Conditionals

The syntax of a simple conditional with no `else` is as follows:

```
conditional-directive
text-if-true
endif
```

The *text-if-true* may be any lines of text, to be considered as part of the makefile if the condition is true. If the condition is false, no text is used instead.

The syntax of a complex conditional is as follows:

```
conditional-directive
text-if-true
else
text-if-false
endif
```

or:

```
conditional-directive-one
text-if-one-is-true
else conditional-directive-two
text-if-two-is-true
else
text-if-one-and-two-are-false
endif
```

There can be as many “`else` *conditional-directive*” clauses as necessary. Once a given condition is true, *text-if-true* is used and no other clause is used; if no condition is true then *text-if-false* is used. The *text-if-true* and *text-if-false* can be any number of lines of text.

The syntax of the *conditional-directive* is the same whether the conditional is simple or complex; after an `else` or not. There are four different directives that test different conditions. Here is a table of them:

**`ifeq (*arg1*, *arg2*)`**

**`ifeq '*arg1*' '*arg2*'`**

**`ifeq "*arg1*" "*arg2*"`**

**`ifeq "*arg1*" '*arg2*'`**

**`ifeq '*arg1*' "*arg2*"`**

Expand all variable references in *arg1* and *arg2* and compare them. If they are identical, the *text-if-true* is effective; otherwise, the *text-if-false*, if any, is effective.

Often you want to test if a variable has a non-empty value. When the value results from complex expansions of variables and functions, expansions you would consider empty may actually contain whitespace characters and thus are not seen as empty. However, you can use the `strip` function (see Functions for String Substitution and Analysis) to avoid interpreting whitespace as a non-empty value. For example:

```
ifeq ($(strip $(foo)),)
text-if-empty
endif
```

will evaluate *text-if-empty* even if the expansion of `$(foo)` contains whitespace characters.

**`ifneq (*arg1*, *arg2*)`**

**`ifneq '*arg1*' '*arg2*'`**

**`ifneq "*arg1*" "*arg2*"`**

**`ifneq "*arg1*" '*arg2*'`**

**`ifneq '*arg1*' "*arg2*"`**

Expand all variable references in *arg1* and *arg2* and compare them. If they are different, the *text-if-true* is effective; otherwise, the *text-if-false*, if any, is effective.

**`ifdef *variable-name*`**

The `ifdef` form takes the *name* of a variable as its argument, not a reference to a variable. If the value of that variable has a non-empty value, the *text-if-true* is effective; otherwise, the *text-if-false*, if any, is effective. Variables that have never been defined have an empty value. The text *variable-name* is expanded, so it could be a variable or function that expands to the name of a variable. For example:

```
bar = true
foo = bar
ifdef $(foo)
frobozz = yes
endif
```

The variable reference `$(foo)` is expanded, yielding `bar`, which is considered to be the name of a variable. The variable `bar` is not expanded, but its value is examined to determine if it is non-empty.

Note that `ifdef` only tests whether a variable has a value. It does not expand the variable to see if that value is nonempty. Consequently, tests using `ifdef` return true for all definitions except those like `foo =`. To test for an empty value, use `ifeq ($(foo),)`. For example,

```
bar =
foo = $(bar)
ifdef foo
frobozz = yes
else
frobozz = no
endif
```

sets ‘frobozz’ to ‘yes’, while:

```
foo =
ifdef foo
frobozz = yes
else
frobozz = no
endif
```

sets ‘frobozz’ to ‘no’.

**`ifndef *variable-name*`**

If the variable *variable-name* has an empty value, the *text-if-true* is effective; otherwise, the *text-if-false*, if any, is effective. The rules for expansion and testing of *variable-name* are identical to the `ifdef` directive.

Extra spaces are allowed and ignored at the beginning of the conditional directive line, but a tab is not allowed. (If the line begins with a tab, it will be considered part of a recipe for a rule.) Aside from this, extra spaces or tabs may be inserted with no effect anywhere except within the directive name or within an argument. A comment starting with ‘#’ may appear at the end of the line.

The other two directives that play a part in a conditional are `else` and `endif`. Each of these directives is written as one word, with no arguments. Extra spaces are allowed and ignored at the beginning of the line, and spaces or tabs at the end. A comment starting with ‘#’ may appear at the end of the line.

Conditionals affect which lines of the makefile `make` uses. If the condition is true, `make` reads the lines of the *text-if-true* as part of the makefile; if the condition is false, `make` ignores those lines completely. It follows that syntactic units of the makefile, such as rules, may safely be split across the beginning or the end of the conditional.

`make` evaluates conditionals when it reads a makefile. Consequently, you cannot use automatic variables in the tests of conditionals because they are not defined until recipes are run (see Automatic Variables).

To prevent intolerable confusion, it is not permitted to start a conditional in one makefile and end it in another. However, you may write an `include` directive within a conditional, provided you do not attempt to terminate the conditional inside the included file.

Previous: Syntax of Conditionals, Up: Conditional Parts of Makefiles   [Contents][Index]

### 7.3 Conditionals that Test Flags

You can write a conditional that tests `make` command flags such as ‘-t’ by using the variable `MAKEFLAGS` together with the `findstring` function (see Functions for String Substitution and Analysis). This is useful when `touch` is not enough to make a file appear up to date.

Recall that `MAKEFLAGS` will put all single-letter options (such as ‘-t’) into the first word, and that word will be empty if no single-letter options were given. To work with this, it’s helpful to add a value at the start to ensure there’s a word: for example ‘-$(MAKEFLAGS)’.

The `findstring` function determines whether one string appears as a substring of another. If you want to test for the ‘-t’ flag, use ‘t’ as the first string and the first word of `MAKEFLAGS` as the other.

For example, here is how to arrange to use ‘ranlib -t’ to finish marking an archive file up to date:

```
archive.a: …
ifneq (,$(findstring t,$(firstword -$(MAKEFLAGS))))
        +touch archive.a
        +ranlib -t archive.a
else
        ranlib archive.a
endif
```

The ‘+’ prefix marks those recipe lines as “recursive” so that they will be executed despite use of the ‘-t’ flag. See Recursive Use of `make`.

Next: How to Run `make`, Previous: Conditional Parts of Makefiles, Up: GNU `make`   [Contents][Index]
