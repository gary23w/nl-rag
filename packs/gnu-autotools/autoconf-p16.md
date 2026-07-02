---
title: "Autoconf (part 16/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 16/26
---

# Autoconf

**`basename`**

Long ago some hosts lacked a working `basename`, and portable scripts needed to use `expr` instead. Nowadays it is safe to use `basename`. For example:

```
base=`basename -- "$file"`
```

**`cat`**

Don’t rely on any option.

**`cc`**

The command ‘cc -c foo.c’ traditionally produces an object file named foo.o. Most compilers allow -c to be combined with -o to specify a different object file name, but POSIX does not require this combination and a few compilers lack support for it. See C Compiler Characteristics, for how GNU Make tests for this feature with `AC_PROG_CC_C_O`.

When a compilation such as ‘cc -o foo foo.c’ fails, some compilers (such as CDS on Reliant Unix) leave a foo.o.

HP-UX `cc` doesn’t accept .S files to preprocess and assemble. ‘cc -c foo.S’ appears to succeed, but in fact does nothing.

The default executable, produced by ‘cc foo.c’, can be

- a.out – usual POSIX convention.
- b.out – i960 compilers (including `gcc`).
- a.exe – DJGPP port of `gcc`.
- a_out.exe – GNV `cc` wrapper for DEC C on OpenVMS.
- foo.exe – various MS-DOS compilers.

The C compiler’s traditional name is `cc`, but other names like `gcc` are common. POSIX 1003.1-2024 specifies the name `c17`, but older POSIX editions specified `c99` or `c89`, future POSIX standards will likely specify other commands, and anyway these standard names are rarely used in practice. Typically the C compiler is invoked from makefiles that use ‘$(CC)’, so the value of the ‘CC’ make variable selects the compiler name.

**`chgrp`**

**`chown`**

It is not portable to change a file’s group to a group that the owner does not belong to.

**`chmod`**

Avoid usages like ‘chmod -w file’; use ‘chmod a-w file’ instead, for two reasons. First, plain -w does not necessarily make the file unwritable, since it does not affect mode bits that correspond to bits in the file mode creation mask. Second, POSIX says that the -w might be interpreted as an implementation-specific option, not as a mode; POSIX suggests using ‘chmod -- -w file’ to avoid this confusion, but unfortunately ‘--’ does not work on some older hosts.

**`cmp`**

`cmp` performs a raw data comparison of two files, while `diff` compares two text files. Therefore, if you might compare DOS files, even if only checking whether two files are different, use `diff` to avoid spurious differences due to differences of newline encoding.

**`cp`**

The -i, -f, -p and -R options are widely used. POSIX also specifies -H, -L, and -P. Avoid other options in portable scripts.

Traditionally, file timestamps had 1-second resolution, and ‘cp -p’ copied the timestamps exactly. However, many modern file systems have timestamps with 1-nanosecond resolution. Unfortunately, some older ‘cp -p’ implementations truncate timestamps when copying files, which can cause the destination file to appear to be older than the source. The exact amount of truncation depends on the resolution of the system calls that `cp` uses. Traditionally this was `utime`, which has 1-second resolution. Since GNU Core Utilities 6.12 (2008), GNU `cp` can set timestamps to the full nanosecond resolution, using the system calls `futimens` and `utimensat` when they are available. As of 2024, though, some platforms (such as AIX 7.3) still have ‘cp -p’ that supports only 1-second resolution, and some operating systems and file systems have similar limitations even when running GNU `cp`.

Although ‘cp -p’ always *tries* to copy ownerships, whether it actually does so is a system dependent policy decision implemented by the kernel. If the kernel allows it then it happens. If the kernel does not allow it then it does not happen. It is not something `cp` itself has control over.

In Unix System V any user can chown files to any other user, and System V also has a non-sticky /tmp. That probably derives from the heritage of System V in a business environment without hostile users. BSD changed this to be a more secure model where only root can `chown` files and a sticky /tmp is used. That undoubtedly derives from the heritage of BSD in a campus environment.

GNU/Linux and Solaris by default follow BSD, but can be configured to allow a System V style `chown`. On the other hand, HP-UX follows System V, but can be configured to use the modern security model and disallow `chown`. Since it is an administrator-configurable parameter you can’t use the name of the kernel as an indicator of the behavior.

**`date`**

When most versions of `date` do not recognize a ‘%’ conversion specification, they quietly pass it through, and exit with success:

```
$ date --version | head -n 1
date (GNU coreutils) 9.5
$ date +'%H:%M %Q'
17:25 %Q
```

However, this behavior is not required by POSIX.

**`dirname`**

Long ago some hosts lacked a working `dirname` and portable scripts needed to use use `AS_DIRNAME` (see Programming in M4sh). Nowadays `dirname` suffices and the following are equivalent:

```
dir=`dirname -- "$file"`
dir=`AS_DIRNAME(["$file"])`
```

**`egrep`**

Although POSIX stopped requiring `egrep` in 2001, a few traditional hosts (notably Solaris 11) do not support the POSIX replacement `grep -E`. Also, some traditional implementations do not work on long input lines. To work around these problems, invoke `AC_PROG_EGREP` and then use `$EGREP`.

Portable extended regular expressions should use ‘\’ only to escape characters in the string ‘$()*+.?[\^{|’. For example, ‘\}’ is not portable, even though it typically matches ‘}’.

The empty alternative is not portable. Use ‘?’ instead. For instance with Digital Unix v5.0:

```
> printf 'foo\n|foo\n' | $EGREP '^(|foo|bar)$'
|foo
> printf 'bar\nbar|\n' | $EGREP '^(foo|bar|)$'
bar|
> printf 'foo\nfoo|\n|bar\nbar\n' | $EGREP '^(foo||bar)$'
foo
|bar
```

For more information about what can appear in portable extended regular expressions, see Problematic Expressions in *GNU Grep*.

`$EGREP` also suffers the limitations of `grep` (see Limitations of Usual Tools).

**`expr`**

Not all implementations obey the POSIX rule that ‘--’ separates options from arguments; likewise, not all implementations provide the extension to POSIX that the first argument can be treated as part of a valid expression rather than an invalid option if it begins with ‘-’. When performing arithmetic, use ‘expr 0 + $var’ if ‘$var’ might be a negative number, to keep `expr` from interpreting it as an option.

No `expr` keyword starts with ‘X’, so use ‘expr X"*word*" : 'X*regex*'’ to keep `expr` from misinterpreting *word*.

Don’t use `length`, `substr`, `match` and `index`.

**`expr` (‘|’) ¶**

You can use ‘|’. Although POSIX does require that ‘expr ''’ return the empty string, it does not specify the result when you ‘|’ together the empty string (or zero) with the empty string. For example:

```
expr '' \| ''
```

POSIX 1003.2-1992 returns the empty string for this case, but traditional Unix returns ‘0’ (Solaris is one such example). In POSIX 1003.1-2001, the specification was changed to match traditional Unix’s behavior (which is bizarre, but it’s too late to fix this). Please note that the same problem does arise when the empty string results from a computation, as in:

```
expr bar : foo \| foo : bar
```

Avoid this portability problem by avoiding the empty string.

**`expr` (‘:’)**

Portable `expr` regular expressions should use ‘\’ to escape only characters in the string ‘$()*.123456789[\^{}’. For example, alternation, ‘\|’, is common but POSIX does not require its support, so it should be avoided in portable scripts. Similarly, ‘\+’ and ‘\?’ should be avoided.

Portable `expr` regular expressions should not begin with ‘^’. Patterns are automatically anchored so leading ‘^’ is not needed anyway.

On the other hand, the behavior of the ‘$’ anchor is not portable on multi-line strings. POSIX is ambiguous whether the anchor applies to each line, as was done in older versions of the GNU Core Utilities, or whether it applies only to the end of the overall string, as in Coreutils 6.0 and most other implementations.

```
$ baz='foo
> bar'
$ expr "X$baz" : 'X\(foo\)$'

$ expr-5.97 "X$baz" : 'X\(foo\)$'
foo
```

The POSIX standard is ambiguous as to whether ‘expr 'a' : '\(b\)'’ outputs ‘0’ or the empty string. In practice, it outputs the empty string on most platforms, but portable scripts should not assume this. For instance, the QNX 4.25 native `expr` returns ‘0’.

One might think that a way to get a uniform behavior would be to use the empty string as a default value:

```
expr a : '\(b\)' \| ''
```

Unfortunately this behaves exactly as the original expression; see the `expr` (‘|’) entry for more information.

Some ancient `expr` implementations (e.g., Solaris 10 `/usr/ucb/expr`) have a silly length limit that causes `expr` to fail if the matched substring is longer than 120 bytes. In this case, you might want to fall back on ‘printf|sed’ if `expr` fails. Nowadays this is of practical importance only for the rare installer who mistakenly puts /usr/ucb before /usr/bin in `PATH` on Solaris 10.

On Mac OS X 10.4, `expr` mishandles the pattern ‘[^-]’ in some cases. For example, the command

```
expr Xpowerpc-apple-darwin8.1.0 : 'X[^-]*-[^-]*-\(.*\)'
```

outputs ‘apple-darwin8.1.0’ rather than the correct ‘darwin8.1.0’. This particular case can be worked around by substituting ‘[^--]’ for ‘[^-]’.

Don’t leave, there is some more!

The QNX 4.25 `expr`, in addition of preferring ‘0’ to the empty string, has a funny behavior in its exit status: it’s always 1 when parentheses are used!

```
$ val=`expr 'a' : 'a'`; echo "$?: $val"
0: 1
$ val=`expr 'a' : 'b'`; echo "$?: $val"
1: 0

$ val=`expr 'a' : '\(a\)'`; echo "?: $val"
1: a
$ val=`expr 'a' : '\(b\)'`; echo "?: $val"
1: 0
```

In practice this can be a big problem if you are ready to catch failures of `expr` programs with some other method (such as using `sed`), since you may get twice the result. For instance

```
$ expr 'a' : '\(a\)' || echo 'a' | sed 's/^\(a\)$/\1/'
```

outputs ‘a’ on most hosts, but ‘aa’ on QNX 4.25. A simple workaround consists of testing `expr` and using a variable set to `expr` or to `false` according to the result.

On HP-UX 11, `expr` supports only a single sub-expression.

```
$ expr 'Xfoo' : 'X\(f\(oo\)*\)$'
expr: More than one '\(' was used.
```

**`fgrep`**

Although POSIX stopped requiring `fgrep` in 2001, a few traditional hosts (notably Solaris 11) do not support the POSIX replacement `grep -F`. Also, some traditional implementations do not work on long input lines. To work around these problems, invoke `AC_PROG_FGREP` and then use `$FGREP`.

**`find`**

Many operands of GNU `find` are not standardized by POSIX and are missing on many platforms. These nonportable operands include -follow, -maxdepth, -mindepth, -printf, and ,. See the POSIX spec for `find` for `find` operands that should be portable nowadays.

The replacement of ‘{}’ is guaranteed only if the argument is exactly ‘{}’, not if ‘{}’ only a part of a larger argument. For instance, on AIX 7.3:

```
$ touch foo
$ find . -name foo -exec echo '{}-{}' \;
{}-{}
```

while GNU `find` reports ‘./foo-./foo’. POSIX allows either behavior.

AIX 7.3 ‘find ... -exec *command* +’ incorrectly fails if *command* is not executed. For example, ‘find . -name '*.tmp' -exec rm {} +’ incorrectly outputs a diagnostic and fails if no file names end in ‘.tmp’. To work around this problem you can use a circumlocution like ‘find . -name '*.tmp' -exec rm -f {} + -o -exec true ';'’.

**`grep`**

Portable scripts can rely on the `grep` options -c, -l, -n, and -v, but should avoid other options. For example, don’t use -w, as POSIX does not require it. Also, portable scripts should not combine -c with -l, as POSIX does not allow this.

Some of the options required by POSIX are not portable in practice. Don’t use ‘grep -q’ to suppress output, because traditional `grep` implementations (e.g., Solaris 10) do not support -q. Don’t use ‘grep -s’ to suppress output either, because POSIX says -s does not suppress output, only some error messages; also, the -s option of traditional `grep` behaved like -q does in most modern implementations. Instead, redirect the standard output and standard error (in case the file doesn’t exist) of `grep` to /dev/null. Check the exit status of `grep` to determine whether it found a match.

The QNX4 implementation fails to count lines with `grep -c '$'`, but works with `grep -c '^'`. Other alternatives for counting lines are to use `sed -n '$='` or `wc -l`.

Some traditional `grep` implementations do not work on long input lines. On AIX the default `grep` silently truncates long lines on the input before matching.

Also, Solaris 11 `grep` does not support -e. To work around this, invoke `AC_PROG_GREP` and then use `$GREP`.

Another possible workaround for the multiple -e problem is to separate the patterns by newlines, for example:

```
grep 'foo
bar' in.txt
```

except that this fails with traditional `grep` implementations and with OpenBSD 3.8 `grep`.

Traditional `grep` implementations (e.g., Solaris 11) do not support the -E or -F options. To work around these problems, invoke `AC_PROG_EGREP` and then use `$EGREP`, and similarly for `AC_PROG_FGREP` and `$FGREP`. Even if you are willing to require support for POSIX `grep`, your script should not use both -E and -F, since POSIX does not allow this combination.

Portable `grep` regular expressions should use ‘\’ only to escape characters in the string ‘$()*.123456789[\^{}’. For example, alternation, ‘\|’, is common but POSIX does not require its support in basic regular expressions, so it should be avoided in portable scripts. Solaris and HP-UX `grep` do not support it. Similarly, the following escape sequences should also be avoided: ‘\<’, ‘\>’, ‘\+’, ‘\?’, ‘\`’, ‘\'’, ‘\B’, ‘\b’, ‘\S’, ‘\s’, ‘\W’, and ‘\w’. For more information about what can appear in portable regular expressions, see Problematic Expressions in *GNU Grep*.

POSIX does not specify the behavior of `grep` on binary files. An example where this matters is using BSD `grep` to search text that includes embedded ANSI escape sequences for colored output to terminals (‘\033[m’ is the sequence to restore normal output); the behavior depends on whether input is seekable:

```
$ printf 'esc\033[mape\n' > sample
$ grep . sample
Binary file sample matches
$ cat sample | grep .
escape
```

**`join`**

On NetBSD, `join -a 1 file1 file2` mistakenly behaves like `join -a 1 -a 2 1 file1 file2`, resulting in a usage warning; the workaround is to use `join -a1 file1 file2` instead.

On some circa-2020 BSD-based systems `join` mishandles inputs with missing fields. For example, an empty line is not treated as containing an empty join field. As a workaround, input lines should always have a join field.

On platforms with the BusyBox tools, the `join` command is entirely missing. As a workaround, you can simulate special cases of the `join` command using an `awk` script. For an example, see https://lists.gnu.org/r/bug-gnulib/2021-04/msg00054.html.

**`ln`**

The -f option is portable nowadays.

Symbolic links are not available on some systems; use ‘$(LN_S)’ as a portable substitute.

For versions of the DJGPP before 2.04, `ln` emulates symbolic links to executables by generating a stub that in turn calls the real program. This feature also works with nonexistent files like in the POSIX spec. So ‘ln -s file link’ generates link.exe, which attempts to call file.exe if run. But this feature only works for executables, so ‘cp -p’ is used instead for these systems. DJGPP versions 2.04 and later have full support for symbolic links.

**`ls`**

The portable options are -acdilrtu. Current practice is for -l to output both owner and group, even though ancient versions of `ls` omitted the group.

On ancient hosts, ‘ls foo’ sent the diagnostic ‘foo not found’ to standard output if foo did not exist. Hence a shell command like ‘sources=`ls *.c 2>/dev/null`’ did not always work, since it was equivalent to ‘sources='*.c not found'’ in the absence of ‘.c’ files. This is no longer a practical problem, since current `ls` implementations send diagnostics to standard error.

The behavior of `ls` on a directory that is being concurrently modified is not always predictable, because of a data race where cached information returned by `readdir` does not match the current directory state. In fact, Mac OS X 10.5 had an intermittent bug where `readdir`, and thus `ls`, sometimes lists a file more than once if other files were added or removed from the directory immediately prior to the `ls` call. Since `ls` already sorts its output, the duplicate entries can be avoided by piping the results through `uniq`.

**`mkdir`**

Combining the -m and -p options, as in ‘mkdir -m go-w -p *dir*’, often leads to trouble. FreeBSD `mkdir` incorrectly attempts to change the permissions of *dir* even if it already exists. HP-UX 11.23 `mkdir` often assigns the wrong permissions to any newly-created parents of *dir*.

POSIX does not clearly specify whether ‘mkdir -p foo’ should succeed when foo is a symbolic link to an already-existing directory. The GNU `mkdir` succeeds, but Solaris 10 `mkdir` fails.

Traditional `mkdir -p` implementations suffer from race conditions. For example, if you invoke `mkdir -p a/b` and `mkdir -p a/c` at the same time, both processes might detect that a is missing, one might create a, then the other might try to create a and fail with a `File exists` diagnostic. Solaris 10 `mkdir` is vulnerable, and other traditional Unix systems are probably vulnerable too. This possible race is harmful in parallel builds when several Make rules call `mkdir -p` to construct directories. You may use `install-sh -d` as a safe replacement, for example by setting ‘MKDIR_P='/path/to/install-sh -d'’ in the environment of `configure`, assuming the package distributes install-sh.

**`mkfifo`**

**`mknod`**

The GNU Coding Standards state that `mknod` is safe to use on platforms where it has been tested to exist; but it is generally portable only for creating named FIFOs, since device numbers are platform-specific. Autotest uses `mkfifo` to implement parallel testsuites. POSIX states that behavior is unspecified when opening a named FIFO for both reading and writing; on at least Cygwin, this results in failure on any attempt to read or write to that file descriptor.

**`mktemp`**

Shell scripts can use temporary files safely with `mktemp`, but it does not exist on all systems. A portable way to create a safe temporary file name is to create a temporary directory with mode 700 and use a file inside this directory. Both methods prevent attackers from gaining control, though `mktemp` is far less likely to fail gratuitously under attack.

Here is sample code to create a new temporary directory ‘$dir’ safely:

```
# Create a temporary directory $dir in $TMPDIR (default /tmp).
# Use mktemp if possible; otherwise fall back on mkdir,
# with $RANDOM to make collisions less likely.
: "${TMPDIR:=/tmp}"
{
  dir=`
    (umask 077 && mktemp -d "$TMPDIR/fooXXXXXX") 2>/dev/null
  ` &&
  test -d "$dir"
} || {
  dir=$TMPDIR/foo$$-$RANDOM
  (umask 077 && mkdir "$dir")
} || exit $?
```

**`mv`**

The only portable options are -f and -i.

Moving individual files between file systems is portable (it was in Unix version 6), but it is not always atomic: when doing ‘mv new existing’, there’s a critical section where neither the old nor the new version of existing actually exists.

On some systems moving files from /tmp can sometimes cause undesirable (but perfectly valid) warnings, even if you created these files. This is because /tmp belongs to a group that ordinary users are not members of, and files created in /tmp inherit the group of /tmp. When the file is copied, `mv` issues a diagnostic without failing:

```
$ touch /tmp/foo
$ mv /tmp/foo .
error→mv: ./foo: set owner/group (was: 100/0): Operation not permitted
$ echo $?
0
$ ls foo
foo
```

This annoying behavior conforms to POSIX, unfortunately.

Moving directories across mount points is not portable, use `cp` and `rm`.

DOS variants cannot rename or remove open files, and do not support commands like ‘mv foo bar >foo’, even though this is perfectly portable among POSIX hosts.

**`od`**

In Mac OS X versions prior to 10.4.3, `od` does not support the standard POSIX options -A, -j, -N, or -t, or the XSI option, -s. The only supported POSIX option is -v, and the only supported XSI options are those in -bcdox. The BSD `hexdump` program can be used instead.

In some versions of some operating systems derived from Solaris 11, `od` prints decimal byte values padded with zeros rather than with spaces:

```
$ printf '#!' | od -A n -t d1 -N 2
         035 033
```

instead of

```
$ printf '#!' | od -A n -t d1 -N 2
          35  33
```

We have observed this on both OpenIndiana and OmniOS; Illumos may also be affected. As a workaround, you can use octal output (option `-t o1`).

**`rm`**

The -f and -r options are portable.

It is not portable to invoke `rm` without options or operands. On the other hand, POSIX now requires `rm -f` to silently succeed when there are no operands (useful for constructs like `rm -rf $filelist` without first checking if ‘$filelist’ was empty). But this was not always portable; at least NetBSD `rm` built before 2008 would fail with a diagnostic.

A file might not be removed even if its parent directory is writable and searchable. Many POSIX hosts cannot remove a mount point, a named stream, a working directory, or a last link to a file that is being executed.

DOS variants cannot rename or remove open files, and do not support commands like ‘rm foo >foo’, even though this is perfectly portable among POSIX hosts.

**`rmdir`**

Just as with `rm`, some platforms refuse to remove a working directory.

**`sed`**

The portable options are -e, -f, and -n. POSIX standardized -E in 2024 but some older implementations lack it. Although GNU `sed` supports other options like -i, these can be missing or have different meanings elsewhere.

Patterns should not include the separator (unless escaped), even as part of a character class. Even when escaped, patterns should not include separators that are also used as `sed` metacharacters. For example, GNU sed 4.0.9 rejects ‘s,x\{1\,\},,’, while sed 4.1 strips the backslash before the comma before evaluating the basic regular expression.

Avoid empty patterns, such as the parenthesized empty pattern in ‘\(\)’ or the empty pattern followed by an interval expression in ‘\{2\}’. POSIX does not require support for empty patterns.

Comments in Sed scripts should not contain ‘n’ immediately after the leading ‘#’. Although POSIX.1-2024 says this is equivalent to the -n option, earlier POSIX editions said that the equivalence occurs only if the comment is the first line of the script, and many `sed` implementations are confused about this. It is more portable to use -n.

HP-UX sed has a limit of 99 commands (not counting ‘:’ commands) and 48 labels, which cannot be circumvented by using more than one script file. It can execute up to 19 reads with the ‘r’ command per cycle. Solaris 10 `/usr/ucb/sed` rejects usages that exceed a limit of about 6000 bytes for the internal representation of commands.

Some `sed` implementations have a buffer limited to 4000 bytes, and this limits the size of input lines, output lines, and internal buffers that can be processed portably. Likewise, not all `sed` implementations can handle embedded `NUL` or a missing trailing newline.

Ranges within a bracket expression of a regular expression are only well-defined in the ‘C’ (or ‘POSIX’) locale. Meanwhile, support for character classes like ‘[[:upper:]]’ is not yet universal, so if you cannot guarantee the setting of `LC_ALL`, it is better to spell out a range ‘[ABCDEFGHIJKLMNOPQRSTUVWXYZ]’ than to rely on ‘[A-Z]’.

Additionally, POSIX states that regular expressions are only well-defined on characters. Unfortunately, there exist platforms such as Mac OS X 10.5 where not all 8-bit byte values are valid characters, even though that platform has a single-byte ‘C’ locale. Although this practice was disallowed by recent releases of POSIX, it means that in the ‘C’ locale not all bytes will be matched by the regular expression ‘.’:

```
$ printf '\200\n' | LC_ALL=C sed -n /./p | wc -l
0
$ printf '\200\n' | LC_ALL=en_US.ISO8859-1 sed -n /./p | wc -l
1
```

Anchors (‘^’ and ‘$’) inside groups are not portable.

Some `sed` implementations, e.g., Solaris 11.4, restrict the special role of the asterisk ‘*’ to one-character regular expressions and back-references, and the special role of interval expressions ‘\{*m*\}’, ‘\{*m*,\}’, or ‘\{*m*,*n*\}’ to one-character regular expressions. This may lead to unexpected behavior:

```
$ echo '1*23*4' | /usr/bin/sed 's/\(.\)*/x/g'
x2x4
$ echo '1*23*4' | /usr/xpg4/bin/sed 's/\(.\)*/x/g'
x
```

In the normal case when -E is not used, portable `sed` regular expressions should use ‘\’ only to escape characters in the string ‘$*.123456789[\^n’. For example, POSIX.1-2024 says it is implementation-defined whether ‘\|’ means alternation or simply matches ‘|’, so it should be avoided in portable scripts. Solaris `sed` does not support alternation; e.g., ‘sed '/a\|b/d'’ deletes only lines that contain the literal string ‘a|b’. Similarly, ‘\+’ and ‘\?’ should be avoided.

Portable `sed` replacement strings should use ‘\’ only to escape the delimiter character, newline, and characters in the string ‘&123456789\’. For example, although in GNU `sed` the command ‘s/AB/\n/’ replaces the first ‘AB’ with a newline, in OpenBSD and Solaris `sed` it acts like ‘s/AB/n/’. To be portable, escape a newline instead:

```
# This is portable; "sed 's/AB/\n/'" is not.
sed 's/AB/\
/'
```

The -e option is mostly portable. However, its argument cannot be empty, as this fails on AIX 7.3. Some people prefer to use ‘-e’:

```
sed -e 'command-1' \
    -e 'command-2'
```

as opposed to the equivalent:

```
sed '
  command-1
  command-2
'
```

The following usage is sometimes equivalent:

```
sed 'command-1;command-2'
```

but POSIX says that this use of a semicolon has undefined effect if *command-1*’s verb is ‘{’, ‘a’, ‘b’, ‘c’, ‘i’, ‘r’, ‘t’, ‘w’ or ‘:’, or if *command-1* is an ‘s’ with the ‘w’ option, so you should use semicolon only with simple scripts that do not use these constructs.

Avoid redundant ‘;’, as some `sed` implementations, such as NetBSD 1.4.2’s, incorrectly try to interpret the second ‘;’ as a command:

```
$ echo a | sed 's/x/x/;;s/x/x/'
sed: 1: "s/x/x/;;s/x/x/": invalid command code ;
```

POSIX requires each -e and -f option to specify a syntactically complete script. Although GNU `sed` also allows -e and -f options to specify script fragments that it assembles into a full script, this is not portable. For example, the `sed` programs on Solaris 11, HP-UX 11, and AIX do not allow script fragments:

```
$ sed -e 'i\' -e ouch
Unrecognized command: ouch
```

In practice, however, this technique of joining fragments through -e works for multiple `sed` functions within ‘{’ and ‘}’, even if that is not specified by POSIX:

```
$ echo a | sed -n -e '/a/{' -e s/a/b/ -e p -e '}'
b
```

Commands should not be followed by white space. Although trailing white space often works, it can be dicey in some situations and it is simpler to avoid it entirely.

Commands inside { } brackets are further restricted. POSIX.1-2004 says that they cannot be preceded by addresses, ‘!’, or ‘;’, and that each command must be followed immediately by a newline, without any intervening blanks or semicolons. The closing bracket must be alone on a line, other than white space preceding or following it. Although these restrictions were lifted in POSIX.1-2008, it is more portable to respect them.

Contrary to yet another urban legend, you may portably use ‘&’ in the replacement part of the `s` command to mean “what was matched”. All descendants of Unix version 7 `sed` (at least; we don’t have first hand experience with older `sed` implementations) have supported it.

POSIX requires that you must not have any white space between ‘!’ and the following command. It is OK to have blanks between the address and the ‘!’. For instance, on Solaris:

```
$ echo "foo" | sed -n '/bar/ ! p'
error→Unrecognized command: /bar/ ! p
$ echo "foo" | sed -n '/bar/! p'
error→Unrecognized command: /bar/! p
$ echo "foo" | sed -n '/bar/ !p'
foo
```

POSIX also says that you should not combine ‘!’ and ‘;’. If you use ‘!’, it is best to put it on a command that is delimited by newlines rather than ‘;’.

POSIX requires that the ‘b’, ‘t’, ‘r’, and ‘w’ commands be followed by exactly one space before their argument. On the other hand, no white space is allowed between ‘:’ and the subsequent label. Branch labels should contain at most 8 bytes, each of which should be an ASCII graphical character. Do not put trailing white space after a branch label.

If a sed script is specified on the command line and ends in an ‘a’, ‘c’, or ‘i’ command, the last line of inserted text should be followed by a newline. Otherwise some `sed` implementations (e.g., OpenBSD 3.9) do not append a newline to the inserted text.

Many `sed` implementations (e.g., Mac OS X 10.4, OpenBSD 3.9, Solaris 11 `/usr/ucb/sed`) strip leading white space from the text of ‘a’, ‘c’, and ‘i’ commands. Prepend a backslash to work around this incompatibility with POSIX:

```
$ echo flushleft | sed 'a\
>    indented
> '
flushleft
indented
$ echo foo | sed 'a\
> \   indented
> '
flushleft
   indented
```

POSIX requires that with a missing regular expression, the last regular expression from either an address specification or substitution command is used. However, busybox 1.6.1 complains when using a substitution command with a replacement containing a back-reference to a missing regular expression; the workaround is repeating the regular expression.

```
$ echo abc | busybox sed '/a\(b\)c/ s//\1/'
sed: No previous regexp.
$ echo abc | busybox sed '/a\(b\)c/ s/a\(b\)c/\1/'
b
```

Portable scripts should be aware of the inconsistencies and options for handling word boundaries, as these are not specified by POSIX.

```
                \<      \b      [[:<:]]
Solaris 11      yes     no      no
Solaris XPG4    yes     no      error
NetBSD 5.1      no      no      yes
FreeBSD 9.1     no      no      yes
GNU             yes     yes     error
busybox         yes     yes     error
```

**`sed` (‘t’)**

There are two things one should remember about ‘t’ in `sed`. First, ‘t’ jumps if *some* substitution succeeded, not only the immediately preceding substitution. Therefore, always use a fake ‘t clear’ followed by a ‘:clear’ on the next line, to reset the ‘t’ flag where needed.

Second, do not rely on `sed` to clear the flag at each new cycle.

For example, the following script replaces all instances of “keep me” with “kept”, and replaces the contents of all lines that did not contain “keep me” with “deleted”.

```
t clear
:clear
s/keep me/kept/g
t end
s/.*/deleted/g
:end
```

**`sed` (‘w’)**

When a script contains multiple commands to write lines to the same output file, BusyBox `sed` mistakenly opens a separate output stream for each command. This can cause one of the commands to “win” and the others to “lose”, in the sense that their output is discarded. For example:

```
sed -n -e '
  /a/w xxx
  /b/w xxx
' <<EOF
a
b
EOF
```

This might output only ‘a’ to xxx; the ‘b’ is lost. To avoid the problem, a portable script should contain at most one ‘w’ or ‘s/.../.../w’ command per output file.

**`sleep`**

Using `sleep` is generally portable. However, remember that adding a `sleep` to work around timestamp issues, with a minimum granularity of one second, doesn’t scale well for parallel builds on modern machines with sub-second process completion.

**`sort`**

Remember that sort order is influenced by the current locale. Inside configure, the C locale is in effect, but in Makefile snippets, you may need to specify `LC_ALL=C sort`.

**`tar`**

There are multiple file formats for `tar`; if you use Automake, the macro `AM_INIT_AUTOMAKE` has some options controlling which level of portability to use.

**`touch`**

If you specify the desired timestamp (e.g., with the -r option), older `touch` implementations use the `utime` or `utimes` system call, which can result in the same kind of timestamp truncation problems that ‘cp -p’ has.

**`tr`**

Many `tr` implementations do not support multi-byte locales well. For example, Solaris 10 `tr` rejects character classes in multi-byte locales. Also, ranges have well-defined behavior only in the ‘C’ (or ‘POSIX’) locale, so if you cannot guarantee the setting of `LC_ALL` it is better to spell out a range ‘[ABCDEFGHIJKLMNOPQRSTUVWXYZ]’ than to rely on ‘[A-Z]’.

Not all versions of `tr` handle all backslash character escapes. For example, Solaris 10 `/usr/ucb/tr` falls over, even though Solaris contains more modern `tr` in other locations. Using octal escapes is more portable for carriage returns, since ‘\015’ is the same for both ASCII and EBCDIC, and since use of literal carriage returns in scripts causes a number of other problems. But for other characters, like newline, using octal escapes ties the operation to ASCII, so it is better to use literal characters.

```
$ { echo moon; echo light; } | /usr/ucb/tr -d '\n' ; echo
moo
light
$ { echo moon; echo light; } | /usr/bin/tr -d '\n' ; echo
moonlight
$ { echo moon; echo light; } | /usr/ucb/tr -d '\012' ; echo
moonlight
$ nl='
'; { echo moon; echo light; } | /usr/ucb/tr -d "$nl" ; echo
moonlight
```

Not all versions of `tr` recognize direct ranges of characters: at least Solaris `/usr/bin/tr` still fails to do so. But you can use `/usr/xpg4/bin/tr` instead, or add brackets (which in POSIX transliterate to themselves).

```
$ echo "Hazy Fantazy" | LC_ALL=C /usr/bin/tr a-z A-Z
HAZy FAntAZy
$ echo "Hazy Fantazy" | LC_ALL=C /usr/bin/tr '[a-z]' '[A-Z]'
HAZY FANTAZY
$ echo "Hazy Fantazy" | LC_ALL=C /usr/xpg4/bin/tr a-z A-Z
HAZY FANTAZY
```

When providing two arguments, be sure the second string is at least as long as the first.

```
$ echo abc | /usr/xpg4/bin/tr bc d
adc
$ echo abc | coreutils/tr bc d
add
```

On platforms with the BusyBox tools, `tr` does not support the `[*x***n*]` option syntax.

```
$ echo abc | tr 'abcd' '[A*4]'
[A*
$ echo abc | coreutils/tr 'abcd' '[A*4]'
AAA
$ echo xyz | tr 'a-z' '[A*]'
]]]
$ echo xyz | coreutils/tr 'a-z' '[A*]'
AAA
```

POSIX requires `tr` to operate on binary files. But at least Solaris `/usr/ucb/tr` and `/usr/bin/tr` silently discard `NUL` in the input prior to doing any translation. When using `tr` to process a binary file that may contain `NUL` bytes, it is necessary to use `/usr/xpg4/bin/tr` instead, or `/usr/xpg6/bin/tr` if that is available.

```
$ printf 'a\0b' | /usr/ucb/tr x x | od -An -tx1
 61 62
$ printf 'a\0b' | /usr/bin/tr x x | od -An -tx1
 61 62
$ printf 'a\0b' | /usr/xpg4/bin/tr x x | od -An -tx1
 61 00 62
```

Solaris `/usr/ucb/tr` additionally fails to handle ‘\0’ as the octal escape for `NUL`.

```
$ printf 'abc' | /usr/ucb/tr 'bc' '\0d' | od -An -tx1
 61 62 63
$ printf 'abc' | /usr/bin/tr 'bc' '\0d' | od -An -tx1
 61 00 64
$ printf 'abc' | /usr/xpg4/bin/tr 'bc' '\0d' | od -An -tx1
 61 00 64
```
