---
title: "automake (part 10/14)"
source: https://www.gnu.org/software/automake/manual/automake.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 10/14
---

## 18 Miscellaneous Rules

There are a few rules and variables that didn’t fit anywhere else.

### 18.1 Interfacing to `etags`

Automake will generate rules to generate TAGS files for use with GNU Emacs under some circumstances.

If any C, C++ or Fortran 77 source code or headers are present, then `tags` and `TAGS` rules will be generated for the directory. All files listed using the `_SOURCES`, `_HEADERS`, and `_LISP` primaries will be used to generate tags. Generated source files that are not distributed must be declared in variables like `nodist_noinst_HEADERS` or `nodist_*prog*_SOURCES` or they will be ignored.

A `tags` rule will be output at the topmost directory of a multi-directory package. When run from this topmost directory, ‘make tags’ will generate a TAGS file that includes by reference all TAGS files from subdirectories.

The `tags` rule will also be generated if the variable `ETAGS_ARGS` is defined. This variable is intended for use in directories that contain taggable source that `etags` does not understand. The user can use the `ETAGSFLAGS` to pass additional flags to `etags`; `AM_ETAGSFLAGS` is also available for use in Makefile.am. The variable `ETAGS` is the name of the program to invoke (by default `etags`).

Here is how Automake generates tags for its source, and for nodes in its Texinfo file:

```
ETAGS_ARGS = automake.in --lang=none \
 --regex='/^@node[ \t]+\([^,]+\)/\1/' automake.texi
```

If you add file names to `ETAGS_ARGS`, you will probably also want to define `TAGS_DEPENDENCIES`. The contents of this variable are added directly to the dependencies for the `tags` rule.

Automake also generates a `ctags` rule that can be used to build `vi`-style tags files. The variable `CTAGS` is the name of the program to invoke (by default `ctags`); `CTAGSFLAGS` can be used by the user to pass additional flags, and `AM_CTAGSFLAGS` can be used by the Makefile.am.

Automake will also generate an `ID` rule that will run `mkid` on the source. This is only supported on a directory-by-directory basis.

Similarly, the `cscope` rule will create a list of all the source files in the tree and run `cscope` to build an inverted index database. The variable `CSCOPE` is the name of the program to invoke (by default `cscope`); `CSCOPEFLAGS` and `CSCOPE_ARGS` can be used by the user to pass additional flags and file names respectively, while `AM_CSCOPEFLAGS` can be used by the Makefile.am. Note that, currently, the Automake-provided `cscope` support, when used in a VPATH build, might not work well with non-GNU make implementations (especially with make implementations performing VPATH rewrites in *The Autoconf Manual*).

Finally, Automake also emits rules to support the GNU Global Tags program. The `GTAGS` rule runs Global Tags and puts the result in the top build directory. The variable `GTAGS_ARGS` holds arguments that are passed to `gtags`.

### 18.2 Handling new file extensions

It is sometimes useful to introduce a new implicit rule to handle a file type that Automake does not know about.

For instance, suppose you had a compiler that could compile .foo files to .o files. You would simply define a suffix rule for your language:

```
.foo.o:
        foocc -c -o $@ $<
```

Then you could directly use a .foo file in a `_SOURCES` variable and expect the correct results:

```
bin_PROGRAMS = doit
doit_SOURCES = doit.foo
```

That is the simpler and more common case. In other cases, you have to help Automake to figure out which extensions you are defining your suffix rule for. This usually happens when your extension does not start with a dot. Then, you have to put the list of new suffixes in the `SUFFIXES` variable *before* you define your implicit rule.

For instance, the following definition prevents Automake from misinterpreting the ‘.idlC.cpp:’ rule as an attempt to transform .idlC files into .cpp files.

```
SUFFIXES = .idl C.cpp
.idlC.cpp:
        # whatever
```

As you may have noted, the `SUFFIXES` variable behaves like the `.SUFFIXES` special target of `make`. You should not touch `.SUFFIXES` yourself, but use `SUFFIXES` instead and let Automake generate the suffix list for `.SUFFIXES`. Any given `SUFFIXES` go at the start of the generated suffixes list, followed by Automake generated suffixes not already in the list.

Automake disables the Make program’s built-in rules with a `.SUFFIXES:` rule, and then adds whatever suffixes are necessary. Automake also disables GNU Make’s built-in pattern rules.


## 19 Include

Automake supports an `include` directive that can be used to include other Makefile fragments when `automake` is run. Note that these fragments are read and interpreted by `automake`, not by `make`. As with conditionals, `make` has no idea that `include` is in use.

There are two forms of `include`:

**`include $(srcdir)/file`**

Include a fragment that is found relative to the current source directory.

**`include $(top_srcdir)/file`**

Include a fragment that is found relative to the top source directory.

Note that if a fragment is included inside a conditional, then the condition applies to the entire contents of that fragment.

Makefile fragments included this way are always distributed because they are needed to rebuild Makefile.in.

Inside a fragment, the construct `%reldir%` is replaced with the directory of the fragment relative to the base Makefile.am. Similarly, `%canon_reldir%` is replaced with the canonicalized (see How derived variables are named) form of `%reldir%`. As a convenience, `%D%` is a synonym for `%reldir%`, and `%C%` is a synonym for `%canon_reldir%`.

A special feature is that if the fragment is in the same directory as the base Makefile.am (i.e., `%reldir%` is `.`), then:

**`%reldir%`**

together with a following slash expands to the empty string, otherwise it expands to a dot;

**`%canon_reldir%`**

together with a following underscore expands to the empty string, otherwise it expands to an underscore.

Thus, a Makefile fragment might look like this:

```
bin_PROGRAMS += %reldir%/mumble
%canon_reldir%_mumble_SOURCES = %reldir%/one.c
```


## 20 Conditionals

Automake supports a simple type of conditional.

These conditionals are not the same as conditionals in GNU Make. Automake conditionals are checked at configure time by the configure script, and affect the translation from Makefile.in to Makefile. They are based on options passed to configure and on results that configure has discovered about the host system. GNU Make conditionals are checked at `make` time, and are based on variables passed to the make program or defined in the Makefile.

Automake conditionals will work with any make program.

### 20.1 Usage of Conditionals

Before using a conditional, you must define it by using `AM_CONDITIONAL` in the configure.ac file (see Autoconf macros supplied with Automake).

**Macro: **AM_CONDITIONAL** *(*conditional*, *condition*)* ¶**

The conditional name, *conditional*, should be a simple string starting with a letter and containing only letters, digits, and underscores. It must be different from ‘TRUE’ and ‘FALSE’, which are reserved by Automake.

The shell *condition* (suitable for use in a shell `if` statement) is evaluated when `configure` is run. Note that you must arrange for *every* `AM_CONDITIONAL` to be invoked every time `configure` is run. If `AM_CONDITIONAL` is run conditionally (e.g., in a shell `if` statement), then the result will confuse `automake`.

For portability, it is best to use shell operators `&&` and `||` and parentheses, when constructing a compound *condition* using the `test` command, and not the `-a` and `-o` options and parentheses as options to `test`, all of which have been marked obsolescent by POSIX (https://pubs.opengroup.org/onlinepubs/9699919799/utilities/test.html#tag_20_128_161). The name `test` is also more portable than `[`. See Limitations of Builtins in *The Autoconf Manual*.

Conditionals typically depend upon options that the user provides to the `configure` script. Here is an example of how to write a conditional that is true if the user uses the --enable-debug option.

```
AC_ARG_ENABLE([debug],
[  --enable-debug    Turn on debugging],
[case "${enableval}" in
  yes) debug=true ;;
  no)  debug=false ;;
  *) AC_MSG_ERROR([bad value ${enableval} for --enable-debug]) ;;
esac],[debug=false])
AM_CONDITIONAL([DEBUG], [test x$debug = xtrue])
```

Here is an example of how to use that conditional in Makefile.am:

```
if DEBUG
DBG = debug
else
DBG =
endif
noinst_PROGRAMS = $(DBG)
```

This trivial example could also be handled using `EXTRA_PROGRAMS` (see Conditional compilation of programs).

You may only test a single variable in an `if` statement, possibly negated using ‘!’. The `else` statement may be omitted. Conditionals may be nested to any depth. You may specify an argument to `else` in which case it must be the negation of the condition used for the current `if`. Similarly you may specify the condition that is closed on the `endif` line:

```
if DEBUG
DBG = debug
else !DEBUG
DBG =
endif !DEBUG
```

Unbalanced conditions are errors. The `if`, `else`, and `endif` statements should not be indented, i.e., start on column one.

The `else` branch of the above two examples could be omitted, since assigning the empty string to an otherwise undefined variable makes no difference.

In order to allow access to the condition registered by `AM_CONDITIONAL` inside configure.ac, and to allow conditional `AC_CONFIG_FILES`, `AM_COND_IF` may be used:

**Macro: **AM_COND_IF** *(*conditional*, [*if-true*], [*if-false*])* ¶**

If *conditional* is fulfilled, execute *if-true*, otherwise execute *if-false*. If either branch contains `AC_CONFIG_FILES`, it will cause `automake` to output the rules for the respective files only for the given condition.

`AM_COND_IF` macros may be nested when M4 quotation is used properly (see M4 Quotation in *The Autoconf Manual*).

Here is an example of how to define a conditional config file:

```
AM_CONDITIONAL([SHELL_WRAPPER], [test "x$with_wrapper" = xtrue])
AM_COND_IF([SHELL_WRAPPER],
           [AC_CONFIG_FILES([wrapper:wrapper.in])])
```

### 20.2 Limits of Conditionals

Conditionals should enclose complete statements like variables or rules definitions. Automake cannot deal with conditionals used inside a variable definition, for instance, and is not even able to diagnose this situation. The following example would not work:

```
# This syntax is not understood by Automake
AM_CPPFLAGS = \
  -DFEATURE_A \
if WANT_DEBUG
  -DDEBUG \
endif
  -DFEATURE_B
```

However the intended definition of `AM_CPPFLAGS` can be achieved with

```
if WANT_DEBUG
  DEBUGFLAGS = -DDEBUG
endif
AM_CPPFLAGS = -DFEATURE_A $(DEBUGFLAGS) -DFEATURE_B
```

or

```
AM_CPPFLAGS = -DFEATURE_A
if WANT_DEBUG
AM_CPPFLAGS += -DDEBUG
endif
AM_CPPFLAGS += -DFEATURE_B
```

More details and examples of conditionals are described alongside various Automake features in this manual (see Conditional Subdirectories, see Conditional compilation of sources, see Conditional compilation of programs, see Building Libtool Libraries Conditionally, see Libtool Libraries with Conditional Sources).


## 21 Silencing `make`

### 21.1 Make is verbose by default

Normally, when executing the set of rules associated with a target, `make` prints each rule before it is executed. This behavior, despite having been in place since the beginning of `make`, and being mandated by the POSIX standard, starkly violates the “silence is golden” UNIX principle5:

> When a program has nothing interesting or surprising to say, it should say nothing. Well-behaved Unix programs do their jobs unobtrusively, with a minimum of fuss and bother. Silence is golden.

The traditional verbosity of `make` is understandable, as it is useful, often necessary, in order to understand reasons of failures. However, it can also hide warning and error messages from `make`-invoked tools, drowning them in uninteresting and seldom useful messages, and thus allowing them to easily go undetected.

This can be quite problematic, especially for developers, who usually know quite well what’s going on behind the scenes, and for whom the verbose output from `make` ends up being mostly noise that hampers the easy detection of potentially important warning messages.

So Automake provides some support for silencing `make`.

### 21.2 Standard and generic ways to silence Make

Here we describe some common idioms/tricks to obtain a quieter `make` output, with their relative advantages and drawbacks. In the next section (How Automake can help in silencing Make) we’ll see how Automake can help in this respect, providing more elaborate and flexible idioms.

- `make -s` This simply causes `make` not to print *any* rule before executing it. The -s flag is mandated by POSIX, universally supported, and its purpose and function are easy to understand. But it also has serious limitations. First of all, it embodies an “all or nothing” strategy, i.e., either everything is silenced, or nothing is; in practice, this lack of granularity makes it unsuitable as a general solution. When the -s flag is used, the `make` output might turn out to be too terse; in case of errors, the user won’t be able to easily see what rule or command have caused them, or even, in case of tools with poor error reporting, what the errors were.
- `make >/dev/null || make` Apparently, this perfectly obeys the “silence is golden” rule: warnings from stderr are passed through, output reporting is done only in case of error, and in that case it should provide a verbose-enough report to allow an easy determination of the error location and causes. However, calling `make` two times in a row might hide errors (especially intermittent ones), or subtly change the expected semantics of the `make` calls—these things can clearly make debugging and error assessment very difficult.
- `make --no-print-directory` This is GNU `make` specific. When called with the --no-print-directory option, GNU `make` will disable printing of the working directory by invoked sub-`make`s (the well-known “*Entering/Leaving directory …*” messages). This helps to decrease the verbosity of the output, but experience has shown that it can also often render debugging considerably harder in projects using deeply-nested `make` recursion. As an aside, the --no-print-directory option is automatically activated if the -s flag is used.

### 21.3 How Automake can help in silencing Make

The tricks and idioms for silencing `make` described in the previous section can be useful from time to time, but we’ve seen that they all have their serious drawbacks and limitations. That’s why automake provides support for a more advanced and flexible way of obtaining quieter output from `make` (for most rules at least).

To give the gist of what Automake can do in this respect, here is a simple comparison between a typical `make` output (where silent rules are disabled) and one with silent rules enabled:

```
% cat Makefile.am
bin_PROGRAMS = foo
foo_SOURCES = main.c func.c
% cat main.c
int main (void) { return func (); }  /* func used undeclared */
% cat func.c
int func (void) { int i; return i; } /* i used uninitialized */

The make output is by default very verbose.  This causes warnings
from the compiler to be somewhat hidden, and not immediate to spot.
% make CFLAGS=-Wall
gcc -DPACKAGE_NAME=\"foo\" -DPACKAGE_TARNAME=\"foo\" ...
-DPACKAGE_STRING=\"foo\ 1.0\" -DPACKAGE_BUGREPORT=\"\" ...
-DPACKAGE=\"foo\" -DVERSION=\"1.0\" -I. -Wall -MT main.o
-MD -MP -MF .deps/main.Tpo -c -o main.o main.c
main.c: In function ‘main’:
main.c:3:3: warning: implicit declaration of function ‘func’
mv -f .deps/main.Tpo .deps/main.Po
gcc -DPACKAGE_NAME=\"foo\" -DPACKAGE_TARNAME=\"foo\" ...
-DPACKAGE_STRING=\"foo\ 1.0\" -DPACKAGE_BUGREPORT=\"\" ...
-DPACKAGE=\"foo\" -DVERSION=\"1.0\" -I. -Wall -MT func.o
-MD -MP -MF .deps/func.Tpo -c -o func.o func.c
func.c: In function ‘func’:
func.c:4:3: warning: ‘i’ used uninitialized in this function
mv -f .deps/func.Tpo .deps/func.Po
gcc -Wall -o foo main.o func.o

Clean up, so that we can rebuild everything from scratch.
% make clean
test -z "foo" || rm -f foo
rm -f *.o

Silent rules enabled: the output is minimal but informative.
The warnings from the compiler stick out very clearly.
% make V=0 CFLAGS=-Wall
  CC     main.o
main.c: In function ‘main’:
main.c:3:3: warning: implicit declaration of function ‘func’
  CC     func.o
func.c: In function ‘func’:
func.c:4:3: warning: ‘i’ used uninitialized in this function
  CCLD   foo
```

Also, in projects using Libtool, the use of silent rules can automatically enable `libtool`’s --silent option:

```
% cat Makefile.am
lib_LTLIBRARIES = libx.la

% make # Both make and libtool are verbose by default.
...
libtool: compile: gcc -DPACKAGE_NAME=\"foo\" ... -DLT_OBJDIR=\".libs/\"
  -I. -g -O2 -MT libx.lo -MD -MP -MF .deps/libx.Tpo -c libx.c -fPIC
  -DPIC -o .libs/libx.o
mv -f .deps/libx.Tpo .deps/libx.Plo
/bin/sh ./libtool --tag=CC --mode=link gcc -g -O2 -o libx.la -rpath
  /usr/local/lib libx.lo
libtool: link: gcc -shared .libs/libx.o -Wl,-soname -Wl,libx.so.0
  -o .libs/libx.so.0.0.0
libtool: link: cd .libs && rm -f libx.so && ln -s libx.so.0.0.0 libx.so
...

% make V=0
  CC     libx.lo
  CCLD   libx.la
```

For Automake-generated Makefiles, the user may influence the verbosity at `configure` run time as well as at `make` run time:

- Passing --enable-silent-rules to `configure` will cause build rules to be less verbose; the option --disable-silent-rules will cause normal verbose output.
- At `make` run time, the default chosen at `configure` time may be overridden: `make V=1` will produce verbose output, `make V=0` less verbose output. Unfortunately, if `V` is assigned a value other than 0 or 1, errors will result. This is problematic when a third-party program or library is built in the same tree and also uses the make variable `V`, with different values. The best workaround is probably to set `AM_V_P=true` (or similar), either on the make command line or in the `V`-using project’s `Makefile.am`. (For more discussion, see https://bugs.gnu.org/20077.)

Silent rules are *disabled* by default; the user must enable them explicitly at either `configure` run time or at `make` run time. We think that this is a good policy, since it provides the casual user with enough information to prepare a good bug report in case anything breaks.

Notwithstanding those rationales, developers who want to enable silent rules by default in their own packages can do so by calling `AM_SILENT_RULES([yes])` in configure.ac.

Analogously, users who prefer to have silent rules enabled by default for everything on their system can edit their config.site file to make the variable `enable_silent_rules` default to ‘yes’. This still allows disabling silent rules at `configure` time and at `make` time.

To work best, the current implementation of this feature normally uses nested variable expansion ‘$(*var1*$(V))’, a Makefile feature that is not required by POSIX 2008 but is widely supported in practice. On the rare `make` implementations that do not support nested variable expansion, whether rules are silent is always determined at configure time, and cannot be overridden at make time. Future versions of POSIX are likely to require nested variable expansion, so this minor limitation should go away with time.

To extend the silent mode to your own rules, you have a few choices:

- You can use the predefined variable `AM_V_GEN` as a prefix to commands that should output a status line in silent mode, and `AM_V_at` as a prefix to commands that should not output anything in silent mode. When output is to be verbose, both of these variables will expand to the empty string.
- You can silence a recipe unconditionally with `@`, and then use the predefined variable `AM_V_P` to know whether make is being run in silent or verbose mode; adjust the verbose information your recipe displays accordingly. For example: generate-headers: @set -e; \ ... [commands defining shell variable '$headers'] ...; \ if $(AM_V_P); then set -x; else echo " GEN [headers]"; fi; \ rm -f $$headers && generate-header --flags $$headers `AM_V_P` is (must be) always set to a simple command, not needing shell quoting, typically either `:` or `true` or `false`.
- You can add your own variables, so strings of your own choice are shown. The following snippet shows how you would define your own equivalent of `AM_V_GEN`, say a string ‘PKG-GEN’: pkg_verbose = $(pkg_verbose_@AM_V@) pkg_verbose_ = $(pkg_verbose_@AM_DEFAULT_V@) pkg_verbose_0 = @echo PKG-GEN $@; foo: foo.in $(pkg_verbose)cp $(srcdir)/foo.in $@

Even when silent rules are enabled, the --no-print-directory option is still required with GNU `make` if the “*Entering/Leaving directory …*” messages are to be elided.

### 21.4 Unsilencing Automake

With the `AM_SILENT_RULES` macro described in the previous section, Automake does a good job reducing `make` output to a bare minimum. Sometimes you want to see more than that, especially when debugging. Let’s summarize ways to get more information out of Automake packages:

- Running `make V=1` will produce generally verbose output.
- Adding `AM_V_GEN= AM_V_at=` will unsilence more rules. Thus, in all: `make V=1 AM_V_GEN= AM_V_at=`.
- Even this will not unsilence everything. To see the real truth of what gets executed, resort to GNU Make’s debugging feature: `make --debug=p ... *otherargs* ...`. This reports every command being run, ignoring the `@` prefix on rules (which is what silences them). In the case of Automake, these commands are generally complex shell constructs, and you’ll want to track down the source files in Automake to actually understand them; but at least you’ll have the text to search for. You may wish to include other debugging options. See Options Summary in *The GNU Make Manual*.


## 22 When Automake Isn’t Enough

In some situations, where Automake is not up to one task, one has to resort to handwritten rules or even handwritten Makefiles.

### 22.1 Extending Automake Rules

With some minor exceptions (for example `_PROGRAMS` variables, `TESTS`, or `XFAIL_TESTS`) being rewritten to append ‘$(EXEEXT)’), the contents of a Makefile.am is copied to Makefile.in verbatim.

These copying semantics mean that many problems can be worked around by simply adding some `make` variables and rules to Makefile.am. Automake will ignore these additions.

Since a Makefile.in is built from data gathered from three different places (Makefile.am, configure.ac, and `automake` itself), it is possible to have conflicting definitions of rules or variables. When building Makefile.in the following priorities are respected by `automake` to ensure the user always has the last word:

- User defined variables in Makefile.am have priority over variables `AC_SUBST`ed from configure.ac, and `AC_SUBST`ed variables have priority over `automake`-defined variables.
- As far as rules are concerned, a user-defined rule overrides any `automake`-defined rule for the same target.

These overriding semantics make it possible to fine tune some default settings of Automake, or replace some of its rules. Overriding Automake rules is often inadvisable, particularly in the topmost directory of a package with subdirectories. The -Woverride option (see Creating a Makefile.in: Invoking `automake`) comes in handy to catch overridden definitions.

Note that Automake does not make any distinction between rules with commands and rules that only specify dependencies. So it is not possible to append new dependencies to an `automake`-defined target without redefining the entire rule.

However, various useful targets have a ‘-local’ version you can specify in your Makefile.am. Automake will supplement the standard target with these user-supplied targets.

The targets that support a local version are `all`, `info`, `dvi`, `ps`, `pdf`, `html`, `check`, `install-data`, `install-dvi`, `install-exec`, `install-html`, `install-info`, `install-pdf`, `install-ps`, `uninstall`, `installdirs`, `installcheck` and the various `clean` targets (`mostlyclean`, `clean`, `distclean`, and `maintainer-clean`).

Note that there are no `uninstall-exec-local` or `uninstall-data-local` targets; just use `uninstall-local`. It doesn’t make sense to uninstall just data or just executables.

For instance, here is one way to erase a subdirectory during ‘make clean’ (see What Gets Cleaned).

```
clean-local:
        -rm -rf testSubDir
```

You may be tempted to use `install-data-local` to install a file to some hard-coded location, but you should avoid this (see Installing to Hard-Coded Locations).

With the `-local` targets, there is no particular guarantee of execution order; typically, they are run early, but with parallel make, there is no way to be sure of that.

In contrast, some rules also have a way to run another rule, called a *hook*; hooks are always executed after the main rule’s work is done. The hook is named after the principal target, with ‘-hook’ appended. The targets allowing hooks are `install-data`, `install-exec`, `uninstall`, `dist`, and `distcheck`.

For instance, here is how to create a hard link to an installed program:

```
install-exec-hook:
        ln $(DESTDIR)$(bindir)/program$(EXEEXT) \
           $(DESTDIR)$(bindir)/proglink$(EXEEXT)
```

Although cheaper and more portable than symbolic links, hard links will not work everywhere (for instance, OS/2 does not have `ln`). Ideally you should fall back to ‘cp -p’ when `ln` does not work. An easy way, if symbolic links are acceptable to you, is to add `AC_PROG_LN_S` to configure.ac (see Particular Program Checks in *The Autoconf Manual*) and use ‘$(LN_S)’ in Makefile.am.

For instance, here is how you could install a versioned copy of a program using ‘$(LN_S)’:

```
install-exec-hook:
        cd $(DESTDIR)$(bindir) && \
          mv -f prog$(EXEEXT) prog-$(VERSION)$(EXEEXT) && \
          $(LN_S) prog-$(VERSION)$(EXEEXT) prog$(EXEEXT)
```

Note that we rename the program so that a new version will erase the symbolic link, not the real binary. Also we `cd` into the destination directory in order to create relative links.

When writing `install-exec-hook` or `install-data-hook`, please bear in mind that the exec/data distinction is based on the installation directory, not on the primary used (see The Two Parts of Install). So a `foo_SCRIPTS` will be installed by `install-data`, and a `barexec_SCRIPTS` will be installed by `install-exec`. You should define your hooks accordingly.

### 22.2 Third-Party Makefiles

In most projects all Makefiles are generated by Automake. In some cases, however, projects need to embed subdirectories with handwritten Makefiles. For instance, one subdirectory could be a third-party project with its own build system, not using Automake.

It is possible to list arbitrary directories in `SUBDIRS` or `DIST_SUBDIRS` provided each of these directories has a Makefile that recognizes all the following recursive targets.

When a user runs one of these targets, that target is run recursively in all subdirectories. This is why it is important that even third-party Makefiles support them.

**`all`**

Compile the entire package. This is the default target in Automake-generated Makefiles, but it does not need to be the default in third-party Makefiles.

**`distdir` ¶**

Copy files to distribute into ‘$(distdir)’, before a tarball is constructed. Of course this target is not required if the no-dist option (see Changing Automake’s Behavior) is used.

The variables ‘$(top_distdir)’ and ‘$(distdir)’ (see The dist Hook) will be passed from the outer package to the subpackage when the `distdir` target is invoked. These two variables have been adjusted for the directory that is being recursed into, so they are ready to use.

**`install`**

**`install-data`**

**`install-exec`**

**`uninstall`**

Install or uninstall files (see What Gets Installed).

**`install-dvi`**

**`install-html`**

**`install-info`**

**`install-ps`**

**`install-pdf`**

Install only some specific documentation format (see Texinfo).

**`installdirs`**

Create install directories, but do not install any files.

**`check`**

**`installcheck`**

Check the package (see Support for test suites).

**`mostlyclean`**

**`clean`**

**`distclean`**

**`maintainer-clean`**

Cleaning rules (see What Gets Cleaned).

**`dvi`**

**`pdf`**

**`ps`**

**`info`**

**`html`**

Build the documentation in various formats (see Texinfo).

**`tags`**

**`ctags`**

Build TAGS and CTAGS (see Interfacing to `etags`).

If you have ever used Gettext in a project, this is a good example of how third-party Makefiles can be used with Automake. The Makefiles that `gettextize` puts in the po/ and intl/ directories are handwritten Makefiles that implement all of these targets. That way they can be added to `SUBDIRS` in Automake packages.

Directories that are only listed in `DIST_SUBDIRS` but not in `SUBDIRS` need only the `distclean`, `maintainer-clean`, and `distdir` rules (see Conditional Subdirectories).

Usually, many of these rules are irrelevant to the third-party subproject, but they are required for the whole package to work. It’s OK to have a rule that does nothing, so if you are integrating a third-party project with no documentation or tag support, you could augment its Makefile as follows:

```
EMPTY_AUTOMAKE_TARGETS = dvi pdf ps info html tags ctags
.PHONY: $(EMPTY_AUTOMAKE_TARGETS)
$(EMPTY_AUTOMAKE_TARGETS):
```

To be clear, there is nothing special about the variable name `EMPTY_AUTOMAKE_TARGETS`; the name could be anything.

Another aspect of integrating third-party build systems is whether they support VPATH builds (see Parallel Build Trees (a.k.a. VPATH Builds)). Obviously if the subpackage does not support VPATH builds the whole package will not support VPATH builds. This in turns means that ‘make distcheck’ will not work, because it relies on VPATH builds. Some people can live without this (indeed, many Automake users have never heard of ‘make distcheck’). Other people may prefer to revamp the existing Makefiles to support VPATH. Doing so does not necessarily require Automake; only Autoconf is needed (see Build Directories in *The Autoconf Manual*). The necessary substitutions: ‘@srcdir@’, ‘@top_srcdir@’, and ‘@top_builddir@’ are defined by configure when it processes a Makefile (see Preset Output Variables in *The Autoconf Manual*); they are not computed by the Makefile like the aforementioned ‘$(distdir)’ and ‘$(top_distdir)’ variables.

It is sometimes inconvenient to modify a third-party Makefile to introduce the above required targets. For instance, one may want to keep the third-party sources untouched to ease upgrades to new versions.

Here are two other ideas. If GNU Make is assumed, one possibility is to add to that subdirectory a GNUmakefile that defines the required targets and includes the third-party Makefile. For this to work in VPATH builds, GNUmakefile must lie in the build directory; the easiest way to do this is to write a GNUmakefile.in instead, and have it processed with `AC_CONFIG_FILES` from the outer package. For example, if we assume Makefile defines all targets except the documentation targets, and that the real `check` target is named `test`, we could write GNUmakefile (or GNUmakefile.in) like this:

```
# First, include the real Makefile
include Makefile
# Then, define the other targets needed by Automake Makefiles.
.PHONY: dvi pdf ps info html check
dvi pdf ps info html:
check: test
```

A similar idea that does not use `include` is to write a proxy Makefile that dispatches rules to the real Makefile, either with ‘$(MAKE) -f Makefile.real $(AM_MAKEFLAGS) target’ (if it’s OK to rename the original Makefile) or with ‘cd subdir && $(MAKE) $(AM_MAKEFLAGS) target’ (if it’s OK to store the subdirectory project one directory deeper). The good news is that this proxy Makefile can be generated with Automake. All we need are -local targets (see Extending Automake Rules) that perform the dispatch. Of course the other Automake features are available, so you could decide to let Automake perform distribution or installation. Here is a possible Makefile.am:

```
all-local:
        cd subdir && $(MAKE) $(AM_MAKEFLAGS) all
check-local:
        cd subdir && $(MAKE) $(AM_MAKEFLAGS) test
clean-local:
        cd subdir && $(MAKE) $(AM_MAKEFLAGS) clean

# Assuming the package knows how to install itself
install-data-local:
        cd subdir && $(MAKE) $(AM_MAKEFLAGS) install-data
install-exec-local:
        cd subdir && $(MAKE) $(AM_MAKEFLAGS) install-exec
uninstall-local:
        cd subdir && $(MAKE) $(AM_MAKEFLAGS) uninstall

# Distribute files from here.
EXTRA_DIST = subdir/Makefile subdir/program.c ...
```

Pushing this idea to the extreme, it is also possible to ignore the subproject build system and build everything from this proxy Makefile.am. This might well be sensible if you need VPATH builds but the subproject does not support them.


## 23 Distributing Makefile.ins

Automake places no restrictions on the distribution of the resulting Makefile.ins. We encourage software authors to distribute their work under terms like those of the GPL, but doing so is not required to use Automake.

Some of the files that can be automatically installed via the --add-missing switch do fall under the GPL. However, these also have a special exception allowing you to distribute them with your package, regardless of the licensing you choose.


## 24 Automake API Versioning

New Automake releases usually include bug fixes and new features. Unfortunately they may also introduce new bugs and incompatibility. This makes four reasons why a package may require a particular Automake version.

Things get worse when maintaining a large tree of packages, each one requiring a different version of Automake. In the past, this meant that any developer (and sometimes users) had to install several versions of Automake in different places, and switch ‘$PATH’ appropriately for each package.

Starting with version 1.6, Automake installs versioned binaries. This means you can install several versions of Automake in the same ‘$prefix’, and can select an arbitrary Automake version by running `automake-1.6` or `automake-1.7` without juggling with ‘$PATH’. Furthermore, Makefiles generated by Automake 1.6 will use `automake-1.6` explicitly in their rebuild rules.

The number ‘1.6’ in `automake-1.6` is Automake’s API version, not Automake’s version. If a bug fix release is made, for instance Automake 1.6.1, the API version will remain 1.6. This means that a package that works with Automake 1.6 should also work with 1.6.1; after all, this is what people expect from bug fix releases.

If your package relies on a feature or a bug fix introduced in a release, you can pass this version as an option to Automake to ensure older releases will not be used. For instance, use this in your configure.ac:

```
  AM_INIT_AUTOMAKE([1.6.1])    dnl Require Automake 1.6.1 or better.
```

or, in a particular Makefile.am:

```
  AUTOMAKE_OPTIONS = 1.6.1   # Require Automake 1.6.1 or better.
```

Automake will print an error message if its version is older than the requested version.

### What is in the API

Automake’s programming interface is not easy to define. It includes at least all documented variables and targets that a Makefile.am author can use, any behavior associated with them (e.g., the places where ‘-hook’’s are run), the command line interface of `automake` and `aclocal`, …

### What is not in the API

Every undocumented variable, target, or command line option is not part of the API. You should avoid using them, as they could change from one version to the other (even in bug fix releases, if this helps to fix a bug).

If it turns out you need to use such an undocumented feature, contact automake@gnu.org and try to get it documented and exercised by the test-suite.


## 25 Upgrading a Package to a Newer Automake Version

Automake maintains three kinds of files in a package.

- aclocal.m4
- Makefile.ins
- auxiliary tools like install-sh or py-compile

aclocal.m4 is generated by `aclocal` and contains some Automake-supplied M4 macros. Auxiliary tools are installed by ‘automake --add-missing’ when needed. Makefile.ins are built from Makefile.am by `automake`, and rely on the definitions of the M4 macros put in aclocal.m4 as well as the behavior of the auxiliary tools installed.

Because all of these files are closely related, it is important to regenerate all of them when upgrading to a newer Automake release. The usual way to do that is

```
aclocal # with any option needed (such as -I m4)
autoconf
automake --add-missing --force-missing
```

or more conveniently:

```
autoreconf -vfi
```

The use of --force-missing ensures that auxiliary tools will be overridden by new versions (see Creating a Makefile.in: Invoking `automake`).

It is important to regenerate all of these files each time Automake is upgraded, even between bug fix releases. For instance, it is not unusual for a bug fix to involve changes to both the rules generated in Makefile.in and the supporting M4 macros copied to aclocal.m4.

Presently `automake` is able to diagnose situations where aclocal.m4 has been generated with another version of `aclocal`. However it never checks whether auxiliary scripts are up-to-date. In other words, `automake` will tell you when `aclocal` needs to be rerun, but it will never diagnose a missing --force-missing.

Before upgrading to a new major release, it is a good idea to read the file NEWS. This file lists all changes between releases: new features, obsolete constructs, known incompatibility, and workarounds.
