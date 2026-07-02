---
title: "Autoconf (part 17/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 17/26
---

## 12 Portable Make Programming

Writing portable makefiles is an art. Since a makefile’s commands are executed by the shell, you must consider the shell portability issues already mentioned. However, other issues are specific to `make` itself.

### 12.1 `$<` in Ordinary Make Rules

POSIX says that the ‘$<’ construct in makefiles can be used only in inference rules and in the ‘.DEFAULT’ rule; its meaning in ordinary rules is unspecified. Solaris `make` for instance replaces it with the empty string. OpenBSD (3.0 and later) `make` diagnoses these uses and errors out.

### 12.2 Failure in Make Rules

Unless errors are being ignored (e.g., because a makefile command line is preceded by a ‘-’ prefix), POSIX 2008 requires that `make` must invoke each command with the equivalent of a ‘sh -e -c’ subshell, which causes the subshell to exit immediately if a subsidiary simple-command fails, with some complicated exceptions. Historically not all `make` implementations followed this rule. For example, the command ‘touch T; rm -f U’ may attempt to remove U even if the `touch` fails, although this is not permitted with POSIX make. One way to work around failures in simple commands is to reword them so that they always succeed, e.g., ‘touch T || :; rm -f U’. However, even this approach can run into common bugs in BSD implementations of the -e option of `sh` and `set` (see Limitations of Shell Builtins), so if you are worried about porting to buggy BSD shells it may be simpler to migrate complicated `make` actions into separate scripts.

### 12.3 Makefile Command Line Prefixes

Makefile command lines can be preceded by zero or more of the command line prefixes ‘-’, ‘@’, and ‘+’, which modify how `make` processes the command. Although POSIX says these are the only command line prefixes, some `make` implementations, such as Solaris `make`, support the additional prefixes ‘!’ and ‘?’. Portable makefiles should therefore avoid using these two characters at the start of a makefile command line. For example:

```
mishandled-by-Solaris-make:; ! grep FIXME foo.c
portable-to-Solaris-make:; :;! grep FIXME foo.c
```

### 12.4 Special Characters in Make Macro Names

POSIX limits macro names to nonempty strings containing only ASCII letters and digits, ‘.’, and ‘_’. Many `make` implementations allow a wider variety of characters, but portable makefiles should avoid them. It is portable to start a name with a special character, e.g., ‘$(.FOO)’.

Some ancient `make` implementations don’t support leading underscores in macro names. An example is NEWS-OS 4.2R.

```
$ cat Makefile
_am_include = #
_am_quote =
all:; @echo this is test
$ make
Make: Must be a separator on rules line 2.  Stop.
$ cat Makefile2
am_include = #
am_quote =
all:; @echo this is test
$ make -f Makefile2
this is test
```

However, this problem is no longer of practical concern.

### 12.5 Backslash-Newline Before Empty Lines

On some versions of HP-UX, `make` reads multiple newlines following a backslash, continuing to the next non-empty line. For example,

```
FOO = one \

BAR = two

test:
        : FOO is "$(FOO)"
        : BAR is "$(BAR)"
```

shows `FOO` equal to `one BAR = two`. Other implementations sensibly let a backslash continue only to the immediately following line.

### 12.7 `make macro=value` and Submakes

A command-line variable definition such as `foo=bar` overrides any definition of `foo` in a makefile. Some `make` implementations (such as GNU `make`) propagate this override to subsidiary invocations of `make`. Some other implementations do not pass the substitution along to submakes.

```
$ cat Makefile
foo = foo
one:
        @printf '%s\n' $(foo)
        $(MAKE) two
two:
        @printf '%s\n' $(foo)
$ make foo=bar            # GNU make 3.79.1
bar
make two
make[1]: Entering directory `/home/adl'
bar
make[1]: Leaving directory `/home/adl'
$ pmake foo=bar           # BSD make
bar
pmake two
foo
```

You have a few possibilities if you do want the `foo=bar` override to propagate to submakes. One is to use the -e option, which causes all environment variables to have precedence over the makefile macro definitions, and declare foo as an environment variable:

```
$ env foo=bar make -e
```

The -e option is propagated to submakes automatically, and since the environment is inherited between `make` invocations, the `foo` macro is overridden in submakes as expected.

This syntax (`foo=bar make -e`) is portable only when used outside of a makefile, for instance from a script or from the command line. When run inside a `make` rule, GNU `make` 3.80 and prior versions forget to propagate the -e option to submakes.

Moreover, using -e could have unexpected side effects if your environment contains some other macros usually defined by the makefile. (See also the note about `make -e` and `SHELL` below.)

If you can foresee all macros that a user might want to override, then you can propagate them to submakes manually, from your makefile:

```
foo = foo
one:
        @printf '%s\n' $(foo)
        $(MAKE) foo=$(foo) two
two:
        @printf '%s\n' $(foo)
```

Another way to propagate a variable to submakes in a portable way is to expand an extra variable in every invocation of ‘$(MAKE)’ within your makefile:

```
foo = foo
one:
        @printf '%s\n' $(foo)
        $(MAKE) $(SUBMAKEFLAGS) two
two:
        @printf '%s\n' $(foo)
```

Users must be aware that this technique is in use to take advantage of it, e.g. with `make foo=bar SUBMAKEFLAGS='foo=bar'`, but it allows any macro to be overridden. Makefiles generated by `automake` use this technique, expanding `$(AM_MAKEFLAGS)` on the command lines of submakes (see Automake in *GNU Automake*).

### 12.8 The Make Macro MAKEFLAGS

POSIX requires `make` to use `MAKEFLAGS` to affect the current and recursive invocations of make, but allows implementations several formats for the variable. It is tricky to parse `$MAKEFLAGS` to determine whether -s for silent execution or -k for continued execution are in effect. For example, you cannot assume that the first space-separated word in `$MAKEFLAGS` contains single-letter options, since in the Cygwin version of GNU `make` it is either --unix or --win32 with the second word containing single-letter options.

```
$ cat Makefile
all:
        @printf 'MAKEFLAGS = %s\n' '$(MAKEFLAGS)'
$ make
MAKEFLAGS = --unix
$ make -k
MAKEFLAGS = --unix -k
```

### 12.9 The Make Macro `SHELL`

Many `make` implementations use the `$(SHELL)` macro to spawn shell processes and execute Make rules. This is a builtin macro with a default value upplied by `make`; the default can be overridden by a makefile or by a command-line argument, though not by the environment.

Other `make` implementations use other ways to spawn shell processes, and the POSIX standard for `make` says that portable makefiles should neither define nor use the `$(SHELL)` macro.

Despite this prohibition, in practice it does not hurt to define and then possibly use `SHELL` in your makefiles and in some cases it can help your builds use a better shell to spawn shell processes. So it’s a good idea to define `SHELL` in your makefiles. If you use Autoconf, you can use its standard output variable `SHELL` as follows:

```
SHELL = @SHELL@
```

If you use Automake, this is done for you.

Do not force `SHELL = /bin/sh` because that is not correct everywhere. Remember, /bin/sh is not POSIX compliant on some systems, such as Solaris 10. Additionally, DJGPP lacks `/bin/sh`, and when its GNU `make` port sees such a setting it enters a special emulation mode where features like pipes and redirections are emulated on top of DOS’s `command.com`. Unfortunately this emulation is incomplete; for instance it does not handle command substitutions. Using `@SHELL@` means that your makefile will benefit from the same improved shell, such as `bash` or `ksh`, that was discovered during `configure`, so that you aren’t fighting two different sets of shell bugs between the two contexts.

Do not rely on whether `make`’s `SHELL` settings are exported to subprocesses, as implementations differ:

```
$ cat Makefile
all:
        @printf '%s\n' '$(SHELL)'
        @printenv SHELL
$ env SHELL=/bin/sh make -e SHELL=/bin/ksh  # BSD make, AIX make
/bin/ksh
/bin/ksh
$ env SHELL=/bin/sh make -e SHELL=/bin/ksh  # GNU make
/bin/ksh
sh
```

### 12.10 Parallel Make

Support for parallel execution in `make` implementation varies. Generally, using GNU make is your best bet.

When NetBSD or FreeBSD `make` are run in parallel mode, they will reuse the same shell for multiple commands within one recipe. This can have various unexpected consequences. For example, changes of directories or variables persist between recipes, so that:

```
all:
        @var=value; cd /; pwd; echo $$var; echo $$$$
        @pwd; echo $$var; echo $$$$
```

may output the following with `make -j1`, at least on NetBSD up to 5.1 and FreeBSD up to 8.2:

```
/
value
32235
/
value
32235
```

while without -j1, or with -B, the output looks less surprising:

```
/
value
32238
/tmp

32239
```

Another consequence is that, if one command in a recipe uses `exit 0` to indicate a successful exit, the shell will be gone and the remaining commands of this recipe will not be executed.

The BSD `make` implementations, when run in parallel mode, will also pass the `Makefile` recipes to the shell through its standard input, thus making it unusable from the recipes:

```
$ cat Makefile
read:
        @read line; echo LINE: $$line
$ echo foo | make read
LINE: foo
$ echo foo | make -j1 read # NetBSD 5.1 and FreeBSD 8.2
LINE:
```

Moreover, when FreeBSD `make` (up at least to 8.2) is run in parallel mode, it implements the `@` and `-` “recipe modifiers” by dynamically modifying the active shell flags. This behavior has the effects of potentially clobbering the exit status of recipes silenced with the `@` modifier if they also unset the errexit shell flag, and of mangling the output in unexpected ways:

```
$ cat Makefile
a:
        @echo $$-; set +e; false
b:
        -echo $$-; false; echo set -
$ make a; echo status: $?
ehBc
*** Error code 1
status: 1
$ make -j1 a; echo status: $?
ehB
status: 0
$ make b
echo $-; echo set -
hBc
set -
$ make -j1 b
echo $-; echo hvB
```

You can avoid all these issues by using the -B option to enable compatibility semantics. However, that will effectively also disable all parallelism as that will cause prerequisites to be updated in the order they are listed in a rule.

Some make implementations (among them, FreeBSD `make`, NetBSD `make`, and Solaris `dmake`), when invoked with a -j*N* option, connect the standard output and standard error of all their child processes to pipes or temporary regular files. This can lead to subtly different semantics in the behavior of the spawned processes. For example, even if the `make` standard output is connected to a tty, the recipe command will not be:

```
$ cat Makefile
all:
        @test -t 1 && echo "Is a tty" || echo "Is not a tty"
$ make -j 2 # FreeBSD 8.2 make
Is not a tty
$ make -j 2 # NetBSD 5.1 make
--- all ---
Is not a tty
$ dmake -j 2 # Solaris 10 dmake
hostname --> 1 job
hostname --> Job output
Is not a tty
```

On the other hand:

```
$ make -j 2 # GNU make, Heirloom make
Is a tty
```

The above examples also show additional status output produced in parallel mode for targets being updated by Solaris `dmake` and NetBSD `make` (but *not* by FreeBSD `make`).

Furthermore, parallel runs of those `make` implementations will route standard error from commands that they spawn into their own standard output, and may remove leading whitespace from output lines.

### 12.12 Newlines in Make Rules

In shell scripts, newlines can be used inside string literals. But in the shell statements of Makefile rules, this is not possible: a newline not preceded by a backslash separates commands, whereas a newline preceded by a backslash becomes part of the shell statement. So, how can a newline be used in a string literal?

The trick is to set up a shell variable `nl` that contains a newline. For example, the following uses a multi-line ‘sed’ expression that appends an empty line after every line of a file:

```
output: input
        eval "$$(printf 'nl="\n"\n')"; \
        sed "a\\$$nl" input >$@
```

### 12.14 Trailing whitespace in Make Macros

GNU `make` 3.80 mistreats trailing whitespace in macro substitutions and appends another spurious suffix:

```
empty =
foo = bar $(empty)
print: ; @echo $(foo:=.test)
```

prints ‘bar.test .test’.

BSD and Solaris `make` implementations do not honor trailing whitespace in macro definitions as POSIX requires:

```
foo = bar # Note the space after "bar".
print: ; @echo $(foo)t
```

prints ‘bart’ instead of ‘bar t’. To work around this, you can use a helper macro as in the previous example.

### 12.15 Command-line Macros and whitespace

Some `make` implementations may strip trailing whitespace off of macros set on the command line in addition to leading whitespace. Further, some may strip leading whitespace off of macros set from environment variables:

```
$ echo 'print: ; @echo "x$(foo)x$(bar)x"' |
  foo=' f f ' make -f - bar=' b b '
x f f xb b x  # AIX, BSD, GNU make
xf f xb b x   # HP-UX
x f f xb bx   # Solaris make
```

### 12.16 The obj/ Subdirectory and Make

Never name one of your subdirectories obj/ if you don’t like surprises.

If an obj/ directory exists, BSD `make` enters it before reading the makefile. Hence the makefile in the current directory is not read.

```
$ cat Makefile
all:
        echo Hello
$ cat obj/Makefile
all:
        echo World
$ make      # GNU make
echo Hello
Hello
$ pmake     # BSD make
echo World
World
```

### 12.17 Exit Status of `make -k`

Do not rely on the exit status of `make -k`. Some implementations reflect whether they encountered an error in their exit status; other implementations always succeed.

```
$ cat Makefile
all:
        false
$ make -k; echo exit status: $?    # GNU make
false
make: *** [all] Error 1
exit status: 2
$ pmake -k; echo exit status: $?   # BSD make
false
*** Error code 1 (continuing)
exit status: 0
```

### 12.18 `VPATH` and Make

POSIX does not specify the semantics of `VPATH`. Typically, `make` supports `VPATH`, but its implementation is not consistent.

Autoconf and Automake support makefiles whose usages of `VPATH` are portable to recent-enough popular implementations of `make`, but to keep the resulting makefiles portable, a package’s makefile prototypes must take the following issues into account. These issues are complicated and are often poorly understood, and installers who use `VPATH` should expect to find many bugs in this area. If you use `VPATH`, the simplest way to avoid these portability bugs is to stick with GNU `make`, since it is the most commonly-used `make` among Autoconf users.

Here are some known issues with some `VPATH` implementations.

#### 12.18.1 Variables listed in `VPATH`

Do not set `VPATH` to the value of another variable, for example ‘VPATH = $(srcdir)’, because some ancient versions of `make` do not do variable substitutions on the value of `VPATH`. For example, use this

```
srcdir = @srcdir@
VPATH = @srcdir@
```

rather than ‘VPATH = $(srcdir)’. Note that with GNU Automake, there is no need to set this yourself.

#### 12.18.2 `VPATH` and Double-colon Rules

With ancient versions of Sun `make`, any assignment to `VPATH` causes `make` to execute only the first set of double-colon rules. However, this problem is no longer of practical concern.

#### 12.18.3 `$<` Not Supported in Explicit Rules

Using `$<` in explicit rules is not portable. The prerequisite file must be named explicitly in the rule. If you want to find the prerequisite via a `VPATH` search, you have to code the whole thing manually. See Build Directories.

#### 12.18.4 Automatic Rule Rewriting

Some `make` implementations, such as Solaris, search for prerequisites in `VPATH` and then rewrite each occurrence as a plain word in the rule. For instance:

```
# This isn't portable to GNU make.
VPATH = ../pkg/src
f.c: if.c
        cp if.c f.c
```

executes `cp ../pkg/src/if.c f.c` if if.c is found in ../pkg/src.

However, this rule leads to real problems in practice. For example, if the source directory contains an ordinary file named test that is used in a dependency, Solaris `make` rewrites commands like ‘if test -r foo; …’ to ‘if ../pkg/src/test -r foo; …’, which is typically undesirable. In fact, `make` is completely unaware of shell syntax used in the rules, so the VPATH rewrite can potentially apply to *any* whitespace-separated word in a rule, including shell variables, functions, and keywords.

```
$ mkdir build
$ cd build
$ cat > Makefile <<'END'
VPATH = ..
all: arg func for echo
        func () { for arg in "$$@"; do echo $$arg; done; }; \
        func "hello world"
END
$ touch ../arg ../func ../for ../echo
$ make
../func () { ../for ../arg in "$@"; do ../echo $arg; done; }; \
../func "hello world"
sh: syntax error at line 1: `do' unexpected
*** Error code 2
```

To avoid this problem, portable makefiles should never mention a source file or dependency whose name is that of a shell keyword like for or until, a shell command like `cat` or `gcc` or `test`, or a shell function or variable used in the corresponding `Makefile` recipe.

Because of these problems GNU `make` and many other `make` implementations do not rewrite commands, so portable makefiles should search `VPATH` manually. It is tempting to write this:

```
# This isn't portable to Solaris make.
VPATH = ../pkg/src
f.c: if.c
        cp `test -f if.c || echo $(VPATH)/`if.c f.c
```

However, the “prerequisite rewriting” still applies here. So if if.c is in ../pkg/src, Solaris `make` executes

```
cp `test -f ../pkg/src/if.c || echo ../pkg/src/`if.c f.c
```

which reduces to

```
cp if.c f.c
```

and thus fails. Oops.

A simple workaround, and good practice anyway, is to use ‘$?’ and ‘$@’ when possible:

```
VPATH = ../pkg/src
f.c: if.c
        cp $? $@
```

but this does not generalize well to commands with multiple prerequisites. A more general workaround is to rewrite the rule so that the prerequisite if.c never appears as a plain word. For example, these three rules would be safe, assuming if.c is in ../pkg/src and the other files are in the working directory:

```
VPATH = ../pkg/src
f.c: if.c f1.c
        cat `test -f ./if.c || echo $(VPATH)/`if.c f1.c >$@
g.c: if.c g1.c
        cat `test -f 'if.c' || echo $(VPATH)/`if.c g1.c >$@
h.c: if.c h1.c
        cat `test -f "if.c" || echo $(VPATH)/`if.c h1.c >$@
```

Things get worse when your prerequisites are in a macro.

```
VPATH = ../pkg/src
HEADERS = f.h g.h h.h
install-HEADERS: $(HEADERS)
        for i in $(HEADERS); do \
          $(INSTALL) -m 644 \
            `test -f $$i || echo $(VPATH)/`$$i \
            $(DESTDIR)$(includedir)/$$i; \
        done
```

The above `install-HEADERS` rule is not Solaris-proof because `for i in $(HEADERS);` is expanded to `for i in f.h g.h h.h;` where `f.h` and `g.h` are plain words and are hence subject to `VPATH` adjustments.

If the three files are in ../pkg/src, the rule is run as:

```
for i in ../pkg/src/f.h ../pkg/src/g.h h.h; do \
  install -m 644 \
     `test -f $i || echo ../pkg/src/`$i \
     /usr/local/include/$i; \
done
```

where the two first `install` calls fail. For instance, consider the `f.h` installation:

```
install -m 644 \
  `test -f ../pkg/src/f.h || \
    echo ../pkg/src/ \
  `../pkg/src/f.h \
  /usr/local/include/../pkg/src/f.h;
```

It reduces to:

```
install -m 644 \
  ../pkg/src/f.h \
  /usr/local/include/../pkg/src/f.h;
```

Note that the manual `VPATH` search did not cause any problems here; however this command installs f.h in an incorrect directory.

Trying to quote `$(HEADERS)` in some way, as we did for `foo.c` a few makefiles ago, does not help:

```
install-HEADERS: $(HEADERS)
        headers='$(HEADERS)'; \
        for i in $$headers; do \
          $(INSTALL) -m 644 \
            `test -f $$i || echo $(VPATH)/`$$i \
            $(DESTDIR)$(includedir)/$$i; \
        done
```

Now, `headers='$(HEADERS)'` macro-expands to:

```
headers='f.h g.h h.h'
```

but `g.h` is still a plain word. (As an aside, the idiom `headers='$(HEADERS)'; for i in $$headers;` is a good idea if `$(HEADERS)` can be empty, because some shells diagnose a syntax error on `for i in;`.)

One workaround is to strip this unwanted ../pkg/src/ prefix manually:

```
VPATH = ../pkg/src
HEADERS = f.h g.h h.h
install-HEADERS: $(HEADERS)
        headers='$(HEADERS)'; \
        for i in $$headers; do \
          i=`expr "$$i" : '$(VPATH)/\(.*\)'`;
          $(INSTALL) -m 644 \
            `test -f $$i || echo $(VPATH)/`$$i \
            $(DESTDIR)$(includedir)/$$i; \
        done
```

Automake does something similar.

#### 12.18.5 Make Target Lookup

GNU `make` uses a complex algorithm to decide when it should use files found via a `VPATH` search. See How Directory Searches are Performed in *The GNU Make Manual*.

If a target needs to be rebuilt, GNU `make` discards the file name found during the `VPATH` search for this target, and builds the file locally using the file name given in the makefile. If a target does not need to be rebuilt, GNU `make` uses the file name found during the `VPATH` search.

Other `make` implementations, like NetBSD `make`, are easier to describe: the file name found during the `VPATH` search is used whether the target needs to be rebuilt or not. Therefore new files are created locally, but existing files are updated at their `VPATH` location.

OpenBSD and FreeBSD `make`, however, never perform a `VPATH` search for a dependency that has an explicit rule. This is extremely annoying.

When attempting a `VPATH` build for an autoconfiscated package (e.g., `mkdir build && cd build && ../configure`), this means GNU `make` builds everything locally in the build directory, while BSD `make` builds new files locally and updates existing files in the source directory.

```
$ cat Makefile
VPATH = ..
all: foo.x bar.x
foo.x bar.x: newer.x
        @echo Building $@
$ touch ../bar.x
$ touch ../newer.x
$ make        # GNU make
Building foo.x
Building bar.x
$ pmake       # NetBSD make
Building foo.x
Building ../bar.x
$ fmake       # FreeBSD make, OpenBSD make
Building foo.x
Building bar.x
$ make        # GNU make
Building foo.x
$ pmake       # NetBSD make
Building foo.x
$ fmake       # FreeBSD make, OpenBSD make
Building foo.x
Building bar.x
```

Note how NetBSD `make` updates ../bar.x in its VPATH location, and how FreeBSD and OpenBSD `make` always update bar.x, even when ../bar.x is up to date.

Another point worth mentioning is that once GNU `make` has decided to ignore a `VPATH` file name (e.g., it ignored ../bar.x in the above example) it continues to ignore it when the target occurs as a prerequisite of another rule.

The following example shows that GNU `make` does not look up bar.x in `VPATH` before performing the `.x.y` rule, because it ignored the `VPATH` result of bar.x while running the `bar.x: newer.x` rule.

```
$ cat Makefile
VPATH = ..
all: bar.y
bar.x: newer.x
        @echo Building $@
.SUFFIXES: .x .y
.x.y:
        cp $< $@
$ touch ../bar.x
$ touch ../newer.x
$ make        # GNU make
Building bar.x
cp bar.x bar.y
cp: cannot stat 'bar.x': No such file or directory
make: *** [bar.y] Error 1
$ pmake       # NetBSD make
Building ../bar.x
cp ../bar.x bar.y
$ rm bar.y
$ fmake       # FreeBSD make, OpenBSD make
echo Building bar.x
cp bar.x bar.y
cp: cannot stat 'bar.x': No such file or directory
*** Error code 1
```

Note that if you drop away the command from the `bar.x: newer.x` rule, GNU `make` magically starts to work: it knows that `bar.x` hasn’t been updated, therefore it doesn’t discard the result from `VPATH` (../bar.x) in succeeding uses. FreeBSD and OpenBSD still don’t work, though.

```
$ cat Makefile
VPATH = ..
all: bar.y
bar.x: newer.x
.SUFFIXES: .x .y
.x.y:
        cp $< $@
$ touch ../bar.x
$ touch ../newer.x
$ make        # GNU make
cp ../bar.x bar.y
$ rm bar.y
$ pmake       # NetBSD make
cp ../bar.x bar.y
$ rm bar.y
$ fmake       # FreeBSD make, OpenBSD make
cp bar.x bar.y
cp: cannot stat 'bar.x': No such file or directory
*** Error code 1
```

It seems the sole solution that would please every `make` implementation is to never rely on `VPATH` searches for targets. In other words, `VPATH` should be reserved to sources that are not built.

### 12.19 Single Suffix Rules and Separated Dependencies

A *Single Suffix Rule* is basically a usual suffix (inference) rule (‘.from.to:’), but which *destination* suffix is empty (‘.from:’).

*Separated dependencies* simply refers to listing the prerequisite of a target, without defining a rule. Usually one can list on the one hand side, the rules, and on the other hand side, the dependencies.

Solaris `make` does not support separated dependencies for targets defined by single suffix rules:

```
$ cat Makefile
.SUFFIXES: .in
foo: foo.in
.in:
        cp $< $@
$ touch foo.in
$ make
$ ls
Makefile  foo.in
```

while GNU Make does:

```
$ gmake
cp foo.in foo
$ ls
Makefile  foo       foo.in
```

Note it works without the ‘foo: foo.in’ dependency.

```
$ cat Makefile
.SUFFIXES: .in
.in:
        cp $< $@
$ make foo
cp foo.in foo
```

and it works with double suffix inference rules:

```
$ cat Makefile
foo.out: foo.in
.SUFFIXES: .in .out
.in.out:
        cp $< $@
$ make
cp foo.in foo.out
```

As a result, in such a case, you have to write target rules.

### 12.20 Timestamp Resolution and Make

Traditionally, file timestamps had 1-second resolution, and `make` used those timestamps to determine whether one file was newer than the other. However, many modern file systems have timestamps with 1-nanosecond resolution. Some `make` implementations look at the entire timestamp; others ignore the fractional part, which can lead to incorrect results. Normally this is not a problem, but in some extreme cases you may need to use tricks like ‘sleep 1’ to work around timestamp truncation bugs.

Traditionally, commands like ‘cp -p’ and ‘touch -r’ did not copy file timestamps to their full resolutions (see Limitations of Usual Tools). Hence you should be wary of rules like this:

```
dest: src
        cp -p src dest
```

as dest often appears to be older than src after the timestamp is truncated, and this can cause `make` to do needless rework the next time it is invoked. To work around this problem, you can use a timestamp file, e.g.:

```
dest-stamp: src
        cp -p src dest
        echo >dest-stamp
```

Apart from timestamp resolution, there are also differences in handling equal timestamps. Although POSIX suggests that `make` update a target with the same timestamp as its newest prerequisite, only HP-UX `make` is known to do so; GNU and other `make` implementations do not update, a behavior that POSIX also allows.

The HP-UX behavior can cause spurious rebuilds and this in turn can cause `make` to fail if it tries to rebuild generated files in a possibly read-only source tree with tools not present on the build machine. Conversely, if a source file is updated immediately after running `make` in a file system with low-resolution timestamps, the GNU behavior can cause a later `make` to neglect rebuilds and quietly generate incorrect results. To avoid both these problems, use GNU `make` on a platform with high-resolution timestamps.
