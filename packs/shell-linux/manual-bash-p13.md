---
title: "Bash Reference Manual (part 13/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 13/15
---

## 9 Using History Interactively

This chapter describes how to use the GNU History Library interactively, from a user’s standpoint. It should be considered a user’s guide. For information on using the GNU History Library in other programs, see the GNU Readline Library Manual.

### 9.1 Bash History Facilities

When the -o history option to the `set` builtin is enabled (see The Set Builtin), the shell provides access to the *command history*, the list of commands previously typed. The value of the `HISTSIZE` shell variable is used as the number of commands to save in a history list: the shell saves the text of the last `$HISTSIZE` commands (default 500). The shell stores each command in the history list prior to parameter and variable expansion but after history expansion is performed, subject to the values of the shell variables `HISTIGNORE` and `HISTCONTROL`.

When the shell starts up, Bash initializes the history list by reading history entries from the file named by the `HISTFILE` variable (default ~/.bash_history). This is referred to as the *history file*. The history file is truncated, if necessary, to contain no more than the number of history entries specified by the value of the `HISTFILESIZE` variable. If `HISTFILESIZE` is unset, or set to null, a non-numeric value, or a numeric value less than zero, the history file is not truncated.

When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry. These timestamps are optionally displayed depending on the value of the `HISTTIMEFORMAT` variable (see Bash Variables). When present, history timestamps delimit history entries, making multi-line entries possible.

When a shell with history enabled exits, Bash copies the last `$HISTSIZE` entries from the history list to the file named by `$HISTFILE`. If the `histappend` shell option is set (see Bash Builtin Commands), Bash appends the entries to the history file, otherwise it overwrites the history file. If `HISTFILE` is unset or null, or if the history file is unwritable, the history is not saved. After saving the history, Bash truncates the history file to contain no more than `$HISTFILESIZE` lines as described above.

If the `HISTTIMEFORMAT` variable is set, the shell writes the timestamp information associated with each history entry to the history file, marked with the history comment character, so timestamps are preserved across shell sessions. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry. As above, when using `HISTTIMEFORMAT`, the timestamps delimit multi-line history entries.

The `fc` builtin command will list or edit and re-execute a portion of the history list. The `history` builtin can display or modify the history list and manipulate the history file. When using command-line editing, search commands are available in each editing mode that provide access to the history list (see Commands For Manipulating The History).

The shell allows control over which commands are saved on the history list. The `HISTCONTROL` and `HISTIGNORE` variables are used to save only a subset of the commands entered. If the `cmdhist` shell option is enabled, the shell attempts to save each line of a multi-line command in the same history entry, adding semicolons where necessary to preserve syntactic correctness. The `lithist` shell option modifies `cmdhist` by saving the command with embedded newlines instead of semicolons. The `shopt` builtin is used to set these options. See The Shopt Builtin, for a description of `shopt`.

### 9.2 Bash History Builtins

Bash provides two builtin commands which manipulate the history list and history file.

**`fc` ¶**

```
fc [-e ename] [-lnr] [first] [last]
fc -s [pat=rep] [command]
```

The first form selects a range of commands from *first* to *last* from the history list and displays or edits and re-executes them. Both *first* and *last* may be specified as a string (to locate the most recent command beginning with that string) or as a number (an index into the history list, where a negative number is used as an offset from the current command number).

When listing, a *first* or *last* of 0 is equivalent to -1 and -0 is equivalent to the current command (usually the `fc` command); otherwise 0 is equivalent to -1 and -0 is invalid.

If *last* is not specified, it is set to the current command for listing and to *first* otherwise. If *first* is not specified, it is set to the previous command for editing and −16 for listing.

If the -l flag is supplied, the commands are listed on standard output. The -n flag suppresses the command numbers when listing. The -r flag reverses the order of the listing.

Otherwise, `fc` invokes the editor named by *ename* on a file containing those commands. If *ename* is not supplied, `fc` uses the value of the following variable expansion: `${FCEDIT:-${EDITOR:-vi}}`. This says to use the value of the `FCEDIT` variable if set, or the value of the `EDITOR` variable if that is set, or `vi` if neither is set. When editing is complete, `fc` reads the file of edited commands and echoes and executes them.

In the second form, `fc` re-executes *command* after replacing each instance of *pat* in the selected command with *rep*. *command* is interpreted the same as *first* above.

A useful alias to use with the `fc` command is `r='fc -s'`, so that typing ‘r cc’ runs the last command beginning with `cc` and typing ‘r’ re-executes the last command (see Aliases).

If the first form is used, the return value is zero unless an invalid option is encountered or *first* or *last* specify history lines out of range. When editing and re-executing a file of commands, the return value is the value of the last command executed or failure if an error occurs with the temporary file. If the second form is used, the return status is that of the re-executed command, unless *command* does not specify a valid history entry, in which case `fc` returns a non-zero status.

**`history` ¶**

```
history [n]
history -c
history -d offset
history -d start-end
history [-anrw] [filename]
history -ps arg
```

With no options, display the history list with numbers. Entries prefixed with a ‘*’ have been modified. An argument of *n* lists only the last *n* entries. If the shell variable `HISTTIMEFORMAT` is set and not null, it is used as a format string for `strftime`(3) to display the time stamp associated with each displayed history entry. If `history` uses `HISTTIMEFORMAT`, it does not print an intervening space between the formatted time stamp and the history entry.

Options, if supplied, have the following meanings:

**`-c`**

Clear the history list. This may be combined with the other options to replace the history list.

**`-d *offset*`**

Delete the history entry at position *offset*. If *offset* is positive, it should be specified as it appears when the history is displayed. If *offset* is negative, it is interpreted as relative to one greater than the last history position, so negative indices count back from the end of the history, and an index of ‘-1’ refers to the current `history -d` command.

**`-d *start*-*end*`**

Delete the range of history entries between positions *start* and *end*, inclusive. Positive and negative values for *start* and *end* are interpreted as described above.

**`-a`**

Append the "new" history lines to the history file. These are history lines entered since the beginning of the current Bash session, but not already appended to the history file.

**`-n`**

Read the history lines not already read from the history file and add them to the current history list. These are lines appended to the history file since the beginning of the current Bash session.

**`-r`**

Read the history file and append its contents to the history list.

**`-w`**

Write the current history list to the history file, overwriting the history file.

**`-p`**

Perform history substitution on the *arg*s and display the result on the standard output, without storing the results in the history list.

**`-s`**

Add the *arg*s to the end of the history list as a single entry. The last command in the history list is removed before adding the *arg*s.

If a *filename* argument is supplied with any of the -w, -r, -a, or -n options, Bash uses *filename* as the history file. If not, it uses the value of the `HISTFILE` variable. If `HISTFILE` is unset or null, these options have no effect.

If the `HISTTIMEFORMAT` variable is set, `history` writes the time stamp information associated with each history entry to the history file, marked with the history comment character as described above. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry.

The return value is 0 unless an invalid option is encountered, an error occurs while reading or writing the history file, an invalid *offset* or range is supplied as an argument to -d, or the history expansion supplied as an argument to -p fails.

### 9.3 History Expansion

The shell provides a history expansion feature that is similar to the history expansion provided by `csh` (also referred to as history substitution where appropriate). This section describes the syntax used to manipulate the history information.

History expansion is enabled by default for interactive shells, and can be disabled using the +H option to the `set` builtin command (see The Set Builtin). Non-interactive shells do not perform history expansion by default, but it can be enabled with `set -H`.

History expansions introduce words from the history list into the input stream, making it easy to repeat commands, insert the arguments to a previous command into the current input line, or fix errors in previous commands quickly.

History expansion is performed immediately after a complete line is read, before the shell breaks it into words, and is performed on each line individually. Bash attempts to inform the history expansion functions about quoting still in effect from previous lines.

History expansion takes place in two parts. The first is to determine which entry from the history list should be used during substitution. The second is to select portions of that entry to include into the current one.

The entry selected from the history is called the *event*, and the portions of that entry that are acted upon are *words*. Various *modifiers* are available to manipulate the selected words. The entry is split into words in the same fashion that Bash does when reading input, so that several words surrounded by quotes are considered one word. The *event designator* selects the event, the optional *word designator* selects words from the event, and various optional *modifiers* are available to manipulate the selected words.

History expansions are introduced by the appearance of the history expansion character, which is ‘!’ by default. History expansions may appear anywhere in the input, but do not nest.

History expansion implements shell-like quoting conventions: a backslash can be used to remove the special handling for the next character; single quotes enclose verbatim sequences of characters, and can be used to inhibit history expansion; and characters enclosed within double quotes may be subject to history expansion, since backslash can escape the history expansion character, but single quotes may not, since they are not treated specially within double quotes.

When using the shell, only ‘\’ and ‘'’ may be used to escape the history expansion character, but the history expansion character is also treated as quoted if it immediately precedes the closing double quote in a double-quoted string.

Several characters inhibit history expansion if found immediately following the history expansion character, even if it is unquoted: space, tab, newline, carriage return, ‘=’, and the other shell metacharacters.

There is a special abbreviation for substitution, active when the *quick substitution* character (described above under `histchars`) is the first character on the line. It selects the previous history list entry, using an event designator equivalent to `!!`, and substitutes one string for another in that entry. It is described below (see Event Designators). This is the only history expansion that does not begin with the history expansion character.

Several shell options settable with the `shopt` builtin (see The Shopt Builtin) modify history expansion behavior If the `histverify` shell option is enabled, and Readline is being used, history substitutions are not immediately passed to the shell parser. Instead, the expanded line is reloaded into the Readline editing buffer for further modification. If Readline is being used, and the `histreedit` shell option is enabled, a failed history expansion is reloaded into the Readline editing buffer for correction.

The -p option to the `history` builtin command shows what a history expansion will do before using it. The -s option to the `history` builtin may be used to add commands to the end of the history list without actually executing them, so that they are available for subsequent recall. This is most useful in conjunction with Readline.

The shell allows control of the various characters used by the history expansion mechanism with the `histchars` variable, as explained above (see Bash Variables). The shell uses the history comment character to mark history timestamps when writing the history file.

#### 9.3.1 Event Designators

An event designator is a reference to an entry in the history list. The event designator consists of the portion of the word beginning with the history expansion character, and ending with the word designator if one is present, or the end of the word. Unless the reference is absolute, events are relative to the current position in the history list.

**`!`**

Start a history substitution, except when followed by a space, tab, the end of the line, ‘=’, or the rest of the shell metacharacters defined above (see Definitions).

**`!*n*`**

Refer to history list entry *n*.

**`!-*n*`**

Refer to the history entry minus *n*.

**`!!`**

Refer to the previous entry. This is a synonym for ‘!-1’.

**`!*string*`**

Refer to the most recent command preceding the current position in the history list starting with *string*.

**`!?*string*[?]`**

Refer to the most recent command preceding the current position in the history list containing *string*. The trailing ‘?’ may be omitted if the *string* is followed immediately by a newline. If *string* is missing, this uses the string from the most recent search; it is an error if there is no previous search string.

**`^*string1*^*string2*^`**

Quick Substitution. Repeat the last command, replacing *string1* with *string2*. Equivalent to `!!:s^*string1*^*string2*^`.

**`!#`**

The entire command line typed so far.

#### 9.3.2 Word Designators

Word designators are used to select desired words from the event. They are optional; if the word designator isn’t supplied, the history expansion uses the entire event. A ‘:’ separates the event specification from the word designator. It may be omitted if the word designator begins with a ‘^’, ‘$’, ‘*’, ‘-’, or ‘%’. Words are numbered from the beginning of the line, with the first word being denoted by 0 (zero). That first word is usually the command word, and the arguments begin with the second word. Words are inserted into the current line separated by single spaces.

For example,

**`!!`**

designates the preceding command. When you type this, the preceding command is repeated in toto.

**`!!:$`**

designates the last word of the preceding command. This may be shortened to `!$`.

**`!fi:2`**

designates the second argument of the most recent command starting with the letters `fi`.

Here are the word designators:

**`0 (zero)`**

The `0`th word. For the shell, and many other, applications, this is the command word.

**`*n*`**

The *n*th word.

**`^`**

The first argument: word 1.

**`$`**

The last word. This is usually the last argument, but expands to the zeroth word if there is only one word in the line.

**`%`**

The first word matched by the most recent ‘?*string*?’ search, if the search string begins with a character that is part of a word. By default, searches begin at the end of each line and proceed to the beginning, so the first word matched is the one closest to the end of the line.

**`*x*-*y*`**

A range of words; ‘-*y*’ abbreviates ‘0-*y*’.

**`*`**

All of the words, except the `0`th. This is a synonym for ‘1-$’. It is not an error to use ‘*’ if there is just one word in the event; it expands to the empty string in that case.

**`*x**`**

Abbreviates ‘*x*-$’.

**`*x*-`**

Abbreviates ‘*x*-$’ like ‘*x**’, but omits the last word. If ‘x’ is missing, it defaults to 0.

If a word designator is supplied without an event specification, the previous command is used as the event, equivalent to `!!`.

#### 9.3.3 Modifiers

After the optional word designator, you can add a sequence of one or more of the following modifiers, each preceded by a ‘:’. These modify, or edit, the word or words selected from the history event.

**`h`**

Remove a trailing filename component, leaving only the head.

**`t`**

Remove all leading filename components, leaving the tail.

**`r`**

Remove a trailing suffix of the form ‘.*suffix*’, leaving the basename.

**`e`**

Remove all but the trailing suffix.

**`p`**

Print the new command but do not execute it.

**`q`**

Quote the substituted words, escaping further substitutions.

**`x`**

Quote the substituted words as with ‘q’, but break into words at spaces, tabs, and newlines. The ‘q’ and ‘x’ modifiers are mutually exclusive; expansion uses the last one supplied.

**`s/*old*/*new*/`**

Substitute *new* for the first occurrence of *old* in the event line. Any character may be used as the delimiter in place of ‘/’. The delimiter may be quoted in *old* and *new* with a single backslash. If ‘&’ appears in *new*, it is replaced with *old*. A single backslash quotes the ‘&’ in *old* and *new*. If *old* is null, it is set to the last *old* substituted, or, if no previous history substitutions took place, the last *string* in a !?*string*`[?]` search. If *new* is null, each matching *old* is deleted. The final delimiter is optional if it is the last character on the input line.

**`&`**

Repeat the previous substitution.

**`g`**

**`a`**

Cause changes to be applied over the entire event line. This is used in conjunction with ‘s’, as in `gs/*old*/*new*/`, or with ‘&’.

**`G`**

Apply the following ‘s’ or ‘&’ modifier once to each word in the event.


## 10 Installing Bash

This chapter provides basic instructions for installing Bash on the various supported platforms. The distribution supports the GNU operating systems, nearly every version of Unix, and several non-Unix systems such as BeOS and Interix. Other independent ports exist for Windows platforms.

### 10.1 Basic Installation

These are installation instructions for Bash.

The simplest way to compile Bash is:

1. `cd` to the directory containing the source code and type ‘./configure’ to configure Bash for your system. If you’re using `csh` on an old version of System V, you might need to type ‘sh ./configure’ instead to prevent `csh` from trying to execute `configure` itself. Running `configure` takes some time. While running, it prints messages telling which features it is checking for.
2. Type ‘make’ to compile Bash and build the `bashbug` bug reporting script.
3. Optionally, type ‘make tests’ to run the Bash test suite.
4. Type ‘make install’ to install `bash` and `bashbug`. This will also install the manual pages and Info file, message translation files, some supplemental documentation, a number of example loadable builtin commands, and a set of header files for developing loadable builtins. You may need additional privileges to install `bash` to your desired destination, which may require ‘sudo make install’. More information about controlling the locations where `bash` and other files are installed is below (see Installation Names).

The `configure` shell script attempts to guess correct values for various system-dependent variables used during compilation. It uses those values to create a Makefile in each directory of the package (the top directory, the builtins, doc, po, and support directories, each directory under lib, and several others). It also creates a config.h file containing system-dependent definitions. Finally, it creates a shell script named `config.status` that you can run in the future to recreate the current configuration, a file config.cache that saves the results of its tests to speed up reconfiguring, and a file config.log containing compiler output (useful mainly for debugging `configure`). If at some point config.cache contains results you don’t want to keep, you may remove or edit it.

To find out more about the options and arguments that the `configure` script understands, type

```
bash-4.2$ ./configure --help
```

at the Bash prompt in your Bash source directory.

If you want to build Bash in a directory separate from the source directory – to build for multiple architectures, for example – just use the full path to the configure script. The following commands will build Bash in a directory under /usr/local/build from the source code in /usr/local/src/bash-4.4:

```
mkdir /usr/local/build/bash-4.4
cd /usr/local/build/bash-4.4
bash /usr/local/src/bash-4.4/configure
make
```

See Compiling For Multiple Architectures for more information about building in a directory separate from the source.

If you need to do unusual things to compile Bash, please try to figure out how `configure` could check whether or not to do them, and mail diffs or instructions to bash-maintainers@gnu.org so they can be considered for the next release.

The file configure.ac is used to create `configure` by a program called Autoconf. You only need configure.ac if you want to change it or regenerate `configure` using a newer version of Autoconf. If you do this, make sure you are using Autoconf version 2.69 or newer.

You can remove the program binaries and object files from the source code directory by typing ‘make clean’. To also remove the files that `configure` created (so you can compile Bash for a different kind of computer), type ‘make distclean’.

### 10.2 Compilers and Options

Some systems require unusual options for compilation or linking that the `configure` script does not know about. You can give `configure` initial values for variables by setting them in the environment. Using a Bourne-compatible shell, you can do that on the command line like this:

```
CC=c89 CFLAGS=-O2 LIBS=-lposix ./configure
```

On systems that have the `env` program, you can do it like this:

```
env CPPFLAGS=-I/usr/local/include LDFLAGS=-s ./configure
```

The configuration process uses GCC to build Bash if it is available.

### 10.3 Compiling For Multiple Architectures

You can compile Bash for more than one kind of computer at the same time, by placing the object files for each architecture in their own directory. To do this, you must use a version of `make` that supports the `VPATH` variable, such as GNU `make`. `cd` to the directory where you want the object files and executables to go and run the `configure` script from the source directory (see Basic Installation). You may need to supply the --srcdir=PATH argument to tell `configure` where the source files are. `configure` automatically checks for the source code in the directory that `configure` is in and in ...

If you have to use a `make` that does not support the `VPATH` variable, you can compile Bash for one architecture at a time in the source code directory. After you have installed Bash for one architecture, use ‘make distclean’ before reconfiguring for another architecture.

Alternatively, if your system supports symbolic links, you can use the support/mkclone script to create a build tree which has symbolic links back to each file in the source directory. Here’s an example that creates a build directory in the current directory from a source directory /usr/gnu/src/bash-2.0:

```
bash /usr/gnu/src/bash-2.0/support/mkclone -s /usr/gnu/src/bash-2.0 .
```

The `mkclone` script requires Bash, so you must have already built Bash for at least one architecture before you can create build directories for other architectures.

### 10.4 Installation Names

By default, ‘make install’ will install into /usr/local/bin, /usr/local/man, etc.; that is, the *installation prefix* defaults to /usr/local. You can specify an installation prefix other than /usr/local by giving `configure` the option --prefix=*PATH*, or by specifying a value for the `prefix` ‘make’ variable when running ‘make install’ (e.g., ‘make install prefix=*PATH*’). The `prefix` variable provides a default for `exec_prefix` and other variables used when installing Bash.

You can specify separate installation prefixes for architecture-specific files and architecture-independent files. If you give `configure` the option --exec-prefix=*PATH*, ‘make install’ will use *PATH* as the prefix for installing programs and libraries. Documentation and other data files will still use the regular prefix.

If you would like to change the installation locations for a single run, you can specify these variables as arguments to `make`: ‘make install exec_prefix=/’ will install `bash` and `bashbug` into /bin instead of the default /usr/local/bin.

If you want to see the files Bash will install and where it will install them without changing anything on your system, specify the variable `DESTDIR` as an argument to `make`. Its value should be the absolute directory path you’d like to use as the root of your sample installation tree. For example,

```
mkdir /fs1/bash-install
make install DESTDIR=/fs1/bash-install
```

will install `bash` into /fs1/bash-install/usr/local/bin/bash, the documentation into directories within /fs1/bash-install/usr/local/share, the example loadable builtins into /fs1/bash-install/usr/local/lib/bash, and so on. You can use the usual `exec_prefix` and `prefix` variables to alter the directory paths beneath the value of `DESTDIR`.

The GNU Makefile standards provide a more complete description of these variables and their effects.

### 10.5 Specifying the System Type

There may be some features `configure` can not figure out automatically, but needs to determine by the type of host Bash will run on. Usually `configure` can figure that out, but if it prints a message saying it can not guess the host type, give it the --host=TYPE option. ‘TYPE’ can either be a short name for the system type, such as ‘sun4’, or a canonical name with three fields: ‘CPU-COMPANY-SYSTEM’ (e.g., ‘i386-unknown-freebsd4.2’).

See the file support/config.sub for the possible values of each field.

### 10.6 Sharing Defaults

If you want to set default values for `configure` scripts to share, you can create a site shell script called `config.site` that gives default values for variables like `CC`, `cache_file`, and `prefix`. `configure` looks for PREFIX/share/config.site if it exists, then PREFIX/etc/config.site if it exists. Or, you can set the `CONFIG_SITE` environment variable to the location of the site script. A warning: the Bash `configure` looks for a site script, but not all `configure` scripts do.

### 10.7 Operation Controls

`configure` recognizes the following options to control how it operates.

**`--cache-file=*file*`**

Use and save the results of the tests in *file* instead of ./config.cache. Set *file* to /dev/null to disable caching, for debugging `configure`.

**`--help`**

Print a summary of the options to `configure`, and exit.

**`--quiet`**

**`--silent`**

**`-q`**

Do not print messages saying which checks are being made.

**`--srcdir=*dir*`**

Look for the Bash source code in directory *dir*. Usually `configure` can determine that directory automatically.

**`--version`**

Print the version of Autoconf used to generate the `configure` script, and exit.

`configure` also accepts some other, not widely used, boilerplate options. ‘configure --help’ prints the complete list.

### 10.8 Optional Features

The Bash `configure` has a number of --enable-*feature* options, where *feature* indicates an optional part of Bash. There are also several --with-*package* options, where *package* is something like ‘bash-malloc’ or ‘afs’. To turn off the default use of a package, use --without-*package*. To configure Bash without a feature that is enabled by default, use --disable-*feature*.

Here is a complete list of the --enable- and --with- options that the Bash `configure` recognizes.

**`--with-afs`**

Define if you are using the Andrew File System from Transarc.

**`--with-bash-malloc`**

Use the Bash version of `malloc` in the directory lib/malloc. This is not the same `malloc` that appears in GNU libc, but a custom version originally derived from the 4.2 BSD `malloc`. This `malloc` is very fast, but wastes some space on each allocation, though it uses several techniques to minimize the waste. This option is enabled by default. The NOTES file contains a list of systems for which this should be turned off, and `configure` disables this option automatically for a number of systems.

**`--with-curses`**

Use the curses library instead of the termcap library. `configure` usually chooses this automatically, since most systems include the termcap functions in the curses library.

**`--with-gnu-malloc`**

A synonym for `--with-bash-malloc`.

**`--with-installed-readline[=*PREFIX*]`**

Define this to make Bash link with a locally-installed version of Readline rather than the version in lib/readline. This works only with Readline 5.0 and later versions. If *PREFIX* is `yes` or not supplied, `configure` uses the values of the make variables `includedir` and `libdir`, which are subdirectories of `prefix` by default, to find the installed version of Readline if it is not in the standard system include and library directories. If *PREFIX* is `no`, Bash links with the version in lib/readline. If *PREFIX* is set to any other value, `configure` treats it as a directory pathname and looks for the installed version of Readline in subdirectories of that directory (include files in *PREFIX*/`include` and the library in *PREFIX*/`lib`). The Bash default is to link with a static library built in the lib/readline subdirectory of the build directory.

**`--with-libintl-prefix[=*PREFIX*]`**

Define this to make Bash link with a locally-installed version of the libintl library instead of the version in lib/intl.

**`--with-libiconv-prefix[=*PREFIX*]`**

Define this to make Bash look for libiconv in *PREFIX* instead of the standard system locations. The Bash distribution does not include this library.

**`--enable-minimal-config`**

This produces a shell with minimal features, closer to the historical Bourne shell.

There are several --enable- options that alter how Bash is compiled, linked, and installed, rather than changing run-time features.

**`--enable-largefile`**

Enable support for large files if the operating system requires special compiler options to build programs which can access large files. This is enabled by default, if the operating system provides large file support.

**`--enable-profiling`**

This builds a Bash binary that produces profiling information to be processed by `gprof` each time it is executed.

**`--enable-separate-helpfiles`**

Use external files for the documentation displayed by the `help` builtin instead of storing the text internally.

**`--enable-static-link`**

This causes Bash to be linked statically, if `gcc` is being used. This could be used to build a version to use as root’s shell.

The ‘minimal-config’ option can be used to disable all of the following options, but it is processed first, so individual options may be enabled using ‘enable-*feature*’.

All of the following options except for ‘alt-array-implementation’, ‘disabled-builtins’, ‘direxpand-default’, ‘strict-posix-default’, and ‘xpg-echo-default’ are enabled by default, unless the operating system does not provide the necessary support.

**`--enable-alias`**

Allow alias expansion and include the `alias` and `unalias` builtins (see Aliases).

**`--enable-alt-array-implementation`**

This builds Bash using an alternate implementation of arrays (see Arrays) that provides faster access at the expense of using more memory (sometimes many times more, depending on how sparse an array is).

**`--enable-arith-for-command`**

Include support for the alternate form of the `for` command that behaves like the C language `for` statement (see Looping Constructs).

**`--enable-array-variables`**

Include support for one-dimensional array shell variables (see Arrays).

**`--enable-bang-history`**

Include support for `csh`-like history substitution (see History Expansion).

**`--enable-bash-source-fullpath-default`**

Set the default value of the `bash_source_fullpath` shell option described above under The Shopt Builtin to be enabled. This controls how filenames are assigned to the `BASH_SOURCE` array variable.

**`--enable-brace-expansion`**

Include `csh`-like brace expansion ( `b{a,b}c` → `bac bbc` ). See Brace Expansion, for a complete description.

**`--enable-casemod-attributes`**

Include support for case-modifying attributes in the `declare` builtin and assignment statements. Variables with the `uppercase` attribute, for example, will have their values converted to uppercase upon assignment.

**`--enable-casemod-expansion`**

Include support for case-modifying word expansions.

**`--enable-command-timing`**

Include support for recognizing `time` as a reserved word and for displaying timing statistics for the pipeline following `time` (see Pipelines). This allows timing pipelines, shell compound commands, shell builtins, and shell functions, which an external command cannot do easily.

**`--enable-cond-command`**

Include support for the `[[` conditional command. (see Conditional Constructs).

**`--enable-cond-regexp`**

Include support for matching POSIX regular expressions using the ‘=~’ binary operator in the `[[` conditional command. (see Conditional Constructs).

**`--enable-coprocesses`**

Include support for coprocesses and the `coproc` reserved word (see Pipelines).

**`--enable-debugger`**

Include support for the Bash debugger (distributed separately).

**`--enable-dev-fd-stat-broken`**

If calling `stat` on /dev/fd/*N* returns different results than calling `fstat` on file descriptor *N*, supply this option to enable a workaround. This has implications for conditional commands that test file attributes.

**`--enable-direxpand-default`**

Cause the `direxpand` shell option (see The Shopt Builtin) to be enabled by default when the shell starts. It is normally disabled by default.

**`--enable-directory-stack`**

Include support for a `csh`-like directory stack and the `pushd`, `popd`, and `dirs` builtins (see The Directory Stack).

**`--enable-disabled-builtins`**

Allow builtin commands to be invoked via ‘builtin xxx’ even after `xxx` has been disabled using ‘enable -n xxx’. See Bash Builtin Commands, for details of the `builtin` and `enable` builtin commands.

**`--enable-dparen-arithmetic`**

Include support for the `((…))` command (see Conditional Constructs).

**`--enable-extended-glob`**

Include support for the extended pattern matching features described above under Pattern Matching.

**`--enable-extended-glob-default`**

Set the default value of the `extglob` shell option described above under The Shopt Builtin to be enabled.

**`--enable-function-import`**

Include support for importing function definitions exported by another instance of the shell from the environment. This option is enabled by default.

**`--enable-glob-asciiranges-default`**

Set the default value of the `globasciiranges` shell option described above under The Shopt Builtin to be enabled. This controls the behavior of character ranges when used in pattern matching bracket expressions.

**`--enable-help-builtin`**

Include the `help` builtin, which displays help on shell builtins and variables (see Bash Builtin Commands).

**`--enable-history`**

Include command history and the `fc` and `history` builtin commands (see Bash History Facilities).

**`--enable-job-control`**

This enables the job control features (see Job Control), if the operating system supports them.

**`--enable-multibyte`**

This enables support for multibyte characters if the operating system provides the necessary support.

**`--enable-net-redirections`**

This enables the special handling of filenames of the form `/dev/tcp/*host*/*port*` and `/dev/udp/*host*/*port*` when used in redirections (see Redirections).

**`--enable-process-substitution`**

This enables process substitution (see Process Substitution) if the operating system provides the necessary support.

**`--enable-progcomp`**

Enable the programmable completion facilities (see Programmable Completion). If Readline is not enabled, this option has no effect.

**`--enable-prompt-string-decoding`**

Turn on the interpretation of a number of backslash-escaped characters in the `$PS0`, `$PS1`, `$PS2`, and `$PS4` prompt strings. See Controlling the Prompt, for a complete list of prompt string escape sequences.

**`--enable-readline`**

Include support for command-line editing and history with the Bash version of the Readline library (see Command Line Editing).

**`--enable-restricted`**

Include support for a *restricted shell*. If this is enabled, Bash enters a restricted mode when called as `rbash`. See The Restricted Shell, for a description of restricted mode.

**`--enable-select`**

Include the `select` compound command, which allows generation of simple menus (see Conditional Constructs).

**`--enable-single-help-strings`**

Store the text displayed by the `help` builtin as a single string for each help topic. This aids in translating the text to different languages. You may need to disable this if your compiler cannot handle very long string literals.

**`--enable-strict-posix-default`**

Make Bash POSIX-conformant by default (see Bash and POSIX).

**`--enable-translatable-strings`**

Enable support for `$"*string*"` translatable strings (see Locale-Specific Translation).

**`--enable-usg-echo-default`**

A synonym for `--enable-xpg-echo-default`.

**`--enable-xpg-echo-default`**

Make the `echo` builtin expand backslash-escaped characters by default, without requiring the -e option. This sets the default value of the `xpg_echo` shell option to `on`, which makes the Bash `echo` behave more like the version specified in the Single Unix Specification, version 3. See Bash Builtin Commands, for a description of the escape sequences that `echo` recognizes.

The file config-top.h contains C Preprocessor ‘#define’ statements for options which are not settable from `configure`. Some of these are not meant to be changed; beware of the consequences if you do. Read the comments associated with each definition for more information about its effect.


## Appendix A Reporting Bugs

Please report all bugs you find in Bash. But first, you should make sure that it really is a bug, and that it appears in the latest version of Bash. The latest released version of Bash is always available for FTP from ftp://ftp.gnu.org/pub/gnu/bash/ and from http://git.savannah.gnu.org/cgit/bash.git/snapshot/bash-master.tar.gz.

Once you have determined that a bug actually exists, use the `bashbug` command to submit a bug report or use the form at the Bash project page. If you have a fix, you are encouraged to submit that as well! Suggestions and ‘philosophical’ bug reports may be mailed to bug-bash@gnu.org or help-bash@gnu.org.

All bug reports should include:

- The version number of Bash.
- The hardware and operating system.
- The compiler used to compile Bash.
- A description of the bug behavior.
- A short script or ‘recipe’ which exercises the bug and may be used to reproduce it.

`bashbug` inserts the first three items automatically into the template it provides for filing a bug report.

Please send all reports concerning this manual to bug-bash@gnu.org.
