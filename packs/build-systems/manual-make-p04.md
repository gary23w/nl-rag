---
title: "GNU make (part 4/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 4/17
---

# GNU make

**`.DEFAULT`**

The recipe specified for `.DEFAULT` is used for any target for which no rules are found (either explicit rules or implicit rules). See Defining Last-Resort Default Rules. If a `.DEFAULT` recipe is specified, every file mentioned as a prerequisite, but not as a target in a rule, will have that recipe executed on its behalf. See Implicit Rule Search Algorithm.

**`.PRECIOUS` ¶**

The targets which `.PRECIOUS` depends on are given the following special treatment: if `make` is killed or interrupted during the execution of their recipes, the target is not deleted. See Interrupting or Killing `make`. Also, if the target is an intermediate file, it will not be deleted after it is no longer needed, as is normally done. See Chains of Implicit Rules. In this latter respect it overlaps with the `.SECONDARY` special target.

You can also list the target pattern of an implicit rule (such as ‘%.o’) as a prerequisite file of the special target `.PRECIOUS` to preserve intermediate files created by rules whose target patterns match that file’s name.

**`.INTERMEDIATE` ¶**

The targets which `.INTERMEDIATE` depends on are treated as intermediate files. See Chains of Implicit Rules. `.INTERMEDIATE` with no prerequisites has no effect.

**`.NOTINTERMEDIATE` ¶**

Prerequisites of the special target `.NOTINTERMEDIATE` are never considered intermediate files. See Chains of Implicit Rules. `.NOTINTERMEDIATE` with no prerequisites causes all targets to be treated as not intermediate.

If the prerequisite is a target pattern then targets that are built using that pattern rule are not considered intermediate.

**`.SECONDARY` ¶**

The targets which `.SECONDARY` depends on are treated as intermediate files, except that they are never automatically deleted. See Chains of Implicit Rules.

`.SECONDARY` can be used to avoid redundant rebuilds in some unusual situations. For example:

```
hello.bin: hello.o bye.o
        $(CC) -o $@ $^

%.o: %.c
        $(CC) -c -o $@ $<

.SECONDARY: hello.o bye.o
```

Suppose hello.bin is up to date in regards to the source files, *but* the object file hello.o is missing. Without `.SECONDARY` make would rebuild hello.o then rebuild hello.bin even though the source files had not changed. By declaring hello.o as `.SECONDARY` `make` will not need to rebuild it and won’t need to rebuild hello.bin either. Of course, if one of the source files *were* updated then all object files would be rebuilt so that the creation of hello.bin could succeed.

`.SECONDARY` with no prerequisites causes all targets to be treated as secondary (i.e., no target is removed because it is considered intermediate).

**`.SECONDEXPANSION`**

If `.SECONDEXPANSION` is mentioned as a target anywhere in the makefile, then all prerequisite lists defined *after* it appears will be expanded a second time after all makefiles have been read in. See Secondary Expansion.

**`.DELETE_ON_ERROR` ¶**

If `.DELETE_ON_ERROR` is mentioned as a target anywhere in the makefile, then `make` will delete the target of a rule if it has changed and its recipe exits with a nonzero exit status, just as it does when it receives a signal. See Errors in Recipes.

**`.IGNORE`**

If you specify prerequisites for `.IGNORE`, then `make` will ignore errors in execution of the recipe for those particular files. The recipe for `.IGNORE` (if any) is ignored.

If mentioned as a target with no prerequisites, `.IGNORE` says to ignore errors in execution of recipes for all files. This usage of ‘.IGNORE’ is supported only for historical compatibility. Since this affects every recipe in the makefile, it is not very useful; we recommend you use the more selective ways to ignore errors in specific recipes. See Errors in Recipes.

**`.LOW_RESOLUTION_TIME`**

If you specify prerequisites for `.LOW_RESOLUTION_TIME`, `make` assumes that these files are created by commands that generate low resolution time stamps. The recipe for the `.LOW_RESOLUTION_TIME` target are ignored.

The high resolution file time stamps of many modern file systems lessen the chance of `make` incorrectly concluding that a file is up to date. Unfortunately, some hosts do not provide a way to set a high resolution file time stamp, so commands like ‘cp -p’ that explicitly set a file’s time stamp must discard its sub-second part. If a file is created by such a command, you should list it as a prerequisite of `.LOW_RESOLUTION_TIME` so that `make` does not mistakenly conclude that the file is out of date. For example:

```
.LOW_RESOLUTION_TIME: dst
dst: src
        cp -p src dst
```

Since ‘cp -p’ discards the sub-second part of src’s time stamp, dst is typically slightly older than src even when it is up to date. The `.LOW_RESOLUTION_TIME` line causes `make` to consider dst to be up to date if its time stamp is at the start of the same second that src’s time stamp is in.

Due to a limitation of the archive format, archive member time stamps are always low resolution. You need not list archive members as prerequisites of `.LOW_RESOLUTION_TIME`, as `make` does this automatically.

**`.SILENT`**

If you specify prerequisites for `.SILENT`, then `make` will not print the recipe used to remake those particular files before executing them. The recipe for `.SILENT` is ignored.

If mentioned as a target with no prerequisites, `.SILENT` says not to print any recipes before executing them. You may also use more selective ways to silence specific recipe command lines. See Recipe Echoing. If you want to silence all recipes for a particular run of `make`, use the ‘-s’ or ‘--silent’ option (see Summary of Options).

**`.EXPORT_ALL_VARIABLES`**

Simply by being mentioned as a target, this tells `make` to export all variables to child processes by default. This is an alternative to using `export` with no arguments. See Communicating Variables to a Sub-`make`.

**`.NOTPARALLEL` ¶**

If `.NOTPARALLEL` is mentioned as a target with no prerequisites, all targets in this invocation of `make` will be run serially, even if the ‘-j’ option is given. Any recursively invoked `make` command will still run recipes in parallel (unless its makefile also contains this target).

If `.NOTPARALLEL` has targets as prerequisites, then all the prerequisites of those targets will be run serially. This implicitly adds a `.WAIT` between each prerequisite of the listed targets. See Disabling Parallel Execution.

**`.ONESHELL` ¶**

If `.ONESHELL` is mentioned as a target, then when a target is built all lines of the recipe will be given to a single invocation of the shell rather than each line being invoked separately. See Recipe Execution.

**`.POSIX` ¶**

If `.POSIX` is mentioned as a target, then the makefile will be parsed and run in POSIX-conforming mode. This does *not* mean that only POSIX-conforming makefiles will be accepted: all advanced GNU `make` features are still available. Rather, this target causes `make` to behave as required by POSIX in those areas where `make`’s default behavior differs.

In particular, if this target is mentioned then recipes will be invoked as if the shell had been passed the `-e` flag: the first failing command in a recipe will cause the recipe to fail immediately.

Any defined implicit rule suffix also counts as a special target if it appears as a target, and so does the concatenation of two suffixes, such as ‘.c.o’. These targets are suffix rules, an obsolete way of defining implicit rules (but a way still widely used). In principle, any target name could be special in this way if you break it in two and add both pieces to the suffix list. In practice, suffixes normally begin with ‘.’, so these special target names also begin with ‘.’. See Old-Fashioned Suffix Rules.

Next: Multiple Rules for One Target, Previous: Special Built-in Target Names, Up: Writing Rules   [Contents][Index]

### 4.10 Multiple Targets in a Rule

When an explicit rule has multiple targets they can be treated in one of two possible ways: as independent targets or as grouped targets. The manner in which they are treated is determined by the separator that appears after the list of targets.

#### Rules with Independent Targets

Rules that use the standard target separator, `:`, define independent targets. This is equivalent to writing the same rule once for each target, with duplicated prerequisites and recipes. Typically, the recipe would use automatic variables such as ‘$@’ to specify which target is being built.

Rules with independent targets are useful in two cases:

- You want just prerequisites, no recipe. For example: kbd.o command.o files.o: command.h gives an additional prerequisite to each of the three object files mentioned. It is equivalent to writing: kbd.o: command.h command.o: command.h files.o: command.h
- Similar recipes work for all the targets. The automatic variable ‘$@’ can be used to substitute the particular target to be remade into the commands (see Automatic Variables). For example: bigoutput littleoutput : text.g generate text.g -$(subst output,,$@) > $@ is equivalent to bigoutput : text.g generate text.g -big > bigoutput littleoutput : text.g generate text.g -little > littleoutput Here we assume the hypothetical program `generate` makes two types of output, one if given ‘-big’ and one if given ‘-little’. See Functions for String Substitution and Analysis, for an explanation of the `subst` function.

Suppose you would like to vary the prerequisites according to the target, much as the variable ‘$@’ allows you to vary the recipe. You cannot do this with multiple targets in an ordinary rule, but you can do it with a *static pattern rule*. See Static Pattern Rules.

#### Rules with Grouped Targets

If instead of independent targets you have a recipe that generates multiple files from a single invocation, you can express that relationship by declaring your rule to use *grouped targets*. A grouped target rule uses the separator `&:` (the ‘&’ here is used to imply “all”).

When `make` builds any one of the grouped targets, it understands that all the other targets in the group are also updated as a result of the invocation of the recipe. Furthermore, if only some of the grouped targets are out of date or missing `make` will realize that running the recipe will update all of the targets. Finally, if any of the grouped targets are out of date, all the grouped targets are considered out of date.

As an example, this rule defines a grouped target:

```
foo bar biz &: baz boz
        echo $^ > foo
        echo $^ > bar
        echo $^ > biz
```

During the execution of a grouped target’s recipe, the automatic variable ‘$@’ is set to the name of the particular target in the group which triggered the rule. Caution must be used if relying on this variable in the recipe of a grouped target rule.

Unlike independent targets, a grouped target rule *must* include a recipe. However, targets that are members of a grouped target may also appear in independent target rule definitions that do not have recipes.

Each target may have only one recipe associated with it. If a grouped target appears in either an independent target rule or in another grouped target rule with a recipe, you will get a warning and the latter recipe will replace the former recipe. Additionally the target will be removed from the previous group and appear only in the new group.

If you would like a target to appear in multiple groups, then you must use the double-colon grouped target separator, `&::` when declaring all of the groups containing that target. Grouped double-colon targets are each considered independently, and each grouped double-colon rule’s recipe is executed at most once, if at least one of its multiple targets requires updating.

Next: Static Pattern Rules, Previous: Multiple Targets in a Rule, Up: Writing Rules   [Contents][Index]

### 4.11 Multiple Rules for One Target

One file can be the target of several rules. All the prerequisites mentioned in all the rules are merged into one list of prerequisites for the target. If the target is older than any prerequisite from any rule, the recipe is executed.

There can only be one recipe to be executed for a file. If more than one rule gives a recipe for the same file, `make` uses the last one given and prints an error message. (As a special case, if the file’s name begins with a dot, no error message is printed. This odd behavior is only for compatibility with other implementations of `make`… you should avoid using it). Occasionally it is useful to have the same target invoke multiple recipes which are defined in different parts of your makefile; you can use *double-colon rules* (see Double-Colon Rules) for this.

An extra rule with just prerequisites can be used to give a few extra prerequisites to many files at once. For example, makefiles often have a variable, such as `objects`, containing a list of all the compiler output files in the system being made. An easy way to say that all of them must be recompiled if config.h changes is to write the following:

```
objects = foo.o bar.o
foo.o : defs.h
bar.o : defs.h test.h
$(objects) : config.h
```

This could be inserted or taken out without changing the rules that really specify how to make the object files, making it a convenient form to use if you wish to add the additional prerequisite intermittently.

Another wrinkle is that the additional prerequisites could be specified with a variable that you set with a command line argument to `make` (see Overriding Variables). For example,

```
extradeps=
$(objects) : $(extradeps)
```

means that the command ‘make extradeps=foo.h’ will consider foo.h as a prerequisite of each object file, but plain ‘make’ will not.

If none of the explicit rules for a target has a recipe, then `make` searches for an applicable implicit rule to find one see Using Implicit Rules).

Next: Double-Colon Rules, Previous: Multiple Rules for One Target, Up: Writing Rules   [Contents][Index]

### 4.12 Static Pattern Rules

*Static pattern rules* are rules which specify multiple targets and construct the prerequisite names for each target based on the target name. They are more general than ordinary rules with multiple targets because the targets do not have to have identical prerequisites. Their prerequisites must be *analogous*, but not necessarily *identical*.

Next: Static Pattern Rules versus Implicit Rules, Previous: Static Pattern Rules, Up: Static Pattern Rules   [Contents][Index]

#### 4.12.1 Syntax of Static Pattern Rules

Here is the syntax of a static pattern rule:

```
targets …: target-pattern: prereq-patterns …
        recipe
        …
```

The *targets* list specifies the targets that the rule applies to. The targets can contain wildcard characters, just like the targets of ordinary rules (see Using Wildcard Characters in File Names).

The *target-pattern* and *prereq-patterns* say how to compute the prerequisites of each target. Each target is matched against the *target-pattern* to extract a part of the target name, called the *stem*. This stem is substituted into each of the *prereq-patterns* to make the prerequisite names (one from each *prereq-pattern*).

Each pattern normally contains the character ‘%’ just once. When the *target-pattern* matches a target, the ‘%’ can match any part of the target name; this part is called the *stem*. The rest of the pattern must match exactly. For example, the target foo.o matches the pattern ‘%.o’, with ‘foo’ as the stem. The targets foo.c and foo.out do not match that pattern.

The prerequisite names for each target are made by substituting the stem for the ‘%’ in each prerequisite pattern. For example, if one prerequisite pattern is %.c, then substitution of the stem ‘foo’ gives the prerequisite name foo.c. It is legitimate to write a prerequisite pattern that does not contain ‘%’; then this prerequisite is the same for all targets.

‘%’ characters in pattern rules can be quoted with preceding backslashes (‘\’). Backslashes that would otherwise quote ‘%’ characters can be quoted with more backslashes. Backslashes that quote ‘%’ characters or other backslashes are removed from the pattern before it is compared to file names or has a stem substituted into it. Backslashes that are not in danger of quoting ‘%’ characters go unmolested. For example, the pattern the\%weird\\%pattern\\ has ‘the%weird\’ preceding the operative ‘%’ character, and ‘pattern\\’ following it. The final two backslashes are left alone because they cannot affect any ‘%’ character.

Here is an example, which compiles each of foo.o and bar.o from the corresponding .c file:

```
objects = foo.o bar.o

all: $(objects)

$(objects): %.o: %.c
        $(CC) -c $(CFLAGS) $< -o $@
```

Here ‘$<’ is the automatic variable that holds the name of the prerequisite and ‘$@’ is the automatic variable that holds the name of the target; see Automatic Variables.

Each target specified must match the target pattern; a warning is issued for each target that does not. If you have a list of files, only some of which will match the pattern, you can use the `filter` function to remove non-matching file names (see Functions for String Substitution and Analysis):

```
files = foo.elc bar.o lose.o

$(filter %.o,$(files)): %.o: %.c
        $(CC) -c $(CFLAGS) $< -o $@
$(filter %.elc,$(files)): %.elc: %.el
        emacs -f batch-byte-compile $<
```

In this example the result of ‘$(filter %.o,$(files))’ is bar.o lose.o, and the first static pattern rule causes each of these object files to be updated by compiling the corresponding C source file. The result of ‘$(filter %.elc,$(files))’ is foo.elc, so that file is made from foo.el.

Another example shows how to use `$*` in static pattern rules:

```
bigoutput littleoutput : %output : text.g
        generate text.g -$* > $@
```

When the `generate` command is run, `$*` will expand to the stem, either ‘big’ or ‘little’.

Previous: Syntax of Static Pattern Rules, Up: Static Pattern Rules   [Contents][Index]

#### 4.12.2 Static Pattern Rules versus Implicit Rules

A static pattern rule has much in common with an implicit rule defined as a pattern rule (see Defining and Redefining Pattern Rules). Both have a pattern for the target and patterns for constructing the names of prerequisites. The difference is in how `make` decides *when* the rule applies.

An implicit rule *can* apply to any target that matches its pattern, but it *does* apply only when the target has no recipe otherwise specified, and only when the prerequisites can be found. If more than one implicit rule appears applicable, only one applies; the choice depends on the order of rules.

By contrast, a static pattern rule applies to the precise list of targets that you specify in the rule. It cannot apply to any other target and it invariably does apply to each of the targets specified. If two conflicting rules apply, and both have recipes, that’s an error.

The static pattern rule can be better than an implicit rule for these reasons:

- You may wish to override the usual implicit rule for a few files whose names cannot be categorized syntactically but can be given in an explicit list.
- If you cannot be sure of the precise contents of the directories you are using, you may not be sure which other irrelevant files might lead `make` to use the wrong implicit rule. The choice might depend on the order in which the implicit rule search is done. With static pattern rules, there is no uncertainty: each rule applies to precisely the targets specified.

Next: Generating Prerequisites Automatically, Previous: Static Pattern Rules, Up: Writing Rules   [Contents][Index]

### 4.13 Double-Colon Rules

*Double-colon* rules are explicit rules written with ‘::’ instead of ‘:’ after the target names. They are handled differently from ordinary rules when the same target appears in more than one rule. Pattern rules with double-colons have an entirely different meaning (see Match-Anything Pattern Rules).

When a target appears in multiple rules, all the rules must be the same type: all ordinary, or all double-colon. If they are double-colon, each of them is independent of the others. Each double-colon rule’s recipe is executed if the target is older than any prerequisites of that rule. If there are no prerequisites for that rule, its recipe is always executed (even if the target already exists). This can result in executing none, any, or all of the double-colon rules.

Double-colon rules with the same target are in fact completely separate from one another. Each double-colon rule is processed individually, just as rules with different targets are processed.

The double-colon rules for a target are executed in the order they appear in the makefile. However, the cases where double-colon rules really make sense are those where the order of executing the recipes would not matter.

Double-colon rules are somewhat obscure and not often very useful; they provide a mechanism for cases in which the method used to update a target differs depending on which prerequisite files caused the update, and such cases are rare.

Each double-colon rule should specify a recipe; if it does not, an implicit rule will be used if one applies. See Using Implicit Rules.

Previous: Double-Colon Rules, Up: Writing Rules   [Contents][Index]

### 4.14 Generating Prerequisites Automatically

In the makefile for a program, many of the rules you need to write often say only that some object file depends on some header file. For example, if main.c uses defs.h via an `#include`, you would write:

```
main.o: defs.h
```

You need this rule so that `make` knows that it must remake main.o whenever defs.h changes. You can see that for a large program you would have to write dozens of such rules in your makefile. And, you must always be very careful to update the makefile every time you add or remove an `#include`.

To avoid this hassle, most modern C compilers can write these rules for you, by looking at the `#include` lines in the source files. Usually this is done with the ‘-M’ option to the compiler. For example, the command:

```
cc -M main.c
```

generates the output:

```
main.o : main.c defs.h
```

Thus you no longer have to write all those rules yourself. The compiler will do it for you.

Note that such a rule constitutes mentioning main.o in a makefile, so it can never be considered an intermediate file by implicit rule search. This means that `make` won’t ever remove the file after using it; see Chains of Implicit Rules.

With old `make` programs, it was traditional practice to use this compiler feature to generate prerequisites on demand with a command like ‘make depend’. That command would create a file depend containing all the automatically-generated prerequisites; then the makefile could use `include` to read them in (see Including Other Makefiles).

In GNU `make`, the feature of remaking makefiles makes this practice obsolete—you need never tell `make` explicitly to regenerate the prerequisites, because it always regenerates any makefile that is out of date. See How Makefiles Are Remade.

The practice we recommend for automatic prerequisite generation is to have one makefile corresponding to each source file. For each source file *name*.c there is a makefile *name*.d which lists what files the object file *name*.o depends on. That way only the source files that have changed need to be rescanned to produce the new prerequisites.

Here is the pattern rule to generate a file of prerequisites (i.e., a makefile) called *name*.d from a C source file called *name*.c:

```
%.d: %.c
        @set -e; rm -f $@; \
         $(CC) -M $(CPPFLAGS) $< > $@.$$$$; \
         sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
         rm -f $@.$$$$
```

See Defining and Redefining Pattern Rules, for information on defining pattern rules. The ‘-e’ flag to the shell causes it to exit immediately if the `$(CC)` command (or any other command) fails (exits with a nonzero status).

With the GNU C compiler, you may wish to use the ‘-MM’ flag instead of ‘-M’. This omits prerequisites on system header files. See Options Controlling the Preprocessor in *Using GNU CC*, for details.

The purpose of the `sed` command is to translate (for example):

```
main.o : main.c defs.h
```

into:

```
main.o main.d : main.c defs.h
```

This makes each ‘.d’ file depend on all the source and header files that the corresponding ‘.o’ file depends on. `make` then knows it must regenerate the prerequisites whenever any of the source or header files changes.

Once you’ve defined the rule to remake the ‘.d’ files, you then use the `include` directive to read them all in. See Including Other Makefiles. For example:

```
sources = foo.c bar.c

include $(sources:.c=.d)
```

(This example uses a substitution variable reference to translate the list of source files ‘foo.c bar.c’ into a list of prerequisite makefiles, ‘foo.d bar.d’. See Substitution References, for full information on substitution references.) Since the ‘.d’ files are makefiles like any others, `make` will remake them as necessary with no further work from you. See How Makefiles Are Remade.

Note that the ‘.d’ files contain target definitions; you should be sure to place the `include` directive *after* the first, default goal in your makefiles or run the risk of having a random object file become the default goal. See How `make` Processes a Makefile.

Next: How to Use Variables, Previous: Writing Rules, Up: GNU `make`   [Contents][Index]
