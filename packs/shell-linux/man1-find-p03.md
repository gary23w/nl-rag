---
title: "find(1) (part 3/3)"
source: https://man7.org/linux/man-pages/man1/find.1.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 3/3
---

## UNUSUAL FILENAMES

Many of the actions of find result in the printing of data which
is under the control of other users.  This includes file names,
sizes, modification times and so forth.  File names are a
potential problem since they can contain any character except `\0'
and `/'.  Unusual characters in file names can do unexpected and
often undesirable things to your terminal (for example, changing
the settings of your function keys on some terminals).  Unusual
characters are handled differently by various actions, as
described below.

-print0, -fprint0
       Always print the exact filename, unchanged, even if the
       output is going to a terminal.

-ls, -fls
       Unusual characters are always escaped.  White space,
       backslash, and double quote characters are printed using C-
       style escaping (for example `\f', `\"').  Other unusual
       characters are printed using an octal escape.  Other
       printable characters (for -ls and -fls these are the
       characters between octal 041 and 0176) are printed as-is.

-printf, -fprintf
       If the output is not going to a terminal, it is printed as-
       is.  Otherwise, the result depends on which directive is in
       use.  The directives %D, %F, %g, %G, %H, %Y, and %y expand
       to values which are not under control of files' owners, and
       so are printed as-is.  The directives %a, %b, %c, %d, %i,
       %k, %m, %M, %n, %s, %t, %u and %U have values which are
       under the control of files' owners but which cannot be used
       to send arbitrary data to the terminal, and so these are
       printed as-is.  The directives %f, %h, %l, %p and %P are
       quoted.  This quoting is performed in the same way as for
       GNU ls.  This is not the same quoting mechanism as the one
       used for -ls and -fls.  If you are able to decide what
       format to use for the output of find then it is normally
       better to use `\0' as a terminator than to use newline, as
       file names can contain white space and newline characters.
       The setting of the LC_CTYPE environment variable is used to
       determine which characters need to be quoted.

-print, -fprint
       Quoting is handled in the same way as for -printf and
       -fprintf.  If you are using find in a script or in a
       situation where the matched files might have arbitrary
       names, you should consider using -print0 instead of -print.

The -ok and -okdir actions print the current filename as-is.  This
may change in a future release.


## STANDARDS CONFORMANCE

For closest compliance to the POSIX standard, you should set the
POSIXLY_CORRECT environment variable.  The following options are
specified in the POSIX standard (IEEE Std 1003.1-2024 Edition):

-H     This option is supported.

-L     This option is supported.

-name  This option is supported, but POSIX conformance depends on
       the POSIX conformance of the system's fnmatch(3) library
       function.  As of findutils-4.2.2 (2004), shell
       metacharacters (`*', `?' or `[]' for example) match a
       leading `.', because IEEE PASC interpretation 126 requires
       this.  This is a change from previous versions of
       findutils.

-type  Supported.  POSIX specifies `b', `c', `d', `l', `p', `f'
       and `s'.  GNU find also supports `D', representing a Door,
       where the OS provides these.  Furthermore, GNU find allows
       multiple types to be specified at once in a comma-separated
       list.

-ok    Supported.  Interpretation of the response is according to
       the `yes' and `no' patterns selected by setting the
       LC_MESSAGES environment variable.  When the POSIXLY_CORRECT
       environment variable is set, these patterns are taken
       system's definition of a positive (yes) or negative (no)
       response.  See the system's documentation for
       nl_langinfo(3), in particular YESEXPR and NOEXPR.  When
       POSIXLY_CORRECT is not set, the patterns are instead taken
       from find's own message catalogue.

-newer Supported.  If the file specified is a symbolic link, it is
       always dereferenced.  This is a change from previous
       behaviour, which used to take the relevant time from the
       symbolic link; see the HISTORY section below.

-perm  Supported.  If the POSIXLY_CORRECT environment variable is
       not set, some mode arguments (for example +a+x) which are
       not valid in POSIX are supported for backward-
       compatibility.

Other primaries
       The primaries -atime, -ctime, -depth, -exec, -group,
       -links, -mount, -mtime, -nogroup, -nouser, -ok, -path,
       -print, -prune, -size, -user and -xdev are all supported.

The POSIX standard specifies parentheses `(', `)', negation `!'
and the logical AND/OR operators -a and -o.

All other options, predicates, expressions and so forth are
extensions beyond the POSIX standard.  Many of these extensions
are not unique to GNU find, however.

The POSIX standard requires that find detects loops:

       The find utility shall detect infinite loops; that is,
       entering a previously visited directory that is an ancestor
       of the last file encountered.  When it detects an infinite
       loop, find shall write a diagnostic message to standard
       error and shall either recover its position in the
       hierarchy or terminate.

GNU find complies with these requirements.  The link count of
directories which contain entries which are hard links to an
ancestor will often be lower than they otherwise should be.  This
can mean that GNU find will sometimes optimize away the visiting
of a subdirectory which is actually a link to an ancestor.  Since
find does not actually enter such a subdirectory, it is allowed to
avoid emitting a diagnostic message.  Although this behaviour may
be somewhat confusing, it is unlikely that anybody actually
depends on this behaviour.  If the leaf optimisation has been
turned off with -noleaf, the directory entry will always be
examined and the diagnostic message will be issued where it is
appropriate.  Symbolic links cannot be used to create filesystem
cycles as such, but if the -L option or the -follow option is in
use, a diagnostic message is issued when find encounters a loop of
symbolic links.  As with loops containing hard links, the leaf
optimisation will often mean that find knows that it doesn't need
to call stat() or chdir() on the symbolic link, so this diagnostic
is frequently not necessary.

The -d option is supported for compatibility with various BSD
systems, but you should use the POSIX-compliant option -depth
instead.

The POSIXLY_CORRECT environment variable does not affect the
behaviour of the -regex or -iregex tests because those tests
aren't specified in the POSIX standard.


## ENVIRONMENT VARIABLES

LANG   Provides a default value for the internationalization
       variables that are unset or null.

LC_ALL If set to a non-empty string value, override the values of
       all the other internationalization variables.

LC_COLLATE
       The POSIX standard specifies that this variable affects the
       pattern matching to be used for the -name option.  GNU find
       uses the fnmatch(3) library function, and so support for
       LC_COLLATE depends on the system library.  This variable
       also affects the interpretation of the response to -ok;
       while the LC_MESSAGES variable selects the actual pattern
       used to interpret the response to -ok, the interpretation
       of any bracket expressions in the pattern will be affected
       by LC_COLLATE.

LC_CTYPE
       This variable affects the treatment of character classes
       used in regular expressions and also with the -name test,
       if the system's fnmatch(3) library function supports this.
       This variable also affects the interpretation of any
       character classes in the regular expressions used to
       interpret the response to the prompt issued by -ok.  The
       LC_CTYPE environment variable will also affect which
       characters are considered to be unprintable when filenames
       are printed; see the section UNUSUAL FILENAMES.

LC_MESSAGES
       Determines the locale to be used for internationalised
       messages.  If the POSIXLY_CORRECT environment variable is
       set, this also determines the interpretation of the
       response to the prompt made by the -ok action.

NLSPATH
       Determines the location of the internationalisation message
       catalogues.

PATH   Affects the directories which are searched to find the
       executables invoked by -exec, -execdir, -ok and -okdir.

POSIXLY_CORRECT
       Determines the block size used by -ls and -fls.  If
       POSIXLY_CORRECT is set, blocks are units of 512 bytes.
       Otherwise they are units of 1024 bytes.

       Setting this variable also turns off warning messages (that
       is, implies -nowarn) by default, because POSIX requires
       that apart from the output for -ok, all messages printed on
       standard error are diagnostics and must result in a non-
       zero exit status.

       When POSIXLY_CORRECT is not set, -perm +zzz is treated just
       like -perm /zzz if +zzz is not a valid symbolic mode.  When
       POSIXLY_CORRECT is set, such constructs are treated as an
       error.

       When POSIXLY_CORRECT is set, the response to the prompt
       made by the -ok action is interpreted according to the
       system's message catalogue, as opposed to according to
       find's own message translations.

TZ     Affects the time zone used for some of the time-related
       format directives of -printf and -fprintf.


## EXAMPLES

   Simple `find|xargs` approach
•   Find files named core in or below the directory /tmp and
    delete them.

        $ find /tmp -name core -type f -print | xargs /bin/rm -f

    Note that this will work incorrectly if there are any
    filenames containing newlines, single or double quotes, or
    spaces.

   Safer `find -print0 | xargs -0` approach
•   Find files named core in or below the directory /tmp and
    delete them, processing filenames in such a way that file or
    directory names containing single or double quotes, spaces or
    newlines are correctly handled.

        $ find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f

    The -name test comes before the -type test in order to avoid
    having to call stat(2) on every file.

Note that there is still a race between the time find traverses
the hierarchy printing the matching filenames, and the time the
process executed by xargs works with that file.

### Processing arbitrary starting points

•   Given that another program proggy pre-filters and creates a
    huge NUL-separated list of files, process those as starting
    points, and find all regular, empty files among them:

        $ proggy | find -files0-from - -maxdepth 0 -type f -empty

    The use of `-files0-from -' means to read the names of the
    starting points from standard input, i.e., from the pipe; and
    -maxdepth 0 ensures that only explicitly those entries are
    examined without recursing into directories (in the case one
    of the starting points is one).

### Executing a command for each file

•   Run file on every file in or below the current directory.

        $ find . -type f -exec file '{}' \;

    Notice that the braces are enclosed in single quote marks to
    protect them from interpretation as shell script punctuation.
    The semicolon is similarly protected by the use of a
    backslash, though single quotes could have been used in that
    case also.

In many cases, one might prefer the `-exec ... +' or better the
`-execdir ... +' syntax for performance and security reasons.

   Traversing the filesystem just once — for 2 different actions
•   Traverse the filesystem just once, listing set-user-ID files
    and directories into /root/suid.txt and large files into
    /root/big.txt.

        $ find / \
            \( -perm -4000 -fprintf /root/suid.txt '%#m %u %p\n' \) , \
            \( -size +100M -fprintf /root/big.txt '%-10s %p\n' \)

    This example uses the line-continuation character '\' on the
    first two lines to instruct the shell to continue reading the
    command on the next line.

### Searching files by age

•   Search for files in your home directory which have been
    modified in the last twenty-four hours.

        $ find $HOME -mtime 0

    This command works this way because the time since each file
    was last modified is divided by 24 hours and any remainder is
    discarded.  That means that to match -mtime 0, a file will
    have to have a modification in the past which is less than 24
    hours ago.

### Searching files by permissions

•   Search for files which are executable but not readable.

        $ find /sbin /usr/sbin -executable \! -readable -print

•   Search for files which have read and write permission for
    their owner, and group, but which other users can read but not
    write to.

        $ find . -perm 664

    Files which meet these criteria but have other permissions
    bits set (for example if someone can execute the file) will
    not be matched.

•   Search for files which have read and write permission for
    their owner and group, and which other users can read, without
    regard to the presence of any extra permission bits (for
    example the executable bit).

        $ find . -perm -664

    This will match a file which has mode 0777, for example.

•   Search for files which are writable by somebody (their owner,
    or their group, or anybody else).

        $ find . -perm /222

•   Search for files which are writable by either their owner or
    their group.

        $ find . -perm /220
        $ find . -perm /u+w,g+w
        $ find . -perm /u=w,g=w

    All three of these commands do the same thing, but the first
    one uses the octal representation of the file mode, and the
    other two use the symbolic form.  The files don't have to be
    writable by both the owner and group to be matched; either
    will do.

•   Search for files which are writable by both their owner and
    their group.

        $ find . -perm -220
        $ find . -perm -g+w,u+w

    Both these commands do the same thing.

•   A more elaborate search on permissions.

        $ find . -perm -444 -perm /222 \! -perm /111
        $ find . -perm -a+r -perm /a+w \! -perm /a+x

    These two commands both search for files that are readable for
    everybody (-perm -444 or -perm -a+r), have at least one write
    bit set (-perm /222 or -perm /a+w) but are not executable for
    anybody (! -perm /111 or ! -perm /a+x respectively).

   Pruning — omitting files and subdirectories
•   Copy the contents of /source-dir to /dest-dir, but omit files
    and directories named .snapshot (and anything in them).  It
    also omits files or directories whose name ends in `~', but
    not their contents.

        $ cd /source-dir
        $ find . -name .snapshot -prune -o \( \! -name '*~' -print0 \) \
            | cpio -pmd0 /dest-dir

    The construct -prune -o \( ... -print0 \) is quite common.
    The idea here is that the expression before -prune matches
    things which are to be pruned.  However, the -prune action
    itself returns true, so the following -o ensures that the
    right hand side is evaluated only for those directories which
    didn't get pruned (the contents of the pruned directories are
    not even visited, so their contents are irrelevant).  The
    expression on the right hand side of the -o is in parentheses
    only for clarity.  It emphasises that the -print0 action takes
    place only for things that didn't have -prune applied to them.
    Because the default `and' condition between tests binds more
    tightly than -o, this is the default anyway, but the
    parentheses help to show what is going on.

•   Given the following directory of projects and their associated
    SCM administrative directories, perform an efficient search
    for the projects' roots:

        $ find repo/ \
            \( -exec test -d '{}/.svn' \; \
            -or -exec test -d '{}/.git' \; \
            -or -exec test -d '{}/CVS' \; \
            \) -print -prune

    Sample directories:

        repo/project1/CVS
        repo/gnu/project2/.svn
        repo/gnu/project3/.svn
        repo/gnu/project3/src/.svn
        repo/project4/.git

    Output:

        repo/project1
        repo/gnu/project2
        repo/gnu/project3
        repo/project4

    In this example, -prune prevents unnecessary descent into
    directories that have already been discovered (here we do not
    search project3/src because we already found project3/.svn),
    but ensures sibling directories (project2 and project3) are
    found.

### Other useful examples

•   Search for several file types.

        $ find /tmp -type f,d,l

    Search for files, directories, and symbolic links in the
    directory /tmp passing these types as a comma-separated list
    (GNU extension), which is otherwise equivalent to the longer,
    yet more portable:

        $ find /tmp \( -type f -o -type d -o -type l \)

•   Search for files with the particular name needle and stop
    immediately when we find the first one.

        $ find / -name needle -print -quit

•   Demonstrate the interpretation of the %f and %h format
    directives of the -printf action for some corner-cases.  Here
    is an example including some output.

        $ find . .. / /tmp /tmp/TRACE compile compile/64/tests/find \
          -maxdepth 0 -printf '[%h][%f]\n'
        [.][.]
        [.][..]
        [][/]
        [][tmp]
        [/tmp][TRACE]
        [.][compile]
        [compile/64/tests][find]


## EXIT STATUS

find exits with status 0 if all files are processed successfully,
greater than 0 if errors occur.  This is deliberately a very broad
description, but if the return value is non-zero, you should not
rely on the correctness of the results of find.

When some error occurs, find may stop immediately, without
completing all the actions specified.  For example, some starting
points may not have been examined or some pending program
invocations for -exec ... {} + or -execdir ... {} + may not have
been performed.


## HISTORY

A find program appeared in Version 5 Unix as part of the
Programmer's Workbench project and was written by Dick Haight.
Doug McIlroy's A Research UNIX Reader: Annotated Excerpts from the
Programmer's Manual, 1971–1986 provides some additional details;
you can read it on-line at
<https://www.cs.dartmouth.edu/~doug/reader.pdf>.

GNU find was originally written by Eric Decker, with enhancements
by David MacKenzie, Jay Plett, and Tim Wood.  The idea for find
-print0 and xargs -0 came from Dan Bernstein.


## COMPATIBILITY

### Feature Additions

Feature                Added in   Year   Also occurs in
-files0-from           4.9.0      2022
-newerXY               4.3.3      2007   BSD
-D                     4.3.1      2006
-O                     4.3.1      2006
-readable              4.3.0      2005
-writable              4.3.0      2005
-executable            4.3.0      2005
-regextype             4.2.24     2004
-exec ... +            4.2.12     2005   POSIX
-execdir               4.2.12     2005   BSD
-okdir                 4.2.12     2005
-samefile              4.2.11     2004
-H                     4.2.5      2004   POSIX
-L                     4.2.5      2004   POSIX
-P                     4.2.5      2004   BSD
-delete                4.2.3      2004
-quit                  4.2.3      2004
-d                     4.2.3      2004   BSD
-wholename             4.2.0      2003
-iwholename            4.2.0      2003
-ignore_readdir_race   4.2.0      2003
-fls                   4.0        1994
-ilname                3.8        1993
-iname                 3.8        1993   POSIX (from Issue 8, IEEE Std 1003.1-2024)
-ipath                 3.8        1993
-iregex                3.8        1993
-print0                2.0        1990   POSIX (from Issue 8, IEEE Std 1003.1-2024)

### Functional Changes

Version   Year   Change
4.5.12    2013   The syntax -perm
                 +MODE is removed,
                 in favour of -perm
                 /MODE.  The +MODE
                 syntax had been
                 deprecated since
                 findutils-4.2.21
                 (2005).
4.3.11    2007   The -delete action
                 sets find's exit
                 status to a
                 nonzero value when
                 it fails.
                 However, find will
                 not exit
                 immediately.
                 Previously, find's
                 exit status was
                 unaffected by the
                 failure of
                 -delete.
4.3.3     2007   Nanosecond-
                 resolution
                 timestamps;
                 seconds fields are
                 no longer
                 integers.
4.3.3     2007   -perm /000 now
                 matches all files
                 instead of none.
4.2.2     2004   Shell
                 metacharacters
                 (`*', `?' or `[]'
                 for example) used
                 in filename
                 patterns match a
                 leading `.',
                 because IEEE POSIX
                 interpretation 126
                 requires this.


## NON-BUGS

### Operator precedence surprises

The command find . -name afile -o -name bfile -print will never
print afile because this is actually equivalent to find . -name
afile -o \( -name bfile -a -print \).  Remember that the
precedence of -a is higher than that of -o and when there is no
operator specified between tests, -a is assumed.

   “paths must precede expression” error message
$ find . -name *.c -print
find: paths must precede expression
find: possible unquoted pattern after predicate `-name'?

This happens when the shell could expand the pattern *.c to more
than one file name existing in the current directory, and passing
the resulting file names in the command line to find like this:
find . -name frcode.c locate.c word_io.c -print
That command is of course not going to work, because the -name
predicate allows exactly only one pattern as argument.  Instead of
doing things this way, you should enclose the pattern in quotes or
escape the wildcard, thus allowing find to use the pattern with
the wildcard during the search for file name matching instead of
file names expanded by the parent shell:
$ find . -name '*.c' -print
$ find . -name \*.c -print


## BUGS

There are security problems inherent in the behaviour that the
POSIX standard specifies for find, which therefore cannot be
fixed.  For example, the -exec action is inherently insecure, and
-execdir should be used instead.

The environment variable LC_COLLATE has no effect on the -ok
action.


## COPYRIGHT

Copyright © 1990–2026 Free Software Foundation, Inc.  License
GPLv3+: GNU GPL version 3 or later
<https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


## SEE ALSO

chmod(1), locate(1), ls(1), updatedb(1), xargs(1), lstat(2),
stat(2), ctime(3) fnmatch(3), printf(3), strftime(3), locatedb(5),
regex(7)

Full documentation <https://www.gnu.org/software/findutils/find>
or available locally via: info find
