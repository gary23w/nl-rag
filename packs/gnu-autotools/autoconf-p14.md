---
title: "Autoconf (part 14/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 14/26
---

## 11 Portable Shell Programming

When writing your own checks, there are some shell-script programming techniques you should avoid in order to make your code portable. The Bourne shell and upward-compatible shells like the Korn shell and Bash have evolved over the years, and many features added to the original System7 shell are now supported on all interesting porting targets. However, the following discussion between Russ Allbery and Robert Lipe is worth reading:

Russ Allbery:

> The GNU assumption that `/bin/sh` is the one and only shell leads to a permanent deadlock. Vendors don’t want to break users’ existing shell scripts, and there are some corner cases in the Bourne shell that are not completely compatible with a POSIX shell. Thus, vendors who have taken this route will *never* (OK…“never say never”) replace the Bourne shell (as `/bin/sh`) with a POSIX shell.

Robert Lipe:

> This is exactly the problem. While most (at least most System V’s) do have a Bourne shell that accepts shell functions most vendor `/bin/sh` programs are not the POSIX shell.
> 
> So while most modern systems do have a shell *somewhere* that meets the POSIX standard, the challenge is to find it.

For this reason, part of the job of M4sh (see Programming in M4sh) is to find such a shell. But to prevent trouble, if you’re not using M4sh you should not take advantage of features that were added after Unix version 7, circa 1977 (see Systemology); you should not use aliases, negated character classes, or even `unset`. `#` comments, while not in Unix version 7, were retrofitted in the original Bourne shell and can be assumed to be part of the least common denominator.

On the other hand, if you’re using M4sh you can assume that the shell has the features that were added in SVR2 (circa 1984), including shell functions, `return`, `unset`, and I/O redirection for builtins. For more information, refer to https://www.in-ulm.de/~mascheck/bourne/. However, some pitfalls have to be avoided for portable use of these constructs; these will be documented in the rest of this chapter. See in particular Shell Functions and Limitations of Shell Builtins.

The set of external programs you should run in a `configure` script is fairly small. See Utilities in Makefiles in *The GNU Coding Standards*, for the list. This restriction allows users to start out with a fairly small set of programs and build the rest, avoiding too many interdependencies between packages.

Some of these external utilities have a portable subset of features; see Limitations of Usual Tools.

There are other sources of documentation about shells. The specification for the POSIX Shell Command Language, though more generous than the restrictive shell subset described above, is fairly portable nowadays. Also please see the Shell FAQs.

### 11.1 Systemology

This section aims at presenting some systems and pointers to documentation. It may help you addressing particular problems reported by users.

POSIX-conforming systems are derived from the Unix operating system.

The Rosetta Stone for Unix contains a table correlating the features of various POSIX-conforming systems. Unix History is a simplified diagram of how many Unix systems were derived from each other.

The Heirloom Project provides some variants of traditional implementations of Unix utilities.

**Darwin ¶**

Darwin is a partially proprietary operating system maintained by Apple Computer and used by most of their products. It is also known as macOS, iOS, etc. depending on the exact variant. Older versions were called “Mac OS X.”

By default the file system will be case insensitive, albeit case preserving. This can cause nasty problems: for instance, the installation attempt for a package having an INSTALL file can result in ‘make install’ reporting that nothing is to be done!

Darwin does support case-sensitive file systems, but they must be formatted specially as such, and Apple discourages use of a case-sensitive volume for the base operating system. To build software that expects case-sensitive filenames, it is best to create a separate disk volume or disk image formatted as case sensitive; this can be done using the `diskutil` command or the Disk Utility application.

**QNX ¶**

QNX is a realtime operating system running on Intel architecture meant to be scalable from the small embedded systems to the hundred processor super-computer. More information is available on the QNX home page.

**Unix version 7 ¶**

Officially this was called the “Seventh Edition” of “the UNIX time-sharing system” but we use the more-common name “Unix version 7”. Documentation is available in the Unix Seventh Edition Manual. Previous versions of Unix are called “Unix version 6”, etc., but they were not as widely used.

### 11.2 Shellology

There are several families of shells, most prominently the Bourne family and the C shell family which are deeply incompatible. If you want to write portable shell scripts, avoid members of the C shell family. The the Shell difference FAQ includes a small history of POSIX shells, and a comparison between several of them.

Below we describe some of the members of the Bourne shell family.

**Ash ¶**

Ash is often used on GNU/Linux and BSD systems as a light-weight Bourne-compatible shell. Ash 0.2 has some bugs that are fixed in the 0.3.x series, but portable shell scripts should work around them, since version 0.2 is still shipped with many GNU/Linux distributions.

To be compatible with Ash 0.2:

- don’t use ‘$?’ after expanding empty or unset variables, or at the start of an `eval`: foo= false $foo echo "Do not use it: $?" false eval 'echo "Do not use it: $?"'
- don’t use command substitution within variable expansion: cat ${FOO=`bar`}
- beware that single builtin substitutions are not performed by a subshell, hence their effect applies to the current shell! See Shell Substitutions, item “Command Substitution”.

**Bash ¶**

To detect whether you are running Bash, test whether `BASH_VERSION` is set. To require POSIX compatibility, run ‘set -o posix’. See Bash POSIX Mode in *The GNU Bash Reference Manual*, for details.

**Bash 2.05 and later ¶**

Versions 2.05 and later of Bash use a different format for the output of the `set` builtin, designed to make evaluating its output easier. However, this output is not compatible with earlier versions of Bash (or with many other shells, probably). So if you use Bash 2.05 or higher to execute `configure`, you’ll need to use Bash 2.05 for all other build tasks as well.

**Ksh ¶**

The Korn shell is compatible with the Bourne family and it mostly conforms to POSIX. It has two major variants commonly called ‘ksh88’ and ‘ksh93’, named after the years of initial release. It is usually called `ksh`, but is called `sh` on some hosts if you set your path appropriately.

On Solaris 11, `/bin/sh` and `/usr/bin/ksh` are both ‘ksh93’. On Solaris 10 and earlier, `/bin/sh` is a pre-POSIX Bourne shell and the Korn shell is found elsewhere: `/usr/bin/ksh` is ‘ksh88’ on Solaris 10, `/usr/xpg4/bin/sh` is a POSIX-compliant variant of ‘ksh88’ on Solaris 10 and later, and `/usr/dt/bin/dtksh` is ‘ksh93’. Variants that are not standard may be parts of optional packages. There is no extra charge for these packages, but they are not part of a minimal OS install and therefore some installations may not have it.

**Pdksh ¶**

A public-domain clone of the Korn shell called `pdksh` is widely available: it has most of the ‘ksh88’ features along with a few of its own. It usually sets `KSH_VERSION`, except if invoked as `/bin/sh` on OpenBSD, and similarly to Bash you can require POSIX compatibility by running ‘set -o posix’. Unfortunately, with `pdksh` 5.2.14 (the latest stable version as of 2025) POSIX mode is buggy and causes `pdksh` to depart from POSIX in at least one respect, see Shell Substitutions.

**Zsh ¶**

To detect whether you are running `zsh`, test whether `ZSH_VERSION` is set. By default `zsh` is *not* compatible with the Bourne shell: you must execute ‘emulate sh’, and for `zsh` versions before 3.1.6-dev-18 you must also set `NULLCMD` to ‘:’. See Compatibility in *The Z Shell Manual*, for details.

The default Mac OS X `sh` was originally Zsh; it was changed to Bash in Mac OS X 10.2 (2002) and changed back to Zsh in macOS 10.15 (2019).

### 11.3 Invoking the Shell

The Korn shell (up to at least version M-12/28/93d) has a bug when invoked on a file whose name does not contain a slash. It first searches for the file’s name in `PATH`, and if found it executes that rather than the original file. For example, assuming there is a binary executable /usr/bin/script in your `PATH`, the last command in the following example fails because the Korn shell finds /usr/bin/script and refuses to execute it as a shell script:

```
$ touch xxyzzyz script
$ ksh xxyzzyz
$ ksh ./script
$ ksh script
ksh: script: cannot execute
```

Bash 2.03 has a bug when invoked with the -c option: if the option-argument ends in backslash-newline, Bash incorrectly reports a syntax error. The problem does not occur if a character follows the backslash:

```
$ $ bash -c 'echo foo \
> '
bash: -c: line 2: syntax error: unexpected end of file
$ bash -c 'echo foo \
>  '
foo
```

See Backslash-Newline Before Empty Lines, for how this can cause problems in makefiles.

### 11.4 Here-Documents

Because unquoted here-documents are subject to parameter expansion and command substitution, the characters ‘$’ and ‘`’ are special in unquoted here-documents and should be escaped by ‘\’ if you want them as-is. Also, ‘\’ is special if it precedes ‘$’, ‘`’, newline or ‘\’ itself, so ‘\’ should be doubled if it appears before these characters and you want it as-is.

Using command substitutions in a here-document that is fed to a shell function is not portable. For example, with Solaris 10 `/bin/sh`:

```
$ kitty () { cat; }
$ kitty <<EOF
> `echo ok`
> EOF
/tmp/sh199886: cannot open
$ echo $?
1
```

Some shells mishandle large here-documents: for example, Solaris 10 `dtksh` and the UnixWare 7.1.1 POSIX shell, which are derived from Korn shell version M-12/28/93d, mishandle braced variable expansion that crosses a 1024- or 4096-byte buffer boundary within a here-document. Only the part of the variable name after the boundary is used. For example, `${variable}` could be replaced by the expansion of `${ble}`. If the end of the variable name is aligned with the block boundary, the shell reports an error, as if you used `${}`. Instead of `${variable-default}`, the shell may expand `${riable-default}`, or even `${fault}`. This bug can often be worked around by omitting the braces: `$variable`. The bug was fixed in ‘ksh93g’ (1998-04-30) but as of 2006 many operating systems were still shipping older versions with the bug.

Empty here-documents are not portable either; with the following code, `zsh` up to at least version 4.3.10 creates a file with a single newline, whereas other shells create an empty file:

```
cat >file <<EOF
EOF
```

Many shells (including the Bourne shell) implement here-documents inefficiently. In particular, some shells can be extremely inefficient when a single statement contains many here-documents. For instance if your configure.ac includes something like:

```
AS_IF([<cross_compiling>],
  [assume this and that],
  [check this
   check that
   check something else
   ...
   on and on forever
   ...])
```

A shell parses the whole `if`/`fi` construct generated by `AS_IF`, creating temporary files for each here-document in it. Some shells create links for such here-documents on every `fork`, so that the clean-up code they had installed correctly removes them. It is creating the links that can take the shell forever.

Moving the tests out of the `if`/`fi`, or creating multiple `if`/`fi` constructs, would improve the performance significantly. Anyway, this kind of construct is not exactly the typical use of Autoconf. In fact, it’s even not recommended, because M4 macros can’t look into shell conditionals, so we may fail to expand a macro when it was expanded before in a conditional path, and the condition turned out to be false at runtime, and we end up not executing the macro at all.

Be careful with the use of ‘<<-’ to unindent here-documents. The behavior is only portable for stripping leading TABs, and things can silently break if an overzealous editor converts to using leading spaces (not all shells are nice enough to warn about unterminated here-documents).

```
$ printf 'cat <<-x\n\t1\n\t 2\n\tx\n' | bash && echo done
1
 2
done
$ printf 'cat <<-x\n 1\n  2\n x\n' | bash-3.2 && echo done
 1
  2
 x
done
```

### 11.5 File Descriptors

Most shells, if not all (including Bash, Zsh, Ash), output traces on stderr, even for subshells. This might result in undesirable content if you meant to capture the standard-error output of the inner command:

```
$ ash -x -c '(eval "echo foo >&2") 2>stderr'
$ cat stderr
+ eval echo foo >&2
+ echo foo
foo
$ bash -x -c '(eval "echo foo >&2") 2>stderr'
$ cat stderr
+ eval 'echo foo >&2'
++ echo foo
foo
$ zsh -x -c '(eval "echo foo >&2") 2>stderr'
# Traces on startup files deleted here.
$ cat stderr
+zsh:1> eval echo foo >&2
+zsh:1> echo foo
foo
```

One workaround is to grep out uninteresting lines, hoping not to remove good ones.

If you intend to redirect both standard error and standard output, redirect standard output first. This works better with AIX, since its shell mishandles tracing if standard error is redirected first:

```
$ sh -x -c ': 2>err >out'
+ :
+ 2> err $ cat err
1> out
```

Don’t try to redirect the standard error of a command substitution. It must be done *inside* the command substitution. When running ‘: `cd /zorglub` 2>/dev/null’ expect the error message to escape, while ‘: `cd /zorglub 2>/dev/null`’ works properly.

On the other hand, some shells, such as Solaris or FreeBSD `/bin/sh`, warn about missing programs before performing redirections. Therefore, to silently check whether a program exists, it is necessary to perform redirections on a subshell or brace group:

```
$ /bin/sh -c 'nosuch 2>/dev/null'
nosuch: not found
$ /bin/sh -c '(nosuch) 2>/dev/null'
$ /bin/sh -c '{ nosuch; } 2>/dev/null'
$ bash -c 'nosuch 2>/dev/null'
```

FreeBSD 6.2 sh may mix the trace output lines from the statements in a shell pipeline.

It is worth noting that Zsh (but not Ash nor Bash) makes it possible in assignments though: ‘foo=`cd /zorglub` 2>/dev/null’.

Some shells, like `ash`, don’t recognize bi-directional redirection (‘<>’). And even on shells that recognize it, it is not portable to use on fifos: POSIX does not require read-write support for named pipes, and Cygwin does not support it:

```
$ mkfifo fifo
$ exec 5<>fifo
$ echo hi >&5
bash: echo: write error: Communication error on send
```

Furthermore, versions of `dash` before 0.5.6 mistakenly truncate regular files when using ‘<>’:

```
$ echo a > file
$ bash -c ': 1<>file'; cat file
a
$ dash -c ': 1<>file'; cat file
$ rm a
```

Solaris 10 `/bin/sh` executes redirected compound commands in a subshell, while other shells don’t:

```
$ /bin/sh -c 'foo=0; { foo=1; } 2>/dev/null; echo $foo'
0
$ ksh -c 'foo=0; { foo=1; } 2>/dev/null; echo $foo'
1
$ bash -c 'foo=0; { foo=1; } 2>/dev/null; echo $foo'
1
```

Solaris 10 `sh` will try to optimize away a `:` command (even if it is redirected) in a loop after the first iteration, or in a shell function after the first call:

```
$ for i in 1 2 3 ; do : >x$i; done
$ ls x*
x1
$ f () { : >$1; }; f y1; f y2; f y3;
$ ls y*
y1
```

As a workaround, `echo` or `eval` can be used.

When running a subsidiary program be careful if descriptor 0 is not open for reading or decriptors 1 and 2 are not open for writing, as the subsidiary program might not behave as expected. In particular, don’t rely on file descriptors 0, 1, and 2 remaining closed in a subsidiary program. If any of these descriptors is closed, the operating system may open an unspecified file for the descriptor in the newly created process.

If you want a file descriptor above 2 to be inherited into a child process, then you must use redirections specific to that command or a containing subshell or command group, rather than relying on `exec` in the shell. In `ksh` as well as HP-UX `sh`, file descriptors above 2 which are opened using ‘exec *n*>file’ are closed by a subsequent ‘exec’ (such as that involved in the fork-and-exec which runs a program or script):

```
$ echo 'echo hello >&5' >k
$ /bin/sh -c 'exec 5>t; ksh ./k; exec 5>&-; cat t
hello
$ bash -c 'exec 5>t; ksh ./k; exec 5>&-; cat t
hello
$ ksh -c 'exec 5>t; ksh ./k; exec 5>&-; cat t
./k[1]: 5: cannot open [Bad file number]
$ ksh -c '(ksh ./k) 5>t; cat t'
hello
$ ksh -c '{ ksh ./k; } 5>t; cat t'
hello
$ ksh -c '5>t ksh ./k; cat t
hello
```

Don’t rely on duplicating a closed file descriptor to cause an error. With Solaris 10 `/bin/sh`, failed duplication is silently ignored, which can cause unintended leaks to the original file descriptor. In this example, observe the leak to standard output:

```
$ bash -c 'echo hi >&3' 3>&-; echo $?
bash: 3: Bad file descriptor
1
$ /bin/sh -c 'echo hi >&3' 3>&-; echo $?
hi
0
```

Fortunately, an attempt to close an already closed file descriptor will portably succeed. Likewise, it is safe to use either style of ‘*n*<&-’ or ‘*n*>&-’ for closing a file descriptor, even if it doesn’t match the read/write mode that the file descriptor was opened with.

DOS variants cannot rename or remove open files, such as in ‘mv foo bar >foo’ or ‘rm foo >foo’, even though this is perfectly portable among POSIX hosts.

A few ancient systems reserved some file descriptors. By convention, file descriptor 3 was opened to /dev/tty when you logged into Eighth Edition (1985) through Tenth Edition Unix (1989). File descriptor 4 had a special use on the Stardent/Kubota Titan (circa 1990), though we don’t now remember what it was. Both these systems are obsolete, so it’s now safe to treat file descriptors 3 and 4 like any other file descriptors.

On the other hand, you can’t portably use multi-digit file descriptors. `dash` and Solaris `ksh` don’t understand any file descriptor larger than ‘9’:

```
$ bash -c 'exec 10>&-'; echo $?
0
$ ksh -c 'exec 9>&-'; echo $?
0
$ ksh -c 'exec 10>&-'; echo $?
ksh[1]: exec: 10: not found
127
$ dash -c 'exec 9>&-'; echo $?
0
$ dash -c 'exec 10>&-'; echo $?
exec: 1: 10: not found
2
```

### 11.6 Signal Handling

Portable handling of signals within the shell is another major source of headaches. This is worsened by the fact that various different, mutually incompatible approaches are possible in this area, each with its distinctive merits and demerits. A detailed description of these possible approaches, as well as of their pros and cons, can be found in this article.

Solaris 10 `/bin/sh` automatically traps most signals by default; the shell still exits with error upon termination by one of those signals, but in such a case the exit status might be somewhat unexpected (even if allowed by POSIX, strictly speaking):

```
$ bash -c 'kill -1 $$'; echo $? # Will exit 128 + (signal number).
Hangup
129
$ /bin/ksh -c 'kill -15 $$'; echo $? # Likewise.
Terminated
143
$ for sig in 1 2 3 15; do
>   echo $sig:
>   /bin/sh -c "kill -$s \$\$"; echo $?
> done
signal 1:
Hangup
129
signal 2:
208
signal 3:
208
signal 15:
208
```

This gets even worse if one is using the POSIX “wait” interface to get details about the shell process terminations: it will result in the shell having exited normally, rather than by receiving a signal.

```
$ cat > foo.c <<'END'
#include <stdio.h>    /* for printf */
#include <stdlib.h>   /* for system */
#include <sys/wait.h> /* for WIF* macros */
int main(void)
{
  int status = system ("kill -15 $$");
  printf ("Terminated by signal: %s\n",
          WIFSIGNALED (status) ? "yes" : "no");
  printf ("Exited normally: %s\n",
          WIFEXITED (status) ? "yes" : "no");
  return 0;
}
END
$ cc -o foo foo.c
$ ./a.out # On GNU/Linux
Terminated by signal: no
Exited normally: yes
$ ./a.out # On Solaris 10
Terminated by signal: yes
Exited normally: no
```

Various shells seem to handle `SIGQUIT` specially: they ignore it even if it is not blocked, and even if the shell is not running interactively (in fact, even if the shell has no attached tty); among these shells are at least Bash (from version 2 onward), Zsh 4.3.12, Solaris 10 `/bin/ksh` and `/usr/xpg4/bin/sh`, and AT&T `ksh93` (2011). Still, `SIGQUIT` seems to be trappable quite portably within all these shells. OTOH, some other shells doesn’t special-case the handling of `SIGQUIT`; among these shells are at least `pdksh` 5.2.14, Solaris 10 and NetBSD 5.1 `/bin/sh`, and the Almquist Shell 0.5.5.1.

Some shells (especially Korn shells and derivatives) might try to propagate to themselves a signal that has killed a child process; this is not a bug, but a conscious design choice (although its overall value might be debatable). The exact details of how this is attained vary from shell to shell. For example, upon running `perl -e 'kill 2, $$'`, after the perl process has been interrupted, AT&T `ksh93` (2011) will proceed to send itself a `SIGINT`, while Solaris 10 `/bin/ksh` and `/usr/xpg4/bin/sh` will proceed to exit with status 130 (i.e., 128 + 2). In any case, if there is an active trap associated with `SIGINT`, those shells will correctly execute it.

Some Korn shells, when a child process die due receiving a signal with signal number *n*, can leave in ‘$?’ an exit status of 256+*n* instead of the more common 128+*n*. Observe the difference between AT&T `ksh93` (2011) and `bash` 4.1.5 on Debian:

```
$ /bin/ksh -c 'sh -c "kill -1 \$\$"; echo $?'
/bin/ksh: line 1: 7837: Hangup
257
$ /bin/bash -c 'sh -c "kill -1 \$\$"; echo $?'
/bin/bash: line 1:  7861 Hangup        (sh -c "kill -1 \$\$")
129
```

This `ksh` behavior is allowed by POSIX, if implemented with due care; see this Austin Group discussion for more background. However, if it is not implemented with proper care, such a behavior might cause problems in some corner cases. To see why, assume we have a “wrapper” script like this:

```
#!/bin/sh
# Ignore some signals in the shell only, not in its child processes.
trap : 1 2 13 15
wrapped_command "$@"
ret=$?
other_command
exit $ret
```

If `wrapped_command` is interrupted by a `SIGHUP` (which has signal number 1), `ret` will be set to 257. Unless the `exit` shell builtin is smart enough to understand that such a value can only have originated from a signal, and adjust the final wait status of the shell appropriately, the value 257 will just get truncated to 1 by the closing `exit` call, so that a caller of the script will have no way to determine that termination by a signal was involved. Observe the different behavior of AT&T `ksh93` (2011) and `bash` 4.1.5 on Debian:

```
$ cat foo.sh
#!/bin/sh
sh -c 'kill -1 $$'
ret=$?
echo $ret
exit $ret
$ /bin/ksh foo.sh; echo $?
foo.sh: line 2: 12479: Hangup
257
1
$ /bin/bash foo.sh; echo $?
foo.sh: line 2: 12487 Hangup        (sh -c 'kill -1 $$')
129
129
```

### 11.7 File System Conventions

Autoconf uses shell-script processing extensively, so the file names that it processes should not contain characters that are special to the shell. Special characters include space, tab, newline, NUL, and the following:

```
" # $ & ' ( ) * ; < = > ? [ \ ` |
```

Also, file names should not begin with ‘~’ or ‘-’, and should contain neither ‘-’ immediately after ‘/’ nor ‘~’ immediately after ‘:’. On POSIX-like platforms, directory names should not contain ‘:’, as this runs afoul of ‘:’ used as the path separator.

These restrictions apply not only to the files that you distribute, but also to the absolute file names of your source, build, and destination directories.

On some POSIX-like platforms, ‘!’ and ‘^’ are special too, so they should be avoided.

POSIX lets implementations treat leading // specially, but requires leading /// and beyond to be equivalent to /. Most Unix variants treat // like /. However, some treat // as a “super-root” that can provide access to files that are not otherwise reachable from /. The super-root tradition began with Apollo Domain/OS, which died out long ago, but unfortunately Cygwin has revived it.

While `autoconf` and friends are usually run on some POSIX variety, they can be used on other systems, most notably DOS variants. This impacts several assumptions regarding file names.

For example, the following code:

```
case $foo_dir in
  /*) # Absolute
     ;;
  *)
     foo_dir=$dots$foo_dir ;;
esac
```

fails to properly detect absolute file names on those systems, because they can use a drivespec, and usually use a backslash as directory separator. If you want to be portable to DOS variants (at the price of rejecting valid but oddball POSIX file names like a:\b), you can check for absolute file names like this:

```
case $foo_dir in
  [\\/]* | ?:[\\/]* ) # Absolute
     ;;
  *)
     foo_dir=$dots$foo_dir ;;
esac
```

Make sure you quote the brackets if appropriate and keep the backslash as first character. See Limitations of Shell Builtins.

Also, because the colon is used as part of a drivespec, these systems don’t use it as path separator. When creating or accessing paths, you can use the `PATH_SEPARATOR` output variable instead. `configure` sets this to the appropriate value for the build system (‘:’ or ‘;’) when it starts up.

File names need extra care as well. While DOS variants that are POSIXy enough to run `autoconf` (such as DJGPP) are usually able to handle long file names properly, there are still limitations that can seriously break packages. Several of these issues can be easily detected by the doschk package.

A short overview follows; problems are marked with SFN/LFN to indicate where they apply: SFN means the issues are only relevant to plain DOS, not to DOS under Microsoft Windows variants, while LFN identifies problems that exist even under Microsoft Windows variants.

**No multiple dots (SFN)**

DOS cannot handle multiple dots in file names. This is an especially important thing to remember when building a portable configure script, as `autoconf` uses a .in suffix for template files.

This is perfectly OK on POSIX variants:

```
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([source.c foo.bar])
AC_OUTPUT
```

but it causes problems on DOS, as it requires ‘config.h.in’, ‘source.c.in’ and ‘foo.bar.in’. To make your package more portable to DOS-based environments, you should use this instead:

```
AC_CONFIG_HEADERS([config.h:config.hin])
AC_CONFIG_FILES([source.c:source.cin foo.bar:foobar.in])
AC_OUTPUT
```

**No leading dot (SFN)**

DOS cannot handle file names that start with a dot. This is usually not important for `autoconf`.

**Case insensitivity (LFN)**

DOS is case insensitive, so you cannot, for example, have both a file called ‘INSTALL’ and a directory called ‘install’. This also affects `make`; if there’s a file called ‘INSTALL’ in the directory, ‘make install’ does nothing (unless the ‘install’ target is marked as PHONY).

**The 8+3 limit (SFN)**

Because the DOS file system only stores the first 8 characters of the file name and the first 3 of the extension, those must be unique. That means that foobar-part1.c, foobar-part2.c and foobar-prettybird.c all resolve to the same file name (FOOBAR-P.C). The same goes for foo.bar and foo.bartender.

The 8+3 limit is not usually a problem under Microsoft Windows, as it uses numeric tails in the short version of file names to make them unique. However, a registry setting can turn this behavior off. While this makes it possible to share file trees containing long file names between SFN and LFN environments, it also means the above problem applies there as well.

**Invalid characters (LFN)**

Some characters are invalid in DOS file names, and should therefore be avoided. In a LFN environment, these are ‘/’, ‘\’, ‘?’, ‘*’, ‘:’, ‘<’, ‘>’, ‘|’ and ‘"’. In a SFN environment, other characters are also invalid. These include ‘+’, ‘,’, ‘[’ and ‘]’.

**Invalid names (LFN)**

Some DOS file names are reserved, and cause problems if you try to use files with those names. These names include CON, AUX, COM1, COM2, COM3, COM4, LPT1, LPT2, LPT3, NUL, and PRN. File names are case insensitive, so even names like aux/config.guess are disallowed.

### 11.8 Shell Pattern Matching

Portable patterns should avoid the following constructs:

- A bracket expression like ‘[a-z]’ outside the C locale. This pattern may match characters that are not lower-case letters. Outside the C locale, use ‘[[:lower:]]’ instead, or to match just lower-case ASCII letters use ‘[abcdefghijklmnopqrstuvwxyz]’.
- A bracket expression starting with ‘^’. For example, ‘[!-aeiou]’ is portable, but ‘[^-aeiou]’ is not.
- When matching file names, a pattern containing ‘*’, ‘?’ or ‘[...]’ that might match the file names ‘.’ or ‘..’. For example ‘.*’ might match ‘.’ and ‘..’, but it might not.
- Any of the following characters, unless quoted or escaped or in a bracket expression: ! # % = [ ] ^ { } ~ An unescaped ‘[’ that does not introduce a bracket expression is problematic because, for example, ‘a*[’ might match the file name ‘abc[’, but it might not. Curly braces are problematic because POSIX allows but does not require brace expansion. For example, the shell command ‘echo a{b,c,d}e’ outputs ‘abe ace ade’ with Bash, but ‘a{b,c,d}e’ with Dash.
- Backlashes in bracket expressions, unless doubled. For example, ‘[\\^]’ is portable, but ‘[\^]’ is not.
- An unescaped backslash at pattern end.
- A NUL byte. More generally, a NUL byte should never appear anywhere in a portable shell script.

### 11.9 Shell Substitutions

Contrary to a persistent urban legend, the Bourne shell does not systematically split variables and back-quoted expressions, in particular on the right-hand side of assignments and in the argument of `case`. For instance, the following code:

```
case "$given_srcdir" in
.)  top_srcdir="`printf '%s\n' "$dots" | sed 's|/$||'`" ;;
*)  top_srcdir="$dots$given_srcdir" ;;
esac
```

is more readable when written as:

```
case $given_srcdir in
.)  top_srcdir=`printf '%s\n' "$dots" | sed 's|/$||'` ;;
*)  top_srcdir=$dots$given_srcdir ;;
esac
```

and in fact it is even *more* portable: in the first case of the first attempt, the computation of `top_srcdir` is not portable, since not all shells properly understand "`…"…"…`", for example Solaris 10 `ksh`:

```
$ foo="`echo " bar" | sed 's, ,,'`"
ksh: : cannot execute
ksh: bar | sed 's, ,,': cannot execute
```

POSIX does not specify behavior for this sequence. On the other hand, behavior for "`…\"…\"…`" is specified by POSIX, but in practice, not all shells understand it the same way: pdksh 5.2.14 prints spurious quotes when in POSIX mode:

```
$ echo "`echo \"hello\"`"
hello
$ set -o posix
$ echo "`echo \"hello\"`"
"hello"
```

There is just no portable way to use double-quoted strings inside double-quoted back-quoted expressions (pfew!).

Bash 4.1 has a bug where quoted empty strings adjacent to unquoted parameter expansions are elided during word splitting. Meanwhile, zsh does not perform word splitting except when in Bourne compatibility mode. In the example below, the correct behavior is to have five arguments to the function, and exactly two spaces on either side of the middle ‘-’, since word splitting collapses multiple spaces in ‘$f’ but leaves empty arguments intact.

```
$ bash -c 'n() { echo "$#$@"; }; f="  -  "; n - ""$f"" -'
3- - -
$ ksh -c 'n() { echo "$#$@"; }; f="  -  "; n - ""$f"" -'
5-  -  -
$ zsh -c 'n() { echo "$#$@"; }; f="  -  "; n - ""$f"" -'
3-   -   -
$ zsh -c 'emulate sh;
> n() { echo "$#$@"; }; f="  -  "; n - ""$f"" -'
5-  -  -
```

You can work around this by doing manual word splitting, such as using ‘"$str" $list’ rather than ‘"$str"$list’.

There are also portability pitfalls with particular expansions:

**`$@` ¶**

Autoconf macros often use the `set` command to update ‘$@’, so if you are writing shell code intended for `configure` you should not assume that the value of ‘$@’ persists for any length of time.

You may see usages like ‘${1+"$@"}’ in older shell scripts designed to work around a portability problem in ancient shells. Unfortunately this runs afoul of bugs in more-recent shells, and nowadays it is better to use plain ‘"$@"’ instead.

The portability problem with ancient shells was significant. When there are no positional arguments ‘"$@"’ should be discarded, but the original Unix version 7 Bourne shell mistakenly treated it as equivalent to ‘""’ instead, and many ancient shells followed its lead.

For many years shell scripts worked around this portability problem by using ‘${1+"$@"}’ instead of ‘"$@"’, and you may see this usage in older scripts. Unfortunately, ‘${1+"$@"}’ does not work with `ksh93` M 93t+ (2009) as shipped in AIX 7.2 (2015), as this shell drops a trailing empty argument:

```
$ set a b c ""
$ set ${1+"$@"}
$ echo $#
3
```

Also, ‘${1+"$@"}’ does not work with Zsh 4.2.6 (2005) and earlier, as shipped in Mac OS X releases before 10.5, as this old Zsh incorrectly word splits the result:

```
zsh $ emulate sh
zsh $ for i in "$@"; do echo $i; done
Hello World
!
zsh $ for i in ${1+"$@"}; do echo $i; done
Hello
World
!
```

To work around these problems Autoconf does two things. First, in the shell code that it generates Autoconf avoids ‘"$@"’ if it is possible that there may be no positional arguments. You can use this workaround in your own code, too, if you want it to be portable to ancient shells. For example, instead of:

```
cat conftest.c "$@"
```

you can use this:

```
case $# in
  0) cat conftest.c;;
  *) cat conftest.c "$@";;
esac
```

Second, Autoconf-generated `configure` scripts work around most of the old Zsh problem by using Zsh’s “global aliases” to convert ‘${1+"$@"}’ into ‘"$@"’ by itself:

```
test ${ZSH_VERSION+y} && alias -g '${1+"$@"}'='"$@"'
```

This workaround is for the benefit of any instances of ‘${1+"$@"}’ in user-written code appearing in `configure` scripts. However, it is not a complete solution, as Zsh recognizes the alias only when a shell word matches it exactly, which means older Zsh still mishandles more-complicated cases like ‘"foo"${1+"$@"}’.

**`${10}` ¶**

The 10th, 11th, … positional parameters can be accessed only after a `shift`. The 7th Edition shell reported an error if given `${10}`, and Solaris 10 `/bin/sh` still acts that way:

```
$ set 1 2 3 4 5 6 7 8 9 10
$ echo ${10}
bad substitution
```

Conversely, not all shells obey the POSIX rule that when braces are omitted, multiple digits beyond a ‘$’ imply the single-digit positional parameter expansion concatenated with the remaining literal digits. To work around the issue, you must use braces.

```
$ bash -c 'set a b c d e f g h i j; echo $10 ${1}0'
a0 a0
$ dash -c 'set a b c d e f g h i j; echo $10 ${1}0'
j a0
```

**`${*var*-*value*}` ¶**

**`${*var*:-*value*}`**

**`${*var*=*value*}`**

**`${*var*:=*value*}`**

**`${*var*?*value*}`**

**`${*var*:?*value*}`**

**`${*var*+*value*}`**

**`${*var*:+*value*}`**

When using ‘${*var*-*value*}’ or similar notations that modify a parameter expansion, POSIX requires that *value* must be a single shell word, which can contain quoted strings but cannot contain unquoted spaces. If this requirement is not met Solaris 10 `/bin/sh` sometimes complains, and anyway the behavior is not portable.

```
$ /bin/sh -c 'echo ${a-b c}'
/bin/sh: bad substitution
$ /bin/sh -c 'echo ${a-'\''b c'\''}'
b c
$ /bin/sh -c 'echo "${a-b c}"'
b c
$ /bin/sh -c 'cat <<EOF
${a-b c}
EOF
b c
```

Most shells treat the special parameters `*` and `@` as being unset if there are no positional parameters. However, some shells treat them as being set to the empty string. POSIX does not clearly specify either behavior.

```
$ bash -c 'echo "* is ${*-unset}."'
* is unset.
$ dash -c 'echo "* is ${*-unset}."'
* is .
```

According to POSIX, if an expansion occurs inside double quotes, then the use of unquoted double quotes within *value* is unspecified, and any single quotes become literal characters; in that case, escaping must be done with backslash. Likewise, the use of unquoted here-documents is a case where double quotes have unspecified results:

```
$ /bin/sh -c 'echo "${a-"b  c"}"'
/bin/sh: bad substitution
$ ksh -c 'echo "${a-"b  c"}"'
b c
$ bash -c 'echo "${a-"b  c"}"'
b  c
$ /bin/sh -c 'a=; echo ${a+'\''b  c'\''}'
b  c
$ /bin/sh -c 'a=; echo "${a+'\''b  c'\''}"'
'b  c'
$ /bin/sh -c 'a=; echo "${a+\"b  c\"}"'
"b  c"
$ /bin/sh -c 'a=; echo "${a+b  c}"'
b  c
$ /bin/sh -c 'cat <<EOF
${a-"b  c"}
EOF'
"b  c"
$ /bin/sh -c 'cat <<EOF
${a-'b  c'}
EOF'
'b  c'
$ bash -c 'cat <<EOF
${a-"b  c"}
EOF'
b  c
$ bash -c 'cat <<EOF
${a-'b  c'}
EOF'
'b  c'
```

Perhaps the easiest way to work around quoting issues in a manner portable to all shells is to place the results in a temporary variable, then use ‘$t’ as the *value*, rather than trying to inline the expression needing quoting.

```
$ /bin/sh -c 't="b  c\"'\''}\\"; echo "${a-$t}"'
b  c"'}\
$ ksh -c 't="b  c\"'\''}\\"; echo "${a-$t}"'
b  c"'}\
$ bash -c 't="b  c\"'\''}\\"; echo "${a-$t}"'
b  c"'}\
```

**`${*var*=*value*}` ¶**

When using ‘${*var*=*value*}’ to assign a default value to *var*, remember that even though the assignment to *var* does not undergo file name expansion, the result of the variable expansion does unless the expansion occurred within double quotes. In particular, when using `:` followed by unquoted variable expansion for the side effect of setting a default value, if the final value of ‘$var’ contains any globbing characters (either from *value* or from prior contents), the shell has to spend time performing file name expansion and field splitting even though those results will not be used. Therefore, it is a good idea to consider double quotes when performing default initialization; while remembering how this impacts any quoting characters appearing in *value*.

```
$ time bash -c ': "${a=/usr/bin/*}"; echo "$a"'
/usr/bin/*

real	0m0.005s
user	0m0.002s
sys	0m0.003s
$ time bash -c ': ${a=/usr/bin/*}; echo "$a"'
/usr/bin/*

real	0m0.039s
user	0m0.026s
sys	0m0.009s
$ time bash -c 'a=/usr/bin/*; : ${a=noglob}; echo "$a"'
/usr/bin/*

real	0m0.031s
user	0m0.020s
sys	0m0.010s

$ time bash -c 'a=/usr/bin/*; : "${a=noglob}"; echo "$a"'
/usr/bin/*

real	0m0.006s
user	0m0.002s
sys	0m0.003s
```

As with ‘+’ and ‘-’, *value* must be a single shell word, otherwise some shells, such as Solaris 10 `/bin/sh` or on Digital Unix V 5.0, die because of a “bad substitution”. Meanwhile, POSIX requires that with ‘=’, quote removal happens prior to the assignment, and the expansion be the final contents of *var* without quoting (and thus subject to field splitting), in contrast to the behavior with ‘-’ passing the quoting through to the final expansion. However, `bash` 4.1 does not obey this rule.

```
$ ksh -c 'echo ${var-a\ \ b}'
a  b
$ ksh -c 'echo ${var=a\ \ b}'
a b
$ bash -c 'echo ${var=a\ \ b}'
a  b
```

Finally, POSIX states that when mixing ‘${a=b}’ with regular commands, it is unspecified whether the assignments affect the parent shell environment. It is best to perform assignments independently from commands, to avoid the problems demonstrated in this example running on Solaris 10:

```
$ cmd='x= y=${x:=b} sh -c "echo +\$x+\$y+";printf "%s\\n" -$x-'
$ bash -c "$cmd"
+b+b+
-b-
$ /bin/sh -c "$cmd"
++b+
--
$ ksh -c "$cmd"
+b+b+
--
```

**`${*var*=*value*}` ¶**

Solaris 10 `/bin/sh` has a frightening bug in its handling of literal assignments. Imagine you need set a variable to a string containing ‘}’. This ‘}’ character confuses Solaris 10 `/bin/sh` when the affected variable was already set. This bug can be exercised by running:

```
$ unset foo
$ foo=${foo='}'}
$ echo $foo
}
$ foo=${foo='}'   # no error; this hints to what the bug is
$ echo $foo
}
$ foo=${foo='}'}
$ echo $foo
}}
 ^ ugh!
```

It seems that ‘}’ is interpreted as matching ‘${’, even though it is enclosed in single quotes. The problem doesn’t happen using double quotes, or when using a temporary variable holding the problematic string.

**`${*var*=*expanded-value*}` ¶**

On shells so old that they are no longer relevant, the command

```
# Set the shell variable to a default value
# if it is not already set.
: ${var="$default"}
```

misbehaved badly in some cases. Older scripts worked around the bugs by using one of following two lines, the latter of which was more portable:

```
var=${var="$default"}
test ${var+y} || var=$default
```

However, these workarounds are no longer needed.

**`${#*var*}` ¶**

**`${*var*%*word*}`**

**`${*var*%%*word*}`**

**`${*var*#*word*}`**

**`${*var*##*word*}`**

POSIX requires support for these usages, but they do not work with many traditional shells, e.g., Solaris 10 `/bin/sh`.

Also, `pdksh` 5.2.14 mishandles some *word* forms. For example if ‘$1’ is ‘a/b’ and ‘$2’ is ‘a’, then ‘${1#$2}’ should yield ‘/b’, but with `pdksh` it yields the empty string.

**`*commands*` ¶**

POSIX requires shells to trim all trailing newlines from command output before substituting it, so assignments like ‘dir=`printf '%s\n' "$file" | tr a A`’ do not work as expected if ‘$file’ ends in a newline.

While in general it makes no sense, do not substitute a single builtin with side effects, because Ash 0.2, trying to optimize, does not fork a subshell to perform the command. For instance, if you wanted to check that `cd` is silent, do not use ‘test -z "`cd /`"’ because the following can happen:

```
$ pwd
/tmp
$ test -z "`cd /`" && pwd
/
```

The result of ‘foo=`exit 1`’ is left as an exercise to the reader.

The MSYS shell leaves a stray byte in the expansion of a double-quoted command substitution of a native program, if the end of the substitution is not aligned with the end of the double quote. This may be worked around by inserting another pair of quotes:

```
$ echo "`printf 'foo\r\n'` bar" > broken
$ echo "`printf 'foo\r\n'`"" bar" | cmp - broken
- broken differ: char 4, line 1
```

Upon interrupt or SIGTERM, some shells may abort a command substitution, replace it with a null string, and wrongly evaluate the enclosing command before entering the trap or ending the script. This can lead to spurious errors:

```
$ sh -c 'if test `sleep 5; echo hi` = hi; then echo yes; fi'
$ ^C
sh: test: hi: unexpected operator/operand
```

You can avoid this by assigning the command substitution to a temporary variable:

```
$ sh -c 'res=`sleep 5; echo hi`
         if test "x$res" = xhi; then echo yes; fi'
$ ^C
```

**`$(*commands*)` ¶**

This construct is meant to replace ‘`*commands*`’, and it has most of the problems listed under `*commands*`.

This construct can be nested while this is impossible to do portably with back quotes. Although it is almost universally supported, unfortunately Solaris 10 and earlier releases lack it:

```
$ showrev -c /bin/sh | grep version
Command version: SunOS 5.10 Generic 142251-02 Sep 2010
$ echo $(echo blah)
syntax error: `(' unexpected
```

If you do use ‘$(*commands*)’, make sure that the commands do not start with a parenthesis, as that would cause confusion with a different notation ‘$((*expression*))’ that in modern shells is an arithmetic expression not a command. To avoid the confusion, insert a space between the two opening parentheses.

Avoid *commands* that contain unbalanced parentheses in here-documents, comments, or case statement patterns, as many shells mishandle them. For example, Bash 3.1, ‘ksh88’, `pdksh` 5.2.14, and Zsh 4.2.6 all mishandle the following valid command:

```
echo $(case x in x) echo hello;; esac)
```

**`$((*expression*))` ¶**

Arithmetic expansion is not portable as some shells (most notably Solaris 10 `/bin/sh`) don’t support it.

Among shells that do support ‘$(( ))’, not all of them obey the POSIX rule that octal and hexadecimal constants must be recognized:

```
$ bash -c 'echo $(( 010 + 0x10 ))'
24
$ zsh -c 'echo $(( 010 + 0x10 ))'
26
$ zsh -c 'emulate sh; echo $(( 010 + 0x10 ))'
24
$ pdksh -c 'echo $(( 010 + 0x10 ))'
pdksh:  010 + 0x10 : bad number `0x10'
$ pdksh -c 'echo $(( 010 ))'
10
```

When it is available, using arithmetic expansion provides a noticeable speedup in script execution; but testing for support requires `eval` to avoid syntax errors. The following construct is used by `AS_VAR_ARITH` to provide arithmetic computation when all arguments are decimal integers without leading zeros, and all operators are properly quoted and appear as distinct arguments:

```
if ( eval 'test $(( 1 + 1 )) = 2' ) 2>/dev/null; then
  eval 'func_arith ()
  {
    func_arith_result=$(( $* ))
  }'
else
  func_arith ()
  {
    func_arith_result=`expr "$@"`
  }
fi
func_arith 1 + 1
foo=$func_arith_result
```

**`^` ¶**

Always quote ‘^’, otherwise traditional shells such as `/bin/sh` on Solaris 10 treat this like ‘|’.

### 11.10 Assignments

When setting several variables in a row, be aware that the order of the evaluation is undefined. For instance ‘foo=1 foo=2; echo $foo’ gives ‘1’ with Solaris 10 `/bin/sh`, but ‘2’ with Bash. You must use ‘;’ to enforce the order: ‘foo=1; foo=2; echo $foo’.

Don’t rely on the following to find subdir/program:

```
PATH=subdir$PATH_SEPARATOR$PATH program
```

as this does not work with Zsh 3.0.6. Use something like this instead:

```
(PATH=subdir$PATH_SEPARATOR$PATH; export PATH; exec program)
```

Don’t rely on the exit status of an assignment: Ash 0.2 does not change the status and propagates that of the last statement:

```
$ false || foo=bar; echo $?
1
$ false || foo=`:`; echo $?
0
```

and to make things even worse, QNX 4.25 just sets the exit status to 0 in any case:

```
$ foo=`exit 1`; echo $?
0
```

To assign default values, follow this algorithm:

1. If the default value is a literal and does not contain any closing brace, use: : "${var='my literal'}"
2. If the default value contains no closing brace, has to be expanded, and the variable being initialized is not intended to be IFS-split (i.e., it’s not a list), then use: : ${var="$default"}
3. If the default value contains no closing brace, has to be expanded, and the variable being initialized is intended to be IFS-split (i.e., it’s a list), then use: var=${var="$default"}
4. If the default value contains a closing brace, then use: test ${var+y} || var="has a '}'"

In most cases ‘var=${var="$default"}’ is fine, but in case of doubt, just use the last form. See Shell Substitutions, items ‘${*var*:-*value*}’ and ‘${*var*=*value*}’ for the rationale.

### 11.11 Parentheses in Shell Scripts

Beware of two opening parentheses in a row, as many shell implementations treat them specially, and POSIX says that a portable script cannot use ‘((’ outside the ‘$((’ form used for shell arithmetic. In traditional shells, ‘((cat))’ behaves like ‘(cat)’; but many shells, including Bash and the Korn shell, treat ‘((cat))’ as an arithmetic expression equivalent to ‘let "cat"’, and may or may not report an error when they detect that ‘cat’ is not a number. As another example, ‘pdksh’ 5.2.14 does not treat the following code as a traditional shell would:

```
if ((true) || false); then
  echo ok
fi
```

To work around this problem, insert a space between the two opening parentheses. There is a similar problem and workaround with ‘$((’; see Shell Substitutions.

### 11.12 Special Shell Variables

Some shell variables should not be used, since they can have a deep influence on the behavior of the shell. In order to recover a sane behavior from the shell, some variables should be unset; M4sh takes care of this and provides fallback values, whenever needed, to cater for a very old /bin/sh that does not support `unset`. (see Portable Shell Programming).

As a general rule, shell variable names containing a lower-case letter are safe; you can define and use these variables without worrying about their effect on the underlying system, and without worrying about whether the shell changes them unexpectedly. (The exception is the shell variable `status`, as described below.)

Here is a list of names that are known to cause trouble. This list is not exhaustive, but you should be safe if you avoid the name `status` and names containing only upper-case letters and underscores.

**`?`**

Not all shells correctly reset ‘$?’ after conditionals (see Limitations of Shell Builtins). Not all shells manage ‘$?’ correctly in shell functions (see Shell Functions) or in traps (see Limitations of Shell Builtins). Not all shells reset ‘$?’ to zero after an empty command.

```
$ bash -c 'false; $empty; echo $?'
0
$ zsh -c 'false; $empty; echo $?'
1
```

**`_` ¶**

Many shells reserve ‘$_’ for various purposes, e.g., the name of the last command executed.

**`CDPATH` ¶**

When this variable is set it specifies a list of directories to search when invoking `cd` with a relative file name that did not start with ‘./’ or ‘../’. POSIX says that if a nonempty directory name from `CDPATH` is used successfully, `cd` prints the resulting absolute file name. Unfortunately this output can break idioms like ‘abs=`cd src && pwd`’ because `abs` receives the name twice. Also, many shells do not conform to this part of POSIX; for example, `zsh` prints the result only if a directory name other than . was chosen from `CDPATH`.

In practice the shells that have this problem also support `unset`, so you can work around the problem as follows:

```
(unset CDPATH) >/dev/null 2>&1 && unset CDPATH
```

You can also avoid output by ensuring that your directory name is absolute or anchored at ‘./’, as in ‘abs=`cd ./src && pwd`’.

Configure scripts use M4sh, which automatically unsets `CDPATH` if possible, so you need not worry about this problem in those scripts.

**`CLICOLOR_FORCE` ¶**

When this variable is set, some implementations of tools like `ls` attempt to add color to their output via terminal escape sequences, even when the output is not directed to a terminal, and can thus cause spurious failures in scripts. Configure scripts use M4sh, which automatically unsets this variable.

**`DUALCASE` ¶**

In the MKS shell, case statements and file name generation are case-insensitive unless `DUALCASE` is nonzero. Autoconf-generated scripts export this variable when they start up.

**`ENV` ¶**

**`MAIL`**

**`MAILPATH`**

**`PS1`**

**`PS2`**

**`PS4`**

These variables should not matter for shell scripts, since they are supposed to affect only interactive shells. However, at least one shell (the pre-3.0 UWIN Korn shell) gets confused about whether it is interactive, which means that (for example) a `PS1` with a side effect can unexpectedly modify ‘$?’. To work around this bug, M4sh scripts (including configure scripts) do something like this:

```
(unset ENV) >/dev/null 2>&1 && unset ENV MAIL MAILPATH
PS1='$ '
PS2='> '
PS4='+ '
```

(actually, there is some complication due to bugs in `unset`; see Limitations of Shell Builtins).

**`FPATH` ¶**

The Korn shell uses `FPATH` to find shell functions, so avoid `FPATH` in portable scripts. `FPATH` is consulted after `PATH`, but you still need to be wary of tests that use `PATH` to find whether a command exists, since they might report the wrong result if `FPATH` is also set.

**`GREP_OPTIONS` ¶**

When this variable is set, some implementations of `grep` honor these options, even if the options include direction to enable colored output via terminal escape sequences, and the result can cause spurious failures when the output is not directed to a terminal. Configure scripts use M4sh, which automatically unsets this variable.

**`HOME` ¶**

Strange things can happen if `HOME` is unset or empty. For example, plain `cd` (with no arguments) has unspecified behavior. Also, `HOME` should be absolute, not relative.

**`IFS` ¶**

Long ago, shell scripts inherited `IFS` from the environment, but this caused many problems so modern shells ignore any environment settings for `IFS`.

Don’t set the first character of `IFS` to backslash. Indeed, Bourne shells use the first character (backslash) when joining the components in ‘"$@"’ and some shells then reinterpret (!) the backslash escapes, so you can end up with backspace and other strange characters.

The proper value for `IFS` (in regular code, not when performing splits) is ‘SPCTABRET’. The first character is especially important, as it is used to join the arguments in ‘$*’; however, note that traditional shells, but also bash-2.04, fail to adhere to this and join with a space anyway.

M4sh guarantees that `IFS` will have the default value at the beginning of a script, and many macros within autoconf rely on this setting. It is okay to use blocks of shell code that temporarily change the value of `IFS` in order to split on another character, but remember to restore it before expanding further macros.

Unsetting `IFS` instead of resetting it to the default sequence is not suggested, since code that tries to save and restore the variable’s value will incorrectly reset it to an empty value, thus disabling field splitting:

```
unset IFS
# default separators used for field splitting

save_IFS=$IFS
IFS=:
# ...
IFS=$save_IFS
# no field splitting performed
```

**`LANG` ¶**

**`LC_ALL`**

**`LC_COLLATE`**

**`LC_CTYPE`**

**`LC_MESSAGES`**

**`LC_MONETARY`**

**`LC_NUMERIC`**

**`LC_TIME`**

You should set all these variables to ‘C’ because so much configuration code assumes the C locale and POSIX requires that locale environment variables be set to ‘C’ if the C locale is desired; configure scripts and M4sh do that for you. Export these variables after setting them.

**`LANGUAGE` ¶**

`LANGUAGE` is not specified by POSIX, but it is a GNU extension that overrides `LC_ALL` in some cases, so you (or M4sh) should set it too.

**`LC_ADDRESS` ¶**

**`LC_IDENTIFICATION`**

**`LC_MEASUREMENT`**

**`LC_NAME`**

**`LC_PAPER`**

**`LC_TELEPHONE`**

These locale environment variables are GNU extensions. They are treated like their POSIX brethren (`LC_COLLATE`, etc.) as described above.

**`LINENO` ¶**

Most modern shells provide the current line number in `LINENO`. Its value is the line number of the beginning of the current command. M4sh, and hence Autoconf, attempts to execute `configure` with a shell that supports `LINENO`. If no such shell is available, it attempts to implement `LINENO` with a Sed prepass that replaces each instance of the string `$LINENO` (not followed by an alphanumeric character) with the line’s number. In M4sh scripts you should execute `AS_LINENO_PREPARE` so that these workarounds are included in your script; configure scripts do this automatically in `AC_INIT`.

You should not rely on `LINENO` within `eval` or shell functions, as the behavior differs in practice. The presence of a quoted newline within simple commands can alter which line number is used as the starting point for `$LINENO` substitutions within that command. Also, the possibility of the Sed prepass means that you should not rely on `$LINENO` when quoted, when in here-documents, or when line continuations are used. Subshells should be OK, though. In the following example, lines 1, 9, and 14 are portable, but the other instances of `$LINENO` do not have deterministic values:

```
$ cat lineno
echo 1. $LINENO
echo "2. $LINENO
3. $LINENO"
cat <<EOF
5. $LINENO
6. $LINENO
7. \$LINENO
EOF
( echo 9. $LINENO )
eval 'echo 10. $LINENO'
eval 'echo 11. $LINENO
echo 12. $LINENO'
echo 13. '$LINENO'
echo 14. $LINENO '
15.' $LINENO
f () { echo $1 $LINENO;
echo $1 $LINENO }
f 18.
echo 19. \
$LINENO
```

```
$ bash-3.2 ./lineno
1. 1
2. 3
3. 3
5. 4
6. 4
7. $LINENO
9. 9
10. 10
11. 12
12. 13
13. $LINENO
14. 14
15. 14
18. 16
18. 17
19. 19
```

```
$ zsh-4.3.4 ./lineno
1. 1
2. 2
3. 2
5. 4
6. 4
7. $LINENO
9. 9
10. 1
11. 1
12. 2
13. $LINENO
14. 14
15. 14
18. 0
18. 1
19. 19
```

```
$ pdksh-5.2.14 ./lineno
1. 1
2. 2
3. 2
5. 4
6. 4
7. $LINENO
9. 9
10. 0
11. 0
12. 0
13. $LINENO
14. 14
15. 14
18. 16
18. 17
19. 19
```

```
$ sed '=' <lineno |
>   sed '
>     N
>     s,$,-,
>     t loop
>     :loop
>     s,^\([0-9]*\)\(.*\)[$]LINENO\([^a-zA-Z0-9_]\),\1\2\1\3,
>     t loop
>     s,-$,,
>     s,^[0-9]*\n,,
>   ' |
>   sh
1. 1
2. 2
3. 3
5. 5
6. 6
7. \7
9. 9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
18. 16
18. 17
19. 20
```

In particular, note that config.status (and any other subsidiary script created by `AS_INIT_GENERATED`) might report line numbers relative to the parent script as a result of the potential Sed pass.

**`NULLCMD` ¶**

When executing the command ‘>foo’, `zsh` executes ‘$NULLCMD >foo’ unless it is operating in Bourne shell compatibility mode and the `zsh` version is newer than 3.1.6-dev-18. If you are using an older `zsh` and forget to set `NULLCMD`, your script might be suspended waiting for data on its standard input.

**`OLDPWD` ¶**

POSIX requires that `cd` must update the `OLDPWD` environment variable, if set, to point to the name of the previous directory, but Solaris 10 `/bin/sh` does not support this.

**`options` ¶**

For `zsh` 4.3.10, `options` is treated as an associative array even after `emulate sh`, so it should not be used.

**`PATH_SEPARATOR` ¶**

On DJGPP systems, the `PATH_SEPARATOR` environment variable can be set to either ‘:’ or ‘;’ to control the path separator Bash uses to set up certain environment variables (such as `PATH`). You can set this variable to ‘;’ if you want `configure` to use ‘;’ as a separator; this might be useful if you plan to use non-POSIX shells to execute files. See File System Conventions, for more information about `PATH_SEPARATOR`.

**`POSIXLY_CORRECT` ¶**

In the GNU environment, exporting `POSIXLY_CORRECT` with any value (even empty) causes programs to try harder to conform to POSIX. Autoconf does not directly manipulate this variable, but `bash` ties the shell variable `POSIXLY_CORRECT` to whether the script is running in POSIX mode. Therefore, take care when exporting or unsetting this variable, so as not to change whether `bash` is in POSIX mode.

```
$ bash --posix -c 'set -o | grep posix
> unset POSIXLY_CORRECT
> set -o | grep posix'
posix           on
posix           off
```

**`PWD` ¶**

POSIX requires that `cd` must update the `PWD` environment variable to point to the name of the current directory, but traditional shells do not support this. This can cause confusion if one shell instance maintains `PWD` but a subsidiary and different shell does not know about `PWD` and executes `cd`; in this case `PWD` points to the wrong directory. Use ‘`pwd`’ rather than ‘$PWD’.

**`RANDOM` ¶**

Many shells provide `RANDOM`, a variable that returns a different integer each time it is used. It is common practice to use `$RANDOM` as part of a file name, but code shouldn’t rely on `$RANDOM` expanding to a nonempty string.

**`status` ¶**

This variable is an alias to ‘$?’ for `zsh` (at least 3.1.6), hence read-only. Do not use it.

### 11.13 Shell Functions

Nowadays, it is difficult to find a shell that does not support shell functions at all. However, some differences should be expected.

When declaring a shell function, you must include whitespace between the ‘)’ after the function name and the start of the compound expression, to avoid upsetting `ksh`. While it is possible to use any compound command, most scripts use ‘{…}’.

```
$ /bin/sh -c 'a(){ echo hi;}; a'
hi
$ ksh -c 'a(){ echo hi;}; a'
ksh: syntax error at line 1: `}' unexpected
$ ksh -c 'a() { echo hi;}; a'
hi
```

Inside a shell function, you should not rely on the error status of a subshell if the last command of that subshell was `exit` or `trap`, as this triggers bugs in zsh 4.x; while Autoconf tries to find a shell that does not exhibit the bug, zsh might be the only shell present on the user’s machine.

Likewise, the state of ‘$?’ is not reliable when entering a shell function. This has the effect that using a function as the first command in a `trap` handler can cause problems.

```
$ bash -c 'foo() { echo $?; }; trap foo 0; (exit 2); exit 2'; echo $?
2
2
$ ash -c 'foo() { echo $?; }; trap foo 0; (exit 2); exit 2'; echo $?
0
2
```

DJGPP bash 2.04 has a bug in that `return` from a shell function which also used a command substitution causes a segmentation fault. To work around the issue, you can use `return` from a subshell, or ‘AS_SET_STATUS’ as last command in the execution flow of the function (see Common Shell Constructs).

Not all shells treat shell functions as simple commands impacted by ‘set -e’, for example with Solaris 10 `/bin/sh`:

```
$ bash -c 'f() { return 1; }; set -e; f; echo oops'
$ /bin/sh -c 'f() { return 1; }; set -e; f; echo oops'
oops
```

Shell variables and functions may share the same namespace, for example with Solaris 10 `/bin/sh`:

```
$ f () { :; }; f=; f
f: not found
```

For this reason, Autoconf (actually M4sh, see Programming in M4sh) uses the prefix ‘as_fn_’ for its functions.

Handling of positional parameters and shell options varies among shells. For example, Korn shells reset and restore trace output (‘set -x’) and other options upon function entry and exit.

It is not portable to pass temporary environment variables to shell functions. Solaris 10 `/bin/sh` does not see the variable. Meanwhile, not all shells follow the POSIX rule that the assignment must affect the current environment in the same manner as special built-ins.

```
$ /bin/sh -c 'func() { echo $a;}; a=1 func; echo $a'
⇒
⇒
$ ash -c 'func() { echo $a;}; a=1 func; echo $a'
⇒1
⇒
$ bash -c 'set -o posix; func() { echo $a;}; a=1 func; echo $a'
⇒1
⇒1
```

Some ancient Bourne shell variants with function support did not reset ‘$*i*, *i* >= 0’, upon function exit, so effectively the arguments of the script were lost after the first function invocation. It is probably not worth worrying about these shells any more.

With AIX sh, a `trap` on 0 installed in a shell function triggers at function exit rather than at script exit. See Limitations of Shell Builtins.

### 11.14 Limitations of Shell Builtins

No, no, we are serious: some shells do have limitations! :)

You should always keep in mind that any builtin or command may support options, and therefore differ in behavior with arguments starting with a dash. For instance, even the innocent ‘echo "$word"’ can give unexpected results when `word` starts with a dash. To avoid this problem, use ‘printf '%s\n' "$word"’. Many of these limitations can be worked around using M4sh (see Programming in M4sh).

**`.`**

Use `.` only with regular files (use ‘test -f’). Bash 2.03, for instance, chokes on ‘. /dev/null’. Remember that `.` uses `PATH` if its argument contains no slashes. Also, some shells, including bash 3.2, implicitly append the current directory to this `PATH` search, even though POSIX forbids it. So if you want to use `.` on a file foo in the current directory, you must use ‘. ./foo’.

Not all shells gracefully handle syntax errors within a sourced file. On one extreme, some non-interactive shells abort the entire script. On the other, `zsh` 4.3.10 has a bug where it fails to react to the syntax error.

```
$ echo 'fi' > syntax
$ bash -c '. ./syntax; echo $?'
./syntax: line 1: syntax error near unexpected token `fi'
./syntax: line 1: `fi'
2
$ ash -c '. ./syntax; echo $?'
./syntax: 1: Syntax error: "fi" unexpected
$ zsh -c '. ./syntax; echo $?'
./syntax:1: parse error near `fi'
0
```

**`!`**

The Unix version 7 shell did not support negating the exit status of commands with `!`, and this feature is still absent from some shells (e.g., Solaris 10 `/bin/sh`). Other shells, such as FreeBSD `/bin/sh` or `ash`, have bugs when using `!`:

```
$ sh -c '! : | :'; echo $?
1
$ ash -c '! : | :'; echo $?
0
$ sh -c '! { :; }'; echo $?
1
$ ash -c '! { :; }'; echo $?
{: not found
Syntax error: "}" unexpected
2
```

Shell code like this:

```
if ! cmp file1 file2 >/dev/null 2>&1; then
  echo files differ or trouble
fi
```

is therefore not portable in practice. Typically it is easy to rewrite such code, e.g.:

```
cmp file1 file2 >/dev/null 2>&1 ||
  echo files differ or trouble
```

In M4sh, the `AS_IF` macro provides an easy way to write these kinds of conditionals:

```
AS_IF([cmp -s file file.new], [],
  [echo files differ or trouble])
```

This kind of rewriting is needed in code outside macro definitions that calls other macros. See Common Shell Constructs. It is also useful inside macro definitions, where the *then* and *else* branches might contain macro arguments.

More generally, one can always rewrite ‘! *command*’ as:

```
AS_IF([command], [(exit 1)])
```

**`&&` and `||`**

If an AND-OR list is not inside `AC_DEFUN`, and it contains calls to Autoconf macros, it should be rewritten using `AS_IF`. See Common Shell Constructs. The operators `&&` and `||` have equal precedence and are left associative, so instead of:

```
# This is dangerous outside AC_DEFUN.
cmp a b >/dev/null 2>&1 &&
  AS_ECHO([files are same]) >$tmpfile ||
    AC_MSG_NOTICE([files differ, or echo failed])
```

you can use:

```
# This is OK outside AC_DEFUN.
AS_IF([AS_IF([cmp a b >/dev/null 2>&1],
         [AS_ECHO([files are same]) >$tmpfile],
         [false])],
  [AC_MSG_NOTICE([files differ, or echo failed])])
```

**`{...}`**

Bash 3.2 (and earlier versions) sometimes does not properly set ‘$?’ when failing to write redirected output of a compound command. This problem is most commonly observed with ‘{…}’; it does not occur with ‘(…)’. For example:

```
$ bash -c '{ echo foo; } >/bad; echo $?'
bash: line 1: /bad: Permission denied
0
$ bash -c 'while :; do echo; done >/bad; echo $?'
bash: line 1: /bad: Permission denied
0
```

To work around the bug, prepend ‘:;’:

```
$ bash -c ':;{ echo foo; } >/bad; echo $?'
bash: line 1: /bad: Permission denied
1
```

POSIX requires a syntax error if a brace list has no contents. However, not all shells obey this rule; and on shells where empty lists are permitted, the effect on ‘$?’ is inconsistent. To avoid problems, ensure that a brace list is never empty.

```
$ bash -c 'false; { }; echo $?' || echo $?
bash: line 1: syntax error near unexpected token `}'
bash: line 1: `false; { }; echo $?'
2
$ zsh -c 'false; { }; echo $?' || echo $?
1
$ pdksh -c 'false; { }; echo $?' || echo $?
0
```

**`break`**

The use of ‘break 2’ etc. is safe.

**`case`**

If a `case` command is not inside `AC_DEFUN`, and it contains calls to Autoconf macros, it should be rewritten using `AS_CASE`. See Common Shell Constructs. Instead of:

```
# This is dangerous outside AC_DEFUN.
case $filename in
  *.[ch]) AC_MSG_NOTICE([C source file]);;
esac
```

use:

```
# This is OK outside AC_DEFUN.
AS_CASE([$filename],
  [[*.[ch]]], [AC_MSG_NOTICE([C source file])])
```

You don’t need to quote the argument; no splitting is performed.

You don’t need the final ‘;;’, but you should use it.

POSIX requires support for `case` patterns with opening parentheses like this:

```
case $file_name in
  (*.c) echo "C source code";;
esac
```

but the `(` in this example is not portable to a few obsolescent Bourne shell implementations, which is a pity for those of us using tools that rely on balanced parentheses. For instance, with Solaris 10 `/bin/sh`:

```
$ case foo in (foo) echo foo;; esac
error→syntax error: `(' unexpected
```

The leading ‘(’ can be omitted safely. Unfortunately, there are contexts where unbalanced parentheses cause other problems, such as when using a syntax-highlighting editor that searches for the balancing counterpart, or more importantly, when using a case statement as an underquoted argument to an Autoconf macro. See Dealing with unbalanced parentheses, for trade-offs involved in various styles of dealing with unbalanced ‘)’.

Zsh handles pattern fragments derived from parameter expansions or command substitutions as though quoted:

```
$ pat=\?; case aa in ?$pat) echo match;; esac
$ pat=\?; case a? in ?$pat) echo match;; esac
match
```

Because of a bug in its `fnmatch`, Bash fails to properly handle backslashes in character classes:

```
bash-2.02$ case /tmp in [/\\]*) echo OK;; esac
bash-2.02$
```

This is extremely unfortunate, since you are likely to use this code to handle POSIX or MS-DOS absolute file names. To work around this bug, always put the backslash first:

```
bash-2.02$ case '\TMP' in [\\/]*) echo OK;; esac
OK
bash-2.02$ case /tmp in [\\/]*) echo OK;; esac
OK
```

Many Bourne shells cannot handle closing brackets in character classes correctly.

Some shells also have problems with backslash escaping in case you do not want to match the backslash: both a backslash and the escaped character match this pattern. To work around this, specify the character class in a variable, so that quote removal does not apply afterwards, and the special characters don’t have to be backslash-escaped:

```
$ case '\' in [\<]) echo OK;; esac
OK
$ scanset='[<]'; case '\' in $scanset) echo OK;; esac
$
```

Even with this, Solaris `ksh` matches a backslash if the set contains any of the characters ‘|’, ‘&’, ‘(’, or ‘)’.

Some shells, such as Ash 0.3.8, are confused by an empty `case`/`esac`:
