---
title: "Autoconf (part 23/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 23/26
---

## 20 Frequent Autoconf Questions, with answers

Several questions about Autoconf come up occasionally. Here some of them are addressed.

### 20.1 Distributing `configure` Scripts

```
What are the restrictions on distributing configure
scripts that Autoconf generates?  How does that affect my
programs that use them?
```

There are no restrictions on how the configuration scripts that Autoconf produces may be distributed or used. In Autoconf version 1, they were covered by the GNU General Public License. We still encourage software authors to distribute their work under terms like those of the GPL, but doing so is not required to use Autoconf.

Of the other files that might be used with `configure`, config.h.in is under whatever copyright you use for your configure.ac. config.sub and config.guess have an exception to the GPL when they are used with an Autoconf-generated `configure` script, which permits you to distribute them under the same terms as the rest of your package. install-sh is from the X Consortium and is not copyrighted.

### 20.2 Why Require GNU M4?

```
Why does Autoconf require GNU M4?
```

Many M4 implementations have hard-coded limitations on the size and number of macros that Autoconf exceeds. They also lack several builtin macros that it would be difficult to get along without in a sophisticated application like Autoconf, including:

```
m4_builtin
m4_indir
m4_bpatsubst
__file__
__line__
```

Autoconf requires version 1.4.8 or later of GNU M4. It works better with version 1.4.16 or later.

Since only software maintainers need to use Autoconf, and since GNU M4 is simple to configure and install, it seems reasonable to require GNU M4 to be installed also. Many maintainers of GNU and other free software already have most of the GNU utilities installed, since they prefer them.

### 20.3 How Can I Bootstrap?

```
If Autoconf requires GNU M4 and GNU M4 has an Autoconf
configure script, how do I bootstrap?  It seems like a chicken
and egg problem!
```

This is a misunderstanding. Although GNU M4 does come with a `configure` script produced by Autoconf, Autoconf is not required in order to run the script and install GNU M4. Autoconf is only required if you want to change the M4 `configure` script, which few people have to do (mainly its maintainer).

### 20.4 Why Not Imake?

```
Why not use Imake instead of configure scripts?
```

Several people have written addressing this question, so adaptations of their explanations are included here.

The following answer is based on one written by Richard Pixley:

> Autoconf generated scripts frequently work on machines that it has never been set up to handle before. That is, it does a good job of inferring a configuration for a new system. Imake cannot do this.
> 
> Imake uses a common database of host specific data. For X11, this makes sense because the distribution is made as a collection of tools, by one central authority who has control over the database.
> 
> GNU tools are not released this way. Each GNU tool has a maintainer; these maintainers are scattered across the world. Using a common database would be a maintenance nightmare. Autoconf may appear to be this kind of database, but in fact it is not. Instead of listing host dependencies, it lists program requirements.
> 
> If you view the GNU suite as a collection of native tools, then the problems are similar. But the GNU development tools can be configured as cross tools in almost any host+target permutation. All of these configurations can be installed concurrently. They can even be configured to share host independent files across hosts. Imake doesn’t address these issues.
> 
> Imake templates are a form of standardization. The GNU coding standards address the same issues without necessarily imposing the same restrictions.

Here is some further explanation, written by Per Bothner:

> One of the advantages of Imake is that it is easy to generate large makefiles using the ‘#include’ and macro mechanisms of `cpp`. However, `cpp` is not programmable: it has limited conditional facilities, and no looping. And `cpp` cannot inspect its environment.
> 
> All of these problems are solved by using `sh` instead of `cpp`. The shell is fully programmable, has macro substitution, can execute (or source) other shell scripts, and can inspect its environment.

Paul Eggert elaborates more:

> With Autoconf, installers need not assume that Imake itself is already installed and working well. This may not seem like much of an advantage to people who are accustomed to Imake. But on many hosts Imake is not installed or the default installation is not working well, and requiring Imake to install a package hinders the acceptance of that package on those hosts. For example, the Imake template and configuration files might not be installed properly on a host, or the Imake build procedure might wrongly assume that all source files are in one big directory tree, or the Imake configuration might assume one compiler whereas the package or the installer needs to use another, or there might be a version mismatch between the Imake expected by the package and the Imake supported by the host. These problems are much rarer with Autoconf, where each package comes with its own independent configuration processor.
> 
> Also, Imake often suffers from unexpected interactions between `make` and the installer’s C preprocessor. The fundamental problem here is that the C preprocessor was designed to preprocess C programs, not makefiles. This is much less of a problem with Autoconf, which uses the general-purpose preprocessor M4, and where the package’s author (rather than the installer) does the preprocessing in a standard way.

Finally, Mark Eichin notes:

> Imake isn’t all that extensible, either. In order to add new features to Imake, you need to provide your own project template, and duplicate most of the features of the existing one. This means that for a sophisticated project, using the vendor-provided Imake templates fails to provide any leverage—since they don’t cover anything that your own project needs (unless it is an X11 program).
> 
> On the other side, though:
> 
> The one advantage that Imake has over `configure`: Imakefile files tend to be much shorter (likewise, less redundant) than Makefile.in files. There is a fix to this, however—at least for the Kerberos V5 tree, we’ve modified things to call in common post.in and pre.in makefile fragments for the entire tree. This means that a lot of common things don’t have to be duplicated, even though they normally are in `configure` setups.

### 20.5 How Do I `#define` Installation Directories?

```
My program needs library files, installed in datadir and
similar.  If I use
```

```
AC_DEFINE_UNQUOTED([DATADIR], [$datadir],
  [Define to the read-only architecture-independent
   data directory.])
```

```
I get
```

```
#define DATADIR "${prefix}/share"
```

As already explained, this behavior is on purpose, mandated by the GNU Coding Standards, see Installation Directory Variables. There are several means to achieve a similar goal:

- Do not use `AC_DEFINE` but use your makefile to pass the actual value of `datadir` via compilation flags. See Installation Directory Variables, for the details.
- This solution can be simplified when compiling a program: you may either extend the `CPPFLAGS`: CPPFLAGS = -DDATADIR='"$(datadir)"' @CPPFLAGS@ If you are using Automake, you should use `AM_CPPFLAGS` instead: AM_CPPFLAGS = -DDATADIR='"$(datadir)"' Alternatively, create a dedicated header file: DISTCLEANFILES = myprog-paths.h myprog-paths.h: Makefile printf '%s\n' '#define DATADIR "$(datadir)"' >$@ The Gnulib module ‘configmake’ provides such a header with all the standard directory variables defined, see configmake in *GNU Gnulib*.
- Use `AC_DEFINE` but have `configure` compute the literal value of `datadir` and others. Many people have wrapped macros to automate this task; for an example, see the macro `AC_DEFINE_DIR` from the Autoconf Macro Archive. This solution does not conform to the GNU Coding Standards.
- Note that all the previous solutions hard wire the absolute name of these directories in the executables, which is not a good property. You may try to compute the names relative to `prefix`, and try to find `prefix` at runtime, this way your package is relocatable.

### 20.6 What is autom4te.cache?

```
What is this directory autom4te.cache?  Can I safely remove it?
```

In the GNU Build System, configure.ac plays a central role and is read by many tools: `autoconf` to create configure, `autoheader` to create config.h.in, `automake` to create Makefile.in, `autoscan` to check the completeness of configure.ac, `autoreconf` to check the GNU Build System components that are used. To “read configure.ac” actually means to compile it with M4, which can be a long process for complex configure.ac.

This is why all these tools, instead of running directly M4, invoke `autom4te` (see Invoking `autom4te`) which, while answering to a specific demand, stores additional information in autom4te.cache for future runs. For instance, if you run `autoconf`, behind the scenes, `autom4te` also stores information for the other tools, so that when you invoke `autoheader` or `automake` etc., reprocessing configure.ac is not needed. The speed up is frequently 30%, and is increasing with the size of configure.ac.

But it is and remains being simply a cache: you can safely remove it.

```
Can I permanently get rid of it?
```

The creation of this cache can be disabled from ~/.autom4te.cfg, see Customizing `autom4te`, for more details. You should be aware that disabling the cache slows down the Autoconf test suite by 40%. The more GNU Build System components are used, the more the cache is useful; for instance running ‘autoreconf -f’ on the Core Utilities is twice slower without the cache *although --force implies that the cache is not fully exploited*, and eight times slower than without --force.

### 20.7 Header Present But Cannot Be Compiled

The most important guideline to bear in mind when checking for features is to mimic as much as possible the intended use. Unfortunately, old versions of `AC_CHECK_HEADER` and `AC_CHECK_HEADERS` failed to follow this idea, and called the preprocessor, instead of the compiler, to check for headers. As a result, incompatibilities between headers went unnoticed during configuration, and maintainers finally had to deal with this issue elsewhere.

The transition began with Autoconf 2.56. As of Autoconf 2.64 both checks are performed, and `configure` complains loudly if the compiler and the preprocessor do not agree. However, only the compiler result is considered. As of Autoconf 2.70, only the compiler check is performed.

Consider the following example:

```
$ cat number.h
typedef int number;
$ cat pi.h
const number pi = 3;
$ cat configure.ac
AC_INIT([Example], [1.0], [bug-example@example.org])
AC_CHECK_HEADERS([pi.h])
$ autoconf -Wall
$ ./configure CPPFLAGS='-I.'
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C23 features... -std=gnu23
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for pi.h... no
```

The proper way to handle this case is using the fourth argument (see Generic Header Checks):

```
$ cat configure.ac
AC_INIT([Example], [1.0], [bug-example@example.org])
AC_CHECK_HEADERS([number.h pi.h], [], [],
[[#ifdef HAVE_NUMBER_H
# include <number.h>
#endif
]])
$ autoconf -Wall
$ ./configure CPPFLAGS='-I.'
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C23 features... -std=gnu23
checking for number.h... yes
checking for pi.h... yes
```

See Particular Header Checks, for a list of headers with their prerequisites.

### 20.8 Expanded Before Required

Older versions of Autoconf silently built files with incorrect ordering between dependent macros if an outer macro first expanded, then later indirectly required, an inner macro. Starting with Autoconf 2.64, this situation no longer generates out-of-order code, but results in duplicate output and a syntax warning:

```
$ cat configure.ac
⇒AC_DEFUN([TESTA], [[echo in A
⇒if test -n "$SEEN_A" ; then echo duplicate ; fi
⇒SEEN_A=:]])
⇒AC_DEFUN([TESTB], [AC_REQUIRE([TESTA])[echo in B
⇒if test -z "$SEEN_A" ; then echo bug ; fi]])
⇒AC_DEFUN([TESTC], [AC_REQUIRE([TESTB])[echo in C]])
⇒AC_DEFUN([OUTER], [[echo in OUTER]
⇒TESTA
⇒TESTC])
⇒AC_INIT
⇒OUTER
⇒AC_OUTPUT
$ autoconf
⇒configure.ac:11: warning: AC_REQUIRE:
⇒ 'TESTA' was expanded before it was required
⇒configure.ac:4: TESTB is expanded from...
⇒configure.ac:6: TESTC is expanded from...
⇒configure.ac:7: OUTER is expanded from...
⇒configure.ac:11: the top level
```

To avoid this warning, decide what purpose the macro in question serves. If it only needs to be expanded once (for example, if it provides initialization text used by later macros), then the simplest fix is to change the macro to be declared with `AC_DEFUN_ONCE` (see One-Shot Macros), although this only works in Autoconf 2.64 and newer. A more portable fix is to change all instances of direct calls to instead go through `AC_REQUIRE` (see Prerequisite Macros). If, instead, the macro is parameterized by arguments or by the current definition of other macros in the m4 environment, then the macro should always be directly expanded instead of required.

For another case study, consider this example trimmed down from an actual package. Originally, the package contained shell code and multiple macro invocations at the top level of configure.ac:

```
AC_DEFUN([FOO], [AC_COMPILE_IFELSE([...])])
foobar=
AC_PROG_CC
FOO
```

but that was getting complex, so the author wanted to offload some of the text into a new macro in another file included via aclocal.m4. The naïve approach merely wraps the text in a new macro:

```
AC_DEFUN([FOO], [AC_COMPILE_IFELSE([...])])
AC_DEFUN([BAR], [
foobar=
AC_PROG_CC
FOO
])
BAR
```

With older versions of Autoconf, the setting of ‘foobar=’ occurs before the single compiler check, as the author intended. But with Autoconf 2.64, this issues the “expanded before it was required” warning for `AC_PROG_CC`, and outputs two copies of the compiler check, one before ‘foobar=’, and one after. To understand why this is happening, remember that the use of `AC_COMPILE_IFELSE` includes a call to `AC_REQUIRE([AC_PROG_CC])` under the hood. According to the documented semantics of `AC_REQUIRE`, this means that `AC_PROG_CC` *must* occur before the body of the outermost `AC_DEFUN`, which in this case is `BAR`, thus preceding the use of ‘foobar=’. The older versions of Autoconf were broken with regards to the rules of `AC_REQUIRE`, which explains why the code changed from one over to two copies of `AC_PROG_CC` when upgrading autoconf. In other words, the author was unknowingly relying on a bug exploit to get the desired results, and that exploit broke once the bug was fixed.

So, what recourse does the author have, to restore their intended semantics of setting ‘foobar=’ prior to a single compiler check, regardless of whether Autoconf 2.63 or 2.64 is used? One idea is to remember that only `AC_DEFUN` is impacted by `AC_REQUIRE`; there is always the possibility of using the lower-level `m4_define`:

```
AC_DEFUN([FOO], [AC_COMPILE_IFELSE([...])])
m4_define([BAR], [
foobar=
AC_PROG_CC
FOO
])
BAR
```

This works great if everything is in the same file. However, it does not help in the case where the author wants to have `aclocal` find the definition of `BAR` from its own file, since `aclocal` requires the use of `AC_DEFUN`. In this case, a better fix is to recognize that if `BAR` also uses `AC_REQUIRE`, then there will no longer be direct expansion prior to a subsequent require. Then, by creating yet another helper macro, the author can once again guarantee a single invocation of `AC_PROG_CC`, which will still occur after `foobar=`. The author can also use `AC_BEFORE` to make sure no other macro appearing before `BAR` has triggered an unwanted expansion of `AC_PROG_CC`.

```
AC_DEFUN([FOO], [AC_COMPILE_IFELSE([...])])
AC_DEFUN([BEFORE_CC], [
foobar=
])
AC_DEFUN([BAR], [
AC_BEFORE([$0], [AC_PROG_CC])dnl
AC_REQUIRE([BEFORE_CC])dnl
AC_REQUIRE([AC_PROG_CC])dnl
FOO
])
BAR
```

### 20.9 Debugging `configure` scripts

While in general, `configure` scripts generated by Autoconf strive to be fairly portable to various systems, compilers, shells, and other tools, it may still be necessary to debug a failing test, broken script or makefile, or fix or override an incomplete, faulty, or erroneous test, especially during macro development. Failures can occur at all levels, in M4 syntax or semantics, shell script issues, or due to bugs in the test or the tools invoked by `configure`. Together with the rather arcane error message that `m4` and `make` may produce when their input contains syntax errors, this can make debugging rather painful.

Nevertheless, here is a list of hints and strategies that may help:

- When `autoconf` fails, common causes for error include: Typically, it helps to go back to the last working version of the input and compare the differences for each of these errors. Another possibility is to sprinkle pairs of `m4_traceon` and `m4_traceoff` judiciously in the code, either without a parameter or listing some macro names and watch `m4` expand its input verbosely (see Debugging via autom4te).
  - mismatched or unbalanced parentheses or braces (see Dealing with unbalanced parentheses),
  - under- or over-quoted macro arguments (see The Autoconf Language, see Quoting and Parameters, see Quotation and Nested Macros),
  - spaces between macro name and opening parenthesis (see The Autoconf Language).
- Sometimes `autoconf` succeeds but the generated `configure` script has invalid shell syntax. You can detect this case by running ‘bash -n configure’ or ‘sh -n configure’. If this command fails, the same tips apply, as if `autoconf` had failed.
- Debugging `configure` script execution may be done by sprinkling pairs of `set -x` and `set +x` into the shell script before and after the region that contains a bug. Running the whole script with ‘*shell* -vx ./configure 2>&1 | tee *log-file*’ with a decent *shell* may work, but produces lots of output. Here, it can help to search for markers like ‘checking for’ a particular test in the *log-file*.
- Alternatively, you might use a shell with debugging capabilities like bashdb.
- When `configure` tests produce invalid results for your system, it may be necessary to override them:
  - For programs, tools or libraries variables, preprocessor, compiler, or linker flags, it is often sufficient to override them at `make` run time with some care (see `make macro=value` and Submakes). Since this normally won’t cause `configure` to be run again with these changed settings, it may fail if the changed variable would have caused different test results from `configure`, so this may work only for simple differences.
  - Most tests which produce their result in a substituted variable allow to override the test by setting the variable on the `configure` command line (see Compilers and Options, see Defining Variables).
  - Many tests store their result in a cache variable (see Caching Results). This lets you override them either on the `configure` command line as above, or through a primed cache or site file (see Cache Files, see Setting Site Defaults). The name of a cache variable is documented with a test macro or may be inferred from Cache Variable Names; the precise semantics of undocumented variables are often internal details, subject to change.
- Alternatively, `configure` may produce invalid results because of uncaught programming errors, in your package or in an upstream library package. For example, when `AC_CHECK_LIB` fails to find a library with a specified function, always check config.log. This will reveal the exact error that produced the failing result: the library linked by `AC_CHECK_LIB` probably has a fatal bug.

Conversely, as macro author, you can make it easier for users of your macro:

- by minimizing dependencies between tests and between test results as far as possible,
- by using `make` variables to factorize and allow override of settings at `make` run time,
- by honoring the GNU Coding Standards and not overriding flags reserved for the user except temporarily during `configure` tests,
- by not requiring users of your macro to use the cache variables. Instead, expose the result of the test via *run-if-true* and *run-if-false* parameters. If the result is not a boolean, then provide it through documented shell variables.


## 21 History of Autoconf

*This chapter was written by the original author, David MacKenzie.*

You may be wondering, Why was Autoconf originally written? How did it get into its present form? (Why does it look like gorilla spit?) If you’re not wondering, then this chapter contains no information useful to you, and you might as well skip it. If you *are* wondering, then let there be light...

### 21.1 Genesis

In June 1991 I was maintaining many of the GNU utilities for the Free Software Foundation. As they were ported to more platforms and more programs were added, the number of -D options that users had to select in the makefile (around 20) became burdensome. Especially for me—I had to test each new release on a bunch of different systems. So I wrote a little shell script to guess some of the correct settings for the fileutils package, and released it as part of fileutils 2.0. That `configure` script worked well enough that the next month I adapted it (by hand) to create similar `configure` scripts for several other GNU utilities packages. Brian Berliner also adapted one of my scripts for his CVS revision control system.

Later that summer, I learned that Richard Stallman and Richard Pixley were developing similar scripts to use in the GNU compiler tools; so I adapted my `configure` scripts to support their evolving interface: using the file name Makefile.in as the templates; adding ‘+srcdir’, the first option (of many); and creating config.status files.

### 21.2 Exodus

As I got feedback from users, I incorporated many improvements, using Emacs to search and replace, cut and paste, similar changes in each of the scripts. As I adapted more GNU utilities packages to use `configure` scripts, updating them all by hand became impractical. Rich Murphey, the maintainer of the GNU graphics utilities, sent me mail saying that the `configure` scripts were great, and asking if I had a tool for generating them that I could send him. No, I thought, but I should! So I started to work out how to generate them. And the journey from the slavery of hand-written `configure` scripts to the abundance and ease of Autoconf began.

Cygnus `configure`, which was being developed at around that time, is table driven; it is meant to deal mainly with a discrete number of system types with a small number of mainly unguessable features (such as details of the object file format). The automatic configuration system that Brian Fox had developed for Bash takes a similar approach. For general use, it seems to me a hopeless cause to try to maintain an up-to-date database of which features each variant of each operating system has. It’s easier and more reliable to check for most features on the fly—especially on hybrid systems that people have hacked on locally or that have patches from vendors installed.

I considered using an architecture similar to that of Cygnus `configure`, where there is a single `configure` script that reads pieces of configure.in when run. But I didn’t want to have to distribute all of the feature tests with every package, so I settled on having a different `configure` made from each configure.in by a preprocessor. That approach also offered more control and flexibility.

I looked briefly into using the Metaconfig package, by Larry Wall, Harlan Stenn, and Raphael Manfredi, but I decided not to for several reasons. The `Configure` scripts it produces are interactive, which I find quite inconvenient; I didn’t like the ways it checked for some features (such as library functions); I didn’t know that it was still being maintained, and the `Configure` scripts I had seen didn’t work on many modern systems (such as System V R4 and NeXT); it wasn’t flexible in what it could do in response to a feature’s presence or absence; I found it confusing to learn; and it was too big and complex for my needs (I didn’t realize then how much Autoconf would eventually have to grow).

I considered using Perl to generate my style of `configure` scripts, but decided that M4 was better suited to the job of simple textual substitutions: it gets in the way less, because output is implicit. Plus, everyone already has it. (Initially I didn’t rely on the GNU extensions to M4.) Also, some of my friends at the University of Maryland had recently been putting M4 front ends on several programs, including `tvtwm`, and I was interested in trying out a new language.

### 21.3 Leviticus

Since my `configure` scripts determine the system’s capabilities automatically, with no interactive user intervention, I decided to call the program that generates them Autoconfig. But with a version number tacked on, that name would be too long for old Unix file systems, so I shortened it to Autoconf.

In the fall of 1991 I called together a group of fellow questers after the Holy Grail of portability (er, that is, alpha testers) to give me feedback as I encapsulated pieces of my handwritten scripts in M4 macros and continued to add features and improve the techniques used in the checks. Prominent among the testers were François Pinard, who came up with the idea of making an Autoconf shell script to run M4 and check for unresolved macro calls; Richard Pixley, who suggested running the compiler instead of searching the file system to find include files and symbols, for more accurate results; Karl Berry, who got Autoconf to configure TeX and added the macro index to the documentation; and Ian Lance Taylor, who added support for creating a C header file as an alternative to putting -D options in a makefile, so he could use Autoconf for his UUCP package. The alpha testers cheerfully adjusted their files again and again as the names and calling conventions of the Autoconf macros changed from release to release. They all contributed many specific checks, great ideas, and bug fixes.

### 21.4 Numbers

In July 1992, after months of alpha testing, I released Autoconf 1.0, and converted many GNU packages to use it. I was surprised by how positive the reaction to it was. More people started using it than I could keep track of, including people working on software that wasn’t part of the GNU Project (such as TCL, FSP, and Kerberos V5). Autoconf continued to improve rapidly, as many people using the `configure` scripts reported problems they encountered.

Autoconf turned out to be a good torture test for M4 implementations. Unix M4 started to dump core because of the length of the macros that Autoconf defined, and several bugs showed up in GNU M4 as well. Eventually, we realized that we needed to use some features that only GNU M4 has. 4.3BSD M4, in particular, has an impoverished set of builtin macros; the System V version is better, but still doesn’t provide everything we need.

More development occurred as people put Autoconf under more stresses (and to uses I hadn’t anticipated). Karl Berry added checks for X11. david zuhn contributed C++ support. François Pinard made it diagnose invalid arguments. Jim Blandy bravely coerced it into configuring GNU Emacs, laying the groundwork for several later improvements. Roland McGrath got it to configure the GNU C Library, wrote the `autoheader` script to automate the creation of C header file templates, and added a --verbose option to `configure`. Noah Friedman added the --autoconf-dir option and `AC_MACRODIR` environment variable. (He also coined the term *autoconfiscate* to mean “adapt a software package to use Autoconf”.) Roland and Noah improved the quoting protection in `AC_DEFINE` and fixed many bugs, especially when I got sick of dealing with portability problems from February through June, 1993.

### 21.5 Deuteronomy

A long wish list for major features had accumulated, and the effect of several years of patching by various people had left some residual cruft. In April 1994, while working for Cygnus Support, I began a major revision of Autoconf. I added most of the features of the Cygnus `configure` that Autoconf had lacked, largely by adapting the relevant parts of Cygnus `configure` with the help of david zuhn and Ken Raeburn. These features include support for using config.sub, config.guess, --host, and --target; making links to files; and running `configure` scripts in subdirectories. Adding these features enabled Ken to convert GNU `as`, and Rob Savoye to convert DejaGNU, to using Autoconf.

I added more features in response to other peoples’ requests. Many people had asked for `configure` scripts to share the results of the checks between runs, because (particularly when configuring a large source tree, like Cygnus does) they were frustratingly slow. Mike Haertel suggested adding site-specific initialization scripts. People distributing software that had to unpack on MS-DOS asked for a way to override the .in extension on the file names, which produced file names like config.h.in containing two dots. Jim Avera did an extensive examination of the problems with quoting in `AC_DEFINE` and `AC_SUBST`; his insights led to significant improvements. Richard Stallman asked that compiler output be sent to config.log instead of /dev/null, to help people debug the Emacs `configure` script.

I made some other changes because of my dissatisfaction with the quality of the program. I made the messages showing results of the checks less ambiguous, always printing a result. I regularized the names of the macros and cleaned up coding style inconsistencies. I added some auxiliary utilities that I had developed to help convert source code packages to use Autoconf. With the help of François Pinard, I made the macros not interrupt each others’ messages. (That feature revealed some performance bottlenecks in GNU M4, which he hastily corrected!) I reorganized the documentation around problems people want to solve. And I began a test suite, because experience had shown that Autoconf has a pronounced tendency to regress when we change it.

Again, several alpha testers gave invaluable feedback, especially François Pinard, Jim Meyering, Karl Berry, Rob Savoye, Ken Raeburn, and Mark Eichin.

Finally, version 2.0 was ready. And there was much rejoicing. (And I have free time again. I think. Yeah, right.)
