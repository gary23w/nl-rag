---
title: "GNU make (part 11/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 11/17
---

## 10 Using Implicit Rules

Certain standard ways of remaking target files are used very often. For example, one customary way to make an object file is from a C source file using the C compiler, `cc`.

*Implicit rules* tell `make` how to use customary techniques so that you do not have to specify them in detail when you want to use them. For example, there is an implicit rule for C compilation. File names determine which implicit rules are run. For example, C compilation typically takes a .c file and makes a .o file. So `make` applies the implicit rule for C compilation when it sees this combination of file name endings.

A chain of implicit rules can apply in sequence; for example, `make` will remake a .o file from a .y file by way of a .c file.

The built-in implicit rules use several variables in their recipes so that, by changing the values of the variables, you can change the way the implicit rule works. For example, the variable `CFLAGS` controls the flags given to the C compiler by the implicit rule for C compilation.

You can define your own implicit rules by writing *pattern rules*.

*Suffix rules* are a more limited way to define implicit rules. Pattern rules are more general and clearer, but suffix rules are retained for compatibility.

Next: Catalogue of Built-In Rules, Previous: Using Implicit Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.1 Using Implicit Rules

To allow `make` to find a customary method for updating a target file, all you have to do is refrain from specifying recipes yourself. Either write a rule with no recipe, or don’t write a rule at all. Then `make` will figure out which implicit rule to use based on which kind of source file exists or can be made.

For example, suppose the makefile looks like this:

```
foo : foo.o bar.o
        cc -o foo foo.o bar.o $(CFLAGS) $(LDFLAGS)
```

Because you mention foo.o but do not give a rule for it, `make` will automatically look for an implicit rule that tells how to update it. This happens whether or not the file foo.o currently exists.

If an implicit rule is found, it can supply both a recipe and one or more prerequisites (the source files). You would want to write a rule for foo.o with no recipe if you need to specify additional prerequisites, such as header files, that the implicit rule cannot supply.

Each implicit rule has a target pattern and prerequisite patterns. There may be many implicit rules with the same target pattern. For example, numerous rules make ‘.o’ files: one, from a ‘.c’ file with the C compiler; another, from a ‘.p’ file with the Pascal compiler; and so on. The rule that actually applies is the one whose prerequisites exist or can be made. So, if you have a file foo.c, `make` will run the C compiler; otherwise, if you have a file foo.p, `make` will run the Pascal compiler; and so on.

Of course, when you write the makefile, you know which implicit rule you want `make` to use, and you know it will choose that one because you know which possible prerequisite files are supposed to exist. See Catalogue of Built-In Rules, for a catalogue of all the predefined implicit rules.

Above, we said an implicit rule applies if the required prerequisites “exist or can be made”. A file “can be made” if it is mentioned explicitly in the makefile as a target or a prerequisite, or if an implicit rule can be recursively found for how to make it. When an implicit prerequisite is the result of another implicit rule, we say that *chaining* is occurring. See Chains of Implicit Rules.

In general, `make` searches for an implicit rule for each target, and for each double-colon rule, that has no recipe. A file that is mentioned only as a prerequisite is considered a target whose rule specifies nothing, so implicit rule search happens for it. See Implicit Rule Search Algorithm, for the details of how the search is done.

Note that explicit prerequisites do not influence implicit rule search. For example, consider this explicit rule:

```
foo.o: foo.p
```

The prerequisite on foo.p does not necessarily mean that `make` will remake foo.o according to the implicit rule to make an object file, a .o file, from a Pascal source file, a .p file. For example, if foo.c also exists, the implicit rule to make an object file from a C source file is used instead, because it appears before the Pascal rule in the list of predefined implicit rules (see Catalogue of Built-In Rules).

If you do not want an implicit rule to be used for a target that has no recipe, you can give that target an empty recipe by writing a semicolon (see Defining Empty Recipes).

Next: Variables Used by Implicit Rules, Previous: Using Implicit Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.2 Catalogue of Built-In Rules

Here is a catalogue of predefined implicit rules which are always available unless the makefile explicitly overrides or cancels them. See Canceling Implicit Rules, for information on canceling or overriding an implicit rule. The ‘-r’ or ‘--no-builtin-rules’ option cancels all predefined rules.

This manual only documents the default rules available on POSIX-based operating systems. Other operating systems, such as VMS, Windows, OS/2, etc. may have different sets of default rules. To see the full list of default rules and variables available in your version of GNU `make`, run ‘make -p’ in a directory with no makefile.

Not all of these rules will always be defined, even when the ‘-r’ option is not given. Many of the predefined implicit rules are implemented in `make` as suffix rules, so which ones will be defined depends on the *suffix list* (the list of prerequisites of the special target `.SUFFIXES`). The default suffix list is: `.out`, `.a`, `.ln`, `.o`, `.c`, `.cc`, `.C`, `.cpp`, `.p`, `.f`, `.F`, `.m`, `.r`, `.y`, `.l`, `.ym`, `.lm`, `.s`, `.S`, `.mod`, `.sym`, `.def`, `.h`, `.info`, `.dvi`, `.tex`, `.texinfo`, `.texi`, `.txinfo`, `.w`, `.ch` `.web`, `.sh`, `.elc`, `.el`. All of the implicit rules described below whose prerequisites have one of these suffixes are actually suffix rules. If you modify the suffix list, the only predefined suffix rules in effect will be those named by one or two of the suffixes that are on the list you specify; rules whose suffixes fail to be on the list are disabled. See Old-Fashioned Suffix Rules, for full details on suffix rules.

**Compiling C programs ¶**

*n*.o is made automatically from *n*.c with a recipe of the form ‘$(CC) $(CPPFLAGS) $(CFLAGS) -c’.

**Compiling C++ programs ¶**

*n*.o is made automatically from *n*.cc, *n*.cpp, or *n*.C with a recipe of the form ‘$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c’. We encourage you to use the suffix ‘.cc’ or ‘.cpp’ for C++ source files instead of ‘.C’ to better support case-insensitive file systems.

**Compiling Pascal programs ¶**

*n*.o is made automatically from *n*.p with the recipe ‘$(PC) $(PFLAGS) -c’.

**Compiling Fortran and Ratfor programs ¶**

*n*.o is made automatically from *n*.r, *n*.F or *n*.f by running the Fortran compiler. The precise recipe used is as follows:

**‘.f’**

‘$(FC) $(FFLAGS) -c’.

**‘.F’**

‘$(FC) $(FFLAGS) $(CPPFLAGS) -c’.

**‘.r’**

‘$(FC) $(FFLAGS) $(RFLAGS) -c’.

**Preprocessing Fortran and Ratfor programs**

*n*.f is made automatically from *n*.r or *n*.F. This rule runs just the preprocessor to convert a Ratfor or preprocessable Fortran program into a strict Fortran program. The precise recipe used is as follows:

**‘.F’**

‘$(FC) $(CPPFLAGS) $(FFLAGS) -F’.

**‘.r’**

‘$(FC) $(FFLAGS) $(RFLAGS) -F’.

**Compiling Modula-2 programs ¶**

*n*.sym is made from *n*.def with a recipe of the form ‘$(M2C) $(M2FLAGS) $(DEFFLAGS)’. *n*.o is made from *n*.mod; the form is: ‘$(M2C) $(M2FLAGS) $(MODFLAGS)’.

**Assembling and preprocessing assembler programs ¶**

*n*.o is made automatically from *n*.s by running the assembler, `as`. The precise recipe is ‘$(AS) $(ASFLAGS)’.

*n*.s is made automatically from *n*.S by running the C preprocessor, `cpp`. The precise recipe is ‘$(CPP) $(CPPFLAGS)’.

**Linking a single object file ¶**

*n* is made automatically from *n*.o by running the C compiler to link the program. The precise recipe used is ‘$(CC) $(LDFLAGS) *n*.o $(LOADLIBES) $(LDLIBS)’.

This rule does the right thing for a simple program with only one source file. It will also do the right thing if there are multiple object files (presumably coming from various other source files), one of which has a name matching that of the executable file. Thus,

```
x: y.o z.o
```

when x.c, y.c and z.c all exist will execute:

```
cc -c x.c -o x.o
cc -c y.c -o y.o
cc -c z.c -o z.o
cc x.o y.o z.o -o x
rm -f x.o
rm -f y.o
rm -f z.o
```

In more complicated cases, such as when there is no object file whose name derives from the executable file name, you must write an explicit recipe for linking.

Each kind of file automatically made into ‘.o’ object files will be automatically linked by using the compiler (‘$(CC)’, ‘$(FC)’ or ‘$(PC)’; the C compiler ‘$(CC)’ is used to assemble ‘.s’ files) without the ‘-c’ option. This could be done by using the ‘.o’ object files as intermediates, but it is faster to do the compiling and linking in one step, so that’s how it’s done.

**Yacc for C programs ¶**

*n*.c is made automatically from *n*.y by running Yacc with the recipe ‘$(YACC) $(YFLAGS)’.

**Lex for C programs ¶**

*n*.c is made automatically from *n*.l by running Lex. The actual recipe is ‘$(LEX) $(LFLAGS)’.

**Lex for Ratfor programs**

*n*.r is made automatically from *n*.l by running Lex. The actual recipe is ‘$(LEX) $(LFLAGS)’.

The convention of using the same suffix ‘.l’ for all Lex files regardless of whether they produce C code or Ratfor code makes it impossible for `make` to determine automatically which of the two languages you are using in any particular case. If `make` is called upon to remake an object file from a ‘.l’ file, it must guess which compiler to use. It will guess the C compiler, because that is more common. If you are using Ratfor, make sure `make` knows this by mentioning *n*.r in the makefile. Or, if you are using Ratfor exclusively, with no C files, remove ‘.c’ from the list of implicit rule suffixes with:

```
.SUFFIXES:
.SUFFIXES: .o .r .f .l …
```

**Making Lint Libraries from C, Yacc, or Lex programs ¶**

*n*.ln is made from *n*.c by running `lint`. The precise recipe is ‘$(LINT) $(LINTFLAGS) $(CPPFLAGS) -i’. The same recipe is used on the C code produced from *n*.y or *n*.l.

**TeX and Web ¶**

*n*.dvi is made from *n*.tex with the recipe ‘$(TEX)’. *n*.tex is made from *n*.web with ‘$(WEAVE)’, or from *n*.w (and from *n*.ch if it exists or can be made) with ‘$(CWEAVE)’. *n*.p is made from *n*.web with ‘$(TANGLE)’ and *n*.c is made from *n*.w (and from *n*.ch if it exists or can be made) with ‘$(CTANGLE)’.

**Texinfo and Info ¶**

*n*.dvi is made from *n*.texinfo, *n*.texi, or *n*.txinfo, with the recipe ‘$(TEXI2DVI) $(TEXI2DVI_FLAGS)’. *n*.info is made from *n*.texinfo, *n*.texi, or *n*.txinfo, with the recipe ‘$(MAKEINFO) $(MAKEINFO_FLAGS)’.

**RCS ¶**

Any file *n* is extracted if necessary from an RCS file named either *n*,v or RCS/*n*,v. The precise recipe used is ‘$(CO) $(COFLAGS)’. *n* will not be extracted from RCS if it already exists, even if the RCS file is newer. The rules for RCS are terminal (see Match-Anything Pattern Rules), so RCS files cannot be generated from another source; they must actually exist.

**SCCS ¶**

Any file *n* is extracted if necessary from an SCCS file named either s.*n* or SCCS/s.*n*. The precise recipe used is ‘$(GET) $(GFLAGS)’. The rules for SCCS are terminal (see Match-Anything Pattern Rules), so SCCS files cannot be generated from another source; they must actually exist.

For the benefit of SCCS, a file *n* is copied from *n*.sh and made executable (by everyone). This is for shell scripts that are checked into SCCS. Since RCS preserves the execution permission of a file, you do not need to use this feature with RCS.

We recommend that you avoid using of SCCS. RCS is widely held to be superior, and is also free. By choosing free software in place of comparable (or inferior) proprietary software, you support the free software movement.

Usually, you want to change only the variables listed in the table above, which are documented in the following section.

However, the recipes in built-in implicit rules actually use variables such as `COMPILE.c`, `LINK.p`, and `PREPROCESS.S`, whose values contain the recipes listed above.

`make` follows the convention that the rule to compile a .*x* source file uses the variable `COMPILE.*x*`. Similarly, the rule to produce an executable from a .*x* file uses `LINK.*x*`; and the rule to preprocess a .*x* file uses `PREPROCESS.*x*`.

Every rule that produces an object file uses the variable `OUTPUT_OPTION`. `make` defines this variable either to contain ‘-o $@’, or to be empty, depending on a compile-time option. You need the ‘-o’ option to ensure that the output goes into the right file when the source file is in a different directory, as when using `VPATH` (see Searching Directories for Prerequisites). However, compilers on some systems do not accept a ‘-o’ switch for object files. If you use such a system, and use `VPATH`, some compilations will put their output in the wrong place. A possible workaround for this problem is to give `OUTPUT_OPTION` the value ‘; mv $*.o $@’.

Next: Chains of Implicit Rules, Previous: Catalogue of Built-In Rules, Up: Using Implicit Rules   [Contents][Index]

### 10.3 Variables Used by Implicit Rules

The recipes in built-in implicit rules make liberal use of certain predefined variables. You can alter the values of these variables in the makefile, with arguments to `make`, or in the environment to alter how the implicit rules work without redefining the rules themselves. You can cancel all variables used by implicit rules with the ‘-R’ or ‘--no-builtin-variables’ option.

For example, the recipe used to compile a C source file actually says ‘$(CC) -c $(CFLAGS) $(CPPFLAGS)’. The default values of the variables used are ‘cc’ and nothing, resulting in the command ‘cc -c’. By redefining ‘CC’ to ‘ncc’, you could cause ‘ncc’ to be used for all C compilations performed by the implicit rule. By redefining ‘CFLAGS’ to be ‘-g’, you could pass the ‘-g’ option to each compilation. *All* implicit rules that do C compilation use ‘$(CC)’ to get the program name for the compiler and *all* include ‘$(CFLAGS)’ among the arguments given to the compiler.

The variables used in implicit rules fall into two classes: those that are names of programs (like `CC`) and those that contain arguments for the programs (like `CFLAGS`). (The “name of a program” may also contain some command arguments, but it must start with an actual executable program name.) If a variable value contains more than one argument, separate them with spaces.

The following tables describe of some of the more commonly-used predefined variables. This list is not exhaustive, and the default values shown here may not be what `make` selects for your environment. To see the complete list of predefined variables for your instance of GNU `make` you can run ‘make -p’ in a directory with no makefiles.

Here is a table of some of the more common variables used as names of programs in built-in rules:

**`AR` ¶**

Archive-maintaining program; default ‘ar’.

**`AS` ¶**

Program for compiling assembly files; default ‘as’.

**`CC` ¶**

Program for compiling C programs; default ‘cc’.

**`CXX` ¶**

Program for compiling C++ programs; default ‘g++’.

**`CPP` ¶**

Program for running the C preprocessor, with results to standard output; default ‘$(CC) -E’.

**`FC` ¶**

Program for compiling or preprocessing Fortran and Ratfor programs; default ‘f77’.

**`M2C` ¶**

Program to use to compile Modula-2 source code; default ‘m2c’.

**`PC` ¶**

Program for compiling Pascal programs; default ‘pc’.

**`CO` ¶**

Program for extracting a file from RCS; default ‘co’.

**`GET` ¶**

Program for extracting a file from SCCS; default ‘get’.

**`LEX` ¶**

Program to use to turn Lex grammars into source code; default ‘lex’.

**`YACC` ¶**

Program to use to turn Yacc grammars into source code; default ‘yacc’.

**`LINT` ¶**

Program to use to run lint on source code; default ‘lint’.

**`MAKEINFO` ¶**

Program to convert a Texinfo source file into an Info file; default ‘makeinfo’.

**`TEX` ¶**

Program to make TeX DVI files from TeX source; default ‘tex’.

**`TEXI2DVI` ¶**

Program to make TeX DVI files from Texinfo source; default ‘texi2dvi’.

**`WEAVE` ¶**

Program to translate Web into TeX; default ‘weave’.

**`CWEAVE` ¶**

Program to translate C Web into TeX; default ‘cweave’.

**`TANGLE` ¶**

Program to translate Web into Pascal; default ‘tangle’.

**`CTANGLE` ¶**

Program to translate C Web into C; default ‘ctangle’.

**`RM` ¶**

Command to remove a file; default ‘rm -f’.

Here is a table of variables whose values are additional arguments for the programs above. The default values for all of these is the empty string, unless otherwise noted.

**`ARFLAGS` ¶**

Flags to give the archive-maintaining program; default ‘rv’.

**`ASFLAGS` ¶**

Extra flags to give to the assembler (when explicitly invoked on a ‘.s’ or ‘.S’ file).

**`CFLAGS` ¶**

Extra flags to give to the C compiler.

**`CXXFLAGS` ¶**

Extra flags to give to the C++ compiler.

**`COFLAGS` ¶**

Extra flags to give to the RCS `co` program.

**`CPPFLAGS` ¶**

Extra flags to give to the C preprocessor and programs that use it (the C and Fortran compilers).

**`FFLAGS` ¶**

Extra flags to give to the Fortran compiler.

**`GFLAGS` ¶**

Extra flags to give to the SCCS `get` program.

**`LDFLAGS` ¶**

Extra flags to give to compilers when they are supposed to invoke the linker, ‘ld’, such as `-L`. Libraries (`-lfoo`) should be added to the `LDLIBS` variable instead.

**`LDLIBS` ¶**

Library flags or names given to compilers when they are supposed to invoke the linker, ‘ld’. `LOADLIBES` is a deprecated (but still supported) alternative to `LDLIBS`. Non-library linker flags, such as `-L`, should go in the `LDFLAGS` variable.

**`LFLAGS` ¶**

Extra flags to give to Lex.

**`YFLAGS` ¶**

Extra flags to give to Yacc.

**`PFLAGS` ¶**

Extra flags to give to the Pascal compiler.

**`RFLAGS` ¶**

Extra flags to give to the Fortran compiler for Ratfor programs.

**`LINTFLAGS` ¶**
