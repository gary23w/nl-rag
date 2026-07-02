---
title: "Command-line argument parsing"
source: https://en.wikipedia.org/wiki/Command-line_argument_parsing
domain: cobra-cli-go
license: CC-BY-SA-4.0
tags: cobra cli, go command line, cobra subcommands, cobra command tree
fetched: 2026-07-02
---

# Command-line argument parsing

**Command-line argument parsing** refers to methods used in a programming language to parse command-line arguments.

## Command-line options

A command-line option or simply option (also known as a flag or switch) modifies the operation of a command; the effect is determined by the command's program. Options follow the command name on the command line, separated by, e.g., commas, spaces. Separators are not always required, such as `Dir/?` and `DIR /?` in DOS, which have the same effect of listing the DIR command's available options, whereas `dir --help` (in many versions of Unix) *does* require the option to be preceded by at least one space (and is case-sensitive).

The format of options varies widely between operating systems. In most cases, the syntax is by convention rather than an operating system requirement; the entire command line is simply a string passed to a program, which can process it in any way the programmer wants, so long as the interpreter can tell where the command name ends and its arguments and options begin.

A few representative samples of command-line options, most relating to listing files in a directory, to illustrate some conventions:

| Operating system | Command | Valid alternative | Notes |
|---|---|---|---|
| OpenVMS | `directory/owner` | `Dir /Owner` | instruct the *directory* command to also display the ownership of the files. *Note the Directory command name is not case sensitive, and can be abbreviated to as few letters as required to remain unique.* |
| Windows | `DIR/Q/O:S d*` | `dir /q d* /o:s` | display ownership of files whose names begin with d (or D), sorted by size, smallest first. *Note spaces around argument d* are required.* |
| Unix-like systems | `ls -lS D*` | `ls -S -l D*` | display in long format files and directories whose names begin with D (but not d), sorted by size (largest first). *Note spaces are required around all arguments and options, but some can be run together, e.g. -lS is the same as -l -S.* |
| Data General RDOS CLI | `list/e/s 04-26-80/b` | `List /S/E 4-26-80/B` | list every attribute for files created before 26 April 1980. *Note the /B at the end of the date argument is a local switch, that modifies the meaning of that argument, while /S and /E are global switches, i.e. apply to the whole command.* |
| VM/CMS CLI | `LISTFILE (FULLDATE)` | `l(ful` | includes the date the file was last written in the list. *Note the LISTFILE command name is not case sensitive, and can be abbreviated to as few letters as required to remain unique.* |
| OS/360 operator commands | `START TAPERDR,DSNAME=FOO.BAR` | `S TAPERDR,DSN=FOO.BAR` | Start the procedure named TAPERDR with the supplied data set name |
| TSO | `LISTCAT LEVEL(FOO) MEMBERS` | `LISTC L(FOO) M` | List datasets at specified index level and list members for each PDS. |
| `SEND 'text' USER(FOO)` | `SE 'text' U(FOO)` | Send message to specified user |   |

Command-line argument parsing is used to parse the arguments of a program, and such functionality is offered in various languages. For example, getopt() is in the C POSIX library for parsing arguments.

## Parsing methods

Many languages offer functionality for argument parsing. For example, the C POSIX library provides getopt(), Python offers a module called `argparse`, while C# provides a namespace `System.CommandLine`. In others, they are not bundled in the standard library, but rather must be used through third-party libraries.

In many languages, particularly C-derived languages, arguments are accessed through the parameters of the `main()` method. For example, in C and C++, the `main` method has signature `int main(int argc, char* argv[]);`, where `argc` is the number of arguments plus the name of the program, and `argv` is an array of C-strings where `argv[0]` is the name of the program. In Java and C#, the `main()` method instead takes one parameter `args` of type `String[]` (an array of strings). Meanwhile, in some other languages, such as Rust, command-line arguments are accessed by a method `std::env::args()`, allowing a global point of access rather than having to be obtained from `main()`.

## In different programming languages

### AWK

AWK uses `ARGV` also.

```mw
BEGIN {
   for ( i = 0; i < ARGC; i++ )
   {
       print ARGV[i]
   }
}
```

### C

C uses `argv` to process command-line arguments.

An example of C argument parsing would be:

```mw
#include <stdio.h>

int main(int argc, char* argv[]) {
    for (int i = 0; i < argc; ++i) {
        printf("%s\n", argv[count]);
    }
}
```

C POSIX library also has functions called `getopt()` and `getopt_long()`.

### C++

C++ accesses arguments the same way as C.

```mw
import std;

using std::string;
using std::vector;

int main(int argc, char* argv[]) {
    vector<string> args(argv, argv + argc);
    for (const string& s: args) {
        std::println("{}", s);
    }
}
```

The POCO C++ Libraries offer a class `Poco::Util::OptionProcessor` for parsing command-line arguments. Boost provides a class `boost::program_options::command_line_parser`. Meanwhile, Google has a library called `gflags`. There is also a `argparse` library for C++17+ offers a similar API for argument parsing to Python `argparse`.

### C

An example of C# argument parsing would be:

```mw
class ReadArgs
{
    static void Main(string[] args)
    {
        foreach (string arg in args)
        {
            Console.WriteLine(arg);
        }
    }
}
```

C# provides the `System.CommandLine` namespace for advanced command-line argument parsing.

### D

The D programming language provides a module `std.getopt`.

### Go

Go provides the `flag` package for argument parsing.

### Haskell

Haskell provides the library `System.Console.GetOpt`.

### Java

An example of Java argument parsing would be:

```mw
public class ReadArgs {
    public static void main(String[] args) {
        for (String s: args) {
            System.out.println(s);
        }
    }
}
```

The Apache Commons library `org.apache.commons.cli` provides command-line argument parsing capabilities. There is also the `gnu.getopt` library, ported from GNU getopt.

### Kotlin

Here are some possible ways to print arguments in Kotlin:

```mw
fun main(args: Array<String>) = println(args.joinToString())
```

```mw
fun main(args: Array<String>) = println(args.contentToString())
```

```mw
fun main(args: Array<String>) {
    for (arg in args) {
        println(arg)
    }
}
```

### Perl

Perl uses `@ARGV`.

```mw
foreach $arg (@ARGV)
{
    print $arg;
}
```

or

```mw
foreach $argnum (0 .. $#ARGV)
{
    print $ARGV[$argnum];
}
```

There is also `Getopt::Long` and `Getopt::Std` for argument parsing.

### PHP

PHP uses `argc` as a count of arguments and `argv` as an array containing the values of the arguments. To create an array from command-line arguments in the `-foo:bar` format, the following might be used:

```mw
$args = parseArgs($argv);
echo getArg($args, "foo");

function parseArgs(array $args): array {
    foreach ($args as $arg) {
        $tmp = explode(":", $arg, 2);
        if ($arg[0] === "-") {
            $args[substr($tmp[0], 1)] = $tmp[1];
        }
    }
    return $args;
}

function getArg(array $args, string $arg): string | bool {
    if (isset($args[$arg])) {
        return $args[$arg];
    }
    return false;
}
```

PHP can also use `getopt()`.

### Python

Python uses `sys.argv`, e.g.:

```mw
import sys

if __name__ == "__main__":
    for arg in sys.argv:
        print(arg)
```

Python also has a module called `argparse` in the standard library for parsing command-line arguments.

### Racket

Racket uses a `current-command-line-arguments` parameter, and provides a `racket/cmdline` library for parsing these arguments. Example:

```mw
#lang racket

(require racket/cmdline)

(define smile? (make-parameter #t))
(define nose?  (make-parameter #false))
(define eyes   (make-parameter ":"))

(command-line #:program "emoticon"

              #:once-any; the following two are mutually exclusive
              [("-s" "--smile") "smile mode" (smile? #true)]
              [("-f" "--frown") "frown mode" (smile? #false)]

              #:once-each
              [("-n" "--nose") "add a nose"  (nose? #true)]
              [("-e" "--eyes") char "use <char> for the eyes" (eyes char)])

(printf "~a~a~a\n"
        (eyes)
        (if (nose?) "-" "")
        (if (smile?) ")" "("))
```

The library parses long and short flags, handles arguments, allows combining short flags, and handles `-h` and `--help` automatically:

```mw
$ racket /tmp/c -nfe 8
8-(
```

### Rexx

Rexx uses `arg`, e.g.:

```mw
do i=1 to words(arg(1))
	say word(arg(1), i)
end
```

### Rust

Rather than being part of the parameters of `main()` (like other C-style languages), in Rust the args are in `std::env::args()`, which returns a `std::env::Args` and is converted to a `Vec<String>` with `.collect()`.

```mw
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query: &String = &args[1];
    let file_path: &String = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

A popular Rust library for command-line argument parsing is `clap`.

### JavaScript

#### Node.js

JavaScript programs written for Node.js use the `process.argv` global variable.

```mw
// argv.js
console.log(process.argv);
```

```mw
$ node argv.js one two three four five
[ 'node',
  '/home/avian/argvdemo/argv.js',
  'one',
  'two',
  'three',
  'four',
  'five' ]
```

Node.js programs are invoked by running the interpreter node interpreter with a given file, so the first two arguments will be `node` and the name of the JavaScript source file. It is often useful to extract the rest of the arguments by slicing a sub-array from `process.argv`.

```mw
// process-args.js
console.log(process.argv.slice(2));
```

```mw
$ node process-args.js one two=three four
[ 
  'one',
  'two=three',
  'four' ]
```

#### Bun

JavaScript written for Bun use `Bun.argv` and the `util.parseArgs` function.

```mw
console.log(Bun.argv);
```

#### Deno

JavaScript written for Deno use `Deno.args` and the `parseArgs` function.

```mw
console.log(Deno.args);
```
