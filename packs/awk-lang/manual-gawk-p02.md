---
title: "The GNU Awk User’s Guide (part 2/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 2/38
---

## 1 Getting Started with `awk`

The basic function of `awk` is to search files for lines (or other units of text) that contain certain patterns. When a line matches one of the patterns, `awk` performs specified actions on that line. `awk` continues to process input lines in this way until it reaches the end of the input files.

Programs in `awk` are different from programs in most other languages, because `awk` programs are *data driven* (i.e., you describe the data you want to work with and then what to do when you find it). Most other languages are *procedural*; you have to describe, in great detail, every step the program should take. When working with procedural languages, it is usually much harder to clearly describe the data your program will process. For this reason, `awk` programs are often refreshingly easy to read and write.

When you run `awk`, you specify an `awk` *program* that tells `awk` what to do. The program consists of a series of *rules* (it may also contain *function definitions*, an advanced feature that we will ignore for now; see User-Defined Functions). Each rule specifies one pattern to search for and one action to perform upon finding the pattern.

Syntactically, a rule consists of a *pattern* followed by an *action*. The action is enclosed in braces to separate it from the pattern. Newlines usually separate rules. Therefore, an `awk` program looks like this:

```
pattern { action }
pattern { action }
...
```

### 1.1 How to Run `awk` Programs

There are several ways to run an `awk` program. If the program is short, it is easiest to include it in the command that runs `awk`, like this:

```
awk 'program' input-file1 input-file2 ...
```

When the program is long, it is usually more convenient to put it in a file and run it with a command like this:

```
awk -f program-file input-file1 input-file2 ...
```

This section discusses both mechanisms, along with several variations of each.

#### 1.1.1 One-Shot Throwaway `awk` Programs

Once you are familiar with `awk`, you will often type in simple programs the moment you want to use them. Then you can write the program as the first argument of the `awk` command, like this:

```
awk 'program' input-file1 input-file2 ...
```

where *program* consists of a series of patterns and actions, as described earlier.

This command format instructs the *shell*, or command interpreter, to start `awk` and use the *program* to process records in the input file(s). There are single quotes around *program* so the shell won’t interpret any `awk` characters as special shell characters. The quotes also cause the shell to treat all of *program* as a single argument for `awk`, and allow *program* to be more than one line long.

This format is also useful for running short or medium-sized `awk` programs from shell scripts, because it avoids the need for a separate file for the `awk` program. A self-contained shell script is more reliable because there are no other files to misplace.

Later in this chapter, in Some Simple Examples, we’ll see examples of several short, self-contained programs.

#### 1.1.2 Running `awk` Without Input Files

You can also run `awk` without any input files. If you type the following command line:

```
awk 'program'
```

`awk` applies the *program* to the *standard input*, which usually means whatever you type on the keyboard. This continues until you indicate end-of-file by typing Ctrl-d. (On non-POSIX operating systems, the end-of-file character may be different.)

As an example, the following program prints a friendly piece of advice (from Douglas Adams’s *The Hitchhiker’s Guide to the Galaxy*), to keep you from worrying about the complexities of computer programming:

```
$ awk 'BEGIN { print "Don\47t Panic!" }'
-| Don't Panic!
```

`awk` executes statements associated with `BEGIN` before reading any input. If there are no other statements in your program, as is the case here, `awk` just stops, instead of trying to read input it doesn’t know how to process. The ‘\47’ is a magic way (explained later) of getting a single quote into the program, without having to engage in ugly shell quoting tricks.

> **NOTE:** If you use Bash as your shell, you should execute the command ‘set +H’ before running this program interactively, to disable the C shell-style command history, which treats ‘!’ as a special character. We recommend putting this command into your personal startup file.

This next simple `awk` program emulates the `cat` utility; it copies whatever you type on the keyboard to its standard output (why this works is explained shortly):

```
$ awk '{ print }'
Now is the time for all good men
-| Now is the time for all good men
to come to the aid of their country.
-| to come to the aid of their country.
Four score and seven years ago, ...
-| Four score and seven years ago, ...
What, me worry?
-| What, me worry?
Ctrl-d
```

#### 1.1.3 Running Long Programs

Sometimes `awk` programs are very long. In these cases, it is more convenient to put the program into a separate file. In order to tell `awk` to use that file for its program, you type:

```
awk -f source-file input-file1 input-file2 ...
```

The -f instructs the `awk` utility to get the `awk` program from the file *source-file* (see Command-Line Options). Any file name can be used for *source-file*. For example, you could put the program:

```
BEGIN { print "Don't Panic!" }
```

into the file advice. Then this command:

```
awk -f advice
```

does the same thing as this one:

```
awk 'BEGIN { print "Don\47t Panic!" }'
```

This was explained earlier (see Running `awk` Without Input Files). Note that you don’t usually need single quotes around the file name that you specify with -f, because most file names don’t contain any of the shell’s special characters. (If your file names have spaces in them, then you will need the single quotes.) Notice that in advice, the `awk` program did not have single quotes around it. The quotes are only needed for programs that are provided on the `awk` command line. (Also, placing the program in a file allows us to use a literal single quote in the program text, instead of the magic ‘\47’.)

If you want to clearly identify an `awk` program file as such, you can add the extension .awk to the file name. This doesn’t affect the execution of the `awk` program but it does make “housekeeping” easier.

#### 1.1.4 Executable `awk` Programs

Once you have learned `awk`, you may want to write self-contained `awk` scripts, using the ‘#!’ script mechanism. You can do this on many systems.8 For example, you could update the file advice to look like this:

```
#! /bin/awk -f

BEGIN { print "Don't Panic!" }
```

After making this file executable (with the `chmod` utility), simply type ‘advice’ at the shell and the system arranges to run `awk` as if you had typed ‘awk -f advice’:

```
$ chmod +x advice
$ ./advice
-| Don't Panic!
```

Self-contained `awk` scripts are useful when you want to write a program that users can invoke without their having to know that the program is written in `awk`.

| Understanding ‘#!’ |
|---|
| `awk` is an *interpreted* language. This means that the `awk` utility reads your program and then processes your data according to the instructions in your program. (This is different from a *compiled* language such as C, where your program is first compiled into machine code that is executed directly by your system’s processor.) The `awk` utility is thus termed an *interpreter*. Many modern languages are interpreted. The line beginning with ‘#!’ lists the full file name of an interpreter to run and a single optional initial command-line argument to pass to that interpreter. The operating system then runs the interpreter with the given argument and the full argument list of the executed program. The first argument in the list is the full file name of the `awk` program. The rest of the argument list contains either options to `awk`, or data files, or both. (Note that on many systems `awk` is found in /usr/bin instead of in /bin.) Some systems limit the length of the interpreter name to 32 characters. Often, this can be dealt with by using a symbolic link. You should not put more than one argument on the ‘#!’ line after the path to `awk`. It does not work. The operating system treats the rest of the line as a single argument and passes it to `awk`. Doing this leads to confusing behavior—most likely a usage diagnostic of some sort from `awk`. Finally, the value of `ARGV[0]` (see Predefined Variables) varies depending upon your operating system. Some systems put ‘awk’ there, some put the full pathname of `awk` (such as /bin/awk), and some put the name of your script (‘advice’). (d.c.) Don’t rely on the value of `ARGV[0]` to provide your script name. |

#### 1.1.6 Shell Quoting Issues

For short to medium-length `awk` programs, it is most convenient to enter the program on the `awk` command line. This is best done by enclosing the entire program in single quotes. This is true whether you are entering the program interactively at the shell prompt, or writing it as part of a larger shell script:

```
awk 'program text' input-file1 input-file2 ...
```

Once you are working with the shell, it is helpful to have a basic knowledge of shell quoting rules. The following rules apply only to POSIX-compliant, Bourne-style shells (such as Bash, the GNU Bourne-Again Shell). If you use the C shell, you’re on your own.

Before diving into the rules, we introduce a concept that appears throughout this Web page, which is that of the *null*, or empty, string.

The null string is character data that has no value. In other words, it is empty. It is written in `awk` programs like this: `""`. In the shell, it can be written using single or double quotes: `''` or `""`. Although the null string has no characters in it, it does exist. For example, consider this command:

```
$ echo ""
```

Here, the `echo` utility receives a single argument, even though that argument has no characters in it. In the rest of this Web page, we use the terms *null string* and *empty string* interchangeably. Now, on to the quoting rules:

- Quoted items can be concatenated with nonquoted items as well as with other quoted items. The shell turns everything into one argument for the command.
- Preceding any single character with a backslash (‘\’) quotes that character. The shell removes the backslash and passes the quoted character on to the command.
- Single quotes protect everything between the opening and closing quotes. The shell does no interpretation of the quoted text, passing it on verbatim to the command. It is *impossible* to embed a single quote inside single-quoted text. Refer back to Comments in `awk` Programs for an example of what happens if you try.
- Double quotes protect most things between the opening and closing quotes. The shell does at least variable and command substitution on the quoted text. Different shells may do additional kinds of processing on double-quoted text. Because certain characters within double-quoted text are processed by the shell, they must be *escaped* within the text. Of note are the characters ‘$’, ‘`’, ‘\’, and ‘"’, all of which must be preceded by a backslash within double-quoted text if they are to be passed on literally to the program. (The shell strips the leading backslash first.) Thus, the example seen previously in Running `awk` Without Input Files: awk 'BEGIN { print "Don\47t Panic!" }' could instead be written this way: $ awk "BEGIN { print \"Don't Panic!\" }" -| Don't Panic! Note that the single quote is not special within double quotes.
- Null strings are removed when they occur as part of a non-null command-line argument, while explicit null objects are kept. For example, to specify that the field separator `FS` should be set to the null string, use: awk -F "" '*program*' *files* # correct Don’t use this: awk -F"" '*program*' *files* # wrong! In the second case, `awk` attempts to use the text of the program as the value of `FS`, and the first file name as the text of the program! This results in syntax errors at best, and confusing behavior at worst.

Mixing single and double quotes is difficult. You have to resort to shell quoting tricks, like this:

```
$ awk 'BEGIN { print "Here is a single quote <'"'"'>" }'
-| Here is a single quote <'>
```

This program consists of three concatenated quoted strings. The first and the third are single-quoted, and the second is double-quoted.

This can be “simplified” to:

```
$ awk 'BEGIN { print "Here is a single quote <'\''>" }'
-| Here is a single quote <'>
```

Judge for yourself which of these two is the more readable.

Another option is to use double quotes, escaping the embedded, `awk`-level double quotes:

```
$ awk "BEGIN { print \"Here is a single quote <'>\" }"
-| Here is a single quote <'>
```

This option is also painful, because double quotes, backslashes, and dollar signs are very common in more advanced `awk` programs.

A third option is to use the octal escape sequence equivalents (see Escape Sequences) for the single- and double-quote characters, like so:

```
$ awk 'BEGIN { print "Here is a single quote <\47>" }'
-| Here is a single quote <'>
$ awk 'BEGIN { print "Here is a double quote <\42>" }'
-| Here is a double quote <">
```

This works nicely, but you should comment clearly what the escape sequences mean.

A fourth option is to use command-line variable assignment, like this:

```
$ awk -v sq="'" 'BEGIN { print "Here is a single quote <" sq ">" }'
-| Here is a single quote <'>
```

(Here, the two string constants and the value of `sq` are concatenated into a single string that is printed by `print`.)

If you really need both single and double quotes in your `awk` program, it is probably best to move it into a separate file, where the shell won’t be part of the picture and you can say what you mean.

#### 1.1.6.1 Quoting in MS-Windows Batch Files

Although this Web page generally only worries about POSIX systems and the POSIX shell, the following issue arises often enough for many users that it is worth addressing.

The “shells” on Microsoft Windows systems use the double-quote character for quoting, and make it difficult or impossible to include an escaped double quote character in a command-line script. The following example, courtesy of Jeroen Brink, shows how to escape the double quotes from this one liner script that prints all lines in a file surrounded by double quotes:

```
{ print "\"" $0 "\"" }
```

In an MS-Windows command-line the one-liner script above may be passed as follows:

```
gawk "{ print \"\042\" $0 \"\042\" }" file
```

In this example the ‘\042’ is the octal code for a double quote; `gawk` converts it into a real double-quote for output by the `print` statement.

In MS-Windows escaping double quotes is a little tricky because you use backslashes to escape double quotes, but backslashes themselves are not escaped in the usual way; indeed they are either duplicated or not, depending upon whether there is a subsequent double quote. The MS-Windows rule for double-quoting a string is the following:

1. For each double quote in the original string, let *N* be the number of backslash(es) before it, *N* might be zero. Replace these *N* backslash(es) by *2**N*+1* backslash(es)
2. Let *N* be the number of backslash(es) tailing the original string, *N* might be zero. Replace these *N* backslash(es) by *2**N** backslash(es)
3. Surround the resulting string by double quotes.

So to double-quote the one-liner script ‘{ print "\"" $0 "\"" }’ from the previous example you would do it this way:

```
gawk "{ print \"\\\"\" $0 \"\\\"\" }" file
```

However, the use of ‘\042’ instead of ‘\\\"’ is also possible and easier to read, because backslashes that are not followed by a double quote don’t need duplication.

### 1.2 Data files for the Examples

Many of the examples in this Web page take their input from two sample data files. The first, mail-list, represents a list of peoples’ names together with their email addresses and information about those people. The second data file, called inventory-shipped, contains information about monthly shipments. In both files, each line is considered to be one *record*.

In mail-list, each record contains the name of a person, his/her phone number, his/her email address, and a code for his/her relationship with the author of the list. The columns are aligned using spaces. An ‘A’ in the last column means that the person is an acquaintance. An ‘F’ in the last column means that the person is a friend. An ‘R’ means that the person is a relative:

```
Amelia       555-5553     amelia.zodiacusque@gmail.com    F
Anthony      555-3412     anthony.asserturo@hotmail.com   A
Becky        555-7685     becky.algebrarum@gmail.com      A
Bill         555-1675     bill.drowning@hotmail.com       A
Broderick    555-0542     broderick.aliquotiens@yahoo.com R
Camilla      555-2912     camilla.infusarum@skynet.be     R
Fabius       555-1234     fabius.undevicesimus@ucb.edu    F
Julie        555-6699     julie.perscrutabor@skeeve.com   F
Martin       555-6480     martin.codicibus@hotmail.com    A
Samuel       555-3430     samuel.lanceolis@shu.edu        A
Jean-Paul    555-2127     jeanpaul.campanorum@nyu.edu     R
```

The data file inventory-shipped represents information about shipments during the year. Each record contains the month, the number of green crates shipped, the number of red boxes shipped, the number of orange bags shipped, and the number of blue packages shipped, respectively. There are 16 entries, covering the 12 months of last year and the first four months of the current year. An empty line separates the data for the two years:

```
Jan  13  25  15 115
Feb  15  32  24 226
Mar  15  24  34 228
Apr  31  52  63 420
May  16  34  29 208
Jun  31  42  75 492
Jul  24  34  67 436
Aug  15  34  47 316
Sep  13  55  37 277
Oct  29  54  68 525
Nov  20  87  82 577
Dec  17  35  61 401

Jan  21  36  64 620
Feb  26  58  80 652
Mar  24  75  70 495
Apr  21  70  74 514
```

The sample files are included in the `gawk` distribution, in the directory awklib/eg/data.

### 1.3 Some Simple Examples

The following command runs a simple `awk` program that searches the input file mail-list for the character string ‘li’ (a grouping of characters is usually called a *string*; the term *string* is based on similar usage in English, such as “a string of pearls” or “a string of cars in a train”):

```
awk '/li/ { print $0 }' mail-list
```

When lines containing ‘li’ are found, they are printed because ‘print $0’ means print the current line. (Just ‘print’ by itself means the same thing, so we could have written that instead.)

You will notice that slashes (‘/’) surround the string ‘li’ in the `awk` program. The slashes indicate that ‘li’ is the pattern to search for. This type of pattern is called a *regular expression*, which is covered in more detail later (see Regular Expressions). The pattern is allowed to match parts of words. There are single quotes around the `awk` program so that the shell won’t interpret any of it as special shell characters.

Here is what this program prints:

```
$ awk '/li/ { print $0 }' mail-list
-| Amelia       555-5553     amelia.zodiacusque@gmail.com    F
-| Broderick    555-0542     broderick.aliquotiens@yahoo.com R
-| Julie        555-6699     julie.perscrutabor@skeeve.com   F
-| Samuel       555-3430     samuel.lanceolis@shu.edu        A
```

In an `awk` rule, either the pattern or the action can be omitted, but not both. If the pattern is omitted, then the action is performed for *every* input line. If the action is omitted, the default action is to print all lines that match the pattern.

Thus, we could leave out the action (the `print` statement and the braces) in the previous example and the result would be the same: `awk` prints all lines matching the pattern ‘li’. By comparison, omitting the `print` statement but retaining the braces makes an empty action that does nothing (i.e., no lines are printed).

Many practical `awk` programs are just a line or two long. Following is a collection of useful, short programs to get you started. Some of these programs contain constructs that haven’t been covered yet. (The description of the program will give you a good idea of what is going on, but you’ll need to read the rest of the Web page to become an `awk` expert!) Most of the examples use a data file named data. This is just a placeholder; if you use these programs yourself, substitute your own file names for data.

Some of the following examples use the output of ‘ls -l’ as input. `ls` is a system command that gives you a listing of the files in a directory. With the -l option, this listing includes each file’s size and the date the file was last modified. Its output looks like this:

```
-rw-r--r--  1 arnold   user   1933 Nov  7 13:05 Makefile
-rw-r--r--  1 arnold   user  10809 Nov  7 13:03 awk.h
-rw-r--r--  1 arnold   user    983 Apr 13 12:14 awk.tab.h
-rw-r--r--  1 arnold   user  31869 Jun 15 12:20 awkgram.y
-rw-r--r--  1 arnold   user  22414 Nov  7 13:03 awk1.c
-rw-r--r--  1 arnold   user  37455 Nov  7 13:03 awk2.c
-rw-r--r--  1 arnold   user  27511 Dec  9 13:07 awk3.c
-rw-r--r--  1 arnold   user   7989 Nov  7 13:03 awk4.c
```

The first field contains read-write permissions, the second field contains the number of links to the file, and the third field identifies the file’s owner. The fourth field identifies the file’s group. The fifth field contains the file’s size in bytes. The sixth, seventh, and eighth fields contain the month, day, and time, respectively, that the file was last modified. Finally, the ninth field contains the file name.

For future reference, note that there is often more than one way to do things in `awk`. At some point, you may want to look back at these examples and see if you can come up with different ways to do the same things shown here:

- Print every line that is longer than 80 characters: awk 'length($0) > 80' data The sole rule has a relational expression as its pattern and has no action—so it uses the default action, printing the record.
- Print the length of the longest input line: awk '{ if (length($0) > max) max = length($0) } END { print max }' data The code associated with `END` executes after all input has been read; it’s the other side of the coin to `BEGIN`.
- Print the length of the longest line in data: expand data | awk '{ if (x < length($0)) x = length($0) } END { print "maximum line length is " x }' This example differs slightly from the previous one: the input is processed by the `expand` utility to change TABs into spaces, so the widths compared are actually the right-margin columns, as opposed to the number of input characters on each line.
- Print every line that has at least one field: awk 'NF > 0' data This is an easy way to delete blank lines from a file (or rather, to create a new file similar to the old file but from which the blank lines have been removed).
- Print seven random numbers from 0 to 100, inclusive: awk 'BEGIN { for (i = 1; i <= 7; i++) print int(101 * rand()) }'
- Print the total number of bytes used by *files*: ls -l *files* | awk '{ x += $5 } END { print "total bytes: " x }'
- Print the total number of kilobytes used by *files*: ls -l *files* | awk '{ x += $5 } END { print "total K-bytes:", x / 1024 }'
- Print a sorted list of the login names of all users: awk -F: '{ print $1 }' /etc/passwd | sort
- Count the lines in a file: awk 'END { print NR }' data
- Print the even-numbered lines in the data file: awk 'NR % 2 == 0' data If you used the expression ‘NR % 2 == 1’ instead, the program would print the odd-numbered lines.

### 1.4 An Example with Two Rules

The `awk` utility reads the input files one line at a time. For each line, `awk` tries the patterns of each rule. If several patterns match, then several actions execute in the order in which they appear in the `awk` program. If no patterns match, then no actions run.

After processing all the rules that match the line (and perhaps there are none), `awk` reads the next line. (However, see The `next` Statement and also see The `nextfile` Statement.) This continues until the program reaches the end of the file. For example, the following `awk` program contains two rules:

```
/12/  { print $0 }
/21/  { print $0 }
```

The first rule has the string ‘12’ as the pattern and ‘print $0’ as the action. The second rule has the string ‘21’ as the pattern and also has ‘print $0’ as the action. Each rule’s action is enclosed in its own pair of braces.

This program prints every line that contains the string ‘12’ *or* the string ‘21’. If a line contains both strings, it is printed twice, once by each rule.

This is what happens if we run this program on our two sample data files, mail-list and inventory-shipped:

```
$ awk '/12/ { print $0 }
>      /21/ { print $0 }' mail-list inventory-shipped
-| Anthony      555-3412     anthony.asserturo@hotmail.com   A
-| Camilla      555-2912     camilla.infusarum@skynet.be     R
-| Fabius       555-1234     fabius.undevicesimus@ucb.edu    F
-| Jean-Paul    555-2127     jeanpaul.campanorum@nyu.edu     R
-| Jean-Paul    555-2127     jeanpaul.campanorum@nyu.edu     R
-| Jan  21  36  64 620
-| Apr  21  70  74 514
```

Note how the line beginning with ‘Jean-Paul’ in mail-list was printed twice, once for each rule.

### 1.5 A More Complex Example

Now that we’ve mastered some simple tasks, let’s look at what typical `awk` programs do. This example shows how `awk` can be used to summarize, select, and rearrange the output of another utility. It uses features that haven’t been covered yet, so don’t worry if you don’t understand all the details:

```
ls -l | awk '$6 == "Nov" { sum += $5 }
             END { print sum }'
```

This command prints the total number of bytes in all the files in the current directory that were last modified in November (of any year).

As a reminder, the output of ‘ls -l’ gives you a listing of the files in a directory, including each file’s size and the date the file was last modified. The first field contains read-write permissions, the second field contains the number of links to the file, and the third field identifies the file’s owner. The fourth field identifies the file’s group. The fifth field contains the file’s size in bytes. The sixth, seventh, and eighth fields contain the month, day, and time, respectively, that the file was last modified. Finally, the ninth field contains the file name.

The ‘$6 == "Nov"’ in our `awk` program is an expression that tests whether the sixth field of the output from ‘ls -l’ matches the string ‘Nov’. Each time a line has the string ‘Nov’ for its sixth field, `awk` performs the action ‘sum += $5’. This adds the fifth field (the file’s size) to the variable `sum`. As a result, when `awk` has finished reading all the input lines, `sum` is the total of the sizes of the files whose lines matched the pattern. (This works because `awk` variables are automatically initialized to zero.)

After the last line of output from `ls` has been processed, the `END` rule executes and prints the value of `sum`. In this example, the value of `sum` is 80600.

These more advanced `awk` techniques are covered in later sections (see Actions). Before you can move on to more advanced `awk` programming, you have to know how `awk` interprets your input and displays your output. By manipulating fields and using `print` statements, you can produce some very useful and impressive-looking reports.

### 1.6 `awk` Statements Versus Lines

Most often, each line in an `awk` program is a separate statement or separate rule, like this:

```
awk '/12/  { print $0 }
     /21/  { print $0 }' mail-list inventory-shipped
```

However, `gawk` ignores newlines after any of the following symbols and keywords:

```
,    {    ?    :    ||    &&    do    else
```

A newline at any other point is considered the end of the statement.9

If you would like to split a single statement into two lines at a point where a newline would terminate it, you can *continue* it by ending the first line with a backslash character (‘\’). The backslash must be the final character on the line in order to be recognized as a continuation character. A backslash followed by a newline is allowed anywhere in the statement, even in the middle of a string or regular expression. For example:

```
awk '/This regular expression is too long, so continue it\
 on the next line/ { print $1 }'
```

We have generally not used backslash continuation in our sample programs. `gawk` places no limit on the length of a line, so backslash continuation is never strictly necessary; it just makes programs more readable. For this same reason, as well as for clarity, we have kept most statements short in the programs presented throughout the Web page.

Backslash continuation is most useful when your `awk` program is in a separate source file instead of entered from the command line. You should also note that many `awk` implementations are more particular about where you may use backslash continuation. For example, they may not allow you to split a string constant using backslash continuation. Thus, for maximum portability of your `awk` programs, it is best not to split your lines in the middle of a regular expression or a string.

> **CAUTION:** *Backslash continuation does not work as described with the C shell.* It works for `awk` programs in files and for one-shot programs, *provided* you are using a POSIX-compliant shell, such as the Unix Bourne shell or Bash. But the C shell behaves differently! There you must use two backslashes in a row, followed by a newline. Note also that when using the C shell, *every* newline in your `awk` program must be escaped with a backslash. To illustrate:
> 
> ```
> % awk 'BEGIN { \
> ?   print \\
> ?       "hello, world" \
> ? }'
> -| hello, world
> ```
> 
> Here, the ‘%’ and ‘?’ are the C shell’s primary and secondary prompts, analogous to the standard shell’s ‘$’ and ‘>’.
> 
> Compare the previous example to how it is done with a POSIX-compliant shell:
> 
> ```
> $ awk 'BEGIN {
> >   print \
> >       "hello, world"
> > }'
> -| hello, world
> ```

`awk` is a line-oriented language. Each rule’s action has to begin on the same line as the pattern. To have the pattern and action on separate lines, you *must* use backslash continuation; there is no other option.

Another thing to keep in mind is that backslash continuation and comments do not mix. As soon as `awk` sees the ‘#’ that starts a comment, it ignores *everything* on the rest of the line. For example:

```
$ gawk 'BEGIN { print "don\47t panic" # a friendly \
>                                    BEGIN rule
> }'
error→ gawk: cmd. line:2:                BEGIN rule
error→ gawk: cmd. line:2:                ^ syntax error
```

In this case, it looks like the backslash would continue the comment onto the next line. However, the backslash-newline combination is never even noticed because it is “hidden” inside the comment. Thus, the `BEGIN` is noted as a syntax error.

Backslash continuation comes into play in an additional, unexpected situation. Consider:

```
gawk -F'\
a' '...'
```

This command line assigns a value to `FS`. But what value? There are several possibilities, and in fact different versions of `awk` do different things. `gawk` treats this as if it were written:

```
BEGIN { FS = "\
a"
}
...
```

In short, the backslash and newline are removed, assigning `"a"` to `FS`. This same treatment applies to variable assignments made with the -v option (see Command-Line Options) and to regular command-line variable assignments (see Assigning Variables on the Command Line).

If you’re interested, see https://lists.gnu.org/archive/html/bug-gawk/2022-10/msg00025.html for a source code patch that allows lines to be continued when inside parentheses. This patch was not added to `gawk` since it would quietly decrease the portability of `awk` programs.

When `awk` statements within one rule are short, you might want to put more than one of them on a line. This is accomplished by separating the statements with a semicolon (‘;’). This also applies to the rules themselves. Thus, the program shown at the start of this section could also be written this way:

```
/12/ { print $0 } ; /21/ { print $0 }
```

> **NOTE:** The requirement that states that rules on the same line must be separated with a semicolon was not in the original `awk` language; it was added for consistency with the treatment of statements within an action.

### 1.7 Other Features of `awk`

The `awk` language provides a number of predefined, or *built-in*, variables that your programs can use to get information from `awk`. There are other variables your program can set as well to control how `awk` processes your data.

In addition, `awk` provides a number of built-in functions for doing common computational and string-related operations. `gawk` provides built-in functions for working with timestamps, performing bit manipulation, for runtime string translation (internationalization), determining the type of a variable, and array sorting.

As we develop our presentation of the `awk` language, we will introduce most of the variables and many of the functions. They are described systematically in Predefined Variables and in Built-in Functions.

### 1.8 When to Use `awk`

Now that you’ve seen some of what `awk` can do, you might wonder how `awk` could be useful for you. By using utility programs, advanced patterns, field separators, arithmetic statements, and other selection criteria, you can produce much more complex output. The `awk` language is very useful for producing reports from large amounts of raw data, such as summarizing information from the output of other utility programs like `ls`. (See A More Complex Example.)

Programs written with `awk` are usually much smaller than they would be in other languages. This makes `awk` programs easy to compose and use. Often, `awk` programs can be quickly composed at your keyboard, used once, and thrown away. Because `awk` programs are interpreted, you can avoid the (usually lengthy) compilation part of the typical edit-compile-test-debug cycle of software development.

Complex programs have been written in `awk`, including a complete retargetable assembler for eight-bit microprocessors (see Glossary, for more information), and a microcode assembler for a special-purpose Prolog computer. The original `awk`’s capabilities were strained by tasks of such complexity, but modern versions are more capable.

If you find yourself writing `awk` scripts of more than, say, a few hundred lines, you might consider using a different programming language. The shell is good at string and pattern matching; in addition, it allows powerful use of the system utilities. Python offers a nice balance between high-level ease of programming and access to system facilities.10

### 1.9 Summary

- Programs in `awk` consist of *pattern*–*action* pairs.
- An *action* without a *pattern* always runs. The default *action* for a pattern without one is ‘{ print $0 }’.
- Use either ‘awk '*program*' *files*’ or ‘awk -f *program-file* *files*’ to run `awk`.
- You may use the special ‘#!’ header line to create `awk` programs that are directly executable.
- Comments in `awk` programs start with ‘#’ and continue to the end of the same line.
- Be aware of quoting issues when writing `awk` programs as part of a larger shell script (or MS-Windows batch file).
- You may use backslash continuation to continue a source line. Lines are automatically continued after a comma, open brace, question mark, colon, ‘||’, ‘&&’, `do`, and `else`.
