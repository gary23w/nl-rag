---
title: "GNU make (part 5/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 5/17
---

## 5 Writing Recipes in Rules

The recipe of a rule consists of one or more shell command lines to be executed, one at a time, in the order they appear. Typically, the result of executing these commands is that the target of the rule is brought up to date.

Users use many different shell programs, but recipes in makefiles are always interpreted by /bin/sh unless the makefile specifies otherwise. See Recipe Execution.

Next: Recipe Echoing, Previous: Writing Recipes in Rules, Up: Writing Recipes in Rules   [Contents][Index]

### 5.1 Recipe Syntax

Makefiles have the unusual property that there are really two distinct syntaxes in one file. Most of the makefile uses `make` syntax (see Writing Makefiles). However, recipes are meant to be interpreted by the shell and so they are written using shell syntax. The `make` program does not try to understand shell syntax: it performs only a very few specific translations on the content of the recipe before handing it to the shell.

Each line in the recipe must start with a tab (or the first character in the value of the `.RECIPEPREFIX` variable; see Other Special Variables), except that the first recipe line may be attached to the target-and-prerequisites line with a semicolon in between. *Any* line in the makefile that begins with a tab and appears in a “rule context” (that is, after a rule has been started until another rule or variable definition) will be considered part of a recipe for that rule. Blank lines and lines of just comments may appear among the recipe lines; they are ignored.

Some consequences of these rules include:

- A blank line that begins with a tab is not blank: it’s an empty recipe (see Using Empty Recipes).
- A comment in a recipe is not a `make` comment; it will be passed to the shell as-is. Whether the shell treats it as a comment or not depends on your shell.
- A variable definition in a “rule context” which is indented by a tab as the first character on the line, will be considered part of a recipe, not a `make` variable definition, and passed to the shell.
- A conditional expression (`ifdef`, `ifeq`, etc. see Syntax of Conditionals) in a “rule context” which is indented by a tab as the first character on the line, will be considered part of a recipe and be passed to the shell.

Next: Using Variables in Recipes, Previous: Recipe Syntax, Up: Recipe Syntax   [Contents][Index]

#### 5.1.1 Splitting Recipe Lines

One of the few ways in which `make` does interpret recipes is checking for a backslash just before the newline. As in normal makefile syntax, a single logical recipe line can be split into multiple physical lines in the makefile by placing a backslash before each newline. A sequence of lines like this is considered a single recipe line, and one instance of the shell will be invoked to run it.

However, in contrast to how they are treated in other places in a makefile (see Splitting Long Lines), backslash/newline pairs are *not* removed from the recipe. Both the backslash and the newline characters are preserved and passed to the shell. How the backslash/newline is interpreted depends on your shell. If the first character of the next line after the backslash/newline is the recipe prefix character (a tab by default; see Other Special Variables), then that character (and only that character) is removed. Whitespace is never added to the recipe.

For example, the recipe for the all target in this makefile:

```
all :
        @echo no\
space
        @echo no\
        space
        @echo one \
        space
        @echo one\
         space
```

consists of four separate shell commands where the output is:

```
nospace
nospace
one space
one space
```

As a more complex example, this makefile:

```
all : ; @echo 'hello \
        world' ; echo "hello \
    world"
```

will invoke one shell with a command of:

```
echo 'hello \
world' ; echo "hello \
    world"
```

which, according to shell quoting rules, will yield the following output:

```
hello \
world
hello     world
```

Notice how the backslash/newline pair was removed inside the string quoted with double quotes (`"…"`), but not from the string quoted with single quotes (`'…'`). This is the way the default shell (/bin/sh) handles backslash/newline pairs. If you specify a different shell in your makefiles it may treat them differently.

Sometimes you want to split a long line inside of single quotes, but you don’t want the backslash/newline to appear in the quoted content. This is often the case when passing scripts to languages such as Perl, where extraneous backslashes inside the script can change its meaning or even be a syntax error. One simple way of handling this is to place the quoted string, or even the entire command, into a `make` variable then use the variable in the recipe. In this situation the newline quoting rules for makefiles will be used, and the backslash/newline will be removed. If we rewrite our example above using this method:

```
HELLO = 'hello \
world'

all : ; @echo $(HELLO)
```

we will get output like this:

```
hello world
```

If you like, you can also use target-specific variables (see Target-specific Variable Values) to obtain a tighter correspondence between the variable and the recipe that uses it.

Previous: Splitting Recipe Lines, Up: Recipe Syntax   [Contents][Index]

#### 5.1.2 Using Variables in Recipes

The other way in which `make` processes recipes is by expanding any variable references in them (see Basics of Variable References). This occurs after make has finished reading all the makefiles and the target is determined to be out of date; so, the recipes for targets which are not rebuilt are never expanded.

Variable and function references in recipes have identical syntax and semantics to references elsewhere in the makefile. They also have the same quoting rules: if you want a dollar sign to appear in your recipe, you must double it (‘$$’). For shells like the default shell, that use dollar signs to introduce variables, it’s important to keep clear in your mind whether the variable you want to reference is a `make` variable (use a single dollar sign) or a shell variable (use two dollar signs). For example:

```
LIST = one two three
all:
        for i in $(LIST); do \
            echo $$i; \
        done
```

results in the following command being passed to the shell:

```
for i in one two three; do \
    echo $i; \
done
```

which generates the expected result:

```
one
two
three
```

Next: Recipe Execution, Previous: Recipe Syntax, Up: Writing Recipes in Rules   [Contents][Index]

### 5.2 Recipe Echoing

Normally `make` prints each line of the recipe before it is executed. We call this *echoing* because it gives the appearance that you are typing the lines yourself.

When a line starts with ‘@’, the echoing of that line is suppressed. The ‘@’ is discarded before the line is passed to the shell. Typically you would use this for a command whose only effect is to print something, such as an `echo` command to indicate progress through the makefile:

```
@echo About to make distribution files
```

When `make` is given the flag ‘-n’ or ‘--just-print’ it only echoes most recipes, without executing them. See Summary of Options. In this case even the recipe lines starting with ‘@’ are printed. This flag is useful for finding out which recipes `make` thinks are necessary without actually doing them.

The ‘-s’ or ‘--silent’ flag to `make` prevents all echoing, as if all recipes started with ‘@’. A rule in the makefile for the special target `.SILENT` without prerequisites has the same effect (see Special Built-in Target Names).

Next: Parallel Execution, Previous: Recipe Echoing, Up: Writing Recipes in Rules   [Contents][Index]

### 5.3 Recipe Execution

When it is time to execute recipes to update a target, they are executed by invoking a new sub-shell for each line of the recipe, unless the `.ONESHELL` special target is in effect (see Using One Shell) (In practice, `make` may take shortcuts that do not affect the results.)

**Please note:** this implies that setting shell variables and invoking shell commands such as `cd` that set a context local to each process will not affect the following lines in the recipe.3 If you want to use `cd` to affect the next statement, put both statements in a single recipe line. Then `make` will invoke one shell to run the entire line, and the shell will execute the statements in sequence. For example:

```
foo : bar/lose
        cd $(<D) && gobble $(<F) > ../$@
```

Here we use the shell AND operator (`&&`) so that if the `cd` command fails, the script will fail without trying to invoke the `gobble` command in the wrong directory, which could cause problems (in this case it would certainly cause ../foo to be truncated, at least).

Next: Choosing the Shell, Previous: Recipe Execution, Up: Recipe Execution   [Contents][Index]

#### 5.3.1 Using One Shell

Sometimes you would prefer that all the lines in the recipe be passed to a single invocation of the shell. There are generally two situations where this is useful: first, it can improve performance in makefiles where recipes consist of many command lines, by avoiding extra processes. Second, you might want newlines to be included in your recipe command (for example perhaps you are using a very different interpreter as your `SHELL`). If the `.ONESHELL` special target appears anywhere in the makefile then *all* recipe lines for each target will be provided to a single invocation of the shell. Newlines between recipe lines will be preserved. For example:

```
.ONESHELL:
foo : bar/lose
        cd $(<D)
        gobble $(<F) > ../$@
```

would now work as expected even though the commands are on different recipe lines.

If `.ONESHELL` is provided, then only the first line of the recipe will be checked for the special prefix characters (‘@’, ‘-’, and ‘+’). Subsequent lines will include the special characters in the recipe line when the `SHELL` is invoked. If you want your recipe to start with one of these special characters you’ll need to arrange for them to not be the first characters on the first line, perhaps by adding a comment or similar. For example, this would be a syntax error in Perl because the first ‘@’ is removed by make:

```
.ONESHELL:
SHELL = /usr/bin/perl
.SHELLFLAGS = -e
show :
        @f = qw(a b c);
        print "@f\n";
```

However, either of these alternatives would work properly:

```
.ONESHELL:
SHELL = /usr/bin/perl
.SHELLFLAGS = -e
show :
        # Make sure "@" is not the first character on the first line
        @f = qw(a b c);
        print "@f\n";
```

or

```
.ONESHELL:
SHELL = /usr/bin/perl
.SHELLFLAGS = -e
show :
        my @f = qw(a b c);
        print "@f\n";
```

As a special feature, if `SHELL` is determined to be a POSIX-style shell, the special prefix characters in “internal” recipe lines will be *removed* before the recipe is processed. This feature is intended to allow existing makefiles to add the `.ONESHELL` special target and still run properly without extensive modifications. Since the special prefix characters are not legal at the beginning of a line in a POSIX shell script this is not a loss in functionality. For example, this works as expected:

```
.ONESHELL:
foo : bar/lose
        @cd $(@D)
        @gobble $(@F) > ../$@
```

Even with this special feature, however, makefiles with `.ONESHELL` will behave differently in ways that could be noticeable. For example, normally if any line in the recipe fails, that causes the rule to fail and no more recipe lines are processed. Under `.ONESHELL` a failure of any but the final recipe line will not be noticed by `make`. You can modify `.SHELLFLAGS` to add the `-e` option to the shell which will cause any failure anywhere in the command line to cause the shell to fail, but this could itself cause your recipe to behave differently. Ultimately you may need to harden your recipe lines to allow them to work with `.ONESHELL`.

Previous: Using One Shell, Up: Recipe Execution   [Contents][Index]

#### 5.3.2 Choosing the Shell

The program used as the shell is taken from the variable `SHELL`. If this variable is not set in your makefile, the program /bin/sh is used as the shell. The argument(s) passed to the shell are taken from the variable `.SHELLFLAGS`. The default value of `.SHELLFLAGS` is `-c` normally, or `-ec` in POSIX-conforming mode.

Unlike most variables, the variable `SHELL` is never set from the environment. This is because the `SHELL` environment variable is used to specify your personal choice of shell program for interactive use. It would be very bad for personal choices like this to affect the functioning of makefiles. See Variables from the Environment.

Furthermore, when you do set `SHELL` in your makefile that value is *not* exported in the environment to recipe lines that `make` invokes. Instead, the value inherited from the user’s environment, if any, is exported. You can override this behavior by explicitly exporting `SHELL` (see Communicating Variables to a Sub-`make`), forcing it to be passed in the environment to recipe lines.

However, on MS-DOS and MS-Windows the value of `SHELL` in the environment **is** used, since on those systems most users do not set this variable, and therefore it is most likely set specifically to be used by `make`. On MS-DOS, if the setting of `SHELL` is not suitable for `make`, you can set the variable `MAKESHELL` to the shell that `make` should use; if set it will be used as the shell instead of the value of `SHELL`.

#### Choosing a Shell in DOS and Windows

Choosing a shell in MS-DOS and MS-Windows is much more complex than on other systems.

On MS-DOS, if `SHELL` is not set, the value of the variable `COMSPEC` (which is always set) is used instead.

The processing of lines that set the variable `SHELL` in Makefiles is different on MS-DOS. The stock shell, command.com, is ridiculously limited in its functionality and many users of `make` tend to install a replacement shell. Therefore, on MS-DOS, `make` examines the value of `SHELL`, and changes its behavior based on whether it points to a Unix-style or DOS-style shell. This allows reasonable functionality even if `SHELL` points to command.com.

If `SHELL` points to a Unix-style shell, `make` on MS-DOS additionally checks whether that shell can indeed be found; if not, it ignores the line that sets `SHELL`. In MS-DOS, GNU `make` searches for the shell in the following places:

1. In the precise place pointed to by the value of `SHELL`. For example, if the makefile specifies ‘SHELL = /bin/sh’, `make` will look in the directory /bin on the current drive.
2. In the current directory.
3. In each of the directories in the `PATH` variable, in order.

In every directory it examines, `make` will first look for the specific file (sh in the example above). If this is not found, it will also look in that directory for that file with one of the known extensions which identify executable files. For example .exe, .com, .bat, .btm, .sh, and some others.

If any of these attempts is successful, the value of `SHELL` will be set to the full pathname of the shell as found. However, if none of these is found, the value of `SHELL` will not be changed, and thus the line that sets it will be effectively ignored. This is so `make` will only support features specific to a Unix-style shell if such a shell is actually installed on the system where `make` runs.

Note that this extended search for the shell is limited to the cases where `SHELL` is set from the Makefile; if it is set in the environment or command line, you are expected to set it to the full pathname of the shell, exactly as things are on Unix.

The effect of the above DOS-specific processing is that a Makefile that contains ‘SHELL = /bin/sh’ (as many Unix makefiles do), will work on MS-DOS unaltered if you have e.g. sh.exe installed in some directory along your `PATH`.

Next: Errors in Recipes, Previous: Recipe Execution, Up: Writing Recipes in Rules   [Contents][Index]

### 5.4 Parallel Execution

GNU `make` knows how to execute several recipes at once. Normally, `make` will execute only one recipe at a time, waiting for it to finish before executing the next. However, the ‘-j’ or ‘--jobs’ option tells `make` to execute many recipes simultaneously. You can inhibit parallelism for some or all targets from within the makefile (see Disabling Parallel Execution).

On MS-DOS, the ‘-j’ option has no effect, since that system doesn’t support multi-processing.

If the ‘-j’ option is followed by an integer, this is the number of recipes to execute at once; this is called the number of *job slots*. If there is nothing looking like an integer after the ‘-j’ option, there is no limit on the number of job slots. The default number of job slots is one, which means serial execution (one thing at a time).

Handling recursive `make` invocations raises issues for parallel execution. For more information on this, see Communicating Options to a Sub-`make`.

If a recipe fails (is killed by a signal or exits with a nonzero status), and errors are not ignored for that recipe (see Errors in Recipes), the remaining recipe lines to remake the same target will not be run. If a recipe fails and the ‘-k’ or ‘--keep-going’ option was not given (see Summary of Options), `make` aborts execution. If make terminates for any reason (including a signal) with child processes running, it waits for them to finish before actually exiting.

When the system is heavily loaded, you will probably want to run fewer jobs than when it is lightly loaded. You can use the ‘-l’ option to tell `make` to limit the number of jobs to run at once, based on the load average. The ‘-l’ or ‘--max-load’ option is followed by a floating-point number. For example,

```
-l 2.5
```

will not let `make` start more than one job if the load average is above 2.5. The ‘-l’ option with no following number removes the load limit, if one was given with a previous ‘-l’ option.

More precisely, when `make` goes to start up a job, and it already has at least one job running, it checks the current load average; if it is not lower than the limit given with ‘-l’, `make` waits until the load average goes below that limit, or until all the other jobs finish.

By default, there is no load limit.

Next: Output During Parallel Execution, Previous: Parallel Execution, Up: Parallel Execution   [Contents][Index]

#### 5.4.1 Disabling Parallel Execution

If a makefile completely and accurately defines the dependency relationships between all of its targets, then `make` will correctly build the goals regardless of whether parallel execution is enabled or not. This is the ideal way to write makefiles.

However, sometimes some or all of the targets in a makefile cannot be executed in parallel and it’s not feasible to add the prerequisites needed to inform `make`. In that case the makefile can use various methods to disable parallel execution.

If the `.NOTPARALLEL` special target with no prerequisites is specified anywhere then the entire instance of `make` will be run serially, regardless of the parallel setting. For example:

```
all: one two three
one two three: ; @sleep 1; echo $@

.NOTPARALLEL:
```

Regardless of how `make` is invoked, the targets one, two, and three will be run serially.

If the `.NOTPARALLEL` special target has prerequisites, then each of those prerequisites will be considered a target and all prerequisites of these targets will be run serially. Note that only when building this target will the prerequisites be run serially: if some other target lists the same prerequisites and is not in `.NOTPARALLEL` then these prerequisites may be run in parallel. For example:

```
all: base notparallel

base: one two three
notparallel: one two three

one two three: ; @sleep 1; echo $@

.NOTPARALLEL: notparallel
```

Here ‘make -j base’ will run the targets one, two, and three in parallel, while ‘make -j notparallel’ will run them serially. If you run ‘make -j all’ then they *will* be run in parallel since base lists them as prerequisites and is not serialized.

The `.NOTPARALLEL` target should not have commands.

Finally you can control the serialization of specific prerequisites in a fine-grained way using the `.WAIT` special target. When this target appears in a prerequisite list and parallel execution is enabled, `make` will not build any of the prerequisites to the *right* of `.WAIT` until all prerequisites to the *left* of `.WAIT` have completed. For example:

```
all: one two .WAIT three
one two three: ; @sleep 1; echo $@
```

If parallel execution is enabled, `make` will try to build one and two in parallel but will not try to build three until both are complete.

As with targets provided to `.NOTPARALLEL`, `.WAIT` takes effect only when building the target in whose prerequisite list it appears. If the same prerequisites are present in other targets, without `.WAIT`, then they may still be run in parallel. Because of this, neither `.NOTPARALLEL` with targets nor `.WAIT` are as reliable for controlling parallel execution as defining a prerequisite relationship. However they are easy to use and may be sufficient in less complex situations.

The `.WAIT` prerequisite will not be present in any of the automatic variables for the rule.

You can create an actual target `.WAIT` in your makefile for portability but this is not required to use this feature. If a `.WAIT` target is created it should not have prerequisites or commands.

The `.WAIT` feature is also implemented in other versions of `make` and it’s specified in the POSIX standard for `make`.

Next: Input During Parallel Execution, Previous: Disabling Parallel Execution, Up: Parallel Execution   [Contents][Index]

#### 5.4.2 Output During Parallel Execution

When running several recipes in parallel the output from each recipe appears as soon as it is generated, with the result that messages from different recipes may be interspersed, sometimes even appearing on the same line. This can make reading the output very difficult.

To avoid this you can use the ‘--output-sync’ (‘-O’) option. This option instructs `make` to save the output from the commands it invokes and print it all once the commands are completed. Additionally, if there are multiple recursive `make` invocations running in parallel, they will communicate so that only one of them is generating output at a time.

If working directory printing is enabled (see The ‘--print-directory’ Option), the enter/leave messages are printed around each output grouping. If you prefer not to see these messages add the ‘--no-print-directory’ option to `MAKEFLAGS`.

There are four levels of granularity when synchronizing output, specified by giving an argument to the option (e.g., ‘-Oline’ or ‘--output-sync=recurse’).

**`none`**

This is the default: all output is sent directly as it is generated and no synchronization is performed.

**`line`**

Output from each individual line of the recipe is grouped and printed as soon as that line is complete. If a recipe consists of multiple lines, they may be interspersed with lines from other recipes.

**`target`**

Output from the entire recipe for each target is grouped and printed once the target is complete. This is the default if the `--output-sync` or `-O` option is given with no argument.

**`recurse`**

Output from each recursive invocation of `make` is grouped and printed once the recursive invocation is complete.

Regardless of the mode chosen, the total build time will be the same. The only difference is in how the output appears.

The ‘target’ and ‘recurse’ modes both collect the output of the entire recipe of a target and display it uninterrupted when the recipe completes. The difference between them is in how recipes that contain recursive invocations of `make` are treated (see Recursive Use of `make`). For all recipes which have no recursive lines, the ‘target’ and ‘recurse’ modes behave identically.

If the ‘recurse’ mode is chosen, recipes that contain recursive `make` invocations are treated the same as other targets: the output from the recipe, including the output from the recursive `make`, is saved and printed after the entire recipe is complete. This ensures output from all the targets built by a given recursive `make` instance are grouped together, which may make the output easier to understand. However it also leads to long periods of time during the build where no output is seen, followed by large bursts of output. If you are not watching the build as it proceeds, but instead viewing a log of the build after the fact, this may be the best option for you.

If you are watching the output, the long gaps of quiet during the build can be frustrating. The ‘target’ output synchronization mode detects when `make` is going to be invoked recursively, using the standard methods, and it will not synchronize the output of those lines. The recursive `make` will perform the synchronization for its targets and the output from each will be displayed immediately when it completes. Be aware that output from recursive lines of the recipe are not synchronized (for example if the recursive line prints a message before running `make`, that message will not be synchronized).

The ‘line’ mode can be useful for front-ends that are watching the output of `make` to track when recipes are started and completed.

Some programs invoked by `make` may behave differently if they determine they’re writing output to a terminal versus a file (often described as “interactive” vs. “non-interactive” modes). For example, many programs that can display colorized output will not do so if they determine they are not writing to a terminal. If your makefile invokes a program like this then using the output synchronization options will cause the program to believe it’s running in “non-interactive” mode even though the output will ultimately go to the terminal.
