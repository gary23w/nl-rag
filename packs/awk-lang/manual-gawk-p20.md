---
title: "The GNU Awk User’s Guide (part 20/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 20/38
---

# The GNU Awk User’s Guide

```
...
This program has a @code{BEGIN} rule
that prints a nice message:

@example
@c file examples/messages.awk
BEGIN @{ print "Don't panic!" @}
@c endfile
@end example

It also prints some final advice:

@example
@c file examples/messages.awk
END @{ print "Always avoid bored archaeologists!" @}
@c endfile
@end example
...
```

extract.awk begins by setting `IGNORECASE` to one, so that mixed upper- and lowercase letters in the directives won’t matter.

The first rule handles calling `system()`, checking that a command is given (`NF` is at least three) and also checking that the command exits with a zero exit status, signifying OK:

```
# extract.awk --- extract files and run programs from Texinfo files

BEGIN    { IGNORECASE = 1 }

/^@c(omment)?[ \t]+system/ {
    if (NF < 3) {
        e = ("extract: " FILENAME ":" FNR)
        e = (e  ": badly formed `system' line")
        print e > "/dev/stderr"
        next
    }
    $1 = ""
    $2 = ""
    stat = system($0)
    if (stat != 0) {
        e = ("extract: " FILENAME ":" FNR)
        e = (e ": warning: system returned " stat)
        print e > "/dev/stderr"
    }
}
```

The variable `e` is used so that the rule fits nicely on the screen.

The second rule handles moving data into files. It verifies that a file name is given in the directive. If the file named is not the current file, then the current file is closed. Keeping the current file open until a new file is encountered allows the use of the ‘>’ redirection for printing the contents, keeping open-file management simple.

The `for` loop does the work. It reads lines using `getline` (see Explicit Input with `getline`). For an unexpected end-of-file, it calls the `unexpected_eof()` function. If the line is an “endfile” line, then it breaks out of the loop. If the line is an ‘@group’ or ‘@end group’ line, then it ignores it and goes on to the next line. Similarly, comments within examples are also ignored.

Most of the work is in the following few lines. If the line has no ‘@’ symbols, the program can print it directly. Otherwise, each leading ‘@’ must be stripped off. To remove the ‘@’ symbols, the line is split into separate elements of the array `a`, using the `split()` function (see String-Manipulation Functions). The ‘@’ symbol is used as the separator character. Each element of `a` that is empty indicates two successive ‘@’ symbols in the original line. For each two empty elements (‘@@’ in the original file), we have to add a single ‘@’ symbol back in.

When the processing of the array is finished, `join()` is called with the value of `SUBSEP` (see Multidimensional Arrays), to rejoin the pieces back into a single line. That line is then printed to the output file:

```
/^@c(omment)?[ \t]+file/ {
    if (NF != 3) {
        e = ("extract: " FILENAME ":" FNR ": badly formed `file' line")
        print e > "/dev/stderr"
        next
    }
    if ($3 != curfile) {
        if (curfile != "")
            filelist[curfile] = 1   # save to close later
        curfile = $3
    }

    for (;;) {
        if ((getline line) <= 0)
            unexpected_eof()
        if (line ~ /^@c(omment)?[ \t]+endfile/)
            break
        else if (line ~ /^@(end[ \t]+)?group/)
            continue
        else if (line ~ /^@c(omment+)?[ \t]+/)
            continue
        if (index(line, "@") == 0) {
            print line > curfile
            continue
        }
        n = split(line, a, "@")
        # if a[1] == "", means leading @,
        # don't add one back in.
        for (i = 2; i <= n; i++) {
            if (a[i] == "") { # was an @@
                a[i] = "@"
                if (a[i+1] == "")
                    i++
            }
        }
```

```
        print join(a, 1, n, SUBSEP) > curfile
    }
}
```

An important thing to note is the use of the ‘>’ redirection. Output done with ‘>’ only opens the file once; it stays open and subsequent output is appended to the file (see Redirecting Output of `print` and `printf`). This makes it easy to mix program text and explanatory prose for the same sample source file (as has been done here!) without any hassle. The file is only closed when a new data file name is encountered or at the end of the input file.

When a new file name is encountered, instead of closing the file, the program saves the name of the current file in `filelist`. This makes it possible to interleave the code for more than one file in the Texinfo input file. (Previous versions of this program *did* close the file. But because of the ‘>’ redirection, a file whose parts were not all one after the other ended up getting clobbered.) An `END` rule then closes all the open files when processing is finished:

```
END {
    close(curfile)          # close the last one
    for (f in filelist)     # close all the rest
        close(f)
}
```

Finally, the function `unexpected_eof()` prints an appropriate error message and then exits:

```
function unexpected_eof()
{
    printf("extract: %s:%d: unexpected EOF or error\n",
                     FILENAME, FNR) > "/dev/stderr"
    exit 1
}
```

#### 11.3.8 A Simple Stream Editor

The `sed` utility is a *stream editor*, a program that reads a stream of data, makes changes to it, and passes it on. It is often used to make global changes to a large file or to a stream of data generated by a pipeline of commands. Although `sed` is a complicated program in its own right, its most common use is to perform global substitutions in the middle of a pipeline:

```
command1 < orig.data | sed 's/old/new/g' | command2 > result
```

Here, ‘s/old/new/g’ tells `sed` to look for the regexp ‘old’ on each input line and globally replace it with the text ‘new’ (i.e., all the occurrences on a line). This is similar to `awk`’s `gsub()` function (see String-Manipulation Functions).

The following program, awksed.awk, accepts at least two command-line arguments: the pattern to look for and the text to replace it with. Any additional arguments are treated as data file names to process. If none are provided, the standard input is used:

```
# awksed.awk --- do s/foo/bar/g using just print
#    Thanks to Michael Brennan for the idea

function usage()
{
    print "usage: awksed pat repl [files...]" > "/dev/stderr"
    exit 1
}
```

```
BEGIN {
    # validate arguments
    if (ARGC < 3)
        usage()
```

```
    RS = ARGV[1]
    ORS = ARGV[2]

    # don't use arguments as files
    ARGV[1] = ARGV[2] = ""
}
```

```
# look ma, no hands!
{
    if (RT == "")
        printf "%s", $0
    else
        print
}
```

The program relies on `gawk`’s ability to have `RS` be a regexp, as well as on the setting of `RT` to the actual text that terminates the record (see How Input Is Split into Records).

The idea is to have `RS` be the pattern to look for. `gawk` automatically sets `$0` to the text between matches of the pattern. This is text that we want to keep, unmodified. Then, by setting `ORS` to the replacement text, a simple `print` statement outputs the text we want to keep, followed by the replacement text.

There is one wrinkle to this scheme, which is what to do if the last record doesn’t end with text that matches `RS`. Using a `print` statement unconditionally prints the replacement text, which is not correct. However, if the file did not end in text that matches `RS`, `RT` is set to the null string. In this case, we can print `$0` using `printf` (see Using `printf` Statements for Fancier Printing).

The `BEGIN` rule handles the setup, checking for the right number of arguments and calling `usage()` if there is a problem. Then it sets `RS` and `ORS` from the command-line arguments and sets `ARGV[1]` and `ARGV[2]` to the null string, so that they are not treated as file names (see Using `ARGC` and `ARGV`).

The `usage()` function prints an error message and exits. Finally, the single rule handles the printing scheme outlined earlier, using `print` or `printf` as appropriate, depending upon the value of `RT`.

#### 11.3.9 An Easy Way to Use Library Functions

In Including Other Files into Your Program, we saw how `gawk` provides a built-in file-inclusion capability. However, this is a `gawk` extension. This section provides the motivation for making file inclusion available for standard `awk`, and shows how to do it using a combination of shell and `awk` programming.

Using library functions in `awk` can be very beneficial. It encourages code reuse and the writing of general functions. Programs are smaller and therefore clearer. However, using library functions is only easy when writing `awk` programs; it is painful when running them, requiring multiple -f options. If `gawk` is unavailable, then so too is the `AWKPATH` environment variable and the ability to put `awk` functions into a library directory (see Command-Line Options). It would be nice to be able to write programs in the following manner:

```
# library functions
@include getopt.awk
@include join.awk
...

# main program
BEGIN {
    while ((c = getopt(ARGC, ARGV, "a:b:cde")) != -1)
        ...
    ...
}
```

The following program, igawk.sh, provides this service. It simulates `gawk`’s searching of the `AWKPATH` variable and also allows *nested* includes (i.e., a file that is included with `@include` can contain further `@include` directives). `igawk` makes an effort to only include files once, so that nested includes don’t accidentally include a library function twice.

`igawk` should behave just like `gawk` externally. This means it should accept all of `gawk`’s command-line arguments, including the ability to have multiple source files specified via -f and the ability to mix command-line and library source files.

The program is written using the POSIX Shell (`sh`) command language.82 It works as follows:

1. Loop through the arguments, saving anything that doesn’t represent `awk` source code for later, when the expanded program is run.
2. For any arguments that do represent `awk` text, put the arguments into a shell variable that will be expanded. There are two cases:
  1. Literal text, provided with -e or --source. This text is just appended directly.
  2. Source file names, provided with -f. We use a neat trick and append ‘@include *filename*’ to the shell variable’s contents. Because the file-inclusion program works the way `gawk` does, this gets the text of the file included in the program at the correct point.
3. Run an `awk` program (naturally) over the shell variable’s contents to expand `@include` directives. The expanded program is placed in a second shell variable.
4. Run the expanded program with `gawk` and any other original command-line arguments that the user supplied (such as the data file names).

This program uses shell variables extensively: for storing command-line arguments and the text of the `awk` program that will expand the user’s program, for the user’s original program, and for the expanded program. Doing so removes some potential problems that might arise were we to use temporary files instead, at the cost of making the script somewhat more complicated.

The initial part of the program turns on shell tracing if the first argument is ‘debug’.

The next part loops through all the command-line arguments. There are several cases of interest:

**--**

This ends the arguments to `igawk`. Anything else should be passed on to the user’s `awk` program without being evaluated.

**-W**

This indicates that the next option is specific to `gawk`. To make argument processing easier, the -W is appended to the front of the remaining arguments and the loop continues. (This is an `sh` programming trick. Don’t worry about it if you are not familiar with `sh`.)

**-v, -F**

These are saved and passed on to `gawk`.

**-f, --file, --file=, -Wfile=**

The file name is appended to the shell variable `program` with an `@include` directive. The `expr` utility is used to remove the leading option part of the argument (e.g., ‘--file=’). (Typical `sh` usage would be to use the `echo` and `sed` utilities to do this work. Unfortunately, some versions of `echo` evaluate escape sequences in their arguments, possibly mangling the program text. Using `expr` avoids this problem.)

**--source, --source=, -Wsource=**

The source text is appended to `program`.

**--version, -Wversion**

`igawk` prints its version number, runs ‘gawk --version’ to get the `gawk` version information, and then exits.

If none of the -f, --file, -Wfile, --source, or -Wsource arguments are supplied, then the first nonoption argument should be the `awk` program. If there are no command-line arguments left, `igawk` prints an error message and exits. Otherwise, the first argument is appended to `program`. In any case, after the arguments have been processed, the shell variable `program` contains the complete text of the original `awk` program.

The program is as follows:

```
#! /bin/sh
# igawk --- like gawk but do @include processing

if [ "$1" = debug ]
then
    set -x
    shift
fi

# A literal newline, so that program text is formatted correctly
n='
'

# Initialize variables to empty
program=
opts=

while [ $# -ne 0 ] # loop over arguments
do
    case $1 in
    --)     shift
            break ;;

    -W)     shift
            # The ${x?'message here'} construct prints a
            # diagnostic if $x is the null string
            set -- -W"${@?'missing operand'}"
            continue ;;

    -[vF])  opts="$opts $1 '${2?'missing operand'}'"
            shift ;;

    -[vF]*) opts="$opts '$1'" ;;

    -f)     program="$program$n@include ${2?'missing operand'}"
            shift ;;

    -f*)    f=$(expr "$1" : '-f\(.*\)')
            program="$program$n@include $f" ;;

    -[W-]file=*)
            f=$(expr "$1" : '-.file=\(.*\)')
            program="$program$n@include $f" ;;

    -[W-]file)
            program="$program$n@include ${2?'missing operand'}"
            shift ;;

    -[W-]source=*)
            t=$(expr "$1" : '-.source=\(.*\)')
            program="$program$n$t" ;;

    -[W-]source)
            program="$program$n${2?'missing operand'}"
            shift ;;

    -[W-]version)
            echo igawk: version 3.0 1>&2
            gawk --version
            exit 0 ;;

    -[W-]*) opts="$opts '$1'" ;;

    *)      break ;;
    esac
    shift
done

if [ -z "$program" ]
then
     program=${1?'missing program'}
     shift
fi

# At this point, `program' has the program.
```

The `awk` program to process `@include` directives is stored in the shell variable `expand_prog`. Doing this keeps the shell script readable. The `awk` program reads through the user’s program, one line at a time, using `getline` (see Explicit Input with `getline`). The input file names and `@include` directives are managed using a stack. As each `@include` is encountered, the current file name is “pushed” onto the stack and the file named in the `@include` directive becomes the current file name. As each file is finished, the stack is “popped,” and the previous input file becomes the current input file again. The process is started by making the original file the first one on the stack.

The `pathto()` function does the work of finding the full path to a file. It simulates `gawk`’s behavior when searching the `AWKPATH` environment variable (see The `AWKPATH` Environment Variable). If a file name has a ‘/’ in it, no path search is done. Similarly, if the file name is `"-"`, then that string is used as-is. Otherwise, the file name is concatenated with the name of each directory in the path, and an attempt is made to open the generated file name. The only way to test if a file can be read in `awk` is to go ahead and try to read it with `getline`; this is what `pathto()` does.83 If the file can be read, it is closed and the file name is returned:

```
expand_prog='

function pathto(file,    i, t, junk)
{
    if (index(file, "/") != 0)
        return file

    if (file == "-")
        return file

    for (i = 1; i <= ndirs; i++) {
        t = (pathlist[i] "/" file)
```

```
        if ((getline junk < t) > 0) {
            # found it
            close(t)
            return t
        }
```

```
    }
    return ""
}
```

The main program is contained inside one `BEGIN` rule. The first thing it does is set up the `pathlist` array that `pathto()` uses. After splitting the path on ‘:’, null elements are replaced with `"."`, which represents the current directory:

```
BEGIN {
    path = ENVIRON["AWKPATH"]
    ndirs = split(path, pathlist, ":")
    for (i = 1; i <= ndirs; i++) {
        if (pathlist[i] == "")
            pathlist[i] = "."
    }
```

The stack is initialized with `ARGV[1]`, which will be `"/dev/stdin"`. The main loop comes next. Input lines are read in succession. Lines that do not start with `@include` are printed verbatim. If the line does start with `@include`, the file name is in `$2`. `pathto()` is called to generate the full path. If it cannot, then the program prints an error message and continues.

The next thing to check is if the file is included already. The `processed` array is indexed by the full file name of each included file and it tracks this information for us. If the file is seen again, a warning message is printed. Otherwise, the new file name is pushed onto the stack and processing continues.

Finally, when `getline` encounters the end of the input file, the file is closed and the stack is popped. When `stackptr` is less than zero, the program is done:

```
    stackptr = 0
    input[stackptr] = ARGV[1] # ARGV[1] is first file

    for (; stackptr >= 0; stackptr--) {
        while ((getline < input[stackptr]) > 0) {
            if (tolower($1) != "@include") {
                print
                continue
            }
            fpath = pathto($2)
            if (fpath == "") {
                printf("igawk: %s:%d: cannot find %s\n",
                    input[stackptr], FNR, $2) > "/dev/stderr"
                continue
            }
            if (! (fpath in processed)) {
                processed[fpath] = input[stackptr]
                input[++stackptr] = fpath  # push onto stack
            } else
                print $2, "included in", input[stackptr],
                    "already included in",
                    processed[fpath] > "/dev/stderr"
        }
        close(input[stackptr])
    }
}'  # closing single quote ends `expand_prog' variable

processed_program=$(gawk -- "$expand_prog" /dev/stdin << EOF
$program
EOF
)
```

The shell construct ‘*command* << *marker*’ is called a *here document*. Everything in the shell script up to the *marker* is fed to *command* as input. The shell processes the contents of the here document for variable and command substitution (and possibly other things as well, depending upon the shell).

The shell construct ‘$(…)’ is called *command substitution*. The output of the command inside the parentheses is substituted into the command line. Because the result is used in a variable assignment, it is saved as a single string, even if the results contain whitespace.

The expanded program is saved in the variable `processed_program`. It’s done in these steps:

1. Run `gawk` with the `@include`-processing program (the value of the `expand_prog` shell variable) reading standard input.
2. Standard input is the contents of the user’s program, from the shell variable `program`. Feed its contents to `gawk` via a here document.
3. Save the results of this processing in the shell variable `processed_program` by using command substitution.

The last step is to call `gawk` with the expanded program, along with the original options and command-line arguments that the user supplied:

```
eval gawk $opts -- '"$processed_program"' '"$@"'
```

The `eval` command is a shell construct that reruns the shell’s parsing process. This keeps things properly quoted.

This version of `igawk` represents the fifth version of this program. There are four key simplifications that make the program work better:

- Using `@include` even for the files named with -f makes building the initial collected `awk` program much simpler; all the `@include` processing can be done once.
- Not trying to save the line read with `getline` in the `pathto()` function when testing for the file’s accessibility for use with the main program simplifies things considerably.
- Using a `getline` loop in the `BEGIN` rule does it all in one place. It is not necessary to call out to a separate loop for processing nested `@include` directives.
- Instead of saving the expanded program in a temporary file, putting it in a shell variable avoids some potential security problems. This has the disadvantage that the script relies upon more features of the `sh` language, making it harder to follow for those who aren’t familiar with `sh`.

Also, this program illustrates that it is often worthwhile to combine `sh` and `awk` programming together. You can usually accomplish quite a lot, without having to resort to low-level programming in C or C++, and it is frequently easier to do certain kinds of string and argument manipulation using the shell than it is in `awk`.

Finally, `igawk` shows that it is not always necessary to add new features to a program; they can often be layered on top.84

Before `gawk` acquired its built-in `@include` mechanism, `igawk` and its manual page were installed as part of the regular `gawk` installation (‘make install’). This is no longer done, because it’s no longer necessary. But we’ve kept the program in this Web page for its educational value.

#### 11.3.10 Finding Anagrams from a Dictionary

An interesting programming challenge is to search for *anagrams* in a word list (such as /usr/share/dict/words on many GNU/Linux systems). One word is an anagram of another if both words contain the same letters (e.g., “babbling” and “blabbing”).

Column 2, Problem C, of Jon Bentley’s *Programming Pearls*, Second Edition, presents an elegant algorithm. The idea is to give words that are anagrams a common signature, sort all the words together by their signatures, and then print them. Dr. Bentley observes that taking the letters in each word and sorting them produces those common signatures.

The following program uses arrays of arrays to bring together words with the same signature and array sorting to print the words in sorted order:

```
# anagram.awk --- An implementation of the anagram-finding algorithm
#                 from Jon Bentley's "Programming Pearls," 2nd edition.
#                 Addison Wesley, 2000, ISBN-10: 0-201-65788-0,
#                 ISBN-13: 978-0-201-65788-3.
#                 Column 2, Problem C, section 2.8, pp 18-20.

/'s$/   { next }        # Skip possessives
```

The program starts with a header, and then a rule to skip possessives in the dictionary file. The next rule builds up the data structure. The first dimension of the array is indexed by the signature; the second dimension is the word itself:

```
{
    key = word2key($1)  # Build signature
    data[key][$1] = $1  # Store word with signature
}
```

The `word2key()` function creates the signature. It splits the word apart into individual letters, sorts the letters, and then joins them back together:

```
# word2key --- split word apart into letters, sort, and join back together

function word2key(word,     a, i, n, result)
{
    n = split(word, a, "")
    asort(a)

    for (i = 1; i <= n; i++)
        result = result a[i]

    return result
}
```

Finally, the `END` rule traverses the array and prints out the anagram lists. It sends the output to the system `sort` command because otherwise the anagrams would appear in arbitrary order:

```
END {
    sort = "sort"
    for (key in data) {
        # Sort words with same key
        nwords = asorti(data[key], words)
        if (nwords == 1)
            continue

        # And print. Minor glitch: trailing space at end of each line
        for (j = 1; j <= nwords; j++)
            printf("%s ", words[j]) | sort
        print "" | sort
    }
    close(sort)
}
```

Here is some partial output when the program is run:

```
$ gawk -f anagram.awk /usr/share/dict/words | grep '^b'
...
babbled blabbed
babbler blabber brabble
babblers blabbers brabbles
babbling blabbing
babbly blabby
babel bable
babels beslab
babery yabber
...
```

#### 11.3.11 And Now for Something Completely Different

The following program was written by Davide Brini and is published on his website. It serves as his signature in the Usenet group `comp.lang.awk`. He supplies the following copyright terms:

> Copyright © 2008 Davide Brini
> 
> Copying and distribution of the code published in this page, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.

Here is the program:

```
awk 'BEGIN{O="~"~"~";o="=="=="==";o+=+o;x=O""O;while(X++<=x+o+o)c=c"%c";
printf c,(x-O)*(x-O),x*(x-o)-o,x*(x-O)+x-O-o,+x*(x-O)-x+o,X*(o*o+O)+x-O,
X*(X-x)-o*o,(x+X)*o*o+o,x*(X-x)-O-O,x-O+(O+o+X+x)*(o+O),X*X-X*(x-O)-x+O,
O+X*(o*(o+O)+O),+x+O+X*o,x*(x-o),(o+X+x)*o*o-(x-O-O),O+(X-x)*(X+O),x-O}'
```

We leave it to you to determine what the program does. (If you are truly desperate to understand it, see Chris Johansen’s explanation, which is embedded in the Texinfo source file for this Web page.)

#### 11.3.12 Demonstrating Shortest and Longest Match Operators

In Shortest Match, or “Non-greedy” Regexp Operators, we described the POSIX 2024 shortest-match operators, and show the output of a program that demonstrated the differences. Here is the program, shortest-match.awk:

```
# shortest-match.awk --- Demonstrate shortest match operators

BEGIN {
    text[1] = "aaaxxxzzz";
        shortpat[1] = @/x+?/
        longpat[1] = @/x+/
    text[2] = "aaaxxxyzzz";
        shortpat[2] = @/x+?y/
        longpat[2] = @/x+y/
    text[3] = "aaaxxxxxxxxxxxxxxxxzzz";
        shortpat[3] = @/(x+?)(x+)(x+?)(x+)/
        longpat[3] = @/(x+)(x+)(x+)(x+)/
    text[4] = "aaaxyxxyxxyxzzz"
        shortpat[4] = @/((x+)(y+?)(x+))+/
        longpat[4] = @/((x+)(y+)(x+))+/
    text[5] = "aaaxyxxyxxyxzzz"
        shortpat[5] = @/((x+)(y+?)(x+)){2}/
        longpat[5] = @/((x+)(y+)(x+)){2}/

    count = length(text)
    for (i = 1; i <= count; i++) {
        show(text[i], shortpat[i], longpat[i])
    }
}

# show --- show the results of using shortest- and longest-match operators

function show(text, shortpat, longpat,
          s_offsets, l_offsets, i, n)   # locals
{
    printf("\"%s\"\n", text)

    match(text, shortpat, s_offsets)
    subresult = gensub(shortpat, "X", 1, text)
    printf("\tshortpat: /%s/, result: \"%s\"\n", shortpat, subresult)
    dump(text, s_offsets)

    match(text, longpat, l_offsets)
    subresult = gensub(longpat, "X", 1, text)
    printf("\tlongpat: /%s/, result: \"%s\"\n", longpat, subresult)
    dump(text, l_offsets)
}

# dump --- dump out the start and length of subpattern matches

function dump(text, offsets,    i, n, s, l)
{
    n = length(offsets)
    for (i = 0; i <= n; i++) {
        if ((i, "start") in offsets) {
            s = offsets[i, "start"]
            l = offsets[i, "length"]
            printf("\t\t%d: (s: %d, l: %d) -> \"%s\"\n", i,
                s, l, substr(text, s, l))
        }
    }
}
```

The program makes use of strongly typed regexp constants (see Strongly Typed Regexp Constants), the optional fourth argument to the `match()` function, and the `gensub()` and `substr()` functions (see String-Manipulation Functions).

### 11.4 Summary

- The programs provided in this chapter continue on the theme that reading programs is an excellent way to learn Good Programming.
- Using ‘#!’ to make `awk` programs directly runnable makes them easier to use. Otherwise, invoke the program using ‘awk -f …’.
- Reimplementing standard POSIX programs in `awk` is a pleasant exercise; `awk`’s expressive power lets you write such programs in relatively few lines of code, yet they are functionally complete and usable.
- One of standard `awk`’s weaknesses is working with individual characters. The ability to use `split()` with the empty string as the separator can considerably simplify such tasks.
- The examples here demonstrate the usefulness of the library functions from A Library of `awk` Functions for a number of real (if small) programs.
- Besides reinventing POSIX wheels, other programs solved a selection of interesting problems, such as finding duplicate words in text, printing mailing labels, and finding anagrams.

### 11.5 Exercises

1. Rewrite cut.awk (see Cutting Out Fields and Columns) using `split()` with `""` as the separator.
2. In Searching for Regular Expressions in Files, we mentioned that ‘egrep -i’ could be simulated in versions of `awk` without `IGNORECASE` by using `tolower()` on the line and the pattern. In a footnote there, we also mentioned that this solution has a bug: the translated line is output, and not the original one. Fix this problem.
3. POSIX versions of `grep` accept a -F option which causes `grep` to match fixed strings. Add support for this to egrep.awk.
4. Similarly, POSIX versions of `grep` allow you to provide multiple patterns to match, in either of two ways. You may provide a quoted string on the command line where the patterns are separated by newlines. Or you may use the -f option to provide a file containing the patterns, one per line. Implement both of these features.
5. The POSIX version of `id` takes options that control which information is printed. Modify the `awk` version (see Printing Out User Information) to accept the same arguments and perform in the same way.
6. The split.awk program (see Splitting a Large File into Pieces) assumes that letters are contiguous in the character set, which isn’t true for EBCDIC systems. Fix this problem. (Hint: Consider a different way to work through the alphabet, without relying on `ord()` and `chr()`.)
7. In uniq.awk (see Printing Nonduplicated Lines of Text, the logic for choosing which lines to print represents a *state machine*, which is “a device which can be in one of a set number of stable conditions depending on its previous condition and on the present values of its inputs.”85 Brian Kernighan suggests that “an alternative approach to state machines is to just read the input into an array, then use indexing. It’s almost always easier code, and for most inputs where you would use this, just as fast.” Rewrite the logic to follow this suggestion.
8. Why can’t the wc.awk program (see Counting Things) just use the value of `FNR` in `endfile()`? Hint: Examine the code in Noting Data file Boundaries.
9. Manipulation of individual characters in the `translate` program (see Transliterating Characters) is painful using standard `awk` functions. Given that `gawk` can split strings into individual characters using `""` as the separator, how might you use this feature to simplify the program?
10. The extract.awk program (see Extracting Programs from Texinfo Source Files) was written before `gawk` had the `gensub()` function. Use it to simplify the code.
11. Compare the performance of the awksed.awk program (see A Simple Stream Editor) with the more straightforward: BEGIN { pat = ARGV[1] repl = ARGV[2] ARGV[1] = ARGV[2] = "" } { gsub(pat, repl); print }
12. What are the advantages and disadvantages of awksed.awk versus the real `sed` utility?
13. In An Easy Way to Use Library Functions, we mentioned that not trying to save the line read with `getline` in the `pathto()` function when testing for the file’s accessibility for use with the main program simplifies things considerably. What problem does this engender though?
14. As an additional example of the idea that it is not always necessary to add new features to a program, consider the idea of having two files in a directory in the search path: default.awk This file contains a set of default library functions, such as `getopt()` and `assert()`. site.awk This file contains library functions that are specific to a site or installation; i.e., locally developed functions. Having a separate file allows default.awk to change with new `gawk` releases, without requiring the system administrator to update it each time by adding the local functions. One user suggested that `gawk` be modified to automatically read these files upon startup. Instead, it would be very simple to modify `igawk` to do this. Since `igawk` can process nested `@include` directives, default.awk could simply contain `@include` directives for the desired library functions. Make this change.
15. Modify anagram.awk (see Finding Anagrams from a Dictionary), to avoid the use of the external `sort` utility.

# Part III: Moving Beyond Standard `awk` with `gawk`
