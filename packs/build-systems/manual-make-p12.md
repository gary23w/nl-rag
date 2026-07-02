---
title: "GNU make (part 12/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 12/17
---

# GNU make

Extra flags to give to lint.

Next: Defining and Redefining Pattern Rules, Previous: Variables Used by Implicit Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.4 Chains of Implicit Rules

Sometimes a file can be made by a sequence of implicit rules. For example, a file *n*.o could be made from *n*.y by running first Yacc and then `cc`. Such a sequence is called a *chain*.

If the file *n*.c exists, or is mentioned in the makefile, no special searching is required: `make` finds that the object file can be made by C compilation from *n*.c; later on, when considering how to make *n*.c, the rule for running Yacc is used. Ultimately both *n*.c and *n*.o are updated.

However, even if *n*.c does not exist and is not mentioned, `make` knows how to envision it as the missing link between *n*.o and *n*.y! In this case, *n*.c is called an *intermediate file*. Once `make` has decided to use the intermediate file, it is entered in the data base as if it had been mentioned in the makefile, along with the implicit rule that says how to create it.

Intermediate files are remade using their rules just like all other files. But intermediate files are treated differently in two ways.

The first difference is what happens if the intermediate file does not exist. If an ordinary file *b* does not exist, and `make` considers a target that depends on *b*, it invariably creates *b* and then updates the target from *b*. But if *b* is an intermediate file, then `make` can leave well enough alone: it won’t create *b* unless one of its prerequisites is out of date. This means the target depending on *b* won’t be rebuilt either, unless there is some other reason to update that target: for example the target doesn’t exist or a different prerequisite is newer than the target.

The second difference is that if `make` *does* create *b* in order to update something else, it deletes *b* later on after it is no longer needed. Therefore, an intermediate file which did not exist before `make` also does not exist after `make`. `make` reports the deletion to you by printing a ‘rm’ command showing which file it is deleting.

You can explicitly mark a file as intermediate by listing it as a prerequisite of the special target `.INTERMEDIATE`. This takes effect even if the file is mentioned explicitly in some other way.

A file cannot be intermediate if it is mentioned in the makefile as a target or prerequisite, so one way to avoid the deletion of intermediate files is by adding it as a prerequisite to some target. However, doing so can cause make to do extra work when searching pattern rules (see Implicit Rule Search Algorithm).

As an alternative, listing a file as a prerequisite of the special target `.NOTINTERMEDIATE` forces it to not be considered intermediate (just as any other mention of the file will do). Also, listing the target pattern of a pattern rule as a prerequisite of `.NOTINTERMEDIATE` ensures that no targets generated using that pattern rule are considered intermediate.

You can disable intermediate files completely in your makefile by providing `.NOTINTERMEDIATE` as a target with no prerequisites: in that case it applies to every file in the makefile.

If you do not want `make` to create a file merely because it does not already exist, but you also do not want `make` to automatically delete the file, you can mark it as a *secondary* file. To do this, list it as a prerequisite of the special target `.SECONDARY`. Marking a file as secondary also marks it as intermediate.

A chain can involve more than two implicit rules. For example, it is possible to make a file foo from RCS/foo.y,v by running RCS, Yacc and `cc`. Then both foo.y and foo.c are intermediate files that are deleted at the end.

No single implicit rule can appear more than once in a chain. This means that `make` will not even consider such a ridiculous thing as making foo from foo.o.o by running the linker twice. This constraint has the added benefit of preventing any infinite loop in the search for an implicit rule chain.

There are some special implicit rules to optimize certain cases that would otherwise be handled by rule chains. For example, making foo from foo.c could be handled by compiling and linking with separate chained rules, using foo.o as an intermediate file. But what actually happens is that a special rule for this case does the compilation and linking with a single `cc` command. The optimized rule is used in preference to the step-by-step chain because it comes earlier in the ordering of rules.

Finally, for performance reasons `make` will not consider non-terminal match-anything rules (i.e., ‘%:’) when searching for a rule to build a prerequisite of an implicit rule (see Match-Anything Pattern Rules).

Next: Defining Last-Resort Default Rules, Previous: Chains of Implicit Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.5 Defining and Redefining Pattern Rules

You define an implicit rule by writing a *pattern rule*. A pattern rule looks like an ordinary rule, except that its target contains the character ‘%’ (exactly one of them). The target is considered a pattern for matching file names; the ‘%’ can match any nonempty substring, while other characters match only themselves. The prerequisites likewise use ‘%’ to show how their names relate to the target name.

Thus, a pattern rule ‘%.o : %.c’ says how to make any file *stem*.o from another file *stem*.c.

Note that expansion using ‘%’ in pattern rules occurs **after** any variable or function expansions, which take place when the makefile is read. See How to Use Variables, and Functions for Transforming Text.

Next: Pattern Rule Examples, Previous: Defining and Redefining Pattern Rules, Up: Defining and Redefining Pattern Rules   [Contents][Index]

#### 10.5.1 Introduction to Pattern Rules

A pattern rule contains the character ‘%’ (exactly one of them) in the target; otherwise, it looks exactly like an ordinary rule. The target is a pattern for matching file names; the ‘%’ matches any nonempty substring, while other characters match only themselves.

For example, ‘%.c’ as a pattern matches any file name that ends in ‘.c’. ‘s.%.c’ as a pattern matches any file name that starts with ‘s.’, ends in ‘.c’ and is at least five characters long. (There must be at least one character to match the ‘%’.) The substring that the ‘%’ matches is called the *stem*.

‘%’ in a prerequisite of a pattern rule stands for the same stem that was matched by the ‘%’ in the target. In order for the pattern rule to apply, its target pattern must match the file name under consideration and all of its prerequisites (after pattern substitution) must name files that exist or can be made. These files become prerequisites of the target.

Thus, a rule of the form

```
%.o : %.c ; recipe…
```

specifies how to make a file *n*.o, with another file *n*.c as its prerequisite, provided that *n*.c exists or can be made.

There may also be prerequisites that do not use ‘%’; such a prerequisite attaches to every file made by this pattern rule. These unvarying prerequisites are useful occasionally.

A pattern rule need not have any prerequisites that contain ‘%’, or in fact any prerequisites at all. Such a rule is effectively a general wildcard. It provides a way to make any file that matches the target pattern. See Defining Last-Resort Default Rules.

More than one pattern rule may match a target. In this case `make` will choose the “best fit” rule. See How Patterns Match.

Pattern rules may have more than one target; however, every target must contain a `%` character. Multiple target patterns in pattern rules are always treated as grouped targets (see Multiple Targets in a Rule) regardless of whether they use the `:` or `&:` separator.

There is one exception: if a pattern target is out of date or does not exist and the makefile does not need to build it, then it will not cause the other targets to be considered out of date. Note that this historical exception will be removed in future versions of GNU `make` and should not be relied on. If this situation is detected `make` will generate a warning *pattern recipe did not update peer target*; however, `make` cannot detect all such situations. Please be sure that your recipe updates *all* the target patterns when it runs.

Next: Automatic Variables, Previous: Introduction to Pattern Rules, Up: Defining and Redefining Pattern Rules   [Contents][Index]

#### 10.5.2 Pattern Rule Examples

Here are some examples of pattern rules actually predefined in `make`. First, the rule that compiles ‘.c’ files into ‘.o’ files:

```
%.o : %.c
        $(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
```

defines a rule that can make any file *x*.o from *x*.c. The recipe uses the automatic variables ‘$@’ and ‘$<’ to substitute the names of the target file and the source file in each case where the rule applies (see Automatic Variables).

Here is a second built-in rule:

```
% :: RCS/%,v
        $(CO) $(COFLAGS) $<
```

defines a rule that can make any file *x* whatsoever from a corresponding file *x*,v in the sub-directory RCS. Since the target is ‘%’, this rule will apply to any file whatever, provided the appropriate prerequisite file exists. The double colon makes the rule *terminal*, which means that its prerequisite may not be an intermediate file (see Match-Anything Pattern Rules).

This pattern rule has two targets:

```
%.tab.c %.tab.h: %.y
        bison -d $<
```

This tells `make` that the recipe ‘bison -d *x*.y’ will make both *x*.tab.c and *x*.tab.h. If the file foo depends on the files parse.tab.o and scan.o and the file scan.o depends on the file parse.tab.h, when parse.y is changed, the recipe ‘bison -d parse.y’ will be executed only once, and the prerequisites of both parse.tab.o and scan.o will be satisfied. (Presumably the file parse.tab.o will be recompiled from parse.tab.c and the file scan.o from scan.c, while foo is linked from parse.tab.o, scan.o, and its other prerequisites, and it will execute happily ever after.)

Next: How Patterns Match, Previous: Pattern Rule Examples, Up: Defining and Redefining Pattern Rules   [Contents][Index]

#### 10.5.3 Automatic Variables

Suppose you are writing a pattern rule to compile a ‘.c’ file into a ‘.o’ file: how do you write the ‘cc’ command so that it operates on the right source file name? You cannot write the name in the recipe, because the name is different each time the implicit rule is applied.

What you do is use a special feature of `make`, the *automatic variables*. These variables have values computed afresh for each rule that is executed, based on the target and prerequisites of the rule. In this example, you would use ‘$@’ for the object file name and ‘$<’ for the source file name.

It’s very important that you recognize the limited scope in which automatic variable values are available: they only have values within the recipe. In particular, you cannot use them anywhere within the target list of a rule; they have no value there and will expand to the empty string. Also, they cannot be accessed directly within the prerequisite list of a rule. A common mistake is attempting to use `$@` within the prerequisites list; this will not work. However, there is a special feature of GNU `make`, secondary expansion (see Secondary Expansion), which will allow automatic variable values to be used in prerequisite lists.

Here is a table of automatic variables:

**`$@`**

The file name of the target of the rule. If the target is an archive member, then ‘$@’ is the name of the archive file. In a pattern rule that has multiple targets (see Introduction to Pattern Rules), ‘$@’ is the name of whichever target caused the rule’s recipe to be run.

**`$%`**

The target member name, when the target is an archive member. See Using `make` to Update Archive Files. For example, if the target is foo.a(bar.o) then ‘$%’ is bar.o and ‘$@’ is foo.a. ‘$%’ is empty when the target is not an archive member.

**`$<`**

The name of the first prerequisite. If the target got its recipe from an implicit rule, this will be the first prerequisite added by the implicit rule (see Using Implicit Rules).

**`$?`**

The names of all the prerequisites that are newer than the target, with spaces between them. If the target does not exist, all prerequisites will be included. For prerequisites which are archive members, only the named member is used (see Using `make` to Update Archive Files).

‘$?’ is useful even in explicit rules when you wish to operate on only the prerequisites that have changed. For example, suppose that an archive named lib is supposed to contain copies of several object files. This rule copies just the changed object files into the archive:

```
lib: foo.o bar.o lose.o win.o
        ar r lib $?
```

**`$^`**

The names of all the prerequisites, with spaces between them. For prerequisites which are archive members, only the named member is used (see Using `make` to Update Archive Files). A target has only one prerequisite on each other file it depends on, no matter how many times each file is listed as a prerequisite. So if you list a prerequisite more than once for a target, the value of `$^` contains just one copy of the name. This list does **not** contain any of the order-only prerequisites; for those see the ‘$|’ variable, below.

**`$+`**

This is like ‘$^’, but prerequisites listed more than once are duplicated in the order they were listed in the makefile. This is primarily useful for use in linking commands where it is meaningful to repeat library file names in a particular order.

**`$|`**

The names of all the order-only prerequisites, with spaces between them.

**`$*`**

The stem with which an implicit rule matches (see How Patterns Match). If the target is dir/a.foo.b and the target pattern is a.%.b then the stem is dir/foo. The stem is useful for constructing names of related files.

In a static pattern rule, the stem is part of the file name that matched the ‘%’ in the target pattern.

In an explicit rule, there is no stem; so ‘$*’ cannot be determined in that way. Instead, if the target name ends with a recognized suffix (see Old-Fashioned Suffix Rules), ‘$*’ is set to the target name minus the suffix. For example, if the target name is ‘foo.c’, then ‘$*’ is set to ‘foo’, since ‘.c’ is a suffix. GNU `make` does this bizarre thing only for compatibility with other implementations of `make`. You should generally avoid using ‘$*’ except in implicit rules or static pattern rules.

If the target name in an explicit rule does not end with a recognized suffix, ‘$*’ is set to the empty string for that rule.

Of the variables listed above, four have values that are single file names, and three have values that are lists of file names. These seven have variants that get just the file’s directory name or just the file name within the directory. The variant variables’ names are formed by appending ‘D’ or ‘F’, respectively. The functions `dir` and `notdir` can be used to obtain a similar effect (see Functions for File Names). Note, however, that the ‘D’ variants all omit the trailing slash which always appears in the output of the `dir` function. Here is a table of the variants:

**‘$(@D)’**

The directory part of the file name of the target, with the trailing slash removed. If the value of ‘$@’ is dir/foo.o then ‘$(@D)’ is dir. This value is . if ‘$@’ does not contain a slash.

**‘$(@F)’**

The file-within-directory part of the file name of the target. If the value of ‘$@’ is dir/foo.o then ‘$(@F)’ is foo.o. ‘$(@F)’ is equivalent to ‘$(notdir $@)’.

**‘$(*D)’**

**‘$(*F)’**

The directory part and the file-within-directory part of the stem; dir and foo in this example.

**‘$(%D)’**

**‘$(%F)’**

The directory part and the file-within-directory part of the target archive member name. This makes sense only for archive member targets of the form *archive*(*member*) and is useful only when *member* may contain a directory name. (See Archive Members as Targets.)

**‘$(<D)’**

**‘$(<F)’**

The directory part and the file-within-directory part of the first prerequisite.

**‘$(^D)’**

**‘$(^F)’**

Lists of the directory parts and the file-within-directory parts of all prerequisites.

**‘$(+D)’**

**‘$(+F)’**

Lists of the directory parts and the file-within-directory parts of all prerequisites, including multiple instances of duplicated prerequisites.

**‘$(?D)’**

**‘$(?F)’**

Lists of the directory parts and the file-within-directory parts of all prerequisites that are newer than the target.

Note that we use a special stylistic convention when we talk about these automatic variables; we write “the value of ‘$<’”, rather than “the variable `<`” as we would write for ordinary variables such as `objects` and `CFLAGS`. We think this convention looks more natural in this special case. Please do not assume it has a deep significance; ‘$<’ refers to the variable named `<` just as ‘$(CFLAGS)’ refers to the variable named `CFLAGS`. You could just as well use ‘$(<)’ in place of ‘$<’.

Next: Match-Anything Pattern Rules, Previous: Automatic Variables, Up: Defining and Redefining Pattern Rules   [Contents][Index]

#### 10.5.4 How Patterns Match

A target pattern is composed of a ‘%’ between a prefix and a suffix, either or both of which may be empty. The pattern matches a file name only if the file name starts with the prefix and ends with the suffix, without overlap. The text between the prefix and the suffix is called the *stem*. Thus, when the pattern ‘%.o’ matches the file name test.o, the stem is ‘test’. The pattern rule prerequisites are turned into actual file names by substituting the stem for the character ‘%’. Thus, if in the same example one of the prerequisites is written as ‘%.c’, it expands to ‘test.c’.

When the target pattern does not contain a slash (and it usually does not), directory names in the file names are removed from the file name before it is compared with the target prefix and suffix. After the comparison of the file name to the target pattern, the directory names, along with the slash that ends them, are added on to the prerequisite file names generated from the pattern rule’s prerequisite patterns and the file name. The directories are ignored only for the purpose of finding an implicit rule to use, not in the application of that rule. Thus, ‘e%t’ matches the file name src/eat, with ‘src/a’ as the stem. When prerequisites are turned into file names, the directories from the stem are added at the front, while the rest of the stem is substituted for the ‘%’. The stem ‘src/a’ with a prerequisite pattern ‘c%r’ gives the file name src/car.

A pattern rule can be used to build a given file only if there is a target pattern that matches the file name, *and* all prerequisites in that rule either exist or can be built. The rules you write take precedence over those that are built in. Note however, that a rule which can be satisfied without chaining other implicit rules (for example, one which has no prerequisites or its prerequisites already exist or are mentioned) always takes priority over a rule with prerequisites that must be made by chaining other implicit rules.

It is possible that more than one pattern rule will meet these criteria. In that case, `make` will choose the rule with the shortest stem (that is, the pattern that matches most specifically). If more than one pattern rule has the shortest stem, `make` will choose the first one found in the makefile.

This algorithm results in more specific rules being preferred over more generic ones; for example:

```
%.o: %.c
        $(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@

%.o : %.f
        $(COMPILE.F) $(OUTPUT_OPTION) $<

lib/%.o: lib/%.c
        $(CC) -fPIC -c $(CFLAGS) $(CPPFLAGS) $< -o $@
```

Given these rules and asked to build bar.o where both bar.c and bar.f exist, `make` will choose the first rule and compile bar.c into bar.o. In the same situation where bar.c does not exist, then `make` will choose the second rule and compile bar.f into bar.o.

If `make` is asked to build lib/bar.o and both lib/bar.c and lib/bar.f exist, then the third rule will be chosen since the stem for this rule (‘bar’) is shorter than the stem for the first rule (‘lib/bar’). If lib/bar.c does not exist then the third rule is not eligible and the second rule will be used, even though the stem is longer.

Next: Canceling Implicit Rules, Previous: How Patterns Match, Up: Defining and Redefining Pattern Rules   [Contents][Index]

#### 10.5.5 Match-Anything Pattern Rules

When a pattern rule’s target is just ‘%’, it matches any file name whatever. We call these rules *match-anything* rules. They are very useful, but it can take a lot of time for `make` to think about them, because it must consider every such rule for each file name listed either as a target or as a prerequisite.

Suppose the makefile mentions foo.c. For this target, `make` would have to consider making it by linking an object file foo.c.o, or by C compilation-and-linking in one step from foo.c.c, or by Pascal compilation-and-linking from foo.c.p, and many other possibilities.

We know these possibilities are ridiculous since foo.c is a C source file, not an executable. If `make` did consider these possibilities, it would ultimately reject them, because files such as foo.c.o and foo.c.p would not exist. But these possibilities are so numerous that `make` would run very slowly if it had to consider them.

To gain speed, we have put various constraints on the way `make` considers match-anything rules. There are two different constraints that can be applied, and each time you define a match-anything rule you must choose one or the other for that rule.

One choice is to mark the match-anything rule as *terminal* by defining it with a double colon. When a rule is terminal, it does not apply unless its prerequisites actually exist. Prerequisites that could be made with other implicit rules are not good enough. In other words, no further chaining is allowed beyond a terminal rule.

For example, the built-in implicit rules for extracting sources from RCS and SCCS files are terminal; as a result, if the file foo.c,v does not exist, `make` will not even consider trying to make it as an intermediate file from foo.c,v.o or from RCS/SCCS/s.foo.c,v. RCS and SCCS files are generally ultimate source files, which should not be remade from any other files; therefore, `make` can save time by not looking for ways to remake them.

If you do not mark the match-anything rule as terminal, then it is non-terminal. A non-terminal match-anything rule cannot apply to a prerequisite of an implicit rule, or to a file name that indicates a specific type of data. A file name indicates a specific type of data if some non-match-anything implicit rule target matches it.

For example, the file name foo.c matches the target for the pattern rule ‘%.c : %.y’ (the rule to run Yacc). Regardless of whether this rule is actually applicable (which happens only if there is a file foo.y), the fact that its target matches is enough to prevent consideration of any non-terminal match-anything rules for the file foo.c. Thus, `make` will not even consider trying to make foo.c as an executable file from foo.c.o, foo.c.c, foo.c.p, etc.

The motivation for this constraint is that non-terminal match-anything rules are used for making files containing specific types of data (such as executable files) and a file name with a recognized suffix indicates some other specific type of data (such as a C source file).

Special built-in dummy pattern rules are provided solely to recognize certain file names so that non-terminal match-anything rules will not be considered. These dummy rules have no prerequisites and no recipes, and they are ignored for all other purposes. For example, the built-in implicit rule

```
%.p :
```

exists to make sure that Pascal source files such as foo.p match a specific target pattern and thereby prevent time from being wasted looking for foo.p.o or foo.p.c.

Dummy pattern rules such as the one for ‘%.p’ are made for every suffix listed as valid for use in suffix rules (see Old-Fashioned Suffix Rules).

Previous: Match-Anything Pattern Rules, Up: Defining and Redefining Pattern Rules   [Contents][Index]

#### 10.5.6 Canceling Implicit Rules

You can override a built-in implicit rule (or one you have defined yourself) by defining a new pattern rule with the same target and prerequisites, but a different recipe. When the new rule is defined, the built-in one is replaced. The new rule’s position in the sequence of implicit rules is determined by where you write the new rule.

You can cancel a built-in implicit rule by defining a pattern rule with the same target and prerequisites, but no recipe. For example, the following would cancel the rule that runs the assembler:

```
%.o : %.s
```

Next: Old-Fashioned Suffix Rules, Previous: Defining and Redefining Pattern Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.6 Defining Last-Resort Default Rules

You can define a last-resort implicit rule by writing a terminal match-anything pattern rule with no prerequisites (see Match-Anything Pattern Rules). This is just like any other pattern rule; the only thing special about it is that it will match any target. So such a rule’s recipe is used for all targets and prerequisites that have no recipe of their own and for which no other implicit rule applies.

For example, when testing a makefile, you might not care if the source files contain real data, only that they exist. Then you might do this:

```
%::
        touch $@
```

to cause all the source files needed (as prerequisites) to be created automatically.

You can instead define a recipe to be used for targets for which there are no rules at all, even ones which don’t specify recipes. You do this by writing a rule for the target `.DEFAULT`. Such a rule’s recipe is used for all prerequisites which do not appear as targets in any explicit rule, and for which no implicit rule applies. Naturally, there is no `.DEFAULT` rule unless you write one.

If you use `.DEFAULT` with no recipe or prerequisites:

```
.DEFAULT:
```

the recipe previously stored for `.DEFAULT` is cleared. Then `make` acts as if you had never defined `.DEFAULT` at all.

If you do not want a target to get the recipe from a match-anything pattern rule or `.DEFAULT`, but you also do not want any recipe to be run for the target, you can give it an empty recipe (see Defining Empty Recipes).

You can use a last-resort rule to override part of another makefile. See Overriding Part of Another Makefile.

Next: Implicit Rule Search Algorithm, Previous: Defining Last-Resort Default Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.7 Old-Fashioned Suffix Rules

*Suffix rules* are the old-fashioned way of defining implicit rules for `make`. Suffix rules are obsolete because pattern rules are more general and clearer. They are supported in GNU `make` for compatibility with old makefiles. They come in two kinds: *double-suffix* and *single-suffix*.

A double-suffix rule is defined by a pair of suffixes: the target suffix and the source suffix. It matches any file whose name ends with the target suffix. The corresponding implicit prerequisite is made by replacing the target suffix with the source suffix in the file name. A two-suffix rule ‘.c.o’ (whose target and source suffixes are ‘.o’ and ‘.c’) is equivalent to the pattern rule ‘%.o : %.c’.

A single-suffix rule is defined by a single suffix, which is the source suffix. It matches any file name, and the corresponding implicit prerequisite name is made by appending the source suffix. A single-suffix rule whose source suffix is ‘.c’ is equivalent to the pattern rule ‘% : %.c’.

Suffix rule definitions are recognized by comparing each rule’s target against a defined list of known suffixes. When `make` sees a rule whose target is a known suffix, this rule is considered a single-suffix rule. When `make` sees a rule whose target is two known suffixes concatenated, this rule is taken as a double-suffix rule.

For example, ‘.c’ and ‘.o’ are both on the default list of known suffixes. Therefore, if you define a rule whose target is ‘.c.o’, `make` takes it to be a double-suffix rule with source suffix ‘.c’ and target suffix ‘.o’. Here is the old-fashioned way to define the rule for compiling a C source file:

```
.c.o:
        $(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<
```

Suffix rules cannot have any prerequisites of their own. If they have any, they are treated as normal files with funny names, not as suffix rules. Thus, the rule:

```
.c.o: foo.h
        $(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<
```

tells how to make the file .c.o from the prerequisite file foo.h, and is not at all like the pattern rule:

```
%.o: %.c foo.h
        $(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<
```

which tells how to make ‘.o’ files from ‘.c’ files, and makes all ‘.o’ files using this pattern rule also depend on foo.h.

Suffix rules with no recipe are also meaningless. They do not remove previous rules as do pattern rules with no recipe (see Canceling Implicit Rules). They simply enter the suffix or pair of suffixes concatenated as a target in the data base.

The known suffixes are simply the names of the prerequisites of the special target `.SUFFIXES`. You can add your own suffixes by writing a rule for `.SUFFIXES` that adds more prerequisites, as in:

```
.SUFFIXES: .hack .win
```

which adds ‘.hack’ and ‘.win’ to the end of the list of suffixes.

If you wish to eliminate the default known suffixes instead of just adding to them, write a rule for `.SUFFIXES` with no prerequisites. By special dispensation, this eliminates all existing prerequisites of `.SUFFIXES`. You can then write another rule to add the suffixes you want. For example,

```
.SUFFIXES:            # Delete the default suffixes
.SUFFIXES: .c .o .h   # Define our suffix list
```

The ‘-r’ or ‘--no-builtin-rules’ flag causes the default list of suffixes to be empty.

The variable `SUFFIXES` is defined to the default list of suffixes before `make` reads any makefiles. You can change the list of suffixes with a rule for the special target `.SUFFIXES`, but that does not alter this variable.

Next: Extending GNU `make`, Previous: Using Implicit Rules, Up: GNU `make`   [Contents][Index]


## 11 Using `make` to Update Archive Files

*Archive files* are files containing named sub-files called *members*; they are maintained with the program `ar` and their main use is as subroutine libraries for linking.

Next: Implicit Rule for Archive Member Targets, Previous: Using `make` to Update Archive Files, Up: Using `make` to Update Archive Files   [Contents][Index]

### 11.1 Archive Members as Targets

An individual member of an archive file can be used as a target or prerequisite in `make`. You specify the member named *member* in archive file *archive* as follows:

```
archive(member)
```

This construct is available only in targets and prerequisites, not in recipes! Most programs that you might use in recipes do not support this syntax and cannot act directly on archive members. Only `ar` and other programs specifically designed to operate on archives can do so. Therefore, valid recipes to update an archive member target probably must use `ar`. For example, this rule says to create a member hack.o in archive foolib by copying the file hack.o:

```
foolib(hack.o) : hack.o
        ar cr foolib hack.o
```

In fact, nearly all archive member targets are updated in just this way and there is an implicit rule to do it for you. **Please note:** The ‘c’ flag to `ar` is required if the archive file does not already exist.

To specify several members in the same archive, you can write all the member names together between the parentheses. For example:

```
foolib(hack.o kludge.o)
```

is equivalent to:

```
foolib(hack.o) foolib(kludge.o)
```

You can also use shell-style wildcards in an archive member reference. See Using Wildcard Characters in File Names. For example, ‘foolib(*.o)’ expands to all existing members of the foolib archive whose names end in ‘.o’; perhaps ‘foolib(hack.o) foolib(kludge.o)’.

Next: Dangers When Using Archives, Previous: Archive Members as Targets, Up: Using `make` to Update Archive Files   [Contents][Index]

### 11.2 Implicit Rule for Archive Member Targets

Recall that a target that looks like *a*(*m*) stands for the member named *m* in the archive file *a*.

When `make` looks for an implicit rule for such a target, as a special feature it considers implicit rules that match (*m*), as well as those that match the actual target *a*(*m*).

This causes one special rule whose target is (%) to match. This rule updates the target *a*(*m*) by copying the file *m* into the archive. For example, it will update the archive member target foo.a(bar.o) by copying the *file* bar.o into the archive foo.a as a *member* named bar.o.

When this rule is chained with others, the result is very powerful. Thus, ‘make "foo.a(bar.o)"’ (the quotes are needed to protect the ‘(’ and ‘)’ from being interpreted specially by the shell) in the presence of a file bar.c is enough to cause the following recipe to be run, even without a makefile:

```
cc -c bar.c -o bar.o
ar r foo.a bar.o
rm -f bar.o
```

Here `make` has envisioned the file bar.o as an intermediate file. See Chains of Implicit Rules.

Implicit rules such as this one are written using the automatic variable ‘$%’. See Automatic Variables.

An archive member name in an archive cannot contain a directory name, but it may be useful in a makefile to pretend that it does. If you write an archive member target foo.a(dir/file.o), `make` will perform automatic updating with this recipe:

```
ar r foo.a dir/file.o
```

which has the effect of copying the file dir/file.o into a member named file.o. In connection with such usage, the automatic variables `%D` and `%F` may be useful.

Previous: Implicit Rule for Archive Member Targets, Up: Implicit Rule for Archive Member Targets   [Contents][Index]

#### 11.2.1 Updating Archive Symbol Directories

An archive file that is used as a library usually contains a special member named __.SYMDEF that contains a directory of the external symbol names defined by all the other members. After you update any other members, you need to update __.SYMDEF so that it will summarize the other members properly. This is done by running the `ranlib` program:

```
ranlib archivefile
```

Normally you would put this command in the rule for the archive file, and make all the members of the archive file prerequisites of that rule. For example,

```
libfoo.a: libfoo.a(x.o y.o …)
        ranlib libfoo.a
```

The effect of this is to update archive members x.o, y.o, etc., and then update the symbol directory member __.SYMDEF by running `ranlib`. The rules for updating the members are not shown here; most likely you can omit them and use the implicit rule which copies files into the archive, as described in the preceding section.

This is not necessary when using the GNU `ar` program, which updates the __.SYMDEF member automatically.

Next: Suffix Rules for Archive Files, Previous: Implicit Rule for Archive Member Targets, Up: Using `make` to Update Archive Files   [Contents][Index]

### 11.3 Dangers When Using Archives

The built-in rules for updating archives are incompatible with parallel builds. These rules (required by the POSIX standard) add each object file into the archive as it’s compiled. When parallel builds are enabled this allows multiple `ar` commands to be updating the same archive simultaneously, which is not supported.

If you want to use parallel builds with archives you can override the default rules by adding these lines to your makefile:

```
(%) : % ;
%.a : ; $(AR) $(ARFLAGS) $@ $?
```

The first line changes the rule that updates an individual object in the archive to do nothing, and the second line changes the default rule for building an archive to update all the outdated objects (`$?`) in one command.

Of course you will still need to declare the prerequisites of your library using the archive syntax:

```
libfoo.a: libfoo.a(x.o y.o …)
```

If you prefer to write an explicit rule you can use:

```
libfoo.a: libfoo.a(x.o y.o …)
        $(AR) $(ARFLAGS) $@ $?
```

Previous: Dangers When Using Archives, Up: Using `make` to Update Archive Files   [Contents][Index]

### 11.4 Suffix Rules for Archive Files

You can write a special kind of suffix rule for dealing with archive files. See Old-Fashioned Suffix Rules, for a full explanation of suffix rules. Archive suffix rules are obsolete in GNU `make`, because pattern rules for archives are a more general mechanism (see Implicit Rule for Archive Member Targets). But they are retained for compatibility with other `make`s.

To write a suffix rule for archives, you simply write a suffix rule using the target suffix ‘.a’ (the usual suffix for archive files). For example, here is the old-fashioned suffix rule to update a library archive from C source files:

```
.c.a:
        $(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $*.o
        $(AR) r $@ $*.o
        $(RM) $*.o
```

This works just as if you had written the pattern rule:

```
(%.o): %.c
        $(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $*.o
        $(AR) r $@ $*.o
        $(RM) $*.o
```

In fact, this is just what `make` does when it sees a suffix rule with ‘.a’ as the target suffix. Any double-suffix rule ‘.*x*.a’ is converted to a pattern rule with the target pattern ‘(%.o)’ and a prerequisite pattern of ‘%.*x*’.

Since you might want to use ‘.a’ as the suffix for some other kind of file, `make` also converts archive suffix rules to pattern rules in the normal way (see Old-Fashioned Suffix Rules). Thus a double-suffix rule ‘.*x*.a’ produces two pattern rules: ‘(%.o): %.*x*’ and ‘%.a: %.*x*’.

Next: Integrating GNU `make`, Previous: Using `make` to Update Archive Files, Up: GNU `make`   [Contents][Index]
