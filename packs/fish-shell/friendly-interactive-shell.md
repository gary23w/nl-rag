---
title: "fish (Unix shell)"
source: https://en.wikipedia.org/wiki/Friendly_interactive_shell
domain: fish-shell
license: CC-BY-SA-4.0
tags: fish shell, friendly interactive shell, fishshell
fetched: 2026-07-02
---

# fish (Unix shell)

(Redirected from

Friendly interactive shell

)

**fish** (**friendly interactive shell**; stylized in lowercase) is a Unix-like shell with a focus on interactivity and usability. fish is designed to be feature-rich by default, rather than highly configurable, and does not adhere to POSIX shell standards by design.

## Features

fish displays incremental suggestions as the user types, based on command history and the current directory. This functions similarly to Bash's Ctrl+R history search, but is always on, giving the user continuous feedback while typing commands. fish also includes feature-rich tab completion, with support for expanding file paths (with wildcards and brace expansion), environment variables, and command-specific completions. Command-specific completions, including options with descriptions, can be to some extent generated from the commands' man pages, but custom completions can also be included with software or written by users of the shell.

The creator of fish preferred to add new features as commands rather than syntax. This made features more discoverable, as the built-in features allow searching commands with options and help texts. Functions can also include human readable descriptions. A special *help* command gives access to all the fish documentation in the user's web browser.

## Syntax

The syntax resembles a POSIX compatible shell (such as Bash), but deviates in many ways

```mw
# Variable assignment
#
# Set the variable 'foo' to the value 'bar'.
# fish doesn't use the = operator, which is inherently whitespace sensitive.
# The 'set' command extends to work with arrays, scoping, etc.

> set foo bar
> echo $foo
bar

# Command substitution
#
# Assign the output of the command 'pwd' into the variable 'wd'.
# fish doesn't use backticks (``), which can't be nested and may be confused with single quotes (' ').

> set wd (pwd)
> set wd $(pwd) # since version 3.4
> echo $wd
~

# Array variables. 'A' becomes an array with 5 values:
> set A 3 5 7 9 12
# Array slicing. 'B' becomes the first two elements of 'A':
> set B $A[1 2]
> echo $B
3 5
# You can index with other arrays and even command
# substitution output:
> echo $A[(seq 3)]
3 5 7
# Erase the third and fifth elements of 'A'
> set --erase A[$B]
> echo $A
3 5 9

# for-loop, convert jpegs to pngs
> for i in *.jpg
      convert $i (basename $i .jpg).png
  end

# fish supports multi-line history and editing.
# Semicolons work like newlines:
> for i in *.jpg; convert $i (basename $i .jpg).png; end

# while-loop, read lines /etc/passwd and output the fifth
# colon-separated field from the file. This should be
# the user description.
> while read line
      set arr (echo $line|tr : \n)
      echo $arr[5]
  end < /etc/passwd

# String replacement (replacing all i by I)
> string replace -a "i" "I" "Wikipedia"
WIkIpedIa
```

### No implicit subshell

Some language constructs, like pipelines, functions and loops, have been implemented using so called subshells in other shell languages. Subshells are child programs that run a few commands to perform a task, then exit back to the parent shell. This implementation detail typically has the side effect that any state changes made in the subshell, such as variable assignments, do not propagate to the main shell. fish never creates subshells for language features; all builtins happen within the parent shell.

```mw
# This will not work in many other shells, since the 'read' builtin
# will run in its own subshell. In Bash, the right side of the pipe
# can't have any side effects. In ksh, the below command works, but
# the left side can't have any side effects. In fish and zsh, both
# sides can have side effects.
> cat *.txt | read line
```

#### Variable assignment example

This Bash example doesn't do what it seems: because the loop body is a subshell, the update to `$found` is not persistent.

```mw
found=''
cat /etc/fstab | while read dev mnt rest; do
  if test "$mnt" = "/"; then
    found="$dev"
  fi
done
```

Workaround:

```mw
found=''
while read dev mnt rest; do
  if test "$mnt" = "/"; then
    found="$dev"
  fi
done < /etc/fstab
```

Fish example:

```mw
set found ''
cat /etc/fstab | while read dev mnt rest
  if test "$mnt" = "/"
    set found $dev
  end
end
```

## Universal variables

fish has a feature known as universal variables, which allows a user to permanently assign a value to a variable across all the user's running fish shells. The variable value is remembered across logouts and reboots, and updates are immediately propagated to all running shells.

```mw
# This will make emacs the default text editor. The '--universal' (or '-U') tells fish to
# make this a universal variable.
> set --universal EDITOR emacs

# This command will make the current working directory part of the fish
# prompt turn blue on all running fish instances.
> set --universal fish_color_cwd blue
```

## Other features

- Advanced tab completion (with support for writing custom completions).
- Syntax highlighting with extensive error checking.
- Support for the X clipboard.
- Smart terminal handling based on terminfo.
- Searchable command history.
- Web-based configuration (fish_config).

## Bash/fish translation table

| Feature | Bash syntax | fish syntax | Comment |
|---|---|---|---|
| variable expansion: with word splitting and glob interpretation | $var or ${var[@]} or ${var[*]} | deliberately omitted | Identified as a primary cause of bugs in posix compatible shell languages |
| variable expansion: scalar | "$var" | deliberately omitted | Every variable is an array |
| variable expansion: array | "${var[@]}" | $var | Quoting not necessary to suppress word splitting and glob interpretation. Instead, quoting signifies serialization. |
| variable expansion: as a space separated string | "${var[*]}" | "$var" |   |
| edit line in text editor | Ctrl+X,Ctrl+E | Alt+E | Upon invocation, moves line input to a text editor |
| evaluate line input | Ctrl+Alt+E | —N/a | Evaluates expressions in-place on the line editor |
| history completion | Ctrl+R | implicit |   |
| history substitution | !! | deliberately omitted | Not discoverable |
| explicit subshell | (expression) | fish -c expression |   |
| command substitution | "$(expression)" | `"$(expression)"` or `(expression \| string collect)` |   |
| process substitution | <(expression) | (expression \| psub) | Command, not syntax |
| logical operators | !cmd && echo FAIL \|\| echo OK | not command and echo FAIL or echo OK |   |
| variable assignment | var=value | set var value |   |
| string processing: replace | "${HOME/alice/bob}" | string replace alice bob $HOME |   |
| string processing: remove prefix or suffix pattern, non-greedily or greedily | var=a.b.c "${var#*.}" #b.c "${var##*.}" #c "${var%.*}" #a.b "${var%%.*}" #a | string replace --regex '.*?\.(.*)' '$1' a.b.c #b.c string replace --regex '.*\.(.*)' '$1' a.b.c #c string replace --regex '(.*)\..*' '$1' a.b.c #a.b string replace --regex '(.*?)\..*' '$1' a.b.c #a |   |
| export variable | export var | set --export var | Options discoverable via tab completion |
| function-local variable | local var | by default |   |
| scope-local variable | no equivalent | set --local var |   |
| remove variable | unset var | set --erase var |   |
| check if a variable exists | test -v var | set --query var |   |
| array initialization | var=( a b c ) | set var a b c | Every variable is an array |
| array iteration | for i in "${var[@]}"; do echo "$i" done | for i in $var echo $i end |   |
| argument vector: all arguments | "$@" | $argv |   |
| argument vector: indexing | "$1" | $argv[1] |   |
| argument vector: length | $# | (count $argv) |   |
| argument vector: shift | shift | set --erase argv[1] |   |
| array representation in environment variables | PATH="$PATH:$HOME/.local/bin" | set PATH $PATH $HOME/.local/bin | fish assumes colon as array delimiter for translating variables to and from the environment. This aligns with many array-like environment variables, like $PATH and $LS_COLORS. |
| export and run | LANG=C.UTF-8 python3 | env LANG=C.UTF-8 python3 | `env LANG=C.UTF-8 python3` works in any shell, as env is a standalone program. |
| arithmetic | $((10/3)) | math '10/3' | `expr 10 / 3` works in any shell, as expr is a standalone program. |
| escape sequence | $'\e' | \e | `printf '\e'` works in both shells; their `printf` builtins are both compatible with the GNU `printf` standalone program. |
| single quoted string: escape sequences | 'mom'\''s final backslash: \' | 'mom\'s final backslash: \\' | Bash only requires replacement of the single quote itself in single quoted strings, but the replacement is 4 characters long. The same replacement works in fish, but fish supports a regular escape sequence for this, thus requires escaping backslashes too (except permits single backslashes that don't precede another backslash or single quote). |
