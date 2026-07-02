---
title: "GNU make (part 3/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 3/17
---

## 4 Writing Rules

A *rule* appears in the makefile and says when and how to remake certain files, called the rule’s *targets* (most often only one per rule). It lists the other files that are the *prerequisites* of the target, and the *recipe* to use to create or update the target.

The order of rules is not significant, except for determining the *default goal*: the target for `make` to consider, if you do not otherwise specify one. The default goal is the first target of the first rule in the first makefile. There are two exceptions: a target starting with a period is not a default unless it also contains one or more slashes, ‘/’; and, a target that defines a pattern rule has no effect on the default goal. (See Defining and Redefining Pattern Rules.)

Therefore, we usually write the makefile so that the first rule is the one for compiling the entire program or all the programs described by the makefile (often with a target called ‘all’). See Arguments to Specify the Goals.

Next: Rule Syntax, Previous: Writing Rules, Up: Writing Rules   [Contents][Index]

### 4.1 Rule Example

Here is an example of a rule:

```
foo.o : foo.c defs.h       # module for twiddling the frobs
        cc -c -g foo.c
```

Its target is foo.o and its prerequisites are foo.c and defs.h. It has one command in the recipe: ‘cc -c -g foo.c’. The recipe starts with a tab to identify it as a recipe.

This rule says two things:

- How to decide whether foo.o is out of date: it is out of date if it does not exist, or if either foo.c or defs.h is more recent than it.
- How to update the file foo.o: by running `cc` as stated. The recipe does not explicitly mention defs.h, but we presume that foo.c includes it, and that is why defs.h was added to the prerequisites.

Next: Types of Prerequisites, Previous: Rule Example, Up: Writing Rules   [Contents][Index]

### 4.2 Rule Syntax

In general, a rule looks like this:

```
targets : prerequisites
        recipe
        …
```

or like this:

```
targets : prerequisites ; recipe
        recipe
        …
```

The *targets* are file names, separated by spaces. Wildcard characters may be used (see Using Wildcard Characters in File Names) and a name of the form *a*(*m*) represents member *m* in archive file *a* (see Archive Members as Targets). Usually there is only one target per rule, but occasionally there is a reason to have more (see Multiple Targets in a Rule).

The *recipe* lines start with a tab character (or the first character in the value of the `.RECIPEPREFIX` variable; see Other Special Variables). The first recipe line may appear on the line after the prerequisites, with a tab character, or may appear on the same line, with a semicolon. Either way, the effect is the same. There are other differences in the syntax of recipes. See Writing Recipes in Rules.

Because dollar signs are used to start `make` variable references, if you really want a dollar sign in a target or prerequisite you must write two of them, ‘$$’ (see How to Use Variables). If you have enabled secondary expansion (see Secondary Expansion) and you want a literal dollar sign in the prerequisites list, you must actually write *four* dollar signs (‘$$$$’).

You may split a long line by inserting a backslash followed by a newline, but this is not required, as `make` places no limit on the length of a line in a makefile.

A rule tells `make` two things: when the targets are out of date, and how to update them when necessary.

The criterion for being out of date is specified in terms of the *prerequisites*, which consist of file names separated by spaces. (Wildcards and archive members (see Using `make` to Update Archive Files) are allowed here too.) A target is out of date if it does not exist or if it is older than any of the prerequisites (by comparison of last-modification times). The idea is that the contents of the target file are computed based on information in the prerequisites, so if any of the prerequisites changes, the contents of the existing target file are no longer necessarily valid.

How to update is specified by a *recipe*. This is one or more lines to be executed by the shell (normally ‘sh’), but with some extra features (see Writing Recipes in Rules).

Next: Using Wildcard Characters in File Names, Previous: Rule Syntax, Up: Writing Rules   [Contents][Index]

### 4.3 Types of Prerequisites

There are two different types of prerequisites understood by GNU `make`: normal prerequisites, described in the previous section, and *order-only* prerequisites. A normal prerequisite makes two statements: first, it imposes an order in which recipes will be invoked: the recipes for all prerequisites of a target will be completed before the recipe for the target is started. Second, it imposes a dependency relationship: if any prerequisite is newer than the target, then the target is considered out-of-date and must be rebuilt.

Normally, this is exactly what you want: if a target’s prerequisite is updated, then the target should also be updated.

Occasionally you may want to ensure that a prerequisite is built before a target, but *without* forcing the target to be updated if the prerequisite is updated. *Order-only* prerequisites are used to create this type of relationship. Order-only prerequisites can be specified by placing a pipe symbol (`|`) in the prerequisites list: any prerequisites to the left of the pipe symbol are normal; any prerequisites to the right are order-only:

```
targets : normal-prerequisites | order-only-prerequisites
```

The normal prerequisites section may of course be empty. Also, you may still declare multiple lines of prerequisites for the same target: they are appended appropriately (normal prerequisites are appended to the list of normal prerequisites; order-only prerequisites are appended to the list of order-only prerequisites). Note that if you declare the same file to be both a normal and an order-only prerequisite, the normal prerequisite takes precedence (since they have a strict superset of the behavior of an order-only prerequisite).

Order-only prerequisites are never checked when determining if the target is out of date; even order-only prerequisites marked as phony (see Phony Targets) will not cause the target to be rebuilt.

Consider an example where your targets are to be placed in a separate directory, and that directory might not exist before `make` is run. In this situation, you want the directory to be created before any targets are placed into it but, because the timestamps on directories change whenever a file is added, removed, or renamed, we certainly don’t want to rebuild all the targets whenever the directory’s timestamp changes. One way to manage this is with order-only prerequisites: make the directory an order-only prerequisite on all the targets:

```
OBJDIR := objdir
OBJS := $(addprefix $(OBJDIR)/,foo.o bar.o baz.o)

$(OBJDIR)/%.o : %.c
        $(COMPILE.c) $(OUTPUT_OPTION) $<

all: $(OBJS)

$(OBJS): | $(OBJDIR)

$(OBJDIR):
        mkdir $(OBJDIR)
```

Now the rule to create the objdir directory will be run, if needed, before any ‘.o’ is built, but no ‘.o’ will be built because the objdir directory timestamp changed.

Next: Searching Directories for Prerequisites, Previous: Types of Prerequisites, Up: Writing Rules   [Contents][Index]

### 4.4 Using Wildcard Characters in File Names

A single file name can specify many files using *wildcard characters*. The wildcard characters in `make` are ‘*’, ‘?’ and ‘[…]’, the same as in the Bourne shell. For example, *.c specifies a list of all the files (in the working directory) whose names end in ‘.c’.

If an expression matches multiple files then the results will be sorted.2 However multiple expressions will not be globally sorted. For example, *.c *.h will list all the files whose names end in ‘.c’, sorted, followed by all the files whose names end in ‘.h’, sorted.

The character ‘~’ at the beginning of a file name also has special significance. If alone, or followed by a slash, it represents your home directory. For example ~/bin expands to /home/you/bin. If the ‘~’ is followed by a word, the string represents the home directory of the user named by that word. For example ~john/bin expands to /home/john/bin. On systems which don’t have a home directory for each user (such as MS-DOS or MS-Windows), this functionality can be simulated by setting the environment variable *HOME*.

Wildcard expansion is performed by `make` automatically in targets and in prerequisites. In recipes, the shell is responsible for wildcard expansion. In other contexts, wildcard expansion happens only if you request it explicitly with the `wildcard` function.

The special significance of a wildcard character can be turned off by preceding it with a backslash. Thus, foo\*bar would refer to a specific file whose name consists of ‘foo’, an asterisk, and ‘bar’.

Next: Pitfalls of Using Wildcards, Previous: Using Wildcard Characters in File Names, Up: Using Wildcard Characters in File Names   [Contents][Index]

#### 4.4.1 Wildcard Examples

Wildcards can be used in the recipe of a rule, where they are expanded by the shell. For example, here is a rule to delete all the object files:

```
clean:
        rm -f *.o
```

Wildcards are also useful in the prerequisites of a rule. With the following rule in the makefile, ‘make print’ will print all the ‘.c’ files that have changed since the last time you printed them:

```
print: *.c
        lpr -p $?
        touch print
```

This rule uses print as an empty target file; see Empty Target Files to Record Events. (The automatic variable ‘$?’ is used to print only those files that have changed; see Automatic Variables.)

Wildcard expansion does not happen when you define a variable. Thus, if you write this:

```
objects = *.o
```

then the value of the variable `objects` is the actual string ‘*.o’. However, if you use the value of `objects` in a target or prerequisite, wildcard expansion will take place there. If you use the value of `objects` in a recipe, the shell may perform wildcard expansion when the recipe runs. To set `objects` to the expansion, instead use:

```
objects := $(wildcard *.o)
```

See The Function `wildcard`.

Next: The Function `wildcard`, Previous: Wildcard Examples, Up: Using Wildcard Characters in File Names   [Contents][Index]

#### 4.4.2 Pitfalls of Using Wildcards

Now here is an example of a naive way of using wildcard expansion, that does not do what you would intend. Suppose you would like to say that the executable file foo is made from all the object files in the directory, and you write this:

```
objects = *.o

foo : $(objects)
        cc -o foo $(CFLAGS) $(objects)
```

The value of `objects` is the actual string ‘*.o’. Wildcard expansion happens in the rule for foo, so that each *existing* ‘.o’ file becomes a prerequisite of foo and will be recompiled if necessary.

But what if you delete all the ‘.o’ files? When a wildcard matches no files, it is left as it is, so then foo will depend on the oddly-named file *.o. Since no such file is likely to exist, `make` will give you an error saying it cannot figure out how to make *.o. This is not what you want!

Actually it is possible to obtain the desired result with wildcard expansion, but you need more sophisticated techniques, including the `wildcard` function and string substitution. See The Function `wildcard`.

Microsoft operating systems (MS-DOS and MS-Windows) use backslashes to separate directories in pathnames, like so:

```
  c:\foo\bar\baz.c
```

This is equivalent to the Unix-style c:/foo/bar/baz.c (the c: part is the so-called drive letter). When `make` runs on these systems, it supports backslashes as well as the Unix-style forward slashes in pathnames. However, this support does *not* include the wildcard expansion, where backslash is a quote character. Therefore, you *must* use Unix-style slashes in these cases.

Previous: Pitfalls of Using Wildcards, Up: Using Wildcard Characters in File Names   [Contents][Index]

#### 4.4.3 The Function `wildcard`

Wildcard expansion happens automatically in rules. But wildcard expansion does not normally take place when a variable is set, or inside the arguments of a function. If you want to do wildcard expansion in such places, you need to use the `wildcard` function, like this:

```
$(wildcard pattern…)
```

This string, used anywhere in a makefile, is replaced by a space-separated list of names of existing files that match one of the given file name patterns. If no existing file name matches a pattern, then that pattern is omitted from the output of the `wildcard` function. Note that this is different from how unmatched wildcards behave in rules, where they are used verbatim rather than ignored (see Pitfalls of Using Wildcards).

As with wildcard expansion in rules, the results of the `wildcard` function are sorted. But again, each individual expression is sorted separately, so ‘$(wildcard *.c *.h)’ will expand to all files matching ‘.c’, sorted, followed by all files matching ‘.h’, sorted.

One use of the `wildcard` function is to get a list of all the C source files in a directory, like this:

```
$(wildcard *.c)
```

We can change the list of C source files into a list of object files by replacing the ‘.c’ suffix with ‘.o’ in the result, like this:

```
$(patsubst %.c,%.o,$(wildcard *.c))
```

(Here we have used another function, `patsubst`. See Functions for String Substitution and Analysis.)

Thus, a makefile to compile all C source files in the directory and then link them together could be written as follows:

```
objects := $(patsubst %.c,%.o,$(wildcard *.c))

foo : $(objects)
        cc -o foo $(objects)
```

(This takes advantage of the implicit rule for compiling C programs, so there is no need to write explicit rules for compiling the files. See The Two Flavors of Variables, for an explanation of ‘:=’, which is a variant of ‘=’.)

Next: Rules without Recipes or Prerequisites, Previous: Searching Directories for Prerequisites, Up: Writing Rules   [Contents][Index]

### 4.6 Phony Targets

A phony target is one that is not really the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request. There are two reasons to use a phony target: to avoid a conflict with a file of the same name, and to improve performance.

If you write a rule whose recipe will not create the target file, the recipe will be executed every time the target comes up for remaking. Here is an example:

```
clean:
        rm *.o temp
```

Because the `rm` command does not create a file named clean, probably no such file will ever exist. Therefore, the `rm` command will be executed every time you say ‘make clean’.

In this example, the clean target will not work properly if a file named clean is ever created in this directory. Since it has no prerequisites, clean would always be considered up to date and its recipe would not be executed. To avoid this problem you can explicitly declare the target to be phony by making it a prerequisite of the special target `.PHONY` (see Special Built-in Target Names) as follows:

```
.PHONY: clean
clean:
        rm *.o temp
```

Once this is done, ‘make clean’ will run the recipe regardless of whether there is a file named clean.

Prerequisites of `.PHONY` are always interpreted as literal target names, never as patterns (even if they contain ‘%’ characters). To always rebuild a pattern rule consider using a “force target” (see Rules without Recipes or Prerequisites).

Phony targets are also useful in conjunction with recursive invocations of `make` (see Recursive Use of `make`). In this situation the makefile will often contain a variable which lists a number of sub-directories to be built. A simplistic way to handle this is to define one rule with a recipe that loops over the sub-directories, like this:

```
SUBDIRS = foo bar baz

subdirs:
        for dir in $(SUBDIRS); do \
          $(MAKE) -C $$dir; \
        done
```

There are problems with this method, however. First, any error detected in a sub-make is ignored by this rule, so it will continue to build the rest of the directories even when one fails. This can be overcome by adding shell commands to note the error and exit, but then it will do so even if `make` is invoked with the `-k` option, which is unfortunate. Second, and perhaps more importantly, you cannot take full advantage of `make`’s ability to build targets in parallel (see Parallel Execution), since there is only one rule. Each individual makefile’s targets will be built in parallel, but only one sub-directory will be built at a time.

By declaring the sub-directories as `.PHONY` targets (you must do this as the sub-directory obviously always exists; otherwise it won’t be built) you can remove these problems:

```
SUBDIRS = foo bar baz

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
        $(MAKE) -C $@

foo: baz
```

Here we’ve also declared that the foo sub-directory cannot be built until after the baz sub-directory is complete; this kind of relationship declaration is particularly important when attempting parallel builds.

The implicit rule search (see Using Implicit Rules) is skipped for `.PHONY` targets. This is why declaring a target as `.PHONY` is good for performance, even if you are not worried about the actual file existing.

A phony target should not be a prerequisite of a real target file; if it is, its recipe will be run every time `make` considers that file. As long as a phony target is never a prerequisite of a real target, the phony target recipe will be executed only when the phony target is a specified goal (see Arguments to Specify the Goals).

You should not declare an included makefile as phony. Phony targets are not intended to represent real files, and because the target is always considered out of date make will always rebuild it then re-execute itself (see How Makefiles Are Remade). To avoid this, `make` will not re-execute itself if an included file marked as phony is re-built.

Phony targets can have prerequisites. When one directory contains multiple programs, it is most convenient to describe all of the programs in one makefile ./Makefile. Since the target remade by default will be the first one in the makefile, it is common to make this a phony target named ‘all’ and give it, as prerequisites, all the individual programs. For example:

```
all : prog1 prog2 prog3
.PHONY : all

prog1 : prog1.o utils.o
        cc -o prog1 prog1.o utils.o

prog2 : prog2.o
        cc -o prog2 prog2.o

prog3 : prog3.o sort.o utils.o
        cc -o prog3 prog3.o sort.o utils.o
```

Now you can say just ‘make’ to remake all three programs, or specify as arguments the ones to remake (as in ‘make prog1 prog3’). Phoniness is not inherited: the prerequisites of a phony target are not themselves phony, unless explicitly declared to be so.

When one phony target is a prerequisite of another, it serves as a subroutine of the other. For example, here ‘make cleanall’ will delete the object files, the difference files, and the file program:

```
.PHONY: cleanall cleanobj cleandiff

cleanall : cleanobj cleandiff
        rm program

cleanobj :
        rm *.o

cleandiff :
        rm *.diff
```

Next: Empty Target Files to Record Events, Previous: Phony Targets, Up: Writing Rules   [Contents][Index]

### 4.7 Rules without Recipes or Prerequisites

If a rule has no prerequisites or recipe, and the target of the rule is a nonexistent file, then `make` imagines this target to have been updated whenever its rule is run. This implies that all targets depending on this one will always have their recipe run.

An example will illustrate this:

```
clean: FORCE
        rm $(objects)
FORCE:
```

Here the target ‘FORCE’ satisfies the special conditions, so the target clean that depends on it is forced to run its recipe. There is nothing special about the name ‘FORCE’, but that is one name commonly used this way.

As you can see, using ‘FORCE’ this way has the same results as using ‘.PHONY: clean’.

Using ‘.PHONY’ is more explicit and more efficient. However, other versions of `make` do not support ‘.PHONY’; thus ‘FORCE’ appears in many makefiles. See Phony Targets.

Next: Special Built-in Target Names, Previous: Rules without Recipes or Prerequisites, Up: Writing Rules   [Contents][Index]

### 4.8 Empty Target Files to Record Events

The *empty target* is a variant of the phony target; it is used to hold recipes for an action that you request explicitly from time to time. Unlike a phony target, this target file can really exist; but the file’s contents do not matter, and usually are empty.

The purpose of the empty target file is to record, with its last-modification time, when the rule’s recipe was last executed. It does so because one of the commands in the recipe is a `touch` command to update the target file.

The empty target file should have some prerequisites (otherwise it doesn’t make sense). When you ask to remake the empty target, the recipe is executed if any prerequisite is more recent than the target; in other words, if a prerequisite has changed since the last time you remade the target. Here is an example:

```
print: foo.c bar.c
        lpr -p $?
        touch print
```

With this rule, ‘make print’ will execute the `lpr` command if either source file has changed since the last ‘make print’. The automatic variable ‘$?’ is used to print only those files that have changed (see Automatic Variables).

Next: Multiple Targets in a Rule, Previous: Empty Target Files to Record Events, Up: Writing Rules   [Contents][Index]

### 4.9 Special Built-in Target Names

Certain names have special meanings if they appear as targets.

**`.PHONY`**

The prerequisites of the special target `.PHONY` are considered to be phony targets. When it is time to consider such a target, `make` will run its recipe unconditionally, regardless of whether a file with that name exists or what its last-modification time is. See Phony Targets.

**`.SUFFIXES`**

The prerequisites of the special target `.SUFFIXES` are the list of suffixes to be used in checking for suffix rules. See Old-Fashioned Suffix Rules.
