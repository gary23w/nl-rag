---
title: "GNU make (part 2/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 2/17
---

## 3 Writing Makefiles

The information that tells `make` how to recompile a system comes from reading a data base called the *makefile*.

Next: Including Other Makefiles, Previous: What Makefiles Contain, Up: Writing Makefiles   [Contents][Index]

### 3.2 What Name to Give Your Makefile

By default, when `make` looks for the makefile, it tries the following names, in order: GNUmakefile, makefile and Makefile.

Normally you should call your makefile either makefile or Makefile. (We recommend Makefile because it appears prominently near the beginning of a directory listing, right near other important files such as README.) The first name checked, GNUmakefile, is not recommended for most makefiles. You should use this name if you have a makefile that is specific to GNU `make`, and will not be understood by other versions of `make`. Other `make` programs look for makefile and Makefile, but not GNUmakefile.

If `make` finds none of these names, it does not use any makefile. Then you must specify a goal with a command argument, and `make` will attempt to figure out how to remake it using only its built-in implicit rules. See Using Implicit Rules.

If you want to use a nonstandard name for your makefile, you can specify the makefile name with the ‘-f’ or ‘--file’ option. The arguments ‘-f *name*’ or ‘--file=*name*’ tell `make` to read the file *name* as the makefile. If you use more than one ‘-f’ or ‘--file’ option, you can specify several makefiles. All the makefiles are effectively concatenated in the order specified. The default makefile names GNUmakefile, makefile and Makefile are not checked automatically if you specify ‘-f’ or ‘--file’.

Next: The Variable `MAKEFILES`, Previous: What Name to Give Your Makefile, Up: Writing Makefiles   [Contents][Index]

### 3.3 Including Other Makefiles

The `include` directive tells `make` to suspend reading the current makefile and read one or more other makefiles before continuing. The directive is a line in the makefile that looks like this:

```
include filenames…
```

*filenames* can contain shell file name patterns. If *filenames* is empty, nothing is included and no error is printed.

Extra spaces are allowed and ignored at the beginning of the line, but the first character must not be a tab (or the value of `.RECIPEPREFIX`)—if the line begins with a tab, it will be considered a recipe line. Whitespace is required between `include` and the file names, and between file names; extra whitespace is ignored there and at the end of the directive. A comment starting with ‘#’ is allowed at the end of the line. If the file names contain any variable or function references, they are expanded. See How to Use Variables.

For example, if you have three .mk files, a.mk, b.mk, and c.mk, and `$(bar)` expands to `bish bash`, then the following expression

```
include foo *.mk $(bar)
```

is equivalent to

```
include foo a.mk b.mk c.mk bish bash
```

When `make` processes an `include` directive, it suspends reading of the containing makefile and reads from each listed file in turn. When that is finished, `make` resumes reading the makefile in which the directive appears.

One occasion for using `include` directives is when several programs, handled by individual makefiles in various directories, need to use a common set of variable definitions (see Setting Variables) or pattern rules (see Defining and Redefining Pattern Rules).

Another such occasion is when you want to generate prerequisites from source files automatically; the prerequisites can be put in a file that is included by the main makefile. This practice is generally cleaner than that of somehow appending the prerequisites to the end of the main makefile as has been traditionally done with other versions of `make`. See Generating Prerequisites Automatically.

If the specified name does not start with a slash (or a drive letter and colon when GNU Make is compiled with MS-DOS / MS-Windows path support), and the file is not found in the current directory, several other directories are searched. First, any directories you have specified with the ‘-I’ or ‘--include-dir’ options are searched (see Summary of Options). Then the following directories (if they exist) are searched, in this order: *prefix*/include (normally /usr/local/include 1) /usr/gnu/include, /usr/local/include, /usr/include.

The `.INCLUDE_DIRS` variable will contain the current list of directories that make will search for included files. See Other Special Variables.

You can avoid searching in these default directories by adding the command line option `-I` with the special value `-` (e.g., `-I-`) to the command line. This will cause `make` to forget any already-set include directories, including the default directories.

If an included makefile cannot be found in any of these directories it is not an immediately fatal error; processing of the makefile containing the `include` continues. Once it has finished reading makefiles, `make` will try to remake any that are out of date or don’t exist. See How Makefiles Are Remade. Only after it has failed to find a rule to remake the makefile, or it found a rule but the recipe failed, will `make` diagnose the missing makefile as a fatal error.

If you want `make` to simply ignore a makefile which does not exist or cannot be remade, with no error message, use the `-include` directive instead of `include`, like this:

```
-include filenames…
```

This acts like `include` in every way except that there is no error (not even a warning) if any of the *filenames* (or any prerequisites of any of the *filenames*) do not exist or cannot be remade.

For compatibility with some other `make` implementations, `sinclude` is another name for `-include`.

Next: How Makefiles Are Remade, Previous: Including Other Makefiles, Up: Writing Makefiles   [Contents][Index]

### 3.4 The Variable `MAKEFILES`

If the environment variable `MAKEFILES` is defined, `make` considers its value as a list of names (separated by whitespace) of additional makefiles to be read before the others. This works much like the `include` directive: various directories are searched for those files (see Including Other Makefiles). In addition, the default goal is never taken from one of these makefiles (or any makefile included by them) and it is not an error if the files listed in `MAKEFILES` are not found.

The main use of `MAKEFILES` is in communication between recursive invocations of `make` (see Recursive Use of `make`). It usually is not desirable to set the environment variable before a top-level invocation of `make`, because it is usually better not to mess with a makefile from outside. However, if you are running `make` without a specific makefile, a makefile in `MAKEFILES` can do useful things to help the built-in implicit rules work better, such as defining search paths (see Searching Directories for Prerequisites).

Some users are tempted to set `MAKEFILES` in the environment automatically on login, and program makefiles to expect this to be done. This is a very bad idea, because such makefiles will fail to work if run by anyone else. It is much better to write explicit `include` directives in the makefiles. See Including Other Makefiles.

Next: Overriding Part of Another Makefile, Previous: The Variable `MAKEFILES`, Up: Writing Makefiles   [Contents][Index]

### 3.5 How Makefiles Are Remade

Sometimes makefiles can be remade from other files, such as RCS or SCCS files. If a makefile can be remade from other files, you probably want `make` to get an up-to-date version of the makefile to read in.

To this end, after reading in all makefiles `make` will consider each as a goal target, in the order in which they were processed, and attempt to update it. If parallel builds (see Parallel Execution) are enabled then makefiles will be rebuilt in parallel as well.

If a makefile has a rule which says how to update it (found either in that very makefile or in another one) or if an implicit rule applies to it (see Using Implicit Rules), it will be updated if necessary. After all makefiles have been checked, if any have actually been changed, `make` starts with a clean slate and reads all the makefiles over again. (It will also attempt to update each of them over again, but normally this will not change them again, since they are already up to date.) Each restart will cause the special variable `MAKE_RESTARTS` to be updated (see Other Special Variables).

If you know that one or more of your makefiles cannot be remade and you want to keep `make` from performing an implicit rule search on them, perhaps for efficiency reasons, you can use any normal method of preventing implicit rule look-up to do so. For example, you can write an explicit rule with the makefile as the target, and an empty recipe (see Using Empty Recipes).

If the makefiles specify a double-colon rule to remake a file with a recipe but no prerequisites, that file will always be remade (see Double-Colon Rules). In the case of makefiles, a makefile that has a double-colon rule with a recipe but no prerequisites will be remade every time `make` is run, and then again after `make` starts over and reads the makefiles in again. This would cause an infinite loop: `make` would constantly remake the makefile and restart, and never do anything else. So, to avoid this, `make` will **not** attempt to remake makefiles which are specified as targets of a double-colon rule with a recipe but no prerequisites.

Phony targets (see Phony Targets) have the same effect: they are never considered up-to-date and so an included file marked as phony would cause `make` to restart continuously. To avoid this `make` will not attempt to remake makefiles which are marked phony.

You can take advantage of this to optimize startup time: if you know you don’t need your Makefile to be remade you can prevent make from trying to remake it by adding either:

```
.PHONY: Makefile
```

or:

```
Makefile:: ;
```

If you do not specify any makefiles to be read with ‘-f’ or ‘--file’ options, `make` will try the default makefile names; see What Name to Give Your Makefile. Unlike makefiles explicitly requested with ‘-f’ or ‘--file’ options, `make` is not certain that these makefiles should exist. However, if a default makefile does not exist but can be created by running `make` rules, you probably want the rules to be run so that the makefile can be used.

Therefore, if none of the default makefiles exists, `make` will try to make each of them until it succeeds in making one, or it runs out of names to try. Note that it is not an error if `make` cannot find or make any makefile; a makefile is not always necessary.

When you use the ‘-t’ or ‘--touch’ option (see Instead of Executing Recipes), you would not want to use an out-of-date makefile to decide which targets to touch. So the ‘-t’ option has no effect on updating makefiles; they are really updated even if ‘-t’ is specified. Likewise, ‘-q’ (or ‘--question’) and ‘-n’ (or ‘--just-print’) do not prevent updating of makefiles, because an out-of-date makefile would result in the wrong output for other targets. Thus, ‘make -f mfile -n foo’ will update mfile, read it in, and then print the recipe to update foo and its prerequisites without running it. The recipe printed for foo will be the one specified in the updated contents of mfile.

However, on occasion you might actually wish to prevent updating of even the makefiles. You can do this by specifying the makefiles as goals in the command line as well as specifying them as makefiles. When the makefile name is specified explicitly as a goal, the options ‘-t’ and so on do apply to them.

Thus, ‘make -f mfile -n mfile foo’ would read the makefile mfile, print the recipe needed to update it without actually running it, and then print the recipe needed to update foo without running that. The recipe for foo will be the one specified by the existing contents of mfile.

Next: How `make` Reads a Makefile, Previous: How Makefiles Are Remade, Up: Writing Makefiles   [Contents][Index]

### 3.6 Overriding Part of Another Makefile

Sometimes it is useful to have a makefile that is mostly just like another makefile. You can often use the ‘include’ directive to include one in the other, and add more targets or variable definitions. However, it is invalid for two makefiles to give different recipes for the same target. But there is another way.

In the containing makefile (the one that wants to include the other), you can use a match-anything pattern rule to say that to remake any target that cannot be made from the information in the containing makefile, `make` should look in another makefile. See Defining and Redefining Pattern Rules, for more information on pattern rules.

For example, if you have a makefile called Makefile that says how to make the target ‘foo’ (and other targets), you can write a makefile called GNUmakefile that contains:

```
foo:
        frobnicate > foo

%: force
        @$(MAKE) -f Makefile $@
force: ;
```

If you say ‘make foo’, `make` will find GNUmakefile, read it, and see that to make foo, it needs to run the recipe ‘frobnicate > foo’. If you say ‘make bar’, `make` will find no way to make bar in GNUmakefile, so it will use the recipe from the pattern rule: ‘make -f Makefile bar’. If Makefile provides a rule for updating bar, `make` will apply the rule. And likewise for any other target that GNUmakefile does not say how to make.

The way this works is that the pattern rule has a pattern of just ‘%’, so it matches any target whatever. The rule specifies a prerequisite force, to guarantee that the recipe will be run even if the target file already exists. We give the force target an empty recipe to prevent `make` from searching for an implicit rule to build it—otherwise it would apply the same match-anything rule to force itself and create a prerequisite loop!

Next: How Makefiles Are Parsed, Previous: Overriding Part of Another Makefile, Up: Writing Makefiles   [Contents][Index]

### 3.7 How `make` Reads a Makefile

GNU `make` does its work in two distinct phases. During the first phase it reads all the makefiles, included makefiles, etc. and internalizes all the variables and their values and implicit and explicit rules, and builds a dependency graph of all the targets and their prerequisites. During the second phase, `make` uses this internalized data to determine which targets need to be updated and run the recipes necessary to update them.

It’s important to understand this two-phase approach because it has a direct impact on how variable and function expansion happens; this is often a source of some confusion when writing makefiles. Below is a summary of the different constructs that can be found in a makefile, and the phase in which expansion happens for each part of the construct.

We say that expansion is *immediate* if it happens during the first phase: `make` will expand that part of the construct as the makefile is parsed. We say that expansion is *deferred* if it is not immediate. Expansion of a deferred construct part is delayed until the expansion is used: either when it is referenced in an immediate context, or when it is needed during the second phase.

You may not be familiar with some of these constructs yet. You can reference this section as you become familiar with them, in later chapters.

#### Variable Assignment

Variable definitions are parsed as follows:

```
immediate = deferred
immediate ?= deferred
immediate := immediate
immediate ::= immediate
immediate :::= immediate-with-escape
immediate += deferred or immediate
immediate != immediate

define immediate
  deferred
endef

define immediate =
  deferred
endef

define immediate ?=
  deferred
endef

define immediate :=
  immediate
endef

define immediate ::=
  immediate
endef

define immediate :::=
  immediate-with-escape
endef

define immediate +=
  deferred or immediate
endef

define immediate !=
  immediate
endef
```

For the append operator ‘+=’, the right-hand side is considered immediate if the variable was previously set as a simple variable (‘:=’ or ‘::=’), and deferred otherwise.

For the *immediate-with-escape* operator ‘:::=’, the value on the right-hand side is immediately expanded but then escaped (that is, all instances of `$` in the result of the expansion are replaced with `$$`).

For the shell assignment operator ‘!=’, the right-hand side is evaluated immediately and handed to the shell. The result is stored in the variable named on the left, and that variable is considered a recursively expanded variable (and will thus be re-evaluated on each reference).

#### Conditional Directives

Conditional directives are parsed immediately. This means, for example, that automatic variables cannot be used in conditional directives, as automatic variables are not set until the recipe for that rule is invoked. If you need to use automatic variables in a conditional directive you *must* move the condition into the recipe and use shell conditional syntax instead.

#### Rule Definition

A rule is always expanded the same way, regardless of the form:

```
immediate : immediate ; deferred
        deferred
```

That is, the target and prerequisite sections are expanded immediately, and the recipe used to build the target is always deferred. This is true for explicit rules, pattern rules, suffix rules, static pattern rules, and simple prerequisite definitions.

Next: Secondary Expansion, Previous: How `make` Reads a Makefile, Up: Writing Makefiles   [Contents][Index]

### 3.8 How Makefiles Are Parsed

GNU `make` parses makefiles line-by-line. Parsing proceeds using the following steps:

1. Read in a full logical line, including backslash-escaped lines (see Splitting Long Lines).
2. Remove comments (see What Makefiles Contain).
3. If the line begins with the recipe prefix character and we are in a rule context, add the line to the current recipe and read the next line (see Recipe Syntax).
4. Expand elements of the line which appear in an *immediate* expansion context (see How `make` Reads a Makefile).
5. Scan the line for a separator character, such as ‘:’ or ‘=’, to determine whether the line is a macro assignment or a rule (see Recipe Syntax).
6. Internalize the resulting operation and read the next line.

An important consequence of this is that a macro can expand to an entire rule, *if it is one line long*. This will work:

```
myrule = target : ; echo built

$(myrule)
```

However, this will not work because `make` does not re-split lines after it has expanded them:

```
define myrule
target:
        echo built
endef

$(myrule)
```

The above makefile results in the definition of a target ‘target’ with prerequisites ‘echo’ and ‘built’, as if the makefile contained `target: echo built`, rather than a rule with a recipe. Newlines still present in a line after expansion is complete are ignored as normal whitespace.

In order to properly expand a multi-line macro you must use the `eval` function: this causes the `make` parser to be run on the results of the expanded macro (see The `eval` Function).

Previous: How Makefiles Are Parsed, Up: Writing Makefiles   [Contents][Index]

### 3.9 Secondary Expansion

Previously we learned that GNU `make` works in two distinct phases: a read-in phase and a target-update phase (see How `make` Reads a Makefile). GNU Make also has the ability to enable a *second expansion* of the prerequisites (only) for some or all targets defined in the makefile. In order for this second expansion to occur, the special target `.SECONDEXPANSION` must be defined before the first prerequisite list that makes use of this feature.

If `.SECONDEXPANSION` is defined then when GNU `make` needs to check the prerequisites of a target, the prerequisites are expanded a *second time*. In most circumstances this secondary expansion will have no effect, since all variable and function references will have been expanded during the initial parsing of the makefiles. In order to take advantage of the secondary expansion phase of the parser, then, it’s necessary to *escape* the variable or function reference in the makefile. In this case the first expansion merely un-escapes the reference but doesn’t expand it, and expansion is left to the secondary expansion phase. For example, consider this makefile:

```
.SECONDEXPANSION:
ONEVAR = onefile
TWOVAR = twofile
myfile: $(ONEVAR) $$(TWOVAR)
```

After the first expansion phase the prerequisites list of the myfile target will be `onefile` and `$(TWOVAR)`; the first (unescaped) variable reference to *ONEVAR* is expanded, while the second (escaped) variable reference is simply unescaped, without being recognized as a variable reference. Now during the secondary expansion the first word is expanded again but since it contains no variable or function references it remains the value onefile, while the second word is now a normal reference to the variable *TWOVAR*, which is expanded to the value twofile. The final result is that there are two prerequisites, onefile and twofile.

Obviously, this is not a very interesting case since the same result could more easily have been achieved simply by having both variables appear, unescaped, in the prerequisites list. One difference becomes apparent if the variables are reset; consider this example:

```
.SECONDEXPANSION:
AVAR = top
onefile: $(AVAR)
twofile: $$(AVAR)
AVAR = bottom
```

Here the prerequisite of onefile will be expanded immediately, and resolve to the value top, while the prerequisite of twofile will not be full expanded until the secondary expansion and yield a value of bottom.

This is marginally more exciting, but the true power of this feature only becomes apparent when you discover that secondary expansions always take place within the scope of the automatic variables for that target. This means that you can use variables such as `$@`, `$*`, etc. during the second expansion and they will have their expected values, just as in the recipe. All you have to do is defer the expansion by escaping the `$`. Also, secondary expansion occurs for both explicit and implicit (pattern) rules. Knowing this, the possible uses for this feature increase dramatically. For example:

```
.SECONDEXPANSION:
main_OBJS := main.o try.o test.o
lib_OBJS := lib.o api.o

main lib: $$($$@_OBJS)
```

Here, after the initial expansion the prerequisites of both the main and lib targets will be `$($@_OBJS)`. During the secondary expansion, the `$@` variable is set to the name of the target and so the expansion for the main target will yield `$(main_OBJS)`, or `main.o try.o test.o`, while the secondary expansion for the lib target will yield `$(lib_OBJS)`, or `lib.o api.o`.

You can also mix in functions here, as long as they are properly escaped:

```
main_SRCS := main.c try.c test.c
lib_SRCS := lib.c api.c

.SECONDEXPANSION:
main lib: $$(patsubst %.c,%.o,$$($$@_SRCS))
```

This version allows users to specify source files rather than object files, but gives the same resulting prerequisites list as the previous example.

Evaluation of automatic variables during the secondary expansion phase, especially of the target name variable `$$@`, behaves similarly to evaluation within recipes. However, there are some subtle differences and “corner cases” which come into play for the different types of rule definitions that `make` understands. The subtleties of using the different automatic variables are described below.

#### Secondary Expansion of Explicit Rules

During the secondary expansion of explicit rules, `$$@` and `$$%` evaluate, respectively, to the file name of the target and, when the target is an archive member, the target member name. The `$$<` variable evaluates to the first prerequisite in the first rule for this target. `$$^` and `$$+` evaluate to the list of all prerequisites of rules *that have already appeared* for the same target (`$$+` with repetitions and `$$^` without). The following example will help illustrate these behaviors:

```
.SECONDEXPANSION:

foo: foo.1 bar.1 $$< $$^ $$+    # line #1

foo: foo.2 bar.2 $$< $$^ $$+    # line #2

foo: foo.3 bar.3 $$< $$^ $$+    # line #3
```

In the first prerequisite list, all three variables (`$$<`, `$$^`, and `$$+`) expand to the empty string. In the second, they will have values `foo.1`, `foo.1 bar.1`, and `foo.1 bar.1` respectively. In the third they will have values `foo.1`, `foo.1 bar.1 foo.2 bar.2`, and `foo.1 bar.1 foo.2 bar.2 foo.1 foo.1 bar.1 foo.1 bar.1` respectively.

Rules undergo secondary expansion in makefile order, except that the rule with the recipe is always evaluated last.

The variables `$$?` and `$$*` are not available and expand to the empty string.

#### Secondary Expansion of Static Pattern Rules

Rules for secondary expansion of static pattern rules are identical to those for explicit rules, above, with one exception: for static pattern rules the `$$*` variable is set to the pattern stem. As with explicit rules, `$$?` is not available and expands to the empty string.

#### Secondary Expansion of Implicit Rules

As `make` searches for an implicit rule, it substitutes the stem and then performs secondary expansion for every rule with a matching target pattern. The value of the automatic variables is derived in the same fashion as for static pattern rules. As an example:

```
.SECONDEXPANSION:

foo: bar

foo foz: fo%: bo%

%oo: $$< $$^ $$+ $$*
```

When the implicit rule is tried for target foo, `$$<` expands to bar, `$$^` expands to bar boo, `$$+` also expands to bar boo, and `$$*` expands to f.

Note that the directory prefix (D), as described in Implicit Rule Search Algorithm, is appended (after expansion) to all the patterns in the prerequisites list. As an example:

```
.SECONDEXPANSION:

/tmp/foo.o:

%.o: $$(addsuffix /%.c,foo bar) foo.h
        @echo $^
```

The prerequisite list printed, after the secondary expansion and directory prefix reconstruction, will be /tmp/foo/foo.c /tmp/bar/foo.c foo.h. If you are not interested in this reconstruction, you can use `$$*` instead of `%` in the prerequisites list.

Next: Writing Recipes in Rules, Previous: Writing Makefiles, Up: GNU `make`   [Contents][Index]
