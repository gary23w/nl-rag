---
title: "Bash Reference Manual (part 3/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 3/15
---

# Bash Reference Manual

**`~-*N*`**

The string that would be displayed by ‘dirs -*N*’.

Bash also performs tilde expansion on words satisfying the conditions of variable assignments (see Shell Parameters) when they appear as arguments to simple commands. Bash does not do this, except for the declaration commands listed above, when in POSIX mode.

#### 3.5.3 Shell Parameter Expansion

The ‘$’ character introduces parameter expansion, command substitution, or arithmetic expansion. The parameter name or symbol to be expanded may be enclosed in braces, which are optional but serve to protect the variable to be expanded from characters immediately following it which could be interpreted as part of the name. For example, if the first positional parameter has the value ‘a’, then `${11}` expands to the value of the eleventh positional parameter, while `$11` expands to ‘a1’.

When braces are used, the matching ending brace is the first ‘}’ not escaped by a backslash or within a quoted string, and not within an embedded arithmetic expansion, command substitution, or parameter expansion.

The basic form of parameter expansion is ${*parameter*}, which substitutes the value of *parameter*. The *parameter* is a shell parameter as described above (see Shell Parameters) or an array reference (see Arrays). The braces are required when *parameter* is a positional parameter with more than one digit, or when *parameter* is followed by a character that is not to be interpreted as part of its name.

If the first character of *parameter* is an exclamation point (!), and *parameter* is not a nameref, it introduces a level of indirection. Bash uses the value formed by expanding the rest of *parameter* as the new *parameter*; this new parameter is then expanded and that value is used in the rest of the expansion, rather than the expansion of the original *parameter*. This is known as `indirect expansion`. The value is subject to tilde expansion, parameter expansion, command substitution, and arithmetic expansion. If *parameter* is a nameref, this expands to the name of the variable referenced by *parameter* instead of performing the complete indirect expansion, for compatibility. The exceptions to this are the expansions of ${!*prefix**} and ${!*name*[@]} described below. The exclamation point must immediately follow the left brace in order to introduce indirection.

In each of the cases below, *word* is subject to tilde expansion, parameter expansion, command substitution, and arithmetic expansion.

When not performing substring expansion, using the forms described below (e.g., ‘:-’), Bash tests for a parameter that is unset or null. Omitting the colon results in a test only for a parameter that is unset. Put another way, if the colon is included, the operator tests for both *parameter*’s existence and that its value is not null; if the colon is omitted, the operator tests only for existence.

**`${*parameter*:−*word*}`**

If *parameter* is unset or null, the expansion of *word* is substituted. Otherwise, the value of *parameter* is substituted.

```
$ v=123
$ echo ${v-unset}
123
$ echo ${v:-unset-or-null}
123
$ unset v
$ echo ${v-unset}
unset
$ v=
$ echo ${v-unset}

$ echo ${v:-unset-or-null}
unset-or-null
```

**`${*parameter*:=*word*}`**

If *parameter* is unset or null, the expansion of *word* is assigned to *parameter*, and the result of the expansion is the final value of *parameter*. Positional parameters and special parameters may not be assigned in this way.

```
$ unset var
$ : ${var=DEFAULT}
$ echo $var
DEFAULT
$ var=
$ : ${var=DEFAULT}
$ echo $var

$ var=
$ : ${var:=DEFAULT}
$ echo $var
DEFAULT
$ unset var
$ : ${var:=DEFAULT}
$ echo $var
DEFAULT
```

**`${*parameter*:?*word*}`**

If *parameter* is null or unset, the shell writes the expansion of *word* (or a message to that effect if *word* is not present) to the standard error and, if it is not interactive, exits with a non-zero status. An interactive shell does not exit, but does not execute the command associated with the expansion. Otherwise, the value of *parameter* is substituted.

```
$ var=
$ : ${var:?var is unset or null}
bash: var: var is unset or null
$ echo ${var?var is unset}

$ unset var
$ : ${var?var is unset}
bash: var: var is unset
$ : ${var:?var is unset or null}
bash: var: var is unset or null
$ var=123
$ echo ${var:?var is unset or null}
123
```

**`${*parameter*:+*word*}`**

If *parameter* is null or unset, nothing is substituted, otherwise the expansion of *word* is substituted. The value of *parameter* is not used.

```
$ var=123
$ echo ${var:+var is set and not null}
var is set and not null
$ echo ${var+var is set}
var is set
$ var=
$ echo ${var:+var is set and not null}

$ echo ${var+var is set}
var is set
$ unset var
$ echo ${var+var is set}

$ echo ${var:+var is set and not null}

$ 
```

**`${*parameter*:*offset*}`**

**`${*parameter*:*offset*:*length*}`**

This is referred to as Substring Expansion. It expands to up to *length* characters of the value of *parameter* starting at the character specified by *offset*. If *parameter* is ‘@’ or ‘*’, an indexed array subscripted by ‘@’ or ‘*’, or an associative array name, the results differ as described below. If :*length* is omitted (the first form above), this expands to the substring of the value of *parameter* starting at the character specified by *offset* and extending to the end of the value. If *offset* is omitted, it is treated as 0. If *length* is omitted, but the colon after *offset* is present, it is treated as 0. *length* and *offset* are arithmetic expressions (see Shell Arithmetic).

If *offset* evaluates to a number less than zero, the value is used as an offset in characters from the end of the value of *parameter*. If *length* evaluates to a number less than zero, it is interpreted as an offset in characters from the end of the value of *parameter* rather than a number of characters, and the expansion is the characters between *offset* and that result.

Note that a negative offset must be separated from the colon by at least one space to avoid being confused with the ‘:-’ expansion.

Here are some examples illustrating substring expansion on parameters and subscripted arrays:

```
$ string=01234567890abcdefgh
$ echo ${string:7}
7890abcdefgh
$ echo ${string:7:0}

$ echo ${string:7:2}
78
$ echo ${string:7:-2}
7890abcdef
$ echo ${string: -7}
bcdefgh
$ echo ${string: -7:0}

$ echo ${string: -7:2}
bc
$ echo ${string: -7:-2}
bcdef
$ set -- 01234567890abcdefgh
$ echo ${1:7}
7890abcdefgh
$ echo ${1:7:0}

$ echo ${1:7:2}
78
$ echo ${1:7:-2}
7890abcdef
$ echo ${1: -7}
bcdefgh
$ echo ${1: -7:0}

$ echo ${1: -7:2}
bc
$ echo ${1: -7:-2}
bcdef
$ array[0]=01234567890abcdefgh
$ echo ${array[0]:7}
7890abcdefgh
$ echo ${array[0]:7:0}

$ echo ${array[0]:7:2}
78
$ echo ${array[0]:7:-2}
7890abcdef
$ echo ${array[0]: -7}
bcdefgh
$ echo ${array[0]: -7:0}

$ echo ${array[0]: -7:2}
bc
$ echo ${array[0]: -7:-2}
bcdef
```

If *parameter* is ‘@’ or ‘*’, the result is *length* positional parameters beginning at *offset*. A negative *offset* is taken relative to one greater than the greatest positional parameter, so an offset of -1 evaluates to the last positional parameter (or 0 if there are no positional parameters). It is an expansion error if *length* evaluates to a number less than zero.

The following examples illustrate substring expansion using positional parameters:

```
$ set -- 1 2 3 4 5 6 7 8 9 0 a b c d e f g h
$ echo ${@:7}
7 8 9 0 a b c d e f g h
$ echo ${@:7:0}

$ echo ${@:7:2}
7 8
$ echo ${@:7:-2}
bash: -2: substring expression < 0
$ echo ${@: -7:2}
b c
$ echo ${@:0}
./bash 1 2 3 4 5 6 7 8 9 0 a b c d e f g h
$ echo ${@:0:2}
./bash 1
$ echo ${@: -7:0}
```

If *parameter* is an indexed array name subscripted by ‘@’ or ‘*’, the result is the *length* members of the array beginning with `${*parameter*[*offset*]}`. A negative *offset* is taken relative to one greater than the maximum index of the specified array. It is an expansion error if *length* evaluates to a number less than zero.

These examples show how you can use substring expansion with indexed arrays:

```
$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
$ echo ${array[@]:7}
7 8 9 0 a b c d e f g h
$ echo ${array[@]:7:2}
7 8
$ echo ${array[@]: -7:2}
b c
$ echo ${array[@]: -7:-2}
bash: -2: substring expression < 0
$ echo ${array[@]:0}
0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h
$ echo ${array[@]:0:2}
0 1
$ echo ${array[@]: -7:0}
```

Substring expansion applied to an associative array produces undefined results.

Substring indexing is zero-based unless the positional parameters are used, in which case the indexing starts at 1 by default. If *offset* is 0, and the positional parameters are used, `$0` is prefixed to the list.

**`${!*prefix**}`**

**`${!*prefix*@}`**

Expands to the names of variables whose names begin with *prefix*, separated by the first character of the `IFS` special variable. When ‘@’ is used and the expansion appears within double quotes, each variable name expands to a separate word.

**`${!*name*[@]}`**

**`${!*name*[*]}`**

If *name* is an array variable, expands to the list of array indices (keys) assigned in *name*. If *name* is not an array, expands to 0 if *name* is set and null otherwise. When ‘@’ is used and the expansion appears within double quotes, each key expands to a separate word.

**`${#*parameter*}`**

Substitutes the length in characters of the value of *parameter*. If *parameter* is ‘*’ or ‘@’, the value substituted is the number of positional parameters. If *parameter* is an array name subscripted by ‘*’ or ‘@’, the value substituted is the number of elements in the array. If *parameter* is an indexed array name subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of *parameter*, so negative indices count back from the end of the array, and an index of -1 references the last element.

**`${*parameter*#*word*}`**

**`${*parameter*##*word*}`**

The *word* is expanded to produce a pattern and matched against the expanded value of *parameter* according to the rules described below (see Pattern Matching). If the pattern matches the beginning of the expanded value of *parameter*, then the result of the expansion is the expanded value of *parameter* with the shortest matching pattern (the ‘#’ case) or the longest matching pattern (the ‘##’ case) deleted. If *parameter* is ‘@’ or ‘*’, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list. If *parameter* is an array variable subscripted with ‘@’ or ‘*’, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

**`${*parameter*%*word*}`**

**`${*parameter*%%*word*}`**

The *word* is expanded to produce a pattern and matched against the expanded value of *parameter* according to the rules described below (see Pattern Matching). If the pattern matches a trailing portion of the expanded value of *parameter*, then the result of the expansion is the value of *parameter* with the shortest matching pattern (the ‘%’ case) or the longest matching pattern (the ‘%%’ case) deleted. If *parameter* is ‘@’ or ‘*’, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list. If *parameter* is an array variable subscripted with ‘@’ or ‘*’, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

**`${*parameter*/*pattern*/*string*}`**

**`${*parameter*//*pattern*/*string*}`**

**`${*parameter*/#*pattern*/*string*}`**

**`${*parameter*/%*pattern*/*string*}`**

The *pattern* is expanded to produce a pattern and matched against the expanded value of *parameter* as described below (see Pattern Matching). The longest match of *pattern* in the expanded value is replaced with *string*. *string* undergoes tilde expansion, parameter and variable expansion, arithmetic expansion, command and process substitution, and quote removal.

In the first form above, only the first match is replaced. If there are two slashes separating *parameter* and *pattern* (the second form above), all matches of *pattern* are replaced with *string*. If *pattern* is preceded by ‘#’ (the third form above), it must match at the beginning of the expanded value of *parameter*. If *pattern* is preceded by ‘%’ (the fourth form above), it must match at the end of the expanded value of *parameter*.

If the expansion of *string* is null, matches of *pattern* are deleted and the ‘/’ following *pattern* may be omitted.

If the `patsub_replacement` shell option is enabled using `shopt` (see The Shopt Builtin), any unquoted instances of ‘&’ in *string* are replaced with the matching portion of *pattern*. This is intended to duplicate a common `sed` idiom.

Quoting any part of *string* inhibits replacement in the expansion of the quoted portion, including replacement strings stored in shell variables. Backslash escapes ‘&’ in *string*; the backslash is removed in order to permit a literal ‘&’ in the replacement string. Users should take care if *string* is double-quoted to avoid unwanted interactions between the backslash and double-quoting, since backslash has special meaning within double quotes. Pattern substitution performs the check for unquoted ‘&’ after expanding *string*, so users should ensure to properly quote any occurrences of ‘&’ they want to be taken literally in the replacement and ensure any instances of ‘&’ they want to be replaced are unquoted.

For instance,

```
var=abcdef
rep='& '
echo ${var/abc/& }
echo "${var/abc/& }"
echo ${var/abc/$rep}
echo "${var/abc/$rep}"
```

will display four lines of "abc def", while

```
var=abcdef
rep='& '
echo ${var/abc/\& }
echo "${var/abc/\& }"
echo ${var/abc/"& "}
echo ${var/abc/"$rep"}
```

will display four lines of "& def". Like the pattern removal operators, double quotes surrounding the replacement string quote the expanded characters, while double quotes enclosing the entire parameter substitution do not, since the expansion is performed in a context that doesn’t take any enclosing double quotes into account.

Since backslash can escape ‘&’, it can also escape a backslash in the replacement string. This means that ‘\\’ will insert a literal backslash into the replacement, so these two `echo` commands

```
var=abcdef
rep='\\&xyz'
echo ${var/abc/\\&xyz}
echo ${var/abc/$rep}
```

will both output ‘\abcxyzdef’.

It should rarely be necessary to enclose only *string* in double quotes.

If the `nocasematch` shell option (see the description of `shopt` in The Shopt Builtin) is enabled, the match is performed without regard to the case of alphabetic characters.

If *parameter* is ‘@’ or ‘*’, the substitution operation is applied to each positional parameter in turn, and the expansion is the resultant list. If *parameter* is an array variable subscripted with ‘@’ or ‘*’, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list.

**`${*parameter*^*pattern*}`**

**`${*parameter*^^*pattern*}`**

**`${*parameter*,*pattern*}`**

**`${*parameter*,,*pattern*}`**

This expansion modifies the case of alphabetic characters in *parameter*. First, the *pattern* is expanded to produce a pattern as described below in Pattern Matching.

`Bash` then examines characters in the expanded value of *parameter* against *pattern* as described below. If a character matches the pattern, its case is converted. The pattern should not attempt to match more than one character.

Using ‘^’ converts lowercase letters matching *pattern* to uppercase; ‘,’ converts matching uppercase letters to lowercase. The ‘^’ and ‘,’ variants examine the first character in the expanded value and convert its case if it matches *pattern*; the ‘^^’ and ‘,,’ variants examine all characters in the expanded value and convert each one that matches *pattern*. If *pattern* is omitted, it is treated like a ‘?’, which matches every character.

If *parameter* is ‘@’ or ‘*’, the case modification operation is applied to each positional parameter in turn, and the expansion is the resultant list. If *parameter* is an array variable subscripted with ‘@’ or ‘*’, the case modification operation is applied to each member of the array in turn, and the expansion is the resultant list.

**`${*parameter*@*operator*}`**

The expansion is either a transformation of the value of *parameter* or information about *parameter* itself, depending on the value of *operator*. Each *operator* is a single letter:

**`U`**

The expansion is a string that is the value of *parameter* with lowercase alphabetic characters converted to uppercase.

**`u`**

The expansion is a string that is the value of *parameter* with the first character converted to uppercase, if it is alphabetic.

**`L`**

The expansion is a string that is the value of *parameter* with uppercase alphabetic characters converted to lowercase.

**`Q`**

The expansion is a string that is the value of *parameter* quoted in a format that can be reused as input.

**`E`**

The expansion is a string that is the value of *parameter* with backslash escape sequences expanded as with the `$'…'` quoting mechanism.

**`P`**

The expansion is a string that is the result of expanding the value of *parameter* as if it were a prompt string (see Controlling the Prompt).

**`A`**

The expansion is a string in the form of an assignment statement or `declare` command that, if evaluated, recreates *parameter* with its attributes and value.

**`K`**

Produces a possibly-quoted version of the value of *parameter*, except that it prints the values of indexed and associative arrays as a sequence of quoted key-value pairs (see Arrays). The keys and values are quoted in a format that can be reused as input.

**`a`**

The expansion is a string consisting of flag values representing *parameter*’s attributes.

**`k`**

Like the ‘K’ transformation, but expands the keys and values of indexed and associative arrays to separate words after word splitting.

If *parameter* is ‘@’ or ‘*’, the operation is applied to each positional parameter in turn, and the expansion is the resultant list. If *parameter* is an array variable subscripted with ‘@’ or ‘*’, the operation is applied to each member of the array in turn, and the expansion is the resultant list.

The result of the expansion is subject to word splitting and filename expansion as described below.

#### 3.5.4 Command Substitution

Command substitution allows the output of a command to replace the command itself. The standard form of command substitution occurs when a command is enclosed as follows:

```
$(command)
```

or (deprecated)

```
`command`.
```

Bash performs command substitution by executing *command* in a subshell environment and replacing the command substitution with the standard output of the command, with any trailing newlines deleted. Embedded newlines are not deleted, but they may be removed during word splitting. The command substitution `$(cat *file*)` can be replaced by the equivalent but faster `$(< *file*)`.

With the old-style backquote form of substitution, backslash retains its literal meaning except when followed by ‘$’, ‘`’, or ‘\’. The first backquote not preceded by a backslash terminates the command substitution. When using the `$(*command*)` form, all characters between the parentheses make up the command; none are treated specially.

There is an alternate form of command substitution:

```
${c command; }
```

which executes *command* in the current execution environment and captures its output, again with trailing newlines removed.

The character *c* following the open brace must be a space, tab, newline, or ‘|’, and the close brace must be in a position where a reserved word may appear (i.e., preceded by a command terminator such as semicolon). Bash allows the close brace to be joined to the remaining characters in the word without being followed by a shell metacharacter as a reserved word would usually require.

Any side effects of *command* take effect immediately in the current execution environment and persist in the current environment after the command completes (e.g., the `exit` builtin exits the shell).

This type of command substitution superficially resembles executing an unnamed shell function: local variables are created as when a shell function is executing, and the `return` builtin forces *command* to complete; however, the rest of the execution environment, including the positional parameters, is shared with the caller.

If the first character following the open brace is a ‘|’, the construct expands to the value of the `REPLY` shell variable after *command* executes, without removing any trailing newlines, and the standard output of *command* remains the same as in the calling shell. Bash creates `REPLY` as an initially-unset local variable when *command* executes, and restores `REPLY` to the value it had before the command substitution after *command* completes, as with any local variable.

For example, this construct expands to ‘12345’, and leaves the shell variable `X` unchanged in the current execution environment:

```
${ local X=12345 ; echo $X; }
```

(not declaring `X` as local would modify its value in the current environment, as with normal shell function execution), while this construct does not require any output to expand to ‘12345’:

```
${| REPLY=12345; }
```

and restores `REPLY` to the value it had before the command substitution.

Command substitutions may be nested. To nest when using the backquoted form, escape the inner backquotes with backslashes.

If the substitution appears within double quotes, Bash does not perform word splitting and filename expansion on the results.

#### 3.5.5 Arithmetic Expansion

Arithmetic expansion evaluates an arithmetic expression and substitutes the result. The format for arithmetic expansion is:

```
$(( expression ))
```

The *expression* undergoes the same expansions as if it were within double quotes, but unescaped double quote characters in *expression* are not treated specially and are removed. All tokens in the expression undergo parameter and variable expansion, command substitution, and quote removal. The result is treated as the arithmetic expression to be evaluated. Since the way Bash handles double quotes can potentially result in empty strings, arithmetic expansion treats those as expressions that evaluate to 0. Arithmetic expansions may be nested.

The evaluation is performed according to the rules listed below (see Shell Arithmetic). If the expression is invalid, Bash prints a message indicating failure to the standard error, does not perform the substitution, and does not execute the command associated with the expansion.

#### 3.5.6 Process Substitution

Process substitution allows a process’s input or output to be referred to using a filename. It takes the form of

```
<(list)
```

or

```
>(list)
```

The process *list* is run asynchronously, and its input or output appears as a filename. This filename is passed as an argument to the current command as the result of the expansion.

If the `>(*list*)` form is used, writing to the file provides input for *list*. If the `<(*list*)` form is used, reading the file obtains the output of *list*. Note that no space may appear between the `<` or `>` and the left parenthesis, otherwise the construct would be interpreted as a redirection.

Process substitution is supported on systems that support named pipes (FIFOs) or the /dev/fd method of naming open files.

When available, process substitution is performed simultaneously with parameter and variable expansion, command substitution, and arithmetic expansion.

#### 3.5.7 Word Splitting

The shell scans the results of parameter expansion, command substitution, and arithmetic expansion that did not occur within double quotes for word splitting. Words that were not expanded are not split.

The shell treats each character of `$IFS` as a delimiter, and splits the results of the other expansions into fields using these characters as field terminators.

An *IFS whitespace* character is whitespace as defined above (see Definitions) that appears in the value of `IFS`. Space, tab, and newline are always considered IFS whitespace, even if they don’t appear in the locale’s `space` category.

If `IFS` is unset, word splitting behaves as if its value were `<space><tab><newline>`, and treats these characters as IFS whitespace. If the value of `IFS` is null, no word splitting occurs, but implicit null arguments (see below) are still removed.

Word splitting begins by removing sequences of IFS whitespace characters from the beginning and end of the results of the previous expansions, then splits the remaining words.

If the value of `IFS` consists solely of IFS whitespace, any sequence of IFS whitespace characters delimits a field, so a field consists of characters that are not unquoted IFS whitespace, and null fields result only from quoting.

If `IFS` contains a non-whitespace character, then any character in the value of `IFS` that is not IFS whitespace, along with any adjacent IFS whitespace characters, delimits a field. This means that adjacent non-IFS-whitespace delimiters produce a null field. A sequence of IFS whitespace characters also delimits a field.

Explicit null arguments (`""` or `''`) are retained and passed to commands as empty strings. Unquoted implicit null arguments, resulting from the expansion of parameters that have no values, are removed. Expanding a parameter with no value within double quotes produces a null field, which is retained and passed to a command as an empty string.

When a quoted null argument appears as part of a word whose expansion is non-null, word splitting removes the null argument portion, leaving the non-null expansion. That is, the word `-d''` becomes `-d` after word splitting and null argument removal.

#### 3.5.8 Filename Expansion

After word splitting, unless the -f option has been set (see The Set Builtin), Bash scans each word for the characters ‘*’, ‘?’, and ‘[’. If one of these characters appears, and is not quoted, then the word is regarded as a *pattern*, and replaced with a sorted list of filenames matching the pattern (see Pattern Matching), subject to the value of the `GLOBSORT` shell variable (see Bash Variables).

If no matching filenames are found, and the shell option `nullglob` is disabled, the word is left unchanged. If the `nullglob` option is set, and no matches are found, the word is removed. If the `failglob` shell option is set, and no matches are found, Bash prints an error message and does not execute the command. If the shell option `nocaseglob` is enabled, the match is performed without regard to the case of alphabetic characters.

When a pattern is used for filename expansion, the character ‘.’ at the start of a filename or immediately following a slash must be matched explicitly, unless the shell option `dotglob` is set. In order to match the filenames . and .., the pattern must begin with ‘.’ (for example, ‘.?’), even if `dotglob` is set. If the `globskipdots` shell option is enabled, the filenames . and .. never match, even if the pattern begins with a ‘.’. When not matching filenames, the ‘.’ character is not treated specially.

When matching a filename, the slash character must always be matched explicitly by a slash in the pattern, but in other matching contexts it can be matched by a special pattern character as described below (see Pattern Matching).

See the description of `shopt` in The Shopt Builtin, for a description of the `nocaseglob`, `nullglob`, `globskipdots`, `failglob`, and `dotglob` options.

The `GLOBIGNORE` shell variable may be used to restrict the set of file names matching a pattern. If `GLOBIGNORE` is set, each matching file name that also matches one of the patterns in `GLOBIGNORE` is removed from the list of matches. If the `nocaseglob` option is set, the matching against the patterns in `GLOBIGNORE` is performed without regard to case. The filenames . and .. are always ignored when `GLOBIGNORE` is set and not null. However, setting `GLOBIGNORE` to a non-null value has the effect of enabling the `dotglob` shell option, so all other filenames beginning with a ‘.’ match. To get the old behavior of ignoring filenames beginning with a ‘.’, make ‘.*’ one of the patterns in `GLOBIGNORE`. The `dotglob` option is disabled when `GLOBIGNORE` is unset. The `GLOBIGNORE` pattern matching honors the setting of the `extglob` shell option.

The value of the `GLOBSORT` shell variable controls how the results of pathname expansion are sorted, as described below (see Bash Variables).

#### 3.5.8.1 Pattern Matching

Any character that appears in a pattern, other than the special pattern characters described below, matches itself. The NUL character may not occur in a pattern. A backslash escapes the following character; the escaping backslash is discarded when matching. The special pattern characters must be quoted if they are to be matched literally.

The special pattern characters have the following meanings:
