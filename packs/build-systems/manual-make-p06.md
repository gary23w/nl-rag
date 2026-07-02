---
title: "GNU make (part 6/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 6/17
---

# GNU make

Previous: Output During Parallel Execution, Up: Parallel Execution   [Contents][Index]

#### 5.4.3 Input During Parallel Execution

Two processes cannot both take input from the same device at the same time. To make sure that only one recipe tries to take input from the terminal at once, `make` will invalidate the standard input streams of all but one running recipe. If another recipe attempts to read from standard input it will usually incur a fatal error (a ‘Broken pipe’ signal).

It is unpredictable which recipe will have a valid standard input stream (which will come from the terminal, or wherever you redirect the standard input of `make`). The first recipe run will always get it first, and the first recipe started after that one finishes will get it next, and so on.

We will change how this aspect of `make` works if we find a better alternative. In the mean time, you should not rely on any recipe using standard input at all if you are using the parallel execution feature; but if you are not using this feature, then standard input works normally in all recipes.

Next: Interrupting or Killing `make`, Previous: Parallel Execution, Up: Writing Recipes in Rules   [Contents][Index]

### 5.5 Errors in Recipes

After each shell invocation returns, `make` looks at its exit status. If the shell completed successfully (the exit status is zero), the next line in the recipe is executed in a new shell; after the last line is finished, the rule is finished.

If there is an error (the exit status is nonzero), `make` gives up on the current rule, and perhaps on all rules.

Sometimes the failure of a certain recipe line does not indicate a problem. For example, you may use the `mkdir` command to ensure that a directory exists. If the directory already exists, `mkdir` will report an error, but you probably want `make` to continue regardless.

To ignore errors in a recipe line, write a ‘-’ at the beginning of the line’s text (after the initial tab). The ‘-’ is discarded before the line is passed to the shell for execution.

For example,

```
clean:
        -rm -f *.o
```

This causes `make` to continue even if `rm` is unable to remove a file.

When you run `make` with the ‘-i’ or ‘--ignore-errors’ flag, errors are ignored in all recipes of all rules. A rule in the makefile for the special target `.IGNORE` has the same effect, if there are no prerequisites. This is less flexible but sometimes useful.

When errors are to be ignored, because of either a ‘-’ or the ‘-i’ flag, `make` treats an error return just like success, except that it prints out a message that tells you the status code the shell exited with, and says that the error has been ignored.

When an error happens that `make` has not been told to ignore, it implies that the current target cannot be correctly remade, and neither can any other that depends on it either directly or indirectly. No further recipes will be executed for these targets, since their preconditions have not been achieved.

Normally `make` gives up immediately in this circumstance, returning a nonzero status. However, if the ‘-k’ or ‘--keep-going’ flag is specified, `make` continues to consider the other prerequisites of the pending targets, remaking them if necessary, before it gives up and returns nonzero status. For example, after an error in compiling one object file, ‘make -k’ will continue compiling other object files even though it already knows that linking them will be impossible. See Summary of Options.

The usual behavior assumes that your purpose is to get the specified targets up to date; once `make` learns that this is impossible, it might as well report the failure immediately. The ‘-k’ option says that the real purpose is to test as many of the changes made in the program as possible, perhaps to find several independent problems so that you can correct them all before the next attempt to compile. This is why Emacs’ `compile` command passes the ‘-k’ flag by default.

Usually when a recipe line fails, if it has changed the target file at all, the file is corrupted and cannot be used—or at least it is not completely updated. Yet the file’s time stamp says that it is now up to date, so the next time `make` runs, it will not try to update that file. The situation is just the same as when the shell is killed by a signal; see Interrupting or Killing `make`. So generally the right thing to do is to delete the target file if the recipe fails after beginning to change the file. `make` will do this if `.DELETE_ON_ERROR` appears as a target. This is almost always what you want `make` to do, but it is not historical practice; so for compatibility, you must explicitly request it.

Next: Recursive Use of `make`, Previous: Errors in Recipes, Up: Writing Recipes in Rules   [Contents][Index]

### 5.6 Interrupting or Killing `make`

If `make` gets a fatal signal while a shell is executing, it may delete the target file that the recipe was supposed to update. This is done if the target file’s last-modification time has changed since `make` first checked it.

The purpose of deleting the target is to make sure that it is remade from scratch when `make` is next run. Why is this? Suppose you type Ctrl-c while a compiler is running, and it has begun to write an object file foo.o. The Ctrl-c kills the compiler, resulting in an incomplete file whose last-modification time is newer than the source file foo.c. But `make` also receives the Ctrl-c signal and deletes this incomplete file. If `make` did not do this, the next invocation of `make` would think that foo.o did not require updating—resulting in a strange error message from the linker when it tries to link an object file half of which is missing.

You can prevent the deletion of a target file in this way by making the special target `.PRECIOUS` depend on it. Before remaking a target, `make` checks to see whether it appears on the prerequisites of `.PRECIOUS`, and thereby decides whether the target should be deleted if a signal happens. Some reasons why you might do this are that the target is updated in some atomic fashion, or exists only to record a modification-time (its contents do not matter), or must exist at all times to prevent other sorts of trouble.

Although `make` does its best to clean up there are certain situations in which cleanup is impossible. For example, `make` may be killed by an uncatchable signal. Or, one of the programs make invokes may be killed or crash, leaving behind an up-to-date but corrupt target file: `make` will not realize that this failure requires the target to be cleaned. Or `make` itself may encounter a bug and crash.

For these reasons it’s best to write *defensive recipes*, which won’t leave behind corrupted targets even if they fail. Most commonly these recipes create temporary files rather than updating the target directly, then rename the temporary file to the final target name. Some compilers already behave this way, so that you don’t need to write a defensive recipe.

Next: Defining Canned Recipes, Previous: Interrupting or Killing `make`, Up: Writing Recipes in Rules   [Contents][Index]

### 5.7 Recursive Use of `make`

Recursive use of `make` means using `make` as a command in a makefile. This technique is useful when you want separate makefiles for various subsystems that compose a larger system. For example, suppose you have a sub-directory subdir which has its own makefile, and you would like the containing directory’s makefile to run `make` on the sub-directory. You can do it by writing this:

```
subsystem:
        cd subdir && $(MAKE)
```

or, equivalently, this (see Summary of Options):

```
subsystem:
        $(MAKE) -C subdir
```

You can write recursive `make` commands just by copying this example, but there are many things to know about how they work and why, and about how the sub-`make` relates to the top-level `make`. You may also find it useful to declare targets that invoke recursive `make` commands as ‘.PHONY’ (for more discussion on when this is useful, see Phony Targets).

For your convenience, when GNU `make` starts (after it has processed any `-C` options) it sets the variable `CURDIR` to the pathname of the current working directory. This value is never touched by `make` again: in particular note that if you include files from other directories the value of `CURDIR` does not change. The value has the same precedence it would have if it were set in the makefile (by default, an environment variable `CURDIR` will not override this value). Note that setting this variable has no impact on the operation of `make` (it does not cause `make` to change its working directory, for example).

Next: Communicating Variables to a Sub-`make`, Previous: Recursive Use of `make`, Up: Recursive Use of `make`   [Contents][Index]

#### 5.7.1 How the `MAKE` Variable Works

Recursive `make` commands should always use the variable `MAKE`, not the explicit command name ‘make’, as shown here:

```
subsystem:
        cd subdir && $(MAKE)
```

The value of this variable is the file name with which `make` was invoked. If this file name was /bin/make, then the recipe executed is ‘cd subdir && /bin/make’. If you use a special version of `make` to run the top-level makefile, the same special version will be executed for recursive invocations.

As a special feature, using the variable `MAKE` in the recipe of a rule alters the effects of the ‘-t’ (‘--touch’), ‘-n’ (‘--just-print’), or ‘-q’ (‘--question’) option. Using the `MAKE` variable has the same effect as using a ‘+’ character at the beginning of the recipe line. See Instead of Executing the Recipes. This special feature is only enabled if the `MAKE` variable appears directly in the recipe: it does not apply if the `MAKE` variable is referenced through expansion of another variable. In the latter case you must use the ‘+’ token to get these special effects.

Consider the command ‘make -t’ in the above example. (The ‘-t’ option marks targets as up to date without actually running any recipes; see Instead of Executing Recipes.) Following the usual definition of ‘-t’, a ‘make -t’ command in the example would create a file named subsystem and do nothing else. What you really want it to do is run ‘cd subdir && make -t’; but that would require executing the recipe, and ‘-t’ says not to execute recipes.

The special feature makes this do what you want: whenever a recipe line of a rule contains the variable `MAKE`, the flags ‘-t’, ‘-n’ and ‘-q’ do not apply to that line. Recipe lines containing `MAKE` are executed normally despite the presence of a flag that causes most recipes not to be run. The usual `MAKEFLAGS` mechanism passes the flags to the sub-`make` (see Communicating Options to a Sub-`make`), so your request to touch the files, or print the recipes, is propagated to the subsystem.

Next: Communicating Options to a Sub-`make`, Previous: How the `MAKE` Variable Works, Up: Recursive Use of `make`   [Contents][Index]

#### 5.7.2 Communicating Variables to a Sub-`make`

Variable values of the top-level `make` can be passed to the sub-`make` through the environment by explicit request. These variables are defined in the sub-`make` as defaults, but they do not override variables defined in the makefile used by the sub-`make` unless you use the ‘-e’ switch (see Summary of Options).

To pass down, or *export*, a variable, `make` adds the variable and its value to the environment for running each line of the recipe. The sub-`make`, in turn, uses the environment to initialize its table of variable values. See Variables from the Environment.

Except by explicit request, `make` exports a variable only if it is either defined in the environment initially, or if set on the command line and its name consists only of letters, numbers, and underscores.

The value of the `make` variable `SHELL` is not exported. Instead, the value of the `SHELL` variable from the invoking environment is passed to the sub-`make`. You can force `make` to export its value for `SHELL` by using the `export` directive, described below. See Choosing the Shell.

The special variable `MAKEFLAGS` is always exported (unless you unexport it). `MAKEFILES` is exported if you set it to anything.

`make` automatically passes down variable values that were defined on the command line, by putting them in the `MAKEFLAGS` variable. See Communicating Options to a Sub-`make`.

Variables are *not* normally passed down if they were created by default by `make` (see Variables Used by Implicit Rules). The sub-`make` will define these for itself.

If you want to export specific variables to a sub-`make`, use the `export` directive, like this:

```
export variable …
```

If you want to *prevent* a variable from being exported, use the `unexport` directive, like this:

```
unexport variable …
```

In both of these forms, the arguments to `export` and `unexport` are expanded, and so could be variables or functions which expand to a (list of) variable names to be (un)exported.

As a convenience, you can define a variable and export it at the same time by doing:

```
export variable = value
```

has the same result as:

```
variable = value
export variable
```

and

```
export variable := value
```

has the same result as:

```
variable := value
export variable
```

Likewise,

```
export variable += value
```

is just like:

```
variable += value
export variable
```

See Appending More Text to Variables.

You may notice that the `export` and `unexport` directives work in `make` in the same way they work in the shell, `sh`.

If you want all variables to be exported by default, you can use `export` by itself:

```
export
```

This tells `make` that variables which are not explicitly mentioned in an `export` or `unexport` directive should be exported. Any variable given in an `unexport` directive will still *not* be exported.

The behavior elicited by an `export` directive by itself was the default in older versions of GNU `make`. If your makefiles depend on this behavior and you want to be compatible with old versions of `make`, you can add the special target `.EXPORT_ALL_VARIABLES` to your makefile instead of using the `export` directive. This will be ignored by old `make`s, while the `export` directive will cause a syntax error.

When using `export` by itself or `.EXPORT_ALL_VARIABLES` to export variables by default, only variables whose names consist solely of alphanumerics and underscores will be exported. To export other variables you must specifically mention them in an `export` directive.

Adding a variable’s value to the environment requires it to be expanded. If expanding a variable has side-effects (such as the `info` or `eval` or similar functions) then these side-effects will be seen every time a command is invoked. You can avoid this by ensuring that such variables have names which are not exportable by default. However, a better solution is to *not* use this “export by default” facility at all, and instead explicitly `export` the relevant variables by name.

You can use `unexport` by itself to tell `make` *not* to export variables by default. Since this is the default behavior, you would only need to do this if `export` had been used by itself earlier (in an included makefile, perhaps). You **cannot** use `export` and `unexport` by themselves to have variables exported for some recipes and not for others. The last `export` or `unexport` directive that appears by itself determines the behavior for the entire run of `make`.

As a special feature, the variable `MAKELEVEL` is changed when it is passed down from level to level. This variable’s value is a string which is the depth of the level as a decimal number. The value is ‘0’ for the top-level `make`; ‘1’ for a sub-`make`, ‘2’ for a sub-sub-`make`, and so on. The incrementation happens when `make` sets up the environment for a recipe.

The main use of `MAKELEVEL` is to test it in a conditional directive (see Conditional Parts of Makefiles); this way you can write a makefile that behaves one way if run recursively and another way if run directly by you.

You can use the variable `MAKEFILES` to cause all sub-`make` commands to use additional makefiles. The value of `MAKEFILES` is a whitespace-separated list of file names. This variable, if defined in the outer-level makefile, is passed down through the environment; then it serves as a list of extra makefiles for the sub-`make` to read before the usual or specified ones. See The Variable `MAKEFILES`.

Next: The ‘--print-directory’ Option, Previous: Communicating Variables to a Sub-`make`, Up: Recursive Use of `make`   [Contents][Index]

#### 5.7.3 Communicating Options to a Sub-`make`

Flags such as ‘-s’ and ‘-k’ are passed automatically to the sub-`make` through the variable `MAKEFLAGS`. This variable is set up automatically by `make` to contain the flag letters that `make` received. Thus, if you do ‘make -ks’ then `MAKEFLAGS` gets the value ‘ks’.

As a consequence, every sub-`make` gets a value for `MAKEFLAGS` in its environment. In response, it takes the flags from that value and processes them as if they had been given as arguments. See Summary of Options. This means that, unlike other environment variables, `MAKEFLAGS` specified in the environment take precedence over `MAKEFLAGS` specified in the makefile.

The value of `MAKEFLAGS` is a possibly empty group of characters representing single-letter options that take no argument, followed by a space and any options that take arguments or which have long option names. If an option has both single-letter and long options, the single-letter option is always preferred. If there are no single-letter options on the command line, then the value of `MAKEFLAGS` starts with a space.

Likewise variables defined on the command line are passed to the sub-`make` through `MAKEFLAGS`. Words in the value of `MAKEFLAGS` that contain ‘=’, `make` treats as variable definitions just as if they appeared on the command line. See Overriding Variables.

The options ‘-C’, ‘-f’, ‘-o’, and ‘-W’ are not put into `MAKEFLAGS`; these options are not passed down.

The ‘-j’ option is a special case (see Parallel Execution). If you set it to some numeric value ‘N’ and your operating system supports it (most any UNIX system will; others typically won’t), the parent `make` and all the sub-`make`s will communicate to ensure that there are only ‘N’ jobs running at the same time between them all. Note that any job that is marked recursive (see Instead of Executing Recipes) doesn’t count against the total jobs (otherwise we could get ‘N’ sub-`make`s running and have no slots left over for any real work!)

If your operating system doesn’t support the above communication, then no ‘-j’ is added to `MAKEFLAGS`, so that sub-`make`s run in non-parallel mode. If the ‘-j’ option were passed down to sub-`make`s you would get many more jobs running in parallel than you asked for. If you give ‘-j’ with no numeric argument, meaning to run as many jobs as possible in parallel, this is passed down, since multiple infinities are no more than one.

If you do not want to pass the other flags down, you must change the value of `MAKEFLAGS`, for example like this:

```
subsystem:
        cd subdir && $(MAKE) MAKEFLAGS=
```

The command line variable definitions really appear in the variable `MAKEOVERRIDES`, and `MAKEFLAGS` contains a reference to this variable. If you do want to pass flags down normally, but don’t want to pass down the command line variable definitions, you can reset `MAKEOVERRIDES` to empty, like this:

```
MAKEOVERRIDES =
```

This is not usually useful to do. However, some systems have a small fixed limit on the size of the environment, and putting so much information into the value of `MAKEFLAGS` can exceed it. If you see the error message ‘Arg list too long’, this may be the problem. (For strict compliance with POSIX.2, changing `MAKEOVERRIDES` does not affect `MAKEFLAGS` if the special target ‘.POSIX’ appears in the makefile. You probably do not care about this.)

A similar variable `MFLAGS` exists also, for historical compatibility. It has the same value as `MAKEFLAGS` except that it does not contain the command line variable definitions, and it always begins with a hyphen unless it is empty (`MAKEFLAGS` begins with a hyphen only when it begins with an option that has no single-letter version, such as ‘--warn-undefined-variables’). `MFLAGS` was traditionally used explicitly in the recursive `make` command, like this:

```
subsystem:
        cd subdir && $(MAKE) $(MFLAGS)
```

but now `MAKEFLAGS` makes this usage redundant. If you want your makefiles to be compatible with old `make` programs, use this technique; it will work fine with more modern `make` versions too.

The `MAKEFLAGS` variable can also be useful if you want to have certain options, such as ‘-k’ (see Summary of Options), set each time you run `make`. You simply put a value for `MAKEFLAGS` in your environment. You can also set `MAKEFLAGS` in a makefile, to specify additional flags that should also be in effect for that makefile. (Note that you cannot use `MFLAGS` this way. That variable is set only for compatibility; `make` does not interpret a value you set for it in any way.)

When `make` interprets the value of `MAKEFLAGS` (either from the environment or from a makefile), it first prepends a hyphen if the value does not already begin with one. Then it chops the value into words separated by blanks, and parses these words as if they were options given on the command line (except that ‘-C’, ‘-f’, ‘-h’, ‘-o’, ‘-W’, and their long-named versions are ignored; and there is no error for an invalid option).

If you do put `MAKEFLAGS` in your environment, you should be sure not to include any options that will drastically affect the actions of `make` and undermine the purpose of makefiles and of `make` itself. For instance, the ‘-t’, ‘-n’, and ‘-q’ options, if put in one of these variables, could have disastrous consequences and would certainly have at least surprising and probably annoying effects.

If you’d like to run other implementations of `make` in addition to GNU `make`, and hence do not want to add GNU `make`-specific flags to the `MAKEFLAGS` variable, you can add them to the `GNUMAKEFLAGS` variable instead. This variable is parsed just before `MAKEFLAGS`, in the same way as `MAKEFLAGS`. When `make` constructs `MAKEFLAGS` to pass to a recursive `make` it will include all flags, even those taken from `GNUMAKEFLAGS`. As a result, after parsing `GNUMAKEFLAGS` GNU `make` sets this variable to the empty string to avoid duplicating flags during recursion.

It’s best to use `GNUMAKEFLAGS` only with flags which won’t materially change the behavior of your makefiles. If your makefiles require GNU Make anyway then simply use `MAKEFLAGS`. Flags such as ‘--no-print-directory’ or ‘--output-sync’ may be appropriate for `GNUMAKEFLAGS`.

Previous: Communicating Options to a Sub-`make`, Up: Recursive Use of `make`   [Contents][Index]

#### 5.7.4 The ‘--print-directory’ Option

If you use several levels of recursive `make` invocations, the ‘-w’ or ‘--print-directory’ option can make the output a lot easier to understand by showing each directory as `make` starts processing it and as `make` finishes processing it. For example, if ‘make -w’ is run in the directory /u/gnu/make, `make` will print a line of the form:

```
make: Entering directory `/u/gnu/make'.
```

before doing anything else, and a line of the form:

```
make: Leaving directory `/u/gnu/make'.
```

when processing is completed.

Normally, you do not need to specify this option because ‘make’ does it for you: ‘-w’ is turned on automatically when you use the ‘-C’ option, and in sub-`make`s. `make` will not automatically turn on ‘-w’ if you also use ‘-s’, which says to be silent, or if you use ‘--no-print-directory’ to explicitly disable it.

Next: Using Empty Recipes, Previous: Recursive Use of `make`, Up: Writing Recipes in Rules   [Contents][Index]

### 5.8 Defining Canned Recipes

When the same sequence of commands is useful in making various targets, you can define it as a canned sequence with the `define` directive, and refer to the canned sequence from the recipes for those targets. The canned sequence is actually a variable, so the name must not conflict with other variable names.

Here is an example of defining a canned recipe:

```
define run-yacc =
yacc $(firstword $^)
mv y.tab.c $@
endef
```

Here `run-yacc` is the name of the variable being defined; `endef` marks the end of the definition; the lines in between are the commands. The `define` directive does not expand variable references and function calls in the canned sequence; the ‘$’ characters, parentheses, variable names, and so on, all become part of the value of the variable you are defining. See Defining Multi-Line Variables, for a complete explanation of `define`.

The first command in this example runs Yacc on the first prerequisite of whichever rule uses the canned sequence. The output file from Yacc is always named y.tab.c. The second command moves the output to the rule’s target file name.

To use the canned sequence, substitute the variable into the recipe of a rule. You can substitute it like any other variable (see Basics of Variable References). Because variables defined by `define` are recursively expanded variables, all the variable references you wrote inside the `define` are expanded now. For example:

```
foo.c : foo.y
        $(run-yacc)
```

‘foo.y’ will be substituted for the variable ‘$^’ when it occurs in `run-yacc`’s value, and ‘foo.c’ for ‘$@’.

This is a realistic example, but this particular one is not needed in practice because `make` has an implicit rule to figure out these commands based on the file names involved (see Using Implicit Rules).

In recipe execution, each line of a canned sequence is treated just as if the line appeared on its own in the rule, preceded by a tab. In particular, `make` invokes a separate sub-shell for each line. You can use the special prefix characters that affect command lines (‘@’, ‘-’, and ‘+’) on each line of a canned sequence. See Writing Recipes in Rules. For example, using this canned sequence:

```
define frobnicate =
@echo "frobnicating target $@"
frob-step-1 $< -o $@-step-1
frob-step-2 $@-step-1 -o $@
endef
```

`make` will not echo the first line, the `echo` command. But it *will* echo the following two recipe lines.

On the other hand, prefix characters on the recipe line that refers to a canned sequence apply to every line in the sequence. So the rule:

```
frob.out: frob.in
        @$(frobnicate)
```

does not echo *any* recipe lines. (See Recipe Echoing, for a full explanation of ‘@’.)

Previous: Defining Canned Recipes, Up: Writing Recipes in Rules   [Contents][Index]

### 5.9 Using Empty Recipes

It is sometimes useful to define recipes which do nothing. This is done simply by giving a recipe that consists of nothing but whitespace. For example:

```
target: ;
```

defines an empty recipe for target. You could also use a line beginning with a recipe prefix character to define an empty recipe, but this would be confusing because such a line looks empty.

You may be wondering why you would want to define a recipe that does nothing. One reason this is useful is to prevent a target from getting implicit recipes (from implicit rules or the `.DEFAULT` special target; see Using Implicit Rules and see Defining Last-Resort Default Rules).

Empty recipes can also be used to avoid errors for targets that will be created as a side-effect of another recipe: if the target does not exist the empty recipe ensures that `make` won’t complain that it doesn’t know how to build the target, and `make` will assume the target is out of date.

You may be inclined to define empty recipes for targets that are not actual files, but only exist so that their prerequisites can be remade. However, this is not the best way to do that, because the prerequisites may not be remade properly if the target file actually does exist. See Phony Targets, for a better way to do this.

Next: Conditional Parts of Makefiles, Previous: Writing Recipes in Rules, Up: GNU `make`   [Contents][Index]
