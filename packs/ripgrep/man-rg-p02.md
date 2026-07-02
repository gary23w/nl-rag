---
title: "rg(1) (part 2/2)"
source: https://man.archlinux.org/man/rg.1
domain: ripgrep
license: CC-BY-SA-4.0
tags: ripgrep search, string searching, recursive grep, command-line search
fetched: 2026-07-02
part: 2/2
---

## OUTPUT OPTIONS

**-A** *NUM*, **--after-context**=*NUM*

Show

NUM

lines after each match.

This overrides the **--passthru** flag and partially overrides the **-C/--context** flag.

**-B** *NUM*, **--before-context**=*NUM*

Show

NUM

lines before each match.

This overrides the **--passthru** flag and partially overrides the **-C/--context** flag.

**--block-buffered**

When enabled, ripgrep will use block buffering. That is, whenever a matching line is found, it will be written to an in-memory buffer and will not be written to stdout until the buffer reaches a certain size. This is the default when ripgrep's stdout is redirected to a pipeline or a file. When ripgrep's stdout is connected to a tty, line buffering will be used by default. Forcing block buffering can be useful when dumping a large amount of contents to a tty.

This overrides the **--line-buffered** flag.

This flag can be disabled with **--no-block-buffered**.

**-b**, **--byte-offset**

Print the 0-based byte offset within the input file before each line of output. If

-o/--only-matching

is specified, print the offset of the matched text itself.

If ripgrep does transcoding, then the byte offset is in terms of the result of transcoding and not the original data. This applies similarly to other transformations on the data, such as decompression or a **--pre** filter.

This flag can be disabled with **--no-byte-offset**.

**--color**=*WHEN*

This flag controls when to use colors. The default setting is

auto

, which means ripgrep will try to guess when to use colors. For example, if ripgrep is printing to a tty, then it will use colors, but if it is redirected to a file or a pipe, then it will suppress color output.

ripgrep will suppress color output by default in some other circumstances as well. These include, but are not limited to:

- When the **TERM** environment variable is not set or set to **dumb**.
- When the **NO_COLOR** environment variable is set (regardless of value).
- When flags that imply no use for colors are given. For example, **--vimgrep** and **--json**.

The possible values for this flag are:

****never****

Colors will never be used.

****auto****

The default. ripgrep tries to be smart.

****always****

Colors will always be used regardless of where output is sent.

****ansi****

Like 'always', but emits ANSI escapes (even in a Windows console).

This flag also controls whether hyperlinks are emitted. For example, when a hyperlink format is specified, hyperlinks won't be used when color is suppressed. If one wants to emit hyperlinks but no colors, then one must use the **--colors** flag to manually set all color styles to **none**:

```
    --colors 'path:none' \
    --colors 'line:none' \
    --colors 'column:none' \
    --colors 'match:none' \
    --colors 'highlight:none'
```

**--colors**=*COLOR_SPEC*

This flag specifies color settings for use in the output. This flag may be provided multiple times. Settings are applied iteratively. Pre-existing color labels are limited to one of eight choices:

red

,

blue

,

green

,

cyan

,

magenta

,

yellow

,

white

and

black

. Styles are limited to

nobold

,

bold

,

nointense

,

intense

,

nounderline

,

underline

,

noitalic

or

italic

.

The format of the flag is **{***type***}:{***attribute***}:{***value***}**. *type* should be one of **path**, **line**, **column**, **highlight** or **match**. *attribute* can be **fg**, **bg** or **style**. *value* is either a color (for **fg** and **bg**) or a text style. A special format, **{***type***}:none**, will clear all color settings for *type*.

For example, the following command will change the match color to magenta and the background color for line numbers to yellow:

```
    rg --colors 'match:fg:magenta' --colors 'line:bg:yellow'
```

Another example, the following command will "highlight" the non-matching text in matching lines:

```
    rg --colors 'highlight:bg:yellow' --colors 'highlight:fg:black'
```

The "highlight" color type is particularly useful for contrasting matching lines with surrounding context printed by the **-B/--before-context**, **-A/--after-context**, **-C/--context** or **--passthru** flags.

Extended colors can be used for *value* when the tty supports ANSI color sequences. These are specified as either *x* (256-color) or *x***,***x***,***x* (24-bit truecolor) where *x* is a number between **0** and **255** inclusive. *x* may be given as a normal decimal number or a hexadecimal number, which is prefixed by **0x**.

For example, the following command will change the match background color to that represented by the rgb value (0,128,255):

```
    rg --colors 'match:bg:0,128,255'
```

or, equivalently,

```
    rg --colors 'match:bg:0x0,0x80,0xFF'
```

Note that the **intense** and **nointense** styles will have no effect when used alongside these extended color codes.

**--column**

Show column numbers (1-based). This only shows the column numbers for the first match on each line. This does not try to account for Unicode. One byte is equal to one column. This implies

-n/--line-number

.

When **-o/--only-matching** is used, then the column numbers written correspond to the start of each match.

This flag can be disabled with **--no-column**.

**-C** *NUM*, **--context**=*NUM*

Show

NUM

lines before and after each match. This is equivalent to providing both the

-B/--before-context

and

-A/--after-context

flags with the same value.

This overrides the **--passthru** flag. The **-A/--after-context** and **-B/--before-context** flags both partially override this flag, regardless of the order. For example, **-A2 -C1** is equivalent to **-A2 -B1**.

**--context-separator**=*SEPARATOR*

The string used to separate non-contiguous context lines in the output. This is only used when one of the context flags is used (that is,

-A/--after-context

,

-B/--before-context

or

-C/--context

). Escape sequences like

\x7F

or

\t

may be used. The default value is

--

.

When the context separator is set to an empty string, then a line break is still inserted. To completely disable context separators, use the **--no-context-separator** flag.

**--field-context-separator**=*SEPARATOR*

Set the field context separator. This separator is only used when printing contextual lines. It is used to delimit file paths, line numbers, columns and the contextual line itself. The separator may be any number of bytes, including zero. Escape sequences like

\x7F

or

\t

may be used.

The **-** character is the default value.

**--field-match-separator**=*SEPARATOR*

Set the field match separator. This separator is only used when printing matching lines. It is used to delimit file paths, line numbers, columns and the matching line itself. The separator may be any number of bytes, including zero. Escape sequences like

\x7F

or

\t

may be used.

The **:** character is the default value.

**--heading**

This flag prints the file path above clusters of matches from each file instead of printing the file path as a prefix for each matched line.

This is the default mode when printing to a tty.

When **stdout** is not a tty, then ripgrep will default to the standard grep-like format. One can force this format in Unix-like environments by piping the output of ripgrep to **cat**. For example, **rg** *foo* **|** **cat**.

This flag can be disabled with **--no-heading**.

**-h**, **--help**

This flag prints the help output for ripgrep.

Unlike most other flags, the behavior of the short flag, **-h**, and the long flag, **--help**, is different. The short flag will show a condensed help output while the long flag will show a verbose help output. The verbose help output has complete documentation, where as the condensed help output will show only a single line for every flag.

**--hostname-bin**=*COMMAND*

This flag controls how ripgrep determines this system's hostname. The flag's value should correspond to an executable (either a path or something that can be found via your system's

PATH

environment variable). When set, ripgrep will run this executable, with no arguments, and treat its output (with leading and trailing whitespace stripped) as your system's hostname.

When not set (the default, or the empty string), ripgrep will try to automatically detect your system's hostname. On Unix, this corresponds to calling **gethostname**. On Windows, this corresponds to calling **GetComputerNameExW** to fetch the system's "physical DNS hostname."

ripgrep uses your system's hostname for producing hyperlinks.

**--hyperlink-format**=*FORMAT*

Set the format of hyperlinks to use when printing results. Hyperlinks make certain elements of ripgrep's output, such as file paths, clickable. This generally only works in terminal emulators that support OSC-8 hyperlinks. For example, the format

file://{host}{path}

will emit an RFC 8089 hyperlink. To see the format that ripgrep is using, pass the

--debug

flag.

Alternatively, a format string may correspond to one of the following aliases: **default**, **none**, **cursor**, **file**, **grep+**, **kitty**, **macvim**, **textmate**, **vscode**, **vscode-insiders**, **vscodium**. The alias will be replaced with a format string that is intended to work for the corresponding application.

The following variables are available in the format string:

****{path}****

Required. This is replaced with a path to a matching file. The path is guaranteed to be absolute and percent encoded such that it is valid to put into a URI. Note that a path is guaranteed to start with a /.

****{host}****

Optional. This is replaced with your system's hostname. On Unix, this corresponds to calling

gethostname

. On Windows, this corresponds to calling

GetComputerNameExW

to fetch the system's "physical DNS hostname." Alternatively, if

--hostname-bin

was provided, then the hostname returned from the output of that program will be returned. If no hostname could be found, then this variable is replaced with the empty string.

****{line}****

Optional. If appropriate, this is replaced with the line number of a match. If no line number is available (for example, if

--no-line-number

was given), then it is automatically replaced with the value 1.

****{column}****

Optional, but requires the presence of

{line}

. If appropriate, this is replaced with the column number of a match. If no column number is available (for example, if

--no-column

was given), then it is automatically replaced with the value 1.

****{wslprefix}****

Optional. This is a special value that is set to

wsl$/

WSL_DISTRO_NAME

, where

WSL_DISTRO_NAME

corresponds to the value of the equivalent environment variable. If the system is not Unix or if the

WSL_DISTRO_NAME

environment variable is not set, then this is replaced with the empty string.

A format string may be empty. An empty format string is equivalent to the **none** alias. In this case, hyperlinks will be disabled.

At present, ripgrep does not enable hyperlinks by default. Users must opt into them. If you aren't sure what format to use, try **default**.

Like colors, when ripgrep detects that stdout is not connected to a tty, then hyperlinks are automatically disabled, regardless of the value of this flag. Users can pass **--color=always** to forcefully emit hyperlinks.

Note that hyperlinks are only written when a path is also in the output and colors are enabled. To write hyperlinks without colors, you'll need to configure ripgrep to not colorize anything without actually disabling all ANSI escape codes completely:

```
    --colors 'path:none' \
    --colors 'line:none' \
    --colors 'column:none' \
    --colors 'match:none'
```

ripgrep works this way because it treats the **--color** flag as a proxy for whether ANSI escape codes should be used at all. This means that environment variables like **NO_COLOR=1** and **TERM=dumb** not only disable colors, but hyperlinks as well. Similarly, colors and hyperlinks are disabled when ripgrep is not writing to a tty. (Unless one forces the issue by setting **--color=always**.)

If you're searching a file directly, for example:

```
    rg foo path/to/file
```

then hyperlinks will not be emitted since the path given does not appear in the output. To make the path appear, and thus also a hyperlink, use the **-H/--with-filename** flag.

For more information on hyperlinks in terminal emulators, see: https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda

**--include-zero**

When used with

-c/--count

or

--count-matches

, this causes ripgrep to print the number of matches for each file even if there were zero matches. This is disabled by default but can be enabled to make ripgrep behave more like grep.

This flag can be disabled with **--no-include-zero**.

**--line-buffered**

When enabled, ripgrep will always use line buffering. That is, whenever a matching line is found, it will be flushed to stdout immediately. This is the default when ripgrep's stdout is connected to a tty, but otherwise, ripgrep will use block buffering, which is typically faster. This flag forces ripgrep to use line buffering even if it would otherwise use block buffering. This is typically useful in shell pipelines, for example:

```
    tail -f something.log | rg foo --line-buffered | rg bar
```

This overrides the **--block-buffered** flag.

This flag can be disabled with **--no-line-buffered**.

**-n**, **--line-number**

Show line numbers (1-based).

This is enabled by default when stdout is connected to a tty.

This flag can be disabled by **-N/--no-line-number**.

**-N**, **--no-line-number**

Suppress line numbers.

Line numbers are off by default when stdout is not connected to a tty.

Line numbers can be forcefully turned on by **-n/--line-number**.

**-M** *NUM*, **--max-columns**=*NUM*

When given, ripgrep will omit lines longer than this limit in bytes. Instead of printing long lines, only the number of matches in that line is printed.

When this flag is omitted or is set to **0**, then it has no effect.

**--max-columns-preview**

Prints a preview for lines exceeding the configured max column limit.

When the **-M/--max-columns** flag is used, ripgrep will by default completely replace any line that is too long with a message indicating that a matching line was removed. When this flag is combined with **-M/--max-columns**, a preview of the line (corresponding to the limit size) is shown instead, where the part of the line exceeding the limit is not shown.

If the **-M/--max-columns** flag is not set, then this has no effect.

This flag can be disabled with **--no-max-columns-preview**.

**-0**, **--null**

Whenever a file path is printed, follow it with a

NUL

byte. This includes printing file paths before matches, and when printing a list of matching files such as with

-c/--count

,

-l/--files-with-matches

and

--files

. This option is useful for use with

xargs

.

**-o**, **--only-matching**

Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.

**--path-separator**=*SEPARATOR*

Set the path separator to use when printing file paths. This defaults to your platform's path separator, which is

/

on Unix and

\

on Windows. This flag is intended for overriding the default when the environment demands it (e.g., cygwin). A path separator is limited to a single byte.

Setting this flag to an empty string reverts it to its default behavior. That is, the path separator is automatically chosen based on the environment.

**--passthru**

Print both matching and non-matching lines.

Another way to achieve a similar effect is by modifying your pattern to match the empty string. For example, if you are searching using **rg** *foo*, then using **rg** **'^|***foo***'** instead will emit every line in every file searched, but only occurrences of *foo* will be highlighted. This flag enables the same behavior without needing to modify the pattern.

An alternative spelling for this flag is **--passthrough**.

This overrides the **-C/--context**, **-A/--after-context** and **-B/--before-context** flags.

**-p**, **--pretty**

This is a convenience alias for

--color=always --heading

--line-number

. This flag is useful when you still want pretty output even if you're piping ripgrep to another program or file. For example:

rg -p

foo

| less -R

.

**-q**, **--quiet**

Do not print anything to stdout. If a match is found in a file, then ripgrep will stop searching. This is useful when ripgrep is used only for its exit code (which will be an error code if no matches are found).

When **--files** is used, ripgrep will stop finding files after finding the first file that does not match any ignore rules.

**-r** *REPLACEMENT*, **--replace**=*REPLACEMENT*

Replaces every match with the text given when printing results. Neither this flag nor any other ripgrep flag will modify your files.

Capture group indices (e.g., **$***5*) and names (e.g., **$***foo*) are supported in the replacement string. Capture group indices are numbered based on the position of the opening parenthesis of the group, where the leftmost such group is **$***1*. The special **$***0* group corresponds to the entire match.

The name of a group is formed by taking the longest string of letters, numbers and underscores (i.e. **[_0-9A-Za-z]**) after the **$**. For example, **$***1a* will be replaced with the group named *1a*, not the group at index *1*. If the group's name contains characters that aren't letters, numbers or underscores, or you want to immediately follow the group with another string, the name should be put inside braces. For example, **${***1***}***a* will take the content of the group at index *1* and append *a* to the end of it.

If an index or name does not refer to a valid capture group, it will be replaced with an empty string.

In shells such as Bash and zsh, you should wrap the pattern in single quotes instead of double quotes. Otherwise, capture group indices will be replaced by expanded shell variables which will most likely be empty.

To write a literal **$**, use **$$**.

Note that the replacement by default replaces each match, and not the entire line. To replace the entire line, you should match the entire line.

This flag can be used with the **-o/--only-matching** flag.

**--sort**=*SORTBY*

This flag enables sorting of results in ascending order. The possible values for this flag are:

****none****

(Default) Do not sort results. Fastest. Can be multi-threaded.

****path****

Sort by file path. Always single-threaded. The order is determined by sorting files in each directory entry during traversal. This means that given the files

a/b

and

a+

, the latter will sort after the former even though

+

would normally sort before

/

.

****modified****

Sort by the last modified time on a file. Always single-threaded.

****accessed****

Sort by the last accessed time on a file. Always single-threaded.

****created****

Sort by the creation time on a file. Always single-threaded.

If the chosen (manually or by-default) sorting criteria isn't available on your system (for example, creation time is not available on ext4 file systems), then ripgrep will attempt to detect this, print an error and exit without searching.

To sort results in reverse or descending order, use the **--sortr** flag. Also, this flag overrides **--sortr**.

Note that sorting results currently always forces ripgrep to abandon parallelism and run in a single thread.

**--sortr**=*SORTBY*

This flag enables sorting of results in descending order. The possible values for this flag are:

****none****

(Default) Do not sort results. Fastest. Can be multi-threaded.

****path****

Sort by file path. Always single-threaded. The order is determined by sorting files in each directory entry during traversal. This means that given the files

a/b

and

a+

, the latter will sort before the former even though

+

would normally sort after

/

when doing a reverse lexicographic sort.

****modified****

Sort by the last modified time on a file. Always single-threaded.

****accessed****

Sort by the last accessed time on a file. Always single-threaded.

****created****

Sort by the creation time on a file. Always single-threaded.

If the chosen (manually or by-default) sorting criteria isn't available on your system (for example, creation time is not available on ext4 file systems), then ripgrep will attempt to detect this, print an error and exit without searching.

To sort results in ascending order, use the **--sort** flag. Also, this flag overrides **--sort**.

Note that sorting results currently always forces ripgrep to abandon parallelism and run in a single thread.

**--trim**

When set, all ASCII whitespace at the beginning of each line printed will be removed.

This flag can be disabled with **--no-trim**.

**--vimgrep**

This flag instructs ripgrep to print results with every match on its own line, including line numbers and column numbers.

With this option, a line with more than one match will be printed in its entirety more than once. For that reason, the total amount of output as a result of this flag can be quadratic in the size of the input. For example, if the pattern matches every byte in an input file, then each line will be repeated for every byte matched. For this reason, users should only use this flag when there is no other choice. Editor integrations should prefer some other way of reading results from ripgrep, such as via the **--json** flag. One alternative to avoiding exorbitant memory usage is to force ripgrep into single threaded mode with the **-j/--threads** flag. Note though that this will not impact the total size of the output, just the heap memory that ripgrep will use.

**-H**, **--with-filename**

This flag instructs ripgrep to print the file path for each matching line. This is the default when more than one file is searched. If

--heading

is enabled (the default when printing to a tty), the file path will be shown above clusters of matches from each file; otherwise, the file name will be shown as a prefix for each matched line.

This flag overrides **-I/--no-filename**.

**-I**, **--no-filename**

This flag instructs ripgrep to never print the file path with each matching line. This is the default when ripgrep is explicitly instructed to search one file or stdin.

This flag overrides **-H/--with-filename**.

**--sort-files**

DEPRECATED. Use

--sort=path

instead.

This flag instructs ripgrep to sort search results by file path lexicographically in ascending order. Note that this currently disables all parallelism and runs search in a single thread.

This flag overrides **--sort** and **--sortr**.

This flag can be disabled with **--no-sort-files**.


## OUTPUT MODES

**-c**, **--count**

This flag suppresses normal output and shows the number of lines that match the given patterns for each file searched. Each file containing a match has its path and count printed on each line. Note that unless

-U/--multiline

is enabled and the pattern(s) given can match over multiple lines, this reports the number of lines that match and not the total number of matches. When multiline mode is enabled and the pattern(s) given can match over multiple lines,

-c/--count

is equivalent to

--count-matches

.

If only one file is given to ripgrep, then only the count is printed if there is a match. The **-H/--with-filename** flag can be used to force printing the file path in this case. If you need a count to be printed regardless of whether there is a match, then use **--include-zero**.

Note that it is possible for this flag to have results inconsistent with the output of **-l/--files-with-matches**. Notably, by default, ripgrep tries to avoid searching files with binary data. With this flag, ripgrep needs to search the entire content of files, which may include binary data. But with **-l/--files-with-matches**, ripgrep can stop as soon as a match is observed, which may come well before any binary data. To avoid this inconsistency without disabling binary detection, use the **--binary** flag.

This overrides the **--count-matches** flag. Note that when **-c/--count** is combined with **-o/--only-matching**, then ripgrep behaves as if **--count-matches** was given.

**--count-matches**

This flag suppresses normal output and shows the number of individual matches of the given patterns for each file searched. Each file containing matches has its path and match count printed on each line. Note that this reports the total number of individual matches and not the number of lines that match.

If only one file is given to ripgrep, then only the count is printed if there is a match. The **-H/--with-filename** flag can be used to force printing the file path in this case.

This overrides the **-c/--count** flag. Note that when **-c/--count** is combined with **-o/--only-matching**, then ripgrep behaves as if **--count-matches** was given.

**-l**, **--files-with-matches**

Print only the paths with at least one match and suppress match contents.

Note that it is possible for this flag to have results inconsistent with the output of **-c/--count**. Notably, by default, ripgrep tries to avoid searching files with binary data. With this flag, ripgrep might stop searching before the binary data is observed. But with **-c/--count**, ripgrep has to search the entire contents to determine the match count, which means it might see binary data that causes it to skip searching that file. To avoid this inconsistency without disabling binary detection, use the **--binary** flag.

This overrides **--files-without-match**.

**--files-without-match**

Print the paths that contain zero matches and suppress match contents.

This overrides **-l/--files-with-matches**.

**--json**

Enable printing results in a JSON Lines format.

When this flag is provided, ripgrep will emit a sequence of messages, each encoded as a JSON object, where there are five different message types:

****begin****

A message that indicates a file is being searched and contains at least one match.

****end****

A message the indicates a file is done being searched. This message also include summary statistics about the search for a particular file.

****match****

A message that indicates a match was found. This includes the text and offsets of the match.

****context****

A message that indicates a contextual line was found. This includes the text of the line, along with any match information if the search was inverted.

****summary****

The final message emitted by ripgrep that contains summary statistics about the search across all files.

Since file paths or the contents of files are not guaranteed to be valid UTF-8 and JSON itself must be representable by a Unicode encoding, ripgrep will emit all data elements as objects with one of two keys: **text** or **bytes**. **text** is a normal JSON string when the data is valid UTF-8 while **bytes** is the base64 encoded contents of the data.

The JSON Lines format is only supported for showing search results. It cannot be used with other flags that emit other types of output, such as **--files**, **-l/--files-with-matches**, **--files-without-match**, **-c/--count** or **--count-matches**. ripgrep will report an error if any of the aforementioned flags are used in concert with **--json**.

Other flags that control aspects of the standard output such as **-o/--only-matching**, **--heading**, **-r/--replace**, **-M/--max-columns**, etc., have no effect when **--json** is set. However, enabling JSON output will always implicitly and unconditionally enable **--stats**.

A more complete description of the JSON format used can be found here: https://docs.rs/grep-printer/*/grep_printer/struct.JSON.html.

This flag can be disabled with **--no-json**.


## LOGGING OPTIONS

**--debug**

Show debug messages. Please use this when filing a bug report.

The **--debug** flag is generally useful for figuring out why ripgrep skipped searching a particular file. The debug messages should mention all files skipped and why they were skipped.

To get even more debug output, use the **--trace** flag, which implies **--debug** along with additional trace data.

**--no-ignore-messages**

When this flag is enabled, all error messages related to parsing ignore files are suppressed. By default, error messages are printed to stderr. In cases where these errors are expected, this flag can be used to avoid seeing the noise produced by the messages.

This flag can be disabled with **--ignore-messages**.

**--no-messages**

This flag suppresses some error messages. Specifically, messages related to the failed opening and reading of files. Error messages related to the syntax of the pattern are still shown.

This flag can be disabled with **--messages**.

**--stats**

When enabled, ripgrep will print aggregate statistics about the search. When this flag is present, ripgrep will print at least the following stats to stdout at the end of the search: number of matched lines, number of files with matches, number of files searched, and the time taken for the entire search to complete.

This set of aggregate statistics may expand over time.

This flag is always and implicitly enabled when **--json** is used.

Note that this flag has no effect if **--files**, **-l/--files-with-matches** or **--files-without-match** is passed.

This flag can be disabled with **--no-stats**.

**--trace**

Show trace messages. This shows even more detail than the

--debug

flag. Generally, one should only use this if

--debug

doesn't emit the information you're looking for.


## OTHER BEHAVIORS

**--files**

Print each file that would be searched without actually performing the search. This is useful to determine whether a particular file is being searched or not.

This overrides **--type-list**.

**--generate**=*KIND*

This flag instructs ripgrep to generate some special kind of output identified by

KIND

and then quit without searching.

KIND

can be one of the following values:

****man****

Generates a manual page for ripgrep in the

roff

format.

****complete-bash****

Generates a completion script for the

bash

shell.

****complete-zsh****

Generates a completion script for the

zsh

shell.

****complete-fish****

Generates a completion script for the

fish

shell.

****complete-powershell****

Generates a completion script for PowerShell.

The output is written to **stdout**. The list above may expand over time.

**--no-config**

When set, ripgrep will never read configuration files. When this flag is present, ripgrep will not respect the

RIPGREP_CONFIG_PATH

environment variable.

If ripgrep ever grows a feature to automatically read configuration files in pre-defined locations, then this flag will also disable that behavior as well.

**--pcre2-version**

When this flag is present, ripgrep will print the version of PCRE2 in use, along with other information, and then exit. If PCRE2 is not available, then ripgrep will print an error message and exit with an error code.

**--type-list**

Show all supported file types and their corresponding globs. This takes any

--type-add

and

--type-clear

flags given into account. Each type is printed on its own line, followed by a

:

and then a comma-delimited list of globs for that type on the same line.

**-V**, **--version**

This flag prints ripgrep's version. This also may print other relevant information, such as the presence of target specific optimizations and the

git

revision that this build of ripgrep was compiled from.

# EXIT STATUS

If ripgrep finds a match, then the exit status of the program is **0**. If no match could be found, then the exit status is **1**. If an error occurred, then the exit status is always **2** unless ripgrep was run with the **-q/--quiet** flag and a match was found. In summary:

- **0** exit status occurs only when at least one match was found, and if no error occurred, unless **-q/--quiet** was given.
- **1** exit status occurs only when no match was found and no error occurred.
- **2** exit status occurs when an error occurred. This is true for both catastrophic errors (e.g., a regex syntax error) and for soft errors (e.g., unable to read a file).

# AUTOMATIC FILTERING

ripgrep does a fair bit of automatic filtering by default. This section describes that filtering and how to control it.

**TIP**: To disable automatic filtering, use **rg -uuu**.

ripgrep's automatic "smart" filtering is one of the most apparent differentiating features between ripgrep and other tools like **grep**. As such, its behavior may be surprising to users that aren't expecting it.

ripgrep does four types of filtering automatically:

**1.**

Files and directories that match ignore rules are not searched.

**2.**

Hidden files and directories are not searched.

**3.**

Binary files (files with a

NUL

byte) are not searched.

**4.**

Symbolic links are not followed.

The first type of filtering is the most sophisticated. ripgrep will attempt to respect your **gitignore** rules as faithfully as possible. In particular, this includes the following:

- Any global rules, e.g., in **$HOME/.config/git/ignore**.
- Any rules in relevant **.gitignore** files. This includes **.gitignore** files in parent directories that are part of the same **git** repository. (Unless **--no-require-git** is given.)
- Any local rules, e.g., in **.git/info/exclude**.

In some cases, ripgrep and **git** will not always be in sync in terms of which files are ignored. For example, a file that is ignored via **.gitignore** but is tracked by **git** would not be searched by ripgrep even though **git** tracks it. This is unlikely to ever be fixed. Instead, you should either make sure your exclude rules match the files you track precisely, or otherwise use **git grep** for search.

Additional ignore rules can be provided outside of a **git** context:

- Any rules in **.ignore**. ripgrep will also respect **.ignore** files in parent directories.
- Any rules in **.rgignore**. ripgrep will also respect **.rgignore** files in parent directories.
- Any rules in files specified with the **--ignore-file** flag.

The precedence of ignore rules is as follows, with later items overriding earlier items:

- Files given by **--ignore-file**.
- Global gitignore rules, e.g., from **$HOME/.config/git/ignore**.
- Local rules from **.git/info/exclude**.
- Rules from **.gitignore**.
- Rules from **.ignore**.
- Rules from **.rgignore**.

So for example, if *foo* were in a **.gitignore** and **!***foo* were in an **.rgignore**, then *foo* would not be ignored since **.rgignore** takes precedence over **.gitignore**.

Each of the types of filtering can be configured via command line flags:

- There are several flags starting with **--no-ignore** that toggle which, if any, ignore rules are respected. **--no-ignore** by itself will disable all of them.
- **-./--hidden** will force ripgrep to search hidden files and directories.
- **--binary** will force ripgrep to search binary files.
- **-L/--follow** will force ripgrep to follow symlinks.

As a special short hand, the **-u** flag can be specified up to three times. Each additional time incrementally decreases filtering:

- **-u** is equivalent to **--no-ignore**.
- **-uu** is equivalent to **--no-ignore --hidden**.
- **-uuu** is equivalent to **--no-ignore --hidden --binary**.

In particular, **rg -uuu** should search the same exact content as **grep** **-r**.

# CONFIGURATION FILES

ripgrep supports reading configuration files that change ripgrep's default behavior. The format of the configuration file is an "rc" style and is very simple. It is defined by two rules:

**1.**

Every line is a shell argument, after trimming whitespace.

**2.**

Lines starting with

#

(optionally preceded by any amount of whitespace) are ignored.

ripgrep will look for a single configuration file if and only if the **RIPGREP_CONFIG_PATH** environment variable is set and is non-empty. ripgrep will parse arguments from this file on startup and will behave as if the arguments in this file were prepended to any explicit arguments given to ripgrep on the command line. Note though that the **rg** command you run must still be valid. That is, it must always contain at least one pattern at the command line, even if the configuration file uses the **-e/--regexp** flag.

For example, if your ripgreprc file contained a single line:

```
    --smart-case
```

then the following command

```
    RIPGREP_CONFIG_PATH=wherever/.ripgreprc rg foo
```

would behave identically to the following command:

```
    rg --smart-case foo
```

Another example is adding types, like so:

```
    --type-add
    web:*.{html,css,js}*
```

The above would behave identically to the following command:

```
    rg --type-add 'web:*.{html,css,js}*' foo
```

The same applies to using globs. This:

```
    --glob=!.git
```

or this:

```
    --glob
    !.git
```

would behave identically to the following command:

```
    rg --glob '!.git' foo
```

The bottom line is that every shell argument needs to be on its own line. So for example, a config file containing

```
    -j 4
```

is probably not doing what you intend. Instead, you want

```
    -j
    4
```

or

```
    -j4
```

ripgrep also provides a flag, **--no-config**, that when present will suppress any and all support for configuration. This includes any future support for auto-loading configuration files from pre-determined paths.

Conflicts between configuration files and explicit arguments are handled exactly like conflicts in the same command line invocation. That is, assuming your config file contains only **--smart-case**, then this command:

```
    RIPGREP_CONFIG_PATH=wherever/.ripgreprc rg foo --case-sensitive
```

is exactly equivalent to

```
    rg --smart-case foo --case-sensitive
```

in which case, the **--case-sensitive** flag would override the **--smart-case** flag.

# SHELL COMPLETION

Shell completion files are included in the release tarball for Bash, Fish, Zsh and PowerShell.

For **bash**, move **rg.bash** to **$XDG_CONFIG_HOME/bash_completion** or **/etc/bash_completion.d/**.

For **fish**, move **rg.fish** to **$HOME/.config/fish/completions**.

For **zsh**, move **_rg** to one of your **$fpath** directories.

# CAVEATS

ripgrep may abort unexpectedly when using default settings if it searches a file that is simultaneously truncated. This behavior can be avoided by passing the **--no-mmap** flag which will forcefully disable the use of memory maps in all cases.

ripgrep may use a large amount of memory depending on a few factors. Firstly, if ripgrep uses parallelism for search (the default), then the entire output for each individual file is buffered into memory in order to prevent interleaving matches in the output. To avoid this, you can disable parallelism with the **-j1** flag. Secondly, ripgrep always needs to have at least a single line in memory in order to execute a search. A file with a very long line can thus cause ripgrep to use a lot of memory. Generally, this only occurs when searching binary data with the **-a/--text** flag enabled. (When the **-a/--text** flag isn't enabled, ripgrep will replace all NUL bytes with line terminators, which typically prevents exorbitant memory usage.) Thirdly, when ripgrep searches a large file using a memory map, the process will likely report its resident memory usage as the size of the file. However, this does not mean ripgrep actually needed to use that much heap memory; the operating system will generally handle this for you.

# VERSION

15.1.0

# HOMEPAGE

https://github.com/BurntSushi/ripgrep

Please report bugs and feature requests to the issue tracker. Please do your best to provide a reproducible test case for bugs. This should include the corpus being searched, the **rg** command, the actual output and the expected output. Please also include the output of running the same **rg** command but with the **--debug** flag.

If you have questions that don't obviously fall into the "bug" or "feature request" category, then they are welcome in the Discussions section of the issue tracker: https://github.com/BurntSushi/ripgrep/discussions.

# AUTHORS

Andrew Gallant <*jamslam@gmail.com*>

| 2025-10-22 | 15.1.0 |
|---|---|
